#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 29–32 集，追加稿 013（2026-10-14）。以 012 的 JSON 为底（style／素材／角色逐字复制），必须等 012 在插件里全部跑完再追加。
hh 2026-10-14 18:19：“再更新出来 16 集，我挂通宵。不要着急，一批一批来，一次 4 集；太长影响质量就停下来跟我说。”本批＝第一批（29–32），后面 014（33–36）、015（37–40）、016（41–44）。

写法＝012 同一套：台词顺滑写法（句内无标点、任务长度按语速收紧）＋全批固定视频种子 37407＋视频文字里也锁人数＋每个任务一句“光和空气”；
  每集至少一个低机位上摇、一个起重机下降／上升、一个光的特写插镜；环绕镜头本批不用。
偏离大纲（交稿时已告诉 hh）：
  · 第 29 集：草莓果酱写成“第一茬自己种的草莓熬的”（养成的新进展）；“监控屏幕里的侦察兵”改成直接切到地表（不拍屏幕套屏幕）；“地层声波探测仪”只拍一根插进雪里的黑色探测杆；
    “高能定向破甲炸弹”只拍一个黑色圆盘（红灯闪），倒计时用红灯越闪越快＋林峰一句“三二一晚安”代替屏幕数字；
  · 第 30 集：EMP 只拍结果——圆盘熄灭、雪面几缕蓝白电火花、装甲灯全灭；“不到五秒冻死”拆成：灯灭→手抓头盔→白霜爬满装甲→直挺挺倒下四个任务，不拍脸；侦察兵没有枪战；
    官方指挥官只有声音，用画面里的收音机出声（收音机的电源线已重新插回，不另拍）；
  · 第 31 集：车顶“重机枪”不拍，只有热成像雷达圆罩；“伪装暗门打开、巨兽冲出”只拍冲进雪原的结果（航拍）；
  · 第 32 集：“车载音响放乡村音乐”整句删掉（不要电子娱乐），驾驶舱里只有热咖啡和暖光；苏清月“只穿贴身战术服”改成黑色长袖保暖衣＋外套叠在腿上。
H3 方面的风险（交稿时单列，不算我的错）：
  · 29-04／29-05 头盔面罩后面的人说话（嘴看不见，声音可能被画成别的人张嘴）；29-07 圆盘红灯闪烁；
  · 30-02 按回车键（手指动作）；30-03 蓝白电火花；30-04 装甲灯熄灭；30-05 白霜爬满装甲；30-06 人直挺挺倒下（快动作）；30-08／30-09 收音机旁白（可能多出说话的人）；
  · 31-03 横移跟拍里的两句台词；31-05 巨大金属墙裂开后的车库（只拍结果）；31-06 巨型装甲房车（新道具，没有任何数据）；31-08、32-01、32-07 装甲车在雪原上行驶（运动的车辆）；
  · 32-02～32-04 驾驶舱里两人并排（侧剖视角）、蒸汽咖啡杯；32-05 雷达屏幕上一串红点；开场图约一成不按文字画；“同一处”场景用参照图。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _jihan_base5 import *
from _scene import smooth_task

import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407)   # hh 2026-10-14 16:20：台词顺滑写法＋全批固定视频种子
OUT = '合并稿/013_第29-32集_草莓酱电磁处决黑色巨兽冰原狂飙_制作稿_追加'
S = Session('合并稿/012_第25-28集_拔线子留声机冰震冰窖阀门面包香_制作稿_追加.json', OUT, 45000)


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

# ================================================================================================ 第 29 集
b29 = S.episode('剧本第29集｜白雪中的顶级猎犬', '早晨，林峰切开冒着热气的面包，抹上厚厚的草莓酱递给苏清月，那是他们自己种的第一茬草莓熬的；她咬了一口酥脆的面包，舒服得眯起眼睛；林峰端着咖啡杯瞥了一眼监控，杯子停在半空，眼神变冷；地表雪原上，那个穿白色外骨骼装甲的侦察兵把探测杆插进雪里，对着头盔对讲机汇报：赵虎小队已全灭，死于高压蒸汽陷阱，下方有巨大的中空建筑，坐标已锁定；他走到地下室正上方，把一枚闪着红灯的黑色圆盘按在雪地上；苏清月放下面包：军用破甲弹，他要炸开外壳；林峰咽下最后一口咖啡，在主控台上敲下一串指令：高级货，就用点高级的死法。', 29)
b29.prop('jam_jar', '一罐自己种的草莓熬的果酱（透明玻璃罐，红宝石色，里面能看见整颗的草莓，罐里插着一把小勺）',
         'A clear glass jar of thick ruby-red homemade strawberry jam with whole berries visible inside and a small spoon resting in it. The reference fixes its shape.',
         '一个透明的玻璃罐，里面是浓稠的红宝石色自制草莓酱，能看见整颗的草莓，罐里搁着一把小勺。参考图固定它的外形。',
         'A photorealistic product shot of a clear glass jar of thick ruby-red homemade strawberry jam with whole berries visible inside and a small spoon resting in it, on a wooden board against a plain neutral gray background.')
b29.prop('breach_disc', '定向破甲炸弹（哑光黑金属圆盘，餐盘大小，中心一点红灯）',
         'A round matte-black metal disc the size of a dinner plate with a thick flat rim and a small red light at its center. The reference fixes its shape.',
         '一个哑光黑色的金属圆盘，餐盘大小，边缘厚实平整，中心有一点红灯。参考图固定它的外形。',
         'A photorealistic product shot of a round matte-black metal disc the size of a dinner plate with a thick flat rim and a small red light at its center, against a plain neutral gray background.')
new_scene(b29, 'snow_field', '地表雪原（一望无际的雪地，远处一线黑压压的松林，上空的绿色极光）',
          'A vast open black-night snowfield rippled by the wind, a dark line of snow-laden pines far away along the horizon and a faint green aurora curtain hanging above.',
          '一片一望无际、被风吹出波纹的夜间雪原，远处地平线上一线黑压压挂满雪的松林，上空悬着一片淡淡的绿色极光。',
          'the open snowfield, the far dark pine line and the green aurora')

insert2('29-01', '01｜插镜：厨房台面上，一块切开的金黄面包冒着热气，红宝石色的草莓酱一层厚厚地铺在断面上，亮得像彩色玻璃', 5, JAM_CLOSE,
        'Close shot of the cutting board, the halved loaf and the jam jar in the middle third of the frame, nobody in the scene.',
        "A thick glossy layer of ruby strawberry jam lies across the steaming cut face of a halved golden loaf with whole red berries glinting inside it, and a ribbon of steam curls up through the amber light beside the open jam jar. Nothing else moves.",
        "一层厚厚的、亮晶晶的红宝石色草莓酱铺在一块切开的金黄面包冒着热气的断面上，酱里整颗的红草莓闪着光，一缕蒸汽在打开的果酱罐旁边卷过琥珀色的灯光。别的什么都不动。",
        SOUND_JAM, 'The frame holds the cutting board, the halved golden loaf and the jar of ruby jam, and nobody in the scene.',
        push1('the glistening jam on the cut loaf', '切开的面包上亮晶晶的草莓酱'), AES_JAM, extra_assets=('jam_jar',))

