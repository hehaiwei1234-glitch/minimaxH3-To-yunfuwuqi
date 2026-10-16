#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》补拍包 3（2026-10-16，hh 10:14：末日来临的大场面——城市被冻住、从地球视角拍几秒固定镜头、一对情侣相拥被冻成雕像）。
以 026（剧本第 55–74 集合并稿）的 JSON 为底，只新增 4 个素材（2 个太空地球、天桥活着／冻住 2 个共 3 个场景＋2 个人物），必须等 026 在插件里全部跑完再追加；追加窗口不要勾每集／总／任务秒数。
补拍2（降临全城）里已经有“城市被冻住”（雾墙吞城、地铁口、雾锋扫街、白领、冰雕街、吊臂冻城），本包补它没有的两样：
  搞笑恶搞 3 个（F-01…F-03，hh 10-16 加的：街边吃烧烤的老哥背对寒潮、对着镜头喊台词、冻成冰雕）；地球 2 个（E-01、E-02，各 6 秒，固定镜头，硬切：蓝色地球→整个地球变白）；
  情侣冰雕 3 个（C-01 相拥、白雾逼近，两句台词；C-02 同一机位已成冰雕，只拍结果；C-03 冰封天桥全景、慢慢推近，正常拍，不拉远）。
放进成片的位置（补拍2 的降临段）：E-01 放在 A-01 之前（开场）→ A-01…A-06 → C-01、C-02、C-03 → A-07…A-09 → E-02（最后一镜，全球皆冻）。
写法：A（慢）为主，一个任务一件慢的事；冻结的过程不拍（H3 做不好变化），只拍“白雾逼近”和“冻完之后的静止画面”两个状态，中间硬切；
  冰雕的开场图直接画成冰雕（冰壳、睫毛挂霜、保持相拥）；每任务一句“光和空气”；运镜：E 固定、C-01 推近、C-02 固定、C-03 推近；现场音写响（只在本脚本里开，不改公共底座）。
H3 方面的风险（交稿时单列、不算我的错）：
  · E-01／E-02 太空地球是大场景，云层“慢慢飘”可能不动；整个地球变白靠开场图，不靠视频；
  · C-01 两人相拥（双人近身，一向稳）＋远处雾墙（背景里的大场景）＋两句台词（开口晚、第二句可能挤）；
  · C-02／C-03 冰雕可能画成蜡像或塑料质感；“冰壳”可能只画成一层白粉；
  · 约一成开场图不按文字画；“中国人”的脸是否真的出对。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
import _jihan_base7 as B7
from _jihan_base7 import *
import _jihan_base8 as B8
from _jihan_base8 import *
import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407, cap=12)   # hh 2026-10-16：每个任务最长 12 秒（他开最高分辨率，15 秒容易中断）
OUT = '补拍/追加版_接在主剧后面_带全剧素材/补拍3_地球固定镜头与情侣冰雕_制作稿_追加'
S = Session('合并稿/026_第55-74集_合并_冰川墓碑到陌生人的声音_制作稿_追加.json', OUT, 96000)
B6.S = S
B7.S = S

# ---------------------------------------------------------------------------------------------- 外貌／声音
CNM = 'a Chinese man in his late twenties'
CNF = 'a Chinese woman in her late twenties'
CY_LIVE = "in a charcoal wool overcoat over a grey crewneck sweater and dark trousers, his short neat black hair tousled by the wind"
XR_LIVE = "in a long camel wool coat over a cream knit sweater, her long black hair loose and lifted by the wind"
CY_ICE = "in a charcoal wool overcoat completely sealed in clear glittering ice and thick white frost, long icicles hanging from the sleeves and the hem, his black hair stiff with white rime"
XR_ICE = "in a long camel wool coat completely sealed in clear glittering ice and thick white frost, icicles hanging from the hem, her long black hair stiff with white rime and frozen mid-air"
look('chenyu', 'Chenyu', CY_LIVE, 'steady dark-brown', 'his', eth=CNM)
look('xuran', 'Xuran', XR_LIVE, 'soft dark-brown', 'her', eth=CNF)
B7.ZN.update({'chenyu': '陈屿', 'xuran': '许然'})
CY_EN = "A warm, steady young man's voice, low and gentle, speaking clear Mandarin Chinese." + VT_EN
CY_ZH = '温暖而沉稳的年轻男声，低沉温和，普通话清楚。' + VT_ZH
XR_EN = "A soft young woman's voice, trembling a little, speaking clear Mandarin Chinese." + VT_EN
XR_ZH = '轻柔的年轻女声，微微发颤，普通话清楚。' + VT_ZH

