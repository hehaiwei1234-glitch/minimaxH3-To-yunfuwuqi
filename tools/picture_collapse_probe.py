#!/usr/bin/env python3
"""Find the moment a generated clip's picture collapses into noise (花屏). Needs ffmpeg + numpy + Pillow-free.

Usage:  python picture_collapse_probe.py clip1.mp4 clip2.mp4 ...     (or --dir folder, --ffmpeg path)
Per frame it measures colourfulness, brightness, fine detail and frame-to-frame change on a
downscaled copy. A healthy shot keeps these steady; a collapse shows as a sudden jump in change
followed by colourfulness falling well below the clip's own baseline and staying there.
"""
import argparse, pathlib, subprocess, sys
import numpy as np

W, H = 224, 84

def frames(ffmpeg, path):
    p = subprocess.run([ffmpeg, '-v', 'error', '-i', str(path), '-an', '-vf', f'scale={W}:{H}', '-pix_fmt', 'rgb24',
                        '-f', 'rawvideo', '-'], capture_output=True)
    if p.returncode or not p.stdout: raise RuntimeError(p.stderr.decode(errors='replace')[:200] or 'no video')
    n = len(p.stdout) // (W * H * 3)
    return np.frombuffer(p.stdout[:n * W * H * 3], dtype=np.uint8).reshape(n, H, W, 3).astype(np.float32)

def fps_of(ffmpeg, path):
    ffprobe = ffmpeg.replace('ffmpeg', 'ffprobe')
    try:
        out = subprocess.run([ffprobe, '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate',
                              '-of', 'default=nw=1:nk=1', str(path)], capture_output=True, text=True).stdout.strip()
        a, b = out.split('/'); return float(a) / float(b)
    except Exception: return 24.0

def analyse(ffmpeg, path):
    f = frames(ffmpeg, path); fps = fps_of(ffmpeg, path); n = len(f)
    chroma = (f.max(axis=3) - f.min(axis=3)).mean(axis=(1, 2))
    luma = f.mean(axis=(1, 2, 3))
    g = f.mean(axis=3)
    detail = np.abs(4 * g[:, 1:-1, 1:-1] - g[:, :-2, 1:-1] - g[:, 2:, 1:-1] - g[:, 1:-1, :-2] - g[:, 1:-1, 2:]).mean(axis=(1, 2))
    diff = np.r_[0, np.abs(f[1:] - f[:-1]).mean(axis=(1, 2, 3))]
    base = slice(0, max(8, int(n * .4)))
    c0, d0, m0 = np.median(chroma[base]), np.median(detail[base]), np.median(diff[1:base.stop]) + 1e-6
    bad = (chroma < .72 * c0) | (detail < .6 * d0)
    run = None; i = 0
    while i < n:                                   # first sustained run (>= 0.3s) of 'bad' frames
        if bad[i]:
            j = i
            while j < n and bad[j]: j += 1
            if (j - i) >= max(6, int(.3 * fps)) or j == n and (j - i) >= 4: run = (i, j); break
            i = j
        else: i += 1
    if not run: return dict(frames=n, fps=fps, collapsed=False, chroma0=c0)
    start = run[0]
    for k in range(max(1, start - 8), start + 1):  # walk back to the first frame where the picture jumped
        if diff[k] > 8 * m0 and diff[k] > 2.5: start = k; break
    return dict(frames=n, fps=fps, collapsed=True, onset_frame=start, onset_s=start / fps, duration_s=n / fps,
                bad_share=float(bad[start:].mean()), chroma0=c0, chroma_after=float(np.median(chroma[start + 4:])) if n > start + 4 else float(chroma[-1]))

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('files', nargs='*'); ap.add_argument('--dir'); ap.add_argument('--ffmpeg', default='ffmpeg')
    a = ap.parse_args(); files = [pathlib.Path(x) for x in a.files]
    if a.dir: files += sorted(pathlib.Path(a.dir).rglob('*.mp4'))
    if not files: ap.error('no files')
    print(f"{'file':52s} {'len':>6s}  verdict"); bad = 0
    for p in files:
        try: r = analyse(a.ffmpeg, p)
        except Exception as e: print(f'{p.name[:52]:52s} ERROR {e}'); continue
        if r['collapsed']:
            bad += 1
            print(f"{p.name[:52]:52s} {r['duration_s']:6.2f}  COLLAPSE from {r['onset_s']:.2f}s  (colour {r['chroma0']:.0f} -> {r['chroma_after']:.0f}, rest of clip {r['bad_share']*100:.0f}% bad)")
        else: print(f"{p.name[:52]:52s} {r['frames']/r['fps']:6.2f}  ok")
    print(f'\n{bad}/{len(files)} clips collapse')
