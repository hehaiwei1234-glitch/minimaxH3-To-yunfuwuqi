"""《极寒末日》第 55–74 集（021 起）共用工具（2026-10-15 夜，hh 挂机：20 集，A／B 两种写法按剧情混用）。
A＝正常快慢版：对白任务 12–15 秒，句从 0.6 秒起、句间 0.9 秒，结尾带动作。
B＝短剧快速版：句从 0.4 秒起、句间 0.2 秒、语速快两成写进文字、现场音写响；任务仍可到 15 秒，塞更多短句（hh 18:36 说 15 秒多塞内容效果更好）。
同一集里可以随时切换：先 mode('A') 或 mode('B')，再写任务。声音要用本模块的 V()／Q()（切到 B 之后才会写响）。
用法：生成脚本里  `import _jihan_base7 as B7; from _jihan_base7 import *`，再 `B7.S = B6.S = Session(...)`。
"""
import math, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
from _jihan_base6 import *
import _h3draft as _H
import _voiceins as VI
import _scene
from _scene import smooth_text, TONE_FIX, new_person, new_scene, Scene, P, look, LOOKS
from _h3draft import breathy, voiced

S = None
MODE = {'m': 'A'}
GAPM = {'A': 0.9, 'B': 0.2}
STARTM = {'A': 0.6, 'B': 0.4}
TAILM = {'A': 2.0, 'B': 1.5}
MINM = {'A': 6, 'B': 5}
BRISK_A_EN = ' The lines follow one another at once with only a very short breath between them, each said in one breath with no pause inside the sentence.'
BRISK_A_ZH = ' 台词一句紧接着一句，中间只有很短的换气，每句一口气说完、句中不停顿。'
BRISK_B_EN = BRISK_A_EN + ' The dialogue is delivered at a fast, snappy pace, about twenty percent quicker than normal speech, with no lingering pauses.'
BRISK_B_ZH = BRISK_A_ZH + ' 台词语速偏快利落，比平常说话快两成左右，没有拖沓的停顿。'
USED = {'A': 0, 'B': 0}


def mode(m):
    MODE['m'] = m
    _H.CFG['sfx_loud'] = (m == 'B')


def V(en, zh):
    return voiced(en, zh)


def Q(en, zh):
    return breathy(en, zh)


def times(spec):
    m = MODE['m']
    out, t = [], STARTM[m]
    for sp, tx, to in spec:
        tx2 = smooth_text(tx)
        out.append((sp, tx2, round(t, 2), to))
        t = t + _H.line_seconds(tx2) + GAPM[m]
    return out


def _retime(lines, dur, act_en, zh):
    """S.T 里会再调一次：只重排时间，文字已由 DL 写好，不再重复添加。"""
    return times([(a, b, d) for a, b, c, d in lines]), dur, act_en, zh


_scene.smooth_task = _retime

ORD = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
ORD_ZH = ['第一句', '第二句', '第三句', '第四句', '第五句', '第六句', '第七句']
ZN = VI.ZN
ZN.update({'su_cozy': '苏清月', 'lin_home': '林峰', 'su_arctic': '苏清月', 'lin_arctic': '林峰', 'su_surgeon': '苏清月', 'su_tac': '苏清月',
      'lin_work': '林峰', 'lin_white': '林峰', 'eden_voice': '伊甸', 'ning_partner': '周宁'})
VOICE_ONLY = {'eden_voice'}
VD = VI.VD
REPORT = []
FAILS = []


def who(a):
    return LOOKS[a].who


def _a(w):
    return ('an ' if w[:1].lower() in 'aeiou' else 'a ') + w


