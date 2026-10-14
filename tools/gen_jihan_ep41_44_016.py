#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 41–44 集，追加稿 016（2026-10-14）。以 015 的 JSON 为底（style／素材／角色逐字复制），必须等 015 在插件里全部跑完再追加。
hh 2026-10-14 18:19：“再更新出来 16 集，我挂通宵，一批一批来，一次 4 集。”本批＝第四批（41–44，最后一批）。写法＝013／014／015 同一套（共用定义在 _jihan_base6.py）。

偏离大纲（交稿时已告诉 hh）：
  · 第 41 集：不拍“温度被篡改下降”的数字；用“农场灯光闪烁、叶子结霜、番茄花”表现变冷，切断线缆之后叶子上的霜化开、番茄花张开（养成：开花）；
    “缓冲舱外门被打开三厘米”只拍缝里灌进来的风雪这个结果；林峰拔匕首切线缆只拍切断后的两截线头和熄灭的火花（结果）；
    黑客的最后威胁用画外合成声音（同第 40 集），不写屏幕文字；
  · 第 42 集：弹药箱只拍林峰扛箱、不拍“电磁脉冲手雷”的细节；苏清月的战术笔电不写屏幕文字，只有脸上的蓝光；“扔给她一把手枪”改成他把枪柄递过去；
    装甲车碾冰出库只拍车头冲上坡道的结果；三架无人机只拍透过天窗看到的黑影和红色光点；
  · 第 43 集：无人机开火只拍装甲上的火花和曳光；漂移只拍车厢里两个人随车身倾斜；重机枪塔只拍升起后的结果；三架无人机变火球只拍天空里三团橙色火光和坠落的残骸；
    新增极地堡垒车（移动指挥中心）的远景，炮口对准镜头只拍结果；
  · 第 44 集：轨道炮发射只拍蓝色电弧划过的结果和后面塌了一半的塔台；撞门只拍结果（车头铲子嵌进撕裂的侧装甲门）；
    黑客 K 两句求饶压成两句（“我知道所有物资的密码”“我能让你成为冰河纪的王”）；开枪不拍过程和伤口：只拍林峰的台词，再切车外一个空镜（沉闷的一声响，雪原重归死寂），再拍林峰独自站在蓝光的量子计算核心前，K 不再入画。
H3 方面的风险（交稿时单列，不算我的错）：
  · 41-01 灯光闪烁＋叶子结霜；41-04 门缝里的风雪；41-06 切断的线头和火花；41-08 画外合成声音（可能画成屏幕里有人或画面里的人张嘴念）；
  · 42-01 车库大场景；42-02 扛箱子；42-04 递枪；42-05 装甲车冲出坡道；42-06 高速公路上的疾驰车辆；42-08 三架无人机（多个小物体）；
  · 43-01 火花与曳光（快速）；43-03 按开火键；43-04 机枪塔；43-05 三团火球和残骸；43-07 堡垒车的大场景；
  · 44-01 轨道炮蓝色电弧；44-03 撞门；44-04／44-05 林峰端着散弹枪和 K（新人物、没有数据）；44-08 发光的圆柱形计算核心；开场图约一成不按文字画；“同一处”场景用参照图。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
from _jihan_base6 import *
from _scene import smooth_task

import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407)   # hh 2026-10-14 16:20：台词顺滑写法＋全批固定视频种子
OUT = '合并稿/016_第41-44集_幽灵入侵重装出阵钢铁华尔兹幽灵陨落_制作稿_追加'
S = Session('合并稿/015_第37-40集_请君入瓮熊排溶洞温泉幽灵黑客_制作稿_追加.json', OUT, 48000)
B6.S = S

# ---------------------------------------------------------------------------------------------- 光和空气（本批新增）
AES_FLICK = ("The pink-violet grow lamps stutter and flicker over the green leaves, a thin crust of white frost creeps across one leaf and a single small yellow tomato flower trembles in the cold.",
             "粉紫色的植物灯在绿叶上方一闪一闪地跳着，一层薄薄的白霜爬上一片叶子，一朵小小的黄色番茄花在寒气里发着抖。")
AES_HACKRED = ("A hard red pulse from the alarm lamp slams across the dark console in sharp waves while green code light flickers on their faces and deep black shadow fills the edges of the frame.",
               "警报灯打出的强烈红光一下一下撞过黑色的控制台，绿色的代码光在两个人脸上闪，画面四周落满深深的黑影。")
AES_GAP = ("A thin blade of cold blue-white storm light cuts through the narrow gap in the gate and snow whips in across the steel floor in streaming ribbons, with a red warning glow on the walls.",
           "一道窄窄的冷蓝白色风暴光从闸门的缝里切进来，雪在钢板地面上拉成一条条飘带，墙上是一层红色的警告光。")
AES_CUT = ("Bright blue-white sparks die away in the air around the cut ends of the cable, a thread of grey smoke curls up and the dark console falls back into a calm cool green glow.",
           "亮亮的蓝白色火花在被切断的线头周围渐渐熄灭，一缕灰烟卷着上升，黑色的控制台重新沉入平静的冷绿色光里。")
AES_THAWLEAF = ("Steady pink-violet light settles over the green leaves, the frost melts into bright beads of water and the small yellow tomato flower slowly opens in the warm glow.",
                "稳稳的粉紫色光重新落在绿叶上，霜化成亮亮的水珠，小小的黄色番茄花在温暖的光里慢慢张开。")
AES_GHOSTDARK = ("The last pale green glow of the screen fades from their faces into a deep blue darkness while a tiny amber standby light glows on the console.",
                 "屏幕最后一点淡绿色的光从两个人脸上褪去，沉入深蓝色的黑暗里，控制台上一点小小的琥珀色待机灯亮着。")
AES_VOW = ("A cold white glow from the dark screen rim-lights his hard jaw and a dull red afterglow of the alarm lamp lingers on the wall behind him.",
           "黑下去的屏幕透出的冷白光给他绷紧的下颌描上轮廓，身后墙上警报灯残留着暗暗的红光。")
AES_GAR2 = ("Hot exhaust shimmers in the cold white floodlight, steam rolls off the idling armored vehicle and stacked green crates throw long hard shadows across the concrete.",
            "灼热的废气在冷白色的泛光灯下颤动，怠速的装甲车身上冒着蒸汽，一摞摞绿色箱子在水泥地上投下长长的硬影子。")
AES_CRATE = ("Cold white floodlight edges the crates and his shoulders in hard teal rim light while orange exhaust glow flickers on the concrete behind him and breath clouds drift in the air.",
             "冷白色泛光灯给箱子和他的肩膀描上硬朗的青色轮廓光，身后水泥地上闪着橙色的尾气光，呼出的白气在空气里飘。")
AES_LAPTOP = ("A soft blue glow from the laptop screen lights her face from below while the harsh white floodlight rim-lights her ponytail and a thin haze of exhaust hangs behind her.",
              "笔电屏幕柔和的蓝光从下面照亮她的脸，刺眼的白色泛光灯给她的马尾描上轮廓光，身后飘着一层薄薄的尾气雾。")
AES_HANDGUN = ("A sliver of cold light runs along the dark steel of the pistol between their hands while warm exhaust glow flickers behind them and a thin haze of steam drifts past.",
               "一线冷光沿着两个人手间那把手枪的深色钢身滑过，身后闪着温暖的尾气光，一缕缕蒸汽飘过。")
AES_RAMP = ("A white wall of blizzard light pours down the exit ramp into the dark garage, the black armored vehicle climbs into it with its headlights blazing and snow powder explodes off its blade.",
            "一面白色的暴风雪光从出口坡道倾泻进黑暗的车库，黑色的装甲车亮着车灯冲进光里，粉雪从车头铲子上炸开。")
AES_HWY = ("A white blizzard streams across the frozen highway in long ribbons, the green aurora flickers faintly through the storm and the black armored vehicle's headlights cut two long shafts through the white.",
           "白色的暴风雪在冰封的高速公路上拉成长长的飘带，绿色的极光在风暴里隐隐闪烁，黑色装甲车的车灯在白色里劈出两道长长的光柱。")
AES_RADARRED = ("A hard red pulse floods the compact cab from the radar screen and rim-lights both faces while the dashboard glows amber behind them and the windshield is a rushing white.",
                "一阵强烈的红光从雷达屏幕里涌满窄窄的驾驶舱，给两张脸描上红色轮廓光，背后仪表盘亮着琥珀色，挡风玻璃外是飞快掠过的白。")
AES_DRONES = ("Pinpricks of red light glow on the underside of three black drones as they dive through the blizzard, the green aurora glimmers behind them and snow streams past the thick skylight glass.",
              "三架黑色无人机从暴风雪里俯冲下来，机腹上亮着针尖一样的红光，绿色的极光在它们身后隐隐闪烁，雪从厚厚的天窗玻璃外飞快地掠过。")
AES_SPARKS = ("Bright orange tracer lines streak down from three black drones and burst into showers of white sparks across the dark armor, the green aurora glimmers above and snow streams across the frame.",
              "亮橙色的曳光从三架黑色无人机上划下来，在黑色的装甲上炸成一阵阵白色的火花，绿色的极光在上方隐隐闪烁，雪从画面里飞快地掠过。")
AES_SKYLIGHT = ("A cold white light from the skylight glass falls across their faces while the amber dashboard glow warms the lower half of the frame in a hard teal-and-orange contrast.",
                "天窗玻璃透进来的冷白光落在两个人脸上，琥珀色的仪表灯光暖暖地照亮画面的下半部分，形成强烈的青橙对比。")
AES_TURRET = ("Heavy gun barrels glow dull orange at their tips and rotate in a blur, hot brass casings tumble through the white blizzard and flashes light the snow in staccato pulses.",
              "沉重的枪管前端发着暗橙色的光，在模糊的旋转里喷出火光，滚烫的弹壳在白色的暴风雪里翻着掉下去，一闪一闪的火光把雪地照亮。")
AES_FIREBALL = ("Three orange fireballs bloom against the black sky and light the blizzard from within, burning wreckage tumbles out of them trailing black smoke and bright embers drift down into the snow.",
                "三团橙色的火球在黑色的天空里炸开，把暴风雪从里面照亮，燃烧的残骸拖着黑烟从里面翻着掉出来，明亮的火星飘落进雪里。")
