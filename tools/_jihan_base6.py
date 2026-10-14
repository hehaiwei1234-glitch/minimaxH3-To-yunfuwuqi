"""《极寒末日》第 29 集起共用的定义（2026-10-14）：从 gen_jihan_ep29_32_013.py 原样复制（运镜 drop、光和空气 AES_*、TA／TAV／insert2、新外貌、场景、声音）。
013 的生成脚本一字不动。014 起 `import _jihan_base6 as B6; B6.S = S; from _jihan_base6 import *`（TA／TAV／insert2 用的是本模块里的 S，所以要先把 Session 赋给 B6.S）。"""
from _jihan_base5 import *
from _scene import smooth_task

S = None   # 由使用它的生成脚本赋值（B6.S = Session(...)）


# ---------------------------------------------------------------------------------------------- 运镜
def drop(to_en, to_zh):
    return (f'The camera starts high above and sinks slowly on a crane until {to_en} fill the middle third of the frame.',
            f'镜头从高处开始，像吊臂一样缓缓降下来，直到{to_zh}占满画面中间三分之一。')


# ---------------------------------------------------------------------------------------------- 光和空气（唯美）
AES_BF = ("Soft golden lamp light pools on the wooden table, steam from the mugs curls up through the beam, and the cool blue flicker of the monitor wall on one side gives a gentle teal-and-orange contrast.",
          "柔和的金色灯光洒在木桌上，杯子里的热气一缕缕卷过光束，一侧监控墙冷冷的蓝光和暖光形成淡淡的青橙对比。")
AES_JAM = ("Honey-gold lamp light makes the ruby jam glow translucent like stained glass, fine crumbs and floating steam catch the light and the whole picture glows warm.",
           "蜂蜜般的金色灯光让红宝石色的果酱像彩色玻璃一样透亮，细细的面包屑和飘着的蒸汽都被光照亮，整个画面暖洋洋地发光。")
AES_AURORA = ("A faint green aurora ripples across the black sky and its light glitters on the snow, and powdery snow crystals sparkle as they blow through the air.",
              "一片淡淡的绿色极光在漆黑的天空里流动，光洒在雪地上闪着光，被风吹起的粉雪晶体在空气里闪烁。")
AES_DISC = ("A hard red blinking light throws a pulsing red rim over the glittering snow crystals while the green aurora washes the far snowfield in cold light, deep blue shadows falling away at the edges of the frame.",
            "一点硬朗的红色闪光在闪亮的雪晶上投下一圈圈脉动的红边，绿色极光用冷冷的光洗过远处的雪原，画面四周落入深深的蓝色阴影。")
AES_TEAL = ("The cool blue-green glow of the console screens on one side and the warm amber lamp on the other split the light into a rich teal-and-orange contrast that rims the edges of everything.",
            "控制台屏幕蓝绿色的光在一侧，温暖的琥珀灯光在另一侧，把光分成浓郁的青橙对比，勾出每样东西的轮廓。")
AES_SPARK = ("Faint blue-white sparks glitter on the snow in the dark and thin curls of frost smoke drift through the green aurora light.",
             "几缕淡淡的蓝白色电火花在黑暗里的雪面上闪光，细细的霜雾在绿色极光的光里飘散。")
AES_FROST = ("Pale blue aurora light slides over the dull armor while ice crystals glitter in the air and a rim of cold light outlines every plate.",
             "淡蓝色的极光在暗淡的装甲上滑过，空气里的冰晶闪着光，一圈冷光勾出每一块甲片的轮廓。")
AES_GARAGE = ("Cool white floodlights from the high ceiling fall on the matte-black armor in long rim lights, dust motes drift through the beams and a thin line of warm orange glows from the corridor behind.",
              "冷白色的泛光灯从高高的天花板上照下来，在哑光黑的装甲上勾出长长的轮廓光，尘埃在光束里飘，身后走廊里有一线温暖的橙光。")
AES_PAD = ("A soft green glow from the fingerprint pad rims his profile against the dark steel wall and a few specks of dust drift through the beam.",
           "指纹板柔和的绿光勾出他的侧脸轮廓，映在深色的钢墙上，几粒尘埃在光束里飘。")
AES_CAB = ("The warm amber glow of the dashboard lights rims their faces and the steam of the cups curls through it, while behind the windshield the world is a cold blue-white snowfield under a green aurora, a rich teal-and-orange contrast.",
           "仪表盘温暖的琥珀色灯光勾出两人的脸，杯子里的热气在光里卷着，挡风玻璃外是冷冷的蓝白雪原和绿色极光，形成浓郁的青橙对比。")
