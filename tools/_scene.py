"""剧本第 27 集起的写稿工具（2026-10-12 12:30 起）：开场图提示词、站位表、镜头文字从“同一张表”生成。

为什么：第 25–26 集 6 个问题里，开场图／视频没照做的不算我的错，但“一个任务里塞 3–4 个快动作”“前后镜头状态对不上”
是我的错；而且每个任务手写 2.5 KB 英文，漏写“看着谁”“表情”“旁边的人”太容易。现在每个任务只写一次：
  · P(...)   一个画面里的人：站在哪一边、姿势、看着谁、表情 → 自动生成开场图里这个人的那一句，同时进站位表（看着谁、左右）；
  · lines    每句台词写明对谁说 → 站位表检查“听的人在不在画面里”；
  · st       每个人这一镜开头／结尾的状态 → 站位表检查前后镜头接不接得上；
  · 动作文字里用 <killian_gold> 这样的写法，自动换成 [[asset:killian_gold]]。
交稿前 Session.finish() 会跑：站位表检查、种子不重复检查、写入 json 和“全选复制粘贴.txt”。
"""
import copy, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _h3draft as H
from _h3draft import Batch, FOLDER, IMG, breathy, voiced, configure
from _blocking import B, check

FIX = ('The camera holds still.', '镜头固定不动。')
CUE = re.compile(r"lips?|mouth|jaw|brows?|tears?|frown|glar|scowl|narrow|expression|wince|grimace|smirk|smil|pale|stern|cold|blank|clench|tighten|wide eyes|eyes (?:\w+ )?wide|eyes (?:widen|shut|close|lower)|glisten|shine|bite|bites|quiver|tremble", re.I)
LOOKS = {}


def smooth_text(tx):
    """台词只留句末一个标点：句内逗号、顿号、省略号、感叹号、问号全去掉（“他们，还有救……”→“他们还有救。”）。"""
    m = re.search(r'[。！？…]+$', tx)
    run = m.group() if m else ''
    end = '？' if '？' in run else ('！' if '！' in run else '。')
    body = re.sub(r'[，、；：。！？…,.!?]+', '', tx)
    return body + end


# ---------------------------------------------------------------------------------------------- 光和空气词拦截（2026-10-16）
# hh 10-16 回传的 11 个片段：突然“披上一层别的东西”、一个人变两个人，都对上了开场图／视频文字里的光边、轮廓、闪光、热气飘这类词
# （例：“pale rim along her cheek and his shoulder”“glows like a fresh wound”“rims their shoulders”“steam curls through the beam”“frost-furred”）。
# H3 和生图模型把它们当成真的东西画出来（一圈边、一层壳、第二个轮廓）。所以这些词不再写，剩下的光只写“光源＋颜色＋它照到哪”。
BAN_AE = re.compile(r"\b(?:rim\w*|edges?|outlin\w*|halo\w*|auras?|shimmer\w*|sparkl\w*|glitter\w*|glint\w*|gleam\w*|beams?|rays?|shafts?|motes?|specks?|furr?\w*|lantern\w*|wounds?|veil\w*|bloom\w*|flare\w*|crystals?|translucent|stained|flicker\w*|puls\w*|wash\w*|slid\w*|curl\w*|drift\w*|swirl\w*|float\w*|hover\w*|steam\w*|mist\w*|haze|hazy|fog\w*|dust\w*|droplets?|spray\w*|sparks?|particles?|snowflakes?|flakes?|embers?|cinders?|smoke|graz\w+|spill\w*|glisten\w*|shin(?:e|es|ing|y)|lustre|luster|sheen|dappl\w*|streak\w*|ripple\w*|burns?|burning)\b|\blike an? |\bas if\b|\bglow\w* like\b|\bglow\w* (?:through|over|across|along|around|on|upon|against|from within|past|beyond)\b|\bglow\w* and\b|\bglow\w* (?:above|below|beside|behind|near|inside|within)\b|\blight (?:falls?|lies|lay|catches|lands|touches|sits)\b", re.I)
BAN_AE_ZH = re.compile(r"边|轮廓|勾|描出|光束|光柱|光线|光晕|光环|闪|晶莹|晶体|冰晶|尘|粉雪|雪粒|热气|蒸汽|水汽|雾|卷|飘|像|仿佛|宛如|如同|洗过|罩|镀|镶|倒影|辉|耀|粼|折射|透亮|火星|火花|烟|余烬|涟漪|烧")
_SPLIT_EN = re.compile(r",\s+(?:and\s+)?|\s+while\s+|;\s+", re.I)
_BAD_START = re.compile(r"^(?:which|that|making|giving|casting|leaving|turning|lending|with|as|so|but|then|until|where|whose|creating|forming|adding)\b", re.I)


