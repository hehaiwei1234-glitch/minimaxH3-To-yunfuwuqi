#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 45–46 集，追加稿 018（2026-10-15）——“15 秒满内容”先行测试版。
hh 2026-10-15 09:58：“测试 15s 镜头，每集尽量多塞内容，不要让节奏这么慢吞吞的；角色干活的时候可以无对白时间长一点，正常聊天不要让对白空余时间超过 1.5 秒；
大场面要么好好做特效；先写 1–2 集让我先在服务器上跑。”（不写进文档，是先行测试版。）
以 017（剧本第 29–44 集合并稿）的 JSON 为底（style／素材／角色逐字复制），必须等 017 在插件里全部跑完再追加。

写法（本批与前 44 集不同的地方）：
  · 对白任务一律 15 秒，4 句（或 3 句＋收尾动作）从 0.6 秒起一句接一句，句间只留约 0.9 秒的换气（`GAP`），全任务说话约占 11–12 秒，后面留 2–3 秒收尾动作（H27 ① 的测法：12–15 秒 4 句短话＋结尾动作）；
  · 台词仍是“只留句末标点、一口气说完”（smooth_text），但不再收紧任务长度（本批覆盖 `_scene.smooth_task`，任务长度按我写的）；
  · 画外音（伊甸、黑客 K 的录音广播）和画面里的人混在同一个任务里排时间；
  · 大场面认真写特效（45-03 堡垒车爆炸、45-05 岩石门关上、46-06 车队），开场图把主体、光、特效的起点状态写清楚（H29）；
  · 每集有 lowrise／crane／光的近景插镜；运镜每个任务不同。
偏离大纲（交稿时已告诉 hh）：
  · 第 45 集：“快剪辑搜刮”改成一场两人对话里边拆边聊；炸掉堡垒车是我加的特效大场面（原大纲没有，要写成“满载而归”前的收尾，留下“敌人没有据点了”）；
    温泉里苏清月裹着白色浴巾坐在水里，只拍到锁骨以上，林峰穿浴袍坐在岩台上按她的肩，不拍入水的身体；
  · 第 46 集：伊甸苏醒、农场自动化、黑客遗言广播（只有声音和红色音频波形，不拍黑客的脸）、五百人车队（雷达红点＋雪原远景）；
    林峰说“等它红了，我亲手摘”是给结局埋的伏笔（第一颗番茄）。
H3 方面的风险（交稿时单列，不算我的错）：
  · 45-01 搬起玻璃圆柱＋收尾走向破损的门；45-03 爆炸（火球、冲击波、碎片，快动作）；45-05 巨大的岩石门合上（机械变化）；45-06 亲吻时两张脸融合、温泉里的人；
  · 46-02 伊甸画外音可能被画成多出一个人或画面里的人张嘴念；46-03 喷淋臂和果实；46-04 K 的广播（声音＋红色波形）；46-06 几百辆车的车队（多个小物体）；
  · 15 秒任务可能在约 8 秒自己切镜；后几句台词可能被挤到片尾；约一成开场图不按文字画。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
from _jihan_base6 import *
import _scene
from _scene import smooth_text, TONE_FIX
import _h3draft as _H

_H.configure(smooth=True, fixed_seed=37407, cap=12)   # 2026-10-15：15 秒任务让 sage attention 崩溃，全部压到 12 秒以内
OUT = '合并稿/018_第45-46集_十二秒版_制作稿_追加'
S = Session('合并稿/017_第29-44集_合并_草莓酱到幽灵陨落_制作稿_追加.json', OUT, 50000)
B6.S = S

# ---- 前几批脚本里的局部定义（017 的 JSON 里已有对应素材，这里只为生成文字）
LIN_GUN = "in a charcoal henley under a dark olive utility vest with a black tactical chest rig over it"
SU_WAR = "in a black quilted tactical cold-weather jacket zipped to the collarbone over a black thermal top, black trousers and black gloves, her long black hair in a high ponytail"
SERVER = Scene('server_cabin', " Cold blue server light fills a cramped armoured cabin.",
               " Fixed stage layout: a long narrow armoured cabin fills the frame; floor-to-ceiling server racks with thousands of tiny blue lights line both walls; a black swivel chair with a wide desk of dark screens stands at frame-left; at frame-right the torn steel edge of the breached side door lets in a slash of grey storm light; a glowing blue glass cylinder stands at the far end of the cabin.")
HC_WIDE = Scene('hot_cave', " Soft blue moss light and rolling white mist fill a vast natural cavern.",
                " Fixed stage layout: a vast natural cavern with walls and ceiling of dark rock thickly covered in softly glowing blue moss like a night sky; a steaming turquoise hot spring pool fills the middle of the frame with white mist rolling off it; smooth rock shelves line its edge; a narrow dark tunnel mouth is at frame-left.")

# ---------------------------------------------------------------------------------------------- 本批的台词排时间（15 秒任务、句间只留一口气）
GAP = 0.5
BRISK_EN = ' The lines follow one another at once with only a very short breath between them, each said in one breath with no pause inside the sentence.'
BRISK_ZH = ' 台词一句紧接着一句，中间只有很短的换气，每句一口气说完、句中不停顿。'
VOICE_ONLY = {'eden_voice', 'k_rec'}


def times(spec, gap=None):
    def run(g):
        out, t = [], 0.4
        for sp, tx, to in spec:
            tx2 = smooth_text(tx)
            out.append((sp, tx2, round(t, 2), to))
            t = t + _H.line_seconds(tx2) + g
        return out
    if gap is not None: return run(gap)
    out = run(GAP)
    if out[-1][2] + _H.line_seconds(out[-1][1]) + 1.1 > 12: out = run(0.35)     # 12 秒放不下：句间收到 0.35 秒
    return out


def smooth15(lines, dur, act_en, zh):
    spec = [(a, b, d) for a, b, c, d in lines]
    new = times(spec)
    need = lambda n: n[-1][2] + _H.line_seconds(n[-1][1]) + 0.05 + 1.0
    if need(new) > dur: new = times(spec, gap=0.35)           # 台词放不下：句间收到 0.35 秒
    if need(new) > dur:
        dur = min(13, int(need(new) + 0.99)); print('  [放宽到 %d 秒] ' % dur, act_en[:50])   # 仍放不下：最多放宽到 13 秒（009 里跑过 13 秒）
    for a, b in TONE_FIX: act_en = act_en.replace(a, b)
    return new, dur, act_en + BRISK_EN, zh + BRISK_ZH


