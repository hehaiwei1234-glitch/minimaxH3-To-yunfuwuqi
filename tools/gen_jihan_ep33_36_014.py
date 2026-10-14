#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 33–36 集，追加稿 014（2026-10-14）。以 013 的 JSON 为底（style／素材／角色逐字复制），必须等 013 在插件里全部跑完再追加。
hh 2026-10-14 18:19：“再更新出来 16 集，我挂通宵，一批一批来，一次 4 集。”本批＝第二批（33–36）。写法＝013 同一套（共用定义在 _jihan_base6.py）。

偏离大纲（交稿时已告诉 hh）：
  · 第 33 集：车队只拍两个远景（缓缓开进冰谷、被雪盖住后的白谷），不拍人群；队长一个人站在头车天窗里（一个任务，没有司机入画）；“超声波次声炮”看不见，只拍林峰按下红色按钮和悬崖雪面裂开；
    雪崩只拍一个 7 秒大远景；车队被吞没只拍结果（冰谷被填平）；“气象雷达”改成苏清月看着驾驶舱仪表上的雷达，只说台词；
  · 第 34 集：“履带摩擦出火花”不拍；“方向盘”改成操纵杆（驾驶舱里本来就是杆）；水瓶掉在地毯上只留声音；“被困死会不会后悔”压成一句“要是我们被困死，你会后悔吗？”；亲密只拍到她抱住他的脖子；
  · 第 35 集：“翻身压住”改成他俯身吻她、慢慢放倒（不拍翻身）；不露骨：窗玻璃起雾、阳光穿过冰洞、两人裹着毯子睡着（都穿着衣服）；回家后的早餐加一个回家安全感的任务（没有新作物，下一批会补养成）；“咖啡杯摔碎”只拍碎片和洒出的咖啡（结果）；
    “深层生物热能探测仪”只拍一块宽屏上一个大红橙色热源（不写字）；
  · 第 36 集：巨熊本批不出镜（只有探测仪屏幕上的轮廓、墙上的凹痕和撞击声）；“钛合金墙拍变形”只拍凹痕结果；废料缓冲舱只拍闸门外观（陷阱下一批才用）；苏清月手里是细长的战术匕首。
H3 方面的风险（交稿时单列，不算我的错）：
  · 33-01 车队行驶；33-02 队长一个人在车顶天窗说话；33-03 悬崖上压着的雪檐；33-06 雪面裂开；33-07 雪崩（大自然的大场面，没有任何数据）；33-08 队长抬头惊呼；33-09 填平的冰谷；
  · 34-01 房车冲进冰洞（运动车辆＋暴风雪）；34-02 驾驶舱外一片白；34-06 脚下一滑跌进怀里（快动作）；34-07、34-08 两人贴近、抱住脖子；
  · 35-02 亲吻（两张脸可能融合）；35-03 窗玻璃起雾；35-05 阳光穿过冰洞折射彩虹；35-06 两人裹着毯子睡着（闭眼）；35-07 房车驶出冰洞；35-10 咖啡杯碎片；
  · 36-01 叶子震颤、尘土落下；36-02 宽屏上的红橙色热源；36-04 墙上的凹痕；开场图约一成不按文字画；“同一处”场景用参照图。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
from _jihan_base6 import *
from _scene import smooth_task

import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407)   # hh 2026-10-14 16:20：台词顺滑写法＋全批固定视频种子
OUT = '合并稿/014_第33-36集_雪崩冰洞心跳吻里的末日巨熊_制作稿_追加'
S = Session('合并稿/013_第29-32集_草莓酱电磁处决黑色巨兽冰原狂飙_制作稿_追加.json', OUT, 46000)
B6.S = S

# ---------------------------------------------------------------------------------------------- 光和空气（本批新增）
AES_VALLEY = ("The headlight beams of the convoy cut long white shafts through the blowing snow while the black canyon walls rise into a thin strip of aurora-green sky, and glittering ice crystals drift through every beam.",
              "车队的车灯在飘飞的雪里切出一道道长长的白色光柱，黑色的冰谷峭壁升进一线绿色极光的天空，闪光的冰晶在每一道光束里飘。")
AES_CLIFF = ("A faint green aurora glows over the cliff edge, powdery snow streams off the overhanging slab in the wind and the dark silhouette of the motorhome is rimmed with a thin line of cold blue light.",
             "淡淡的绿色极光在悬崖边缘上空发亮，粉雪被风从压在头顶的雪檐上吹散，房车黑色的剪影被一线冷冷的蓝光勾出轮廓。")
AES_AVAL = ("A colossal cloud of glittering white powder boils ahead of the thundering wall of snow, the green aurora light glints on every ice block and the convoy headlights are swallowed one by one in the white.",
            "巨大的、闪着光的白色粉雪云翻滚在轰鸣的雪墙前面，绿色极光的光在每一块冰块上闪烁，车队的车灯一盏盏被白色吞没。")
AES_HUSH = ("A deep blue hush lies over the smooth fresh snow, a thin haze of powder drifts and glitters in the green aurora light and the cliffs on either side hold a thin rim of cold light.",
            "一片深蓝色的寂静盖在平滑的新雪上，一层薄薄的粉雪雾飘着，在绿色极光的光里闪烁，两侧悬崖的边缘镶着一线冷冷的光。")
AES_BTN = ("A ring of red light pulses around the red button and washes over the dark console in slow waves, with the cool green glow of the radar screen behind it.",
           "一圈红光围着红色按钮脉动，慢慢地一波一波洗过黑色的控制台，背后是雷达屏幕冷冷的绿光。")
AES_STORM = ("A roaring blank white blizzard fills the windshield and throws a cold white glow across their faces while the warm amber dashboard light rims them in a teal-and-orange contrast.",
             "呼啸的一片空白的暴风雪占满挡风玻璃，把冷冷的白光洒在两人脸上，温暖的琥珀色仪表灯光给他们描上一圈青橙对比的轮廓。")
AES_CAVE = ("Warm amber light spills from the motorhome windows across glittering blue ice walls, long icicles catch the glow like crystal and fine ice dust drifts in the beams.",
            "温暖的琥珀色灯光从房车的窗户里洒到闪闪发光的蓝色冰壁上，长长的冰柱像水晶一样接住光，细细的冰尘在光束里飘。")
AES_LOUNGE = ("Warm amber light pools on the leather sofa and the cream wool rug while the frosted windows glow cold blue, a gentle teal-and-orange contrast, with a few tiny dust motes drifting through the glow.",
              "温暖的琥珀色灯光洒在皮沙发和奶白色羊毛地毯上，结霜的窗户透着冷冷的蓝光，形成柔和的青橙对比，几粒细小的尘埃在光里飘。")
AES_FOG = ("A soft white veil of warm breath clouds the thick glass, the blizzard glows faintly blue beyond it and amber lamp light blurs into soft golden halos on the fogged pane.",
           "一层柔软的白色暖气雾蒙在厚厚的玻璃上，玻璃外暴风雪发着淡淡的蓝光，琥珀色的灯光在起雾的玻璃上晕成柔和的金色光晕。")
AES_RAINBOW = ("Shafts of pale morning sun slant through the cracks of the ice and break into soft rainbow beams across the blue walls, with glittering ice dust floating through the colored light.",
               "淡淡的晨光斜斜地穿过冰缝，在蓝色的冰壁上折射成柔和的七彩光束，闪光的冰尘在彩色的光里漂浮。")
AES_DAWN = ("Pale rose-gold dawn light spreads over the calm fresh snow, long blue shadows lie behind every ridge and fine snow crystals glitter in the still air.",
            "淡淡的玫瑰金色晨光铺在平静的新雪上，每一道雪脊后面拖着长长的蓝色影子，细小的雪晶在静止的空气里闪烁。")
AES_RED = ("A slow red warning pulse washes the room and rim-lights the edges of everything, with a deep darkness falling off at the edges of the frame.",
           "缓慢的红色警报光脉动着漫过房间，给所有东西的边缘描上红边，画面四周落入深深的暗。")
AES_HEAT = ("A glowing red-orange heat bloom burns in the middle of the dark wide screen and its warm light flares across the cool teal edge of the console in slow pulses.",
            "一团发光的红橙色热源在黑色宽屏的中间燃着，它温暖的光一阵阵地照到控制台冷冷的青色边缘上。")
AES_FARM = ("Soft pink-violet light from the grow lamps washes over the green leaves and rim-lights every droplet of water, fine dust drifts in the glow and the concrete beyond falls into deep shadow.",
            "粉紫色的植物灯光柔和地洗过绿叶，给每一滴水珠描上轮廓光，细细的尘埃在光里飘，远处的混凝土落入深深的阴影。")
AES_GATE = ("Cold white light falls across the yellow-black warning stripes of the huge gate and the frosted glass window glows pale blue while the warm pink-violet grow lamps glow behind the camera.",
            "冷白色的光落在巨大闸门黄黑相间的警示条纹上，结霜的玻璃窗透着淡蓝色的光，镜头背后是粉紫色植物灯温暖的光。")

# ---------------------------------------------------------------------------------------------- 新外貌／声音
look('captain', 'Captain', "in a white winter-camouflage military parka with a black headset on his head and the fur-trimmed hood pushed back, a tablet in one gloved hand", 'hard', 'his', eth='a Chinese military officer in his forties')
CAP_EN = 'A rough, loud, hurried adult male voice, clipped and commanding, speaking clear Mandarin Chinese.' + VT_EN
CAP_ZH = '粗犷、响亮、急促的成年男声，短促而带命令的口气，普通话清楚。' + VT_ZH
LOUNGE_L = "in a fitted black long-sleeve thermal top and black trousers, her long black hair in a high ponytail"
LIN_OPEN = "in a charcoal henley with the collar pulled open and the utility vest off"

