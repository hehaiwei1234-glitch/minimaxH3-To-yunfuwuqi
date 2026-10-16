"""“只有声音”的台词（伊甸、收音机、耳机、录音）→ 不带人的插镜（2026-10-16，hh 反馈：系统播报几乎 100% 被配给女主的嘴）。
原因（已有记录：规律 2“对白栏里的字一律当作某个人在说”、自查清单 55）：台词一进对白栏，H3 就把它配给画面里的某张脸
（女声配给女主的嘴），画面里没有脸可配时还会凭空多画一个人（收音机里的男声让女主张嘴＋多出一个人）。
办法：这类台词单独放在不带人的插镜里（只拍音箱／收音机／耳机／控制台屏幕），声音出来的那几秒画面里没有任何一张脸；
人物的反应和回话放在前后的任务里。

本模块不依赖 _jihan_base7，018–020 这类手写脚本和 021 起的 DL() 都能用：
    import _voiceins as VI
    VI.insert(S, tid, run, scene, sound, room, new, timer=..., brisk=(en, zh), mode_label='A')
run = [(说话人 look 键, 台词, None, 英语语气, 中文语气), ...]，timer(spec)->[(sp, 台词, 开口秒, to)]。
"""
import math, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _h3draft as _H
import _scene
from _scene import look
from _jihan_base import push1

ORD = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
ORD_ZH = ['第一句', '第二句', '第三句', '第四句', '第五句', '第六句', '第七句']
VD = {'eden_voice': ('the soft, calm, polite female synthetic voice from the flat wall speaker panel with the thin blue ring', '墙上那块带着一圈细细蓝圈的扁扁的扬声器里传出的轻柔平静、礼貌的女性合成声音'),
      'k_rec': ("the manic cracked young man's recorded voice from the console speaker", '控制台扬声器里传出的、疯狂发破的年轻男人的录音'),
      'radio_cmd': ("the stern, cold, authoritative middle-aged man's voice crackling out of the olive-green military radio", '从橄榄绿军用收音机里沙沙传出的威严冰冷的中年男声'),
      'ghost_voice': ('the flat, cold, androgynous synthetic voice from the small round speaker grille beside the screen', '屏幕旁边的小圆扬声器里传出的、平板冰冷、听不出男女的合成声音')}
ZN = {'radio_cmd': '指挥官', 'stranger_radio': '陌生人', 'k_rec': '黑客K', 'lin_rec': '林峰（录音）', 'radio_ning': '周宁', 'radio_pei': '裴远山', 'eden_voice': '伊甸', 'ghost_voice': '合成声音'}
SPLITS = []

SRC = {
    'eden': dict(obj_en='a flat round white speaker panel with a thin blue ring around it', obj_zh='一块扁扁的圆形白色扬声器面板，周围一圈细细的蓝圈',
                 layout=' Fixed stage layout: a close view of a flat round white speaker panel with a thin blue ring around it, set into the pale wall in the middle of the frame; the room beyond is a soft blur; nobody is in the scene.',
                 assets=('hack_screen',), title_zh='墙上的扬声器', cam_en='the speaker panel', cam_zh='扬声器面板'),
    'krec': dict(obj_en='a wide black console screen showing a jagged red audio waveform', obj_zh='一块宽宽的黑色控制台屏幕，上面是一条锯齿状的红色声波',
                 layout=' Fixed stage layout: a close view of a wide black console screen showing a jagged red audio waveform fills the middle of the frame; a small round speaker grille sits beside it; the room beyond is a soft blur; nobody is in the scene.',
                 assets=('hack_screen',), title_zh='控制台屏幕', cam_en='the console screen', cam_zh='控制台屏幕'),
    'ghost': dict(obj_en='a wide black console screen covered in rows of tiny green characters, with a small round speaker grille beside it', obj_zh='一块宽宽的黑色控制台屏幕，上面是一行行小小的绿色字符，旁边有一个圆形的小扬声器',
                  layout=' Fixed stage layout: a close view of a wide black console screen covered in rows of tiny green characters fills the middle of the frame, a small round speaker grille sits beside it; the room beyond is a soft blur; nobody is in the scene.',
                  assets=('hack_screen',), title_zh='控制台屏幕', cam_en='the console screen', cam_zh='控制台屏幕'),
    'radio': dict(obj_en='the olive-green military long-wave radio with a round tuning dial and a cloth speaker grille, standing on a steel side table', obj_zh='钢桌上那台橄榄绿的军用长波收音机，带着圆形调谐盘和布面扬声器',
                  layout=' Fixed stage layout: a close view of the olive-green military long-wave radio on a steel side table fills the middle of the frame, its round tuning dial, a pole antenna and a cloth speaker grille clearly visible; the room beyond is a soft blur; nobody is in the scene.',
                  assets=('radio_set',), title_zh='收音机', cam_en='the radio', cam_zh='收音机'),
    'belt': dict(obj_en='a small olive handheld field radio with a short antenna, clipped to a belt', obj_zh='别在腰带上的一台橄榄绿小型手持收音机，带一根短天线',
                 layout=' Fixed stage layout: a close view of a small olive handheld field radio with a short antenna clipped to a worn belt fills the middle of the frame; a fold of grey waterproof jacket and a blur of dark ice are behind it; nobody is in the scene.',
                 assets=('radio_set',), title_zh='腰间的收音机', cam_en='the field radio', cam_zh='手持收音机'),
    'headset': dict(obj_en='a slim black communications headset with a short boom microphone, lying on a steel console desk', obj_zh='放在钢制控制台上的一副黑色细耳机，带一根短短的麦克风杆',
                    layout=' Fixed stage layout: a close view of a slim black communications headset with a short boom microphone, lying on a steel console desk in the middle of the frame; the room beyond is a soft blur; nobody is in the scene.',
                    assets=('headset',), title_zh='耳机', cam_en='the headset', cam_zh='耳机'),
}
VPH = {'su': ("a low smooth woman's voice, calm and sharp, heard through the small headset speaker", '一个低沉顺滑、冷静而锐利的女声，从耳机的小扬声器里传出'),
       'lin': ("a low steady man's voice, slightly muffled by radio hiss, heard through the small headset speaker", '一个低沉平稳的男声，带着电流声，略微发闷，从耳机的小扬声器里传出')}