AES_BASEFAR = ("A pale grey dawn-like glow breaks through the blizzard behind the dark radar dishes of the airbase and the huge white fortress truck gleams with a cold blue light along its armored flanks.",
               "一片灰白的、像黎明一样的光从暴风雪里透出来，照着空军基地黑色的雷达天线，巨大的白色堡垒车的装甲侧面泛着冷冷的蓝光。")
AES_RAIL = ("A forked blue electric arc tears across the blizzard in a blinding streak, white afterglow scars the dark air and the old control tower in the distance crumbles in a cloud of dust and sparks.",
            "一道分叉的蓝色电弧撕开暴风雪，划出耀眼的一道，白色的余光在黑暗的空气里留下灼痕，远处旧塔台在一团尘土和火花里塌下去。")
AES_DASH = ("The amber dashboard glow warms his hard face from below while the white storm rushes past the windshield and a blue arc afterglow flickers once across the glass.",
            "琥珀色的仪表灯光从下面照暖他绷紧的脸，挡风玻璃外白色的暴风雪飞快地掠过，一道蓝色电弧的余光在玻璃上闪了一下。")
AES_RAM = ("Dust and snow billow in a huge cloud around the buried blade, torn white armor plates glitter in the cold blue light and fine sparks rain down from the buckled metal.",
           "尘土和雪在嵌住的铲子周围翻成一大团云，撕裂的白色装甲板在冷蓝色的光里闪着，细细的火花从扭曲的金属上落下来。")
AES_SERVER = ("Cold blue server light washes the cramped cabin from rack after rack of tiny lights while pale screens glow behind them and every surface is rimmed with a thin blue edge.",
              "冷蓝色的服务器光从一排排小小的指示灯里洗遍狭窄的车厢，苍白的屏幕在他们身后发着光，每一个表面都被描上一圈细细的蓝边。")
AES_CORE = ("Pulses of deep blue light climb slowly up the glass cylinder in rhythmic waves, tiny threads of white light shiver inside it and a cold blue glow rim-lights the metal racks around it.",
            "一波一波深蓝色的光有节奏地沿着玻璃圆柱慢慢往上爬，细细的白色光丝在里面轻轻颤动，冷蓝色的光给周围金属架子描上一圈轮廓光。")
AES_QUIET = ("A deep blue hush lies over the airbase, thin blowing snow glitters across the apron and a small thread of grey smoke rises from the breach in the white truck into the dark sky.",
             "一片深蓝色的寂静盖在空军基地上，薄薄的吹雪在停机坪上闪着光，一缕灰色的细烟从白色大车的破口里升进黑色的天空。")

# ---------------------------------------------------------------------------------------------- 外貌／声音
look('hacker_k', 'HackerK', "in a washed-out grey hoodie with the hood down, thin round metal glasses sliding down his nose, a tangle of unwashed black hair", 'wide frightened dark', 'his', eth='a thin pale Chinese man in his late twenties')
look('ghost_voice', 'Ghost', "a wide black console screen", 'none', 'its')
K_EN = 'A thin, high, shaky young adult male voice, breathless and pleading, speaking clear Mandarin Chinese.' + VT_EN
K_ZH = '细细发高、发着抖的年轻成年男声，喘不上气地哀求，普通话清楚。' + VT_ZH
GHOST_EN = 'A flat, cold, androgynous synthetic voice from a console speaker, slow and unhurried, speaking clear Mandarin Chinese.' + VT_EN
GHOST_ZH = '平板冰冷、听不出男女的合成声音，从控制台扬声器里传出，缓慢不急，普通话清楚。' + VT_ZH
LIN_GUN = "in a charcoal henley under a dark olive utility vest with a black tactical chest rig over it"
SU_WAR = "in a black quilted tactical cold-weather jacket zipped to the collarbone over a black thermal top, black trousers and black gloves, her long black hair in a high ponytail"

# ---------------------------------------------------------------------------------------------- 场景
EDEN_LEAF = Scene('eden', EDEN.end,
                  " Fixed stage layout: long tiers of white hydroponic channels full of young tomato plants fill the middle of the frame under rows of pink-violet grow lamps; in the foreground a single tomato vine carries one small yellow flower and a thin crust of frost creeps across a nearby leaf; the concrete walls fill the background.")
CTRL_HK = Scene('bunker_control', CONTROL.end,
                CONTROL.layout + " A wide black screen on the console streams dense columns of unreadable green characters, a round red alarm lamp flashes high on the wall above it, and a black swivel chair stands in front of the console.")
CTRL_WIRE = Scene('bunker_control', CONTROL.end,
                  " Fixed stage layout: a thick bundle of black superconducting cable runs up the concrete wall behind the steel console in the middle of the frame to a hatch in the ceiling, with a red emergency lamp glowing on the wall at frame-left and the console with rows of small lights at frame-right.")
CTRL_CUT = Scene('bunker_control', CONTROL.end,
                 " Fixed stage layout: a thick bundle of black superconducting cable severed clean in two fills the middle of the frame, its cut ends hanging apart with a few dying blue sparks and a thread of grey smoke, a dark console below.")
CTRL_DARK = Scene('bunker_control', CONTROL.end,
                  CONTROL.layout + " A wide black screen on the console has gone dark with only a small amber standby light glowing, and a black swivel chair stands in front of the console.")
CH_GAP = Scene('buffer_chamber', " A red warning glow and cold blue storm light fill a bare steel chamber.",
               " Fixed stage layout: seen through a thick armoured-glass door in the foreground, a bare steel chamber with four round spray nozzles in its ceiling; the huge outer gate at the far end stands open only a narrow crack with a bright blade of blizzard light and streaming snow pouring through it.")
GARAGE_LOAD = Scene('bunker_garage', " Cool white floodlights fill the vast underground garage and hot exhaust shimmers in the air.",
                    " Fixed stage layout: the eight-metre long matte-black armoured tracked motorhome idles at frame-left with its rear cargo ramp lowered and exhaust steaming from it; stacked green metal ammunition crates stand in the middle of the frame on the grey concrete floor; the huge brushed-steel wall stands split open at frame-right.")
GARAGE_WIDE = Scene('bunker_garage', GARAGE.end,
                    " Fixed stage layout: the vast grey concrete garage hall fills the frame; in the middle the eight-metre long matte-black armoured tracked motorhome idles with hot exhaust steaming and its radar dome turning slowly, green ammunition crates being stacked by its rear ramp; the huge brushed-steel wall stands split open at frame-left.")
GARAGE_RAMP = Scene('bunker_garage', " A white wall of blizzard light pours into the dark garage from the exit ramp.",
                    " Fixed stage layout: a long steep concrete exit ramp climbs from the dark garage up toward a huge opening at frame-right full of white blizzard light; the matte-black armoured tracked motorhome climbs the ramp at the middle of the frame with its headlights blazing and a spray of snow thrown up at its blade.")
HWY = Scene('ice_highway', " A white blizzard fills the dark sky over a frozen highway with a faint green aurora glimmering through it.",
            " Fixed stage layout: a wide frozen highway lined with ice-encased cars and snow-covered guardrails recedes down the middle of the frame; the matte-black armoured tracked motorhome races along it from frame-left toward frame-right on wide tracks, throwing up a huge plume of snow; the storm streams in long ribbons across the frame.")
CAB_ALERT = Scene('rv_cab', " Warm amber dashboard glow and a pulsing red radar glow fill the compact armoured cab while the windshield shows a rushing white blizzard.",
                  " Fixed stage layout: a cutaway side view of the cab; two leather bucket seats stand side by side across the middle of the frame, both facing frame-right toward the wide armoured windshield, the passenger seat at frame-left with a small round radar screen set in the dashboard in front of it glowing red, and the driver's seat at frame-center-right with a short steel control lever beside it; the windshield at the right edge is a rushing white blizzard; a thick armoured skylight is in the roof above.")
CAB_FIGHT = Scene('rv_cab', " Warm amber dashboard glow fills the compact armoured cab while the windshield shows a rushing white blizzard.",
                  " Fixed stage layout: a cutaway side view of the cab; two leather bucket seats stand side by side across the middle of the frame, both facing frame-right toward the wide armoured windshield, the passenger seat at frame-left with a black rugged laptop open on her knees and the driver's seat at frame-center-right with a short steel control lever beside it and a red fire button on top of the lever; the windshield at the right edge is a rushing white blizzard.")
CAB_SKY = Scene('rv_cab', " Cold white skylight glow falls into the compact armoured cab from above.",
                " Fixed stage layout: seen from inside the cab looking straight up, a thick armoured skylight fills the middle of the frame, a rushing white blizzard beyond it; three small black armed drones with glowing red sensors dive through the storm toward the glass; the dark cab roof frames the skylight at the edges.")
SKY_BOOM = Scene('ice_highway', " A black blizzard sky is lit from within by burning fireballs.",
                 " Fixed stage layout: seen from low on the frozen highway looking up, the black blizzard sky fills the frame; three orange fireballs burn in the air in the middle of the frame with burning wreckage tumbling out of them toward the snow; the matte-black armoured motorhome stands at frame-bottom with a roof-mounted heavy machine-gun turret raised, its barrels glowing.")
TURRET = Scene('ice_highway', " A white blizzard fills the dark sky over a frozen highway.",
               " Fixed stage layout: a close low view of the roof of the matte-black armoured tracked motorhome; a heavy machine-gun turret with three thick barrels has risen from the roof and stands in the middle of the frame, firing upward into a white blizzard sky; the frozen highway streams past behind.")
BASE_FAR = Scene('airbase', " A grey-white glow breaks through a blizzard behind a ruined airbase.",
                 " Fixed stage layout: a huge frozen airbase apron fills the frame; dark radar dishes stand far away along the back of the frame; in the middle stands a colossal white polar all-terrain fortress truck twice the size of a motorhome, with a long electromagnetic railgun on its roof aimed straight down the apron toward the foreground; the matte-black armoured motorhome is a small dark shape at frame-bottom; blizzard snow streams across everything.")
BASE_TOWER = Scene('airbase', " A blinding blue electric arc tears through the blizzard over a ruined airbase.",
                   " Fixed stage layout: a vast frozen airbase apron fills the frame; the colossal white fortress truck stands at frame-right with a railgun on its roof pointed past the camera; a forked blue electric arc streaks across the middle of the frame; an old control tower stands at frame-left crumbling in a cloud of dust.")