# ---------------------------------------------------------------------------------------------- 场景
EARTH_BLUE = Scene('earth_blue', " Hard white sunlight rakes across the curve of the planet from frame-right and the stars burn steady and cold in the black.",
                   " Fixed stage layout: the great curved limb of the Earth sweeps across the lower half of the frame like a huge blue arc, deep blue oceans streaked with white spiral clouds, a thin glowing blue line of atmosphere along its edge, the sunlit side bright at frame-right and the night side dark at frame-left with faint scattered gold city lights, a thin glittering white band of polar ice at the top of the globe; the upper half of the frame is black space full of tiny stars; nobody in the scene.")
EARTH_WHITE = Scene('earth_white', " A cold white glow rakes across the curve of the planet from frame-right and the stars burn steady and cold in the black.",
                    " Fixed stage layout: the great curved limb of the Earth sweeps across the lower half of the frame like a huge pale arc, every ocean and continent buried under dull white and pale blue-grey ice and thick white swirling cloud, a thin faint blue line of atmosphere along its edge, the sunlit side bright at frame-right and the night side completely dark at frame-left with no city lights at all, a faint green aurora ring shimmering over the top of the globe; the upper half of the frame is black space full of tiny stars; nobody in the scene.")
BRIDGE = Scene('footbridge', " A low amber dusk sun glows through thin haze and a cold wind lifts loose hair and coat hems.",
               " Fixed stage layout: a long city pedestrian footbridge with a clear glass railing and a grey steel deck runs across the frame from frame-right to frame-left; below it a wide boulevard of stopped cars; a skyline of glass towers stands at the back of the frame, and over the towers at the far left end of the bridge a huge white wall of mist is rolling in; the sky is amber and grey.")
BRIDGE_FROST = Scene('footbridge_frost', " A pale dim white sun glows through a grey sky and drifting white mist lies low across the frozen city; the air is utterly still.",
                     " Fixed stage layout: a long city pedestrian footbridge with its glass railing thick with white frost and its grey steel deck coated in white rime runs across the frame from frame-right to frame-left; below it a wide boulevard of frost-white silent cars; a skyline of glass towers hung with long icicles stands at the back of the frame under drifting white mist; the sky is pale grey.")
AE = lambda en, zh: (en, zh)

mode('A')
_H.CFG['sfx_loud'] = True      # hh 10-15：现场音／环境音太弱——本脚本两种写法都写响（公共底座 mode() 里 A 还没改）

bE = S.episode('补拍3｜地球两个固定镜头＋情侣相拥冻成冰雕（插入补拍2的降临段）',
               '开场放地球固定镜头（蓝色地球），降临段中间插入一对情侣在天桥相拥、白雾逼近、同机位已成冰雕、拉远看整座冰封的天桥；最后一镜放整个地球变白。', 75)

new_scene(bE, 'earth_blue', '太空里看地球（蓝色的地球弧线横在画面下半部，白色旋涡云，右侧被阳光照亮，左侧夜面有零星金色灯火，极冠一圈白色，上半部是黑色星空）',
          'The Earth seen from space, a huge blue curved limb across the lower half of the frame with white spiral clouds, the sunlit side at frame-right, faint gold city lights on the night side at frame-left, a white polar ice band and a black star-filled sky above.',
          '从太空看到的地球：蓝色的巨大弧线横在画面下半部，白色旋涡状的云，右侧被阳光照亮，左侧夜面有零星金色灯火，极冠是一圈白色，上半部是布满星星的黑色太空。',
          'the blue curve of the Earth, the white clouds and the black starry sky')
new_scene(bE, 'earth_white', '太空里看冻住的地球（同一个构图，地球整个被白色和浅蓝灰色的冰盖住，厚厚的白云，夜面没有任何灯火，极点上方有一圈淡淡的绿色极光）',
          'The Earth seen from space in the same composition, its whole surface buried under dull white and pale blue-grey ice and thick white cloud, no city lights on the night side, and a faint green aurora ring over the pole.',
          '从太空看到的冻住的地球，构图和前一张相同，整个星球被白色和浅蓝灰色的冰盖住，云层厚白，夜面没有任何灯火，极点上方有一圈淡淡的绿色极光。',
          'the white ice-covered Earth, the aurora ring and the black starry sky')
