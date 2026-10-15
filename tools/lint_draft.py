#!/usr/bin/env python3
"""制作稿写法检查（现行写法：规律文档 v1.8、自查清单 1–49）。用法: python3 tools/lint_draft.py 制作稿.json
只查“写法规则”，不替代插件自己的格式校验。2026-10-12 按长镜头写法更新（旧稿用它会多报“运镜／多句”以外的新规则）：
  · 允许运镜，但必须写成“动作＋终点”（until/to …）；结尾必须有一句 The camera … 。
  · 一个任务最多 2 句台词；2 句时任务 ≥8 秒；每句计划开口都在任务前半段；15 秒的任务给提示。
  · 新增：开场图里每个人都要写“看着谁”（eyes … on/at 某人/某物，或闭眼）；
          每句台词都要在镜头文字里写明“对谁说”（… to/at [[asset:X]]），X 必须在这个任务里且不是说话人自己；
          旁观的人不准写成虚化（blurred … men/people/elders…）。
"""
import json, re, sys

BANNED = [  # (正则, 说明)
    (r'(?<!sweet )(?<!smug )(?<!coy )(?<!sugary )(?<!sweetly )\bsmil', '不要写 smile（会让人笑；有意的笑要写成 sweet/smug/coy smile）'),
    (r'outside the frame|off-?screen|off-?frame|just outside|beyond the frame|out of frame', '不要把视线目标/人物写在画面之外'),
    (r'mirror|reflection|reflect', '不要镜子/倒影'),
    (r'facing the camera|into the lens|at the camera|stares? ahead|looks? straight ahead|eyes level', '视线不要朝镜头/前方，也不要只写“目光平视”'),
    (r'over[- ]the[- ]shoulder|over her shoulder|over his shoulder', '不要过肩'),
    (r'from the edge|enters? the frame|reaches? in from', '手不要从画面边缘伸进来'),
    (r'twist|strain|\bspin\b|whirl', '动作太大/物理风险'),
    (r'(?:blurred|blurry)[^.;]{0,40}\b(?:men|man|women|woman|people|figures|elders|guests|crowd|couple)\b|\b(?:men|people|figures|elders|guests|crowd|couple)\b[^.;]{0,40}\b(?:blurred|blurry)', '旁观的人不要写成虚化（下一镜会被读成“人消失了”）'),
]
CUE = re.compile(r"lips?|mouth|jaw|brows?|tears?|frown|glar|scowl|narrow|expression|wince|grimace|smirk|smil|pale|stern|cold|blank|clench|tighten|wide eyes|eyes (?:\w+ )?wide|eyes (?:widen|shut|close|lower)|glisten|shine|bite|bites|quiver|tremble", re.I)
GAZE = re.compile(r"eyes[^.;]{0,60}\b(?:on|at|toward|towards|fixed on|locked on)\b|eyes (?:\w+ )?(?:closed|shut)|eyes squeezed shut|\b(?:looks?|looking|stares?|staring|glares?|glaring|gazes?|gazing) (?:up |down )?(?:at|toward|into)\b", re.I)
SPEAK = re.compile(r"\b(?:says?|speaks?|asks?|shouts?|snarls?|hisses?|whispers?|answers?|spits?|growls?|calls?|tells?|line)\b", re.I)
FEMALE = {'Lily', 'Mary', 'Selena', 'Mia', 'Maid', 'Nurse', 'Friend', 'Vivian', 'Jenna', 'Su', 'Wen', 'Tang', 'Liang', 'Xiao'}
FAST = re.compile(r'\b(backhand\w*|hurl\w*|lunge\w*|slam\w*|shove\w*|kick\w*|sprint\w*|charge[sd]?|leap\w*|jump\w*|dive\w*|flies|fly|crash\w*|smash\w*|tackle\w*|punch\w*|stab\w*|plunge\w*|hurtle\w*|blast\w*|throw\w*|hurled)\b', re.I)
MECH = re.compile(r'\b(lock\w*|unlock\w*|curtains?|drapes?|latch\w*|bursts? open|swing\w* open|slam\w* shut|shatter\w*)\b', re.I)
errs = 0
def bad(seg, msg):
    global errs; errs += 1
    print(f'  ✗ {seg}: {msg}')