def calm(ae):
    """ae=(英文, 中文) 的“光和空气”句：逐个分句检查，带拦截词的分句整句丢掉，剩下的重新写成句子。可能返回 ('','')。"""
    en, zh = ae
    keep = []
    for c in _SPLIT_EN.split(en.strip()):
        c = c.strip().rstrip('.').strip()
        if not c or BAN_AE.search(c) or _BAD_START.match(c): continue
        keep.append(c[0].upper() + c[1:] + '.')
    keep_zh = []
    for c in re.split(r"[，；。]", zh.strip()):
        c = c.strip()
        if not c or BAN_AE_ZH.search(c): continue
        keep_zh.append(c)
    return (' '.join(keep), ('，'.join(keep_zh) + '。') if keep_zh else '')


WORD_FIX = [(r'with a thin line of pink-violet light glowing around its edges', 'with a small pink-violet lit panel'), (r'\bsun glows through\b', 'sun shows through'), (r'\b(gold|silver|thin|round|metal|black|steel)-rimmed\b', r'\1-framed'), (r' like a lone wolf\'s', ''), (r'frost-furred', 'frost-covered'), (r'\bthin glowing blue ring\b', 'thin blue ring'),
            (r'\beyes (?:shining|sparkling|glittering|gleaming)\b', 'eyes bright'), (r'\beyes glistening\b', 'eyes wet'), (r'\beyes burning\b', 'eyes fierce'),
            (r'red-rimmed', 'reddened'), (r'\bglows? on (his|her|their) (faces?)\b', r'lights \1 \2'),
            (r'flares up with a cold white glow', 'turns a cold bright white'),
            (r'\bfurred with\b', 'crusted with'), (r'\bfurred\b', 'frosted'), (r'\bglistening\b', 'wet'), (r'\bember-orange\b', 'deep orange')]


def fixw(text):
    """个别会被画成“多出一层东西”的词换成平实的说法（眼睛发光、毛茸茸的霜、一圈红边）。"""
    for a, b in WORD_FIX: text = re.sub(a, b, text)
    return text


LATERAL = re.compile(r"tracks sideways|slides slowly|arcs slowly around|slowly (?:left|right)\b", re.I)


def safe_cam(cam, n_people):
    """画面里有人时，不用左右平移／环绕（会露出一块新空间，H3 往里填人：2026-10-16 hh 的 11 个片段里 3 个）；改成推近。"""
    if n_people and LATERAL.search(cam[0]):
        who_en, who_zh = ('the person fills', '这个人占满') if n_people == 1 else ('both of them fill', '两人占满')
        return (f'The camera pushes in slowly until {who_en} the middle third of the frame.', f'镜头慢慢推近，直到{who_zh}画面中间三分之一。')
    return cam


TONE_FIX = [(', quiet voice', ', clear voice'), ('breathy voice', 'bright voice'), (', hoarse voice', ', rough voice')]


