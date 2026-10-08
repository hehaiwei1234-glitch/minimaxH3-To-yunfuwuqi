import sherpa_onnx,subprocess,numpy as np,json
d='asr/sherpa-onnx-streaming-paraformer-bilingual-zh-en/'
rec=sherpa_onnx.OnlineRecognizer.from_paraformer(tokens=d+'tokens.txt',encoder=d+'encoder.int8.onnx',decoder=d+'decoder.int8.onnx',num_threads=4,sample_rate=16000,feature_dim=80)
names=['video.mp4']+[f'video ({i}).mp4' for i in range(1,15)]
res={}
for n,name in enumerate(names,1):
    raw=subprocess.check_output(['ffmpeg','-v','error','-i','r1/片子/'+name,'-vn','-ac','1','-ar','16000','-f','f32le','-'])
    a=np.frombuffer(raw,dtype=np.float32)
    s=rec.create_stream(); last='';ev=[]
    step=1600
    for i in range(0,len(a)+16000,step):
        chunk=a[i:i+step] if i<len(a) else np.zeros(step,dtype=np.float32)
        s.accept_waveform(16000,chunk)
        while rec.is_ready(s): rec.decode_stream(s)
        r=rec.get_result(s); r=r if isinstance(r,str) else r.text
        if r!=last: ev.append((round((i+step)/16000,1),r)); last=r
    res[n]=ev
    print(n,ev[0] if ev else None,'...',ev[-1] if ev else None,flush=True)
json.dump(res,open('asr/r1_timing.json','w'),ensure_ascii=False)
