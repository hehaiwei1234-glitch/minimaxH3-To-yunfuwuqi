#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 47–50 集，追加稿 019（2026-10-15）——接在 018（第 45–46 集）后面。
hh 2026-10-15 11:02：“你继续写内容吧，现在确保能先把内容执行完成。”
以 018 的 JSON 为底（style／素材／角色逐字复制），必须等 018 在插件里全部跑完再追加。
写法＝018 的 15 秒满内容（对白任务 12–15 秒、句间 0.9 秒、结尾带动作、每任务一句光和空气、运镜每任务不同；画外音和画面里的人混排）。

内容（取自 70 集大纲第 47–50 集）：
  第 47 集 暴风雪前的顶级晚餐：独眼统帅在重型指挥车里下令全速前进 → 暖屋里煎鹅肝 → 苏清月问为什么不设伏、林峰说那是最蠢的笑话 →
            暴风雪里的黑血车队 → 林峰在全息台前说四重伪装 → 炮响、吊灯晃，伊甸报告，林峰“启动深雪地狱协议”。
  第 48 集 深雪地狱：迫击炮轰雪丘、独眼骂“门呢” → 几百人散开找 → 小头目踩上平整的雪（只拍裂纹，再拍窟窿）→ 林峰给苏清月剥橘子、监控墙红点一个个灭
            → 独眼说“把温压弹拉上来”→ 伊甸警报：正上方引爆温泉岩层六成塌方。
  第 49 集 雪原幽灵：林峰“几只虫子得亲手捏死”→ 穿白色吉利服出门（伏笔：最后一道手动闸门只有他的手能关）→ 趴着爬进暴风雪 → 爆破组在组装温压弹 →
            弩箭 → 圈里没人了 → 组长被捂住 → 林峰从雪里站起拆下起爆器 → 风吹开雪雾，独眼和上百个暴徒就在二十米外。
  第 50 集 绝对零度的恐慌：独眼“开火”、林峰按下副开关 → 强光致盲＋白烟 → 烟散后雪地空了，独眼“他是山里的鬼”→ 暴徒溃逃 →
            缓冲舱里苏清月给他擦霜（伏笔：他的手冰得吓人）→ 去泡温泉 → 起爆器的红灯亮、杯中水起波纹（次声波）→ 溶洞顶的岩石裂开。
偏离大纲（交稿时已告诉 hh）：
  · 小头目掉进冰窟只拍裂纹和后来的窟窿（不拍掉下去、不拍捅穿）；温压弹爆破组被杀不拍血和刀，只拍弩箭飞出去、圈里变空、组长被捂住拖进雪里；
  · 第 50 集“滑落回地下”不拍，只拍烟散后雪地空空、没有脚印；“温压弹弹壳亮灯”改成林峰带回来的起爆器亮灯（弹留在外面）；
  · 苏清月的橘子：农场新结的第一批橘子（给养成再加一样作物）；林峰的手冰得吓人是给结局埋的伏笔。
H3 方面的风险（交稿时单列，不算我的错）：
  · 47-01 指挥车颠簸；48-01 迫击炮连发雪柱（大场面）；48-03 脚下雪壳裂开；48-04 窟窿里落下的步枪和“叫声”；48-06 监控墙里套着的红点屏幕；
  · 49-02 厚重的暗门被风推开（机械变化）；49-03 白衣人趴在雪里几乎看不见；49-05 弩箭飞出（快动作）；49-07 组长被捂住拖进雪里（快动作＋雪里钻出来）；
  · 49-09、50-01 上百个暴徒（多个小人）；50-02 强光＋白烟（特效）；50-04 溃逃的人群；50-07 起爆器亮灯＋水杯起波纹；50-08 岩顶裂开（大场面）；
  · 15 秒任务可能在约 8 秒自己切镜；后几句台词可能被挤到片尾；约一成开场图不按文字画；画外音可能被画成多出一个人。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
from _jihan_base6 import *
import _scene
from _scene import smooth_text, TONE_FIX
import _h3draft as _H

_H.configure(smooth=True, fixed_seed=37407)
OUT = '合并稿/019_第47-50集_顶级晚餐深雪地狱雪原幽灵绝对零度_制作稿_追加'
S = Session('合并稿/018_第45-46集_十五秒满内容先行测试版_制作稿_追加.json', OUT, 70000)
B6.S = S

# ---------------------------------------------------------------------------------------------- 本批的台词排时间（同 018）
GAP = 0.9
BRISK_EN = ' The lines follow one another at once with only a very short breath between them, each said in one breath with no pause inside the sentence.'
BRISK_ZH = ' 台词一句紧接着一句，中间只有很短的换气，每句一口气说完、句中不停顿。'
VOICE_ONLY = {'eden_voice'}
VT = ' Every word is fully voiced and audible.'


def times(spec):
    out, t = [], 0.6
    for sp, tx, to in spec:
        tx2 = smooth_text(tx)
        out.append((sp, tx2, round(t, 2), to))
        t = t + _H.line_seconds(tx2) + GAP
    return out


def smooth15(lines, dur, act_en, zh):
    new = times([(a, b, d) for a, b, c, d in lines])
    for a, b in TONE_FIX: act_en = act_en.replace(a, b)
    return new, dur, act_en + BRISK_EN, zh + BRISK_ZH


_scene.smooth_task = smooth15


def MIX(spec):
    allv = times(spec)
    on = [x for x in allv if x[0] not in VOICE_ONLY]
    off = [x for x in allv if x[0] in VOICE_ONLY]
    return on, off


def LN(*spec):
    """画面里的人的台词：spec = [(look, text, to)] → TA 的 lines 参数（起点已按 15 秒写法排好）。"""
    return times(list(spec))


# ---------------------------------------------------------------------------------------------- 外貌／声音（018 里已有的）
look('eden_voice', 'Eden', "a flat wall speaker panel with a thin glowing blue ring", 'none', 'its')
LIN_ROBE = "in a thick grey terry bathrobe tied at the waist, his black hair damp"
CN_M40 = 'a Chinese man in his forties'

# 本批新人物
look('duyan_boss', 'Duyan', "in a heavy black fur-collared military greatcoat with a red armband, a black leather patch over his left eye and frost crusted in his stubble", 'cold hard dark', 'his', eth='a gaunt scarred Chinese man in his forties')
look('pang_aide', 'Pang', "in a dirty white-and-grey winter camouflage parka with the hood up and a frosted scarf pulled down under his chin", 'nervous dark', 'his', eth='a stocky Chinese man in his thirties')
look('tou_thug', 'Tou', "in a stained grey-white padded coat with a rifle slung across his chest and a frosted scarf over his nose", 'wary bloodshot', 'his', eth='a lean Chinese man in his thirties')
look('qian_chief', 'Qian', "in a bulky olive-drab padded coverall with a tool belt, thick fur-lined gloves and a frosted knitted mask rolled up over his nose", 'tense squinting dark', 'his', eth=CN_M40)
look('xiaoliu_bomber', 'Xiaoliu', "in an olive-drab padded coverall and a fur-lined hat with ear flaps, thick gloves, his cheeks raw red from the cold", 'watery dark', 'his', eth='a young Chinese man in his twenties')
look('lin_ghillie', 'LinGhillie', "in a pure-white ghillie suit of frayed white strips with the hood up over a charcoal henley, white thermal goggles pushed up on his forehead and a white scarf around his chin", 'steady dark-brown', 'his', eth=CN30)

DUYAN_EN = 'A harsh, gravelly adult male voice, ragged from shouting in the cold, cruel and commanding, speaking clear Mandarin Chinese.' + VT
DUYAN_ZH = '粗哑沙哑的成年男声，在寒风里吼得发破，残忍又带着命令的口气，普通话清楚。每个字都正常发声、清晰可辨。'
PANG_EN = 'A tense adult male voice, thin and nervous, speaking clear Mandarin Chinese.' + VT
PANG_ZH = '紧张的成年男声，细而发紧，普通话清楚。每个字都正常发声、清晰可辨。'
TOU_EN = 'A wary adult male voice, low and hoarse, speaking clear Mandarin Chinese.' + VT
TOU_ZH = '警惕的成年男声，低沉沙哑，普通话清楚。每个字都正常发声、清晰可辨。'
QIAN_EN = 'A rough, hoarse middle-aged male voice, gruff and irritable, speaking clear Mandarin Chinese.' + VT
QIAN_ZH = '粗哑的中年男声，粗声粗气、不耐烦，普通话清楚。每个字都正常发声、清晰可辨。'
XIAOLIU_EN = 'A shivering young adult male voice, cracked by the cold, speaking clear Mandarin Chinese.' + VT
XIAOLIU_ZH = '冻得发抖的年轻成年男声，被寒冷弄得发破，普通话清楚。每个字都正常发声、清晰可辨。'

# ---------------------------------------------------------------------------------------------- 场景
WAR_CAB = Scene('war_cab', " Cold green navigation-screen glow and frost-blue storm light fill the cramped cab of a heavy armoured command vehicle.",
                " Fixed stage layout: a cramped armoured cab seen from the side; two padded steel bench seats face each other across a narrow steel table in the middle of the frame with a glowing green navigation screen set into its top, the commander's seat at frame-left and the aide's seat at frame-right; a small frost-crusted porthole in the back wall shows a white roaring blizzard; a black radio handset hangs on a hook above the commander's seat.")
KITCH_SEAR = Scene('bunker_living', LIVING.end,
                   " Fixed stage layout: a close view of the black-and-gold stove at frame-left with a black iron pan on it, the marble counter in the middle of the frame with an open bottle of red wine and a crystal decanter on it, two long-stemmed glasses and a white plate beside them; the cream rug and the round wooden table blur softly behind.")
KITCH_BAR = Scene('bunker_living', LIVING.end,
                  " Fixed stage layout: the marble counter fills the middle of the frame with a cutting board, a black iron pan holding two golden-seared slices of foie gras, a crystal decanter of red wine and two long-stemmed glasses on it; the black-and-gold stove is at frame-left behind it; a high wooden stool stands at the counter at frame-left; the wall of small security monitors is at frame-center-right.")
STORM_COL = Scene('snow_field', " A black night in a roaring blizzard, thick snow swirling in the light of headlights.",
                  " Fixed stage layout: a vast flat snowfield in a roaring blizzard; a very long column of black heavy armoured tracked vehicles with spiked front plates and towed howitzers grinds across it from frame-right toward frame-left, their headlights boring tunnels into the swirling snow and thick ice crusting their hulls; there is no building anywhere.")
CTRL_HOLO = Scene('bunker_control', CONTROL.end,
                  " Fixed stage layout: a round holographic projection table stands in the middle of the frame showing a glowing pale-blue three-dimensional contour model of a snowy mountain range with four thin concentric rings marked around one peak; the wall of six small monitors is at frame-left; the heavy steel door is in the right wall at frame-right.")