new_scene(bE, 'footbridge', '黄昏的城市天桥（玻璃护栏、灰色钢板桥面，桥下是停住的车流，身后一排玻璃大楼，左边远处一道巨大的白色雾墙正翻过楼顶压过来）',
          'A city pedestrian footbridge at dusk with a glass railing and a grey steel deck, stopped cars on the boulevard below, glass towers behind it and a huge white wall of mist rolling over the towers at the far left.',
          '黄昏的城市行人天桥，玻璃护栏，灰色钢板桥面，桥下是停住的车流，身后是一排玻璃大楼，左边远处一道巨大的白色雾墙正翻过楼顶压过来。',
          'the glass railing, the steel deck, the stopped cars and the wall of mist at the far end')
new_scene(bE, 'footbridge_frost', '冻住的城市天桥（同一座天桥，玻璃护栏和桥面都厚厚地结满白霜，桥下是白霜覆盖的车，身后的玻璃大楼挂满长长的冰柱，白雾低低地飘着）',
          'The same city footbridge frozen solid, its glass railing and steel deck thick with white frost, frost-white cars on the boulevard below, glass towers hung with long icicles and low white mist drifting.',
          '同一座城市天桥已经冻住，玻璃护栏和钢板桥面都结着厚厚的白霜，桥下是白霜覆盖的车，身后的玻璃大楼挂满长长的冰柱，白雾低低地飘着。',
          'the frosted railing, the white rime deck, the frost-white cars and the icicle-hung towers')
new_person(bE, 'chenyu', '陈屿（二十多岁的中国男青年，炭灰色羊毛大衣，灰色圆领毛衣，短黑发，被风吹乱）', 'man',
           'A Chinese man in his late twenties with short neat black hair, a clean-shaven kind face and steady dark-brown eyes, wearing a charcoal wool overcoat over a grey crewneck sweater.',
           '一个二十多岁的中国男青年，黑色短发整齐，脸干净而温和，眼睛是沉稳的深棕色，穿着炭灰色羊毛大衣，里面是灰色圆领毛衣。',
           'short neat black hair, a clean-shaven kind face, steady dark-brown eyes, wearing a charcoal wool overcoat over a grey crewneck sweater', 'a gentle, steady expression', eth='Chinese')
new_person(bE, 'xuran', '许然（二十多岁的中国女青年，驼色长款羊毛大衣，奶白色毛衣，披着长黑发）', 'woman',
           'A Chinese woman in her late twenties with long black hair, a soft oval face and warm dark-brown eyes, wearing a long camel wool coat over a cream knit sweater.',
           '一个二十多岁的中国女青年，披着黑色长发，脸型柔和偏椭圆，眼睛是温暖的深棕色，穿着驼色长款羊毛大衣，里面是奶白色毛衣。',
           'long black hair, a soft oval face, warm dark-brown eyes, wearing a long camel wool coat over a cream knit sweater', 'a soft, gentle expression', eth='Chinese')
bE.character('Chenyu', 'chenyu', CY_EN, CY_ZH)
bE.character('Xuran', 'xuran', XR_EN, XR_ZH)

# ================================================================================================ 地球 E-01
INS('E-01', '01｜太空：蓝色的地球静静悬在黑色星空里，白色的云慢慢飘过海洋，右边被太阳照亮，左边夜面有零星的金色灯火（固定镜头）', 6, EARTH_BLUE,
    'Wide shot of the Earth from space, the blue curve across the lower half of the frame and the globe centered in the middle third of the frame, nobody in the scene.',
    "The Earth hangs silent in the black star-filled space, white spiral clouds drifting very slowly over the deep blue oceans, the sunlit edge glowing at frame-right and a few faint gold city lights twinkling on the dark side at frame-left. Nothing else moves.",
    "地球静静地悬在布满星星的黑色太空里，白色的旋涡状云慢慢地飘过深蓝色的海洋，右边的边缘被太阳照得发亮，左边的夜面有几点零星的金色城市灯火在闪。别的什么都不动。",
    Q('A deep, low, silent hum of space and, far underneath it, one faint distant rumble like the planet drawing a slow breath.', '太空里深深的、低低的寂静嗡鸣，最底下隐隐有一声遥远的低沉轰鸣，像这颗星球缓缓吸了一口气。'),
    'The frame holds the Earth, the stars, and nobody in the scene.',
    FIX,
    AE("Hard white sunlight rakes along the thin blue line of atmosphere and the edges of the clouds glow like silver while the stars burn steady in the deep black.",
       "刺眼的白色阳光沿着那一线薄薄的蓝色大气划过，云的边缘像银子一样发亮，星星在深深的黑色里稳稳地燃着。"))

