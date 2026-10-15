"""《极寒末日》第 55–74 集（021 起）共用工具（2026-10-15 夜，hh 挂机：20 集，A／B 两种写法按剧情混用）。
A＝正常快慢版：对白任务 12–15 秒，句从 0.6 秒起、句间 0.9 秒，结尾带动作。
B＝短剧快速版：句从 0.4 秒起、句间 0.2 秒、语速快两成写进文字、现场音写响；任务仍可到 15 秒，塞更多短句（hh 18:36 说 15 秒多塞内容效果更好）。
同一集里可以随时切换：先 mode('A') 或 mode('B')，再写任务。声音要用本模块的 V()／Q()（切到 B 之后才会写响）。
用法：生成脚本里  `import _jihan_base7 as B7; from _jihan_base7 import *`，再 `B7.S = B6.S = Session(...)`。
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
from _jihan_base6 import *
import _h3draft as _H
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
ZN = {'su_cozy': '苏清月', 'lin_home': '林峰', 'su_arctic': '苏清月', 'lin_arctic': '林峰', 'su_surgeon': '苏清月', 'su_tac': '苏清月',
      'lin_work': '林峰', 'lin_white': '林峰', 'eden_voice': '伊甸', 'ning_partner': '周宁'}
VOICE_ONLY = {'eden_voice'}
VD = {'eden_voice': ('the soft, calm, polite female synthetic voice from the flat wall speaker panel with the thin glowing blue ring', '墙上那块带着一圈细细蓝光的扁扁的扬声器里传出的轻柔平静、礼貌的女性合成声音')}
REPORT = []
FAILS = []


def who(a):
    return LOOKS[a].who


def DL(tid, title, scene, people, framing, spec, sound, aes, pre_en='', pre_zh='', post_en='', post_zh='', tail=None, mind=None, dur=None, cam=None, vd=None, ld=None, **kw):
    """对白任务。spec = [(说话人素材键, 台词, 对谁说的素材键, 英语语气, 中文语气)]。
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
            tgt_en, tgt_zh = ldd[c] if c in ldd else ('toward ' + VD[c][0], '朝着' + VD[c][1] + '所在的墙面')
        else:
            to_blk = who(c)
            tgt_en, tgt_zh = f'<{c}>', ZN.get(c, who(c))
        entry = (a, tx, st, to_blk)
        if a_off or a == c or c_off:
            vo.append(entry)
        else:
            lines.append(entry)
        if a_off:
            parts_en.append(f"{lead}{vdd[a][0]} speaks the {ORD[i]} line as a voice-over to <{c}> in a {te} voice")
            parts_zh.append(f"{lead_zh}{vdd[a][1]}以旁白的方式对{ZN.get(c, who(c))}用{tz}的声音说出{ORD_ZH[i]}")
        else:
            if c_off and isinstance(tgt_en, str) and not tgt_en.startswith('toward'):
                parts_en.append(f"{lead}<{a}> speaks the {ORD[i]} line {tgt_en} in a {te} voice")
            else:
                parts_en.append(f"{lead}<{a}> speaks the {ORD[i]} line to {tgt_en} in a {te} voice")
            parts_zh.append(f"{lead_zh}{ZN.get(a, who(a))}用{tz}的声音{'对' if not c_off else ''}{tgt_zh}说出{ORD_ZH[i]}")
    last = timed[-1]
    end = last[2] + _H.line_seconds(last[1])
    d = dur or max(mind, min(15, math.ceil(end + tail)))
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


# ---------------------------------------------------------------------------------------------- 本模块补充的外貌（别的脚本里定义过、但不在公共底座里的）
look('eden_voice', 'Eden', "a flat wall speaker panel with a thin glowing blue ring", 'none', 'its')
look('su_arctic', 'SuArctic', "in a bulky pure-white polar expedition suit with the hood up, white goggles pushed up on her forehead and a white neck gaiter pulled down under her chin, a few strands of black hair at her temples, frost on her lashes", 'sharp dark-brown', 'her', eth=CN_F28)
SU_SHIRT = "in an oversized crisp white men's dress shirt with the sleeves rolled, the hem reaching mid-thigh, bare legs and bare feet, her long black hair loose and tousled"
LIN_PJ = "in a loose light-grey cotton sleep shirt and soft grey pyjama trousers, barefoot, his black hair slightly messy from sleep"
