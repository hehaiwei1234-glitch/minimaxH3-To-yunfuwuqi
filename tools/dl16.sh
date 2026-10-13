#!/bin/bash
# 16 路并行下载（aria2c，断点续传，断了再运行同一条命令就接着下）。
# 用法：
#   bash dl16.sh "下载地址" [保存文件夹] [保存文件名]
#   bash dl16.sh 地址清单.txt [保存文件夹]          （清单每行一个地址，同时下 3 个文件，每个 16 路）
# 默认保存到 /root/rivermind-data/downloads（数据盘；系统盘太小）。
# 可选环境变量：
#   N=8            路数（默认 16，aria2 单服务器最多 16；对方拒绝时降到 8 或 4）
#   HFMIRROR=1     把 https://huggingface.co 换成 https://hf-mirror.com（国内机器常更快）
#   SHA256=xxxx    下完后核对校验码（只对单个文件有效）
URL="${1:-}"; DIR="${2:-/root/rivermind-data/downloads}"; NAME="${3:-}"
N="${N:-16}"
if [ -z "$URL" ]; then sed -n 2,10p "$0" | sed 's/^# \{0,1\}//'; exit 1; fi

if ! command -v aria2c >/dev/null 2>&1; then
  echo "未检测到 aria2c，正在安装…"
  (apt-get update -qq && apt-get install -y -qq aria2) >/dev/null 2>&1 || { echo "安装 aria2 失败，请手动运行：apt-get install -y aria2"; exit 1; }
fi

mkdir -p "$DIR" || exit 1
echo "保存到：$DIR"; df -h "$DIR" | tail -1

COMMON=(-x"$N" -s"$N" -k1M -c --file-allocation=none --auto-file-renaming=false
        --max-tries=0 --retry-wait=3 --connect-timeout=15 --timeout=60
        --summary-interval=10 --console-log-level=warn -d "$DIR")

if [ -f "$URL" ]; then
  if [ "${HFMIRROR:-0}" = 1 ]; then sed 's#https://huggingface.co#https://hf-mirror.com#' "$URL" > /tmp/dl16_list.txt; URL=/tmp/dl16_list.txt; fi
  aria2c "${COMMON[@]}" -j 3 -i "$URL"; rc=$?
else
  if [ "${HFMIRROR:-0}" = 1 ]; then URL="${URL/https:\/\/huggingface.co/https://hf-mirror.com}"; fi
  aria2c "${COMMON[@]}" ${NAME:+-o "$NAME"} "$URL"; rc=$?
fi

if [ $rc -ne 0 ]; then echo "下载没成功（aria2 退出码 $rc）。重新运行同一条命令会从断点接着下；若提示 403/429，试试 N=8 或 N=4。"; exit $rc; fi

if [ -n "${SHA256:-}" ] && [ -z "${NAME:-}" ] && [ ! -f "$URL" ]; then NAME=$(basename "${URL%%\?*}"); fi
if [ -n "${SHA256:-}" ] && [ -n "${NAME:-}" ] && [ -f "$DIR/$NAME" ]; then
  echo "核对校验码…"; GOT=$(sha256sum "$DIR/$NAME" | awk '{print $1}')
  [ "$GOT" = "$SHA256" ] && echo "校验通过" || { echo "校验码不一致！期望 $SHA256，实际 $GOT"; exit 2; }
fi
echo "完成。"; ls -lh "$DIR" | tail -5
