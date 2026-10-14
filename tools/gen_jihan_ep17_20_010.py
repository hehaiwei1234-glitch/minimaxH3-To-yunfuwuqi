#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 17–20 集，追加稿 010（2026-10-14）。以 009 的 JSON 为底（style／素材／角色逐字复制），必须等 009 在插件里全部跑完再追加。
hh 2026-10-14 11:11：“先写接下来的剧情，后面找机会统一重拍；17-20、21-24 四集四集更新。”

写法＝004–007 同一套，加上 10-14 的“写稿前必看”：
  · 每个任务先定景别＋机位＋运镜（升降／平移／拉／低机位上摇／推），不再整集推近；
  · 每句台词带语气，同一个任务里语气有起伏；
  · 外面的危险是这四集的主线（赵虎一伙→热成像→诱饵井→蒸汽闪冻），里面的“安全温暖”夹在中间当对比；
  · 对话任务不超过 12 秒；两人以上的任务，开场图和视频文字里都写“exactly N people”；
  · 承接前段（dep）一律不用，每个任务自己生成开场图；
  · 机械／物理变化只拍结果（格栅下的蒸汽喷发拍成“开场图是喷发前一刻”，闪冻只拍冻住之后的广场，按钮只拍按下后的样子）。
偏离大纲（交稿时已告诉 hh）：
  · 第 18 集开头“电影之夜”（投影幕布、爆米花）按 10-12 的决定删掉，改成两人盘腿坐在地毯上打牌喝热茶；
    监控画面被投到幕布上的设定不用，外面的赵虎直接拍外景（不拍屏幕里套着的屏幕）；
  · 第 19 集“喝咖啡”改成端着杯子；“四重隔热伪装”只用台词交代，不拍管道；
  · 第 20 集结尾“电影放到哪了”改成“饿了吧？煮点热的。”＋一个煮汤圆的无人插镜；
  · 暴徒：几十个→背景一群（十来个，写成清楚不虚化）；赵虎冻掉两根手指→左手缠着黑布条、只露三根手指（手部有风险）；
  · 蒸汽“100℃烫红皮肉”不拍，只拍喷发（喷发前一刻的开场图）和冻住之后的冰雕广场；“探测仪摔碎”拍成倒在雪里已碎的样子。
H3 方面的风险（交稿时单列，不算我的错）：
  · 17-02、17-04、17-05 赵虎三根手指的左手（手部）；17-05 拉发电机拉绳＋机器亮屏（机械状态变化）；背景一群发抖的暴徒；
  · 17-06 卡车外挂着很小的人影；18-04 从高处降下来的运镜（降到雪面）；18-05、19-02 一群人同时挖雪（群体动作）；
  · 19-05 手悬在按钮上方、按下去；19-06 按钮发红光（机械灯）；20-02 蒸汽冲天（快大动作，单独成 6 秒）；
  · 20-03 十几座冰雕站姿（人物冻结的静止画面）；20-04 赵虎坐在雪里（可能自己切镜）；新场景“同一个坑”用参照图（没测过）；
  · 开场图约一成不按文字画。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _jihan_base4 import *

OUT = '合并稿/010_第17-20集_猎犬热成像诱饵井蒸汽闪冻冰雕广场_制作稿_追加'
S = Session('合并稿/009_第1-16集_合并_重拍低清晰度的1-4集加后12集_制作稿_首批.json', OUT, 38000)


# ---------------------------------------------------------------------------------------------- 运镜（动作＋终点）
def lowrise(to_en, to_zh):
    return (f'The camera starts low near the ground and rises slowly in a smooth tilt up until {to_en} fill the middle third of the frame.',
            f'镜头从贴近地面的低处开始，顺滑地慢慢上摇，直到{to_zh}占满画面中间三分之一。')


def tilt(to_en, to_zh):
    return (f'The camera tilts up slowly until {to_en} fills the top of the frame.', f'镜头缓缓上摇，直到{to_zh}占满画面上方。')


# ---------------------------------------------------------------------------------------------- 新外貌
look('zhao_frost', 'ZhaoFrost', "in a filthy patchwork fur-lined coat hanging open over his black leather vest, a dirty knitted cap pulled low over his shaved head, frost clumped in his stubble, his left hand wrapped in a blackened rag with only three fingers showing", 'small hollow bloodshot', 'his', eth='a gaunt Chinese man in his fifties')
look('biao_frost', 'BiaoFrost', "in an oversized puffer jacket patched with tape and stuffed with newspaper at the seams, a dirty scarf wound up to his nose and his backwards baseball cap pulled over a knitted hat, frost on his lashes", 'restless bloodshot', 'his', eth='a wiry Chinese man in his twenties')

# ---------------------------------------------------------------------------------------------- 新场景（Scene 对象）
MARKET = Scene('ruin_market', " Dim orange glow from a dying barrel fire and cold blue night light through a broken skylight fill the frost-furred wrecked supermarket.",
               " Fixed stage layout: a dented oil barrel with a nearly dead orange fire stands in the middle of the frame; toppled empty shelves and smashed freezer cases coated in thick white frost line both sides; a long cracked checkout counter stands at frame-left; the dark smashed front windows are at frame-right.")
MARKET_OUT = Scene('ruin_front', " A frozen night under a black sky, thin snow blowing across the empty street.",
                   " Fixed stage layout: the huge wrecked supermarket fills the middle of the frame, its glass front smashed out and sheeted in thick frost with a faint orange glow flickering deep inside; a row of shopping carts half buried in snow lies in the foreground; dead streetlamps stand at both sides.")
PLOW = Scene('plow_road', " A frozen night under a black sky with a faint green aurora, white mist hanging at the far end of the boulevard.",
             " Fixed stage layout: the frozen boulevard recedes down the middle of the frame between ice-furred buildings; ice-encased cars line both sides; the heavy snowplow truck with chains wound round its huge tyres and a wide steel blade stands in the middle third of the frame with its headlights blazing and a dozen small dark figures clinging to its sides and roof.")
EDGE = Scene('forest_edge', " A black night under a faint green aurora, blowing snow in the headlight beams, the white light of the snow glows.",
             " Fixed stage layout: the heavy snowplow truck with its headlights blazing stands at frame-left at the edge of a vast snowfield; the open snowfield with a long low snow mound fills the middle of the frame; a dark wall of snow-laden pines stands along the back of the frame.")
DIG = Scene('dig_site', " A black night under a faint green aurora; the snow glares in the light of handheld lamps.",
            " Fixed stage layout: a long low snow mound and a half-dug trench cut into it fill the middle of the frame; shovels and piles of dug snow lie along the trench; snow-laden pines stand behind; the snowplow truck's headlights glow far at frame-left.")
PIT = Scene('grille_pit', " A black night under a faint green aurora; the snow glares in the light of handheld lamps.",
            " Fixed stage layout: a deep square pit dug through two metres of snow fills the middle of the frame, a large black steel grille set in the frozen ground at its bottom with a thin curl of white vapor rising through its bars; steep snow walls surround the pit; snow-laden pines stand behind the rim; the snowplow truck's headlights glow far at frame-left.")
PIT_ICE = Scene('grille_pit', " A black night under a faint green aurora; thin white vapor drifts away over the glittering snow.",
                " Fixed stage layout: the same deep square pit fills the middle of the frame, its black grille capped with a crown of clear ice; around the pit and on its rim stand a dozen ice-encased men frozen in violent poses, one with a sledgehammer raised over his head, another with his arms thrown over his face, every figure sheathed in glittering white ice; snow-laden pines stand behind; the snowplow truck's headlights glow far at frame-left.")