def _dl_one(tid, title, scene, people, framing, spec, sound, aes, pre_en='', pre_zh='', post_en='', post_zh='', tail=None, mind=None, dur=None, cam=None, vd=None, ld=None, **kw):
    """对白任务（一个任务，说话人都在画面里；ISOLATE 关掉时也用于“只有声音”的台词）。spec = [(说话人素材键, 台词, 对谁说的素材键, 英语语气, 中文语气)]。
    说话人／对象都在画面里：普通台词；说话人＝对象：自言自语（走旁白通道）；
    说话人不在画面里（伊甸、收音机、耳机里的人）：画外音，需要在 vd 或模块里的 VD 给“声音从哪来”的描述（英文，中文）；
    对象不在画面里（对着耳机麦克风、对着墙上的扬声器说）：在 ld 里给“朝向哪”的描述（英文，中文），站位表按“对自己”处理，走旁白通道。"""
    m = MODE['m']
    tail = TAILM[m] if tail is None else tail
    mind = MINM[m] if mind is None else mind
    vdd = dict(VD, **(vd or {}))
    ldd = dict(ld or {})
    onscreen = [p['lk'] for p in people]
    timed = times([(a, t, None) for a, t, c, te, tz in spec])
    lines, vo = [], []
    parts_en, parts_zh = [], []
    for i, ((a, t, c, te, tz), (sp, tx, st, _)) in enumerate(zip(spec, timed)):
        lead = 'then ' if i else ''
        lead_zh = '接着' if i else ''
        a_off = (a in VOICE_ONLY) or (a not in onscreen)
        c_off = (c in VOICE_ONLY) or (c not in onscreen and c != a)
        assert not (a_off and c_off), (tid, '说话人和对象都不在画面里', a, c)
        if a == c:
            to_blk = who(a)
            tgt_en, tgt_zh = ('herself aloud' if LOOKS[a].pron == 'her' else 'himself aloud'), '自己低声'
        elif c_off:
            to_blk = who(a)
            if c in ldd: tgt_en, tgt_zh = ldd[c]
            else:
                _s = SRC[src_of(c)[0]]
                tgt_en, tgt_zh = 'toward ' + _s['obj_en'], '朝着' + _s['obj_zh']
        else:
            to_blk = who(c)
            tgt_en, tgt_zh = f'<{c}>', ZN.get(c, who(c))
        entry = (a, tx, st, to_blk)
        if a_off or a == c or c_off:
            vo.append(entry)
        else:
            lines.append(entry)
        if a_off:
            parts_en.append(f"{lead}{vdd[a][0]} speaks the {ORD[i]} line as a voice-over to <{c}> in {_a(te)} voice")
            parts_zh.append(f"{lead_zh}{vdd[a][1]}以旁白的方式对{ZN.get(c, who(c))}用{tz}的声音说出{ORD_ZH[i]}")
        else:
            if c_off:
                parts_en.append(f"{lead}<{a}> speaks the {ORD[i]} line {tgt_en} in {_a(te)} voice")
            else:
                parts_en.append(f"{lead}<{a}> speaks the {ORD[i]} line to {tgt_en} in {_a(te)} voice")
            parts_zh.append(f"{lead_zh}{ZN.get(a, who(a))}用{tz}的声音{'对' if not c_off else ''}{tgt_zh}说出{ORD_ZH[i]}")
    last = timed[-1]
    end = last[2] + _H.line_seconds(last[1])
    d = dur or max(mind, min(15, math.ceil(end + tail)))
    d = max(d, {2: 6, 3: 7, 4: 8}.get(len(spec), 0)) if len(spec) > 1 else d      # 写法检查：2 句 ≥6 秒、3 句 ≥7 秒、4 句 ≥8 秒
    if post_en and not post_en.rstrip().endswith('.'): post_en = post_en.rstrip() + '.'
    if post_zh and not post_zh.rstrip().endswith('。'): post_zh = post_zh.rstrip() + '。'
    if end + 1.06 > d or d > 15:
        FAILS.append(f'{tid}: 最后一句说完约 {end:.1f} 秒，放不进 15 秒任务（要 ≤13.9）——台词太长或句数太多')
        return None
    brisk_en, brisk_zh = (BRISK_B_EN, BRISK_B_ZH) if m == 'B' else (BRISK_A_EN, BRISK_A_ZH)
    act_en = (pre_en + ' ' if pre_en else '') + ', '.join(parts_en) + ('; ' + post_en if post_en else '.') + brisk_en
    zh = (pre_zh if pre_zh else '') + '，'.join(parts_zh) + ('；' + post_zh if post_zh else '。') + brisk_zh
    REPORT.append((tid, m, d, round(end, 1), len(spec)))
    USED[m] += d
    if cam is None: cam = push('both of them', '两人') if len(people) > 1 else push1('the face', '脸')
    room = kw.pop('room', None) or {who(p) for p in onscreen}
    return B6.TA(tid, title, d, scene, people, framing, act_en, zh, sound, aes, cam=cam, room=room, new=kw.pop('new', True),
                 lines=lines or None, vo=vo or (), **kw)


