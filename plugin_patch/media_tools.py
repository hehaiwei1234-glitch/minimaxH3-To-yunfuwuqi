from __future__ import annotations
import asyncio
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

def resolve_tools(config, plugin_root):
    """Keep explicit settings; discover private or existing tools for defaults."""
    result=dict(config);root=Path(plugin_root)
    comfy_root=root.parent.parent
    folders=[root/'tools'/'ffmpeg',root/'tools',comfy_root/'ffmpeg'/'bin',
             comfy_root/'ffmpeg',comfy_root/'bin',comfy_root,
             comfy_root.parent/'ffmpeg'/'bin',Path(sys.executable).parent,
             Path(sys.executable).parent/'Scripts']
    for name in ('ffmpeg','ffprobe'):
        configured=str(result.get(name) or '').strip()
        if configured and configured.lower() not in {name,name+'.exe'}:
            result[name]=configured
            continue
        found=None
        filenames=(name+'.exe',name) if sys.platform=='win32' else (name,)
        for folder in folders:
            for filename in filenames:
                candidate=folder/filename
                if candidate.is_file():
                    found=str(candidate.resolve());break
            if found:break
        result[name]=found or shutil.which(name) or shutil.which(name+'.exe') or name
    return result

async def _thread_command(argv):
    # Windows hosts may use a SelectorEventLoop without async subprocess support.
    # Leave the host's event loop untouched and wait in a worker thread.
    flags=getattr(subprocess,'CREATE_NO_WINDOW',0) if sys.platform=='win32' else 0
    process=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE,creationflags=flags)
    waiter=asyncio.create_task(asyncio.to_thread(process.communicate))
    try:
        out,err=await asyncio.shield(waiter)
    except asyncio.CancelledError:
        if process.poll() is None:
            try:process.terminate()
            except ProcessLookupError:pass
        await asyncio.shield(waiter)
        raise
    return out,err,process.returncode

async def command(argv):
    argv=list(map(str,argv))
    try:
        try:
            process=await asyncio.create_subprocess_exec(*argv,stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)
        except NotImplementedError:
            out,err,returncode=await _thread_command(argv)
        else:
            try:out,err=await process.communicate()
            except asyncio.CancelledError:
                try:process.terminate()
                except ProcessLookupError:pass
                await process.wait();raise
            returncode=process.returncode
    except FileNotFoundError as e:
        help_text='；请在新插件文件夹双击 Windows准备工具.cmd，或在设置中填写程序路径。' if sys.platform=='win32' else '；请安装该程序或在设置中填写路径。'
        raise RuntimeError('ComfyUI主机缺少程序：'+str(argv[0])+help_text) from e
    if returncode:raise RuntimeError(str(argv[0])+'执行失败：'+err.decode('utf-8','replace')[-4000:])
    return out

async def probe(path,config):
    data=json.loads(await command([config['ffprobe'],'-v','error','-show_streams','-show_format','-of','json',path]))
    video=next((s for s in data.get('streams',[]) if s['codec_type']=='video'),None)
    audio=next((s for s in data.get('streams',[]) if s['codec_type']=='audio'),None)
    duration=float(data.get('format',{}).get('duration') or (video or {}).get('duration') or 0)
    if not video or not duration>0:raise RuntimeError('视频文件无有效画面或时长：'+str(path))
    return {'duration':duration,'video':video,'audio':audio}

async def keep_duration(source,target,seconds,config):
    """Trim excess generated tail frames, retaining speed and an audio track."""
    target=Path(target);meta=await probe(source,config)
    actual=float(meta['video'].get('duration') or meta['duration'])
    if actual+1/24<seconds:
        raise RuntimeError(f'工作流输出仅{actual:.3f}秒，短于本段所需{seconds:.3f}秒；请检查时长关联和输出帧率。原生成文件已保留。')
    if abs(actual-seconds)<=.001 and meta['duration']<=seconds+.04:return Path(source),meta
    temp=target.with_name(target.stem+'.working.mp4');target.parent.mkdir(parents=True,exist_ok=True)
    ten=any(x in meta['video'].get('pix_fmt','') for x in ('10','12','16'))
    args=[config['ffmpeg'],'-y','-v','error','-i',source,'-map','0:v:0','-map','0:a:0?',
          '-t',f'{seconds:.9f}','-c:v','libx265' if ten else 'libx264','-preset','fast','-crf','16',
          '-pix_fmt','yuv420p10le' if ten else 'yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',temp]
    await command(args);checked=await probe(temp,config)
    if abs(float(checked['video'].get('duration') or checked['duration'])-seconds)>1/24+.001:
        raise RuntimeError('保留片段的时长校验失败，原生成文件已保留。')
    os.replace(temp,target)
    return target,checked

