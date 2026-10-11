#!/usr/bin/env python3
"""H3 片段“停顿压缩”工具：自动剪掉 台词中间的长停顿、开口前的空等、念完后的空等，
只剪“没有人声 且 画面几乎不动 且 剪掉后前后画面接得上”的部分，其余一帧不动。

用法:
    python trim_dead_time.py <mp4 或 文件夹> [更多 mp4 或文件夹] [--dry] [--out 输出文件夹]
    --dry     只分析、只出报告，不生成视频（先用这个看它打算剪哪里）
    --all     连没有台词的片段也处理（默认没有人声的片段不动）
    --ffmpeg  指定 ffmpeg 路径（默认先找 PATH，再找 ComfyUI 插件自带的）
调参（一般不用动）:
    --gap 0.45     台词中间的停顿，压到这么长（秒）
    --lead 0.8     第一个字之前，最多留这么长（秒）
    --tail 0.8     最后一个字之后，最多留这么长（秒）
    --motion 0.45  “画面几乎不动”的门槛（每帧平均变化量，越小越严）
    --match 1.2    “剪掉后前后画面接得上”的门槛（越小越严，越小越容易“不剪”）

安全规则（不影响表演和台词的保证）:
 1. 只在没有人声的地方剪；人声前后各多留 0.2 秒，保护轻辅音和气口。
 2. 被剪掉的那一段，画面平均变化量必须低于门槛（人在“站着不动/微表情”，不是在做动作）。
 3. 剪口两端的画面必须几乎一样（最像的一对），所以看上去是连续的，不会跳。找不到就不剪。
 4. 每个片段开头 0.5 秒不剪（保持和上一个片段的衔接）；声音在剪口处做 20 毫秒交叉渐变，不会“啪”一声。
 5. 原文件不动，结果放到新文件夹（默认“压缩后”），并写 压缩报告.txt。
"""
import argparse
import glob
import json
import os
import shutil
import subprocess
import sys

import numpy as np

SR = 16000
W, H = 96, 36


def find_ffmpeg(explicit, name):
    if explicit:
        d = os.path.dirname(explicit)
        cand = os.path.join(d, name + ('.exe' if os.name == 'nt' else '')) if name != 'ffmpeg' else explicit
        if os.path.isfile(cand):
            return cand
    found = shutil.which(name)
    if found:
        return found
    here = os.path.dirname(os.path.abspath(__file__))
    roots = [here]
    p = here
    for _ in range(5):
        p = os.path.dirname(p)
        roots.append(p)
    for r in roots:
        for pat in ('custom_nodes/*/tools/ffmpeg/%s*', 'tools/ffmpeg/%s*', 'ffmpeg/bin/%s*', 'ComfyUI/custom_nodes/*/tools/ffmpeg/%s*'):
            hits = glob.glob(os.path.join(r, pat % name))
            hits = [h for h in hits if os.path.isfile(h)]
            if hits:
                return hits[0]
    sys.exit('找不到 %s。请先双击 ComfyUI 插件文件夹里的 Windows准备工具.cmd，或用 --ffmpeg 指定路径。' % name)