TA('29-02', '02｜餐桌边：林峰把抹好草莓酱的面包递给苏清月，说第一茬草莓熬的酱，她咬了一口，舒服得眯起眼睛，说好脆好甜我不想出门了', 9, LIV_BF,
   [P('lin_home', 'center', "sitting at the small round table in profile facing frame-left, holding out a thick slice of golden bread spread with ruby strawberry jam toward her", 'Su', "one corner of his mouth lifting, his jaw relaxed, his brows soft", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'left', "sitting at the table in profile facing frame-right, taking the slice in both hands and biting into it", 'obj:the slice of bread in her hands', "her eyes drifting half shut, a blissful sweet smile on her lips, her brows lifted")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dining table.',
   "<lin_home> holds out the slice and speaks the first line to <su_cozy> in a low, warm voice, one corner of his mouth lifting and his brows soft. <su_cozy> takes a bite with a crisp crunch and her eyes slide half shut like a lazy cat, then she speaks the second line to <lin_home> in a soft, dreamy voice, a blissful sweet smile on her lips and her brows lifted.",
   "林峰把面包递过去，用低沉温暖的声音对苏清月说出第一句，嘴角微微上扬、眉毛舒展。苏清月咬下一口，发出酥脆的咔嚓声，眼睛像一只慵懒的猫一样慢慢眯起来，然后用柔软、梦幻的声音对林峰说出第二句，嘴角带着幸福的甜笑、眉毛上扬。",
   SOUND_BF, AES_BF, lines=[('lin_home', "第一茬草莓熬的酱，尝尝。", 0.8, 'Su'), ('su_cozy', "好脆好甜，我不想出门了。", 3.2, 'Lin')],
   cam=push('both of them', '两人'), extra_assets=('jam_jar',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the black-and-gold stove glows warm at frame-left and the wall of small monitors glows cool blue at frame-right.',
   holds='The frame holds exactly two people: Lin and Su, at the dining table, nobody else.')

TA('29-03', '03｜餐桌边：苏清月嚼着面包，林峰端着咖啡杯，眼睛扫了一眼监控墙，杯子停在半空，眼神一下子冷了', 6, LIV_BF,
   [P('su_cozy', 'left', "sitting at the table in profile facing frame-right, chewing happily with the half-eaten slice in both hands", 'obj:the slice of bread in her hands', "her eyes half shut, a contented sweet smile on her lips, her brows soft"),
    P('lin_home', 'center', "sitting at the table in profile facing frame-right, a white mug stopped halfway to his lips, his head turned toward the wall of small monitors at frame-right", 'obj:the wall of small monitors at frame-right', "his eyes narrowing to dangerous slits, his jaw tightening, his lips pressing flat, his brows lowering", outfit="in a soft grey henley and dark lounge pants")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dining table.',
   "<su_cozy> keeps chewing, lost in the taste, her eyes half shut and a contented sweet smile on her lips. <lin_home> stops with the mug halfway to his lips and holds still, his eyes narrowing to dangerous slits, his jaw tightening, his lips pressing flat and his brows lowering. Nobody speaks.",
   "苏清月继续嚼着，沉浸在味道里，眼睛半眯、嘴角带着满足的甜笑。林峰端着杯子停在半空，一动不动，眼睛眯成危险的细缝，下颌绷紧、嘴唇抿平、眉头压低。没有人说话。",
   SOUND_BF_B, AES_BF, cam=slide('right', '右', 'Lin and the wall of small monitors fill the middle third of the frame', '林峰和监控墙占满画面中间三分之一'),
   room={'Su', 'Lin'}, new=True,
   bg='At frame-right the wall of small monitors glows cool blue behind him and the black-and-gold stove glows warm at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, at the dining table, nobody else.')

TAV('29-04', '04｜地表雪原：侦察兵跪在冰雕前，把探测杆插进雪里，面罩后面传出冰冷的机械音，汇报赵虎小队全灭、死于高压蒸汽陷阱', PIT_ICE,
    [P('scout', 'right', "kneeling in the snow in profile facing frame-left at the rim of the pit in front of an ice-encased man, one gloved hand pressing the slim black probe deep into the snow", 'obj:the slim black probe in the snow', "his mouth and jaw hidden behind the black faceplate")],
    'Medium close shot, the kneeling armored figure from the head to the knees at frame-right, in the middle third of the frame, at the rim of the pit.',
    "<scout> holds the probe steady in the snow, his mouth and jaw hidden behind the black faceplate, and a flat cold synthetic voice from his helmet speaker reports the first line as a voice-over and then the second line while the green aurora ripples across his faceplate. Nobody else is in the scene.",
    "外骨骼侦察兵稳稳握着插进雪里的探测杆，嘴和下巴藏在黑色面罩后面，一个平板冰冷的合成声音从头盔扬声器里说出第一句，接着说出第二句，绿色的极光在他的面罩上流动。画面里没有别人。",
    SOUND_SCOUT, AES_AURORA, lines=[('scout', "报告总部，赵虎小队已全灭。", 0.8, 'Scout'), ('scout', "死于高压蒸汽陷阱。", 3.2, 'Scout')],
    cam=push1('the helmeted head and shoulders of the armored figure', '装甲身影的头盔和肩甲'),
    room={'Scout', 'the ice figures'}, new=True, groups=[('the ice figures', 'center', 'obj:the pit')],
    bg='Around the pit behind him stand the ring of ice-encased men, and the snowplow truck\'s headlights glow far at frame-left.',
    holds='The frame holds exactly one armored figure kneeling beside the ring of ice-encased men, nobody else alive.')

TAV('29-05', '05｜地表雪原：侦察兵换了个地方，再次把探测杆插进雪里，探测杆上一点绿灯亮起，他说下方有巨大的中空建筑、坐标已锁定', FIELD,
    [P('scout', 'center', "kneeling alone in the open snowfield in profile facing frame-left, both gloved hands holding the slim black probe driven into the snow, his helmeted head bowed toward it", 'obj:the slim black probe in the snow', "his mouth and jaw hidden behind the black faceplate")],
    'Medium shot, the kneeling armored figure from the head to the knees, in the middle third of the frame, in the open snowfield.',
    "<scout> kneels motionless over the probe with a small green light glowing on its handle, his mouth and jaw hidden behind the black faceplate, and a flat cold synthetic voice from his helmet speaker reports the first line as a voice-over and then the second line while powdery snow blows across the field. Nobody else is in the scene.",
    "外骨骼侦察兵跪在探测杆前一动不动，探测杆手柄上亮着一点小绿灯，嘴和下巴藏在黑色面罩后面，一个平板冰冷的合成声音从头盔扬声器里说出第一句，接着说出第二句，粉雪从雪原上吹过。画面里没有别人。",
    SOUND_SCOUT, AES_AURORA, lines=[('scout', "下方有巨大的中空建筑。", 0.8, 'Scout'), ('scout', "坐标已锁定。", 3.4, 'Scout')],
    cam=push1('the helmeted head and the probe', '头盔和探测杆'), room={'Scout'}, new=True,
    bg='Far behind him the dark line of snow-laden pines stands along the horizon.',
    holds='The frame holds exactly one armored figure kneeling alone in the open snowfield, nobody else.')

TA('29-06', '06｜地表雪原：侦察兵扛着探测杆在雪地上大步走，最后停在一片平坦的雪地中央，站定不动', 6, FIELD,
   [P('scout', 'center', "striding across the open snowfield in profile facing frame-right, the slim probe slung over his shoulder, his boots sinking into the snow", 'obj:the snow ahead of him', "his mouth and jaw hidden behind the black faceplate")],
   'Wide shot, the armored figure small in the middle third of the frame, in the open snowfield.',
   "<scout> strides across the snowfield with long steady steps, the servo joints of his armor whirring, and then halts and plants his feet in the middle of the flat snow, standing perfectly still as the aurora ripples above him; his mouth and jaw stay hidden behind the black faceplate. Nobody else is in the scene.",
   "外骨骼侦察兵迈着长长稳稳的步子穿过雪原，装甲的关节嗡嗡作响，然后站定，两脚扎在平坦的雪地中央，一动不动地站着，头顶的极光在流动；他的嘴和下巴一直藏在黑色面罩后面。画面里没有别人。",
   SOUND_STRIDE, AES_AURORA, cam=drop('the armored figure standing alone on the flat snow', '独自站在平坦雪地上的装甲身影'),
   room={'Scout'}, new=True, bg='Far away along the horizon stands the dark line of snow-laden pines.',
   holds='The frame holds exactly one armored figure, alone in the open snowfield, nobody else.')

TA('29-07', '07｜地表雪原：侦察兵单膝跪在雪地上，把一枚黑色圆盘放在雪里，红灯一下一下闪，他的手慢慢收回来', 6, FIELD_DISC,
   [P('scout', 'right', "kneeling on one knee in the snow in profile facing frame-left, both gloved hands just drawing back from the black disc lying flat on the snow in front of him", 'obj:the black disc on the snow', "his mouth and jaw hidden behind the black faceplate")],
   'Low shot at snow level, the disc in the middle third of the frame with the armored figure kneeling at frame-right.',
   "The small red light at the center of the black disc blinks steadily while <scout> draws his gloved hands slowly back from it and begins to rise, his mouth and jaw hidden behind the black faceplate. Nobody else is in the scene.",
   "黑色圆盘中心的小红灯稳稳地一下一下闪着，外骨骼侦察兵把戴手套的手慢慢从圆盘上收回来，开始站起身；他的嘴和下巴藏在黑色面罩后面。画面里没有别人。",
   SOUND_DISC, AES_DISC, cam=lowrise('the blinking disc and the rising armored figure', '闪着红光的圆盘和站起来的装甲身影'),
   extra_assets=('breach_disc',), room={'Scout'}, new=True,
   bg='In the foreground the black disc lies flat on the snow with its red light blinking, and the dark line of snow-laden pines stands far away.',
   holds='The frame holds exactly one armored figure kneeling beside the black disc, nobody else.')

TA('29-08', '08｜餐桌边：苏清月放下面包盯着监控墙，转头对林峰说那是军用破甲弹，他要炸开外壳；林峰把最后一口咖啡咽下去', 7, LIV_BF,
   [P('su_cozy', 'left', "sitting at the table in profile facing frame-right, the half-eaten slice lowered to her plate, her head turned from the monitors to him", 'Lin', "her lips parted, her face gone pale, her brows pulled together"),
    P('lin_home', 'center', "sitting at the table in profile facing frame-right, tipping the last of the coffee from the white mug into his mouth, his eyes on the wall of small monitors at frame-right", 'obj:the wall of small monitors at frame-right', "his jaw tight, his lips pressing flat, his brows low", outfit="in a soft grey henley and dark lounge pants")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dining table.',
   "<su_cozy> speaks the one line to <lin_home> in a tense, hurried voice, her lips parted, her face gone pale and her brows pulled together. <lin_home> swallows the last of his coffee calmly and sets the mug down on the table, his eyes on the monitors, his jaw tight, his lips pressing flat and his brows low.",
   "苏清月用紧绷急促的声音对林峰说出这一句，嘴唇微张、脸色发白、眉头拧在一起。林峰平静地咽下最后一口咖啡，把杯子放回桌上，眼睛盯着监控墙，下颌绷紧、嘴唇抿平、眉头压低。",
   SOUND_BF, AES_BF, lines=[('su_cozy', "那是军用破甲弹！他要炸开外壳！", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='At frame-right the wall of small monitors glows cool blue behind him and the black-and-gold stove glows warm at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, at the dining table, nobody else.')

TA('29-09', '09｜控制室：林峰坐进转椅，十指在键盘上飞快敲出一串红色指令，头也不回地对身后的苏清月说高级货就用点高级的死法', 8, CONTROL_C,
   [P('lin_home', 'right', "sitting in the black swivel chair at the console in profile facing frame-left, both hands flying across the keyboard, his head turned a little toward her", 'Su', "a cold thin curve at one corner of his mouth, his jaw tight, his brows low", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'center', "standing behind his chair in profile facing frame-left, one hand resting on the chair back", 'obj:the glowing console screens', "her lips pressed tight, her eyes wide, her brows pulled together")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "<lin_home> types fast, a column of red text racing across the screens, and speaks the one line to <su_cozy> in a low, cold, unhurried voice, a cold thin curve at one corner of his mouth, his jaw tight and his brows low. <su_cozy> watches the screens beside him, her lips pressed tight, her eyes wide and her brows pulled together.",
   "林峰飞快地敲着键盘，一列红色的字在屏幕上飞快滚过，同时用低沉冰冷、不紧不慢的声音对苏清月说出这一句，嘴角带着一丝冷冷的弧度、下颌绷紧、眉头压低。苏清月看着他身旁的屏幕，嘴唇紧抿、眼睛睁大、眉头拧在一起。",
   SOUND_KEY, AES_TEAL, lines=[('lin_home', "高级货，就用点高级的死法。", 1.0, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the wall of six small monitors glows at frame-left and the large red digital clock hangs high on the back wall.',
   holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

# ================================================================================================ 第 30 集
b30 = S.episode('剧本第30集｜死寂的电磁处决', '雪地上，圆盘的红灯越闪越快，侦察兵退后两步举起步枪，准备在炸开缺口的一瞬间冲进去；控制室里林峰说三二一，晚安，按下回车键；圆盘的红灯熄灭了，雪面上只有几缕蓝白色的电火花，没有爆炸声；侦察兵身上的灯全灭，面罩变得漆黑，他拼命去扯头盔，白霜一层层爬满装甲，最后直挺挺倒在雪地上；林峰坐回桌边吃剩下的半片面包，说再高级的盔甲也怕断电；收音机里忽然传出一个威严的声音：猎犬一号，收到请回答，猎犬一号失联，目标极度危险，启动备用计划，带上钻地导弹，去深山；苏清月和林峰对视，真正的军团盯上他们了，画面在急促的警报声中切黑。', 30)
b30.character('RadioCmd', 'radio_set', RADIOCMD_EN, RADIOCMD_ZH)

TA('30-01', '01｜地表雪原：圆盘的红灯越闪越快，侦察兵退后两步，举起步枪对准圆盘', 6, FIELD_DISC,
   [P('scout', 'right', "standing a few steps behind the black disc in profile facing frame-left, a compact black rifle raised to his shoulder and aimed toward the disc", 'obj:the black disc on the snow', "his mouth and jaw hidden behind the black faceplate")],
   'Medium wide shot, the black disc in the foreground and the armored figure at frame-right, in the middle third of the frame.',
   "The red light on the black disc blinks faster and faster while <scout> holds the rifle steady at his shoulder, standing perfectly still with his mouth and jaw hidden behind the black faceplate. Nobody else is in the scene.",
   "黑色圆盘上的红灯越闪越快，外骨骼侦察兵把步枪稳稳架在肩上，一动不动地站着，嘴和下巴藏在黑色面罩后面。画面里没有别人。",
   SOUND_DISC, AES_DISC, cam=push('the blinking disc and the armored figure beyond it', '闪着红光的圆盘和后面的装甲身影'),
   extra_assets=('breach_disc',), room={'Scout'}, new=True,
   bg='In the foreground the black disc lies flat on the snow with its red light blinking fast.',
   holds='The frame holds exactly one armored figure standing behind the black disc, nobody else.')

TA('30-02', '02｜控制室：林峰低声说三二一晚安，右手食指干脆地按下回车键，苏清月屏住呼吸', 7, CONTROL_C,
   [P('lin_home', 'right', "sitting in the black swivel chair at the console in profile facing frame-left, his right index finger resting over the big Enter key of the keyboard", 'obj:the glowing console screens', "a cold thin curve at one corner of his mouth, his jaw tight, his brows low", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'center', "standing behind his chair in profile facing frame-left, both hands pressed against her chest", 'obj:the glowing console screens', "her lips pressed tight, her eyes wide, her brows pulled together")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "<lin_home> speaks the one line to <su_cozy> in a low, cold voice, then presses his right index finger down on the Enter key with one firm tap, a cold thin curve at one corner of his mouth, his jaw tight and his brows low. <su_cozy> holds her breath beside him, her lips pressed tight, her eyes wide and her brows pulled together.",
   "林峰用低沉冰冷的声音对苏清月说出这一句，然后右手食指在回车键上干脆地按了一下，嘴角带着一丝冷冷的弧度、下颌绷紧、眉头压低。苏清月在他身旁屏住呼吸，嘴唇紧抿、眼睛睁大、眉头拧在一起。",
   SOUND_KEY, AES_TEAL, lines=[('lin_home', "三，二，一，晚安。", 0.8, 'Su')],
   cam=push1('Lin and the keyboard', '林峰和键盘'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the wall of six small monitors glows at frame-left and the large red digital clock hangs high on the back wall.',
   holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

insert2('30-03', '03｜插镜：雪地上，黑色圆盘的红灯已经熄灭，几缕蓝白色的电火花贴着雪面爬了一圈，然后消失，一片死寂', 5, FIELD_DEAD,
        'Low close shot of the dead disc on the snow in the middle third of the frame, nobody in the scene.',
        "Faint blue-white sparks crawl across the snow around the dark dead disc, flicker once and fade, and a thin curl of frost smoke rises and drifts away into the green aurora light, leaving a deep stillness. Nothing else moves.",
        "黑色圆盘中心的灯已经灭了，几缕淡淡的蓝白色电火花贴着圆盘周围的雪面爬行，闪了一下，消失，一缕细细的霜雾升起来，飘散在绿色极光的光里，只剩一片深深的静。别的什么都不动。",
        SOUND_SPARK, 'The frame holds the dead black disc on the snow, and nobody in the scene.',
        lowrise('the dead disc and the fading sparks', '熄灭的圆盘和渐渐消失的电火花'), AES_SPARK, extra_assets=('breach_disc',))

TA('30-04', '04｜地表雪原：侦察兵身上所有的指示灯全灭了，面罩变成一片漆黑，他僵在原地，双手慢慢抬向头盔', 6, FIELD,
   [P('scout', 'center', "standing rigid in the snow in profile facing frame-left, the compact rifle hanging from one hand, the dark dead armor without a single glowing light, his gloved hands slowly rising toward the neck ring of his helmet", 'obj:the neck ring of his own helmet', "his mouth and jaw hidden behind the black faceplate")],
   'Medium close shot, the armored figure from the head to the waist, in the middle third of the frame, in the open snowfield.',
   "<scout> stands rigid, his armor dark and dead, and a muffled labored groan escapes from his helmet as his gloved hands rise slowly toward the neck ring, his mouth and jaw hidden behind the dull black faceplate. Nobody else is in the scene.",
   "外骨骼侦察兵僵直地站着，装甲全暗、毫无生气，头盔里漏出一声被闷住的吃力的低哼，戴手套的双手慢慢抬向头盔的颈环，嘴和下巴藏在暗淡的黑色面罩后面。画面里没有别人。",
   SOUND_STILL, AES_FROST, cam=push1('the dead helmeted head and the rising hands', '熄灭的头盔和抬起的双手'), room={'Scout'}, new=True,
   bg='Behind him the open snowfield stretches away to the dark line of snow-laden pines.',
   holds='The frame holds exactly one armored figure standing rigid in the snow, nobody else.')

TA('30-05', '05｜地表雪原：侦察兵的手在头盔颈环上徒劳地扯着，白霜从他的手臂和肩甲上一层层爬上去，动作越来越慢，最后停住', 7, FIELD,
   [P('scout', 'center', "standing in the snow in profile facing frame-left, both gloved hands clawing at the neck ring of his helmet, white frost spreading over the dark plates of his arms and shoulders", 'obj:the neck ring of his own helmet', "his mouth and jaw hidden behind the black faceplate")],
   'Medium close shot, the armored figure from the head to the waist, in the middle third of the frame, in the open snowfield.',
   "<scout> claws at the neck ring of his helmet while a thick layer of white frost creeps over his arms and shoulders and his movements grow slower and slower until his hands stop and hang frozen at his helmet; his mouth and jaw stay hidden behind the black faceplate. Nobody else is in the scene.",
   "外骨骼侦察兵用力扯着头盔的颈环，一层厚厚的白霜爬上他的手臂和肩膀，他的动作越来越慢，最后双手停在头盔旁边，冻住了；他的嘴和下巴一直藏在黑色面罩后面。画面里没有别人。",
   SOUND_FREEZE, AES_FROST, cam=push1('the frosted helmet and hands', '结霜的头盔和双手'), room={'Scout'}, new=True,
   bg='Behind him the open snowfield stretches away to the dark line of snow-laden pines.',
   holds='The frame holds exactly one armored figure standing frosted in the snow, nobody else.')

TA('30-06', '06｜地表雪原：结满白霜的装甲身影像一根木桩一样慢慢向后倒下，直挺挺躺在雪地上，旁边是熄灭的圆盘', 6, FIELD_DEAD,
   [P('scout', 'center', "standing rigid in the snow in profile facing frame-left, sheathed in thick white frost and leaning slightly backward", 'obj:the dead disc on the snow in front of him', "his mouth and jaw hidden behind the frosted black faceplate")],
   'Wide shot, the frosted armored figure at frame-center with the dead disc in front of him, in the middle third of the frame.',
   "<scout> tips slowly backward like a felled post and lies flat on his back in the snow, a puff of powder rising around him, and then lies perfectly still beside the dead disc under the rippling green aurora. Nobody else is in the scene.",
   "结满白霜的外骨骼侦察兵像一根木桩一样慢慢向后倒下，平躺在雪地上，周围扬起一团粉雪，然后一动不动地躺在熄灭的圆盘旁边，头顶是流动的绿色极光。画面里没有别人。",
   SOUND_FALL, AES_AURORA, cam=pull('the frosted helmet', '结霜的头盔', 'the fallen figure, the dead disc and the vast snowfield', '倒下的身影、熄灭的圆盘和辽阔的雪原'),
   extra_assets=('breach_disc',), room={'Scout'}, new=True,
   bg='In front of him the dead black disc lies on the snow and the dark line of snow-laden pines stands far away.',
   holds='The frame holds exactly one armored figure, falling backward in the snow, nobody else.')

TA('30-07', '07｜餐桌边：林峰坐回桌边吃剩下的半片面包，苏清月说这就完了，林峰说再高级的盔甲也怕断电', 8, LIV_BF,
   [P('su_cozy', 'left', "sitting at the table in profile facing frame-right, both hands wrapped round her white mug, her head turned to him", 'Lin', "her lips parted, her eyes wide, her brows lifted"),
    P('lin_home', 'center', "sitting at the table in profile facing frame-left, lifting the last half slice of jam bread to his mouth", 'Su', "a lazy curve at one corner of his mouth, his jaw relaxed, his brows soft", outfit="in a soft grey henley and dark lounge pants")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dining table.',
   "<su_cozy> speaks the first line to <lin_home> in an amazed, breathless voice, her lips parted, her eyes wide and her brows lifted. <lin_home> takes an easy bite of the bread and answers with the second line to <su_cozy> in a low, lazy voice, a lazy curve at one corner of his mouth, his jaw relaxed and his brows soft.",
   "苏清月用惊讶、屏着气的声音对林峰说出第一句，嘴唇微张、眼睛睁大、眉毛上扬。林峰轻松地咬了一口面包，用低沉慵懒的声音对苏清月答出第二句，嘴角带着一丝懒懒的弧度、下颌放松、眉毛舒展。",
   SOUND_BF, AES_BF, lines=[('su_cozy', "这就完了？", 0.8, 'Lin'), ('lin_home', "再高级的盔甲，也怕断电。", 2.4, 'Su')],
   cam=push('both of them', '两人'), extra_assets=('jam_jar',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the black-and-gold stove glows warm at frame-left and the wall of small monitors glows cool blue at frame-right.',
   holds='The frame holds exactly two people: Su and Lin, at the dining table, nobody else.')

TAV('30-08', '08｜控制室：收音机的琥珀色刻度盘忽然亮起，传出一个威严的声音喊猎犬一号收到请回答，猎犬一号已失联，林峰和苏清月同时转头', CONTROL_R,
    [P('lin_home', 'right', "standing at the steel side table in profile facing frame-left, one hand holding the last piece of bread, his eyes on the radio", 'obj:the olive-green military radio on the side table', "his jaw tight, his lips set flat, his brows low", outfit="in a soft grey henley and dark lounge pants"),
     P('su_cozy', 'left', "standing beside him in profile facing frame-right, her arms folded tight, her eyes on the radio", 'obj:the olive-green military radio on the side table', "her lips parting, her brows pulled together")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the control console with the radio beside them.',
    "A stern, cold, authoritative middle-aged man's voice from the radio speaks the first line as a voice-over, then the second line, edged with static. <lin_home> stands without moving, his jaw tight, his lips set flat and his brows low. <su_cozy> freezes beside him, her lips parting and her brows pulled together.",
    "收音机里传出一个威严冰冷的中年男声，以旁白的方式说出第一句，接着说出第二句，带着沙沙的杂音。林峰站着一动不动，下颌绷紧、嘴唇抿平、眉头压低。苏清月在他身边僵住，嘴唇微张、眉头拧在一起。",
    SOUND_RADIO, AES_TEAL, lines=[('radio_cmd', "猎犬一号，收到请回答。", 0.8, 'Lin'), ('radio_cmd', "猎犬一号已失联。", 3.2, 'Lin')],
    cam=push('both of them', '两人'), extra_assets=('radio_set',), room={'Su', 'Lin'}, new=True,
    bg='Beside them on the steel side table the olive-green military radio glows with its amber dial, and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly two people: Su and Lin, at the control console with the radio beside them, nobody else.')

TAV('30-09', '09｜控制室：收音机里的声音说目标极度危险，启动备用计划，带上钻地导弹去深山；苏清月和林峰对视，红灯闪起、警报声响起', CONTROL_R,
    [P('lin_home', 'right', "standing at the steel side table in profile facing frame-left, turning his head to meet her eyes", 'Su', "his jaw tight, his eyes cold and steady, his brows low", outfit="in a soft grey henley and dark lounge pants"),
     P('su_cozy', 'left', "standing beside him in profile facing frame-right, turning her head to meet his eyes", 'Lin', "her lips pressed tight, her face pale, her brows pulled together")],
    'Close medium two-shot, both from the head to the chest, in the middle third of the frame, at the control console with the radio beside them.',
    "A stern, cold, authoritative middle-aged man's voice from the radio speaks the first line as a voice-over, then the second line, edged with static, while a small red alarm lamp on the wall begins to pulse. <su_cozy> and <lin_home> turn their heads and hold each other's eyes, her lips pressed tight, her face pale and her brows pulled together, and his jaw tight, his eyes cold and steady and his brows low.",
    "收音机里传出一个威严冰冷的中年男声，以旁白的方式说出第一句，接着说出第二句，带着沙沙的杂音，墙上的一盏小红灯开始一闪一闪。苏清月和林峰转过头，目光对在一起，她嘴唇紧抿、脸色发白、眉头拧在一起，他下颌绷紧、眼神冰冷而沉稳、眉头压低。",
    SOUND_RADIO_ALARM, AES_TEAL, lines=[('radio_cmd', "目标极度危险，启动备用计划。", 0.8, 'Lin'), ('radio_cmd', "带上钻地导弹，去深山。", 4.2, 'Lin')],
    cam=push('both of them', '两人'), extra_assets=('radio_set',), room={'Su', 'Lin'}, new=True,
    bg='Beside them on the steel side table the olive-green military radio glows with its amber dial, a small red alarm lamp on the wall behind them pulses red, and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly two people: Su and Lin, at the control console, nobody else.')

# ================================================================================================ 第 31 集
b31 = S.episode('剧本第31集｜黑色巨兽', '截获的电台里，威严的声音还在下令：钻地导弹已装车，四十分钟后抵达目标雪山；苏清月咬着嘴唇说我们的外壳防不住，必须转移；林峰说这是我的家，谁也别想让我搬走，连人带弹，一起送上天；他走到地下二层尽头的一面金属墙前按下指纹，金属墙向两边裂开，里面是一辆八米长的黑色哑光履带装甲房车，车头一把重型破冰铲，车顶一个热成像雷达圆罩；他把一套黑色防寒战术服递给苏清月：换上，今天带你兜风；五分钟后，黑色的钢铁巨兽冲进零下八十度的雪原，画面拉黑。', 31)
new_person(b31, 'su_tac', '苏清月（黑色棉服式战术防寒外套拉到锁骨，黑色保暖内衣，黑裤、黑手套，高马尾）', 'woman',
           'Su, the same elegant Chinese woman in her late twenties as in the reference, wearing a black quilted tactical cold-weather jacket zipped to the collarbone over a black thermal top, black trousers and black gloves, her long black hair in a high ponytail.',
           '苏清月，和参考图是同一位二十八岁左右、优雅美丽的中国女性，穿着拉到锁骨的黑色棉服式战术防寒外套，里面是黑色保暖上衣，黑裤子、黑手套，一头长黑发扎成高马尾。',
           'wearing a black quilted tactical cold-weather jacket zipped to the collarbone over a black thermal top, black trousers and black gloves, her long black hair in a high ponytail',
           'a determined, excited expression', ref='su_cozy')
b31.character('SuTac', 'su_tac', SU_EN, SU_ZH)
b31.prop('armored_rv', '履带式全地形装甲房车（八米长，哑光黑防弹装甲，车头厚重的钢制破冰铲，车顶热成像雷达圆罩，宽履带）',
         'An eight-metre long armoured tracked all-terrain motorhome in matte black, with a heavy steel ice-breaker blade at its front, a thermal-radar dome on its roof, wide tracks and a dark armoured windshield. The reference fixes its shape.',
         '一辆八米长的履带式全地形装甲房车：哑光黑色装甲，车头是厚重的钢制破冰铲，车顶有热成像雷达圆罩，宽宽的履带，深色的装甲挡风玻璃。参考图固定它的外形。',
         'A photorealistic product shot of an eight-metre long armoured tracked all-terrain motorhome in matte black with a heavy steel ice-breaker blade at its front, a thermal-radar dome on its roof, wide tracks and a dark armoured windshield, three-quarter view against a plain neutral gray background.')
new_scene(b31, 'garage_wall', '地下二层走廊尽头（灰色混凝土走廊，尽头是一整面拉丝钢大墙，墙上一块亮着微弱绿光的指纹板）',
          'A long grey concrete underground corridor that ends at a huge seamless brushed-steel wall, a small fingerprint pad with a faint green glow set into the wall at the right and a red emergency lamp on the ceiling at the left.',
          '一条长长的灰色混凝土地下走廊，尽头是一整面无缝的拉丝钢大墙，墙的右边嵌着一块亮着微弱绿光的指纹板，左边天花板上有一盏红色的应急灯。',
          'the long grey corridor, the huge brushed-steel wall and the glowing fingerprint pad')
new_scene(b31, 'bunker_garage', '地下二层隐蔽车库（空旷高大的灰色混凝土大厅，中间停着一辆黑色装甲房车，左侧金属墙已裂开）',
          'A vast, high grey concrete underground garage hall lit by cool white floodlights, with a matte-black armoured tracked motorhome parked in the middle and the huge steel wall split open at the left showing the corridor beyond.',
          '一座空旷高大的灰色混凝土地下车库大厅，冷白色的泛光灯照着，中间停着一辆哑光黑色的履带装甲房车，左侧巨大的钢墙已经裂开，露出后面的走廊。',
          'the vast grey garage hall, the matte-black armoured motorhome in the middle and the split-open steel wall at the left')

TAV('31-01', '01｜控制室：收音机里的威严声音继续下令，说钻地导弹已装车、四十分钟后抵达目标雪山，林峰和苏清月站在红灯下听着', CONTROL_R,
    [P('lin_home', 'right', "standing at the steel side table in profile facing frame-left, both arms folded, his eyes on the radio", 'obj:the olive-green military radio on the side table', "his jaw tight, his lips set flat, his brows low", outfit="in a soft grey henley and dark lounge pants"),
     P('su_cozy', 'left', "standing beside him in profile facing frame-right, one hand pressed against her mouth, her eyes on the radio", 'obj:the olive-green military radio on the side table', "her lips pressing tight, her brows pulled together")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the control console with the radio beside them.',
    "A stern, cold, authoritative middle-aged man's voice from the radio speaks the first line as a voice-over, then the second line, edged with static, while a small red alarm lamp on the wall pulses behind them. <lin_home> stands without moving, his jaw tight, his lips set flat and his brows low. <su_cozy> stands rigid beside him, her lips pressing tight and her brows pulled together.",
    "收音机里传出一个威严冰冷的中年男声，以旁白的方式说出第一句，接着说出第二句，带着沙沙的杂音，他们身后墙上的一盏小红灯一闪一闪。林峰站着一动不动，下颌绷紧、嘴唇抿平、眉头压低。苏清月僵在他身边，嘴唇紧抿、眉头拧在一起。",
    SOUND_RADIO, AES_TEAL, lines=[('radio_cmd', "钻地导弹已装车。", 0.8, 'Lin'), ('radio_cmd', "四十分钟后抵达目标雪山。", 3.0, 'Lin')],
    cam=push('both of them', '两人'), extra_assets=('radio_set',), room={'Su', 'Lin'}, new=True,
    bg='Beside them on the steel side table the olive-green military radio glows with its amber dial, a small red alarm lamp on the wall behind them pulses red, and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly two people: Su and Lin, at the control console, nobody else.')

TA('31-02', '02｜控制室：苏清月咬着嘴唇，手心全是汗，对林峰说外壳防不住，我们必须转移', 7, CONTROL_R,
   [P('su_cozy', 'left', "standing at the control console in profile facing frame-right, her fingers twisting in front of her, her head turned to him", 'Lin', "her lips caught between her teeth, her face pale, her brows pulled high"),
    P('lin_home', 'right', "standing at the steel side table in profile facing frame-left, one hand resting on the radio, his head turned to her", 'Su', "his jaw set, his eyes steady, his brows low", outfit="in a soft grey henley and dark lounge pants")],
   'Close medium two-shot, both from the head to the chest, in the middle third of the frame, at the control console.',
   "<su_cozy> speaks the one line to <lin_home> in a tight, shaking, urgent voice, her lips caught between her teeth, her face pale and her brows pulled high. <lin_home> listens calmly, his jaw set, his eyes steady and his brows low.",
   "苏清月用紧绷发抖又急促的声音对林峰说出这一句，嘴唇咬在牙齿间、脸色发白、眉毛高高挑起。林峰平静地听着，下颌绷住、眼神沉稳、眉头压低。",
   SOUND_CTRL, AES_TEAL, lines=[('su_cozy', "外壳防不住，我们必须转移！", 0.8, 'Lin')],
   cam=slide('right', '右', 'the two of them stand in the middle third of the frame', '两人占画面中间三分之一'), extra_assets=('radio_set',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the wall of six small monitors glows at frame-left and the olive-green military radio glows with its amber dial on the side table.',
   holds='The frame holds exactly two people: Su and Lin, at the control console, nobody else.')

TA('31-03', '03｜地下二层走廊：林峰大步走向尽头的金属大墙，说这是我的家，谁也别想让我搬走，连人带弹一起送上天，苏清月跟在身后', 10, GARAGE_DOOR,
   [P('lin_home', 'center', "striding along the concrete corridor in profile facing frame-right toward the huge steel wall, his fists loose at his sides", 'obj:the huge brushed-steel wall ahead of him', "his jaw set, his eyes cold and steady, his brows low", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'left', "hurrying a step behind him in profile facing frame-right, her eyes on his back", 'Lin', "her lips pressed tight, her brows pulled together")],
   'Wide tracking shot, both from the head to the knees, in the middle third of the frame, in the concrete corridor.',
   "<lin_home> strides toward the steel wall and speaks the first line to <su_cozy> in a low, iron-hard voice, then the second line in a colder voice, his jaw set, his eyes cold and steady and his brows low. <su_cozy> hurries a step behind him, her lips pressed tight and her brows pulled together.",
   "林峰大步走向那面钢墙，用低沉如铁的声音对苏清月说出第一句，接着用更冷的声音说出第二句，下颌绷住、眼神冰冷而沉稳、眉头压低。苏清月急急地跟在他身后一步，嘴唇紧抿、眉头拧在一起。",
   SOUND_CTRL, AES_PAD, lines=[('lin_home', "这是我的家，谁也别想让我搬走。", 0.8, 'Su'), ('lin_home', "连人带弹，一起送上天。", 4.6, 'Su')],
   cam=track('the two of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Ahead of them the huge brushed-steel wall fills the end of the corridor with a small fingerprint pad glowing green at frame-right.',
   holds='The frame holds exactly two people: Lin and Su, in the concrete corridor, nobody else.')

TA('31-04', '04｜地下二层走廊：林峰把拇指按在墙上的指纹板上，板子亮起绿光', 5, GARAGE_DOOR,
   [P('lin_home', 'center', "standing close to the steel wall in profile facing frame-right, his right thumb pressed flat on the glowing fingerprint pad", 'obj:the fingerprint pad under his thumb', "his jaw set, his lips pressed flat, his brows low", outfit="in a soft grey henley and dark lounge pants")],
   'Medium close shot, Lin from the head to the chest at the steel wall, in the middle third of the frame.',
   "<lin_home> holds his thumb on the fingerprint pad and the pad glows a steady green across his profile, his jaw set, his lips pressed flat and his brows low. Nobody else is in the corridor.",
   "林峰把拇指按在指纹板上不动，指纹板亮着稳稳的绿光，映在他的侧脸上，下颌绷住、嘴唇抿平、眉头压低。走廊里没有别人。",
   SOUND_PAD, AES_PAD, cam=push1('Lin and the glowing pad', '林峰和亮着绿光的指纹板'), room={'Lin'}, new=True,
   bg='Behind him the huge brushed-steel wall fills the frame.',
   holds='The frame holds exactly one person: Lin, at the steel wall, nobody else.')

TA('31-05', '05｜车库：钢墙已经向两边裂开，林峰和苏清月站在门口，面前是一座空旷的大厅，中间停着一辆黑色的装甲房车，苏清月惊得睁大了眼睛', 7, GARAGE,
   [P('lin_home', 'left', "standing in the opened doorway in profile facing frame-right, his hands in his pockets", 'obj:the matte-black armoured motorhome in the middle of the hall', "a cold satisfied curve at one corner of his mouth, his jaw relaxed, his brows soft", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'center-left', "standing beside him in the doorway in profile facing frame-right, one hand lifting toward her mouth", 'obj:the matte-black armoured motorhome in the middle of the hall', "her eyes wide, her lips parted, her brows lifted high")],
   'Wide shot from behind, the two of them small at frame-left, the vast garage hall and the black motorhome in the middle third of the frame.',
   "<lin_home> and <su_cozy> stand side by side in the opened doorway looking at the huge motorhome, his hands in his pockets with a cold satisfied curve at one corner of his mouth, his jaw relaxed and his brows soft, and her eyes wide, her lips parted and her brows lifted high. Nobody speaks.",
   "林峰和苏清月并排站在敞开的门口，看着那辆巨大的房车，他双手插在口袋里，嘴角带着一丝冷冷的满意的弧度、下颌放松、眉毛舒展，她眼睛睁大、嘴唇微张、眉毛高高扬起。没有人说话。",
   SOUND_GARAGE_B, AES_GARAGE, cam=rise('the whole vast garage hall with the black motorhome in the middle', '整座空旷的车库大厅和中间的黑色房车'),
   extra_assets=('armored_rv',), room={'Su', 'Lin'}, new=True,
   bg='In the middle of the hall stands the eight-metre long matte-black armoured tracked motorhome with a heavy ice-breaker blade at its front and a radar dome on its roof.',
   holds='The frame holds exactly two people: Lin and Su, small in the doorway, nobody else.')

insert2('31-06', '06｜插镜：黑色装甲房车的车头，厚重的破冰铲、深色的挡风玻璃和车顶的雷达圆罩，在冷白色的灯光里泛着光', 6, GARAGE_RV,
        'Low close shot of the front of the motorhome, the ice-breaker blade and the windshield in the middle third of the frame, nobody in the scene.',
        "Cool white light slides slowly along the heavy steel ice-breaker blade, the dark armoured windshield and the thermal-radar dome of the matte-black motorhome while fine dust drifts through the beams. Nothing else moves.",
        "冷白色的光慢慢滑过哑光黑色房车厚重的钢制破冰铲、深色的装甲挡风玻璃和车顶的热成像雷达圆罩，细细的灰尘在光束里飘。别的什么都不动。",
        SOUND_RV_IDLE, 'The frame holds the front of the matte-black armoured motorhome with its ice-breaker blade, windshield and radar dome, and nobody in the scene.',
        lowrise('the ice-breaker blade, the windshield and the radar dome', '破冰铲、挡风玻璃和雷达圆罩'), AES_GARAGE, extra_assets=('armored_rv',))

TA('31-07', '07｜车库：林峰把一件折好的黑色防寒战术服递给苏清月，说换上，今天带你兜风，她接过来，眼睛亮了，说我早就想看看外面', 9, GARAGE_HANDOVER,
   [P('lin_home', 'right', "standing in front of the motorhome in profile facing frame-left, holding out a neatly folded black tactical cold-weather jacket in both hands", 'Su', "a quiet warm curve at one corner of his mouth, his jaw relaxed, his brows soft", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'left', "standing in front of the motorhome in profile facing frame-right, reaching out with both hands to take the folded jacket", 'obj:the folded jacket in his hands', "her eyes bright, her lips parting in an eager sweet smile, her brows lifted")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in front of the motorhome.',
   "<lin_home> holds out the folded jacket and speaks the first line to <su_cozy> in a low, warm voice, a quiet warm curve at one corner of his mouth and his brows soft. <su_cozy> takes it in both hands and speaks the second line to <lin_home> in a bright, eager voice, her eyes bright, her lips parting in an eager sweet smile and her brows lifted.",
   "林峰把折好的外套递过去，用低沉温暖的声音对苏清月说出第一句，嘴角带着一丝安静的暖意、眉毛舒展。苏清月用双手接过来，用明亮急切的声音对林峰说出第二句，眼睛发亮、嘴唇绽开急切的甜笑、眉毛上扬。",
   SOUND_GARAGE, AES_GARAGE, lines=[('lin_home', "换上，今天带你去兜风。", 0.8, 'Su'), ('su_cozy', "我早就想看看外面了。", 3.2, 'Lin')],
   cam=slide('left', '左', 'the two of them stand in the middle third of the frame with the folded jacket between them', '两人占画面中间三分之一、中间是那件折好的外套'),
   extra_assets=('armored_rv',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the long flank of the matte-black motorhome fills the back of the frame and a steel workbench stands at frame-left.',
   holds='The frame holds exactly two people: Lin and Su, in front of the motorhome, nobody else.')

insert2('31-08', '08｜地表雪原：黑色的钢铁巨兽在雪原上狂奔，履带卷起漫天雪雾，留下两道深深的辙痕，头顶是流动的极光', 7, SNOW_RV,
        'Wide aerial shot of the snowfield, the black motorhome crossing the middle third of the frame, nobody visible.',
        "The matte-black armoured motorhome thunders across the snowfield on its wide tracks, hurling a long plume of powdery snow into the air behind it and carving two deep tread lines across the white while the green aurora ripples above. Nothing else moves.",
        "哑光黑色的装甲房车在宽宽的履带上轰鸣着驶过雪原，在身后抛起一长条粉雪，在白色的雪地上碾出两道深深的辙痕，头顶的绿色极光在流动。别的什么都不动。",
        SOUND_ROAR, 'The frame holds the open snowfield with the black motorhome crossing it, and nobody visible.',
        drop('the black motorhome and its plume of snow', '黑色房车和它扬起的雪雾'), AES_SNOWRV, extra_assets=('armored_rv',))

# ================================================================================================ 第 32 集
b32 = S.episode('剧本第32集｜冰原狂飙', '一片纯白的雪原上，幽绿的极光像巨大的帷幕，一辆漆黑的履带装甲车如履平地；驾驶舱里却开着26度的暖风，苏清月脱了厚外套，只穿黑色保暖衣，手里捧着一杯冒着热气的咖啡；她看着窗外的极光，又看了一眼单手握着操纵杆的林峰，笑着说开着装甲车喝着热咖啡去杀人，林老板你真是把末日过成了度假；林峰说只要有我在，你每一天都是度假；突然雷达发出急促的滴滴声，屏幕上一串红点沿着十公里外的冰谷排开，那是带着钻地导弹的官方车队；林峰眼神瞬间像孤狼一样冷下来：找到了，坐稳，好戏开场；装甲车猛地加速冲向冰谷上方，画面切断。', 32)
new_person(b32, 'su_tacfit', '苏清月（黑色长袖保暖上衣，黑裤，黑色棉服外套叠在腿上，高马尾）', 'woman',
           'Su, the same elegant Chinese woman in her late twenties as in the reference, wearing a fitted black long-sleeve thermal top and black trousers, her black quilted jacket folded over her knees, her long black hair in a high ponytail.',
           '苏清月，和参考图是同一位二十八岁左右、优雅美丽的中国女性，穿着修身的黑色长袖保暖上衣和黑裤子，黑色棉服外套叠放在膝盖上，一头长黑发扎成高马尾。',
           'wearing a fitted black long-sleeve thermal top and black trousers, her black quilted jacket folded over her knees, her long black hair in a high ponytail',
           'a relaxed, content expression', ref='su_cozy')
b32.character('SuTacfit', 'su_tacfit', SU_EN, SU_ZH)
new_scene(b32, 'rv_cab', '装甲房车驾驶舱（两张皮质座椅并排，中间两个冒热气的咖啡杯，仪表盘上的小雷达屏，宽大的装甲挡风玻璃外是蓝白雪原和极光）',
          'The compact warm cab of an armoured motorhome in a cutaway side view: two leather bucket seats side by side facing a wide armoured windshield, a console between them with two steaming paper cups, a short steel control lever and a small round radar screen in the dashboard, with a vast blue-white snowfield and a green aurora beyond the glass.',
          '一辆装甲房车温暖紧凑的驾驶舱，侧剖视角：两张皮质座椅并排，面向宽大的装甲挡风玻璃，中间的控制台上放着两个冒着热气的纸杯，旁边有一根短短的钢制操纵杆，仪表盘上嵌着一块圆形的小雷达屏，玻璃外是辽阔的蓝白雪原和绿色的极光。',
          'the two leather seats, the two steaming cups, the small radar screen and the windshield with the snowfield and aurora')

insert2('32-01', '01｜地表雪原：一辆黑色的履带装甲车在一望无际的雪原上缓缓前行，卷起一道雪雾，头顶是巨大的绿色极光帷幕', 7, SNOW_RV,
        'Wide aerial shot of the vast snowfield, the tiny black motorhome in the middle third of the frame, nobody visible.',
        "The tiny matte-black armoured motorhome glides across the vast white snowfield on its wide tracks, trailing a long ribbon of powdery snow mist and two deep tread lines while a huge green aurora curtain ripples across the black sky above. Nothing else moves.",
        "小小的哑光黑色装甲房车在辽阔的白色雪原上平稳地滑行，身后拖着一条长长的粉雪雾带和两道深深的辙痕，头顶巨大的绿色极光帷幕在漆黑的天空里流动。别的什么都不动。",
        SOUND_ROAR, 'The frame holds the vast snowfield with the tiny black motorhome and the aurora above it, and nobody visible.',
        rise('the vast snowfield, the tiny black motorhome and the huge aurora curtain', '辽阔的雪原、小小的黑色房车和巨大的极光帷幕'), AES_SNOWRV, extra_assets=('armored_rv',))

TA('32-02', '02｜驾驶舱：暖光里，苏清月穿着黑色保暖衣捧着热咖啡望着窗外的极光，林峰单手握着操纵杆开车', 6, CAB,
   [P('su_tacfit', 'left', "sitting in the passenger seat in profile facing frame-right, both hands wrapped round a steaming paper cup, her eyes on the aurora beyond the windshield", 'obj:the green aurora beyond the windshield', "a soft content sweet smile on her lips, her eyes bright, her brows soft"),
    P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, one hand resting easily on the short steel control lever", 'obj:the snowfield beyond the windshield', "a faint relaxed curve at one corner of his mouth, his jaw relaxed, his brows soft", outfit="in a charcoal henley under a dark olive utility vest")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<su_tacfit> sips her coffee and gazes at the aurora, a soft content sweet smile on her lips, her eyes bright and her brows soft, while <lin_work> drives with one easy hand on the lever, a faint relaxed curve at one corner of his mouth, his jaw relaxed and his brows soft. Steam curls up from the two cups. Nobody speaks.",
   "苏清月啜着咖啡，望着窗外的极光，嘴角带着柔和满足的甜笑、眼睛发亮、眉毛舒展，林峰一只手轻松地搭在操纵杆上开着车，嘴角带着一丝放松的弧度、下颌放松、眉毛舒展。两只杯子里冒着热气。没有人说话。",
   SOUND_CAB_B, AES_CAB, cam=slide('right', '右', 'the two of them sit in the middle third of the frame with the aurora beyond the glass', '两人占画面中间三分之一、玻璃外是极光'),
   room={'Su', 'Lin'}, new=True,
   bg='Between them two steaming paper cups stand in the cup holders and beyond the windshield a green aurora ripples over the blue-white snowfield.',
   holds='The frame holds exactly two people: Su and Lin, sitting side by side in the cab, nobody else.')

TA('32-03', '03｜驾驶舱：苏清月回过头看着林峰，轻笑着说开着装甲车喝热咖啡去杀人，林老板你把末日过成了度假', 10, CAB,
   [P('su_tacfit', 'left', "sitting in the passenger seat in profile facing frame-right, a steaming paper cup raised in one hand, her head turned to him", 'Lin', "a teasing sweet smile on her lips, her eyes sparkling, her brows lifted"),
    P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, one hand resting on the control lever, his eyes on the snowfield", 'obj:the snowfield beyond the windshield', "one corner of his mouth lifting, his jaw relaxed, his brows soft", outfit="in a charcoal henley under a dark olive utility vest")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<su_tacfit> speaks the first line to <lin_work> in a light, teasing voice and then the second line in a warmer voice, a teasing sweet smile on her lips, her eyes sparkling and her brows lifted. <lin_work> keeps his hand on the lever and his eyes ahead, one corner of his mouth lifting, his jaw relaxed and his brows soft.",
   "苏清月用轻快逗弄的声音对林峰说出第一句，接着用更温暖的声音说出第二句，嘴角带着逗弄的甜笑、眼睛发亮、眉毛上扬。林峰一只手搭在操纵杆上，眼睛看着前方，嘴角微微上扬、下颌放松、眉毛舒展。",
   SOUND_CAB, AES_CAB, lines=[('su_tacfit', "开着装甲车，喝着热咖啡去杀人。", 0.8, 'Lin'), ('su_tacfit', "林老板，你把末日过成了度假。", 4.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Between them two steaming paper cups stand in the cup holders and beyond the windshield a green aurora ripples over the blue-white snowfield.',
   holds='The frame holds exactly two people: Su and Lin, sitting side by side in the cab, nobody else.')

TA('32-04', '04｜驾驶舱：林峰偏过头看着苏清月，嘴角一扬，说只要有我在，你每一天都是度假', 7, CAB,
   [P('su_tacfit', 'left', "sitting in the passenger seat in profile facing frame-right, her cup lowered to her lap, her head turned to him", 'Lin', "a soft surprised sweet smile on her lips, her eyes bright, her brows lifted"),
    P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-left, one hand on the control lever, his head turned to her", 'Su', "one corner of his mouth lifting, his eyes warm and sure, his brows soft", outfit="in a charcoal henley under a dark olive utility vest")],
   'Close medium two-shot, both from the head to the chest, in the middle third of the frame, in the cab.',
   "<lin_work> turns his head and speaks the one line to <su_tacfit> in a low, warm, sure voice, one corner of his mouth lifting, his eyes warm and sure and his brows soft. <su_tacfit> listens, a soft surprised sweet smile spreading on her lips, her eyes bright and her brows lifted.",
   "林峰偏过头，用低沉温暖、笃定的声音对苏清月说出这一句，嘴角微微上扬、眼神温暖笃定、眉毛舒展。苏清月听着，嘴角慢慢绽开柔和又惊讶的甜笑、眼睛发亮、眉毛上扬。",
   SOUND_CAB, AES_CAB, lines=[('lin_work', "只要有我在，你每天都是度假。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Between them two steaming paper cups stand in the cup holders and beyond the windshield a green aurora ripples over the blue-white snowfield.',
   holds='The frame holds exactly two people: Lin and Su, sitting side by side in the cab, nobody else.')

insert2('32-05', '05｜插镜：仪表盘上的小雷达屏幕，绿色的圆环上突然出现一长串红点，沿着一条窄窄的线排开，屏幕在急促地嘀嘀响', 6, CAB_RADAR,
        'Close shot of the small radar screen in the dashboard, its round screen in the middle third of the frame, nobody in the scene.',
        "A long chain of small bright red dots strung along a narrow line pulses on the green concentric rings of the radar screen while the screen beeps quickly and the warm amber dashboard light flickers across it. Nothing else moves.",
        "仪表盘上小雷达屏幕的绿色同心圆上，一长串明亮的小红点沿着一条窄窄的线排开，一闪一闪，屏幕急促地嘀嘀作响，温暖的琥珀色仪表灯光在上面轻轻闪烁。别的什么都不动。",
        SOUND_BEEP, 'The frame holds the small radar screen with its green rings and the chain of red dots, and nobody in the scene.',
        push1('the chain of red dots on the radar screen', '雷达屏幕上那一串红点'), AES_RADAR)

TA('32-06', '06｜驾驶舱：林峰的眼神一下子冷下来，像孤狼一样盯着前方，说找到了，坐稳，好戏开场，苏清月一把抓住扶手', 8, CAB,
   [P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, both hands now gripping the control lever, his eyes locked on the windshield", 'obj:the snowfield beyond the windshield', "his eyes narrowing like a lone wolf's, his jaw clenched, his lips pressed hard, his brows low", outfit="in a charcoal henley under a dark olive utility vest"),
    P('su_tacfit', 'left', "sitting in the passenger seat in profile facing frame-right, one hand clutching the grab handle above the door, her cup set down in its holder", 'Lin', "her lips parted, her eyes wide, her brows pulled together")],
   'Medium two-shot from a low angle, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<lin_work> speaks the one line to <su_tacfit> in a low, cold, deadly calm voice, his eyes narrowing like a lone wolf's, his jaw clenched, his lips pressed hard and his brows low. <su_tacfit> grabs the handle and braces, her lips parted, her eyes wide and her brows pulled together.",
   "林峰用低沉冰冷、杀气腾腾却平静的声音对苏清月说出这一句，眼睛像孤狼一样眯起、下颌咬紧、嘴唇用力抿着、眉头压低。苏清月一把抓住扶手，身体绷紧，嘴唇微张、眼睛睁大、眉头拧在一起。",
   SOUND_CAB, AES_CAB, lines=[('lin_work', "找到了。坐稳，好戏开场。", 0.8, 'Su')],
   cam=lowrise('Lin and Su', '林峰和苏清月'), room={'Su', 'Lin'}, new=True,
   bg='Between them one steaming paper cup stands in a cup holder and the small radar screen glows green in the dashboard at frame-right.',
   holds='The frame holds exactly two people: Lin and Su, sitting side by side in the cab, nobody else.')

insert2('32-07', '07｜地表雪原：黑色的装甲房车猛地加速，咆哮着冲上长长的雪坡，雪浪从两侧翻起，直扑山脊', 6, SNOW_RIDGE,
        'Low wide shot at snow level, the black motorhome charging up the slope in the middle third of the frame, nobody visible.',
        "The matte-black armoured motorhome charges up the long snow slope with a thundering roar, its wide tracks hurling two great waves of snow to either side as it surges toward the ridge under the rippling green aurora. Nothing else moves.",
        "哑光黑色的装甲房车轰鸣着冲上长长的雪坡，宽宽的履带把两大片雪浪抛向两侧，在流动的绿色极光下直扑向山脊。别的什么都不动。",
        SOUND_ROAR, 'The frame holds the long snow slope with the black motorhome charging up it, and nobody visible.',
        lowrise('the black motorhome charging up the slope', '冲上雪坡的黑色房车'), AES_SNOWRV, extra_assets=('armored_rv',))

doc = S.finish()
