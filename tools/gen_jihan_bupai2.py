#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》补拍包 2（2026-10-15）——取代补拍包 1（补拍包 1 以 009 为底，已经接不上后面的批次）。
以 018（剧本第 45–46 集）的 JSON 为底（style／素材／角色逐字复制），放在 `极寒末日_隐秘安全屋/补拍/`；
**必须等 009→010→011→012→017→018 在插件里全部跑完再追加**，追加窗口不要勾“每集／总／任务秒数”。

起因（hh 2026-10-15 10:11）：补拍里先确定的是两件事——① 末日降临：群众的状况、世界的状况需要一个过程；② 女主怎么到男主那里：这段遭遇需要过程。
“既然是 AI 为什么不写大场面？我相信可以的，角色表演写好一点。”
我对照 009 查到的缺口：
  · 降临（剧本第 6 集 01、02 号）只有 10 秒、一条街、一个路口，没有“全城”的尺度，也没有一个人从“热闹”到“冻住”的过程；
  · 苏清月从酒窖到林峰那里（剧本第 8 集）只有“酒窖对峙”（1 个 6 秒镜头）和“雪原里走”（1 个 8 秒镜头）：她怎么出楼、怎么走过冻城、怎么过冰河、怎么差点倒在路上，全是空的。
写法＝018 同一套（每个任务 15 秒左右，句间留约 0.9 秒、不超过 1.5 秒；有台词的任务结尾带一个动作；大场面把主体、光、特效起点状态写进开场图；
每个任务一句“光和空气”；运镜每个任务不同，写“动作＋终点”）。这套 15 秒写法是先行测试版，hh 明确不写进文档。

三组（插入或替换的位置）：
  补拍 A（9 个任务，约 119 秒）：替换剧本第 6 集 01、02 号 ——
      A-01 全城航拍：无人机一样贴着楼顶飞向天边，白线长成白色雾墙（15）→ A-02 烧烤摊：老板和白领发现天变凉、手机没信号（15）→
      A-03 街上人群拼命朝镜头跑，镜头倒退（15）→ A-04 苏清月和文助理在大平层落地窗前看着雾墙一栋楼一栋楼吞掉城市（15）→
      A-05 地铁口：人群涌下台阶，白雾顺着台阶灌下去（12）→ A-06 雾锋扫过街面，车、树、楼全挂上霜（12）→
      A-07 白领靠着结霜的车给妈妈打电话，一句比一句轻（15）→ A-08 拉远：他一动不动，整条街的人保持奔跑姿势成了冰雕（8）→
      A-09 吊臂升起，整座冰封的城市（12）。
  补拍 B（9 个任务，约 109 秒）：替换剧本第 8 集 02、03 号，并在第 8 集 04 号（穿第三件羽绒服）和 06 号（林峰装水泵）之间插入她走出冻城的整段路 ——
      B-01 钢门被砸得发抖（6）→ B-02 暴徒堵在台阶上，苏清月举着点着的酒精瓶回话（15）→ B-03 瓶子砸向台阶（6）→ B-04 火还烧着，她靠着货箱自言自语（10）→
      （剧本第 8 集 04 号：穿第三件羽绒服，原样保留）→
      B-05 她从地下出口爬出来，走过冰雕街，在白领的车旁停下（15，白领的脸是 A-07 的回呼）→ B-06 冰封高速公路上，她扶着冻住的车顶往前走，镜头升起，车队排到天边（15）→
      B-07 过冰河：趴在冰上一寸一寸爬，冰面裂开（15）→ B-08 暴风雪里倒下，自己把自己骂起来（15）→ B-09 暮色里的雪原，山脊上一排冰雕，极光亮起（12）→
      （剧本第 8 集 06 号林峰装水泵、07 号坐标处，原样保留）。
  补拍 C（5 个任务，约 59 秒）：手术前插一条信任戏（C-01）；替换剧本第 10 集 04 号（C-02、C-03）和 06 号（C-04、C-05）。内容同补拍包 1，改成 15 秒写法。

偏离大纲（交稿时告诉 hh）：
  · 降临里不拍“瞬间冻住”的过程，只拍雾锋过去的结果；冻住的人保持奔跑姿势；
  · 白领是我加的路人，为了给“世界末日”一个有脸的人，也为 B-05 苏清月路过时回呼；
  · 酒窖里加了暴徒“阿瘦”（有一句台词）；“跳窗入雪”改成从地下出口爬出来；冰河、高速公路、暴风雪倒下是我补的路程；
  · 手术前的信任戏、“从你买下我房子那天”是我补的（同补拍包 1）。
H3 方面的风险（交稿时单列、不算我的错）：
  · A-01 航拍飞行＋雾墙（大场景）；A-03 人群奔跑（快动作）；A-05 白雾灌下台阶；A-06 霜的蔓延（状态变化）；A-09 整座城市；
  · A-04 落地窗外的雾墙吞掉大楼（窗外画面里套着的画面）；B-02 三人同框；B-03 砸瓶子（快动作）、火焰；
  · B-05 白领是 A-07 的人物，要靠素材保脸；B-06 一眼望不到头的车队；B-07 冰面裂纹的蔓延（慢）；B-08 倒地再爬起来；
  · 画外自言自语时嘴还是会动（本批的自言自语都是低声出声说话，不是内心独白）；C-01…C-03 没有场景参照图；
  · 15 秒任务可能在约 8 秒自己切镜；后几句台词可能挤到片尾；约一成开场图不按文字画。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
from _jihan_base6 import *
import _scene
from _scene import smooth_text, TONE_FIX
import _h3draft as _H

_H.configure(smooth=True, fixed_seed=37407, cap=12, fast=True)   # fast：hh 2026-10-15 要求对白更快、句间更紧、现场音写响   # 2026-10-15：15 秒任务让 sage attention 崩溃，全部压到 12 秒以内
OUT = '补拍/追加版_接在主剧后面_带全剧素材/补拍2_十二秒版_降临全城_苏清月的求生之路_手术信任_制作稿_追加'
S = Session('合并稿/018_第45-46集_十二秒版_制作稿_追加.json', OUT, 61000)
B6.S = S

# ---------------------------------------------------------------------------------------------- 台词排时间（同 018）
GAP = 0.2
BRISK_EN = ' The lines follow one another at once with only a very short breath between them, each said in one breath with no pause inside the sentence.'
BRISK_ZH = ' 台词一句紧接着一句，中间只有很短的换气，每句一口气说完、句中不停顿。'


def times(spec, t0=0.4, gap=None):
    def run(g):
        out, t = [], t0
        for sp, tx, to in spec:
            tx2 = smooth_text(tx)
            out.append((sp, tx2, round(t, 2), to))
            t = t + _H.line_seconds(tx2) + g
        return out
    if gap is not None: return run(gap)
    out = run(GAP)
    if out[-1][2] + _H.line_seconds(out[-1][1]) + 1.1 > 12: out = run(0.1)     # 12 秒放不下：句间收到 0.1 秒
    return out


def smooth15(lines, dur, act_en, zh):
    spec = [(a, b, d) for a, b, c, d in lines]
    new = times(spec)
    need = lambda n: n[-1][2] + _H.line_seconds(n[-1][1]) + 0.05 + 1.0
    if need(new) > dur: new = times(spec, gap=0.1)           # 台词放不下：句间收到 0.1 秒
    if need(new) > dur:
        dur = min(13, int(need(new) + 0.99)); print('  [放宽到 %d 秒] ' % dur, act_en[:50])   # 仍放不下：最多放宽到 13 秒（009 里跑过 13 秒）
    tight = int(new[-1][2] + _H.line_seconds(new[-1][1]) + 1.6 + .99)   # 最后一句说完后留约 1.6 秒收尾动作；对白任务不拖空
    if dur > tight: dur = max(6, tight)
    for a, b in TONE_FIX: act_en = act_en.replace(a, b)
    return new, dur, act_en + BRISK_EN + ' The dialogue is delivered at a fast, snappy pace, about twenty percent quicker than normal speech.', zh + BRISK_ZH + ' 台词语速偏快利落，比平常快两成左右。'


_scene.smooth_task = smooth15


def cam(en, zh):
    return (en, zh)


# ---------------------------------------------------------------------------------------------- 光和空气（本批新增，每个任务一句）
AES_A01 = ("Hard white noon sunlight glints off the glass towers, the heat shimmer over the streets slowly thickens into a drifting haze and the sun above the advancing wall fades to a dim pale disc.",
           "正午刺眼的白色阳光在玻璃大楼上闪着光，街面上的热浪渐渐变成一层飘着的薄雾，逼近的雾墙上方，太阳暗成一个淡白色的圆盘。")
AES_A02 = ("Blinding noon sun makes the grill glow orange while a cold pale shadow slides across the street behind them and the smoke from the coals bends sideways in a sudden chill.",
           "正午刺眼的阳光照得烤架发出橙红色的光，他们身后一片冷冷的灰影滑过街面，炭火的烟被一阵突然的寒风吹得横着飘。")
AES_A03 = ("Hard noon sun glares on the rushing crowd while the towering wall of white mist throws a cold blue shadow forward across the boulevard, and dust, paper and dropped cups swirl in the rising wind.",
           "正午的烈日照着狂奔的人群，高耸的白色雾墙向前投下一大片冷蓝色的影子压过大街，灰尘、纸片和掉落的杯子在越来越大的风里打转。")
AES_A04 = ("The dimming white light of the mist wall floods through the glass and drains the colour from their faces while the penthouse lamps flicker and a cold blue shadow creeps across the white sofa.",
           "雾墙越来越暗的白光涌过玻璃，把两个人脸上的血色一点点抽走，大平层里的灯一闪一闪，一片冷蓝色的影子爬过白色沙发。")
