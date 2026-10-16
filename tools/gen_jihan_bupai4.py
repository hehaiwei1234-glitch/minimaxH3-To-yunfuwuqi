#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》补拍包 4（2026-10-16，hh 11:30–11:33）：末日景色切镜用，4 集 18 个任务，每个任务 10 秒，全部无台词。
以补拍3 的 JSON 为底（026 → 补拍3 → 补拍4），必须等补拍3 在插件里全部跑完再追加；追加窗口不要勾每集／总／任务秒数。
分配（hh 要的 18 个，他全选）：
  补拍4A 冰雪自然（4）：冰封森林、极光雪原、冰川峡谷冰瀑、冰封海岸；
  补拍4B 冻城废墟（4）：冻城全景、冰封游乐场、冰封高速车队、男主走在冰封街上抬头看大楼；
  补拍4C 天象与男主（5）：雪夜银河、冰原日出、男主走过极光雪原、男主蹲在冰湖边看气泡、男主在山脊看黑掉的城市；
  补拍4D 两个人（5）：并肩走过极光雪原（他拉起她的领口）、冰封森林里她伸手接雪粉、冻住的游乐场里她踮脚碰摩天轮的霜、山脊上并肩看日出、温泉口的暖区（她蹲下摸一棵绿芽）。
男主一个人的散步全部算在林峰还活着的阶段（他后面要留下关最后一道闸门）。
写法：A（慢）、每个任务一句“光和空气”、运镜每个任务不同（动作＋终点）、现场音写响（风声、踩雪、冰裂）；纯景色任务不写人，人物用已有素材 lin_arctic／su_arctic（白色极地服）保脸。
H3 方面的风险（交稿时单列、不算我的错）：
  · 景色里的云、雪粉、极光、蒸汽可能只是静止的，不会真的流动；
  · 走路的镜头：人可能原地踏步、脚印可能没有（要靠开场图画好）；呼出的白气要靠开场图；
  · 两人并肩（4D）、她接雪粉／碰摩天轮的霜（手部）；4D-1 拉起领口（手到脖子，慢动作）；
  · 大场景（冻城全景、高速车队、冰封海岸）可能画成一堆糊的白；游乐场摩天轮的结构可能画歪；
  · 约一成开场图不按文字画；“中国人”的脸是否出对。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
import _jihan_base7 as B7
from _jihan_base7 import *
import _jihan_base8 as B8
from _jihan_base8 import *
import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407, cap=12)
OUT = '补拍/补拍4_末日景色十八个_制作稿_追加'
S = Session('补拍/补拍3_地球固定镜头与情侣冰雕_制作稿_追加.json', OUT, 97000)
B6.S = S
B7.S = S
AE = lambda en, zh: (en, zh)
CM = lambda en, zh: (en, zh)


def new_scenery(b, key, label, en, zh, holds):
    new_scene(b, key, label, en, zh, holds)


mode('A')
_H.CFG['sfx_loud'] = True      # hh 10-15：现场音／环境音要写响

# ---------------------------------------------------------------------------------------------- 场景
FOREST = Scene('frost_forest', " A low pale sun filters through thin white mist and fine ice crystals drift in the still cold air.",
               " Fixed stage layout: a hushed forest of tall pines and birches fills the frame, every trunk and branch thickly furred with white hoarfrost and glittering rime, the snowy ground smooth and unmarked, soft shafts of pale sunlight slanting between the trunks and mist lying low along the ground; nobody in the scene.")
FOREST_PATH = Scene('frost_forest', FOREST.end,
                    " Fixed stage layout: a narrow path of smooth white snow winds down the middle of the frame between tall frost-furred pines and birches, fine ice crystals hanging in slanting shafts of pale sunlight, soft mist low along the ground.")
AURORA = Scene('snow_field', " A broad green aurora ripples across the black sky and its light glitters on the snow, the air cold and crystal clear.",
               " Fixed stage layout: a vast smooth snowfield fills the lower half of the frame, a dark line of far pines along the horizon at the back, and a broad green and violet aurora band fills the whole sky above; nobody in the scene.")
AURORA_WALK = Scene('snow_field', AURORA.end,
                    " Fixed stage layout: a vast smooth snowfield stretches across the middle of the frame with a long line of boot prints running across it, a dark line of far pines along the horizon at the back and a broad green and violet aurora band filling the sky above.")
GLACIER = Scene('glacier_falls', " Cold blue light filters down between the ice walls and fine ice dust glitters in the still air.",
                " Fixed stage layout: a deep blue glacier canyon whose sheer walls of layered translucent blue ice rise on both sides of the frame, a huge frozen waterfall hanging from the wall in the middle of the frame like a giant organ of long icicles, a floor of smooth snow and a narrow strip of pale sky at the very top; nobody in the scene.")
COAST = Scene('ice_coast', " A dull white sun hangs low in a flat grey sky and a thin wind drags a veil of snow across the ice.",
              " Fixed stage layout: a vast grey frozen sea fills the lower half of the frame with huge pale blue icebergs locked in the ice, a rusted cargo ship tilted and stuck in the ice at frame-right, a flat grey sky and a dull white sun low at the back; nobody in the scene.")
CITY = Scene('frozen_city_wide', " A pale cold sun glows through thin white mist and a few flakes of rime drift down between the towers.",
             " Fixed stage layout: a dense downtown of tall glass towers hung with long icicles fills the frame, a silent street canyon of frost-white cars opening down the middle of the frame, white mist drifting between the towers and a pale sun low in a grey-blue sky; nobody in the scene.")
STREET = Scene('frozen_street', CITY.end,
               " Fixed stage layout: a wide silent city boulevard of frost-white cars and white frozen street trees recedes down the middle of the frame, glass towers hung with long icicles rising on both sides, white mist drifting low along the road.")
FAIR = Scene('frozen_fair', " A pale dim sun hangs in a grey sky and a thin mist of ice crystals drifts across the deserted ground.",
             " Fixed stage layout: a deserted amusement park with a giant Ferris wheel frozen under thick white frost at the centre of the frame, its gondolas hung with icicles, frost-furred carousel horses in the foreground and snow on the ground; nobody in the scene.")
FAIR_WHEEL = Scene('frozen_fair', FAIR.end,
                   " Fixed stage layout: the foot of a giant Ferris wheel thick with white frost fills the middle of the frame, a frosted carousel with frost-furred horses stands at frame-left, a deserted snowy path runs through the middle of the frame, and icicle-hung gondolas hang high above.")
