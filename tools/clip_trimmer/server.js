'use strict';
// H3 片段整理工具：本机小网页（只在你自己的电脑上运行，不联网上传）。
const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const lib = require('./lib');
const AdmZip = require('adm-zip');

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

const merged = new Map();         // key -> 成片文件路径（页面上预览用）
const clips = new Map();          // id -> {name, group, file, info, opt}
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
      if (id === 'merged') { const f = merged.get(decodeURIComponent(which || '')); return f ? serveFile(req, res, f) : (res.writeHead(404), res.end()); }
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
      clips.set(id, { name, group: '', file, outFile: path.join(dir, 'out.mp4') });
      return json(res, 200, { id });
    }
    if (req.method === 'POST' && url.pathname === '/api/upload-zip') {
      // 整集（或整批）的 zip：解压出里面的 mp4。zip 里没有子文件夹：zip 的名字就是“这一集”的名字；
      // zip 里每集一个子文件夹：子文件夹的名字是“这一集”的名字。
      const zipName = url.searchParams.get('name') || 'batch.zip';
      const base = safeName(zipName.replace(/\.zip$/i, '')).trim() || 'zip';
      const zip = new AdmZip(await readBody(req));
      const groups = new Map();
      for (const e of zip.getEntries()) {
        if (e.isDirectory || !/\.mp4$/i.test(e.entryName) || /(^|\/)(__MACOSX|\.)/.test(e.entryName)) continue;
        const parts = e.entryName.split('/').filter(Boolean);
        const group = parts.length > 1 ? safeName(parts[parts.length - 2]).trim() || base : base;
        const name = parts[parts.length - 1];
        const id = String(++counter) + '_' + Date.now().toString(36);
        const dir = path.join(WORK, id); fs.mkdirSync(dir, { recursive: true });
        const file = path.join(dir, 'in.mp4');
        fs.writeFileSync(file, e.getData());
        clips.set(id, { name, group, file, outFile: path.join(dir, 'out.mp4') });
        if (!groups.has(group)) groups.set(group, []);
        groups.get(group).push({ id, name });
      }
      if (!groups.size) return json(res, 400, { error: 'zip 里没有找到 mp4 片段：' + zipName });
      return json(res, 200, { groups: [...groups].map(([group, list]) => ({ group, clips: list })) });
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
      const outDir = c.group ? path.join(OUTDIR, c.group) : OUTDIR;
      fs.mkdirSync(outDir, { recursive: true });
      const dst = path.join(outDir, base + '_整理.mp4');
      const r = await lib.render(ffmpeg, c.file, c.outFile, c.info, use || [], speed || 1);
      fs.copyFileSync(c.outFile, dst);
      return json(res, 200, { dur: +r.dur.toFixed(2), saved: dst });
    }
    if (req.method === 'POST' && url.pathname === '/api/merge') {
      const { ids, group, total } = JSON.parse((await readBody(req)).toString('utf8'));
      const files = [], names = [];
      for (const id of ids || []) {
        const c = clips.get(id);
        if (!c || !fs.existsSync(c.outFile)) return json(res, 400, { error: '有片段还没整理保存，请先点“整理这一个”' });
        files.push(c.outFile); names.push(c.name);
      }
      if (!files.length) return json(res, 400, { error: '没有选中的片段' });
      // 每个 zip 一集：存到 输出/<zip名>/成片_<zip名>.mp4；整批总片：输出/成片_整批合并.mp4；直接拖的 mp4：输出/成片_合并.mp4
      let dst, key;
      if (total) { dst = path.join(OUTDIR, '成片_整批合并.mp4'); key = 'total'; }
      else if (group) { fs.mkdirSync(path.join(OUTDIR, group), { recursive: true }); dst = path.join(OUTDIR, group, '成片_' + group + '.mp4'); key = 'g_' + group; }
      else { dst = path.join(OUTDIR, '成片_合并.mp4'); key = 'plain'; }
      const r = await lib.mergeClips(ffmpeg, files, dst);
      merged.set(key, dst);
      return json(res, 200, { count: r.count, dur: +r.dur.toFixed(2), saved: dst, order: names, key });
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
