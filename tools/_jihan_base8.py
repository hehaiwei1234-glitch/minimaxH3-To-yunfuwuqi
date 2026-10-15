"""《极寒末日》第 59 集起共用的外貌／场景／画外音定义（从 gen_jihan_ep59_62_022.py 原样抽出，2026-10-15 夜）。
用法：`import _jihan_base8 as B8; from _jihan_base8 import *`（先 import _jihan_base7）。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base7 as B7
from _jihan_base7 import *
import _jihan_base6 as B6
import _h3draft as _H

# ---------------------------------------------------------------------------------------------- 衣着
SU_CLINIC = "in a cream knit sweater and black thermal leggings, thick grey socks, her long black hair loose"
LIN_CLINIC = "in a soft grey cotton henley with the left sleeve rolled up to the elbow and loose dark lounge pants"
SU_SLIP = "in a cream knit sweater and black thermal leggings with fluffy white slippers on her feet, her long black hair loose"
SU_WORK = "in a cream knit sweater with the sleeves pushed up to her elbows, black thermal leggings and soft boots, her long black hair tied back in a loose low ponytail"
LIN_WORK = "in a charcoal henley with the sleeves pushed up to his forearms, dark cargo trousers and soft boots"
SU_HEAD = "in a cream knit sweater with the sleeves pushed up, black thermal leggings and soft boots, a black over-ear headset with a slim boom microphone on her head, her long black hair tied back"
LIN_FLOOD_OUT = "in a black neoprene wetsuit with an orange life vest, a dive mask pushed up onto his wet hair and a small headlamp on his forehead, water running down his face and arms"

# ---------------------------------------------------------------------------------------------- 画外音（收音机里的人、耳机另一端的人）
look('radio_ning', 'RadioNing', "a military long-wave radio", 'none', 'its')
look('radio_pei', 'RadioPei', "a military long-wave radio", 'none', 'its')
look('lin_flood', 'LinFlood', LIN_FLOOD_OUT, 'steady dark-brown', 'his', eth=CN30)
RADIO_D = 'the olive-green long-wave radio on the steel side table'
RADIO_DZ = '钢桌上那台橄榄绿的长波收音机'
B7.VOICE_ONLY.update({'radio_ning', 'radio_pei'})
B7.VD['radio_ning'] = (f"the hoarse, frantic man's voice crackling out of {RADIO_D}", f'从{RADIO_DZ}里沙沙传出的嘶哑慌乱的男声')
B7.VD['radio_pei'] = (f"the cold, courteous, deep middle-aged man's voice crackling out of {RADIO_D}", f'从{RADIO_DZ}里沙沙传出的冷静客气、低沉的中年男声')
B7.VD['lin_flood'] = ("Lin's low steady voice heard through the small headset speaker, slightly muffled by water and radio hiss", '林峰低沉平稳的声音，从耳机的小扬声器里传出，带着水声和电流声，略微发闷')
B7.VD['su_cozy'] = ("Su's low smooth voice heard through the small headset speaker, calm and sharp", '苏清月低沉顺滑的声音，从耳机的小扬声器里传出，冷静而锐利')
B7.ZN.update({'radio_ning': '周宁', 'radio_pei': '裴远山', 'lin_flood': '林峰'})
RADIOPEI_EN = "A cold, courteous, unhurried deep middle-aged man's voice heard through crackling radio static, speaking clear Mandarin Chinese." + VT_EN
RADIOPEI_ZH = '隔着收音机沙沙杂音传来的、冷静客气、不紧不慢的低沉中年男声，普通话清楚。' + VT_ZH

# ---------------------------------------------------------------------------------------------- 场景
PERI = Scene('periscope_room', " Cool blue-white light from a round view screen and a faint amber work lamp fill the small round concrete periscope room.",
             " Fixed stage layout: a small circular concrete room; a thick vertical black steel periscope column with a padded rubber eyepiece at chest height stands at frame-left rising into the ceiling; a round view screen the size of a dinner plate glows on the wall at frame-right; a steel wall ladder stands behind; a narrow steel door is at the far frame-right.")
THAW = Scene('ice_army', " A deep blue pre-dawn with a faint green aurora fading, the ice glittering and beginning to run with water.",
             " Fixed stage layout: a vast snowfield under a pale green aurora in deep blue pre-dawn light fills the frame; rows of men in black winter gear and fur hats and a dozen heavy black trucks stand frozen across it, each sheathed in clear glittering ice; thin dark streaks of meltwater run down the ice and dark wet patches show in the snow around the feet of the nearest figures; nobody moves.")
DROP = Scene('ice_army', THAW.end,
             " Fixed stage layout: a close view of the raised arm of one frozen man sheathed in clear ice, a small icicle hanging from his clenched fist in the middle of the frame with a single bright drop of meltwater hanging at its tip and a thin wet shine spreading on the ice below; the ranks of other ice figures soft behind; nobody alive in the scene.")
CONTROL_RADIO = Scene('bunker_control', CONTROL.end, CONTROL.layout + " A steel side table at frame-right holds an olive-green military long-wave radio with a large round dial glowing amber, a pole antenna and a cloth speaker grille.")
RADIO_CLOSE = Scene('bunker_control', CONTROL.end,
                    " Fixed stage layout: a close view of the olive-green long-wave radio on the steel side table filling the middle of the frame, its round dial glowing amber with the needle trembling at one frequency, the pole antenna rising at frame-right; the green status lights of the console blur behind; nobody in the scene.")
PLAN = Scene('bunker_living', LIVING.end,
             " Fixed stage layout: the open kitchen with the black-and-gold stove is at frame-left; the small round wooden dining table fills the middle of the frame covered by a large hand-drawn paper map of mountains with a red pencil circle around a small blue lake and a steel ruler on it; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
FLOOD_DRY = Scene('flood_bay', " Cold white work-lamp light fills the long concrete flood-control bay and a few red emergency strobes pulse far down it.",
                  " Fixed stage layout: a long narrow concrete bay with a dry floor; a huge grey titanium wall panel with riveted seams fills the left half of the frame; thick silver pipes run along the ceiling; a steel ladder stands at frame-right; cans of grey sealant, a paint roller tray and a coil of hose stand on the floor.")
FLOOD_BRACE = Scene('flood_bay', FLOOD_DRY.end,
                    " Fixed stage layout: a long narrow concrete bay with a dry floor; the huge grey titanium wall panel with riveted seams fills the left half of the frame freshly coated in matte grey sealant; a row of heavy hydraulic steel brace jacks spans from the wall to the concrete pillars; thick silver pipes run along the ceiling; a steel ladder stands at frame-right.")
LIV_NOODLE = Scene('bunker_living', LIVING.end,
                   " Fixed stage layout: the open kitchen with the black-and-gold stove is at frame-left, a steaming pot on it; the small round wooden dining table fills the middle of the frame set with two white bowls of steaming noodles in clear broth topped with golden fried eggs and green leaves, two pairs of chopsticks beside them; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
BUOY2 = Scene('pump_room', " Cool white light from a work lamp falls on the clear tank and pipes of the small pump room.",
              " Fixed stage layout: a tall clear water tank fills the middle of the frame with a red float marker bobbing high on the water inside it beside a vertical white scale with painted tick marks, the water level now two notches higher than before; clear water pipes run along the wall at frame-left; nobody in the scene.")
FLOOD_JET = Scene('flood_bay', " Cold white work-lamp light and a pulsing red emergency strobe fill the long concrete flood-control bay, mist hanging in the air.",
                  " Fixed stage layout: a long narrow concrete bay; the huge grey titanium wall panel fills the left half of the frame with a hairline crack running down the middle of it, a thin high-pressure jet of clear water spraying sideways out of the crack across the bay in a long white blade of spray; the floor is wet and shining; thick silver pipes run along the ceiling; a steel ladder stands at frame-right; nobody in the scene.")
FLOOD_PLANK = Scene('flood_bay', FLOOD_JET.end,
                    " Fixed stage layout: a long narrow concrete bay; the titanium wall panel at frame-left has a hairline crack from which a thin white jet of water sprays across the frame; a pale wooden plank lies cut cleanly in two halves on the wet floor in the middle of the frame where the jet struck it, water pooling around the halves; nobody in the scene.")
FLOOD_WATER = Scene('flood_bay', " Cold white work-lamp light and a pulsing red emergency strobe fill the long concrete bay, water spraying and mist hanging in the air.",
                    " Fixed stage layout: a long narrow concrete bay with the floor flooded knee-deep in dark water; the huge grey titanium wall panel with riveted seams and a hairline crack down its middle fills the left half of the frame, a thin jet of water spraying out of the crack; thick silver pipes run along the ceiling; a steel ladder stands at frame-right; floating wooden planks and a yellow plastic crate drift on the water.")
FLOOD_WELD = Scene('flood_bay', " Cold white work-lamp light falls on the long concrete bay, the water calm and the mist thinning.",
                   " Fixed stage layout: a long narrow concrete bay with the floor flooded knee-deep in still dark water; the titanium wall panel fills the left half of the frame and down its middle runs a fresh bright seam of weld, glowing orange-white and cooling, with no water spraying; thick silver pipes run along the ceiling; nobody in the scene.")
FLOOD_DONE = Scene('flood_bay', " Cold white work-lamp light falls on the long concrete bay, the water now only ankle deep and still; a low muffled roar of water comes through the wall.",
                   " Fixed stage layout: a long narrow concrete bay with the floor covered by ankle-deep still water; the titanium wall panel at frame-left with a clean grey seam down its middle, perfectly dry; a steel ladder stands at frame-right; a white towel hangs from the lowest rung.")
GATE = Scene('gate_room', " A single caged work lamp lights a cold bare concrete chamber and dust hangs in the beam.",
             " Fixed stage layout: a small bare concrete chamber whose back wall is filled by a massive round steel gate door two metres tall with a big black iron hand-wheel the size of a car tyre at its centre; a rectangular brass plate with a hand-shaped recess is set into the wall at frame-right beside the gate; a rusty ladder stands at frame-left.")
GATE_CLOSE = Scene('gate_room', GATE.end,
                   " Fixed stage layout: a close view of the big black iron hand-wheel filling the middle of the frame with the dull steel gate door behind it and the rectangular brass plate with a hand-shaped recess at frame-right; nobody in the scene.")
CONVOY_FAR = Scene('snow_field', FIELD.end,
                   " Fixed stage layout: a vast dark snowfield seen from far away fills the frame; along the far horizon at the back of the frame a long chain of tiny white headlights crawls slowly along a ridge road; a faint green aurora hangs above; nobody in the scene.")

B7.VD['lin_work'] = B7.VD['lin_flood']
B7.VD['lin_home'] = B7.VD['lin_flood']
AE = lambda en, zh: (en, zh)


# ---------------------------------------------------------------------------------------------- 内心独白（画面里的人嘴闭着，独白在画面上方响起）
def MONO(tid, title, scene, people, framing, act_en, zh, sound, aes, lines, tail=2.0, mind=6, **kw):
    """独白任务：lines 是独白句子的列表（说话人就是画面里的第一个人）。时间按当前 A／B 模式排；嘴写成闭着不动。"""
    import math
    a = people[0]['lk']
    timed = B7.times([(a, t, None) for t in lines])
    end = timed[-1][2] + _H.line_seconds(timed[-1][1])
    d = max(mind, min(15, math.ceil(end + tail)))
    if end + 1.06 > d or d > 15:
        B7.FAILS.append(f'{tid}: 独白最后一句说完约 {end:.1f} 秒，放不进任务（要 ≤13.9）')
        return None
    vo = [(a, tx, st, B7.who(a)) for _, tx, st, _ in timed]
    en = act_en.rstrip() + ' The lines are his inner voice-over, heard over the scene while his lips stay closed and do not move.' if LOOKS[a].pron == 'his' else act_en.rstrip() + ' The lines are her inner voice-over, heard over the scene while her lips stay closed and do not move.'
    zz = zh.rstrip() + ('这些话是他的内心独白，在画面上方响起，他的嘴唇一直闭着、不动。' if LOOKS[a].pron == 'his' else '这些话是她的内心独白，在画面上方响起，她的嘴唇一直闭着、不动。')
    return B7.TAA(tid, title, d, scene, people, framing, en, zz, sound, aes, vo=vo, **kw)
