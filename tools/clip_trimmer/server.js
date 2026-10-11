'use strict';
// H3 片段整理工具：本机小网页（只在你自己的电脑上运行，不联网上传）。
const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const lib = require('./lib');

const PORT = Number(process.env.PORT) || 8765;
const ROOT = __dirname;
const WORK = path.join(ROOT, '工作区');
const OUTDIR = path.join(ROOT, '输出');
fs.mkdirSync(WORK, { recursive: true });
fs.mkdirSync(OUTDIR, { recursive: true });

const ffmpeg = lib.findFfmpeg();
if (!ffmpeg) {
  console.log('\n找不到 ffmpeg。请先在本文件夹里运行 npm install（需要联网，会自动下载 ffmpeg），');
  console.log('或者设置环境变量 FFMPEG_PATH 指向你电脑上的 ffmpeg.exe。\n');
  process.exit(1);
}
console.log('使用 ffmpeg：' + ffmpeg);

const clips = new Map();          // id -> {name, file, info, opt}
let counter = 0;

function json(res, code, obj) {
  const b = Buffer.from(JSON.stringify(obj));
  res.writeHead(code, { 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': b.length });
  res.end(b);
}
function readBody(req) {
  return new Promise((ok, bad) => { const c = []; req.on('data', d => c.push(d)); req.on('end', () => ok(Buffer.concat(c))); req.on('error', bad); });
}
function safeName(s) { return s.replace(/[\\/:*?"<>|]/g, '_'); }

function serveFile(req, res, file) {
  if (!fs.existsSync(file)) { res.writeHead(404); return res.end('not found'); }
  const st = fs.statSync(file);
  const range = /bytes=(\d*)-(\d*)/.exec(req.headers.range || '');
  const type = file.endsWith('.html') ? 'text/html; charset=utf-8' : file.endsWith('.mp4') ? 'video/mp4' : 'application/octet-stream';
  if (range) {
    const s = range[1] ? parseInt(range[1], 10) : 0, e = range[2] ? parseInt(range[2], 10) : st.size - 1;
    res.writeHead(206, { 'Content-Type': type, 'Accept-Ranges': 'bytes', 'Content-Range': `bytes ${s}-${e}/${st.size}`, 'Content-Length': e - s + 1 });
    fs.createReadStream(file, { start: s, end: e }).pipe(res);
  } else {
    res.writeHead(200, { 'Content-Type': type, 'Accept-Ranges': 'bytes', 'Content-Length': st.size, 'Cache-Control': 'no-store' });
    fs.createReadStream(file).pipe(res);
  }
}

function cutsView(info) {
  return info.cuts.map(c => ({ kind: c.kind, from: +(c.a / info.fps).toFixed(2), to: +(c.b / info.fps).toFixed(2), len: +((c.b - c.a) / info.fps).toFixed(2) }));
}

const server = http.createServer(async (req, res) => {
  try {
    const url = new URL(req.url, 'http://x');
    if (req.method === 'GET' && url.pathname === '/') return serveFile(req, res, path.join(ROOT, 'public', 'index.html'));
    if (req.method === 'GET' && url.pathname === '/api/presets') return json(res, 200, lib.PRESETS);
    if (req.method === 'GET' && url.pathname.startsWith('/media/')) {
      const [, , id, which] = url.pathname.split('/');
      const c = clips.get(id);
      if (!c) { res.writeHead(404); return res.end(); }
      return serveFile(req, res, which === 'out' ? c.outFile : c.file);
    }
    if (req.method === 'POST' && url.pathname === '/api/upload') {
      const name = url.searchParams.get('name') || 'clip.mp4';
      const id = String(++counter) + '_' + Date.now().toString(36);
      const dir = path.join(WORK, id); fs.mkdirSync(dir, { recursive: true });
      const file = path.join(dir, 'in.mp4');
      fs.writeFileSync(file, await readBody(req));
      clips.set(id, { name, file, outFile: path.join(dir, 'out.mp4') });
      return json(res, 200, { id });
    }
    if (req.method === 'POST' && url.pathname === '/api/analyze') {
      const { id, preset } = JSON.parse((await readBody(req)).toString('utf8'));
      const c = clips.get(id);
      if (!c) return json(res, 404, { error: '找不到这个片段，请重新拖进来' });
      const p = lib.PRESETS[preset] || lib.PRESETS.safe;
      c.info = await lib.analyze(ffmpeg, c.file, p);
      const removed = c.info.cuts.reduce((s, x) => s + (x.b - x.a), 0) / c.info.fps;
      return json(res, 200, { dur: +c.info.dur.toFixed(2), newDur: +(c.info.dur - removed).toFixed(2), cuts: cutsView(c.info), notes: c.info.notes,
        speech: c.info.regs.map(([s, e]) => [+(s / c.info.fps).toFixed(2), +(e / c.info.fps).toFixed(2)]), hasAudio: c.info.hasAudio });
    }
    if (req.method === 'POST' && url.pathname === '/api/render') {
      const { id, use, speed } = JSON.parse((await readBody(req)).toString('utf8'));
      const c = clips.get(id);
      if (!c || !c.info) return json(res, 404, { error: '请先分析' });
      const base = safeName(c.name.replace(/\.mp4$/i, ''));
      const dst = path.join(OUTDIR, base + '_整理.mp4');
      const r = await lib.render(ffmpeg, c.file, c.outFile, c.info, use || [], speed || 1);
      fs.copyFileSync(c.outFile, dst);
      return json(res, 200, { dur: +r.dur.toFixed(2), saved: dst });
    }
    if (req.method === 'POST' && url.pathname === '/api/open-output') {
      const cmd = process.platform === 'win32' ? ['explorer', [OUTDIR]] : process.platform === 'darwin' ? ['open', [OUTDIR]] : ['xdg-open', [OUTDIR]];
      try { spawn(cmd[0], cmd[1], { detached: true, stdio: 'ignore' }).unref(); } catch (e) { /* 打不开就算了 */ }
      return json(res, 200, { dir: OUTDIR });
    }
    res.writeHead(404); res.end('not found');
  } catch (e) {
    console.error(e);
    json(res, 500, { error: String(e.message || e).slice(-800) });
  }
});

server.listen(PORT, '127.0.0.1', () => {
  const url = `http://localhost:${PORT}`;
  console.log(`\n已启动：${url}\n（用完直接关掉这个黑窗口就行）\n`);
  if (!process.env.NO_BROWSER) {
    try {
      if (process.platform === 'win32') spawn('cmd', ['/c', 'start', '', url], { detached: true, stdio: 'ignore', windowsHide: true }).unref();
      else if (process.platform === 'darwin') spawn('open', [url], { detached: true, stdio: 'ignore' }).unref();
    } catch (e) { /* 打不开浏览器就让用户手动打开 */ }
  }
});
server.on('error', e => {
  if (e.code === 'EADDRINUSE') console.log(`端口 ${PORT} 被占用：可能已经开着一个本工具的窗口，直接打开 http://localhost:${PORT} 即可。`);
  else console.log(String(e));
  process.exit(1);
});