_scene.smooth_task = smooth15          # 单个说话人集合的任务：保留我写的任务长度（15 秒），只改台词排法


def MIX(spec):
    """画外音和画面里的人混在一个任务里：返回 (画面里的人的台词, 画外音台词)，起点按整串排。"""
    allv = times(spec)
    on = [x for x in allv if x[0] not in VOICE_ONLY]
    off = [x for x in allv if x[0] in VOICE_ONLY]
    return on, off


# ---------------------------------------------------------------------------------------------- 光和空气（本批新增）
AES_SV = ("Cold blue server light washes both of them while the glass cylinder pours a deep blue glow across the cabin, a slash of grey storm light cuts the floor and a warm work lamp edges the equipment case in orange.",
          "冷蓝色的服务器光洗过两个人，玻璃圆柱把深蓝色的光泼满整节车厢，一道灰色的风暴光切过地板，一盏暖色的工作灯把设备箱描上橙色的边。")
AES_COREGLOW = ("Waves of deep blue light surge up the glass cylinder and spill across the dark racks, tiny threads of white light shiver inside it and loose cables trail dying blue sparks at its base.",
                "一波波深蓝色的光冲上玻璃圆柱，泼洒在黑暗的机架上，细细的白色光丝在里面颤动，松开的线缆在底座旁拖着快要熄灭的蓝色火花。")
AES_BLAST = ("A blinding orange-white fireball lights the whole black apron from within, the shockwave rolls a white wall of snow outward in a glittering ring, burning debris arcs through the dark in trails of embers and heat shimmers over the ice.",
             "一团耀眼的橙白色火球从里面照亮整片漆黑的停机坪，冲击波把一面白色的雪墙一圈圈推开，闪着光，燃烧的碎片拖着火星划过黑暗的空气，冰面上空热浪在颤动。")
AES_HOMEWARD = ("A fading orange afterglow flickers across the side glass while the warm amber dashboard glow settles on their faces and steam curls up from the two mugs in a hard teal-and-orange contrast.",
                "一点渐渐暗下去的橙色余光在侧窗上闪着，琥珀色的仪表灯光暖暖地落在两张脸上，两个杯子里的热气一缕缕卷起来，青橙对比分明。")
AES_GATE = ("The green aurora ripples across the black sky and its light glitters on the powder snow, headlight beams carve two bright shafts up the ramp and a deep amber glow spills from the opening in the mountain.",
            "绿色的极光在黑色的天空里流动，光洒在粉雪上闪着，车灯在坡道上劈出两道明亮的光柱，山体上的洞口里流出深琥珀色的光。")
AES_MTN = ("The green aurora pours its cold light over the whole white mountainside, a roaring blizzard streams across the slope in ribbons and a single thin thread of warm vapor glows pale gold as it rises from the snow.",
           "绿色的极光把冷冷的光倾泻在整座白色的山坡上，呼啸的暴风雪在山坡上拉成一条条飘带，一缕细细的暖色热气泛着淡金色的光从雪里升起。")
AES_BATH2 = ("Soft blue moss light and warm golden lamp glow meet over the rising steam, silver droplets bead on her shoulders and the rock, and a slow teal-and-orange glow rim-lights both faces.",
             "柔和的蓝色苔藓光和暖金色的灯光在升起的蒸汽上交汇，银色的水珠挂在她的肩膀和岩石上，缓缓的青橙色轮廓光描着两张脸。")
AES_RIPPLE = ("A slow wave of electric blue light sweeps across the whole wall of monitors one screen after another, each screen flaring from black to deep blue and washing the dim control room in cool light.",
              "一道缓缓的电蓝色光波从左到右一块接一块扫过整面监控墙，每块屏幕从黑色亮成深蓝，把昏暗的控制室洗成一片冷光。")
AES_PLUG = ("A deep blue glow from the cylinder rim-lights his hands and jaw while pale green indicator lights wink on across the console and her face glows faintly blue from the side.",
            "圆柱里深蓝色的光给他的手和下颌描上轮廓光，控制台上淡绿色的指示灯一盏盏亮起，她的脸侧面泛着淡淡的蓝光。")
AES_FARMAUTO = ("Fine silver mist from the ceiling rails drifts down through the pink-violet grow light and catches it in glittering threads, the leaves shine wet and the small green fruit glows soft in the haze.",
                "天花板轨道上喷出的细银色水雾缓缓飘下来穿过粉紫色的植物灯光，被照成一条条闪光的丝线，叶子湿润发亮，那颗小小的青色果实在雾里柔柔地发着光。")
AES_BCAST = ("A hard red pulse from the alarm lamp slams across the dark console in sharp waves and a jagged red audio waveform thrashes on the black screen, rim-lighting both faces in red.",
             "警报灯打出的强烈红光一下一下撞过黑色的控制台，黑色屏幕上一条锯齿状的红色音频波形在疯狂跳动，把两张脸描上红色轮廓光。")
AES_SAT = ("A cold blue map glow washes the console and both faces while a long column of tiny red dots crawls across the white terrain on the screen and a round red alarm lamp pulses on the wall.",
           "冷蓝色的地图光洗过控制台和两张脸，屏幕上白色的地形图中一长串小小的红点在缓缓爬动，墙上一盏圆形的红色警报灯一明一暗地闪着。")
AES_RAID = ("Hundreds of headlights string a long glowing line across the black snowfield under a faint green aurora, exhaust plumes rise white in the cold and blowing snow glitters in every beam.",
            "成百上千盏车灯在黑色的雪原上拉成一条长长的发光的线，上空一片淡淡的绿色极光，白色的尾气在寒气里升起，每一道光柱里都有吹雪在闪。")