# ---------------------------------------------------------------------------------------------- 场景
CAB_BTN = Scene('rv_cab', CAB.end, CAB.layout + " On the console between the seats a big red push-button stands under an open clear flip-up cover.")
CAB_STORM = Scene('rv_cab', " Warm amber dashboard glow fills the compact armoured cab while the windshield is a roaring blank white blizzard.",
                  " Fixed stage layout: a cutaway side view of the cab; two leather bucket seats stand side by side across the middle of the frame, both facing frame-right toward the wide armoured windshield, the passenger seat at frame-left and the driver's seat at frame-center-right with a short steel control lever beside it; between them a console holds a steaming paper cup; a small round radar screen is set in the dashboard at frame-right; the windshield at the right edge is a roaring blank white blizzard.")
BTN_CLOSE = Scene('rv_cab', CAB.end,
                  " Fixed stage layout: a big red push-button sunk flush in a black console fills the middle of the frame, its open clear flip-up cover beside it and a ring of red light pulsing around it; the dark dashboard and the green radar screen glow behind.")
VALLEY = Scene('ice_valley', " A black night under a thin strip of faint green aurora; snow blows through the headlight beams of a convoy.",
               " Fixed stage layout: a narrow frozen canyon with sheer snow-laden cliffs a hundred metres high on both sides runs down the middle of the frame; a convoy of five heavy white-painted military off-road trucks and a long missile launcher truck crawls along the canyon floor through deep snow with their headlights blazing; a thin strip of aurora-green sky lies above.")
HATCH = Scene('ice_valley', VALLEY.end,
              " Fixed stage layout: the roof of a heavy white-painted military truck in the foreground with an open roof hatch at the middle of the frame; snow-laden canyon cliffs rise behind it and more white trucks with blazing headlights crawl along the canyon floor in the distance.")
CLIFF = Scene('cliff_top', " A black night under a faint green aurora; wind-blown snow glitters along the cliff edge.",
              " Fixed stage layout: the very edge of a high snow-laden cliff fills the middle of the frame with a thick overhanging slab of snow hanging over the drop; the matte-black armoured tracked motorhome stands motionless at frame-left on the cliff top with its lights dark; far below in the dark canyon a line of tiny headlights crawls.")
CLIFF_CRACK = Scene('cliff_top', CLIFF.end,
                    " Fixed stage layout: seen from below, the steep snow-laden cliff face fills the middle of the frame; a thin dark crack runs across the snow slope under the overhanging slab and the slab's edge has begun to slip with a sheet of powder streaming off it; a faint green aurora hangs in the strip of sky above.")
AVAL = Scene('ice_valley', VALLEY.end,
             " Fixed stage layout: a vast white wall of snow and ice blocks thunders down the cliffs on both sides into the narrow canyon, a huge billowing cloud of white powder rolling ahead of it, and at the bottom of the frame the small convoy of white trucks with blazing headlights is just about to be swallowed.")
VALLEY_AFTER = Scene('ice_valley', " A deep hush under the faint green aurora; a thin haze of white powder drifts over the snow.",
                     " Fixed stage layout: the narrow canyon lies completely filled with smooth fresh snow from wall to wall, a faint haze of powder drifting across it; the sheer cliffs rise on both sides; not a single vehicle is visible.")
CAVE_MOUTH = Scene('ice_cave', " A roaring white wall of blizzard fills the black sky behind the cave mouth and the headlights of the motorhome blaze through it.",
                   " Fixed stage layout: a huge natural ice cave mouth, a dark arch glittering with blue ice, fills the middle of the frame; the matte-black armoured tracked motorhome is plunging into it from frame-right with its headlights blazing; behind it a roaring white wall of blizzard sweeps across the snowfield.")
CAVE_IN = Scene('ice_cave', " Deep blue darkness inside a glittering ice cave with warm amber light spilling from the parked motorhome.",
                " Fixed stage layout: the inside of a vast natural ice cave with walls and ceiling of glittering blue ice and long icicles hanging; the matte-black armoured tracked motorhome stands parked in the middle of the frame with warm amber light glowing from its windows; at the far end the cave mouth is a pale white arch veiled by blowing snow.")
CAVE_RAY = Scene('ice_cave', " Soft pale morning light slants into the glittering ice cave through cracks in the ice.",
                 " Fixed stage layout: a wall of glittering blue ice fills the middle of the frame with long icicles hanging at the top; slanting shafts of morning sun come through two cracks in the ice and break into soft rainbow beams across the wall; the dark flank of the parked motorhome is at frame-left.")
LOUNGE = Scene('rv_lounge', " Warm amber light fills the cozy rear lounge of the armoured motorhome while the frosted windows glow cold blue with the blizzard.",
               " Fixed stage layout: the rear lounge of the motorhome; a deep brown leather sofa runs along the back wall in the middle of the frame with a thick cream wool rug on the floor in front of it and a grey wool blanket folded over one arm; two small thick-glass windows are set into the wall above the sofa at frame-right, white with blowing snow outside; a small steel cabinet stands at frame-left.")
LOUNGE_WIN = Scene('rv_lounge', LOUNGE.end,
                   " Fixed stage layout: a small thick-glass window fills the middle of the frame, its pane white with a soft veil of fog and frost ferns at the edges and a faint blue blizzard glow beyond; the brown leather sofa and a corner of the cream wool rug are at the bottom of the frame.")
LOUNGE_MORN = Scene('rv_lounge', " Soft rainbow morning light slants into the quiet rear lounge of the armoured motorhome.",
                    LOUNGE.layout)
DAWN = Scene('snow_field', " A calm pale rose-gold dawn over the snowfield after the storm.",
             " Fixed stage layout: a vast calm snowfield of deep fresh snow fills the frame; a great ice cave arch stands at frame-left with the matte-black armoured tracked motorhome rolling slowly out of it on wide tracks; a faint pink dawn glow lies along the horizon.")
EDEN_WALL = Scene('eden', EDEN.end,
                  " Fixed stage layout: a thick grey alloy wall at the end of the farm level fills the middle of the frame with a huge rounded dent bulging inward across it, a fine veil of dust sifting down and the torn edge of insulation showing along a seam; pink-violet grow lamps glow above.")
EDEN_SHAKE = Scene('eden', EDEN.end,
                   " Fixed stage layout: long tiers of white hydroponic channels full of young lettuce and tomato seedlings fill the middle of the frame under rows of hanging pink-violet grow lamps; the water in the channels is rippling; a fine veil of dust sifts down from the concrete ceiling; a warm incubator box with a glass window and a red heat lamp stands at frame-right.")
EDEN_GATE = Scene('eden', EDEN.end,
                  " Fixed stage layout: at the far end of the farm level a huge grey alloy sliding gate with yellow-black warning stripes and a small armoured-glass window stands closed in the middle of the frame; long tiers of young lettuce and tomato seedlings under pink-violet grow lamps line both sides in the foreground; a steel staircase rises at frame-left.")
GATE_CLOSE = Scene('eden', EDEN.end,
                   " Fixed stage layout: the huge grey alloy gate with its yellow-black warning stripes fills the middle of the frame, a small thick armoured-glass window set in it frosted with pale blue ice on the outer side; a steel control panel with a red lever stands at frame-right.")
EDEN_STAIR = Scene('eden', EDEN.end,
                   " Fixed stage layout: a steel staircase rises at frame-left down into the farm level; long tiers of white hydroponic channels full of young lettuce and tomato seedlings fill the middle of the frame under rows of hanging pink-violet grow lamps; the concrete walls fill the background.")