BASE_RAM = Scene('airbase', " Cold blue light and billowing dust fill the frozen airbase apron.",
                 " Fixed stage layout: the matte-black armoured motorhome fills frame-left with its heavy steel blade buried deep in the torn side armor door of the colossal white fortress truck that fills frame-right, buckled white armor plates splayed around the breach, dust and snow billowing and sparks falling.")
BASE_QUIET = Scene('airbase', " A deep blue silence lies over a frozen ruined airbase under a dark sky.",
                   " Fixed stage layout: a vast frozen airbase apron fills the frame; the colossal white fortress truck stands in the middle with the black blade of the motorhome still buried in its torn side door and a thin thread of grey smoke rising from the breach; the dark radar dishes stand far away; thin snow blows across the apron.")
SERVER = Scene('server_cabin', " Cold blue server light fills a cramped armoured cabin.",
               " Fixed stage layout: a long narrow armoured cabin fills the frame; floor-to-ceiling server racks with thousands of tiny blue lights line both walls; a black swivel chair with a wide desk of dark screens stands at frame-left; at frame-right the torn steel edge of the breached side door lets in a slash of grey storm light; a glowing blue glass cylinder stands at the far end of the cabin.")
SERVER_K = Scene('server_cabin', SERVER.end,
                 " Fixed stage layout: the long narrow armoured cabin with server racks lining both walls fills the frame; a black swivel chair with a desk of dark screens stands in the middle of the frame; the torn steel edge of the breached door is at frame-right; the glowing blue glass cylinder stands at the far end.")
CORE_CLOSE = Scene('server_cabin', SERVER.end,
                   " Fixed stage layout: a tall glass cylinder of about a metre fills the middle of the frame, pulses of deep blue light climbing slowly up inside it and threads of white light shivering within, its metal base and cables at the bottom of the frame and dark server racks behind.")
CORE_MAN = Scene('server_cabin', SERVER.end,
                 " Fixed stage layout: the tall glowing blue glass cylinder stands in the middle of the frame with dark server racks on both sides; a slash of grey storm light from the breached door falls across the floor at frame-right.")

# ---------------------------------------------------------------------------------------------- 声音
SOUND_FLICK = breathy('A faint electric stutter from the lamps, a soft rustle of leaves and a thin hum of the air system.', '灯光闪动时细细的电流颤声、叶子轻轻的沙沙声和空气系统细细的嗡鸣。')
SOUND_HACK = voiced('The rapid clatter of a keyboard, a sharp repeating alarm beep and the hum of the console.', '键盘急促的敲击声、尖锐反复的警报声和控制台的嗡鸣。')
SOUND_HACK_B = breathy('The rapid clatter of a keyboard, a sharp repeating alarm beep and the hum of the console.', '键盘急促的敲击声、尖锐反复的警报声和控制台的嗡鸣。')
SOUND_GAP = breathy('A thin shrieking howl of wind through a narrow crack, snow hissing across steel and a low warning tone.', '风从一道窄缝里挤进来尖细的呼啸、雪嘶嘶地滑过钢板和一声低低的警告音。')
SOUND_CABLE = voiced('A low electric hum, a sharp repeating alarm beep and the creak of a thick cable.', '低低的电流嗡鸣、尖锐反复的警报声和一根粗电缆的吱呀声。')
SOUND_CUT = breathy('A single sharp electric crackle dying away, then a deep hush and the soft tick of cooling metal.', '一声尖脆的电流噼啪渐渐消失，然后是深深的寂静和金属冷却时轻轻的嘀嗒声。')
SOUND_THAWLEAF = breathy('The soft hush of a steady lamp, a gentle trickle of melting frost and a faint hum of the air system.', '一盏稳稳的灯轻轻的嘶声、霜融化时轻轻的淌水声和空气系统细细的嗡鸣。')
SOUND_GHOST = voiced('A deep silence, the faint hum of a speaker and a low crackle of static.', '深深的寂静、扬声器细细的嗡鸣和低低的电流杂音。')
SOUND_VOW = voiced('A deep hush, the faint hum of the console and the dull tick of cooling electronics.', '深深的寂静、控制台细细的嗡鸣和电子设备冷却时钝钝的嘀嗒声。')
SOUND_GAR = breathy('A deep rumble of an idling diesel engine, the hiss of steam and the clank of metal crates.', '柴油发动机怠速时深沉的低鸣、蒸汽的嘶嘶声和金属箱子的碰撞声。')
SOUND_GAR_V = voiced('A deep rumble of an idling diesel engine, the hiss of steam and the clank of metal crates.', '柴油发动机怠速时深沉的低鸣、蒸汽的嘶嘶声和金属箱子的碰撞声。')
SOUND_LAPTOP = voiced('A deep rumble of an idling diesel engine and the soft electronic chirp of a laptop starting up.', '柴油发动机怠速时深沉的低鸣和笔电启动时一声轻轻的电子嘀声。')
SOUND_RAMP = breathy('A thundering roar of a heavy engine climbing a ramp, the grinding of tracks and a howling rush of wind.', '重型发动机爬坡时雷鸣般的轰响、履带的碾压声和呼啸涌进来的风声。')
SOUND_HWY = breathy('The thundering roar of a diesel engine at full power, the hammering of tracks on ice and a screaming wind.', '柴油发动机全速时雷鸣般的轰响、履带砸在冰面上的敲击声和尖啸的风声。')
SOUND_RADAR_V = voiced('A sharp rising electronic alarm beep from the radar and the roar of the engine.', '雷达尖锐渐强的电子警报声和发动机的轰响。')
SOUND_DRONES = breathy('A rising high whine of rotors through the blizzard and the soft hiss of snow on glass.', '旋翼穿过暴风雪渐渐变高的尖啸声和雪打在玻璃上轻轻的嘶嘶声。')
SOUND_SPARKS = breathy('A brutal rattle of bullets hammering steel, a shower of ricochets and the howl of a blizzard.', '子弹砸在钢板上野蛮的哒哒声、一阵乱飞的跳弹声和暴风雪的呼啸。')
SOUND_CABFIGHT = voiced('The roar of the engine, the hammering rattle of bullets on armor and a quick electronic chirp.', '发动机的轰响、子弹砸在装甲上的哒哒声和一声急促的电子嘀声。')
SOUND_TURRET = breathy('The thunderous hammering roar of a heavy machine gun, the clatter of falling casings and a howling wind.', '重机枪雷鸣般的连发轰响、弹壳掉落时哗啦的声音和呼啸的风。')
SOUND_BOOM = breathy('A series of three heavy explosions rolling across the sky and a rain of burning debris hissing into snow.', '天空里三声沉重的爆炸一路滚过去，燃烧的残骸嘶嘶地砸进雪里。')
SOUND_CABQ = voiced('The smooth roar of the engine, the howl of the blizzard past the glass and a soft electronic hum.', '发动机平稳的轰响、玻璃外暴风雪的呼啸和轻轻的电子嗡鸣。')
SOUND_BASEFAR = breathy('A long low howl of wind across a vast airfield, the rattle of loose metal and a deep electric hum.', '风掠过辽阔的机场长长的低啸、松动金属的哗啦声和深沉的电流嗡鸣。')
SOUND_RAIL = breathy('A violent crackling electric whip-crack, a thunderous crash of masonry and the howl of the blizzard.', '一声猛烈的、噼啪作响的电流鞭击声、砖石轰然倒塌的巨响和暴风雪的呼啸。')
SOUND_RAM = breathy('A colossal tearing crash of steel, the screech of metal on metal and a rain of debris.', '钢铁被撕裂时巨大的碰撞声、金属刮擦金属的尖啸和碎片落下的哗啦声。')
SOUND_SERVER = voiced('The cold electronic hum of servers, the slow tick of cooling cables and a faint whistle of storm wind through the breach.', '服务器冷冷的电子嗡鸣、线缆冷却时缓慢的嘀嗒声和风暴从破口里透进来细细的啸声。')
SOUND_QUIET = breathy('A single muffled gunshot, then a deep dead silence and the thin hiss of blown snow.', '一声被闷住的枪响，然后是死一样的寂静和吹雪细细的嘶嘶声。')
SOUND_CORE = breathy('A slow rhythmic electronic pulse, a deep low hum and the faint crackle of static.', '缓慢有节奏的电子脉冲声、深沉的低鸣和细细的电流杂音。')

# ================================================================================================ 第 41 集
b41 = S.episode('剧本第41集｜幽灵入侵', '农场里的植物灯忽然疯狂闪烁，叶子上结了一层霜，那朵刚冒头的小番茄花在冷气里发抖；主控台上绿色的代码像瀑布一样滚动，林峰两手飞快地敲着键盘，冷笑着说想黑我的乌龟壳，你还嫩了点；苏清月脸色大变，说他在强行打开缓冲舱的外门，门缝已经三厘米了，极寒的风雪正从缝里灌进来；林峰没有犹豫，冲到主控台后面，一刀砍断了通往地表卫星天线的粗电缆，火花熄灭，大门重新锁死，农场的灯重新亮稳，叶子上的霜化成水珠，小番茄花在暖光里慢慢张开；屏幕在彻底黑掉之前，一个合成的声音说废弃空军基地，三天内来见我，否则我广播你的位置；林峰看着黑下去的屏幕，说敢威胁我，我成全你。', 41)

insert2('41-01', '01｜农场：粉紫色的植物灯疯狂闪烁，一片绿叶上爬满了白霜，旁边一朵小小的黄色番茄花在冷气里发抖', 6, EDEN_LEAF,
        'Low close shot of the tomato vine, the yellow flower and the frosted leaf in the middle third of the frame, nobody in the scene.',
        "The pink-violet grow lamps stutter and flicker over the tomato plants while a thin crust of white frost creeps across a green leaf and a single small yellow tomato flower trembles beside it in the cold. Nothing else moves.",
        "粉紫色的植物灯在番茄苗上方一闪一闪地跳着，一层薄薄的白霜爬满一片绿叶，旁边一朵小小的黄色番茄花在冷气里发着抖。别的什么都不动。",
        SOUND_FLICK, 'The frame holds the tomato vine with the yellow flower and the frosted leaf, and nobody in the scene.',
        lowrise('the trembling yellow flower and the frosted leaf', '发抖的黄色小花和结霜的叶子'), AES_FLICK)