# ---------------------------------------------------------------------------------------------- 声音
VT = ' Every word is fully voiced and audible.'
SOUND_SV = voiced('The cold electronic hum of servers, the click of latches and the scrape of a heavy case on steel.', '服务器冷冷的电子嗡鸣、搭扣的咔嗒声和沉重的箱子在钢板上拖动的刮擦声。')
SOUND_COREPULSE = breathy('A slow rhythmic electronic pulse, a deep low hum and a faint crackle of static.', '缓慢有节奏的电子脉冲声、深沉的低鸣和细细的电流杂音。')
SOUND_BLAST = breathy('A colossal thunderous explosion, a rolling shockwave roar, the crackle of fire and the patter of falling debris.', '一声巨大雷鸣般的爆炸、滚过去的冲击波轰响、火焰的噼啪声和碎片落下的哗啦声。')
SOUND_HOMEWARD = voiced('The smooth low hum of the engine, the soft hiss of warm air vents and a distant fading rumble.', '发动机顺滑的低鸣、暖风口轻轻的嘶嘶声和远处渐渐消失的隆隆声。')
SOUND_GATE = breathy('The thundering roar of tracks climbing a ramp, a deep grinding boom of a huge stone slab sliding shut and the soft hiss of settling snow.', '履带爬坡雷鸣般的轰响、巨大的石板合上时深沉的摩擦闷响和积雪落下轻轻的嘶嘶声。')
SOUND_MTN = breathy('A long low howl of a blizzard across a mountainside and the faint hiss of blowing snow.', '暴风雪掠过山坡长长的低啸和吹雪细细的嘶嘶声。')
SOUND_BATH2 = voiced('The gentle bubbling of hot water, a soft drift of water droplets and a faint far drip echoing.', '热水轻轻的咕嘟声、水珠轻轻滴落的声音和远处一滴水落下的回响。')
SOUND_RIPPLE = breathy('A rising soft electronic chime sweeping across a bank of screens and a low hum of power.', '一阵渐渐升高的轻柔电子鸣音扫过一排屏幕和低低的电流嗡鸣。')
SOUND_EDENWAKE = voiced('A soft rising electronic chime, the quiet clicking of relays and the low hum of the console.', '一阵轻柔渐强的电子鸣音、继电器细细的咔嗒声和控制台低低的嗡鸣。')
SOUND_FARMAUTO = voiced('The soft hiss of fine mist from the ceiling rails, the faint hum of the grow lamps and the quiet trickle of water in the channels.', '天花板轨道上细雾轻轻的嘶嘶声、植物灯细细的嗡鸣和水槽里水安静的淌水声。')
SOUND_BCAST = voiced('A sharp repeating alarm beep, crackling long-wave static and the hum of the console.', '尖锐反复的警报声、长波噼啪作响的杂音和控制台的嗡鸣。')
SOUND_SAT = voiced('A slow electronic ping, a sharp repeating alarm beep and the hum of the console.', '缓慢的电子嘀声、尖锐反复的警报声和控制台的嗡鸣。')
SOUND_RAID = breathy('The grinding crawl of hundreds of heavy engines through snow and a long low howl of wind.', '成百上千台重型发动机碾过雪地缓慢的轰鸣和风长长的低啸。')

# ---------------------------------------------------------------------------------------------- 外貌／声音
look('eden_voice', 'Eden', "a flat wall speaker panel with a thin glowing blue ring", 'none', 'its')
look('k_rec', 'KRec', "a wide black console screen showing a jagged red audio waveform", 'none', 'its')
EDEN_EN = 'A soft, calm, polite female synthetic voice from a wall speaker, smooth and unhurried, speaking clear Mandarin Chinese.' + VT
EDEN_ZH = '轻柔平静、礼貌的女性合成声音，从墙上的扬声器里传出，顺滑不急，普通话清楚。每个字都正常发声、清晰可辨。'
KREC_EN = 'A manic, cracking, gleeful young adult male voice with wild laughter, a distorted old recording from a speaker, speaking clear Mandarin Chinese.' + VT
KREC_ZH = '疯狂、发破、带着得意的年轻成年男声，夹着狂笑，是一段失真的旧录音，从扬声器里传出，普通话清楚。每个字都正常发声、清晰可辨。'
LIN_ROBE2 = "in a thick grey terry bathrobe tied at the waist, his black hair damp"
SU_TOWEL = "a white bath towel wrapped above her chest, her long black hair pinned up with damp strands clinging to her neck"

# ---------------------------------------------------------------------------------------------- 场景
SV_CORE = Scene('server_cabin', SERVER.end,
                " Fixed stage layout: the long narrow armoured cabin with server racks lining both walls fills the frame; in the middle the one-metre glowing blue glass cylinder stands in an open steel cradle with thick cables hanging loose from its base; an open grey equipment case lies on the floor at frame-left; the torn steel edge of the breached door at frame-right lets in a slash of grey storm light.")
SV_CLOSE = Scene('server_cabin', SERVER.end,
                 " Fixed stage layout: a close view of the one-metre glowing blue glass cylinder standing in its open steel cradle in the middle of the frame, thick cables hanging loose from its base with a few blue sparks, dark server racks glinting behind it.")
BASE_RIG = Scene('airbase', " A black frozen night over a vast airbase, blowing snow glittering in the headlights.",
                 " Fixed stage layout: a vast frozen airbase apron fills the frame at night; at frame-right the colossal white fortress truck stands intact with its torn side door dark and a small red lamp blinking on its flank; far behind it dark radar dishes stand against the black sky; at frame-left in the foreground the matte-black armoured tracked motorhome rolls away from the truck with its tail lights glowing and its back to it, snow glittering in its headlight beams.")
RG_OPEN = Scene('rock_gate', " A black night under a faint green aurora, powder snow glittering on a steep mountain flank.",
                " Fixed stage layout: a steep snow-covered mountain flank fills the frame; in the middle a huge slab of grey rock swung open reveals a dark tunnel mouth glowing amber from inside; a ramp of packed snow leads up to it; the matte-black armoured tracked motorhome climbs the ramp at frame-left with its headlights blazing, aimed into the opening; the aurora glows at the top of the frame.")