# ================================================================================================ 情侣 C-01
DL('C-01', '01｜天桥：黄昏的天桥上，陈屿紧紧抱着许然，远处一道白色的雾墙正翻过楼顶压过来，他低声说别怕，她说别松手', BRIDGE,
   [P('chenyu', 'center-right', "standing on the steel deck of the footbridge in profile facing frame-left, both arms wrapped around Xuran's back with both hands holding her shoulder blades, his chin resting lightly against her forehead", 'Xuran', "his jaw set, his eyes steady and gentle, his brows level", outfit=CY_LIVE),
    P('xuran', 'center-left', "standing in profile facing frame-right pressed against his chest, both hands gripping the back of his overcoat, her face tilted up toward his", 'Chenyu', "her lips trembling, her eyes wide and wet, her brows drawn together", outfit=XR_LIVE)],
   'Medium shot, the two of them from the head to the knees, in the middle third of the frame, on the bridge.',
   [('chenyu', "别怕，我在这儿。", 'xuran', 'low gentle', '低沉温和'),
    ('xuran', "嗯。别松手。", 'chenyu', 'soft trembling', '轻柔发颤')],
   V('A cold wind whistling across the bridge, the rustle of coats and a low far rumble of the mist rolling closer.', '冷风掠过天桥的呼啸声、大衣衣料的摩擦声和远处雾墙滚过来的低沉轰鸣。'),
   AE("A low amber sun rims their faces and her wind-blown hair with gold while the huge white wall of mist behind them glows cold blue-white, a rich amber-and-teal contrast.",
      "低低的琥珀色夕阳给他们的脸和被风吹起的头发勾上一圈金边，他们身后那一大片白色雾墙泛着冷冷的蓝白色，形成浓郁的琥珀与青色对比。"),
   pre_en="Far behind them at the left end of the bridge the huge white wall of mist rolls steadily over the glass towers toward the bridge while a cold wind whips her hair and the hem of his overcoat; the two of them hold each other,",
   pre_zh="他们身后桥的左边尽头，一大片白色雾墙稳稳地翻过玻璃大楼朝天桥压过来，冷风吹起她的头发和他大衣的下摆；两个人紧紧抱着彼此，",
   post_en='after the last line he tightens his arms around her and she closes her eyes and presses her face against his chest while the first thin tendrils of white mist crawl across the deck beside their feet',
   post_zh='最后一句之后，他把手臂收得更紧，她闭上眼睛把脸埋进他的胸口，第一缕薄薄的白雾顺着桥面爬到他们的脚边',
   cam=push('the two of them', '两人'), bg='A huge white wall of mist fills the far end of the bridge behind them.', tail=2.0)

# ================================================================================================ 情侣 C-02
TAA('C-02', '02｜天桥：同一个机位，两个人已经成了冰雕，保持着相拥的样子，睫毛挂着白霜，白雾静静飘过他们的脚边', 8, BRIDGE_FROST,
    [P('chenyu', 'center-right', "standing on the frost-white deck of the footbridge in profile facing frame-left, both arms wrapped around Xuran's back with both hands holding her shoulder blades, his chin resting lightly against her forehead", 'closed', "his face calm under a layer of white frost, tiny ice crystals clinging to his lashes and brows", outfit=CY_ICE, shut='gently closed'),
     P('xuran', 'center-left', "standing in profile facing frame-right pressed against his chest, both hands gripping the back of his overcoat, her face tilted up toward his", 'closed', "her face calm and peaceful under a layer of white frost, one tiny frozen tear on her cheek", outfit=XR_ICE, shut='gently closed')],
    'Medium shot, the two of them from the head to the knees, in the middle third of the frame, on the bridge.',
    "<chenyu> and <xuran> stand perfectly still in the same embrace as before, sealed in clear glittering ice, their faces calm under a layer of white frost, their breath no longer clouding. Nothing moves except thin white mist drifting slowly past their feet and a few fine ice crystals glittering in the air.",
    "陈屿和许然保持着刚才同样的拥抱，一动不动，被封在晶莹发亮的冰里，脸被一层白霜盖着，平静，嘴里不再冒白气。只有薄薄的白雾慢慢飘过他们的脚边，空气里几粒细小的冰晶在闪。",
    Q('A deep hush, one thin breath of wind and, very faint, the tick of ice settling around them.', '深深的寂静，一缕细细的风声，和很轻很轻的、冰在他们身边凝紧的细响。'),
    AE("A pale cold sun refracts through the clear ice around them, casting faint prismatic glints onto the white deck, and the frozen embrace glows softly blue-white against the dim grey towers.",
       "一轮苍白冰冷的太阳透过他们周身的透明冰层折出淡淡的彩虹光斑，落在白色的桥面上，冻住的拥抱泛着柔和的蓝白色光，衬着身后暗灰色的大楼。"),
    holds='The frame holds the two of them frozen in their embrace, the frosted bridge and the icicle-hung towers.',
    cam=FIX)