CARDS = Scene('bunker_living', LIVING.end,
              " Fixed stage layout: the open kitchen with a black-and-gold stove is at frame-left; a thick cream wool rug with two steaming mugs of tea and a fanned deck of playing cards lies in the middle of the frame; a wall of small security monitors showing white blizzards is at frame-center-right with a small red alarm lamp above it; the heavy round steel hatch door is in the right wall at far frame-right.")
ALARM_WALL = Scene('bunker_living', " The cozy underground room is washed in a pulsing red glow.",
                   " Fixed stage layout: the open kitchen with a black-and-gold stove is at frame-left; a thick cream wool rug with two steaming mugs of tea and scattered playing cards lies in the middle of the frame; a wall of small security monitors showing white blizzards is at frame-center-right with a small red alarm lamp above it flashing bright red; the heavy round steel hatch door is in the right wall at far frame-right.")
CONTROL_C = Scene('bunker_control', CONTROL.end, CONTROL.layout + " A black swivel chair stands in front of the console.")
CONTROL_BTN = Scene('bunker_control', " Cool green indicator glow mixes with a sudden red pulse in the compact underground control room.",
                    " Fixed stage layout: the steel control console with rows of small status lights stands in the middle of the frame; at its center the big red push-button under an open clear flip-up cover is sunk flush and ringed with pulsing red light; a wall of six small monitors is at frame-left; a large red digital clock hangs high on the back wall at center-right; a heavy steel door stands in the right wall at frame-right.")
KITCH_WARM = Scene('bunker_living', LIVING.end,
                   " Fixed stage layout: the open kitchen with a black-and-gold stove is at frame-left, a small copper pot at a gentle boil on it; a thick cream wool rug and the small round wooden dining table fill the middle of the frame, with two white bowls of round white glutinous-rice dumplings in clear sweet soup steaming on it beside two porcelain spoons; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")

# ---------------------------------------------------------------------------------------------- 声音
ZHAOF_EN = 'A heavy adult male voice, hoarse and cracked from the cold, gravelly and feverish, speaking clear Mandarin Chinese.' + VT_EN
ZHAOF_ZH = '粗重的成年男声，被寒冷冻得沙哑开裂，沙砾般粗糙而亢奋，普通话清楚。' + VT_ZH
BIAOF_EN = 'A young adult male voice, nasal and shivering, eager and afraid, speaking clear Mandarin Chinese.' + VT_EN
BIAOF_ZH = '年轻成年男声，带鼻音、发着抖，急切又害怕，普通话清楚。' + VT_ZH
SOUND_RUIN = voiced('A low howl of wind through the wrecked store, the dying crackle of a barrel fire and chattering teeth.', '风穿过破败商场的低低呼啸、火桶快熄灭时的噼啪声和牙齿打颤的声音。')
SOUND_RUIN_B = breathy('A low howl of wind through the wrecked store, the faint hum of a generator and the dying crackle of a barrel fire.', '风穿过破败商场的低低呼啸、发电机轻轻的嗡鸣和火桶快熄灭时的噼啪声。')
SOUND_RUIN_OUT = breathy('A long low howl of wind across the empty street and the faint crackle of a far fire.', '风掠过空街长长的低啸和远处火堆微弱的噼啪声。')
SOUND_GEN = voiced('The sputter and rising roar of a small petrol generator, wind and the crackle of a fire.', '小汽油发电机突突几声后越来越响的轰鸣、风声和火的噼啪声。')
SOUND_PLOW = breathy('The grinding roar of a heavy diesel engine, the clank of tyre chains and wind.', '重型柴油发动机的轰鸣、轮胎防滑链的哗啦声和风声。')
SOUND_CARD = voiced('The soft shuffle of cards, the gentle clink of mugs and a faint warm hum of the air system.', '纸牌轻轻的洗牌声、杯子轻轻的碰响和空气系统温暖的嗡鸣。')
SOUND_ALARM = breathy('A sharp repeating electronic alarm beep over a rising howl of wind outside.', '尖锐反复的电子警报声，压在外面渐渐变大的风声之上。')
SOUND_ALARM_V = voiced('A sharp repeating electronic alarm beep and the howl of wind outside.', '尖锐反复的电子警报声和外面的风声。')
SOUND_EDGE = voiced('A roaring wind, a heavy truck engine idling and the crunch of boots in snow.', '呼啸的风、重型卡车发动机的怠速声和靴子踩雪的嘎吱声。')
SOUND_DIG = breathy('The ragged scrape and chop of shovels and picks into frozen snow and harsh breaths.', '铁锹和镐头铲砍冻雪粗糙的刮擦声和粗重的喘息。')
SOUND_RUMBLE = breathy('A deep low rumble rising under the snow and a thin howl of wind.', '雪下渐渐变大的深沉低鸣和风细细的呼啸。')
SOUND_STEAM = breathy('A thunderous hiss and roar of steam and ragged screams cut short.', '蒸汽雷鸣般的嘶吼轰响和被截断的凄厉惨叫。')
SOUND_ICE = breathy('A thin howl of wind, the faint glassy tick of freezing ice and a deep hush.', '风细细的呼啸、冰层冻结时玻璃般细细的嘀嗒声和深深的寂静。')
SOUND_KITCH = breathy('The gentle bubbling of a pot and the soft hum of the air system.', '锅里轻轻的咕嘟声和空气系统轻微的嗡鸣。')


def insert_task(tid, title, dur, scene, framing, act_en, zh, snd, holds, cam, bg='', extra_assets=(), groups=()):
    return S.T(tid, title, dur, scene, [], framing, act_en, zh, snd, cam=cam, holds=holds, room={g[0] for g in groups}, groups=list(groups), new=True, bg=bg, extra_assets=extra_assets)


RAID_STEXT = "about a dozen ragged raiders in patchwork winter clothes, every face sharp and in focus"

# ================================================================================================ 第 17 集
b17 = S.episode('剧本第17集｜贪婪的猎犬', '冰封的大超市里，暴徒们围着快熄灭的火桶发抖；赵虎冻掉了两根手指，掏出那张写着林峰坐标的运单：山里有座地下宫殿；小弟推来军用热成像探测仪，能看穿五十米冻土；赵虎拉响发电机，带人开着绑满防滑链的推雪车冲进雪原。', 17)
new_person(b17, 'zhao_frost', '赵虎（冻伤后：破旧皮毛大衣、针织帽，左手缠黑布只剩三根手指）', 'man',
           'Zhao Hu, the same heavy-set Chinese man in his fifties as in the reference but gaunt now, wearing a filthy patchwork fur-lined coat hanging open over his black leather vest, a dirty knitted cap pulled low over his shaved head, frost clumped in his stubble, his left hand wrapped in a blackened rag with only three fingers showing.',
           '赵虎，和参考图是同一位五十岁左右的中国男性，但现在瘦削憔悴，穿着肮脏的拼接毛皮内衬大衣、敞开着，里面是黑色皮背心，脏针织帽压得很低盖住光头，胡茬上结着霜，左手缠着发黑的破布、只露出三根手指。',
           'gaunt, frost clumped in his stubble, wearing a filthy patchwork fur-lined coat hanging open over a black leather vest and a dirty knitted cap pulled low, his left hand wrapped in a blackened rag with only three fingers showing',
           'a feverish, greedy expression', ref='zhao_boss')