def run(argv, binary=False):
    r = subprocess.run(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode:
        raise RuntimeError(r.stderr.decode('utf-8', 'replace')[-1500:])
    return r.stdout if binary else r.stdout.decode('utf-8', 'replace')


def probe(ffprobe, path):
    d = json.loads(run([ffprobe, '-v', 'error', '-show_streams', '-show_format', '-of', 'json', path]))
    v = next(s for s in d['streams'] if s['codec_type'] == 'video')
    a = next((s for s in d['streams'] if s['codec_type'] == 'audio'), None)
    num, den = v['r_frame_rate'].split('/')
    fps = float(num) / float(den)
    return v, a, fps


def load_frames(ffmpeg, path):
    raw = run([ffmpeg, '-v', 'error', '-i', path, '-an', '-vf', 'scale=%d:%d:flags=area,format=gray' % (W, H), '-f', 'rawvideo', '-'], True)
    return np.frombuffer(raw, dtype=np.uint8).reshape(-1, H, W).astype(np.float32)


def load_speech_env(ffmpeg, path, fps, nframes):
    """每帧一个数：150–3800 Hz 频带的短时能量（平滑 5 帧）。"""
    raw = run([ffmpeg, '-v', 'error', '-i', path, '-vn', '-ac', '1', '-ar', str(SR),
               '-af', 'highpass=f=150,lowpass=f=3800', '-f', 'f32le', '-'], True)
    a = np.frombuffer(raw, dtype=np.float32)
    e = np.zeros(nframes, dtype=np.float32)
    for i in range(nframes):
        s0, s1 = int(i * SR / fps), int((i + 1) * SR / fps)
        seg = a[s0:s1]
        e[i] = float(np.sqrt((seg ** 2).mean())) if len(seg) else 0.0
    k = 5
    sm = np.sqrt(np.convolve(e ** 2, np.ones(k) / k, mode='same'))
    return sm


def speech_regions(env, fps, pad_s, merge_s, thr_ratio=0.10, min_len_s=0.3):
    """返回帧区间列表 [(s,e)]：有人声的部分（已前后各加 pad 保护；相距 < merge 的合并）。"""
    if env.max() <= 0:
        return []
    floor = 3.0 * float(np.median(env))          # 稳定的环境声（风声、底噪）不算人声
    on = env > max(thr_ratio * env.max(), floor, 1e-3)
    regs = []
    i, n = 0, len(on)
    while i < n:
        if on[i]:
            j = i
            while j < n and on[j]:
                j += 1
            regs.append([i, j])
            i = j
        else:
            i += 1
    merged = []
    for r in regs:
        if merged and (r[0] - merged[-1][1]) / fps < merge_s:
            merged[-1][1] = r[1]
        else:
            merged.append(r)
    merged = [r for r in merged if (r[1] - r[0]) / fps >= min_len_s]
    pad = int(round(pad_s * fps))
    out = []
    for s, e in merged:
        s, e = max(0, s - pad), min(n, e + pad)
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out


def best_cut(F, d, csum, lo, hi, max_remove, min_remove, thr_motion, thr_match):
    """在帧区间 [lo,hi] 里找一对 (a,b)：剪掉 a..b-1，b-a<=max_remove，平均变化量低，a 与 b 两帧最像。
    返回 (a,b,diff,motion) 或 (None, 原因)。"""
    best = None
    seen_motion_ok = False
    for a in range(lo, hi - min_remove + 1):
        for b in range(a + min_remove, min(hi, a + max_remove) + 1):
            motion = (csum[b] - csum[a]) / (b - a)
            if motion > thr_motion:
                continue
            seen_motion_ok = True
            diff = float(np.abs(F[a - 1] - F[b]).mean())   # 剪完后 a-1 帧直接接 b 帧
            if diff > thr_match:
                continue
            key = (b - a, -diff)
            if best is None or key > best[0]:
                best = (key, a, b, diff, motion)
    if best:
        return best[1], best[2], best[3], best[4]
    return None, None, ('画面在动，不剪' if not seen_motion_ok else '找不到前后接得上的剪口，不剪'), None


def plan_clip(F, env, fps, opt):
    n = len(F)
    d = np.abs(np.diff(F, axis=0)).mean(axis=(1, 2))  # d[i] = 第 i 帧到 i+1 帧
    csum = np.concatenate([[0.0], np.cumsum(d)])      # 区间 [a,b) 的变化量 = csum[b]-csum[a]
    regs = speech_regions(env, fps, opt.pad, opt.merge)
    notes, cuts = [], []
    if not regs:
        return cuts, ['没有检测到人声，不处理（加 --all 可强制处理）'], d, regs
    ks = int(round(opt.keep_start * fps))
    minr = max(2, int(round(opt.min_cut * fps)))
    # 句子中间的停顿
    for (s1, e1), (s2, e2) in zip(regs[:-1], regs[1:]):
        gap_s = (s2 - e1) / fps          # 含两侧保护的静音长度
        raw_gap = gap_s + 2 * opt.pad    # 真正的静音长度（不含保护）
        if raw_gap <= opt.gap + 0.05:
            continue
        max_remove = int(round((raw_gap - opt.gap) * fps))
        max_remove = min(max_remove, s2 - e1)
        a, b, *rest = best_cut(F, d, csum, e1, s2, max_remove, minr, opt.motion, opt.match)
        if a is None:
            notes.append('句中停顿 %.2f–%.2f 秒（静音约 %.1f 秒）：%s' % (e1 / fps, s2 / fps, raw_gap, rest[0]))
        else:
            cuts.append(('句中停顿', a, b, rest[0], rest[1]))
    # 第一个字之前
    s0 = regs[0][0]
    lead = s0 / fps + opt.pad
    if lead > opt.lead + 0.05:
        lo, hi = ks, s0
        max_remove = int(round((lead - opt.lead) * fps))
        max_remove = min(max_remove, hi - lo)
        if hi - lo >= minr:
            a, b, *rest = best_cut(F, d, csum, lo, hi, max_remove, minr, opt.motion, opt.match)
            if a is None:
                notes.append('开口前 0–%.2f 秒：%s' % (s0 / fps, rest[0]))
            else:
                cuts.append(('开口前', a, b, rest[0], rest[1]))
    # 最后一个字之后（直接截掉末尾：要求末尾一直几乎不动）
    el = regs[-1][1]
    tail = (n - el) / fps + opt.pad
    if tail > opt.tail + 0.05:
        start = el + int(round((opt.tail - opt.pad) * fps)) if opt.tail > opt.pad else el
        start = max(start, el)
        # 找最长的“不动后缀”
        c = n - 1
        tail_motion = opt.motion * 0.55            # 片尾要求几乎冻住，比别处更严
        while c - 1 >= start and d[c - 1] <= tail_motion * 3:
            c -= 1
        cs = max(start, c)
        if n - cs >= minr and (csum[n - 1] - csum[cs]) / max(1, (n - 1 - cs)) <= tail_motion:
            cuts.append(('念完之后', cs, n, 0.0, float((csum[n - 1] - csum[cs]) / max(1, (n - 1 - cs)))))
        else:
            notes.append('念完之后 %.2f–%.2f 秒：画面还在动，不剪' % (el / fps, n / fps))
    cuts.sort(key=lambda x: x[1])
    return cuts, notes, d, regs


def build_output(ffmpeg, src, dst, n, fps, cuts, has_audio, ten_bit):
    # 保留的帧区间
    keep, pos = [], 0
    for _, a, b, *_ in cuts:
        if a > pos:
            keep.append((pos, a))
        pos = b
    if pos < n:
        keep.append((pos, n))
    parts, vlabels, alabels = [], [], []
    for i, (s, e) in enumerate(keep):
        parts.append('[0:v]trim=start_frame=%d:end_frame=%d,setpts=PTS-STARTPTS[v%d]' % (s, e, i))
        vlabels.append('[v%d]' % i)
    parts.append(''.join(vlabels) + 'concat=n=%d:v=1:a=0[vout]' % len(keep))
    maps = ['-map', '[vout]']
    if has_audio:
        x = 0.01
        for i, (s, e) in enumerate(keep):
            t0 = s / fps - (x if i > 0 else 0)
            t1 = e / fps + (x if i < len(keep) - 1 else 0)
            parts.append('[0:a]atrim=start=%.6f:end=%.6f,asetpts=PTS-STARTPTS[a%d]' % (max(0, t0), t1, i))
            alabels.append('[a%d]' % i)
        cur = alabels[0]
        for i in range(1, len(keep)):
            out = '[ax%d]' % i
            parts.append('%s%sacrossfade=d=0.02:c1=tri:c2=tri%s' % (cur, alabels[i], out))
            cur = out
        maps += ['-map', cur]
    args = [ffmpeg, '-y', '-v', 'error', '-i', src, '-filter_complex', ';'.join(parts)] + maps + [
        '-r', '%g' % fps, '-c:v', 'libx265' if ten_bit else 'libx264', '-preset', 'medium', '-crf', '16',
        '-pix_fmt', 'yuv420p10le' if ten_bit else 'yuv420p']
    if has_audio:
        args += ['-c:a', 'aac', '-b:a', '192k']
    args += ['-movflags', '+faststart', dst]
    run(args)
    return sum(e - s for s, e in keep)


def collect(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d != '压缩后']
                for f in sorted(files):
                    if f.lower().endswith('.mp4') and not f.endswith('_压缩.mp4'):
                        out.append(os.path.join(root, f))
        elif p.lower().endswith('.mp4'):
            out.append(p)
    return out


def main():
    ap = argparse.ArgumentParser(description='H3 片段停顿压缩')
    ap.add_argument('paths', nargs='+')
    ap.add_argument('--dry', action='store_true')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--out', default=None)
    ap.add_argument('--ffmpeg', default=None)
    ap.add_argument('--gap', type=float, default=0.45)
    ap.add_argument('--lead', type=float, default=0.8)
    ap.add_argument('--tail', type=float, default=0.8)
    ap.add_argument('--motion', type=float, default=0.45)
    ap.add_argument('--match', type=float, default=1.2)
    ap.add_argument('--pad', type=float, default=0.2)
    ap.add_argument('--merge', type=float, default=0.55, help='相距小于这么多秒的人声当作同一段')
    ap.add_argument('--keep-start', dest='keep_start', type=float, default=0.5)
    ap.add_argument('--min-cut', dest='min_cut', type=float, default=0.25)
    opt = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    ffmpeg = find_ffmpeg(opt.ffmpeg, 'ffmpeg')
    ffprobe = find_ffmpeg(opt.ffmpeg, 'ffprobe')
    files = collect(opt.paths)
    if not files:
        sys.exit('没有找到 mp4 文件。')
    first_dir = os.path.dirname(os.path.abspath(files[0]))
    outdir = opt.out or os.path.join(first_dir, '压缩后')
    if not opt.dry:
        os.makedirs(outdir, exist_ok=True)
    report, total_in, total_out = [], 0.0, 0.0
    for path in files:
        name = os.path.basename(path)
        try:
            v, a, fps = probe(ffprobe, path)
            F = load_frames(ffmpeg, path)
            n = len(F)
            if a is None:
                report.append('== %s\n  没有音轨，不处理' % name)
                continue
            env = load_speech_env(ffmpeg, path, fps, n)
            cuts, notes, d, regs = plan_clip(F, env, fps, opt)
            dur = n / fps
            total_in += dur
            lines = ['== %s  原长 %.2f 秒；人声 %s' % (name, dur, '、'.join('%.2f–%.2f' % (s / fps, e / fps) for s, e in regs) or '无')]
            if not regs and not opt.all:
                report.append('\n'.join(lines + ['  没有检测到人声，不处理（加 --all 可强制处理）']))
                total_out += dur
                print(report[-1])
                continue
            removed = 0.0
            for kind, a_, b_, diff, motion in cuts:
                removed += (b_ - a_) / fps
                lines.append('  剪 %s：原片 %.2f–%.2f 秒，去掉 %.2f 秒（前后画面差 %.2f，期间画面变化 %.2f）' % (kind, a_ / fps, b_ / fps, (b_ - a_) / fps, diff, motion))
            for t in notes:
                lines.append('  没剪：' + t)
            if not cuts:
                lines.append('  没有可以安全剪掉的地方，原样保留')
                total_out += dur
            else:
                new_len = dur - removed
                total_out += new_len
                if not opt.dry:
                    dst = os.path.join(outdir, os.path.splitext(name)[0] + '_压缩.mp4')
                    ten = any(x in v.get('pix_fmt', '') for x in ('10', '12', '16'))
                    kept = build_output(ffmpeg, path, dst, n, fps, cuts, a is not None, ten)
                    lines.append('  → %s（%.2f 秒 → %.2f 秒）' % (os.path.basename(dst), dur, kept / fps))
                else:
                    lines.append('  （--dry：只分析，没有生成）%.2f 秒 → %.2f 秒' % (dur, new_len))
            report.append('\n'.join(lines))
        except Exception as ex:  # 单个文件出错不影响其他文件
            report.append('== %s\n  出错，已跳过：%s' % (name, str(ex)[-300:]))
        print(report[-1])
    summary = '\n合计：%d 个片段，%.1f 秒 → %.1f 秒（少了 %.1f 秒）' % (len(files), total_in, total_out, total_in - total_out)
    print(summary)
    if not opt.dry:
        with open(os.path.join(outdir, '压缩报告.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(report) + summary + '\n')
        print('报告：' + os.path.join(outdir, '压缩报告.txt'))


if __name__ == '__main__':
    main()