def warn(seg, msg):
    print(f'  ⚠ {seg}: {msg}')

d = json.load(open(sys.argv[1], encoding='utf-8'))
roles = {a['key']: a.get('role') for a in d.get('assets', [])}
char_assets = {n: c['image_keys'] for n, c in d.get('characters', {}).items()}
for name, c in d.get('characters', {}).items():
    if d.get('dialogue_language') == 'en' and re.search(r'Mandarin|Chinese', c['voice_description']['en'], re.I): bad(name, '人物声音描述还是普通话')
for ep in d['episodes']:
    for s in ep['segments']:
        t = s['title']
        vis = ' '.join(sh['visual_en'] for sh in s['shots'])
        for sh in s['shots']:
            en = sh['visual_en']
            for rx, why in BANNED:
                m = re.search(rx, en, re.I)
                if m: bad(t, f'{why}（命中“{m.group(0)}”）')
            last = re.split(r'(?<=\.)\s+', en.strip())[-1]
            if not last.startswith('The camera'):
                bad(t, '镜头文字最后一句不是 The camera …（镜头固定或“动作＋终点”）')
            elif 'holds still' not in last and not re.search(r'\buntil\b|\bto (?:a|the|her|his)\b', last):
                bad(t, f'运镜没写终点（要写成“推近到…占满画面”这种“动作＋终点”）：{last}')
            if len(s['shots']) > 1: bad(t, '含片内切镜（不用）')
        visc = re.sub(r'brows? (?:crashing|crash) (?:together|down)', '', vis, flags=re.I)
        fast = sorted({m.group(0).lower() for m in FAST.finditer(visc)})
        mech = sorted({m.group(0).lower() for m in MECH.finditer(re.sub(r'locked (?:on|onto|in)\b', '', vis))})
        beats = vis.count(';') + len(re.findall(r'\bthen\b', vis)) + 1
        if fast: warn(t, f'快动作／位移（{",".join(fast)}）：H3 常在这里自己切镜或丢动作；开场图要从接触起手、这个任务只放这一件（H3 风险，不算写错）')
        if mech: warn(t, f'机械／场景状态变化（{",".join(mech)}）：第 25–26 集的锁门、窗帘都没做出来（H3 风险）')
        if beats > 3: warn(t, f'一个任务里有 {beats} 个先后动作（分号／then），超过 3 个：慢的持续动作可以，快动作会被丢')
        ip = s['image_prompt']
        for rx, why in BANNED[:4] + BANNED[-1:]:
            m = re.search(rx, ip, re.I)
            if m: bad(t, f'开场图提示词：{why}（命中“{m.group(0)}”）')
        if 'middle third' not in ip: bad(t, '开场图提示词没写 centered / middle third')
        if len(s['characters']) > 3: bad(t, '有名字的人物超过 3 个')
        elif len(s['characters']) == 3: warn(t, '有名字的人物 3 个（多人镜头，开场图先看人数）')
        if d.get('dialogue_language') == 'en' and re.search(r'Mandarin|Chinese', s['sound_en'] + vis + ip, re.I): bad(t, '提示词里出现 Mandarin/Chinese')
        persons = [a['key'] for a in d.get('assets', []) if a.get('role') == 'character' and a['key'] in s.get('asset_keys', [])]
        names = {k: k.split('_')[0].capitalize() for k in persons}
        def first_person(sent):
            best = None
            for k in persons:
                for rx in (r'\[\[asset:%s\]\]' % re.escape(k), r"\b%s\b" % re.escape(names[k])):
                    m = re.search(rx, sent)
                    if m and (best is None or m.start() < best[0]): best = (m.start(), k)
            if best: return best[1]
            m = re.match(r'\s*(he|his|she|her)\b', sent, re.I)
            if m:
                fem = m.group(1).lower() in ('she', 'her')
                cand = [k for k in persons if (names[k] in FEMALE) == fem]
                if len(cand) == 1: return cand[0]
            return None
        for src_name, txt in (('开场图', ip), ('镜头文字', vis)):
            span = {k: '' for k in persons}
            cur = None
            for sent in re.split(r'(?<=[.;])\s+', txt):
                k = first_person(sent) or cur
                if k: span[k] += ' ' + sent; cur = k
            for k in persons:
                if not CUE.search(span[k]):
                    bad(t, f'{src_name}里人物 {k} 没写具体表情（眼睛＋嘴／下颌）')
                if src_name == '开场图' and not GAZE.search(span[k]):
                    bad(t, f'开场图里人物 {k} 没写看着谁（eyes … on 某人／某物，或闭眼）')
        dl = s['dialogue']
        dur = s['duration_seconds']
        if dl and dur < 5: bad(t, '有台词的任务不要短于 5 秒（2026-10-15 快节奏写法；此前是 6 秒）')
        if len(dl) > 4: bad(t, '一个任务多于四句台词')
        if len(dl) == 4 and dur < 10: bad(t, '四句台词的任务要 ≥10 秒（2026-10-13 新剧第 5 集起测试 12–15 秒四句短话＋结尾动作，待验证）')
        if len(dl) == 4: warn(t, '四句台词（测试写法：每句 ≤ 约 8 个汉字，最后要有一个结尾动作）')
        if len(dl) == 3 and dur < 7: bad(t, '三句台词的任务要 ≥8 秒（2026-10-13 新剧第 1–4 集 004 起允许 3 句短话，待验证）')
        if len(dl) >= 2 and dur < 6: bad(t, '两句台词的任务要 ≥6 秒（2026-10-14 起台词顺滑写法，任务按台词长度收紧）')
        if dur >= 15 and len(dl) > 2: warn(t, '15 秒任务台词多于两句')
        # 每句台词：镜头文字里要写“对谁说”，对象在这个任务里、不是说话人
        targets = [m.group(1) for m in re.finditer(SPEAK.pattern + r"[^.;]{0,80}?\b(?:to|at) \[\[asset:(\w+)\]\]", vis, re.I)]
        for x in dl:
            if x is dl[0] and x['start_seconds'] > dur / 2: bad(t, f'台词“{x["text"]}”计划开口 {x["start_seconds"]} 秒，不在任务前半段（实际会晚 1–6 秒）')
            sp_keys = char_assets.get(x['speaker'], [])
            ok = [k for k in targets if k in s['asset_keys'] and roles.get(k) == 'character' and k not in sp_keys]
            if not ok and not re.search(r'inner voice|voice-over|to (?:himself|herself)', vis, re.I): bad(t, f'台词“{x["text"]}”没在镜头文字里写明对谁说（… to [[asset:某人]]，那人要在画面里）；独白要写 inner voice')
            han = len(re.findall(r'[㐀-鿿]', x['text']))
            lang = x.get('language') or s.get('dialogue_language') or d.get('dialogue_language')
            if lang == 'en':
                if han: bad(t, '英语台词里出现汉字')
                words = len(re.findall(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)*", x['text']))
                if words > 7: bad(t, f'英语台词 {words} 个单词，超过 7 个')
                elif words == 7: warn(t, '英语台词 7 个单词（≤6 更稳）')
                if re.match(r"^\s*[A-Z][a-z]+[,.!?]\s+\S", x['text']) and x['text'].split()[0].strip(',.!?') in ('Lily', 'Killian', 'Paul', 'Mary', 'Selena', 'Noah', 'Vivian', 'Jenna', 'Rick', 'Mack', 'Daniel', 'Webb'):
                    bad(t, f'台词以名字开头再接一句（名字后会停很久）：{x["text"]}')
            elif han > 14: bad(t, f'台词 {han} 个字，超过约 13 字')
            if dur - x['end_seconds'] < 1.0: bad(t, '台词后余量不足 1 秒')
        if not dl:
            if 'free of voices' not in s['sound_en'] and 'no vocal' not in s['sound_en'] and 'No one speaks' not in s['sound_en']:
                bad(t, '无台词片没写“完全没有人声”（或新写法 No one speaks…）')
            if 'Voices stay close and clear' in s['sound_en']: bad(t, '无台词片写了 Voices stay close and clear（H11）')
print('合计问题：', errs)
sys.exit(1 if errs else 0)