AES_A05 = ("A thick white fog pours down the subway stairs in slow rolling waves lit by the warm yellow stairwell lamps and a rim of frost crackles across the steel handrail.",
           "浓浓的白雾一浪一浪缓缓灌下地铁台阶，被楼梯口温暖的黄灯照亮，钢扶手上一圈白霜噼啪作响地爬过去。")
AES_A06 = ("Pale cold light filters through the boiling mist and glitters on the frost crystals spreading across glass and leaves while thin ribbons of mist curl around the stopped cars.",
           "淡淡的冷光穿过翻滚的白雾，照在爬过玻璃和树叶的霜晶上闪着光，一缕缕细细的雾带绕着停住的车打转。")
AES_A07 = ("Cold pale light drifts through thick mist onto his frost-crusted face, white breath trembles in the air and ice crystals glitter on his lashes.",
           "冷冷的淡光穿过浓雾落在他结满霜的脸上，白色的气息在空气里发着抖，睫毛上的冰晶闪着光。")
AES_A08 = ("A thin pale light glows through the drifting mist across the silent street and the ice-encased runners glitter like glass sculptures.",
           "一线淡淡的光穿过飘着的薄雾，照着寂静的街，被冰裹住的奔跑的人像玻璃雕塑一样闪着光。")
AES_A09 = ("A dim pale sun hangs in a grey-blue sky over the silent city while ice crystals glitter in the still air and the frost-furred glass towers throw soft cold highlights.",
           "一轮暗淡的白色太阳挂在灰蓝色的天空里，照着寂静的城市，静止的空气里冰晶闪着光，挂满霜的玻璃大楼投下柔和的冷色高光。")
AES_B01 = ("Dim yellow bulb light flickers as the steel door shudders, and flakes of frost and dust drift down slowly through the beam.",
           "昏黄的灯泡光一闪一闪，钢门每震一下，霜片和灰尘就从光束里缓缓飘落下来。")
AES_B02 = ("Flickering orange flame light from the burning bottle fights the cold blue night glow from the broken doorway and splits across three tense faces.",
           "燃烧的酒精瓶跳动的橙色火光，和被砸坏的门口透进来的冷蓝色夜光交锋，把三张紧绷的脸切成两半。")
AES_B03 = ("A roaring orange flare lights the whole cellar and throws long dancing shadows across the frost-furred bottles.",
           "轰然腾起的橙色火光照亮整个酒窖，在挂满霜的酒瓶上投下长长的、跳动的影子。")
AES_B04 = ("Orange firelight pulses on the steps and glitters in the frost on the walls while thin streams of snow blow in through the doorway and melt in the heat.",
           "橙色的火光一明一暗地照着台阶，在墙上的霜里闪光，细细的雪从门口吹进来，在热气里化掉。")
AES_B05 = ("Dim blue-grey light filters through the drifting mist onto the frozen street, the ice-encased figures glitter like glass and her white breath hangs in the air.",
           "昏暗的蓝灰色光穿过飘着的薄雾落在冰封的街上，被冰裹住的人形像玻璃一样闪着光，她呼出的白气停在空气里。")
AES_B06 = ("A cold blue storm light rakes across the ice-encased cars and glitters in the blowing snow while her long shadow stretches thin along the road.",
           "冷蓝色的风暴光扫过被冰包住的汽车，在吹着的雪里闪着光，她细细长长的影子被拉在路面上。")
AES_B07 = ("Pale blue dusk light glints off the black ice and tiny ice crystals spark in the air as a hairline crack creeps across the surface.",
           "淡蓝色的暮光在黑色的冰面上闪着，一条发丝一样的裂纹慢慢爬过冰面，空气里细小的冰晶一闪一闪。")
AES_B08 = ("A roaring white blizzard glows with grey-blue light, fine snow lashes across her face and her breath streams away in the wind.",
           "咆哮的白色暴风雪发着灰蓝色的光，细雪抽打在她脸上，她呼出的白气被风扯着飘走。")
AES_B09 = ("A first faint green aurora ripples across a deepening blue dusk and its light glitters on the snow while the tiny traveler casts a long blue shadow.",
           "第一缕淡淡的绿色极光在渐深的蓝色暮色里流动，光洒在雪面上闪着光，那个小小的行路人拖着一条长长的蓝色影子。")
AES_C01 = ("Hard white surgical light falls on the blue drape and the bright steel while a cool shadow sits on both faces and a thin curl of steam rises from a mug on the shelf.",
           "手术灯的白光硬朗地落在蓝色的无菌布和亮闪闪的钢器上，两个人脸上是一层冷冷的影子，架子上杯子里升起一缕细细的热气。")
AES_C02 = ("The round surgical lamp throws a soft white halo over the neat stitches and the white gauze while fine dust floats in the beam and the tension drains from both faces.",
           "圆形的手术灯在整齐的缝线和白纱布上投下一圈柔和的白光，细细的灰尘在光束里飘，两个人脸上的紧绷慢慢松下来。")
AES_C03 = ("Warm lamp light catches the edge of the folded paper and the faint curve at the corner of his mouth while her gloved fingers draw the paper slowly across the blue drape.",
           "暖暖的灯光落在折好的纸的边缘，也落在他嘴角那一丝弧度上，她戴着手套的手指把纸慢慢拉过蓝布。")
AES_C04 = ("A thin line of pink-violet light glows around the edges of the steel door and paints a soft rim on both profiles, and a faint warm breeze lifts a few strands of her hair.",
           "钢门边缘一线粉紫色的光，在两个人的侧脸上勾出一圈柔和的光边，一阵淡淡的暖风吹起她几缕头发。")
AES_C05 = ("Warm pink-violet light pours out of the doorway across the concrete in a golden-violet flood, dust motes and glittering mist drift in the beam and a rim of warm light edges the doorway.",
           "暖暖的粉紫色的光从门里涌出来，铺在混凝土地面上，像一片金紫色的潮水，光束里飘着尘埃和闪光的水雾，门框被一圈暖光勾出轮廓。")

# ---------------------------------------------------------------------------------------------- 声音
SOUND_HUSH = breathy('A dead hush, a thin wind and the faint tick of ice forming.', '一片死寂，细细的风声和冰层形成时轻轻的嘀嗒声。')
SOUND_PHONE = voiced('A rising low howl of wind, his shaky breath and the faint ticking of frost forming on cloth.', '渐渐变大的低沉风声、他发抖的呼吸声和衣料上结霜时轻轻的嘀嗒声。')
SOUND_CITY2 = breathy('The bright din of a busy downtown at noon, a rising low howl of wind and a deep faint rumble from the horizon.', '中午市中心热闹的嘈杂、渐渐变大的低沉风声和地平线上深沉的隆隆声。')
SOUND_STALL = voiced('The sizzle of the grill, cicadas droning in the heat, then a rising cold wind and the rattle of loose signs.', '烤架的滋滋声、热浪里的知了叫，然后是越来越冷的风声和招牌的哗啦声。')
SOUND_STAMPEDE = breathy('Pounding footsteps, blaring car horns, screams and a rising roar of wind.', '密集的奔跑脚步声、汽车刺耳的喇叭声、尖叫声和越来越响的风吼。')
SOUND_PENT = voiced('The faint hum of air conditioning cutting out, a rising far howl of wind against the glass and the flicker of lamps.', '空调轻轻的嗡鸣断掉、远处越来越响的风吼拍在玻璃上，还有灯光闪烁的细响。')
SOUND_SUBWAY = breathy('Screams echoing in a stairwell, hurried footsteps and the long hiss of fog pouring down stairs.', '楼梯口回荡的尖叫声、急促的脚步声和白雾灌下台阶长长的嘶嘶声。')
SOUND_FRONT = breathy('A long rising howl of wind, the crackle of ice creeping over glass and the creak of freezing branches.', '风长长地越来越响的呼啸、冰爬过玻璃时的噼啪声和树枝冻住时的嘎吱声。')
SOUND_CELLAR2 = breathy('Heavy hammer blows booming on steel, rattling bottles and a low wind whistling through the door seam.', '钢门上沉重的锤击闷响、酒瓶的震动和风从门缝里钻进来的低低呼啸。')
SOUND_FLAME = breathy('A roaring whoosh of flame, shattering glass and the howl of wind through the doorway.', '火焰轰然腾起的声音、玻璃碎裂的声音和风从门口灌进来的呼啸。')
SOUND_TRUDGE = voiced('The crunch of boots in frozen snow, a long low wind and her ragged breathing.', '靴子踩在冻硬的雪上的嘎吱声、风长长的低吼和她粗重的呼吸。')
SOUND_ICE = voiced('A deep groan of ice shifting under weight, the faint tick of a crack spreading and her shuddering breath.', '冰面承重时深沉的呻吟声、裂纹蔓延时细细的嘀嗒声和她发抖的呼吸。')
SOUND_WHITEOUT = voiced('A roaring blizzard, lashing snow and her gasping breath.', '咆哮的暴风雪、抽打的雪粒声和她喘不上气的呼吸。')
SOUND_DUSK = breathy('A long low wind over open snow and the faint crunch of distant footsteps.', '风掠过空旷雪地长长的低啸和远处细细的脚步声。')
SOUND_MED2 = voiced('The faint electric hum of the surgical lamp, a tick of cooling metal and slow breathing.', '手术灯细细的电流嗡鸣、金属冷却时的嘀嗒声和缓慢的呼吸。')
SOUND_DOOR2 = voiced('A low hum from beyond the steel door and soft footsteps on concrete.', '钢门后低低的嗡鸣和混凝土地面上轻轻的脚步声。')
SOUND_EDENLIGHT = breathy('A soft rising hum from beyond the doorway and a hush of awe.', '门后轻轻升起的嗡鸣和敬畏的寂静。')