HIGHWAY = Scene('highway_calm', " A pale white sun glows through a high thin haze and the air over the road is perfectly still.",
                " Fixed stage layout: a wide multi-lane highway runs straight down the middle of the frame to the vanishing point, packed with a long unbroken line of cars and trucks encased in clear ice, snow-covered guardrails and a flat grey-blue plain on both sides; nobody in the scene.")
STARS = Scene('star_night', " Starlight lays a faint cold blue glow over the snow, and the air is dry and absolutely still.",
              " Fixed stage layout: a vast snowfield glowing faint blue fills the lower third of the frame with a dark ridge silhouette along the back, and an unbelievably dense Milky Way arcs across the black sky above with thousands of stars; no lights anywhere; nobody in the scene.")
SUNRISE = Scene('sunrise_ice', " A dull white sun climbs over the horizon and the cold air glows pink and gold.",
                " Fixed stage layout: an endless frozen plain stretches across the frame with pale pressure ridges of ice and long soft shadows, a dull white sun rising on the horizon at the back and the ice flushed pink and gold; nobody in the scene.")
RIDGE = Scene('ridge_dead_city', " A faint blue dawn glows on the horizon and mist lies in the valleys; the cold air is dead still.",
              " Fixed stage layout: a snowy ridge top with a few bare dark rocks fills the foreground, and far below it a vast dark city with no lights at all spreads across the valley under a faint blue dawn, mist in the low streets; nobody in the scene.")
RIDGE_SUN = Scene('ridge_dead_city', " A dull white sun rises over the city and the cold air glows pink and gold.",
                  " Fixed stage layout: a snowy ridge top with a few bare dark rocks fills the foreground, and far below it a vast dead city of frost-white towers spreads across the valley, a dull white sun rising behind it and flushing the snow and the mist pink and gold.")
LAKE_EDGE = Scene('ice_lake', " A broad green aurora lays cold colour on the glassy ice and the air is cold and still.",
                  " Fixed stage layout: the snowy shore is at the bottom of the frame and the dark glassy ice of the frozen lake fills the middle of the frame, a pale crack running across it and rows of grey frozen bubbles trapped deep inside; a broad aurora fills the sky.")
SPRING = Scene('spring_meadow', " Pale warm light falls through drifting steam and the air over the thawed ground is soft and damp.",
               " Fixed stage layout: a ring of thawed ground fills the middle of the frame, dark wet soil with patches of vivid green grass and tiny green sprouts around a pool of clear steaming water, white steam rising from it, a high wall of snow and ice all around the edge of the ring; nobody in the scene.")
SPRING_WALK = Scene('spring_meadow', SPRING.end,
                    " Fixed stage layout: a ring of thawed ground fills the middle of the frame, dark wet soil with patches of vivid green grass and tiny green sprouts around a pool of clear steaming water, white steam rising from it, a high wall of snow and ice all around the edge of the ring; a narrow trodden path of footprints leads in from frame-left.")

# ================================================================================================ 补拍4A 冰雪自然
bA = S.episode('补拍4A｜末日景色：冰雪自然（冰封森林、极光雪原、冰川峡谷冰瀑、冰封海岸）',
               '四个纯景色切镜：雾凇森林里细小的冰晶往下飘、极光铺满雪原、蓝色冰壁间的冻瀑布、灰色冻海里搁浅的货轮。', 77)
new_scenery(bA, 'frost_forest', '雾凇森林（高高的松树和桦树，每一根树干树枝都裹着白色的霜花，雪地平整无痕，斜斜的淡淡阳光，低低的雾）',
            'A hushed forest of tall pines and birches, every trunk and branch furred with white hoarfrost, smooth unmarked snow, slanting shafts of pale sunlight and low mist.',
            '一片寂静的树林，高高的松树和桦树，每一根树干和树枝都裹着白色的霜花，雪地平整、没有脚印，淡淡的阳光斜斜地穿过树干，雾低低地贴着地面。',
            'the frost-furred trunks, the unmarked snow and the slanting sunlight')
new_scenery(bA, 'glacier_falls', '冰川峡谷（两侧是上百米高的蓝色层叠冰壁，中间一道巨大的冻瀑布像巨大的管风琴一样挂着长长的冰柱，谷底是平整的雪）',
            'A deep blue glacier canyon with sheer layered blue ice walls and a huge frozen waterfall hanging like a giant organ of icicles in the middle, a smooth snow floor and a narrow strip of pale sky.',
            '一条深蓝色的冰川峡谷，两侧是笔直的层叠蓝色冰壁，中间挂着一道像巨大管风琴一样的冻瀑布，谷底是平整的雪，头顶只有一线苍白的天空。',
            'the blue ice walls, the frozen waterfall and the snow floor')
new_scenery(bA, 'ice_coast', '冰封海岸（灰色的冻海，巨大的浅蓝色冰山冻在冰里，右边有一艘锈迹斑斑的货轮歪着搁浅在冰里，灰色的天，一轮低低的暗白色太阳）',
            'A vast grey frozen sea with huge pale blue icebergs locked in the ice, a rusted cargo ship tilted and stuck in the ice at the right, a flat grey sky and a dull white sun low.',
            '一片辽阔的灰色冻海，巨大的浅蓝色冰山冻在冰里，右边一艘锈迹斑斑的货轮歪着搁浅在冰里，天空灰蒙蒙，一轮暗白色的太阳低低地挂着。',
            'the grey ice, the icebergs and the stranded ship')