CAB_HOME = Scene('rv_cab', " Warm amber dashboard glow fills the compact armoured cab while the windshield shows a rushing white blizzard.",
                 " Fixed stage layout: a cutaway side view of the cab; two leather bucket seats stand side by side across the middle of the frame, both facing frame-right toward the wide armoured windshield showing a white blizzard, the passenger seat at frame-left and the driver's seat at frame-center-right with a short steel control lever beside it; two steaming mugs sit in the cup holders between the seats; a glass cylinder is strapped upright behind the seats with a faint blue glow.")
HC_BATH = Scene('hot_cave', HC_WIDE.end,
                " Fixed stage layout: a steaming turquoise hot spring pool fills the left and middle of the frame with white mist rolling off it; a smooth flat rock ledge fills the right of the frame at the pool's edge; walls of softly glowing blue moss rise at the back.")
SNOW_MTN = Scene('snow_field', " A black night under a bright green aurora over a white mountainside, a blizzard streaming across it.",
                 " Fixed stage layout: a vast white mountainside under a black sky fills the frame with a green aurora across the top; a blizzard streams across the slope in ribbons; in the middle of the slope a single thin thread of pale warm vapor rises from the snow; there is no door, no building and no vehicle anywhere in the frame.")
CTRL_RIP = Scene('bunker_control', " The compact underground control room lies in dim shadow.",
                 " Fixed stage layout: the wall of six small monitors at frame-left is dark; the steel control console stands in the middle of the frame with the one-metre glowing blue glass cylinder resting on it, thick cables running from its base into the console; a heavy steel door is in the right wall.")
CTRL_CORE = Scene('bunker_control', CONTROL.end,
                  " Fixed stage layout: the steel control console stands in the middle of the frame with the one-metre glowing blue glass cylinder on it, a thick cable plug at its base; the wall of six small monitors glows at frame-left; a small round speaker grille is set into the wall above the console.")
EDEN_AUTO = Scene('eden', EDEN.end,
                  " Fixed stage layout: long tiers of white hydroponic channels full of tomato plants fill the middle of the frame under rows of pink-violet grow lamps; thin silver sprinkler arms run along rails in the ceiling above them misting the plants; in the foreground one tomato vine carries a single small green fruit; the concrete walls fill the background.")
CTRL_RED = Scene('bunker_control', CONTROL.end,
                 CONTROL.layout + " A wide black screen on the console shows a jagged red audio waveform, a round red alarm lamp flashes high on the wall above it, and a black swivel chair stands in front of the console.")
CTRL_SAT = Scene('bunker_control', CONTROL.end,
                 CONTROL.layout + " A wide screen on the console shows a white terrain map with a long column of small red dots crawling toward its center, a round red alarm lamp flashes high on the wall above it, and a black swivel chair stands in front of the console.")
RAIDERS = Scene('snow_field', " A black night under a faint green aurora, a vast snowfield glittering in thousands of headlights.",
                " Fixed stage layout: a vast flat snowfield stretches to the horizon under a faint green aurora; a very long column of black heavy armoured trucks with spiked front plates and towed howitzers crawls from the far right toward the middle of the frame, hundreds of headlights stringing a glowing line across the snow; white exhaust plumes rise from every engine.")

# ================================================================================================ 第 45 集
b45 = S.episode('剧本第45集｜满载而归的温泉浴',
                '堡垒车服务器车厢里，苏清月蹲在敞开的设备箱前拆雷达模块，林峰把一米高发光的量子核心从支架里抱起来，两个人一边搬一边斗嘴；核心特写里蓝光一波波往上爬；装甲房车离开基地，身后白色堡垒车被引爆，橙白色的火球照亮整片停机坪；驾驶舱里苏清月说只想泡温泉，靠在林峰肩上；房车驶进山体的隐蔽石门，石门合上，雪盖住接缝；溶洞温泉里林峰给她按肩说核心接上以后全自动，她说接下来会很无聊，他低头吻她；最后镜头拉远到暴风雪的山坡，雪里只有一缕暖暖的热气。', 45)
b45.prop('raider_column', '黑血军团车队（一长列黑色重型装甲卡车，车头有尖刺撞板，后面拖着榴弹炮，白色的尾气）',
         'A very long column of black heavy armoured trucks with spiked front ram plates and towed howitzers, headlights blazing and white exhaust plumes rising. The reference fixes its look.',
         '一长列黑色重型装甲卡车，车头是尖刺撞板，后面拖着榴弹炮，车灯亮着，白色尾气升起。参考图固定它的外形。',
         'A photorealistic shot of a very long column of black heavy armoured trucks with spiked front ram plates and towed howitzers on a snowfield at night, headlights blazing, against a dark background.')
new_scene(b45, 'rock_gate', '山体上的隐蔽石门（陡峭的积雪山坡，中间一整块灰色的巨大岩石门板，一条压实的雪坡通向它）',
          'A steep snow-covered mountain flank at night with a huge slab of grey rock set into it like a door and a ramp of packed snow leading up to it.',
          '夜里一座陡峭的积雪山坡，中间嵌着一整块巨大的灰色岩石门板，一条压实的雪坡通向它。',
          'the steep snowy flank, the huge grey rock slab and the packed-snow ramp')

