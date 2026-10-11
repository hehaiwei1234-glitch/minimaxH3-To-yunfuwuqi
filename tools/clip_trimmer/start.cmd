@echo off
chcp 65001 >nul
cd /d "%~dp0"
title H3 片段整理工具
where node >nul 2>nul
if errorlevel 1 (
  echo 没有找到 Node.js。请先安装 Node.js，到 nodejs.org 下载 LTS 版，装好后再双击本文件。
  pause
  exit /b 1
)
set NEED=0
if not exist "node_modules\ffmpeg-static" set NEED=1
if not exist "node_modules\adm-zip" set NEED=1
if "%NEED%"=="1" (
  echo 第一次使用：正在安装需要的组件，约 1 到 2 分钟，需要联网……
  call npm install --no-audit --no-fund
  if errorlevel 1 (
    echo.
    echo 安装失败。请检查网络后再双击一次；还是不行就把这个窗口截图发给 Claude。
    pause
    exit /b 1
  )
)
node server.js
echo.
echo 工具已停止。
pause