new_person(b17, 'biao_frost', '彪子（冻僵：打补丁的鼓鼓囊囊羽绒服，围巾裹到鼻子，棒球帽下压着针织帽）', 'man',
           'Biao, the same lean wiry Chinese man in his twenties as in the reference, wearing an oversized puffer jacket patched with tape and stuffed with newspaper at the seams, a dirty scarf wound up to his nose and his backwards baseball cap pulled over a knitted hat, frost on his lashes.',
           '彪子，和参考图是同一位二十多岁、瘦而精悍的中国男性，穿着打满胶带补丁、接缝处塞着报纸的肥大羽绒服，脏围巾裹到鼻子，反戴的棒球帽压在针织帽上，睫毛上有霜。',
           'wearing an oversized puffer jacket patched with tape and stuffed with newspaper at the seams, a dirty scarf wound up to his nose and his backwards baseball cap pulled over a knitted hat, frost on his lashes',
           'a shivering, anxious expression', ref='biao_thug')
b17.prop('imager', '军用地质热成像探测仪（橄榄绿金属箱，圆形黑镜头，橙蓝热感屏幕，连着小汽油发电机）',
         'A bulky olive-drab military thermal-imaging probe: a scuffed metal case on a rusty hand cart with a round black lens on a short mast, a small screen glowing with orange and blue heat colors and a thick black cable to a small petrol generator. The reference fixes its shape.',
         '一台笨重的橄榄绿军用热成像探测仪：磨损的金属箱放在生锈的手推车上，短桅杆上有一个圆形黑色镜头，一块小屏幕亮着橙蓝色热感图，一根粗黑电缆连着一台小汽油发电机。参考图固定它的外形。',
         'A photorealistic product shot of a bulky olive-drab military thermal-imaging probe: a scuffed metal case on a rusty hand cart with a round black lens on a short mast, a small screen glowing with orange and blue heat colors and a thick black cable to a small petrol generator, standing on a frosty concrete floor against a plain neutral gray background.')
new_scene(b17, 'ruin_market', '被砸烂的冰封大超市（中间一个快熄灭的火桶）',
          'The wrecked interior of a huge supermarket at night: toppled empty shelves and smashed freezer cases coated in thick white frost, a dented oil barrel with a nearly dead orange fire at the center of the frame, frost-furred walls, a long cracked checkout counter at the left and smashed dark front windows at the right.',
          '深夜被砸烂的巨大超市内部：倒塌的空货架和砸碎的冷柜上盖着厚厚的白霜，画面中间是一个快熄灭的橙色火桶，墙上长满白霜，左边是裂开的长收银台，右边是砸碎的黑漆漆的橱窗。',
          'the dying barrel fire in the middle, the frosted toppled shelves, the cracked checkout counter and the smashed windows')
new_scene(b17, 'ruin_front', '被砸烂的大超市外景（玻璃门脸碎光，里面有微弱橙光）',
          'A frozen night street in front of a huge wrecked supermarket: the glass front smashed out and sheeted in thick frost, a faint orange glow flickering deep inside, a row of shopping carts half buried in snow in the foreground, dead streetlamps at both sides.',
          '冰封的夜晚，一座巨大的被砸烂的超市门前：玻璃门脸被砸碎、盖着厚厚的白霜，深处有微弱的橙色火光在闪，前景是半埋在雪里的一排购物车，两侧是熄灭的路灯。',
          'the wrecked supermarket front with its faint orange glow, the half-buried shopping carts and the dead streetlamps')
new_scene(b17, 'plow_road', '冰封的大街上，绑满防滑链的重型推雪车开着大灯驶向远处',
          'A frozen boulevard at night between ice-furred buildings: ice-encased cars line both sides, a heavy snowplow truck with chains wound round its huge tyres and a wide steel blade stands in the middle with its headlights blazing and a dozen small dark figures clinging to its sides and roof, white mist at the far end.',
          '夜晚冰封的大街，两边是长满白霜的楼：两侧是冻在冰里的汽车，中间一辆轮胎绑满防滑链、装着宽钢铲的重型推雪车大灯亮着，车身和车顶挂着十来个很小的深色人影，远处一片白雾。',
          'the boulevard receding between ice-furred buildings, the ice-encased cars and the heavy snowplow truck with its blazing headlights')
new_scene(b17, 'forest_edge', '雪原边缘的树林：推雪车亮着大灯停在左侧',
          'A black night at the edge of a vast snowfield under a faint green aurora: a heavy snowplow truck with blazing headlights stands at the left, a long low snow mound lies in the middle of the open snowfield, a dark wall of snow-laden pines along the back.',
          '黑夜里，广阔雪原的边缘，淡淡的绿色极光下：左边停着一辆大灯亮着的重型推雪车，空旷的雪原中间有一道长长的低矮雪包，后面是一排黑压压的挂满雪的松树。',
          'the snowplow truck with its blazing headlights at the left, the long snow mound in the middle and the dark pines')
new_scene(b17, 'dig_site', '雪包上挖开了一半的壕沟（雪原边缘）',
          'A black night under a faint green aurora: a long low snow mound with a half-dug trench cut into it in the middle of the frame, shovels and piles of dug snow along the trench, snow-laden pines behind, and the truck headlights glowing far at the left.',
          '黑夜里淡淡的绿色极光下：画面中间是一道长长的低矮雪包，上面挖开了一半的壕沟，沟边是铁锹和挖出来的雪堆，后面是挂满雪的松树，远处左边亮着卡车的大灯。',
          'the long snow mound with its half-dug trench, the piles of snow and the pines')
new_scene(b17, 'grille_pit', '挖开两米深积雪后露出的方坑，坑底是一块冒着微弱白汽的黑色金属格栅',
          'A deep square pit dug through two metres of snow, a large black steel grille set in the frozen ground at its bottom with a thin curl of white vapor rising through its bars, steep snow walls around it, snow-laden pines behind the rim and the truck headlights glowing far at the left.',
          '挖穿两米积雪后露出的深深的方形大坑，坑底冻土里嵌着一块巨大的黑色钢格栅，细细一缕白汽从栅条里冒出来，四周是陡峭的雪壁，坑沿后面是挂满雪的松树，远处左边亮着卡车的大灯。',
          'the deep square pit with the black steel grille at its bottom and the steep snow walls')
b17.character('ZhaoFrost', 'zhao_frost', ZHAOF_EN, ZHAOF_ZH)
b17.character('BiaoFrost', 'biao_frost', BIAOF_EN, BIAOF_ZH)

insert_task('17-01', '01｜插镜：冰封的深夜，被砸烂的大超市，玻璃门脸碎光，深处有微弱的橙色火光', 5, MARKET_OUT,
            'Wide shot of the street in front of the wrecked supermarket, the supermarket front in the middle third of the frame, nobody in the scene.',
            "The huge supermarket stands wrecked in the frozen night, its glass front smashed out and sheeted in thick frost, a faint orange glow flickering deep inside it, thin snow blowing across the empty street and the half-buried row of shopping carts. Nothing else moves.",
            "冰封的深夜，巨大的超市被砸得稀烂，玻璃门脸碎光、盖着厚厚的白霜，深处有微弱的橙色火光在闪，细雪吹过空荡荡的街道和半埋在雪里的一排购物车。别的什么都不动。",
            SOUND_RUIN_OUT, 'The frame holds the wrecked supermarket front with its faint orange glow, the half-buried shopping carts and the dead streetlamps, and nobody in the scene.',
            descend('the smashed glass front of the supermarket with the faint orange glow inside', '超市被砸碎的门脸和里面微弱的橙色火光'))

