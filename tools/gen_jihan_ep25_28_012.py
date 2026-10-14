#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 25–28 集，追加稿 012（2026-10-14）。以 011 的 JSON 为底（style／素材／角色逐字复制），必须等 011 在插件里全部跑完再追加。
hh 2026-10-14 14:58：“继续吧。镜头感还是不够好莱坞大片感，镜头画面需要唯美。其他方面暂时没有什么问题，你继续保持之前的吧。”

写法＝011 同一套（每个任务先定景别＋机位＋运镜；每句台词带语气；两人以上写 exactly N people；dep 一律不用；对话任务 ≤12 秒；机械／物理变化只拍结果）。
本批新增：每个任务多写一句“光和空气”（主光＋轮廓光＋冷暖对比＋飘着的东西），同时放进开场图文字和视频文字（见技巧文档第二十三节）；
  每集至少一个低机位上摇、一个起重机下降／上升、一个光的特写插镜；环绕镜头只用一次（25-03）。
偏离大纲（交稿时已告诉 hh）：
  · 第 25 集：“黑胶唱片机”（带电）改成黄铜大喇叭、手摇的老留声机（不带电、不是电子娱乐）；“壁炉前”改成厨房炉火旁的羊毛地毯；
    “拔掉电源线”只拍一个 6 秒任务（开场图是手握着线、临拔前），拔掉之后收音机灯灭、静电声切断；雷达的“红色不规则阴影”用画面里的雷达屏幕拍，不写屏幕上的字；
  · 第 26 集：“扯下衬衫扣子换战术服”改成他从门边墙钩上取下白色极地服（不脱衣服）；“冰震”只拍杯中水纹、吊灯摇晃、天花板掉灰和碎块，不拍墙壁变形；
    “弃点逃生”改成“要逃出去吗”；苏清月在这集不说要跟去（第 27 集她拿着喷枪出现是惊喜）；
  · 第 27 集：林峰穿白色极地服（不是紧身战术服）、苏清月穿奶白羽绒服；“手臂青筋暴起”改成呼出白雾、整个人压在轮子上；阀门开启只拍结果（轮子转了、压力表指针落下）；
    水管爆裂只拍一个 6 秒任务，“金属碎片如子弹”改成“水柱和冰碴”；
  · 第 28 集：伤口只拍袖子被划开、渗红，不拍“深可见骨”；“蒙太奇”拆成包扎、揉面、烤箱、出炉四个任务；新增“外骨骼侦察兵”（头盔全遮脸，没有台词，下一集才说话）。
H3 方面的风险（交稿时单列，不算我的错）：
  · 25-01 拔线（快动作＋灯灭）；25-03 环绕镜头（人脸可能变形）；25-04 唱针落下、唱片转（机械）；25-05 切番茄（刀＋汁）；25-06 起重机下降（人从小变大）；
  · 26-02 杯中水纹；26-04、26-08 吊灯摇晃、掉灰、掉碎块；26-07 从墙钩取极地服；
  · 27-01 厚重隔离门开着、白雾里的手电光束；27-03 阀门纹丝不动（人用力却不动）；27-06 轮子被转动、冰块崩落；27-07 压力表指针下落；27-08 水管爆开＋林峰扑过去（快动作）；
  · 28-03 缠纱布；28-06 端出一盘面包；28-07、28-08 外骨骼侦察兵（脸全遮、新人物没有任何数据）；开场图约一成不按文字画；“同一处”场景用参照图。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _jihan_base5 import *

OUT = '合并稿/012_第25-28集_拔线子留声机冰震冰窖阀门面包香_制作稿_追加'
S = Session('合并稿/011_第21-24集_盲盒窄井越界幽灵电台_制作稿_追加.json', OUT, 44000)


# ---------------------------------------------------------------------------------------------- 运镜（新增）
def arc(who_en, who_zh, to_en, to_zh):
    return (f'The camera arcs slowly around {who_en} toward frame-right until {to_en}.', f'镜头缓缓绕着{who_zh}向右环绕，直到{to_zh}。')


def drop(to_en, to_zh):
    return (f'The camera starts high above and sinks slowly on a crane until {to_en} fill the middle third of the frame.',
            f'镜头从高处开始，像吊臂一样缓缓降下来，直到{to_zh}占满画面中间三分之一。')


# ---------------------------------------------------------------------------------------------- 光和空气（唯美）
AES_TEAL = ("The cool blue-green glow of the console screens on one side and the warm amber lamp on the other split the light into a rich teal-and-orange contrast that rims the edges of everything.",
            "控制台屏幕蓝绿色的光在一侧，温暖的琥珀灯光在另一侧，把光分成浓郁的青橙对比，勾出每样东西的轮廓。")
AES_AMBER = ("Golden amber lamp light wraps the scene with a soft warm rim light on hair and shoulders, tiny dust motes drift through the beams and the far lights melt into soft golden bokeh.",
             "金黄的暖灯光裹住画面，头发和肩膀上有一圈柔和的暖色轮廓光，细小的尘埃在光束里缓缓飘，远处的灯光化成柔软的金色光斑。")
AES_KITCH = ("Honey-gold light from the pendant lamp pools on the marble counter, wisps of steam from the stove curl through the beam and the red of the tomato glows like a jewel.",
             "蜂蜜般的金色吊灯光洒在大理石台面上，炉子的蒸汽一缕缕卷过光束，番茄的红像宝石一样发亮。")
AES_RED = ("A slow red warning pulse washes the room and rim-lights the edges of everything, with a deep darkness falling off at the edges of the frame.",
           "缓慢的红色警报光脉动着漫过房间，给所有东西的边缘描上红边，画面四周落入深深的暗。")
AES_DUSTRED = ("Warm amber lamp light mixes with a faint red pulse from the radar, and fine white dust glitters in the beams.",
               "温暖的琥珀灯光里混进雷达发出的淡淡红色脉动，细细的白色灰尘在光束里闪着光。")
AES_FOG = ("Thick white fog rolls through the flashlight beam in visible shafts of light and the frost on the pipes glitters like crushed diamonds, with a thin line of warm orange light behind the open door.",
           "浓浓的白雾在手电光束里翻滚，形成一束束看得见的光柱，管道上的霜像碎钻一样闪光，敞开的门后有一线温暖的橙色光。")
AES_ICEWARM = ("Pale blue ice-light on one side and a warm orange glow spilling from the open door on the other give a teal-and-orange contrast, and fine ice crystals glitter in the air.",
               "一侧是淡蓝色的冰光，另一侧是从敞开的门里漏出来的温暖橙光，形成青橙对比，空气里细小的冰晶闪着光。")
AES_FLAME = ("A hard blue flame lights the frost from below while the orange glow of the open door warms the far wall, and glittering ice crystals and rolling steam fill the air.",
             "一团坚硬的蓝色火焰从下方照亮霜层，敞开的门里漏出的橙光暖暖地照着远处的墙，闪光的冰晶和翻滚的蒸汽充满空气。")
AES_BREAD = ("Honey-gold light from the pendant lamp and the orange glow of the oven wrap the frame, backlit wisps of steam and floating flour dust catch the light and the whole picture glows golden.",
             "吊灯蜂蜜般的金光和烤箱的橙色光裹住画面，逆光里的蒸汽和飘着的面粉粉尘闪着光，整个画面金灿灿的。")
AES_AURORA = ("A faint green aurora ripples across the black sky and its light glitters on the snow, and powdery snow crystals sparkle as they blow through the air.",
              "一片淡淡的绿色极光在漆黑的天空里流动，光洒在雪地上闪着光，被风吹起的粉雪晶体在空气里闪烁。")


def TA(tid, title, dur, scene, people, framing, act_en, zh, sound, aes, **kw):
    kw['bg'] = (kw.get('bg', '') + ' ' + aes[0]).strip()
    return S.T(tid, title, dur, scene, people, framing, act_en.rstrip() + ' ' + aes[0], zh.rstrip() + aes[1], sound, **kw)


def insert2(tid, title, dur, scene, framing, act_en, zh, snd, holds, cam, aes, extra_assets=(), groups=()):
    return S.T(tid, title, dur, scene, [], framing, act_en.rstrip() + ' ' + aes[0], zh.rstrip() + aes[1], snd, cam=cam, holds=holds,
               room={g[0] for g in groups}, groups=list(groups), new=True, bg=aes[0], extra_assets=extra_assets)


# ---------------------------------------------------------------------------------------------- 新外貌
look('su_silk', 'SuSilk', "in a long wine-red satin robe-style nightgown with long sleeves and a high neckline belted at the waist, a white towel around her neck, her damp long black hair loose over her shoulders", 'soft dark-brown', 'her', eth=CN_F28)
look('scout', 'Scout', "in a sleek matte-white military polar exoskeleton armor with articulated servo joints, a full white helmet with a black tinted faceplate hiding his whole face, and a slim black survey probe in one gloved hand", 'visor-covered', 'his', eth='a tall armored soldier')
SCOUT_EN = 'A flat, cold synthetic adult male voice filtered through a helmet speaker, speaking clear Mandarin Chinese.' + VT_EN
SCOUT_ZH = '经过头盔扬声器处理的、平板冰冷的合成感成年男声，普通话清楚。' + VT_ZH

