import sherpa_onnx,subprocess,numpy as np,json,sys
d='asr/sherpa-onnx-streaming-paraformer-bilingual-zh-en/'
rec=sherpa_onnx.OnlineRecognizer.from_paraformer(tokens=d+'tokens.txt',encoder=d+'encoder.int8.onnx',decoder=d+'decoder.int8.onnx',num_threads=4,sample_rate=16000,feature_dim=80)
def tx(a):
    s=rec.create_stream(); s.accept_waveform(16000,a); s.accept_waveform(16000,np.zeros(12000,dtype=np.float32)); s.input_finished()
    while rec.is_ready(s): rec.decode_stream(s)
    r=rec.get_result(s); return r if isinstance(r,str) else r.text
for n in range(1,14):
    raw=subprocess.check_output(['ffmpeg','-v','error','-i',f'e3/第3轮/{n}.mp4','-vn','-ac','1','-ar','16000','-f','f32le','-'])
    a=np.frombuffer(raw,dtype=np.float32); dur=len(a)/16000
    ev=[];last='';t=0.5
    while t<dur+0.01:
        r=tx(a[:int(t*16000)])
        if r!=last: ev.append((round(t,2),r)); last=r
        t+=0.25
    # envelope
    raw2=subprocess.check_output(['ffmpeg','-v','error','-i',f'e3/第3轮/{n}.mp4','-vn','-ac','1','-ar','16000','-af','highpass=f=150,lowpass=f=3800','-f','f32le','-'])
    b=np.frombuffer(raw2,dtype=np.float32);h=4000;k=len(b)//h
    e=np.sqrt((b[:k*h].reshape(k,h)**2).mean(1));m=e.max()
    print(f'#{n:2d} dur {dur:.2f} first {ev[0] if ev else None} final {ev[-1] if ev else None}')
    print('     env',''.join(str(int(9*x/m)) for x in e),flush=True)