INS('S-01', '01｜冰封森林：雾凇把每根树枝都裹成白色，细小的冰晶从斜斜的阳光里飘下来，镜头在树干之间低低地滑过去', 10, FOREST,
    'Wide shot of the frost forest, the sunlit trunks centered in the middle third of the frame, nobody in the scene.',
    "Fine ice crystals drift down through the slanting shafts of pale sunlight and a few loose flakes of rime fall silently from a branch; the mist stirs gently along the ground and nothing else moves.",
    "细小的冰晶从斜斜的淡淡阳光里飘下来，几片松散的霜花从树枝上悄悄落下；雾贴着地面轻轻地动，别的什么都不动。",
    Q('A long low sigh of wind through the rimed branches, the faint tinkle of falling ice and a distant soft crack of a frozen trunk.', '风吹过挂满霜的树枝长长低低的叹息声、冰晶落下细细的叮当声和远处一棵冻住的树干轻轻开裂的声音。'),
    'The frame holds the frost-furred trunks, the unmarked snow and the shafts of sunlight, nobody in the scene.',
    CM('The camera glides forward low along the snow between the trunks until a shaft of sunlight shining through the rime-covered branches fills the middle of the frame.', '镜头贴着雪地低低地向前滑过树干之间，直到一道穿过挂满霜花树枝的阳光占满画面中间。'),
    AE("Slanting shafts of pale gold sunlight set every rimed twig glittering like glass while fine ice crystals sparkle in the beams and the mist glows soft white.",
       "斜斜的淡金色阳光把每一根挂霜的细枝照得像玻璃一样闪，光束里细小的冰晶在发亮，雾泛着柔和的白色。"))

INS('S-02', '02｜极光雪原：一片绿紫色的极光铺满整个天空，光洒在平整的雪原上闪着，镜头缓缓从雪面抬起，一直摇到满天的极光', 10, AURORA,
    'Wide shot of the snowfield and the sky, the horizon line centered in the middle third of the frame, nobody in the scene.',
    "The broad green and violet aurora band ripples slowly across the whole sky and its light glitters on the smooth snow; a thin ribbon of powder snow drifts across the ground in the wind.",
    "宽阔的绿紫色极光帷幕缓缓地在整个天空里流动，光洒在平整的雪面上闪着；一缕细细的粉雪被风吹着从地面上飘过。",
    Q('A long low sigh of wind over the open snow, the soft hiss of drifting powder and a deep silence behind it.', '风掠过空旷雪原长长低低的叹息、粉雪飘过细细的沙沙声，和它背后深深的寂静。'),
    'The frame holds the snowfield, the dark line of pines and the sky of aurora, nobody in the scene.',
    CM('The camera starts low on the glittering snow and tilts up slowly until the whole sky of aurora fills the frame.', '镜头从闪光的雪面开始，慢慢向上摇，直到满天的极光占满画面。'),
    AE("Green and violet aurora light slides over the snow in long soft waves and powder crystals sparkle in the air like fine silver dust against the deep blue shadows.",
       "绿色和紫色的极光光线在雪面上一层层柔和地滑过，空气里的粉雪晶体像细细的银粉一样发亮，衬着深蓝色的阴影。"))

INS('S-03', '03｜冰川峡谷：蓝色的冰壁之间挂着一道巨大的冻瀑布，像管风琴一样垂着长长的冰柱，镜头从谷底慢慢升到瀑布的顶端', 10, GLACIER,
    'Wide shot of the glacier canyon, the frozen waterfall centered in the middle third of the frame, nobody in the scene.',
    "The huge frozen waterfall hangs motionless between the blue ice walls while fine ice dust sparkles in the cold light and one long icicle at its edge slowly drips a single bright drop.",
    "巨大的冻瀑布一动不动地挂在蓝色冰壁之间，细小的冰尘在冷光里闪着，瀑布边缘一根长长的冰柱慢慢地滴下一颗发亮的水珠。",
    Q('A deep resonant hush with a slow groan of shifting ice far below and the tiny sharp tick of one drop falling.', '深沉带着回声的寂静，远处冰层移动缓缓的呻吟，和一颗水珠滴落细细的一声脆响。'),
    'The frame holds the blue ice walls, the frozen waterfall and the snow floor, nobody in the scene.',
    CM('The camera rises slowly on a crane from the snow floor along the length of the frozen waterfall until its top and the strip of pale sky fill the frame.', '镜头像吊臂一样从谷底缓缓升起，沿着冻瀑布一路向上，直到瀑布顶端和那一线苍白的天空占满画面。'),
    AE("Cold blue light glows through the translucent ice walls from within and the long icicles catch a thin line of white at every tip while ice dust glitters in the beams.",
       "冷冷的蓝光从半透明的冰壁里面透出来，长长的冰柱每一个尖头都挂着一线白光，冰尘在光束里闪着。"))

INS('S-04', '04｜冰封海岸：灰色的冻海里冻着巨大的浅蓝色冰山，右边一艘锈迹斑斑的货轮歪着搁浅在冰里，一缕雪雾贴着冰面飘过', 10, COAST,
    'Wide shot of the frozen coast, the ice plain centered in the middle third of the frame, nobody in the scene.',
    "A thin veil of snow drifts slowly across the grey ice in front of the huge pale blue icebergs, and the stranded rusted ship sits tilted and silent with a trickle of rime falling from its rail.",
    "一缕薄薄的雪雾慢慢飘过灰色冰面，经过巨大的浅蓝色冰山前面，搁浅的锈迹斑斑的货轮歪在那里一动不动，栏杆上落下一线细细的霜。",
    Q('A broad low moan of wind across the open ice, a long slow creak of the ship\'s frozen hull and the distant boom of ice cracking.', '风掠过辽阔冰面宽宽低低的呜咽、货轮冻住的船体长长慢慢的吱嘎声，和远处冰层开裂的一声闷响。'),
    'The frame holds the grey ice, the icebergs and the stranded ship, nobody in the scene.',
    CM('The camera pushes forward slowly low across the ice until the stranded ship fills the middle third of the frame.', '镜头贴着冰面慢慢向前推，直到搁浅的货轮占满画面中间三分之一。'),
    AE("A dull white sun glows low behind the veil of snow and the ice shines with a cold pearl sheen while the rusted hull takes a thin orange edge of light.",
       "一轮暗白色的太阳低低地从雪雾后面透出光，冰面泛着冷冷的珍珠色光泽，锈红的船体被勾出一线橙色的边光。"))

# ================================================================================================ 补拍4B 冻城废墟
bB = S.episode('补拍4B｜末日景色：冻城废墟（冻城全景、冰封游乐场、冰封高速车队、男主走在冰封街上）',
               '三个纯景色切镜：挂满冰柱的大楼之间滑行、冻住的摩天轮和旋转木马、一直排到天边的冰封车队；再加男主一个人走在冰封的街上，抬头看大楼。', 78)