TA('45-01', '01｜堡垒车车厢：苏清月蹲在敞开的设备箱前把雷达模块塞进去，林峰把发光的玻璃圆柱从支架里抱起来，两个人一句接一句地斗嘴，最后他抱着核心朝破损的门走去，她合上箱子跟在后面', 15, SV_CORE,
   [P('su_tac', 'left', "kneeling at the open grey equipment case on the floor in profile facing frame-right, sliding a flat black radar module into the case, her head turned up to him", 'Lin', "her eyes bright and playful, her lips pressed in a teasing thin curl, her brows lifted", outfit=SU_WAR),
    P('lin_work', 'center-right', "standing at the open steel cradle in profile facing frame-left, both arms wrapped around the glowing blue glass cylinder lifting it out, his eyes on her", 'Su', "his jaw set, one corner of his mouth lifting in dry affection, his brows lifted", outfit=LIN_GUN)],
   'Medium wide two-shot, both from the head to the knees, in the middle third of the frame, in the server cabin.',
   "<su_tac> slides the radar module into the case and speaks the first line to <lin_work> in a brisk teasing voice, then <lin_work> lifts the glowing glass cylinder out of its cradle and answers with the second line to <su_tac> in a low dry voice, then <su_tac> speaks the third line to <lin_work> and <lin_work> answers with the fourth line to <su_tac>; after the last line <lin_work> carries the glowing cylinder toward the torn door while <su_tac> closes the case and follows him, her eyes bright and playful, her lips pressed in a teasing thin curl and her brows lifted.",
   "苏清月把雷达模块塞进箱子，用干脆带笑的声音对林峰说出第一句，接着林峰把发光的玻璃圆柱从支架里抱起来，用低沉干涩的声音对苏清月答出第二句，苏清月再对林峰说出第三句，林峰再对苏清月答出第四句；最后一句之后，林峰抱着发光的圆柱朝破损的门走去，苏清月合上箱子跟在他后面，眼神明亮俏皮、嘴唇抿出调皮的一弯、眉毛上扬。",
   SOUND_SV, AES_SV,
   lines=[('su_tac', "雷达模块拆好了。", 0.8, 'Lin'), ('lin_work', "核心小心点，别磕着。", 0.8, 'Su'), ('su_tac', "它比我还金贵？", 0.8, 'Lin'), ('lin_work', "你金贵，它只会算数。", 0.8, 'Su')],
   cam=track('the two of them', '两人'), extra_assets=('ai_core',), room={'Su', 'Lin'}, new=True,
   bg='Behind them dark server racks glint in rows on both walls and a slash of grey storm light falls through the torn steel door.',
   holds='The frame holds exactly two people: Su and Lin, in the server cabin, nobody else.')

insert2('45-02', '02｜插镜：一米高的玻璃圆柱立在敞开的支架里，一波波深蓝色的光冲上去，细细的白色光丝在里面颤动，松开的线缆在底座旁拖着快要熄灭的蓝色火花', 6, SV_CLOSE,
        'Close shot of the glass cylinder, the climbing blue light in the middle third of the frame, nobody in the scene.',
        "The one-metre glass cylinder stands in its open steel cradle as waves of deep blue light surge up inside it, tiny threads of white light shiver in the glass and the loose cables at its base trail a few dying blue sparks. Nothing else is in the scene.",
        "一米高的玻璃圆柱立在敞开的钢支架里，一波波深蓝色的光冲上去，细细的白色光丝在玻璃里颤动，底座旁松开的线缆拖着几点快要熄灭的蓝色火花。画面里没有别的东西。",
        SOUND_COREPULSE, 'The frame holds the glowing glass cylinder in its cradle, and nobody in the scene.',
        tilt('the glowing top of the glass cylinder', '玻璃圆柱发光的顶端'), AES_COREGLOW, extra_assets=('ai_core',))

insert2('45-03', '03｜空军基地：黑色的装甲房车载着核心驶离，身后巨大的白色堡垒车从内部炸开，一团橙白色的火球掀飞车顶，冲击波把雪墙一圈圈推开，燃烧的碎片划过黑夜', 15, BASE_RIG,
        'Wide shot of the airbase apron, centered in the middle third of the frame, the intact fortress truck at frame-right and the motorhome rolling away at frame-left, nobody visible.',
        "The matte-black armoured motorhome rolls away across the frozen apron with its tail lights glowing while the small red lamp on the flank of the colossal white fortress truck behind it blinks faster and faster, then the truck bursts open from the inside in a blinding orange-white fireball that blows its roof panels into the black sky, a ring of shockwave rolls a white wall of snow outward across the apron, burning debris arcs through the dark in trails of embers and the black motorhome in the foreground is lit orange from behind as it keeps rolling. Nothing else is in the scene.",
        "哑光黑色的装甲房车载着核心缓缓驶过冰封的停机坪，尾灯亮着，身后巨大的白色堡垒车侧面那盏小红灯越闪越快，然后堡垒车从里面炸开，一团耀眼的橙白色火球把车顶板掀进黑色的天空，一圈冲击波把一面白色的雪墙推开滚过整片停机坪，燃烧的碎片拖着火星划过黑暗，前景里黑色的房车被身后的火光照成橙色，仍然往前开。画面里没有别的东西。",
        SOUND_BLAST, 'The frame holds the airbase apron with the fortress truck, the fireball and the motorhome, and nobody visible.',
        rise('the whole burning airbase with the fireball, the shockwave and the departing motorhome', '整座燃烧的基地、火球、冲击波和远去的房车'), AES_BLAST, extra_assets=('fortress_truck', 'armored_rv'))