AES_RADAR = ("The green glow of the radar screen and the warm amber dashboard light meet in a teal-and-orange contrast, and a thin haze of steam drifts in the beam.",
             "雷达屏幕的绿光和仪表盘温暖的琥珀灯光交汇成青橙对比，光束里飘着一层薄薄的热气。")
AES_SNOWRV = ("A green aurora curtain ripples over the snowfield and its light glitters on the churned snow, while a long plume of powdery snow glows in the headlight beams.",
              "绿色的极光帷幕在雪原上空流动，光洒在被碾起的雪上闪着光，一长条粉雪在车灯光束里发亮。")


def TA(tid, title, dur, scene, people, framing, act_en, zh, sound, aes, **kw):
    kw['bg'] = (kw.get('bg', '') + ' ' + aes[0]).strip()
    return S.T(tid, title, dur, scene, people, framing, act_en.rstrip() + ' ' + aes[0], zh.rstrip() + aes[1], sound, **kw)


def TAV(tid, title, scene, people, framing, act_en, zh, sound, aes, lines, **kw):
    """画外音／头盔对讲／收音机的台词：同样走顺滑写法（算起点、算任务长度），再用 vo 传进去。"""
    new, d, a, z = smooth_task(lines, 0, act_en, zh)
    return TA(tid, title, d, scene, people, framing, a, z, sound, aes, vo=new, **kw)


def insert2(tid, title, dur, scene, framing, act_en, zh, snd, holds, cam, aes, extra_assets=(), groups=()):
    return S.T(tid, title, dur, scene, [], framing, act_en.rstrip() + ' ' + aes[0], zh.rstrip() + aes[1], snd, cam=cam, holds=holds,
               room={g[0] for g in groups}, groups=list(groups), new=True, bg=aes[0], extra_assets=extra_assets)


# ---------------------------------------------------------------------------------------------- 新外貌
look('scout', 'Scout', "in a sleek matte-white military polar exoskeleton armor with articulated servo joints, a full white helmet with a black tinted faceplate hiding his whole face, and a slim black survey probe in one gloved hand", 'visor-covered', 'his', eth='a tall armored soldier')
look('su_tac', 'SuTac', "in a black quilted tactical cold-weather jacket zipped to the collarbone over a black thermal top, black trousers and black gloves, her long black hair in a high ponytail", 'sharp dark-brown', 'her', eth=CN_F28)
look('su_tacfit', 'SuTacfit', "in a fitted black long-sleeve thermal top and black trousers, her black quilted jacket folded over her knees, her long black hair in a high ponytail", 'soft dark-brown', 'her', eth=CN_F28)
look('radio_cmd', 'RadioCmd', "a military long-wave radio", 'none', 'its')
SCOUT_EN = 'A flat, cold synthetic adult male voice filtered through a helmet speaker, speaking clear Mandarin Chinese.' + VT_EN
SCOUT_ZH = '经过头盔扬声器处理的、平板冰冷的合成感成年男声，普通话清楚。' + VT_ZH
RADIOCMD_EN = "A stern, cold, authoritative middle-aged man's voice, deep and slow, heard through crackling radio static, speaking clear Mandarin Chinese." + VT_EN
RADIOCMD_ZH = '威严冰冷的中年男声，低沉缓慢，带着收音机沙沙的杂音，普通话清楚。' + VT_ZH

# ---------------------------------------------------------------------------------------------- 场景
CONTROL_R = Scene('bunker_control', CONTROL.end, CONTROL.layout + " A steel side table at frame-right holds an olive-green military long-wave radio with a large round dial glowing amber, a pole antenna and a cloth speaker grille.")
LIV_BF = Scene('bunker_living', LIVING.end,
               LIVING.layout + " On the small round wooden dining table stand a wooden board with a halved golden loaf, a glass jar of ruby strawberry jam, two white plates and two steaming white mugs.")
JAM_CLOSE = Scene('bunker_living', LIVING.end,
                  " Fixed stage layout: a wooden cutting board in the middle of the frame holds a halved golden loaf steaming on its cut faces, thick ruby strawberry jam glistening across one cut face, beside an open glass jar of jam with a small spoon resting in it; behind the board the thick cream rug and the black-and-gold stove glow softly.")