new_scenery(bB, 'frozen_city_wide', '冰封的市中心（密密麻麻挂满长冰柱的玻璃大楼，中间一条安静的街，霜白色的车，白雾在楼之间飘，一轮苍白的太阳低低挂在灰蓝色的天上）',
            'A dense frozen downtown of glass towers hung with long icicles, a silent street of frost-white cars, white mist drifting between the towers and a pale sun low in a grey-blue sky.',
            '冰封的市中心，密密麻麻的玻璃大楼挂满长长的冰柱，中间一条安静的街停着霜白色的车，白雾在大楼之间飘，一轮苍白的太阳低低地挂在灰蓝色的天空里。',
            'the icicle-hung towers, the frost-white street and the drifting mist')
new_scenery(bB, 'frozen_street', '冰封的大街（宽阔安静的大街，霜白色的车和白色的行道树，两边的玻璃大楼挂着长长的冰柱，白雾贴着路面飘）',
            'A wide silent city boulevard of frost-white cars and white frozen street trees, glass towers hung with long icicles on both sides and white mist drifting low along the road.',
            '宽阔安静的城市大街，霜白色的车和白色的行道树，两边的玻璃大楼挂着长长的冰柱，白雾贴着路面低低地飘。',
            'the frost-white cars, the frozen trees and the icicle-hung towers')
new_scenery(bB, 'frozen_fair', '冰封的游乐场（空无一人，巨大的摩天轮被厚厚的白霜包着，吊舱挂满冰柱，旋转木马的木马长着霜毛，地上是雪）',
            'A deserted frozen amusement park with a giant Ferris wheel under thick white frost, icicle-hung gondolas, frost-furred carousel horses and snow on the ground.',
            '空无一人的冰封游乐场，巨大的摩天轮被厚厚的白霜包着，吊舱挂满冰柱，旋转木马的木马长着一层霜毛，地上是雪。',
            'the frosted Ferris wheel, the carousel and the snowy ground')
new_scenery(bB, 'highway_calm', '冰封的高速公路（笔直宽阔的多车道高速，被透明的冰包住的车和卡车排成一条看不到头的长龙，积雪的护栏，灰蓝色的平原）',
            'A wide straight multi-lane highway packed with a long unbroken line of cars and trucks encased in clear ice, snow-covered guardrails and a flat grey-blue plain.',
            '笔直宽阔的多车道高速公路，被透明的冰包住的车和卡车排成一条看不到头的长龙，护栏上盖着积雪，两边是灰蓝色的平原。',
            'the ice-encased cars and trucks, the guardrails and the vanishing point')

INS('S-05', '05｜冻城全景：挂满长冰柱的玻璃大楼之间，一条霜白色的空街静静地伸向远处，白雾在楼之间飘，镜头像无人机一样在楼群之间向前滑去', 10, CITY,
    'Wide shot of the frozen city, the street canyon centered in the middle third of the frame, nobody in the scene.',
    "White mist drifts slowly between the icicle-hung glass towers, a few flakes of rime fall from a high ledge and the long street of frost-white cars lies perfectly silent below.",
    "白雾在挂满冰柱的玻璃大楼之间慢慢地飘，几片霜花从高处的窗沿落下来，下面那条长街上霜白色的车一动不动，一片寂静。",
    Q('A long hollow sigh of wind through the empty street canyon, the faint tinkle of ice shards falling from the towers and a deep hush behind it.', '风穿过空荡荡的楼群之间长长空空的叹息声、冰碴从大楼上落下细细的叮当声，和它背后深深的寂静。'),
    'The frame holds the icicle-hung towers, the frost-white street and the mist, nobody in the scene.',
    CM('The camera glides forward slowly at rooftop height between the towers like a drone until the long street canyon opens ahead and fills the middle of the frame.', '镜头像无人机一样贴着楼顶的高度在大楼之间缓缓向前滑，直到前方那条长长的街道敞开、占满画面中间。'),
    AE("A pale cold sun glows through the mist and rakes along the glass towers so every icicle catches a thin bright line, while a soft blue shadow fills the street canyon.",
       "一轮苍白冰冷的太阳透过雾气斜斜地扫过玻璃大楼，每一根冰柱都挂着一条细细的亮边，街道里落满柔和的蓝色阴影。"))

INS('S-06', '06｜冰封游乐场：巨大的摩天轮被厚厚的白霜包着，吊舱挂满冰柱，旋转木马的木马长着霜毛，镜头缓缓向摩天轮推过去', 10, FAIR,
    'Wide shot of the frozen fair, the Ferris wheel centered in the middle third of the frame, nobody in the scene.',
    "A thin mist of ice crystals drifts across the deserted ground, an icicle breaks off a gondola and falls silently into the snow, and the frost-furred carousel horses stand frozen in mid-gallop.",
    "一层薄薄的冰晶雾飘过空荡荡的地面，一根冰柱从吊舱上折断、悄悄掉进雪里，长着霜毛的旋转木马停在奔跑的姿势里一动不动。",
    Q('A long low moan of wind through the steel spokes of the wheel, a slow creak of frozen metal and the faint tick of falling ice.', '风吹过摩天轮钢辐条长长低低的呜咽、冻住的金属缓缓的吱嘎声，和冰块落下细细的嗒嗒声。'),
    'The frame holds the Ferris wheel, the carousel and the snowy ground, nobody in the scene.',
    CM('The camera pushes forward slowly past the frost-furred carousel horses until the great Ferris wheel fills the middle third of the frame.', '镜头慢慢向前推，经过长着霜毛的旋转木马，直到巨大的摩天轮占满画面中间三分之一。'),
    AE("A pale dim sun hangs behind the wheel and its thick white frost glows like spun sugar while the icicles on the gondolas catch a thin line of silver light.",
       "一轮苍白暗淡的太阳挂在摩天轮后面，包着它的厚厚白霜像糖丝一样发亮，吊舱上的冰柱被勾出一线银色的光。"))