async def keep_full(source,seconds,config):
    """Keep everything H3 generated (no cut of the tail); only fail if the file is shorter than planned.

    Continued clips are generated with extra alignment frames after the planned end. Cutting them
    at the planned length removed the last syllables of lines the model was still speaking.
    If the audio stream overhangs the picture by more than a frame-ish (0.02s) the file is remuxed
    with stream copy so both streams end together: later steps seek to "duration - 0.08s" for the
    last frame and would otherwise land after the final picture.
    """
    source=Path(source);meta=await probe(source,config)
    video=float(meta['video'].get('duration') or meta['duration'])
    if video+1/24<seconds:
        raise RuntimeError(f'工作流输出仅{video:.3f}秒，短于本段所需{seconds:.3f}秒；请检查时长关联和输出帧率。原生成文件已保留。')
    audio=float((meta['audio'] or {}).get('duration') or 0)
    if audio<=video+.02:return source,meta
    temp=source.with_name(source.stem+'_对齐.mp4')
    await command([config['ffmpeg'],'-y','-v','error','-i',source,'-map','0:v:0','-map','0:a:0?','-c','copy','-t',f'{video:.6f}','-movflags','+faststart',temp])
    return temp,await probe(temp,config)

def signature(meta):
    v=meta['video'];a=meta['audio'] or {}
    return tuple(v.get(k) for k in ('codec_name','width','height','pix_fmt','r_frame_rate','time_base','codec_tag_string','profile','level'))+tuple(a.get(k) for k in ('codec_name','sample_rate','channels','channel_layout','time_base'))

def concat_line(path):
    # FFmpeg concat grammar, not shell quoting.
    return "file '"+Path(path).resolve().as_posix().replace("'","'\\''")+"'\n"

async def merge(paths,target,config):
    target=Path(target);target.parent.mkdir(parents=True,exist_ok=True)
    metas=[await probe(p,config) for p in paths]
    temp=target.with_name(target.stem+'.working.mp4')
    manifest=target.with_suffix('.concat.txt')
    same=all(signature(m)==signature(metas[0]) for m in metas)
    used=list(paths);mode='copy'
    if same:
        manifest.write_text(''.join(concat_line(p) for p in used),encoding='utf-8')
        try:await command([config['ffmpeg'],'-y','-v','error','-f','concat','-safe','0','-i',manifest,'-map','0:v:0','-map','0:a:0?','-c','copy','-movflags','+faststart',temp])
        except RuntimeError:same=False
    if not same:
        mode='normalized';used=[]
        width=metas[0]['video']['width'];height=metas[0]['video']['height']
        tenbit=any(('10' in m['video'].get('pix_fmt','') or '12' in m['video'].get('pix_fmt','')) for m in metas)
        for i,(path,meta) in enumerate(zip(paths,metas)):
            normalized=target.parent/f'merge_{target.stem}_{i:04d}.mp4'
            argv=[config['ffmpeg'],'-y','-v','error','-i',path]
            if not meta['audio']:argv+=['-f','lavfi','-i','anullsrc=channel_layout=stereo:sample_rate=48000']
            argv+=['-map','0:v:0','-map','0:a:0' if meta['audio'] else '1:a:0','-vf',f'scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,fps=24,setsar=1',
                   '-c:v','libx265' if tenbit else 'libx264','-preset','medium','-crf','16','-pix_fmt','yuv420p10le' if tenbit else 'yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-t',str(meta['duration']),normalized]
            await command(argv);used.append(normalized)
        manifest.write_text(''.join(concat_line(p) for p in used),encoding='utf-8')
        await command([config['ffmpeg'],'-y','-v','error','-f','concat','-safe','0','-i',manifest,'-map','0:v:0','-map','0:a:0?','-c','copy','-movflags','+faststart',temp])
    final_meta=await probe(temp,config)
    expected=sum(m['duration'] for m in metas)
    if abs(final_meta['duration']-expected)>max(1,len(paths)*0.12):raise RuntimeError('合并后的时长与各镜头总时长不一致。')
    os.replace(temp,target)
    return {'duration':final_meta['duration'],'merge_mode':mode,'filename':target.name}
