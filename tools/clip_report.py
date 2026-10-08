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
