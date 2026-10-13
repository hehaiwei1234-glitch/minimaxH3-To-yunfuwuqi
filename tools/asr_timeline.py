"""一遍过的流式中文语音识别：在含有 0*.mp4 的目录里运行，逐个打印整段识别结果和文字出现的时间（约每 0.2 秒一次，只打印每隔一个变化点）。
注意：文字出现的时间比真正开口晚约 0.7–1 秒；开口时间以 tools/clip_trimmer 的人声检测为准。需要先跑 tools/setup_asr.sh 下载模型（路径写在下面 d= 里，按实际改）。
"""
import sys,subprocess,numpy as np,sherpa_onnx,glob
d='/tmp/claude-0/asr/sherpa-onnx-streaming-paraformer-bilingual-zh-en'
rec=sherpa_onnx.OnlineRecognizer.from_paraformer(tokens=d+'/tokens.txt',encoder=d+'/encoder.int8.onnx',decoder=d+'/decoder.int8.onnx',num_threads=4,sample_rate=16000,feature_dim=80)
for f in sorted(glob.glob('0*.mp4')):
    a=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',f,'-vn','-ac','1','-ar','16000','-f','f32le','-']),dtype=np.float32)
    s=rec.create_stream(); step=3200; last='';hist=[]
    for i in range(0,len(a),step):
        s.accept_waveform(16000,a[i:i+step])
        while rec.is_ready(s): rec.decode_stream(s)
        t=rec.get_result(s)
        t=t if isinstance(t,str) else t.text
        if t!=last: hist.append(((i+step)/16000,t)); last=t
    s.accept_waveform(16000,np.zeros(16000,dtype=np.float32)); s.input_finished()
    while rec.is_ready(s): rec.decode_stream(s)
    t=rec.get_result(s); t=t if isinstance(t,str) else t.text
    print(f[:5],'最终:',t)
    print("   ",[(round(x,1),y) for x,y in hist][::2])