S.T('17-02', '02｜超市里：赵虎举着运单说城里连老鼠都冻死了，山里有座地下宫殿', 10, MARKET,
    [P('zhao_frost', 'left', "standing beside the dying barrel in profile facing frame-right, holding a crumpled waybill with a hand-drawn red circle up in his bandaged left hand", 'Biao', "his lips pulled back from his teeth, his brows low in a greedy glare"),
     P('biao_frost', 'right', "standing beside him in profile facing frame-left, his shoulders hunched and his hands tucked under his armpits", 'Zhao', "his lips trembling with cold, his brows pulled up")],
    'Medium wide shot, Zhao and Biao from the head to the knees in the middle third of the frame beside the dying barrel fire.',
    "<zhao_frost> shakes the waybill and speaks the first line to <biao_frost> in a cracked bitter growl, his lips pulled back from his teeth and his brows low in a greedy glare. Then he taps the red circle with his three good fingers and speaks the second line to <biao_frost> in a rising feverish voice. <biao_frost> nods fast, his lips trembling with cold and his brows pulled up.",
    "赵虎抖着手里的运单，用沙哑苦涩的低吼对彪子说出第一句，嘴唇咧开露出牙、眉头压低、眼神贪婪凶狠。接着他用三根好手指点着那个红圈，用越来越亢奋的声音对彪子说出第二句。彪子飞快地点头，嘴唇冻得发抖、眉毛上扬。",
    SOUND_RUIN, lines=[('zhao_frost', "城里的老鼠，都冻死了。", 0.8, 'Biao'), ('zhao_frost', "可山里，有座地下宫殿！", 4.0, 'Biao')],
    cam=slide('right', '右', 'Zhao and Biao stand in the middle third of the frame with the huddled raiders behind them', '赵虎和彪子走到画面中间三分之一、身后是缩成一团的暴徒'),
    groups=[('the raiders', 'back', 'obj:the dying barrel fire')], room={'Zhao', 'Biao', 'the raiders'}, new=True,
    bg=f"Behind them, around the nearly dead barrel fire, {RAID_STEXT}, huddle shivering in torn quilts and blankets, none of them speaking.",
    holds='The frame holds exactly two named men, Zhao and Biao, in front, and about a dozen ragged raiders huddled behind the barrel, everyone sharp and in focus.')

insert_task('17-03', '03｜插镜：手推车上的军用热成像探测仪，橙蓝色的热感图在小屏幕上闪', 5, MARKET,
            'Close shot of the bulky military machine on its rusty hand cart in the middle third of the frame, the frosted wrecked store behind it, nobody in the scene.',
            "On the rusty hand cart the bulky olive-drab military thermal-imaging probe stands with its round black lens on the short mast, its small screen glowing with blotches of orange and blue heat colors and a thick black cable running to the small petrol generator beside it. Nothing else moves.",
            "生锈的手推车上，笨重的橄榄绿军用热成像探测仪立着，短桅杆上是圆形的黑色镜头，小屏幕上亮着一块块橙色和蓝色的热感图，一根粗黑电缆连到旁边的小汽油发电机。别的什么都不动。",
            SOUND_RUIN_B, 'The frame holds the machine on its hand cart with the lens and the glowing screen, the small generator and the frosted store behind, and nobody in the scene.',
            push1('the glowing heat-colored screen', '亮着热感图的小屏幕'), extra_assets=('imager',))

S.T('17-04', '04｜超市里：彪子拍着机器说能看穿五十米冻土，赵虎说他只要烧煤就藏不住', 9, MARKET,
    [P('biao_frost', 'left', "standing at the hand cart in profile facing frame-right, one hand patting the top of the machine", 'Zhao', "his eyes bright, his lips parted in eager excitement, his brows lifted"),
     P('zhao_frost', 'right', "standing across the cart in profile facing frame-left, his bandaged left hand resting on the machine's lens mast", 'Biao', "his lips curled in a slow cruel grin, his brows low")],
    'Medium two-shot, both from the head to the knees, the hand cart with the machine between them in the middle third of the frame.',
    "<biao_frost> pats the machine and speaks the first line to <zhao_frost> in a nasal eager voice, his eyes bright, his lips parted in eager excitement and his brows lifted. <zhao_frost> strokes the lens mast with his three fingers and speaks the second line to <biao_frost> in a low, satisfied growl, his lips curled in a slow cruel grin and his brows low.",
    "彪子拍着机器，用带鼻音的急切声音对赵虎说出第一句，眼睛发亮、嘴唇因兴奋微张、眉毛上扬。赵虎用三根手指摩挲着镜头桅杆，用低沉满意的低吼对彪子说出第二句，嘴角慢慢咧开一个残忍的笑弧、眉头压低。",
    SOUND_RUIN, lines=[('biao_frost', "这机器，能看穿五十米冻土。", 0.8, 'Zhao'), ('zhao_frost', "他只要烧煤，就藏不住。", 4.8, 'Biao')],
    cam=lowrise('the two faces', '两人的脸'), extra_assets=('imager',), room={'Biao', 'Zhao'}, new=True,
    bg='Between them the rusty hand cart carries the bulky military machine with its glowing heat-colored screen, and the dying barrel fire glows behind.',
    holds='The frame holds exactly two people: Biao and Zhao, with the machine on its hand cart between them.')

S.T('17-05', '05｜超市里：赵虎一把拉响发电机，大喊抄家伙，把乌龟壳挖出来', 9, MARKET,
    [P('zhao_frost', 'left', "standing at the small petrol generator in profile facing frame-right, his good right hand yanking its starter cord, an empty rusty fuel can at his feet", 'Biao', "his teeth bared, his brows low, wild-eyed"),
     P('biao_frost', 'right', "standing beside him in profile facing frame-left, one hand steadying the hand cart with the machine", 'Zhao', "his lips parted, his brows pulled up")],
    'Medium wide shot, Zhao and Biao from the head to the knees in the middle third of the frame beside the machine, the raiders at the right of the frame.',
    "<zhao_frost> yanks the starter cord and the generator catches and roars, the machine's screen flaring orange; he turns to <biao_frost> and speaks the first line to <biao_frost> in a hoarse bellowing voice, his teeth bared and his brows low, wild-eyed. He jabs his three-fingered hand toward the dark windows and speaks the second line to <biao_frost> in a cracked howl. <biao_frost> watches him, his lips parted and his brows pulled up. The raiders surge to their feet, snatching up shovels, crowbars and sledgehammers.",
    "赵虎一把拉动发电机的拉绳，发电机咳了两声轰地响起来，机器屏幕亮起橙光；他转向彪子，用嘶哑的吼声对彪子说出第一句，龇着牙、眉头压低、双眼发狂。他用三根手指的手戳向黑漆漆的窗外，用开裂的嚎叫对彪子说出第二句。彪子看着他，嘴唇微张、眉毛上扬。暴徒们一下子全站起来，抄起铁锹、撬棍和大锤。",
    SOUND_GEN, lines=[('zhao_frost', "都叫起来，抄家伙！", 3.0, 'Biao'), ('zhao_frost', "把那只乌龟壳，挖出来！", 5.2, 'Biao')],
    cam=push1('Zhao', '赵虎'), extra_assets=('imager',),
    groups=[('the raiders', 'right', 'Zhao')], room={'Zhao', 'Biao', 'the raiders'}, new=True,
    bg=f"At frame-right {RAID_STEXT}, stand around the barrel fire facing Zhao, the machine on its hand cart between Zhao and Biao.",
    holds='The frame holds exactly two named men, Zhao and Biao, at the machine, and about a dozen ragged raiders at the right, everyone sharp and in focus.')