# ================================================================================================ 情侣 C-03
TAA('C-03', '03｜天桥：冰封天桥的全景，桥中间两个相拥的冰雕小小的立在那里，白雾在桥面上慢慢飘，镜头缓缓推近', 8, BRIDGE_FROST,
    [P('chenyu', 'center-right', "standing on the frost-white deck of the footbridge in profile facing frame-left, both arms wrapped around Xuran's back with both hands holding her shoulder blades, his chin resting lightly against her forehead", 'closed', "his face calm under a layer of white frost, tiny ice crystals clinging to his lashes and brows", outfit=CY_ICE, shut='gently closed'),
     P('xuran', 'center-left', "standing in profile facing frame-right pressed against his chest, both hands gripping the back of his overcoat, her face tilted up toward his", 'closed', "her face calm and peaceful under a layer of white frost, one tiny frozen tear on her cheek", outfit=XR_ICE, shut='gently closed')],
    'Wide shot of the whole footbridge, the two frozen figures small in the middle third of the frame, on the bridge.',
    "<chenyu> and <xuran> stand sealed in clear ice in their embrace at the centre of the frozen footbridge, perfectly still, while thin white mist drifts slowly across the frost-white deck. Below the bridge the boulevard is lined with frost-white silent cars, and behind it the glass towers hang with long icicles.",
    "陈屿和许然保持着拥抱，被封在晶莹的冰里，立在冰封天桥的正中间，一动不动，薄薄的白雾慢慢飘过白霜覆盖的桥面。桥下的大街两边是白霜覆盖的、一片寂静的车，身后的玻璃大楼挂满长长的冰柱。",
    Q('A deep hush, the long low sigh of the wind across the empty bridge and one faint far crack of ice from the towers.', '深深的寂静，风掠过空空的天桥长长低低的叹息，和远处大楼上传来的一声很轻的冰裂声。'),
    AE("A pale dim sun hangs low behind the icicle-hung towers and their long cold shadows stretch across the frost-white deck while fine ice crystals glitter like dust in the still air.",
       "一轮苍白暗淡的太阳低低地挂在挂满冰柱的大楼后面，长长的冷色影子横过白霜覆盖的桥面，细小的冰晶像灰尘一样在静止的空气里闪。"),
    holds='The frame holds the two frozen figures at the centre of the frosted bridge, the frost-white cars and the icicle-hung towers.',
    cam=push('the two frozen figures', '两个冰封的身影'))

# ================================================================================================ 地球 E-02
INS('E-02', '02｜太空：同一个构图，整个地球已经被白色的冰盖住，云层厚白，夜面没有一点灯火，极点上空一圈淡淡的绿色极光（固定镜头）', 6, EARTH_WHITE,
    'Wide shot of the Earth from space, the pale curve across the lower half of the frame and the globe centered in the middle third of the frame, nobody in the scene.',
    "The Earth hangs silent in the black star-filled space, its whole surface buried under dull white and pale blue-grey ice, thick white cloud bands creeping very slowly over it, the dark side without a single light and a faint green aurora ring pulsing gently over the pole. Nothing else moves.",
    "地球静静地悬在布满星星的黑色太空里，整个表面被灰白和浅蓝灰色的冰盖住，厚厚的白色云带慢慢地爬过，夜面没有一点灯火，极点上空一圈淡淡的绿色极光在轻轻地一明一暗。别的什么都不动。",
    Q('A deep, low, silent hum of space, a long faint groan of ice settling and then a stillness that goes on and on.', '太空里深深的、低低的寂静嗡鸣，一声长长的、很轻的冰层凝紧的呻吟，然后是一片绵绵不断的寂静。'),
    'The frame holds the white Earth, the stars, and nobody in the scene.',
    FIX,
    AE("A cold white glow rims the frozen planet and the thin green aurora ring shimmers over its pole while the dark side lies in total blackness among the steady stars.",
       "一圈冷冷的白光勾着冻住的星球，细细的绿色极光环在极点上空闪着，夜面完全沉在黑暗里，星星稳稳地亮着。"))

