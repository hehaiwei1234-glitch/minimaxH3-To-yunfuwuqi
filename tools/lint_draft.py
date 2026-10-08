#!/usr/bin/env python3
"""制作稿写法检查（对照 CLAUDE.md 第 4 节）。用法: python3 tools/lint_draft.py 制作稿.json
只查“写法规则”，不替代插件自己的格式校验。"""
import json, re, sys

BANNED = [  # (正则, 说明)
    (r'\bsmil', '不要写 smile（手册：会让人笑）'),
    (r'mirror|reflection|reflect', '不要镜子/倒影'),
    (r'facing the camera|into the lens|at the camera|stares? ahead|looks? straight ahead', '视线不要朝镜头/前方'),
    (r'over[- ]the[- ]shoulder|over her shoulder|over his shoulder', '不要过肩'),
    (r'push(es|ed)? in|dolly|zoom|pan |tracking', '运镜只写 The camera holds still'),
    (r'from the edge|enters? the frame|reaches? in from', '手不要从画面边缘伸进来'),
    (r'twist|strain|\bspin\b|whirl', '动作太大/物理风险'),
    (r'blur', '不要虚化前景'),
]
errs = 0
def bad(seg, msg):
    global errs; errs += 1
    print(f'  ✗ {seg}: {msg}')

d = json.load(open(sys.argv[1], encoding='utf-8'))
for ep in d['episodes']:
    for s in ep['segments']:
        t = s['title']
        for sh in s['shots']:
            en = sh['visual_en']
            for rx, why in BANNED:
                m = re.search(rx, en, re.I)
                if m: bad(t, f'{why}（命中“{m.group(0)}”）')
            if not en.rstrip().endswith('The camera holds still.'): bad(t, '镜头描述没以 The camera holds still. 结尾')
            if len(s['shots']) > 1: bad(t, '含片内切镜（本集不用）')
        ip = s['image_prompt']
        for rx, why in BANNED[:3]:
            m = re.search(rx, ip, re.I)
            if m: bad(t, f'开场图提示词：{why}（命中“{m.group(0)}”）')
        if 'middle third' not in ip: bad(t, '开场图提示词没写 centered / middle third')
        if len(s['characters']) > 2: bad(t, '在场人数超过 2')
        dl = s['dialogue']
        if len(dl) > 1: bad(t, '一个任务多于一句台词')
        if len({x['speaker'] for x in dl}) > 1: bad(t, '一个任务多于一个说话人')
        for x in dl:
            n = len(re.findall(r'[㐀-鿿]', x['text']))
            if n > 14: bad(t, f'台词 {n} 个字，超过约 13 字')
            if s['duration_seconds'] - x['end_seconds'] < 1.0: bad(t, '台词后余量不足 1 秒')
        if not dl:
            if 'free of voices' not in s['sound_en'] and 'no vocal' not in s['sound_en']: bad(t, '无台词片没写“完全没有人声”')
            if 'Voices stay close and clear' in s['sound_en']: bad(t, '无台词片写了 Voices stay close and clear（H11）')
print('合计问题：', errs)
sys.exit(1 if errs else 0)