INS('S-07', '07｜冰封高速：笔直宽阔的高速公路上，被透明的冰包住的车和卡车排成一条看不到头的长龙，镜头从路面缓缓升到高空', 10, HIGHWAY,
    'Wide shot of the frozen highway, the road centered in the middle third of the frame, nobody in the scene.',
    "The long line of ice-encased cars and trucks lies perfectly still along the whole highway while a thin ribbon of snow dust slides across the road in the wind.",
    "整条高速公路上，被冰包住的车和卡车排成的长龙一动不动，一缕细细的雪尘被风吹着从路面上滑过。",
    Q('A broad low whistle of wind along the empty road, the faint crystalline creak of ice-sheathed cars and the far crack of a frozen windshield.', '风吹过空荡荡的公路宽宽低低的呼啸声、被冰包住的车轻轻的晶体吱嘎声，和远处一块冻住的挡风玻璃开裂的脆响。'),
    'The frame holds the long line of frozen vehicles and the vanishing point, nobody in the scene.',
    CM('The camera rises slowly on a crane from road level until the whole highway with its endless line of frozen vehicles stretches to the horizon and fills the frame.', '镜头像吊臂一样从路面的高度缓缓升起，直到整条高速公路和它那一眼望不到头的冻住的车队伸向天边、占满画面。'),
    AE("A pale white sun glows through a high thin haze and every ice-sheathed car body gives off a faint blue-white gleam, a thin line of light running along the guardrails.",
       "一轮苍白的太阳透过高处薄薄的雾霭发着光，每一辆被冰包住的车身都泛着淡淡的蓝白色光泽，一线光沿着护栏延伸出去。"))

TAA('S-08', '08｜冰封街头：男主一个人走在冰封的大街上，停下来，抬头看着挂满冰柱的大楼，镜头从他身边缓缓升起', 10, STREET,
    [P('lin_arctic', 'center', "standing in the middle of the frost-white boulevard in profile facing frame-left, his head tilted far back, his gloved hands hanging at his sides and a trail of boot prints behind him in the white frost", 'obj:the icicle-hung glass towers high above', "his lips slightly parted, his eyes wide and quiet, his brows lifted a little")],
    'Wide shot, the man full-length and small in the middle third of the frame, on the boulevard.',
    "<lin_arctic> walks slowly down the middle of the silent boulevard past the frost-white cars, his breath streaming white, then stops and tilts his head back to look up at the glass towers hung with long icicles; a few flakes of rime drift down past him. The camera rises slowly beside him.",
    "林峰一个人慢慢地走在安静的大街中间，经过霜白色的车，呼出的白气飘着，然后停下来，仰起头看着挂满长冰柱的玻璃大楼；几片霜花从他身边飘落。镜头在他身边缓缓升起。",
    Q('The slow crunch of boots on frost, a long hollow sigh of wind between the towers and the faint tinkle of falling ice.', '靴子踩在白霜上缓缓的脆响、风在楼之间长长空空的叹息声，和冰碴落下细细的叮当声。'),
    AE("A pale cold sun glows through the mist and rims his white suit with silver while a soft blue shadow fills the boulevard and the icicles on the towers catch thin bright lines.",
       "一轮苍白冰冷的太阳透过雾气给他的白色极地服勾上一圈银边，大街里落满柔和的蓝色阴影，大楼上的冰柱挂着细细的亮线。"),
    holds='The frame holds the man small on the frost-white boulevard, the frozen cars and the icicle-hung towers.',
    cam=rise('the man small on the boulevard with the whole row of icicle-hung towers behind him', '大街上那个小小的男人和他身后整排挂满冰柱的大楼'))

# ================================================================================================ 补拍4C 天象与男主
bC = S.episode('补拍4C｜末日景色：天象与男主（雪夜银河、冰原日出、男主三段散步）',
               '两个天象切镜：没有一盏灯的雪夜银河、冰原上的日出；再加男主三段一个人的散步：走过极光雪原、蹲在冰湖边看冰里的气泡、站在山脊上看黑掉的城市。', 79)
new_scenery(bC, 'star_night', '雪夜银河（平整的雪原泛着淡淡的蓝光，后面是一道深色的山脊剪影，上方黑色的天空里一条极其密集的银河横跨天空，没有任何灯光）',
            'A snowfield glowing faint blue at night with a dark ridge silhouette at the back and an unbelievably dense Milky Way arcing across a black sky, no lights anywhere.',
            '夜里的雪原泛着淡淡的蓝光，后面是一道深色的山脊剪影，黑色的天空里一条极其密集的银河横跨天空，没有任何灯光。',
            'the snowfield, the ridge silhouette and the Milky Way')
new_scenery(bC, 'sunrise_ice', '冰原日出（一望无际的冰原有浅色的冰脊和长长的柔和阴影，地平线上一轮暗白色的太阳正在升起，冰面被染成粉金色）',
            'An endless frozen plain with pale pressure ridges and long soft shadows, a dull white sun rising on the horizon and the ice flushed pink and gold.',
            '一望无际的冰原，有浅色的冰脊和长长的柔和阴影，地平线上一轮暗白色的太阳正在升起，冰面被染成粉金色。',
            'the ice plain, the pressure ridges and the rising sun')
new_scenery(bC, 'ridge_dead_city', '山脊上看死城（前景是山脊顶上积雪的深色岩石，远处山谷里一整座没有任何灯光的城市，淡淡的蓝色黎明，低处的街上有雾）',
            'A snowy ridge top with bare dark rocks in the foreground and a vast dark city with no lights spreading across the valley below under a faint blue dawn, mist in the low streets.',
            '山脊顶上积着雪的深色岩石在前景，下面的山谷里是一整座没有任何灯光的城市，天边是淡淡的蓝色黎明，低处的街上有雾。',
            'the snowy ridge, the dark rocks and the dead city below')

INS('S-09', '09｜雪夜银河：没有一盏灯的雪原上，一条极其密集的银河横跨黑色的天空，雪面泛着淡淡的蓝光，镜头从山脊剪影缓缓摇向银河中心', 10, STARS,
    'Wide shot of the snowfield and the sky, the Milky Way arc centered in the middle third of the frame, nobody in the scene.',
    "The dense Milky Way arcs across the black sky while the faint blue glow on the snow shimmers and a single meteor slides silently down the sky behind the ridge.",
    "密集的银河横跨黑色的天空，雪面上淡淡的蓝光微微闪着，一颗流星悄悄地从山脊后面的天空里滑落。",
    Q('A deep dry silence, a very thin whisper of wind over the snow and the faint squeak of cold snow settling.', '深深干燥的寂静，一缕极细的风声掠过雪面，和冷雪轻轻压实的细细吱响。'),
    'The frame holds the snowfield, the ridge silhouette and the Milky Way, nobody in the scene.',
    CM('The camera starts on the dark ridge silhouette and tilts up slowly until the bright core of the Milky Way fills the middle of the frame.', '镜头从深色的山脊剪影开始，慢慢向上摇，直到银河明亮的中心占满画面中间。'),
    AE("Thousands of stars burn in cold white and gold and a faint green airglow tints the horizon while the snow glows a soft blue as if lit from within.",
       "成千上万颗星星燃着冷白和金色的光，地平线上泛着一点淡淡的绿色夜辉，雪面像从里面透出光一样泛着柔和的蓝。"))

