#!/usr/bin/env python3
"""制作稿写法检查（对照 CLAUDE.md 第 4 节）。用法: python3 tools/lint_draft.py 制作稿.json
只查“写法规则”，不替代插件自己的格式校验。"""
import json, re, sys

BANNED = [  # (正则, 说明)
    # 只有写明“甜/得意/娇”这类有意的笑才放行（sweet/smug/coy/sugary smile）；其余 smile 一律不要
    (r'(?<!sweet )(?<!smug )(?<!coy )(?<!sugary )(?<!sweetly )\bsmil', '不要写 smile（会让人笑；有意的笑要写成 sweet/smug/coy smile）'),
    (r'outside the frame|off-?screen|off-?frame|just outside|beyond the frame|out of frame', '不要把视线目标/人物写在画面之外（会被画到画面边缘，甚至冒出陌生人）'),
    (r'mirror|reflection|reflect', '不要镜子/倒影'),
    (r'facing the camera|into the lens|at the camera|stares? ahead|looks? straight ahead', '视线不要朝镜头/前方'),
    (r'over[- ]the[- ]shoulder|over her shoulder|over his shoulder', '不要过肩'),
    (r'push(es|ed)? in|dolly|zoom|pan |tracking', '运镜只写 The camera holds still'),
    (r'from the edge|enters? the frame|reaches? in from', '手不要从画面边缘伸进来'),
    (r'twist|strain|\bspin\b|whirl', '动作太大/物理风险'),
    (r'blur', '不要虚化前景'),
]
# 表情线索：眼睛＋嘴／下颌／眉的具体描写（只写“看着谁”不算表情）
CUE = re.compile(r"lips?|mouth|jaw|brows?|tears?|frown|glar|scowl|narrow|expression|wince|grimace|smirk|smil|pale|stern|cold|blank|clench|tighten|wide eyes|eyes (?:\w+ )?wide|eyes (?:widen|shut|close|lower)|glisten|shine|bite|bites|quiver|tremble", re.I)
FEMALE = {'Lily', 'Mary'}
errs = 0
def bad(seg, msg):
    global errs; errs += 1
    print(f'  ✗ {seg}: {msg}')

d = json.load(open(sys.argv[1], encoding='utf-8'))
for name, c in d.get('characters', {}).items():
    if d.get('dialogue_language') == 'en' and re.search(r'Mandarin|Chinese', c['voice_description']['en'], re.I): bad(name, '人物声音描述还是普通话')
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
        if d.get('dialogue_language') == 'en' and re.search(r'Mandarin|Chinese', s['sound_en'] + s['shots'][0]['visual_en'] + s['image_prompt'], re.I): bad(t, '提示词里出现 Mandarin/Chinese')
        # 每个人物每个任务都要有具体表情（H3 默认补微笑）：按“句子的第一个出场人物”切分，逐人检查
        persons = [a['key'] for a in d.get('assets', []) if a.get('role') == 'character' and a['key'] in s.get('asset_keys', [])]
        names = {k: k.split('_')[0].capitalize() for k in persons}
        def first_person(sent):
            best = None
            for k in persons:
                for rx in (r'\[\[asset:%s\]\]' % re.escape(k), r"\b%s\b" % re.escape(names[k])):
                    m = re.search(rx, sent)
                    if m and (best is None or m.start() < best[0]): best = (m.start(), k)
            if best: return best[1]
            # 以代词开头的句子：按性别对应到在场的唯一男／女人物
            m = re.match(r'\s*(he|his|she|her)\b', sent, re.I)
            if m:
                fem = m.group(1).lower() in ('she', 'her')
                cand = [k for k in persons if (names[k] in FEMALE) == fem]
                if len(cand) == 1: return cand[0]
            return None
        for src_name, txt in (('开场图', ip), ('镜头文字', ' '.join(sh['visual_en'] for sh in s['shots']))):
            span = {k: '' for k in persons}
            cur = None
            for sent in re.split(r'(?<=[.;])\s+', txt):
                k = first_person(sent) or cur
                if k: span[k] += ' ' + sent; cur = k
            for k in persons:
                if not CUE.search(span[k]):
                    bad(t, f'{src_name}里人物 {k} 没写具体表情（眼睛＋嘴／下颌）')
        dl = s['dialogue']
        if dl and s['duration_seconds'] < 6: bad(t, '有台词的任务不要用 5 秒（台词会贴片尾），用 6 秒以上')
        if len(dl) > 1: bad(t, '一个任务多于一句台词')
        if len({x['speaker'] for x in dl}) > 1: bad(t, '一个任务多于一个说话人')
        for x in dl:
            han = len(re.findall(r'[\u3400-\u9fff]', x['text']))
            lang = x.get('language') or s.get('dialogue_language') or d.get('dialogue_language')
            if lang == 'en':
                if han: bad(t, '英语台词里出现汉字')
                words = len(re.findall(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)*", x['text']))
                if words > 7: bad(t, f'英语台词 {words} 个单词，超过 7 个')
                elif words == 7: print(f'  ⚠ {t}: 英语台词 7 个单词（≤6 更稳）')
            elif han > 14: bad(t, f'台词 {han} 个字，超过约 13 字')
            if s['duration_seconds'] - x['end_seconds'] < 1.0: bad(t, '台词后余量不足 1 秒')
        if not dl:
            if 'free of voices' not in s['sound_en'] and 'no vocal' not in s['sound_en'] and 'No one speaks' not in s['sound_en']:
                bad(t, '无台词片没写“完全没有人声”（或新写法 No one speaks…）')
            if 'Voices stay close and clear' in s['sound_en']: bad(t, '无台词片写了 Voices stay close and clear（H11）')
print('合计问题：', errs)
sys.exit(1 if errs else 0)