def smooth_task(lines, dur, act_en, zh):
    """把一个任务的台词改成“紧凑一口气”的写法并收紧任务长度。窗口 ≈ 自然说话时间 × 1.4。"""
    new, t, tot = [], H.CFG['start'], 0.
    for sp, tx, start, to in lines:
        tx2 = smooth_text(tx); nat = H.line_seconds(tx2)
        new.append((sp, tx2, round(t, 2), to)); t = t + nat + H.CFG['gap']; tot += nat
    n = len(new)
    need = 0.75 + H.CFG['need_k'] * tot + 0.12 * (n - 1)
    last_end = new[-1][2] + H.line_seconds(new[-1][1]) + 0.05
    floor = H.CFG['floors'].get(n, max(H.CFG['floors'].values()) + 1)
    d = max(floor, int(-(-need // 1)), int(-(-(last_end + 1.0) // 1)))
    for a, b in TONE_FIX: act_en = act_en.replace(a, b)
    if H.CFG['fast_text']:
        act_en += ' The dialogue is delivered at a fast, snappy pace, about twenty percent quicker than normal speech, with no lingering pauses.'
        zh += ' 台词语速偏快利落，比平常说话快两成左右，没有拖沓的停顿。'
    if n == 1:
        act_en += ' The line is spoken naturally in one breath, with no pause inside the sentence.'
        zh += ' 这句话自然地一口气说完，句中不停顿。'
    else:
        act_en += ' The lines are spoken briskly and naturally, each in one breath with no pause inside the sentence, and the next line follows right away.'
        zh += ' 台词说得利落自然，每句一口气说完、句中不停顿，下一句紧接着开口。'
    return new, d, act_en, zh


ENDS = set()
RISK = []     # (任务编号, 位置, 词, 前后文)：生成后仍留在文字里的“光边／闪光／热气飘”类词，finish() 会列出


class Look:
    def __init__(self, asset, char, outfit, eyes, pron, eth=''):
        self.asset, self.char, self.outfit, self.eyes, self.pron = asset, char, outfit, eyes, pron
        self.eth = eth          # 人种／年龄的括号说明，例如 'a Chinese man'（新剧用；旧剧不填，输出不变）
        self.who = asset.split('_')[0].capitalize()          # 和 lint_draft 的取名规则一致


def look(asset, char, outfit, eyes, pron, eth=''):
    LOOKS[asset] = Look(asset, char, outfit, eyes, pron, eth)


class Scene:
    def __init__(self, key, end, layout):
        self.key, self.end, self.layout = key, end, layout


def P(lk, side, pose, target, expr, extra='', eyes=None, outfit=None, verb='on', shut='squeezed shut'):
    """target: 画面里另一个人的名字（'Lily'），或 'obj:一个具体的东西'（要写进句子里的原文），或 'closed'（闭眼）。"""
    return dict(lk=lk, side=side, pose=pose, target=target, expr=expr, extra=extra, eyes=eyes, outfit=outfit, verb=verb, shut=shut)


def sentence(p):
    L = LOOKS[p['lk']]
    side = p['side']
    pos = side if ' ' in side else 'frame-' + side
    outfit = p['outfit'] or L.outfit
    t = p['target']
    extra = (p['extra'] + ', ') if p['extra'] else ''
    if t == 'closed':
        eye = f"{L.pron} eyes {p.get('shut', 'squeezed shut')}"
    else:
        tt = t[4:] if t.startswith('obj:') else t
        eye = f"{L.pron} {p['eyes'] or L.eyes} eyes {p['verb']} {tt}"
    head = f"{L.who} ({L.eth})" if L.eth else L.who
    pose = re.sub(r"\b(?:standing |sitting |leaning )?(?:close |right |just )?behind (her|him)\b", r"beside \1", p['pose'])
    return f"{head} at {pos}, {pose}, {outfit}, {extra}{eye}, {p['expr']}."


def new_person(b, key, label, who, en, zh, core, expr, ref=None, full=False, eth=''):
    """一次写好人物素材的三段文字。who='man'/'woman'；en/zh 是素材描述（写清长相、衣着、特征）；core 是肖像提示词里的外貌短语。"""
    pron = 'He' if who == 'man' else 'She'
    shot = 'full-body' if full else 'half-body'
    same = f"the same {who} as in the reference image" if ref else f"a {eth + ' ' if eth else ''}{who}"
    b.person(key, label, en + ' The portrait fixes identity, clothes and features, not staging.', zh + ' 肖像固定长相、衣着和特征，不固定姿势。',
             f"A photorealistic {shot} portrait of {same}, {core}. {pron} faces the camera with {expr}. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.", ref=ref)


def new_scene(b, key, label, en, zh, holds):
    b.scene(key, label, en + ' The reference fixes the layout and decor.', zh + ' 参考图固定布局与陈设。',
            f"A photorealistic ultra-wide 8:3 cinemascope shot of {en[0].lower() + en[1:].rstrip('.')}, nobody in the scene. The frame holds {holds}.")


def refs(text):
    return re.sub(r'<(\w+)>', lambda m: '[[asset:%s]]' % m.group(1), text)


class Session:
    def __init__(self, base_json, out_name, seed_base, title=None, style=None):
        rev = os.environ.get('H3_REV')      # 修订版模式（2026-10-16）：所有脚本都以这一份 JSON 为底，输出到 合并稿/修订版/，文件名加“修订”
        if rev and base_json is not None:
            base_json = rev
            d_, f_ = os.path.split(out_name)
            out_name = os.path.join(d_, '修订版', f_.replace('_制作稿', '_制作稿_修订', 1))
            os.makedirs(os.path.join(H.CFG['folder'], d_, '修订版'), exist_ok=True)
        self.base, self.out, self.seed_base, self.style = base_json, out_name, seed_base, style
        if base_json is None:      # 新剧第一批：空白底稿
            self.src = {'title': title, 'style': style, 'assets': [], 'characters': {}}
        else:
            self.src = json.load(open(os.path.join(H.CFG['folder'], base_json), encoding='utf-8'))
        self.eps = []          # [(Batch, 集标题, 摘要)]
        self.groups = []       # 站位表分组：同一个地点同一段时间的任务按顺序放一组
        self.prompts = {}
        self.names = {}
        self.cur = None
        self.last_blk = None

    # ---- 素材：每个 Batch 各复制一份底稿，所以新素材要同时加到每个 Batch；统一在 finish 里补到最终文档 ----
    def episode(self, title, summary, ep_no):
        b = Batch(self.base, self.src['title'], self.seed_base + ep_no * 100, style=self.style)
        self.eps.append((b, title, summary))
        self.cur = b
        return b

    def new_assets(self, fn):
        """fn(batch)：在第一个 Batch 上加新素材／人物（Batch.scene/person/prop/character）。最终文档取第一个 Batch 的素材。"""
        fn(self.eps[0][0] if self.eps else None)

    def T(self, tid, title, dur, scene, people, framing, act_en, zh, sound, *, lines=None, cam=FIX, dep=False,
          room=None, enter=(), exit=(), groups=(), bg='', holds=None, st=None, trigger=None, effect=None,
          interrupt=(), new=False, extra_assets=(), speaker_extra=(), vo=()):
        b = self.cur
        cam = safe_cam(cam, len(people))
        if H.CFG.get('cap') and dur > H.CFG['cap']: dur = H.CFG['cap']
        if H.CFG.get('smooth') and lines and not vo:
            lines, dur, act_en, zh = smooth_task(lines, dur, act_en, zh)
        names = {}
        sents, chars, assets = [], [], []
        frame, gaze = {}, {}
        for p in people:
            L = LOOKS[p['lk']]
            names[L.who] = L.who
            sents.append(sentence(p))
            chars.append(L.char)
            assets.append(L.asset)
            frame[L.who] = p['side']
            gaze[L.who] = p['target']
        for g in groups:                           # 群体（长老、宾客）：进站位表，不进人物素材；文字由 bg 写
            frame[g[0]] = g[1]; gaze[g[0]] = g[2]
        act_en = act_en.replace(cam[0], '').strip(); zh = zh.replace(cam[1], '').strip()     # 运镜句只由 cam 参数写一次
        # 每个人在镜头文字里都要有表情（写法检查要求）：没写的，自动补一句 “<x> keeps <开场图里的表情>.”
        vis = refs(act_en)
        tokens = ['[[asset:%s]]' % p['lk'] for p in people]
        span, cur = {t_: '' for t_ in tokens}, None
        for sent in re.split(r'(?<=[.;])\s+', vis):
            hits = [(sent.find(t_), t_) for t_ in tokens if sent.find(t_) >= 0]
            k = min(hits)[1] if hits else cur
            if k: span[k] += ' ' + sent; cur = k
        add = ' '.join(f"{t_} keeps {p['expr']}." for t_, p in zip(tokens, people) if not CUE.search(span[t_]))
        if add: act_en = act_en.rstrip() + ' ' + add
        if H.CFG.get('smooth') and people and not groups:       # 视频文字里也锁人数（2026-10-14：009 的 59 个多人任务只有开场图没有锁，hh 回传的 3 段都多出一个人）
            nm = [LOOKS[p['lk']].who for p in people]
            word = {1: 'One person is', 2: 'Exactly two people are', 3: 'Exactly three people are'}[len(nm)]
            act_en = act_en.rstrip() + f" {word} in the frame: {' and '.join(nm)}, each shown once."
            zh = zh.rstrip() + '画面里恰好是' + '、'.join(nm) + '，每个人只出现一次。'
        n = len(people)
        if holds is None:
            word = {1: 'one person', 2: 'exactly two people', 3: 'exactly three people'}[n]
            holds = f"The frame holds {word}: " + ', '.join(LOOKS[p['lk']].who for p in people) + '.'
        img = framing + ' ' + ' '.join(sents) + ((' ' + bg) if bg else '') + ' ' + holds
        end = (scene.end + scene.layout) if scene else ''
        if scene: ENDS.add(scene.end)
        spoken = []
        says = []
        for sp, tx, start, to in (lines or []):
            spoken.append((LOOKS[sp].char, tx, start))
            says.append((LOOKS[sp].who, to))
        for sp, tx, start, to in vo:                 # 画外音：说话的人不进画面，只出声；对象必须在画面里
            spoken.append((LOOKS[sp].char, tx, start))
            if LOOKS[sp].char not in chars: chars.append(LOOKS[sp].char)
            assert to is None or to in frame, (tid, '画外音的对象不在画面里')
        spoken.sort(key=lambda x: x[2])             # 画外音和画面里的人混排时，按开口时间排
        for x in speaker_extra:
            if x not in chars: chars.append(x)
        for where_, text_ in (('视频', refs(act_en)), ('开场图', img + end)):
            for m_ in BAN_AE.finditer(text_):
                RISK.append((tid, where_, m_.group(0), text_[max(0, m_.start() - 45):m_.end() + 25].replace('\n', ' ')))
        asset_list = ([scene.key] if scene else []) + assets + list(extra_assets)
        if H.CFG.get('cap') and spoken:
            need = max(st_ + H.line_seconds(tx_) + 0.05 for _c, tx_, st_ in spoken) + 1.0
            if need > dur:
                dur = min(13, int(need) + (need > int(need)))      # 放不下：最多放宽到 13 秒（009 里跑过 13 秒）
                print('  [放宽到 %d 秒]' % dur, tid)
        s = b.task(title, dur, chars, asset_list, [scene.key] if scene else [], fixw(img), fixw(end), zh,
                   '0—%d秒，%s' % (dur, cam[1]), None, fixw(refs(act_en)) + ' ' + fixw(cam[0]), zh + ' ' + cam[1], sound, lines=spoken or None)
        s['depends_on_previous'] = dep
        # ---- 站位表 ----
        if new or self.last_blk is None or not self.groups:
            self.groups.append([])
            prev_room = set()
        else:
            prev_room = self.last_blk['room'] - self.last_blk['exit']
        if room is None and len(self.groups[-1]) == 0:
            raise ValueError(f'{tid}: 新场景的第一个任务必须写 room')
        r = set(room) if room is not None else (prev_room | set(enter))
        st_in = {w: v[0] for w, v in (st or {}).items() if v[0] is not None}
        st_out = {w: v[1] for w, v in (st or {}).items() if v[1] is not None}
        blk = B(room=r, frame=frame, gaze=gaze, says=says, enter=set(enter), exit=set(exit), st_in=st_in, st_out=st_out,
                trigger=trigger, effect=effect, interrupt=list(interrupt), nogaze={g[0] for g in groups})
        self.groups[-1].append((tid, blk))
        self.last_blk = blk
        self.prompts[tid] = s['image_prompt']
        self.names.update(names)
        return s

    def finish(self, extra_allow_seeds=()):
        problems = []
        for g in self.groups:
            problems += check(g, self.names, self.prompts)
        if problems:
            print('站位表检查没过：'); [print('  ✗', p) for p in problems]; sys.exit(1)
        print('站位表检查通过：', sum(len(g) for g in self.groups), '个任务')
        doc = copy.deepcopy(self.eps[0][0].d)
        # 所有 Batch 加的新素材取并集（按 key 去重）
        have = {a['key'] for a in doc['assets']}
        for b, _, _ in self.eps[1:]:
            for a in b.d['assets']:
                if a['key'] not in have: doc['assets'].append(a); have.add(a['key'])
            for k, c in b.d['characters'].items():
                doc['characters'].setdefault(k, c)
        doc['episodes'] = []
        for b, title, summary in self.eps:
            out = []
            for i_, t in enumerate(b.tasks, 1):      # 拆出插入镜头后编号要连续
                t['title'] = '%02d｜' % i_ + t['title'].split('｜', 1)[1]
                out.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
                for x in t['dialogue']:
                    out.append(f"{x['speaker']}：“{x['text']}”")
            doc['episodes'].append({'title': title, 'summary': summary, 'script': '\n'.join(out), 'segments': b.tasks, 'dialogue_language': H.CFG['lang']})
        # 素材键必须都存在
        akeys = {a['key'] for a in doc['assets']}
        for e in doc['episodes']:
            for s in e['segments']:
                for k in s['asset_keys']: assert k in akeys, (s['title'], k)
                for c in s['characters']: assert c in doc['characters'], (s['title'], c)
        # 种子不重复
        seen = set()
        folder = os.path.join(H.CFG['folder'], '合并稿')
        for sub in ('', '旧合并稿'):
            d_ = os.path.join(folder, sub)
            if not os.path.isdir(d_): continue
            for fn in os.listdir(d_):
                if fn.endswith('.json') and not fn.startswith(os.path.basename(self.out)[:4]):
                    try:
                        dd = json.load(open(os.path.join(d_, fn), encoding='utf-8'))
                        for e in dd['episodes']:
                            for s in e['segments']: seen.add(s['seed'])
                    except Exception:
                        pass
        mine = [s['seed'] for e in doc['episodes'] for s in e['segments']]
        assert len(set(mine)) == len(mine) or H.CFG.get('fixed_seed'), '本稿内种子重复'
        clash = sorted(x for x in set(mine) if x in seen and x not in extra_allow_seeds)
        assert not clash or H.CFG.get('fixed_seed'), f'与库里已有种子重复：{clash}'
        txt = json.dumps(doc, ensure_ascii=False, indent=1)
        open(os.path.join(H.CFG['folder'], self.out + '.json'), 'w', encoding='utf-8').write(txt)
        open(os.path.join(H.CFG['folder'], self.out + '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(txt)
        n = len(mine); sec = sum(s['duration_seconds'] for e in doc['episodes'] for s in e['segments'])
        if os.environ.get('H3_DUMP_END'):
            open(os.environ['H3_DUMP_END'], 'a', encoding='utf-8').write('\n'.join(sorted(ENDS)) + '\n')
        if RISK:
            import collections
            cnt = collections.Counter((w_, k_.lower()) for _t, w_, k_, _c in RISK)
            print('仍留在文字里的光边／闪光／热气类词（视频文字／开场图文字，词：次数）：', dict(cnt.most_common(20)))
            for _t, w_, k_, c_ in RISK[:200]:
                if w_ == '视频': print('   ', _t, w_, '…' + c_ + '…')
        print(f'{len(doc["episodes"])} 集、{n} 个任务、约 {sec} 秒；文件 {len(txt.encode())/1024:.0f} KB → {self.out}')
        for e in doc['episodes']:
            print('  ', e['title'], len(e['segments']), '个任务', sum(s['duration_seconds'] for s in e['segments']), '秒')
        return doc