# ---------------------------------------------------------------------------------------------- 场景
CONTROL_R = Scene('bunker_control', CONTROL.end, CONTROL.layout + " A steel side table at frame-right holds an olive-green military long-wave radio with a large round dial glowing amber, a pole antenna and a cloth speaker grille.")
GRAM_TXT = (" A brass-horn hand-crank gramophone with a black record on its turntable stands on a small wooden cabinet beside the dining table at frame-center-right, and a rugged olive-drab geological radar unit with a small round dark screen stands on a steel tripod at frame-right in front of the monitor wall; a heavy white polar suit hangs on a wall hook beside the round hatch door at far frame-right.")
LIV_GR = Scene('bunker_living', LIVING.end, LIVING.layout + GRAM_TXT)
GRAM_CLOSE = Scene('bunker_living', LIVING.end,
                   " Fixed stage layout: a hand-crank gramophone with a polished brass horn stands on a small dark wooden cabinet in the middle of the frame, a black record on its turntable and the slim tonearm resting above it; behind it the thick cream rug and the round wooden dining table glow softly in the warm light.")
RADAR_SCR = Scene('bunker_living', " The cozy room behind glows warm amber, with a faint pulsing red wash creeping across it.",
                  " Fixed stage layout: a rugged olive-drab geological radar unit stands on a steel tripod in the middle of the frame, its round screen glowing green with concentric rings and a small red lamp on top; behind it the round wooden dining table with two white bowls and the wall of small monitors glow warm.")
RADAR_RED = Scene('bunker_living', " The cozy room behind is washed in a slow pulsing red glow.",
                  " Fixed stage layout: a rugged olive-drab geological radar unit stands on a steel tripod in the middle of the frame, its round screen glowing green with concentric rings; a vast irregular red shadow now covers half of the screen and presses toward a small bright green square at its center; the small red lamp on top of the unit flashes; behind it the round wooden dining table with two white bowls and the wall of small monitors glow dimly.")
WATER = Scene('bunker_living', LIVING.end,
              " Fixed stage layout: on the small round wooden dining table in the middle of the frame stand a clear glass of water and two white porcelain bowls with chopsticks resting across them; the black-and-gold stove glows warm at frame-left; the wall of small monitors is at frame-center-right.")
CEIL = Scene('bunker_living', LIVING.end,
             " Fixed stage layout: the thick cream rug and the small round wooden dining table lie in the lower part of the frame; above them a round pendant lamp hangs from a visible seam in the grey concrete ceiling; the black-and-gold stove glows at frame-left.")
DEBRIS = Scene('bunker_living', " The cozy room is washed in a slow pulsing red glow.",
               " Fixed stage layout: the small round wooden dining table with two white bowls stands in the lower middle of the frame; above it a hairline split has opened in the grey concrete ceiling seam with a fine veil of dust sifting from it, and a round pendant lamp hangs below the split; the black-and-gold stove glows at frame-left.")
ICE = Scene('ice_hall', " Bright white flashlight beams cut through drifting white fog in the freezing hall, and a thin line of warm orange light leaks in through the open door.",
            " Fixed stage layout: a heavy round steel isolation door stands open at frame-left with white fog rolling out of it; thick pipes furred with white hoar frost run along the ceiling and the right wall; long icicles hang from the ceiling; the concrete floor is glazed with ice; at the far end in the middle of the frame stands a huge red cast-iron gear valve over a metre across, rimed with ice.")
ICE_GEAR = Scene('ice_hall', ICE.end,
                 " Fixed stage layout: the huge red cast-iron gear teeth of the valve wheel fill the middle of the frame, thick with white frost and ice; the frost-furred pipes run behind them in the fog.")
ICE_GAUGE = Scene('ice_hall', ICE.end,
                  " Fixed stage layout: a big round pressure gauge with a red danger zone hangs on a frost-furred pipe in the middle of the frame, its needle deep in the red; a thick relief pipe rises above it; the huge red gear valve stands clear behind it at frame-right; the frosted hall fills the background.")
ICE_BURST = Scene('ice_hall', ICE.end,
                  ICE.layout + " An old side pipe on the right wall has just split open and is spraying a fan of water and ice shards across the hall toward the valve.")
ICE_AFTER = Scene('ice_hall', " Pale blue ice-light fills the freezing hall, thin white mist drifts through it and a warm orange glow spills in through the open door.",
                  ICE.layout + " The split side pipe on the right wall hangs open and drips; ice shards lie scattered across the glazed floor; the big valve wheel stands partly turned.")
SOFA_AID = Scene('bunker_sofa', SOFA.end,
                 SOFA.layout + " A white first-aid box lies open on the coffee table with rolls of gauze and a small bottle of antiseptic.")
KITCH_BREAD = Scene('bunker_living', LIVING.end,
                    " Fixed stage layout: the open kitchen is at frame-left, a floured wooden board holding a smooth mound of dough on the marble counter beside a bag of white flour, a block of butter and a small jar of yeast, a round pendant lamp hanging low over the counter and the black-and-gold stove with a glass-windowed oven door beside it; the thick cream rug and the small round wooden dining table fill the middle of the frame; the wall of small monitors is at frame-center-right.")
OVEN = Scene('bunker_living', LIVING.end,
             " Fixed stage layout: the glass-windowed oven door of the black-and-gold stove glows orange in the middle of the frame, three round golden-brown loaves swelling behind the glass; a floured wooden counter is at frame-left.")
OVEN_OPEN = Scene('bunker_living', LIVING.end,
                  " Fixed stage layout: the black-and-gold stove with its oven door open and the oven rack pulled out stands in the middle of the frame, a warm orange glow pouring from the oven; the floured marble counter is at frame-left; the cream rug and the round wooden dining table fill the background.")

# ---------------------------------------------------------------------------------------------- 声音
SOUND_CTRL_QUIET = breathy('Crackling radio static that cuts off sharply into a deep, heavy silence, with only the faint hum of the control room.', '收音机沙沙的杂音忽然被切断，变成深沉厚重的寂静，只剩控制室轻微的嗡鸣。')
SOUND_CTRL_SILENT = voiced('The faint hum of the control room and a deep, heavy silence where the radio used to hiss.', '控制室轻微的嗡鸣，和收音机原先沙沙作响的地方一片深沉厚重的寂静。')
SOUND_GRAM = breathy('The soft crackle of a needle in a groove and then a warm, slow classical violin melody begins.', '针尖落进唱片纹路轻轻的噼啪声，接着响起温暖缓慢的古典小提琴旋律。')
SOUND_KITCHEN = voiced('The soft knock of a knife on a wooden board, the quiet bubble of a pot and a slow violin melody from a gramophone.', '刀轻轻敲在木砧板上的声音、锅里安静的咕嘟声和留声机传来的缓慢小提琴旋律。')
SOUND_EAT = voiced('A slow violin melody, the soft clink of chopsticks on porcelain and the warm hum of the stove.', '缓慢的小提琴旋律、筷子碰到瓷碗轻轻的响声和炉子温暖的嗡鸣。')
SOUND_RADAR = breathy('A rising low rumble, a slow repeating electronic beep and a thin hum from the radar unit.', '渐渐变大的低沉隆隆声、缓慢反复的电子嘀声和雷达仪细细的嗡鸣。')
SOUND_QUAKE = breathy('A long, low metallic groan running through concrete and the faint tick of falling dust.', '一声长长的低沉金属呻吟从混凝土里传来，和灰尘落下细细的嘀嗒声。')
SOUND_QUAKE_V = voiced('A long, low metallic groan running through concrete and the faint hum of the radar unit.', '一声长长的低沉金属呻吟从混凝土里传来，和雷达仪轻微的嗡鸣。')
SOUND_CRACK = breathy('A dry sharp crack, a heavy thud on wood, rattling bowls and a rising metallic groan.', '一声干脆的开裂声、木头上沉重的撞击声、碗碟的哗啦声和越来越响的金属呻吟。')
SOUND_HALL = breathy('A thin howl of wind in the doorway, the slow drip of melting frost and a deep hush.', '门口细细的风声、融化的霜缓缓滴落的声音和深深的寂静。')
SOUND_HALL_V = voiced('The roar of a blowtorch, chattering teeth, the hiss of melting ice and ragged breath.', '喷枪的轰响、打颤的牙齿声、冰融化的嘶嘶声和粗重的喘息。')
SOUND_HEAVE = breathy('Ragged breath, the creak of frozen metal and boots slipping on ice.', '粗重的喘息、冻住的金属吱呀声和靴子在冰上打滑的声音。')
SOUND_FLAME = breathy('The steady roar of a blowtorch flame and the sharp hiss of ice flashing to steam.', '喷枪火焰稳定的轰响和冰一下子变成蒸汽的尖锐嘶嘶声。')
SOUND_WHEEL = breathy('A groan of rusted iron turning, cracking ice, hissing steam and heavy breath.', '生锈铁轮转动的呻吟、冰层开裂声、嘶嘶的蒸汽和沉重的呼吸。')
SOUND_BURST2 = breathy('A sharp bang, a roaring burst of water and ice and a startled gasp.', '一声尖锐的巨响、水和冰碴爆开的轰鸣和一声受惊的抽气。')
SOUND_AFTER = breathy('The roar of water dying away into dripping, the slow groan of the walls fading into silence and ragged breath.', '水声的轰鸣渐渐变成滴水声，墙壁的呻吟慢慢消失在寂静里，还有粗重的喘息。')
SOUND_AFTER_V = voiced('Dripping water, thin mist hissing softly and ragged breath.', '滴水声、细细的雾气轻轻嘶嘶的声音和粗重的喘息。')
SOUND_SOFA = voiced('The faint hum of the air system and the soft rustle of gauze.', '空气系统轻微的嗡鸣和纱布轻轻的摩擦声。')
SOUND_BREAD = voiced('The soft press of dough on wood and the faint hum of the stove.', '面团按在木头上轻轻的声音和炉子轻微的嗡鸣。')
SOUND_OVEN = breathy('The gentle tick of a hot oven and a soft crackle of baking crust.', '烤箱加热时轻轻的嘀嗒声和面包外皮烤脆时细细的噼啪声。')
SOUND_OVEN_V = voiced('The clack of an oven rack, a rush of steam and the faint hum of the stove.', '烤架被拉出的咔哒声、涌出的蒸汽声和炉子轻微的嗡鸣。')
SOUND_SNOW = breathy('A long low howl of wind over the snowfield and a faint electronic ping.', '风掠过雪原长长的低啸和一声细细的电子提示音。')
SOUND_SNOW_SERVO = breathy('A long low howl of wind, the soft whir of armor servos and a faint electronic ping.', '风长长的低啸、装甲关节轻轻的嗡嗡声和一声细细的电子提示音。')

