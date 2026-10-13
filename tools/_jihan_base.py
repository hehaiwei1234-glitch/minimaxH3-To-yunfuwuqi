"""《极寒末日：我的隐秘安全屋》第 5 集起共用的定义（2026-10-13 夜）：风格、第 1–4 集已有的外貌／场景／声音，从 gen_jihan_ep1_4_004.py 原样复制。
追加稿（005、006、007）都先 `from _jihan_base import *`，再定义自己的新外貌／新场景／新素材。
004 生成脚本一字不动（保证 004 可重现）。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _h3draft as H
from _scene import *

H.configure(folder=os.path.join(H.ROOT, '极寒末日_隐秘安全屋'), lang='zh',
            img=("One coherent first frame from a photorealistic live-action post-apocalyptic survival drama set in modern China, ultra-wide 8:3 cinemascope composition. "
                 "Natural skin with visible pores, realistic fabric and materials. The fixed scene reference defines the place, and the character portraits define only the named people. "),
            lead="Live-action, cinematic, photorealistic with natural skin texture, naturalistic high-contrast lighting, ultra-wide 8:3 cinemascope frame. ")

STYLE = ("Photorealistic live-action post-apocalyptic survival drama set in modern-day China, with a cinematic, high-contrast look. Two clear visual worlds: "
         "the blinding white heat of a summer world that does not know what is coming, and later a warm amber-lit hidden shelter set against a silent frozen white world of snow, ice and green aurora. "
         "Every named character is Chinese. Rich natural skin texture with visible pores, realistic fabrics, restrained cinematic color grading, and an ultra-wide 8:3 cinemascope frame in which the people are placed deliberately and the room is visible around them.")

CN30 = 'a Chinese man in his early thirties'
# ---------------------------------------------------------------------------------------------- 外貌（全部写明 Chinese）
look('lin_studio', 'LinStudio', "in a rumpled white dress shirt with the sleeves rolled to his forearms and a loosened collar", 'tired but steady dark-brown', 'his', eth=CN30)
look('lin_bank', 'LinBank', "in a fitted charcoal blazer over a white open-collar shirt, his black hair neatly combed", 'steady dark-brown', 'his', eth=CN30)
look('lin_work', 'LinWork', "in a charcoal henley under a dark olive utility vest with many pockets and dark cargo pants", 'steady dark-brown', 'his', eth=CN30)
look('lin_home', 'LinHome', "in a soft grey cotton long-sleeve henley and loose dark lounge pants, barefoot, his hair damp from a shower", 'steady dark-brown', 'his', eth=CN30)
look('su_suit', 'Su', "in a fitted black silk blouse and a black pencil skirt, thin gold-rimmed glasses on her nose, her long glossy black hair falling straight over one shoulder", 'sharp dark-brown', 'her', eth='a Chinese woman in her late twenties')
look('wen_blazer', 'Wen', "in a navy blazer over a white blouse, her black hair in a neat low ponytail", 'clear dark', 'her', eth='a Chinese woman in her mid-twenties')
look('ning_partner', 'Ning', "in a grey hooded sweatshirt with a dark puffer coat draped over his shoulders", 'bleary dark', 'his', eth=CN30)
look('liang_banker', 'Liang', "in a tailored dove-grey skirt suit over a white blouse, small pearl earrings, her black hair in a neat shoulder-length bob", 'composed dark', 'her', eth='a Chinese woman in her early forties')
look('sun_agent', 'Sun', "in a short-sleeved white shirt with a loosened pale blue tie, his hair damp with sweat", 'nervous dark', 'his', eth='a Chinese man in his mid-thirties')
look('ma_outdoor', 'Ma', "in a straining red polo shirt under a canvas shop apron", 'small cheerful dark', 'his', eth='a stout Chinese man in his fifties')
look('gu_coal', 'Gu', "in a coal-streaked grey work shirt with a damp towel around his neck and a yellow hard hat", 'squinting dark', 'his', eth='a weathered, tanned Chinese man in his fifties')
look('xiao_agri', 'Xiao', "in a bright green company polo shirt under a khaki apron, her black hair in a high ponytail", 'bright eager dark', 'her', eth='a Chinese woman in her mid-twenties')
look('ranger_old', 'Ranger', "in a faded olive forestry jacket and a battered straw hat", 'deep-set dark', 'his', eth='an old Chinese man in his late sixties')
look('zhao_boss', 'Zhao', "in a sleeveless black leather vest over a sweat-stained grey t-shirt, a gold chain at his thick neck, his head shaved", 'small dark', 'his', eth='a Chinese man in his fifties')
look('biao_thug', 'Biao', "in a faded grey hoodie and a backwards baseball cap over short black hair, lean and wiry", 'restless dark', 'his', eth='a Chinese man in his twenties')

# ---------------------------------------------------------------------------------------------- 场景（开场图后缀 + 固定布局）
LIVING = Scene('bunker_living', " Warm amber light from soft recessed lamps fills the cozy underground living area.",
               " Fixed stage layout: the open kitchen with a black-and-gold stove and a marble counter is at frame-left; a thick cream wool rug and a small round wooden dining table fill the middle of the frame; a wall of small security monitors is at frame-center-right; a heavy round steel hatch door is in the right wall at the far frame-right.")
STUDIO = Scene('studio_night', " Warm amber desk-lamp light and the cool glow of two monitors fill the late-night studio while the sleepless city glitters outside the window.",
               " Fixed stage layout: the long desk with two large monitors showing a pale satellite map of an ash cloud and several orange curves falling downward is at frame-left; the worn brown leather sofa with a rumpled blanket stands at frame-right; the floor-to-ceiling window across the back wall shows a warm night city with a long line of car headlights on an elevated road and rows of lit apartment windows.")
BANK = Scene('bank_room', " Bright clear morning sunlight pours through the tall windows into the quiet, spotless private banking room.",
             " Fixed stage layout: the long walnut meeting table with a stack of thick documents and a pen stands in the middle of the frame; the floor-to-ceiling windows across the back wall show bright morning sunlight over a city skyline; a glass door is at frame-right; a potted palm stands at frame-left.")
PENT = Scene('penthouse', " Cool air-conditioned light fills the luxury penthouse while harsh white sunlight glares through the windows.",
             " Fixed stage layout: the glass dining table stands in the middle of the frame; the floor-to-ceiling windows across the back wall show a white-hot city of glass towers under a blazing sun; the white sectional sofa stands against the left wall; the wide entry hall opens at frame-right with three black tactical backpacks lined up on the floor beside it.")
OUTDOOR = Scene('outdoor_store', " Hard white summer sunlight glares through the shopfront into the cool air-conditioned outdoor-gear store.",
                " Fixed stage layout: racks of thick down parkas, ski jackets and sleeping bags fill the left wall; the checkout counter with a cash register stands at the middle-right of the frame; the broad glass shopfront at frame-right shows a white-hot summer street.")
COAL = Scene('coal_yard', " Hazy white summer sun beats down on the black coal yard, heat shimmering over the dust.",
             " Fixed stage layout: huge black mountains of anthracite fill the left half of the yard; a small brick office with a weighbridge stands at the middle-right of the frame; a yellow wheel loader is parked at frame-right; a white-hot sky fills the top of the frame.")
AGRI = Scene('agri_store', " Bright white shop light fills the neat, modern agricultural-supply showroom.",
             " Fixed stage layout: tall shelves of full-spectrum grow lamps and rows of colorful vegetable seed packets fill the left wall; the long counter stands in the middle of the frame with stacks of white foam seedling blocks, seed trays and jugs of nutrient solution on it; the glass front door at frame-right shows a hot bright street.")
YARD = Scene('freight_yard', " Hard white summer sunlight falls over the dusty gravel freight yard, heat shimmering over the trucks.",
             " Fixed stage layout: a small yard office with a rolled-up shutter is at frame-left; a row of box trucks stands along the back of the yard; stacks of wooden pallets stand at the middle-right of the frame; the open chain-link yard gate is at frame-right with a dirt road leading out of it.")
OLD = Scene('shelter_old', " Soft hazy noon light filters through tall pines onto the quiet, overgrown forest hillside.",
            " Fixed stage layout: an old concrete shelter portal overgrown with vines, its rusted steel door standing half open, is cut into the hillside at frame-left; a narrow dirt trail runs through the middle of the frame; tall pine trees fill the background and the pale sky is visible between the treetops; no vehicles.")
EMPTY = Scene('bunker_empty', " Pale flashlight beams cut through the dusty dark of the vast empty concrete hall.",
              " Fixed stage layout: a vast bare concrete hall with rusty railings on two upper levels fills the back of the frame; a shallow concrete channel of clear running water crosses the foreground from left to right; round concrete pillars stand in a row at frame-right.")
WORK = Scene('bunker_work', " Hard white work lamps cast sharp shadows across the huge concrete hall packed with supplies.",
             " Fixed stage layout: a steel workbench with a shallow tub of clear water, a stack of white foam seeding blocks and an open seed packet stands at frame-center; towering stacks of steel crates, pallets of boxes, generators and big water tanks fill the hall behind it and along both sides.")
TUNNEL = Scene('tunnel_mouth', " Hard noon light falls through tall pines onto the gravel clearing in front of the tunnel mouth.",
               " Fixed stage layout: the dark concrete tunnel mouth is cut into the forested hillside at frame-left; the gravel clearing fills the middle of the frame; a large box truck with its rear door rolled up and crates stacked at its back stands at frame-right; tall pine trees fill the background.")
HIDDEN = Scene('hill_hidden', " Hard noon light falls through tall pines onto the quiet forest hillside.",
               " Fixed stage layout: the forested hillside at frame-left holds a moss-covered boulder and a dead tree stump; the gravel clearing fills the middle of the frame; the large box truck stands at frame-right; tall pine trees fill the background.")

# ---------------------------------------------------------------------------------------------- 声音（中文普通话）
VT_EN = ' Every word is fully voiced and audible.'
VT_ZH = '每个字都正常发声、清晰可辨。'
LIN_EN = 'A mature adult male voice, calm and level with a dry cold edge, speaking clear Mandarin Chinese. He never raises his voice.' + VT_EN
LIN_ZH = '成熟成年男声，平稳镇定，带一点干冷的质感，普通话清楚。他从不提高音量。' + VT_ZH

SOUND_STUDIO = voiced('A faint electronic hum from the monitors and the low murmur of the sleeping city far below.', '显示器轻微的电子嗡鸣，和楼下沉睡的城市低低的嘈杂。')
SOUND_BANK = voiced('A quiet air-conditioned room with the soft rustle of paper and the scratch of a pen.', '安静的、开着空调的房间，纸页轻轻的沙沙声和笔尖划过的声音。')
SOUND_PENT = voiced('The faint hum of the air conditioner and the distant murmur of the city.', '空调轻微的嗡鸣和远处城市的低语。')
SOUND_STORE = voiced('A quiet air conditioner hum and the faint rattle of hangers.', '空调安静的嗡鸣和衣架轻轻的碰撞声。')
SOUND_COAL = voiced('Cicadas droning in the heat and a distant loader engine idling.', '知了在热浪里不停地叫，远处装载机发动机怠速的声音。')
SOUND_AGRI = voiced('A quiet shop with a faint air-conditioner hum.', '安静的店里有空调轻微的嗡鸣。')
SOUND_YARD = voiced('Cicadas droning in the heat, a truck engine idling and gravel shifting underfoot.', '知了在热浪里不停地叫，卡车发动机怠速，脚下的碎石沙沙响。')
SOUND_FOREST = voiced('A hushed forest with a faint breeze in the pines and no birdsong at all.', '寂静的树林，松林里有一丝轻风，一点鸟叫声都没有。')
SOUND_TUNNEL = voiced('A truck engine idling, boots on gravel and the faint breeze in the pines.', '卡车发动机怠速的声音、靴子踩在碎石上的嘎吱声和松林里的轻风。')


def push(who_en, who_zh):
    return (f'The camera pushes in slowly until {who_en} fill the middle third of the frame.', f'镜头慢慢推近，直到{who_zh}占满画面中间三分之一。')


def push1(who_en, who_zh):
    return (f'The camera pushes in slowly until {who_en} fills the middle third of the frame.', f'镜头慢慢推近，直到{who_zh}占满画面中间三分之一。')


SIDE_BANK = '炭灰西装外套，白衬衫，坐在桌边'
SIDE_WORK = '深灰亨利衫和工装背心'


SU_EN = "A confident adult woman's voice, low, smooth and slightly husky, speaking clear Mandarin Chinese with a sharp, measured edge." + VT_EN
SU_ZH = '自信的成年女声，低沉、顺滑、略带沙哑，普通话清楚，带着锐利而有分寸的质感。' + VT_ZH
CN_F28 = 'a Chinese woman in her late twenties'
BASE_004 = '合并稿/004_第1-4集_七天半价扫货山里_长任务多句自言自语插镜_制作稿.json'