TA('41-02', '02｜控制室：屏幕上绿色的代码像瀑布一样滚动，林峰两手飞快地敲着键盘，冷笑着说想黑我的乌龟壳，你还嫩了点，苏清月站在他身后', 8, CTRL_HK,
   [P('lin_home', 'right', "sitting in the black swivel chair at the console in profile facing frame-left, both hands flying across the keyboard, his eyes on the screen", 'obj:the wide black screen streaming green characters', "one corner of his mouth lifting in a cold sneer, his eyes sharp and burning, his brows low", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'center', "standing behind his chair in profile facing frame-left, one hand on the chair back, her eyes on the screen", 'obj:the wide black screen streaming green characters', "her lips pressed tight, her eyes wide, her brows pulled together")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "<lin_home> types fast with his eyes on the screen and speaks the one line to <su_cozy> in a low, cold, mocking voice, one corner of his mouth lifting in a cold sneer, his eyes sharp and burning and his brows low, while <su_cozy> watches the streaming green code from behind his chair, her lips pressed tight, her eyes wide and her brows pulled together.",
   "林峰一边飞快地敲着键盘一边盯着屏幕，用低沉冰冷、带着嘲讽的声音对苏清月说出这一句，嘴角冷冷地一挑、眼睛锐利发亮、眉头压低，苏清月站在他椅子后面看着滚动的绿色代码，嘴唇紧抿、眼睛睁大、眉头拧在一起。",
   SOUND_HACK, AES_HACKRED, lines=[('lin_home', "想黑我的乌龟壳，你还嫩了点。", 0.8, 'Su')],
   cam=push('both of them', '两人'), extra_assets=('hack_screen',), room={'Su', 'Lin'}, new=True,
   bg='Behind them a round red alarm lamp flashes high on the wall and the wall of six small monitors glows at frame-left.',
   holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

TA('41-03', '03｜控制室：苏清月盯着墙上的小监视器，脸色大变，对林峰说他在强行打开缓冲舱的外门，门缝已经三厘米了，林峰还在敲键盘', 10, CTRL_HK,
   [P('su_cozy', 'center', "standing beside the swivel chair in profile facing frame-left, one hand pointing at the wall of small monitors, her head turned to him", 'Lin', "her face gone white, her lips trembling, her brows pulled high"),
    P('lin_home', 'right', "sitting in the black swivel chair in profile facing frame-left, his hands still on the keyboard, his eyes snapping to her", 'Su', "his jaw clenched, his eyes hard, his brows low", outfit="in a soft grey henley and dark lounge pants")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "<su_cozy> points at the wall of small monitors and speaks the first line to <lin_home> in a tight, frightened voice and then the second line in a higher, shaking voice, her face gone white, her lips trembling and her brows pulled high, while <lin_home> keeps his hands on the keyboard and looks up at her, his jaw clenched, his eyes hard and his brows low.",
   "苏清月指着墙上的一排小监视器，用紧绷害怕的声音对林峰说出第一句，接着用更高、发抖的声音说出第二句，脸色发白、嘴唇发颤、眉毛高高挑起，林峰两手还放在键盘上，抬头看着她，下颌咬紧、眼神冷硬、眉头压低。",
   SOUND_HACK, AES_HACKRED, lines=[('su_cozy', "他在强行打开缓冲舱外门！", 0.8, 'Lin'), ('su_cozy', "门缝已经三厘米了！", 4.8, 'Lin')],
   cam=push('both of them', '两人'), extra_assets=('hack_screen',), room={'Su', 'Lin'}, new=True,
   bg='Behind them a round red alarm lamp flashes high on the wall and the wall of six small monitors glows at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, at the control console, nobody else.')

insert2('41-04', '04｜缓冲舱：外侧的合金闸门打开了一道窄窄的缝，一道刺眼的蓝白色风暴光从缝里切进来，雪在钢板地面上拉成一条条飘带', 6, CH_GAP,
        'Wide shot through the glass door, the narrow gap in the gate in the middle third of the frame, nobody visible.',
        "Seen through the thick glass door, the huge outer gate of the bare steel chamber stands open only a narrow crack and a blade of cold blue-white storm light cuts in through it while snow streams across the steel floor in long ribbons. Nothing else moves.",
        "透过厚厚的玻璃门，光秃秃的钢铁舱室里那扇巨大的外侧闸门只打开了窄窄的一道缝，一道冷冷的蓝白色风暴光从缝里切进来，雪在钢板地面上拉成长长的飘带。别的什么都不动。",
        SOUND_GAP, 'The frame holds the steel chamber with the narrow crack in the gate, and nobody visible.',
        push1('the narrow crack of storm light in the gate', '闸门缝里涌进来的风暴光'), AES_GAP)

TAV('41-05', '05｜控制室：林峰站在主控台后面，右手举起战术匕首，对准墙上那一大束通向地表卫星天线的粗电缆，低声说物理断网，现在', CTRL_WIRE,
    [P('lin_work', 'center', "standing in front of the thick black cable on the concrete wall in profile facing frame-right, his right hand raising a slim tactical dagger high over the cable, his eyes on the cable", 'obj:the thick black cable on the wall', "his jaw clenched, his eyes cold and absolutely certain, his brows low", outfit="in a charcoal henley under a dark olive utility vest"),
     P('su_cozy', 'left', "standing a step behind him in profile facing frame-right, one hand pressed to her chest, her eyes on the cable", 'obj:the thick black cable on the wall', "her lips parted, her eyes wide, her brows pulled together")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the cable.',
    "<lin_work> raises the slim tactical dagger high over the thick black cable and speaks the one line aloud to himself in a low, cold, fierce voice, his jaw clenched, his eyes cold and absolutely certain and his brows low, while <su_cozy> stands a step behind him holding her breath, her lips parted, her eyes wide and her brows pulled together.",
    "林峰把细长的战术匕首高高举在粗黑的电缆上方，用低沉冰冷凶狠的声音对自己说出这一句，下颌咬紧、眼神冰冷而绝对笃定、眉头压低，苏清月站在他身后一步屏住呼吸，嘴唇微张、眼睛睁大、眉头拧在一起。",
    SOUND_CABLE, AES_HACKRED, [('lin_work', "物理断网，现在。", 0.8, 'Lin')],
    cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
    bg='On the wall the thick bundle of black cable runs up toward a hatch in the ceiling and a red emergency lamp glows at frame-left.',
    holds='The frame holds exactly two people: Lin and Su, at the cable, nobody else.')

insert2('41-06', '06｜插镜：墙上那一大束粗黑的电缆被整齐地切成了两截，两截线头断开地垂着，几点蓝白色的火花正在熄灭，一缕灰烟往上卷', 5, CTRL_CUT,
        'Close shot of the severed cable, the cut ends in the middle third of the frame, nobody in the scene.',
        "The thick bundle of black cable hangs severed clean in two, its cut ends dangling apart as a few bright blue sparks die away and a thread of grey smoke curls slowly upward. Nothing else moves.",
        "那一大束粗黑的电缆被整齐地切成了两截，断开的两个线头垂着，几点亮亮的蓝白色火花慢慢熄灭，一缕灰烟慢慢往上卷。别的什么都不动。",
        SOUND_CUT, 'The frame holds the severed cable with its cut ends, and nobody in the scene.',
        push1('the two cut ends and the dying sparks', '断开的两个线头和熄灭的火花'), AES_CUT)

insert2('41-07', '07｜农场：植物灯重新稳稳地亮着，叶子上的白霜化成亮亮的水珠，那朵小小的黄色番茄花在暖光里慢慢张开了花瓣', 6, EDEN_LEAF,
        'Low close shot of the tomato vine, the opening yellow flower in the middle third of the frame, nobody in the scene.',
        "The pink-violet grow lamps burn steady again and the frost on the green leaf melts into bright beads of water while the small yellow tomato flower slowly opens its petals in the warm light. Nothing else moves.",
        "粉紫色的植物灯重新稳稳地亮着，绿叶上的白霜化成亮亮的水珠，那朵小小的黄色番茄花在暖光里慢慢张开了花瓣。别的什么都不动。",
        SOUND_THAWLEAF, 'The frame holds the tomato vine with the opening yellow flower, and nobody in the scene.',
        lowrise('the opening yellow flower and the beaded leaf', '张开的黄色小花和挂着水珠的叶子'), AES_THAWLEAF)

TAV('41-08', '08｜控制室：屏幕上的绿光一点点暗下去，扬声器里传出那个合成的声音说废弃空军基地，三天内来见我，否则我广播你的位置，林峰和苏清月一动不动', CTRL_DARK,
    [P('lin_home', 'right', "sitting in the black swivel chair at the console in profile facing frame-left, his hands resting on the keyboard, his eyes on the dimming screen", 'obj:the dimming wide black screen', "his jaw tight, his eyes sharp and cold, his brows low", outfit="in a soft grey henley and dark lounge pants"),
     P('su_cozy', 'center', "standing behind his chair in profile facing frame-left, one hand on the chair back, her eyes on the dimming screen", 'obj:the dimming wide black screen', "her lips parting, her face pale, her brows pulled high")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
    "A flat, cold, androgynous synthetic voice from the small speaker beside the screen speaks the first line and then the second line as a voice-over. <lin_home> sits motionless with his hands on the keyboard, his jaw tight, his eyes sharp and cold and his brows low, and <su_cozy> stands rigid behind him, her lips parting, her face pale and her brows pulled high, as the last green glow fades from the screen.",
    "控制台屏幕旁边的小扬声器里传出平板冰冷、听不出男女的合成声音，以旁白的方式说出第一句，接着说出第二句。林峰一动不动地坐着，两手放在键盘上，下颌绷紧、眼神锐利冰冷、眉头压低，苏清月僵直地站在他身后，嘴唇微张、脸色发白、眉毛高高挑起，屏幕上最后一点绿光慢慢褪去。",
    SOUND_GHOST, AES_GHOSTDARK, [('ghost_voice', "废弃空军基地，三天内来见我。", 0.8, 'Lin'), ('ghost_voice', "否则，我广播你的位置。", 4.8, 'Lin')],
    cam=push('both of them', '两人'), extra_assets=('hack_screen',), room={'Su', 'Lin'}, new=True,
    bg='Beside the screen on the console a small round speaker grille glows faintly and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

TA('41-09', '09｜控制室：屏幕全黑了，林峰盯着黑色的屏幕，眼里杀意翻涌，低声说敢威胁我，我成全你，苏清月在旁边看着他', 7, CTRL_DARK,
   [P('lin_home', 'right', "sitting in the black swivel chair at the console in profile facing frame-left, his hands curling into fists on the desk, his eyes on the black screen", 'obj:the black screen', "his eyes burning with cold murderous heat, one corner of his mouth lifting coldly, his jaw tight, his brows low", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'center', "standing beside the chair in profile facing frame-left, her eyes on him", 'Lin', "her lips parted, her eyes wide, her brows pulled together")],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, at the control console.',
   "<lin_home> keeps his eyes on the black screen and speaks the one line to <su_cozy> in a low, cold, quiet voice, his eyes burning with cold murderous heat, one corner of his mouth lifting coldly, his jaw tight and his brows low, while <su_cozy> watches him, her lips parted, her eyes wide and her brows pulled together.",
   "林峰眼睛盯着黑掉的屏幕，用低沉冰冷安静的声音对苏清月说出这一句，眼里翻涌着冰冷的杀意、嘴角冷冷一挑、下颌绷紧、眉头压低，苏清月看着他，嘴唇微张、眼睛睁大、眉头拧在一起。",
   SOUND_VOW, AES_VOW, lines=[('lin_home', "敢威胁我？我成全你。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the wall of six small monitors glows at frame-left and a dull red afterglow of the alarm lamp lingers on the wall.',
   holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

# ================================================================================================ 第 42 集
b42 = S.episode('剧本第42集｜重装出阵', '地下车库里灯光冷冽，八米长的黑色履带装甲房车引擎轰鸣，喷着灼热的废气；林峰一箱箱地把穿甲弹箱搬上车尾的货斜坡，这次的对手是懂高科技的顶尖黑客；苏清月换了一身干练的黑色战术防寒服，头发高高扎起，提着一台军用战术笔电走过来；林峰问她外面零下八十度还有电磁干扰，你不留在家里泡温泉；苏清月打开笔电，屏幕的蓝光映在她脸上，说你负责开枪，我负责电子战，没有我，林老板容易吃亏；林峰露出一丝赞赏的笑，把一把手枪柄朝她递过去；装甲车冲上出口坡道，冲进漫天风雪的白色废土，在冰封的高速公路上全速狂飙；忽然，苏清月面前的雷达屏幕发出刺耳的红光，她喊头顶有高频热源，速度极快；林峰猛地抬头，透过加厚的天窗，三架带红色传感器的武装无人机正穿透暴风雪，朝车顶俯冲下来。', 42)

insert2('42-01', '01｜地下车库：冷冷的泛光灯下，八米长的黑色履带装甲房车怠速轰鸣，车尾冒着灼热的废气和蒸汽，旁边一摞摞绿色的弹药箱', 6, GARAGE_WIDE,
        'Wide shot of the garage, the idling motorhome and the crates in the middle third of the frame, nobody visible.',
        "In the vast garage under cold white floodlights the matte-black armoured motorhome idles with hot exhaust and steam rolling off it, its radar dome turning slowly, and stacks of green ammunition crates stand by its lowered rear ramp. Nothing else moves.",
        "空旷的车库里，冷白色的泛光灯下，哑光黑色的装甲房车怠速轰鸣，车身上翻滚着灼热的废气和蒸汽，车顶雷达圆罩慢慢转着，放下的车尾斜坡旁堆着一摞摞绿色的弹药箱。别的什么都不动。",
        SOUND_GAR, 'The frame holds the vast garage with the idling armored motorhome and the ammunition crates, and nobody visible.',
        pull('the glinting ammunition crates by the ramp', '车尾斜坡旁闪着光的弹药箱', 'the whole garage hall with the idling motorhome', '整座车库大厅和怠速的装甲房车'), AES_GAR2, extra_assets=('armored_rv',))

TA('42-02', '02｜地下车库：林峰扛起一只绿色的弹药箱往车尾的斜坡上放，转头对走过来的苏清月说对手是顶尖黑客，还有电磁干扰，你不留在家泡温泉', 10, GARAGE_LOAD,
   [P('lin_work', 'left', "standing at the foot of the rear ramp in profile facing frame-right, setting a green metal ammunition crate down on the ramp with both hands, his head turned to her", 'Su', "his jaw set, one corner of his mouth lifting in dry challenge, his brows lifted", outfit=LIN_GUN),
    P('su_tac', 'center-right', "walking toward him across the concrete in profile facing frame-left, a rugged black laptop case in one hand, her ponytail swinging behind her", 'Lin', "her eyes bright and determined, her lips pressed in a firm line, her brows lifted", outfit=SU_WAR)],
   'Medium wide two-shot, both from the head to the knees, in the middle third of the frame, at the rear ramp.',
   "<lin_work> sets the crate down and speaks the first line to <su_tac> and then the second line in a low, dry, challenging voice, his jaw set, one corner of his mouth lifting in dry challenge and his brows lifted, while <su_tac> walks up to him with the laptop case in her hand, her eyes bright and determined, her lips pressed in a firm line and her brows lifted.",
   "林峰把弹药箱放在斜坡上，用低沉干涩、带点挑衅的声音对苏清月说出第一句，接着说出第二句，下颌绷住、嘴角带着干干的挑衅一挑、眉毛上扬，苏清月提着笔电箱朝他走过来，眼神明亮坚定、嘴唇抿成一条坚定的线、眉毛上扬。",
   SOUND_GAR_V, AES_CRATE, lines=[('lin_work', "对手是顶尖黑客，还有电磁干扰。", 0.8, 'Su'), ('lin_work', "你不留家里泡温泉？", 5.4, 'Su')],
   cam=track('the two of them', '两人'), extra_assets=('armored_rv',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the idling black motorhome steams under the cold floodlights and stacked green crates stand beside the ramp.',
   holds='The frame holds exactly two people: Lin and Su, in the garage, nobody else.')

TA('42-03', '03｜地下车库：苏清月把笔电放在车尾斜坡上打开，蓝光映在她脸上，抬头对林峰说你负责开枪，我负责电子战，没有我，林老板容易吃亏', 10, GARAGE_LOAD,
   [P('su_tac', 'left', "standing at the ramp in profile facing frame-right, one hand opening a rugged black laptop on the ramp, her head turned up to him", 'Lin', "her eyes bright and bold, her lips pressed in a confident curl, her brows lifted", outfit=SU_WAR),
    P('lin_work', 'right', "standing beside her in profile facing frame-left, his arms folded, his eyes on her", 'Su', "his eyes appraising, one corner of his mouth lifting, his brows lifted", outfit=LIN_GUN)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the rear ramp.',
   "<su_tac> opens the laptop, its blue glow lighting her face, and speaks the first line to <lin_work> and then the second line in a crisp, confident, teasing voice, her eyes bright and bold, her lips pressed in a confident curl and her brows lifted, while <lin_work> listens with his arms folded, his eyes appraising, one corner of his mouth lifting and his brows lifted.",
   "苏清月打开笔电，蓝光映亮她的脸，用干脆自信、带点挑逗的声音对林峰说出第一句，接着说出第二句，眼神明亮大胆、嘴唇抿出自信的一弯、眉毛上扬，林峰抱着手臂听着，眼神打量着她、嘴角一挑、眉毛上扬。",
   SOUND_LAPTOP, AES_LAPTOP, lines=[('su_tac', "你负责开枪，我负责电子战。", 0.8, 'Lin'), ('su_tac', "没有我，林老板容易吃亏。", 5.0, 'Lin')],
   cam=push('both of them', '两人'), extra_assets=('armored_rv',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the idling black motorhome steams under the cold floodlights and stacked green crates stand beside the ramp.',
   holds='The frame holds exactly two people: Su and Lin, at the rear ramp, nobody else.')

TA('42-04', '04｜地下车库：林峰露出一丝赞赏的笑，把一把手枪的枪柄朝苏清月递过去，说接着，苏清月伸手接住', 6, GARAGE_LOAD,
   [P('lin_work', 'right', "standing in profile facing frame-left, holding a compact black pistol out toward her handle-first at chest height", 'Su', "one corner of his mouth lifting in an approving smug smile, his eyes warm, his brows lifted", outfit=LIN_GUN),
    P('su_tac', 'left', "standing in profile facing frame-right, her gloved right hand closing around the pistol grip, her eyes on his face", 'Lin', "her eyes bright, her lips pressed in a fierce thin curl, her brows lifted", outfit=SU_WAR)],
   'Medium close two-shot, both from the head to the chest, with the pistol between them in the middle third of the frame, in the garage.',
   "<lin_work> holds out the pistol handle-first and speaks the one line to <su_tac> in a low, warm voice, one corner of his mouth lifting in an approving smug smile, his eyes warm and his brows lifted, and <su_tac> closes her gloved hand around the grip, her eyes bright, her lips pressed in a fierce thin curl and her brows lifted.",
   "林峰把手枪枪柄朝前递出去，用低沉温暖的声音对苏清月说出这一句，嘴角带着一丝赞赏得意的笑、眼神温暖、眉毛上扬，苏清月戴着手套的手握住枪柄，眼神明亮、嘴唇抿出凌厉的一弯细线、眉毛上扬。",
   SOUND_LAPTOP, AES_HANDGUN, lines=[('lin_work', "接着。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the idling black motorhome steams under the cold floodlights.',
   holds='The frame holds exactly two people: Lin and Su, in the garage, nobody else.')

insert2('42-05', '05｜出口坡道：黑色的装甲房车亮着车灯，轰鸣着冲上陡陡的混凝土坡道，车头的钢铲扬起一片粉雪，坡道尽头是白茫茫的暴风雪光', 6, GARAGE_RAMP,
        'Wide shot of the ramp, the climbing motorhome in the middle third of the frame, nobody else visible.',
        "The matte-black armoured motorhome roars up the steep concrete ramp with its headlights blazing, powder snow bursting off its blade, toward a huge opening full of white blizzard light at the top. Nothing else moves.",
        "哑光黑色的装甲房车亮着车灯，轰鸣着冲上陡陡的混凝土坡道，车头的钢铲炸开一片粉雪，坡道顶上是一个满是白色暴风雪光的巨大出口。别的什么都不动。",
        SOUND_RAMP, 'The frame holds the steep ramp with the climbing motorhome, and nobody else visible.',
        rise('the climbing motorhome and the white blizzard light at the top of the ramp', '爬坡的房车和坡道顶上白色的暴风雪光'), AES_RAMP, extra_assets=('armored_rv',))

insert2('42-06', '06｜冰封高速公路：漫天风雪里，黑色的装甲房车在结冰的高速公路上全速狂奔，宽履带砸起一大片雪雾，车灯劈开白色的风暴', 7, HWY,
        'Wide shot of the highway, the racing motorhome in the middle third of the frame, nobody else visible.',
        "On the frozen highway the matte-black armoured motorhome races at full speed through the blizzard on its wide tracks, throwing up a huge plume of snow while its headlights cut two long shafts through the white storm. Nothing else moves.",
        "冰封的高速公路上，哑光黑色的装甲房车在暴风雪里宽履带全速狂奔，扬起一大片雪雾，车灯在白色的风暴里劈出两道长长的光柱。别的什么都不动。",
        SOUND_HWY, 'The frame holds the frozen highway with the racing motorhome, and nobody else visible.',
        track('the racing motorhome', '飞驰的房车'), AES_HWY, extra_assets=('armored_rv',))

TAV('42-07', '07｜驾驶舱：雷达屏幕忽然发出刺耳的红光，苏清月瞪着屏幕喊头顶有高频热源，速度极快，林峰猛地抬头', CAB_ALERT,
    [P('su_tac', 'left', "sitting in the passenger seat in profile facing frame-right, one hand gripping the grab handle and the other pointing at the red radar screen, her eyes on the screen", 'obj:the small round radar screen glowing red', "her face gone white, her lips parted, her brows pulled high", outfit=SU_WAR),
     P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, his hands on the control lever, his head tilting up toward the skylight", 'obj:the armoured skylight in the roof', "his jaw clenched, his eyes sharp, his brows low", outfit=LIN_GUN)],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
    "<su_tac> stares at the red radar screen and speaks the one line aloud as a shout to <lin_work> in a tight, frightened voice, her face gone white, her lips parted and her brows pulled high, while <lin_work> grips the lever and tilts his head up toward the skylight, his jaw clenched, his eyes sharp and his brows low, a red pulse flooding the cab.",
    "苏清月瞪着发红光的雷达屏幕，用紧绷害怕的声音对林峰喊出这一句，脸色发白、嘴唇微张、眉毛高高挑起，林峰握紧操纵杆，抬头看向天窗，下颌咬紧、眼神锐利、眉头压低，红色的光一阵阵涌满驾驶舱。",
    SOUND_RADAR_V, AES_RADARRED, [('su_tac', "头顶有高频热源，速度极快！", 0.8, 'Lin')],
    cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
    bg='Above them a thick armoured skylight is set in the roof and the small round radar screen glows red in the dashboard at frame-left.',
    holds='The frame holds exactly two people: Su and Lin, in the cab, nobody else.')

insert2('42-08', '08｜天窗：透过加厚的天窗玻璃，三架黑色的武装无人机从暴风雪里俯冲下来，机腹上亮着针尖一样的红色传感器光', 6, CAB_SKY,
        'Low shot looking straight up through the skylight, the three drones in the middle third of the frame, nobody in the scene.',
        "Looking up through the thick armoured skylight, three black armed drones with pinpricks of red light on their undersides dive in formation through the rushing blizzard toward the glass. Nothing else moves.",
        "透过加厚的装甲天窗往上看，三架黑色的武装无人机排成一队从飞驰的暴风雪里俯冲下来，机腹上亮着针尖一样的红光，朝着玻璃压过来。别的什么都不动。",
        SOUND_DRONES, 'The frame holds the skylight with the three diving drones, and nobody in the scene.',
        tilt('the three diving drones', '三架俯冲的无人机'), AES_DRONES, extra_assets=('combat_drone',))

# ================================================================================================ 第 43 集
b43 = S.episode('剧本第43集｜雪原上的钢铁华尔兹', '三架武装无人机在风雪里开火，机炮子弹打在黑色钛合金装甲上，火花四溅，根本打不穿；车厢里林峰握着操纵杆对苏清月说干扰它们的信号，把火控权交给我；苏清月在笔电上飞快地敲着，说干扰成功，它们盲了三秒；林峰按下操纵杆上的红色开火键，说三秒，足够了；车顶一座重机枪塔升起，三根粗枪管喷着火光；天空里炸开三团橙色火球，燃烧的残骸砸进雪里；装甲车继续往前，苏清月说前面就是空军基地的雷达塔；暴风雪的尽头，基地停机坪上停着一辆比装甲车大一倍的白色极地堡垒车，车顶一门电磁轨道炮炮口朝着停机坪这一头。', 43)
b43.prop('combat_drone', '武装无人机（黑色的、机身扁平的四旋翼无人机，机腹有一个小炮口和针尖一样的红色传感器灯）',
         'A small flat-bodied black four-rotor armed drone with a tiny cannon muzzle and a pinprick red sensor light on its underside. The reference fixes its look.',
         '一架黑色的机身扁平的四旋翼武装无人机，机腹有一个小炮口和针尖一样的红色传感器灯。参考图固定它的外形。',
         'A photorealistic shot of a small flat-bodied black four-rotor armed drone with a tiny cannon muzzle and a pinprick red sensor light on its underside, seen from below in a three-quarter view against a plain dark gray background.')
b43.prop('fortress_truck', '极地全地形堡垒车（白色涂装、比装甲房车大一倍的巨型移动指挥中心，车顶一门长长的电磁轨道炮）',
         'A colossal white-painted polar all-terrain fortress truck twice the size of an armoured motorhome with huge wheels, thick armor plates and a long electromagnetic railgun on its roof. The reference fixes its look.',
         '一辆白色涂装的极地全地形堡垒车，比装甲房车大一倍，轮子巨大，装甲板厚重，车顶有一门长长的电磁轨道炮。参考图固定它的外形。',
         'A photorealistic shot of a colossal white-painted polar all-terrain fortress truck twice the size of an armoured motorhome with huge wheels, thick armor plates and a long electromagnetic railgun on its roof, seen from a low three-quarter angle against a plain dark gray background.')
new_scene(b43, 'ice_highway', '冰封的高速公路（宽阔的高速公路，两侧是被冰包住的废弃汽车和盖满雪的护栏，漫天暴风雪）',
          'A wide frozen highway lined with ice-encased abandoned cars and snow-covered guardrails under a white blizzard.',
          '一条宽阔的冰封高速公路，两侧是被冰包住的废弃汽车和盖满雪的护栏，漫天是白色的暴风雪。',
          'the frozen highway, the ice-encased cars and the snow-covered guardrails')

insert2('43-01', '01｜冰封高速公路：三架黑色的无人机在暴风雪里俯冲着开火，亮橙色的曳光打在黑色的装甲上，炸成一阵阵白色的火花', 6, HWY,
        'Wide shot of the highway, the motorhome and the diving drones in the middle third of the frame, nobody else visible.',
        "Three black armed drones dive through the blizzard above the racing matte-black armoured motorhome and bright orange tracer lines streak down from them to burst in showers of white sparks across its dark armor. Nothing else moves.",
        "三架黑色的武装无人机在暴风雪里朝着飞驰的哑光黑色装甲房车俯冲，亮橙色的曳光从它们身上划下来，在黑色的装甲上炸成一阵阵白色的火花。别的什么都不动。",
        SOUND_SPARKS, 'The frame holds the highway with the racing motorhome and the three diving drones, and nobody else visible.',
        track('the racing motorhome under the drones', '无人机下面飞驰的房车'), AES_SPARKS, extra_assets=('armored_rv', 'combat_drone'))

TA('43-02', '02｜驾驶舱：车厢随着车身在冰面上倾斜，林峰两手握紧操纵杆，对苏清月说干扰它们的信号，把火控权交给我，苏清月在腿上的笔电上飞快地敲着，说干扰成功，它们盲了三秒', 10, CAB_FIGHT,
   [P('su_tac', 'left', "sitting in the passenger seat in profile facing frame-right, both gloved hands flying across a black rugged laptop on her knees, her eyes on its screen", 'obj:the black rugged laptop on her knees', "her eyes fierce and focused, her lips pressed tight, her brows low", outfit=SU_WAR),
    P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, both hands gripping the control lever as the cab tilts, his head turned slightly to her", 'Su', "his jaw clenched, his eyes hard and sharp, his brows low", outfit=LIN_GUN)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<lin_work> grips the lever as the cab tilts and speaks the first line to <su_tac> in a low, hard, commanding voice, his jaw clenched, his eyes hard and sharp and his brows low, and then <su_tac> types fast and answers with the second line to <lin_work> in a quick, fierce voice, her eyes fierce and focused, her lips pressed tight and her brows low, bullets hammering on the armor outside.",
   "车厢随着车身倾斜，林峰握紧操纵杆，用低沉强硬、带命令的声音对苏清月说出第一句，下颌咬紧、眼神冰冷锐利、眉头压低，然后苏清月飞快地敲着键盘，用又快又凶的声音对林峰答出第二句，眼神凶狠专注、嘴唇紧抿、眉头压低，外面的子弹哒哒地砸在装甲上。",
   SOUND_CABFIGHT, AES_SKYLIGHT, lines=[('lin_work', "干扰它们的信号，火控权交给我！", 0.8, 'Su'), ('su_tac', "干扰成功，它们盲了三秒！", 5.4, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Above them a thick armoured skylight shows the rushing white blizzard and the windshield at the right edge is a rushing white storm.',
   holds='The frame holds exactly two people: Lin and Su, in the cab, nobody else.')

TA('43-03', '03｜驾驶舱：林峰的右手拇指按下操纵杆顶端的红色开火键，低声说三秒，足够了，苏清月抬头看着天窗', 6, CAB_FIGHT,
   [P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, his right thumb pressing down on the red fire button on top of the control lever, his eyes on the skylight", 'obj:the skylight above', "his eyes cold and bright, his jaw tight, his brows low", outfit=LIN_GUN),
    P('su_tac', 'left', "sitting in the passenger seat in profile facing frame-right, her laptop on her knees, her head tilted up toward the skylight", 'obj:the skylight above', "her lips parted, her eyes wide, her brows lifted", outfit=SU_WAR)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<lin_work> presses the red fire button with his thumb and speaks the one line to <su_tac> in a low, cold, satisfied voice, his eyes cold and bright, his jaw tight and his brows low, while <su_tac> looks up at the skylight with the laptop on her knees, her lips parted, her eyes wide and her brows lifted.",
   "林峰用拇指按下红色开火键，用低沉冰冷满意的声音对苏清月说出这一句，眼神冰冷发亮、下颌绷紧、眉头压低，苏清月腿上放着笔电，抬头看着天窗，嘴唇微张、眼睛睁大、眉毛上扬。",
   SOUND_CABFIGHT, AES_SKYLIGHT, lines=[('lin_work', "三秒，足够了。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Above them a thick armoured skylight shows the rushing white blizzard.',
   holds='The frame holds exactly two people: Lin and Su, in the cab, nobody else.')

insert2('43-04', '04｜车顶：一座有三根粗枪管的重机枪塔从车顶升起，枪管前端发着暗橙色的光，朝着暴风雪的天空连发，滚烫的弹壳翻着往下掉', 6, TURRET,
        'Low close shot of the roof turret, the three barrels in the middle third of the frame, nobody in the scene.',
        "A heavy machine-gun turret with three thick barrels stands risen on the roof of the matte-black armoured motorhome and fires upward into the blizzard, its barrel tips glowing dull orange and hot brass casings tumbling past in the white storm. Nothing else moves.",
        "哑光黑色装甲房车车顶上，一座有三根粗枪管的重机枪塔已经升起来，朝着暴风雪的天空连发，枪管前端发着暗橙色的光，滚烫的弹壳在白色的风暴里翻着往下掉。别的什么都不动。",
        SOUND_TURRET, 'The frame holds the roof turret with its firing barrels, and nobody in the scene.',
        push1('the three glowing barrels', '三根发着光的枪管'), AES_TURRET, extra_assets=('armored_rv',))

insert2('43-05', '05｜暴风雪的天空：三团橙色的火球在黑色的天空里接连炸开，把暴风雪从里面照亮，燃烧的残骸拖着黑烟翻着往雪地里掉', 6, SKY_BOOM,
        'Low wide shot looking up at the sky, the three fireballs in the middle third of the frame, nobody visible.',
        "Three orange fireballs bloom one after another in the black blizzard sky and light the storm from within while burning wreckage tumbles out of them trailing black smoke toward the snow. Nothing else moves.",
        "三团橙色的火球在黑色的暴风雪天空里接连炸开，把风暴从里面照亮，燃烧的残骸拖着黑烟翻着往雪地里掉。别的什么都不动。",
        SOUND_BOOM, 'The frame holds the sky with the three fireballs and the falling wreckage, and nobody visible.',
        lowrise('the three fireballs in the sky', '天空里三团火球'), AES_FIREBALL, extra_assets=('combat_drone',))

TA('43-06', '06｜驾驶舱：林峰冷笑着看着前方，装甲车碾过一地燃烧的残骸继续往前，苏清月指着挡风玻璃外说前面就是空军基地的雷达塔', 8, CAB_FIGHT,
   [P('su_tac', 'left', "sitting in the passenger seat in profile facing frame-right, one gloved hand pointing through the windshield, her laptop closed on her knees", 'obj:the far dark radar towers beyond the windshield', "her eyes narrowed and bright, her lips parted, her brows lifted", outfit=SU_WAR),
    P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, both hands on the control lever, his eyes on the road", 'obj:the far dark radar towers beyond the windshield', "one corner of his mouth lifting in a cold smirk, his jaw relaxed, his brows low", outfit=LIN_GUN)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<su_tac> points through the windshield and speaks the one line to <lin_work> in a crisp, tense voice, her eyes narrowed and bright, her lips parted and her brows lifted, while <lin_work> keeps his eyes on the road ahead, one corner of his mouth lifting in a cold smirk, his jaw relaxed and his brows low, the rushing white storm thinning beyond the glass.",
   "苏清月指着挡风玻璃外面，用干脆紧张的声音对林峰说出这一句，眼睛眯起发亮、嘴唇微张、眉毛上扬，林峰目光盯着前面的路，嘴角冷冷地一挑、下颌放松、眉头压低，玻璃外飞快的白色风暴渐渐变薄。",
   SOUND_CABQ, AES_DASH, lines=[('su_tac', "前面就是空军基地的雷达塔。", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Beyond the windshield at the right edge the white storm thins and the dark shapes of far radar towers appear.',
   holds='The frame holds exactly two people: Su and Lin, in the cab, nobody else.')

insert2('43-07', '07｜空军基地：暴风雪的尽头，冰封的停机坪上一座白色的、比装甲房车大一倍的极地堡垒车，车顶一门长长的电磁轨道炮炮口朝着停机坪这一头，远处是黑色的雷达天线', 7, BASE_FAR,
        'Wide shot of the airbase apron, the huge white fortress truck in the middle third of the frame, nobody visible.',
        "At the end of the blizzard the frozen apron of the airbase holds a colossal white fortress truck twice the size of a motorhome with a long railgun on its roof aimed straight down the apron toward the foreground, dark radar dishes standing far behind it. Nothing else moves.",
        "暴风雪的尽头，冰封的空军基地停机坪上停着一辆比房车大一倍的巨型白色堡垒车，车顶一门长长的电磁轨道炮炮口朝着停机坪这一头，更远处是黑色的雷达天线。别的什么都不动。",
        SOUND_BASEFAR, 'The frame holds the airbase apron with the huge white fortress truck, and nobody visible.',
        push1('the railgun on the white fortress truck', '白色堡垒车车顶的轨道炮'), AES_BASEFAR, extra_assets=('fortress_truck', 'armored_rv'))

# ================================================================================================ 第 44 集
b44 = S.episode('剧本第44集｜幽灵的陨落', '堡垒车顶的轨道炮打出一道蓝色的电弧，擦着装甲车飞过，把后面一座旧塔台轰塌；林峰冷冷地说他的炮在冷却，现在冲，把油门踩到底，装甲车像一颗黑色的炮弹冲向堡垒车；车头的钢铲撞进堡垒车撕裂的侧装甲门；林峰提着散弹枪冲进车厢，车厢里满是服务器和屏幕，一个戴着眼镜、极其瘦弱的年轻人瘫在转椅里，举起双手哀求，说别开枪，我知道所有物资的密码，我能让你成为冰河纪的王；林峰低头看着他，说我不想当王，只想在家吃火锅，你，打扰到我了；镜头切到车外，一声沉闷的枪响，空军基地彻底死寂；林峰独自站在车厢深处发着蓝光的圆柱形设备前，说这趟，没白来，那是量子 AI 辅助计算核心。', 44)
b44.prop('ai_core', '量子 AI 辅助计算核心（一米高的圆柱形玻璃设备，里面一波波深蓝色的光往上爬，细细的白色光丝在颤动，底座连着粗电缆）',
         'A tall one-metre glass cylinder computing core with pulses of deep blue light climbing slowly up inside it and tiny threads of white light shivering within, a metal base with thick cables at its bottom. The reference fixes its look.',
         '一台一米高的圆柱形玻璃计算核心，里面一波波深蓝色的光慢慢往上爬，细细的白色光丝在颤动，金属底座连着粗电缆。参考图固定它的外形。',
         'A photorealistic shot of a tall one-metre glass cylinder computing core with pulses of deep blue light climbing slowly up inside it and tiny threads of white light shivering within, a metal base with thick cables, against a plain dark background.')
new_person(b44, 'hacker_k', '黑客 K（二十来岁、极其瘦弱的中国青年，洗得发白的灰色连帽衫，圆框金属眼镜滑到鼻尖，头发乱糟糟）', 'man',
           'A thin pale Chinese man in his late twenties with a frightened face, wearing a washed-out grey hoodie with the hood down, thin round metal glasses sliding down his nose and a tangle of unwashed black hair.',
           '一个二十来岁、瘦弱苍白、一脸惊恐的中国青年，穿着洗得发白的灰色连帽衫，帽子放在脑后，圆框金属眼镜滑到鼻尖，一头乱糟糟没洗的黑头发。',
           'wearing a washed-out grey hoodie with the hood down, thin round metal glasses sliding down his nose and a tangle of unwashed black hair',
           'a frightened, wide-eyed expression', eth='a thin pale Chinese man in his late twenties')
b44.character('HackerK', 'hacker_k', K_EN, K_ZH)
new_scene(b44, 'airbase', '废弃空军基地（一片辽阔的冰封停机坪，远处是黑色的雷达天线，旧塔台，漫天暴风雪）',
          'A vast frozen abandoned airbase apron under a blizzard with dark radar dishes far away and an old control tower.',
          '一片辽阔的冰封废弃机场停机坪，漫天暴风雪，远处是黑色的雷达天线和一座旧塔台。',
          'the frozen apron, the radar dishes and the old control tower')
new_scene(b44, 'server_cabin', '堡垒车的服务器车厢（狭长的装甲车厢，两侧从地板到天花板全是服务器机架，亮着成千上万个小小的蓝色指示灯，一张黑色转椅配着一排暗屏，车厢尽头是一个发蓝光的玻璃圆柱）',
          'A long narrow armoured cabin with floor-to-ceiling server racks lit by thousands of tiny blue lights on both walls, a black swivel chair and a desk of dark screens, and a glowing blue glass cylinder at the far end.',
          '一节狭长的装甲车厢，两侧从地板到天花板全是服务器机架，亮着成千上万个小小的蓝色指示灯，一张黑色转椅配着一排暗屏，车厢尽头是一个发蓝光的玻璃圆柱。',
          'the server racks, the black swivel chair with its dark screens and the glowing blue cylinder')

insert2('44-01', '01｜空军基地：一道分叉的蓝色电弧撕开暴风雪，划过镜头中间，后面一座旧塔台在一团尘土和火花里塌了半截', 6, BASE_TOWER,
        'Wide shot of the airbase apron, the blue arc in the middle third of the frame, nobody visible.',
        "A forked blue electric arc tears across the blizzard in a blinding streak and leaves a white afterglow in the dark air while the old control tower beyond it crumbles halfway in a cloud of dust and sparks. Nothing else moves.",
        "一道分叉的蓝色电弧撕开暴风雪，划出耀眼的一道，在黑暗的空气里留下白色的余光，后面的旧塔台在一团尘土和火花里塌下去半截。别的什么都不动。",
        SOUND_RAIL, 'The frame holds the airbase apron with the blue arc and the crumbling tower, and nobody visible.',
        push1('the crumbling tower and the fading blue arc', '塌下去的塔台和渐渐消失的蓝色电弧'), AES_RAIL, extra_assets=('fortress_truck',))

TA('44-02', '02｜驾驶舱：蓝色电弧的余光在挡风玻璃上闪了一下，林峰把操纵杆往前一推，低声说他的炮在冷却，现在冲，苏清月紧紧抓住扶手', 7, CAB_FIGHT,
   [P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, pushing the control lever hard forward with both hands, his head turned to her", 'Su', "his eyes ablaze, his jaw clenched, his brows low", outfit=LIN_GUN),
    P('su_tac', 'left', "sitting in the passenger seat in profile facing frame-right, both hands clutching the grab handle, her eyes on the road", 'obj:the fortress truck beyond the windshield', "her lips pressed tight, her eyes wide, her brows pulled together", outfit=SU_WAR)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<lin_work> shoves the lever forward and speaks the one line to <su_tac> in a low, fierce, quick voice, his eyes ablaze, his jaw clenched and his brows low, while <su_tac> clutches the grab handle beside him, her lips pressed tight, her eyes wide on the road and her brows pulled together, a last blue flicker fading on the windshield.",
   "林峰把操纵杆用力往前一推，用低沉凶狠又快的声音对苏清月说出这一句，眼睛里烧着火、下颌咬紧、眉头压低，苏清月在他身边紧紧抓着扶手，嘴唇紧抿、眼睛睁大盯着路、眉头拧在一起，挡风玻璃上最后一点蓝光渐渐褪去。",
   SOUND_CABFIGHT, AES_DASH, lines=[('lin_work', "他的炮在冷却，现在冲！", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Beyond the windshield at the right edge the huge white fortress truck looms ahead through the blizzard.',
   holds='The frame holds exactly two people: Lin and Su, in the cab, nobody else.')

insert2('44-03', '03｜空军基地：黑色装甲房车车头的钢铲深深嵌进白色堡垒车撕裂的侧装甲门，白色的装甲板向外翻开，尘土和雪翻成一大团，火花往下落', 6, BASE_RAM,
        'Wide shot of the collision, the buried blade and the torn door in the middle third of the frame, nobody visible.',
        "The heavy steel blade of the matte-black armoured motorhome is buried deep in the torn side armor door of the colossal white fortress truck, buckled white plates splayed out around the breach while a huge cloud of dust and snow billows and fine sparks rain down. Nothing else moves.",
        "哑光黑色装甲房车车头厚重的钢铲深深嵌进白色堡垒车撕裂的侧装甲门里，扭曲的白色装甲板向外翻开，尘土和雪翻成一大团云，细细的火花往下落。别的什么都不动。",
        SOUND_RAM, 'The frame holds the buried blade and the torn armor door, and nobody visible.',
        push1('the buried blade and the torn armor door', '嵌住的铲子和撕裂的装甲门'), AES_RAM, extra_assets=('fortress_truck', 'armored_rv'))

TA('44-04', '04｜堡垒车车厢：林峰端着散弹枪冲进满是服务器的车厢，瘦弱的黑客K瘫在转椅里举起双手，发着抖说别开枪，我知道所有物资的密码，我能让你成为冰河纪的王', 10, SERVER_K,
   [P('hacker_k', 'left', "slumped in the black swivel chair in profile facing frame-right, both hands raised high beside his head, his glasses crooked on his nose", 'Lin', "his eyes wide and wet with terror, his lips trembling, his brows pulled high"),
    P('lin_work', 'right', "standing in the breached doorway in profile facing frame-left, a pump-action shotgun held low across his body in both hands, his eyes on the man in the chair", 'obj:the man in the chair', "his jaw set, his eyes flat and merciless, his brows low", outfit=LIN_GUN)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the server cabin.',
   "<hacker_k> trembles in the chair with both hands raised and speaks the first line to <lin_work> in a thin, shaking, pleading voice and then the second line in a higher, frantic voice, his eyes wide and wet with terror, his lips trembling and his brows pulled high, while <lin_work> stands in the breached doorway with the shotgun held low, his jaw set, his eyes flat and merciless and his brows low.",
   "黑客K瘫在转椅里，两手高高举起，用细细发抖的哀求声音对林峰说出第一句，接着用更高、更慌乱的声音说出第二句，眼睛因恐惧睁大发湿、嘴唇发颤、眉毛高高挑起，林峰站在被撞开的门口，散弹枪低低端着，下颌绷住、眼神冰冷无情、眉头压低。",
   SOUND_SERVER, AES_SERVER, lines=[('hacker_k', "别开枪！我知道所有物资的密码！", 0.8, 'Lin'), ('hacker_k', "我能让你成为冰河纪的王！", 5.6, 'Lin')],
   cam=push('both of them', '两人'), room={'Hacker', 'Lin'}, new=True,
   bg='Behind them floor-to-ceiling server racks with thousands of tiny blue lights line both walls and the glowing blue glass cylinder stands at the far end of the cabin.',
   holds='The frame holds exactly two people: K and Lin, in the server cabin, nobody else.')

TA('44-05', '05｜堡垒车车厢：林峰走到黑客K面前，低头看着他，一字一句地说我不想当王，只想在家吃火锅，你，打扰到我了', 10, SERVER_K,
   [P('lin_work', 'right', "standing over the chair in profile facing frame-left, the shotgun held low in both hands, his head bent to look down at the man in the chair", 'obj:the man in the chair', "his eyes flat and utterly cold, his jaw tight, his brows low", outfit=LIN_GUN),
    P('hacker_k', 'left', "slumped in the black swivel chair in profile facing frame-right, both hands still raised, his head tipped up to look at him", 'Lin', "his eyes wide with terror, his lips trembling, his brows pulled high")],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, in the server cabin.',
   "<lin_work> looks down at <hacker_k> and speaks the first line to <hacker_k> and then the second line to <hacker_k> in a low, flat, terrible voice, his eyes flat and utterly cold, his jaw tight and his brows low, while <hacker_k> looks up at him with both hands raised, his eyes wide with terror, his lips trembling and his brows pulled high.",
   "林峰低头看着黑客K，用低沉平板、让人毛骨悚然的声音对他说出第一句，接着说出第二句，眼神冰冷平板到极点、下颌绷紧、眉头压低，黑客K两手仍举着，抬头看着他，眼睛因恐惧睁大、嘴唇发颤、眉毛高高挑起。",
   SOUND_SERVER, AES_SERVER, lines=[('lin_work', "我不想当王，只想在家吃火锅。", 0.8, 'Hacker'), ('lin_work', "你，打扰到我了。", 5.6, 'Hacker')],
   cam=push('both of them', '两人'), room={'Hacker', 'Lin'}, new=True,
   bg='Behind them floor-to-ceiling server racks with thousands of tiny blue lights line both walls.',
   holds='The frame holds exactly two people: Lin and K, in the server cabin, nobody else.')

insert2('44-06', '06｜车外：空军基地的停机坪上，一声被闷住的枪响之后，一切重归死寂，薄薄的吹雪在白色堡垒车破口旁闪着光，一缕灰烟从破口里升进黑色的天空', 6, BASE_QUIET,
        'Wide shot of the airbase apron, the fortress truck and its breach in the middle third of the frame, nobody visible.',
        "A single muffled gunshot dies away and a dead silence settles over the frozen airbase while thin snow blows across the apron and a thread of grey smoke rises from the breach in the white fortress truck into the dark sky. Nothing else moves.",
        "一声被闷住的枪响渐渐消失，冰封的空军基地重归死寂，薄薄的吹雪在停机坪上掠过，一缕灰色的细烟从白色堡垒车的破口里升进黑色的天空。别的什么都不动。",
        SOUND_QUIET, 'The frame holds the airbase apron with the fortress truck and its breach, and nobody visible.',
        rise('the whole silent airbase and the thread of smoke', '整座寂静的空军基地和那缕细烟'), AES_QUIET, extra_assets=('fortress_truck', 'armored_rv'))

TAV('44-07', '07｜堡垒车车厢：林峰一个人站在发着蓝光的圆柱形计算核心前，枪垂在身旁，嘴角勾起一抹满意的冷笑，低声说这趟，没白来', CORE_MAN,
   [P('lin_work', 'center', "standing alone in front of the tall glowing blue glass cylinder in profile facing frame-right, the shotgun hanging low in one hand, his eyes on the cylinder", 'obj:the glowing blue glass cylinder', "one corner of his mouth lifting in a cold satisfied smirk, his eyes bright with cold light, his brows lifted", outfit=LIN_GUN)],
   'Medium shot, Lin from the head to the knees at frame-left and the glowing cylinder in the middle third of the frame, in the server cabin.',
   "<lin_work> stands alone before the glowing glass cylinder and speaks the one line aloud to himself in a low, quiet, satisfied voice, one corner of his mouth lifting in a cold satisfied smirk, his eyes bright with cold light and his brows lifted, the blue pulses of the core washing over his face. Nobody else is in the frame.",
   "林峰一个人站在发光的玻璃圆柱前，用低沉安静满意的声音对自己说出这一句，嘴角勾起一抹冷冷的满意的笑、眼睛里映着冷冷的光、眉毛上扬，计算核心一波波的蓝光洗过他的脸。画面里没有别人。",
   SOUND_CORE, AES_CORE, [('lin_work', "这趟，没白来。", 0.8, 'Lin')],
   cam=push1('Lin and the glowing core', '林峰和发光的核心'), extra_assets=('ai_core',), room={'Lin'}, new=True,
   bg='Behind him dark server racks line both walls and a slash of grey storm light from the breached door falls across the floor.',
   holds='The frame holds exactly one person: Lin, in the server cabin, nobody else.')

insert2('44-08', '08｜插镜：一米高的玻璃圆柱里，一波一波深蓝色的光有节奏地慢慢往上爬，细细的白色光丝在里面颤动，金属底座和粗电缆泛着冷蓝的光', 6, CORE_CLOSE,
        'Close shot of the glass cylinder, the climbing blue light in the middle third of the frame, nobody in the scene.',
        "Pulses of deep blue light climb slowly up the glass cylinder in steady waves while tiny threads of white light shiver inside it and the metal base and thick cables glint with cold blue edge light. Nothing else moves.",
        "一波一波深蓝色的光有节奏地沿着玻璃圆柱慢慢往上爬，细细的白色光丝在里面颤动，金属底座和粗电缆泛着冷蓝色的轮廓光。别的什么都不动。",
        SOUND_CORE, 'The frame holds the glowing glass cylinder, and nobody in the scene.',
        pull('the climbing blue light in the glass', '玻璃里往上爬的蓝光', 'the whole glowing cylinder and its cables', '整个发光的圆柱和它的线缆'), AES_CORE, extra_assets=('ai_core',))

doc = S.finish()