TA('45-04', '04｜驾驶舱：装甲房车行驶在白茫茫的暴风雪里，苏清月笑着问他是不是把整座基地炸了，说现在只想泡温泉，林峰说泡到皮都皱，她把头靠在他的肩上闭上眼睛', 15, CAB_HOME,
   [P('su_tacfit', 'left', "sitting in the passenger seat in profile facing frame-right, her black jacket folded over her knees, her head turned to him", 'Lin', "her eyes warm and amused, her lips curved in a tired sweet smile, her brows lifted"),
    P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, one hand on the control lever, his eyes on the white road ahead", 'obj:the rushing white road beyond the windshield', "his jaw loosening, one corner of his mouth lifting, his brows soft", outfit=LIN_GUN)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<su_tacfit> turns her head to <lin_work> and speaks the first line to him in a warm teasing voice, then <lin_work> keeps his eyes on the road and answers with the second line to <su_tacfit> in a low dry voice, then <su_tacfit> speaks the third line to <lin_work> and <lin_work> answers with the fourth line to <su_tacfit>; after the last line <su_tacfit> lays her head on his shoulder and closes her eyes while he drives on, her lips curved in a tired sweet smile and her brows soft.",
   "苏清月转头用温暖带笑的声音对林峰说出第一句，接着林峰眼睛看着路，用低沉干涩的声音对苏清月答出第二句，苏清月再对林峰说出第三句，林峰再对苏清月答出第四句；最后一句之后，苏清月把头靠在他肩上闭上眼睛，他继续开车，她的嘴唇弯着一个疲惫甜蜜的笑、眉头舒展。",
   SOUND_HOMEWARD, AES_HOMEWARD,
   lines=[('su_tacfit', "你把整座基地炸了？", 0.8, 'Lin'), ('lin_work', "留给别人当窝点吗？", 0.8, 'Su'), ('su_tacfit', "我现在只想泡温泉。", 0.8, 'Lin'), ('lin_work', "泡到你皮都皱。", 0.8, 'Su')],
   cam=push('both of them', '两人'), extra_assets=('ai_core', 'armored_rv'), room={'Su', 'Lin'}, new=True,
   bg='Behind the seats the glass cylinder is strapped upright with a faint blue glow and the windshield shows a rushing white blizzard.',
   holds='The frame holds exactly two people: Su and Lin, in the cab, nobody else.')

insert2('45-05', '05｜山体石门：黑色的装甲房车亮着车灯冲上积雪的坡道，开进山体上那个流着琥珀色光的洞口，巨大的岩石门板在身后轰隆隆地合上，飘落的雪盖住接缝，山坡重新变成一片完整的白', 12, RG_OPEN,
        'Wide low shot of the mountain flank, the huge rock slab and the climbing motorhome in the middle third of the frame, nobody else visible.',
        "The matte-black armoured motorhome climbs the packed-snow ramp with its headlights blazing and drives into the amber-lit tunnel mouth in the mountain flank, then the huge grey rock slab swings shut behind it with a deep grinding boom, powder snow drifts down across the seam and the slope becomes one unbroken white flank under the glowing green aurora. Nothing else is in the scene.",
        "哑光黑色的装甲房车亮着车灯冲上压实的雪坡，开进山体上那个流着琥珀色光的洞口，然后巨大的灰色岩石门板在它身后带着深沉的摩擦闷响合上，粉雪飘落盖住接缝，山坡在发光的绿色极光下变成一整片没有缝的白。画面里没有别的东西。",
        SOUND_GATE, 'The frame holds the mountain flank with the rock slab and the motorhome, and nobody else visible.',
        lowrise('the sealed white mountain flank under the green aurora', '合上后完整的白色山坡和上空的绿色极光'), AES_GATE, extra_assets=('armored_rv',))

TA('45-06', '06｜溶洞温泉：苏清月裹着白浴巾泡在温泉里，只露出肩膀，林峰穿着浴袍坐在岩台上给她按肩，说核心接上以后全自动，她说接下来几十年会很无聊，他低头吻了下去', 15, HC_BATH,
   [P('su_cozy', 'left', "sitting in the steaming turquoise water up to her collarbone with her back against his knees in three-quarter profile facing frame-right, her head tipped back and turned up to him, her bare shoulders above the water", 'Lin', "her eyes half-closed and soft, her lips parted in a blissful sweet smile, her brows relaxed", outfit=SU_TOWEL),
    P('lin_home', 'right', "sitting on the smooth rock ledge behind her in profile facing frame-left, both hands resting on her shoulders and kneading them, his head bent toward her", 'Su', "his eyes dark and warm on her face, his jaw loose, one corner of his mouth lifting, his brows soft", outfit=LIN_ROBE2)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, at the pool edge.',
   "<lin_home> kneads her shoulders and speaks the first line to <su_cozy> in a low lazy voice, then <su_cozy> tips her head back and answers with the second line to <lin_home> in a soft drowsy voice, then <lin_home> speaks the third line to <su_cozy> in a low warm voice; after the last line <lin_home> bends down and presses his lips to hers in a slow kiss while white steam rolls around them, his eyes closing and his brows soft, her lips parted in a blissful sweet smile.",
   "林峰给她按着肩，用低沉慵懒的声音对苏清月说出第一句，接着苏清月仰起头，用轻柔困倦的声音对林峰答出第二句，林峰再用低沉温暖的声音对苏清月说出第三句；最后一句之后，林峰低下头，在翻滚的白色蒸汽里慢慢吻住她的嘴唇，眼睛闭上、眉头舒展，她的嘴唇微张带着甜蜜幸福的笑。",
   SOUND_BATH2, AES_BATH2,
   lines=[('lin_home', "核心接上，浇水温控全自动。", 0.8, 'Su'), ('su_cozy', "接下来几十年，会很无聊。", 0.8, 'Lin'), ('lin_home', "无聊？那就找点事做。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the steaming turquoise pool rolls with white mist under walls of glowing blue moss.',
   holds='The frame holds exactly two people: Su and Lin, at the pool edge, nobody else.')

insert2('45-07', '07｜山坡：暴风雪呼啸着掠过整面白色的山坡，绿色的极光铺满上空，雪里只有一缕细细的暖色热气静静升起', 8, SNOW_MTN,
        'Wide shot of the white mountainside, the thread of vapor in the middle third of the frame, nobody visible.',
        "A roaring blizzard streams in ribbons across the whole white mountainside under the glowing green aurora while from one small spot in the middle of the slope a single thin thread of pale warm vapor rises steadily from the snow. Nothing else is in the scene.",
        "呼啸的暴风雪在发光的绿色极光下一条条飘带似的掠过整面白色的山坡，山坡中间雪里的一个小点，一缕细细的、淡淡的暖色热气静静地往上升。画面里没有别的东西。",
        SOUND_MTN, 'The frame holds the white mountainside with the thread of vapor, and nobody visible.',
        pull('the thin thread of warm vapor rising from the snow', '雪里升起的那缕暖色热气', 'the whole white mountainside under the green aurora', '整面白色的山坡和上空的绿色极光'), AES_MTN)

# ================================================================================================ 第 46 集
b46 = S.episode('剧本第46集｜潘多拉的死人倒计时',
                '控制室里，林峰把量子核心的粗线缆插进主控台，一道电蓝色的光波扫过整面监控墙，墙上的扬声器里传出温柔的合成女声：系统重启完毕，伊甸为您服务；地下二层的农场里天花板轨道喷出银色的细雾，苏清月看着第一颗青色的小番茄，林峰从背后抱住她说等它红了我亲手摘；忽然警报灯红光狂闪，截获的长波广播里是黑客K疯狂的录音：谁杀了我，坐标就发出去，黑血军团会来找你们；雷达屏幕上一长串红点爬向基地，伊甸报五十公里外有五百人的装甲车队，林峰按掉警报说那得多备几把扫雪铲；最后是雪原上成百上千盏车灯拉成的长线。', 46)
b46.character('Eden', 'hack_screen', EDEN_EN, EDEN_ZH)
b46.character('KRec', 'hack_screen', KREC_EN, KREC_ZH)

insert2('46-01', '01｜控制室：一道电蓝色的光波从左到右一块接一块扫过整面监控墙，黑色的屏幕一块块亮成深蓝，核心里的蓝光在控制台上一波波地涌', 5, CTRL_RIP,
        'Medium wide shot of the control room, the glowing cylinder on the console in the middle third of the frame, nobody in the scene.',
        "The one-metre glowing blue glass cylinder rests on the steel console as a slow wave of electric blue light sweeps across the wall of monitors from left to right, each black screen flaring to deep blue one after another. Nothing else is in the scene.",
        "一米高发光的蓝色玻璃圆柱放在钢制控制台上，一道缓缓的电蓝色光波从左到右扫过整面监控墙，每块黑色屏幕接连亮成深蓝。画面里没有别的东西。",
        SOUND_RIPPLE, 'The frame holds the control room with the glowing cylinder and the screens, and nobody in the scene.',
        slide('toward frame-left', '左', 'the whole wall of awakening monitors fills the left of the frame', '整面苏醒的监控墙占满画面左侧'), AES_RIPPLE, extra_assets=('ai_core',))

on, off = MIX([('eden_voice', "系统重启完毕，伊甸为您服务。", 'Lin'), ('eden_voice', "农场湿度百分之四十五。", 'Lin'), ('eden_voice', "温泉水温四十一度。", 'Lin'), ('eden_voice', "外部风暴，八级。", 'Lin')])
TA('46-02', '02｜控制室：林峰把核心的粗线缆插头用力推进底座，苏清月在旁边抱着手臂看，墙上的扬声器里传出温柔的合成女声，一连报出农场湿度、温泉水温和外面的风暴等级，苏清月忍不住弯起嘴角', 15, CTRL_CORE,
   [P('lin_work', 'right', "standing at the console in profile facing frame-left, both hands pushing a thick cable plug into the base of the glowing blue cylinder, his eyes on the plug", 'obj:the thick cable plug at the base of the glowing blue glass cylinder', "his jaw set, his eyes focused, one corner of his mouth lifting, his brows low", outfit=LIN_GUN),
    P('su_tac', 'left', "standing beside the console in profile facing frame-right, her arms folded, her eyes on the cylinder", 'obj:the glowing blue glass cylinder on the console', "her lips pressed in a curious thin line, her eyes bright, her brows lifted", outfit=SU_WAR)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "A soft, calm, polite female synthetic voice from the small speaker grille in the wall above the console speaks the first line, then the second line, then the third line and then the fourth line one right after another as a voice-over to <lin_work>. <lin_work> pushes the cable plug home with both hands, his jaw set, his eyes focused, one corner of his mouth lifting and his brows low, while <su_tac> stands beside the console with her arms folded, her lips pressed in a curious thin line, her eyes bright and her brows lifted, and at the end her lips curve upward.",
   "控制台上方墙里的小扬声器里传出轻柔平静、礼貌的女性合成声音，以旁白的方式一句接一句地说出第一句、第二句、第三句和第四句，对着林峰说。林峰双手把线缆插头推到底，下颌绷住、眼神专注、嘴角微微上扬、眉头压低，苏清月抱着手臂站在控制台旁边，嘴唇抿成一条好奇的细线、眼睛明亮、眉毛上扬，最后她的嘴角弯了起来。" + BRISK_ZH,
   SOUND_EDENWAKE, AES_PLUG,
   lines=on, vo=off,
   cam=push1('the plug in his hands and the glowing cylinder', '他手里的插头和发光的圆柱'), extra_assets=('ai_core', 'hack_screen'), room={'Su', 'Lin'}, new=True,
   bg='Above the console a small round speaker grille is set into the concrete wall and the wall of six small monitors glows deep blue at frame-left.',
   holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

TA('46-03', '03｜地下农场：天花板轨道上的细银水雾缓缓喷下来，苏清月捏着藤上那颗小小的青番茄惊喜地问它自己浇水施肥吗，林峰从背后抱着她说第一颗等它红了我亲手摘', 15, EDEN_AUTO,
   [P('su_cozy', 'left', "standing between two tiers of tomato plants in profile facing frame-right, her fingertips holding a small green tomato on the vine, her head turned up to him", 'Lin', "her eyes shining with delight, her lips parted in a delighted sweet smile, her brows lifted"),
    P('lin_home', 'center-right', "standing close behind her in profile facing frame-left, both arms around her waist and his chin resting beside her shoulder, his eyes on the green tomato", 'obj:the small green tomato on the vine', "his eyes warm and amused, one corner of his mouth lifting, his brows soft")],
   'Medium close two-shot, both from the head to the waist, in the middle third of the frame, between the tiers.',
   "<su_cozy> holds the small green tomato between her fingertips and speaks the first line to <lin_home> in a soft amazed voice, then <lin_home> answers with the second line to <su_cozy> in a low warm voice, then <su_cozy> speaks the third line to <lin_home> and <lin_home> answers with the fourth line to <su_cozy>; after the last line he tightens his arms around her while the fine silver mist drifts down over them, her eyes shining with delight and her brows lifted, his eyes warm and his brows soft.",
   "苏清月用指尖捏着那颗小小的青番茄，用轻柔惊喜的声音对林峰说出第一句，接着林峰用低沉温暖的声音对苏清月答出第二句，苏清月再对林峰说出第三句，林峰再对苏清月答出第四句；最后一句之后，他把手臂收得更紧，细银色的水雾缓缓飘落在两个人身上，她眼睛亮亮的、眉毛上扬，他眼神温暖、眉头舒展。",
   SOUND_FARMAUTO, AES_FARMAUTO,
   lines=[('su_cozy', "它自己浇水施肥？", 0.8, 'Lin'), ('lin_home', "控温授粉，全包。", 0.8, 'Su'), ('su_cozy', "第一颗番茄结果了。", 0.8, 'Lin'), ('lin_home', "等它红了，我亲手摘。", 0.8, 'Su')],
   cam=drop('the two of them between the tiers', '两排水培架中间的两个人'), room={'Su', 'Lin'}, new=True,
   bg='Above them thin silver sprinkler arms glide along the ceiling rails misting the plants and rows of pink-violet grow lamps glow along the tiers.',
   holds='The frame holds exactly two people: Su and Lin, between the tiers, nobody else.')

on, off = MIX([('k_rec', "谁杀了我，坐标就发出去。", 'Lin'), ('k_rec', "黑血军团会来找你们。", 'Lin'), ('k_rec', "一起下地狱吧，哈哈哈！", 'Lin')])
TA('46-04', '04｜控制室：红色警报灯狂闪，黑色屏幕上一条锯齿状的红色音频波形疯狂跳动，扬声器里传出黑客K疯狂失真的录音，林峰盯着屏幕，苏清月脸色发白抓紧他的肩膀', 15, CTRL_RED,
   [P('lin_home', 'right', "sitting in the black swivel chair at the console in profile facing frame-left, his hands flat on the desk, his eyes on the thrashing red waveform", 'obj:the jagged red waveform on the black screen', "his jaw clenched, his eyes cold and sharp, his brows low", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'center', "standing behind his chair in profile facing frame-left, one hand gripping his shoulder, her eyes on the screen", 'obj:the jagged red waveform on the black screen', "her lips parting, her face pale, her brows pulled high")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "A manic, cracking, gleeful young man's voice with wild laughter from the speaker beside the screen speaks the first, second and third lines one right after another as a voice-over to <lin_home>. <lin_home> sits motionless with his hands flat on the desk, his jaw clenched, his eyes cold and sharp and his brows low, while <su_cozy> stands rigid behind him gripping his shoulder, her lips parting, her face pale and her brows pulled high, as the red alarm pulse washes over them.",
   "屏幕旁边的扬声器里传出一个疯狂、发破、带着得意狂笑的年轻男声，以旁白的方式一句接一句地说出第一句、第二句和第三句，对着林峰说。林峰一动不动地坐着，两手平放在桌上，下颌咬紧、眼神冰冷锐利、眉头压低，苏清月僵直地站在他身后抓着他的肩膀，嘴唇微张、脸色发白、眉毛高高挑起，红色警报的光一阵阵洗过两个人。" + BRISK_ZH,
   SOUND_BCAST, AES_BCAST,
   lines=on, vo=off,
   cam=push('both of them', '两人'), extra_assets=('hack_screen',), room={'Su', 'Lin'}, new=True,
   bg='Beside the screen on the console a small round speaker grille glows faintly and the wall of six small monitors glows deep blue at frame-left.',
   holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

on, off = MIX([('eden_voice', "五百人车队，两小时后到。", 'Lin'), ('su_cozy', "五百个全副武装的人？", 'Lin'), ('lin_home', "那得多备几把扫雪铲。", 'Su')])
TA('46-05', '05｜控制室：雷达屏幕上一长串红点爬向基地中心，伊甸报出车队的人数和到达时间，苏清月脸色苍白地问五百个全副武装的人，林峰淡定地按掉警报，红光停了，说那得多备几把扫雪铲', 15, CTRL_SAT,
   [P('lin_home', 'right', "sitting in the black swivel chair at the console in profile facing frame-left, one finger resting on a red alarm button on the console, his eyes on the screen", 'obj:the long column of red dots crawling across the screen', "his jaw loose, one corner of his mouth lifting coldly, his eyes calm and dark, his brows relaxed", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'center', "standing beside his chair in profile facing frame-left, one hand pressed to her collarbone, her eyes on the screen", 'obj:the long column of red dots crawling across the screen', "her lips parted, her face pale, her brows pulled together")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "A soft, calm, polite female synthetic voice from the speaker beside the screen speaks the first line as a voice-over to <lin_home>; then <su_cozy> turns her face to <lin_home> and speaks the second line in a shaky voice, and <lin_home> answers with the third line to <su_cozy> in a calm low voice; as he finishes he presses the alarm button and the red pulse stops, his jaw loose, one corner of his mouth lifting coldly, his eyes calm and dark and his brows relaxed, while her lips stay parted, her face pale and her brows pulled together.",
   "屏幕旁边的扬声器里传出轻柔平静、礼貌的女性合成声音，以旁白的方式说出第一句，对着林峰说；接着苏清月转脸看着林峰，用发抖的声音说出第二句，林峰用平静低沉的声音对苏清月答出第三句；他说完按下警报按钮，红光停了，他下颌放松、嘴角冷冷一挑、眼神平静深沉、眉头舒展，她的嘴唇仍微张、脸色发白、眉头拧在一起。" + BRISK_ZH,
   SOUND_SAT, AES_SAT,
   lines=on, vo=off,
   cam=push('both of them', '两人'), extra_assets=('hack_screen',), room={'Su', 'Lin'}, new=True,
   bg='On the console a small round speaker grille glows faintly beside the wide terrain screen and the wall of six small monitors glows deep blue at frame-left.',
   holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

insert2('46-06', '06｜雪原：成百上千盏车灯在黑色的雪原上拉成一条长长的发光的线，一长列黑色的重型装甲卡车拖着榴弹炮缓缓爬向画面中央，白色的尾气一缕缕升起', 10, RAIDERS,
        'Wide low shot of the snowfield, the long column of trucks in the middle third of the frame, nobody visible.',
        "A very long column of black heavy armoured trucks with spiked front plates and towed howitzers crawls across the vast snowfield toward the middle of the frame under the faint green aurora, hundreds of headlights stringing a glowing line across the snow while white exhaust plumes rise from every engine. Nothing else is in the scene.",
        "一长列黑色的重型装甲卡车，车头是尖刺撞板，后面拖着榴弹炮，在淡淡的绿色极光下缓缓爬过辽阔的雪原，朝画面中央爬来，成百上千盏车灯在雪地上拉成一条长长的发光的线，每台发动机都升起白色的尾气。画面里没有别的东西。",
        SOUND_RAID, 'The frame holds the snowfield with the long column of trucks, and nobody visible.',
        lowrise('the endless column of glowing headlights across the snow', '雪原上无边无际的一长串发光的车灯'), AES_RAID, extra_assets=('raider_column',))

doc = S.finish()
