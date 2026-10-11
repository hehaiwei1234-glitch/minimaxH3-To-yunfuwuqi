'use strict';
// H3 片段整理：分析（哪里是没人说话又几乎不动的空等）+ 输出。
// 算法与 trim_dead_time.py 完全一致（那份用 numpy，这份只用 Node 自带的东西 + ffmpeg）。
const { spawn, spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const SR = 16000, W = 96, H = 36;

function findFfmpeg() {
  const env = process.env.FFMPEG_PATH;
  if (env && fs.existsSync(env)) return env;
  try { const p = require('ffmpeg-static'); if (p && fs.existsSync(p)) return p; } catch (e) { /* 没装也行，继续找 */ }
  const r = spawnSync(process.platform === 'win32' ? 'where' : 'which', ['ffmpeg'], { encoding: 'utf8' });
  if (r.status === 0) {
    const l = r.stdout.split(/\r?\n/).map(s => s.trim()).filter(Boolean)[0];
    if (l) return l;
  }
  return null;
}

function run(bin, args, allowFail) {
  return new Promise((res, rej) => {
    const p = spawn(bin, args, { windowsHide: true });
    const out = [], err = [];
    p.stdout.on('data', d => out.push(d));
    p.stderr.on('data', d => err.push(d));
    p.on('error', rej);
    p.on('close', code => {
      const o = { out: Buffer.concat(out), err: Buffer.concat(err).toString('utf8') };
      if (code === 0 || allowFail) res(o); else rej(new Error(o.err.slice(-1500)));
    });
  });
}

async function probe(bin, file) {
  const { err } = await run(bin, ['-hide_banner', '-i', file], true);
  const vline = (err.match(/Stream #\d+:\d+[^\n]*Video:[^\n]*/) || [''])[0];
  const fps = parseFloat((vline.match(/([\d.]+) fps/) || [])[1]) || 24;
  return { fps, hasAudio: /Stream #\d+:\d+[^\n]*Audio:/.test(err), tenBit: /10le|10be|p010|12le|12be/.test(vline) };
}

async function loadFrames(bin, file) {
  const { out } = await run(bin, ['-v', 'error', '-i', file, '-an', '-vf', `scale=${W}:${H}:flags=area,format=gray`, '-f', 'rawvideo', '-']);
  const n = Math.floor(out.length / (W * H));
  return { F: new Uint8Array(out.buffer.slice(out.byteOffset, out.byteOffset + n * W * H)), n };
}

async function loadEnv(bin, file, fps, n) {
  const { out } = await run(bin, ['-v', 'error', '-i', file, '-vn', '-ac', '1', '-ar', String(SR),
    '-af', 'highpass=f=150,lowpass=f=3800', '-f', 'f32le', '-']);
  const len = Math.floor(out.length / 4);
  const a = new Float32Array(out.buffer.slice(out.byteOffset, out.byteOffset + len * 4));
  const e = new Float64Array(n);
  for (let i = 0; i < n; i++) {
    const s0 = Math.trunc(i * SR / fps), s1 = Math.min(len, Math.trunc((i + 1) * SR / fps));
    if (s1 > s0) { let q = 0; for (let j = s0; j < s1; j++) q += a[j] * a[j]; e[i] = Math.sqrt(q / (s1 - s0)); }
  }
  const sm = new Float64Array(n);                      // 5 帧平滑（等同 numpy convolve mode='same'）
  for (let i = 0; i < n; i++) {
    let q = 0;
    for (let m = -2; m <= 2; m++) { const j = i + m; if (j >= 0 && j < n) q += e[j] * e[j]; }
    sm[i] = Math.sqrt(q / 5);
  }
  return sm;
}

function median(arr) {
  const s = Array.from(arr).sort((x, y) => x - y), n = s.length;
  return n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2;
}

function speechRegions(env, fps, padS, mergeS, thrRatio = 0.10, minLenS = 0.3) {
  let mx = 0; for (const v of env) if (v > mx) mx = v;
  if (mx <= 0) return [];
  const thr = Math.max(thrRatio * mx, 3.0 * median(env), 1e-3);
  const n = env.length, regs = [];
  let i = 0;
  while (i < n) {
    if (env[i] > thr) { let j = i; while (j < n && env[j] > thr) j++; regs.push([i, j]); i = j; } else i++;
  }
  const merged = [];
  for (const r of regs) {
    if (merged.length && (r[0] - merged[merged.length - 1][1]) / fps < mergeS) merged[merged.length - 1][1] = r[1];
    else merged.push(r.slice());
  }
  const kept = merged.filter(r => (r[1] - r[0]) / fps >= minLenS);
  const pad = Math.round(padS * fps), out = [];
  for (let [s, e] of kept) {
    s = Math.max(0, s - pad); e = Math.min(n, e + pad);
    if (out.length && s <= out[out.length - 1][1]) out[out.length - 1][1] = Math.max(out[out.length - 1][1], e);
    else out.push([s, e]);
  }
  return out;
}

function frameDiff(F, a, b) {
  const oa = a * W * H, ob = b * W * H;
  let s = 0;
  for (let k = 0; k < W * H; k++) s += Math.abs(F[oa + k] - F[ob + k]);
  return s / (W * H);
}

function bestCut(F, csum, lo, hi, maxRemove, minRemove, thrMotion, thrMatch) {
  let best = null, seenMotionOk = false;
  for (let a = lo; a <= hi - minRemove; a++) {
    if (a < 1) continue;
    const bMax = Math.min(hi, a + maxRemove);
    for (let b = a + minRemove; b <= bMax; b++) {
      const motion = (csum[b] - csum[a]) / (b - a);
      if (motion > thrMotion) continue;
      seenMotionOk = true;
      const diff = frameDiff(F, a - 1, b);             // 剪完后 a-1 帧直接接 b 帧
      if (diff > thrMatch) continue;
      if (!best || (b - a) > best.len || ((b - a) === best.len && -diff > -best.diff)) best = { a, b, diff, motion, len: b - a };
    }
  }
  if (best) return best;
  return { fail: seenMotionOk ? '找不到前后接得上的剪口，不剪' : '画面在动，不剪' };
}

const PRESETS = {
  safe:  { name: '稳妥（推荐）', motion: 0.45, match: 1.2, lead: 0.4, tail: 0.4 },
  more:  { name: '多剪一点',     motion: 0.70, match: 1.6, lead: 0.3, tail: 0.3 },
  bold:  { name: '最大胆',       motion: 1.00, match: 2.2, lead: 0.2, tail: 0.2 },
};

function planClip(F, n, env, fps, o) {
  const d = new Float64Array(Math.max(0, n - 1));
  for (let i = 0; i < n - 1; i++) d[i] = frameDiff(F, i, i + 1);
  const csum = new Float64Array(n);
  for (let i = 1; i < n; i++) csum[i] = csum[i - 1] + d[i - 1];
  const regs = speechRegions(env, fps, o.pad, o.merge);
  const notes = [], cuts = [];
  if (!regs.length) return { cuts, notes: ['没有检测到人声，不处理'], regs };
  const ks = Math.round(o.keepStart * fps), minr = Math.max(2, Math.round(o.minCut * fps));
  // 第一个字之前
  const s0 = regs[0][0], lead = s0 / fps + o.pad;
  if (lead > o.lead + 0.05) {
    const lo = ks, hi = s0, maxRemove = Math.min(Math.round((lead - o.lead) * fps), hi - lo);
    if (hi - lo >= minr) {
      const r = bestCut(F, csum, lo, hi, maxRemove, minr, o.motion, o.match);
      if (r.fail) notes.push(`开头（0–${(s0 / fps).toFixed(2)} 秒）：${r.fail}`);
      else cuts.push({ kind: '开头', a: r.a, b: r.b, diff: r.diff, motion: r.motion });
    }
  }
  // 最后一个字之后（直接截掉末尾，要求末尾一直几乎不动）
  const el = regs[regs.length - 1][1], tail = (n - el) / fps + o.pad;
  if (tail > o.tail + 0.05) {
    let start = o.tail > o.pad ? el + Math.round((o.tail - o.pad) * fps) : el;
    start = Math.max(start, el);
    let c = n - 1;
    const tm = o.motion * 0.55;
    while (c - 1 >= start && d[c - 1] <= tm * 3) c--;
    const cs = Math.max(start, c);
    const mot = (csum[n - 1] - csum[cs]) / Math.max(1, n - 1 - cs);
    if (n - cs >= minr && mot <= tm) cuts.push({ kind: '结尾', a: cs, b: n, diff: 0, motion: mot });
    else notes.push(`结尾（${(el / fps).toFixed(2)}–${(n / fps).toFixed(2)} 秒）：画面还在动，不剪`);
  }
  cuts.sort((x, y) => x.a - y.a);
  return { cuts, notes, regs };
}

async function analyze(bin, file, optIn) {
  const o = Object.assign({ pad: 0.2, merge: 0.55, keepStart: 0.5, minCut: 0.25 }, PRESETS.safe, optIn || {});
  const pr = await probe(bin, file);
  const { F, n } = await loadFrames(bin, file);
  if (!pr.hasAudio) return { fps: pr.fps, n, dur: n / pr.fps, hasAudio: false, cuts: [], notes: ['没有声音轨，不处理'], regs: [], tenBit: pr.tenBit };
  const env = await loadEnv(bin, file, pr.fps, n);
  const p = planClip(F, n, env, pr.fps, o);
  return { fps: pr.fps, n, dur: n / pr.fps, hasAudio: true, tenBit: pr.tenBit, regs: p.regs, cuts: p.cuts, notes: p.notes };
}

async function render(bin, src, dst, info, cutIdx, speed) {
  const { n, fps, hasAudio, tenBit } = info;
  const cuts = cutIdx.map(i => info.cuts[i]).filter(Boolean).sort((x, y) => x.a - y.a);
  const keep = []; let pos = 0;
  for (const c of cuts) { if (c.a > pos) keep.push([pos, c.a]); pos = c.b; }
  if (pos < n) keep.push([pos, n]);
  if (keep.length === 1 && keep[0][0] === 0 && keep[0][1] === n && Math.abs((Number(speed) || 1) - 1) < 1e-6) {
    fs.copyFileSync(src, dst);                       // 什么都不剪、不加速：原样复制，不重新编码，画质零损失
    return { frames: n, dur: n / fps };
  }
  const parts = [], vl = [], al = [];
  keep.forEach(([s, e], i) => { parts.push(`[0:v]trim=start_frame=${s}:end_frame=${e},setpts=PTS-STARTPTS[v${i}]`); vl.push(`[v${i}]`); });
  parts.push(`${vl.join('')}concat=n=${keep.length}:v=1:a=0[vc]`);
  const sp = Number(speed) || 1;
  let vlast = '[vc]';
  if (Math.abs(sp - 1) > 1e-6) { parts.push(`[vc]setpts=PTS/${sp}[vout]`); vlast = '[vout]'; }
  const maps = ['-map', vlast];
  if (hasAudio) {
    const x = 0.01;
    keep.forEach(([s, e], i) => {
      const t0 = s / fps - (i > 0 ? x : 0), t1 = e / fps + (i < keep.length - 1 ? x : 0);
      parts.push(`[0:a]atrim=start=${Math.max(0, t0).toFixed(6)}:end=${t1.toFixed(6)},asetpts=PTS-STARTPTS[a${i}]`);
      al.push(`[a${i}]`);
    });
    let cur = al[0];
    for (let i = 1; i < keep.length; i++) { parts.push(`${cur}${al[i]}acrossfade=d=0.02:c1=tri:c2=tri[ax${i}]`); cur = `[ax${i}]`; }
    if (Math.abs(sp - 1) > 1e-6) { parts.push(`${cur}atempo=${sp}[aout]`); cur = '[aout]'; }
    maps.push('-map', cur);
  }
  const args = ['-y', '-v', 'error', '-i', src, '-filter_complex', parts.join(';'), ...maps,
    '-r', String(fps), '-c:v', tenBit ? 'libx265' : 'libx264', '-preset', 'medium', '-crf', '16',
    '-pix_fmt', tenBit ? 'yuv420p10le' : 'yuv420p'];
  if (hasAudio) args.push('-c:a', 'aac', '-b:a', '192k');
  args.push('-movflags', '+faststart', dst);
  await run(bin, args);
  const frames = keep.reduce((s, [a, b]) => s + (b - a), 0);
  return { frames, dur: frames / fps / sp };
}

// 读出合并需要的信息：尺寸、帧率、时长、有没有声音、是不是 10 位
async function probeFull(bin, file) {
  const { err } = await run(bin, ['-hide_banner', '-i', file], true);
  const vline = (err.match(/Stream #\d+:\d+[^\n]*Video:[^\n]*/) || [''])[0];
  const wh = vline.match(/,\s*(\d{2,5})x(\d{2,5})/);
  const fps = parseFloat((vline.match(/([\d.]+) fps/) || [])[1]) || 24;
  const dm = err.match(/Duration:\s*(\d+):(\d+):([\d.]+)/);
  return {
    w: wh ? +wh[1] : 0, h: wh ? +wh[2] : 0, fps,
    dur: dm ? (+dm[1]) * 3600 + (+dm[2]) * 60 + parseFloat(dm[3]) : 0,
    hasAudio: /Stream #\d+:\d+[^\n]*Audio:/.test(err),
    tenBit: /10le|10be|p010|12le|12be/.test(vline),
  };
}

// 把若干个 mp4 按给定顺序接成一个成片（重新编码一次，保证声画同步；尺寸、帧率以第一个为准）
async function mergeClips(bin, files, dst) {
  if (!files.length) throw new Error('没有可以合并的片段');
  if (files.length === 1) { fs.copyFileSync(files[0], dst); const i = await probeFull(bin, dst); return { count: 1, dur: i.dur }; }
  const infos = [];
  for (const f of files) infos.push(await probeFull(bin, f));
  const w = Math.floor(infos[0].w / 2) * 2, h = Math.floor(infos[0].h / 2) * 2, fps = infos[0].fps;
  const anyAudio = infos.some(i => i.hasAudio);
  const ten = infos.every(i => i.tenBit);
  const pix = ten ? 'yuv420p10le' : 'yuv420p';
  const args = ['-y', '-v', 'error'];
  files.forEach(f => args.push('-i', f));
  const parts = [], cat = [];
  infos.forEach((it, i) => {
    parts.push(`[${i}:v]scale=${w}:${h}:force_original_aspect_ratio=decrease,pad=${w}:${h}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=${fps},format=${pix},setpts=PTS-STARTPTS[v${i}]`);
    cat.push(`[v${i}]`);
    if (anyAudio) {
      if (it.hasAudio) parts.push(`[${i}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,asetpts=PTS-STARTPTS[a${i}]`);
      else parts.push(`anullsrc=r=48000:cl=stereo,atrim=duration=${it.dur.toFixed(3)},asetpts=PTS-STARTPTS[a${i}]`);
      cat.push(`[a${i}]`);
    }
  });
  parts.push(`${cat.join('')}concat=n=${files.length}:v=1:a=${anyAudio ? 1 : 0}[vo]${anyAudio ? '[ao]' : ''}`);
  args.push('-filter_complex', parts.join(';'), '-map', '[vo]');
  if (anyAudio) args.push('-map', '[ao]');
  args.push('-r', String(fps), '-c:v', ten ? 'libx265' : 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', pix);
  if (anyAudio) args.push('-c:a', 'aac', '-b:a', '192k');
  args.push('-movflags', '+faststart', dst);
  await run(bin, args);
  const out = await probeFull(bin, dst);
  return { count: files.length, dur: out.dur };
}

module.exports = { findFfmpeg, analyze, render, mergeClips, probeFull, PRESETS };
