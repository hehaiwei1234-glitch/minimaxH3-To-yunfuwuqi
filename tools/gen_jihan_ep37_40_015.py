#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 37–40 集，追加稿 015（2026-10-14）。以 014 的 JSON 为底（style／素材／角色逐字复制），必须等 014 在插件里全部跑完再追加。
hh 2026-10-14 18:19：“再更新出来 16 集，我挂通宵，一批一批来，一次 4 集。”本批＝第三批（37–40）。写法＝013／014 同一套（共用定义在 _jihan_base6.py）。

偏离大纲（交稿时已告诉 hh）：
  · 第 37 集：只拍巨熊冲进缓冲舱、闸门关死后的结果、舱里一整面白雾、雾散后冻在扑击姿势的冰雕；“闸门升起”“门锁死”“液氮喷射的过程”都不拍过程，拍结果；
    苏清月拉不拉杆都不拍，只拍林峰一只手拉下红色拉杆；“凄厉惨叫三秒”只留声音；
  · 第 38 集：解剖不拍剥皮和血，只拍苏清月在白色瓷砖的处理间里切一大块修剪整齐的深红色肉、林峰把包好的肉块搬上推车，之后拍冷库里一排排结霜的包裹；
    “壁炉”改成家里本来就有的黑金色炉子（上面架铁网烤熊排）；熊排只喂一口；“地下二层警报器响一声”＋声纳图里冻土后面一个大空洞；
  · 第 39 集：地洞里没有熊（已被冻成冰雕）；手电改成头灯；“盲鱼”只拍一个近景和喂食；加固通道只拍结果（钢拱肋＋灯带＋一台小型黄色工程机器停在边上）；
  · 第 40 集：温泉不拍泡在水里的身体：两个人穿着厚白色浴袍坐在池边岩台，脚泡在水里，他吻她的头发，不拍“吻锁骨”；
    喂盲鱼＋炖鱼汤合成一个任务；“I SEE YOU”不写画面文字，改成主控台扬声器里一个合成的声音说“我看到你了。”（画外旁白，屏幕道具开口，不画人）；绿色代码只拍一屏看不清字的绿色字符瀑布。
H3 方面的风险（交稿时单列，不算我的错）：
  · 37-03 巨熊冲过舱室（大型动物快动作，没有任何数据）；37-04 熊掌拍在玻璃上＋裂纹；37-06 液氮白雾；37-07 熊冻在扑击姿势的冰雕；37-02／37-05／37-08 人在前景、巨熊（冰雕）隔着玻璃在后景；
  · 38-01 融冰滴水；38-02 切肉（手和刀）；38-05 喂熊排（叉子到嘴边）；38-06 红灯；
  · 39-01 头灯手电的光束；39-02 发光苔藓＋温泉的大场景；39-05 盲鱼；39-07 工程机器；39-08 拉开领口；
  · 40-01 坐在池边浴袍靠肩；40-03 喂鱼＋盛汤；40-05 到 40-07 屏幕上的绿色代码和画外合成声音（可能被画成屏幕里有一个人或画面里的人张嘴念）；
  · 开场图约一成不按文字画；“同一处”场景（缓冲舱、溶洞）用参照图。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
from _jihan_base6 import *
from _scene import smooth_task

import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407)   # hh 2026-10-14 16:20：台词顺滑写法＋全批固定视频种子
OUT = '合并稿/015_第37-40集_请君入瓮熊排溶洞温泉幽灵黑客_制作稿_追加'
S = Session('合并稿/014_第33-36集_雪崩冰洞心跳吻里的末日巨熊_制作稿_追加.json', OUT, 47000)
B6.S = S

# ---------------------------------------------------------------------------------------------- 光和空气（本批新增）
AES_RED = ("A slow red warning pulse washes the room and rim-lights the edges of everything, with a deep darkness falling off at the edges of the frame.",
           "缓慢的红色警报光脉动着漫过房间，给所有东西的边缘描上红边，画面四周落入深深的暗。")
AES_OPENGATE = ("A roaring cold blue-white wind blows swirling snow in through the huge open outer gate and across the dark steel floor, while the warm pink-violet glow of the farm lamps rim-lights the edge of the glass door in the foreground.",
                "呼啸的冷蓝白色风把旋转的雪从巨大的外闸门敞开的缺口灌进来，吹过黑色的钢板地面，前景玻璃门的边缘被农场温暖的粉紫色灯光描上一圈亮边。")
AES_CHARGE = ("Cold blue storm light streams through the open gate behind the charging bear, ice dust and snow explode off its armor in the air and glints of red light burn in its eyes.",
              "冷冷的蓝色风暴光从冲进来的巨熊身后的敞开闸门涌进来，冰尘和雪从它的冰甲上炸开在空气里，眼睛里燃着两点红光。")
AES_CRACK = ("Cold white light from the ceiling lamps floods the steel chamber and every crack in the glass catches it like a bright thread, while frost smokes off the bear's fur into the harsh light.",
             "天花板上的冷白灯光洒满钢铁舱室，玻璃上每一道裂纹都像亮亮的丝线接住光，熊毛上冒着的寒霜白烟飘进刺眼的灯光里。")
AES_LEVER = ("Warm pink-violet light from the grow lamps rim-lights Lin's hand and the red lever while a cold white glow from the chamber glass slides across the steel panel in a hard teal-and-orange contrast.",
             "农场植物灯温暖的粉紫色光给林峰的手和红色拉杆描上轮廓光，舱室玻璃里透出的冷白光从钢制控制盘上滑过，形成强烈的青橙对比。")
AES_NITRO = ("Dense white vapor boils out of four ceiling nozzles and rolls across the chamber in thick slow waves, ice crystals glittering in the cold light and a pale blue haze creeping across the glass.",
             "浓浓的白色蒸汽从四个顶喷头里涌出来，一波一波厚重缓慢地滚过整个舱室，冰晶在冷光里闪烁，一层淡淡的蓝色寒雾爬满玻璃。")
AES_ICEBEAR = ("Cold light from the ceiling lamps catches every ice-sheathed hair of the frozen bear and breaks into glittering white sparks, while a thin haze of vapor drifts and settles over the steel floor.",
               "天花板的冷光落在冻僵的巨熊每一根结满冰的毛上，碎成闪烁的白色光点，一层薄薄的蒸汽雾飘着，慢慢落在钢板地面上。")
AES_THAW = ("Drops of meltwater gleam along the ice-furred flank of the thawing bear and run in thin bright lines toward the drain, a faint mist rising into the warm pink-violet glow from the farm side.",
            "融化的水珠沿着正在解冻的巨熊结满冰的身侧闪着光，细细亮亮地淌向排水口，一缕淡淡的雾气升进农场一侧温暖的粉紫色光里。")
AES_LAB = ("Bright clean white light from hanging surgical lamps falls across the steel table and gleams along the long blade of the scalpel, with crisp soft shadows on the white tiles.",
           "悬挂的手术灯洁净明亮的白光洒在不锈钢台面上，沿着手术刀长长的刀刃闪光，白色瓷砖上落着清晰柔和的影子。")
AES_MEAT = ("Cold white light glitters on the frost that furs every white parcel on the steel shelves and a slow veil of cold breath drifts along the aisle in a soft teal haze.",
            "冷白色的光在钢架上每一个白色包裹结着的霜上闪烁，一层缓缓的冷气沿着走道飘着，泛起柔和的青色雾气。")
AES_STEAK = ("Orange firelight dances on the glistening steak, golden fat drips and flares into leaping flames, and thin silver smoke curls up into the warm amber glow of the room.",
             "橘色的火光在滋滋发亮的熊排上跳动，金黄的油脂滴下去，腾起窜高的火苗，一缕缕银色的细烟卷着升进房间温暖的琥珀色光里。")
AES_FEAST = ("Warm amber lamp light glows on the glistening steak and on their faces, steam curls from the plate and tiny flecks of black pepper and sea salt glitter on the meat.",
             "温暖的琥珀色灯光映在发亮的熊排和两个人的脸上，盘子里的热气卷着往上飘，肉上细细的黑胡椒和海盐闪着光。")
AES_SONAR = ("A cool teal glow from the sonar screen washes across the console and their faces while a small red lamp on the wall flashes softly and the rest of the room falls into deep shadow.",
             "声纳屏幕冷冷的青色光洗过控制台和两个人的脸，墙上的一盏小红灯轻轻闪着，房间其他地方落进深深的阴影里。")
AES_TUNNEL = ("Narrow white flashlight beams cut through the dark and light up drifting ice dust while the rough frozen walls glitter and a faint blue glow waits at the far end of the tunnel.",
              "窄窄的白色手电光束劈开黑暗，照亮飘着的冰尘，粗糙的冻土壁闪着光，隧道尽头一线淡淡的蓝光在等着。")
AES_MOSS = ("Soft blue light pours from the luminous moss on the walls and ceiling like a sky of stars, white mist rolls slowly off the turquoise water and the whole cavern glows with a deep teal-and-gold calm.",
            "柔和的蓝光从墙壁和洞顶发光的苔藓里洒下来，像一整片星空，白色的雾气慢慢从碧绿色的水面上翻起来，整座溶洞笼在深青色和金色交织的宁静里。")
AES_POOL = ("Warm steam rolls over the glowing turquoise water, ripples break the blue moss light into trembling threads and a few fine droplets hang and glitter in the mist.",
            "温暖的蒸汽滚过发光的碧绿色水面，涟漪把苔藓的蓝光揉成颤动的细线，几颗细小的水珠挂在雾里闪烁。")
AES_FISH = ("Clear warm water glows pale blue from the moss above, slow rings of light ripple across the pale bodies of the fish and tiny bubbles rise in thin silver threads.",
            "清澈温暖的水被上面的苔藓映着发出淡蓝色的光，一圈圈缓慢的光纹滑过苍白的鱼身，细小的气泡拉成细细的银线往上升。")
AES_REINF = ("Warm amber strip lights run along the steel arch ribs of the freshly braced passage and glow against the cold blue moss light at the far end, dust motes drifting through the beams.",
             "温暖的琥珀色灯带沿着刚加固好的通道里的钢拱肋亮着，和尽头冷冷的蓝色苔藓光对在一起，尘埃在光束里飘。")
