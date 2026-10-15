#!/usr/bin/env python3
"""【B 短剧快速版：2026-10-15 15:17 起的写法（fast=True，016 的每任务 ≤2 句），2026-10-15 18:45 hh 决定先用 A 写法重做剧本第 51–54 集，本脚本保留以便以后用 B。输出放在 旧合并稿/。】
《极寒末日：我的隐秘安全屋》剧本第 51–54 集，追加稿 020（2026-10-15）。以 019（十二秒版）的 JSON 为底（style／素材／角色逐字复制），必须等 019 在插件里全部跑完再追加。
hh 2026-10-15 13:15：“制作要求回到 29–44 阶段，保留 41–44 的制作需求。”本批严格用 016（第 41–44 集）的做法：
  · 每个任务 5–10 秒（台词按 smooth 算长度），每任务最多 2 句台词、每句 ≤13 个汉字；台词顺滑写法＋全批视频种子 37407；
  · 每个任务一句“光和空气”（AES_*）；运镜写“动作＋终点”；机械／物理变化只拍结果（石头砸落、电缆被切、门被顶开只拍结果）；
  · 引发动作的台词和动作结果拆成两个任务；画外音（伊甸）用 TAV；每人看着谁写进开场图；最多 2 人同框。
大纲：第 51 集 天崩地裂／第 52 集 体温的底线／第 53 集 黑暗中的外科手术／第 54 集 重见光明（见 /root/.claude/uploads 里的 70 集大纲第 51–54 集）。

偏离大纲（交稿时告诉 hh）：
  · 第 51 集：次声波只拍水面涟漪和石壁裂缝（结果）；钟乳石坠落只拍“两人抬头看”＋“砸在变形的门上”两个镜头（不拍坠落过程）；主电缆被切断只拍断头；灯光熄灭＋霜只拍熄灭后的暗和霜慢慢爬上头发；
  · 第 52 集：手表温度数字不写（屏幕上的字读不出来），只拍荧光表盘和白气；亲吻改成吻额头；林峰潜水只拍水面气泡散开＋苏清月一个人守在岸边（嘴动的“回来”用画外低语）；
  · 第 53 集：水下只拍林峰摸线缆、拔出（人在水下，脸朝侧面）；剥线和接线合成一个慢镜头；电火花只拍线头；液压杆压下只拍林峰用力，门缝开出半米只拍结果；
  · 第 54 集：“滑行钻过去”改成苏清月侧身钻过窄缝＋林峰已经躺在门后喘气（结果）；备用电源箱推闸只拍林峰和一盏亮起的绿灯；暖色灯一排排亮起只拍亮起后的屋子；壁炉改成黑金炉灶旁的沙发（屋里没有壁炉）；结尾监控屏亮起只拍两个人愣住的脸（屏幕内容不拍，留给第 55 集）。
H3 方面的风险（交稿时单列，不算我的错）：
  · 51-01 水面涟漪、51-02 石壁裂缝；51-03 抓手腕；51-04 两人奔跑（动作快，可能被拉慢）；51-05 抬头；51-06 钟乳石砸变形的门（结果镜头，大块岩石与金属）；51-08 霜慢慢爬上头发；
  · 52-03 滑进温泉；52-04 水里相拥；52-06 吻额头；52-07 水面气泡；
  · 53-01 水下镜头（人在水里，头发漂动）；53-02 破水而出（快）；53-03 身上结薄冰；53-05 剥线接线的细小手部动作；53-06 电火花；53-08 压杠杆；53-09 门缝；
  · 54-02 侧身钻缝；54-04 推闸亮灯；54-05 伊甸画外音可能被画成多出一个人；54-08 拥抱；54-10 监控屏亮起；
  · 新场景 blast_door（被砸变形的合金防爆门）、dark_river（漆黑的地下暗河水下）没有数据；开场图约一成不按文字画；“同一处”场景用参照图。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
from _jihan_base6 import *
from _scene import smooth_task

import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407, cap=12, fast=True)   # 台词顺滑写法＋全批固定视频种子；cap 只是保险（本批任务都 ≤10 秒）
OUT = '合并稿/旧合并稿/020_第51-54集_B快节奏版_天崩地裂体温底线黑暗手术重见光明_制作稿_追加'
S = Session('合并稿/019_第47-50集_十二秒版_顶级晚餐深雪地狱雪原幽灵绝对零度_制作稿_追加.json', OUT, 80000)
B6.S = S

# ---------------------------------------------------------------------------------------------- 衣着
SU_ROBE = "in a thick white terry bathrobe tied at the waist, her long black hair wet and pinned up with damp strands at her neck"
LIN_ROBE = "in a thick grey terry bathrobe tied at the waist, his black hair damp"
SU_ROBE_WET = "in a soaked white terry bathrobe clinging to her shoulders, her long black hair wet and plastered to her neck"
LIN_ROBE_WET = "in a soaked grey terry bathrobe clinging to his shoulders, his black hair wet and plastered to his forehead"
SU_ROBE_FROST = "in a white terry bathrobe, thin white frost crusting her wet black hair"
LIN_ROBE_ICE = "in a grey terry bathrobe stiff with a thin skin of ice, white frost in his black hair and eyebrows"
SU_HOMEWEAR = "in a soft cream cotton lounge set and thick grey wool socks, her long black hair loose and still damp"

# ---------------------------------------------------------------------------------------------- 光和空气
AES_RIPPLE = ("Soft blue moss light shimmers on the trembling turquoise water, silver mist curls up from the pool and every spreading ring catches a thin line of light.",
              "柔和的蓝色苔藓光在微微发颤的碧绿水面上闪烁，银色的水雾从池面卷起，每一圈扩散的波纹都亮着一线细光。")
AES_CRACK = ("Soft blue moss light flickers across the rock wall as a ragged black crack runs through it, fine dust and glowing flakes of moss drift down through the white mist.",
             "柔和的蓝色苔藓光在岩壁上闪动，一条锯齿状的黑色裂缝贯穿其间，细细的尘土和发光的苔藓碎片在白色水雾里飘落。")
AES_GRAB = ("Soft blue moss light rims their wet faces against the dark cavern while white mist rolls off the pool behind them and fine dust trickles down from above.",
            "柔和的蓝色苔藓光给两个人湿漉漉的脸描上轮廓，黑暗的溶洞里白色的水雾从身后的池面翻滚，细细的尘土从上方淌下来。")
AES_RUN = ("Blue moss light streaks past in soft glowing bands as the two figures race along the rock path, mist trailing behind them and the heavy door glinting grey ahead.",
           "蓝色的苔藓光变成一条条柔和的发光带飞快掠过，两个人沿着岩石小路奔跑，水雾拖在身后，前方灰色的大门闪着冷光。")
AES_LOOKUP = ("A shower of fine grit sifts down through the blue moss glow and a cold deep-blue hush settles over their upturned faces.",
              "一阵细细的碎石粒穿过蓝色的苔藓光筛落下来，一片冰冷深邃的蓝色寂静落在他们仰起的脸上。")
AES_WRECK = ("A heavy cloud of grey dust rolls slowly across the wreckage in the blue moss glow, bright scraps of torn metal glint and small stones are still trickling down.",
             "一大团灰色的尘土在蓝色苔藓光里缓缓滚过废墟，撕裂的金属碎片闪着光，细小的石子还在往下淌。")
AES_CABLECUT = ("A few last blue-white sparks die on the severed cable ends in the rubble, a thread of grey smoke curls up through the blue moss glow and the dust settles.",
                "碎石堆里断掉的电缆线头上几点最后的蓝白色火花渐渐熄灭，一缕灰烟穿过蓝色的苔藓光卷上去，尘土慢慢落定。")
AES_BLACKOUT = ("Only the faint blue moss glow remains in the near-total darkness, thin white frost crystals sparkle as they spread across her wet hair and a pale breath cloud drifts from her lips.",
                "几乎完全的黑暗里只剩一点淡淡的蓝色苔藓光，细细的白色霜晶闪着光爬过她湿漉漉的头发，一团淡淡的白气从她嘴唇边飘出来。")
AES_WATCH = ("A faint green glow from the wrist watch dial lights his tired face from below in the dark cave, his breath puffs out in white clouds and a cold blue moss glow outlines his shoulders.",
             "腕表表盘一点微弱的绿光从下面照亮他疲惫的脸，黑暗的溶洞里他呼出一团团白气，冷冷的蓝色苔藓光描出他肩膀的轮廓。")
AES_SHIVER = ("Cold blue moss light outlines their hunched shoulders, thick white breath clouds hang between their faces and thin frost sparkles on the stone ledge.",
              "冷冷的蓝色苔藓光描出他们缩起的肩膀，浓浓的白气悬在两张脸之间，石台上细细的霜闪着光。")
AES_SLIDEIN = ("Warm turquoise water glows from beneath the surface, thick white steam rolls up around their shoulders and the cold blue moss light rims their wet hair.",
               "温暖的碧绿水光从水面下透出来，浓浓的白色蒸汽从他们的肩膀周围卷起，冷冷的蓝色苔藓光描出他们湿漉漉的头发。")
AES_HUDDLE = ("Soft blue moss light and the warm turquoise glow of the water meet in a teal rim light on their faces, white steam curls between them and fine droplets bead on their cheeks.",
              "柔和的蓝色苔藓光和温暖的碧绿水光在他们脸上交汇成青色的轮廓光，白色的蒸汽在两人之间卷着，细细的水珠挂在脸颊上。")
AES_WRIST = ("Cold blue moss light carves hard edges along their faces and her gripping hand, white steam drifts across the frame and her breath clouds hang in the dark.",
             "冷冷的蓝色苔藓光在他们的脸和她攥紧的手上勾出硬朗的边，白色的蒸汽从画面里飘过，她呼出的白气悬在黑暗里。")
AES_FOREHEAD = ("A faint turquoise water glow lights the underside of their faces, the blue moss light rim-lights his wet hair and slow white steam curls up between them.",
                "一点碧绿的水光从下面照亮他们的脸，蓝色苔藓光给他湿漉漉的头发描上轮廓光，缓缓的白色蒸汽在两人之间卷上去。")
AES_BUBBLES = ("Pale silver bubbles rise through the dark turquoise water and burst in slow rings, the blue moss light shivers on the surface and thin steam drifts over it.",
               "淡银色的气泡从深青绿色的水里升上来，一圈一圈地破开，蓝色苔藓光在水面上颤动，一缕缕薄薄的蒸汽从上面飘过。")
AES_WAIT = ("A faint blue moss glow outlines her bent shoulders against the black water, thin steam curls past her pale face and a single drop falls from her hair into the pool.",
            "一点淡淡的蓝色苔藓光描出她俯着的肩膀，背后是漆黑的水面，一缕薄薄的蒸汽擦过她苍白的脸，一滴水从她发梢落进池里。")
AES_DIVE = ("A thin ghostly blue glow filters down into the black water, silver bubbles stream from his mouth and his hair drifts in slow dark ribbons around his face.",
            "一道细细的、幽灵般的蓝光滤进漆黑的水里，银色的气泡从他嘴边一串串冒出来，他的头发在脸旁飘成慢慢的黑色丝带。")
AES_SURFACE = ("A faint blue moss glow catches the sheet of water running off his shoulders, thick steam pours off his skin and silver droplets fly in slow arcs around him.",
               "一点淡淡的蓝色苔藓光映在从他肩上淌下的水幕上，浓浓的蒸汽从他的皮肤上冒出来，银色的水珠在他周围划出缓慢的弧线。")
AES_ICEHAND = ("A faint blue moss glow catches a thin skin of ice forming over his wet robe and shoulders, white breath pours from his mouth and the thin cable gleams silver in his fist.",
               "一点淡淡的蓝色苔藓光映在他湿袍子和肩膀上正在结起的薄冰上，白气从他嘴里涌出来，他拳头里那根细线缆闪着银光。")
AES_SURGEON = ("A tiny cold blue moss glow edges her fixed, steady face, white breath ghosts out in thin puffs and hard shadows fall across her frosted lashes.",
               "一点小小的冷蓝色苔藓光描出她专注而沉稳的脸，一小缕一小缕的白气飘出来，她结霜的睫毛上落着硬朗的阴影。")
AES_STRIP = ("A pale blue moss glow falls on the thin cable and the gleaming dagger point, white breath drifts across it and the shadows of their bent heads lie sharp on the rock.",
             "淡淡的蓝色苔藓光落在细线缆和闪亮的匕首尖上，白气从上面飘过，他们低着的头的影子清晰地落在岩石上。")
AES_SPARK = ("A blinding blue-white flash bursts at the joined wires and throws every ripple of the cave wall into sharp relief before it settles into a small steady blue glow.",
             "一团耀眼的蓝白色闪光在接起来的线头上爆开，把溶洞岩壁的每一道起伏照得清清楚楚，然后沉成一点小小的、稳稳的蓝色光。")
AES_CONNECTED = ("The small blue glow of the joined wires lights her pale determined face from below and white breath streams from both of them in the freezing dark.",
                 "接好的线头那点小小的蓝光从下面照亮她苍白而坚定的脸，冰冷的黑暗里两个人呼出的白气一缕缕飘着。")
AES_LEVER = ("A hard blue spark-light flickers over the groaning steel lever and his taut forearms while grey dust sifts down around him and white breath bursts from his open mouth.",
             "一闪一闪的蓝色火花光照在绷紧的钢杠杆和他紧绷的前臂上，灰色的尘土在他周围筛落，白气从他张开的嘴里喷出来。")
AES_GAP = ("A thin slice of faint blue moss light cuts through the half-metre gap in the buckled door, grey dust hangs in the air and small stones tick down onto the floor.",
           "一道细细的淡蓝色苔藓光从变形的门里那条半米宽的缝中切过去，灰色的尘土悬在空气里，小石子嘀嘀嗒嗒掉在地上。")
AES_GAPHOLD = ("Cold blue moss light and the dull glow of dust-filled air fall across his clenched jaw and braced shoulders, white breath bursts from his lips and grit rains down.",
               "冷冷的蓝色苔藓光和布满灰尘的空气里暗淡的光落在他咬紧的下颌和撑住的肩膀上，白气从他嘴唇间喷出来，碎石粒落雨一样落下。")
AES_SQUEEZE = ("A thin slice of pale blue moss light from behind her outlines her body in the narrow gap, grey dust swirls in the beam and white breath streams from her lips.",
               "身后一道细细的淡蓝色苔藓光描出她挤在窄缝里的身形，灰色的尘土在光束里打着旋，白气从她嘴唇间飘出来。")
AES_FLOOR = ("Faint grey dust drifts down in the pitch dark of the upper level and the only light is a dim cold blue seeping around the edge of the shut door.",
             "上层完全的黑暗里，灰色的尘土轻轻飘落，唯一的光是从关死的门边缘渗进来的一线暗淡的冷蓝色。")
AES_BREAKER = ("A tiny green indicator lamp blooms on the grey breaker box and washes his exhausted face with a soft emerald light in the pitch dark.",
               "灰色配电箱上一盏小小的绿色指示灯亮起来，在漆黑里把他疲惫的脸洗上一层柔和的翡翠色光。")
AES_EDENWAKE = ("A thin ring of blue light glows on the wall speaker above them, the soft green glow of the breaker box lights their faces and the room beyond them is still black.",
                "他们头顶墙上的扬声器亮着一圈细细的蓝光，配电箱柔和的绿光照亮他们的脸，他们身后的屋子还是一片漆黑。")
AES_LAMPS = ("Row after row of warm amber lamps glow across the room, golden light pools on the cream rug and the marble counter and the black-and-gold stove glows with a deep ember-orange.",
             "一排排温暖的琥珀色灯光亮满整间屋子，金色的光洒在奶油色的地毯和大理石台面上，黑金炉灶透出深深的炭橙色光。")
AES_WARMAIR = ("Soft amber lamp light glows on their faces as warm air ripples the edges of the robes and lifts strands of her damp hair, and tiny droplets glitter on their cheeks.",
               "柔和的琥珀色灯光落在他们脸上，暖风吹得浴袍边缘微微起伏，吹起她潮湿的几缕头发，细细的水珠在他们脸颊上闪着光。")
AES_COZY = ("Honey-gold lamp light wraps the sofa in warmth, the grey cashmere blanket glows softly and the amber ember-glow of the stove warms the edge of the frame.",
            "蜂蜜般的金色灯光把沙发裹进暖意里，灰色的羊绒毯子软软地发着光，炉灶琥珀色的炭火光暖暖地落在画面边缘。")
AES_REMOTE = ("Warm amber lamp light lies across the blanket and his hand as the dark remote clicks, and the cool blue wall of monitors glows faintly behind them.",
              "温暖的琥珀色灯光落在毯子和他的手上，黑色遥控器一按，身后那面监控墙泛着淡淡的冷蓝光。")
AES_SCREEN = ("A cold white glow from the monitor wall floods their stunned faces and washes the warm amber room in a hard teal-and-orange contrast.",
              "监控墙发出的冷白色光涌满他们愣住的脸，把温暖的琥珀色屋子洗出一片强烈的青橙对比。")

# ---------------------------------------------------------------------------------------------- 外貌
look('eden_voice', 'Eden', "a flat wall speaker panel with a thin glowing blue ring", 'none', 'its')
SU_HUSKY = None   # 声音沿用素材库里已有的 SuCozy／LinHome 等角色，本批没有新声音

# ---------------------------------------------------------------------------------------------- 场景
HC_WIDE = Scene('hot_cave', " Soft blue moss light and rolling white mist fill a vast natural cavern.",
                " Fixed stage layout: a vast natural cavern with walls and ceiling of dark rock thickly covered in softly glowing blue moss like a night sky; a steaming turquoise hot spring pool fills the middle of the frame with white mist rolling off it; smooth rock shelves line its edge; a narrow dark tunnel mouth is at frame-left.")
HC_LEDGE = Scene('hot_cave', HC_WIDE.end,
                 " Fixed stage layout: a steaming turquoise hot spring pool fills the left and middle of the frame with white mist rolling off it; a smooth flat rock ledge fills the right of the frame at the pool edge; walls of softly glowing blue moss rise at the back.")
HC_RIPPLE = Scene('hot_cave', HC_WIDE.end,
                  " Fixed stage layout: a close low view of the turquoise water of the hot spring filling the frame, white mist curling off it, concentric rings of ripples spreading outward from the middle of the frame; the glowing blue moss wall is a soft blur at the top edge.")
HC_CRACK = Scene('hot_cave', HC_WIDE.end,
                 " Fixed stage layout: a close view of a rock wall thickly covered in softly glowing blue moss filling the frame, a long ragged black crack running from the top edge down through the middle of the frame, fine dust and moss flakes drifting; white mist at the bottom edge.")
HC_RUN = Scene('hot_cave', HC_WIDE.end,
               " Fixed stage layout: a flat rock path runs along the edge of the steaming turquoise pool from frame-left to frame-right under walls of glowing blue moss; at the far end of the path at frame-right a heavy grey alloy blast door is set into the rock wall.")
HC_LOOKUP = Scene('hot_cave', HC_WIDE.end,
                  " Fixed stage layout: a flat rock path at the foot of a wall of glowing blue moss; above the figures a huge pale stalactite hangs from the ceiling at the top of the frame with a black crack through its root and dust trickling from it; the grey alloy blast door is set into the wall at frame-right.")
HC_DARK = Scene('hot_cave', " Almost total darkness in a vast cavern, only a faint blue moss glow and thin white steam.",
                " Fixed stage layout: a vast dark cavern, the walls of blue moss now glowing only faintly; the steaming turquoise hot spring pool fills the middle of the frame with thin white steam rolling off it; a smooth rock ledge at the pool edge on the right of the frame is furred with white frost.")
HC_DARK_SIDE = Scene('hot_cave', HC_DARK.end,
                     " Fixed stage layout: the dark cavern; a smooth rock ledge furred with white frost fills the right half of the frame and the steaming turquoise pool the left half; the blue moss wall glows faintly behind.")
HC_ALCOVE = Scene('hot_cave', HC_DARK.end,
                  " Fixed stage layout: a small rock alcove at the corner of the dark pool, the water reaching up to the figures chest height, thin steam rolling off the turquoise water and a curved rock wall faintly glowing with blue moss behind them.")
HC_WATER = Scene('hot_cave', HC_DARK.end,
                 " Fixed stage layout: a close low view of the dark turquoise water of the pool filling the frame, thin steam drifting, a few bubbles rising in the middle of the frame and the surface smoothing out; the faint blue moss glow at the top edge.")
HC_LEDGE_DARK = Scene('hot_cave', HC_DARK.end,
                      " Fixed stage layout: the pool surface fills the left and middle of the frame, black and still with thin steam above it; a frost-furred rock ledge fills the right of the frame at the pool edge; the faint blue moss glow behind.")
HC_ICE = Scene('hot_cave', HC_DARK.end,
               " Fixed stage layout: a frost-furred flat rock ledge at the pool edge fills the frame, the dark water close at frame-left with a few last wisps of steam, and a wall of faintly glowing blue moss behind.")
HC_TWO = Scene('hot_cave', HC_DARK.end,
               " Fixed stage layout: a frost-furred flat rock ledge at the dark pool edge fills the right of the frame, the black water at frame-left, a wall of faintly glowing blue moss behind.")
RIVER = Scene('dark_river', " Nearly pitch-black water with a thin ghostly blue glow filtering down from far above.",
              " Fixed stage layout: underwater in a narrow black underground river channel; the rough rock wall runs across the middle of the frame with a thin dark seam in it; a thin silver cable glints inside the seam; faint blue light filters down from the top of the frame; silver bubbles rise.")
DOOR_WRECK = Scene('blast_door', " Grey dust hangs in the air in a dim cavern lit by faint blue moss.",
                   " Fixed stage layout: a heavy grey alloy blast door set in a rock wall fills the middle of the frame, its metal frame crumpled and bent inward, a huge broken pale stalactite lying across its base amid rubble; grey dust hangs in the air; the wall of blue moss glows faintly on both sides.")
DOOR_CABLE = Scene('blast_door', DOOR_WRECK.end,
                   " Fixed stage layout: a close low view of the rubble at the foot of the wall; a thick black power cable lies severed in two among broken stones in the middle of the frame, its cut ends apart with a few dying blue sparks and a thread of grey smoke; the crumpled alloy door is a soft blur behind.")
DOOR_LEVER = Scene('blast_door', DOOR_WRECK.end,
                   " Fixed stage layout: the crumpled grey alloy blast door in its rock wall fills the frame-left; a steel hydraulic lever with a thick handle is mounted in the floor beside the door at frame-right; broken stones lie on the floor; grey dust hangs in the air.")
DOOR_GAP = Scene('blast_door', DOOR_WRECK.end,
                 " Fixed stage layout: the crumpled grey alloy blast door fills the frame with a vertical gap about half a metre wide forced open in the middle of the frame, faint blue moss light beyond it; grey dust sifts down; the steel hydraulic lever stands at frame-right.")
DOOR_SHUT = Scene('blast_door', " A pitch dark concrete corridor with a thin dim blue line of light around a shut door.",
                  " Fixed stage layout: seen from the dark upper level, the crumpled grey alloy blast door is jammed shut in its bent frame at frame-right with a dim cold blue line of light around its edge; grey dust drifts; the concrete floor of a dark corridor fills the rest of the frame.")
DARK_LIVING = Scene('bunker_living', " Pitch black underground living area, no lights at all.",
                    " Fixed stage layout: a pitch dark underground living area; the shapes of the open kitchen with the black-and-gold stove are at frame-left and the cream rug and the round wooden table in the middle; a grey steel breaker box with a heavy lever is mounted on the concrete wall at frame-right beside the round steel hatch door.")
LIV_LIT = Scene('bunker_living', LIVING.end,
                " Fixed stage layout: the whole open underground living area now lit: the open kitchen with the black-and-gold stove glowing ember-orange at frame-left, the thick cream wool rug and round wooden table in the middle, the wall of small security monitors at frame-center-right, the heavy round steel hatch door in the right wall; wooden shelves of supplies stacked behind; nobody in the scene.")
LIV_VENT = Scene('bunker_living', LIVING.end,
                 " Fixed stage layout: a close view of the cream rug and the round wooden table in the middle of the frame, a square ceiling air vent above them at the top of the frame, the open kitchen with the black-and-gold stove glowing at frame-left, the wall of monitors dark at frame-right.")
SOFA_HOME = Scene('bunker_sofa', SOFA.end, SOFA.layout + " A thick grey cashmere blanket lies over the sofa and the black-and-gold stove glows ember-orange at frame-left.")
SOFA_SCREEN = Scene('bunker_sofa', SOFA.end,
                    " Fixed stage layout: seen from the front of the room, the deep brown leather sofa stands in the middle of the frame facing the wall of small security monitors at the far end of the room behind the camera; a thick grey cashmere blanket lies over the sofa; the open kitchen with the black-and-gold stove glows at frame-left.")

# ---------------------------------------------------------------------------------------------- 声音
SOUND_TREMOR = breathy('A deep low throbbing hum felt more than heard, the soft lap of trembling water and a faint far rumble.', '一阵深沉的低频震颤声，与其说听见不如说感觉到，水面轻轻晃动的拍水声和远处一声轻轻的轰隆。')
SOUND_CRACK = breathy('A dry splitting groan of rock, a thin trickle of falling dust and the faint bubbling of the pool.', '岩石干涩的裂开呻吟声、尘土细细的淌落声和水池轻轻的咕嘟声。')
SOUND_GRAB = voiced('A deep low rumble, the splash of water and the quick rustle of wet fabric.', '深沉的低低的隆隆声、水花声和湿衣料急促的摩擦声。')
SOUND_RUN = breathy('The slap of bare feet on wet rock, ragged breathing and a deep rumble shaking the cavern.', '赤脚拍在湿岩石上的啪嗒声、急促的喘息声和震动着整个溶洞的深沉隆隆声。')
SOUND_LOOKUP = breathy('A tense rising creak of stone overhead and the patter of falling grit.', '头顶岩石紧绷渐强的吱嘎声和碎石粒落下的噼啪声。')
SOUND_WRECK = breathy('A last rolling crash fading into the soft patter of falling stones and a deep ringing silence.', '最后一阵滚动的巨响渐渐淡去，只剩小石子轻轻的噼啪落地声和一片深深的嗡嗡寂静。')
SOUND_CABLECUT = breathy('A last sharp electric crackle, then a deep hush and the tick of cooling metal.', '最后一声尖脆的电流噼啪，然后是深深的寂静和金属冷却时的嘀嗒声。')
SOUND_BLACKOUT = voiced('A deep dead silence, the faint hiss of icy wind in a far vent and a shivering breath.', '深深的死寂、远处通风口里冰冷的风细细的嘶嘶声和一声发抖的呼吸。')
SOUND_WATCH = breathy('A deep dead silence, the faint tick of a watch and shivering breath.', '深深的死寂、手表细细的嘀嗒声和发抖的呼吸声。')
SOUND_COLD = voiced('A thin whistle of icy wind through the cavern and chattering breath.', '冰冷的风穿过溶洞的细细呼啸和打着颤的呼吸声。')
SOUND_SLIDEIN = breathy('The soft slosh of warm water, a long shuddering breath and the gentle bubbling of the pool.', '温水轻轻的晃动声、一声长长发颤的呼吸和池水轻轻的咕嘟声。')
SOUND_HUDDLE = voiced('The gentle bubbling of warm water, a distant drip and a quiet shivering breath.', '温水轻轻的咕嘟声、远处一滴水声和安静发颤的呼吸。')
SOUND_WRIST = voiced('The gentle bubbling of warm water and a held, trembling breath.', '温水轻轻的咕嘟声和屏住的、发着抖的呼吸。')
SOUND_KISS = voiced('The gentle bubbling of warm water and a long slow breath.', '温水轻轻的咕嘟声和一声长长的、缓慢的呼吸。')
SOUND_BUBBLES = breathy('A single deep plunge of water, the soft burbling of rising bubbles and then stillness.', '一声沉沉的入水声、气泡升起时轻轻的咕噜声，然后一片安静。')
SOUND_WAIT = voiced('A deep dead silence, a single drip of water and a trembling breath.', '深深的死寂、一滴水落下的声音和一声发颤的呼吸。')
SOUND_DIVE = breathy('A muffled underwater silence, a faint slow heartbeat and the soft burble of escaping bubbles.', '被闷住的水下寂静、一声微弱缓慢的心跳和气泡逸出时轻轻的咕噜声。')
SOUND_SURFACE = breathy('A great splash of water, a gasping tearing breath and water streaming off skin.', '一大片水花声、一口撕裂般的喘息声和水从皮肤上淌下的哗哗声。')
SOUND_ICEHAND = voiced('Labored gasping breath, the faint crackle of ice forming on cloth and a drip of water.', '吃力的喘息声、冰在布料上结起时细细的噼啪声和一滴水声。')
SOUND_SURGEON = voiced('A deep dead silence and steady shallow breathing.', '深深的死寂和平稳而浅的呼吸声。')
SOUND_STRIP = breathy('A tiny scrape of steel on insulation, a steady slow breath and the faint tick of frost.', '钢刃刮过绝缘皮时一点极小的刮擦声、平稳缓慢的呼吸和霜细细的嘀嗒声。')
SOUND_SPARK = breathy('A sharp crackling snap of electricity, then a soft steady hum.', '一声尖脆的电流爆响，然后是轻轻稳稳的嗡鸣。')
SOUND_LEVER_NV = breathy('A grinding groan of hydraulic metal, a roaring effortful breath and falling grit.', '液压金属吃力的摩擦呻吟声、一声用尽全力的吼声般的喘息和碎石落下的声音。')
SOUND_LEVER = voiced('A grinding groan of hydraulic metal, a roaring strained breath and falling grit.', '液压金属吃力的摩擦呻吟声、一声用尽全力的吼声般的喘息和碎石落下的声音。')
SOUND_GAPDOOR = breathy('The slow grinding groan of metal giving way, a final dull clank and the patter of falling grit.', '金属一点点让开时缓慢的摩擦呻吟声、最后一声钝钝的当啷声和碎石落下的噼啪声。')
SOUND_SQUEEZE = breathy('A scrape of cloth on rough metal, a held breath and the patter of grit.', '布料擦过粗糙金属的摩擦声、一声屏住的呼吸和碎石落下的声音。')
SOUND_FLOOR = breathy('A deep dead silence, a hoarse dragging breath and the soft tick of settling dust.', '深深的死寂、嘶哑拖长的喘息和尘土落定时细细的嘀嗒声。')
SOUND_BREAKER_NV = breathy('The heavy clunk of a metal lever, a rising electronic hum and a quick ragged breath.', '一声沉重的金属杠杆当啷声、渐渐升起的电子嗡鸣和急促粗重的呼吸。')
SOUND_BREAKER = voiced('The heavy clunk of a metal lever, a rising electronic hum and a quick ragged breath.', '一声沉重的金属杠杆当啷声、渐渐升起的电子嗡鸣和急促粗重的呼吸。')
SOUND_EDEN = voiced('A soft rising electronic chime, the quiet clicking of relays and a slow exhausted breath.', '一阵轻柔渐强的电子鸣音、继电器细细的咔嗒声和一声缓慢疲惫的呼吸。')
SOUND_LAMPS = breathy('A swelling low hum of a heat pump starting up, the soft tick of lamps warming and the gentle crackle of the stove.', '地源热泵启动时渐渐升高的低低嗡鸣、灯具变暖时细细的嘀嗒声和炉灶轻轻的噼啪声。')
SOUND_WARMAIR = voiced('The soft rushing breath of warm air from a vent and a long contented sigh.', '通风口吹出暖风轻柔的呼呼声和一声长长满足的叹息。')
SOUND_COZY = breathy('The soft crackle of the stove, a slow steady breathing and the gentle rustle of a blanket.', '炉灶轻轻的噼啪声、缓慢平稳的呼吸和毯子轻轻的摩擦声。')
SOUND_REMOTE = voiced('The soft crackle of the stove and one quiet click of a remote.', '炉灶轻轻的噼啪声和遥控器一声安静的按键声。')
SOUND_SCREEN = breathy('A deep hush, the faint hum of the monitor wall and the soft crackle of the stove.', '深深的安静、监控墙细细的嗡鸣和炉灶轻轻的噼啪声。')

# ================================================================================================ 第 51 集
b51 = S.episode('剧本第51集｜天崩地裂', '溶洞温泉里，水面被一阵看不见的低频震颤震出一圈圈波纹，发光的苔藓石壁崩开一条黑色裂缝；林峰脸色大变，拉起苏清月说是次声波共振，快离开这；两人裹着浴袍沿岩石小路狂奔，头顶一块巨大的钟乳石断裂，砸在通往上层的防爆合金门前，门框变形卡死，粗电缆被碎石切断；灯全灭了，只剩幽蓝的苔藓光，苏清月湿漉漉的头发开始结霜，他们被困在断电的地底。', 51)
new_scene(b51, 'blast_door', '被砸坏的防爆合金门（岩壁里一扇灰色的厚重合金门，门框被砸得向内弯曲变形，门脚横着一块断裂的苍白钟乳石和碎石）',
          'A heavy grey alloy blast door set in a rock wall with its metal frame crumpled and bent inward and a huge broken pale stalactite lying across its base amid rubble, faint blue moss light on the walls on both sides.',
          '岩壁里一扇灰色的厚重合金防爆门，门框被砸得向内弯曲变形，门脚横着一块断裂的苍白钟乳石和碎石，两边的岩壁上亮着淡淡的蓝色苔藓光。',
          'the crumpled alloy door, the broken stalactite and the rubble')
new_scene(b51, 'dark_river', '漆黑的地下暗河（水下，粗糙的岩壁上有一道细缝，缝里闪着一根银色细线缆，上方滤下一线幽灵似的蓝光）',
          'An underwater view of a narrow black underground river channel with a rough rock wall running across the frame, a thin dark seam in it with a thin silver cable glinting inside, faint ghostly blue light filtering down from above and silver bubbles rising.',
          '漆黑狭窄的地下暗河水下，粗糙的岩壁上有一道细缝，缝里闪着一根银色的细线缆，上方滤下一线幽灵似的蓝光，银色的气泡往上冒。',
          'the rock wall, the seam with the silver cable and the rising bubbles')

insert2('51-01', '01｜溶洞：碧绿的温泉水面微微发颤，一圈一圈的波纹从池中央往外扩散，白色的水雾贴着水面卷着', 6, HC_RIPPLE,
        'Low close shot of the pool surface, the spreading rings in the middle third of the frame, nobody in the scene.',
        "Concentric rings of ripples spread outward across the turquoise water of the hot spring as the surface trembles faintly and white mist curls along it. Nothing else moves.",
        "碧绿的温泉水面微微发颤，一圈一圈同心的波纹从池中央往外扩散，白色的水雾贴着水面卷着。别的什么都不动。",
        SOUND_TREMOR, 'The frame holds the trembling pool surface with the spreading ripples, and nobody in the scene.',
        push1('the spreading ripples', '扩散的波纹'), AES_RIPPLE)

insert2('51-02', '02｜溶洞：发着幽蓝光的苔藓石壁上，一条黑色的裂缝从上到下贯穿开来，细细的尘土和发光的苔藓碎片往下飘', 6, HC_CRACK,
        'Close shot of the rock wall, the long black crack in the middle third of the frame, nobody in the scene.',
        "A long ragged black crack runs from the top to the bottom of the glowing blue-moss rock wall while fine dust and bright flakes of moss drift slowly down through the white mist. Nothing else moves.",
        "发着幽蓝光的苔藓石壁上，一条锯齿状的黑色裂缝从上到下贯穿，细细的尘土和发亮的苔藓碎片在白色水雾里慢慢往下飘。别的什么都不动。",
        SOUND_CRACK, 'The frame holds the glowing rock wall with the long black crack, and nobody in the scene.',
        tilt('the long black crack', '那条长长的黑色裂缝'), AES_CRACK)

TA('51-03', '03｜温泉边：苏清月披着浴袍坐在岩台上，林峰脸色大变，一把抓住她的手腕把她拉起来，说是次声波共振，快离开这', 7, HC_LEDGE,
   [P('su_cozy', 'left', "sitting on the smooth rock ledge in three-quarter profile facing frame-right, her bare feet in the water, her head turned up to him", 'Lin', "her eyes wide with alarm, her lips parted, her brows pulled together", outfit=SU_ROBE),
    P('lin_home', 'right', "standing at the ledge in profile facing frame-left, his right hand gripping her left wrist at chest height, his head bent toward her", 'Su', "his face drawn tight, his jaw clenched, his eyes sharp and alarmed, his brows low", outfit=LIN_ROBE)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the pool edge.',
   "<su_cozy> looks up at <lin_home> and speaks the first line to <lin_home> in a thin worried voice, then <lin_home> grips her wrist and speaks the second line to <su_cozy> in a low urgent voice, her eyes wide with alarm, her lips parted and her brows pulled together, his face drawn tight, his jaw clenched, his eyes sharp and alarmed and his brows low.",
   "苏清月抬头看着林峰，用发细担心的声音对他说出第一句，接着林峰攥着她的手腕，用低沉急迫的声音对苏清月说出第二句，她眼睛睁大满是惊慌、嘴唇微张、眉头拧在一起，他脸绷得紧紧的、下颌咬紧、眼神锐利惊觉、眉头压低。",
   SOUND_GRAB, AES_GRAB, lines=[('su_cozy', "怎么了？", 0.8, 'Lin'), ('lin_home', "是次声波共振，快离开这！", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the steaming turquoise pool and the wall of glowing blue moss fill the cavern.',
   holds='The frame holds exactly two people: Su and Lin, at the pool edge, nobody else.')

TA('51-04', '04｜溶洞：两人裹着浴袍沿着池边的岩石小路拼命往前跑，林峰拉着苏清月的手，前面尽头是一扇灰色的合金大门', 6, HC_RUN,
   [P('lin_home', 'left', "running along the rock path in profile facing frame-right, his right hand holding her left hand and pulling her along, his eyes on the far door", 'obj:the heavy grey alloy door at the end of the path', "his jaw clenched, his eyes fierce and fixed, his brows low", outfit=LIN_ROBE),
    P('su_cozy', 'center', "running a half step behind him in profile facing frame-right, her robe flying open at the hem, her eyes on the far door", 'obj:the heavy grey alloy door at the end of the path', "her lips parted in a gasp, her eyes wide, her brows pulled together", outfit=SU_ROBE)],
   'Medium wide two-shot, both from head to toe, in the middle third of the frame, on the rock path.',
   "<lin_home> runs along the rock path holding <su_cozy> by the hand and pulling her after him, his jaw clenched, his eyes fierce and fixed on the far door and his brows low, while <su_cozy> runs a half step behind him with her robe flying, her lips parted in a gasp, her eyes wide and her brows pulled together. They run steadily toward the door.",
   "林峰拉着苏清月的手沿着岩石小路往前跑，下颌咬紧、眼神凶狠地盯着远处的门、眉头压低，苏清月落后他半步跑着，浴袍下摆飞起来，嘴唇微张喘着气、眼睛睁大、眉头拧在一起。他们稳稳地朝门跑去。",
   SOUND_RUN, AES_RUN, cam=track('the two of them', '他们两个'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the steaming turquoise pool and the walls of glowing blue moss streak past.',
   holds='The frame holds exactly two people: Lin and Su, on the rock path, nobody else.')

TA('51-05', '05｜溶洞：两人在门前停下脚步，同时抬起头往头顶看，细细的碎石粒从上面筛下来', 6, HC_LOOKUP,
   [P('lin_home', 'left', "standing on the rock path in profile facing frame-right, his head tipped back, his arm out in front of her", 'obj:the huge cracked stalactite hanging from the ceiling', "his jaw clenched, his eyes wide with dread, his brows pulled high", outfit=LIN_ROBE),
    P('su_cozy', 'center', "standing close behind him in profile facing frame-right, her head tipped back, one hand gripping his robe", 'obj:the huge cracked stalactite hanging from the ceiling', "her lips parted, her eyes wide with terror, her brows pulled together", outfit=SU_ROBE)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in front of the door.',
   "<lin_home> and <su_cozy> stop and tip their heads back to look up at the huge cracked stalactite overhead while fine grit sifts down on them, <lin_home> with his jaw clenched, his eyes wide with dread and his brows pulled high and his arm out in front of her, <su_cozy> with her lips parted, her eyes wide with terror and her brows pulled together, one hand gripping his robe.",
   "林峰和苏清月停下来，仰起头看着头顶那块裂开的巨大钟乳石，细细的碎石粒落在他们身上，林峰下颌咬紧、眼睛因恐惧睁大、眉毛高高拧起，一只手臂挡在她前面，苏清月嘴唇微张、眼睛因恐惧睁大、眉头拧在一起，一只手攥着他的浴袍。",
   SOUND_LOOKUP, AES_LOOKUP, cam=lowrise('the two upturned faces', '两张仰起的脸'), room={'Su', 'Lin'}, new=True,
   bg='Above them a huge pale stalactite hangs from the ceiling with a black crack through its root, and the grey alloy blast door is set in the wall behind them.',
   holds='The frame holds exactly two people: Lin and Su, in front of the door, nobody else.')

insert2('51-06', '06｜溶洞：灰色的合金大门前，一块巨大的苍白钟乳石断成几截横在门脚，门框被砸得向内弯曲变形，灰色的尘土在碎石上慢慢滚过', 7, DOOR_WRECK,
        'Wide shot of the door and the rubble, the crumpled door frame in the middle third of the frame, nobody in the scene.',
        "A huge pale stalactite lies broken across the foot of the grey alloy blast door, whose metal frame is crumpled and bent inward, while a cloud of grey dust rolls slowly over the rubble and small stones trickle down. Nothing else moves.",
        "一块巨大的苍白钟乳石断成几截横在灰色合金防爆门的门脚，门框被砸得向内弯曲变形，灰色的尘土在碎石上慢慢滚过，细小的石子淌下来。别的什么都不动。",
        SOUND_WRECK, 'The frame holds the crumpled door with the broken stalactite and the rubble, and nobody in the scene.',
        pull('the crumpled door frame', '弯曲变形的门框', 'the whole wrecked door and the fallen stalactite', '整扇被砸坏的门和倒下的钟乳石'), AES_WRECK)

insert2('51-07', '07｜碎石堆里：一根粗黑的主电缆被砸断成两截，断头躺在石头中间，几点蓝白色的火花慢慢熄灭，一缕灰烟往上卷', 5, DOOR_CABLE,
        'Low close shot of the severed cable among the stones, the cut ends in the middle third of the frame, nobody in the scene.',
        "A thick black power cable lies severed in two among the broken stones, its cut ends apart as a few blue-white sparks die away and a thread of grey smoke curls slowly upward. Nothing else moves.",
        "一根粗黑的主电缆被砸断成两截躺在碎石中间，断开的两个线头分开着，几点蓝白色的火花慢慢熄灭，一缕灰烟慢慢往上卷。别的什么都不动。",
        SOUND_CABLECUT, 'The frame holds the severed cable among the stones, and nobody in the scene.',
        push1('the two cut ends and the dying sparks', '断开的两个线头和熄灭的火花'), AES_CABLECUT)

TA('51-08', '08｜溶洞：灯全灭了，只剩幽蓝的苔藓光，苏清月靠在林峰怀里小声说灯全灭了，林峰低声说别怕，我在，她湿漉漉的头发上慢慢爬上一层白霜', 8, HC_DARK_SIDE,
   [P('su_cozy', 'left', "standing in his arms in profile facing frame-right, her head against his chest, her eyes on the dark cavern", 'obj:the dark cavern beyond the pool', "her lips trembling, her eyes wide and glistening, her brows pulled together", outfit=SU_ROBE_FROST),
    P('lin_home', 'right', "standing with both arms wrapped around her in profile facing frame-left, his chin over her hair, his eyes on the dark cavern", 'Su', "his jaw set, his eyes hard and steady, his brows low", outfit=LIN_ROBE)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, in the dark cavern.',
   "<su_cozy> stands in the arms of <lin_home> and speaks the first line to <lin_home> in a small shaking voice, then <lin_home> speaks the second line to <su_cozy> in a low steady voice, her lips trembling, her eyes wide and glistening and her brows pulled together, his jaw set, his eyes hard and steady and his brows low, while thin white frost slowly creeps across her wet hair.",
   "苏清月靠在林峰的怀里，用发抖的小声音对他说出第一句，接着林峰用低沉平稳的声音对苏清月说出第二句，她嘴唇发颤、眼睛睁大含着泪光、眉头拧在一起，他下颌绷紧、眼神冷硬而稳、眉头压低，薄薄的白霜慢慢爬上她湿漉漉的头发。",
   SOUND_BLACKOUT, AES_BLACKOUT, lines=[('su_cozy', "灯，全灭了。", 0.8, 'Lin'), ('lin_home', "别怕，我在。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the frost-furred rock ledge and the dark pool lie under only a faint blue moss glow.',
   holds='The frame holds exactly two people: Su and Lin, in the dark cavern, nobody else.')

# ================================================================================================ 第 52 集
b52 = S.episode('剧本第52集｜体温的底线', '黑暗的溶洞里，林峰的腕表发着微弱的荧光，他呼出一团团白气；他说不能待在岸上，回温泉里去；两人滑进四十度的温泉，只露出肩膀，躲在水里的岩洞死角紧紧相拥；苏清月冷得嘴唇发紫，说主电缆断了水迟早凉透，林峰说水下有备用线缆，我去接；她攥住他的手腕说水下两分钟你没有光，他说阎王都收不走我，等我，吻了吻她的额头，深吸一口气扎进漆黑的水里，水面只留下几个慢慢散开的气泡，苏清月一个人守在岸边低声说回来。', 52)

TA('52-01', '01｜溶洞：林峰坐在结霜的岩台上，抬起手腕看着发荧光的腕表，呼出一团团白气，表盘上的光越来越弱', 6, HC_DARK_SIDE,
   [P('lin_home', 'center', "sitting on the frost-furred rock ledge in three-quarter profile facing frame-left, his left forearm raised in front of his chest, his eyes on the wrist watch", 'obj:the faintly glowing wrist watch on his raised wrist', "his jaw clenched, his eyes narrowed and hard, his brows low", outfit=LIN_ROBE_ICE)],
   'Medium close shot, one man from the head to the chest, in the middle third of the frame, on the rock ledge.',
   "<lin_home> sits on the frost-furred ledge and stares at the faintly glowing wrist watch on his raised wrist while thick white breath pours from his mouth, his jaw clenched, his eyes narrowed and hard and his brows low, and the green glow of the watch dial dims slowly.",
   "林峰坐在结霜的岩台上，盯着抬起的手腕上那只发着微光的腕表，浓浓的白气从嘴里涌出来，下颌咬紧、眼睛眯起冷硬、眉头压低，表盘上的绿光慢慢暗下去。",
   SOUND_WATCH, AES_WATCH, cam=push1('Lin and the dimming watch', '林峰和渐渐暗下去的腕表'), room={'Lin'}, new=True,
   bg='Behind him the dark pool steams faintly under a wall of dim blue moss.',
   holds='The frame holds exactly one person: Lin, on the rock ledge, nobody else.')

TA('52-02', '02｜溶洞：两人缩在结霜的岩台上发抖，林峰呼出一口浓重的白气，对苏清月说不能待在岸上，回温泉里去', 7, HC_TWO,
   [P('su_cozy', 'left', "sitting hunched on the frost-furred ledge in three-quarter profile facing frame-right, her arms wrapped around herself, her eyes up at him", 'Lin', "her lips pale and shaking, her eyes wide, her brows pulled together", outfit=SU_ROBE_FROST),
    P('lin_home', 'right', "sitting beside her in profile facing frame-left, one arm around her shoulders, his head bent toward her", 'Su', "his jaw set, his eyes hard and decisive, his brows low", outfit=LIN_ROBE_ICE)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, on the rock ledge.',
   "<lin_home> blows out a thick cloud of white breath and speaks the one line to <su_cozy> in a low firm voice, his jaw set, his eyes hard and decisive and his brows low, while <su_cozy> huddles against him with her arms wrapped around herself, her lips pale and shaking, her eyes wide and her brows pulled together.",
   "林峰呼出一口浓重的白气，用低沉坚定的声音对苏清月说出这一句，下颌绷紧、眼神冷硬果断、眉头压低，苏清月缩在他身边抱着自己的手臂，嘴唇发白发抖、眼睛睁大、眉头拧在一起。",
   SOUND_COLD, AES_SHIVER, lines=[('lin_home', "不能待在岸上，回温泉里去。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the dark pool steams under a wall of dim blue moss.',
   holds='The frame holds exactly two people: Su and Lin, on the rock ledge, nobody else.')

TA('52-03', '03｜温泉：两人手拉着手慢慢滑进冒着热气的碧绿温泉里，水一点点漫过腰、漫过胸口，白色的蒸汽把他们的肩膀裹住', 7, HC_ALCOVE,
   [P('su_cozy', 'left', "lowering herself into the steaming turquoise water in three-quarter profile facing frame-right, the water up to her collarbone, her eyes closing", 'closed', "her lips parting in a shuddering sigh of relief, her brows relaxing", outfit=SU_ROBE_WET, shut='gently closed'),
    P('lin_home', 'right', "lowering himself into the water beside her in profile facing frame-left, the water up to his chest, his hand still holding hers, his eyes on her face", 'Su', "his jaw easing, his eyes dark and tense, his brows drawn together", outfit=LIN_ROBE_WET)],
   'Medium two-shot, both from the head to the chest, in the middle third of the frame, at the pool corner.',
   "<su_cozy> and <lin_home> slowly slide into the steaming turquoise water hand in hand until it reaches her collarbone and his chest, her eyes closing, her lips parting in a shuddering sigh of relief and her brows relaxing, his jaw easing, his eyes dark and tense on her face and his brows drawn together, while white steam rolls up around their shoulders.",
   "苏清月和林峰手拉着手慢慢滑进冒着热气的碧绿温泉里，水漫到她的锁骨、他的胸口，她闭上眼睛、嘴唇微张发出一声发颤的松气、眉头松开，他下颌放松、眼神深暗而紧绷地看着她、眉头拧着，白色的蒸汽在他们的肩膀周围卷起来。",
   SOUND_SLIDEIN, AES_SLIDEIN, cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the dark cavern walls glow faintly with blue moss and thin steam rolls over the water.',
   holds='The frame holds exactly two people: Su and Lin, in the pool, nobody else.')

TA('52-04', '04｜温泉：两人躲在水里的岩洞死角紧紧相拥，苏清月冷得嘴唇发紫，说主电缆断了水迟早凉透，林峰说水下有备用线缆，我去接', 9, HC_ALCOVE,
   [P('su_cozy', 'left', "in the water up to her collarbone in profile facing frame-right, held tight against his chest, her head turned up to him", 'Lin', "her lips purple and trembling, her eyes sharp and clear, her brows pulled together", outfit=SU_ROBE_WET),
    P('lin_home', 'right', "in the water up to his chest in profile facing frame-left, both arms wrapped around her, his head bent down to her", 'Su', "his jaw set, his eyes dark and sharp, his brows low", outfit=LIN_ROBE_WET)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, in the rock alcove.',
   "<su_cozy> speaks the first line to <lin_home> in a thin trembling clear voice, her lips purple and trembling, her eyes sharp and clear and her brows pulled together, then <lin_home> speaks the second line to <su_cozy> in a low steady voice, his jaw set, his eyes dark and sharp and his brows low, while white steam curls between their faces.",
   "苏清月用发颤却清楚的细声音对林峰说出第一句，嘴唇发紫发颤、眼神清明锐利、眉头拧在一起，接着林峰用低沉平稳的声音对苏清月说出第二句，下颌绷紧、眼神深暗锐利、眉头压低，白色的蒸汽在两张脸之间卷着。",
   SOUND_HUDDLE, AES_HUDDLE, lines=[('su_cozy', "主电缆断了，水迟早凉透。", 0.8, 'Lin'), ('lin_home', "水下有备用线缆，我去接。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them a curved rock wall glows faintly with blue moss and thin steam rolls off the water.',
   holds='The frame holds exactly two people: Su and Lin, in the rock alcove, nobody else.')

TA('52-05', '05｜温泉：苏清月一把攥住林峰的手腕，对他说水下两分钟，你没有光', 7, HC_ALCOVE,
   [P('su_cozy', 'left', "in the water up to her collarbone in profile facing frame-right, her right hand gripping his left wrist at chest height above the water, her head turned up to him", 'Lin', "her lips pale and shaking, her eyes blazing and wide, her brows pulled high", outfit=SU_ROBE_WET),
    P('lin_home', 'right', "in the water up to his chest in profile facing frame-left, his left forearm raised in her grip, his head bent down to her", 'Su', "his jaw tight, his eyes dark and still, his brows low", outfit=LIN_ROBE_WET)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, in the rock alcove.',
   "<su_cozy> grips the wrist of <lin_home> tight with her right hand and speaks the one line to <lin_home> in a cracked urgent voice, her lips pale and shaking, her eyes blazing and wide and her brows pulled high, while <lin_home> looks down at her without moving, his jaw tight, his eyes dark and still and his brows low.",
   "苏清月右手紧紧攥住林峰的手腕，用发破急迫的声音对他说出这一句，嘴唇发白发抖、眼睛瞪大灼灼发亮、眉头高高拧起，林峰一动不动地低头看着她，下颌绷紧、眼神深暗平静、眉头压低。",
   SOUND_WRIST, AES_WRIST, lines=[('su_cozy', "水下两分钟，你没有光！", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them a curved rock wall glows faintly with blue moss and thin steam rolls off the water.',
   holds='The frame holds exactly two people: Su and Lin, in the rock alcove, nobody else.')

TA('52-06', '06｜温泉：林峰低声说阎王都收不走我，等我，然后低下头，在苏清月的额头上轻轻吻了一下', 8, HC_ALCOVE,
   [P('lin_home', 'right', "in the water up to his chest in profile facing frame-left, both hands cupping her face, his head bent down to her", 'Su', "his jaw easing, his eyes dark and fierce with a cold certainty, his brows low", outfit=LIN_ROBE_WET),
    P('su_cozy', 'left', "in the water up to her collarbone in profile facing frame-right, her face tipped up in his hands, her eyes on his face", 'Lin', "her lips trembling, her eyes shining and wide, her brows pulled together", outfit=SU_ROBE_WET)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, in the rock alcove.',
   "<lin_home> holds her face in both hands and speaks the one line to <su_cozy> in a low, fierce, steady voice, his jaw easing, his eyes dark and fierce with a cold certainty and his brows low; then he bends his head and presses his lips to her forehead for a moment, while her lips tremble, her eyes shine wide and her brows pull together and then her eyes close.",
   "林峰两手捧着她的脸，用低沉凶狠而平稳的声音对苏清月说出这一句，下颌放松、眼神深暗带着冰冷的笃定、眉头压低；然后他低下头，用嘴唇在她的额头上贴了一下，她嘴唇发颤、眼睛睁大闪着光、眉头拧在一起，然后闭上了眼睛。",
   SOUND_KISS, AES_FOREHEAD, lines=[('lin_home', "阎王都收不走我，等我。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them a curved rock wall glows faintly with blue moss and thin steam rolls off the water.',
   holds='The frame holds exactly two people: Lin and Su, in the rock alcove, nobody else.')

insert2('52-07', '07｜温泉：漆黑的水面上，几串银色的气泡慢慢升上来、一圈一圈地破开，然后水面渐渐平静下来，薄薄的蒸汽飘过', 6, HC_WATER,
        'Low close shot of the pool surface, the rising bubbles in the middle third of the frame, nobody visible.',
        "A few strings of silver bubbles rise through the dark turquoise water and burst in slow rings, then the surface smooths out and goes still while thin steam drifts over it. Nothing else moves.",
        "几串银色的气泡从深青绿色的水里升上来，一圈一圈地慢慢破开，然后水面渐渐平静下来，薄薄的蒸汽从上面飘过。别的什么都不动。",
        SOUND_BUBBLES, 'The frame holds the pool surface with the bubbles, and nobody visible.',
        push1('the last bubbles and the stilling water', '最后的气泡和渐渐平静的水面'), AES_BUBBLES)

TAV('52-08', '08｜岸边：苏清月一个人趴在岩台边，低头盯着漆黑的水面，小声地对自己说回来', HC_LEDGE_DARK,
    [P('su_cozy', 'right', "kneeling at the frost-furred edge of the ledge in profile facing frame-left, both hands pressed flat on the stone, leaning over the black water", 'obj:the still black water', "her lips pale and trembling, her eyes wide and wet, her brows pulled high", outfit=SU_ROBE_FROST)],
    'Medium close shot, one woman from the head to the waist, in the middle third of the frame, at the pool edge.',
    "<su_cozy> kneels at the edge of the ledge and stares down at the still black water, her lips pale and trembling, her eyes wide and wet and her brows pulled high, and she whispers the one line aloud to herself in a barely audible cracked voice.",
    "苏清月跪在岩台边，低头盯着一动不动的漆黑水面，嘴唇发白发颤、眼睛睁大含着泪、眉毛高高拧起，用几乎听不见的破碎声音对自己低声说出这一句。",
    SOUND_WAIT, AES_WAIT, [('su_cozy', "回来。", 0.8, 'Su')],
    cam=push1('Su and the black water', '苏清月和漆黑的水面'), room={'Su'}, new=True,
    bg='Behind her the pool lies black and still under a faint blue moss glow.',
    holds='The frame holds exactly one person: Su, at the pool edge, nobody else.')

# ================================================================================================ 第 53 集
b53 = S.episode('剧本第53集｜黑暗中的外科手术', '漆黑的水下，林峰在岩壁的细缝里摸到那根备用的超导线缆，把它拔出来；他破水而出，大口喘气，爬上岸，身上结了一层薄冰，把线缆递给苏清月；苏清月握住线缆，外科医生的眼神回来了，说剥开绝缘层，这根线只有两毫米，接错就死；林峰用匕首剥开线皮，她稳稳地对接线芯，一团蓝白色的电火花爆开；她喊接通了，去压液压杆；林峰咬牙压下杠杆，变形的合金门被顶开了一条半米宽的缝。', 53)

TA('53-01', '01｜水下：漆黑的暗河里，林峰顺着岩壁摸索，终于摸到岩缝里那根银色的细线缆，用力把它拔了出来', 8, RIVER,
   [P('lin_home', 'center', "swimming underwater in profile facing frame-right, his right hand running along the seam in the rock wall and closing on the thin silver cable, his left arm stretched forward, his hair drifting", 'obj:the thin silver cable in the rock seam', "his lips pressed tight, his jaw clenched, his eyes narrowed and fixed, his brows low", outfit=LIN_ROBE_WET)],
   'Medium shot underwater, one man from the head to the waist, in the middle third of the frame, at the rock wall.',
   "<lin_home> swims along the rock wall underwater and feels along the seam until his right hand closes on the thin silver cable, his lips pressed tight, his jaw clenched, his eyes narrowed and fixed and his brows low, and then he pulls the cable free of the seam while silver bubbles stream from his mouth and his hair drifts.",
   "林峰在水下顺着岩壁游，手沿着岩缝摸索，右手终于握住那根细细的银色线缆，嘴唇紧闭、下颌咬紧、眼睛眯起盯着、眉头压低，然后把线缆从缝里拔出来，银色的气泡从嘴边冒出来，头发飘着。",
   SOUND_DIVE, AES_DIVE, cam=push1('Lin and the cable in his hand', '林峰和他手里的线缆'), room={'Lin'}, new=True,
   bg='Behind him the rough black rock wall runs across the frame with silver bubbles rising.',
   holds='The frame holds exactly one person: Lin, underwater at the rock wall, nobody else.')

TA('53-02', '02｜岸边：苏清月趴在岩台边死死盯着水面，林峰哗啦一声破水而出，大口大口地喘气，一只拳头里攥着那根细线缆', 7, HC_LEDGE_DARK,
   [P('su_cozy', 'right', "lying flat on the frost-furred ledge at the pool edge in profile facing frame-left, her head over the water, her eyes on the surface", 'Lin', "her lips parted, her eyes huge, her brows pulled high", outfit=SU_ROBE_FROST),
    P('lin_home', 'left', "bursting up out of the water in profile facing frame-right, the water streaming off his shoulders, his right fist raised holding a thin silver cable, his mouth open gasping", 'Su', "his jaw slack with exhaustion, his eyes wide and blazing, his brows pulled together", outfit=LIN_ROBE_WET)],
   'Medium two-shot, both from the head to the chest, in the middle third of the frame, at the pool edge.',
   "<lin_home> bursts up out of the black water, gasping, with the thin silver cable gripped in his raised right fist, his jaw slack with exhaustion, his eyes wide and blazing and his brows pulled together, while <su_cozy> lies flat on the ledge right in front of him, her lips parted, her eyes huge and her brows pulled high.",
   "林峰从漆黑的水里破水而出，大口喘着气，抬起的右拳里攥着那根细细的银色线缆，下颌因脱力而松开、眼睛睁大灼灼发亮、眉头拧在一起，苏清月就趴在他面前的岩台上，嘴唇微张、眼睛瞪得很大、眉毛高高拧起。",
   SOUND_SURFACE, AES_SURFACE, cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the black pool steams and the wall of dim blue moss glows.',
   holds='The frame holds exactly two people: Lin and Su, at the pool edge, nobody else.')

TA('53-03', '03｜岸边：林峰爬上岩台，身上结了一层薄冰，把线缆递到苏清月手里，说接上它，只有你行', 7, HC_ICE,
   [P('lin_home', 'left', "kneeling on the frost-furred ledge in profile facing frame-right, his left hand holding out the thin silver cable to her, a thin skin of ice on his shoulders", 'Su', "his jaw shaking, his eyes fierce and certain, his brows low", outfit=LIN_ROBE_ICE),
    P('su_cozy', 'right', "kneeling opposite him in profile facing frame-left, both hands reaching out to take the cable, her eyes on his face", 'Lin', "her lips trembling, her eyes wide and bright, her brows pulled together", outfit=SU_ROBE_FROST)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, on the ledge.',
   "<lin_home> holds out the thin silver cable to <su_cozy> and speaks the one line to <su_cozy> in a rough hoarse voice, his jaw shaking, his eyes fierce and certain and his brows low, while <su_cozy> takes it with both hands, her lips trembling, her eyes wide and bright and her brows pulled together.",
   "林峰把细细的银色线缆递到苏清月面前，用粗哑的声音对她说出这一句，下颌发抖、眼神凶狠而笃定、眉头压低，苏清月双手接过线缆，嘴唇发颤、眼睛睁大发亮、眉头拧在一起。",
   SOUND_ICEHAND, AES_ICEHAND, lines=[('lin_home', "接上它，只有你行。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the black pool and the wall of dim blue moss lie in the dark.',
   holds='The frame holds exactly two people: Lin and Su, on the ledge, nobody else.')

TA('53-04', '04｜岸边：苏清月握住线缆的一瞬间，眼神变得极度专注，对林峰说剥开绝缘层，只有两毫米，接错就死', 10, HC_ICE,
   [P('su_cozy', 'right', "kneeling on the frost-furred ledge in profile facing frame-left, both hands holding the thin silver cable in front of her chest, her head bent over it", 'obj:the thin silver cable in her hands', "her lips pressed into a firm line, her eyes narrowed and perfectly steady, her brows low", outfit=SU_ROBE_FROST),
    P('lin_home', 'left', "kneeling beside her in profile facing frame-right, his right hand holding a slim dagger, his eyes on her face", 'Su', "his jaw set, his eyes dark and trusting, his brows low", outfit=LIN_ROBE_ICE)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, on the ledge.',
   "<su_cozy> holds the thin silver cable in both hands and speaks the first line to <lin_home> in a low steady voice and then the second line in the same cool clear voice, her lips pressed into a firm line, her eyes narrowed and perfectly steady and her brows low, while <lin_home> listens with the slim dagger in his hand, his jaw set, his eyes dark and trusting and his brows low.",
   "苏清月双手捧着细细的银色线缆，用低沉平稳的声音对林峰说出第一句，接着用同样冷静清楚的声音说出第二句，嘴唇抿成一条坚定的线、眼睛眯起稳得一动不动、眉头压低，林峰手里拿着细长的匕首听着，下颌绷紧、眼神深暗带着信任、眉头压低。",
   SOUND_SURGEON, AES_SURGEON, lines=[('su_cozy', "剥开绝缘层。", 0.8, 'Lin'), ('su_cozy', "只有两毫米，接错就死。", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them a faint blue moss glow outlines the frost-furred rock and the black pool.',
   holds='The frame holds exactly two people: Su and Lin, on the ledge, nobody else.')

TA('53-05', '05｜岸边：林峰用匕首尖极轻地剥开线缆的外皮，苏清月双手捏着露出来的线芯，手抖了一下，然后稳稳地把两根线芯对在一起', 9, HC_ICE,
   [P('lin_home', 'left', "kneeling on the ledge in profile facing frame-right, the tip of the slim dagger slicing the insulation of the thin cable held between them, his head bent over it", 'obj:the thin cable between them', "his lips pressed tight, his eyes narrowed and fixed, his brows low", outfit=LIN_ROBE_ICE),
    P('su_cozy', 'right', "kneeling opposite him in profile facing frame-left, both hands holding the two exposed cable ends and bringing them together, her head bent over them", 'obj:the two exposed cable ends in her hands', "her lips pressed into a firm line, her eyes narrowed and perfectly steady, her brows low", outfit=SU_ROBE_FROST)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, on the ledge.',
   "<lin_home> slices the insulation off the thin cable with the tip of the slim dagger, his lips pressed tight, his eyes narrowed and fixed and his brows low, then <su_cozy> holds the two bare cable ends in both hands and, after one small tremble, brings them steadily together, her lips pressed into a firm line, her eyes narrowed and perfectly steady and her brows low. Nobody speaks.",
   "林峰用匕首尖把细线缆的外皮轻轻划开，嘴唇抿紧、眼睛眯起盯着、眉头压低，然后苏清月双手捏着两根露出来的线芯，手轻轻抖了一下，接着稳稳地把它们对在一起，嘴唇抿成一条坚定的线、眼睛眯起稳得一动不动、眉头压低。没有人说话。",
   SOUND_STRIP, AES_STRIP, cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them a faint blue moss glow outlines the frost-furred rock.',
   holds='The frame holds exactly two people: Lin and Su, on the ledge, nobody else.')

insert2('53-06', '06｜岩台上：两根线芯接在一起的地方迸出一团耀眼的蓝白色电火花，照亮了周围的岩壁，然后沉成一点稳稳的小蓝光', 5, HC_ICE,
        'Close shot of the joined wires on the flat rock, the bright spark in the middle third of the frame, nobody in the scene.',
        "Two thin wires lie joined on the flat frost-furred rock and a blinding blue-white spark bursts at the joint and lights the cave wall before it settles into a small steady blue glow. Nothing else moves.",
        "两根细线接在一起放在结霜的平坦岩石上，接口处迸出一团耀眼的蓝白色电火花，照亮了溶洞的岩壁，然后沉成一点小小的、稳稳的蓝色光。别的什么都不动。",
        SOUND_SPARK, 'The frame holds the joined wires with the spark on the flat rock, and nobody in the scene.',
        push1('the joined wires and the settling blue glow', '接在一起的线头和沉下来的蓝光'), AES_SPARK)

TA('53-07', '07｜岸边：蓝光亮起，苏清月抬起头对林峰喊接通了，去压液压杆', 6, HC_ICE,
   [P('su_cozy', 'right', "kneeling on the ledge in profile facing frame-left, the joined wires glowing blue in her hands, her head up to him", 'Lin', "her lips parted in a ragged gasp, her eyes blazing and bright, her brows pulled high", outfit=SU_ROBE_FROST),
    P('lin_home', 'left', "rising from his knees in profile facing frame-right, his hand braced on the rock, his eyes on her face", 'Su', "his jaw clenched, his eyes fierce and alert, his brows low", outfit=LIN_ROBE_ICE)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, on the ledge.',
   "<su_cozy> looks up from the glowing blue wires in her hands and speaks the one line to <lin_home> in a hoarse sharp voice, her lips parted in a ragged gasp, her eyes blazing and bright and her brows pulled high, while <lin_home> starts to rise from his knees, his jaw clenched, his eyes fierce and alert and his brows low.",
   "苏清月从手里发着蓝光的线头上抬起头，用沙哑尖锐的声音对林峰说出这一句，嘴唇微张喘着粗气、眼睛灼灼发亮、眉毛高高拧起，林峰从跪着的姿势开始站起来，下颌咬紧、眼神凶狠警觉、眉头压低。",
   SOUND_SPARK, AES_CONNECTED, lines=[('su_cozy', "接通了，去压液压杆！", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the frost-furred rock and the black pool lie under a faint blue glow.',
   holds='The frame holds exactly two people: Su and Lin, on the ledge, nobody else.')

TA('53-08', '08｜门边：林峰双手攥住地上的钢制液压杆，全身的肌肉绷紧，张着嘴吼出声来，拼命往下压', 7, DOOR_LEVER,
   [P('lin_home', 'center', "standing at the steel hydraulic lever in profile facing frame-left, both hands gripping its thick handle and pushing it down with his whole body, his feet braced", 'obj:the steel hydraulic lever handle', "his teeth bared in a roar, his jaw clenched, his eyes blazing, his brows pulled low", outfit=LIN_ROBE_ICE)],
   'Medium shot, one man from the head to the knees, in the middle third of the frame, at the lever.',
   "<lin_home> grips the thick steel lever handle with both hands and drives it downward with his whole body, his teeth bared in a roar, his jaw clenched, his eyes blazing and his brows pulled low, while the cords of his neck and forearms stand out and grey dust sifts down around him.",
   "林峰双手攥住粗粗的钢制杠杆把手，用全身的力气把它往下压，龇着牙吼着、下颌咬紧、眼睛灼灼发亮、眉头压低，脖子和前臂的青筋绷出来，灰色的尘土在他周围筛落。",
   SOUND_LEVER_NV, AES_LEVER, cam=push1('Lin and the groaning lever', '林峰和发出呻吟的杠杆'), room={'Lin'}, new=True,
   bg='Behind him the crumpled grey alloy door fills the left of the frame and broken stones lie on the floor.',
   holds='The frame holds exactly one person: Lin, at the lever, nobody else.')

insert2('53-09', '09｜门边：被砸变形的灰色合金门被顶开了一条半米宽的缝，缝里透进来一线淡淡的蓝光，灰色的尘土悬在空气里，小石子往下掉', 6, DOOR_GAP,
        'Wide shot of the door, the gap in the middle third of the frame, nobody in the scene.',
        "The crumpled grey alloy door now stands forced open by a vertical gap half a metre wide and a thin slice of faint blue light slants through it while grey dust hangs in the air and small stones tick down. Nothing else moves.",
        "被砸变形的灰色合金门被顶开了一条半米宽的竖缝，一道淡淡的蓝光斜着从缝里透过去，灰色的尘土悬在空气里，小石子嘀嘀嗒嗒往下掉。别的什么都不动。",
        SOUND_GAPDOOR, 'The frame holds the door with the half-metre gap, and nobody in the scene.',
        push1('the narrow gap and the slice of light', '窄窄的门缝和那道光'), AES_GAP)

# ================================================================================================ 第 54 集
b54 = S.episode('剧本第54集｜重见光明', '林峰死死撑住液压杆，喊快钻过去；苏清月侧身挤过窄窄的门缝；门在身后彻底卡死，林峰已经躺在上层的地面上大口喘气；他踉跄着冲向备用电源箱，一把推上总闸，绿灯亮起；伊甸的声音说备用电源已激活，欢迎回家；暖黄色的灯一排排亮满整间屋子，通风口里吹出二十六度的暖风，苏清月闭着眼笑了；两人换上柔软的家居服，裹着羊绒毯子紧紧抱在一起；苏清月轻声问外面那些疯子还在吗，林峰拿起遥控器打开监控，屏幕亮起来，两个人愣住了。', 54)

TA('54-01', '01｜门边：林峰两手死死撑住液压杆，对门缝边的苏清月吼快钻过去', 7, DOOR_LEVER,
   [P('lin_home', 'right', "standing at the steel hydraulic lever in profile facing frame-left, both hands braced on the handle holding it down, his feet planted, his head turned to her", 'Su', "his teeth gritted, his jaw clenched, his eyes blazing, his brows pulled low", outfit=LIN_ROBE_ICE),
    P('su_cozy', 'left', "standing at the edge of the half-metre gap in the door in profile facing frame-right, one hand on the cold metal, her head turned to him", 'Lin', "her lips parted, her eyes wide, her brows pulled together", outfit=SU_ROBE_FROST)],
   'Medium two-shot, both from head to knees, in the middle third of the frame, at the door.',
   "<lin_home> holds the lever down with both hands and speaks the one line to <su_cozy> in a loud roaring effortful voice, his teeth gritted, his jaw clenched, his eyes blazing and his brows pulled low, while <su_cozy> stands at the edge of the gap, her lips parted, her eyes wide and her brows pulled together.",
   "林峰两手把杠杆死死压住，用吼出来的、吃力的声音对苏清月说出这一句，龇牙咬紧、下颌绷紧、眼睛灼灼发亮、眉头压低，苏清月站在门缝边上，嘴唇微张、眼睛睁大、眉头拧在一起。",
   SOUND_LEVER, AES_GAPHOLD, lines=[('lin_home', "快！钻过去！", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the crumpled grey alloy door stands forced open by a narrow gap and grey dust sifts down.',
   holds='The frame holds exactly two people: Lin and Su, at the door, nobody else.')

TA('54-02', '02｜门缝：苏清月侧着身子，一点一点挤过那条窄窄的门缝，灰色的尘土落在她的肩膀上', 6, DOOR_GAP,
   [P('su_cozy', 'center', "squeezing sideways through the narrow vertical gap in the door in profile facing frame-right, her chest and shoulder already past the metal edge, her hands pressed against the cold metal", 'obj:the dark space beyond the gap', "her lips pressed tight, her eyes wide and fixed, her brows pulled together", outfit=SU_ROBE_FROST)],
   'Medium shot, one woman from the head to the knees, in the middle third of the frame, at the gap.',
   "<su_cozy> squeezes sideways through the narrow gap in the crumpled door, her hands pressed against the cold metal and grey dust landing on her shoulders, her lips pressed tight, her eyes wide and fixed and her brows pulled together, and she slowly works her whole body through toward the dark beyond.",
   "苏清月侧着身子挤过变形的门上那条窄窄的缝，两手按着冰冷的金属，灰色的尘土落在她的肩膀上，嘴唇抿紧、眼睛睁大盯着前方、眉头拧在一起，她一点一点地把整个身子挤过去，朝着缝后面的黑暗。",
   SOUND_SQUEEZE, AES_SQUEEZE, cam=track('Su', '苏清月'), room={'Su'}, new=True,
   bg='Behind her the half-metre gap in the crumpled door shows faint blue moss light.',
   holds='The frame holds exactly one person: Su, at the gap, nobody else.')

TA('54-03', '03｜上层走廊：林峰仰面躺在漆黑的地面上大口喘气，苏清月跪在他身边，变形的合金门已经在他们身后彻底卡死', 7, DOOR_SHUT,
   [P('lin_home', 'left', "lying flat on his back on the dark concrete floor in profile, one arm thrown across his chest, his head turned toward her", 'Su', "his jaw slack with exhaustion, his eyes half-closed and bright, his brows pulled together", outfit=LIN_ROBE_ICE),
    P('su_cozy', 'center', "kneeling beside his shoulder in profile facing frame-left, one hand on his chest, her head bent over him", 'Lin', "her lips trembling, her eyes glistening and wide, her brows pulled together", outfit=SU_ROBE_FROST)],
   'Medium two-shot, both from head to waist, in the middle third of the frame, on the corridor floor.',
   "<lin_home> lies on his back on the dark concrete floor gasping, his jaw slack with exhaustion, his eyes half-closed and bright and his brows pulled together, while <su_cozy> kneels beside him with one hand on his chest, her lips trembling, her eyes glistening and wide and her brows pulled together. Nobody speaks.",
   "林峰仰面躺在漆黑的水泥地上大口喘着气，下颌因脱力而松开、眼睛半闭着发亮、眉头拧在一起，苏清月跪在他身边，一只手按在他胸口，嘴唇发颤、眼睛含着泪睁大、眉头拧在一起。没有人说话。",
   SOUND_FLOOR, AES_FLOOR, cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the crumpled alloy door is jammed shut in its bent frame with a thin dim blue line of light around its edge.',
   holds='The frame holds exactly two people: Lin and Su, on the corridor floor, nobody else.')

TA('54-04', '04｜生活区：漆黑的屋子里，林峰踉跄着扑到墙上的灰色配电箱前，用尽力气把粗杠杆推了上去，箱子上亮起一盏小小的绿灯', 8, DARK_LIVING,
   [P('lin_home', 'right', "standing at the grey breaker box on the wall in profile facing frame-right, both hands on the heavy lever and shoving it upward, his shoulder against the wall to stay upright", 'obj:the heavy lever of the grey breaker box', "his teeth gritted, his jaw clenched, his eyes burning, his brows pulled low", outfit=LIN_ROBE_ICE)],
   'Medium shot, one man from the head to the waist, in the middle third of the frame, at the breaker box.',
   "<lin_home> staggers to the grey breaker box and drives the heavy lever upward with both hands, his teeth gritted, his jaw clenched, his eyes burning and his brows pulled low, and a small green lamp lights on the box and glows on his face.",
   "林峰踉跄着走到墙上的灰色配电箱前，两手把粗杠杆用力往上推，龇牙咬紧、下颌绷紧、眼睛烧着火、眉头压低，箱子上一盏小小的绿灯亮起来，绿光落在他的脸上。",
   SOUND_BREAKER_NV, AES_BREAKER, cam=push1('Lin and the green lamp', '林峰和那盏绿灯'), room={'Lin'}, new=True,
   bg='Behind him the dark shapes of the open kitchen and the round wooden table are barely visible and the round steel hatch door stands in the wall.',
   holds='The frame holds exactly one person: Lin, at the breaker box, nobody else.')

TAV('54-05', '05｜生活区：林峰和苏清月站在刚亮起绿灯的配电箱旁，墙上的扬声器里传出伊甸温柔的声音说备用电源已激活，欢迎回家，林先生，苏女士', DARK_LIVING,
    [P('lin_home', 'right', "standing at the breaker box in profile facing frame-left, one hand still on the lever, his head tipped toward the speaker on the wall", 'obj:the wall speaker with the thin glowing blue ring', "his jaw loosening, his eyes drained and bright, his brows easing", outfit=LIN_ROBE_ICE),
     P('su_cozy', 'center', "standing beside him in profile facing frame-left, her arms wrapped around herself, her head tipped toward the speaker on the wall", 'obj:the wall speaker with the thin glowing blue ring', "her lips parting, her eyes wide and wet, her brows lifting", outfit=SU_ROBE_FROST)],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the breaker box.',
    "A soft, calm, polite female synthetic voice from the flat wall speaker with the thin glowing blue ring speaks the first line and then the second line as a voice-over to <lin_home>. <lin_home> stands with one hand still on the lever, his jaw loosening, his eyes drained and bright and his brows easing, and <su_cozy> stands beside him with her arms wrapped around herself, her lips parting, her eyes wide and wet and her brows lifting.",
    "墙上那块带着一圈细细蓝光的扁扁的扬声器里传出轻柔平静、礼貌的女性合成声音，以旁白的方式说出第一句，接着说出第二句，对着林峰说。林峰一只手还放在杠杆上，下颌松开、眼神疲惫发亮、眉头舒展，苏清月抱着自己的手臂站在他身边，嘴唇微张、眼睛睁大含着泪、眉毛抬起。",
    SOUND_EDEN, AES_EDENWAKE, [('eden_voice', "备用电源已激活。", 0.8, 'Lin'), ('eden_voice', "欢迎回家，林先生，苏女士。", 4.8, 'Lin')],
    cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
    bg='On the wall above them a flat speaker panel with a thin glowing blue ring glows and the grey breaker box glows green.',
    holds='The frame holds exactly two people: Lin and Su, at the breaker box, nobody else.')

insert2('54-06', '06｜生活区：暖黄色的灯一排排亮满了整间屋子，金色的光洒在奶油色的地毯和大理石台面上，黑金炉灶透着炭火般的橙光，屋里一个人也没有', 7, LIV_LIT,
        'Wide shot of the living area, the cream rug and the lamps in the middle third of the frame, nobody in the scene.',
        "Row after row of warm amber lamps glow across the whole underground living area, golden light pooling on the cream rug and the marble counter while the black-and-gold stove glows ember-orange and a thin curl of steam rises from a kettle. Nothing else moves.",
        "暖黄色的灯一排排亮满了整个地下生活区，金色的光洒在奶油色的地毯和大理石台面上，黑金炉灶透着炭火般的橙光，水壶里一缕薄薄的蒸汽升起来。别的什么都不动。",
        SOUND_LAMPS, 'The frame holds the lit living area, and nobody in the scene.',
        slide('toward frame-right', '右', 'the glowing stove and the warm lamps fill the frame', '发光的炉灶和暖灯占满画面'), AES_LAMPS)

TA('54-07', '07｜生活区：暖风从天花板的通风口吹下来，吹起苏清月潮湿的头发，她闭着眼睛笑了，林峰低声说二十六度，回家了', 8, LIV_VENT,
   [P('su_cozy', 'left', "standing on the cream rug in profile facing frame-right, her chin lifted and her eyes closed, her damp hair lifting in the warm air", 'closed', "her lips curving in a tired sweet smile, her brows relaxed", outfit=SU_ROBE_FROST, shut='gently closed'),
    P('lin_home', 'right', "standing beside her in profile facing frame-left, one arm around her shoulders, his head bent toward her", 'Su', "his jaw loosening, his eyes dark and warm, one corner of his mouth lifting, his brows soft", outfit=LIN_ROBE_ICE)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, on the rug.',
   "<lin_home> speaks the one line to <su_cozy> in a low warm hoarse voice, his jaw loosening, his eyes dark and warm, one corner of his mouth lifting and his brows soft, while <su_cozy> stands with her chin lifted and her eyes closed in the warm air, her lips curving in a tired sweet smile and her brows relaxed, and the frost in their hair slowly melts into drops of water.",
   "林峰用低沉温暖沙哑的声音对苏清月说出这一句，下颌放松、眼神深暗温暖、嘴角微微上扬、眉头柔和，苏清月仰着下巴闭着眼睛站在暖风里，嘴唇弯起疲惫的柔软的笑、眉头舒展，他们头发上的霜慢慢化成小水珠。",
   SOUND_WARMAIR, AES_WARMAIR, lines=[('lin_home', "二十六度，回家了。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Above them a square ceiling air vent blows warm air and behind them the black-and-gold stove glows at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, on the rug, nobody else.')

TA('54-08', '08｜沙发上：换上柔软的家居服的两个人裹着灰色的羊绒毯子，紧紧抱在一起，苏清月的头靠在林峰的胸口，谁也没有说话', 10, SOFA_HOME,
   [P('su_cozy', 'left', "sitting curled on the deep brown leather sofa in three-quarter profile facing frame-right, her head resting on his chest, the grey cashmere blanket wrapped around both of them", 'closed', "her lips softly parted, her face utterly relaxed, her brows smooth", outfit=SU_HOMEWEAR, shut='gently closed'),
    P('lin_home', 'right', "sitting on the sofa in profile facing frame-left, both arms wrapped around her, his chin resting on her hair, the blanket over his shoulders", 'closed', "his jaw loose, his lips softly closed, his brows smooth", shut='gently closed')],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, on the sofa.',
   "<su_cozy> lies curled against the chest of <lin_home> on the sofa, wrapped with him in the grey cashmere blanket, her lips softly parted, her face utterly relaxed and her brows smooth, while <lin_home> holds her tight with his chin on her hair, his jaw loose, his lips softly closed and his brows smooth, and their chests rise and fall slowly together. Nobody speaks.",
   "苏清月蜷在林峰胸口，和他一起裹在灰色的羊绒毯子里，嘴唇轻轻张开、整张脸完全放松、眉头舒展，林峰紧紧抱着她，下巴抵在她的头发上，下颌放松、嘴唇轻轻闭着、眉头舒展，两个人的胸口一起慢慢起伏。没有人说话。",
   SOUND_COZY, AES_COZY, cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the black-and-gold stove glows ember-orange at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, on the sofa, nobody else.')

TA('54-09', '09｜沙发上：苏清月靠在林峰怀里轻声问外面那些疯子还在吗，林峰从茶几上拿起遥控器', 8, SOFA_HOME,
   [P('su_cozy', 'left', "sitting curled against his side on the sofa in three-quarter profile facing frame-right, her head turned up to him, the blanket around her shoulders", 'Lin', "her lips soft, her eyes dark and uneasy, her brows drawn together", outfit=SU_HOMEWEAR),
    P('lin_home', 'right', "sitting on the sofa in profile facing frame-left, his left arm around her and his right hand lifting a black remote control from the coffee table, his head bent toward her", 'Su', "his jaw easy, his eyes dark and calm, his brows low", outfit="in a soft grey cotton henley and loose dark lounge pants")],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, on the sofa.',
   "<su_cozy> looks up at <lin_home> and speaks the one line to <lin_home> in a soft low voice, her lips soft, her eyes dark and uneasy and her brows drawn together, while <lin_home> lifts the black remote control from the coffee table with his right hand and looks down at her, his jaw easy, his eyes dark and calm and his brows low.",
   "苏清月抬头看着林峰，用轻轻低低的声音对他说出这一句，嘴唇柔软、眼神深暗带着不安、眉头微蹙，林峰右手从茶几上拿起黑色遥控器，低头看着她，下颌放松、眼神深暗平静、眉头压低。",
   SOUND_REMOTE, AES_REMOTE, lines=[('su_cozy', "外面那些疯子，还在吗？", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the black-and-gold stove glows ember-orange and a wall of dark monitors stands at frame-right.',
   holds='The frame holds exactly two people: Su and Lin, on the sofa, nobody else.')

TA('54-10', '10｜沙发上：身后的监控墙忽然亮起冷白色的光，苏清月和林峰同时转过头去看，两个人都愣住了', 6, SOFA_SCREEN,
   [P('su_cozy', 'left', "sitting on the sofa in profile facing frame-right, the blanket slipping off her shoulder, her head turned toward the monitor wall", 'obj:the bright monitor wall', "her lips falling open, her eyes wide in shock, her brows pulled high", outfit=SU_HOMEWEAR),
    P('lin_home', 'right', "sitting beside her in profile facing frame-right, the black remote control frozen in his raised hand, his head turned toward the monitor wall", 'obj:the bright monitor wall', "his jaw slackening, his eyes wide and fixed, his brows pulled together", outfit="in a soft grey cotton henley and loose dark lounge pants")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, on the sofa.',
   "<su_cozy> and <lin_home> turn their heads toward the monitor wall as it flares up with a cold white glow and then freeze, <su_cozy> with her lips falling open, her eyes wide in shock and her brows pulled high, <lin_home> with the remote frozen in his raised hand, his jaw slackening, his eyes wide and fixed and his brows pulled together. Nobody speaks.",
   "监控墙忽然亮起冷白色的光，苏清月和林峰同时把头转向它，然后都僵住了，苏清月嘴唇张开、眼睛因震惊睁大、眉毛高高抬起，林峰举起的手里遥控器停在半空，下颌松下来、眼睛睁大盯着、眉头拧在一起。没有人说话。",
   SOUND_SCREEN, AES_SCREEN, cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='In front of them the wall of small security monitors glows bright white and the warm amber room lies behind them.',
   holds='The frame holds exactly two people: Su and Lin, on the sofa, nobody else.')

doc = S.finish()
