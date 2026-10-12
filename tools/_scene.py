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
from _h3draft import Batch, FOLDER, IMG, breathy, voiced
from _blocking import B, check

FIX = ('The camera holds still.', '镜头固定不动。')
CUE = re.compile(r"lips?|mouth|jaw|brows?|tears?|frown|glar|scowl|narrow|expression|wince|grimace|smirk|smil|pale|stern|cold|blank|clench|tighten|wide eyes|eyes (?:\w+ )?wide|eyes (?:widen|shut|close|lower)|glisten|shine|bite|bites|quiver|tremble", re.I)
LOOKS = {}


class Look:
    def __init__(self, asset, char, outfit, eyes, pron):
        self.asset, self.char, self.outfit, self.eyes, self.pron = asset, char, outfit, eyes, pron
        self.who = asset.split('_')[0].capitalize()          # 和 lint_draft 的取名规则一致


def look(asset, char, outfit, eyes, pron):
    LOOKS[asset] = Look(asset, char, outfit, eyes, pron)


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
    return f"{L.who} at {pos}, {p['pose']}, {outfit}, {extra}{eye}, {p['expr']}."


def new_person(b, key, label, who, en, zh, core, expr, ref=None, full=False):
    """一次写好人物素材的三段文字。who='man'/'woman'；en/zh 是素材描述（写清长相、衣着、特征）；core 是肖像提示词里的外貌短语。"""
    pron = 'He' if who == 'man' else 'She'
    shot = 'full-body' if full else 'half-body'
    same = f"the same {who} as in the reference image" if ref else f"a {who}"
    b.person(key, label, en + ' The portrait fixes identity, clothes and features, not staging.', zh + ' 肖像固定长相、衣着和特征，不固定姿势。',
             f"A photorealistic {shot} portrait of {same}, {core}. {pron} faces the camera with {expr}. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.", ref=ref)


def new_scene(b, key, label, en, zh, holds):
    b.scene(key, label, en + ' The reference fixes the layout and decor.', zh + ' 参考图固定布局与陈设。',
            f"A photorealistic ultra-wide 8:3 cinemascope shot of {en[0].lower() + en[1:].rstrip('.')}, nobody in the scene. The frame holds {holds}.")


def refs(text):
    return re.sub(r'<(\w+)>', lambda m: '[[asset:%s]]' % m.group(1), text)


class Session:
    def __init__(self, base_json, out_name, seed_base):
        self.base, self.out, self.seed_base = base_json, out_name, seed_base
        self.src = json.load(open(os.path.join(FOLDER, base_json), encoding='utf-8'))
        self.eps = []          # [(Batch, 集标题, 摘要)]
        self.groups = []       # 站位表分组：同一个地点同一段时间的任务按顺序放一组
        self.prompts = {}
        self.names = {}
        self.cur = None
        self.last_blk = None

    # ---- 素材：每个 Batch 各复制一份底稿，所以新素材要同时加到每个 Batch；统一在 finish 里补到最终文档 ----
    def episode(self, title, summary, ep_no):
        b = Batch(self.base, self.src['title'], self.seed_base + ep_no * 100)
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
        n = len(people)
        if holds is None:
            word = {1: 'one person', 2: 'exactly two people', 3: 'exactly three people'}[n]
            holds = f"The frame holds {word}: " + ', '.join(LOOKS[p['lk']].who for p in people) + '.'
        img = framing + ' ' + ' '.join(sents) + ((' ' + bg) if bg else '') + ' ' + holds
        end = (scene.end + scene.layout) if scene else ''
        spoken = []
        says = []
        for sp, tx, start, to in (lines or []):
            spoken.append((LOOKS[sp].char, tx, start))
            says.append((LOOKS[sp].who, to))
        for sp, tx, start, to in vo:                 # 画外音：说话的人不进画面，只出声；对象必须在画面里
            spoken.append((LOOKS[sp].char, tx, start))
            if LOOKS[sp].char not in chars: chars.append(LOOKS[sp].char)
            assert to in frame, (tid, '画外音的对象不在画面里')
        for x in speaker_extra:
            if x not in chars: chars.append(x)
        asset_list = ([scene.key] if scene else []) + assets + list(extra_assets)
        s = b.task(title, dur, chars, asset_list, [scene.key] if scene else [], img, end, zh,
                   '0—%d秒，%s' % (dur, cam[1]), None, refs(act_en) + ' ' + cam[0], zh + ' ' + cam[1], sound, lines=spoken or None)
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
            for t in b.tasks:
                out.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
                for x in t['dialogue']:
                    out.append(f"{x['speaker']}：“{x['text']}”")
            doc['episodes'].append({'title': title, 'summary': summary, 'script': '\n'.join(out), 'segments': b.tasks, 'dialogue_language': 'en'})
        # 素材键必须都存在
        akeys = {a['key'] for a in doc['assets']}
        for e in doc['episodes']:
            for s in e['segments']:
                for k in s['asset_keys']: assert k in akeys, (s['title'], k)
                for c in s['characters']: assert c in doc['characters'], (s['title'], c)
        # 种子不重复
        seen = set()
        folder = os.path.join(FOLDER, '合并稿')
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
        assert len(set(mine)) == len(mine), '本稿内种子重复'
        clash = sorted(x for x in set(mine) if x in seen and x not in extra_allow_seeds)
        assert not clash, f'与库里已有种子重复：{clash}'
        txt = json.dumps(doc, ensure_ascii=False, indent=1)
        open(os.path.join(FOLDER, self.out + '.json'), 'w', encoding='utf-8').write(txt)
        open(os.path.join(FOLDER, self.out + '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(txt)
        n = len(mine); sec = sum(s['duration_seconds'] for e in doc['episodes'] for s in e['segments'])
        print(f'{len(doc["episodes"])} 集、{n} 个任务、约 {sec} 秒；文件 {len(txt.encode())/1024:.0f} KB → {self.out}')
        for e in doc['episodes']:
            print('  ', e['title'], len(e['segments']), '个任务', sum(s['duration_seconds'] for s in e['segments']), '秒')
        return doc