AES_BATHE = ("Soft blue moss light and warm golden lamp glow meet over the rising steam, silver droplets bead on rock and robes, and a slow teal-and-orange glow rim-lights their faces.",
             "柔和的蓝色苔藓光和温暖的金色灯光在升起的蒸汽上方相遇，银色的水珠沾在岩石和浴袍上，一层缓缓的青橙色光给两个人的脸描上轮廓。")
AES_MUSH = ("Pale blue moss light and a thin drift of warm steam catch the tiny white mushroom caps, beads of water glisten on every cap and the dark logs glow with a soft emerald haze.",
            "淡蓝色的苔藓光和一缕缕温暖的蒸汽落在小小的白色菇帽上，每一顶菇帽上的水珠都闪着光，深色的木段笼着一层柔和的翡翠色雾。")
AES_SOUP = ("Warm firelight from the little brazier flickers on the rocks and the steaming soup while the turquoise pool glows pale blue beside them and thin steam curls up between the two lights.",
            "小火盆暖暖的火光在岩石和冒热气的鱼汤上跳动，旁边碧绿色的水池发着淡蓝色的光，薄薄的蒸汽在两种光之间卷着往上升。")
AES_ALARMLAMP = ("A hard red pulse flashes from the alarm lamp and slams across the dark console and walls in sharp waves, with the green indicator lights flickering underneath and deep black shadow filling the edges.",
                 "警报灯一下一下打出强烈的红光，一波一波撞过黑色的控制台和墙壁，下面绿色的指示灯在闪，画面四周落满深深的黑影。")
AES_CODE = ("Columns of bright green characters pour down the black screen in endless streams and wash a cold green glow over the console and their faces, with a deep red pulse from the alarm lamp behind them.",
            "一列列明亮的绿色字符在黑色的屏幕上不停地倾泻而下，把冷冷的绿光洗在控制台和两个人的脸上，身后警报灯打着深红色的脉动光。")
AES_STILL = ("A steady pale green glow fills the screen and lights Lin and Su from the front while the red alarm pulse drops away and the room holds a cold, dead silence.",
             "屏幕上一片稳稳的淡绿色光从正面照亮林峰和苏清月，红色警报的脉动光退了下去，房间里一片冰冷死寂。")

# ---------------------------------------------------------------------------------------------- 新外貌／声音／外观
SU_COAT = "in a crisp white lab coat over her black thermal top, white sterile gloves, thin gold-rimmed glasses on her nose, her long black hair pinned up, a surgical mask pulled down under her chin"
LIN_APRON = "in a charcoal henley with the sleeves rolled to his elbows and a heavy white plastic apron over it"
SU_SUIT = "in a white insulated polar suit with the collar zipped to her chin, a headlamp strapped over her black hair and the ponytail trailing behind"
LIN_SUIT = "in a white insulated polar suit with the collar zipped to his chin and a headlamp strapped over his black hair"
SU_ROBE = "in a thick white terry bathrobe tied at the waist, her long black hair loose and damp over her shoulders, her bare feet in the water"
LIN_ROBE = "in a thick grey terry bathrobe tied at the waist, his black hair damp, his bare feet in the water"
SU_PJ = "in a soft pale pink knit pajama set with the sleeves pushed up, her long black hair in a loose braid, thick white socks"
look('ghost_voice', 'Ghost', "a wide black console screen", 'none', 'its')
GHOST_EN = 'A flat, cold, androgynous synthetic voice from a console speaker, slow and unhurried, speaking clear Mandarin Chinese.' + VT_EN
GHOST_ZH = '平板冰冷、听不出男女的合成声音，从控制台扬声器里传出，缓慢不急，普通话清楚。' + VT_ZH

# ---------------------------------------------------------------------------------------------- 场景
EDEN_GLASS = Scene('eden', EDEN.end,
                   " Fixed stage layout: a thick armoured-glass door in a steel frame stands closed in the middle of the frame with a bare steel chamber beyond it whose huge outer gate is wide open on swirling snow; a steel control panel with a big red lever stands at frame-right; tiers of young lettuce and tomato seedlings under pink-violet grow lamps fill frame-left.")
EDEN_GLASS_BEAR = Scene('eden', EDEN.end,
                        " Fixed stage layout: a thick armoured-glass door in a steel frame stands closed in the middle of the frame; beyond it in the steel chamber a colossal armored polar bear stands on its hind legs with both paws slammed against the glass, a web of white cracks spreading across it; a steel control panel with a big red lever stands at frame-right; tiers of seedlings under pink-violet grow lamps fill frame-left.")
EDEN_GLASS_ICE = Scene('eden', EDEN.end,
                       " Fixed stage layout: a thick armoured-glass door in a steel frame, frosted and cracked, stands closed in the middle of the frame; beyond it in a drifting haze a colossal armored polar bear stands frozen mid-leap sheathed in glittering ice; a steel control panel with a big red lever stands at frame-right; tiers of seedlings under pink-violet grow lamps fill frame-left.")
EDEN_THAW = Scene('eden', EDEN.end,
                  " Fixed stage layout: the thick armoured-glass door stands wide open in the middle of the frame; beyond it in the steel chamber the huge frozen bulk of the bear fills the doorway with meltwater running down its flank toward a floor drain; tiers of seedlings under pink-violet grow lamps fill frame-left and frame-right.")
CH_OPEN = Scene('buffer_chamber', " Cold blue-white storm light and swirling snow pour into a bare steel chamber.",
                " Fixed stage layout: seen through a thick armoured-glass door in the foreground, a bare ten-square-metre steel chamber with four round spray nozzles in its ceiling and a floor drain; at its far end a huge outer alloy gate stands wide open on a black night of swirling blizzard, snow blowing across the steel floor.")
CH_RUSH = Scene('buffer_chamber', " Cold blue-white storm light and swirling snow pour into a bare steel chamber.",
                " Fixed stage layout: seen through a thick armoured-glass door in the foreground, the bare steel chamber with four round spray nozzles in its ceiling; the huge outer gate at the far end is open on the blizzard and a colossal four-metre polar bear covered in jagged plates of white ice armor with glowing red eyes charges across the steel floor toward the glass.")
CH_CRACK = Scene('buffer_chamber', " Hard cold white ceiling light fills a sealed steel chamber.",
                 " Fixed stage layout: seen from inside the chamber's far end, the colossal armored polar bear rears on its hind legs in the middle of the frame with both paws slammed flat against a thick armoured-glass door, a web of white cracks spreading across the glass; the huge outer gate behind the camera is shut; four round spray nozzles hang from the ceiling.")
CH_FOG = Scene('buffer_chamber', " Thick white vapor boils through the sealed steel chamber.",
               " Fixed stage layout: seen through a thick armoured-glass door in the foreground whose pane is beaded with frost, the sealed steel chamber is filled with dense rolling white vapor pouring from four ceiling nozzles; the dark silhouette of the bear shows faintly inside it.")
CH_ICE = Scene('buffer_chamber', " Cold light and a thin settling haze fill the sealed steel chamber.",
               " Fixed stage layout: seen through a thick frosted armoured-glass door in the foreground, the sealed steel chamber with a thin haze drifting over the floor; in the middle of the frame the colossal armored polar bear stands frozen mid-leap on its hind legs, front claws raised, every hair and ice plate sheathed in glittering white ice; four ceiling nozzles drip with ice.")
BUTCHER = Scene('butcher_room', " Bright clean white surgical light fills the white-tiled processing room.",
                " Fixed stage layout: a long stainless-steel table fills the middle of the frame with a large neatly trimmed dark-red cut of meat laid on a clean white cloth; a steel rolling cart with a stack of white-wrapped parcels stands at frame-right; a steel sink is at frame-left; white tiled walls and hanging surgical lamps fill the background.")
COLD_MEAT = Scene('cold_store', COLD.end,
                  " Fixed stage layout: steel shelving along both sides and the middle of the frame is stacked row on row with neatly wrapped white parcels of deep-red bear meat, every parcel furred with white frost and labelled with a small red tag; a heavy insulated door stands at frame-right.")
STOVE_STEAK = Scene('bunker_living', LIVING.end,
                    " Fixed stage layout: the black-and-gold stove fills the middle of the frame with a thick, marbled steak sizzling on a cast-iron grill rack over glowing coals, golden fat dripping and flames leaping; the thick cream wool rug lies in front of it and the wall of small security monitors glows far at frame-right.")
TABLE_STEAK = Scene('bunker_living', LIVING.end,
                    LIVING.layout + " On the small round wooden dining table stand a white plate of thick sliced steak seasoned with black pepper and sea salt, two forks and a small bowl of coarse salt.")
SONAR = Scene('bunker_control', CONTROL.end,
              CONTROL.layout + " A wide dark sonar screen on the console shows a pale-blue cross-section with a large dark empty round cavity behind a thin line of frozen soil. A black swivel chair stands in front of the console.")
TUNNEL = Scene('dug_tunnel', " Pitch dark frozen air and glittering ice dust fill the rough clawed tunnel.",
               " Fixed stage layout: a rough round tunnel clawed through frozen soil and ice recedes down the middle of the frame into darkness, deep claw gouges scored across its glittering frost-furred walls, a faint blue glow far at its end.")
HC_WIDE = Scene('hot_cave', " Soft blue moss light and rolling white mist fill a vast natural cavern.",
                " Fixed stage layout: a vast natural cavern with walls and ceiling of dark rock thickly covered in softly glowing blue moss like a night sky; a steaming turquoise hot spring pool fills the middle of the frame with white mist rolling off it; smooth rock shelves line its edge; a narrow dark tunnel mouth is at frame-left.")
HC_MOUTH = Scene('hot_cave', HC_WIDE.end,
                 " Fixed stage layout: the rough dark tunnel mouth fills frame-left in the foreground; beyond it the vast glowing cavern opens, a steaming turquoise hot spring pool in the middle distance under walls of softly glowing blue moss and rolling white mist.")
HC_POOL = Scene('hot_cave', HC_WIDE.end,
                " Fixed stage layout: the turquoise water of the steaming hot spring fills the middle of the frame with slow ripples and white steam rolling over it; smooth dark rocks edge the water at the bottom of the frame and glowing blue moss shows at the top.")
HC_FISH = Scene('hot_cave', HC_WIDE.end,
                " Fixed stage layout: seen from just above the waterline, clear warm turquoise water fills the frame with three pale eyeless white fish gliding slowly through it; a smooth dark rock edge is at the bottom of the frame and blue moss glows above.")
