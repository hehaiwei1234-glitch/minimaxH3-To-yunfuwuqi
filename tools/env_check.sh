#!/bin/bash
# H3 环境体检：只读，不改任何文件，不下载，不联网（只访问本机 ComfyUI 接口）。
# 用法：bash /root/env_check.sh      输出同时保存到 /root/体检报告.txt
OUT=/root/体检报告.txt
mask(){ sed -E 's/hf_[A-Za-z0-9]+/hf_***/g; s/((token|key|password|secret|authorization)[=: ]+)[^ &"]+/\1***/Ig'; }

main(){
echo "===== 0. 机器 ====="
date; uname -srm
nvidia-smi --query-gpu=name,memory.total,memory.used,driver_version --format=csv,noheader 2>&1 | head -3
free -g | sed -n 2p
df -h / /root/rivermind-data 2>&1

echo; echo "===== 1. ComfyUI 在哪、怎么启动的 ====="
COMFY=""; PID=""
while read -r pid rest; do
  cwd=$(readlink -f /proc/$pid/cwd 2>/dev/null)
  if [ -f "$cwd/main.py" ] && [ -d "$cwd/custom_nodes" ]; then COMFY=$cwd; PID=$pid; break; fi
done < <(ps -eo pid=,args= | grep "[m]ain.py")
if [ -z "$COMFY" ]; then
  for c in /root/comfyui /comfyui /root/ComfyUI /workspace/ComfyUI; do [ -f "$c/main.py" ] && COMFY=$c && break; done
  echo "!! 没找到正在运行的 ComfyUI 进程（可能没启动），改用目录：${COMFY:-没找到}"
fi
PORT=8188; PYBIN=python3
if [ -n "$PID" ]; then
  CMD=$(tr '\0' ' ' < /proc/$PID/cmdline | mask)
  echo "进程：$CMD"
  PYBIN=$(readlink -f /proc/$PID/exe)
  P=$(echo "$CMD" | grep -oE -- "--port[= ][0-9]+" | grep -oE "[0-9]+"); [ -n "$P" ] && PORT=$P
fi
echo "ComfyUI 目录：$COMFY    端口：$PORT    Python：$PYBIN"
[ -n "$COMFY" ] && { echo -n "ComfyUI 版本："; git -C "$COMFY" describe --tags --always 2>/dev/null; git -C "$COMFY" log -1 --format="提交时间 %cd" 2>/dev/null; cat "$COMFY/comfyui_version.py" 2>/dev/null | head -3; }
$PYBIN -c 'import sys,torch;print("python",sys.version.split()[0],"| torch",torch.__version__,"| cuda",torch.version.cuda,"| GPU可用",torch.cuda.is_available())' 2>&1 | tail -1

echo; echo "===== 2. custom_nodes 里装了什么 ====="
if [ -n "$COMFY" ]; then
  for d in "$COMFY"/custom_nodes/*/; do
    n=$(basename "$d"); [ "$n" = "__pycache__" ] && continue
    init=$([ -f "$d/__init__.py" ] && echo "有__init__" || echo "无__init__")
    g=$(git -C "$d" log -1 --format="%h %cd" --date=short 2>/dev/null)
    echo "  $n  [$init]  ${g:-非git}"
  done
  ls -1 "$COMFY"/custom_nodes | grep -E "\.py$" | sed 's/^/  单文件：/'
fi

echo; echo "===== 3. 缺的那个节点（H3ADQwen21MultiReferenceEncodeV1）的代码在这台机器上有没有 ====="
DIRS=""; for d in /root /opt /workspace /home /data /mnt; do [ -d "$d" ] && DIRS="$DIRS $d"; done
FOUND=$(timeout 120 grep -rlsI --include=*.py --exclude-dir=.git --exclude-dir=proc "H3ADQwen21MultiReferenceEncodeV1" $DIRS 2>/dev/null | head -5)
if [ -n "$FOUND" ]; then echo "找到了：$FOUND"; else echo "没有（任何 .py 文件里都没有这个类名）"; fi
python3 - <<'PY'
import zipfile,glob
for z in glob.glob('/root/*.zip')+glob.glob('/root/**/*.zip',recursive=True)[:20]:
    try:
        zf=zipfile.ZipFile(z); hit=[n for n in zf.namelist() if n.endswith('.py') and b'H3ADQwen21MultiReferenceEncodeV1' in zf.read(n)]
        print('压缩包',z,'→','里面有该节点：'+str(hit[:3]) if hit else '里面没有该节点')
    except Exception as e: print('压缩包',z,'读取失败',e)
PY

echo; echo "===== 4. ComfyUI 接口：节点和模型下拉（和插件一键配置检查的是同一批）====="
python3 - "$PORT" <<'PY'
import json,sys,urllib.request
port=sys.argv[1]
try: info=json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/object_info",timeout=120))
except Exception as e: print("连不上 ComfyUI 接口：",e); sys.exit()
print("ComfyUI 已加载节点总数：",len(info))
need=["UNETLoader","CLIPLoader","VAELoader","H3ADQwen21MultiReferenceEncodeV1","KSampler","VAEDecode","SaveImage","LoadImage","H3ADv1BatchReferenceToVideo","MinimaxH3LatentUpscaler3D"]
for n in need: print("  有 " if n in info else "  缺!! ",n)
print("H3 / Minimax / Qwen 相关节点：",sorted(k for k in info if k.startswith(("H3","Minimax","MiniMax")) or "Qwen" in k))
def opts(c,f):
    g=info.get(c,{}).get("input",{}); v=(g.get("required",{}).get(f) or g.get("optional",{}).get(f) or [[]])[0]
    return v if isinstance(v,list) else []
want=[("UNETLoader","unet_name","qwen_image_2.1_int8_convrot.safetensors"),("CLIPLoader","clip_name","qwen3vl_8b_int8_convrot.safetensors"),("VAELoader","vae_name","qwen_image_2.1_vae_bf16.safetensors")]
for c,f,name in want:
    o=opts(c,f); print("  有 " if name in o else "  缺!! ",c,name,"（该下拉共",len(o),"项）")
    print("      下拉里名字含 qwen/h3/minimax 的：",[x for x in o if any(s in x.lower() for s in ("qwen","h3","minimax"))])
print("CLIPLoader 的 type 有 qwen_image：","qwen_image" in opts("CLIPLoader","type"))
PY

echo; echo "===== 5. 模型文件：在哪、多大、有没有下载不全 ====="
du -sh /root/qwen21_models "$COMFY/models" 2>/dev/null
FILES=$(find /root/qwen21_models "$COMFY/models" /root/rivermind-data -maxdepth 5 \( -type f -o -type l \) \( -iname "*qwen*" -o -iname "*h3*" -o -iname "*minimax*" \) \( -iname "*.safetensors" -o -iname "*.gguf" -o -iname "*.pt" \) 2>/dev/null | head -40)
python3 - $FILES <<'PY'
import os,json,struct,sys
if len(sys.argv)<2: print("没找到任何 qwen/h3/minimax 模型文件")
for p in sys.argv[1:]:
    try:
        link=" -> "+os.readlink(p) if os.path.islink(p) else ""
        sz=os.path.getsize(p)
        if not p.endswith(".safetensors"): print(f"  （未校验）{sz/1e9:.2f}GB {p}{link}"); continue
        with open(p,"rb") as f:
            n=struct.unpack("<Q",f.read(8))[0]
            if n>200_000_000: raise ValueError("文件头异常")
            h=json.loads(f.read(n))
        end=max((v["data_offsets"][1] for k,v in h.items() if k!="__metadata__"),default=0); need=8+n+end
        print(("  完整   " if sz==need else "  不完整!! "),f"{sz/1e9:.2f}GB（应为{need/1e9:.2f}GB）",p,link)
    except Exception as e: print("  读取失败!!",p,e)
PY
echo "未下完的残留（.aria2/.part/.tmp，>1MB）："; find /root -maxdepth 5 \( -name "*.aria2" -o -name "*.part" -o -name "*.partial" -o -name "*.tmp" -o -name "*.crdownload" \) -size +1M 2>/dev/null | head -10

echo; echo "===== 6. install_qwen21_parallel.sh 里的关键行（已遮住密钥）====="
[ -f /root/install_qwen21_parallel.sh ] && grep -nE "wget|curl|aria2|huggingface|modelscope|git clone|pip |ln -s|mv |cp |custom_nodes|models/" /root/install_qwen21_parallel.sh | mask | cut -c1-200 | head -40 || echo "没有这个脚本"

echo; echo "===== 7. H3 自动短剧插件 ====="
ls -d "$COMFY"/custom_nodes/*AutoDrama* 2>/dev/null || echo "custom_nodes 里没有 AutoDrama 插件文件夹"
for v in "$COMFY"/custom_nodes/*AutoDrama*/version.py; do [ -f "$v" ] && { echo -n "已装版本："; cat "$v"; }; done
for z in /root/ComfyUI-H3-AutoDrama-Standalone.zip; do [ -f "$z" ] && { echo -n "/root 里压缩包的版本："; unzip -p "$z" 'ComfyUI-H3-AutoDrama-Standalone/version.py' 2>/dev/null; echo; }; done

echo; echo "===== 8. ComfyUI 启动日志：哪些自定义节点导入失败 ====="
LOG=$( (supervisorctl tail -200000 comfyui; supervisorctl tail -200000 comfyui stderr) 2>/dev/null)
if [ -z "$LOG" ]; then LOG=$(cat /var/log/supervisor/comfyui*.log 2>/dev/null | tail -c 200000); fi
echo "$LOG" | grep -A40 "Import times for custom nodes" | tail -45
echo "--- 最近的 Error / Traceback（最后 25 行）---"
echo "$LOG" | grep -iE "IMPORT FAILED|Traceback|Error|cannot import|No module named" | tail -25 | cut -c1-220 | mask
}

main 2>&1 | tee "$OUT"
echo; echo "（以上已保存到 $OUT）"