look('src_headset_su', 'HeadsetSu', 'a slim black headset', 'none', 'its')
look('src_headset_lin', 'HeadsetLin', 'a slim black headset', 'none', 'its')


def _a(w):
    return ('an ' if w[:1].lower() in 'aeiou' else 'a ') + w


def src_of(a):
    """说话人键 → (来源类型, 角色用的 look 键, 声音描述)"""
    if a == 'eden_voice': return 'eden', a, VD[a]
    if a == 'k_rec': return 'krec', a, VD[a]
    if a == 'ghost_voice': return 'ghost', a, VD[a]
    if a in ('radio_ning', 'radio_pei', 'radio_cmd'): return 'radio', a, VD[a]
    if a == 'stranger_radio': return 'belt', a, VD[a]
    if a == 'lin_rec': return 'eden', a, VD[a]
    if a.startswith('su_'): return 'headset', 'src_headset_su', VPH['su']
    if a.startswith('lin_'): return 'headset', 'src_headset_lin', VPH['lin']
    raise KeyError(('不知道这个“只有声音”的说话人是从什么东西里传出来的', a))


def ensure_headset(S):
    b = S.eps[0][0]
    b.prop('headset', '通信耳机（黑色细耳机，带一根短短的麦克风杆）',
           'A slim black over-ear communications headset with a short boom microphone. The reference fixes its look.',
           '一副黑色的细耳机，带一根短短的麦克风杆。参考图固定它的外形。',
           'A photorealistic product shot of a slim black over-ear communications headset with a short boom microphone, against a plain neutral gray background.')
    for nm, basec in (('HeadsetSu', 'SuCozy'), ('HeadsetLin', 'LinWork')):
        v = b.d['characters'][basec]['voice_description']
        b.character(nm, 'headset', v['en'] + ' This voice is heard through a small headset speaker, slightly flattened, with a faint radio hiss.',
                    v['zh'] + '这是从耳机小扬声器里传出的声音，略微发扁，带着细细的电流声。')


_BREATH_EN = re.compile(r"(?:,\s*|\s+and\s+)(?:an? |the |one )?(?:[\w-]+ ){0,2}(?:breath\w*|sigh\w*|gasp\w*|footsteps?|heartbeat|creak of (?:a|the) [\w ]+?(?=[,.]))", re.I)
_BREATH_ZH = re.compile(r"[，、和](?:一声|一口|一阵|一下)?[^，。、；]{0,8}(?:呼吸|喘息|叹息|脚步|心跳)[^，。、；]{0,3}")


def nobody_sound(sound):
    """没有人的插镜：声音描述里去掉呼吸／叹息／脚步这类“有人在场”的声音。"""
    en, zh = sound
    return _BREATH_EN.sub('', en), _BREATH_ZH.sub('', zh)