# ================================================================================================ 搞笑恶搞（hh 2026-10-16 10:24）
new_scene(bE, 'bbq_street', '正午的城市街边烧烤位（路边一张矮折叠桌，桌上纸盘里的烤串和一瓶啤酒，塑料凳，左边一个冒烟的炭烤炉，身后是一条两边停着车、种着行道树、立着玻璃大楼的长街，远处一道巨大的白色雾墙正滚过来）',
          'A roadside barbecue spot on a wide city street at noon, a low folding table with a paper plate of skewers and a beer bottle, a plastic stool, a smoking charcoal grill at the left, and behind it a long street lined with parked cars, street trees and glass towers with a huge white wall of mist rolling in at the far end.',
          '正午城市宽街上的路边烧烤位：一张矮折叠桌，桌上纸盘里放着烤串和一瓶啤酒，一个塑料凳，左边一个冒着烟的炭烤炉，身后是一条两边停着车、种着行道树、立着玻璃大楼的长街，街的尽头一道巨大的白色雾墙正滚过来。',
          'the low table, the skewers, the grill and the long street with the wall of mist at its end')
new_scene(bE, 'bbq_street_frost', '冻住的街边烧烤位（同一个位置，矮桌、塑料凳、烤炉和整条街的车、树、玻璃大楼全部结满白霜，大楼挂着长长的冰柱，白雾低低地飘着）',
          'The same roadside barbecue spot frozen solid, the low table, plastic stool, grill, parked cars, street trees and glass towers all coated in thick white frost and hung with icicles, low white mist drifting along the street.',
          '同一个街边烧烤位已经冻住，矮桌、塑料凳、烤炉、整条街的车、行道树和玻璃大楼都结着厚厚的白霜，挂着长长的冰柱，白雾低低地飘在街上。',
          'the frosted table, stool, grill, cars, trees and icicle-hung towers')
new_person(bE, 'street_guy', '街边吃烧烤的老哥（三十多岁，圆脸，乱糟糟的短发和胡茬，红黄相间的花衬衫，金链子，人字拖，爱凑热闹的样子）', 'man',
           'A stocky cheerful Chinese man in his thirties with a round face, messy short black hair and a scruffy stubble beard, wearing a loud red-and-yellow floral beach shirt, a thin gold chain and flip-flops.',
           '一个三十多岁、敦实又爱热闹的中国男性，圆脸，乱糟糟的黑色短发，满脸胡茬，穿着红黄相间的花衬衫，戴着一条细金链子，脚上是人字拖。',
           'a round face, messy short black hair, a scruffy stubble beard, wearing a loud red-and-yellow floral beach shirt and a thin gold chain', 'a cheerful, goofy expression', eth='Chinese')
look('street_guy', 'Streetguy', "in a loud red-and-yellow floral beach shirt with a thin gold chain and flip-flops, his messy short black hair and stubble beard", 'bright dark-brown', 'his', eth='a Chinese man in his thirties')
SG_ICE = "in a loud floral beach shirt completely sealed in clear glittering ice and thick white frost, icicles hanging from his sleeves and the table edge, his messy black hair stiff with white rime"
SG_EN = "A loud, gravelly, hilariously excitable Chinese man's voice, booming and cracking with comic glee, speaking clear Mandarin Chinese." + VT_EN
SG_ZH = '洪亮、沙哑、爱起哄的中国男声，兴奋得破音，带着滑稽的狂喜，普通话清楚。' + VT_ZH
bE.character('Streetguy', 'street_guy', SG_EN, SG_ZH)
STREET = Scene('bbq_street', " A bright hot noon sun beats down and cooking smoke drifts lazily through the heat.",
               " Fixed stage layout: a low folding table with a paper plate of skewers and a beer bottle and a plastic stool stand in the middle of the frame, a smoking charcoal grill at frame-left; behind the table a long wide city street recedes down the middle of the frame lined with parked cars, green street trees and glass towers, and a huge white wall of mist is rolling toward the camera at the far end of the street.")