# ---------------------------------------------------------------------------------------------- 声音
SOUND_CONVOY = breathy('The grinding crawl of heavy tracked and wheeled engines through deep snow and a long low howl of wind.', '重型履带和轮式发动机碾过深雪缓慢的轰鸣和风长长的低啸。')
SOUND_CAP = voiced('Heavy engines grinding through snow, a long low howl of wind and the squeak of a radio headset.', '重型发动机碾过雪地的轰鸣、风长长的低啸和对讲耳机细细的吱声。')
SOUND_CLIFF = breathy('A long low howl of wind over the cliff top and a faint tick of shifting snow.', '风掠过悬崖顶长长的低啸和雪层缓缓移动细细的嘀嗒声。')
SOUND_BTN = breathy('A deep low electronic hum swelling under the dashboard, a soft click and a thin howl of wind.', '仪表盘下面渐渐变强的深沉电子嗡声、一声轻轻的按键声和风细细的呼啸。')
SOUND_CRACKSNOW = breathy('A long dry crack running through packed snow and a rising hiss of powder.', '一声长长的干脆裂响从压实的雪里传过去，和越来越响的粉雪嘶嘶声。')
SOUND_AVAL = breathy('A thundering roar like a thousand galloping horses, the crash of tumbling ice and the hiss of rolling powder.', '像千万匹马奔腾一样的雷鸣、冰块翻滚的碰撞声和翻腾的粉雪嘶嘶声。')
SOUND_AVAL_V = voiced('A thundering roar of tumbling snow and ice and a rising howl of wind.', '雪和冰翻滚的雷鸣和越来越响的风啸。')
SOUND_HUSH = breathy('A deep hush, a thin howl of wind and the faint hiss of settling powder.', '深深的寂静、风细细的呼啸和落下的粉雪轻轻的嘶嘶声。')
SOUND_STORM_V = voiced('The roar of a blizzard against armored glass, the low hum of the engine and a rising shriek of wind.', '暴风雪拍在装甲玻璃上的轰鸣、发动机的低鸣和越来越尖的风啸。')
SOUND_STORM = breathy('The roar of a blizzard against armored glass, the strain of tracks on ice and a rising shriek of wind.', '暴风雪拍在装甲玻璃上的轰鸣、履带在冰上吃力的声音和越来越尖的风啸。')
SOUND_PLUNGE = breathy('The thundering of heavy tracks, a deep echo as the engine enters a cave and the roar of the blizzard behind.', '重型履带的轰鸣、发动机驶进山洞时深沉的回响和身后暴风雪的怒吼。')
SOUND_CAVE = breathy('A deep echoing hush, the soft tick of cooling metal and the muffled roar of the storm outside.', '深沉带回响的寂静、金属冷却时轻轻的嘀嗒声和洞外被闷住的暴风雪怒吼。')
SOUND_LOUNGE = breathy('The muffled howl of the blizzard against thick glass, the soft hiss of warm air and ragged breath.', '暴风雪拍在厚玻璃上被闷住的呼啸、暖风轻轻的嘶嘶声和粗重的呼吸。')
SOUND_LOUNGE_V = voiced('The muffled howl of the blizzard against thick glass and the soft hiss of warm air.', '暴风雪拍在厚玻璃上被闷住的呼啸和暖风轻轻的嘶嘶声。')
SOUND_SLIP = breathy('The soft slip of a boot on a rug, a startled gasp and the muffled howl of the blizzard.', '靴子在地毯上轻轻一滑的声音、一声受惊的抽气和暴风雪被闷住的呼啸。')
SOUND_KISS = breathy('The muffled howl of the blizzard against thick glass, the soft hiss of warm air and quiet breath.', '暴风雪拍在厚玻璃上被闷住的呼啸、暖风轻轻的嘶嘶声和安静的呼吸。')
SOUND_SLEEP = breathy('A deep calm hush, the faint creak of cooling metal and the slow quiet breath of two sleepers.', '深沉平静的寂静、金属冷却时细细的吱呀声和两个人睡着时缓慢安静的呼吸。')
SOUND_DAWN = breathy('The low rumble of a diesel engine rolling out of a cave and the crunch of fresh snow beneath wide tracks.', '柴油发动机从山洞里缓缓驶出的低鸣和宽履带下新雪的嘎吱声。')
SOUND_HOME = voiced('The soft clink of a mug, the gentle hum of the stove and the faint warm hum of the air system.', '杯子轻轻的碰响、炉子温和的嗡鸣和空气系统温暖的嗡声。')
SOUND_HEAT = breathy('A slow deep electronic pulse, a faint dull scraping thud far away and a thin hum from the console.', '缓慢深沉的电子脉冲声、远处一声声钝钝的刮擦撞击声和控制台细细的嗡鸣。')
SOUND_ALARM = voiced('A sharp repeating electronic alarm beep and a dull heavy thud somewhere beyond the wall.', '尖锐反复的电子警报声和墙外某处一声沉闷厚重的撞击。')
SOUND_THUD = breathy('A deep dull heavy thud through concrete, the soft rattle of water in channels and a faint tick of falling dust.', '一声穿过混凝土的深沉闷响、水槽里水轻轻的晃动声和灰尘落下细细的嘀嗒声。')
SOUND_FARM_V = voiced('A deep dull heavy thud through concrete and the soft rattle of water in the channels.', '一声穿过混凝土的深沉闷响和水槽里水轻轻的晃动声。')
SOUND_STAIR = breathy('Quick footsteps on a steel staircase and a deep dull thud through concrete.', '钢楼梯上急促的脚步声和一声穿过混凝土的深沉闷响。')
SOUND_WALLDENT = breathy('A heavy dull thud, the creak of strained alloy and the faint tick of falling dust.', '一声沉重的闷响、被压弯的合金吱呀的声音和灰尘落下细细的嘀嗒声。')
SOUND_GATE = breathy('The thin howl of wind beyond a sealed gate and the faint tick of frost forming on metal.', '紧闭闸门外风细细的呼啸和金属上结霜细细的嘀嗒声。')

# ================================================================================================ 第 33 集
b33 = S.episode('剧本第33集｜雪崩绞肉机', '冰谷下方，五辆重型军用越野车护着一辆导弹发射车艰难地碾过积雪，队长站在车顶天窗里看着导航，说快到了，炸开地下室，立首功；冰谷上方的悬崖边，林峰的黑色装甲房车像幽灵一样一动不动，悬崖上压着成百上千吨摇摇欲坠的积雪；驾驶舱里，林峰说在大自然面前，你们的导弹只是玩具，按下红色按钮；一道看不见的声波打在悬崖的雪层上，雪面裂开，雪墙像白色海啸一样从两侧悬崖压下来；队长抬头惊呼雪崩快倒车；冰谷被彻底填平，只剩风声；就在林峰准备调头回家时，苏清月看着雷达脸色大变：是超级暴风雪，风力十四级，气温正在降向零下一百度，画面拉黑。', 33)
new_person(b33, 'captain', '车队队长（四十来岁的中国军官，白色冬季迷彩作战服，头戴黑色对讲耳机，毛边风帽拉在脑后，手里拿着平板）', 'man',
           'A Chinese military officer in his forties with a hard weathered face, wearing a white winter-camouflage military parka with a black radio headset on his head and the fur-trimmed hood pushed back, a tablet in one gloved hand.',
           '一个四十来岁、面庞粗硬饱经风霜的中国军官，穿着白色冬季迷彩作战服，头戴黑色对讲耳机，毛边风帽拉在脑后，一只戴手套的手里拿着一块平板。',
           'wearing a white winter-camouflage military parka with a black radio headset on his head and the fur-trimmed hood pushed back, a tablet in one gloved hand',
           'a hard, eager expression', eth='a Chinese military officer in his forties')
b33.character('Captain', 'captain', CAP_EN, CAP_ZH)
b33.prop('convoy', '军用车队（五辆白色涂装的重型军用越野车和一辆长长的导弹发射车，亮着车灯）',
         'A convoy of five heavy white-painted military off-road trucks and one long missile launcher truck in a line on a snowy road with their headlights blazing. The reference fixes their look.',
         '一队军用车：五辆白色涂装的重型军用越野车和一辆长长的导弹发射车排成一行，开在雪路上，车灯亮着。参考图固定它们的外形。',
         'A photorealistic shot of a convoy of five heavy white-painted military off-road trucks and one long missile launcher truck in a line on a snowy road at night with their headlights blazing, seen from a high three-quarter angle, against a plain dark background.')
new_scene(b33, 'ice_valley', '一线天冰谷（两侧上百米高的悬崖、谷底的积雪、窄窄一线绿色极光的天空）',
          'A narrow frozen canyon with sheer snow-laden cliffs a hundred metres high on both sides, deep snow on the canyon floor and a thin strip of faint green aurora sky above.',
          '一条狭窄的冰封峡谷，两侧是上百米高、挂满积雪的悬崖，谷底是深深的积雪，头顶是窄窄一线淡淡绿色极光的天空。',
          'the sheer snow-laden cliffs, the deep snow on the canyon floor and the strip of aurora sky')
new_scene(b33, 'cliff_top', '冰谷上方的悬崖顶（悬崖边压着厚厚的雪檐，远处谷底有一线小小的车灯）',
          'The very edge of a high snow-laden cliff with a thick overhanging slab of snow hanging over the drop, the dark canyon far below with a line of tiny headlights and a faint green aurora above.',
          '一座挂满积雪的高高悬崖的边缘，压着一块厚厚的悬空雪檐，下面是黑漆漆的深谷，谷底有一线小小的车灯，上空是淡淡的绿色极光。',
          'the cliff edge, the overhanging slab of snow and the dark canyon below')

insert2('33-01', '01｜冰谷：五辆白色的重型越野车护着一辆导弹发射车，车灯劈开风雪，在窄窄的冰谷里缓缓向前碾', 6, VALLEY,
        'Wide high shot of the canyon, the convoy in the middle third of the frame, nobody visible.',
        "The convoy of five white military trucks and a long missile launcher truck crawls slowly forward along the canyon floor through deep snow, their headlights cutting long shafts through the blowing snow under the sheer dark cliffs. Nothing else moves.",
        "五辆白色的军用越野车护着一辆长长的导弹发射车，在谷底的深雪里缓缓向前碾，车灯在飘飞的雪里切出长长的光柱，两侧是黑沉沉陡峭的悬崖。别的什么都不动。",
        SOUND_CONVOY, 'The frame holds the narrow canyon with the convoy of white trucks and nobody visible.',
        descend('the convoy crawling along the canyon floor', '谷底缓缓前进的车队'), AES_VALLEY, extra_assets=('convoy',))

TAV('33-02', '02｜冰谷：队长一个人站在头车的车顶天窗里，举着平板看导航，咧着嘴说快到了，炸开地下室，立首功', HATCH,
    [P('captain', 'center', "standing alone in the open roof hatch of the lead white truck from the chest up, a tablet held up in one gloved hand, his headset on", 'obj:the tablet in his hand', "his lips stretched in a greedy eager grin, his eyes bright, his brows lifted")],
    'Medium shot, the officer from the head to the chest, in the middle third of the frame, in the roof hatch.',
    "<captain> looks at the tablet and speaks the one line aloud to himself in a rough, eager voice, his lips stretched in a greedy eager grin, his eyes bright and his brows lifted, while snow blows past and the headlights of the convoy glow behind him. Nobody else is in the frame.",
    "队长看着平板，用粗犷急切的声音对自己大声说出这一句，嘴咧着贪婪急切的笑、眼睛发亮、眉毛上扬，雪从旁边吹过，身后车队的车灯发着光。画面里没有别人。",
    SOUND_CAP, AES_VALLEY, lines=[('captain', "快到了！炸开地下室，立首功！", 0.8, 'Captain')],
    cam=push1('the officer', '队长'), extra_assets=('convoy',), room={'Captain'}, new=True,
    bg='Behind him the snow-laden canyon cliffs rise and more white trucks crawl with blazing headlights in the distance.',
    holds='The frame holds exactly one person: the officer, in the roof hatch, nobody else.')

insert2('33-03', '03｜悬崖顶：林峰的黑色装甲房车像幽灵一样一动不动地停在悬崖边，头顶压着一大片摇摇欲坠的雪檐，谷底有一线小小的车灯', 6, CLIFF,
        'Wide shot of the cliff top, the cliff edge and the overhanging slab in the middle third of the frame, nobody visible.',
        "The matte-black armoured motorhome stands motionless on the cliff top like a ghost while a thick overhanging slab of snow hangs over the drop beside it, powder streaming faintly off its edge, and far below in the dark canyon a line of tiny headlights crawls. Nothing else moves.",
        "哑光黑色的装甲房车像幽灵一样一动不动地停在悬崖顶上，旁边一块厚厚的悬空雪檐压在深谷上，边缘有粉雪轻轻飘落，远远的谷底一线小小的车灯在爬。别的什么都不动。",
        SOUND_CLIFF, 'The frame holds the cliff top with the dark motorhome and the overhanging slab, and nobody visible.',
        pull('the dark motorhome', '黑色房车', 'the cliff edge, the overhanging slab of snow and the tiny headlights far below', '悬崖边缘、压着的雪檐和远处谷底小小的车灯'),
        AES_CLIFF, extra_assets=('armored_rv',))

