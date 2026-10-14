"""《极寒末日》第 21 集起共用的定义（2026-10-14）：第 17–20 集（010）新增的外貌／场景／声音／运镜，从 gen_jihan_ep17_20_010.py 原样复制。011 先 `from _jihan_base5 import *`。010 生成脚本一字不动。"""
from _jihan_base4 import *


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