# ---------------------------------------------------------------------------------------------- 场景
CITY_NOON = Scene('city_noon', " Blinding white noon sun glares over the glass towers of a crowded downtown with a pale line of haze on the far horizon.",
                  " Fixed stage layout: an aerial view just above the rooftops of a dense downtown of glass towers fills the lower two thirds of the frame, the streets packed with slow cars and tiny crowds; a hazy line of heat shimmer lies along the far horizon in the middle of the frame under a clear white-blue sky.")
STALL = Scene('street_summer', " Blinding white midday sun glares over the glass towers and the lunchtime street.",
              " Fixed stage layout: a sidewalk barbecue stall with a smoking charcoal grill and rows of skewers stands in the foreground at frame-left; the wide boulevard recedes down the middle of the frame between glass office towers with slow cars and lunchtime crowds on the sidewalks; leafy trees line the street; at the far end of the street a low white wall of mist rises on the horizon.")
STREET_RUN = Scene('street_summer', " Blinding white midday sun glares over the glass towers while a towering wall of white mist fills the sky at the far end of the street.",
                   " Fixed stage layout: the wide boulevard between glass office towers recedes down the middle of the frame; a dense tide of office workers, delivery riders and shoppers fills the street and the sidewalks running toward the foreground; stopped cars stand among them; at the far end of the street a towering wall of white mist fills the sky.")
PENT_FOG = Scene('penthouse', " Cool air-conditioned light fills the luxury penthouse while the white light outside the windows dims.",
                 " Fixed stage layout: the floor-to-ceiling windows across the back wall fill the middle of the frame and show a vast white wall of mist swallowing the glass towers of the city one after another under a dimming sun; the glass dining table stands at frame-right; the white sectional sofa stands against the left wall; nobody else is in the room.")
SUBWAY = Scene('subway_gate', " Warm yellow lamp light fills the stairwell of a busy subway entrance while white fog begins to spill over the street above.",
               " Fixed stage layout: the mouth of a subway entrance with a steel handrail and a flight of wide concrete stairs descending into warm yellow light fills the middle of the frame; a panicked crowd of commuters pours down the stairs toward the camera; a white wall of mist rolls over the glass-towered street behind the entrance at the top of the frame.")
STREET_FRONT = Scene('street_summer', " Blinding white sun glares on the near half of the boulevard while a boiling white front of mist crosses the street behind it.",
                     " Fixed stage layout: the wide boulevard recedes down the middle of the frame; the near half of the street still has green leafy trees and sunlit stopped cars; a boiling white front of mist stands across the middle of the street; everything beyond the front is furred white with frost, dim and grey-blue; nobody is in the street.")
SIDEWALK_FROST = Scene('street_frozen', " Dim grey-blue light and thick white mist drift at street level over the silent boulevard.",
                       " Fixed stage layout: the boulevard recedes down the middle of the frame in thick drifting mist; the parked cars along the curb are furred white with fresh frost; frost-stiffened trees line the sidewalk; a silver sedan stands at the curb at frame-center with a man sitting against its door; the glass towers are furred with frost.")
FROZEN_WIDE = Scene('city_frozen', " A dim pale sun hangs in a grey-blue sky over a silent frozen downtown.",
                    " Fixed stage layout: a high aerial view of the same downtown fills the lower two thirds of the frame; the glass towers are furred with ice, the streets are jammed with ice-encased cars and the crowds stand frozen mid-run in white ice; a thin mist drifts along the avenues; the sky above is grey-blue with a dim pale sun.")
STREET_FROZEN_RUN = Scene('street_frozen', " Dim grey-blue light and a thin white mist hang over the silent frozen boulevard.",
                          " Fixed stage layout: the wide boulevard recedes down the middle of the frame; the cars are encased in ice; bare frost-furred trees line the sidewalks; people stand frozen mid-run in white ice along both sidewalks and in the middle of the street, their arms still swinging; the glass towers are furred with frost.")
HWY2 = Scene('ice_highway', " A cold blue storm light rakes over a wide frozen highway in a thin blowing snow.",
             " Fixed stage layout: a wide highway runs away from the camera down the middle of the frame, jammed with ice-encased cars that stand bumper to bumper and are buried to the windows in drifted snow; snow-covered guardrails line both sides; a low grey-blue sky fills the top of the frame.")
RIVER = Scene('frozen_river', " Pale blue dusk light lies over a wide frozen river under a low grey sky.",
              " Fixed stage layout: a very wide frozen river fills the frame from left to right, its surface black ice with white drifts of snow; a bank of snow-laden reeds and bare trees stands at the far side of the frame; a long hairline crack runs across the ice in the middle of the frame ahead; blowing snow streams low across the ice.")
WHITEOUT = Scene('snow_trek', " A roaring white blizzard fills a vast frozen snowfield and glows with grey-blue light.",
                 " Fixed stage layout: a vast open snowfield fills the frame but is almost swallowed by a roaring white blizzard that streams across it in sheets; the ground is a deep drift of snow; a single dark leafless frozen tree stands far away at frame-right, half hidden in the white.")
DUSK_RIDGE = Scene('snow_trek', " A deep blue dusk with a first faint green aurora over a vast frozen snowfield.",
                   " Fixed stage layout: a vast open snowfield fills the middle of the frame under a deep blue dusk sky; far at the back a line of white ice-encased human figures frozen mid-run stands along a low ridge; a first faint curtain of green aurora hangs above the ridge; a tiny lone traveler in layered down jackets with a heavy backpack walks across the snow in the middle third of the frame.")

# ================================================================================================ 补拍 A
bA = S.episode('补拍A｜降临全城（替换剧本第6集01、02号镜头）',
               '中午的城市热闹得和往常一样，无人机一样的镜头贴着楼顶飞向天边，白线长成撑满天空的雾墙；烧烤摊老板和白领发现天凉了、手机没信号；人群拼命朝镜头奔跑；苏清月和文助理在大平层的落地窗前看着雾墙把城市一栋楼一栋楼吞掉；地铁口的人群涌下台阶，白雾灌下去；雾锋扫过街面，车、树、楼全挂满霜；白领靠着车给妈妈打电话，一句比一句轻，然后一动不动；镜头拉远，整条街的人保持着奔跑的姿势成了冰雕；吊臂升起，整座城市冻成一片灰蓝色。', 1)

new_person(bA, 'bbq_vendor', '烧烤摊老板（敦实的中年男人，汗湿的白背心，油腻围裙，肩上搭毛巾）', 'man',
           'A stocky Chinese man in his forties with a round sweaty face and small bright eyes, wearing a sweat-stained white tank top and a greasy apron with a towel over one shoulder.',
           '一个四十多岁、敦实的中国男性，圆脸出着汗，眼睛小而亮，穿着被汗浸湿的白色背心和油腻的围裙，肩上搭着一条毛巾。',
           'a round sweaty face, small bright eyes, wearing a sweat-stained white tank top and a greasy apron with a towel over one shoulder', 'a hearty, easy expression', eth='Chinese')
new_person(bA, 'office_guy', '白领（三十多岁，卷袖子的白衬衫，松开的领带，挂着工牌）', 'man',
           'A Chinese office worker in his thirties with neat short black hair and a tired friendly face, wearing a white dress shirt with rolled sleeves, a loosened tie and a lanyard around his neck.',
           '一个三十多岁的中国上班族，黑短发整齐，脸上带着疲惫而和气的神情，穿着卷起袖子的白衬衫，领带松开，脖子上挂着工牌。',
           'neat short black hair, a tired friendly face, wearing a white dress shirt with rolled sleeves, a loosened tie and a lanyard around his neck', 'a relaxed, tired expression', eth='Chinese')
new_person(bA, 'raider_lean', '暴徒阿瘦（精瘦的年轻男人，破迷彩外套，脏围巾遮着口鼻，拿撬棍）', 'man',
           'A wiry Chinese man in his twenties with a gaunt hollow-cheeked face and bloodshot jittery eyes, wearing a torn camouflage jacket with a dirty scarf pulled up over his mouth and nose, holding a steel crowbar.',
           '一个二十多岁、精瘦的中国男性，脸颊凹陷，眼睛布满血丝、神经质地乱转，穿着破旧的迷彩外套，脏围巾拉起来遮住口鼻，手里拿着一根钢撬棍。',
           'a gaunt hollow-cheeked face, bloodshot jittery eyes, wearing a torn camouflage jacket with a dirty scarf pulled up over his mouth and nose', 'a jittery, mean expression', eth='Chinese')
bA.character('Vendor', 'bbq_vendor', VENDOR_EN, VENDOR_ZH)
bA.character('Clerk', 'office_guy', CLERK_EN, CLERK_ZH)
bA.character('Lean', 'raider_lean', LEAN_EN, LEAN_ZH)
new_scene(bA, 'city_noon', '正午的市中心航拍（贴着楼顶，玻璃大楼密密麻麻，街上车和人群，天边一线淡淡的热浪白线）',
          'A low aerial view just above the rooftops of a dense downtown of glass towers under a blazing noon sun, the streets packed with slow cars and tiny crowds and a pale line of haze along the far horizon.',
          '贴着楼顶的低空航拍，正午烈日下密密麻麻的玻璃大楼，街上挤满缓缓挪动的车和小小的人群，天边有一线淡淡的白色热浪。',
          'the glass towers, the crowded streets and the pale line of haze on the horizon')