insert_task('17-06', '06｜插镜：绑满防滑链的重型推雪车开着大灯，载着一群人驶进冰封的大街尽头', 6, PLOW,
            'Low wide shot from behind the snowplow truck at snow level, the truck in the middle third of the frame, the boulevard receding ahead.',
            "The heavy snowplow truck with chains wound round its huge tyres and a wide steel blade rumbles away down the frozen boulevard with its headlights blazing, a dozen small dark figures clinging to its sides and roof, white snow blowing up behind it between the rows of ice-encased cars toward the wall of mist at the end of the street.",
            "绑满防滑链、装着宽钢铲的重型推雪车开着大灯，轰隆隆地驶向冰封大街的尽头，车身和车顶挂着十来个很小的深色人影，车后卷起白雪，两侧是冻在冰里的汽车，远处是一堵白雾。",
            SOUND_PLOW, 'The frame holds the snowplow truck with the small figures clinging to it, the ice-encased cars and the wall of mist, and nobody else in the scene.',
            rise('the whole frozen city with the small truck far down the boulevard', '整座冰封的城市和远处大街上很小的卡车'))

# ================================================================================================ 第 18 集
b18 = S.episode('剧本第18集｜地底的警报', '安全屋里，林峰和苏清月盘腿坐在地毯上打牌喝热茶，输的人洗碗；监控墙上的红灯突然狂闪，警报尖叫；苏清月脸色发白：热成像仪，我们的热气就是黑夜里的灯；外面雪原边缘，赵虎举着探测仪指向安全屋正上方：就在这片雪下面，给我挖。', 18)