STREET_NEAR = Scene('bbq_street', STREET.end,
                    " Fixed stage layout: a low folding table with a paper plate of skewers and a beer bottle and a plastic stool stand in the middle of the frame, a smoking charcoal grill at frame-left; behind the table the huge white wall of mist has rolled up close and fills the back half of the street, frost racing white across the parked cars and the street trees right behind the table.")
STREET_FROST = Scene('bbq_street_frost', " A pale dim white sun glows through a grey sky and drifting white mist lies low along the frozen street; the air is utterly still.",
                     " Fixed stage layout: a low folding table, a plastic stool and a charcoal grill at frame-left stand in the middle of the frame, all coated in white frost; behind them a long wide city street of frost-white silent cars, white frozen street trees and glass towers hung with long icicles recedes down the middle of the frame under drifting white mist.")

bF = S.episode('补拍3b｜搞笑恶搞：街边吃烧烤的老哥背对寒潮，对着镜头喊台词，冻成冰雕（插入补拍2的降临段，放在人群奔跑之后、落地窗之前）',
               '正午街边，老哥坐在塑料凳上美滋滋吃烧烤，镜头在他前面，身后远处一道白色雾墙滚过来；雾墙逼近，车和树一路结霜，他停住嚼的动作，对着镜头喊“卧槽，大场面，大制作啊。我看到显卡在燃烧！”，然后耸肩继续吃；同一机位，他已经冻成冰雕，手里还举着烤串、咧着嘴竖着大拇指。', 76)
mode('B')

TAA('F-01', '01｜街边烧烤：老哥坐在塑料凳上美滋滋地吃烤串，腮帮子鼓鼓的，身后街的尽头一道白色雾墙正滚过来，他没发现', 6, STREET,
    [P('street_guy', 'center', "sitting on the plastic stool at the low table front-on to the viewer, a skewer in his right hand raised to his mouth and a beer bottle in his left hand resting on the table", 'obj:the skewer in his hand', "his cheeks bulging with food, his eyes half closed in bliss, his brows relaxed", outfit=None)],
    'Medium shot, the man from the head to the waist, in the middle third of the frame, at the table.',
    "<street_guy> tears a piece of meat off the skewer with his teeth and chews it with a blissful, goofy face, then lifts the beer bottle and takes a swig. Far behind him at the end of the street the huge white wall of mist rolls steadily closer and he has not noticed.",
    "老哥用牙从串上撕下一块肉，美滋滋地嚼着，一脸傻乐，然后拿起啤酒瓶灌了一口。他身后街的尽头，一大片白色雾墙稳稳地朝这边滚过来，他一点都没发现。",
    Q('The sizzle of the charcoal grill, happy loud munching and, far behind, a low rumble rolling closer.', '炭烤炉滋滋的响声、大声又满足的咀嚼声，和远处越来越近的低沉轰鸣。'),
    AE("Hard white noon sun glints on the beer bottle and the greasy skewers while blue smoke curls off the grill, and the far wall of mist glows cold white against the hot bright street.",
       "刺眼的白色正午阳光在啤酒瓶和油亮的烤串上闪光，蓝色的烟从炭烤炉里卷出来，远处的雾墙泛着冷冷的白色，和这条热烘烘的亮堂堂的街形成对比。"),
    holds='The frame holds the man at the table, the grill and the long street with the wall of mist far behind him.',
    cam=push1('the man', '这个男人'))