new_scene(bA, 'subway_gate', '地铁口（宽宽的水泥台阶通向暖黄色的灯光，钢扶手，台阶上方是玻璃大楼的街）',
          'The mouth of a busy subway entrance with a steel handrail and a flight of wide concrete stairs descending into warm yellow lamp light, the glass-towered street above it.',
          '热闹的地铁出入口，一道宽宽的水泥台阶带着钢扶手通向暖黄色的灯光，上方是玻璃大楼的街。',
          'the steel handrail, the concrete stairs and the warm yellow light')
new_scene(bA, 'frozen_river', '冻住的宽阔河面（黑色的冰面上积着白色的雪堆，对岸一排挂雪的芦苇和光秃秃的树，冰面中间一条细长的裂纹，低低吹过冰面的雪）',
          'A very wide frozen river with a surface of black ice and white drifts of snow, a bank of snow-laden reeds and bare trees on the far side and a long hairline crack across the ice in the middle, blowing snow streaming low across it.',
          '一条非常宽的冰封河面，黑色的冰面上积着白色的雪堆，对岸是一排挂着雪的芦苇和光秃秃的树，冰面中间有一条细长的裂纹，低低的吹雪贴着冰面飘过去。',
          'the black ice, the long crack and the snow-laden reeds on the far bank')
new_scene(bA, 'city_frozen', '冻住的市中心高空俯瞰（玻璃大楼挂满冰，街上全是冰封的车和冻成冰雕的人群，灰蓝色天空里一轮暗淡的白太阳）',
          'A high aerial view of a frozen downtown: glass towers furred with ice, streets jammed with ice-encased cars and crowds frozen mid-run in white ice, a grey-blue sky with a dim pale sun.',
          '冻住的市中心高空俯瞰：玻璃大楼挂满冰，街上全是被冰裹住的车和保持奔跑姿势冻成冰雕的人群，灰蓝色天空里一轮暗淡的白太阳。',
          'the ice-furred towers, the ice-encased streets and the frozen crowds')

insert2('A-01', '01｜全城航拍：无人机一样的镜头贴着楼顶飞向天边，白线越长越高，长成撑满天空的雾墙，太阳暗成一个白盘子', 15, CITY_NOON,
        'Extreme wide aerial shot just above the rooftops, the downtown and the far horizon in the middle third of the frame; no named person.',
        "The camera glides forward over the glittering rooftops of a blazing noon downtown where tiny crowds stream along the streets and cars crawl bumper to bumper, while the pale line on the horizon swells into a towering wall of white mist that climbs the whole sky and swallows the far towers one by one, the sun above it dimming to a pale white disc and the shadows of the towers stretching long across the streets. Nothing else changes.",
        "镜头贴着正午市中心闪着光的楼顶向前飞，街上小小的人群流动，车一辆挨一辆地挪，天边那条淡淡的白线越长越高，长成撑满整个天空的白色雾墙，把远处的大楼一栋接一栋吞进去，雾墙上方的太阳暗成一个淡白色的圆盘，大楼的影子在街上越拉越长。别的什么都不变。",
        SOUND_CITY2, 'The frame holds the glass towers, the crowded streets and the growing white wall of mist on the horizon, and nobody named.',
        cam('The camera glides forward over the rooftops at drone height until the towering white wall fills the middle third of the frame.', '镜头像无人机一样贴着楼顶向前飞，直到高耸的白色雾墙占满画面中间三分之一。'),
        AES_A01, extra_assets=('street_summer',))