# ================================================================================================ 第 25 集
b25 = S.episode('剧本第25集｜绝对领地', '林峰连话筒都没拿，直接拔掉了收音机的电源线，地下室重新恢复绝对的宁静；苏清月笑着问不回复吗，几千条人命，他把她拉进怀里说：我的世界里，只剩你和我，外面的声音，只是风声；他放上一张老唱片，她切了自己种的番茄，煮了一碗番茄鸡蛋面，两人坐在地毯上吃面；林峰无意间瞥见桌边的地质雷达仪，屏幕上出现一个巨大的、正在缓慢移动的红色阴影，正朝着他们的地下安全屋压来，警报红光中画面切断。', 25)
b25.prop('gramophone', '手摇留声机（黄铜大喇叭、深色胡桃木底座、黑胶唱片、细长唱臂）',
         'A hand-crank gramophone with a polished brass horn, a dark walnut wooden base, a black vinyl record on the turntable and a slim chrome tonearm. The reference fixes its shape.',
         '一台手摇留声机：抛光的黄铜大喇叭、深色胡桃木底座、转盘上放着一张黑胶唱片、一根细长的银色唱臂。参考图固定它的外形。',
         'A photorealistic product shot of a hand-crank gramophone with a polished brass horn, a dark walnut wooden base, a black vinyl record on the turntable and a slim chrome tonearm, standing on a small wooden cabinet against a plain neutral gray background.')
b25.prop('radar_unit', '便携地质雷达仪（橄榄绿钢壳、圆形绿色屏幕、顶上一盏小红灯、钢三脚架）',
         'A rugged olive-drab portable geological radar unit with a round dark screen, two knobs, a small red lamp on top and a slim steel tripod stand. The reference fixes its shape.',
         '一台橄榄绿钢壳的便携地质雷达仪：圆形的屏幕，两个旋钮，顶上有一盏小红灯，下面是细长的钢三脚架。参考图固定它的外形。',
         'A photorealistic product shot of a rugged olive-drab portable geological radar unit with a round dark screen, two knobs, a small red lamp on top and a slim steel tripod stand, against a plain neutral gray background.')

TA('25-01', '01｜控制室：林峰一把拔掉收音机的电源线，琥珀色的灯灭了，静电声被切断，屋里一片死寂', 6, CONTROL_R,
   [P('lin_home', 'right', "standing at the steel side table in profile facing frame-left, his right hand closed around the black power cord where it plugs into the back of the olive-green military radio", 'obj:the radio\'s black power cord in his hand', "his jaw set, his lips pressed flat, his brows low", outfit="in a dry soft grey henley")],
   'Low-angle medium shot, Lin from the head to the knees, in the middle third of the frame, at the side table with the radio.',
   "<lin_home> yanks the power cord out of the back of the radio in one decisive pull, his jaw set, his lips pressed flat and his brows low; the amber dial light of the radio dies at once and the hiss of static cuts off into total silence. He stands still in the silence with his steady eyes on the dark radio. Nobody else is in the room.",
   "林峰一把把收音机背后的黑色电源线拔了出来，下颌绷紧、嘴唇抿平、眉头压低；收音机琥珀色的灯一下子灭了，沙沙的静电声被切断，变成彻底的寂静。他在寂静里站着不动，稳稳地看着熄灭的收音机。屋里没有别人。",
   SOUND_CTRL_QUIET, AES_TEAL, cam=lowrise('Lin and the dark radio', '林峰和熄灭的收音机'), extra_assets=('radio_set',), room={'Lin'}, new=True,
   bg='Beside him on the steel side table the olive-green military radio glows with its amber dial, and the wall of six small monitors glows at frame-left.',
   holds='The frame holds exactly one person: Lin, at the side table with the radio, nobody else.')