# ---------------------------------------------------------------------------------------------- “只有声音”的台词：单独拍插镜（2026-10-16）
# hh 10-16：“系统播报几乎 100% 是女主说话，除非女主在播报时不出镜”“收音机里的男声让女主张嘴＋多出一个人”。
# 原因（已有记录：规律 2“对白栏里的字一律当作某个人在说”，自查清单 55，但我把“画外音”当成了常规写法）：
#   台词一进对白栏，H3 就把它配给画面里的某张脸（女声配给女主的嘴），画面里没脸可配时还会凭空多画一个人。
# 办法：伊甸、收音机、耳机、录音这类“只有声音”的台词，单独放在不带人的插镜里（只拍音箱／收音机／耳机），
# 声音出来的那几秒画面里没有任何一张脸；人物的反应和回话放在前后的任务里。
ISOLATE = True
ISLAND = True
SPLITS = []
SRC, VPH, src_of = VI.SRC, VI.VPH, VI.src_of
ZN.update(VI.ZN)


def _voice_insert(tid, run, scene, sound, room, new, cam=None, mind=None, tail=None):
    """一段连续的“只有声音”的台词 → 一个不带人的插镜：只拍声音的来源（音箱／收音机／耳机），声音在这几秒里出来。"""
    m = MODE['m']
    brisk = (BRISK_B_EN, BRISK_B_ZH) if m == 'B' else (BRISK_A_EN, BRISK_A_ZH)
    r, d, end = VI.insert(S, tid, run, scene, sound, room, new, times, brisk=brisk, cam=cam)
    REPORT.append((tid, m, d, round(end, 1), len(run)))
    USED[m] += d
    return r


def _clean_r(t):
    """反应任务的文字：去掉“说完最后一句之后”这类指向别的任务的话，首字母大写，句末加句号。"""
    t = re.sub(r'(?i)\b(?:after|once|when) the (?:last|final|first|second|third) line,?\s*', '', t.strip())
    t = t[:1].upper() + t[1:] if t else t
    return t + ('' if not t or t.endswith('.') else '.')


def _unvoice(snd):
    """没有台词的任务不能写“人声清楚”（H11）：改成“没有人说话”的声音写法。"""
    en, zh = snd
    if en.endswith(' Voices stay close and clear.'):
        en = en[:-len(' Voices stay close and clear.')] + ' ' + _H.NOWORD_EN
        zh = zh[:-len('人声近而清楚。')] + _H.NOWORD_ZH
    elif en.endswith(' The voices are clear.'):
        en = en[:-len(' The voices are clear.')].replace(' ' + _H.LOUD_EN, ' ' + _H.NOWORD_EN + ' ' + _H.LOUD_EN)
        zh = zh[:-len('人声清楚。')].replace(_H.LOUD_ZH, _H.NOWORD_ZH + _H.LOUD_ZH)
    return en, zh