TA('A-02', '02｜街边烧烤摊：老板和白领发现天边发白、天突然变凉，手机还没了信号', 15, STALL,
   [P('bbq_vendor', 'left', "standing behind the smoking grill in profile facing frame-right, a skewer of meat in his right hand and the towel over his shoulder, his chin lifted toward the far end of the street", 'obj:the low white wall of mist at the far end of the street', "his brows knitting, his mouth hanging a little open"),
    P('office_guy', 'center-right', "standing in front of the stall in profile facing frame-left with a plastic bag of skewers in one hand and an iced coffee in the other, his head turned toward the far end of the street", 'obj:the low white wall of mist at the far end of the street', "his lips parting, his brows drawn together")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the barbecue stall.',
   "<bbq_vendor> turns a skewer over the coals with a puzzled frown and speaks the first line to <office_guy> in a loud, puzzled voice, his brows knitting; <office_guy> lowers his iced coffee and answers with the second line to <bbq_vendor> in a small, uneasy voice, his lips parting; <bbq_vendor> rubs his bare arm and speaks the third line to <office_guy> in a lower, spooked voice, his mouth hanging a little open; <office_guy> pulls out his phone, frowns at it and speaks the last line to <bbq_vendor> in a thin, shaky voice, his brows drawn together; after the last line the smoke from the grill bends flat sideways in a cold gust while the iced coffee in his hand clouds over with frost.",
   "烧烤摊老板一边纳闷地皱着眉翻着炭火上的肉串，一边用洪亮又纳闷的声音对白领说出第一句，眉头拧起；白领放下冰咖啡，用很小、发毛的声音对老板答出第二句，嘴唇微张；老板搓着光胳膊，用更低、有点发毛的声音对白领说出第三句，嘴巴微微张着；白领掏出手机，皱着眉看着屏幕，用发颤的细声对老板说出最后一句，眉头拧在一起；最后一句之后，烤架的烟被一阵冷风吹得横着飘，他手里的冰咖啡杯上蒙起一层白霜。",
   SOUND_STALL, AES_A02,
   lines=[('bbq_vendor', "哎，那边怎么白了？", 0.8, 'Office'), ('office_guy', "是雾吗？大中午的。", 0.8, 'Bbq'), ('bbq_vendor', "怎么一下子凉了？", 0.8, 'Office'), ('office_guy', "手机，没信号了！", 0.8, 'Bbq')],
   cam=slide('to the right', '右', 'both men stand in the middle third of the frame with the thin white haze of the far horizon visible behind them', '两个人站在画面中间三分之一，身后能看到远处地平线上那一线淡淡的白雾'),
   room={'Bbq', 'Office'}, new=True,
   bg='Behind them the sidewalk crowd and the boulevard are sharp and clearly visible, and a low white wall of mist rises at the far end of the street.',
   holds='The frame holds exactly two people: Bbq and Office, at the barbecue stall, with the sharp crowd and the boulevard behind them.')

insert2('A-03', '03｜大街：人群丢下东西拼命朝镜头跑，车喇叭乱响，雾墙在他们身后越逼越近', 15, STREET_RUN,
        'Wide low shot at street level, the boulevard in the middle third of the frame; no named person.',
        "A dense crowd of office workers, delivery riders and shoppers breaks into a sprint down the middle of the boulevard straight toward the camera, dropping bags, cups and phones, their mouths open; drivers climb out of the stopped cars and run too while horns blare, and behind them the towering wall of white mist advances steadily down the street, swallowing the far crosswalk and the first line of parked cars at its foot.",
        "一大群上班族、外卖骑手和购物的人在大街中间朝镜头拼命跑，丢下手里的包、杯子和手机，嘴巴张着；停着的车里司机也爬出来跟着跑，喇叭声乱响，高耸的白色雾墙在他们身后沿着大街稳稳地逼近，吞掉了远处的斑马线和脚下的第一排车。",
        SOUND_STAMPEDE, 'The frame holds the boulevard with the running crowd in the foreground, the stopped cars and the white wall of mist at the far end, and nobody named.',
        cam('The camera retreats backward along the boulevard ahead of the running crowd until the whole street fills the frame.', '镜头在奔跑的人群前面向后退，直到整条大街占满画面。'),
        AES_A03, extra_assets=())

TA('A-04', '04｜大平层：苏清月和文助理站在落地窗前，眼看着白色雾墙把城市一栋楼一栋楼吞掉，苏清月从不信到发白', 15, PENT_FOG,
   [P('wen_blazer', 'left', "standing at the window in profile facing frame-right, one hand clutching a tablet to her chest, her eyes on the white wall of mist beyond the glass", 'obj:the white wall of mist swallowing the towers beyond the window', "her lips parting, her brows pulled together"),
    P('su_suit', 'center-right', "standing at the window in profile facing frame-left, her fingertips pressed flat to the glass, her glasses catching the white glow", 'obj:the white wall of mist swallowing the towers beyond the window', "her lips pressed into a thin line, her brows low and tight")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the penthouse window.',
   "<wen_blazer> speaks the first line to <su_suit> in a small, frightened voice, her lips parting; <su_suit> keeps her eyes on the glass and answers with the second line to <wen_blazer> in a low, tight voice, her lips pressed into a thin line and her brows low; <wen_blazer> turns her head to <su_suit> and speaks the third line in a shaking voice, her brows pulled together; <su_suit> turns her head to <wen_blazer> and speaks the last line in a cold, hard voice, her brows low; after the last line the penthouse lamps flicker and go dark and she turns from the window.",
   "文助理用很小、害怕的声音对苏清月说出第一句，嘴唇微张；苏清月眼睛盯着玻璃，用低沉紧绷的声音对文助理答出第二句，嘴唇抿成一条细线、眉头压低；文助理转头看着苏清月，用发抖的声音说出第三句，眉头拧在一起；苏清月转头看着文助理，用冷硬的声音说出最后一句，眉头压低；最后一句之后，大平层里的灯闪了闪，灭了，她从窗边转过身。",
   SOUND_PENT, AES_A04,
   lines=[('wen_blazer', "苏总，外面全白了！", 0.8, 'Su'), ('su_suit', "他说的，是真的。", 0.8, 'Wen'), ('wen_blazer', "那我们怎么办？", 0.8, 'Su'), ('su_suit', "去酒窖。现在。", 0.8, 'Wen')],
   cam=push('both of them', '两人'), room={'Wen', 'Su'}, new=True,
   bg='Beyond the floor-to-ceiling glass behind them a vast white wall of mist swallows the glass towers of the city one after another under a dimming sun.',
   holds='The frame holds exactly two people: Wen and Su, at the penthouse window, with the white wall of mist beyond the glass.')

insert2('A-05', '05｜地铁口：人群挤着涌下台阶，白雾顺着台阶一浪一浪灌下去，钢扶手上一圈白霜爬过去', 12, SUBWAY,
        'Wide shot of the subway entrance, the flight of stairs in the middle third of the frame; no named person.',
        "A panicked crowd of commuters pours down the wide concrete stairs of the subway entrance toward the camera, clutching bags and each other, while above them a thick white fog spills over the top of the stairwell and rolls down the steps in slow waves behind the last runners, and a rim of white frost creeps along the steel handrail and over the concrete edges of the steps.",
        "一大群上班族慌乱地涌下地铁口宽宽的水泥台阶，朝镜头挤过来，抱着包，互相拉扯着，他们头顶上，浓浓的白雾从楼梯口顶上漫出来，一浪一浪缓缓顺着台阶往下滚，跟在最后几个人身后，钢扶手上和台阶的水泥边沿上，一圈白霜慢慢爬过去。",
        SOUND_SUBWAY, 'The frame holds the subway stairs with the fleeing crowd, the warm yellow light below and the white fog spilling over the top, and nobody named.',
        tilt('the white fog rolling down the stairwell', '顺着楼梯口滚下来的白雾'), AES_A05, extra_assets=())

insert2('A-06', '06｜雾锋慢慢扫过街面，被扫过的车、树、大楼全挂上了白霜，雾锋前面的还是绿的、还晒着太阳', 12, STREET_FRONT,
        'Wide shot at street level, the boulevard in the middle third of the frame, the front of the mist crossing the street; nobody in the scene.',
        "The boiling white front of the mist moves slowly across the street over the stopped cars, and everything it has passed lies furred white with frost: the windshields turn milky, the leaves of the trees stiffen white, and a layer of ice climbs the glass of the towers with a crackle, while the cars and trees in front of it are still green and sunlit. Nothing else moves.",
        "翻滚的白色雾锋慢慢扫过街面上停着的车，被它扫过的东西全挂上了白霜：挡风玻璃一片乳白，行道树的叶子又硬又白，大楼的玻璃上带着噼啪声爬满了冰，雾锋前面的车和树还是绿的、还晒着太阳。别的什么都不动。",
        SOUND_FRONT, 'The frame holds the boulevard with the sunlit green half in the foreground, the boiling white front of the mist across the middle of the street and the frosted half beyond it, and nobody in the scene.',
        push1('the edge of the mist', '雾锋的边缘'), AES_A06)

TA('A-07', '07｜同一条大街：雾刚漫过，白领靠着结霜的车坐在路边，举着手机一句比一句轻地叫妈，最后手垂下来', 15, SIDEWALK_FROST,
   [P('office_guy', 'center', "sitting on the curb with his back against the door of a frost-white silver sedan in profile facing frame-right, holding his phone to his ear in his right hand, his other arm wrapped around his knees, white breath pouring from his mouth and frost forming on his lashes and brows", 'obj:the phone screen in his hand', "his lips trembling, his brows pulled high, his eyes wet")],
   'Medium shot, the figure from the head to the knees, in the middle third of the frame, on the frosted boulevard.',
   "<office_guy> shivers against the car door and murmurs each line to himself into the phone in a cracked, trembling voice, talking to nobody in the frame, his lips trembling and his brows pulled high; the lines come slower and smaller, each one softer than the last, white breath thinning, tears freezing on his lashes; after the last line his eyes slowly close, his hand sinks to his lap with the phone and his head rests back against the door. Nobody else is in the frame.",
   "白领缩在车门边发抖，对着手机用破裂发颤的声音说话，不是对画面里的任何人说的，嘴唇发抖、眉毛高高皱起；一句比一句慢、一句比一句小，白气越来越淡，眼泪冻在睫毛上；最后一句之后，他的眼睛慢慢闭上，拿着手机的手落到膝盖上，头靠在车门上。画面里没有别人。",
   SOUND_PHONE, AES_A07,
   vo=times([('office_guy', "喂？妈？", 'Office'), ('office_guy', "你听得到吗？", 'Office'), ('office_guy', "我好冷，妈。", 'Office'), ('office_guy', "我想回家了。", 'Office')], t0=0.8),
   cam=slide('to the left', '左', 'he sits in the middle third of the frame with the frost-white boulevard behind him', '他坐在画面中间三分之一，身后是白霜覆盖的大街'),
   room={'Office'}, new=True,
   bg='Behind him the boulevard is lost in thick drifting mist, and the frost-white cars line the curb.',
   holds='The frame holds Office alone sitting against the frost-white sedan, the curb and the misty boulevard.')

S.T('A-08', '08｜插镜：白领的脸已经不动了，镜头拉远，他小小的一个人靠在车门边，整条街的人保持着奔跑的姿势成了冰雕', 8, SIDEWALK_FROST,
    [P('office_guy', 'center', "sitting on the curb with his back against the door of the frost-white sedan in profile facing frame-right, his phone slipped into his lap, his head resting back against the door", 'closed', "his face still and calm, a layer of white frost over his lashes, brows and hair", shut='gently closed')],
    'Extreme close-up of his face in the middle third of the frame, on the frosted boulevard.',
    "<office_guy> sits perfectly still against the car door, his eyes gently closed and his face calm under a layer of white frost, his breath no longer clouding. Nobody else is in the frame. The camera pulls back, revealing along the whole boulevard behind him people frozen mid-run in white ice with their arms still swinging.",
    "白领一动不动地靠在车门上，眼睛轻轻闭着，脸被一层白霜盖着、平静，嘴里不再冒白气。画面里没有别人。镜头拉远，他身后整条大街上，人们保持着奔跑、手臂还在摆的姿势被冻在白色的冰里。",
    SOUND_HUSH,
    cam=pull('his frost-covered face', '他结满白霜的脸', 'the whole frozen boulevard with the sedan, the small figure sitting at its door and the runners frozen in ice behind him', '整条冰封的大街，靠在车门边的那个小小的身影，和他身后冻成冰的奔跑的人'),
    bg='The frost-white sedan door is behind his head.',
    holds='The frame holds Office alone, his frost-covered face, and the frost-white car door.', room={'Office'}, new=True)

insert2('A-09', '09｜吊臂升起：整座城市彻底冻住了，大楼挂满冰，街上全是冰封的车和冰雕一样的人群，一轮暗淡的白太阳挂在灰蓝色的天空里', 12, FROZEN_WIDE,
        'Extreme wide high aerial shot, the frozen downtown in the middle third of the frame; no living person.',
        "The same downtown lies silent under a grey-blue sky: the glass towers are furred with ice, the avenues are jammed with ice-encased cars and the crowds stand frozen mid-run in white ice along every street, a thin mist drifts between the towers and a dim pale sun hangs low over the skyline. Nothing moves.",
        "同一座市中心，静静地躺在灰蓝色的天空下：玻璃大楼挂满了冰，大街上挤满被冰裹住的车，每一条街上的人群都保持着奔跑的姿势冻在白色的冰里，一层薄雾在大楼之间飘，一轮暗淡的白太阳低低地挂在楼群上方。什么都不动。",
        SOUND_HUSH, 'The frame holds the frozen downtown with the ice-furred towers, the ice-encased streets and the frozen crowds, and no living person.',
        rise('the whole frozen downtown under the dim pale sun', '暗淡白太阳下整座冰封的市中心'), AES_A09, extra_assets=('street_frozen',))

# ================================================================================================ 补拍 B
bB = S.episode('补拍B｜苏清月的求生之路（替换剧本第8集02、03号；并在第8集04号和06号之间插入她走出冻城的整段路）',
               '钢门被锤得发抖；门被砸开，两个暴徒堵在台阶上，苏清月举着点着的酒精瓶对着他们；瓶子砸向台阶，火焰腾起，两人被逼出门；她靠着货箱，手在抖，低声给自己打气；（穿第三件羽绒服）她从地下出口爬出来，走过冰雕一样的街，在白领靠着的车旁停下；她踩着冻住的车流走上高速公路；趴在冰河上一寸一寸往前爬，冰面裂开；在暴风雪里倒下，又自己把自己骂起来；暮色里的雪原，山脊上一排冰雕，极光亮起。', 2)

insert2('B-01', '01｜插镜：钢门被锤子一下一下砸得发抖，门上的霜簌簌往下掉', 6, CELLAR,
        'Wide shot from the foot of the steps, the three concrete steps and the heavy steel door in the middle third of the frame; nobody in the scene.',
        "Heavy hammer blows boom against the steel door at the top of the steps; with every blow the door shudders in its frame, flakes of frost and dust shake loose and drift down over the steps, and the wine bottles on the racks tremble. Nothing else moves.",
        "沉重的锤子一下一下砸在台阶顶上的钢门上，每砸一下，门在门框里震一震，霜片和灰尘簌簌地抖落下来、飘在台阶上，酒架上的酒瓶也跟着发颤。别的什么都不动。",
        SOUND_CELLAR2, 'The frame holds the three concrete steps, the heavy steel door and the frost-furred wine racks, and nobody in the scene.',
        push1('the shuddering steel door', '发抖的钢门'), AES_B01)

TA('B-02', '02｜酒窖：门被砸开，两个暴徒堵在台阶上喊话，苏清月举着点着的酒精瓶，一句句顶回去', 15, CELLAR,
   [P('su_down', 'left', "standing in the cellar in profile facing frame-right between the stacked cases, a bottle of burning alcohol held low at her hip in her right hand with a small flame guttering from its neck", 'Brute', "her eyes narrowed, her lips pressed in a thin hard line, her brows low"),
    P('brute_raider', 'center', "standing on the second concrete step in profile facing frame-left, the sledgehammer raised in both hands", 'Su', "his eyes wild, his lips curled under his scarf, his brows lowered"),
    P('raider_lean', 'right', "standing on the top step in the shattered doorway behind him in profile facing frame-left, a steel crowbar held across his chest", 'Brute', "his eyes jittery, a mean grin under his scarf, his brows raised")],
   'Medium-wide shot, all three from the head to the knees, in the middle third of the frame, in the frozen wine cellar.',
   "<brute_raider> raises the hammer and speaks the first line to <su_down> in a savage, hoarse roar, his eyes wild; <su_down> lifts the burning bottle slowly to her shoulder and answers with the second line to <brute_raider> in a low voice that shakes at first and hardens as she speaks, her eyes narrowed and her lips pressed in a thin hard line; <raider_lean> grins behind the scarf and speaks the third line to <brute_raider> in a shrill, mocking voice, his eyes jittery; <su_down> takes one slow step toward the steps and speaks the last line to <brute_raider> in a cold, steady voice, her brows low; after the last line the flame on the bottle flares higher and <brute_raider> flinches half a step back.",
   "壮实的暴徒举起大锤，用凶狠嘶哑的吼声对苏清月说出第一句，眼睛发狂；苏清月把点着的酒精瓶慢慢举到肩头，用一开始发颤、说着说着变硬的低沉声音对暴徒答出第二句，眼睛眯起、嘴唇抿成一条硬硬的细线；阿瘦在围巾后面咧着嘴笑，用尖利嘲弄的声音对暴徒说出第三句，眼神乱转；苏清月朝台阶慢慢迈了一步，用冰冷平稳的声音对暴徒说出最后一句，眉头压低；最后一句之后，瓶口的火苗猛地蹿高，暴徒往后缩了半步。",
   SOUND_CELLAR2, AES_B02,
   lines=[('brute_raider', "出来！吃的，全交出来！", 0.8, 'Su'), ('su_down', "再进一步，我烧死你。", 0.8, 'Brute'), ('raider_lean', "大哥，她手在抖！", 0.8, 'Brute'), ('su_down', "那你试试。", 0.8, 'Brute')],
   cam=push('all three of them', '三个人'), room={'Su', 'Brute', 'Raider'}, new=True,
   bg='The heavy steel door hangs shattered open at the top of the steps with black night and blowing snow behind it, and the frost-furred wine racks line the left wall.',
   holds='The frame holds exactly three people, Su, Brute and Raider, the stacked cases, the steps and the shattered door.')

S.T('B-03', '03｜酒窖：苏清月把燃烧瓶砸向台阶，火焰腾起，两个暴徒被逼得连连后退', 6, CELLAR,
    [P('su_down', 'left', "standing in the cellar in profile facing frame-right with her right arm cocked back at her shoulder holding the burning bottle, a flame guttering from its neck", 'Brute', "her eyes narrowed, her lips pressed in a hard line, her brows low"),
     P('brute_raider', 'center', "standing on the second concrete step in profile facing frame-left with the sledgehammer raised in both hands", 'Su', "his eyes wild, his lips curled under his scarf, his brows lowered"),
     P('raider_lean', 'right', "standing on the top step in the shattered doorway behind him in profile facing frame-left, a steel crowbar raised across his chest", 'Su', "his eyes wide, his brows raised, his mouth open under his scarf")],
    'Medium-wide shot, all three from the head to the feet, in the middle third of the frame, in the frozen wine cellar.',
    "<su_down> throws the burning bottle at the steps in one hard sweep of her arm, her eyes on <brute_raider>, and it bursts into a ball of orange flame on the second step. <brute_raider> lets the hammer swing wide and reels back with his arm over his face, and <raider_lean> ducks behind him, and both men stagger backward up the steps and out through the doorway until the doorway is empty, flames licking the steps." + ' ' + AES_B03[0],
    "苏清月手臂猛地一挥，把燃烧瓶砸向台阶，眼睛盯着壮实的暴徒，瓶子在第二级台阶上爆成一团橙色的火焰。壮实的暴徒让大锤甩到一边，用手臂挡着脸向后退，阿瘦缩着头躲在他后面，两个人踉踉跄跄地沿着台阶退出门口，直到门口空无一人，火苗舔着台阶。" + AES_B03[1],
    SOUND_FLAME, exit={'Brute', 'Raider'},
    cam=('The camera pulls back slowly from the foot of the steps until the flames, the doorway and Su all fill the frame.', '镜头从台阶脚下缓缓向后拉，直到火焰、门口和苏清月都在画面里。'),
    bg='The heavy steel door hangs shattered open at the top of the steps with black night and blowing snow behind it.',
    holds='The frame holds exactly three people, Su, Brute and Raider, the stacked cases, the steps and the shattered door.', room={'Su', 'Brute', 'Raider'}, new=True)

TA('B-04', '04｜酒窖：台阶上的火还烧着，苏清月靠着货箱坐在地上，手抖得握不住瓶颈，低声给自己打气', 10, CELLAR,
   [P('su_down', 'center', "sitting on the floor between the stacked cases with her back against a case in profile facing frame-right, the broken neck of the bottle still in her trembling right hand, the firelit steps glowing behind her", 'obj:her own shaking right hand', "her breath shuddering, her lips trembling then pressing together, her brows drawn")],
   'Medium close shot, the figure from the head to the waist, in the middle third of the frame, in the frozen wine cellar.',
   "<su_down> stares at her shaking hand with the broken bottle neck, clenches it shut, and murmurs a short line to herself in a thin shaking voice, talking to nobody, her lips trembling, then a second line in a lower, steadier voice, her lips pressing together and her brows drawn. Nobody else is in the cellar.",
   "苏清月盯着自己握着半截瓶颈、不停发抖的手，把手攥紧，然后用细细发颤的声音自言自语了一句很短的话，不是对任何人说的，嘴唇发抖，接着用更低、更稳的声音又说了一句，嘴唇抿紧、眉头拧着。酒窖里没有别人。",
   voiced('The crackle of the dying flames on the steps, a thin wind through the doorway and her shuddering breath.', '台阶上渐渐变小的火焰的噼啪声、风从门口吹进来细细的呼啸和她发抖的呼吸声。'), AES_B04,
   vo=times([('su_down', "手别抖。", 'Su'), ('su_down', "我得去找他。", 'Su')], t0=1.2),
   cam=pull('her shaking hand holding the broken bottle neck', '她颤抖的手和半截瓶颈', 'Su sitting among the stacked cases with the firelit steps behind her', '苏清月坐在货箱之间，身后是映着火光的台阶'),
   room={'Su'}, new=True,
   bg='Behind her the steps glow orange from the dying flames and the shattered doorway stands empty at the top.',
   holds='The frame holds Su alone sitting between the stacked cases, the firelit steps and the empty doorway.')

TA('B-05', '05｜冻城：苏清月从地下出口爬出来，走过一条冰雕一样的街，在白领靠着的车旁停下，看他的脸', 15, SIDEWALK_FROST,
   [P('su_trek', 'left', "walking along the frozen sidewalk in profile facing frame-right, a heavy hiking backpack on her shoulders and ski goggles pushed up on her forehead, her gloved hand reaching toward the man's frosted shoulder", 'obj:the frost-covered face of the man sitting against the sedan', "her lips parted, her brows pulled together, her eyes wet"),
    P('office_guy', 'right', "sitting on the curb with his back against the door of the frost-white silver sedan in profile facing frame-left, his head rested back, a layer of white frost over his lashes, brows and hair", 'closed', "his face still and calm", shut='gently closed')],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, on the frozen boulevard.',
   "<su_trek> walks slowly past the ice-encased runners frozen along the sidewalk, her breath streaming white, and stops in front of the sedan; she stares at <office_guy>'s still frosted face, brushes a layer of frost from his shoulder with her gloved hand and murmurs a short line to herself in a hoarse, shaking voice, her lips parted, then a second line in a harder, lower voice, her brows pulling together; after the last line she lowers her goggles over her eyes and walks on out of the frame to the right while he sits motionless.",
   "苏清月慢慢走过人行道上保持着奔跑姿势冻在冰里的人，白气一缕缕往外喷，在那辆轿车前停下；她盯着白领结满霜、一动不动的脸，用戴手套的手把他肩上的一层霜拂掉，用沙哑发颤的声音低声自言自语了一句，嘴唇微张，接着用更硬、更低的声音又说了一句，眉头拧到一起；最后一句之后，她把护目镜拉下来盖住眼睛，朝右边走出画面，他一动不动地坐着。",
   voiced('The hush of a frozen street, a thin wind and her ragged breath.', '冰封街道的寂静、细细的风声和她粗重的呼吸。'), AES_B05,
   vo=times([('su_trek', "他们没跑掉。", 'Su'), ('su_trek', "我不能，变成这样。", 'Su')], t0=3.0),
   cam=('The camera tracks sideways slowly beside her as she walks until she stops in the middle third of the frame in front of the sedan.', '镜头缓缓横移跟着她走，直到她停在画面中间三分之一、那辆轿车前面。'),
   room={'Su', 'Office'}, new=True,
   bg='Behind them the frozen boulevard lies in thick drifting mist, with people frozen mid-run in white ice along both sidewalks and ice-encased cars.',
   holds='The frame holds exactly two people: Su and Office, on the frozen sidewalk beside the frost-white sedan, with the frozen boulevard behind them.')

TA('B-06', '06｜冰封高速公路：苏清月扶着冻住的车顶，在一眼望不到头的车流里往前走，镜头升起，车队一直排到天边', 15, HWY2,
   [P('su_trek', 'center', "walking along the middle of the highway between the ice-encased cars in profile facing frame-right, one gloved hand sliding along the frost-white roof of a car for balance, a heavy hiking backpack on her shoulders, wind pulling at her black scarf", 'obj:the far end of the frozen highway', "her jaw clenched, her brows low, her lips pressed tight")],
   'Wide shot, the figure from head to toe, in the middle third of the frame, on the frozen highway.',
   "<su_trek> trudges forward along the highway with her gloved hand sliding along a car roof, a gust shoving her sideways so she braces against the car, then she pushes upright and speaks a short line to herself in a cracked, defiant voice, her jaw clenched, and a second line, lower, as she keeps walking. Nobody else is in the frame.",
   "苏清月一步一步沿着高速公路往前走，戴手套的手扶着冻住的车顶，一阵风把她推得往旁边歪，她靠在车上撑住，然后重新站直，用沙哑又不服输的声音低声自言自语了一句，下颌咬紧，接着一边往前走，一边用更低的声音又说了一句。画面里没有别人。",
   SOUND_TRUDGE, AES_B06,
   vo=times([('su_trek', "山里，就在山里。", 'Su'), ('su_trek', "走。", 'Su')], t0=2.4),
   cam=rise('the endless line of frozen cars stretching to the horizon with the tiny traveler among them', '一直排到天边的冰封车流和车流里那个小小的行路人'),
   room={'Su'}, new=True,
   bg='Ice-encased cars stand bumper to bumper to the horizon on both sides of her and the snow-covered guardrails line the road.',
   holds='The frame holds Su alone walking along the frozen highway among the ice-encased cars.')

TA('B-07', '07｜冰河：苏清月趴在黑色的冰面上，一寸一寸往对岸爬，冰在身下呻吟，前面裂开一条细缝', 15, RIVER,
   [P('su_trek', 'center', "lying flat on her stomach on the black ice of the frozen river in profile facing frame-right with her arms and legs spread wide, the heavy backpack on her shoulders, one gloved hand reaching forward across the ice", 'obj:the far bank of the river ahead', "her lips pressed tight, her brows drawn, her breath shuddering")],
   'Wide low shot, the figure from head to toe, in the middle third of the frame, on the frozen river.',
   "<su_trek> crawls forward along the black ice an inch at a time, spreading her weight, her breath streaming white; a deep groan runs under the ice and a hairline crack creeps slowly across the surface in front of her hand, and she freezes with her face against the ice, whispering a short line to herself in a thin, shaking voice, her lips trembling; then she spreads her arms and legs wider and slides forward past the crack, and a second line, steadier, as the far bank draws near. Nobody else is in the frame.",
   "苏清月趴在黑色的冰面上，一寸一寸往前爬，把重量尽量摊开，白气一缕缕往外喷；冰面下传来一声深沉的呻吟，一条发丝一样的裂纹慢慢爬过她手前面的冰，她整个人僵住，脸贴着冰，用细细发颤的声音低声说了一句，嘴唇发抖；然后她把手脚摊得更开，从裂纹旁慢慢滑过去，快到对岸时用更稳的声音又说了一句。画面里没有别人。",
   SOUND_ICE, AES_B07,
   vo=times([('su_trek', "别裂，别裂。", 'Su'), ('su_trek', "快到了。", 'Su')], t0=2.0),
   cam=('The camera creeps forward at ice level in front of her until her face and the spreading crack fill the middle third of the frame.', '镜头贴着冰面在她前面慢慢往前移，直到她的脸和蔓延的裂纹占满画面中间三分之一。'),
   room={'Su'}, new=True,
   bg='Behind her the wide frozen river stretches away under blowing snow and the snow-laden reeds of the far bank rise ahead.',
   holds='The frame holds Su alone lying on the frozen river, the crack in the ice and the far bank.')

TA('B-08', '08｜暴风雪：苏清月倒在雪里，想就躺一会儿，又自己把自己骂起来，撑着爬起来', 15, WHITEOUT,
   [P('su_trek', 'center', "lying face-down in a deep snowdrift in profile facing frame-right, the heavy backpack on her shoulders, one gloved hand clutching a crumpled paper slip in the snow in front of her, her goggles crusted with frost", 'obj:the crumpled paper slip in her hand', "her eyes half-closed, her lips cracked and trembling, her brows slack")],
   'Medium close low shot, the figure from the head to the waist, in the middle third of the frame, in the blizzard.',
   "<su_trek> lies still in the snowdrift with the blizzard streaming over her and speaks a first line to herself in a faint, slack voice, her eyes half-closed; then her gloved hand tightens on the paper slip and she speaks a second line in a harder voice; she plants her palms in the snow and speaks a third line through clenched teeth, her brows pulling low; finally she pushes herself up onto her hands and knees, lifts her head into the wind and speaks the last line in a raw, steady voice, her jaw clenched. Nobody else is in the frame.",
   "苏清月趴在雪堆里一动不动，暴风雪从她身上流过去，她用微弱发软的声音自言自语了第一句，眼睛半闭；然后她戴手套的手攥紧了那张纸，用更硬的声音说了第二句；她把手掌按进雪里，咬着牙说了第三句，眉头压低；最后她撑着自己爬起来，跪在地上，抬起头迎着风，用沙哑却稳的声音说了最后一句，下颌咬紧。画面里没有别人。",
   SOUND_WHITEOUT, AES_B08,
   vo=times([('su_trek', "就躺一会儿。", 'Su'), ('su_trek', "不行。", 'Su'), ('su_trek', "起来！", 'Su'), ('su_trek', "林峰，你欠我的。", 'Su')], t0=1.0),
   cam=push('her face', '她的脸'), room={'Su'}, new=True,
   bg='Around her the blizzard streams across the snowfield in white sheets and the single dark frozen tree at the right edge is half hidden in the white.',
   holds='The frame holds Su alone in the snowdrift, the crumpled paper slip in her hand and the blizzard around her.')

TA('B-09', '09｜暮色雪原：天暗下来，小小的苏清月拖着长长的影子穿过雪原，远处山脊上一排冰雕，第一缕绿色极光亮起来', 12, DUSK_RIDGE,
   [P('su_trek', 'center', "walking across the snowfield as a small figure in profile facing frame-right, layered white and black down jackets, a heavy backpack on her shoulders and ski goggles over her eyes, a long blue shadow stretching behind her", 'obj:the dark mountains ahead beyond the ridge', "her jaw set, her face tired and fierce")],
   'Extreme wide shot, the small figure in the middle third of the frame, across the snowfield at dusk.',
   "<su_trek> keeps walking steadily across the snow at dusk, a small dark figure with a long blue shadow, and she does not glance at the line of white ice-encased human figures frozen mid-run along the low ridge at the back of the frame; the first faint curtain of green aurora ripples into the sky above the ridge and brightens as she walks. Nobody else is in the frame.",
   "暮色里，苏清月作为一个小小的黑色身影，拖着一条长长的蓝色影子，稳稳地往前走过雪原，她没有看一眼画面远处低矮山脊上那一排保持奔跑姿势、冻在白色冰里的人形；山脊上空，第一缕淡淡的绿色极光一圈圈亮起来，随着她一步步往前走越来越亮。画面里没有别人。",
   SOUND_DUSK, AES_B09,
   cam=rise('the small traveler, the ridge of ice figures and the aurora above them', '那个小小的行路人、山脊上的冰雕和上空的极光'),
   room={'Su'}, new=True,
   bg='At the back of the frame a line of white ice-encased human figures frozen mid-run stands along the low ridge under the first green aurora.',
   holds='The frame holds Su alone as a small figure on the snowfield, the ridge of ice figures and the aurora.')

# ================================================================================================ 补拍 C
bC = S.episode('补拍C｜手术室的信任与伊甸园之门（手术前插一条；替换剧本第10集04号、06号）',
               '手术前，林峰把手术刀刀柄朝她推过去，把手交给她；手术后，苏清月剪断线，林峰夸她手稳，然后拿出协议说签了就是自己人，她问他是不是早就想拉她入伙，他说从你买下我房子那天；然后他带她走到钢门前，推开，粉紫色的光涌出来。', 3)

ROOM_BG = ("The room is a small windowless underground medical room: bare white-tiled walls on every side, no windows, no doors and no other furniture in view; "
           "a steel operating table covered with a sterile blue drape stands between them under a round surgical lamp, an open silver case of instruments stands at frame-left and a plain steel chair stands at frame-right. Hard white light from the round surgical lamp falls on them.")
ROOM_HOLDS = 'The frame holds exactly two people, Su and Lin, and nobody else, with the draped table and the surgical lamp between them.'

TA('C-01', '01｜手术前（插在剧本第10集01号前）：林峰把手术刀刀柄朝她推过去，说把手交给她，苏清月怀疑，林峰说你带着药穿过了雪原，她接过刀', 15, None,
   [P('su_surgeon', 'left', "standing at the end of the steel table in profile facing frame-right with one white-gloved hand resting on the edge of the blue drape", 'Lin', "her eyes narrowed, her lips pressed in a thin hard line, her brows low"),
    P('lin_white', 'right', "sitting on the plain steel chair in profile facing frame-left, his swollen dark left hand laid palm-down on the blue drape and his right hand sliding a silver scalpel across the drape handle-first toward her", 'Su', "his jaw relaxed, his lips set flat, his brows level, his eyes steady")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the medical room.',
   "<lin_white> slides the scalpel across the drape handle-first and speaks the first line to <su_surgeon> in a low, calm voice, his jaw relaxed and his eyes steady; <su_surgeon> looks from the scalpel to his face and answers with the second line to <lin_white> in a hard, suspicious voice, her eyes narrowed and her lips pressed in a thin line; <lin_white> speaks the third line to <su_surgeon> in a quiet, sure voice, his brows level; <su_surgeon> exhales, her lips softening, and speaks the last line to <lin_white> in a low, tight voice; after the last line she picks up the scalpel and tilts it in the light.",
   "林峰把手术刀刀柄朝前沿着蓝布推过去，用低沉平静的声音对苏清月说出第一句，下颌放松、眼睛稳稳的；苏清月看看刀，又看看他的脸，用冷硬怀疑的声音对林峰答出第二句，眼睛眯起、嘴唇抿成一条细线；林峰用安静笃定的声音对苏清月说出第三句，眉毛平直；苏清月呼出一口气，嘴唇松下来，用低沉发紧的声音对林峰说出最后一句；最后一句之后，她拿起手术刀，在灯光里微微转了转。",
   SOUND_MED2, AES_C01,
   lines=[('lin_white', "刀给你。手，也给你。", 0.8, 'Su'), ('su_surgeon', "你就不怕，我下错刀？", 0.8, 'Lin'), ('lin_white', "你带着药，穿过了雪原。", 0.8, 'Su'), ('su_surgeon', "别后悔。", 0.8, 'Lin')],
   cam=slide('to the left', '左', 'their two faces and the scalpel on the drape fill the middle third of the frame', '两个人的脸和蓝布上的手术刀占满画面中间三分之一'),
   room={'Su', 'Lin'}, new=True, bg=ROOM_BG, holds=ROOM_HOLDS)

TA('C-02', '02｜手术后（替换剧本第10集04号的前半）：苏清月剪断线头说好了，林峰取下毛巾夸她手稳，她把协议推到他面前', 15, None,
   [P('su_surgeon', 'left', "sitting on the stool in profile facing frame-right, small scissors in her right hand just clipping the end of the thread over his neatly stitched left hand wrapped in white gauze, her shoulders dropping", 'Lin', "her lips softening, her brows relaxing"),
    P('lin_white', 'right', "sitting on the plain steel chair in profile facing frame-left, the rolled towel just dropped from his mouth into his right hand, his pale forehead damp with sweat, a thin folded paper lying on the drape in front of him", 'Su', "a faint tired curve at one corner of his mouth, his brows loosening")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the medical room.',
   "<su_surgeon> clips the end of the thread, sets the scissors down and speaks the first line to <lin_white> in a quiet, tired, relieved voice, her lips softening; <lin_white> takes the towel out of his mouth and answers with the second line to <su_surgeon> in a hoarse, low voice with a trace of awed respect, a faint tired curve at one corner of his mouth; <su_surgeon> glances at the folded paper on the drape and speaks the third line to <lin_white> in a dry, curious voice, one brow lifting; <lin_white> speaks the last line to <su_surgeon> in a low, steady voice and slides the paper an inch toward her with two fingers.",
   "苏清月剪断线头，放下剪刀，用安静疲惫又松了一口气的声音对林峰说出第一句，嘴唇放松；林峰把毛巾从嘴里拿出来，用沙哑低沉、带一点佩服的声音对苏清月答出第二句，嘴角挂着一丝疲倦的弧度；苏清月瞥了一眼蓝布上折好的纸，用干干的、带着好奇的声音对林峰说出第三句，一边眉毛挑起；林峰用低沉稳当的声音对苏清月说出最后一句，用两根手指把那张纸朝她推近一寸。",
   SOUND_MED2, AES_C02,
   lines=[('su_surgeon', "好了。", 0.8, 'Lin'), ('lin_white', "你的手，比我想的稳。", 0.8, 'Su'), ('su_surgeon', "这是什么？", 0.8, 'Lin'), ('lin_white', "签了，就是自己人。", 0.8, 'Su')],
   cam=pull('his neatly stitched left hand wrapped in white gauze on the drape', '他缝合好、缠着白纱布的左手', 'Su and Lin sitting across the table from each other', '隔着桌子对坐的苏清月和林峰'),
   room={'Su', 'Lin'}, new=True, bg=ROOM_BG, holds=ROOM_HOLDS)

TA('C-03', '03｜手术后（替换剧本第10集04号的后半）：她问是不是早就想拉她入伙，他说从你买下我房子那天，她把协议拉到自己面前', 8, None,
   [P('su_surgeon', 'left', "sitting on the stool in profile facing frame-right, one white-gloved hand resting on the edge of the blue drape and her eyes on his face", 'Lin', "one brow arched, her lips curving wryly"),
    P('lin_white', 'right', "sitting on the plain steel chair in profile facing frame-left, his bandaged left hand resting on the drape and his right hand laying a thin folded paper on the drape in front of her", 'Su', "his jaw relaxed, his lips set flat, his brows level")],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, in the medical room.',
   "<su_surgeon> glances at the paper and speaks the first line to <lin_white> in a dry, half-teasing voice, one brow arched and her lips curving wryly; <lin_white> speaks the second line to <su_surgeon> with a faint warm curve at one corner of his mouth; after the last line <su_surgeon> draws the paper toward her.",
   "苏清月瞥了一眼那张纸，用干干的、半带逗弄的声音对林峰说出第一句，一边眉毛挑起、嘴角带着一抹玩味的半笑；林峰嘴角带着一丝温暖的弧度对苏清月说出第二句；最后一句之后，苏清月把纸拉到自己面前。",
   SOUND_MED2, AES_C03,
   lines=[('su_surgeon', "你早就想拉我入伙？", 0.8, 'Lin'), ('lin_white', "从你买下我房子那天。", 0.8, 'Su')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True, bg=ROOM_BG, holds=ROOM_HOLDS)

TA('C-04', '04｜钢门前（替换剧本第10集06号的前半）：林峰把手放在门把上，说带你去看看我们的伊甸园，她一边好奇一边迟疑', 15, EDENDOOR,
   [P('su_cozy', 'left', "standing in the corridor in profile facing frame-right with her arms folded in the oversized cream sweater", 'Lin', "one brow arched, her lips parted in curiosity"),
    P('lin_home', 'right', "standing beside the steel door in profile facing frame-left, his right hand resting on the door handle and his left hand wrapped in white gauze at his side", 'Su', "his jaw relaxed, a faint pleased curve at one corner of his mouth, his brows lifting")],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the concrete corridor.',
   "<lin_home> speaks the first line to <su_cozy> in a quiet, warm voice, a faint pleased curve at one corner of his mouth; <su_cozy> answers with the second line to <lin_home> in a curious, wary voice, one brow arched and her lips parted; <lin_home> speaks the third line to <su_cozy> in a low, proud voice, his hand tightening on the handle; <su_cozy> unfolds her arms and speaks the last line to <lin_home> in a soft, wondering voice, her brows lifting; after the last line he presses the handle down and the door begins to swing open.",
   "林峰用安静温暖的声音对苏清月说出第一句，嘴角带着一丝满意的弧度；苏清月用好奇又有点戒备的声音对林峰答出第二句，一边眉毛挑起、嘴唇微张；林峰用低沉带着骄傲的声音对苏清月说出第三句，握着门把的手收紧；苏清月放下抱着的手臂，用轻柔带着惊奇的声音对林峰说出最后一句，眉毛上扬；最后一句之后，他把门把压下去，门开始向里打开。",
   SOUND_DOOR2, AES_C04,
   lines=[('lin_home', "跟我来。", 0.8, 'Su'), ('su_cozy', "去哪儿？", 0.8, 'Lin'), ('lin_home', "我们的伊甸园。", 0.8, 'Su'), ('su_cozy', "你真的做到了？", 0.8, 'Lin')],
   cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
   bg='The heavy steel door with the keypad stands at frame-right with a thin line of pink-violet light glowing around its edges.',
   holds='The frame holds exactly two people, Su and Lin, and nobody else, in the concrete corridor beside the steel door with the keypad.')

insert2('C-05', '05｜插镜（替换剧本第10集06号的后半）：钢门敞开了，粉紫色的光像潮水一样涌出来，铺满走廊的地面，光里隐约有绿叶', 6, EDENDOOR,
        'Wide shot of the concrete corridor, the open steel door in the middle third of the frame; nobody in the scene.',
        "The heavy steel door stands wide open and a flood of warm pink-violet light pours out of it across the bare concrete floor of the corridor, dust motes and glittering mist drifting in the beam, with a faint green sheen of leaves visible in the glow beyond the doorway. Nothing else moves.",
        "厚重的钢门敞开着，一大片暖暖的粉紫色光像潮水一样从门里涌出来，铺在走廊光秃秃的混凝土地面上，光束里飘着尘埃和闪光的水雾，门后的光里隐约有绿叶的光泽。别的什么都不动。",
        SOUND_EDENLIGHT, 'The frame holds the concrete corridor, the open steel door and the pink-violet light pouring out of it, and nobody in the scene.',
        push1('the open doorway', '敞开的门口'), AES_C05)

doc = S.finish()