DL('F-02', '02｜街边烧烤：雾墙逼近，车和树一路结霜，老哥突然停住，对着镜头喊卧槽大场面大制作啊，我看到显卡在燃烧，喊完耸耸肩继续啃', STREET_NEAR,
   [P('street_guy', 'center', "sitting on the plastic stool at the low table front-on to the viewer, a skewer held in his raised right hand an inch from his mouth and his left hand gripping the edge of the table", 'obj:the camera lens like a presenter', "his eyes bulging, his jaw dropped and his eyebrows shooting up in over-the-top comic awe", verb='staring straight at', outfit=None)],
   'Medium shot, the man from the head to the waist, in the middle third of the frame, at the table.',
   [('street_guy', "卧槽，大场面，大制作啊。", 'viewer', 'booming, hilariously over-excited', '洪亮、夸张又兴奋'),
    ('street_guy', "我看到显卡在燃烧！！！", 'viewer', 'screaming with comic glee', '带着滑稽的狂喜大喊')],
   V('The roar of the rolling mist, the crackling snap of frost racing over cars and the crunch of ice behind him.', '雾墙滚过来的呼啸、霜在车上飞快蔓延的噼啪脆响和他身后冰层咔咔作响的声音。'),
   AE("The huge white wall of mist fills the back of the frame and throws a cold blue-white glow over his face, while the warm orange glow of the grill still rims his round cheeks and a frost-white shine races across the cars and trees behind him.",
      "巨大的白色雾墙占满了画面后半部，把冷冷的蓝白光打在他的脸上，炭烤炉温暖的橙光还在勾着他圆圆的脸颊，他身后的车和树上飞快漫过一层白霜的光。"),
   pre_en="Behind him the huge white wall of mist races down the street while frost whitens the parked cars and street trees one after another; he freezes with the skewer an inch from his mouth, turns his wide eyes straight into the camera and",
   pre_zh="他身后，巨大的白色雾墙沿着街飞快压过来，停着的车和行道树一辆接一辆、一棵接一棵地变白；他举着烤串停在离嘴一寸远的地方，瞪圆了眼睛直直地看向镜头，",
   post_en='after the last line he shrugs, jams the skewer into his mouth and keeps chewing while frost creeps over the back of his stool and white mist rolls across the street behind him',
   post_zh='最后一句之后，他耸耸肩，把烤串塞进嘴里继续嚼，霜顺着他身后的凳子爬上来，白雾扫过他的肩膀',
   cam=FIX, ld={'viewer': ('straight into the camera lens like a presenter', '正对着镜头像主持人一样')}, bg='A huge white wall of mist fills the back half of the street behind him.', tail=1.5)

TAA('F-03', '03｜街边烧烤：同一个机位，老哥已经成了冰雕，咧着嘴，一手举着烤串一手竖大拇指，镜头缓缓升高，整条街都冻住了', 8, STREET_FROST,
    [P('street_guy', 'center', "sitting on the plastic stool at the low table front-on to the viewer, a skewer in his right hand held in front of his open mouth and his left thumb raised high", 'obj:the camera lens', "his mouth stretched in a frozen goofy grin, his eyes bulging, white frost over his hair and stubble", verb='staring straight at', outfit=SG_ICE)],
    'Medium shot, the man from the head to the waist, in the middle third of the frame, at the frosted table.',
    "<street_guy> sits perfectly still on the stool, sealed in clear glittering ice with a frozen goofy grin, a skewer in his right hand and his left thumb raised, his breath no longer clouding. Nothing moves except thin white mist drifting past the frosted table. The camera rises, revealing behind him the whole street of frost-white cars, frozen trees and icicle-hung towers.",
    "老哥一动不动地坐在凳子上，被封在晶莹发亮的冰里，脸上凝固着一个傻乎乎的咧嘴笑，右手举着烤串，左手高高竖着大拇指，嘴里不再冒白气。只有薄薄的白雾慢慢飘过结霜的桌子。镜头升高，露出他身后整条街白霜覆盖的车、冻住的树和挂满冰柱的大楼。",
    Q('A deep hush, one thin breath of wind and a tiny tick of ice settling, then the faint far crack of a frozen tree.', '深深的寂静，一缕细细的风声，一声极小的冰层凝紧的细响，然后远处一棵冻住的树传来一声很轻的开裂声。'),
    AE("A pale cold sun refracts through the clear ice around him, casting faint prismatic glints onto the frosted table, and the frozen goofy grin glows softly blue-white against the dim grey street.",
       "一轮苍白冰冷的太阳透过他周身的透明冰层折出淡淡的彩虹光斑，落在结霜的桌子上，那个冻住的傻乎乎的笑容泛着柔和的蓝白色光，衬着暗灰色的街道。"),
    holds='The frame holds the frozen man at the frosted table, and the frost-white street behind him.',
    cam=rise('the whole frozen street with the small frozen man at the table in front of it', '整条冰封的街和前面桌边那个小小的冻住的男人'))

doc = S.finish()
report()