def insert(S, tid, run, scene, sound, room, new, timer, brisk=('', ''), cam=None, dmin=4):
    """一段连续的“只有声音”的台词 → 一个不带人的插镜。返回 (S.T 的结果, 任务秒数, 最后一句结束秒数)。"""
    a0 = run[0][0]
    key, ck, (vd_en, vd_zh) = src_of(a0)
    s = SRC[key]
    if key == 'headset': ensure_headset(S)
    timed = timer([(a, tx, None) for a, tx, c, te, tz in run])
    parts_en, parts_zh, vo = [], [], []
    prev = None
    for i, ((a, tx, c, te, tz), (_sp, tx2, st, _)) in enumerate(zip(run, timed)):
        k2, ck2, (v2_en, v2_zh) = src_of(a)
        assert k2 == key, (tid, '一个插镜里只能有一种声音来源', a0, a)
        if ck2 == prev:
            lead_en, lead_zh = 'Then the same voice', '接着还是这个声音'
        elif prev is None:
            lead_en = (v2_en[0].upper() + v2_en[1:]) if v2_en.startswith(('the ', 'a ', 'an ')) else f'The {v2_en}'
            lead_zh = v2_zh
        else:
            lead_en = 'Then ' + (v2_en if v2_en.startswith(('the ', 'a ', 'an ')) else f'the {v2_en}')
            lead_zh = '接着是' + v2_zh
        parts_en.append(lead_en + f' speaks the {ORD[i]} line in {_a(te)} voice')
        parts_zh.append(lead_zh + f'用{tz}的声音说出{ORD_ZH[i]}')
        vo.append((ck2, tx2, st, None))
        prev = ck2
    last = timed[-1]
    end = last[2] + _H.line_seconds(last[1])
    d = max(dmin, min(12, math.ceil(end + 1.5)))
    assert end + 1.06 <= d, (tid, '插镜放不下台词', end)
    be, bz = brisk if len(run) > 1 else ('', '')
    act_en = f"A close view of {s['obj_en']}. " + ', '.join(parts_en) + '. Nothing else in the frame moves.' + be
    zh = f"{s['obj_zh']}的特写。" + '，'.join(parts_zh) + '。画面里没有别的东西在动。' + bz
    cam = cam or push1(s['cam_en'], s['cam_zh'])
    first_tx = run[0][1]
    title = f"00｜插镜：{s['title_zh']}里传出{ZN.get(a0, '声音')}的声音，说“{first_tx[:12]}”"
    sc = _scene.Scene(scene.key, scene.end, s['layout'])
    SPLITS.append(tid)
    r = S.T(tid, title, d, sc, [], f"Close view, {s['obj_en']} filling the middle third of the frame, nobody in the scene.", act_en, zh, nobody_sound(sound),
            cam=cam, room=room, new=new, holds=f"The frame holds only {s['obj_en']}; nobody is in the scene.", extra_assets=s['assets'], vo=vo)
    return r, d, end


# ---------------------------------------------------------------------------------------------- 手写脚本（013–020）用的公共小函数
BRISK = (' The lines follow one another at once with only a very short breath between them, each said in one breath with no pause inside the sentence.',
         ' 台词一句紧接着一句，中间只有很短的换气，每句一口气说完、句中不停顿。')


def smooth_timer(spec):
    """顺滑写法的台词排时间：起点和句间取 _h3draft.CFG；12 秒放不下就把句间收到 0.35、再放不下 0.2 秒。"""
    def run(g):
        out, t = [], _H.CFG['start']
        for sp, tx, to in spec:
            tx2 = _scene.smooth_text(tx)
            out.append((sp, tx2, round(t, 2), to))
            t = t + _H.line_seconds(tx2) + g
        return out
    out = run(_H.CFG['gap'])
    for g in (0.35, 0.2):
        if out[-1][2] + _H.line_seconds(out[-1][1]) + 1.06 > 12: out = run(g)
    return out


def vins(S, tid, run, scene, sound, room, new):
    """手写脚本里用：run = [(说话人, 台词, 英语语气, 中文语气)]。"""
    r, d, end = insert(S, tid, [(a, tx, None, te, tz) for a, tx, te, tz in run], scene, sound, room, new, smooth_timer, brisk=BRISK)
    print('  [插镜 %s：%d 秒，最后一句约 %.1f 秒]' % (tid, d, end))
    return r


def unvoice(snd):
    """没有台词的任务不能写“人声清楚”（H11）。"""
    en, zh = snd
    if en.endswith(' Voices stay close and clear.'):
        en = en[:-len(' Voices stay close and clear.')] + ' ' + _H.NOWORD_EN
        zh = zh[:-len('人声近而清楚。')] + _H.NOWORD_ZH
    elif en.endswith(' The voices are clear.'):
        en = en[:-len(' The voices are clear.')].replace(' ' + _H.LOUD_EN, ' ' + _H.NOWORD_EN + ' ' + _H.LOUD_EN)
        zh = zh[:-len('人声清楚。')].replace(_H.LOUD_ZH, _H.NOWORD_ZH + _H.LOUD_ZH)
    return en, zh
