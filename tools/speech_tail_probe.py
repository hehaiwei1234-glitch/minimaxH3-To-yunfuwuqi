#!/usr/bin/env python3
"""Detect whether a generated clip's speech is hard-cut by the end of the file.

Needs only ffmpeg on PATH (or --ffmpeg). No ASR, no numpy.
Usage:  python speech_tail_probe.py clip1.mp4 clip2.mp4 ...
        python speech_tail_probe.py --dir path/to/NG --ffmpeg C:/.../ffmpeg.exe

Heuristic (relative, so ambience does not matter):
  floor  = 10th-percentile 20ms RMS of the clip      (ambient noise level)
  speech = frames above max(floor*4, 12% of the 95th-percentile RMS)
  cut    = the last 40ms are 'hot' (>= 2.5x floor and >= 20% of speech level)
Reports tail margin = seconds between last speech frame and end of file.
A natural ending has margin >= ~0.3s; a hard cut has margin ~0 (and usually hot=True;
if the cut lands in a gap between syllables it is reported as 'speech reaches the end').
"""
import argparse, array, subprocess, sys, math, pathlib

SR = 16000
WIN = int(SR * 0.02)

def load(ffmpeg, path):
    p = subprocess.run([ffmpeg, '-v', 'error', '-i', str(path), '-vn', '-ac', '1', '-ar', str(SR),
                        '-f', 's16le', '-'], capture_output=True)
    if p.returncode or not p.stdout:
        raise RuntimeError(p.stderr.decode(errors='replace')[:200] or 'no audio')
    a = array.array('h'); a.frombytes(p.stdout[: len(p.stdout) // 2 * 2])
    return a

def rms_frames(a):
    out = []
    for i in range(0, len(a) - WIN + 1, WIN):
        s = 0
        for v in a[i:i + WIN]: s += v * v
        out.append(math.sqrt(s / WIN) / 32768.0)
    return out

def pct(v, q):
    s = sorted(v); return s[min(len(s) - 1, int(q * (len(s) - 1)))]

def probe(ffmpeg, path):
    a = load(ffmpeg, path); r = rms_frames(a); dt = WIN / SR
    floor = max(pct(r, .10), 1e-5); level = pct(r, .95)
    thr = max(floor * 4, level * .12)
    speech = [i for i, x in enumerate(r) if x >= thr]
    if not speech:
        return dict(duration=len(a) / SR, speech=False)
    last = speech[-1]; dur = len(r) * dt
    tail_hot = sum(r[-2:]) / 2
    hot = tail_hot >= max(floor * 2.5, level * .20)
    # segments (merge gaps < 0.25s)
    segs = []; s = speech[0]; prev = s
    for i in speech[1:]:
        if (i - prev) * dt > .25: segs.append((s * dt, (prev + 1) * dt)); s = i
        prev = i
    segs.append((s * dt, (prev + 1) * dt))
    return dict(duration=dur, speech=True, first_speech=speech[0] * dt, last_speech_end=(last + 1) * dt,
                tail_margin=dur - (last + 1) * dt, cut_mid_speech=hot, floor_db=20 * math.log10(floor),
                tail_db=20 * math.log10(max(tail_hot, 1e-6)), segments=segs)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('files', nargs='*'); ap.add_argument('--dir')
    ap.add_argument('--ffmpeg', default='ffmpeg'); ap.add_argument('-v', action='store_true')
    args = ap.parse_args(); files = [pathlib.Path(f) for f in args.files]
    if args.dir: files += sorted(pathlib.Path(args.dir).rglob('*.mp4'))
    if not files: ap.error('no files')
    print(f"{'file':50s} {'dur':>6s} {'lastSpeech':>10s} {'margin':>7s}  verdict")
    bad = 0
    for f in files:
        try: r = probe(args.ffmpeg, f)
        except Exception as e: print(f'{f.name[:50]:50s} ERROR {e}'); continue
        if not r['speech']: print(f'{f.name[:50]:50s} {r["duration"]:6.2f}  (no speech found)'); continue
        reaches_end = r['tail_margin'] < .10
        v = ('CUT MID-SPEECH' if r['cut_mid_speech'] else 'CUT? speech reaches the end' if reaches_end
             else 'tight (<0.3s)' if r['tail_margin'] < .3 else 'ok')
        bad += bool(r['cut_mid_speech'] or reaches_end)
        print(f'{f.name[:50]:50s} {r["duration"]:6.2f} {r["last_speech_end"]:10.2f} {r["tail_margin"]:7.2f}  {v}')
        if args.v: print('   segments:', ', '.join(f'{a:.2f}-{b:.2f}' for a, b in r['segments']),
                         f'| floor {r["floor_db"]:.0f}dB tail {r["tail_db"]:.0f}dB')
    print(f'\n{bad}/{len(files)} clips cut mid-speech')