def DL(tid, title, scene, people, framing, spec, sound, aes, pre_en='', pre_zh='', post_en='', post_zh='', tail=None, mind=None, dur=None, cam=None, vd=None, ld=None, **kw):
    """对白任务。spec 里如果有“只有声音”的台词（伊甸、收音机、耳机、录音），自动拆开：这些台词放进不带人的插镜，
    有人说话的台词仍放在人物任务里（没有这条拆法时，声音会被配给画面里的脸）。"""
    onscreen = [p['lk'] for p in people]
    def off(a): return (a in VOICE_ONLY) or (a not in onscreen)
    if not ISOLATE or not any(off(e[0]) for e in spec):
        return _dl_one(tid, title, scene, people, framing, spec, sound, aes, pre_en, pre_zh, post_en, post_zh, tail, mind, dur, cam, vd, ld, **kw)
    runs = []
    def hs(a):
        try: return src_of(a)[0] == 'headset'
        except KeyError: return False
    idx_off = [i for i, e in enumerate(spec) if off(e[0])]
    if ISLAND and len(idx_off) >= 2 and all(hs(e[0]) for e in spec[idx_off[0]:idx_off[-1] + 1]):
        # 耳机里的一问一答（两边都是耳机里的声音）：从第一句“只有声音”的到最后一句，合成一个（太长就分几个）插镜，
        # 不然一个字的接话（“再等。”“还不够。”）也要拆成一个 4–5 秒的小任务，一集会碎成二十多个镜头。
        lo, hi = idx_off[0], idx_off[-1]
        if lo > 0: runs.append((('P', None), list(spec[:lo])))
        cur = []
        for e in spec[lo:hi + 1]:
            t = times([(a, tx, None) for a, tx, c, te, tz in cur + [e]])
            if cur and t[-1][2] + _H.line_seconds(t[-1][1]) + 1.06 > 12:
                runs.append((('V', 'island'), cur)); cur = []
            cur.append(e)
        runs.append((('V', 'island'), cur))
        if hi + 1 < len(spec): runs.append((('P', None), list(spec[hi + 1:])))
    else:
        for e in spec:
            kind = ('V', src_of(e[0])[1]) if off(e[0]) else ('P', None)
            if runs and runs[-1][0] == kind: runs[-1][1].append(e)
            else: runs.append((kind, [e]))
    if not any(k[0] == 'P' for k, _ in runs):
        runs.append((('R', None), []))                     # 全是声音：人物在画面外听不行，补一个人物的反应任务放在声音之后
    pidx = [j for j, (k, _) in enumerate(runs) if k[0] in 'PR']
    room0 = set(kw.pop('room', None) or {who(p) for p in onscreen})
    new0 = kw.pop('new', True)
    exits = set(kw.get('exit', ()))
    assert not kw.get('enter') and not kw.get('trigger') and not kw.get('effect'), (tid, '这个任务有进场／引发动作，拆开前先手工处理')
    st = kw.pop('st', None)
    ex_assets = tuple(x for x in kw.pop('extra_assets', ()) if x not in ('hack_screen', 'radio_set'))
    out = []
    SPLITS.append((tid, ''.join(k[0] for k, _ in runs)))
    for j, ((k, _k2), run) in enumerate(runs):
        new = new0 if j == 0 else False
        last_p = pidx[-1]
        room = room0 if j <= last_p else room0 - exits
        if k == 'V':
            out.append(_voice_insert(f'{tid}v{j}', run, scene, sound, room, new, mind=mind, tail=tail))
            continue
        kw_p = dict(kw)
        if j != last_p: kw_p.pop('exit', None)
        if st:
            if len(pidx) == 1: kw_p['st'] = st
            elif j == pidx[0]: kw_p['st'] = {w: (v[0], None) for w, v in st.items()}
            elif j == last_p: kw_p['st'] = {w: (None, v[1]) for w, v in st.items()}
        if ex_assets: kw_p['extra_assets'] = ex_assets
        first_p, final_p = j == pidx[0], j == last_p
        ttl = title if first_p else title + ('（反应）' if k == 'R' else '（续）')
        if k == 'R':
            names_en = ' and '.join(f"<{p['lk']}>" for p in people)
            pe = _clean_r((pre_en + ' ' + post_en).strip()) or ' '.join(f"{('<%s>' % p['lk'])} listens in silence." for p in people)
            pz = (pre_zh + post_zh).strip() or ''.join(f"{ZN.get(p['lk'], who(p['lk']))}静静地听着。" for p in people)
            if pz and not pz.endswith('。'): pz += '。'
            USED[MODE['m']] += (dur or 6)
            REPORT.append((f'{tid}p{j}', MODE['m'], dur or 6, 0, 0))
            out.append(B6.TA(f'{tid}p{j}', ttl, dur or 6, scene, people, framing, pe, pz, _unvoice(sound), aes, cam=cam or push('both of them', '两人') if len(people) > 1 else cam or push1('the face', '脸'),
                             room=room, new=new, **kw_p))
            continue
        out.append(_dl_one(tid if first_p else f'{tid}p{j}', ttl, scene, people, framing, run, sound, aes,
                           pre_en if first_p else '', pre_zh if first_p else '', post_en if final_p else '', post_zh if final_p else '',
                           tail, mind, dur if len(pidx) == 1 else None, cam, vd, ld, room=room, new=new, **kw_p))
    return out