HC_REINF = Scene('dug_tunnel', " Warm amber strip lights and cold blue moss light meet in a freshly braced passage.",
                 " Fixed stage layout: the passage now lined with steel arch ribs and strips of warm amber lamps recedes down the middle of the frame toward the glowing blue cavern at its end; a small yellow compact tracked utility machine is parked against the left wall.")
HC_EDGE = Scene('hot_cave', HC_WIDE.end,
                " Fixed stage layout: a smooth flat rock ledge at the edge of the steaming turquoise hot spring fills the bottom and middle of the frame; the pool with rolling white mist is behind it; walls of softly glowing blue moss rise at the back of the frame.")
HC_SOUP = Scene('hot_cave', HC_WIDE.end,
                " Fixed stage layout: a smooth flat rock ledge at the pool's edge fills the middle of the frame with a small wooden bowl of crumbs near its lip; at frame-right a small cast-iron brazier with glowing charcoal holds a black iron pot of milky fish soup steaming; the turquoise pool is at frame-left and glowing blue moss covers the wall behind.")
HC_MUSH = Scene('hot_cave', HC_WIDE.end,
                " Fixed stage layout: a row of dark damp logs lies along the cavern edge in the middle of the frame, each log sprouting clusters of small white mushroom caps; the steaming turquoise pool is in the soft background and glowing blue moss covers the wall behind.")
CTRL_ALARM = Scene('bunker_control', " Pulsing red alarm light and cool green indicator glow fill the compact underground control room.",
                   " Fixed stage layout: the steel control console with rows of small status lights stands in the middle of the frame; a round red alarm lamp mounted high on the back wall at center-right flashes bright red; a wall of six small monitors is at frame-left; a heavy steel door stands in the right wall at frame-right; nobody is in the room.")
CTRL_HACK = Scene('bunker_control', CONTROL.end,
                  CONTROL.layout + " A wide black screen on the console streams dense columns of unreadable green characters, a round red alarm lamp flashes high on the wall above it, and a black swivel chair stands in front of the console.")
CODE_CLOSE = Scene('bunker_control', CONTROL.end,
                   " Fixed stage layout: a wide black screen fills the middle of the frame streaming dense columns of tiny unreadable green characters downward, its steel console edge at the bottom of the frame and a flashing round red alarm lamp glowing out of focus above it.")
CTRL_STILL = Scene('bunker_control', CONTROL.end,
                   CONTROL.layout + " A wide black screen on the console glows a steady pale green with every column of characters frozen still, a round red alarm lamp dark on the wall above it, and a black swivel chair stands in front of the console.")

# ---------------------------------------------------------------------------------------------- 声音
SOUND_GATEOPEN = breathy('A roaring howl of wind pouring through a huge open gate and the rattle of blown snow across a steel floor.', '风呼啸着从一扇巨大的敞开的闸门灌进来的声音和被吹起来的雪在钢板地面上沙沙滚过的声音。')
SOUND_PANEL = voiced('A deep low howl of wind beyond thick glass, the soft hum of grow lamps and the faint creak of a steel lever.', '厚玻璃外风深沉的低啸、植物灯轻轻的嗡鸣和钢制拉杆细细的吱呀声。')
SOUND_BEARRUSH = breathy('A deafening animal roar, heavy thundering paws on steel and the hiss of blown snow.', '震耳欲聋的野兽咆哮、沉重的熊掌踏在钢板上的轰响和被吹起来的雪嘶嘶的声音。')
SOUND_GLASSHIT = breathy('A heavy dull slam against thick glass, the sharp crackle of spreading cracks and a furious growl.', '一声沉重的闷响撞在厚玻璃上、裂纹蔓延时尖脆的噼啪声和一声愤怒的低吼。')
SOUND_LEVER = voiced('A hard metallic clunk of a lever dropping and a rising hiss of gas beyond the glass.', '拉杆往下一拉时一声硬朗的金属撞响和玻璃外越来越响的气体嘶嘶声。')
SOUND_NITRO = breathy('A thunderous hiss of vapor, a short choked animal roar cut dead and the sharp crackle of ice forming.', '蒸汽雷鸣般的嘶吼、一声被掐断的短促的野兽吼叫和冰层冻结时尖脆的噼啪声。')
SOUND_ICEDROP = breathy('A deep hush, the faint tick of ice settling and the soft drip of frozen nozzles.', '深深的寂静、冰层沉降时细细的嘀嗒声和冻住的喷头轻轻的滴水声。')
SOUND_ICEQUIP = voiced('A deep hush, the faint tick of ice settling and the soft hum of grow lamps.', '深深的寂静、冰层沉降时细细的嘀嗒声和植物灯轻轻的嗡鸣。')
SOUND_THAWDRIP = voiced('The steady drip and trickle of meltwater and the soft hum of grow lamps.', '融冰的水不断滴落、淌下去的声音和植物灯轻轻的嗡鸣。')
SOUND_LAB = voiced('The soft rasp of a sharp blade through meat and the quiet hum of surgical lamps.', '锋利的刀刃轻轻划过肉的沙沙声和手术灯安静的嗡鸣。')
SOUND_COLDMEAT = breathy('The low hum of a refrigeration compressor and the faint tick of frost.', '制冷压缩机低低的嗡鸣和霜细细的嘀嗒声。')
SOUND_SIZZLE = breathy('The loud crackling sizzle of fat on hot iron and the roar of leaping flames.', '油脂落在烧热的铁网上噼里啪啦的滋滋声和火苗窜高时的呼呼声。')
SOUND_FEAST = voiced('The soft clink of a fork on a plate and the gentle crackle of the stove.', '叉子在盘子上轻轻的碰响和炉子温和的噼啪声。')
SOUND_ALARMSOFT = breathy('A single sharp electronic alarm beep and the soft clink of a plate set down.', '一声尖锐的电子警报声和一只盘子被轻轻放下的碰响。')
SOUND_SONAR = voiced('A slow rhythmic sonar ping, a faint electronic hum and a dull far-off thud.', '缓慢有节奏的声纳嘀声、细细的电子嗡鸣和远处一声钝钝的闷响。')
SOUND_TUNNEL = breathy('Soft footsteps crunching on frozen ground, the low echo of a long tunnel and slow breath.', '脚步踩在冻土上的嘎吱声、长长的隧道里低低的回响和缓慢的呼吸。')
SOUND_CAVE = breathy('A deep soft hush, the gentle bubbling of hot water and a faint far drip echoing.', '深深柔和的寂静、热水轻轻的咕嘟声和远处一滴水落下的回响。')
SOUND_CAVE_V = voiced('A deep soft hush, the gentle bubbling of hot water and a faint far drip echoing.', '深深柔和的寂静、热水轻轻的咕嘟声和远处一滴水落下的回响。')
SOUND_FISH = breathy('The soft ripple of water and faint bubbles rising.', '水轻轻的涟漪声和细小气泡升起的声音。')
SOUND_REINF = breathy('The low hum of strip lights and the faint echo of a small engine ticking as it cools.', '灯带低低的嗡鸣和一台小发动机冷却时细细的嘀嗒回响。')
SOUND_BATHE = voiced('The gentle bubbling of hot water, a soft drift of water droplets and a faint far drip echoing.', '热水轻轻的咕嘟声、水珠轻轻滴落的声音和远处一滴水落下的回响。')
SOUND_SOUP = voiced('The soft bubbling of a pot, the gentle crackle of charcoal and the quiet ripple of water.', '锅里轻轻的咕嘟声、炭火温和的噼啪声和水安静的涟漪声。')
SOUND_ALARMBIG = breathy('A sharp repeating electronic alarm beep and the dull hum of a computer.', '尖锐反复的电子警报声和电脑低沉的嗡鸣。')
SOUND_KEYS = voiced('A sharp repeating electronic alarm beep and the rapid clatter of a keyboard.', '尖锐反复的电子警报声和键盘急促的敲击声。')
SOUND_CODE = breathy('A fast whispering patter of data, a sharp repeating alarm beep and the hum of a computer.', '数据飞快窸窣的声音、尖锐反复的警报声和电脑的嗡鸣。')
SOUND_GHOST = voiced('A sudden dead silence, the faint hum of a speaker and a low crackle of static.', '突然降临的死寂、扬声器细细的嗡鸣和低低的电流杂音。')

# ================================================================================================ 第 37 集
b37 = S.episode('剧本第37集｜请君入瓮', '林峰解锁废料缓冲舱外侧的合金闸门，零下八十度的风雪灌进钢铁舱室；他和苏清月站在农场尽头内侧的防爆玻璃门后，林峰握着红色拉杆说再等等让它进来；浑身长满白色冰甲的巨熊嘶吼着像重型坦克一样冲进舱室，它刚进舱，外侧闸门就锁死了；巨熊被困在不到十平米的钢铁盒子里，疯狂拍打内侧玻璃，玻璃出现蜘蛛网一样的裂纹；林峰冰冷地说一句晚安大家伙，拉下红色拉杆；舱顶四个喷头喷出浓浓的白色液氮雾，把整个舱室吞没，巨熊的吼声被截断；雾气散去，巨熊保持着扑击的姿势冻成了冰雕；林峰转头对苏清月说该你上手术台了，苏医生，画面黑屏。', 37)
new_scene(b37, 'buffer_chamber', '废料缓冲舱（不到十平米的光秃秃的钢铁舱室，天花板上四个圆形喷头，地上一个排水口，远端是一扇巨大的外侧合金闸门，内侧是一扇厚厚的防爆玻璃门）',
          'A bare steel waste buffer chamber of about ten square metres with four round spray nozzles in the ceiling, a floor drain, a huge outer alloy gate at its far end and a thick armoured-glass door on the inner side.',
          '一间不到十平米的光秃秃的钢铁废料缓冲舱，天花板上四个圆形喷头，地上一个排水口，远端是一扇巨大的外侧合金闸门，内侧是一扇厚厚的防爆玻璃门。',
          'the bare steel chamber, its four ceiling nozzles, the floor drain and the huge outer gate')
b37.prop('mutant_bear', '变异巨熊（体长四米的北极熊，浑身长满一块块白色的锯齿状冰甲，眼睛是猩红色，爪子巨大，毛上冒着寒霜）',
         'A colossal four-metre mutated polar bear covered in thick jagged plates of white ice armor over its shoulders and back, glowing red eyes, huge claws and frost smoking from its fur. The reference fixes its look.',
         '一头体长四米的变异北极熊，肩背上长满一块块厚厚的白色锯齿状冰甲，眼睛猩红发光，爪子巨大，毛上冒着寒霜。参考图固定它的外形。',
         'A photorealistic shot of a colossal four-metre mutated polar bear covered in thick jagged plates of white ice armor over its shoulders and back, glowing red eyes, huge claws and frost smoking from its fur, standing on all fours in a three-quarter view against a plain dark background.')