INS('S-10', '10｜冰原日出：一轮暗白色的太阳从地平线上升起，冰面被染成粉金色，长长的柔和阴影从冰脊后面拉出来，镜头贴着冰面向前推', 10, SUNRISE,
    'Wide shot of the ice plain at sunrise, the rising sun centered in the middle third of the frame, nobody in the scene.',
    "The dull white sun climbs slowly over the horizon, the pink and gold light spreads across the ice and a thin veil of ice crystals glitters in the rising light.",
    "暗白色的太阳慢慢爬上地平线，粉色和金色的光漫过冰面，一层薄薄的冰晶在升起的光里闪着。",
    Q('A long low sigh of wind across the open ice, the high thin tick of ice warming and cracking in the first light and a deep stillness.', '风掠过辽阔冰面长长低低的叹息、冰在第一缕光里受热开裂细细高高的嗒嗒声，和深深的寂静。'),
    'The frame holds the ice plain, the pressure ridges and the rising sun, nobody in the scene.',
    CM('The camera pushes forward slowly low across the ice toward the sun until the glowing horizon fills the middle third of the frame.', '镜头贴着冰面慢慢向太阳推过去，直到发光的地平线占满画面中间三分之一。'),
    AE("Pink and gold light skims across the glassy ice in long soft streaks and every pressure ridge casts a long blue shadow while the rising sun wears a faint halo.",
       "粉色和金色的光贴着玻璃般的冰面拉出长长柔和的光带，每一道冰脊都拖着长长的蓝色影子，升起的太阳带着一圈淡淡的光晕。"))

TAA('S-11', '11｜极光雪原：男主一个人走过极光下的雪原，身后一行长长的脚印，呼出的白气飘在冷空气里，镜头从侧面低低地跟着他', 10, AURORA_WALK,
    [P('lin_arctic', 'center', "walking steadily across the snow in profile facing frame-right with long even strides, his gloved hands swinging at his sides and a long line of boot prints trailing behind him", 'obj:the green aurora on the far horizon', "his lips pressed together, his eyes calm and steady, his brows level")],
    'Wide shot, the man full-length in the middle third of the frame, on the snowfield.',
    "<lin_arctic> trudges across the snowfield in long even strides, his breath streaming white and the line of boot prints growing longer behind him; the aurora ripples across the sky above him and powder snow glitters in the air. The camera tracks sideways low alongside him.",
    "林峰在雪原上迈着长长均匀的步子往前走，呼出的白气飘着，身后的那行脚印越来越长；极光在他头顶的天空里流动，空气里的粉雪闪着光。镜头从侧面低低地跟着他。",
    Q('The loud steady crunch of boots on snow, a long low sigh of wind and his slow even breathing.', '靴子踩在雪上响亮均匀的脆响、风长长低低的叹息声和他缓慢均匀的呼吸声。'),
    AE("Green and violet aurora light slides across his white suit and the glittering snow while powder crystals sparkle in the air like fine silver dust against the deep blue shadows.",
       "绿色和紫色的极光光线滑过他的白色极地服和闪光的雪面，空气里的粉雪晶体像细细的银粉一样发亮，衬着深蓝色的阴影。"),
    holds='The frame holds the man walking across the snowfield, his line of footprints and the aurora sky.',
    cam=track('him', '他'))

TAA('S-12', '12｜冰湖边：男主蹲在冰湖边，低头看着冰里冻住的一排灰色气泡，伸出手套轻轻碰了碰冰面，镜头慢慢推近', 10, LAKE_EDGE,
    [P('lin_arctic', 'center', "crouching at the edge of the shore in profile facing frame-right, one gloved hand resting flat on the dark glassy ice and his head bowed over it", 'obj:the row of grey bubbles trapped deep in the ice', "his lips slightly parted, his eyes soft and curious, his brows drawn gently together")],
    'Medium shot, the man from the head to the knees in the middle third of the frame, on the shore.',
    "<lin_arctic> crouches at the edge of the frozen lake and studies the rows of grey bubbles trapped deep in the glassy ice, then lays his gloved fingertips on the ice and slowly follows a pale crack across it; his breath clouds white over the surface.",
    "林峰在冰湖边蹲下来，看着玻璃般的冰里冻住的一排排灰色气泡，然后把戴着手套的指尖轻轻按在冰面上，慢慢顺着一道浅色的裂纹划过去；他呼出的白气在冰面上散开。",
    Q('The soft squeak of a glove on glassy ice, a slow creak deep in the lake and his quiet breathing.', '手套在玻璃般的冰面上轻轻的吱响、湖深处缓缓的吱嘎声和他安静的呼吸声。'),
    AE("Cool green aurora light lays a glow on the glassy ice and shows the grey bubbles like frozen pearls while a thin mist of breath drifts over his gloved hand.",
       "清凉的绿色极光给玻璃般的冰面铺上一层光，把灰色的气泡照得像冻住的珍珠，他呼出的薄薄白气在戴手套的手上飘着。"),
    holds='The frame holds the man crouched at the shore, the glassy ice and the trapped bubbles.',
    cam=push1('his gloved hand on the ice and the trapped bubbles', '他戴手套的手、冰面和冻住的气泡'))