def TAA(tid, title, dur, scene, people, framing, act_en, zh, sound, aes, **kw):
    """没有台词的任务（一个人做一件事）。"""
    kw.setdefault('room', {who(p['lk']) for p in people})
    kw.setdefault('new', True)
    USED[MODE['m']] += dur
    REPORT.append((tid, MODE['m'], dur, 0, 0))
    return B6.TA(tid, title, dur, scene, people, framing, act_en, zh, sound, aes, **kw)


def INS(tid, title, dur, scene, framing, act_en, zh, snd, holds, cam, aes, **kw):
    USED[MODE['m']] += dur
    REPORT.append((tid, MODE['m'], dur, 0, 0))
    return B6.insert2(tid, title, dur, scene, framing, act_en, zh, snd, holds, cam, aes, **kw)


def arc(who_en, who_zh, to_en, to_zh):
    return (f'The camera arcs slowly around {who_en} toward frame-right until {to_en}.', f'镜头缓缓绕着{who_zh}向右环绕，直到{to_zh}。')


def report():
    if FAILS:
        print('台词放不下：'); [print('  ✗', f) for f in FAILS]; sys.exit(1)
    print('\n'.join(f'{t} [{m}] 任务 {d} 秒，最后一句约 {e} 秒，{n} 句' for t, m, d, e, n in REPORT))
    print('A 写法合计', USED['A'], '秒；B 写法合计', USED['B'], '秒')
    if SPLITS: print('只有声音的台词已拆成插镜：', ', '.join(f'{x}({k})' for x, k in SPLITS), '（V＝只拍声音来源的插镜，P＝有人说话的任务，R＝补的人物反应任务）')


# ---------------------------------------------------------------------------------------------- 本模块补充的外貌（别的脚本里定义过、但不在公共底座里的）
look('eden_voice', 'Eden', "a flat wall speaker panel with a thin blue ring", 'none', 'its')
look('su_arctic', 'SuArctic', "in a bulky pure-white polar expedition suit with the hood up, white goggles pushed up on her forehead and a white neck gaiter pulled down under her chin, a few strands of black hair at her temples, frost on her lashes", 'sharp dark-brown', 'her', eth=CN_F28)
SU_SHIRT = "in an oversized crisp white men's dress shirt with the sleeves rolled, the hem reaching mid-thigh, bare legs and bare feet, her long black hair loose and tousled"
LIN_PJ = "in a loose light-grey cotton sleep shirt and soft grey pyjama trousers, barefoot, his black hair slightly messy from sleep"