LIV_BOOM = Scene('bunker_living', LIVING.end,
                 " Fixed stage layout: the open kitchen with the black-and-gold stove is at frame-left; the marble counter stands in the middle of the frame with a crystal decanter and two wine glasses of red wine on it, a pendant lamp hanging above it; a wall of small security monitors showing white blizzards is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
SHELL = Scene('snow_field', " A black night in a howling blizzard, orange flashes lighting the swirling snow.",
              " Fixed stage layout: a low rounded snow mound rises in the middle of the frame and explodes upward in columns of white snow; three black mortar tubes stand in a row on the snow at frame-left with crews in white winter camouflage; a heavy black tracked command vehicle stands far at frame-right with its headlights on; the storm swirls across everything.")
SPREAD = Scene('snow_field', " A black night in a howling blizzard, swinging hand-lamp beams cutting the swirling snow.",
               " Fixed stage layout: a vast flat snowfield fills the frame in a howling blizzard; across it about two hundred small figures in bulky winter coats wade waist-deep in the snow, spread out in a wide line with swinging hand-lamp beams crossing in the swirling snow; a few snow-laden pines stand far behind; there is no door and no building anywhere.")
TRAP = Scene('snow_field', " A black night under a faint green aurora, the snow flat and perfect.",
             " Fixed stage layout: a flat unbroken stretch of white snow fills the middle of the frame under a faint green aurora; a few snow-laden pines stand far behind; there is no door and no building anywhere.")
HOLE = Scene('snow_field', " A black night under a faint green aurora, powder snow drifting on the wind.",
             " Fixed stage layout: a flat stretch of white snow with a ragged round hole broken through its crust in the middle of the frame, the edge crumbling; below it a black shaft of ice drops away with sharp white ice spikes glinting far down; a few snow-laden pines stand far behind.")
SOFA2 = Scene('bunker_sofa', SOFA.end, SOFA.layout + " A glass bowl of small orange mandarins and a loose curl of orange peel sit on the low coffee table.")
MON_WALL = Scene('bunker_living', LIVING.end,
                 " Fixed stage layout: a close view of the wall of small security monitors filling the frame, the largest screen in the middle showing a pale terrain map covered in a dense cloud of small red dots, the smaller screens around it showing white blizzards; a small red alarm lamp is mounted above the wall.")
FROZEN_PACK = Scene('snow_field', " A black night in a howling blizzard, the white storm swirling around lamp light.",
                    " Fixed stage layout: a snow clearing in a howling blizzard; hundreds of small bundled figures in the background stand frozen in place with their rifles lowered; in the foreground a heavy black tracked command vehicle stands at frame-right with its headlights on; the white storm swirls everywhere.")
CTRL_ALARM = Scene('bunker_control', CONTROL.end,
                   CONTROL.layout + " A round red alarm lamp flashes high on the wall above the console, the large red countdown clock is dark, and a black swivel chair stands in front of the console.")
AIR_OUT = Scene('airlock', AIRLOCK.end, AIRLOCK.layout + " The heavy round steel hatch door in the right wall is closed, thick frost on its rim.")
WHITEOUT = Scene('snow_field', " A black night in a howling whiteout, thick snow filling the air.",
                 " Fixed stage layout: a flat snowfield in a howling whiteout fills the frame, visibility only a few metres, snow streaming across it in horizontal ribbons; a dark dead tree stump stands in the snow at frame-right.")
BOMB_SITE = Scene('snow_field', " A white howling blizzard at night, the circle of tripod work lamps glowing yellow in the swirling snow.",
                  " Fixed stage layout: a flat snow clearing in a howling blizzard with visibility of only about five metres; in the middle of the frame a huge olive-drab thermobaric bomb the size of an oil drum lies on a steel sled with its nose cone open; three yellow work lamps on tripods stand around it; a steel toolbox sits open on the snow at frame-right; vague dark shapes of guards stand at the edge of the lamp light.")
BOMB_EMPTY = Scene('snow_field', BOMB_SITE.end,
                   " Fixed stage layout: a flat snow clearing in a howling blizzard; in the middle of the frame the huge olive-drab thermobaric bomb lies on its steel sled with its nose cone open; three yellow work lamps on tripods stand around it, one swaying; a long steel wrench lies half-sunk in the snow at its foot; the snow around it is churned with deep drag furrows leading into the dark at frame-left, a few dark red drops freezing into beads on the white; nobody stands anywhere in the lamp light.")
FACEOFF = Scene('snow_field', " A pale grey dawn-like gloom over the snowfield as the storm tears open.",
                " Fixed stage layout: a wide flat snowfield; the huge thermobaric bomb on its sled stands at frame-left in the foreground; about twenty metres across the snow a dense crowd of hundreds of bundled men with rifles stands in a wide arc at frame-right with a black tracked command vehicle behind them; torn banks of white snow mist drift between them.")
ARC_FIRE = Scene('snow_field', FACEOFF.end,
                 " Fixed stage layout: a wide flat snowfield; the huge thermobaric bomb on its sled stands at frame-left in the foreground; about twenty metres across the snow a dense crowd of hundreds of bundled men in a wide arc at frame-right raise their rifles to their shoulders; the black tracked command vehicle stands behind them.")
SMOKE = Scene('snow_field', " A pale grey gloom under the storm.",
              " Fixed stage layout: a flat snowfield; the huge olive-drab thermobaric bomb on its sled stands in the middle of the frame, its casing split open and its nose cone off; the black tracked command vehicle stands far at frame-right.")
EMPTY_SNOW = Scene('snow_field', " A grey dawn-like gloom after the white smoke has blown away.",
                   " Fixed stage layout: a wide perfectly smooth snowfield fills the middle of the frame with no footprints anywhere on it; the silent thermobaric bomb on its sled stands at frame-left; a few snow-laden pines stand far behind; the black tracked command vehicle stands far at frame-right.")
RETREAT = Scene('snow_field', " A grey gloom under a howling storm.",
                " Fixed stage layout: a vast snowfield; hundreds of small dark figures stream away from the middle of the frame toward frame-right across the snow in a disordered mass, throwing down rifles; a few black tracked vehicles turn around at the far edge of the frame with their tail lights glowing red; the storm swallows everything.")
HC_TUNNEL = Scene('hot_cave', " Soft blue moss light and rolling white mist fill a vast natural cavern.", " Fixed stage layout: the turquoise hot spring pool with white mist rolling off it fills the right of the frame; a smooth rock path lined with softly glowing blue moss runs from a dark tunnel mouth at frame-left toward the pool.")
CTRL_DET = Scene('bunker_control', CONTROL.end,
                 " Fixed stage layout: a close view of the steel control console in the middle of the frame; a small grey metal detonator box with a hinged switch cover lies on it beside a tall glass of water; the wall of six small monitors glows at frame-left; the red countdown clock hangs dark on the back wall.")
HC_QUAKE = Scene('hot_cave', " Soft blue moss light and rolling white mist fill a vast natural cavern.",
                 " Fixed stage layout: a vast natural cavern with a high ceiling of dark rock thickly covered in softly glowing blue moss; the steaming turquoise hot spring pool fills the lower middle of the frame with white mist rolling off it; one huge slab of rock hangs in the ceiling above the pool; a narrow dark tunnel mouth is at frame-left.")

# ---------------------------------------------------------------------------------------------- 光和空气
AES_WARCAB = ("Cold green light from the navigation screen washes both faces from below while a pale frost-blue gleam from the porthole edges their coats and the vehicle's shuddering sends dust trembling in the beam.",
              "导航屏冷冷的绿光从下往上洗过两张脸，舷窗透进来的淡淡霜蓝色在他们的大衣边上描出一道亮边，车身颠簸让光束里的灰尘一阵阵颤动。")
AES_SEAR = ("Warm golden lamp light glows on the foaming butter and the crust of the seared liver, rising steam catches the light in curling threads and the ruby wine glows like a gem in the decanter.",
            "温暖的金色灯光照在冒泡的黄油和煎得金黄的鹅肝表皮上，升起的蒸汽在光里卷成一缕缕，红酒在醒酒器里红得像宝石。")
AES_BAR = ("Honey-gold lamp light pools on the marble counter and rims their faces while the ruby wine throws small red glints and the cool blue flicker of the monitor wall adds a gentle teal edge.",
           "蜂蜜般的金色灯光落在大理石台面上，把两个人的脸描上轮廓光，红酒投下一点点红色的闪光，监控墙冷冷的蓝光在边缘加上一抹淡淡的青色。")
AES_STORMCOL = ("Hundreds of headlights bore tunnels of yellow light into the swirling snow, a violet-grey storm sky rolls above and powdery ice streams off the hulls in glittering ribbons.",
                "成百上千盏车灯在漩涡般的飞雪里钻出一条条黄色的光洞，上空翻滚着紫灰色的风暴天空，粉雪似的碎冰从车身上一条条闪着光飘开。")
AES_HOLO = ("Pale blue holographic light climbs the glass in her eyes and rims his jaw, the red wine glints in his raised glass and a thin haze of hologram dust drifts upward through the beam in a teal-and-orange contrast.",
            "淡蓝色的全息光映进她的眼睛，给他的下颌描上亮边，他举起的杯子里红酒闪光，一层薄薄的全息光尘顺着光束往上飘，青橙对比分明。")
AES_BOOM = ("A deep rumble sets the pendant lamp swinging so its golden light sweeps across their faces, fine dust sifts down through the beam and the red wine in the glasses shivers in concentric rings.",
            "一声沉闷的隆隆声让吊灯晃起来，金色的灯光在两张脸上来回扫过，细细的灰尘从光束里簌簌落下，杯子里的红酒荡起一圈圈同心的波纹。")
AES_SHELL = ("Orange flashes tear the black night into hard strobes, columns of white snow explode upward in glittering sprays that hang in the air, and the howling storm streams sparks of ice across their faces.",
             "橙色的闪光把黑夜撕成一阵阵硬朗的频闪，白色的雪柱冲天而起、碎雪闪着光悬在半空，呼啸的风暴把冰晶像火星一样吹过两张脸。")
AES_SPREAD = ("Hundreds of swinging hand-lamp beams cross each other in the swirling snow like searchlights, their yellow pools sliding over the white and a violet-blue storm gloom pressing in all around.",
              "成百上千道摇晃的手电光在漩涡般的飞雪里像探照灯一样交叉，一圈圈黄色的光斑在白雪上滑动，四周压着紫蓝色的风暴暗影。")
AES_TRAP = ("A faint green aurora washes the flat snow in cold light, powder snow glitters along the wind and the first hairline crack runs silver through the crust under the glow of his headlamp.",
            "淡淡的绿色极光用冷冷的光洗着平整的雪面，粉雪沿着风闪着光，在他头灯的光里，第一道银色的细裂纹从雪壳上爬开。")
AES_HOLE = ("The green aurora glows on the broken crust, dust of powder snow sifts slowly down into the black ice shaft in glittering threads and a few cold white ice spikes glint far below.",
            "绿色的极光照在破裂的雪壳上，粉雪的碎末一缕缕闪着光慢慢飘进黑色的冰井，井底深处有几根冰冷的白色冰刺反着光。")
AES_ORANGE = ("Warm golden lamp light spills over the sofa and the glass bowl of mandarins, the orange peel glows like a small lantern, steam curls from a mug and the monitor wall adds a cool blue edge on one side.",
              "温暖的金色灯光洒在沙发和那碗橘子上，橘子皮像一盏小灯笼发着光，杯子里热气卷起来，监控墙在一侧加了一道冷冷的蓝边。")
AES_MONWALL = ("A cold blue glow floods the whole wall of screens, tiny red dots pulse like embers across the pale map and wink out one by one while a faint red lamp glow pulses at the top of the frame.",
               "一整面屏幕泛着冷冷的蓝光，苍白的地图上一点点红色的光点像炭火一样搏动，再一个个熄灭，画面顶部有一盏红灯淡淡地闪。")
AES_FROZEN = ("The white storm streams across the lamp-lit snow in ribbons, the vehicle's headlights burn two yellow shafts through it, and breath clouds hang in the freezing air above the frozen crowd in the violet-blue gloom.",
              "白色的风暴一条条飘过被灯照亮的雪地，指挥车的车灯烧出两道黄色的光柱，冻僵的人群上方悬着一团团呼出的白气，紫蓝色的暗影里一片死寂。")
AES_ALARM = ("A hard red alarm pulse slams across the console and both faces in sharp waves, the cool green status lights wink beneath it and a thin haze hangs in the red beam.",
             "强烈的红色警报光一阵阵撞过控制台和两张脸，下面冷冷的绿色指示灯一闪一闪，红色的光束里浮着一层薄薄的雾气。")
AES_ORANGEWARM = ("Warm golden lamp light sets the strands of his hair aglow, the orange peel on the table glows softly and the steam from the mug curls up through the beam.",
                  "温暖的金色灯光让他的发丝泛着光，桌上的橘子皮柔柔地发亮，杯子里的热气在光束里卷起来。")
AES_AIRLOCK = ("Hard white strip light falls on the white tiles and glitters on the frost in the folds of his suit while a cold storm-blue seam of light slips from the hatch edge and a few snow crystals swirl in the air.",
               "硬朗的白色灯带光落在白瓷砖上，他衣服褶皱里的白霜闪着光，一道冷冷的风暴蓝从舱门的缝隙里漏出来，空气里有几粒雪晶在打转。")
AES_WHITEOUT = ("A faint teal glow from his thermal goggles stains the white around his face while the ghostly storm light streams sideways in pale ribbons and powder snow drifts over his white hood.",
                "他热成像护目镜里透出一点淡淡的青色，把脸周围的白雪染上一圈色，幽灵似的风暴光一条条横着流过，粉雪飘落在他白色的兜帽上。")
AES_BOMBSITE = ("Three yellow work lamps burn warm halos in the swirling white, the olive casing of the bomb gleams wetly with melting frost and the breath of the crew hangs in white clouds in the amber light.",
                "三盏黄色的工作灯在飞旋的白雪里烧出一团团暖色的光晕，炸弹橄榄绿的外壳上融化的霜水闪着光，工人们的呼气在琥珀色的光里一团团白气。")
AES_CROSSBOW = ("A thin teal glow from his goggles and the cold storm light pick out the pale bolt as it rests in the groove, powder snow drifts across the lens of light and the lamp glow ahead is a blurred amber halo.",
                "护目镜里一点淡淡的青光和冷冷的风暴光照出放在槽里的那支白色弩箭，粉雪从光里飘过，前方的灯光是一团模糊的琥珀色光晕。")
AES_EMPTYCIRCLE = ("The yellow lamps sway on their tripods and throw long shadows that swing across the churned snow, the frozen red beads glint like tiny rubies and the swirling white presses in at the edges.",
                   "黄色的工作灯在三脚架上晃着，长长的影子在被翻乱的雪地上来回扫过，冻成珠子的红点像一粒粒小红宝石闪光，旋转的白雪从四周压过来。")
AES_GRAB = ("Yellow lamp glow catches a spray of flying snow, the white glove flashes out of the white drift and the edges of the frame are swallowed by the swirling storm.",
            "黄色的灯光照亮一蓬飞起的雪，白色的手套从白色的雪堆里闪出来，画面四周被旋转的风暴吞没。")
AES_RISE = ("Loose snow pours off his white shoulders in glittering sheets, the yellow lamp light rims his hood and the little red light of the detonator pulses in his glove like a heartbeat.",
            "松散的雪从他白色的肩膀上一片片闪着光倒下来，黄色的灯光描着他的兜帽，他手套里起爆器上那点红灯像心跳一样一明一暗。")
AES_FACE = ("The storm tears open and a pale grey light falls across the snow, torn banks of white mist drift between the two sides, powder snow glitters in the air and every rifle barrel catches a thin line of cold light.",
            "风暴被撕开，一片苍白的灰光落在雪地上，一团团被撕破的白雾在两边之间飘，空气里的粉雪闪着光，每根枪管都被冷光描出一条细线。")
AES_FLASH = ("A blinding white flash fills the whole frame and burns out all colour, then thick white smoke boils outward in a rolling wall that swallows the snow and the light and glittering ash drifts through the glare.",
             "一道刺眼的白光灌满整个画面、烧掉所有的颜色，然后浓浓的白烟像一堵翻滚的墙向外涌，吞掉雪地和光，闪光的灰屑在强光里飘。")
AES_GLOOM = ("A pale grey light spills across the smoothed snow, thin wisps of white smoke drift low over the ground and the cold wind combs the powder snow into long glittering streaks.",
             "一片苍白的灰光洒在平滑的雪地上，几缕细细的白烟贴着地面飘，冷风把粉雪梳成一道道闪光的长纹。")
AES_RETREAT = ("A grey storm gloom swallows the field while the red tail lights of the vehicles smear into the snow, thrown rifles glint in the white and breath clouds streak behind the running men.",
               "灰色的风暴暗影吞掉整片雪原，车辆的红色尾灯在雪里晕开一道道红光，扔掉的步枪在白雪里反着光，逃跑的人身后拖着一缕缕白气。")
AES_TOWEL = ("Warm steam rises from the towel in soft threads through the hard white strip light, the frost on his hair melts into bright beads and a teal-and-orange glow edges his jaw from the cold storm seam behind him.",
             "毛巾冒出的热气在硬朗的白色灯带光里升成一缕缕柔软的丝，他头发上的霜融成一颗颗发亮的水珠，身后风暴蓝的缝隙在他的下颌描上青橙色的亮边。")
AES_WALK = ("Soft blue moss light and the amber glow from the corridor meet on the path, drifting white mist curls around their ankles and the turquoise pool glimmers ahead in a teal-and-orange contrast.",
            "柔和的蓝色苔藓光和走廊里琥珀色的光在小路上交汇，飘着的白雾在他们脚踝边卷着，前面的青绿色温泉闪着微光，青橙对比分明。")
AES_DET = ("A hard little red LED pulses on the grey box and throws a trembling red halo on the console, the surface of the water in the glass shivers in concentric rings and a cool blue glow washes the wall of screens behind.",
           "灰色盒子上一盏硬朗的小红灯一明一暗，在控制台上投下一圈颤动的红色光晕，玻璃杯里的水面荡起一圈圈同心的波纹，身后的屏幕墙泛着冷冷的蓝光。")
AES_QUAKE = ("Soft blue moss light flickers across the ceiling as a thin black fissure races through the rock, fine white dust and gravel fall in glittering streams into the steaming pool and the mist swirls up in startled coils.",
             "柔和的蓝色苔藓光在天花板上忽明忽暗，一道细细的黑色裂缝飞快地爬过岩石，细细的白灰和碎石一道道闪着光落进冒着热气的温泉，白雾惊起一圈圈盘旋。")

# ---------------------------------------------------------------------------------------------- 声音
SOUND_WARCAB = voiced('The deep rumble and clank of heavy tracks, the whine of a storm against steel and the faint beep of a navigation screen.', '重型履带深沉的隆隆声和碰撞声、暴风雪撞在钢板上的呼啸和导航屏细细的嘀声。')
SOUND_SEAR = breathy('The loud sizzle of liver searing in a hot pan, bubbling butter and the soft clink of crystal.', '鹅肝在热锅里滋滋作响、黄油冒泡的声音和水晶杯轻轻的碰撞声。')
SOUND_BAR = voiced('The soft sizzle of a pan, the gentle clink of a knife on a board and the faint hum of the underground room.', '锅里轻轻的滋滋声、刀在砧板上轻轻的磕碰声和地下房间低低的嗡鸣。')
SOUND_STORMCOL = breathy('The grinding roar of hundreds of heavy tracks and a long howling blizzard.', '成百上千台重型履带碾过的轰隆声和暴风雪长长的呼啸。')
SOUND_HOLO = voiced('The faint electronic hum of a hologram projector and the soft clink of a wine glass.', '全息投影仪细细的电子嗡鸣和酒杯轻轻的碰撞声。')
SOUND_BOOM = voiced('A deep muffled boom through the earth, a rattle of glass, the creak of a swinging lamp and a soft electronic chime.', '穿过大地传来一声沉闷的轰响、玻璃的颤抖声、吊灯晃动的吱嘎声和轻轻的电子鸣音。')
SOUND_SHELL = voiced('The thunderous crump of mortar shells, the hiss of falling snow and the howling roar of a blizzard.', '迫击炮弹雷鸣般的爆炸闷响、落雪的嘶嘶声和暴风雪呼啸的轰鸣。')
SOUND_SPREAD = breathy('The howl of the blizzard, the crunch of hundreds of boots in deep snow and distant muffled shouts.', '暴风雪的呼啸、几百双靴子踩在深雪里的嘎吱声和远处模糊的呼喊。')
SOUND_TRAP = breathy('A low steady wind, the soft crunch of a boot in powder snow and then a thin brittle crackle.', '低低稳定的风声、靴子踩在粉雪里轻轻的嘎吱声，然后一声细细的、脆脆的裂响。')
SOUND_HOLE = breathy('A hollow echoing rumble from below, trickling snow, the clatter of a rifle sliding over the lip and a thin muffled cry fading deep underground.', '从下面传来空洞的回响，雪簌簌流下去，一支步枪滑过边缘的磕碰声，和一声细细的、闷闷的叫喊在地底深处渐渐远去。')
SOUND_ORANGE = voiced('The soft rip of orange peel, a faint muffled thud through the earth and the quiet hum of the room.', '橘子皮被轻轻撕开的声音、一声透过大地传来的微弱闷响和房间安静的嗡鸣。')
SOUND_MONWALL = breathy('A soft electronic blip with each red dot that goes out, and a faint distant thud through the earth.', '每灭掉一个红点就有一声轻轻的电子嘀声，和一声透过大地传来的、遥远的微弱闷响。')
SOUND_FROZEN = voiced('The howl of the blizzard, the idle growl of a heavy engine and the metallic click of a radio handset.', '暴风雪的呼啸、重型发动机怠速的低吼和无线电话筒金属的咔哒声。')
SOUND_ALARM = voiced('A sharp repeating alarm beep, a low electronic hum and a calm synthetic chime.', '尖锐反复的警报声、低低的电子嗡鸣和平静的合成提示音。')
SOUND_AIRLOCK = voiced('The soft hiss of a vent, the muffled howl of a storm beyond a steel door and the creak of frosted fabric.', '通风口轻轻的嘶嘶声、钢门外闷闷的暴风雪呼啸和结霜的衣料嘎吱声。')
SOUND_HATCH = voiced('A calm synthetic chime, the deep grinding of a heavy steel hatch swinging open and the sudden roar of a storm.', '平静的合成提示音、厚重钢门转开时深沉的摩擦声和风暴突然灌进来的轰鸣。')
SOUND_CRAWL = breathy('The howl of a blizzard, a soft rhythmic scrape of fabric on snow and his muffled breath.', '暴风雪的呼啸、衣料在雪上有节奏的轻轻摩擦声和他压低的呼吸。')
SOUND_BOMBSITE = voiced('The howl of the blizzard, the clink of tools on steel and the creak of a swaying lamp.', '暴风雪的呼啸、工具敲在钢铁上的叮当声和灯架晃动的吱嘎声。')
SOUND_BOLT = breathy('The howl of the blizzard and one sharp whisper of a crossbow bolt cutting through the air.', '暴风雪的呼啸和一支弩箭划破空气的一声尖细的轻响。')
SOUND_EMPTY = breathy('The howl of the blizzard, the creak of a swaying lamp and the faint tick of freezing droplets.', '暴风雪的呼啸、灯架晃动的吱嘎声和冻结的水滴细细的嘀嗒声。')
SOUND_GRAB = breathy('The howl of the blizzard, a burst of scuffling snow and one muffled grunt.', '暴风雪的呼啸、雪被蹬乱的一阵窸窣声和一声闷闷的低哼。')
SOUND_RISE = breathy('The howl of the blizzard, the hiss of sliding snow and a soft electronic beep from the detonator.', '暴风雪的呼啸、雪滑落的嘶嘶声和起爆器轻轻的电子嘀声。')
SOUND_FACE = breathy('A fading howl of wind, the creak of hundreds of boots shifting and the metallic click of rifle bolts.', '渐渐减弱的风声、几百双靴子挪动的吱嘎声和步枪枪栓金属的咔哒声。')
SOUND_FIRE = voiced('A distant roar of the wind, the clatter of hundreds of rifles being raised and the sharp click of a button.', '远处的风声、几百支步枪举起来的哗啦声和一声清脆的按键声。')
SOUND_FLASH = breathy('A piercing ringing hiss, the crackling roar of a flash charge, a rolling blast of white smoke and the rattle of rifles firing blindly.', '尖锐的耳鸣似的嘶响、闪光弹噼啪的爆响、白烟翻滚的轰隆声和步枪盲目乱扫的哒哒声。')
SOUND_GLOOM = voiced('The moan of a fading wind, the soft hiss of drifting snow and the metallic rattle of a rifle lowered.', '渐渐减弱的风的呜咽、飘雪轻轻的嘶嘶声和一支步枪放下时金属的碰撞声。')
SOUND_RETREAT = breathy('The roar of engines starting, the scrabble and shouting of a panicked crowd and the howl of the storm.', '发动机启动的轰鸣、慌乱的人群奔逃和呼喊的混杂声和风暴的呼啸。')
SOUND_TOWEL = voiced('The soft hiss of steam, the creak of frosted fabric and the muffled howl of a storm fading beyond the door.', '蒸汽轻轻的嘶嘶声、结霜衣料的嘎吱声和门外渐渐减弱的闷闷的暴风雪声。')
SOUND_WALK = voiced('The gentle bubbling of a hot spring, soft footsteps on wet rock and a faint drip echoing.', '温泉轻轻的咕嘟声、湿润岩石上轻轻的脚步声和远处一滴水落下的回响。')
SOUND_DET = breathy('A quiet repeating electronic beep, a deep low hum felt more than heard and a faint rippling of water.', '安静反复的电子嘀声、一种感觉比听到更明显的深沉低鸣和水面轻轻的涟漪声。')
SOUND_QUAKE = breathy('A deep groaning crack of rock, a rain of falling gravel and splashes into a hot pool.', '岩石深沉的断裂呻吟声、碎石落下的哗啦声和落进温泉里的水花声。')

# ================================================================================================ 第 47 集
b47 = S.episode('剧本第47集｜暴风雪前的顶级晚餐',
                '零下八十五度的暴风雪里，独眼统帅在重型指挥车里下令全速前进抢恒温基地；地下暖屋里，林峰煎好两块金黄的鹅肝，苏清月问五百人还有火炮为什么不去设伏，他说和疯子拼命是最蠢的笑话；黑血军团的车队碾过暴风雪；林峰端着红酒在全息台前说入口有四重伪装，今晚看他们被大自然玩死；一声炮响透过冻土传下来，吊灯晃动，伊甸报告目标进入绝对防御圈，林峰说启动深雪地狱协议。', 47)
new_person(b47, 'duyan_boss', '独眼统帅（四十多岁，脸上有疤、左眼戴黑色皮眼罩，毛领黑色军大衣、红袖标，胡茬上结霜）', 'man',
           'Duyan, a gaunt scarred Chinese man in his forties with a hard cruel face, a black leather patch over his left eye and frost crusted in his stubble, wearing a heavy black fur-collared military greatcoat with a red armband.',
           '独眼统帅，一个四十多岁、瘦削带疤的中国男性，面相冷硬残忍，左眼戴着黑色皮眼罩，胡茬上结着霜，穿着毛领的黑色军大衣，臂上戴着红袖标。',
           'a hard cruel scarred face, a black leather patch over his left eye, frost crusted in his stubble, a heavy black fur-collared military greatcoat with a red armband', 'a cold, hard, commanding expression', eth='Chinese')
new_person(b47, 'pang_aide', '副官老庞（三十多岁，壮实，白灰色雪地迷彩棉袄、兜帽拉起，围巾拉到下巴）', 'man',
           'Pang, a stocky Chinese man in his thirties with a nervous round face, wearing a dirty white-and-grey winter camouflage parka with the hood up and a frosted scarf pulled down under his chin.',
           '副官老庞，一个三十多岁、身材壮实的中国男性，圆脸神情紧张，穿着脏兮兮的白灰色雪地迷彩棉袄、兜帽拉起，结霜的围巾拉到下巴下面。',
           'a nervous round face, a dirty white-and-grey winter camouflage parka with the hood up, a frosted scarf pulled down under his chin', 'a tense, nervous expression', eth='Chinese')
new_scene(b47, 'war_cab', '重型指挥车驾驶舱（狭窄的装甲车厢，两张钢板长凳面对面，中间窄桌上嵌着发绿光的导航屏，后墙一扇结霜的舷窗外是白色暴风雪）',
          'A cramped armoured cab of a heavy command vehicle with two padded steel bench seats facing each other across a narrow table with a glowing green navigation screen set into its top and a small frost-crusted porthole in the back wall showing a white blizzard.',
          '重型指挥车狭窄的装甲车厢，两张钢板长凳面对面，中间窄桌上嵌着发绿光的导航屏，后墙一扇结霜的舷窗外是白色暴风雪。',
          'the bench seats, the glowing navigation table and the frosted porthole')
b47.character('Duyan', 'duyan_boss', DUYAN_EN, DUYAN_ZH)
b47.character('Pang', 'pang_aide', PANG_EN, PANG_ZH)

TA('47-01', '01｜指挥车里：独眼统帅和副官面对面坐在颠簸的车厢里，统帅命令全速前进抢下恒温基地，副官说外面零下八十五度，统帅说抢下来我们就是神', 15, WAR_CAB,
   [P('duyan_boss', 'left', "sitting on the padded steel bench in profile facing frame-right, one gloved fist planted on the table beside the glowing navigation screen, his head turned to his aide", 'Pang', "his one visible eye hard and cruel, his lips pulled back in a harsh snarl, his brows low"),
    P('pang_aide', 'right', "sitting on the bench opposite in profile facing frame-left, one hand clutching an overhead steel bar, his eyes on the commander", 'Duyan', "his lips pressed tight, his eyes wide and anxious, his brows pulled up")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the cab.',
   "<duyan_boss> jabs a finger at the green navigation screen and speaks the first line to <pang_aide> in a harsh commanding growl, then <pang_aide> answers with the second line to <duyan_boss> in a thin anxious voice, then <duyan_boss> speaks the third line to <pang_aide> and <pang_aide> answers with the fourth line to <duyan_boss>; after the last line the vehicle lurches and <duyan_boss> grips the table with a cruel greedy grin while <pang_aide> clings to the bar, <duyan_boss> with his one visible eye hard and his lips pulled back in a harsh snarl and his brows low, <pang_aide> with his lips pressed tight, his eyes wide and anxious and his brows pulled up.",
   "独眼统帅用手指戳着绿色的导航屏，用粗哑的命令口气对副官说出第一句，接着副官用细而发紧的声音对统帅答出第二句，统帅再对副官说出第三句，副官再对统帅答出第四句；最后一句之后，车身猛地一颠，统帅抓住桌子，脸上露出残忍贪婪的笑意，副官死死攥着头顶的钢杆，统帅那只露着的眼睛冷硬、嘴唇咧开露出牙、眉头压低，副官嘴唇抿紧、眼睛睁大满是不安、眉毛上扬。",
   SOUND_WARCAB, AES_WARCAB,
   lines=LN(('duyan_boss', "全速前进，抢下恒温基地！", 'Pang'), ('pang_aide', "统帅，外面零下八十五度！", 'Duyan'), ('duyan_boss', "抢下来，我们就是神！", 'Pang'), ('pang_aide', "是，全速前进！", 'Duyan')),
   cam=push('both of them', '两人'), extra_assets=(), room={'Duyan', 'Pang'}, new=True,
   bg='Behind them the small frost-crusted porthole in the back wall shows a white roaring blizzard and a black radio handset swings on its hook.',
   holds='The frame holds exactly two people: Duyan and Pang, in the cab, nobody else.')

insert2('47-02', '02｜插镜：黑铁锅里两块鹅肝煎得金黄，黄油翻着泡，蒸汽一缕缕升起，旁边水晶醒酒器里的红酒红得像宝石', 6, KITCH_SEAR,
        'Close shot of the black iron pan on the stove at frame-left and the decanter on the counter, the pan in the middle third of the frame, nobody in the scene.',
        "In the black iron pan two thick slices of foie gras sizzle golden-brown in foaming butter as steam curls up in lazy threads, a sprig of thyme crackles at the edge and beside it on the marble counter the crystal decanter holds ruby red wine that glows in the lamp light. Nothing else is in the scene.",
        "黑铁锅里两块厚厚的鹅肝在冒泡的黄油里滋滋煎成金黄色，蒸汽懒洋洋地卷成一缕缕，锅边一枝百里香噼啪作响，旁边大理石台面上的水晶醒酒器里红酒红得发亮。画面里没有别的东西。",
        SOUND_SEAR, 'The frame holds the black iron pan with the golden foie gras and the glowing decanter, and nobody in the scene.',
        descend('the golden-seared slices in the black iron pan', '黑铁锅里煎得金黄的鹅肝'), AES_SEAR)

TA('47-03', '03｜吧台边：林峰穿着干净的白衬衫切鹅肝，苏清月坐在高凳上问五百人还有火炮为什么不去设伏，他说和疯子拼命是最蠢的笑话，把一小块喂进她嘴里，她说好吃', 15, KITCH_BAR,
   [P('su_cozy', 'left', "sitting on the high wooden stool at the counter in profile facing frame-right, her fingertips on the stem of a wine glass, her head turned to him", 'Lin', "her eyes uneasy and searching, her lips pressed in a worried line, her brows pulled together"),
    P('lin_white', 'center-right', "standing behind the counter in profile facing frame-left, a silver fork in one hand with a small piece of seared foie gras on its tines, his eyes on her", 'Su', "his eyes calm and warm, one corner of his mouth lifting, his brows soft", outfit="in a clean white dress shirt with the sleeves rolled to his forearms and dark trousers, his black hair neatly combed")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the counter.',
   "<su_cozy> speaks the first line to <lin_white> in a low uneasy voice, then <lin_white> answers with the second line to <su_cozy> in a calm low voice, then he speaks the third line to <su_cozy> and lifts the fork to her mouth, and <su_cozy> takes the bite and speaks the fourth line to <lin_white> in a soft surprised voice; after the last line her brows ease and her eyes drop to the plate while he refills her glass, her eyes uneasy and her lips pressed in a worried line at first, his eyes calm and warm, one corner of his mouth lifting and his brows soft.",
   "苏清月用低低不安的声音对林峰说出第一句，接着林峰用平静低沉的声音对苏清月答出第二句，他再对苏清月说出第三句，把叉子递到她嘴边，苏清月咬了一口，用轻轻惊讶的声音对林峰说出第四句；最后一句之后，她的眉头松开、目光落到盘子上，他给她把酒杯重新倒满，她开始眼神不安、嘴唇抿成担忧的一条线，他眼神平静温暖、嘴角微微上扬、眉头舒展。",
   SOUND_BAR, AES_BAR,
   lines=LN(('su_cozy', "五百人，还有火炮？", 'Lin'), ('lin_white', "去拼命，是最蠢的笑话。", 'Su'), ('lin_white', "尝尝，火候刚好。", 'Su'), ('su_cozy', "嗯，好吃。", 'Lin')),
   cam=track('the two of them', '两人'), extra_assets=(), room={'Su', 'Lin'}, new=True,
   bg='Behind them the black-and-gold stove glows at frame-left and the wall of small security monitors shows white blizzards at frame-center-right.',
   holds='The frame holds exactly two people: Su and Lin, at the counter, nobody else.')

insert2('47-04', '04｜暴风雪里：一长列黑色的重型履带装甲车拖着榴弹炮碾过被风暴搅成一团白的雪原，车头的尖刺撞板挂满冰，车灯在飞雪里钻出一条条光洞', 6, STORM_COL,
        'Wide low shot of the snowfield in the blizzard, the long column of tracked vehicles in the middle third of the frame, nobody visible.',
        "A very long column of black heavy armoured tracked vehicles with spiked front plates and towed howitzers grinds across the snowfield in the roaring blizzard from frame-right toward frame-left, thick ice crusting their hulls and their headlights boring yellow tunnels into the swirling snow. Nothing else is in the scene.",
        "一长列黑色的重型履带装甲车，车头是尖刺撞板，后面拖着榴弹炮，在呼啸的暴风雪里从画面右边往左边碾过雪原，厚厚的冰盖在车身上，车灯在飞旋的雪里钻出一条条黄色的光洞。画面里没有别的东西。",
        SOUND_STORMCOL, 'The frame holds the snowfield with the long column of tracked vehicles, and nobody visible.',
        lowrise('the grinding column of headlights across the white storm', '风暴里碾过雪原的一长串车灯'), AES_STORMCOL, extra_assets=('raider_column',))

TA('47-05', '05｜全息台前：林峰端着红酒杯走到全息台边，投影里是上方两公里的雪山地形和四圈环，他说入口有四重伪装，苏清月问万一他们掘地三尺，他说只会挖到万年冻土，她说今晚我负责看戏', 15, CTRL_HOLO,
   [P('su_cozy', 'left', "standing at the edge of the holographic table in profile facing frame-right, her arms folded, her eyes on the glowing mountain model", 'obj:the glowing three-dimensional mountain model on the table', "her lips pressed in a thin curious line, her eyes bright, her brows lifted"),
    P('lin_white', 'right', "standing at the other edge of the table in profile facing frame-left, a wine glass in one hand and the other hand tracing a ring in the hologram, his head turned to her", 'Su', "his eyes calm and sure, one corner of his mouth lifting, his brows low", outfit="in a clean white dress shirt with the sleeves rolled to his forearms and dark trousers, his black hair neatly combed")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the holographic table.',
   "<lin_white> traces a glowing ring in the hologram with one finger and speaks the first line to <su_cozy> in a calm low voice, then <su_cozy> turns her head to him and speaks the second line to <lin_white> in a wary voice, then <lin_white> answers with the third line to <su_cozy>, and <su_cozy> speaks the fourth line to <lin_white>; after the last line he raises his glass and she lifts hers toward him, his eyes calm and sure, one corner of his mouth lifting and his brows low, her lips pressed in a thin curious line, her eyes bright and her brows lifted.",
   "林峰用一根手指在全息投影里描出一圈发光的环，用平静低沉的声音对苏清月说出第一句，接着苏清月转头用警惕的声音对林峰说出第二句，林峰再对苏清月答出第三句，苏清月再对林峰说出第四句；最后一句之后，他举起酒杯，她也把杯子朝他举起，他眼神平静笃定、嘴角微微上扬、眉头压低，她嘴唇抿成好奇的细线、眼睛明亮、眉毛上扬。",
   SOUND_HOLO, AES_HOLO,
   lines=LN(('lin_white', "入口有四重伪装。", 'Su'), ('su_cozy', "万一他们掘地三尺？", 'Lin'), ('lin_white', "只会挖到万年冻土。", 'Su'), ('su_cozy', "那今晚，我负责看戏。", 'Lin')),
   cam=push1('the glowing mountain model between them', '两人之间发光的山体模型'), extra_assets=(), room={'Su', 'Lin'}, new=True,
   bg='Between them the round holographic table glows pale blue and the wall of six small monitors shows white blizzards at frame-left.',
   holds='The frame holds exactly two people: Su and Lin, at the holographic table, nobody else.')

on, off = MIX([('eden_voice', "目标进入绝对防御圈。", 'Lin'), ('eden_voice', "他们在炮轰疑似入口。", 'Lin'), ('lin_white', "伊甸，启动深雪地狱协议。", 'Su')])
TA('47-06', '06｜暖屋里：一声沉闷的炮响穿过冻土传下来，吊灯摇晃，杯中红酒荡起波纹，墙上的扬声器里伊甸报告目标进入防御圈，林峰仰头喝尽红酒，下令启动深雪地狱协议', 12, LIV_BOOM,
   [P('su_cozy', 'left', "standing at the marble counter in profile facing frame-right, one hand on the counter, her eyes on the swinging lamp", 'obj:the swinging pendant lamp above the counter', "her lips parted, her eyes wide, her brows pulled together"),
    P('lin_white', 'center-right', "standing at the counter in profile facing frame-left, a wine glass in one hand, his eyes on the swinging lamp", 'obj:the swinging pendant lamp above the counter', "his eyes cold and bright, his jaw loose, one corner of his mouth lifting coldly, his brows low", outfit="in a clean white dress shirt with the sleeves rolled to his forearms and dark trousers, his black hair neatly combed")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the counter.',
   "A soft, calm, polite female synthetic voice from the wall speaker speaks the first line and then the second line as a voice-over to <lin_white>, while the pendant lamp swings and the wine ripples in the glasses; then <lin_white> tips his head back and drains his glass, lowers it and speaks the third line toward the wall speaker in a low cold voice, his eyes cold and bright, one corner of his mouth lifting coldly and his brows low, while <su_cozy> watches him with her lips parted, her eyes wide and her brows pulled together.",
   "墙上的扬声器里传出轻柔平静、礼貌的女性合成声音，以旁白的方式先说出第一句、再说出第二句，对着林峰说，吊灯摇晃，杯子里的红酒荡起波纹；接着林峰仰头喝尽杯中的酒，放下杯子，用低沉冰冷的声音朝着墙上的扬声器说出第三句，他眼神冰冷明亮、嘴角冷冷一挑、眉头压低，苏清月看着他，嘴唇微张、眼睛睁大、眉头拧在一起。" + BRISK_ZH,
   SOUND_BOOM, AES_BOOM,
   lines=on, vo=off,
   cam=pull('the swinging lamp and the two of them at the counter', '摇晃的吊灯和吧台边的两人', 'the whole warm room with the heavy hatch door in the distance', '整间暖屋和远处厚重的圆形钢门'), extra_assets=('hack_screen',), room={'Su', 'Lin'}, new=True,
   bg='Above them a small round speaker grille is set into the concrete wall and the wall of small security monitors shows white blizzards at frame-center-right.',
   holds='The frame holds exactly two people: Su and Lin, at the counter, nobody else.')

# ================================================================================================ 第 48 集
b48 = S.episode('剧本第48集｜深雪地狱',
                '地表雪原上，迫击炮把一座雪丘炸得雪柱冲天，下面只有比钢铁还硬的万年冻土，独眼统帅怒吼“门呢”，下令几百人散开去找；一个小头目踩上一片平整的雪，雪壳裂开细纹，后来雪地上只剩一个破开的窟窿，下面是布满冰刺的冰井；地下暖屋里，林峰给苏清月剥橘子，监控墙上红点一个个熄灭，她说已经死了一百多个；独眼彻底慌了，吼着把军用温压弹拉上来；地下伊甸响起红色警报：如果在正上方引爆，温泉岩层有六成概率塌方。', 48)
new_person(b48, 'tou_thug', '小头目（三十多岁，精瘦，灰白色棉袄，步枪斜挎在胸前，围巾遮到鼻子）', 'man',
           'Tou, a lean Chinese man in his thirties with a wary bloodshot gaze, wearing a stained grey-white padded coat with a rifle slung across his chest and a frosted scarf pulled up over his nose.',
           '小头目，一个三十多岁、精瘦的中国男性，眼睛布满血丝、警惕地打量，穿着脏污的灰白色棉袄，步枪斜挎在胸前，结霜的围巾拉到鼻子上。',
           'a wary bloodshot gaze, a stained grey-white padded coat with a rifle slung across his chest and a frosted scarf pulled up over his nose', 'a wary, tense expression', eth='Chinese')
b48.character('Tou', 'tou_thug', TOU_EN, TOU_ZH)

TA('48-01', '01｜雪原：迫击炮把雪丘炸得雪柱冲天，独眼统帅骂门呢坐标明明在这里，副官说下面全是冻土，他吼着让所有人散开找排气孔和树桩', 15, SHELL,
   [P('pang_aide', 'left', "standing on the snow in profile facing frame-right, one hand holding his hood against the wind, his head turned to his commander", 'Duyan', "his lips pulled tight, his eyes wide and anxious, his brows pulled up"),
    P('duyan_boss', 'center-right', "standing on the snow in profile facing frame-left, one gloved fist raised and shaking, his head turned to his aide", 'Pang', "his one visible eye wild, his lips pulled back in a savage snarl, his brows low")],
   'Medium wide two-shot, both from the head to the knees, in the middle third of the frame, in front of the bombarded mound.',
   "<duyan_boss> shakes his fist and speaks the first line to <pang_aide> in a savage roar over the explosions, then <pang_aide> answers with the second line to <duyan_boss> in a frightened shout, then <duyan_boss> speaks the third line to <pang_aide>; behind them mortar shells keep bursting on the snow mound in columns of white snow; after the last line <duyan_boss> hurls his frosted goggles into the snow, his one visible eye wild, his lips pulled back in a savage snarl and his brows low, <pang_aide> flinching with his eyes wide and his brows pulled up.",
   "独眼统帅挥着拳头，在爆炸声里用狂暴的怒吼对副官说出第一句，接着副官用惊恐的喊声对统帅答出第二句，统帅再对副官说出第三句；他们身后迫击炮弹还在雪丘上一发接一发炸出白色的雪柱；最后一句之后，统帅把结霜的护目镜狠狠摔进雪里，他那只露着的眼睛疯狂、嘴唇咧开露出牙、眉头压低，副官吓得缩了一下，眼睛睁大、眉毛上扬。",
   SOUND_SHELL, AES_SHELL,
   lines=LN(('duyan_boss', "门呢？坐标明明就是这里！", 'Pang'), ('pang_aide', "统帅，下面全是冻土！", 'Duyan'), ('duyan_boss', "散开找，一个排气孔都别放过！", 'Pang')),
   cam=track('the two of them', '两人'), room={'Duyan', 'Pang', 'the mortar crews'}, new=True,
   groups=[('the mortar crews', 'back', 'obj:the bombarded snow mound')],
   bg='Behind them the low snow mound erupts in columns of white snow while three black mortar tubes stand in a row and white-camouflaged crews feed them shells, all sharp and in focus.',
   holds='The frame holds exactly two named men, Duyan and Pang, in front, and about six white-camouflaged mortar crew behind them at the tubes, everyone sharp and in focus.')

insert2('48-02', '02｜插镜：几百个裹得鼓鼓囊囊的暴徒在齐腰深的雪里散成一条宽宽的线，手电光在飞雪里像探照灯一样交叉', 8, SPREAD,
        'Wide shot of the snowfield, the wide line of wading figures in the middle third of the frame, no named person in the scene.',
        "About two hundred small bundled figures wade waist-deep through the snow, spread out in a wide ragged line across the snowfield in the howling blizzard, their hand-lamp beams swinging and crossing in the swirling snow as they poke the snow with poles and rifle butts, and none of them finds anything. Nothing else is in the scene.",
        "大约两百个裹得鼓鼓囊囊的小小人影在齐腰深的雪里蹚着，在呼啸的暴风雪里散成一条宽宽的、歪歪扭扭的线，手电光在飞旋的雪里摇晃交叉，他们用杆子和枪托戳着雪，什么也没找到。画面里没有别的东西。",
        SOUND_SPREAD, 'The frame holds the wide snowfield with about two hundred small bundled figures, and no named person in the scene.',
        slide('left', '左', 'the whole wide line of searching figures fills the middle of the frame', '整条搜寻的人线占满画面中间'), AES_SPREAD, groups=[('the searchers', 'back', 'obj:the snow ahead of them')])

TA('48-03', '03｜平整的雪地：小头目端着枪小心翼翼地踩上一片平得不自然的雪，脚下的雪壳发出一声轻响，一道银色的细裂纹从他靴子边爬开，他僵住，眼睛慢慢往下看', 8, TRAP,
   [P('tou_thug', 'center', "standing on the flat white snow in profile facing frame-right, a rifle held across his chest, one boot just set down on the crust, his head slowly lowering toward his boots", 'obj:the snow under his boots', "his lips parted under the scarf, his eyes wide and frozen, his brows pulled high")],
   'Medium wide shot, one man from the head to the feet, in the middle third of the frame, on the flat snow.',
   "<tou_thug> steps carefully forward and sets his boot down, a thin brittle crack sounds under it and a silver hairline crack spreads across the crust from his boot, then he freezes with his rifle across his chest and slowly lowers his gaze to the snow, his lips parted under the scarf, his eyes wide and frozen and his brows pulled high.",
   "小头目小心翼翼地往前迈步，靴子刚落下，脚下传来一声细细脆脆的裂响，一道银色的细裂纹从他的靴子边在雪壳上爬开，他僵住，步枪横在胸前，目光慢慢往下落到雪面上，围巾下嘴唇微张、眼睛睁大发直、眉毛高高挑起。",
   SOUND_TRAP, AES_TRAP,
   cam=push1('his boots and the spreading crack', '他的靴子和蔓延的裂纹'), room={'Tou'}, new=True,
   bg='Behind him a few snow-laden pines stand far away under the faint green aurora and the wind streams powder snow across the flat white ground.',
   holds='The frame holds one person: Tou, standing alone on the flat snow.')

insert2('48-04', '04｜插镜：刚才那片平整的雪地中间现在破开一个参差的圆窟窿，边缘的雪还在簌簌塌落，下面是一口黑色的冰井，井壁上露出白色的尖冰刺，一支步枪停在洞沿，滑了进去', 6, HOLE,
        'Close high shot looking down at the broken hole, the hole in the middle third of the frame, nobody in the scene.',
        "In the middle of the flat white snow a ragged round hole has broken through the crust, its edge still crumbling, and below it a black shaft of ice drops away with sharp white ice spikes glinting far down; a rifle teeters on the lip, slides over the edge and falls into the dark while powder snow sifts down after it. Nothing else is in the scene.",
        "平整的白色雪地中间，雪壳破开一个参差的圆窟窿，边缘的雪还在塌落，下面是一口往下掉的黑色冰井，深处露出白色的尖冰刺在闪光；一支步枪停在洞沿上晃了晃，滑过边缘落进黑暗，粉雪跟着簌簌落下去。画面里没有别的东西。",
        SOUND_HOLE, 'The frame holds the broken hole in the snow with the ice shaft below it, and nobody in the scene.',
        tilt('the black ice shaft and its white spikes far below', '黑色冰井和深处的白色冰刺'), AES_HOLE)

TA('48-05', '05｜暖屋沙发上：林峰给苏清月剥一个农场新结的橘子，她盯着监控墙说他们连门都没摸到，他说掉进去的才第一批，她说已经少了一百多个，他问橘子甜不甜', 15, SOFA2,
   [P('su_cozy', 'left', "sitting on the leather sofa under a grey cashmere blanket in profile facing frame-right, a mug of tea in both hands, her eyes on the wall of monitors", 'obj:the wall of monitors across the room', "her eyes bright with grim amusement, her lips curved in a faint sly curl, her brows lifted"),
    P('lin_home', 'right', "sitting beside her on the sofa in profile facing frame-left, peeling a small orange mandarin in his hands, his head bent over it", 'obj:the mandarin in his hands', "his eyes calm and warm, one corner of his mouth lifting, his brows soft")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, on the sofa.',
   "<su_cozy> watches the monitors and speaks the first line to <lin_home> in a low amused voice, then <lin_home> keeps peeling and answers with the second line to <su_cozy> in a calm low voice, then <su_cozy> speaks the third line to <lin_home>, and <lin_home> speaks the fourth line to <su_cozy>; after the last line he drops a mandarin segment into her mouth and she chews with her eyes still on the monitors, her eyes bright with grim amusement, her lips curved in a faint sly curl and her brows lifted, his eyes calm and warm, one corner of his mouth lifting and his brows soft.",
   "苏清月看着监控墙，用低低的、带着笑意的声音对林峰说出第一句，接着林峰继续剥着，用平静低沉的声音对苏清月答出第二句，苏清月再对林峰说出第三句，林峰再对苏清月说出第四句；最后一句之后，他把一瓣橘子放进她嘴里，她嚼着，眼睛仍盯着监控墙，她眼神发亮带着冷冷的笑意、嘴唇弯出一抹狡黠、眉毛上扬，他眼神平静温暖、嘴角微微上扬、眉头舒展。",
   SOUND_ORANGE, AES_ORANGE,
   lines=LN(('su_cozy', "他们连门都没摸到。", 'Lin'), ('lin_home', "掉进去的，才第一批。", 'Su'), ('su_cozy', "已经少了一百多个。", 'Lin'), ('lin_home', "橘子甜吗？农场新结的。", 'Su')),
   cam=push('both of them', '两人'), extra_assets=(), room={'Su', 'Lin'}, new=True,
   bg='Behind the sofa the wall of small security monitors glows cool blue and on the coffee table a glass bowl of small orange mandarins and a curl of peel sit beside a steaming mug.',
   holds='The frame holds exactly two people: Su and Lin, on the sofa, nobody else.')

insert2('48-06', '06｜插镜：监控墙上最大的屏幕里，一大片红色光点缩在白色的地形图上，一个接一个熄灭，旁边的小屏幕全是白茫茫的暴风雪，顶上一盏小红灯闪着', 6, MON_WALL,
        'Close shot of the monitor wall, the biggest screen in the middle third of the frame, nobody in the scene.',
        "On the biggest screen a dense cloud of small red dots pulses on a pale terrain map and the dots wink out one after another, thinning from the middle outward, while the smaller screens around it show only white swirling blizzard and a small red lamp above the wall blinks slowly. Nothing else is in the scene.",
        "最大的屏幕上，一大片密密的红色小光点在苍白的地形图上搏动，然后一个接一个熄灭，从中间往外越来越稀，旁边的小屏幕只有白茫茫旋转的暴风雪，墙顶上一盏小红灯慢慢地闪。画面里没有别的东西。",
        SOUND_MONWALL, 'The frame holds the monitor wall with the red dots going out, and nobody in the scene.',
        push1('the thinning red dots on the biggest screen', '最大屏幕上越来越稀的红色光点'), AES_MONWALL)

TA('48-07', '07｜雪原：几百个暴徒冻在原地谁也不敢动，独眼统帅双眼通红，骂这根本是座绞肉机，副官问要不要撤，他吼着把温压弹拉上来，找不到门就烧穿整座山', 13, FROZEN_PACK,
   [P('pang_aide', 'left', "standing in the snow in profile facing frame-right, his rifle hanging from its sling, his head turned to his commander", 'Duyan', "his lips trembling, his eyes wide and afraid, his brows pulled up"),
    P('duyan_boss', 'center-right', "standing in the snow in profile facing frame-left, a black radio handset in one raised gloved fist, his head turned to his aide", 'Pang', "his one visible eye red and wild, his lips pulled back in a savage snarl, his brows low")],
   'Medium wide two-shot, both from the head to the knees, in the middle third of the frame, in the snow clearing.',
   "<duyan_boss> raises the black radio handset and speaks the first line to <pang_aide> in a cracked furious voice, then <pang_aide> answers with the second line to <duyan_boss> in a trembling voice, then <duyan_boss> speaks the third line to <pang_aide> and the fourth line into the handset; after the last line he stares at the frozen mountain slope with a cruel wide-eyed glare, his one visible eye red and wild, his lips pulled back in a savage snarl and his brows low, <pang_aide> shrinking with his lips trembling, his eyes wide and afraid and his brows pulled up.",
   "独眼统帅举起黑色的无线电话筒，用发破的暴怒声音对副官说出第一句，接着副官用发抖的声音对统帅答出第二句，统帅再对副官说出第三句，又对着话筒说出第四句；最后一句之后，他睁着残忍的圆眼死死盯着那座冻僵的山坡，他那只露着的眼睛通红疯狂、嘴唇咧开露出牙、眉头压低，副官缩着身子，嘴唇发抖、眼睛睁大满是恐惧、眉毛上扬。",
   SOUND_FROZEN, AES_FROZEN,
   lines=LN(('duyan_boss', "这根本是座绞肉机！", 'Pang'), ('pang_aide', "统帅，要撤吗？", 'Duyan'), ('duyan_boss', "撤？把温压弹拉上来！", 'Pang'), ('duyan_boss', "我烧穿整座山！", 'Pang')),
   cam=slide('right', '右', 'Duyan stands in the middle third of the frame with the frozen crowd behind him', '独眼站在画面中间三分之一、身后是冻在原地的人群'),
   groups=[('the frozen crowd', 'back', 'obj:the snow ahead of them')], room={'Duyan', 'Pang', 'the frozen crowd'}, new=True,
   bg='Behind them hundreds of bundled men stand frozen in the white storm with their rifles lowered, none of them speaking, all sharp and in focus.',
   holds='The frame holds exactly two named men, Duyan and Pang, in front, and a large crowd of bundled men standing frozen behind them, everyone sharp and in focus.')

on, off = MIX([('eden_voice', "警告，检测到温压弹反应。", 'Lin'), ('eden_voice', "正上方引爆，岩层六成会塌方。", 'Lin'), ('su_cozy', "那是我们的温泉！", 'Lin')])
TA('48-08', '08｜控制室：红色警报灯狂闪，伊甸报告检测到温压弹，如果在正上方引爆，温泉岩层有六成概率塌方，苏清月脸色一变，林峰的眼神瞬间冷下来', 13, CTRL_ALARM,
   [P('lin_home', 'right', "sitting in the black swivel chair at the console in profile facing frame-left, his hands flat on the desk, his eyes on the console", 'obj:the console in front of him', "his jaw clenched, his eyes cold and sharp, his brows low", outfit="in a soft grey henley and dark lounge pants"),
    P('su_cozy', 'center', "standing behind his chair in profile facing frame-left, one hand gripping his shoulder, her head turned to him", 'Lin', "her lips parted, her face pale, her brows pulled high")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
   "A soft, calm, polite female synthetic voice from the speaker above the console speaks the first line and then the second line as a voice-over to <lin_home>; then <su_cozy> speaks the third line to <lin_home> in a tight breathless voice; <lin_home> sits motionless with his hands flat on the desk, his jaw clenched, his eyes cold and sharp and his brows low, while <su_cozy> grips his shoulder with her lips parted, her face pale and her brows pulled high, the red alarm pulse washing over them.",
   "控制台上方的扬声器里传出轻柔平静、礼貌的女性合成声音，以旁白的方式先说出第一句、再说出第二句，对着林峰说；接着苏清月用紧绷、喘不上气的声音对林峰说出第三句；林峰一动不动地坐着，两手平放在桌上，下颌咬紧、眼神冰冷锐利、眉头压低，苏清月抓着他的肩膀，嘴唇微张、脸色发白、眉毛高高挑起，红色警报的光一阵阵洗过两个人。" + BRISK_ZH,
   SOUND_ALARM, AES_ALARM,
   lines=on, vo=off,
   cam=push('both of them', '两人'), extra_assets=('hack_screen',), room={'Su', 'Lin'}, new=True,
   bg='Above the console a small round speaker grille glows faintly and the wall of six small monitors glows deep blue at frame-left.',
   holds='The frame holds exactly two people: Lin and Su, at the control console, nobody else.')

# ================================================================================================ 第 49 集
b49 = S.episode('剧本第49集｜雪原幽灵',
                '监控室里林峰把橘子皮丢进盘子，冷冷说有几只虫子得亲手捏死；苏清月说回来给你热汤；缓冲舱里他穿上纯白色的吉利服，苏清月提醒最后一道手动闸门只有他的手能关，厚重的暗门打开，暴风雪灌进来；他趴着爬进白茫茫的风暴；爆破组在黄色工作灯下组装温压弹，组长要扳手；一支弩箭划过，灯光圈里的人没了，只剩翻乱的雪和拖痕，组长回头；一只白手套捂住他，他被拖进雪里；林峰从雪里站起拆下起爆器；风吹开雪雾，独眼和上百个暴徒就在二十米外。', 49)
new_person(b49, 'lin_ghillie', '林峰（纯白色的吉利服，破布条似的白条覆盖全身，兜帽拉起，白色热成像护目镜推在额头上，白围巾裹着下巴）', 'man',
           'Lin, the same lean, athletic Chinese man in his early thirties as in the reference, wearing a pure-white ghillie suit of frayed white strips with the hood up over a charcoal henley, white thermal goggles pushed up on his forehead and a white scarf around his chin.',
           '林峰，和参考图是同一位三十出头、身形精瘦结实的中国男性，穿着纯白色的吉利服，破布条似的白条覆盖全身，兜帽拉起，里面是炭灰色亨利衫，白色热成像护目镜推在额头上，白围巾裹着下巴。',
           'a pure-white ghillie suit of frayed white strips with the hood up, white thermal goggles pushed up on his forehead and a white scarf around his chin', 'a calm, cold, level expression', ref='lin_work')
new_person(b49, 'qian_chief', '爆破组长老钱（四十多岁，鼓鼓囊囊的橄榄绿棉工装，腰挂工具带，厚毛手套，针织面罩卷到鼻子上）', 'man',
           'Qian, a stocky Chinese man in his forties with a rough squinting face, wearing a bulky olive-drab padded coverall with a tool belt, thick fur-lined gloves and a frosted knitted mask rolled up over his nose.',
           '爆破组长老钱，一个四十多岁、壮实的中国男性，面相粗糙、眯着眼，穿着鼓鼓囊囊的橄榄绿棉工装，腰挂工具带，戴着厚毛手套，结霜的针织面罩卷到鼻子上。',
           'a rough squinting face, a bulky olive-drab padded coverall with a tool belt, thick fur-lined gloves and a frosted knitted mask rolled up over his nose', 'a tense, irritable expression', eth='Chinese')
new_person(b49, 'xiaoliu_bomber', '爆破手小刘（二十多岁，橄榄绿棉工装，带护耳的毛帽，脸颊冻得通红）', 'man',
           'Xiaoliu, a young Chinese man in his twenties with raw red cheeks and watery eyes, wearing an olive-drab padded coverall and a fur-lined hat with ear flaps and thick gloves.',
           '爆破手小刘，一个二十多岁的年轻中国男性，脸颊冻得通红、眼睛湿润，穿着橄榄绿棉工装，戴着带护耳的毛帽和厚手套。',
           'raw red cheeks and watery eyes, an olive-drab padded coverall, a fur-lined hat with ear flaps and thick gloves', 'a shivering, tired expression', eth='Chinese')
b49.prop('thermo_bomb', '军用温压弹（一个油桶大小的橄榄绿圆柱形炸弹，躺在钢板雪橇上，弹头罩打开）',
         'A huge olive-drab thermobaric bomb the size of an oil drum lying on a steel sled with its nose cone open. The reference fixes its look.',
         '一个油桶大小的橄榄绿色圆柱形温压弹，躺在钢板雪橇上，弹头罩打开。参考图固定它的外形。',
         'A photorealistic shot of a huge olive-drab thermobaric bomb the size of an oil drum lying on a steel sled with its nose cone open, on snow, against a dark background.')
b49.prop('detonator', '起爆器（一个巴掌大的灰色金属盒，带铰链盖的开关和一盏小红灯）',
         'A palm-sized grey metal detonator box with a hinged switch cover and a small red LED. The reference fixes its look.',
         '一个巴掌大的灰色金属盒起爆器，带铰链盖的开关和一盏小红灯。参考图固定它的外形。',
         'A photorealistic close shot of a palm-sized grey metal detonator box with a hinged switch cover and a small red LED, resting on dark steel, against a dark background.')
b49.character('LinGhillie', 'lin_ghillie', LIN_EN, LIN_ZH)
b49.character('Qian', 'qian_chief', QIAN_EN, QIAN_ZH)
b49.character('Xiaoliu', 'xiaoliu_bomber', XIAOLIU_EN, XIAOLIU_ZH)

TA('49-01', '01｜监控室：林峰把橘子皮丢进盘子，冷冷说有几只虫子得亲手捏死，苏清月问他一个人去，他说人多了会留脚印，她说回来给你热汤', 15, SOFA2,
   [P('su_cozy', 'left', "sitting on the leather sofa under a grey cashmere blanket in profile facing frame-right, her head turned up to him", 'Lin', "her eyes steady and worried, her lips pressed in a firm line, her brows pulled together"),
    P('lin_home', 'right', "standing at the end of the sofa in profile facing frame-left, dropping an orange peel onto a small white plate, his eyes on her", 'Su', "his eyes cold and calm, his jaw set, his brows low")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the sofa.',
   "<lin_home> drops the orange peel on the plate and speaks the first line to <su_cozy> in a low cold voice, then <su_cozy> answers with the second line to <lin_home> in a steady voice, then <lin_home> speaks the third line to <su_cozy> and <su_cozy> speaks the fourth line to <lin_home>; after the last line he squeezes her hand once and turns toward the equipment room door at frame-right, his eyes cold and calm, his jaw set and his brows low, her eyes steady and worried, her lips pressed in a firm line and her brows pulled together.",
   "林峰把橘子皮丢在小白盘子里，用低沉冰冷的声音对苏清月说出第一句，接着苏清月用沉稳的声音对林峰答出第二句，林峰再对苏清月说出第三句，苏清月再对林峰说出第四句；最后一句之后，他握了握她的手，转身朝画面右边的装备间门走去，他眼神冰冷平静、下颌绷住、眉头压低，她眼神沉稳带着担心、嘴唇抿成一条线、眉头拧在一起。",
   SOUND_BAR, AES_ORANGEWARM,
   lines=LN(('lin_home', "几只虫子，得亲手捏死。", 'Su'), ('su_cozy', "八十五度，你一个人去？", 'Lin'), ('lin_home', "人多了，会留脚印。", 'Su'), ('su_cozy', "回来，汤给你热着。", 'Lin')),
   cam=track('the two of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the wall of small security monitors glows cool blue and the glass bowl of mandarins and the white plate with the orange peel sit on the coffee table.',
   holds='The frame holds exactly two people: Su and Lin, at the sofa, nobody else.')

on, off = MIX([('eden_voice', "外门风速九级。", 'Lin'), ('su_cozy', "最后一道闸门，只有你能关。", 'Lin'), ('lin_ghillie', "我知道，回来再关。", 'Su'), ('eden_voice', "外门开启。", 'Lin')])
TA('49-02', '02｜缓冲舱：林峰穿着纯白色的吉利服站在厚重的暗门前，伊甸报告外面风速九级，苏清月说最后一道手动闸门只有他的手能关，他说回来再关，门转开，暴风雪灌进来', 14, AIR_OUT,
   [P('su_cozy', 'left', "standing on the white tiles in profile facing frame-right, one hand reaching up to straighten the white scarf at his chin, her eyes on his face", 'Lin', "her eyes steady and worried, her lips pressed in a firm line, her brows pulled together"),
    P('lin_ghillie', 'center-right', "standing in front of the closed hatch in profile facing frame-right, his head turned back toward her, a black crossbow slung across his white back", 'Su', "his eyes calm and warm, his jaw set, his brows level")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the airlock.',
   "A soft, calm, polite female synthetic voice from the wall speaker speaks the first line as a voice-over; then <su_cozy> speaks the second line to <lin_ghillie> in a low firm voice as she tightens his scarf, and <lin_ghillie> answers with the third line to <su_cozy> in a low steady voice; then the synthetic voice speaks the fourth line and the heavy steel hatch swings open behind him, a roar of white storm pouring in as <lin_ghillie> pulls his goggles down and steps toward it, his eyes calm and warm, his jaw set and his brows level, her eyes steady and worried, her lips pressed in a firm line and her brows pulled together.",
   "墙上的扬声器里传出轻柔平静、礼貌的女性合成声音，以旁白的方式说出第一句；接着苏清月一边帮他系紧围巾，一边用低而坚定的声音对林峰说出第二句，林峰用低沉平稳的声音对苏清月答出第三句；然后合成声音说出第四句，他身后厚重的钢门转开，白色的暴风雪轰地灌进来，林峰把护目镜拉下来，朝门走去，他眼神平静温暖、下颌绷住、眉毛平直，她眼神沉稳带着担心、嘴唇抿成一条线、眉头拧在一起。" + BRISK_ZH,
   SOUND_HATCH, AES_AIRLOCK,
   lines=on, vo=off,
   cam=push('both of them', '两人'), extra_assets=('hack_screen',), room={'Su', 'Lin'}, new=True,
   bg='On the wall above the steel bench a small round speaker grille glows faintly and the heavy round steel hatch door fills the right of the frame.',
   holds='The frame holds exactly two people: Su and Lin, in the airlock, nobody else.')

TA('49-03', '03｜暴风雪里：纯白色的林峰趴在雪地里，用手肘一点一点往前爬，白色的吉利服和白色的暴风雪几乎融成一片，只有护目镜里透出一点淡淡的青光', 8, WHITEOUT,
   [P('lin_ghillie', 'center', "lying flat on his stomach in the snow in profile facing frame-right, the black crossbow held across his forearms, pulling himself forward on his elbows with his white hood low and his goggles over his eyes", 'obj:the swirling white ahead of him', "his jaw set, his lips pressed tight, his brows level")],
   'Medium wide shot, one man lying on the snow from the head to the feet, in the middle third of the frame.',
   "<lin_ghillie> crawls forward through the snow on his elbows a little at a time, the crossbow across his forearms, the white strips of his suit stirring in the wind, his jaw set, his lips pressed tight and his brows level.",
   "林峰趴在雪地里，用手肘一点一点往前爬，弩横在小臂上，吉利服上的白条在风里轻轻抖动，下颌绷住、嘴唇抿紧、眉毛平直。",
   SOUND_CRAWL, AES_WHITEOUT,
   cam=follow('him', '他', 'he stays in the middle third of the frame as the white storm streams past behind him', '他留在画面中间三分之一、白色的暴风雪在他身后流过'), room={'Lin'}, new=True,
   bg='All around him the snowfield is a howling whiteout with a dark dead stump at frame-right, nobody else anywhere in the frame.',
   holds='The frame holds one person: Lin, alone in the snow.')

TA('49-04', '04｜爆破点：爆破组长老钱蹲在温压弹边让小刘递那个型号的扳手，小刘说手都冻僵了，老钱说装完这颗咱们就是功臣', 15, BOMB_SITE,
   [P('qian_chief', 'left', "kneeling beside the open nose cone of the huge bomb in profile facing frame-right, a long steel wrench in one gloved fist, his head turned to the young man", 'Xiaoliu', "his eyes squinting and irritable, his lips pulled tight, his brows low"),
    P('xiaoliu_bomber', 'right', "crouching beside an open steel toolbox in profile facing frame-left, blowing on his gloved hands, his head turned to the chief", 'Qian', "his eyes watery, his lips trembling with cold, his brows pulled up")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, beside the bomb.',
   "<qian_chief> speaks the first line to <xiaoliu_bomber> in a rough irritable voice, then <xiaoliu_bomber> answers with the second line to <qian_chief> in a shivering voice, then <qian_chief> speaks the third line to <xiaoliu_bomber> and <xiaoliu_bomber> answers with the fourth line to <qian_chief>; after the last line <qian_chief> turns back to the bomb and holds one open glove out behind him without looking, his eyes squinting and irritable, his lips pulled tight and his brows low, <xiaoliu_bomber> with his eyes watery, his lips trembling with cold and his brows pulled up.",
   "爆破组长老钱用粗哑不耐烦的声音对小刘说出第一句，接着小刘用发抖的声音对老钱答出第二句，老钱再对小刘说出第三句，小刘再对老钱答出第四句；最后一句之后，老钱转回身对着炸弹，不回头，把一只戴着手套的手朝后面伸出去，他眯着眼、嘴唇抿紧、眉头压低，小刘眼睛湿润、嘴唇冻得发抖、眉毛上扬。",
   SOUND_BOMBSITE, AES_BOMBSITE,
   lines=LN(('qian_chief', "递我那个型号的扳手。", 'Xiaoliu'), ('xiaoliu_bomber', "组长，手都冻僵了。", 'Qian'), ('qian_chief', "装完这颗，咱们就是功臣。", 'Xiaoliu'), ('xiaoliu_bomber', "是，组长。", 'Qian')),
   cam=pull('the two of them at the bomb', '炸弹旁的两人', 'the whole lamp-lit circle with the guards at its edge', '整个被灯照亮的圈和圈边站着的守卫'), extra_assets=('thermo_bomb',),
   groups=[('the crew and guards', 'back', 'obj:the bomb')], room={'Qian', 'Xiaoliu', 'the crew and guards'}, new=True,
   bg='Around them in the lamp light three more crew members work at the bomb with their backs half turned and a few vague armed guards stand at the edge of the light, all bundled and none of them speaking.',
   holds='The frame holds exactly two named men, Qian and Xiaoliu, in front, and a few bundled crew and guards around the bomb behind them, everyone sharp and in focus.')

TA('49-05', '05｜暴风雪边缘：林峰跪在雪里，把弩端平，护目镜里青光一闪，一支白色的弩箭从弩槽里飞出去，划过飘雪，消失在前面黄色的灯光里', 6, WHITEOUT,
   [P('lin_ghillie', 'left', "kneeling in the snow in profile facing frame-right, the black crossbow raised to his shoulder and aimed at the faint yellow lamp glow far ahead, his goggles over his eyes", 'obj:the faint yellow lamp glow far ahead in the storm', "his jaw set, his lips pressed tight, his brows level")],
   'Medium wide shot, one man kneeling in the snow from the head to the knees, in the middle third of the frame.',
   "<lin_ghillie> holds the crossbow steady against his shoulder, breathes out, and the pale bolt leaves the groove and streaks across the frame into the snow toward the yellow lamp glow, then he lowers the crossbow a little, his jaw set, his lips pressed tight and his brows level.",
   "林峰把弩稳稳抵在肩上，呼出一口气，白色的弩箭离开弩槽，划过画面飞进飘雪里，朝着黄色的灯光飞去，然后他把弩放低了一点，下颌绷住、嘴唇抿紧、眉毛平直。",
   SOUND_BOLT, AES_CROSSBOW,
   cam=push1('him', '他'), room={'Lin'}, new=True,
   bg='Far ahead at frame-right a faint yellow lamp glow shows through the swirling white and nobody else is anywhere in the frame.',
   holds='The frame holds one person: Lin, kneeling alone in the snow.')

insert2('49-06', '06｜插镜：黄色工作灯的圈里空了，温压弹独自躺在雪橇上，扳手半埋在雪里，雪地上翻出几道深深的拖痕伸进黑暗，几滴冻成珠子的暗红点落在白雪上，一盏灯在三脚架上晃', 6, BOMB_EMPTY,
        'Wide low shot of the empty lamp-lit circle, the bomb in the middle third of the frame, nobody in the scene.',
        "The huge bomb lies alone on its steel sled in the empty circle of yellow lamp light, one tripod lamp swaying, a long steel wrench half-sunk in the churned snow at its foot, deep drag furrows leading away into the dark at frame-left and a few dark red drops freezing into beads on the white. Nothing moves except the swaying lamp and the blowing snow.",
        "黄色工作灯的圈里空了，巨大的温压弹独自躺在钢雪橇上，一盏三脚架上的灯晃着，一把长扳手半埋在被翻乱的雪里落在炸弹脚边，几道深深的拖痕往画面左边的黑暗里伸去，几滴暗红色的点在白雪上冻成珠子。除了晃动的灯和吹着的雪，什么都不动。",
        SOUND_EMPTY, 'The frame holds the empty lamp-lit circle with the bomb and the drag furrows, and nobody in the scene.',
        slide('left', '左', 'the drag furrows leading into the dark at the left of the frame', '通向画面左边黑暗的拖痕'), AES_EMPTYCIRCLE, extra_assets=('thermo_bomb',))

on, off = MIX([('qian_chief', "递我那个扳手……人呢？", 'Qian')])
TA('49-07', '07｜爆破点：老钱伸手要扳手，转过头，身后一个人都没有，他的眼睛瞬间睁大，一只戴白手套的手从他身后的白雪里闪出来捂住他的嘴，把他往后拖进雪里', 8, BOMB_EMPTY,
   [P('qian_chief', 'center-right', "standing beside the bomb in profile facing frame-left, one open glove held out behind him, his head just turning back over his shoulder", 'obj:the empty snow where his crew stood', "his lips parted, his eyes wide and frozen, his brows pulled high")],
   'Medium shot, one man from the head to the knees, in the middle third of the frame, beside the bomb.',
   "<qian_chief> holds his open glove out and murmurs the first line to himself toward the empty circle, turns his head and sees no one, his lips parted, his eyes wide and frozen and his brows pulled high, and a white-gloved hand flashes out of the white drift behind him, clamps over his mouth and drags him backward into the snow, out of the frame.",
   "老钱伸着手套朝空荡荡的圈里说出第一句，转过头，发现一个人都没有，嘴唇微张、眼睛睁大发直、眉毛高高挑起，这时一只戴白手套的手从他身后的白雪里闪出来，捂住他的嘴，把他往后拖进雪里，离开画面。",
   SOUND_GRAB, AES_GRAB,
   vo=on, cam=push1('his face', '他的脸'), extra_assets=('thermo_bomb',), room={'Qian'}, new=True,
   bg='Behind him a white drift of snow banks against the lamp stand and the swirling storm swallows the edges of the frame, nobody else visible.',
   holds='The frame holds one person: Qian, standing alone beside the bomb, and only a white-gloved hand emerging from the snow behind him at the end.')

TA('49-08', '08｜爆破点：林峰从雪里缓缓站起，积雪从他白色的肩上倒下来，他走到温压弹边蹲下，从弹体上取下一个巴掌大的灰色起爆器，上面一盏小红灯在闪', 8, BOMB_EMPTY,
   [P('lin_ghillie', 'center', "rising from the snow beside the bomb in profile facing frame-right, loose snow pouring off his white shoulders, then crouching to hold a small grey detonator box in his white glove, his eyes on the box", 'obj:the small grey detonator box in his glove', "his jaw set, his lips pressed tight, his brows low")],
   'Medium wide shot, one man from the head to the knees, in the middle third of the frame, beside the bomb.',
   "<lin_ghillie> rises slowly out of the white drift with loose snow pouring off his shoulders and hood, steps to the bomb and crouches, lifts a small grey detonator box out of its socket and holds it up in his white glove while a small red light pulses on it, his jaw set, his lips pressed tight and his brows low.",
   "林峰缓缓从白色的雪堆里站起来，松散的积雪从肩膀和兜帽上倒下，他走到炸弹边蹲下，从插座里取出一个巴掌大的灰色起爆器，举在白手套里，上面一盏小红灯在闪，他下颌绷住、嘴唇抿紧、眉头压低。",
   SOUND_RISE, AES_RISE,
   cam=pull('the detonator in his glove', '他手套里的起爆器', 'him standing in white beside the bomb with the swirling storm around him', '他一身白色站在炸弹边、暴风雪在周围旋转'), extra_assets=('thermo_bomb', 'detonator'), room={'Lin'}, new=True,
   bg='Around him the empty circle of yellow lamps sways in the swirling white and nobody else is anywhere in the frame.',
   holds='The frame holds one person: Lin, alone beside the bomb.')

TA('49-09', '09｜风吹开雪雾：林峰一身白色站在温压弹边，他身后二十米外，独眼统帅和上百个暴徒端着枪，眼睁睁看着他', 8, FACEOFF,
   [P('lin_ghillie', 'left', "standing beside the bomb in profile facing frame-right, a small grey detonator in his white glove, his head turned toward the crowd across the snow", 'Duyan', "his jaw loose, one corner of his mouth lifting coldly, his brows level"),
    P('duyan_boss', 'center-right', "standing at the front of the crowd in profile facing frame-left, one hand frozen on his rifle sling, his head turned toward the white figure", 'Lin', "his one visible eye wide and shocked, his lips parted, his brows pulled high")],
   'Wide shot of the snowfield, Lin and Duyan small in the frame, the two of them in the middle third of the frame.',
   "A gust tears the white mist open and <lin_ghillie> stands at the bomb in his white suit looking calmly across the snow at <duyan_boss> and the hundreds of bundled men with rifles standing about twenty metres away, who all stare back frozen, <lin_ghillie> with his jaw loose, one corner of his mouth lifting coldly and his brows level, <duyan_boss> with his one visible eye wide and shocked, his lips parted and his brows pulled high.",
   "一阵风撕开白色的雪雾，林峰一身白色站在炸弹边，平静地隔着雪地看着二十米外的独眼统帅和上百个端着枪的鼓鼓囊囊的暴徒，他们全都僵住盯着他，林峰下颌放松、嘴角冷冷一挑、眉毛平直，独眼那只露着的眼睛睁大满是震惊、嘴唇微张、眉毛高高挑起。",
   SOUND_FACE, AES_FACE,
   cam=rise('Lin and the crowd facing each other across the snow', '隔着雪地对峙的林峰和人群'), extra_assets=('thermo_bomb', 'detonator'),
   groups=[('the armed crowd', 'right', 'Lin')], room={'Lin', 'Duyan', 'the armed crowd'}, new=True,
   bg='Behind Duyan hundreds of bundled men with rifles stand in a wide arc, all frozen and staring, with a black tracked command vehicle behind them.',
   holds='The frame holds exactly two named men, Lin at frame-left and Duyan in front of the crowd at frame-center-right, and a large crowd of bundled armed men behind Duyan, everyone sharp and in focus.')

# ================================================================================================ 第 50 集
b50 = S.episode('剧本第50集｜绝对零度的恐慌',
                '二十米的距离，独眼统帅下令开火，上百支枪对准林峰，林峰说晚安，按下起爆器的副开关；耀眼的白光和浓烟吞掉整片雪地，枪声乱响；烟被风吹散，雪地上空空如也，连个脚印都没有，独眼崩溃喊他是山里的鬼，下令撤退，几百个暴徒丢盔弃甲地逃；缓冲舱里苏清月用热毛巾擦去林峰脸上的冰霜，发现他的手冰得吓人，他说泡泡温泉就好，亲了亲她的手；他们走向温泉；控制台上起爆器的小红灯亮起，杯中的水泛起波纹；溶洞顶上一块巨大的岩石传出断裂声。', 50)

TA('50-01', '01｜雪原：独眼统帅尖叫着让上百个暴徒开火把他打成筛子，枪口齐刷刷抬起，林峰低头看了一眼手里的起爆器，用拇指掀开副开关的盖子，对他们说晚安', 12, ARC_FIRE,
   [P('lin_ghillie', 'left', "standing beside the bomb in profile facing frame-right, the detonator in his white glove with his thumb flipping up a small hinged cover, his head lifted toward the crowd", 'Duyan', "his jaw loose, one corner of his mouth lifting coldly, his brows level"),
    P('duyan_boss', 'center-right', "standing at the front of the crowd in profile facing frame-left, one arm thrust out toward Lin, his head turned toward the white figure", 'Lin', "his one visible eye wide and bloodshot, his lips pulled back in a screaming snarl, his brows low")],
   'Wide shot of the snowfield, Lin and Duyan small in the frame, the two of them in the middle third of the frame.',
   "<duyan_boss> thrusts his arm out toward <lin_ghillie> and screams the first line to <lin_ghillie> as an order for the crowd behind him, and the hundreds of bundled men snap their rifles up to their shoulders, then <lin_ghillie> flips up the small cover with his thumb and speaks the second line to <duyan_boss> in a low cold voice, <lin_ghillie> with his jaw loose, one corner of his mouth lifting coldly and his brows level, <duyan_boss> with his one visible eye wide and bloodshot, his lips pulled back in a screaming snarl and his brows low.",
   "独眼统帅伸出手臂，朝着人群尖叫出第一句，他身后几百个鼓鼓囊囊的暴徒齐刷刷把步枪抬到肩上，接着林峰用拇指掀开小盖子，用低沉冰冷的声音对独眼说出第二句，林峰下颌放松、嘴角冷冷一挑、眉毛平直，独眼那只露着的眼睛睁大满是血丝、嘴唇咧开尖叫、眉头压低。" + BRISK_ZH,
   SOUND_FIRE, AES_FACE,
   lines=LN(('duyan_boss', "开火！把他打成筛子！", 'Lin'), ('lin_ghillie', "晚安，各位。", 'Duyan')),
   cam=push1('Lin and the thumb on the detonator', '林峰和按在起爆器上的拇指'), extra_assets=('thermo_bomb', 'detonator'),
   groups=[('the armed crowd', 'right', 'Lin')], room={'Lin', 'Duyan', 'the armed crowd'}, new=True,
   bg='Behind Duyan hundreds of bundled men with rifles stand in a wide arc, raising their rifles to their shoulders, with a black tracked command vehicle behind them.',
   holds='The frame holds exactly two named men, Lin at frame-left and Duyan in front of the crowd at frame-center-right, and a large crowd of bundled armed men behind Duyan, everyone sharp and in focus.')

insert2('50-02', '02｜特写到全景：温压弹的弹壳从里面爆开一道刺眼的白光，浓浓的白烟像一堵墙向外翻涌，吞掉雪地和灯光，一道道枪口的火舌在烟里乱扫', 8, SMOKE,
        'Medium wide shot of the bomb on its sled, the bomb in the middle third of the frame, nobody visible.',
        "The casing of the huge bomb bursts open from within in a blinding white flash that fills the whole frame, then thick white smoke boils outward from it in a rolling wall that swallows the snow, the sled and the far black vehicle, and orange muzzle flashes stab blindly through the smoke from all sides. Nothing else is in the scene.",
        "巨大的炸弹弹壳从里面炸开一道刺眼的白光灌满整个画面，然后浓浓的白烟像一堵翻涌的墙从它身上向外涌，吞掉雪地、雪橇和远处的黑色车辆，橙色的枪口火舌从四面八方在烟里盲目乱扫。画面里没有别的东西。",
        SOUND_FLASH, 'The frame holds the bomb, the white flash, the boiling smoke wall and the muzzle flashes, and nobody visible.',
        pull('the bomb bursting in the white flash', '炸开白光的炸弹', 'the whole snowfield swallowed by the wall of white smoke', '被白色烟墙吞没的整片雪原'), AES_FLASH, extra_assets=('thermo_bomb',))

on, off = MIX([('pang_aide', "统帅，连个脚印都没有！", 'Duyan'), ('duyan_boss', "鬼……他是这座山的鬼！", 'Pang'), ('duyan_boss', "撤退！马上撤退！", 'Pang')])
TA('50-03', '03｜烟散后：白烟被风吹散，雪地上空空如也，只剩光秃秃的炸弹壳，没有人也没有脚印，副官说连个脚印都没有，独眼统帅精神崩溃喊他是山里的鬼，下令撤退', 12, EMPTY_SNOW,
   [P('pang_aide', 'left', "standing in the snow in profile facing frame-right, his rifle lowered, his head turned to his commander", 'Duyan', "his lips trembling, his eyes wide and terrified, his brows pulled high"),
    P('duyan_boss', 'center-right', "standing in the snow in profile facing frame-left, both fists clenched at his sides, his head turned to his aide", 'Pang', "his one visible eye wild and glassy, his lips pulled back from his teeth, his brows pulled together")],
   'Medium wide two-shot, both from the head to the knees, in the middle third of the frame, on the empty snowfield.',
   "As the smoke blows away <pang_aide> speaks the first line to <duyan_boss> in a trembling voice, then <duyan_boss> speaks the second line to <pang_aide> in a cracked broken voice and then the third line, his one visible eye wild and glassy, his lips pulled back from his teeth and his brows pulled together, <pang_aide> with his lips trembling, his eyes wide and terrified and his brows pulled high, and after the last line they both stumble backward from the empty snow.",
   "烟被风吹散时，副官用发抖的声音对独眼统帅说出第一句，接着独眼用发破、崩溃的声音对副官说出第二句，然后是第三句，他那只露着的眼睛疯狂发直、嘴唇咧开露出牙、眉头拧在一起，副官嘴唇发抖、眼睛睁大满是恐惧、眉毛高高挑起，最后一句之后两个人一起踉跄着从空空的雪地往后退。",
   SOUND_GLOOM, AES_GLOOM,
   lines=LN(('pang_aide', "统帅，连个脚印都没有！", 'Duyan'), ('duyan_boss', "鬼……他是这座山的鬼！", 'Pang'), ('duyan_boss', "撤退！马上撤退！", 'Pang')),
   cam=pull('the two men in front of the empty snow', '空雪地前的两个人', 'the whole smooth snowfield with not one footprint on it', '整片没有一个脚印的平滑雪原'), extra_assets=('thermo_bomb',), room={'Duyan', 'Pang'}, new=True,
   bg='Behind them the smooth snowfield lies empty with no footprints, the split bomb casing on its sled and the dark pines far away.',
   holds='The frame holds exactly two people: Duyan and Pang, on the snowfield, nobody else.')

insert2('50-04', '04｜插镜：几百个暴徒在灰色的暴风雪里乱成一团往画面右边逃，扔掉的步枪躺在雪上，远处几辆黑色履带车掉头亮起红色的尾灯', 8, RETREAT,
        'Wide shot of the snowfield, the fleeing mass in the middle third of the frame, no named person in the scene.',
        "Hundreds of small dark figures stream away across the snowfield toward frame-right in a disordered panicked mass, throwing down their rifles that lie scattered on the white, while at the far edge of the frame a few black tracked vehicles grind around to flee with their red tail lights glowing and the storm swallows them. Nothing else is in the scene.",
        "几百个小小的黑色人影在雪原上乱成一团，朝画面右边逃去，扔下的步枪散落在白雪上，画面远处几辆黑色履带车掉头逃走，红色的尾灯亮着，风暴把它们吞没。画面里没有别的东西。",
        SOUND_RETREAT, 'The frame holds the wide snowfield with the fleeing mass and the turning vehicles, and no named person in the scene.',
        rise('the whole panicked retreat swallowed by the storm', '被风暴吞没的整场溃逃'), AES_RETREAT, groups=[('the fleeing mass', 'back', 'obj:the storm ahead of them')])

TA('50-05', '05｜缓冲舱：林峰解开吉利服，头发上挂着融化的霜，苏清月用热毛巾擦去他脸上的冰霜，问解决了吗，他说弹废了外面的人不用管，她握住他的手问怎么这么凉，他说泡泡温泉就好，低头亲了亲她的手', 15, AIR_OUT,
   [P('su_cozy', 'left', "standing on the white tiles in profile facing frame-right, a steaming white towel pressed against his cheek in one hand, her other hand wrapped around his gloveless hand, her eyes on his face", 'Lin', "her eyes shining and worried, her lips pressed in a soft tight line, her brows pulled together"),
    P('lin_ghillie', 'center-right', "standing in profile facing frame-left, his white ghillie suit unzipped and hanging off his shoulders over a charcoal henley, frost melting in his black hair and white goggles hanging at his neck, his head lowered toward her", 'Su', "his eyes tired and warm, one corner of his mouth lifting, his brows soft", outfit="in a white ghillie suit unzipped and hanging off his shoulders over a charcoal henley, frost melting in his black hair and white goggles hanging at his neck")],
   'Medium close two-shot, both from the head to the waist, in the middle third of the frame, in the airlock.',
   "<su_cozy> wipes the frost from his face with the steaming towel and speaks the first line to <lin_ghillie> in a soft anxious voice, then <lin_ghillie> answers with the second line to <su_cozy> in a low easy voice, then <su_cozy> takes his hand in both of hers and speaks the third line to <lin_ghillie>, and <lin_ghillie> speaks the fourth line to <su_cozy>; after the last line he raises her hand and presses a kiss to her knuckles, his eyes tired and warm, one corner of his mouth lifting and his brows soft, her eyes shining and worried, her lips pressed in a soft tight line and her brows pulled together.",
   "苏清月用冒着热气的毛巾擦去他脸上的霜，用轻柔不安的声音对林峰说出第一句，接着林峰用低沉轻松的声音对苏清月答出第二句，苏清月再用两只手握住他的手，对林峰说出第三句，林峰再对苏清月说出第四句；最后一句之后，他抬起她的手，在她的指节上亲了一下，他眼神疲惫温暖、嘴角微微上扬、眉头舒展，她眼睛发亮带着担心、嘴唇抿成柔软的一条线、眉头拧在一起。",
   SOUND_TOWEL, AES_TOWEL,
   lines=LN(('su_cozy', "解决了？", 'Lin'), ('lin_ghillie', "弹废了，外面的人不用管。", 'Su'), ('su_cozy', "你的手，怎么这么凉？", 'Lin'), ('lin_ghillie', "没事，泡泡温泉就好。", 'Su')),
   cam=push1('their joined hands and faces', '两人握在一起的手和脸'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the heavy round steel hatch door is shut with frost thick on its rim and the steel bench with the white polar suits stands against the left wall.',
   holds='The frame holds exactly two people: Su and Lin, in the airlock, nobody else.')

TA('50-06', '06｜通往温泉的小路：林峰牵着苏清月的手沿着发着蓝色苔藓光的小路走向温泉，他说先去泡温泉，她说先让我把你的手焐热', 10, HC_TUNNEL,
   [P('su_cozy', 'left', "walking along the glowing path hand in hand with him in profile facing frame-right, both of her hands wrapped around his one hand, her eyes on his face", 'Lin', "her eyes bright and tender, her lips curved in a soft sweet smile, her brows soft"),
    P('lin_home', 'center-right', "walking beside her in profile facing frame-right, his hand held in both of hers, his head turned to her", 'Su', "his eyes warm and tired, one corner of his mouth lifting, his brows soft", outfit=LIN_ROBE)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, on the mossy path.',
   "<lin_home> leads <su_cozy> along the path and speaks the first line to <su_cozy> in a low warm voice, then <su_cozy> speaks the second line to <lin_home> in a soft firm voice and lifts his hand to her cheek, her eyes bright and tender, her lips curved in a soft sweet smile and her brows soft, his eyes warm and tired, one corner of his mouth lifting and his brows soft.",
   "林峰牵着苏清月沿着小路往前走，用低沉温暖的声音对她说出第一句，接着苏清月用轻柔坚定的声音对林峰说出第二句，把他的手贴到自己的脸颊上，她眼神明亮温柔、嘴唇弯出一个柔软甜蜜的笑、眉头舒展，他眼神温暖疲惫、嘴角微微上扬、眉头舒展。",
   SOUND_WALK, AES_WALK,
   lines=LN(('lin_home', "走，先去泡温泉。", 'Su'), ('su_cozy', "先让我，把你的手焐热。", 'Lin')),
   cam=track('the two of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='Behind them the turquoise hot spring pool glimmers under rolling white mist and the walls of the cavern glow with blue moss.',
   holds='The frame holds exactly two people: Su and Lin, on the mossy path, nobody else.')

insert2('50-07', '07｜插镜：控制台上，那个巴掌大的灰色起爆器盒子里，一盏小红灯悄悄亮起并一明一暗地闪，旁边玻璃杯里的水面荡开一圈圈同心的波纹', 8, CTRL_DET,
        'Close shot of the console, the detonator box in the middle third of the frame, nobody in the scene.',
        "On the dark steel console a small grey detonator box lies beside a tall glass of water; a tiny red LED on the box quietly lights and begins to pulse, and the surface of the water in the glass starts to shiver, concentric rings spreading outward from its center again and again. Nothing else is in the scene.",
        "深色钢制控制台上，一个巴掌大的灰色起爆器盒子躺在一杯高玻璃杯水的旁边；盒子上一盏小红灯悄悄亮起并开始一明一暗地闪，玻璃杯里的水面开始颤动，一圈圈同心的波纹一次又一次从中心扩散开。画面里没有别的东西。",
        SOUND_DET, 'The frame holds the console with the detonator box and the glass of water, and nobody in the scene.',
        push1('the trembling water in the glass', '玻璃杯里颤动的水面'), AES_DET, extra_assets=('detonator',))

insert2('50-08', '08｜插镜：溶洞天花板上，一道细细的黑色裂缝在发光的蓝色苔藓里飞快地爬开，悬在温泉上方的那块巨大岩石发出深沉的断裂声，白灰和碎石落进冒着热气的温泉，白雾惊起打转', 10, HC_QUAKE,
        'Wide low shot of the cavern ceiling above the hot spring, the huge hanging slab in the middle third of the frame, nobody in the scene.',
        "High in the cavern ceiling a thin black fissure races across the dark rock through the glowing blue moss and splits the huge slab that hangs above the steaming pool, fine white dust and fist-sized stones rain down in glittering streams into the turquoise water with heavy splashes and the white mist swirls up in startled coils. Nothing else is in the scene.",
        "溶洞高高的天花板上，一道细细的黑色裂缝穿过发光的蓝色苔藓在深色岩石上飞快地爬开，把悬在冒着热气的温泉上方那块巨大的岩石劈开，细细的白灰和拳头大的石块一道道闪着光落进青绿色的水里，砸起沉重的水花，白雾惊起一圈圈打转。画面里没有别的东西。",
        SOUND_QUAKE, 'The frame holds the cavern ceiling with the cracking slab, the pool and the falling stones, and nobody in the scene.',
        tilt('the cracking slab high in the ceiling', '天花板高处正在裂开的岩石'), AES_QUAKE)

doc = S.finish()