TAA('S-13', '13｜山脊上：男主一个人站在山脊顶上，看着山谷里那座一盏灯都没有的城市，只有他呼出的白气在冷空气里飘，镜头缓缓向他推近', 10, RIDGE,
    [P('lin_arctic', 'center', "standing on the snowy ridge top in profile facing frame-left, his gloved hands hanging at his sides and his white hood pushed back", 'obj:the dead dark city spread across the valley below', "his lips pressed together, his eyes steady and quiet, his brows level")],
    'Wide shot, the man full-length and small in the middle third of the frame, on the ridge.',
    "<lin_arctic> stands motionless on the snowy ridge looking down at the vast dark city in the valley without a single light; his breath streams white in the cold air and a thin ribbon of mist creeps along the low streets below.",
    "林峰一动不动地站在积雪的山脊上，看着山谷里那座没有一盏灯的巨大黑色城市；他呼出的白气在冷空气里飘着，下面低处的街上一缕薄薄的雾慢慢爬过。",
    Q('A long low sigh of wind over the ridge, the faint creak of cold snow under his boots and a vast silence from the valley below.', '风吹过山脊长长低低的叹息声、他靴子下冷雪轻轻的吱嘎声，和山谷里一片辽阔的寂静。'),
    AE("A faint blue dawn glows on the horizon and rims his white suit with a thin cold line while the dark rocks hold a trace of frost and the mist below glows pale grey.",
       "天边淡淡的蓝色黎明给他的白色极地服勾上一圈细细的冷光，深色的岩石上沾着一点霜，下面的雾泛着浅灰色的光。"),
    holds='The frame holds the man standing small on the ridge, the dark rocks and the dead city below.',
    cam=push1('the man standing on the ridge', '站在山脊上的男人'))

# ================================================================================================ 补拍4D 两个人
bD = S.episode('补拍4D｜末日景色：两个人（并肩走过极光雪原、冰封森林接雪粉、游乐场碰摩天轮的霜、山脊看日出、温泉口的绿芽）',
               '男女主一起在末日景色里散步的五个切镜：他拉起她的领口并肩走、她在冰封森林里伸手接雪粉、她在冻住的游乐场里踮脚碰摩天轮上的霜、山脊上并肩看日出、温泉口融开的暖区里她蹲下摸一棵绿芽。', 80)
new_scenery(bD, 'spring_meadow', '温泉口的暖区（一圈融开的土地，湿润的黑土上有一片片鲜绿的草和小小的绿芽，围着一汪冒着白汽的清澈温泉水，四周是一圈高高的冰雪墙）',
            'A ring of thawed ground with dark wet soil, patches of vivid green grass and tiny green sprouts around a pool of clear steaming water, a high wall of snow and ice all round the edge.',
            '一圈融开的土地，湿润的黑土上有一片片鲜绿的草和小小的绿芽，围着一汪冒着白汽的清澈温泉水，四周是一圈高高的冰雪墙。',
            'the green grass, the steaming pool and the wall of snow')

TAA('S-14', '14｜极光雪原：男女主并肩走过极光下的雪原，他停下来，用戴手套的双手把她白色极地服的领口拉高盖住下巴，她抬头看着他', 10, AURORA_WALK,
    [P('lin_arctic', 'center-right', "standing in profile facing frame-left, both gloved hands pulling the white neck gaiter of Su's suit up over her chin", 'Su', "his lips pressed gently together, his eyes soft and attentive, his brows level"),
     P('su_arctic', 'center-left', "standing in profile facing frame-right, her chin lifted a little and her gloved hands hanging at her sides", 'Lin', "her lips slightly parted, her eyes warm and a little amused, her brows relaxed")],
    'Medium shot, the two of them from the head to the knees in the middle third of the frame, on the snowfield.',
    "<lin_arctic> and <su_arctic> have been walking side by side across the snowfield, their two lines of boot prints behind them; he stops, turns to her and pulls the white neck gaiter of her suit up over her chin with both gloved hands, and she tilts her face up to him while their breath mingles in a white cloud. The aurora ripples above them.",
    "林峰和苏清月一直并肩走在雪原上，身后是两行并排的脚印；他停下来，转向她，用戴着手套的双手把她极地服的白色领口拉高、盖住下巴，她仰起脸看着他，两个人呼出的白气混成一团。极光在他们头顶流动。",
    Q('The soft crunch of two pairs of boots stopping in the snow, the rustle of thick fabric, a long low sigh of wind and their quiet breathing.', '两双靴子在雪里停下来轻轻的脆响、厚厚衣料的摩擦声、风长长低低的叹息声和两个人安静的呼吸声。'),
    AE("Green and violet aurora light washes over their white suits and warms the frost on her lashes while their breath glows like silver smoke against the deep blue snow.",
       "绿色和紫色的极光光线洗过他们的白色极地服，照亮了她睫毛上的霜，两个人的白气像银色的烟一样在深蓝色的雪地前发亮。"),
    holds='The frame holds the two of them on the snowfield, their two lines of footprints and the aurora sky.',
    cam=push('the two of them', '两人'))

TAA('S-15', '15｜冰封森林：男女主走在雾凇森林的小路上，她停下来，伸出戴手套的手掌去接从树枝上落下来的雪粉，他站在旁边看着她', 10, FOREST_PATH,
    [P('su_arctic', 'center-left', "standing on the snowy path in profile facing frame-right, one gloved hand held out palm up in front of her to catch the falling snow dust", 'obj:the snow dust falling onto her gloved palm', "her lips parted in a small sweet smile, her eyes wide and bright, her brows lifted gently"),
     P('lin_arctic', 'center-right', "standing beside her in profile facing frame-left with his gloved hands hanging at his sides", 'Su', "his lips pressed gently together, his eyes soft and warm, his brows level")],
    'Medium shot, the two of them from the head to the knees in the middle third of the frame, on the forest path.',
    "<su_arctic> and <lin_arctic> walk slowly down the forest path under the frost-furred trees; she stops and holds out her gloved palm as a fine drift of snow dust falls from the branches onto it, and he stands beside her watching her face.",
    "苏清月和林峰慢慢走在挂满霜花的树下的小路上；她停下来，伸出戴手套的手掌，细细的雪粉从树枝上落到她的手心里，他站在她旁边看着她的脸。",
    Q('The slow soft crunch of snow underfoot, the tinkle of rime falling from the branches and their quiet breathing.', '脚下积雪缓缓轻轻的脆响、霜花从树枝上落下的叮当声和两个人安静的呼吸声。'),
    AE("Slanting shafts of pale gold sunlight catch the falling snow dust so every flake glitters, haloing her hair and the frost on his shoulders while the mist glows soft white.",
       "斜斜的淡金色阳光照亮了飘落的雪粉，每一片雪花都闪着光，给她的头发和他肩上的霜勾出光晕，雾泛着柔和的白色。"),
    holds='The frame holds the two of them on the forest path and the frost-furred trees.',
    cam=track('the two of them', '两人'))

