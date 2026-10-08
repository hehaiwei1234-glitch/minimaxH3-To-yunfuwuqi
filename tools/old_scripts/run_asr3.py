import sherpa_onnx,subprocess,numpy as np,sys,json,os
d='asr/sherpa-onnx-streaming-paraformer-bilingual-zh-en/'
rec=sherpa_onnx.OnlineRecognizer.from_paraformer(tokens=d+'tokens.txt',encoder=d+'encoder.int8.onnx',decoder=d+'decoder.int8.onnx',num_threads=4,sample_rate=16000,feature_dim=80)
def run(path):
    raw=subprocess.check_output(['ffmpeg','-v','error','-i',path,'-vn','-ac','1','-ar','16000','-f','f32le','-'])
    a=np.frombuffer(raw,dtype=np.float32)
    s=rec.create_stream(); 
    s.accept_waveform(16000,a); s.accept_waveform(16000,np.zeros(16000,dtype=np.float32)); s.input_finished()
    while rec.is_ready(s): rec.decode_stream(s)
    r=rec.get_result(s)
    r=r if isinstance(r,str) else r.text
    return r
names=['video.mp4']+[f'video ({i}).mp4' for i in range(1,15)]
out={}
for n,name in enumerate(names,1):
    out[n]=run(f'e3/第3轮/{n}.mp4'); print(n,out[n],flush=True)
json.dump(out,open('asr/e3_asr.json','w'),ensure_ascii=False)