insert2('37-01', '01｜缓冲舱：外侧的合金闸门已经完全敞开，风雪呼啸着灌进光秃秃的钢铁舱室，雪在地面上打着旋', 6, CH_OPEN,
        'Wide shot through the glass door, the open outer gate in the middle third of the frame, nobody visible.',
        "Seen through the thick glass door, the huge outer gate of the bare steel chamber stands wide open on the black night and the blizzard pours in, swirling snow racing across the steel floor and piling against the walls. Nothing else moves.",
        "透过厚厚的玻璃门，光秃秃的钢铁舱室里那扇巨大的外侧闸门完全敞开着，外面是漆黑的夜，暴风雪灌进来，旋转的雪在钢板地面上飞快地滑过，堆在墙边。别的什么都不动。",
        SOUND_GATEOPEN, 'The frame holds the open steel chamber seen through the glass, and nobody visible.',
        lowrise('the open gate and the snow-swept chamber', '敞开的闸门和被风雪扫过的舱室'), AES_OPENGATE)

TA('37-02', '02｜农场尽头：林峰握着红色拉杆，两眼盯着玻璃门后面敞开的舱室，低声说再等等，让它进来，苏清月握着匕首站在他身边', 8, EDEN_GLASS,
   [P('su_surgeon', 'left', "standing at the armoured-glass door in profile facing frame-right, a slim tactical dagger gripped low at her side, her eyes on the open chamber beyond the glass", 'obj:the open chamber beyond the glass door', "her lips pressed pale, her eyes wide, her brows pulled together"),
    P('lin_work', 'right', "standing at the steel control panel in profile facing frame-left, his right hand resting on the big red lever, his eyes on the chamber", 'obj:the open chamber beyond the glass door', "his jaw tight, his eyes cold and narrowed, his brows low", outfit="in a charcoal henley under a dark olive utility vest")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the glass door.',
   "<lin_work> keeps his right hand on the red lever and speaks the one line to <su_surgeon> in a low, calm, deadly voice, his jaw tight, his eyes cold and narrowed and his brows low, while <su_surgeon> stands rigid with the dagger low beside her, her lips pressed pale, her eyes wide on the glass and her brows pulled together.",
   "林峰右手握着红色拉杆，用低沉平稳、杀气腾腾的声音对苏清月说出这一句，下颌绷紧、眼睛冰冷眯起、眉头压低，苏清月僵直地站着，匕首垂在身旁，嘴唇发白抿着、眼睛睁大盯着玻璃、眉头拧在一起。",
   SOUND_PANEL, AES_LEVER, lines=[('lin_work', "再等等，让它进来。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Beyond the glass door the open steel chamber glows cold blue with swirling snow and tiers of seedlings glow pink-violet at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, at the glass door, nobody else.')

insert2('37-03', '03｜缓冲舱：浑身白色冰甲、眼睛猩红的变异巨熊从敞开的闸门口冲进来，爪子踏得钢板轰响，直冲向玻璃门', 6, CH_RUSH,
        'Wide shot through the glass door, the charging bear in the middle third of the frame, nobody else visible.',
        "A colossal four-metre armored polar bear charges in through the open outer gate and across the bare steel floor toward the glass with a deafening roar, ice dust and snow bursting off its armor, and nothing else moves in the chamber.",
        "一头体长四米、浑身白色冰甲的巨熊从敞开的外闸门冲进来，咆哮着直冲过光秃秃的钢板地面扑向玻璃，冰尘和雪从冰甲上炸开，舱里别的什么都不动。",
        SOUND_BEARRUSH, 'The frame holds the steel chamber with the charging armored bear, and nobody else visible.',
        push1('the charging bear', '冲过来的巨熊'), AES_CHARGE, extra_assets=('mutant_bear',))

insert2('37-04', '04｜缓冲舱：外侧闸门已经关死，巨熊被困在钢铁盒子里，人立起来两只巨掌拍在防爆玻璃上，玻璃上蔓开一片白色的蜘蛛网裂纹', 6, CH_CRACK,
        'Medium shot from inside the chamber, the rearing bear and the cracked glass in the middle third of the frame, nobody else visible.',
        "The outer gate is sealed shut and the colossal armored polar bear stands rearing on its hind legs with both huge paws slammed flat against the thick glass door, a web of white cracks spreading slowly across the pane while frost smokes off its fur. Nothing else moves.",
        "外侧闸门已经关死，巨大的冰甲巨熊两条后腿立起来，两只巨掌死死按在厚厚的玻璃门上，一片白色的蜘蛛网裂纹慢慢蔓开，熊毛上冒着寒霜白烟。别的什么都不动。",
        SOUND_GLASSHIT, 'The frame holds the rearing armored bear and the cracked glass door, and nobody else visible.',
        push1('the bear\'s face and paws against the cracked glass', '贴在裂开的玻璃上的熊脸和熊掌'), AES_CRACK, extra_assets=('mutant_bear',))

TAV('37-05', '05｜农场尽头：隔着满是裂纹的玻璃，林峰盯着人立的巨熊，冷冷地说晚安，大家伙，右手把红色拉杆一把拉到底', EDEN_GLASS_BEAR,
   [P('lin_work', 'right', "standing at the steel control panel in profile facing frame-left, his right hand gripping the big red lever and pulling it down, his eyes on the bear beyond the cracked glass", 'obj:the bear beyond the cracked glass door', "his eyes cold and narrowed, one corner of his mouth lifting coldly, his brows low", outfit="in a charcoal henley under a dark olive utility vest"),
    P('su_surgeon', 'left', "standing a step back from the glass in profile facing frame-right, the dagger gripped at her side, her eyes on the bear", 'obj:the bear beyond the cracked glass door', "her face pale, her lips parted, her brows pulled high")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the glass door.',
   "<lin_work> speaks the one line aloud to himself, looking at the bear, in a low, cold, whispering voice, his eyes cold and narrowed, one corner of his mouth lifting coldly and his brows low, and pulls the red lever down hard in his right hand. <su_surgeon> stands a step back from the cracking glass, her face pale, her lips parted and her brows pulled high.",
   "林峰用低沉冰冷的气声对着巨熊说出这一句，眼睛冰冷眯起、嘴角冷冷一挑、眉头压低，右手把红色拉杆用力拉下去。苏清月站在裂开的玻璃后面一步，脸色发白、嘴唇微张、眉毛高高挑起。",
   SOUND_LEVER, AES_LEVER, [('lin_work', "晚安，大家伙。", 0.8, 'Lin')],
   cam=push('both of them', '两人'), extra_assets=('mutant_bear',), room={'Su', 'Lin'}, new=True,
   bg='Beyond the cracked glass door the colossal armored bear rears against the glass in the cold white chamber light and tiers of seedlings glow pink-violet at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, at the glass door, nobody else.')

insert2('37-06', '06｜缓冲舱：舱顶四个喷头喷出浓浓的白色蒸汽，一波一波滚过整个钢铁舱室，玻璃上一层淡蓝色的寒霜爬满，里面巨熊的黑影一点点模糊', 7, CH_FOG,
        'Close shot of the frosting glass door, the white vapor in the middle third of the frame, nobody visible.',
        "Dense white vapor pours from four ceiling nozzles and rolls in thick slow waves through the sealed steel chamber while a pale blue frost creeps across the pane of the glass door and the dark silhouette of the bear inside fades slowly into the white. Nothing else moves.",
        "浓浓的白色蒸汽从四个顶喷头里涌出来，厚重缓慢地一波一波滚过封死的钢铁舱室，淡蓝色的寒霜爬满玻璃门，里面巨熊的黑影慢慢淡进白色里。别的什么都不动。",
        SOUND_NITRO, 'The frame holds the frosting glass door with the rolling white vapor, and nobody visible.',
        push1('the frosting glass and the white vapor beyond', '结霜的玻璃和后面翻滚的白色蒸汽'), AES_NITRO, extra_assets=('mutant_bear',))

insert2('37-07', '07｜缓冲舱：白雾慢慢散开，巨熊保持着人立扑击的姿势，从毛到冰甲全都包着一层闪着光的白冰，僵在舱室中央，一动不动', 7, CH_ICE,
        'Medium shot through the frosted glass, the frozen bear in the middle third of the frame, nobody visible.',
        "The haze thins slowly and the colossal armored polar bear stands frozen mid-leap on its hind legs with its claws raised, every hair and ice plate sheathed in glittering white ice, motionless in the middle of the sealed steel chamber while ice drips from the nozzles. Nothing else moves.",
        "白雾慢慢变薄，巨大的冰甲巨熊保持着人立扑击的姿势，利爪高举，从毛到冰甲全都包着一层闪光的白冰，一动不动地僵在封死的钢铁舱室中央，喷头上挂着的冰一滴滴往下滴。别的什么都不动。",
        SOUND_ICEDROP, 'The frame holds the frozen bear in the steel chamber, and nobody visible.',
        pull('the glittering ice on the bear\'s raised claws', '熊高举的利爪上闪光的冰', 'the whole frozen bear in the steel chamber', '整头冻僵的巨熊和钢铁舱室'), AES_ICEBEAR, extra_assets=('mutant_bear',))

TA('37-08', '08｜农场尽头：林峰转过头，对苏清月冷冷地说该你上手术台了，苏医生，嘴角挑起一丝笑意，苏清月看着冰雕，眼睛亮起来', 8, EDEN_GLASS_ICE,
   [P('lin_work', 'right', "standing at the steel control panel in profile facing frame-left, his head turned from the glass to her, his hand still resting on the red lever", 'Su', "one corner of his mouth lifting in a cool smug smile, his eyes dark and sure, his brows lifted", outfit="in a charcoal henley under a dark olive utility vest"),
    P('su_surgeon', 'left', "standing at the frosted glass door in profile facing frame-right, the dagger lowered at her side, her eyes on the frozen bear beyond the glass", 'obj:the frozen bear beyond the glass door', "her eyes shining, her lips parting in a thin eager line, her brows lifted")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the glass door.',
   "<lin_work> turns his head to <su_surgeon> and speaks the one line to <su_surgeon> in a low, amused, velvety voice, one corner of his mouth lifting in a cool smug smile, his eyes dark and sure and his brows lifted. <su_surgeon> keeps her eyes on the frozen bear beyond the glass, her eyes shining, her lips parting in a thin eager line and her brows lifted.",
   "林峰把头转向苏清月，用低沉带笑、丝绒般的声音对她说出这一句，嘴角挑起一丝冷冷得意的笑、眼神又黑又笃定、眉毛上扬。苏清月的眼睛还停在玻璃后面冻僵的巨熊上，眼睛发亮、嘴唇微张成一条急切的细线、眉毛上扬。",
   SOUND_ICEQUIP, AES_ICEBEAR, lines=[('lin_work', "该你上手术台了，苏医生。", 0.8, 'Su')],
   cam=push('both of them', '两人'), extra_assets=('mutant_bear',), room={'Su', 'Lin'}, new=True,
   bg='Beyond the frosted glass door the frozen bear stands sheathed in glittering ice in a thin drifting haze and tiers of seedlings glow pink-violet at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, at the glass door, nobody else.')

# ================================================================================================ 第 38 集
b38 = S.episode('剧本第38集｜顶级医生的“解剖学”', '缓冲舱里温度恢复，巨熊身上的冰开始融化，苏清月穿着白大褂、戴着无菌手套站在敞开的玻璃门口，眼睛里闪着顶级外科医生见到完美标本的兴奋，说完美的标本；处理间里她拿着长长的手术刀，一块块修剪整齐的深红色熊肉被切下来，林峰把包好的肉块搬上推车，她说人也好，熊也好，都是解剖学；冷库里一排排结着白霜的包裹码得整整齐齐；回到温暖的家里，铁网上一块厚厚的熊排滋滋冒油，油滴下去火苗窜高；林峰撒上黑胡椒和海盐，切一块喂到苏清月嘴边，说尝尝，苏清月咬了一口，说好香，全身都暖了；就在两人享受这顿奢侈的大餐时，墙上的警报灯轻轻闪了一下；林峰皱眉，调出声纳图，说冻土层后面，竟然是空的。', 38)
new_scene(b38, 'butcher_room', '处理间（白色瓷砖墙的明亮房间，中间一张长长的不锈钢台，右边一辆钢制推车，左边一个钢水槽，头顶悬着手术灯）',
          'A bright white-tiled processing room with a long stainless-steel table in the middle, a steel rolling cart at frame-right, a steel sink at frame-left and hanging surgical lamps.',
          '一间明亮的白色瓷砖墙处理间，中间是一张长长的不锈钢台，右边是一辆钢制推车，左边是一个钢水槽，头顶悬着手术灯。',
          'the long steel table, the rolling cart, the sink and the white tiles')

TA('38-01', '01｜缓冲舱门口：巨熊身上的冰在融化，水一道道淌向排水口，苏清月穿着白大褂站在敞开的玻璃门口，眼睛发亮地说完美的标本，林峰站在她身后', 7, EDEN_THAW,
   [P('su_surgeon', 'left', "standing in the open glass doorway in profile facing frame-right, a long slim scalpel held upright in her gloved right hand, her eyes on the thawing bear", 'obj:the thawing bear in the doorway', "her eyes shining with eager delight, her lips curving in a thin eager line, her brows lifted", outfit=SU_COAT),
    P('lin_work', 'right', "standing a step behind her in profile facing frame-left, his arms folded, his eyes on the bear", 'obj:the thawing bear in the doorway', "his lips twitching in dry amusement, his brows lifted", outfit="in a charcoal henley under a dark olive utility vest")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the open glass doorway.',
   "<su_surgeon> gazes at the thawing bear and speaks the one line to <lin_work> in a low, delighted, breathy voice, her eyes shining with eager delight, her lips curving in a thin eager line and her brows lifted, while <lin_work> stands behind her with his arms folded, his lips twitching in dry amusement and his brows lifted, and meltwater trickles down the bear's flank.",
   "苏清月看着正在解冻的巨熊，用低低的、又惊又喜的气声对林峰说出这一句，眼睛发亮、嘴唇弯成一条急切的细线、眉毛上扬，林峰抱着手臂站在她身后，嘴角忍着干干的笑意、眉毛上扬，熊身侧的融冰水一道道往下淌。",
   SOUND_THAWDRIP, AES_THAW, lines=[('su_surgeon', "完美的标本。", 0.8, 'Lin')],
   cam=push('both of them', '两人'), extra_assets=('mutant_bear',), room={'Su', 'Lin'}, new=True,
   bg='Beyond the open glass door the huge bulk of the thawing bear fills the chamber with meltwater running toward the floor drain and tiers of seedlings glow pink-violet behind the camera.',
   holds='The frame holds exactly two people: Su and Lin, in the open doorway, nobody else.')

TA('38-02', '02｜处理间：苏清月握着长长的手术刀，在不锈钢台上把一大块深红色的肉切成整齐的几块，一边说人也好，熊也好，都是解剖学，林峰把包好的肉块搬上推车', 8, BUTCHER,
   [P('su_surgeon', 'left', "standing at the stainless-steel table in profile facing frame-right, slicing a large dark-red cut of meat with a long scalpel in her gloved right hand, her head bent over her work", 'obj:the cut of meat on the steel table', "her eyes bright and focused, her lips set in a thin satisfied line, her brows lifted", outfit=SU_COAT),
    P('lin_work', 'right', "standing at the rolling cart in profile facing frame-left, lifting a white-wrapped parcel onto the stack on the cart, his eyes on her", 'Su', "his lips twitching in dry amusement, his jaw relaxed, his brows lifted", outfit=LIN_APRON)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the processing room.',
   "<su_surgeon> slices the dark-red meat with clean steady strokes and speaks the one line to <lin_work> in a crisp, cool, proud voice, her eyes bright and focused, her lips set in a thin satisfied line and her brows lifted, while <lin_work> lifts a white-wrapped parcel onto the cart and listens, his lips twitching in dry amusement, his jaw relaxed and his brows lifted.",
   "苏清月用稳稳干净的几刀切着深红色的肉，同时用干脆冷静又带点骄傲的声音对林峰说出这一句，眼神明亮专注、嘴唇抿成满足的一条细线、眉毛上扬，林峰把一块包好的白色肉块搬上推车，听着，嘴角忍着干干的笑意、下颌放松、眉毛上扬。",
   SOUND_LAB, AES_LAB, lines=[('su_surgeon', "人也好，熊也好，都是解剖学。", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them white tiled walls gleam under the hanging surgical lamps and a steel sink stands at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, in the processing room, nobody else.')

insert2('38-03', '03｜冷库：钢架上一排排包得整整齐齐的白色肉块，每一包都结着白霜，贴着小红标签，冷气在走道里轻轻飘', 5, COLD_MEAT,
        'Low wide shot of the cold store, the shelves in the middle third of the frame, nobody visible.',
        "Row after row of neatly wrapped white parcels of deep-red meat furred with white frost line the steel shelves, each with a small red tag, and a veil of cold breath drifts slowly along the aisle. Nothing else moves.",
        "钢架上一排又一排包得整整齐齐的白色肉块结着白霜，每一包都贴着小红标签，一层冷气沿着走道慢慢飘着。别的什么都不动。",
        SOUND_COLDMEAT, 'The frame holds the steel shelves of frosted parcels, and nobody visible.',
        lowrise('the rows of frosted parcels', '一排排结霜的肉块包裹'), AES_MEAT)

insert2('38-04', '04｜家里：黑金色炉子上，一块厚厚的、雪花纹理漂亮的熊排在铁网上滋滋冒油，油滴进炭火里，火苗一下窜高', 6, STOVE_STEAK,
        'Close shot of the steak on the grill, the steak in the middle third of the frame, nobody visible.',
        "A thick, beautifully marbled steak sizzles on the cast-iron grill rack over glowing coals, golden fat beading on its surface and dripping into the coals so the flames leap up around it. Nothing else moves.",
        "一块厚厚的、雪花纹理极漂亮的熊排在铁网上滋滋作响，金黄的油珠在肉面上冒出来，滴进炭火里，火苗一下窜高包住肉。别的什么都不动。",
        SOUND_SIZZLE, 'The frame holds the sizzling steak on the stove, and nobody visible.',
        pull('the sizzling steak and the leaping flames', '滋滋冒油的熊排和窜高的火苗', 'the whole stove and the cozy room around it', '整个炉子和周围温暖的房间'), AES_STEAK)

TA('38-05', '05｜家里：林峰撒上黑胡椒和海盐，把切成小块的熊排用叉子送到苏清月嘴边，说尝尝，苏清月咬了一口，闭上眼睛说好香，全身都暖了', 10, TABLE_STEAK,
   [P('lin_home', 'right', "standing beside the dining table in profile facing frame-left, holding a fork with a bite-sized piece of steak out toward her lips", 'Su', "his eyes soft and expectant, a warm soft curve at one corner of his mouth, his brows lifted", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'left', "sitting on a wooden chair at the table in profile facing frame-right, her lips parting to take the bite from the fork, her hands resting in her lap", 'obj:the fork in his hand', "her eyes warm and eager, her brows soft")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dining table.',
   "<lin_home> holds the fork toward <su_cozy> and speaks the first line to <su_cozy> in a low, warm voice, his eyes soft and expectant and his brows lifted, then <su_cozy> takes the bite, chews and closes her eyes in bliss, her brows soft, and speaks the second line to <lin_home> in a soft, contented voice with a blissful sweet smile.",
   "林峰把叉子递到苏清月嘴边，用低沉温暖的声音对她说出第一句，眼神柔软期待、眉毛上扬，然后苏清月咬下那一口，嚼着，幸福地闭上眼睛、眉毛舒展，用柔软满足的声音对林峰说出第二句，嘴角带着幸福的甜笑。",
   SOUND_FEAST, AES_FEAST, lines=[('lin_home', "尝尝。", 0.8, 'Su'), ('su_cozy', "好香，全身都暖了。", 4.2, 'Lin')],
   cam=push('both of them', '两人'), extra_assets=(), room={'Su', 'Lin'}, new=True,
   bg='On the table a white plate of sliced steak glistens with black pepper and sea salt and the black-and-gold stove glows warm at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, at the dining table, nobody else.')

TA('38-06', '06｜家里：两人坐在厚厚的羊毛地毯上吃着，墙上的红色警报灯忽然轻轻闪了一下，两个人同时抬头看向它，动作全停住了', 6, ALARM_WALL,
   [P('su_cozy', 'left', "sitting cross-legged on the cream rug in profile facing frame-right, a plate in her lap and a fork frozen in her hand, her eyes on the small red lamp", 'obj:the small red alarm lamp on the wall', "her lips parting, her eyes wide, her brows pulled together"),
    P('lin_home', 'center-right', "sitting on the rug in profile facing frame-right, one hand holding a plate and the other frozen halfway to his mouth, his eyes on the small red lamp", 'obj:the small red alarm lamp on the wall', "his jaw tight, his eyes sharp, his brows low", outfit="in a soft grey henley and dark lounge pants")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, on the rug.',
   "A small red lamp on the wall flashes once with a single sharp beep while <su_cozy> and <lin_home> sit frozen on the rug looking up at it, <su_cozy> with her lips parting, her eyes wide and her brows pulled together, and <lin_home> with his jaw tight, his eyes sharp and his brows low. Nobody speaks.",
   "墙上的一盏小红灯闪了一下，响了一声尖锐的警报，苏清月和林峰僵坐在地毯上抬头看着它，她嘴唇微张、眼睛睁大、眉头拧在一起，他下颌绷紧、眼神锐利、眉头压低。没有人说话。",
   SOUND_ALARMSOFT, AES_RED, cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Beside them the black-and-gold stove glows warm at frame-left and a wall of small security monitors glows cool blue at frame-center-right.',
   holds='The frame holds exactly two people: Su and Lin, on the rug, nobody else.')

TA('38-07', '07｜控制室：林峰坐在转椅里调出声纳图，屏幕上冻土层后面一个巨大的圆形空洞，他低声说冻土层后面，竟然是空的，苏清月站在他身后', 8, SONAR,
   [P('lin_home', 'right', "sitting in the black swivel chair at the console in profile facing frame-left, one hand on the keyboard, his eyes on the sonar screen", 'obj:the wide dark sonar screen', "his eyes sharp and wide, his jaw tight, his brows lifted", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'center', "standing behind his chair in profile facing frame-left, one hand on the chair back, her eyes on the sonar screen", 'obj:the wide dark sonar screen', "her lips parted, her eyes wide, her brows pulled together")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "<lin_home> studies the sonar screen and speaks the one line to <su_cozy> in a low, incredulous voice, his eyes sharp and wide, his jaw tight and his brows lifted, while <su_cozy> leans in close behind his chair, her lips parted, her eyes wide and her brows pulled together, and the pale-blue sonar map glows between them.",
   "林峰盯着声纳屏幕，用低低的难以置信的声音对苏清月说出这一句，眼睛锐利睁大、下颌绷紧、眉毛上扬，苏清月俯在他肩后，嘴唇微张、眼睛睁大、眉头拧在一起，淡蓝色的声纳图在两人之间发着光。",
   SOUND_SONAR, AES_SONAR, lines=[('lin_home', "冻土层后面，竟然是空的？", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the wall of six small monitors glows at frame-left and a small red lamp flashes softly on the wall.',
   holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

# ================================================================================================ 第 39 集
b39 = S.episode('剧本第39集｜地底的自然奇迹', '林峰和苏清月穿上白色防寒服，戴着头灯，顺着巨熊挖出来的那条地洞往外探索，走了十几米，眼前豁然开朗；头灯的光照亮了一座巨大的天然溶洞，洞壁上长满发着幽蓝色微光的苔藓，像一整片星空，洞中央是一汪冒着热气的碧绿色天然温泉；苏清月捂住嘴说这里居然有温泉；水里游着几条没有眼睛的苍白盲鱼，那是源源不断的蛋白质；林峰眼里闪着基建的狂热，说打通加固，农场扩大三倍，温泉还能代替热泵供暖；几个小时后，通道被钢拱肋和灯带加固好，一台小型黄色工程机器停在边上，溶洞成了避难所最核心的后花园；苏清月看着热气腾腾的温泉，对林峰说泡个温泉，算违反同居守则吗，画面拉黑。', 39)
new_scene(b39, 'dug_tunnel', '巨熊挖出来的地洞（一条粗糙的圆形隧道，穿过冻土和冰层，两侧的冻土壁上全是深深的爪痕，尽头一线淡淡的蓝光）',
          'A rough round tunnel clawed through frozen soil and ice by a giant bear, deep claw gouges scored across its frost-furred walls and a faint blue glow far at its end.',
          '一条被巨熊挖出来的粗糙的圆形隧道，穿过冻土和冰层，结霜的洞壁上全是深深的爪痕，尽头有一线淡淡的蓝光。',
          'the rough clawed tunnel, the frost on its walls and the faint blue glow at its end')
new_scene(b39, 'hot_cave', '地底天然溶洞（洞壁和洞顶长满发着柔和蓝光的苔藓，像一整片星空，中央是一汪冒着热气的碧绿色温泉，四周是光滑的岩台）',
          'A vast natural underground cavern with walls and ceiling thickly covered in softly glowing blue moss like a night sky, a steaming turquoise hot spring pool in its middle with white mist rolling off it and smooth rock shelves around its edge.',
          '一座巨大的地底天然溶洞，洞壁和洞顶长满发着柔和蓝光的苔藓，像一整片星空，中央是一汪冒着热气的碧绿色温泉，白色的雾气翻起来，四周是光滑的岩台。',
          'the glowing blue moss, the steaming turquoise pool and the smooth rock shelves')
b39.prop('blind_fish', '盲鱼（身体苍白、半透明、没有眼睛的小鱼，体长一掌，在温暖的水里慢慢游）',
         'A small pale translucent eyeless cave fish about a hand long with a smooth white body, gliding slowly in warm clear water. The reference fixes its look.',
         '一条身体苍白半透明、没有眼睛的洞穴小鱼，体长一掌，在温暖清澈的水里慢慢游。参考图固定它的外形。',
         'A photorealistic close shot of a small pale translucent eyeless cave fish about a hand long with a smooth white body, gliding in clear warm water against a plain soft blue background.')

TA('39-01', '01｜地洞：林峰和苏清月穿着白色防寒服、戴着头灯，一前一后顺着粗糙的地洞往前走，头灯的光束在冻土壁上晃，爪痕一道道掠过', 7, TUNNEL,
   [P('lin_work', 'right', "walking forward through the tunnel in profile facing frame-right, a flashlight in his right hand, his headlamp beam sweeping the frozen wall", 'obj:the dark tunnel ahead', "his jaw set, his eyes alert, his brows low", outfit=LIN_SUIT),
    P('su_tacfit', 'left', "walking one step behind him in profile facing frame-right, a slim tactical dagger in her right hand and her headlamp beam on the floor", 'obj:the dark tunnel ahead', "her lips pressed tight, her eyes wide and alert, her brows pulled together", outfit=SU_SUIT)],
   'Medium wide tracking shot, both from the head to the knees, in the middle third of the frame, in the tunnel.',
   "<lin_work> leads the way forward with his flashlight beam sweeping the clawed frozen wall, his jaw set, his eyes alert and his brows low, and <su_tacfit> follows a step behind with the dagger in her hand, her lips pressed tight, her eyes wide and alert and her brows pulled together, their boots crunching on the frozen ground. Nobody speaks.",
   "林峰在前面带路，手电的光束扫过爬满爪痕的冻土壁，下颌绷住、眼神警觉、眉头压低，苏清月握着匕首跟在他身后一步，嘴唇紧抿、眼睛睁大警觉地看着、眉头拧在一起，靴子踩在冻土上嘎吱响。没有人说话。",
   SOUND_TUNNEL, AES_TUNNEL, cam=track('the two of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Ahead of them the tunnel narrows into darkness with a faint blue glow far at its end.',
   holds='The frame holds exactly two people: Lin and Su, walking in the tunnel, nobody else.')

insert2('39-02', '02｜溶洞：洞壁上发着幽蓝微光的苔藓一点点拉开，露出一座巨大的天然溶洞，中央一汪冒着热气的碧绿色温泉，白色的雾气在洞顶的蓝光里翻腾', 7, HC_WIDE,
        'Wide shot of the cavern, the steaming turquoise pool in the middle third of the frame, nobody visible.',
        "The glowing blue moss on the rock wall slowly gives way to a vast natural cavern under a ceiling of soft blue stars, a steaming turquoise hot spring pool in its middle with white mist rolling slowly off the water. Nothing else moves.",
        "洞壁上发着幽蓝微光的苔藓慢慢退开，露出一座巨大的天然溶洞，洞顶像一片柔和的蓝色星空，洞中央是一汪冒着热气的碧绿色温泉，白色的雾气慢慢从水面翻起来。别的什么都不动。",
        SOUND_CAVE, 'The frame holds the vast cavern with the glowing moss and the steaming pool, and nobody visible.',
        pull('the glowing blue moss on the rock wall', '岩壁上发着蓝光的苔藓', 'the whole vast cavern with its steaming pool', '整座巨大的溶洞和冒着热气的温泉'), AES_MOSS)

TA('39-03', '03｜溶洞口：苏清月站在地洞口，一只手捂住嘴，睁大眼睛说这里居然有温泉，林峰站在她身边慢慢放下手电', 7, HC_MOUTH,
   [P('su_tacfit', 'left', "standing at the tunnel mouth in profile facing frame-right, one gloved hand pressed over her mouth, her eyes on the glowing cavern", 'obj:the glowing cavern and the steaming pool', "her eyes wide and shining, her brows lifted high", outfit=SU_SUIT),
    P('lin_work', 'center-right', "standing beside her in profile facing frame-right, slowly lowering his flashlight, his eyes on the glowing cavern", 'obj:the glowing cavern and the steaming pool', "his lips parting, his eyes wide, his brows lifted", outfit=LIN_SUIT)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the tunnel mouth.',
   "<su_tacfit> presses a hand over her mouth, gazes at the glowing cavern and speaks the one line in a hushed, awed voice to <lin_work>, her eyes wide and shining and her brows lifted high, while <lin_work> slowly lowers his flashlight, his lips parting, his eyes wide and his brows lifted, and the blue moss light plays across their faces.",
   "苏清月用一只手捂着嘴，看着发光的溶洞，用压低的惊叹的声音对林峰说出这一句，眼睛睁大发亮、眉毛高高挑起，林峰慢慢放下手电，嘴唇微张、眼睛睁大、眉毛上扬，蓝色的苔藓光在两人脸上轻轻浮动。",
   SOUND_CAVE_V, AES_MOSS, lines=[('su_tacfit', "这里居然有温泉！", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Beyond them the vast cavern glows with blue moss and a steaming turquoise pool lies in the middle distance.',
   holds='The frame holds exactly two people: Su and Lin, at the tunnel mouth, nobody else.')

insert2('39-04', '04｜温泉：碧绿色的温泉水面上，白色的蒸汽慢慢翻滚，洞顶的蓝色苔藓光在水波里碎成一道道颤动的光线', 6, HC_POOL,
        'Close shot of the pool water, the ripples in the middle third of the frame, nobody visible.',
        "Warm white steam rolls slowly over the glowing turquoise water of the hot spring while slow ripples break the blue moss light into trembling threads and a few droplets hang and glitter in the mist. Nothing else moves.",
        "温暖的白色蒸汽慢慢滚过发光的碧绿色温泉水面，缓缓的涟漪把苔藓的蓝光揉成一道道颤动的细线，几颗小水珠挂在雾里闪着光。别的什么都不动。",
        SOUND_CAVE, 'The frame holds the steaming turquoise water, and nobody visible.',
        push1('the rippling water and the steam', '泛着涟漪的水面和蒸汽'), AES_POOL)

insert2('39-05', '05｜温泉：清澈温暖的水里，几条苍白半透明、没有眼睛的小鱼慢悠悠地游过，吐出一串细细的气泡', 6, HC_FISH,
        'Low close shot just above the waterline, the fish in the middle third of the frame, nobody visible.',
        "Three small pale translucent eyeless fish glide slowly through the clear warm turquoise water, trailing thin silver strings of bubbles while rings of blue light ripple over their bodies. Nothing else moves.",
        "三条小小的苍白半透明、没有眼睛的鱼在清澈温暖的碧绿色水里慢悠悠地游着，身后拖着细细的银色气泡线，一圈圈蓝光从它们身上滑过。别的什么都不动。",
        SOUND_FISH, 'The frame holds the clear water with the pale fish, and nobody visible.',
        lowrise('the gliding pale fish', '游动的苍白小鱼'), AES_FISH, extra_assets=('blind_fish',))

TA('39-06', '06｜溶洞：林峰眼里闪着基建的狂热，指着溶洞和温泉对苏清月说打通加固，农场扩大三倍，温泉还能代替热泵供暖', 9, HC_EDGE,
   [P('lin_work', 'right', "standing on the rock ledge in profile facing frame-left, one arm sweeping out toward the glowing cavern and the pool, his head turned to her", 'Su', "his eyes blazing with feverish excitement, his lips parted in a quick eager breath, his brows lifted high", outfit=LIN_SUIT),
    P('su_tacfit', 'left', "standing beside him on the ledge in profile facing frame-right, her suit collar unzipped a little, her eyes on his face", 'Lin', "her eyes wide and amused, her lips parted, her brows lifted", outfit=SU_SUIT)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, on the rock ledge.',
   "<lin_work> sweeps one arm toward the cavern and speaks the first line to <su_tacfit> and then the second line in a fast, feverish, delighted voice, his eyes blazing with feverish excitement, his lips parted and his brows lifted high, while <su_tacfit> listens beside him, her eyes wide and amused, her lips parted and her brows lifted.",
   "林峰一只手臂朝溶洞挥出去，用又快又狂热又兴奋的声音对苏清月说出第一句，接着说出第二句，眼睛发亮得灼人、嘴唇急急地微张、眉毛高高挑起，苏清月站在他身边听着，眼睛睁大带着好笑、嘴唇微张、眉毛上扬。",
   SOUND_CAVE_V, AES_MOSS, lines=[('lin_work', "打通加固，农场扩大三倍！", 0.8, 'Su'), ('lin_work', "温泉还能代替热泵供暖！", 4.6, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the steaming turquoise pool rolls with white mist under walls of glowing blue moss.',
   holds='The frame holds exactly two people: Lin and Su, on the rock ledge, nobody else.')

insert2('39-07', '07｜地洞：被钢拱肋和一条条暖黄色灯带加固好的通道里，一台小小的黄色工程机器停在左边的墙边，通道尽头是发着蓝光的溶洞', 7, HC_REINF,
        'Wide shot down the passage, the lit steel-ribbed tunnel in the middle third of the frame, nobody visible.',
        "The freshly braced passage lined with steel arch ribs and strips of warm amber lamps stretches toward the glowing blue cavern at its end, a small yellow compact tracked machine parked against the left wall with its arm folded down. Nothing else moves.",
        "刚加固好的通道里一圈圈钢拱肋和暖黄色的灯带一直延伸到尽头发着蓝光的溶洞，一台小小的黄色履带工程机器停在左边的墙边，机械臂收折着。别的什么都不动。",
        SOUND_REINF, 'The frame holds the braced lit passage with the parked machine, and nobody visible.',
        push1('the lit passage and the glowing cavern at its end', '亮着灯的通道和尽头发着光的溶洞'), AES_REINF)

TA('39-08', '08｜溶洞：苏清月站在温泉边，拉开了一点防寒服的领口，湿湿的头发贴在脖子上，转头对林峰说泡个温泉，算违反同居守则吗', 8, HC_EDGE,
   [P('su_tacfit', 'left', "standing at the edge of the steaming pool in profile facing frame-right, one hand pulling her suit collar open at her throat, her damp hair clinging to her neck, her head turned to him", 'Lin', "her eyes bold and shining, her lips parted in a coy smile, her brows lifted", outfit=SU_SUIT),
    P('lin_work', 'right', "standing beside her in profile facing frame-left, his arms loose at his sides, his eyes on her", 'Su', "his eyes dark and fixed on her face, his jaw loosening, his brows low", outfit=LIN_SUIT)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the pool edge.',
   "<su_tacfit> pulls her collar open and speaks the one line to <lin_work> in a soft, husky, teasing voice, her eyes bold and shining, her lips parted in a coy smile and her brows lifted, while <lin_work> listens beside her, his eyes dark and fixed on her face, his jaw loosening and his brows low, and white steam rolls between them.",
   "苏清月拉开领口，用轻柔沙哑带挑逗的声音对林峰说出这一句，眼睛大胆发亮、嘴唇微张带着一丝俏皮大胆的笑、眉毛上扬，林峰站在她身边听着，眼神又黑又深地盯着她的脸、下颌放松、眉头压低，白色的蒸汽在两人之间翻滚。",
   SOUND_CAVE_V, AES_BATHE, lines=[('su_tacfit', "泡个温泉，算违反同居守则吗？", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the steaming turquoise pool rolls with white mist under walls of glowing blue moss.',
   holds='The frame holds exactly two people: Su and Lin, at the pool edge, nobody else.')

# ================================================================================================ 第 40 集
b40 = S.episode('剧本第40集｜深渊的凝视', '溶洞里幽蓝的苔藓光里，苏清月和林峰穿着厚厚的白色浴袍坐在池边的岩台上，光着脚泡在温泉里，她靠在他肩上，他低头吻着她的头发，说在这里，什么末日都没有；接下来的几天，避难所全面升级，溶洞边缘一排排木段上冒出小小的白色蘑菇；苏清月穿着软软的粉色睡衣蹲在池边喂盲鱼，林峰在旁边的小炭盆上炖着鲜美的鱼汤，两个人说笑着；忽然主控室里网络完全物理隔绝的那盏红色警报灯疯狂闪烁，林峰放下碗冲到主控台前，屏幕上滚出一屏绿色的字符，有人在通过残留的军用卫星链路强行破解他们；字符忽然全部停住，扬声器里一个合成的声音说我看到你了；苏清月毛骨悚然，问外面都死绝了，还有谁在线，林峰冷笑一声说真正的对手来了，画面切断。', 40)
b40.prop('hack_screen', '主控台上的宽屏（黑色宽屏，屏幕上是一列列密密的绿色字符，看不清字，旁边有一个小扬声器）',
         'A wide black console screen showing dense columns of tiny unreadable green characters with a small round speaker grille beside it. The reference fixes its look.',
         '一块黑色的宽屏，上面是一列列密密的、看不清的绿色小字符，旁边有一个圆形的小扬声器。参考图固定它的外形。',
         'A photorealistic product shot of a wide black console screen showing dense columns of tiny unreadable green characters with a small round speaker grille beside it, against a plain neutral gray background.')
b40.character('Ghost', 'hack_screen', GHOST_EN, GHOST_ZH)

TA('40-01', '01｜溶洞：苏清月和林峰穿着厚厚的浴袍并排坐在池边的岩台上，光脚泡在温泉里，她把头靠在他肩上，他低头吻在她的头发上，低声说在这里，什么末日都没有', 8, HC_EDGE,
   [P('lin_home', 'right', "sitting on the rock ledge in profile facing frame-left, bending his head to press his lips against her hair", 'Su', "his eyes closed in contentment, his jaw relaxed, his brows soft", outfit=LIN_ROBE),
    P('su_cozy', 'left', "sitting on the rock ledge in profile facing frame-right, her head resting on his shoulder, her feet in the steaming water", 'Lin', "her eyes closed in peace, her lips softly curved in a blissful sweet smile, her brows soft", outfit=SU_ROBE)],
   'Medium close two-shot, both from the head to the waist, in the middle third of the frame, on the rock ledge.',
   "<lin_home> speaks the one line to <su_cozy> in a low, tender, drowsy voice and presses his lips against her hair, his eyes closed in contentment, his jaw relaxed and his brows soft, while <su_cozy> rests her head on his shoulder, her eyes closed in peace, her lips softly curved in a blissful sweet smile and her brows soft, steam curling around them.",
   "林峰用低沉温柔、带着困意的声音对苏清月说出这一句，然后把嘴唇贴在她的头发上，眼睛满足地闭着、下颌放松、眉毛舒展，苏清月把头靠在他肩上，眼睛安心地闭着、嘴角带着幸福的甜笑、眉毛舒展，蒸汽在两人身边卷着。",
   SOUND_BATHE, AES_BATHE, lines=[('lin_home', "在这里，什么末日都没有。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the steaming turquoise pool rolls with white mist under walls of glowing blue moss.',
   holds='The frame holds exactly two people: Lin and Su, on the rock ledge, nobody else.')

insert2('40-02', '02｜溶洞边：潮湿的深色木段一根根排在洞壁边，每一根上都冒出一簇簇小小的白色蘑菇，菇帽上挂着亮亮的水珠', 6, HC_MUSH,
        'Low close shot of the logs, the mushrooms in the middle third of the frame, nobody visible.',
        "A row of dark damp logs lies along the cavern edge, each sprouting clusters of small white mushroom caps beaded with glistening water droplets, while thin steam drifts past in the pale blue moss light. Nothing else moves.",
        "一排潮湿的深色木段摆在溶洞边，每一根上都冒着一簇簇小小的白色蘑菇，菇帽上挂着亮亮的水珠，淡蓝色的苔藓光里一缕缕蒸汽飘过。别的什么都不动。",
        SOUND_CAVE, 'The frame holds the logs with the white mushrooms, and nobody visible.',
        lowrise('the clusters of white mushroom caps', '一簇簇白色的菇帽'), AES_MUSH)

TA('40-03', '03｜溶洞：苏清月穿着软软的粉色睡衣蹲在池边，往水里撒面包屑喂盲鱼，笑着说它们好像认得我了，林峰在旁边的小炭盆上盛着鱼汤说喂胖点，下锅更鲜', 10, HC_SOUP,
   [P('su_cozy', 'left', "crouching at the pool's edge in profile facing frame-left, dropping crumbs from a small wooden bowl into the water, her eyes on the fish", 'obj:the pale fish in the water', "her eyes bright and delighted, her lips curving in a sweet smile, her brows lifted", outfit=SU_PJ),
    P('lin_home', 'right', "standing at the little brazier in profile facing frame-left, ladling milky fish soup from a black iron pot into a bowl, his head turned to her", 'Su', "one corner of his mouth lifting in a dry, warm smirk, his eyes soft, his brows lifted", outfit="in a soft grey henley and dark lounge pants")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the pool edge.',
   "<su_cozy> drops crumbs into the water and speaks the first line to <lin_home> in a bright, delighted voice, her eyes bright and delighted, her lips curving in a sweet smile and her brows lifted, then <lin_home> ladles the soup into a bowl and answers with the second line to <su_cozy> in a low, dry, warm voice, one corner of his mouth lifting in a warm smirk, his eyes soft and his brows lifted.",
   "苏清月往水里撒着面包屑，用明亮欢喜的声音对林峰说出第一句，眼睛明亮、嘴角弯成甜甜的笑、眉毛上扬，林峰一边把鱼汤盛进碗里，一边用低沉干干的温暖声音对苏清月答出第二句，嘴角挑起一丝暖暖的坏笑、眼神柔软、眉毛上扬。",
   SOUND_SOUP, AES_SOUP, lines=[('su_cozy', "它们好像认得我了。", 0.8, 'Lin'), ('lin_home', "喂胖点，下锅更鲜。", 4.4, 'Su')],
   cam=push('both of them', '两人'), extra_assets=('blind_fish',), room={'Su', 'Lin'}, new=True,
   bg='Beside them the turquoise pool glows pale blue with a few pale fish under the surface and glowing blue moss covers the wall behind.',
   holds='The frame holds exactly two people: Su and Lin, at the pool edge, nobody else.')

insert2('40-04', '04｜控制室：房间里没有人，墙上高处那盏代表“网络完全物理隔绝”的圆形红色警报灯忽然疯狂闪起来，红光一下一下撞过黑色的控制台', 5, CTRL_ALARM,
        'Wide shot of the control room, the console in the middle third of the frame, nobody in the room.',
        "In the empty control room the round red alarm lamp high on the wall begins to flash frantically and the red light slams across the dark console in sharp waves while the green status lights flicker below. Nothing else moves.",
        "空荡荡的控制室里，墙上高处的圆形红色警报灯开始疯狂地闪，红光一下一下撞过黑色的控制台，下面绿色的指示灯在跳。别的什么都不动。",
        SOUND_ALARMBIG, 'The frame holds the empty control room with the flashing red lamp, and nobody in the room.',
        push1('the flashing red alarm lamp and the console', '闪着红光的警报灯和控制台'), AES_ALARMLAMP)

TA('40-05', '05｜控制室：林峰坐在转椅里两手飞快地敲着键盘，屏幕上一列列绿色的字符倾泻而下，他低声说有人在强行破解我们，苏清月站在他身后', 8, CTRL_HACK,
   [P('lin_home', 'right', "sitting in the black swivel chair at the console in profile facing frame-left, both hands flying across the keyboard, his eyes on the wide black screen", 'obj:the wide black screen streaming green characters', "his eyes narrowed and burning, his jaw clenched, his brows low", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'center', "standing behind his chair in profile facing frame-left, one hand on the chair back, her eyes on the screen", 'obj:the wide black screen streaming green characters', "her lips pressed tight, her eyes wide, her brows pulled together")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "<lin_home> types fast with his eyes on the screen and speaks the one line to <su_cozy> in a low, tight, dangerous voice, his eyes narrowed and burning, his jaw clenched and his brows low, while <su_cozy> watches the streaming green characters from behind his chair, her lips pressed tight, her eyes wide and her brows pulled together.",
   "林峰一边飞快地敲着键盘盯着屏幕，一边用低沉紧绷又危险的声音对苏清月说出这一句，眼睛眯起发亮、下颌咬紧、眉头压低，苏清月在他肩后看着滚动的绿色字符，嘴唇紧抿、眼睛睁大、眉头拧在一起。",
   SOUND_KEYS, AES_CODE, lines=[('lin_home', "有人在强行破解我们。", 0.8, 'Su')],
   cam=push('both of them', '两人'), extra_assets=('hack_screen',), room={'Su', 'Lin'}, new=True,
   bg='Behind them a round red alarm lamp flashes high on the wall and the wall of six small monitors glows at frame-left.',
   holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

insert2('40-06', '06｜插镜：宽宽的黑色屏幕上，密密麻麻的绿色字符一列列不停地往下倾泻，字符的光在黑色控制台上流动', 6, CODE_CLOSE,
        'Close shot of the black screen, the streaming characters in the middle third of the frame, nobody in the scene.',
        "Dense columns of tiny unreadable green characters pour endlessly down the wide black screen and their cold green light slides across the steel edge of the console, a red alarm glow pulsing faintly out of focus above. Nothing else moves.",
        "密密麻麻的绿色小字符一列一列地不停倾泻在宽宽的黑色屏幕上，它们冷冷的绿光在控制台的钢边上滑过，上方虚虚的红色警报光微弱地脉动着。别的什么都不动。",
        SOUND_CODE, 'The frame holds the wide black screen with the streaming green characters, and nobody in the scene.',
        pull('the streaming green characters', '倾泻的绿色字符', 'the whole wide screen and the console', '整块宽屏和控制台'), AES_CODE, extra_assets=('hack_screen',))

TAV('40-07', '07｜控制室：屏幕上所有的字符忽然全部停住，亮着一片淡绿色的光，控制台的小扬声器里传出一个合成的声音说我看到你了，林峰和苏清月一动不动', CTRL_STILL,
    [P('lin_home', 'right', "sitting in the black swivel chair at the console in profile facing frame-left, his hands frozen above the keyboard, his eyes on the glowing screen", 'obj:the wide black screen glowing steady pale green', "his jaw tight, his eyes sharp and cold, his brows low", outfit="in a soft grey henley and dark lounge pants"),
     P('su_cozy', 'center', "standing behind his chair in profile facing frame-left, her hand gripping the chair back, her eyes on the screen", 'obj:the wide black screen glowing steady pale green', "her lips parting, her face going pale, her brows pulled high")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
    "A flat, cold, androgynous synthetic voice from the small speaker beside the screen speaks the one line as a voice-over. <lin_home> sits motionless with his hands frozen above the keyboard, his jaw tight, his eyes sharp and cold and his brows low, and <su_cozy> stands rigid behind him, her lips parting, her face going pale and her brows pulled high.",
    "控制台屏幕旁边的小扬声器里传出一个平板冰冷、听不出男女的合成声音，以旁白的方式说出这一句。林峰一动不动地坐着，两手僵在键盘上方，下颌绷紧、眼神锐利冰冷、眉头压低，苏清月僵直地站在他身后，嘴唇微张、脸色发白、眉毛高高挑起。",
    SOUND_GHOST, AES_STILL, lines=[('ghost_voice', "我看到你了。", 0.8, 'Lin')],
    cam=push('both of them', '两人'), extra_assets=('hack_screen',), room={'Su', 'Lin'}, new=True,
    bg='Beside the screen on the console a small round speaker grille glows faintly and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

TA('40-08', '08｜控制室：苏清月脸色发白，对林峰说外面都死绝了，还有谁在线，林峰盯着屏幕，嘴角冷冷一挑，说真正的对手，来了', 10, CTRL_STILL,
   [P('su_cozy', 'center', "standing behind his chair in profile facing frame-left, her hand gripping the chair back, her head turned down to him", 'Lin', "her face pale, her lips trembling, her brows pulled high"),
    P('lin_home', 'right', "sitting in the black swivel chair in profile facing frame-left, his knuckles cracking as he grips the armrest, his eyes on the glowing screen", 'obj:the wide black screen glowing steady pale green', "one corner of his mouth lifting coldly, his eyes hard and bright, his brows low", outfit="in a soft grey henley and dark lounge pants")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "<su_cozy> speaks the first line to <lin_home> in a thin, shaking whisper, her face pale, her lips trembling and her brows pulled high, and then <lin_home> keeps his eyes on the screen and answers with the second line to <su_cozy> in a low, cold, steady voice, one corner of his mouth lifting coldly, his eyes hard and bright and his brows low, the pale green glow of the screen lighting both faces.",
   "苏清月用细细发抖的耳语对林峰说出第一句，脸色发白、嘴唇发颤、眉毛高高挑起，然后林峰眼睛盯着屏幕，用低沉冰冷平稳的声音对苏清月答出第二句，嘴角冷冷一挑、眼神又冷又亮、眉头压低，淡绿色的屏幕光照着两个人的脸。",
   SOUND_GHOST, AES_STILL, lines=[('su_cozy', "外面都死绝了，还有谁在线？", 0.8, 'Lin'), ('lin_home', "真正的对手，来了。", 5.4, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Beside the screen on the console a small round speaker grille glows faintly and the wall of six small monitors glows at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, at the control console, nobody else.')

doc = S.finish()