TAA('S-16', '16｜冻住的游乐场：男女主走到摩天轮脚下，她踮起脚尖，伸出戴手套的手去碰挂着白霜的摩天轮钢辐条，他站在旁边看着她', 10, FAIR_WHEEL,
    [P('su_arctic', 'center-left', "standing on tiptoe at the foot of the Ferris wheel in profile facing frame-right, one gloved hand stretched up to touch a steel spoke thick with white frost", 'obj:the frost-covered steel spoke', "her lips parted in a small sweet smile, her eyes wide and bright, her brows lifted gently"),
     P('lin_arctic', 'center-right', "standing beside her in profile facing frame-left with his gloved hands in front of him", 'Su', "his lips pressed gently together, his eyes soft and warm, his brows level")],
    'Medium shot, the two of them from the head to the knees in the middle third of the frame, at the foot of the wheel.',
    "<su_arctic> and <lin_arctic> walk slowly through the deserted fair; at the foot of the Ferris wheel she rises on tiptoe and brushes a gloved fingertip along the frosted steel spoke so a line of frost falls away, and he stands beside her watching her with quiet warmth.",
    "苏清月和林峰慢慢走过空荡荡的游乐场；在摩天轮的脚下，她踮起脚尖，用戴手套的指尖划过挂满白霜的钢辐条，一道白霜被划落下来，他站在旁边安静而温柔地看着她。",
    Q('The soft crunch of boots on snow, the faint scrape of a glove on frosted steel, a long low sigh of wind through the spokes and the tick of falling ice.', '靴子踩在雪上轻轻的脆响、手套划过结霜钢铁细细的摩擦声、风吹过辐条长长低低的叹息声和冰块落下的嗒嗒声。'),
    AE("A pale dim sun hangs behind the wheel and its thick white frost glows like spun sugar while the loosed frost glitters in a thin cloud around her glove.",
       "一轮苍白暗淡的太阳挂在摩天轮后面，包着它的厚厚白霜像糖丝一样发亮，被划落的霜在她手套周围飘成一团细细闪光的雾。"),
    holds='The frame holds the two of them at the foot of the frosted wheel, the carousel and the snowy path.',
    cam=push('the two of them', '两人'))

TAA('S-17', '17｜山脊日出：男女主并肩站在山脊上，看着太阳从死城后面升起，雪和雾被染成粉金色，两个人呼出的白气在面前混在一起', 10, RIDGE_SUN,
    [P('lin_arctic', 'center-right', "standing on the snowy ridge top in profile facing frame-left, his white hood pushed back and his gloved hands hanging at his sides", 'obj:the rising sun behind the dead city', "his lips pressed gently together, his eyes steady and warm, his brows level"),
     P('su_arctic', 'center-left', "standing beside him in profile facing frame-right with her white hood pushed back and her gloved hand resting lightly in his", 'obj:the rising sun behind the dead city', "her lips parted in a small sweet smile, her eyes bright and wet, her brows relaxed")],
    'Wide shot, the two of them full-length and small in the middle third of the frame, on the ridge.',
    "<lin_arctic> and <su_arctic> stand side by side on the snowy ridge watching the dull white sun climb out from behind the frost-white towers of the dead city; the pink and gold light spreads across the snow and the mist below, and their breath rises and mingles in a white cloud.",
    "林峰和苏清月并肩站在积雪的山脊上，看着一轮暗白色的太阳从死城里霜白色的大楼后面升起来；粉色和金色的光漫过雪面和下面的雾，两个人呼出的白气升起来、混在一起。",
    Q('A long low sigh of wind over the ridge, the faint creak of snow under their boots and their slow quiet breathing.', '风吹过山脊长长低低的叹息声、他们靴子下雪轻轻的吱嘎声和两个人缓慢安静的呼吸声。'),
    AE("Pink and gold sunlight spills over the ridge and rims their white suits with warm light while the long soft shadows stretch behind them and the mist below glows rose and amber.",
       "粉色和金色的阳光漫过山脊，给他们的白色极地服勾上一圈暖光，长长柔和的影子拖在他们身后，下面的雾泛着玫瑰色和琥珀色。"),
    holds='The frame holds the two of them small on the ridge, the dead city below and the rising sun.',
    cam=push('the two of them', '两人'))

TAA('S-18', '18｜温泉口的暖区：男女主并肩走进雪墙中间融开的一圈暖地，她蹲下来，用戴手套的手指轻轻摸一棵刚冒出来的绿芽，他站在旁边看着她', 10, SPRING_WALK,
    [P('su_arctic', 'center-left', "crouching on the thawed dark soil in profile facing frame-right, one gloved fingertip gently touching a tiny green sprout", 'obj:the tiny green sprout', "her lips parted in a soft sweet smile, her eyes shining, her brows lifted gently"),
     P('lin_arctic', 'center-right', "standing beside her in profile facing frame-left with his hood pushed back and his gloved hands hanging at his sides", 'Su', "his lips pressed gently together, his eyes soft and warm, his brows level")],
    'Medium shot, the two of them from the head to the knees in the middle third of the frame, on the thawed ground.',
    "<su_arctic> and <lin_arctic> walk side by side into the ring of thawed ground between the walls of snow; she crouches and touches a gloved fingertip to a tiny green sprout while white steam drifts across them from the pool, and he stands beside her watching her with quiet warmth.",
    "苏清月和林峰并肩走进雪墙中间那一圈融开的暖地；她蹲下来，用戴手套的指尖轻轻碰一棵小小的绿芽，白色的蒸汽从温泉池面上飘过他们，他站在旁边安静而温柔地看着她。",
    Q('The soft squelch of boots on damp soil, the gentle bubbling of the spring, a low sigh of steam and their quiet breathing.', '靴子踩在湿土上轻轻的噗叽声、温泉轻柔的咕嘟声、蒸汽低低的叹息声和两个人安静的呼吸声。'),
    AE("Pale warm light falls through the drifting steam and the vivid green of the grass glows against the white walls of snow while tiny drops of water gleam on the leaves and on her gloves.",
       "淡淡的暖光穿过飘动的蒸汽，鲜绿的草在白色的雪墙前发亮，叶子上和她的手套上挂着发亮的小水珠。"),
    holds='The frame holds the two of them on the thawed ground, the steaming pool and the walls of snow.',
    cam=drop('the two of them', '两人'))

doc = S.finish()
report()
