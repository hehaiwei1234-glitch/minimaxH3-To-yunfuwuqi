#!/usr/bin/env python3
"""H3 片段体检脚本：对每个 mp4 输出 时长 / 语音识别文字 / 开口与结束时间 / 切镜时间。
用法:  python3 clip_report.py <asr模型目录> <mp4> [<mp4> ...]
依赖:  ffmpeg, numpy, sherpa-onnx (pip install sherpa-onnx numpy)
模型:  sherpa-onnx-streaming-paraformer-bilingual-zh-en (encoder.int8.onnx / decoder.int8.onnx / tokens.txt)
说明:
 - 开口/结束 = 150–3800 Hz 频带能量超过全片最大值 12% 的首/末 0.125 秒窗口。
 - 语音识别用“逐步截断前缀”的方法，文字第一次出现的时间≈开口时间的交叉验证。
 - 识别会丢掉句尾轻音（的/子/下），所以“少一个字”不等于“没说”。
 - 切镜检测 = 降采样后相邻帧平均差突增（阈值 18），只适合硬切。
"""
import sys, subprocess, json
import numpy as np
import sherpa_onnx

def load_audio(path, band=False):
    cmd = ['ffmpeg','-v','error','-i',path,'-vn','-ac','1','-ar','16000']
    if band: cmd += ['-af','highpass=f=150,lowpass=f=3800']
    cmd += ['-f','f32le','-']
    return np.frombuffer(subprocess.check_output(cmd), dtype=np.float32)

def make_rec(d):
    return sherpa_onnx.OnlineRecognizer.from_paraformer(
        tokens=d+'/tokens.txt', encoder=d+'/encoder.int8.onnx', decoder=d+'/decoder.int8.onnx',
        num_threads=4, sample_rate=16000, feature_dim=80)

def tx(rec, a):
    s = rec.create_stream()
    s.accept_waveform(16000, a); s.accept_waveform(16000, np.zeros(12000, dtype=np.float32)); s.input_finished()
    while rec.is_ready(s): rec.decode_stream(s)
    r = rec.get_result(s); return r if isinstance(r, str) else r.text

def envelope(path, thr=0.12, win=0.125):
    b = load_audio(path, band=True); h = int(16000*win); k = len(b)//h
    if k == 0: return None
    e = np.sqrt((b[:k*h].reshape(k, h)**2).mean(1)); m = e.max()
    if m == 0: return None
    on = np.where(e > thr*m)[0]
    return (on[0]*win, (on[-1]+1)*win, ''.join(str(int(9*x/m)) for x in e))

def cuts(path, size=32, thr=18.0):
    w = h = size
    raw = subprocess.check_output(['ffmpeg','-v','error','-i',path,'-an','-vf',f'scale={w}:{h},format=gray','-f','rawvideo','-'])
    fr = np.frombuffer(raw, dtype=np.uint8).reshape(-1, h, w).astype(np.float32)
    d = np.abs(np.diff(fr, axis=0)).mean(axis=(1,2))
    fps = 24.0
    return [round(float((i+1)/fps), 2) for i in np.where(d > thr)[0]]

def duration(path):
    out = subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',path])
    return float(out.decode().strip())

def sidebars(path, strip=60, thr=30):
    """两侧黑边检查（第 6 集 6A-05、6A-07 出现过）：左右各取 strip 像素宽的竖条，
    每 0.5 秒抽一帧，整段里最亮像素都低于 thr 就算黑边。返回 (左是否黑, 右是否黑)。"""
    info = subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','csv=p=0',path]).decode().strip().split(',')
    w, h = int(info[0]), int(info[1])
    res = []
    for x in (0, w - strip):
        raw = subprocess.check_output(['ffmpeg','-v','error','-i',path,'-an','-vf',f'fps=2,crop={strip}:{h}:{x}:0,format=gray','-f','rawvideo','-'])
        fr = np.frombuffer(raw, dtype=np.uint8)
        res.append(bool(len(fr) and fr.max() < thr))
    return tuple(res)

if __name__ == '__main__':
    d = sys.argv[1]; rec = make_rec(d)
    for p in sys.argv[2:]:
        a = load_audio(p); dur = len(a)/16000
        ev = []; last = ''; t = 0.5
        while t < dur + 0.01:
            r = tx(rec, a[:int(t*16000)])
            if r != last: ev.append((round(t, 2), r)); last = r
            t += 0.25
        env = envelope(p)
        print('==', p)
        print(f'  视频时长 {duration(p):.3f}s  音频 {dur:.3f}s')
        print('  识别: 首次出现', ev[0] if ev else None, '| 最终', ev[-1][1] if ev else '(空)')
        if env: print(f'  能量: 开口 {env[0]:.2f}s  结束 {env[1]:.2f}s\n  包络: {env[2]}')
        print('  切镜时间(秒):', cuts(p))
        sb = sidebars(p)
        if sb[0] and sb[1]: print('  ⚠ 两侧黑边：画面左右各有一条纯黑竖边（该片段建议换种子重跑）')
