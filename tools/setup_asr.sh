#!/usr/bin/env bash
# 安装分析脚本需要的东西，并下载中文语音识别小模型。
# 用法:  bash tools/setup_asr.sh [模型放在哪个目录，默认 ~/asr]
set -e
pip install --break-system-packages sherpa-onnx numpy aiohttp 2>/dev/null || pip install sherpa-onnx numpy aiohttp
which ffmpeg ffprobe >/dev/null || { echo "缺少 ffmpeg，请先安装: apt-get install -y ffmpeg"; exit 1; }
DIR="${1:-$HOME/asr}"
mkdir -p "$DIR"
cd "$DIR"
M=sherpa-onnx-streaming-paraformer-bilingual-zh-en
if [ ! -d "$M" ]; then
  # 约 1 GB，来自 GitHub release（云端通常放行 GitHub）
  curl -L -o pf.tar.bz2 "https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/$M.tar.bz2"
  tar xjf pf.tar.bz2
  rm -f pf.tar.bz2
fi
echo "模型目录: $DIR/$M"
echo "用法: python3 tools/clip_report.py $DIR/$M 视频1.mp4 视频2.mp4 ..."
