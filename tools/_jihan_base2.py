"""《极寒末日》第 9 集起共用的定义（2026-10-13 夜）：第 5–8 集（005）新增的外貌／场景／声音，从 gen_jihan_ep5_8_005.py 原样复制。
006、007 先 `from _jihan_base2 import *`（它会先导入 _jihan_base）。005 生成脚本一字不动。"""
from _jihan_base import *

look('lin_arctic', 'LinArctic', "in a bulky pure-white polar expedition suit with the hood up, white goggles pushed up on his forehead and a white neck gaiter pulled down under his chin", 'steady dark-brown', 'his', eth=CN30)
look('su_down', 'SuDown', "in a long cream down coat zipped to the chin over her black silk blouse, thin gold-rimmed glasses on her nose, her long black hair tied back, frost on her lashes", 'sharp dark-brown', 'her', eth=CN_F28)
look('su_trek', 'SuTrek', "in layered white and black down jackets with a black scarf wound up to her chin, ski goggles pushed up on her forehead and a heavy hiking backpack on her shoulders, frost on her lashes and cheeks", 'exhausted dark-brown', 'her', eth=CN_F28)
look('gaunt_drifter', 'Gaunt', "in a layered tattered winter coat with a frost-crusted scarf pulled down under his chin", 'sunken bloodshot', 'his', eth='a gaunt Chinese man in his forties')
look('bearded_drifter', 'Bearded', "in a ragged padded jacket and a knitted cap", 'red-rimmed', 'his', eth='a stocky Chinese man in his forties')
look('brute_raider', 'Brute', "in a stained quilted coat with a ragged scarf pulled up over his nose", 'wild bloodshot', 'his', eth='a heavy-set Chinese man in his thirties')

# ---------------------------------------------------------------------------------------------- 新场景（开场图后缀 + 固定布局）
SPROUTS = Scene('bunker_sprouts', " Hard white work lamps and one soft white-purple grow lamp light the huge concrete hall packed with supplies.",
                " Fixed stage layout: a steel workbench stands at frame-center with a shallow tub of clear water and a white tray of foam seeding blocks, each topped with tiny pale-green seedlings, under a hanging white-purple grow lamp; towering stacks of steel crates, pallets of boxes, generators and big water tanks fill the hall behind it and along both sides.")
STUDIO_DAY = Scene('studio_day', " Cold grey dawn light mixes with the glow of the two monitors in the empty studio.",
                   " Fixed stage layout: the long desk with two large monitors showing orange curves falling steeply is at frame-left; the worn brown leather sofa stands at frame-center-right; a glass studio door is at frame-right beyond the sofa; the floor-to-ceiling window across the back wall shows a pale grey dawn over a quiet city.")
CONTROL = Scene('bunker_control', " Cool green indicator glow and pale work-lamp light fill the compact underground control room.",
                " Fixed stage layout: the steel control console with rows of small green status lights and one big red push-button under a clear flip-up cover stands in the middle of the frame; a wall of six small monitors is at frame-left; a large red digital countdown clock hangs high on the back wall at center-right; a heavy steel door stands in the right wall at frame-right.")
STREET = Scene('street_summer', " Blinding white midday sun glares over the glass towers while the sky at the far end of the street is swallowed by white.",
               " Fixed stage layout: a wide boulevard between glass office towers recedes down the middle of the frame; a line of stopped cars fills both lanes; leafy trees line the sidewalks; at the far end of the street a towering wall of white mist fills the sky.")
FROZEN = Scene('street_frozen', " Dim grey-blue light and a thin white mist hang over the silent frozen boulevard.",
               " Fixed stage layout: the same wide boulevard recedes down the middle of the frame; the stopped cars are encased in ice; bare frost-furred trees line the sidewalks; along the sidewalks stand people frozen mid-stride in white ice; the glass towers are furred with frost.")
CELLAR = Scene('wine_cellar', " Dim yellow light from one bulb falls on frost-furred bottles and cases in the bitterly cold stone cellar.",
               " Fixed stage layout: racks of wine bottles line the left wall; stacked cases of canned food and bottled water stand in the middle of the frame; three concrete steps rise to a heavy steel security door at frame-right; a small round thermometer hangs on the wall above the cases.")
AIRLOCK = Scene('airlock', " Hard white strip lights fall on the white-tiled airlock.",
                " Fixed stage layout: a long steel bench with two hanging white polar suits and a shelf of white goggles runs along the left wall; the bare white-tiled floor lies in the middle of the frame; a heavy round steel hatch door stands in the right wall at frame-right.")
HATCH = Scene('snow_hatch', " A silent frozen night forest under a black sky with a faint green aurora; the white light of the snow glows.",
              " Fixed stage layout: a hollow dead tree trunk with its camouflaged hatch standing open on a black passage is at frame-left; waist-deep snow fills the middle of the frame; snow-laden pines fill the background.")
VENT = Scene('snow_vent', " A silent frozen night forest under a black sky with a faint green aurora; the white light of the snow glows.",
             " Fixed stage layout: a thick steel exhaust pipe sticks out of the deep snow at frame-center-right, its mouth sealed in a heavy block of ice; deep snow fills the foreground; snow-laden pines stand behind it.")
TREK = Scene('snow_trek', " A vast frozen snowfield under a black sky with a faint green aurora; the white light of the snow glows.",
             " Fixed stage layout: a vast open snowfield fills the middle of the frame; a few leafless frozen trees stand at frame-right; far at the back a line of white ice-encased human figures frozen mid-run stands along a low ridge.")
STUMP = Scene('snow_stump', " A silent frozen forest under a black sky with a faint green aurora; the white light of the snow glows.",
              " Fixed stage layout: a snow-capped boulder is at frame-left; a dead tree stump stands at center-left with a small round dark glass lens set in its side and a thin patch of snow melting around the glass; an open snowfield fills the middle of the frame; snow-laden pines stand in the background.")



def track(who_en, who_zh):
    return (f'The camera tracks sideways slowly alongside {who_en} until {who_en} stands in the middle third of the frame.', f'镜头缓缓横移跟着{who_zh}，直到{who_zh}走到画面中间三分之一。')


SOUND_CTRL = voiced('A low electric hum from the console and the faint hiss of the air system.', '控制台低低的电流嗡鸣和空气系统轻微的嘶嘶声。')
SOUND_CELLAR = voiced('A thin whistle of wind through the cellar door and her shivering breath.', '风从酒窖门缝里钻进来的细细的呼啸和她发抖的呼吸声。')
SOUND_AIRLOCK = voiced('The low hum of the ventilation and the creak of heavy fabric.', '通风系统低低的嗡鸣和厚重衣料的摩擦声。')