FIELD = Scene('snow_field', " A black night under a faint green aurora; the snow glitters and the white light of the snow glows.",
              " Fixed stage layout: a vast open snowfield rippled by the wind fills the middle of the frame; a dark line of snow-laden pines stands far away along the back of the frame; a faint green aurora curtain hangs above it.")
FIELD_DISC = Scene('snow_field', FIELD.end,
                   " Fixed stage layout: a vast open snowfield fills the middle of the frame; a round matte-black metal disc the size of a dinner plate lies flat on the snow in the middle of the frame with a small red light blinking at its center; the dark line of snow-laden pines stands far away along the back of the frame.")
FIELD_DEAD = Scene('snow_field', FIELD.end,
                   " Fixed stage layout: a vast open snowfield fills the middle of the frame; a round matte-black metal disc the size of a dinner plate lies flat on the snow in the middle of the frame, its center light dark and dead; the dark line of snow-laden pines stands far away along the back of the frame.")
GARAGE_DOOR = Scene('garage_wall', " Cool white concrete-corridor light with a soft green glow from a small fingerprint pad.",
                    " Fixed stage layout: a long grey concrete corridor ends at a huge seamless brushed-steel wall that fills the middle of the frame; a small fingerprint pad with a faint green glow is set into the wall at frame-right; a red emergency lamp glows on the ceiling at frame-left.")
GARAGE = Scene('bunker_garage', " Cool white floodlights from the high ceiling fill the vast underground garage with drifting dust, and a thin line of warm orange glows from the corridor behind.",
               " Fixed stage layout: the vast grey concrete garage hall fills the frame; in the middle of the frame stands an eight-metre long armoured tracked all-terrain motorhome in matte black, with a heavy steel ice-breaker blade at its front and a thermal-radar dome on its roof; the huge brushed-steel wall stands split open at frame-left with the concrete corridor visible beyond it.")
GARAGE_RV = Scene('bunker_garage', GARAGE.end,
                  " Fixed stage layout: the front of the matte-black armoured tracked motorhome fills the middle of the frame, its heavy steel ice-breaker blade at the bottom, its dark windshield above it and the thermal-radar dome on its roof; behind it the vast grey garage hall.")
GARAGE_HANDOVER = Scene('bunker_garage', GARAGE.end,
                        " Fixed stage layout: the long flank of the matte-black armoured tracked motorhome fills the back of the frame; the vast grey concrete garage hall stretches around it; a steel workbench stands at frame-left.")
CAB = Scene('rv_cab', " Warm amber dashboard glow fills the compact armoured cab while the windshield shows a blue-white snowfield under a green aurora.",
            " Fixed stage layout: a cutaway side view of the cab; two leather bucket seats stand side by side across the middle of the frame, both facing frame-right toward the wide armoured windshield, the passenger seat at frame-left and the driver's seat at frame-center-right with a short steel control lever beside it; between them a console holds two steaming paper cups in cup holders; a small round radar screen is set in the dashboard at frame-right; the windshield at the right edge shows a vast blue-white snowfield and a green aurora.")
CAB_RADAR = Scene('rv_cab', CAB.end,
                  " Fixed stage layout: the small round radar screen set in the dark dashboard fills the middle of the frame, its green concentric rings crossed by a long chain of small bright red dots strung along a narrow line; two steaming paper cups stand in the cup holders at frame-left.")
SNOW_RV = Scene('snow_field', FIELD.end,
                " Fixed stage layout: a vast open snowfield fills the frame; the matte-black armoured tracked motorhome crosses the middle of the frame from frame-left toward frame-right on wide tracks, throwing up a long plume of powdery snow and leaving two deep tread lines behind it; a faint green aurora curtain hangs above.")
SNOW_RIDGE = Scene('snow_field', FIELD.end,
                   " Fixed stage layout: seen from a low angle at snow level, the matte-black armoured tracked motorhome charges up a long snow slope toward a ridge at frame-right, throwing up a wall of snow spray; a faint green aurora curtain hangs above.")