TA('25-02', '02｜控制室：苏清月紧绷的肩膀放松下来，笑着问不回复一下吗，那是几千条人命', 7, CONTROL_R,
   [P('su_silk', 'left', "standing beside him in profile facing frame-right, the white towel around her neck, her shoulders loosening", 'Lin', "a bright sweet smile on her lips, her eyes sparkling, her brows lifted"),
    P('lin_home', 'right', "standing at the side table in profile facing frame-left, the unplugged power cord hanging from his right hand, turning his head toward her", 'Su', "his jaw loosening, one corner of his mouth lifting, his brows soft", outfit="in a dry soft grey henley")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the control console.',
   "<su_silk> lets her shoulders drop and speaks the one line to <lin_home> in a light, knowing, teasing voice, a bright sweet smile spreading across her lips, her eyes sparkling and her brows lifted. <lin_home> turns toward her, his jaw loosening, one corner of his mouth lifting and his brows soft.",
   "苏清月紧绷的肩膀放松下来，用轻快、心里有数、带点逗弄的声音对林峰说出这一句，嘴角绽开明艳的甜笑、眼睛发亮、眉毛上扬。林峰转向她，下颌放松、嘴角微微上扬、眉毛舒展。",
   SOUND_CTRL_SILENT, AES_TEAL, lines=[('su_silk', "不回复吗？那是几千条人命。", 1.0, 'Lin')],
   cam=push('both of them', '两人'), extra_assets=('radio_set',), room={'Su', 'Lin'}, new=True,
   bg='Beside them on the steel side table the olive-green military radio sits dark and silent, and the wall of six small monitors glows at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, at the control console with the dark radio beside them, nobody else.')

TA('25-03', '03｜控制室：林峰把苏清月拉进怀里，低头看着她说我的世界里只剩你和我，外面的声音只是风声', 9, CONTROL_R,
   [P('lin_home', 'right', "standing in profile facing frame-left, both arms drawing her gently against his chest, his head bent toward her", 'Su', "his jaw relaxed, his eyes dark and warm, his brows soft", outfit="in a dry soft grey henley"),
    P('su_silk', 'left', "standing in profile facing frame-right, held against his chest with her hands resting on his arms, her face tipped up to him", 'Lin', "her lips parted, her eyes bright, her brows lifted")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "<lin_home> draws <su_silk> gently into his arms and holds her against his chest while he speaks the first line to <su_silk> in a low, firm, possessive voice, then the second line in a softer, deeper voice, his jaw relaxed, his eyes dark and warm and his brows soft. <su_silk> tips her face up to him and listens, her lips parted, her eyes bright and her brows lifted.",
   "林峰把苏清月轻轻拉进怀里，让她靠着自己的胸口，用低沉坚定、带着占有的声音对苏清月说出第一句，接着用更轻更深的声音说出第二句，下颌放松、眼神又黑又暖、眉毛舒展。苏清月仰起脸听着，嘴唇微张、眼睛发亮、眉毛上扬。",
   SOUND_CTRL_SILENT, AES_TEAL, lines=[('lin_home', "我的世界里，只剩你和我。", 1.2, 'Su'), ('lin_home', "外面的声音，只是风声。", 5.0, 'Su')],
   cam=arc('the two of them', '两人', 'their faces are in profile against the glowing monitor wall in the middle third of the frame', '两人的侧脸占满画面中间三分之一、背后是发光的监控墙'),
   room={'Su', 'Lin'}, new=True,
   bg='Behind them the wall of six small monitors glows at frame-left and the dark radio sits silent on the steel side table.',
   holds='The frame holds exactly two people: Lin and Su, standing close together at the control console, nobody else.')

insert2('25-04', '04｜插镜：留声机的唱针落在转动的唱片上，黄铜喇叭泛着金光，小提琴声响起', 5, GRAM_CLOSE,
        'Close shot of the gramophone, the turntable and the brass horn in the middle third of the frame, nobody in the scene.',
        "The tonearm swings down and its needle settles into the groove of the black record turning slowly on the turntable; golden light slides along the curve of the brass horn and tiny dust motes drift through the beam. Nothing else moves.",
        "留声机的唱臂落下来，唱针稳稳落进缓缓转动的黑胶唱片的纹路里；金色的光顺着黄铜喇叭的弧线滑过，细小的尘埃在光束里飘。别的什么都不动。",
        SOUND_GRAM, 'The frame holds the gramophone with its turntable and brass horn, and nobody in the scene.',
        push1('the needle on the turning record', '转动的唱片上的唱针'), AES_AMBER, extra_assets=('gramophone',))

TA('25-05', '05｜厨房：苏清月切开自己种的红番茄，林峰靠着台边问今晚吃什么，她说番茄鸡蛋面', 9, LIV_GR,
   [P('su_silk', 'left', "standing at the marble counter in profile facing frame-left, a sharp kitchen knife in her right hand slicing through a plump red tomato on a wooden board, a beaten egg in a white bowl beside it", 'obj:the tomato on the board', "a sweet smile on her lips, her eyes bright, her brows lifted"),
    P('lin_home', 'right', "leaning his hip against the counter beside her in profile facing frame-left, his arms loosely folded", 'Su', "one corner of his mouth lifting, his jaw relaxed, his brows soft")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the kitchen counter.',
   "<lin_home> watches her and speaks the first line to <su_silk> in a lazy, curious voice, one corner of his mouth lifting and his brows soft. <su_silk> keeps slicing the tomato, the red juice and seeds spilling over the board, and speaks the second line to <lin_home> in a proud, sing-song voice, a sweet smile on her lips and her brows lifted.",
   "林峰看着她，用慵懒好奇的声音对苏清月说出第一句，嘴角微微上扬、眉毛舒展。苏清月继续切着番茄，红色的汁水和籽流满砧板，用得意、带着唱腔的声音对林峰说出第二句，嘴角带着甜笑、眉毛上扬。",
   SOUND_KITCHEN, AES_KITCH, lines=[('lin_home', "今晚吃什么？", 0.8, 'Su'), ('su_silk', "番茄鸡蛋面，番茄自己种的。", 3.0, 'Lin')],
   cam=slide('right', '右', 'the two of them stand in the middle third of the frame with the sliced tomato between them', '两人占画面中间三分之一、中间是切开的番茄'),
   room={'Su', 'Lin'}, new=True,
   bg='Behind them the black-and-gold stove glows warm at frame-left and a brass-horn gramophone stands on its cabinet beside the dining table.',
   holds='The frame holds exactly two people: Su and Lin, at the kitchen counter, nobody else.')

TA('25-06', '06｜地毯上：两人盘腿坐着吃面，苏清月说这碗面比任何宴席都香，林峰说番茄是你种的', 10, LIV_GR,
   [P('su_silk', 'left', "sitting cross-legged on the cream rug in profile facing frame-right, a white bowl of golden tomato-and-egg noodles held in both hands, a forkful of noodles raised on her chopsticks", 'Lin', "a soft sweet smile on her lips, her eyes bright and warm, her brows lifted"),
    P('lin_home', 'right', "sitting cross-legged on the rug in profile facing frame-left, his own bowl in his left hand and chopsticks in his right", 'Su', "one corner of his mouth lifting, his jaw relaxed, his eyes warm and lazy, his brows soft")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, on the rug by the stove.',
   "<su_silk> takes a bite, savors it and speaks the first line to <lin_home> in a soft, dreamy voice, a soft sweet smile on her lips, her eyes bright and warm and her brows lifted. <lin_home> answers with the second line to <su_silk> in a warm, amused voice, one corner of his mouth lifting, his jaw relaxed and his brows soft. Steam curls up from both bowls.",
   "苏清月咬了一口，细细品着，用柔软、梦幻的声音对林峰说出第一句，嘴角带着柔和的甜笑、眼睛又亮又暖、眉毛上扬。林峰用温暖带笑的声音对苏清月答出第二句，嘴角微微上扬、下颌放松、眉毛舒展。两只碗里都冒着热气。",
   SOUND_EAT, AES_AMBER, lines=[('su_silk', "这碗面，比我吃过的宴席都香。", 1.0, 'Lin'), ('lin_home', "番茄是你种的，当然香。", 5.2, 'Su')],
   cam=drop('the two of them seated on the rug', '盘腿坐在地毯上的两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the black-and-gold stove glows warm at frame-left and the brass-horn gramophone stands on its cabinet beside the dining table.',
   holds='The frame holds exactly two people: Su and Lin, sitting on the rug, nobody else.')

TA('25-07', '07｜地毯上：林峰瞥了一眼桌边的雷达仪，脸上的暖意一下子没了，苏清月问怎么了', 6, LIV_GR,
   [P('su_silk', 'left', "sitting on the cream rug in profile facing frame-right, her chopsticks stilled above her bowl, her face turned toward him", 'Lin', "her lips parting, her brows pulling together"),
    P('lin_home', 'right', "sitting on the rug in profile facing frame-right, his bowl lowered to his knee, his head turned toward the radar unit", 'obj:the geological radar unit on its tripod at frame-right', "his easy warmth draining from his face, his jaw tightening, his lips pressing flat, his brows lowering")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, on the rug by the dining table.',
   "<lin_home> glances toward the radar unit and his easy warmth drains from his face, his jaw tightening, his lips pressing flat and his brows lowering. <su_silk> sees it, her chopsticks stilling, and speaks the one line to <lin_home> in a small uneasy voice, her lips parting and her brows pulling together.",
   "林峰朝雷达仪瞥了一眼，脸上轻松的暖意一下子消失，下颌绷紧、嘴唇抿平、眉头压低。苏清月看见了，筷子停在半空，用小而不安的声音对林峰说出这一句，嘴唇微张、眉头拧在一起。",
   SOUND_CTRL_SILENT, AES_DUSTRED, lines=[('su_silk', "怎么了？", 1.8, 'Lin')],
   cam=push1('Lin', '林峰'), extra_assets=('radar_unit',), room={'Su', 'Lin'}, new=True,
   bg='At frame-right the olive-drab geological radar unit stands on its steel tripod with its round screen glowing green, and the black-and-gold stove glows warm at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, sitting on the rug, nobody else.')

insert2('25-08', '08｜插镜：雷达屏幕上，一个巨大的红色阴影正缓缓吞掉中心的绿点，顶上的红灯开始闪烁', 5, RADAR_SCR,
        'Close shot of the radar unit, its round screen in the middle third of the frame, nobody in the scene.',
        "A huge irregular red shadow creeps slowly across the green concentric rings of the radar screen, swallowing the small bright green square at its center, while the small red lamp on top of the unit begins to flash and pulse and the room beyond washes in a slow red glow. Nothing else moves.",
        "一团巨大的、不规则的红色阴影慢慢爬过雷达屏幕上绿色的同心圆，吞掉中心那个小小的亮绿色方块，仪器顶上的小红灯开始闪烁、脉动，远处的房间慢慢浸在红光里。别的什么都不动。",
        SOUND_RADAR, 'The frame holds the radar unit with its green screen and red shadow, and nobody in the scene.',
        push1('the red shadow on the radar screen', '雷达屏幕上的红色阴影'), AES_RED, extra_assets=('radar_unit',))

# ================================================================================================ 第 26 集
b26 = S.episode('剧本第26集｜地底巨兽', '雷达屏幕上，红色阴影正缓慢地、不可阻挡地朝避难所正下方挤压过来，桌上的水杯荡起一圈圈涟漪；苏清月抓住他的手臂问那是什么，林峰说比变异生物可怕得多，是冰震，极寒冻住了地下暗河，水变成冰，体积膨胀，几百万吨的力正在挤压外壳；天花板的接缝发出金属的呻吟，吊灯摇晃、掉灰；她问怎么办、要逃出去吗，他说外面零下八十度，出去必死，唯一的办法是去地下四层开泄洪阀，但那里零下五十度，你留下；话音刚落，头顶掉下一块碎块，砸在桌上，画面黑屏。', 26)

insert2('26-01', '01｜插镜：雷达屏幕上的红色阴影已经占了半个屏幕，正压向中心的绿点，红灯一下一下闪', 5, RADAR_RED,
        'Close shot of the radar unit, its round screen in the middle third of the frame, nobody in the scene.',
        "The vast red shadow slides slowly across the green rings of the radar screen and closes in directly beneath the small bright green square at its center, the rings shivering and distorting while the small red lamp on top pulses and a low rumble trembles through the unit. Nothing else moves.",
        "巨大的红色阴影在雷达屏幕的绿色圆环上缓缓滑动，压到中心亮绿色方块的正下方，圆环跟着颤抖、变形，仪器顶上的小红灯一下一下脉动，一阵低沉的隆隆声让整台仪器微微发抖。别的什么都不动。",
        SOUND_RADAR, 'The frame holds the radar unit with its green screen and the red shadow, and nobody in the scene.',
        push1('the red shadow under the green square', '绿色方块下面的红色阴影'), AES_RED, extra_assets=('radar_unit',))

insert2('26-02', '02｜插镜：餐桌上，一杯清水的水面荡起一圈圈涟漪，碗上的筷子在轻轻发抖', 4, WATER,
        'Close low shot of the dining table, the glass of water in the middle third of the frame, nobody in the scene.',
        "Concentric ripples shiver across the surface of the clear glass of water, the chopsticks tremble across the rim of a white bowl and a thin tick of dust falls onto the tabletop in the amber light. Nothing else moves.",
        "一杯清水的水面荡起一圈圈涟漪，搁在白瓷碗上的筷子轻轻发抖，一缕细细的灰尘落在桌面上的琥珀灯光里。别的什么都不动。",
        SOUND_QUAKE, 'The frame holds the glass of water, the white bowls and the table, and nobody in the scene.',
        lowrise('the shivering glass of water', '颤动的水杯'), AES_DUSTRED)

TA('26-03', '03｜餐桌边：苏清月抓住林峰的手臂问那是什么，是不是变异生物，林峰盯着笔记本说比变异生物可怕得多，是冰震', 10, LIV_GR,
   [P('su_silk', 'left', "standing beside the table in profile facing frame-right, one hand gripping his upper arm", 'Lin', "her lips parted, her face gone pale, her brows pulled together"),
    P('lin_home', 'right', "sitting at the small round table in profile facing frame-left, his fingers moving across the keys of an open black rugged laptop", 'obj:the open black laptop on the table', "his jaw tight, his lips set flat, his brows low", outfit="in a dry soft grey henley")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the dining table.',
   "<su_silk> speaks the first line to <lin_home> in a tight, frightened voice, her lips parted, her face gone pale and her brows pulled together. <lin_home> keeps typing without looking up and speaks the second line to <su_silk> in a low, grim voice, his jaw tight, his lips set flat and his brows low.",
   "苏清月用紧绷害怕的声音对林峰说出第一句，嘴唇微张、脸色发白、眉头拧在一起。林峰眼睛没抬，继续敲着键盘，用低沉凝重的声音对苏清月说出第二句，下颌绷紧、嘴唇抿平、眉头压低。",
   SOUND_QUAKE_V, AES_DUSTRED, lines=[('su_silk', "那是什么？变异生物吗？", 0.8, 'Lin'), ('lin_home', "比变异生物可怕得多，是冰震。", 4.2, 'Su')],
   cam=slide('left', '左', 'the two of them stand in the middle third of the frame', '两人占画面中间三分之一'), extra_assets=('radar_unit',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the radar unit on its steel tripod pulses with a red lamp at frame-right and the two white bowls stand on the table.',
   holds='The frame holds exactly two people: Su and Lin, at the dining table, nobody else.')

insert2('26-04', '04｜插镜：天花板的接缝发出一声长长的金属呻吟，吊灯缓缓摇晃，白灰一缕缕落下来', 5, CEIL,
        'Wide low shot looking up from the rug at the dining table and the ceiling above it, the pendant lamp in the middle third of the frame, nobody in the scene.',
        "A long low groan runs through the concrete; the round pendant lamp above the table sways in a slow arc and a fine veil of white dust sifts down from the ceiling seam into the amber light. Nothing else moves.",
        "一声长长的低沉呻吟从混凝土里传出来；餐桌上方的圆形吊灯划着缓慢的弧度摇晃，一层细细的白灰从天花板接缝里落进琥珀色的灯光里。别的什么都不动。",
        SOUND_QUAKE, 'The frame holds the swaying pendant lamp, the ceiling seam and the table below, and nobody in the scene.',
        lowrise('the swaying pendant lamp and the ceiling seam', '摇晃的吊灯和天花板的接缝'), AES_DUSTRED)

TA('26-05', '05｜餐桌边：林峰说暗河冻结、水变成冰、体积膨胀，几百万吨的力正在挤压外壳', 10, LIV_GR,
   [P('su_silk', 'left', "standing beside the table in profile facing frame-right, both arms wrapped around herself", 'Lin', "her lips pressed tight, her face pale, her brows pulled together"),
    P('lin_home', 'right', "standing at the table in profile facing frame-left, one hand flat on the closed laptop", 'Su', "his jaw tight, his eyes grim, his brows low", outfit="in a dry soft grey henley")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dining table.',
   "<lin_home> speaks the first line to <su_silk> in a low, even, grim voice, then the second line in a heavier voice, his jaw tight, his eyes grim and his brows low. <su_silk> listens, her lips pressed tight, her face pale and her brows pulled together.",
   "林峰用低沉平稳、凝重的声音对苏清月说出第一句，接着用更沉重的声音说出第二句，下颌绷紧、眼神凝重、眉头压低。苏清月听着，嘴唇紧抿、脸色发白、眉头拧在一起。",
   SOUND_QUAKE_V, AES_DUSTRED, lines=[('lin_home', "暗河冻结，水变成冰，体积膨胀。", 0.8, 'Su'), ('lin_home', "几百万吨的力，正在挤压外壳。", 5.2, 'Su')],
   cam=push1('Lin', '林峰'), extra_assets=('radar_unit',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the radar unit on its steel tripod pulses with a red lamp at frame-right and the pendant lamp above the table sways slightly.',
   holds='The frame holds exactly two people: Su and Lin, at the dining table, nobody else.')

TA('26-06', '06｜餐桌边：苏清月脸色惨白问怎么办、要逃出去吗，林峰说外面零下八十度，出去必死', 9, LIV_GR,
   [P('su_silk', 'left', "standing beside the table in profile facing frame-right, her fingers gripping the edge of the table", 'Lin', "her face drained pale, her lips trembling, her brows pulled high"),
    P('lin_home', 'right', "standing at the table in profile facing frame-left, one hand lifted to calm her", 'Su', "his jaw tight, his eyes steady, his brows low", outfit="in a dry soft grey henley")],
   'Close medium two-shot, both from the head to the chest, in the middle third of the frame, at the dining table.',
   "<su_silk> speaks the first line to <lin_home> in a thin, shaking voice, her face drained pale, her lips trembling and her brows pulled high. <lin_home> answers with the second line to <su_silk> in a low, hard voice, his jaw tight, his eyes steady and his brows low.",
   "苏清月用发抖的细声对林峰说出第一句，脸色惨白、嘴唇发颤、眉毛高高挑起。林峰用低沉强硬的声音对苏清月答出第二句，下颌绷紧、眼神稳住、眉头压低。",
   SOUND_QUAKE_V, AES_RED, lines=[('su_silk', "怎么办？要逃出去吗？", 0.8, 'Lin'), ('lin_home', "外面零下八十度，出去必死。", 4.0, 'Su')],
   cam=slide('right', '右', 'the two of them stand in the middle third of the frame', '两人占画面中间三分之一'), extra_assets=('radar_unit',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the radar unit on its steel tripod flashes its red lamp at frame-right and the wall of small monitors glows at frame-center-right.',
   holds='The frame holds exactly two people: Su and Lin, at the dining table, nobody else.')

TA('26-07', '07｜舱门边：林峰从墙钩上取下白色极地服，说唯一的办法是去地下四层开阀门，但那里零下五十度，你留下', 10, LIV_GR,
   [P('lin_home', 'right', "standing beside the round hatch door in profile facing frame-right, both hands lifting the heavy white polar suit from its wall hook, his head turned back toward her", 'Su', "his jaw tight, his eyes steady, his brows low", outfit="in a dry soft grey henley"),
    P('su_silk', 'left', "standing a step behind him in profile facing frame-right, both arms wrapped around herself", 'Lin', "her lips pressed tight, her chin lifting a little, her brows pulled together")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, beside the hatch door.',
   "<lin_home> lifts the white polar suit down from its hook and speaks the first line to <su_silk> in a low, even voice, then the second line in a harder voice, his jaw tight, his eyes steady and his brows low. <su_silk> watches him, her lips pressed tight, her chin lifting a little and her brows pulled together.",
   "林峰把白色极地服从墙钩上取下来，用低沉平稳的声音对苏清月说出第一句，接着用更硬的声音说出第二句，下颌绷紧、眼神沉稳、眉头压低。苏清月看着他，嘴唇紧抿、下巴微微抬起、眉头拧在一起。",
   SOUND_QUAKE_V, AES_RED, lines=[('lin_home', "唯一的办法，去地下四层开阀门。", 0.8, 'Su'), ('lin_home', "但那里零下五十度，你留下。", 5.2, 'Su')],
   cam=lowrise('Lin with the white polar suit', '拿着白色极地服的林峰'), room={'Su', 'Lin'}, new=True,
   bg='Beside them the heavy round steel hatch door stands shut in the right wall and the red lamp of the radar unit pulses at frame-center-left.',
   holds='The frame holds exactly two people: Lin and Su, beside the hatch door, nobody else.')

insert2('26-08', '08｜插镜：天花板接缝崩开一道口子，一块巴掌大的碎块砸在桌上、碗旁，吊灯疯狂摇晃，红光里扬起一团白灰', 5, DEBRIS,
        'Close medium shot of the dining table, the two white bowls in the middle third of the frame, nobody in the scene.',
        "The hairline split in the ceiling seam widens with a dry crack and a palm-sized chunk of concrete drops and lands on the table beside the two white bowls, bouncing once; the pendant lamp swings wildly and a cloud of white dust billows through the red light. Nothing else moves.",
        "天花板接缝上那道细缝啪地裂开，一块巴掌大的混凝土碎块掉下来，砸在桌上两只白碗旁边，弹了一下；吊灯疯狂摇晃，一团白灰在红光里扬起来。别的什么都不动。",
        SOUND_CRACK, 'The frame holds the table, the two white bowls and the fallen chunk of concrete, and nobody in the scene.',
        push1('the chunk of concrete beside the bowls', '碗旁边的混凝土碎块'), AES_RED)

# ================================================================================================ 第 27 集
b27 = S.episode('剧本第27集｜绝对零度的抢修', '厚重的隔离门开着，一股刺骨的白雾涌出来；地下四层是一座冰窖，管道结着厚厚的白霜，林峰举着手电冲向尽头那个一米多宽的红色生铁齿轮阀门，双手压上去，整个人发力，阀门纹丝不动，齿轮已经冻死；一团蓝色火焰喷在齿轮上，是苏清月，她穿着奶白羽绒服冻得发抖，却稳稳举着喷枪：我来化冰，你来转；冰化成蒸汽，阀门终于转动，压力表的指针落下来；旁边一根老水管砰地崩开，水柱和冰碴直冲苏清月，林峰猛地扑了过去，画面切断。', 27)
new_scene(b27, 'ice_hall', '地下四层冰窖（结满白霜的管道、冰柱、尽头一米多宽的红色生铁齿轮阀门）',
          'A freezing underground hall furred with white hoar frost: thick pipes along the ceiling and the right wall, long icicles hanging overhead, a glazed icy concrete floor, a heavy round steel isolation door at the left with white fog rolling out, and at the far end a huge red cast-iron gear valve over a metre across, rimed with ice.',
          '一座结满白霜的地下冰窖：天花板和右墙上是粗管道，头顶挂着长长的冰柱，水泥地面结了一层冰，左边是一扇厚重的圆形钢制隔离门、白雾正从门里涌出来，尽头是一个一米多宽、裹着冰的红色生铁齿轮阀门。',
          'the frost-furred pipes, the icicles, the open steel door with its fog and the huge red gear valve at the far end')

TA('27-01', '01｜冰窖：隔离门大开，白雾涌出来，林峰举着手电走进去，光束在雾里切出一条长长的光路，尽头是红色的大阀门', 6, ICE,
   [P('lin_arctic', 'left', "standing just inside the open heavy round steel door in profile facing frame-right, a bright flashlight in his right hand throwing a long beam into the white fog, the hood of his white polar suit up", 'obj:the huge red valve at the far end of the hall', "his jaw tight, his lips pressed flat, his brows low")],
   'Wide shot of the long icy hall, Lin small at frame-left in the doorway, the long frosted hall with the red valve at its far end in the middle third of the frame.',
   "White fog pours out around <lin_arctic> as he lifts the flashlight and steps forward, the beam cutting a long shaft of light through the drifting fog toward the far end while icicles glint overhead; his jaw is tight, his lips pressed flat and his brows low. Nobody else is in the hall.",
   "白雾从林峰身边涌出来，他举起手电向前迈步，光束在飘动的白雾里切出一道长长的光柱，直射向尽头，头顶的冰柱闪着光；他下颌绷紧、嘴唇抿平、眉头压低。大厅里没有别人。",
   SOUND_HALL, AES_FOG, cam=slide('right', '右', 'the long frosted hall with the red valve at its far end fills the middle third of the frame', '长长的结霜大厅和尽头的红色阀门占满画面中间三分之一'),
   room={'Lin'}, new=True, holds='The frame holds exactly one person: Lin, in the doorway of the icy hall, nobody else.')

TA('27-02', '02｜冰窖：林峰沿着结霜的管道大步走向尽头，手电光束扫过冰面，红色阀门在雾里越来越大', 6, ICE,
   [P('lin_arctic', 'center', "striding down the middle of the icy hall away from the camera with his back to us, the flashlight beam sweeping ahead of him through the fog, the hood of his white polar suit up", 'obj:the huge red valve at the far end of the hall', "his jaw clenched, his breath streaming white, his brows low")],
   'Medium rear shot, Lin from the head to the knees from behind, in the middle third of the frame, in the icy hall.',
   "<lin_arctic> strides down the icy hall toward the huge red valve, his breath streaming white, his jaw clenched and his brows low, the flashlight beam sweeping across the glazed floor and the frost-furred pipes. Nobody else is in the hall.",
   "林峰大步走向那个巨大的红色阀门，呼出的气成了白雾，下颌咬紧、眉头压低，手电光束扫过结了冰的地面和结霜的管道。大厅里没有别人。",
   SOUND_HALL, AES_FOG, cam=follow('Lin', '林峰', 'the huge red valve fills the middle third of the frame ahead of him', '巨大的红色阀门占满他前方画面的中间三分之一'),
   room={'Lin'}, new=True, holds='The frame holds exactly one person: Lin, striding down the icy hall, nobody else.')

TA('27-03', '03｜冰窖：林峰双手握住结满霜的阀门轮，整个人压上去，呼出一大团白雾，阀门纹丝不动', 6, ICE,
   [P('lin_arctic', 'left', "standing at the huge red cast-iron valve wheel in profile facing frame-right, both gloved hands gripping its frost-crusted rim, heaving with his whole body, his breath pouring out in a white cloud", 'obj:the frozen valve wheel', "his jaw clenched, his teeth gritted, his brows low")],
   'Medium shot, Lin from the head to the knees at frame-left with the huge valve wheel in the middle third of the frame, in the icy hall.',
   "<lin_arctic> heaves against the wheel with his whole body, his breath pouring out in a huge white cloud, his jaw clenched, his teeth gritted and his brows low, but the frost-crusted wheel does not move at all. Nobody else is in the hall.",
   "林峰用整个身体压在轮子上，呼出的气像一大团白云，下颌咬紧、牙关紧闭、眉头压低，可是结满霜的轮子一动也不动。大厅里没有别人。",
   SOUND_HEAVE, AES_FOG, cam=slide('left', '左', 'Lin and the huge valve wheel fill the middle third of the frame', '林峰和巨大的阀门轮占满画面中间三分之一'),
   room={'Lin'}, new=True, holds='The frame holds exactly one person: Lin, at the huge valve wheel, nobody else.')

TA('27-04', '04｜冰窖：一团蓝色火焰喷在齿轮上，苏清月举着喷枪站在阀门另一边，冻得牙齿打颤，喊我来化冰，你来转', 7, ICE,
   [P('lin_arctic', 'left', "standing at the valve wheel in profile facing frame-right, both gloved hands still gripping its rim, his head turned toward her", 'Su', "his eyes wide, his jaw loosening, his brows lifting"),
    P('su_down', 'right', "standing at frame-right in profile facing frame-left in her long cream down coat zipped to the chin, a handheld blowtorch in both hands aimed at the gear teeth of the valve wheel, a hard blue flame roaring from its nozzle", 'obj:the iced gear teeth of the valve wheel', "her teeth chattering, her lips pressed tight, her brows drawn together")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the valve wheel.',
   "<su_down> holds the blue flame steady on the iced gear teeth and speaks the one line to <lin_arctic> in a loud, shaking, fiercely determined voice, her teeth chattering, her lips pressed tight and her brows drawn together. <lin_arctic> stares at her, his eyes wide, his jaw loosening and his brows lifting, then gives a short nod.",
   "苏清月把蓝色火焰稳稳地对着结冰的齿轮，用又大声又发抖、却无比坚定的声音对林峰喊出这一句，牙齿打颤、嘴唇紧抿、眉头拧在一起。林峰盯着她，眼睛睁大、下颌放松、眉毛上扬，然后短短点了一下头。",
   SOUND_HALL_V, AES_FLAME, lines=[('su_down', "我来化冰！你来转！", 1.0, 'Lin')],
   cam=push('both of them', '两人'), room={'Lin', 'Su'}, new=True,
   bg='Behind them the frost-furred pipes run into the fog and the open steel door glows orange at frame-left.',
   holds='The frame holds exactly two people: Lin and Su, at the valve wheel, nobody else.')

insert2('27-05', '05｜插镜：蓝色火焰舔过结冰的齿轮，冰层嘶嘶变成翻滚的白色蒸汽，水珠顺着红色的铁往下流', 4, ICE_GEAR,
        'Close shot of the gear teeth and the flame in the middle third of the frame, nobody in the scene.',
        "The hard blue flame licks along the iced teeth of the gear; the white ice softens, hisses and melts into rolling clouds of steam, bright droplets running down the red iron. Nothing else moves.",
        "坚硬的蓝色火焰舔过结冰的齿轮牙，白色的冰层软下来，嘶嘶响着化成翻滚的蒸汽，亮晶晶的水珠顺着红色的铁往下流。别的什么都不动。",
        SOUND_FLAME, 'The frame holds the gear teeth and the blue flame, and nobody in the scene.',
        push1('the blue flame on the gear teeth', '齿轮牙上的蓝色火焰'), AES_FLAME)

TA('27-06', '06｜冰窖：林峰整个人拉着阀门轮，生锈的红轮子呻吟着转动起来，冰块崩落，蒸汽翻滚', 6, ICE,
   [P('lin_arctic', 'left', "standing at the valve wheel in profile facing frame-right, both gloved hands on its rim, his whole body leaning into the pull", 'obj:the turning valve wheel', "his jaw clenched, his teeth gritted, his brows low"),
    P('su_down', 'right', "standing beside the gear in profile facing frame-left, the blue flame of her blowtorch playing on the gear teeth", 'obj:the gear teeth of the valve wheel', "her lips pressed tight, her eyes narrowed, her brows drawn together")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the valve wheel.',
   "<lin_arctic> pulls with his whole body and the rusted red valve wheel groans and begins to turn, flakes of ice cracking off and falling, while <su_down> keeps the flame steady on the gear teeth, white steam rolling around them.",
   "林峰用整个身体往回拉，生锈的红色阀门轮呻吟着转动起来，冰碴一片片崩落，苏清月把火焰稳稳对着齿轮牙，白色蒸汽在两人身边翻滚。",
   SOUND_WHEEL, AES_FLAME, cam=rise('the two of them, the turning valve and the rolling steam', '两人、转动的阀门和翻滚的蒸汽'),
   room={'Lin', 'Su'}, new=True,
   bg='Behind them the frost-furred pipes run into the fog and the open steel door glows orange at frame-left.',
   holds='The frame holds exactly two people: Lin and Su, at the valve wheel, nobody else.')

insert2('27-07', '07｜插镜：压力表的指针从红区慢慢落向绿区，管道顶上喷出一大团白色蒸汽，墙壁的呻吟渐渐停了', 4, ICE_GAUGE,
        'Close shot of the pressure gauge in the middle third of the frame, nobody in the scene.',
        "The needle of the big pressure gauge sinks slowly from the red danger zone toward the green while the relief pipe above it jets a roaring plume of white steam and the groaning of the walls fades away. Nothing else moves.",
        "大压力表的指针从红色危险区慢慢落向绿区，上面的泄压管喷出一大团轰鸣的白色蒸汽，墙壁的呻吟声渐渐消失。别的什么都不动。",
        SOUND_AFTER, 'The frame holds the pressure gauge and the relief pipe, and nobody in the scene.',
        push1('the falling needle of the gauge', '指针往下落的压力表'), AES_ICEWARM)

TA('27-08', '08｜冰窖：旁边的老水管砰地崩开，水柱和冰碴直冲苏清月，林峰猛地扑过去把她罩在身下', 6, ICE_BURST,
   [P('lin_arctic', 'left', "standing at the valve wheel in profile facing frame-right, his head turning toward her, his weight shifting onto his front foot as he starts to move", 'Su', "his jaw clenched, his eyes wide, his brows low"),
    P('su_down', 'right', "standing beside the valve in profile facing frame-left, her blowtorch lowered in her hands, watching the wheel turn", 'obj:the turning valve wheel', "her lips parted, her eyes wide, her brows lifting")],
   'Medium wide two-shot, both from the head to the knees, in the middle third of the frame, at the valve wheel with the split pipe at frame-right.',
   "<lin_arctic> throws himself across the gap and wraps both arms around <su_down>, pulling her down onto the icy floor with his own back to the spray as the burst of water and ice shards hammers across his shoulders, his jaw clenched and his brows low; <su_down> gasps, her eyes wide and her lips parted.",
   "林峰一步扑过去，双手抱住苏清月，把她按倒在冰地上，自己的后背迎着喷射的水柱，水和冰碴砸在他的肩上，他下颌咬紧、眉头压低；苏清月倒抽一口气，眼睛睁大、嘴唇微张。",
   SOUND_BURST2, AES_FLAME, cam=push('both of them', '两人'), room={'Lin', 'Su'}, new=True,
   bg='Behind them the old side pipe on the right wall splits open and sprays a fan of water and ice shards, and the open steel door glows orange at frame-left.',
   holds='The frame holds exactly two people: Lin and Su, at the valve wheel, nobody else.')

# ================================================================================================ 第 28 集
b28 = S.episode('剧本第28集｜血与面包', '水柱渐渐变成滴水，墙壁的挤压声彻底停了，警报解除；林峰的手臂被划开，袖子渗红，他死死把她护在身下；两人瘫坐在结冰的地上喘气，苏清月红着眼眶骂他疯子，林峰擦掉她脸上的冰水：只要你没事就行，走，回家；回到25℃的生活区，苏清月为他包扎伤口；林峰又拿出面粉、黄油和酵母，两人并肩揉面，烤箱里的面包胀成金黄；叮的一声，面包出炉，满屋都是烤面包的香气；然后画面切到地表雪原，一个穿着白色极地军用外骨骼装甲的高大身影，悄无声息地跪在冰雕前，用仪器扫描着雪地。', 28)
new_person(b28, 'scout', '外骨骼侦察兵（哑光白色极地军用外骨骼装甲，全遮脸的白色头盔和黑色护目面罩）', 'man',
           'A tall armored soldier in a sleek matte-white military polar exoskeleton armor with articulated servo joints, a full white helmet with a black tinted faceplate hiding his whole face and a slim black survey probe in one gloved hand.',
           '一个高大的披甲士兵，穿着流线型的哑光白色极地军用外骨骼装甲，关节处有伺服机构，戴着全遮脸的白色头盔和黑色护目面罩，一只戴手套的手里拿着一根细长的黑色探测杆。',
           'a tall figure in sleek matte-white military polar exoskeleton armor with articulated servo joints, a full white helmet with a black tinted faceplate hiding his whole face, a slim black survey probe in one gloved hand',
           'a tinted faceplate hiding his whole face', eth='tall armored')
b28.character('Scout', 'scout', SCOUT_EN, SCOUT_ZH)

TA('28-01', '01｜冰窖：水柱渐渐变成细流和雾，林峰趴在苏清月身上抬起头，袖子被划开、渗出红色，苏清月睁开眼', 6, ICE_AFTER,
   [P('lin_arctic', 'right', "lying over her on his forearms on the icy floor, his back to the dying spray, a long red stain spreading across the torn left sleeve of his white suit", 'Su', "his jaw clenched, his brows low"),
    P('su_down', 'left', "lying on her back on the icy floor under him, her gloved hands gripping his sleeves, her face turned up to him", 'Lin', "her lips trembling, her brows pulled together")],
   'Medium two-shot from slightly above, both lying on the floor, in the middle third of the frame, in the icy hall.',
   "The roaring jet thins into a trickle and then a drifting mist and the ice shards settle on the floor; <lin_arctic> lifts his head slowly, his jaw clenched and his brows low, and <su_down> opens her eyes, her lips trembling and her brows pulled together. The groaning of the walls fades into silence.",
   "咆哮的水柱变成细流，又变成飘散的雾，冰碴落在地上；林峰慢慢抬起头，下颌咬紧、眉头压低，苏清月睁开眼睛，嘴唇发颤、眉头拧在一起。墙壁的呻吟声渐渐消失在寂静里。",
   SOUND_AFTER, AES_ICEWARM, cam=rise('the two of them on the floor and the mist drifting through the hall', '躺在地上的两人和飘过大厅的薄雾'),
   room={'Lin', 'Su'}, new=True, holds='The frame holds exactly two people: Lin and Su, on the icy floor, nobody else.')

TA('28-02', '02｜冰窖：两人坐在结冰的地上喘气，苏清月红着眼眶骂他疯子，林峰擦掉她脸上的冰水，说只要你没事就行，走，回家', 10, ICE_AFTER,
   [P('su_down', 'left', "sitting on the icy floor in profile facing frame-right, her glasses crooked, tears freezing on her lashes", 'Lin', "her eyes red and brimming, her lips trembling, her brows pulled together"),
    P('lin_arctic', 'right', "sitting on the icy floor in profile facing frame-left, his torn left sleeve dark with blood held against his side, his right gloved hand reaching to wipe the ice water from her cheek", 'Su', "his jaw loosening, a faint warm curve at one corner of his mouth, his brows soft")],
   'Close medium two-shot, both from the head to the waist, in the middle third of the frame, on the icy floor.',
   "<su_down> speaks the first line to <lin_arctic> in a shaking, furious, sobbing voice, her eyes red and brimming, her lips trembling and her brows pulled together. <lin_arctic> wipes the ice water from her cheek and speaks the second line to <su_down> in a low, warm voice, then the third line, his jaw loosening, a faint warm curve at one corner of his mouth and his brows soft.",
   "苏清月用发抖、愤怒带着哭腔的声音对林峰说出第一句，眼眶发红含泪、嘴唇发颤、眉头拧在一起。林峰擦掉她脸上的冰水，用低沉温暖的声音对苏清月说出第二句，接着说出第三句，下颌放松、嘴角带着一丝温暖的弧度、眉毛舒展。",
   SOUND_AFTER_V, AES_ICEWARM, lines=[('su_down', "你这个疯子！差点没命！", 0.8, 'Lin'), ('lin_arctic', "只要你没事就行。", 4.4, 'Su'), ('lin_arctic', "走，回家。", 6.9, 'Su')],
   cam=push1('the two of them', '两人'), room={'Lin', 'Su'}, new=True,
   bg='Behind them the open steel door glows orange at frame-left and thin mist drifts over the glazed floor.',
   holds='The frame holds exactly two people: Su and Lin, sitting on the icy floor, nobody else.')

TA('28-03', '03｜沙发边：苏清月戴着手套跪在林峰身边，用白纱布一圈圈缠他划开的小臂，说别动，闭嘴，医生在干活', 9, SOFA_AID,
   [P('su_surgeon', 'left', "kneeling on the rug beside the sofa in profile facing frame-right, white surgical gloves on, winding white gauze round his forearm with both hands", 'obj:the cut on his forearm', "her lips pressed in a firm line, her brows drawn together in concentration"),
    P('lin_home', 'right', "sitting on the leather sofa in profile facing frame-left, his left forearm resting on his knee with a long clean cut across it", 'Su', "one corner of his mouth lifting, his jaw relaxed, his brows soft", outfit="in a soft grey henley with the left sleeve rolled to the elbow")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, beside the sofa.',
   "<su_surgeon> winds the gauze round his forearm with slow careful turns and speaks the first line to <lin_home> in a firm, gentle voice, her lips pressed in a firm line and her brows drawn together in concentration. <lin_home> answers with the second line to <su_surgeon> in a dry, lazy voice, one corner of his mouth lifting, then <su_surgeon> speaks the third line to <lin_home> in a brisk, bossy voice.",
   "苏清月用缓慢仔细的手法把纱布一圈圈缠在他的小臂上，用坚定又轻柔的声音对林峰说出第一句，嘴唇抿成一条线、眉头专注地拧着。林峰用干干的、慵懒的声音对苏清月答出第二句，嘴角微微上扬，然后苏清月用利落、霸道的声音对林峰说出第三句。",
   SOUND_SOFA, AES_AMBER, lines=[('su_surgeon', "别动，伤口很深。", 0.8, 'Lin'), ('lin_home', "小伤。", 3.5, 'Su'), ('su_surgeon', "闭嘴，医生在干活。", 5.0, 'Lin')],
   cam=slide('left', '左', 'the two of them stand out in the middle third of the frame with the bandaged forearm between them', '两人占画面中间三分之一、中间是缠着纱布的小臂'),
   room={'Su', 'Lin'}, new=True,
   bg='Behind them the deep brown leather sofa with its grey cashmere blanket stands against the wall and the open first-aid box lies on the coffee table.',
   holds='The frame holds exactly two people: Su and Lin, beside the sofa, nobody else.')

TA('28-04', '04｜厨房：两人并肩站在台边揉面，苏清月问手都伤了还要做面包，林峰说刚才太冷了，想闻点热的', 10, KITCH_BREAD,
   [P('su_cozy', 'left', "standing at the marble counter in profile facing frame-right, flour on her fingers, her head turned to him", 'Lin', "her lips curving in a small amazed sweet smile, her brows lifted"),
    P('lin_home', 'right', "standing beside her at the counter in profile facing frame-left, pressing the mound of dough with his right hand, a neat white bandage on his left forearm", 'obj:the dough under his hand', "his jaw relaxed, a quiet warm curve at one corner of his mouth, his brows soft", outfit="in a soft grey henley with the left sleeve rolled to the elbow, a neat white bandage on his left forearm")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the kitchen counter.',
   "<su_cozy> speaks the first line to <lin_home> in a half-scolding, half-amused voice, her lips curving in a small amazed sweet smile and her brows lifted. <lin_home> keeps kneading and speaks the second line to <su_cozy> in a low, quiet voice, his jaw relaxed, a quiet warm curve at one corner of his mouth and his brows soft.",
   "苏清月用半是责怪、半是好笑的声音对林峰说出第一句，嘴角弯成一个又惊讶又甜的小笑、眉毛上扬。林峰继续揉着面，用低沉安静的声音对苏清月说出第二句，下颌放松、嘴角带着一丝安静的温暖弧度、眉毛舒展。",
   SOUND_BREAD, AES_BREAD, lines=[('su_cozy', "手都伤了，还要做面包？", 0.8, 'Lin'), ('lin_home', "刚才太冷了，想闻点热的。", 4.3, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Beside the dough on the marble counter stand a bag of white flour, a block of butter and a small jar of yeast, and the black-and-gold stove with its oven glows behind them.',
   holds='The frame holds exactly two people: Su and Lin, at the kitchen counter, nobody else.')

insert2('28-05', '05｜插镜：烤箱的玻璃窗后，三个圆面包慢慢胀大，烤成金黄色，一缕香气的蒸汽从箱门上方卷起来', 5, OVEN,
        'Close shot of the oven door, the glass window in the middle third of the frame, nobody in the scene.',
        "Behind the oven glass three round loaves swell and turn golden brown in the orange glow, and a ribbon of fragrant steam curls up from the vent above the door and catches the lamp light. Nothing else moves.",
        "烤箱的玻璃窗后面，三个圆面包在橙色的光里慢慢胀大，烤成金黄色，一缕带着香气的蒸汽从箱门上方的气孔里卷起来，被灯光照亮。别的什么都不动。",
        SOUND_OVEN, 'The frame holds the oven door with its glass window and the three loaves, and nobody in the scene.',
        push1('the golden loaves behind the glass', '玻璃后面金黄的面包'), AES_BREAD)

TA('28-06', '06｜厨房：林峰戴着隔热手套端出一盘金黄的面包，热气扑出来，苏清月凑过去说好香啊，林峰说趁热尝一口', 8, OVEN_OPEN,
   [P('su_cozy', 'left', "leaning in beside him in profile facing frame-right, her face tipped toward the loaves, her hands clasped under her chin", 'obj:the golden loaves on the tray', "a delighted sweet smile on her lips, her eyes bright, her brows lifted"),
    P('lin_home', 'right', "standing at the open oven in profile facing frame-left, thick oven mitts on both hands lifting out a tray of three golden loaves, steam billowing off them", 'Su', "one corner of his mouth lifting, his jaw relaxed, his brows soft", outfit="in a soft grey henley with the left sleeve rolled to the elbow, a neat white bandage on his left forearm")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the open oven.',
   "<lin_home> lifts the tray out of the oven and the steam billows up between them; <su_cozy> speaks the first line to <lin_home> in a delighted, breathy voice, a delighted sweet smile on her lips, her eyes bright and her brows lifted. <lin_home> answers with the second line to <su_cozy> in a low, warm voice, one corner of his mouth lifting, his jaw relaxed and his brows soft.",
   "林峰把烤盘从烤箱里端出来，热气在两人之间涌起；苏清月用惊喜、屏着气的声音对林峰说出第一句，嘴角带着欣喜的甜笑、眼睛发亮、眉毛上扬。林峰用低沉温暖的声音对苏清月答出第二句，嘴角微微上扬、下颌放松、眉毛舒展。",
   SOUND_OVEN_V, AES_BREAD, lines=[('su_cozy', "好香啊！", 1.0, 'Lin'), ('lin_home', "趁热，尝一口。", 3.2, 'Su')],
   cam=slide('left', '左', 'the two of them stand in the middle third of the frame with the tray of loaves between them', '两人占画面中间三分之一、中间是那盘面包'),
   room={'Su', 'Lin'}, new=True,
   bg='Behind them the floured marble counter stands at frame-left and the cream rug and round wooden table glow softly in the background.',
   holds='The frame holds exactly two people: Su and Lin, at the open oven, nobody else.')

TA('28-07', '07｜地表雪原：极光下，外骨骼装甲的高大身影悄无声息地跪在冰雕前，把探测杆插进雪里，杆上一点红灯亮着', 6, PIT_ICE,
   [P('scout', 'right', "kneeling in the snow in profile facing frame-left at the rim of the pit in front of an ice-encased man, one gloved hand pressing the slim black probe into the snow", 'obj:the ice-encased man in front of him', "his mouth and jaw hidden behind the black faceplate")],
   'Wide high shot over the pit, the pit and the ring of ice figures in the middle third of the frame, the armored figure small at frame-right.',
   "<scout> presses the slim black probe into the snow at the feet of an ice-encased man and holds it there, a tiny red light glowing on the probe, while powdery snow blows past and the green aurora ripples overhead; his mouth and jaw stay hidden behind the black faceplate. Nobody else is in the scene.",
   "外骨骼侦察兵把细长的黑色探测杆插进一个冰雕脚下的雪里，就那样按着，杆上一点小红灯亮着，粉雪从旁边吹过，头顶的绿色极光在流动；他的嘴和下巴一直藏在黑色面罩后面。画面里没有别人。",
   SOUND_SNOW, AES_AURORA, cam=drop('the pit, the ring of ice figures and the kneeling armored figure', '坑、一圈冰雕和跪着的装甲身影'),
   extra_assets=(), room={'Scout', 'the ice figures'}, new=True, groups=[('the ice figures', 'center', 'obj:the pit')],
   bg='Around the pit stand the ring of ice-encased men, and the snowplow truck\'s headlights glow far at frame-left.',
   holds='The frame holds exactly one armored figure kneeling beside the ring of ice-encased men, nobody else alive.')

TA('28-08', '08｜地表雪原：侦察兵缓缓站起身，头盔转向远处黑压压的松林山坡，面罩上流动着绿色的极光，探测杆上的红灯一闪一闪', 6, PIT_ICE,
   [P('scout', 'center', "standing upright at the rim of the pit in profile facing frame-left, the slim probe lowered in his right gloved hand, his helmeted head turned toward the dark pine slope", 'obj:the dark snow-laden pine slope in the distance', "his mouth and jaw hidden behind the black faceplate")],
   'Medium close shot, the armored figure from the head to the waist, in the middle third of the frame, at the rim of the pit.',
   "<scout> rises slowly from his knee to his full height, the servo joints of his armor whirring softly, and turns his helmeted head toward the dark pine slope, the green aurora rippling across his black faceplate and the little red light on the probe blinking; his mouth and jaw stay hidden behind the faceplate. Nobody else is in the scene.",
   "外骨骼侦察兵从单膝跪地缓缓站到完全直立，装甲的关节轻轻嗡嗡响，他把戴着头盔的头转向黑压压的松林山坡，绿色的极光在他黑色的面罩上流动，探测杆上的小红灯一闪一闪；他的嘴和下巴一直藏在面罩后面。画面里没有别人。",
   SOUND_SNOW_SERVO, AES_AURORA, cam=push1('the helmeted head and shoulders of the armored figure', '装甲身影的头盔和肩甲'),
   room={'Scout'}, new=True,
   bg='Behind him the dark snow-laden pine slope rises in the distance and the ring of ice-encased men stands around the pit below him.',
   holds='The frame holds exactly one armored figure, standing at the rim of the pit, nobody else.')

doc = S.finish()