TA('33-04', '04｜驾驶舱：林峰盯着前方，低声说在大自然面前，导弹只是玩具，苏清月屏住呼吸，他把拇指按在红色按钮上', 9, CAB_BTN,
   [P('su_tacfit', 'left', "sitting in the passenger seat in profile facing frame-right, one hand gripping the grab handle, her eyes on the radar screen", 'obj:the small radar screen in the dashboard', "her lips pressed tight, her eyes wide, her brows pulled together"),
    P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, his right thumb resting over the big red push-button on the console", 'obj:the big red push-button under the open cover', "his eyes cold and narrowed, his jaw set, his brows low", outfit="in a charcoal henley under a dark olive utility vest")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<lin_work> speaks the one line aloud to <su_tacfit> in a low, cold, deadly calm voice, his eyes cold and narrowed, his jaw set and his brows low, and then presses his right thumb down firmly on the red button. <su_tacfit> holds her breath beside him, her lips pressed tight, her eyes wide and her brows pulled together.",
   "林峰用低沉冰冷、杀气腾腾却平静的声音对苏清月说出这一句，眼睛冰冷眯起、下颌绷住、眉头压低，然后右手拇指稳稳地按下红色按钮。苏清月在他身边屏住呼吸，嘴唇紧抿、眼睛睁大、眉头拧在一起。",
   SOUND_BTN, AES_BTN, lines=[('lin_work', "大自然面前，导弹只是玩具。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Between them on the console a big red push-button stands under an open clear flip-up cover and the windshield at the right edge shows the dark cliff edge and the green aurora.',
   holds='The frame holds exactly two people: Su and Lin, sitting side by side in the cab, nobody else.')

insert2('33-05', '05｜插镜：控制台上，红色按钮已经按到底，一圈红光一下一下脉动，把黑色的控制台洗成红色', 5, BTN_CLOSE,
        'Close shot of the red push-button on the console in the middle third of the frame, nobody in the scene.',
        "The red push-button sits pressed flush in the black console with its clear flip-up cover open beside it and a ring of red light pulses slowly around it, washing the console in slow red waves while the green radar glow flickers behind. Nothing else moves.",
        "红色按钮已经被按到底，嵌在黑色的控制台里，旁边是掀开的透明翻盖，一圈红光围着它慢慢脉动，把控制台一波一波洗成红色，背后雷达的绿光轻轻闪烁。别的什么都不动。",
        SOUND_BTN, 'The frame holds the red push-button, its open cover and the black console, and nobody in the scene.',
        push1('the pulsing red button', '脉动着红光的按钮'), AES_BTN)

insert2('33-06', '06｜悬崖：悬崖雪面上，一道细长的黑色裂缝横着划开雪坡，裂缝上方的雪檐开始下滑，边缘淌下一片粉雪', 5, CLIFF_CRACK,
        'Low shot looking up at the cliff face, the crack and the slipping slab in the middle third of the frame, nobody in the scene.',
        "A thin dark crack runs across the steep snow slope under the overhanging slab and the slab's edge begins to slip, a sheet of powder streaming down the cliff face under the faint green aurora. Nothing else moves.",
        "陡峭的雪坡上，一道细长的黑色裂缝横着划过压着的雪檐下面，雪檐的边缘开始下滑，一片粉雪沿着悬崖面淌下来，头顶是淡淡的绿色极光。别的什么都不动。",
        SOUND_CRACKSNOW, 'The frame holds the snow-laden cliff face with the crack and the slipping slab, and nobody in the scene.',
        lowrise('the crack and the slipping slab', '裂缝和下滑的雪檐'), AES_CLIFF)

insert2('33-07', '07｜冰谷：一整面白色的雪墙夹着巨大的冰块，从两侧悬崖上轰鸣着压下来，白色的粉雪云在前面翻滚，谷底的车灯一盏盏被吞掉', 7, AVAL,
        'Wide shot of the canyon, the roaring wall of snow in the middle third of the frame, nobody visible.',
        "A colossal white wall of snow and tumbling ice blocks thunders down the cliffs into the narrow canyon, a huge billowing cloud of glittering powder rolling ahead of it, and the headlights of the small convoy at the bottom of the frame are swallowed one by one in the white. Nothing else moves.",
        "一面巨大的白色雪墙夹着翻滚的冰块，轰鸣着从悬崖压进窄窄的峡谷，前面翻腾着一大片闪光的粉雪云，画面下方小小的车队的车灯一盏盏被白色吞掉。别的什么都不动。",
        SOUND_AVAL, 'The frame holds the canyon with the roaring wall of snow and the small convoy, and nobody visible.',
        push1('the roaring white wall of snow and ice', '轰鸣的白色雪墙'), AES_AVAL, extra_assets=('convoy',))

TAV('33-08', '08｜冰谷：队长猛地抬头，瞳孔缩紧，对着头顶压下来的白色惊恐地大喊雪崩，快倒车', HATCH,
    [P('captain', 'center', "standing in the open roof hatch of the lead white truck from the chest up, his tablet dropped to his side, his head thrown back and his face turned up toward the white above him", 'obj:the wall of white snow crashing down above him', "his eyes wide with shrunken pupils, his mouth open in a shout, his face drained pale, his brows pulled high")],
    'Medium shot, the officer from the head to the chest, in the middle third of the frame, in the roof hatch.',
    "<captain> stares up at the white wall crashing down toward him and speaks the one line aloud to himself in a panicked, cracking shout, his eyes wide with shrunken pupils, his mouth open, his face drained pale and his brows pulled high, while a roaring cloud of white powder rolls in behind him. Nobody else is in the frame.",
    "队长瞪着朝他压下来的白色雪墙，用惊恐、嘶哑的声音对自己大声喊出这一句，眼睛睁大、瞳孔缩紧、嘴张着、脸色发白、眉毛高高挑起，身后翻滚的白色粉雪云轰鸣着涌过来。画面里没有别人。",
    SOUND_AVAL_V, AES_AVAL, lines=[('captain', "雪崩！快倒车！", 0.6, 'Captain')],
    cam=push1('the officer', '队长'), room={'Captain'}, new=True,
    bg='Behind him a roaring cloud of white powder rolls through the canyon and swallows the headlights of the convoy.',
    holds='The frame holds exactly one person: the officer, in the roof hatch, nobody else.')

insert2('33-09', '09｜冰谷：风雪渐渐停下来，整条冰谷被平平整整的新雪从这头填到那头，一台车的影子都看不见，只剩一层薄薄的粉雪雾在飘', 6, VALLEY_AFTER,
        'Wide high shot of the canyon, the smooth snow in the middle third of the frame, nobody visible.',
        "The roar dies away into a deep hush and the whole narrow canyon lies filled from wall to wall with smooth fresh snow, a thin haze of white powder drifting and glittering over it in the green aurora light, with not a single vehicle in sight. Nothing else moves.",
        "轰鸣声渐渐变成深深的寂静，整条窄窄的峡谷从这面墙到那面墙被平平整整的新雪填满，一层薄薄的白色粉雪雾在绿色极光的光里飘着、闪着，一辆车的影子都看不到。别的什么都不动。",
        SOUND_HUSH, 'The frame holds the snow-filled canyon, and nobody visible.',
        rise('the whole smooth snow-filled canyon and the strip of aurora sky', '整条被新雪填平的峡谷和一线极光天空'), AES_HUSH)

TA('33-10', '10｜驾驶舱：苏清月盯着仪表盘上的雷达，脸色大变，说是超级暴风雪，风力十四级，气温正降向零下一百度，窗外的天色一点点变白', 10, CAB,
   [P('su_tacfit', 'left', "sitting in the passenger seat in profile facing frame-right, one hand clutching the grab handle, her head turned from the radar screen to him", 'Lin', "her face gone white, her lips parted, her brows pulled high"),
    P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, both hands now gripping the control lever, his eyes on the sky beyond the windshield", 'obj:the whitening sky beyond the windshield', "his jaw clenched, his eyes hard, his brows low", outfit="in a charcoal henley under a dark olive utility vest")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<su_tacfit> speaks the first line to <lin_work> in a tight, shaking voice and then the second line in a flatter, frightened voice, her face gone white, her lips parted and her brows pulled high. <lin_work> grips the lever and keeps his eyes on the white windscreen, his jaw clenched, his eyes hard and his brows low, while the sky beyond the windshield turns slowly white.",
   "苏清月用紧绷发抖的声音对林峰说出第一句，接着用更平、更害怕的声音说出第二句，脸色发白、嘴唇微张、眉毛高高挑起。林峰握紧操纵杆盯着前方，下颌咬紧、眼神冷硬、眉头压低，挡风玻璃外的天空一点点变成白色。",
   SOUND_STORM_V, AES_STORM, lines=[('su_tacfit', "是超级暴风雪！风力十四级！", 0.8, 'Lin'), ('su_tacfit', "气温正降向零下一百度！", 4.0, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Between them a steaming paper cup stands in the cup holder and the small radar screen glows green in the dashboard at frame-right.',
   holds='The frame holds exactly two people: Su and Lin, sitting side by side in the cab, nobody else.')

# ================================================================================================ 第 34 集
b34 = S.episode('剧本第34集｜冰洞里的心跳', '十四级的超级暴风雪像白色的死神压过来，能见度一下子变成零；林峰死死拉着操纵杆，装甲房车在风暴吞掉他们之前，惊险地冲进一座巨大的天然冰洞；洞外狂风像厉鬼一样嘶吼，洞里漆黑一片，只有房车的暖黄色灯光，成了这片死亡大地上唯一的生命孤岛；车厢后部是铺着羊毛地毯的休息区，林峰靠在沙发上扯松领口，胸膛起伏；苏清月递水过来，房车在冰面上微微一滑，她脚下一崴，跌进林峰怀里；安静狭小又暖烘烘的车厢里两人贴得很近，林峰盯着她的嘴唇，哑着嗓子问：要是我们被困死，你会后悔吗；苏清月没有躲，反而伸手环住了他的脖子，画面切断。', 34)
new_scene(b34, 'ice_cave', '天然冰洞（巨大的拱形洞口，蓝色冰壁闪着光，垂着长长的冰柱，洞外是白茫茫的暴风雪）',
          'A huge natural ice cave with a great arched mouth, walls and ceiling of glittering blue ice and long icicles hanging, a roaring white blizzard beyond the arch.',
          '一座巨大的天然冰洞，洞口是高大的拱形，四壁和洞顶都是闪着光的蓝色冰，垂着长长的冰柱，拱口外是呼啸的白茫茫的暴风雪。',
          'the arched cave mouth, the glittering blue ice walls and the long icicles')
new_scene(b34, 'rv_lounge', '装甲房车后舱休息区（深棕色皮沙发靠着后墙，前面铺着厚厚的奶白色羊毛地毯，沙发扶手上叠着一条灰色羊毛毯，沙发上方两扇厚玻璃小窗）',
          'The cozy rear lounge of an armoured motorhome: a deep brown leather sofa along the back wall, a thick cream wool rug on the floor, a grey wool blanket folded over one arm of the sofa and two small thick-glass windows above the sofa white with blowing snow.',
          '一辆装甲房车温暖的后舱休息区：深棕色的皮沙发靠着后墙，地上铺着厚厚的奶白色羊毛地毯，沙发一边的扶手上叠着一条灰色羊毛毯，沙发上方是两扇被暴风雪拍白的厚玻璃小窗。',
          'the brown leather sofa, the cream wool rug, the grey blanket and the two small thick-glass windows')

insert2('34-01', '01｜冰洞口：白色的暴风雪墙从身后席卷过雪原，黑色的装甲房车亮着车灯，刚好冲进巨大的冰洞口', 6, CAVE_MOUTH,
        'Wide shot of the cave mouth, the dark arch and the plunging motorhome in the middle third of the frame, nobody visible.',
        "The matte-black armoured motorhome plunges into the glittering dark arch of the ice cave with its headlights blazing as a roaring white wall of blizzard sweeps across the snowfield right behind it. Nothing else moves.",
        "哑光黑色的装甲房车亮着车灯，一头冲进闪着光的黑色冰洞拱口，一面呼啸的白色暴风雪墙紧贴着它身后席卷过雪原。别的什么都不动。",
        SOUND_PLUNGE, 'The frame holds the ice cave arch with the plunging motorhome and the blizzard wall, and nobody visible.',
        drop('the cave arch and the plunging motorhome', '冰洞拱口和冲进去的房车'), AES_STORM, extra_assets=('armored_rv',))

TA('34-02', '02｜驾驶舱：林峰两手死死拉住操纵杆，肩膀绷紧，眼睛盯着一片空白的挡风玻璃，苏清月紧紧抓住扶手', 6, CAB_STORM,
   [P('su_tacfit', 'left', "sitting in the passenger seat in profile facing frame-right, both hands clutching the grab handle, her body braced", 'obj:the blank white windshield', "her lips pressed tight, her eyes wide, her brows pulled together"),
    P('lin_work', 'center-right', "sitting in the driver's seat in profile facing frame-right, both hands wrenching the steel control lever back, his shoulders braced", 'obj:the blank white windshield', "his jaw clenched, his eyes hard, his brows low", outfit="in a charcoal henley under a dark olive utility vest")],
   'Low-angle medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<lin_work> hauls the lever back with both hands, his shoulders braced, his jaw clenched, his eyes hard and his brows low, while <su_tacfit> clutches the grab handle beside him, her lips pressed tight, her eyes wide and her brows pulled together, and the windshield is a roaring blank white. Nobody speaks.",
   "林峰用双手把操纵杆死死往后拉，肩膀绷紧、下颌咬紧、眼神冷硬、眉头压低，苏清月在他身边紧紧抓着扶手，嘴唇紧抿、眼睛睁大、眉头拧在一起，挡风玻璃外是呼啸的一片空白。没有人说话。",
   SOUND_STORM, AES_STORM, cam=lowrise('Lin and Su', '林峰和苏清月'), room={'Su', 'Lin'}, new=True,
   bg='Between them a steaming paper cup stands in the cup holder and the roaring blank white of the blizzard fills the windshield at the right edge.',
   holds='The frame holds exactly two people: Su and Lin, sitting side by side in the cab, nobody else.')

insert2('34-03', '03｜冰洞里：巨大的冰洞里一片蓝色的幽暗，黑色的房车停在中间，窗户透出暖黄色的灯光，远处洞口被一层白色的风雪蒙着', 6, CAVE_IN,
        'Wide shot of the inside of the cave, the parked motorhome in the middle third of the frame, nobody visible.',
        "Inside the vast glittering ice cave the matte-black motorhome stands parked in the blue darkness with warm amber light glowing from its windows onto the ice, while far behind it the cave mouth is a pale arch veiled by blowing snow. Nothing else moves.",
        "巨大的冰洞里一片闪着光的蓝色幽暗，哑光黑色的房车停在中间，窗户里透出的暖黄色灯光映在冰壁上，远远的身后，洞口是一道被风雪蒙住的白色拱门。别的什么都不动。",
        SOUND_CAVE, 'The frame holds the ice cave with the parked motorhome, and nobody visible.',
        rise('the whole cave with the glowing motorhome and the pale arch beyond', '整座冰洞、发着暖光的房车和远处苍白的洞口'), AES_CAVE, extra_assets=('armored_rv',))

insert2('34-04', '04｜插镜：后舱的厚玻璃窗外，白色的暴风雪一阵阵拍在玻璃上，玻璃内侧结着一圈霜花，暖黄的灯光映在上面', 5, LOUNGE_WIN,
        'Close shot of the small thick-glass window in the middle third of the frame, nobody in the scene.',
        "Beyond the thick glass the white blizzard pounds in slow surges and frost ferns spread slowly at the edges of the pane while warm amber lamp light glows on the glass from inside. Nothing else moves.",
        "厚厚的玻璃窗外，白色的暴风雪一阵一阵地拍着，玻璃边缘的霜花慢慢蔓延，室内温暖的琥珀色灯光映在玻璃上。别的什么都不动。",
        SOUND_LOUNGE, 'The frame holds the small thick-glass window with the blizzard beyond it, and nobody in the scene.',
        push1('the frosted window and the blizzard beyond', '结霜的窗户和玻璃外的暴风雪'), AES_LOUNGE)

TA('34-05', '05｜后舱：林峰靠在沙发上扯松了领口，胸膛起伏，苏清月拿着一瓶水走到他面前，说喝点水吧', 7, LOUNGE,
   [P('lin_work', 'right', "sitting back on the leather sofa in profile facing frame-left, his head resting against the cushion and his chest heaving, one hand pulling his collar open", 'Su', "his jaw loosening, his eyes half closed, his brows soft", outfit=LIN_OPEN),
    P('su_tacfit', 'left', "standing in front of the sofa in profile facing frame-right, holding out a bottle of water in one hand", 'Lin', "her lips pressed softly together in worry, her eyes warm, her brows lifted", outfit=LOUNGE_L)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the rear lounge.',
   "<lin_work> leans back with his chest rising and falling and one hand tugging his collar loose, his jaw loosening, his eyes half closed and his brows soft. <su_tacfit> steps up and holds out the water bottle and speaks the one line to <lin_work> in a soft, gentle voice, her lips pressed softly together in worry, her eyes warm and her brows lifted.",
   "林峰向后靠着，胸膛一起一伏，一只手扯松领口，下颌放松、眼睛半闭、眉毛舒展。苏清月走过来，把水瓶递到他面前，用轻柔温和的声音对林峰说出这一句，嘴角带着柔和担心的笑、眼神温暖、眉毛上扬。",
   SOUND_LOUNGE_V, AES_LOUNGE, lines=[('su_tacfit', "喝点水吧。", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Above the sofa the two thick-glass windows are white with blowing snow and a grey wool blanket is folded over one arm of the sofa.',
   holds='The frame holds exactly two people: Su and Lin, in the rear lounge, nobody else.')

TA('34-06', '06｜后舱：房车在冰面上微微一滑，苏清月脚下一崴，整个人向前跌，林峰伸出双臂把她接进怀里', 5, LOUNGE,
   [P('su_tacfit', 'left', "leaning forward off balance in front of the sofa in profile facing frame-right, one foot slipping on the rug, the water bottle in her hand", 'Lin', "her eyes wide, her lips parting in surprise, her brows lifted", outfit=LOUNGE_L),
    P('lin_work', 'right', "sitting on the leather sofa in profile facing frame-left, leaning forward with both arms opening to catch her", 'Su', "his eyes wide, his jaw loosening, his brows lifted", outfit=LIN_OPEN)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the rear lounge.',
   "The motorhome shudders gently on the ice and <su_tacfit> slips forward, her eyes wide, her lips parting in surprise and her brows lifted, and <lin_work> catches her in both arms and pulls her against his chest, his eyes wide, his jaw loosening and his brows lifted. Nobody speaks.",
   "房车在冰面上轻轻晃了一下，苏清月脚下一滑向前跌去，眼睛睁大、嘴唇惊讶地微张、眉毛上扬，林峰用双臂接住她，把她按在胸前，眼睛睁大、下颌放松、眉毛上扬。没有人说话。",
   SOUND_SLIP, AES_LOUNGE, cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Above the sofa the two thick-glass windows are white with blowing snow.',
   holds='The frame holds exactly two people: Su and Lin, in the rear lounge, nobody else.')

TA('34-07', '07｜后舱：苏清月被他抱在怀里，手按在他胸口上，两张脸只隔着一点点距离，林峰盯着她的嘴唇，哑着嗓子问要是我们被困死你会后悔吗', 8, LOUNGE,
   [P('lin_work', 'right', "sitting on the leather sofa in profile facing frame-left, holding her close against his chest with both arms, his head bent toward her", 'Su', "his eyes burning dark and fixed on her lips, his jaw tight, his brows low", outfit=LIN_OPEN),
    P('su_tacfit', 'left', "held against his chest in profile facing frame-right, one hand resting flat on his chest, her face tipped up to his", 'Lin', "her lips parted, her eyes wide and soft, her brows lifted", outfit=LOUNGE_L)],
   'Close two-shot, both from the head to the chest, in the middle third of the frame, in the rear lounge.',
   "<lin_work> holds <su_tacfit> close and speaks the one line to <su_tacfit> in a rough, hoarse, low voice, his eyes burning dark and fixed on her lips, his jaw tight and his brows low. <su_tacfit> looks up at him with her hand on his chest, her lips parted, her eyes wide and soft and her brows lifted.",
   "林峰把苏清月抱在怀里，用粗哑低沉的声音对苏清月说出这一句，眼睛又黑又烫，盯着她的嘴唇，下颌绷紧、眉头压低。苏清月手按在他胸口，仰脸看着他，嘴唇微张、眼睛睁大又柔软、眉毛上扬。",
   SOUND_LOUNGE_V, AES_LOUNGE, lines=[('lin_work', "要是我们被困死，你会后悔吗？", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the two thick-glass windows are white with blowing snow and the grey wool blanket lies folded over the arm of the sofa.',
   holds='The frame holds exactly two people: Lin and Su, in the rear lounge, nobody else.')

TA('34-08', '08｜后舱：苏清月没有躲开，慢慢抬起双手，环住了林峰的脖子', 6, LOUNGE,
   [P('lin_work', 'right', "sitting on the leather sofa in profile facing frame-left, holding her close with both arms, his head bent toward her", 'Su', "his eyes dark and fixed on her face, his jaw loosening, his brows low", outfit=LIN_OPEN),
    P('su_tacfit', 'left', "held against his chest in profile facing frame-right, both hands slowly sliding up around the back of his neck", 'Lin', "her eyes bold and shining, a small coy smile on her lips, her brows lifted", outfit=LOUNGE_L)],
   'Close two-shot, both from the head to the chest, in the middle third of the frame, in the rear lounge.',
   "<su_tacfit> slides both hands slowly up and around the back of <lin_work>'s neck and holds there, her eyes bold and shining, a small coy smile on her lips and her brows lifted, while <lin_work> goes still, his eyes dark and fixed on her face, his jaw loosening and his brows low. Nobody speaks.",
   "苏清月把双手慢慢滑上去，环住林峰的脖子，停在那里，眼睛大胆发亮、嘴角带着一丝大胆的笑、眉毛上扬，林峰一下子静住，眼睛又黑又深地盯着她的脸，下颌放松、眉头压低。没有人说话。",
   SOUND_KISS, AES_LOUNGE, cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the two thick-glass windows are white with blowing snow.',
   holds='The frame holds exactly two people: Su and Lin, in the rear lounge, nobody else.')

# ================================================================================================ 第 35 集
b35 = S.episode('剧本第35集｜极致占有', '“我只后悔，你废话太多了。”苏清月的话成了最后一点火星，林峰俯身吻住了她，把她慢慢放倒在柔软的羊毛垫上；外面的暴风雪拍着装甲玻璃，零下一百度，车厢里暖风呼呼，玻璃上起了一层白雾；他吻得又霸道又温柔，捧着她的脸说：你比这该死的末日，还让人上瘾；第二天清晨风暴停了，阳光穿过冰缝折成七彩，洒在裹着毯子睡着的两人身上；房车驶出冰洞，平稳地开回地下避难所；回家后苏清月端着咖啡说回家真好；她无意中看了一眼主控台那块平时从不亮的探测仪，屏幕上一个巨大的红橙色热源正在墙外刨地；她手里的杯子啪地摔碎：林峰，有东西在挖我们的墙，警报声里画面拉黑。', 35)

TA('35-01', '01｜后舱：苏清月靠在林峰怀里，手指勾着他的领口，轻声说我只后悔，你废话太多了', 7, LOUNGE,
   [P('su_tacfit', 'left', "sitting close beside him on the leather sofa in profile facing frame-right, one hand hooked in his open collar, her face tipped up to him", 'Lin', "her lips curving in a bold, coy smile, her eyes shining, her brows lifted", outfit=LOUNGE_L),
    P('lin_work', 'right', "sitting on the leather sofa in profile facing frame-left, one arm around her, his head bent toward her", 'Su', "his eyes burning dark, his jaw tight, his brows low", outfit=LIN_OPEN)],
   'Close two-shot, both from the head to the chest, in the middle third of the frame, in the rear lounge.',
   "<su_tacfit> speaks the one line to <lin_work> in a soft, husky, daring voice, her lips curving in a bold coy smile, her eyes shining and her brows lifted. <lin_work> listens, his eyes burning dark, his jaw tight and his brows low.",
   "苏清月用轻柔沙哑、大胆的声音对林峰说出这一句，嘴角带着大胆迷人的笑、眼睛发亮、眉毛上扬。林峰听着，眼睛又黑又烫、下颌绷紧、眉头压低。",
   SOUND_LOUNGE_V, AES_LOUNGE, lines=[('su_tacfit', "我只后悔，你废话太多了。", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the two thick-glass windows are white with blowing snow.',
   holds='The frame holds exactly two people: Su and Lin, in the rear lounge, nobody else.')

TA('35-02', '02｜后舱：林峰俯下身吻住了她，一只手托着她的后背，慢慢把她放倒在沙发的羊毛垫上', 6, LOUNGE,
   [P('lin_work', 'right', "leaning over her on the leather sofa in profile facing frame-left, one hand cradling her back as he lowers her slowly onto the wool cushions, his lips pressed to hers", 'closed', "his brows soft", outfit=LIN_OPEN),
    P('su_tacfit', 'left', "lying back against the wool cushions in profile facing frame-right, one hand curled in his collar, her lips pressed to his", 'closed', "her brows soft", outfit=LOUNGE_L)],
   'Close two-shot, both from the head to the chest, in the middle third of the frame, in the rear lounge.',
   "<lin_work> kisses <su_tacfit> deeply and lowers her slowly back onto the cushions with one hand behind her, his eyes closed and his brows soft, while <su_tacfit> kisses him back, her eyes closed and her brows soft. Nobody speaks.",
   "林峰深深地吻住苏清月，一只手托在她身后，慢慢把她放倒在垫子上，眼睛闭着、眉毛舒展，苏清月回吻着他，眼睛闭着、眉毛舒展。没有人说话。",
   SOUND_KISS, AES_LOUNGE, cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the two thick-glass windows are white with blowing snow.',
   holds='The frame holds exactly two people: Lin and Su, in the rear lounge, nobody else.')

insert2('35-03', '03｜插镜：厚玻璃窗内侧蒙上了一层柔软的白色暖雾，窗外的暴风雪在雾后面发着淡淡的蓝光', 5, LOUNGE_WIN,
        'Close shot of the small thick-glass window in the middle third of the frame, nobody in the scene.',
        "A soft white veil of warm breath clouds the whole pane of the thick-glass window, the blizzard glows faintly blue beyond it and amber lamp light blurs into soft golden halos on the fogged glass. Nothing else moves.",
        "厚玻璃窗整块内侧都蒙着一层柔软的白色暖雾，雾后面暴风雪发着淡淡的蓝光，琥珀色的灯光在起雾的玻璃上晕成柔和的金色光晕。别的什么都不动。",
        SOUND_LOUNGE, 'The frame holds the fogged thick-glass window, and nobody in the scene.',
        push1('the fogged window and the blue glow beyond', '起雾的窗户和雾后淡蓝色的光'), AES_FOG)

TA('35-04', '04｜后舱：林峰捧着苏清月的脸，额头抵着她的额头，低声说你比这该死的末日，还让人上瘾', 7, LOUNGE,
   [P('lin_work', 'right', "sitting on the leather sofa in profile facing frame-left, cupping her face gently in both hands, his forehead resting against hers", 'Su', "his eyes dark and tender, his jaw loosening, his brows soft", outfit=LIN_OPEN),
    P('su_tacfit', 'left', "sitting close in profile facing frame-right, her hands resting on his wrists, her face tipped up to his", 'Lin', "her eyes shining and soft, her lips parted in a quiet sweet smile, her brows lifted", outfit=LOUNGE_L)],
   'Close two-shot, both from the head to the chest, in the middle third of the frame, in the rear lounge.',
   "<lin_work> cups her face and speaks the one line to <su_tacfit> in a low, rough, tender voice, his eyes dark and tender, his jaw loosening and his brows soft. <su_tacfit> listens, her eyes shining and soft, her lips parted in a quiet sweet smile and her brows lifted.",
   "林峰捧着她的脸，用低沉粗哑又温柔的声音对苏清月说出这一句，眼神又黑又温柔、下颌放松、眉毛舒展。苏清月听着，眼睛发亮柔软、嘴唇微张带着安静的甜笑、眉毛上扬。",
   SOUND_LOUNGE_V, AES_LOUNGE, lines=[('lin_work', "你比这末日，还让人上瘾。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the two thick-glass windows glow soft with fog and the grey wool blanket lies over the arm of the sofa.',
   holds='The frame holds exactly two people: Lin and Su, in the rear lounge, nobody else.')

insert2('35-05', '05｜插镜：第二天清晨，一道道晨光从冰缝里斜斜射进冰洞，在蓝色的冰壁上折成柔和的彩虹光束，冰尘在光里飘', 5, CAVE_RAY,
        'Low close shot of the ice wall, the rainbow beams in the middle third of the frame, nobody in the scene.',
        "Slanting shafts of pale morning sun come through two cracks in the ice and break into soft rainbow beams across the glittering blue wall while fine ice dust drifts slowly through the colored light. Nothing else moves.",
        "淡淡的晨光斜斜地从两道冰缝里射进来，在闪光的蓝色冰壁上折成柔和的七彩光束，细细的冰尘慢慢飘过彩色的光。别的什么都不动。",
        SOUND_CAVE, 'The frame holds the glittering ice wall with the rainbow beams, and nobody in the scene.',
        lowrise('the rainbow beams on the ice wall', '冰壁上的七彩光束'), AES_RAINBOW)

TA('35-06', '06｜后舱：七彩的晨光洒进来，林峰和苏清月裹着同一条灰色羊毛毯，依偎在沙发上睡着了，衣服整整齐齐', 6, LOUNGE_MORN,
   [P('lin_work', 'right', "sleeping upright on the leather sofa in profile facing frame-left, the grey wool blanket pulled round both their shoulders, his head resting against hers", 'closed', "his jaw relaxed, his lips softly closed, his brows soft", outfit=LIN_OPEN),
    P('su_tacfit', 'left', "sleeping curled against his shoulder in profile facing frame-right under the same grey blanket, her head tucked beneath his chin", 'closed', "her lips softly parted in sleep, her brows soft", outfit=LOUNGE_L)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, in the rear lounge.',
   "<lin_work> and <su_tacfit> sleep close together under the grey blanket as soft rainbow morning light slides slowly across them, his jaw relaxed, his lips softly closed and his brows soft, and her lips softly parted in sleep and her brows soft. Nobody speaks.",
   "林峰和苏清月裹着灰色的毯子依偎着睡着，柔和的七彩晨光慢慢从他们身上滑过，他下颌放松、嘴唇轻轻闭着、眉毛舒展，她嘴唇在睡梦里微微张开、眉毛舒展。没有人说话。",
   SOUND_SLEEP, AES_RAINBOW, cam=slide('right', '右', 'the two sleepers fill the middle third of the frame', '两个熟睡的人占满画面中间三分之一'), room={'Su', 'Lin'}, new=True,
   bg='Above them the two thick-glass windows glow pale gold with morning light.',
   holds='The frame holds exactly two people: Lin and Su, asleep on the sofa, nobody else.')

insert2('35-07', '07｜地表雪原：风暴停了，粉红色的晨光铺在平静的新雪上，黑色的装甲房车从冰洞拱口里缓缓驶出来，在雪地上留下两道辙痕', 6, DAWN,
        'Wide shot of the snowfield, the ice cave arch and the rolling motorhome in the middle third of the frame, nobody visible.',
        "The matte-black armoured motorhome rolls slowly out of the great ice cave arch onto the calm fresh snow under the pale rose-gold dawn, leaving two deep tread lines behind it as fine snow crystals glitter in the still air. Nothing else moves.",
        "哑光黑色的装甲房车从巨大的冰洞拱口里缓缓驶出来，开到平静的新雪上，淡淡的玫瑰金色晨光里，身后留下两道深深的辙痕，细小的雪晶在静止的空气里闪烁。别的什么都不动。",
        SOUND_DAWN, 'The frame holds the calm snowfield with the ice cave arch and the rolling motorhome, and nobody visible.',
        rise('the calm snowfield, the cave arch and the rolling motorhome', '平静的雪原、冰洞拱口和缓缓驶出的房车'), AES_DAWN, extra_assets=('armored_rv',))

TA('35-08', '08｜家里：苏清月端着热咖啡说回家真好，林峰切着面包说先吃早餐，再睡一觉', 8, LIV_BF,
   [P('su_cozy', 'left', "standing at the dining table in profile facing frame-right, both hands wrapped round a steaming white mug, her damp hair loose over her shoulders", 'Lin', "her eyes closed in relief, a blissful sweet smile on her lips, her brows soft"),
    P('lin_home', 'center', "standing at the table in profile facing frame-left, slicing a golden loaf on the wooden board", 'obj:the loaf on the wooden board', "one corner of his mouth lifting, his jaw relaxed, his brows soft", outfit="in a soft grey henley and dark lounge pants")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dining table.',
   "<su_cozy> takes a slow sip of her coffee and speaks the first line to <lin_home> in a soft, contented voice, her eyes closed in relief, a blissful sweet smile on her lips and her brows soft. <lin_home> keeps slicing the loaf and answers with the second line to <su_cozy> in a low, warm voice, one corner of his mouth lifting, his jaw relaxed and his brows soft.",
   "苏清月慢慢啜了一口咖啡，用柔软满足的声音对林峰说出第一句，眼睛松了口气地闭着、嘴角带着幸福的甜笑、眉毛舒展。林峰继续切着面包，用低沉温暖的声音对苏清月答出第二句，嘴角微微上扬、下颌放松、眉毛舒展。",
   SOUND_HOME, AES_BF, lines=[('su_cozy', "回家真好。", 0.8, 'Lin'), ('lin_home', "先吃早餐，再睡一觉。", 2.4, 'Su')],
   cam=push('both of them', '两人'), extra_assets=('jam_jar',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the black-and-gold stove glows warm at frame-left and the wall of small monitors glows cool blue at frame-right.',
   holds='The frame holds exactly two people: Su and Lin, at the dining table, nobody else.')

insert2('35-09', '09｜插镜：主控台上那块平时从来不亮的宽屏，屏幕中间一团巨大的红橙色热源正在脉动，热源边缘一下一下地刨着一条墙线', 5, Scene('bunker_control', CONTROL.end,
        " Fixed stage layout: a wide dark detector screen in a matte black frame fills the middle of the frame, a huge glowing red-orange heat bloom burning in its center and pulsing, with a faint straight wall line at its edge that the bloom keeps scraping against; the steel control console glows teal around it."),
        'Close shot of the wide detector screen in the middle third of the frame, nobody in the scene.',
        "A huge red-orange heat bloom burns and pulses in the center of the wide dark detector screen while its edge scrapes again and again against a faint straight wall line and the teal console light flickers around the frame. Nothing else moves.",
        "一块宽宽的黑色探测仪屏幕上，一团巨大的红橙色热源在中间燃着、脉动，热源的边缘一下又一下地刮着一条淡淡的直直的墙线，控制台青色的光在屏幕周围轻轻闪烁。别的什么都不动。",
        SOUND_HEAT, 'The frame holds the wide dark detector screen with the red-orange heat bloom, and nobody in the scene.',
        push1('the pulsing heat bloom', '脉动的红橙色热源'), AES_HEAT, extra_assets=('bio_detector',))

TA('35-10', '10｜控制室：苏清月站在探测仪前，咖啡杯已经摔碎在脚边，她脸色惨白地转头对林峰说林峰，有东西在挖我们的墙', 7, CONTROL_C,
   [P('su_cozy', 'left', "standing in front of the wide dark detector screen in profile facing frame-right, her hand still open in the air where the cup fell, shards of a white porcelain cup and a spill of coffee on the floor at her feet, her head turned to him", 'Lin', "her face drained white, her lips trembling, her brows pulled high"),
    P('lin_home', 'right', "standing beside the black swivel chair in profile facing frame-left, his eyes snapping to the screen", 'obj:the wide dark detector screen', "his jaw tightening, his eyes hard, his brows low", outfit="in a soft grey henley and dark lounge pants")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the control console.',
   "<su_cozy> speaks the one line to <lin_home> in a thin, shaking voice, her face drained white, her lips trembling and her brows pulled high, while a small red alarm lamp on the wall pulses. <lin_home> looks at the screen, his jaw tightening, his eyes hard and his brows low.",
   "苏清月用细细发抖的声音对林峰说出这一句，脸色惨白、嘴唇发颤、眉毛高高挑起，墙上的一盏小红灯在脉动。林峰看着屏幕，下颌绷紧、眼神冷硬、眉头压低。",
   SOUND_ALARM, AES_RED, lines=[('su_cozy', "林峰，有东西在挖我们的墙！", 0.8, 'Lin')],
   cam=push('both of them', '两人'), extra_assets=('bio_detector',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the wide dark detector screen glows red-orange on the console and the wall of six small monitors glows at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, at the control console, nobody else.')

# ================================================================================================ 第 36 集
b36 = S.episode('剧本第36集｜地底的巨兽', '“轰……轰……”沉闷的撞击顺着冻土传进地下室，农场里的叶子在抖，水槽里的水泛起波纹；探测仪屏幕上，一头体长近四米、体重超过一吨的极地变异巨熊正在疯狂刨击负二层农场的外墙，它被极寒逼疯了，闻到了里面的热量和小鸡的肉味；两人冲下农场，粉紫色的植物灯下，坚固的合金墙被拍出一道凸起的凹痕；苏清月握着战术匕首脸色苍白：它的爪子能拍变形合金墙，它冲进来农场就全毁了；林峰却看着农场尽头那扇巨大的合金闸门，眼神闪过一丝疯狂的残忍：它要进来，我就请它吃顿好的。', 36)
b36.prop('bio_detector', '深层生物热能探测仪（黑色哑光边框的宽屏，屏幕上是深色的地层剖面，中间一团发光的红橙色热源）',
         'A wide dark detector screen in a matte black frame showing a dark underground cross-section with a huge glowing red-orange heat bloom in its center. The reference fixes its look.',
         '一块黑色哑光边框的宽屏探测仪，屏幕上是深色的地层剖面，中间有一团发光的红橙色热源。参考图固定它的外形。',
         'A photorealistic product shot of a wide dark detector screen in a matte black frame showing a dark underground cross-section with a huge glowing red-orange heat bloom in its center, against a plain neutral gray background.')

insert2('36-01', '01｜农场：沉闷的一声撞击顺着墙传过来，水槽里的水泛起一圈圈波纹，西红柿苗的叶子在抖，细细的灰尘从天花板上落下来', 5, EDEN_SHAKE,
        'Low close shot of the hydroponic channels, the trembling seedlings in the middle third of the frame, nobody in the scene.',
        "A deep dull thud runs through the concrete; ripples spread across the water in the hydroponic channels, the green leaves of the tomato seedlings tremble and a fine veil of dust sifts down through the pink-violet light. Nothing else moves.",
        "一声深沉的闷响穿过混凝土；水槽里的水面泛起一圈圈波纹，西红柿苗的绿叶在发抖，一层细细的灰尘从粉紫色的光里落下来。别的什么都不动。",
        SOUND_THUD, 'The frame holds the hydroponic channels with the trembling tomato seedlings, and nobody in the scene.',
        lowrise('the trembling leaves and the rippling water', '发抖的叶子和泛着波纹的水'), AES_FARM)

TA('36-02', '02｜控制室：林峰指着宽屏上巨大的熊形热源，说四米长，一吨重，被极寒逼疯了，苏清月说它闻到鸡的味道了', 10, CONTROL_C,
   [P('lin_work', 'right', "standing at the console in profile facing frame-left, one hand on the edge of the wide dark detector screen where a huge bear-shaped red-orange heat bloom glows", 'obj:the wide dark detector screen', "his jaw tight, his eyes hard and cold, his brows low", outfit="in a charcoal henley under a dark olive utility vest"),
    P('su_surgeon', 'left', "standing beside him in profile facing frame-right, her gloved hands clasped tight, her eyes on the screen", 'obj:the wide dark detector screen', "her lips pressed pale, her brows pulled together")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "<lin_work> speaks the first line to <su_surgeon> in a low, grim, even voice, his jaw tight, his eyes hard and cold and his brows low. <su_surgeon> answers with the second line to <lin_work> in a tight, quick voice, her lips pressed pale and her brows pulled together, while the red-orange glow of the screen pulses across their faces.",
   "林峰用低沉凝重平稳的声音对苏清月说出第一句，下颌绷紧、眼神冷硬、眉头压低。苏清月用紧绷急促的声音对林峰答出第二句，嘴唇发白抿着、眉头拧在一起，屏幕红橙色的光在两人脸上脉动。",
   SOUND_HEAT, AES_HEAT, lines=[('lin_work', "四米长，一吨重，被极寒逼疯了。", 0.8, 'Su'), ('su_surgeon', "它闻到了小鸡的味道。", 4.8, 'Lin')],
   cam=push('both of them', '两人'), extra_assets=('bio_detector',), room={'Su', 'Lin'}, new=True,
   bg='Behind them the wall of six small monitors glows at frame-left and the wide dark detector screen glows red-orange on the console.',
   holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

TA('36-03', '03｜农场楼梯：林峰和苏清月一前一后快步走下钢楼梯，粉紫色的植物灯光从下面照上来，脚下的楼梯随着闷响轻轻震', 6, EDEN_STAIR,
   [P('lin_work', 'center', "hurrying down the steel staircase in profile facing frame-left, one hand sliding along the rail", 'obj:the farm level below him', "his jaw set, his eyes hard, his brows low", outfit="in a charcoal henley under a dark olive utility vest"),
    P('su_surgeon', 'right', "following one step behind him down the staircase in profile facing frame-left, a slim tactical dagger in her right hand", 'Lin', "her lips pressed tight, her brows pulled together")],
   'Medium wide tracking shot, both from the head to the knees, in the middle third of the frame, on the steel staircase.',
   "<lin_work> hurries down the steel staircase with his hand sliding along the rail, his jaw set, his eyes hard and his brows low, and <su_surgeon> follows a step behind with a slim tactical dagger in her hand, her lips pressed tight and her brows pulled together, while a dull thud shivers through the stairs. Nobody speaks.",
   "林峰快步走下钢楼梯，一只手扶着栏杆滑下去，下颌绷住、眼神冷硬、眉头压低，苏清月手里握着一把细长的战术匕首跟在他身后一步，嘴唇紧抿、眉头拧在一起，一声闷响让楼梯轻轻发颤。没有人说话。",
   SOUND_STAIR, AES_FARM, cam=track('the two of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Below them long tiers of lettuce and tomato seedlings glow under rows of pink-violet grow lamps.',
   holds='The frame holds exactly two people: Lin and Su, on the steel staircase, nobody else.')

insert2('36-04', '04｜农场尽头：一道巨大的圆形凹痕从厚厚的灰色合金墙里向内鼓起，墙缝里的隔热层被撕开，细灰一层层往下落', 5, EDEN_WALL,
        'Low close shot of the alloy wall, the huge dent in the middle third of the frame, nobody in the scene.',
        "A huge rounded dent bulges inward across the thick grey alloy wall, the torn insulation showing along its seam, and a fine veil of dust sifts down through the pink-violet light while the metal gives a long low creak. Nothing else moves.",
        "厚厚的灰色合金墙上，一道巨大的圆形凹痕向内鼓起，墙缝里撕开的隔热层露了出来，细灰在粉紫色的光里一层层落下来，金属发出一声长长的低低的吱呀。别的什么都不动。",
        SOUND_WALLDENT, 'The frame holds the grey alloy wall with its huge dent, and nobody in the scene.',
        lowrise('the huge dent in the alloy wall', '合金墙上巨大的凹痕'), AES_FARM)

TA('36-05', '05｜农场：苏清月握着匕首，脸色发白，说它的爪子能拍变形合金墙，它冲进来农场就全毁了', 10, EDEN_WALL,
   [P('su_surgeon', 'left', "standing before the dented alloy wall in profile facing frame-right, a slim tactical dagger gripped in her right hand, her head turned to him", 'Lin', "her face gone pale, her lips trembling, her brows pulled high"),
    P('lin_work', 'right', "standing beside her in profile facing frame-left, his arms loose at his sides, his eyes on the dent", 'obj:the dent in the alloy wall', "his jaw tight, his eyes hard and calm, his brows low", outfit="in a charcoal henley under a dark olive utility vest")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, before the dented wall.',
   "<su_surgeon> speaks the first line to <lin_work> in a tight, unsteady voice and then the second line in a higher, more frightened voice, her face gone pale, her lips trembling and her brows pulled high. <lin_work> stands calm beside her, his jaw tight, his eyes hard and calm and his brows low, while a dull thud shivers the wall.",
   "苏清月用紧绷不稳的声音对林峰说出第一句，接着用更高、更害怕的声音说出第二句，脸色发白、嘴唇发颤、眉毛高高挑起。林峰平静地站在她身边，下颌绷紧、眼神冷硬而平静、眉头压低，墙上又传来一声闷响。",
   SOUND_FARM_V, AES_FARM, lines=[('su_surgeon', "它的爪子能拍变形合金墙！", 0.8, 'Lin'), ('su_surgeon', "它冲进来，农场就全毁了！", 4.4, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the huge dent bulges across the grey alloy wall and rows of tomato seedlings glow under pink-violet grow lamps.',
   holds='The frame holds exactly two people: Su and Lin, before the dented wall, nobody else.')

TA('36-06', '06｜农场：林峰没有看墙，而是看着农场尽头那扇巨大的合金闸门，眼神闪过一丝疯狂的狠，说它要进来，我就请它吃顿好的', 8, EDEN_GATE,
   [P('lin_work', 'center', "standing in the middle of the farm aisle in profile facing frame-right, his head turned toward the huge grey alloy gate at the far end", 'obj:the huge grey alloy gate at the far end of the farm', "a ruthless, almost mad glint in his eyes, one corner of his mouth lifting coldly, his brows low", outfit="in a charcoal henley under a dark olive utility vest"),
    P('su_surgeon', 'left', "standing a step behind him in profile facing frame-right, the dagger lowered at her side, her head turned to him", 'Lin', "her lips parting, her eyes wide, her brows pulled together")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the farm aisle.',
   "<lin_work> keeps his eyes on the gate and speaks the one line to <su_surgeon> in a low, soft, chilling voice, a ruthless almost mad glint in his eyes, one corner of his mouth lifting coldly and his brows low. <su_surgeon> stares at him, her lips parting, her eyes wide and her brows pulled together.",
   "林峰眼睛盯着那扇闸门，用低沉轻柔、让人发冷的声音对苏清月说出这一句，眼里闪着狠绝近乎疯狂的光，嘴角冷冷地一挑、眉头压低。苏清月瞪着他，嘴唇微张、眼睛睁大、眉头拧在一起。",
   SOUND_GATE, AES_GATE, lines=[('lin_work', "它要进来，我就请它吃顿好的。", 0.8, 'Su')],
   cam=slide('right', '右', 'Lin stands in the middle third of the frame with the huge gate beyond him', '林峰占画面中间三分之一、他身后是那扇巨大的闸门'),
   room={'Su', 'Lin'}, new=True,
   bg='At the far end of the aisle the huge grey alloy gate with yellow-black warning stripes stands closed and tomato seedlings glow under pink-violet grow lamps on both sides.',
   holds='The frame holds exactly two people: Lin and Su, in the farm aisle, nobody else.')

insert2('36-07', '07｜插镜：巨大的合金闸门上，黄黑相间的警示条纹和厚厚的装甲玻璃小窗，玻璃外侧结着一层淡蓝色的冰花，旁边的控制盘上一根红色的拉杆', 5, GATE_CLOSE,
        'Close shot of the huge alloy gate, the armoured-glass window in the middle third of the frame, nobody in the scene.',
        "The thick armoured-glass window of the huge grey alloy gate is frosted with pale blue ice flowers on its outer side, the yellow-black warning stripes run around it and a red lever on the steel control panel at frame-right waits in the cold white light. Nothing else moves.",
        "巨大的灰色合金闸门上，厚厚的装甲玻璃小窗外侧结着淡蓝色的冰花，四周是黄黑相间的警示条纹，右边钢制控制盘上的一根红色拉杆静静地立在冷白色的光里。别的什么都不动。",
        SOUND_GATE, 'The frame holds the grey alloy gate with its frosted window and the red lever, and nobody in the scene.',
        push1('the frosted window of the gate', '闸门上结霜的小窗'), AES_GATE)

doc = S.finish()