S.T('18-01', '01｜地毯上：苏清月甩出同花顺，说今晚你洗碗，林峰说行，输得起', 10, CARDS,
    [P('su_cozy', 'left', "sitting cross-legged on the rug in profile facing frame-right, laying a fan of five cards face-up on the rug with both hands", 'Lin', "her eyes sparkling, her lips curved in a cheeky sweet smile, her brows lifted"),
     P('lin_home', 'right', "sitting cross-legged on the rug in profile facing frame-left, a fan of cards held in his right hand and a steaming mug in his left", 'Su', "his jaw relaxed, one corner of his mouth lifting in a dry amused curve, his brows soft")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, sitting on the rug.',
    "<su_cozy> slaps down her cards and speaks the first line to <lin_home> in a bright triumphant voice, her eyes sparkling, her lips curved in a cheeky sweet smile and her brows lifted. <lin_home> looks at the cards, sets down his own hand and speaks the second line to <su_cozy> in a dry low voice, one corner of his mouth lifting in a dry amused curve and his brows soft. <su_cozy> leans in and speaks the third line to <lin_home> in a sweet teasing voice.",
    "苏清月啪地把牌拍在地毯上，用明快得意的声音对林峰说出第一句，眼睛发亮、嘴角带着俏皮的甜笑、眉毛上扬。林峰看了看牌，放下自己的手牌，用干干的低声对苏清月说出第二句，嘴角带着一丝觉得好笑的弧度、眉毛舒展。苏清月凑近，用甜甜带着逗弄的声音对林峰说出第三句。",
    SOUND_CARD, lines=[('su_cozy', "同花顺！今晚你洗碗。", 0.8, 'Lin'), ('lin_home', "行，我输得起。", 4.0, 'Su'), ('su_cozy', "说话要算数哦。", 6.6, 'Lin')],
    cam=slide('right', '右', 'the two of them stand in the middle third of the frame with the steaming mugs between them', '两人坐在画面中间三分之一、中间是冒着热气的杯子'),
    room={'Su', 'Lin'}, new=True,
    bg='Behind them the open kitchen glows warm at frame-left and the wall of small security monitors shows white blizzards at frame-center-right.',
    holds='The frame holds exactly two people: Su and Lin, sitting on the rug with the cards and the mugs between them.',
    st={'Su': ('奶白色毛衣，盘腿坐在地毯上', '奶白色毛衣，盘腿坐在地毯上'), 'Lin': ('灰色棉质家居服，盘腿坐在地毯上', '灰色棉质家居服，盘腿坐在地毯上')})

insert_task('18-02', '02｜插镜：监控墙上方的小红灯突然狂闪，满屏都是白茫茫的暴风雪', 4, ALARM_WALL,
            'Close shot of the wall of small security monitors and the red alarm lamp above it, the lamp in the middle third of the frame, nobody in the scene.',
            "Above the wall of small monitors, which show nothing but white blizzards, the small red alarm lamp flashes bright and fast, throwing pulses of red light across the screens and the warm room; a scattered deck of cards lies on the rug in the foreground. Nothing else moves.",
            "一排小监控的上方，那盏小红灯狂闪起来，一下一下的红光扫过满是白茫茫暴风雪的屏幕和温暖的房间；前景的地毯上散落着一副牌。别的什么都不动。",
            SOUND_ALARM, 'The frame holds the wall of monitors with the flashing red alarm lamp and the scattered cards on the rug, and nobody in the scene.',
            push1('the flashing red alarm lamp', '狂闪的红色警报灯'))

S.T('18-03', '03｜地毯边：苏清月抓紧林峰的手臂说是热成像仪，林峰冷冷看着监控说来得比我算的早', 10, ALARM_WALL,
    [P('su_cozy', 'left', "standing on the rug in profile facing frame-right, both hands gripping his right forearm, a card falling from her fingers", 'Lin', "her face drained pale, her lips trembling, her brows pulled high"),
     P('lin_home', 'right', "standing beside her in profile facing frame-left, his body still, his eyes on the flashing monitor wall", 'obj:the flashing monitor wall at frame-center-right', "his jaw tight, his lips set flat, his brows low")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, standing on the rug in the red pulsing light.',
    "<su_cozy> speaks the first line to <lin_home> in a breathless shaking voice, then the second line, her face drained pale, her lips trembling and her brows pulled high. <lin_home> does not look at her; he keeps his eyes on the flashing monitor wall and speaks the third line to <su_cozy> in a cold, flat voice, his jaw tight, his lips set flat and his brows low.",
    "苏清月用急促发抖的声音对林峰说出第一句，接着说出第二句，脸色发白、嘴唇发颤、眉毛高高皱起。林峰没有看她，眼睛一直盯着闪着红光的监控墙，用冰冷平淡的声音对苏清月说出第三句，下颌绷紧、嘴唇抿平、眉头压低。",
    SOUND_ALARM_V, lines=[('su_cozy', "是热成像仪！", 0.8, 'Lin'), ('su_cozy', "我们的热气，就是黑夜里的灯。", 2.8, 'Lin'), ('lin_home', "来得比我算的，早。", 6.4, 'Su')],
    cam=push('both of them', '两人'), room={'Su', 'Lin'}, new=True,
    bg='Behind them the open kitchen is washed in pulsing red light at frame-left and the wall of monitors with the flashing lamp is at frame-center-right.',
    holds='The frame holds exactly two people: Su and Lin, standing on the rug.',
    st={'Su': ('奶白色毛衣，站在地毯上抓着他的手臂', '奶白色毛衣，站在地毯上抓着他的手臂'), 'Lin': ('灰色棉质家居服，站在地毯上', '灰色棉质家居服，站在地毯上')})

S.T('18-04', '04｜雪原边缘：赵虎举着探测仪，指着雪包说热气就在这片雪下面，给我挖', 8, EDGE,
    [P('zhao_frost', 'left', "standing in the snow in profile facing frame-right, one hand gripping the lens mast of the machine on its hand cart, the other stabbing his three-fingered hand toward the long snow mound", 'Biao', "his teeth bared in a triumphant grimace, his brows low"),
     P('biao_frost', 'right', "standing beside the hand cart in profile facing frame-left, hunched against the wind with his hands in his sleeves", 'Zhao', "his lips parted, his brows pulled up")],
    'Medium wide shot, Zhao and Biao from the head to the knees in the middle third of the frame beside the machine on its hand cart, the long snow mound behind them.',
    "<zhao_frost> points the lens mast at the snow mound and speaks the first line to <biao_frost> in a rasping triumphant voice, his teeth bared in a triumphant grimace and his brows low, then speaks the second line to <biao_frost> in a savage bellow. <biao_frost> flinches and nods, his lips parted and his brows pulled up. Behind them the raiders jump down from the truck with shovels and crowbars.",
    "赵虎把镜头桅杆对准雪包，用沙哑得意的声音对彪子说出第一句，龇着牙露出得意的狞笑、眉头压低，接着用凶狠的吼声对彪子说出第二句。彪子缩了一下点头，嘴唇微张、眉毛上扬。他们身后，暴徒们拿着铁锹和撬棍从卡车上跳下来。",
    SOUND_EDGE, lines=[('zhao_frost', "热气，就在这片雪下面。", 0.8, 'Biao'), ('zhao_frost', "给我挖！", 4.2, 'Biao')],
    cam=descend('Zhao, Biao and the machine', '赵虎、彪子和机器'), extra_assets=('imager',),
    groups=[('the raiders', 'back', 'Zhao')], room={'Zhao', 'Biao', 'the raiders'}, new=True,
    bg=f"Behind them the snowplow truck's headlights blaze at frame-left and {RAID_STEXT}, jump down from the truck into the snow.",
    holds='The frame holds exactly two named men, Zhao and Biao, in front, and about a dozen ragged raiders behind them, everyone sharp and in focus.')

insert_task('18-05', '05｜插镜：一群暴徒疯了一样用铁锹和镐头砍挖雪包，雪块乱飞', 4, DIG,
            'Wide shot of the snow mound, the half-dug trench in the middle third of the frame, about a dozen raiders along the trench.',
            "Along the half-dug trench about a dozen ragged raiders hack and shovel at the snow mound like madmen, swinging shovels, picks and crowbars, clots of snow flying in the lamplight; every one of them is sharp and in focus. Nothing else moves.",
            "半挖开的壕沟边，十来个衣衫褴褛的暴徒像疯了一样用铁锹、镐头和撬棍砍挖着雪包，雪块在灯光里乱飞；每个人都清楚不虚化。别的什么都不动。",
            SOUND_DIG, 'The frame holds the long snow mound with its half-dug trench and about a dozen raiders working along it, all sharp and in focus.',
            track('the line of digging raiders', '挖雪的暴徒'), groups=[('the raiders', 'center', 'obj:the snow mound')])

# ================================================================================================ 第 19 集
b19 = S.episode('剧本第19集｜幽灵防线', '控制室里，苏清月手心全是汗，林峰端着杯子冷笑：那不是大门，是诱饵；外面暴徒挖开两米深的雪，露出一块冒热气的金属格栅，赵虎喊砸开；林峰的手悬在红色按钮上：喜欢热气，那就暖和个够，重重按下。', 19)

S.T('19-01', '01｜控制室：苏清月问你还笑得出来，林峰端着杯子说那不是大门，是诱饵', 8, CONTROL_C,
    [P('su_cozy', 'left', "standing at the monitor wall in profile facing frame-right, her arms wrapped tight around herself, her palms damp", 'Lin', "her face pale, her lips parted, her brows pulled together"),
     P('lin_home', 'right', "sitting back in the black swivel chair in profile facing frame-left, a steaming cup held in his right hand, his eyes on the monitor wall", 'obj:the monitor wall at frame-left', "one corner of his mouth lifting in a cold curve, his brows low")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
    "<su_cozy> speaks the first line to <lin_home> in a tight, shaking voice, her face pale, her lips parted and her brows pulled together. <lin_home> takes a slow sip from the cup without looking at her, his eyes on the monitor wall, and speaks the second line to <su_cozy> in a cold, easy voice, one corner of his mouth lifting in a cold curve and his brows low.",
    "苏清月用紧绷发抖的声音对林峰说出第一句，脸色发白、嘴唇微张、眉头拧在一起。林峰没有看她，眼睛盯着监控墙，慢慢喝了一口杯子里的东西，用冰冷从容的声音对苏清月说出第二句，嘴角带着一丝冷冷的弧度、眉头压低。",
    SOUND_CTRL, lines=[('su_cozy', "你还笑得出来？", 0.8, 'Lin'), ('lin_home', "那不是大门，是诱饵。", 3.6, 'Su')],
    cam=push1('Lin', '林峰'), room={'Su', 'Lin'}, new=True,
    bg='Behind them the steel console with its rows of green lights stands in the middle of the room and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly two people: Su and Lin, at the console.',
    st={'Su': ('奶白色毛衣，站在监控墙前', '奶白色毛衣，站在监控墙前'), 'Lin': ('灰色棉质家居服，坐在转椅里端着杯子', '灰色棉质家居服，坐在转椅里端着杯子')})

insert_task('19-02', '02｜插镜：暴徒们在雪里挖出了两米深的坑，铁锹不停地往下铲', 5, DIG,
            'Wide low shot along the trench, the deepening pit in the middle third of the frame, about a dozen raiders working around it.',
            "The trench has become a deep pit in the snow; about a dozen ragged raiders shovel and hack frantically around its rim and down its steep walls, snow flying in the lamplight; every one of them is sharp and in focus. Nothing else moves.",
            "壕沟已经挖成雪里一个很深的坑；十来个衣衫褴褛的暴徒在坑沿和陡峭的坑壁上拼命铲、砍，雪在灯光里乱飞；每个人都清楚不虚化。别的什么都不动。",
            SOUND_DIG, 'The frame holds the deepening pit in the snow and about a dozen raiders working around it, all sharp and in focus.',
            track('the digging raiders around the pit', '坑边挖雪的暴徒'), groups=[('the raiders', 'center', 'obj:the pit')])

S.T('19-03', '03｜控制室：林峰说真正的入口隔了四层，苏清月问你到底花了多少钱，林峰说刚好够活命', 9, CONTROL_C,
    [P('lin_home', 'right', "sitting in the black swivel chair in profile facing frame-left, turning the steaming cup slowly in his right hand", 'Su', "his jaw relaxed, one corner of his mouth lifting in a faint dry curve, his brows soft"),
     P('su_cozy', 'left', "standing beside the console in profile facing frame-right, her arms loosely crossed", 'Lin', "her eyes widening, her lips parted, her brows lifted")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
    "<lin_home> speaks the first line to <su_cozy> in a low even voice, his jaw relaxed, one corner of his mouth lifting in a faint dry curve and his brows soft. <su_cozy> stares at him and speaks the second line to <lin_home> in a stunned half-laughing voice, her eyes widening, her lips parted and her brows lifted. <lin_home> answers with the third line to <su_cozy> in a quiet, dry voice.",
    "林峰用低沉平稳的声音对苏清月说出第一句，下颌放松、嘴角带着一丝干干的弧度、眉毛舒展。苏清月瞪着他，用惊呆又带点想笑的声音对林峰说出第二句，眼睛睁大、嘴唇微张、眉毛上扬。林峰用安静干干的声音对苏清月答出第三句。",
    SOUND_CTRL, lines=[('lin_home', "真正的入口，隔了四层。", 0.8, 'Su'), ('su_cozy', "你到底，花了多少钱？", 3.4, 'Lin'), ('lin_home', "刚好够活命。", 6.0, 'Su')],
    cam=slide('left', '左', 'the two of them stand in the middle third of the frame', '两人占画面中间三分之一'), room={'Lin', 'Su'}, new=True,
    bg='Behind them the steel console with its rows of green lights stands in the middle of the room and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly two people: Lin and Su, at the console.',
    st={'Lin': ('灰色棉质家居服，坐在转椅里端着杯子', '灰色棉质家居服，坐在转椅里端着杯子'), 'Su': ('奶白色毛衣，站在控制台边', '奶白色毛衣，站在控制台边')})

S.T('19-04', '04｜坑里：暴徒挖到了冒白汽的黑色格栅，彪子喊挖到了，赵虎喊砸开它', 9, PIT,
    [P('biao_frost', 'left', "standing at the rim of the pit in profile facing frame-right, one arm flung out toward the grille below", 'Zhao', "his eyes wide, his lips stretched in wild excitement, his brows high"),
     P('zhao_frost', 'right', "standing at the rim beside him in profile facing frame-left, his bandaged left hand clutching the machine's cable, his good hand pointing down into the pit", 'Biao', "his eyes burning, his lips pulled back in a feverish grin, his brows low")],
    'Medium wide shot, Biao and Zhao from the head to the knees at the rim of the pit in the middle third of the frame, the grille visible in the pit below them.',
    "<biao_frost> speaks the first line to <zhao_frost> in a cracked excited shout, his eyes wide, his lips stretched in wild excitement and his brows high. <zhao_frost> grabs his shoulder and speaks the second line to <biao_frost> in a feverish roar, his eyes burning, his lips pulled back in a feverish grin and his brows low. A raider in the pit raises a sledgehammer over the grille.",
    "彪子用开裂兴奋的喊声对赵虎说出第一句，眼睛睁大、嘴唇因狂喜咧开、眉毛高扬。赵虎一把抓住他的肩膀，用亢奋的吼声对彪子说出第二句，眼睛烧红、嘴唇咧成一个狂热的笑、眉头压低。坑里一个暴徒把大锤举过了格栅。",
    SOUND_DIG, lines=[('biao_frost', "虎哥，挖到了！是大门！", 0.8, 'Zhao'), ('zhao_frost', "砸开！里面的粮全是咱们的！", 3.8, 'Biao')],
    cam=rise('Biao, Zhao, the pit and the raiders', '彪子、赵虎、深坑和暴徒'),
    groups=[('the raiders', 'back', 'obj:the black grille')], room={'Biao', 'Zhao', 'the raiders'}, new=True,
    bg=f"Below them in the pit and around its rim {RAID_STEXT}, crowd the black grille, one of them lifting a sledgehammer, a thin curl of white vapor rising between them.",
    holds='The frame holds exactly two named men, Biao and Zhao, at the rim, and about a dozen ragged raiders in and around the pit, everyone sharp and in focus.')

S.T('19-05', '05｜控制室：林峰的手悬在红色按钮上方说喜欢热气，那就暖和个够，然后按了下去', 9, CONTROL_C,
    [P('lin_home', 'center', "standing at the console in profile facing frame-right, his right hand poised over the big red push-button beneath its open clear cover, the other hand in his pocket", 'obj:the big red push-button', "his jaw tight, his lips set flat, his brows level, his eyes cold"),
     P('su_cozy', 'right', "standing beside him in profile facing frame-left, one hand pressed to her mouth", 'Lin', "her eyes wide, her lips pressed together, her brows pulled together")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, standing at the console.',
    "<lin_home> speaks one line to <su_cozy> without turning his eyes from the red button, in a quiet, silky, deadly voice, his jaw tight, his lips set flat, his brows level and his eyes cold; then his right finger presses the red button down firmly. <su_cozy> holds her breath, her eyes wide, her lips pressed together and her brows pulled together.",
    "林峰眼睛没离开红色按钮，用安静、柔滑又致命的声音对苏清月说出一句，下颌绷紧、嘴唇抿平、眉毛平直、眼神冰冷；然后他的右手食指重重按下了红色按钮。苏清月屏住呼吸，眼睛睁大、嘴唇紧抿、眉头拧在一起。",
    SOUND_CTRL, lines=[('lin_home', "喜欢热气？那就暖和个够。", 1.2, 'Su')],
    cam=push('both of them', '两人'), room={'Lin', 'Su'}, new=True,
    bg='Behind them the steel console with its rows of small lights stands in the middle of the room, the wall of six small monitors glows at frame-left and the large red digital clock hangs on the back wall.',
    holds='The frame holds exactly two people: Lin and Su, at the console.',
    st={'Lin': ('灰色棉质家居服，站在控制台前手悬在红色按钮上', '灰色棉质家居服，站在控制台前手按在红色按钮上'), 'Su': ('奶白色毛衣，站在林峰身边', '奶白色毛衣，站在林峰身边')})

insert_task('19-06', '06｜插镜：红色按钮已经沉下去，一圈红光在闪，深处传来越来越响的低鸣', 3, CONTROL_BTN,
            'Close shot of the center of the control console, the sunken red button and its ring of red light in the middle third of the frame, nobody in the scene.',
            "At the center of the steel console the big red button sits sunk flush under its open clear cover, its ring of red light pulsing, while the rows of green lights around it flicker to amber and the whole panel trembles with a deep low rumble rising from far below. Nothing else moves.",
            "钢制控制台的中心，那个大红色按钮已经沉到和面板齐平，透明保护盖敞开着，一圈红光在闪，周围一排绿灯闪成琥珀色，整块面板随着从很深的地方传来的越来越响的低鸣微微发抖。别的什么都不动。",
            SOUND_RUMBLE, 'The frame holds the sunken red button with its pulsing red ring and the flickering lights around it, and nobody in the scene.',
            push1('the sunken red button', '沉下去的红色按钮'))

# ================================================================================================ 第 20 集
b20 = S.episode('剧本第20集｜冰雕广场', '雪地里的格栅下传来雷鸣般的闷响，积雪跳动；一股高压蒸汽冲天而起，吞掉围在格栅边的暴徒；在零下八十度里蒸汽瞬间闪冻，十几座狰狞的冰雕站在坑边；赵虎一屁股坐进雪里，探测仪摔得粉碎，他喊魔鬼；控制室里林峰松开按钮：垃圾清理完了，饿了吧，煮点热的。', 20)

insert_task('20-01', '01｜插镜：格栅下面传来低鸣，积雪在格栅边微微跳动，暴徒们围着格栅蹲着、举着大锤', 5, PIT,
            'Low wide shot at snow level of the pit rim, the black grille in the middle third of the frame, about a dozen raiders crouched around it.',
            "At the bottom of the pit the powder snow on the black grille jitters and jumps as a deep rumble climbs, the thin curl of white vapor thickening between the bars, while about a dozen raiders crouch at the rim and in the pit with sledgehammers raised, looking down, every one of them sharp and in focus. Nothing else moves.",
            "坑底的黑色格栅上，粉雪随着越来越响的低鸣微微跳动，栅条之间那一缕白汽越来越浓，十来个暴徒蹲在坑沿和坑里，举着大锤低头看着，每个人都清楚不虚化。别的什么都不动。",
            SOUND_RUMBLE, 'The frame holds the black grille at the bottom of the pit and about a dozen raiders around it, all sharp and in focus.',
            push1('the black grille', '黑色格栅'), groups=[('the raiders', 'center', 'obj:the black grille')])

insert_task('20-02', '02｜插镜：高压蒸汽从格栅里冲天而起，吞掉围在坑边的暴徒', 6, PIT,
            'Low wide shot at snow level of the pit, the grille in the middle third of the frame, about a dozen raiders gathered around it a moment before the blast.',
            "A column of white steam explodes up out of the black grille with a thunderous roar, shooting high into the black sky, swallowing the raiders around the pit in a boiling white cloud as they stagger back and scream; snow and sledgehammers fly.",
            "一股白色的蒸汽带着雷鸣般的轰响从黑色格栅里冲天而起，直冲黑色的夜空，把围在坑边的暴徒吞进翻滚的白雾里，他们踉跄后退、尖叫，积雪和大锤四处飞散。",
            SOUND_STEAM, 'The frame holds the pit with the grille just starting to burst and about a dozen raiders around it, all sharp and in focus.',
            tilt('the white column of steam', '冲天的白色蒸汽柱'), groups=[('the raiders', 'center', 'obj:the black grille')])

insert_task('20-03', '03｜插镜：蒸汽散去，十几座狰狞的冰雕站在坑边，有的还举着大锤', 8, PIT_ICE,
            'Wide high shot over the pit, the pit and the ice figures in the middle third of the frame.',
            "The steam has thinned to drifting wisps and above the pit stands a ring of a dozen ice-encased men frozen in violent poses, one with a sledgehammer raised over his head, another with his arms thrown over his face, another reaching toward the sky with his mouth open in a scream, every figure sheathed in glittering white ice; a crown of clear ice caps the grille; thin vapor drifts away over the glittering snow. Nothing moves.",
            "蒸汽已经淡成飘散的几缕，坑的四周站着一圈十几座冰雕般的人影，保持着狰狞的姿势：一个把大锤举过头顶，一个双臂护着脸，一个张着嘴向天伸手，每一座都裹着闪亮的白冰；格栅上盖着一顶透明的冰冠；细细的白汽在闪光的雪地上飘散。什么都不动。",
            SOUND_ICE, 'The frame holds the pit with its crown of ice over the grille and a ring of about a dozen ice-encased figures around it.',
            descend('the ring of ice-encased men', '那一圈冰雕般的人影'), groups=[('the ice figures', 'center', 'obj:the pit')])

S.T('20-04', '04｜雪原边缘：赵虎瘫坐在雪里喊底下住的是魔鬼，彪子拉着他喊快跑', 9, EDGE,
    [P('zhao_frost', 'left', "sitting sprawled in the snow in profile facing frame-right, the machine lying smashed in pieces beside him, his bandaged hand flung out toward the far pit", 'Biao', "his mouth hanging open, his eyes bulging, his brows high"),
     P('biao_frost', 'right', "crouching beside him in profile facing frame-left, both hands pulling at Zhao's coat", 'Zhao', "his eyes wide, his lips trembling, his brows pulled high")],
    'Medium wide shot, Zhao and Biao from the head to the knees in the middle third of the frame in the snow, the dark far pit small at frame-right.',
    "<zhao_frost> speaks the first line to <biao_frost> in a cracked, shattered whisper that climbs to a shriek, his mouth hanging open, his eyes bulging and his brows high. <biao_frost> yanks at his coat and speaks the second line to <zhao_frost> in a thin terrified voice, his eyes wide, his lips trembling and his brows pulled high.",
    "赵虎用破碎的沙哑低语对彪子说出第一句，声音越说越尖，嘴巴张着、眼珠暴突、眉毛高挑。彪子使劲拽着他的大衣，用细而惊恐的声音对赵虎说出第二句，眼睛睁大、嘴唇发抖、眉毛高高皱起。",
    SOUND_EDGE, lines=[('zhao_frost', "魔鬼！底下住的，是魔鬼！", 1.0, 'Biao'), ('biao_frost', "虎哥，快跑！", 5.4, 'Zhao')],
    cam=lowrise('Zhao and Biao', '赵虎和彪子'), extra_assets=('imager',), room={'Zhao', 'Biao'}, new=True,
    bg="Behind them the snowplow truck's headlights blaze at frame-left and far at frame-right the pit stands dark with a ring of tiny white ice figures around it.",
    holds='The frame holds exactly two people: Zhao and Biao, sprawled in the snow, nobody else near them.')

S.T('20-05', '05｜控制室：林峰松开按钮，苏清月看着监控墙说不用一枪十几个人，林峰说垃圾清理完了，饿了吧', 10, CONTROL_C,
    [P('su_cozy', 'left', "standing at the monitor wall in profile facing frame-right, one hand gripping the edge of the console, her breathing quick", 'Lin', "her eyes wide, her lips parted, her face pale, her brows pulled together"),
     P('lin_home', 'right', "standing beside the console in profile facing frame-left, lifting his right hand off the red button and turning to her", 'Su', "his jaw loosening, a faint gentle curve at one corner of his mouth, his brows soft")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
    "<su_cozy> speaks the first line to <lin_home> in a shaken whisper, her eyes wide, her lips parted, her face pale and her brows pulled together. <lin_home> turns to her and speaks the second line to <su_cozy> in a quiet, offhand voice, then the third line in a warm low voice, his jaw loosening, a faint gentle curve at one corner of his mouth and his brows soft.",
    "苏清月用发颤的耳语对林峰说出第一句，眼睛睁大、嘴唇微张、脸色发白、眉头拧在一起。林峰转向她，用安静随意的声音对苏清月说出第二句，接着用温暖低沉的声音说出第三句，下颌放松、嘴角带着一丝温柔的弧度、眉毛舒展。",
    SOUND_CTRL, lines=[('su_cozy', "不用一枪，十几个人……", 1.0, 'Lin'), ('lin_home', "垃圾，清理完了。", 4.4, 'Su'), ('lin_home', "饿了吧？煮点热的。", 6.6, 'Su')],
    cam=slide('right', '右', 'the two of them stand in the middle third of the frame', '两人占画面中间三分之一'), room={'Su', 'Lin'}, new=True,
    bg='Behind them the steel console with its rows of small lights stands in the middle of the room and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly two people: Su and Lin, at the console.',
    st={'Su': ('奶白色毛衣，站在监控墙前', '奶白色毛衣，站在监控墙前'), 'Lin': ('灰色棉质家居服，站在控制台边', '灰色棉质家居服，站在控制台边')})

insert_task('20-06', '06｜插镜：暖黄灯光下，餐桌上两碗冒热气的汤圆，灶上的小铜锅轻轻地咕嘟', 5, KITCH_WARM,
            'Close shot of the round wooden dining table, two white bowls of dumplings in the middle third of the frame, nobody in the scene.',
            "Under the warm amber light two white bowls of round glutinous-rice dumplings in clear sweet soup steam on the small round wooden table beside two porcelain spoons, and on the black-and-gold stove behind them the small copper pot bubbles gently. Nothing else moves.",
            "暖黄的灯光下，小圆木桌上两只白碗里装着圆圆的汤圆，浸在清甜的汤里冒着热气，旁边是两把瓷勺，后面黑金色灶台上的小铜锅轻轻地咕嘟着。别的什么都不动。",
            SOUND_KITCH, 'The frame holds the two steaming bowls and spoons on the wooden table with the stove and copper pot behind, and nobody in the scene.',
            pull('the steaming bowls of dumplings', '冒着热气的汤圆碗', 'the whole warm kitchen and dining area', '整个温暖的厨房和餐桌区'))

doc = S.finish()