# ---------------------------------------------------------------------------------------------- 声音
SOUND_BF = voiced('The soft crunch of a crisp crust, the quiet clink of a mug on porcelain and the warm hum of the stove.', '酥脆面包皮轻轻的咔嚓声、马克杯碰到瓷盘轻轻的响声和炉子温暖的嗡鸣。')
SOUND_BF_B = breathy('The soft hiss of steam from a mug, the faint hum of the stove and the dim electronic hum of the monitor wall.', '杯子里热气轻轻的嘶嘶声、炉子轻微的嗡鸣和监控墙微弱的电子嗡声。')
SOUND_JAM = breathy('The soft crackle of a warm crust and the faint hum of the stove.', '温热面包皮轻轻的噼啪声和炉子轻微的嗡鸣。')
SOUND_SCOUT = voiced('A long low howl of wind over the snowfield, a faint electronic ping and the soft whir of armor servos.', '风掠过雪原长长的低啸、一声细细的电子提示音和装甲关节轻轻的嗡嗡声。')
SOUND_STRIDE = breathy('The crunch of heavy boots in deep snow, a long low howl of wind and the soft whir of armor servos.', '沉重的靴子踩进深雪的嘎吱声、风长长的低啸和装甲关节轻轻的嗡嗡声。')
SOUND_DISC = breathy('A fast electronic beeping that quickens, a thin howl of wind and the creak of snow.', '越来越快的电子嘀嘀声、风细细的呼啸和雪被踩动的吱嘎声。')
SOUND_CTRL = voiced('A low electric hum from the console and the faint hiss of the air system.', '控制台低低的电流嗡鸣和空气系统轻微的嘶嘶声。')
SOUND_KEY = voiced('The quick tapping of keys, a low electric hum from the console and one firm click.', '键盘急促的敲击声、控制台低低的电流嗡鸣和一声干脆的按键声。')
SOUND_SPARK = breathy('A single soft electric crackle, then a deep hush over the snowfield.', '一声轻轻的电流噼啪，然后雪原上一片深深的寂静。')
SOUND_STILL = breathy('A deep hush, the tick of freezing metal and a muffled labored groan.', '深深的寂静、金属冻结时细细的嘀嗒声和一声被闷住的吃力的低哼。')
SOUND_FREEZE = breathy('The tick and creak of metal freezing, a thin howl of wind and a faint muffled groan.', '金属冻结时的嘀嗒和吱呀声、风细细的呼啸和一声微弱的闷哼。')
SOUND_FALL = breathy('A dull heavy thud into soft snow, a puff of powder and a thin howl of wind.', '一声沉闷厚重的撞击落进松软的雪里、一团粉雪扬起和风细细的呼啸。')
SOUND_RADIO = voiced('Crackling radio static with a thin tuning whistle and the faint hum of the control room.', '收音机沙沙的杂音、细细的调频啸叫和控制室轻微的嗡鸣。')
SOUND_RADIO_ALARM = voiced('Crackling radio static, then a sharp rising electronic alarm that cuts through the control room.', '收音机沙沙的杂音，然后一声尖锐渐强的电子警报划过控制室。')
SOUND_GARAGE_B = breathy('A low hum of floodlights and the faint tick of cooling metal in the vast garage.', '泛光灯低低的嗡鸣和空旷车库里金属冷却时细细的嘀嗒声。')
SOUND_GARAGE = voiced('A low hum of floodlights and the faint tick of cooling metal in the vast garage.', '泛光灯低低的嗡鸣和空旷车库里金属冷却时细细的嘀嗒声。')
SOUND_WALL = breathy('A deep grinding rumble of heavy steel and the soft tick of settling dust.', '厚重钢铁深沉的摩擦隆隆声和落尘细细的嘀嗒声。')
SOUND_PAD = breathy('A soft electronic chirp and the low hum of the corridor.', '一声轻轻的电子嘀声和走廊低低的嗡鸣。')
SOUND_RV_IDLE = breathy('A deep low rumble of a diesel engine and the soft tick of cooling armor.', '柴油发动机深沉的低鸣和装甲冷却时轻轻的嘀嗒声。')
SOUND_ROAR = breathy('A thundering roar of a heavy engine, the grinding of tracks and a hiss of flying snow.', '重型发动机雷鸣般的轰响、履带的碾压声和飞溅的雪的嘶嘶声。')
SOUND_CAB = voiced('The smooth low hum of the engine, the soft hiss of warm air vents and a faint sip.', '发动机顺滑的低鸣、暖风口轻轻的嘶嘶声和一声轻轻的啜饮。')
SOUND_CAB_B = breathy('The smooth low hum of the engine and the soft hiss of warm air vents.', '发动机顺滑的低鸣和暖风口轻轻的嘶嘶声。')
SOUND_BEEP = breathy('A quick repeating electronic beep from the radar and the low hum of the engine.', '雷达急促反复的电子嘀嘀声和发动机的低鸣。')

