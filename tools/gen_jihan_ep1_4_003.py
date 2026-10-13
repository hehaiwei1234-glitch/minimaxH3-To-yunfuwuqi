#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 1–4 集，第一批制作稿（新建一部剧，不是追加），编号 003（2026-10-13 下午）。
取代 002（002 的第 1 集还是“气象局”旧设定；主角已改为自己开工作室的气候建模师）。

hh 2026-10-13 12:57：“先写前4集出来看看效果，现在开始一个任务15s，别拆这种碎的镜头，详细也可以的。”
故事内容来自 `剧本/末日前大纲_第1-6集_v2.md` 和 `剧本/前10集大致介绍.md`（第 1–4 集：七天／半价／扫货／山里）。

写法（规律文档 v1.9，和 002 相同）：每个任务 15 秒 = 同一个地点、同一批人、2–3 拍慢动作 + 最多 2 句话；
每个人的视线对象写进开场图；每句台词写明对谁说、对象在画面里；背景里的人写清楚不虚化；有名字的人最多 3 个；
机械变化只拍结果；画面里不出现读得出的文字；台词 ≤13 个汉字、不以人名开头；站位表程序检查。

四集的任务（共 21 个 × 15 秒 = 315 秒）：
  第 1 集 七天（5）：① 冷开场：地下安全屋里林峰切牛排，监控墙全是暴风雪，画外独白“七天前，没人信我。”
        ② 深夜工作室：林峰重跑模型后摘下眼镜，说“七天后，城里的供暖就停”，周宁说“气象台说，只是一次强寒潮”
        ③ 同一间工作室，林峰在窗边：“房子今天就卖，价格再让一成”，周宁：“房子一卖，就买不回来了”
        ④ 天亮的银行：梁经理：“您一直不肯提授信，现在全拿？”林峰：“全拿。我要修一座度假村。”
        ⑤ 同一张桌子：梁经理收文件鞠躬：“第一笔还款在半年后，记得安排”（从谨慎变殷勤）；林峰低头不动嘴，画外独白“七天后，钱是废纸，欠条也一样。”
  第 2 集 半价（5）：① 中介擦汗递合同：“半价，今天成交，您确定？”林峰：“成交。”（钩子）② 苏清月把黑卡压在合同上：“全款还让一成，你图什么？”林峰：“多买泡面和羽绒服。”
        ③ 她拿起桌上那张写满字的草稿纸：“羽绒服、煤炭、育苗灯？”“你是不是被害妄想症？”④ 林峰收起黑卡，说“说不定，能救你一命”，拎起背包走进玄关
        ⑤ 落地窗前，苏清月对助理：“去查预警数据，把酒窖给我囤满”，画外独白“他不是妄想，他知道些什么。”
  第 3 集 扫货（5）：① 户外店：“极地防寒服，一百套，全要。”老板大笑“夏天买这个？行，白菜价！”② 煤场：“无烟煤，一万吨。”老板愣住“一……一万吨？您没开玩笑吧？”
        ③ 农资公司：“生长灯、种子、营养液，全要。”销售“夏天不用补光的，先生。”→他刷卡，销售睁大眼睛鞠躬
        ④ 货运站：“这批货要送进深山，谁接？”赵虎：“我接，价钱翻三倍。”林峰点头走开 ⑤ 赵虎对彪子：“这小子有鬼，给我跟紧他。”“好嘞，虎哥！”
  第 4 集 山里（6）：① 老护林员抬头看没有鸟的天：“鸟全往南飞了，山里不对劲。”林峰：“整座山，我买了。”② 空荡荡的防空洞大厅，林峰摸地下水脉；护林员：“这荒山野洞的，你图什么呀？”林峰：“修度假村。”
        ③ 同一个大厅已经堆满货：林峰把种子压进海绵块、放进水盆（养成的起点，无台词）④ 山脚：赵虎想进洞：“我就进去看一眼，行不行？”林峰拦住：“货到这儿，钱结清，请回。”
        ⑤ 赵虎和彪子走向卡车，林峰站在洞口暗处按遥控器（无台词）⑥ 同一座山坡：入口不见了，只剩青苔岩石和枯树桩；彪子：“洞口……没了？”赵虎：“把这地方，给我记死了。”

偏离 70 集大纲（交稿时告诉 hh）：
  · 林峰不是气象局的人，是自己开工作室的气候建模师；银行场景里用“度假村”当掩护，原文“设备商还在等我付款”去掉。
  · 周宁、中介都改成当面（不用电话；只有声音的人会被读成缺人）；苏清月的“五十亿”改成“全款还让一成”。
  · 原冷开场的“白色寒流扫过街头、人影被冻住”改成“暖屋里切牛排，监控墙全是暴风雪”（不拍瞬间冻结）；这一个任务以后第 6 集可复用。
  · 扫货只拍三站（户外店／煤场／农资公司），冷链仓库的和牛龙虾不单拍，货堆满只在第 4 集拍一个宽景；货物被搬动的过程不拍。
  · 鸟群南飞改成老护林员抬头看“没有鸟的天”（不拍鸟群）；岩石合上只拍结果；红色电子钟、发电机启动、灯亮留到第 5 集。
  · 大纲里的“第 3 集：赵虎窥视”分到第 3 集结尾（跟紧他）和第 4 集（山脚被拦、记死这地方）。
左右方向（每个场景固定）：
  暖屋：厨房在左，地毯和圆桌在中间，监控墙在中右，圆形舱门在最右；工作室：长桌和两块大屏在左，皮沙发在右，落地窗在后墙；
  银行：长桌在中间，落地窗在后墙，玻璃门在右，盆栽在左；大平层：玻璃餐桌在中间，落地窗在后墙，白沙发在左，玄关和三个背包在右；
  户外店：衣架在左，收银台在中右，玻璃橱窗在右；煤场：煤山在左，砖房和地磅在中右，装载机在右；
  农资公司：灯具和种子架在左，柜台在中间，玻璃门在右；货运站：小办公室在左，卡车排在后，托盘在中右，院门在右；
  旧防空洞口：藤蔓老门洞在左，小路在中间，松树在后；空大厅：水渠从左穿到右，立柱在右；工作台：钢制台在中间，货堆在四周；
  隧道口：洞口在左，空地在中，卡车在右；同一座山坡：青苔岩石和枯树桩在左，卡车在右。
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

OUT = '合并稿/003_第1-4集_七天半价扫货山里_十五秒_制作稿'
S = Session(None, OUT, 32000, title='极寒末日：我的隐秘安全屋｜第1–4集｜七天·半价·扫货·山里', style=STYLE)

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

# ---------------------------------------------------------------------------------------------- 第 1 集（先建第一个 Batch，新素材都加在它上面）
b1 = S.episode('剧本第1集｜七天', '冷开场：外面是暴风雪，地下安全屋里林峰在切牛排。七天前，深夜的工作室里林峰算出七天后全城供暖要停，合伙人周宁不信；他决定把房子车子全卖。第二天银行里，梁经理惊讶地看着他把授信全部拿满，他说要修度假村；签完字，他心里说：七天后，钱是废纸，欠条也一样。', 1)

new_person(b1, 'lin_studio', '林峰（深夜工作室：皱巴巴的白衬衫，一脸倦意）', 'man',
           'Lin, a lean, athletic Chinese man in his early thirties with short messy black hair, a faint shadow of stubble and tired but steady dark-brown eyes, wearing a rumpled white dress shirt with the sleeves rolled to his forearms and a loosened collar.',
           '林峰，三十出头、身形精瘦结实的中国男性，黑色短发有些凌乱，下巴一层淡淡的胡茬，疲惫却沉稳的深褐色眼睛，穿着皱巴巴的白衬衫、袖子卷到小臂、领口松开。',
           'short messy black hair, a faint shadow of stubble, tired but steady dark-brown eyes, wearing a rumpled white dress shirt with the sleeves rolled to his forearms and a loosened collar',
           'a tired, steady expression', eth='Chinese')
new_person(b1, 'lin_bank', '林峰（银行里：炭灰色西装外套，白衬衫）', 'man',
           'Lin, the same lean, athletic Chinese man in his early thirties as in the reference, clean-shaven with short neatly combed black hair and steady dark-brown eyes, wearing a fitted charcoal blazer over a white open-collar shirt.',
           '林峰，和参考图是同一位三十出头、身形精瘦结实的中国男性，胡子刮得干净，黑色短发梳得整齐，沉稳的深褐色眼睛，穿着合身的炭灰色西装外套、里面是白色开领衬衫。',
           'short neatly combed black hair, clean-shaven, steady dark-brown eyes, wearing a fitted charcoal blazer over a white open-collar shirt',
           'a calm, level expression', ref='lin_studio')
new_person(b1, 'lin_work', '林峰（深灰亨利衫，橄榄绿多口袋工装背心）', 'man',
           'Lin, the same lean, athletic Chinese man in his early thirties as in the reference, with short black hair and a faint shadow of stubble, steady dark-brown eyes, wearing a charcoal henley under a dark olive utility vest with many pockets and dark cargo pants.',
           '林峰，和参考图是同一位三十出头、身形精瘦结实的中国男性，黑色短发，带一点淡淡的胡茬，沉稳的深褐色眼睛，穿着深灰色亨利衫、外面是深橄榄绿多口袋工装背心，深色工装裤。',
           'short black hair, a faint shadow of stubble, steady dark-brown eyes, wearing a charcoal henley under a dark olive utility vest with many pockets',
           'a calm, level expression', ref='lin_studio')
new_person(b1, 'lin_home', '林峰（在安全屋里：灰色棉质家居服，光脚）', 'man',
           'Lin, the same lean, athletic Chinese man in his early thirties as in the reference, with short black hair still damp from a shower, steady dark-brown eyes, wearing a soft grey cotton long-sleeve henley and loose dark lounge pants, barefoot.',
           '林峰，和参考图是同一位三十出头、身形精瘦结实的中国男性，黑色短发刚洗过还带着湿气，沉稳的深褐色眼睛，穿着柔软的灰色棉质长袖亨利衫和宽松的深色家居裤，光着脚。',
           'short black hair still damp from a shower, steady dark-brown eyes, wearing a soft grey cotton long-sleeve henley and loose dark lounge pants, barefoot',
           'a relaxed, content expression', ref='lin_studio', full=True)
new_person(b1, 'su_suit', '苏清月（黑色真丝衬衫，金丝眼镜）', 'woman',
           'Su, an elegant, strikingly beautiful Chinese woman in her late twenties with long glossy black hair falling straight over one shoulder, sharp dark-brown eyes behind thin gold-rimmed glasses, wearing a fitted black silk blouse and a black pencil skirt.',
           '苏清月，二十八岁左右、优雅而极其美丽的中国女性，乌黑的长直发光滑地垂在一边肩上，锐利的深褐色眼睛戴着细细的金丝眼镜，穿着合身的黑色真丝衬衫和黑色铅笔裙。',
           'long glossy black hair falling straight over one shoulder, sharp dark-brown eyes behind thin gold-rimmed glasses, wearing a fitted black silk blouse',
           'a composed, sharp expression', eth='Chinese')
new_person(b1, 'wen_blazer', '文助理（苏清月的助理，藏青色西装外套）', 'woman',
           'Wen, a brisk young Chinese woman in her mid-twenties with black hair in a neat low ponytail, clear dark eyes and a smooth fair face, wearing a navy blazer over a white blouse.',
           '文助理，二十五岁左右干练的年轻中国女性，黑色头发扎成利落的低马尾，清亮的深色眼睛，皮肤白净，穿着藏青色西装外套、里面是白衬衫。',
           'black hair in a neat low ponytail, clear dark eyes, a smooth fair face, wearing a navy blazer over a white blouse',
           'an attentive, alert expression', eth='Chinese')
new_person(b1, 'ning_partner', '周宁（林峰的合伙人，灰色卫衣，披着深色羽绒外套）', 'man',
           'Ning, a rumpled Chinese man in his early thirties with messy short black hair, a few days of stubble, a round tired face and bleary dark eyes, wearing a grey hooded sweatshirt with a dark puffer coat draped over his shoulders.',
           '周宁，三十出头、一脸疲态的中国男性，黑色短发凌乱，有几天没刮的胡茬，一张圆脸，睡眼惺忪的深色眼睛，穿着灰色连帽卫衣、肩上披着一件深色羽绒外套。',
           'messy short black hair, a few days of stubble, a round tired face, bleary dark eyes, wearing a grey hooded sweatshirt with a dark puffer coat draped over his shoulders',
           'a sleepy, worried expression', eth='Chinese')
new_person(b1, 'liang_banker', '梁经理（银行客户经理，浅灰色套装）', 'woman',
           'Manager Liang, a polished Chinese woman in her early forties with a neat shoulder-length black bob, composed dark eyes and a courteous bearing, wearing a tailored dove-grey skirt suit over a white blouse with small pearl earrings.',
           '梁经理，四十出头、一丝不苟的中国女性，齐肩的黑色短发整齐利落，沉着的深色眼睛，举止得体，穿着剪裁合身的浅灰色套装、里面是白衬衫，戴着小小的珍珠耳钉。',
           'a neat shoulder-length black bob, composed dark eyes, small pearl earrings, wearing a tailored dove-grey skirt suit over a white blouse',
           'a polite, composed expression', eth='Chinese')
new_person(b1, 'sun_agent', '中介小孙（短袖白衬衫，松开的浅蓝领带）', 'man',
           'Agent Sun, a nervous Chinese man in his mid-thirties with sweat-damp short black hair, a thin face and anxious dark eyes, wearing a short-sleeved white shirt with a loosened pale blue tie.',
           '中介小孙，三十五岁左右、神情紧张的中国男性，短发被汗打湿，一张瘦脸，焦虑的深色眼睛，穿着短袖白衬衫、浅蓝色领带松松地挂着。',
           'sweat-damp short black hair, a thin face, anxious dark eyes, wearing a short-sleeved white shirt with a loosened pale blue tie',
           'a sweaty, nervous expression', eth='Chinese')
new_person(b1, 'ma_outdoor', '户外店马老板（红色POLO衫，帆布围裙，光头）', 'man',
           'Boss Ma, a stout, jovial Chinese man in his fifties with a bald head shiny with sweat, a round red face and small cheerful dark eyes, wearing a straining red polo shirt under a canvas shop apron.',
           '马老板，五十多岁、矮胖爱笑的中国男性，光头上泛着汗光，一张圆圆的红脸，小而爱笑的深色眼睛，穿着绷得很紧的红色POLO衫、外面系着帆布店员围裙。',
           'a bald head shiny with sweat, a round red face, small cheerful dark eyes, wearing a straining red polo shirt under a canvas shop apron',
           'a cheerful, shrewd expression', eth='Chinese')
new_person(b1, 'gu_coal', '煤场顾老板（沾着煤灰的灰衬衫，脖子上搭毛巾，黄色安全帽）', 'man',
           'Boss Gu, a weathered Chinese man in his fifties with deeply tanned skin, a squarish coal-dusted face and squinting dark eyes, wearing a coal-streaked grey work shirt, a damp towel around his neck and a yellow hard hat.',
           '顾老板，五十多岁、饱经风霜的中国男性，皮肤晒得黝黑，方脸上沾着煤灰，眯缝着深色眼睛，穿着沾着煤灰的灰色工作衬衫、脖子上搭着一条湿毛巾、戴着黄色安全帽。',
           'deeply tanned skin, a squarish coal-dusted face, squinting dark eyes, wearing a coal-streaked grey work shirt, a damp towel around his neck and a yellow hard hat',
           'a weary, squinting expression', eth='Chinese')
new_person(b1, 'xiao_agri', '农资公司销售小肖（绿色POLO衫，卡其围裙，高马尾）', 'woman',
           'Xiao, a bright Chinese woman in her mid-twenties with her black hair in a high ponytail, a fresh round face and eager dark eyes, wearing a bright green company polo shirt under a khaki apron.',
           '小肖，二十五岁左右、爽朗的中国女性，黑色头发扎成高马尾，一张清爽的圆脸，热切的深色眼睛，穿着亮绿色公司POLO衫、外面系着卡其色围裙。',
           'her black hair in a high ponytail, a fresh round face, eager dark eyes, wearing a bright green company polo shirt under a khaki apron',
           'a bright, polite expression', eth='Chinese')
new_person(b1, 'ranger_old', '老护林员（褪色的橄榄绿护林外套，旧草帽）', 'man',
           'The old ranger, a lean Chinese man in his late sixties with a deeply weathered face, white stubble and deep-set dark eyes, wearing a faded olive forestry jacket and a battered straw hat.',
           '老护林员，六十多岁、精瘦的中国男性，一张被风吹日晒得满是沟壑的脸，下巴上是白色胡茬，深陷的深色眼睛，穿着褪色的橄榄绿护林外套、戴着一顶旧草帽。',
           'a deeply weathered face, white stubble, deep-set dark eyes, wearing a faded olive forestry jacket and a battered straw hat',
           'a dry, watchful expression', eth='Chinese')
new_person(b1, 'zhao_boss', '赵虎（物流老板，黑色皮背心，金链子）', 'man',
           'Zhao Hu, a heavy-set Chinese man in his fifties with a shaved head, a thick neck, small dark eyes and a gold chain at his neck, wearing a sleeveless black leather vest over a sweat-stained grey t-shirt.',
           '赵虎，五十岁左右、体格粗壮的中国男性，光头，脖子粗，小而黑的眼睛，脖子上戴着金链子，穿着无袖黑色皮背心、里面是被汗浸湿的灰色T恤。',
           'a shaved head, a thick neck, small dark eyes, a gold chain at his neck, wearing a sleeveless black leather vest over a sweat-stained grey t-shirt',
           'a sly, greedy expression', eth='Chinese')
new_person(b1, 'biao_thug', '彪子（赵虎的小弟，灰色连帽衫，反戴棒球帽）', 'man',
           'Biao, a lean wiry Chinese man in his twenties with a thin stubbled face and restless dark eyes, wearing a faded grey hoodie and a backwards baseball cap over short black hair.',
           '彪子，二十多岁、瘦而精悍的中国男性，一张长着胡茬的瘦脸，不安分的深色眼睛，穿着褪色的灰色连帽衫、反戴着棒球帽，帽下是黑色短发。',
           'a thin stubbled face, restless dark eyes, wearing a faded grey hoodie and a backwards baseball cap over short black hair',
           'an eager, nervous expression', eth='Chinese')

new_scene(b1, 'bunker_living', '安全屋的生活区（暖黄灯，25℃）', 'The cozy living area of an underground hideout: an open kitchen with a black-and-gold stove and a marble counter at the left, a thick cream wool rug and a small round wooden dining table in the middle, a wall of small security monitors at the center-right, a heavy round steel hatch door in the right wall, warm amber light from soft recessed lamps.',
          '地下藏身处温馨的生活区：左边是开放式厨房、黑金色炉灶和大理石台面，中间是厚厚的奶白色羊毛地毯和一张小小的圆形木餐桌，中右是一整面小监控屏墙，右墙是一扇厚重的圆形钢制舱门，柔和的嵌灯投下暖琥珀色的光。',
          'the kitchen, the rug, the dining table, the monitor wall and the hatch')
new_scene(b1, 'studio_night', '林峰的气候建模工作室（深夜）', 'A late-night climate-modeling studio in a Chinese city: a long desk with two large monitors showing a pale satellite map of a volcanic ash cloud and several orange prediction curves falling downward at the left, a worn brown leather sofa with a rumpled blanket at the right, cold coffee cups on the desk, a floor-to-ceiling window across the back wall showing a warm night cityscape with a long ribbon of car headlights on an elevated road and rows of lit apartment windows, warm amber lamp light.',
          '深夜里中国某城市的气候建模工作室：左边是一张长桌，上面两块大屏幕，显示着火山灰扩散的苍白卫星图和几条向下落的橙色预测曲线，右边是一张旧的棕色皮沙发、上面一条皱巴巴的毯子，桌上有凉掉的咖啡杯，后墙是落地窗、窗外是暖色的夜景——高架桥上一长串车灯、一排排亮着的住宅窗户，暖琥珀色的台灯光。',
          'the desk with the two monitors, the sofa and the window with the city lights')
new_scene(b1, 'bank_room', '银行的贵宾洽谈室（清晨阳光）', 'A private banking room in a Chinese city bank in bright morning sunlight: a long walnut meeting table in the middle of the room with a stack of thick documents and a pen on it, floor-to-ceiling windows across the back wall showing a sunlit skyline, a glass door in the right wall, a potted palm in the left corner, spotless and quiet.',
          '中国某城市银行清晨阳光里的贵宾洽谈室：房间中间是一张长长的胡桃木会议桌，桌上放着一摞厚厚的文件和一支笔，后墙是落地窗、窗外是阳光下的天际线，右墙是一扇玻璃门，左边角落摆着一盆盆栽，整洁安静。',
          'the walnut table, the sunlit windows, the glass door and the palm')
new_scene(b1, 'penthouse', '市中心豪华大平层（冷气很足，窗外是烈日）', 'A luxury penthouse living room in a Chinese city: a glass dining table in the middle of the room, floor-to-ceiling windows across the back wall showing a white-hot skyline of glass towers under a blazing sun, a white sectional sofa against the left wall, a wide entry hall at the right with three black tactical backpacks lined up on the floor beside it, cool air-conditioned light.',
          '中国某城市的豪华大平层客厅：房间中间是一张玻璃餐桌，后墙是落地窗、窗外是烈日下白热的玻璃幕墙天际线，左墙边是白色组合沙发，右边是宽敞的玄关、旁边地上并排放着三个黑色战术背包，冷色的空调光。',
          'the glass table, the windows, the sofa and the entry hall with the backpacks')
new_scene(b1, 'outdoor_store', '夏天的户外用品店（外面烈日）', 'A well-stocked outdoor-gear store in a Chinese city in midsummer: racks of thick down parkas, ski jackets and sleeping bags along the left wall, a checkout counter with a cash register at the middle-right, a broad glass shopfront at the right showing a white-hot summer street, cool air-conditioned light.',
          '中国某城市盛夏里货品齐全的户外用品店：左墙边是一排排厚厚的羽绒服、滑雪服和睡袋，中右是带收银机的收银台，右边是宽大的玻璃橱窗、窗外是白热的夏日街道，冷色的空调光。',
          'the parka racks, the checkout counter and the sunlit shopfront')
new_scene(b1, 'coal_yard', '夏天的煤场（热浪）', 'A coal yard on the outskirts of a Chinese city in midsummer: huge black mountains of anthracite filling the left half of the yard, a small brick office with a weighbridge at the middle-right, a yellow wheel loader parked at the right, hazy white sun and heat shimmering over the coal dust.',
          '盛夏里中国某城市郊外的煤场：左半边是巨大的黑色无烟煤山，中右是带地磅的小砖房，右边停着一辆黄色轮式装载机，白晃晃的太阳，热浪在煤灰上方抖动。',
          'the coal mountains, the brick office and the loader')
new_scene(b1, 'agri_store', '农资公司的展厅', 'A neat, modern agricultural-supply showroom in a Chinese city: tall shelves of full-spectrum grow lamps and rows of colorful vegetable seed packets along the left wall, a long counter in the middle with stacks of white foam seedling blocks, seed trays and jugs of nutrient solution on it, a glass front door at the right showing a hot bright street, bright white shop light.',
          '中国某城市整洁现代的农资公司展厅：左墙边是高高的全光谱生长灯货架和一排排五颜六色的蔬菜种子，中间是一条长柜台、台面上堆着白色海绵育苗块、育苗盘和一桶桶营养液，右边是玻璃大门、门外是炎热明亮的街道，明亮的白色店内灯光。',
          'the grow-lamp shelves, the seed packets, the counter and the glass door')
new_scene(b1, 'freight_yard', '货运站（碎石院子，卡车排成一排）', 'A dusty gravel freight yard of a trucking company in midsummer: a small yard office with a rolled-up shutter at the left, a row of box trucks along the back, stacks of wooden pallets at the middle-right, an open chain-link yard gate at the right with a dirt road leading out of it, hard white sunlight and heat shimmering.',
          '盛夏里一家货运公司尘土飞扬的碎石货运站：左边是卷帘门拉起的小办公室，后面一排厢式卡车，中右是几摞木托盘，右边是敞开的铁丝网院门、门外一条土路，白花花的硬光，热浪抖动。',
          'the office, the row of trucks, the pallets and the open gate')
new_scene(b1, 'shelter_old', '深山里的旧防空洞口（老铁门半开）', 'A quiet overgrown forest hillside in China: an old concrete shelter portal covered in vines with a rusted steel door standing half open, cut into the hillside at the left, a narrow dirt trail through the middle, tall pine trees all around and a pale hazy sky between the treetops, no vehicles, soft hazy noon light.',
          '中国深山里安静而杂草丛生的树林山坡：左边山坡上有一个爬满藤蔓的旧混凝土防空洞口、生锈的铁门半开着，中间是一条窄窄的土路，四周是高高的松树、树梢之间露出苍白朦胧的天空，没有车，柔和朦胧的正午光。',
          'the old shelter portal, the trail, the pines and the pale sky')
new_scene(b1, 'bunker_empty', '空荡荡的防空洞大厅（地下水渠）', 'A vast empty three-storey concrete hall of an abandoned civil-defense shelter: bare walls, rusty railings along two upper levels at the back, a shallow concrete channel of clear running water crossing the foreground from left to right, a row of round concrete pillars at the right, dust hanging in pale flashlight beams.',
          '废弃防空洞里巨大而空荡荡的三层混凝土大厅：墙面光秃秃的，后面两层楼的生锈栏杆，一条浅浅的混凝土水渠、清澈的水从前景左边流向右边，右边是一排圆形混凝土立柱，灰尘悬在苍白的手电光束里。',
          'the bare hall, the water channel and the pillars')
new_scene(b1, 'bunker_work', '堆满货的防空洞大厅里的工作台', 'A steel workbench in a vast underground concrete hall packed with supplies: the bench at the center with a shallow tub of clear water, a stack of white foam seeding blocks and an open seed packet on it, towering stacks of steel crates, pallets of boxes, generators and big water tanks filling the hall behind it and along both sides, hard white work lamps overhead.',
          '堆满物资的巨大地下混凝土大厅里的一张钢制工作台：台子在中间，上面放着一盆清水、一摞白色海绵育苗块和一包打开的种子，后面和两侧是高高的钢箱、成托盘的货箱、发电机和巨大的水箱，头顶是白色的硬质工作灯。',
          'the workbench with the water tub, and the stacked supplies behind it')
new_scene(b1, 'tunnel_mouth', '深山里的隧道口（同一处旧防空洞，铁门大开，卡车在右）', 'The same forested mountain hillside in summer as in the reference image: the old concrete shelter portal covered in vines with its rusted steel door swung wide open on a black interior, cut into the hillside at the left, a gravel clearing in the middle, a large box truck with its rear door rolled up and crates stacked at its back at the right, tall pine trees all around, hard noon light.',
          '和参考图是同一座夏天的深山树林山坡：左边山坡上是那个爬满藤蔓的旧混凝土防空洞口、生锈的铁门大开着露出黑洞洞的里面，中间是一片碎石空地，右边停着一辆后门卷起、后面堆着箱子的大型厢式卡车，四周是高高的松树，正午的硬光。',
          'the open dark portal, the gravel clearing, the box truck and the pines')
new_scene(b1, 'hill_hidden', '同一座山坡（入口已被伪装，只剩青苔岩石和枯树桩，卡车还在右边）', 'The same forested mountain hillside in summer as in the reference image, now with no tunnel mouth: a moss-covered boulder and a dead tree stump sit on the slope at the left where the tunnel mouth was, a gravel clearing in the middle, the same large box truck still standing at the right, tall pine trees all around, hard noon light.',
          '和参考图是同一座夏天的深山树林山坡，只是隧道口不见了：左边坡上原本是隧道口的位置现在是一块长满青苔的岩石和一截枯树桩，中间是碎石空地，右边还是那辆大型厢式卡车，四周是高高的松树，正午的硬光。',
          'the boulder, the stump, the clearing, the truck and the pines')
# 三处“同一个地方”用参照图（没测过：风险是旧图里的特征盖过新状态）
for _a in b1.d['assets']:
    if _a['key'] == 'tunnel_mouth': _a['generate']['reference_keys'] = ['shelter_old']
    if _a['key'] == 'hill_hidden': _a['generate']['reference_keys'] = ['tunnel_mouth']

# ---------------------------------------------------------------------------------------------- 声音（中文普通话）
VT_EN = ' Every word is fully voiced and audible.'
VT_ZH = '每个字都正常发声、清晰可辨。'
LIN_EN = 'A mature adult male voice, calm and level with a dry cold edge, speaking clear Mandarin Chinese. He never raises his voice.' + VT_EN
LIN_ZH = '成熟成年男声，平稳镇定，带一点干冷的质感，普通话清楚。他从不提高音量。' + VT_ZH
for nm, key in (('LinStudio', 'lin_studio'), ('LinBank', 'lin_bank'), ('LinWork', 'lin_work'), ('LinHome', 'lin_home')):
    b1.character(nm, key, LIN_EN, LIN_ZH)
b1.character('Su', 'su_suit', "A confident adult woman's voice, low, smooth and slightly husky, speaking clear Mandarin Chinese with a sharp, measured edge." + VT_EN,
             '自信的成年女声，低沉、顺滑、略带沙哑，普通话清楚，带着锐利而有分寸的质感。' + VT_ZH)
b1.character('Wen', 'wen_blazer', "A young adult woman's voice, brisk and attentive, speaking clear Mandarin Chinese." + VT_EN, '年轻成年女声，干练、专注，普通话清楚。' + VT_ZH)
b1.character('Ning', 'ning_partner', 'A young adult male voice, hoarse and weary, speaking clear Mandarin Chinese.' + VT_EN, '年轻成年男声，沙哑、疲惫，普通话清楚。' + VT_ZH)
b1.character('Liang', 'liang_banker', "A mature adult woman's voice, polished, courteous and precise, speaking clear Mandarin Chinese." + VT_EN, '成熟成年女声，圆润、有礼貌、吐字精准，普通话清楚。' + VT_ZH)
b1.character('Sun', 'sun_agent', 'A young adult male voice, thin and anxious, speaking clear Mandarin Chinese.' + VT_EN, '年轻成年男声，发细、焦虑，普通话清楚。' + VT_ZH)
b1.character('Ma', 'ma_outdoor', 'A heavy adult male voice, loud and jovial, speaking clear Mandarin Chinese.' + VT_EN, '浑厚的成年男声，嗓门大、爱笑，普通话清楚。' + VT_ZH)
b1.character('Gu', 'gu_coal', 'A gravelly adult male voice, hoarse from coal dust and slow, speaking clear Mandarin Chinese.' + VT_EN, '沙哑的成年男声，被煤灰熏得嘶哑、语速慢，普通话清楚。' + VT_ZH)
b1.character('Xiao', 'xiao_agri', "A young adult woman's voice, bright, polite and eager, speaking clear Mandarin Chinese." + VT_EN, '年轻成年女声，明亮、礼貌、热切，普通话清楚。' + VT_ZH)
b1.character('Ranger', 'ranger_old', 'An old adult male voice, dry, slow and raspy, speaking clear Mandarin Chinese.' + VT_EN, '年老的成年男声，干涩、缓慢、嘶哑，普通话清楚。' + VT_ZH)
b1.character('Zhao', 'zhao_boss', 'A heavy adult male voice, gravelly and smug, speaking clear Mandarin Chinese.' + VT_EN, '粗重的成年男声，沙砾般粗糙、得意，普通话清楚。' + VT_ZH)
b1.character('Biao', 'biao_thug', 'A young adult male voice, nasal and eager, speaking clear Mandarin Chinese.' + VT_EN, '年轻成年男声，带鼻音、急切，普通话清楚。' + VT_ZH)

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

# ---- 第 1 集
S.T('01-01', '01｜冷开场：地下安全屋里林峰切牛排，监控墙全是暴风雪，一句内心独白', 15, LIVING,
    [P('lin_home', 'center', "seated at the small round dining table seen from behind in a three-quarter back view, a knife and fork in his hands over a thick steak, a glass of red wine beside the plate", 'obj:the wall of security monitors at frame-right', "his jaw relaxed, his lips closed, his brows soft")],
    'Medium shot, the figure from the head to the waist, in the middle third of the frame, at the dining table.',
    "<lin_home> slowly cuts a slice from the thick steak with the knife and fork, his bare feet on the cream rug, then lifts his eyes to the wall of monitors where a white blizzard rages on every screen, then lifts the wine glass a little and holds it, his jaw relaxed, his lips closed and his brows soft. The line is his inner voice-over, heard over the scene while his lips stay closed and do not move.",
    "林峰慢慢用刀叉切下厚牛排的一片，光脚踩在奶白色的地毯上，然后抬眼看向监控墙——每块屏幕里都是呼啸的白色暴风雪，然后他把红酒杯微微举起、停住，下颌放松、嘴唇闭着、眉毛舒展。那句台词是他的内心独白，在画面上方响起，他的嘴唇一直闭着、一动不动。",
    voiced('Butter and meat sizzling faintly, a low howl of wind from the monitor speakers and the quiet hum of the air system, with only his calm inner voice-over spoken.', '黄油和牛排轻轻的滋滋声、监控喇叭里低低的风的呼啸和空气系统安静的嗡鸣，只有他平静的内心独白在说话。'),
    cam=push('Lin and the monitor wall', '林峰和监控墙'),
    bg='On the wall of security monitors at frame-right every screen shows a white blizzard raging over a buried, silent street.',
    holds='The frame holds Lin alone at the dining table and the monitor wall.', room={'Lin'}, new=True, vo=[('lin_home', "七天前，没人信我。", 3.0, 'Lin')],
    st={'Lin': ('灰色棉质家居服，光脚，坐在圆桌边', '灰色棉质家居服，光脚，坐在圆桌边')})

S.T('01-02', '02｜深夜工作室：林峰重跑模型后摘下眼镜，说七天后供暖就停，周宁不信', 15, STUDIO,
    [P('lin_studio', 'center', "standing beside the long desk in profile facing frame-left, one hand resting on the keyboard", 'obj:the orange curves on the monitors at frame-left', "his jaw set, his brows pulled low", extra='thin black-framed glasses on his nose'),
     P('ning_partner', 'right', "half-lying on the leather sofa in profile facing frame-left, propped on one elbow with the puffer coat draped over his shoulders", 'Lin', "his lips parted, his brows pulled together")],
    'Medium-wide shot, both men from the head to the knees, in the middle third of the frame, in the late-night studio.',
    "<lin_studio> stands at the desk with his eyes on the monitors where the orange curves fall steeply and match the earlier ones almost line for line, then slowly takes off his glasses, then turns his head about 45 degrees toward <ning_partner> and speaks the first line to <ning_partner> in a low flat voice, his jaw set and his brows pulled low. <ning_partner> sits up on the sofa with the coat sliding down one shoulder and speaks the second line to <lin_studio> in a hoarse, doubtful voice, his lips pressed and his brows pulled together.",
    "林峰站在桌边，眼睛盯着显示器——橙色的曲线陡直下落，几乎和之前那几条一条线一条线地重合，然后他慢慢摘下眼镜，然后把头转向周宁约四十五度，用低沉平淡的声音对周宁说出第一句，下颌绷紧、眉头压低。周宁从沙发上坐起来，外套从一边肩膀滑下去，用沙哑而怀疑的声音对林峰说出第二句，嘴唇抿着、眉头拧在一起。",
    SOUND_STUDIO,
    lines=[('lin_studio', "七天后，城里的供暖就停。", 2.0, 'Ning'), ('ning_partner', "气象台说，只是一次强寒潮。", 6.5, 'Lin')],
    holds='The frame holds Lin at the desk with the monitors and Ning on the sofa.', room={'Lin', 'Ning'}, new=True,
    st={'Lin': ('皱巴巴的白衬衫，戴着眼镜', '皱巴巴的白衬衫，眼镜摘下拿在手里'), 'Ning': ('外套披在肩上，半躺在沙发上', '外套披在肩上，坐直在沙发上')})

S.T('01-03', '03｜同一间工作室，林峰在窗边说房子今天就卖，周宁劝他想清楚', 15, STUDIO,
    [P('lin_studio', 'center', "standing at the floor-to-ceiling window in a three-quarter back view, his right hand in his pocket", 'obj:the glittering street far below the window', "his jaw set, his brows level", extra='a pair of thin black-framed glasses held in his left hand'),
     P('ning_partner', 'right', "sitting forward on the leather sofa in profile facing frame-left, his elbows on his knees and the puffer coat draped over his shoulders", 'Lin', "his lips parted, his brows pulled together")],
    'Medium-wide shot, both men from the head to the knees, in the middle third of the frame, in the late-night studio.',
    "<lin_studio> looks down through the window at the glittering street far below, then turns his head toward <ning_partner> and speaks the first line to <ning_partner> in a flat steady voice, his jaw set and his brows level. <ning_partner> sits bolt upright on the sofa and speaks the second line to <lin_studio> in an alarmed voice, his lips parted and his brows pulled together.",
    "林峰站在落地窗前，低头看着楼下闪着灯光的街道，然后把头转向周宁，用平淡稳当的声音对周宁说出第一句，下颌绷紧、眉毛平直。周宁在沙发上一下子坐直，用惊惶的声音对林峰说出第二句，嘴唇微张、眉头拧在一起。",
    SOUND_STUDIO,
    lines=[('lin_studio', "房子今天就卖，价格再让一成。", 2.0, 'Ning'), ('ning_partner', "房子一卖，就买不回来了。", 6.5, 'Lin')],
    holds='The frame holds Lin at the window and Ning on the sofa.',
    st={'Lin': ('皱巴巴的白衬衫，眼镜摘下拿在手里', '皱巴巴的白衬衫，眼镜摘下拿在手里'), 'Ning': ('外套披在肩上，坐直在沙发上', '外套披在肩上，坐直在沙发上')})

S.T('01-04', '04｜天亮的银行：梁经理翻着厚厚的资产文件，问他是不是全拿，林峰说要修度假村', 15, BANK,
    [P('lin_bank', 'left', "seated at the walnut table in profile facing frame-right, a pen in his right hand", 'Liang', "his lips set flat, his brows level"),
     P('liang_banker', 'right', "seated at the walnut table in profile facing frame-left, flipping through a thick stack of documents with one hand", 'Lin', "her lips parted, her brows raised")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the bank room.',
    "<liang_banker> flips through the thick stack of documents, her brows rising higher with every page, then looks up and speaks the first line to <lin_bank> in a cautious, surprised voice, her lips parted and her brows raised. <lin_bank> speaks the second line to <liang_banker> in a calm even voice, his eyes steady on her, his lips set flat and his brows level, and begins to sign the first page.",
    "梁经理翻着那一大摞厚厚的文件，眉毛随着每一页越挑越高，然后抬起头，用谨慎而吃惊的声音对林峰说出第一句，嘴唇微张、眉毛高挑。林峰用平静稳当的声音对梁经理说出第二句，眼睛稳稳看着她，嘴唇抿平、眉毛平直，同时开始在第一页上签字。",
    SOUND_BANK,
    lines=[('liang_banker', "您一直不肯提授信，现在全拿？", 1.5, 'Lin'), ('lin_bank', "全拿。我要修一座度假村。", 6.5, 'Liang')],
    bg='On the walnut table between them lie the thick stack of documents and a pen, and the sunlit windows behind them glare with the bright morning skyline.',
    holds='The frame holds Lin and Liang, the walnut table with the documents and the sunlit windows behind them.', room={'Lin', 'Liang'}, new=True,
    st={'Lin': (SIDE_BANK, SIDE_BANK), 'Liang': ('灰色西装，坐在桌边', '灰色西装，坐在桌边')})

S.T('01-05', '05｜同一张桌子：梁经理收好文件鞠躬，林峰低头不动嘴，一句内心独白', 15, BANK,
    [P('lin_bank', 'left', "seated at the walnut table in profile facing frame-right, rubbing his right wrist with his left hand, the signed pages spread in front of him", 'obj:the signed pages on the table in front of him', "his jaw relaxed, his lips closed, his brows soft"),
     P('liang_banker', 'right', "seated at the walnut table in profile facing frame-left, squaring the signed pages into a folder", 'Lin', "her lips curved in an eager pleased curve, her brows lifted")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the bank room.',
    "<liang_banker> squares the signed pages into a folder, stands up with it held in both hands and speaks the line to <lin_bank> in a warm, eager voice, her lips curved in an eager pleased curve and her brows lifted, and gives him a small respectful bow. <lin_bank> rubs his sore wrist and keeps his eyes on the signed pages in front of him, his jaw relaxed, his lips closed and his brows soft. The second line is his inner voice-over, heard over the scene while his lips stay closed and do not move.",
    "梁经理把签好的文件一页页理齐放进文件夹，站起来，双手捧着它，用热情殷勤的声音对林峰说出那句话，嘴角带着殷勤满意的弧度、眉毛上扬，并对他微微欠身致意。林峰揉着发酸的手腕，眼睛一直看着面前签好的文件，下颌放松、嘴唇闭着、眉毛舒展。第二句台词是他的内心独白，在画面上方响起，他的嘴唇一直闭着、一动不动。",
    voiced('A quiet air-conditioned room with the soft rustle of paper, and only his calm inner voice-over spoken after her line.', '安静的、开着空调的房间，纸页轻轻的沙沙声；她说完之后，只有他平静的内心独白在说话。'),
    lines=[('liang_banker', "第一笔还款在半年后，记得安排。", 1.5, 'Lin')], vo=[('lin_bank', "七天后，钱是废纸，欠条也一样。", 7.0, 'Lin')], dep=True,
    bg='On the walnut table in front of Lin lie the signed pages, and the sunlit windows behind them glare with the bright morning skyline.',
    holds='The frame holds Lin and Liang, the walnut table with the signed pages and the sunlit windows behind them.',
    st={'Lin': (SIDE_BANK, SIDE_BANK), 'Liang': ('灰色西装，坐在桌边', '灰色西装，站着，抱着文件夹')})

# ---------------------------------------------------------------------------------------------- 第 2 集
b2 = S.episode('剧本第2集｜半价', '中介擦着汗递来合同：半价，今天成交；林峰说成交，签字时看都没看。买家苏清月全款、黑卡压在合同上，问他图什么，他答：多买泡面和羽绒服。她拿起桌上那张写满字的草稿纸，问他是不是被害妄想。他收起黑卡，说一句“说不定，能救你一命”，拎起背包走出玄关。苏清月站在落地窗前，让助理查预警数据、把酒窖囤满，心里说：他不是妄想，他知道些什么。', 2)

S.T('02-01', '01｜大平层：中介擦着汗递合同，林峰看都不看就签字', 15, PENT,
    [P('sun_agent', 'left', "standing at the left end of the glass table in profile facing frame-right, a tablet tucked under one arm and a damp handkerchief pressed to his forehead", 'Lin', "his lips tight, his brows knitted nervously"),
     P('lin_bank', 'right', "standing at the right end of the glass table in profile facing frame-left, one hand in his trouser pocket", 'Sun', "his lips set in a calm flat line, his brows level")],
    'Medium two-shot, both men from the head to the knees, in the middle third of the frame, in the penthouse living room.',
    "<sun_agent> mops his forehead with the handkerchief, slides the thick contract across the glass table toward <lin_bank> and speaks the first line to <lin_bank> in a hurried, nervous voice, his lips tight and his brows knitted nervously. <lin_bank> picks up the pen and speaks the second line to <sun_agent> in a calm voice, then signs the last page without reading it, his lips set in a calm flat line and his brows level. <sun_agent> stares at him with his mouth hanging open, his brows knitted nervously.",
    "中介小孙用手帕擦着额头，把厚厚的合同沿玻璃桌推到林峰面前，用急促紧张的声音对林峰说出第一句，嘴唇绷着、眉头紧张地拧着。林峰拿起笔，用平静的声音对小孙说出第二句，然后连看都没看就在最后一页上签了字，嘴唇抿成平静的一条线，眉毛平直。小孙张着嘴盯着他，眉头紧张地拧着。",
    SOUND_PENT,
    lines=[('sun_agent', "半价，今天成交，您确定？", 1.0, 'Lin'), ('lin_bank', "成交。", 5.5, 'Sun')],
    bg='On the glass table between them lie a thick contract and a pen, and the floor-to-ceiling windows behind them glare with the white-hot city.',
    holds='The frame holds Sun and Lin, the glass table with the contract and the windows behind them.', room={'Sun', 'Lin'}, new=True,
    st={'Sun': ('白衬衫，松开的领带，夹着平板', '白衬衫，松开的领带，夹着平板'), 'Lin': ('炭灰西装外套，白衬衫', '炭灰西装外套，白衬衫')})

S.T('02-02', '02｜苏清月把黑卡压在合同上，问林峰图什么，林峰答非所问', 15, PENT,
    [P('su_suit', 'left', "seated at the glass table in profile facing frame-right, a black bank card lying under her fingertips on the signed contract", 'Lin', "one brow arched, her lips pressed in a thin sharp line"),
     P('lin_bank', 'right', "standing across the table in profile facing frame-left, one hand in his trouser pocket", 'Su', "his lips set flat, his brows level")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the penthouse living room.',
    "<su_suit> slides the black card forward with one fingertip across the signed contract and speaks the first line to <lin_bank> in a sharp, amused voice, one brow arched and her lips pressed in a thin sharp line. <lin_bank> looks down at the card, then lifts his eyes to her and speaks the second line to <su_suit> in a calm flat voice, his lips set flat and his brows level, and glances once at the crumpled sheet beside the contract. <su_suit> follows his glance to the sheet, her eyes narrowing and her lips pressed in a thin sharp line.",
    "苏清月用一根手指把黑卡沿着签好的合同向前推，用锐利带笑意的声音对林峰说出第一句，一边眉毛挑起，嘴唇抿成一条细而锐利的线。林峰低头看了看卡，然后抬起眼睛看着她，用平静淡然的声音对苏清月说出第二句，嘴唇抿平、眉毛平直，并朝合同旁那张皱巴巴的纸扫了一眼。苏清月顺着他的目光看向那张纸，眼睛眯起，嘴唇抿成一条细而锐利的线。",
    SOUND_PENT,
    lines=[('su_suit', "全款还让一成，你图什么？", 1.2, 'Lin'), ('lin_bank', "多买泡面和羽绒服。", 6.0, 'Su')],
    bg='On the glass table between them lie the signed contract with the black card and a crumpled sheet of paper covered in dense handwritten lines, and the floor-to-ceiling windows behind them glare with the white-hot city.',
    holds='The frame holds Su and Lin, the glass table with the contract, the black card and the crumpled sheet, and the windows behind them.', room={'Lin', 'Su', 'Wen'}, new=True,
    st={'Su': ('黑色真丝衬衫，坐在玻璃桌边，黑卡压在合同上', '黑色真丝衬衫，坐在玻璃桌边，黑卡推到桌中间'), 'Lin': ('炭灰西装外套，白衬衫', '炭灰西装外套，白衬衫')})

S.T('02-03', '03｜苏清月拿起草稿纸念出上面的字，问林峰是不是被害妄想症', 15, PENT,
    [P('su_suit', 'left', "seated at the glass table in profile facing frame-right, holding the crumpled sheet of paper up in both hands", 'obj:the dense handwritten lines on the sheet', "one brow arched, her lips pressed in a thin sharp line"),
     P('lin_bank', 'right', "standing across the table in profile facing frame-left, one hand in his trouser pocket", 'Su', "a faint knowing smirk at one corner of his mouth, his brows level")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the penthouse living room.',
    "<su_suit> scans the dense handwritten lines on the sheet, speaks the first line to <lin_bank> in a disbelieving voice, then lowers the sheet and speaks the second line to <lin_bank> in a cutting voice, one brow arched and her lips pressed in a thin sharp line. <lin_bank> stands unmoved with his eyes on her, a faint knowing smirk at one corner of his mouth and his brows level, and takes the sheet back from her fingers.",
    "苏清月扫视着那张纸上密密麻麻的手写字，用难以置信的声音对林峰说出第一句，然后放下纸，用刻薄的声音对林峰说出第二句，一边眉毛挑起，嘴唇抿成一条细而锐利的线。林峰纹丝不动地站着，眼睛看着她，嘴角挂着一丝意味深长的冷笑，眉毛平直，最后从她的手指间把那张纸拿了回去。",
    SOUND_PENT,
    lines=[('su_suit', "羽绒服、煤炭、育苗灯？", 1.0, 'Lin'), ('su_suit', "你是不是被害妄想症？", 5.0, 'Lin')], dep=True,
    bg='On the glass table beside her lie the signed contract and the black card, and the floor-to-ceiling windows behind them glare with the white-hot city.',
    holds='The frame holds Su and Lin, the glass table with the contract and the card, and the windows behind them.',
    st={'Su': ('黑色真丝衬衫，坐在玻璃桌边，黑卡推到桌中间', '黑色真丝衬衫，坐在玻璃桌边，手空着'), 'Lin': ('炭灰西装外套，白衬衫', '炭灰西装外套，白衬衫，草稿纸在手里')})

S.T('02-04', '04｜林峰收起黑卡，留下一句话，拎起背包走进玄关', 15, PENT,
    [P('su_suit', 'left', "seated at the glass table in profile facing frame-right with her hands empty on the table", 'Lin', "her eyes narrowed, her lips pressed in a thin sharp line"),
     P('lin_bank', 'center', "standing beside the table in profile facing frame-left, the folded sheet in his left hand", 'Su', "a faint knowing smirk at one corner of his mouth, his brows level")],
    'Medium-wide shot, both from the head to the knees, in the middle third of the frame, in the penthouse living room.',
    "<lin_bank> tucks the folded sheet into his pocket, picks up the black card from the table and speaks the line to <su_suit> in a quiet, almost gentle voice, a faint knowing smirk at one corner of his mouth and his brows level, then picks up a black backpack from beside the entry hall and carries it away through the entry hall at frame-right until the hall is empty. <su_suit> watches him go, her eyes narrowed and her lips pressed in a thin sharp line.",
    "林峰把折好的纸塞进口袋，从桌上拿起那张黑卡，用安静、近乎温和的声音对苏清月说出那句话，嘴角挂着一丝意味深长的冷笑，眉毛平直，然后从玄关边拎起一个黑色背包，拿着它穿过画面右边的玄关继续往里走，直到玄关里空无一人。苏清月目送他离开，眼睛眯起，嘴唇抿成一条细而锐利的线。",
    voiced('The faint hum of the air conditioner and soft receding footsteps on the floor.', '空调轻微的嗡鸣和渐渐远去的轻轻脚步声。'),
    lines=[('lin_bank', "说不定，能救你一命。", 1.5, 'Su')], dep=True, exit={'Lin'},
    bg='The three black tactical backpacks stand lined up beside the entry hall at frame-right, and the floor-to-ceiling windows behind the table glare with the white-hot city.',
    holds='The frame holds Su and Lin, the glass table, the entry hall with the backpacks and the windows behind them.',
    st={'Su': ('黑色真丝衬衫，坐在玻璃桌边，手空着', '黑色真丝衬衫，坐在玻璃桌边，手空着'), 'Lin': ('炭灰西装外套，白衬衫，草稿纸在手里', None)})

S.T('02-05', '05｜落地窗前：苏清月让助理查预警数据、把酒窖囤满，一句内心独白', 15, PENT,
    [P('wen_blazer', 'left', "standing beside Su in profile facing frame-right, the tablet hugged to her chest", 'Su', "her brows lifted, her lips pressed together"),
     P('su_suit', 'center', "standing at the floor-to-ceiling window in profile facing frame-right with her arms folded", 'obj:the blazing sun in the window at frame-right', "her eyes narrowed, her lips pressed in a thin line")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in front of the floor-to-ceiling window.',
    "<su_suit> stands at the window with her arms folded and speaks the first line to <wen_blazer> in a low, firm voice, her eyes narrowed and her lips pressed in a thin line. <wen_blazer> listens and nods once, her eyes on Su, her brows lifted and her lips pressed together, while <su_suit> turns her eyes to the blazing sun in the window and holds still, her jaw set and her lips closed. The second line is her inner voice-over, heard over the scene while her lips stay closed and do not move.",
    "苏清月抱着双臂站在窗前，用低沉而坚定的声音对文助理说出第一句，眼睛眯起，嘴唇抿成一条细线。文助理听着，点了一下头，眼睛看着苏清月，眉毛上提，嘴唇抿紧；同时苏清月把目光转向窗里那轮烈日，一动不动，下颌绷紧，嘴唇闭着。第二句台词是她的内心独白，在画面上方响起，她的嘴唇一直闭着、一动不动。",
    voiced('The faint hum of the air conditioner and the distant murmur of the city, and only her low inner voice-over spoken after her line.', '空调轻微的嗡鸣和远处城市的低语；她说完那句话之后，只有她低沉的内心独白在说话。'),
    lines=[('su_suit', "去查预警数据，把酒窖给我囤满。", 1.0, 'Wen')], vo=[('su_suit', "他不是妄想，他知道些什么。", 6.5, 'Su')],
    cam=push1('Su', '苏清月'), bg='Behind them the floor-to-ceiling window glares with the white-hot city, the blazing sun hanging in the glass at frame-right.',
    holds='The frame holds Wen and Su in front of the glaring window.', room={'Su', 'Wen'}, new=True,
    st={'Su': ('黑色真丝衬衫，站在落地窗前', '黑色真丝衬衫，站在落地窗前'), 'Wen': ('藏青西装外套，站在她旁边', '藏青西装外套，站在她旁边')})

# ---------------------------------------------------------------------------------------------- 第 3 集
b3 = S.episode('剧本第3集｜扫货', '夏天，林峰开始扫货：户外店里他要一百套极地防寒服，老板笑他是傻子；煤场里他要一万吨无烟煤，老板愣住；农资公司里他把生长灯、种子、营养液全要，销售劝他夏天不用补光，他刷卡，她睁大眼睛鞠躬。货太多，没有车队肯往深山送，货运站的老板赵虎开价三倍，林峰一口答应；他走后，赵虎对小弟彪子说：这小子有鬼，给我跟紧他。', 3)

S.T('03-01', '01｜户外店：林峰要一百套极地防寒服，老板笑他是傻子', 15, OUTDOOR,
    [P('lin_work', 'left', "standing at the parka rack in profile facing frame-right, one hand gripping a heavy polar parka by its hanger", 'Ma', "his lips set flat, his brows level"),
     P('ma_outdoor', 'right', "standing behind the checkout counter in profile facing frame-left, both palms flat on the counter", 'Lin', "his mouth hanging open in a loose grin, his brows lifted")],
    'Medium two-shot, both men from the head to the waist, in the middle third of the frame, in the outdoor-gear store.',
    "<lin_work> lifts the heavy polar parka off the rack and speaks the first line to <ma_outdoor> in a flat, level voice, his lips set flat and his brows level. <ma_outdoor> bursts into loud laughter, slaps the counter and speaks the second line to <lin_work> in a hearty, mocking voice, his mouth wide open and his brows lifted, then pulls a calculator toward himself, still chuckling.",
    "林峰把那件厚重的极地防寒服从衣架上取下来，用平淡的声音对马老板说出第一句，嘴唇抿平、眉毛平直。马老板放声大笑，拍着柜台，用洪亮带嘲弄的声音对林峰说出第二句，嘴巴大张、眉毛上挑，然后把计算器拉到自己面前，还在笑个不停。",
    SOUND_STORE,
    lines=[('lin_work', "极地防寒服，一百套，全要。", 1.0, 'Ma'), ('ma_outdoor', "夏天买这个？行，白菜价！", 5.5, 'Lin')],
    bg='Behind Lin the rack is packed with thick down parkas, and the glass shopfront at frame-right glares with the white-hot summer street.',
    holds='The frame holds Lin and Ma, the parka rack and the checkout counter.', room={'Lin', 'Ma'}, new=True,
    st={'Lin': (SIDE_WORK, SIDE_WORK), 'Ma': ('红色POLO衫和帆布围裙', '红色POLO衫和帆布围裙')})

S.T('03-02', '02｜煤场：林峰要一万吨无烟煤，老板愣住', 15, COAL,
    [P('lin_work', 'left', "standing at the foot of a black coal mountain in profile facing frame-right, one arm sweeping out toward the coal", 'Gu', "his lips set flat, his brows level"),
     P('gu_coal', 'right', "standing in front of the brick office in profile facing frame-left, the damp towel in his hand", 'Lin', "his mouth hanging open, his brows shot up")],
    'Medium two-shot, both men from the head to the knees, in the middle third of the frame, in the coal yard.',
    "<lin_work> gestures at the black mountains of coal with one arm and speaks the first line to <gu_coal> in a flat, level voice, his lips set flat and his brows level. <gu_coal> freezes with the towel halfway to his face and stares at <lin_work>, his mouth hanging open and his brows shot up, then speaks the second line to <lin_work> in a hoarse, disbelieving voice.",
    "林峰用一只手臂朝那些黑色的煤山比划了一下，用平淡的声音对顾老板说出第一句，嘴唇抿平、眉毛平直。顾老板举着毛巾僵在半空，盯着林峰，嘴巴张开、眉毛高高挑起，然后用沙哑而难以置信的声音对林峰说出第二句。",
    SOUND_COAL,
    lines=[('lin_work', "无烟煤，一万吨。", 1.0, 'Gu'), ('gu_coal', "一……一万吨？您没开玩笑吧？", 5.0, 'Lin')],
    bg='Behind Lin the huge black mountains of anthracite fill the left half of the yard, and the yellow wheel loader stands at frame-right.',
    holds='The frame holds Lin and Gu, the coal mountains and the brick office.', room={'Lin', 'Gu'}, new=True,
    st={'Lin': (SIDE_WORK, SIDE_WORK), 'Gu': ('沾着煤灰的灰衬衫，黄色安全帽，毛巾在手里', '沾着煤灰的灰衬衫，黄色安全帽，毛巾在手里')})

S.T('03-03', '03｜农资公司：林峰要生长灯、种子、营养液，销售劝他夏天不用补光，他刷卡，她鞠躬', 15, AGRI,
    [P('lin_work', 'left', "standing at the counter in profile facing frame-right, one palm laid flat on a stack of grow-lamp boxes", 'Xiao', "his lips set flat, his brows level"),
     P('xiao_agri', 'right', "standing behind the counter in profile facing frame-left, a seed packet in her hand", 'Lin', "her head tilted, her lips pressed in a polite puzzled line, her brows pulled together")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the agricultural-supply showroom.',
    "<lin_work> speaks the first line to <xiao_agri> in a level voice, his hand flat on the stack of grow-lamp boxes, his lips set flat and his brows level. <xiao_agri> speaks the second line to <lin_work> in a polite, puzzled voice, her head tilted, her lips pressed in a polite puzzled line and her brows pulled together. <lin_work> lays a slim black bank card on the counter; <xiao_agri> looks at the card and her eyes widen, her mouth falling open, and she bows deeply.",
    "林峰一只手按在那摞生长灯的箱子上，用平淡的声音对小肖说出第一句，嘴唇抿平、眉毛平直。小肖歪着头，用礼貌而困惑的声音对林峰说出第二句，嘴唇抿成礼貌而困惑的一条线，眉头拧在一起。林峰把一张细长的黑色银行卡放在柜台上；小肖看着那张卡，眼睛睁大、嘴巴张开，然后深深鞠了一躬。",
    SOUND_AGRI,
    lines=[('lin_work', "生长灯、种子、营养液，全要。", 1.0, 'Xiao'), ('xiao_agri', "夏天不用补光的，先生。", 5.5, 'Lin')],
    bg='On the counter between them stand stacks of white foam seedling blocks, seed trays and jugs of nutrient solution, and behind them the shelves are full of grow lamps and colorful seed packets.',
    holds='The frame holds Lin and Xiao, the counter with the seedling blocks and nutrient jugs, and the shelves behind them.', room={'Lin', 'Xiao'}, new=True,
    st={'Lin': (SIDE_WORK, SIDE_WORK), 'Xiao': ('绿色POLO衫和卡其围裙', '绿色POLO衫和卡其围裙')})

S.T('03-04', '04｜货运站：林峰问谁肯往深山送货，赵虎开价三倍，林峰点头走开', 15, YARD,
    [P('lin_work', 'left', "standing on the gravel in profile facing frame-right, his hands at his sides", 'Zhao', "his lips set flat, his brows level"),
     P('zhao_boss', 'right', "standing in front of the line of trucks in profile facing frame-left, a cigarette hanging from the corner of his mouth, one thick hand scratching his shaved head", 'Lin', "a greedy sly leer on his lips, his brows lifted")],
    'Medium two-shot, both men from the head to the knees, in the middle third of the frame, in the freight yard.',
    "<lin_work> speaks the first line to <zhao_boss> in a level voice, his eyes steady on Zhao, his lips set flat and his brows level. <zhao_boss> looks him up and down, takes the cigarette from his lips, holds up three thick fingers and speaks the second line to <lin_work> in a gravelly, greedy voice, a greedy sly leer on his lips and his brows lifted. <lin_work> gives one slow nod and walks away toward the yard gate at frame-right until he is out of sight, his lips set flat and his brows level.",
    "林峰用平淡的声音对赵虎说出第一句，眼睛稳稳看着赵虎，嘴唇抿平、眉毛平直。赵虎上下打量着他，把烟从嘴里拿下来，竖起三根粗手指，用沙哑而贪婪的声音对林峰说出第二句，嘴唇挂着狡猾贪婪的邪笑，眉毛上挑。林峰慢慢点了一下头，朝画面右边的院门走去，直到走出视线，嘴唇抿平、眉毛平直。",
    SOUND_YARD,
    lines=[('lin_work', "这批货要送进深山，谁接？", 1.0, 'Zhao'), ('zhao_boss', "我接，价钱翻三倍。", 5.5, 'Lin')], exit={'Lin'},
    bg='Behind them a row of box trucks stands along the back of the yard, and the open yard gate is at frame-right.',
    holds='The frame holds Lin and Zhao, the row of trucks and the open yard gate.', room={'Lin', 'Zhao'}, new=True,
    st={'Lin': (SIDE_WORK, None), 'Zhao': ('黑色皮背心，叼着烟，站在卡车前', '黑色皮背心，香烟夹在手指间')})

S.T('03-05', '05｜赵虎看着空荡荡的院门，对彪子说这小子有鬼，让他跟紧', 15, YARD,
    [P('zhao_boss', 'left', "standing at the center-left of the yard in profile facing frame-right, his arms folded over his chest, a cigarette held between two thick fingers", 'obj:the empty yard gate at frame-right where the dust is still settling', "a sly greedy leer on his lips, his brows lifted"),
     P('biao_thug', 'center', "standing beside Zhao in profile facing frame-left, his hands in his hoodie pocket", 'Zhao', "his lips parted, his brows pulled up")],
    'Medium two-shot, both men from the head to the knees, in the middle third of the frame, in the freight yard.',
    "<zhao_boss> watches the open yard gate where the dust is still settling, takes a slow drag on the cigarette, then turns his head toward <biao_thug> and speaks the first line to <biao_thug> in a low, sly voice, a sly greedy leer on his lips and his brows lifted. <biao_thug> nods eagerly with his eyes on Zhao and speaks the second line to <zhao_boss> in a quick, eager voice, his lips parted and his brows pulled up.",
    "赵虎看着敞开的院门，门外的尘土还没落定，他慢慢吸了一口烟，然后把头转向彪子，用低沉狡猾的声音对彪子说出第一句，嘴唇挂着狡猾贪婪的邪笑，眉毛上挑。彪子急切地点着头，眼睛看着赵虎，用又快又急切的声音对赵虎说出第二句，嘴唇微张、眉毛上提。",
    SOUND_YARD,
    lines=[('zhao_boss', "这小子有鬼，给我跟紧他。", 3.0, 'Biao'), ('biao_thug', "好嘞，虎哥！", 7.0, 'Zhao')], enter={'Biao'},
    bg='Behind them the row of box trucks stands along the back of the yard, and the open yard gate is at frame-right with a trail of dust still hanging in the sunlit air.',
    holds='The frame holds Zhao and Biao, the row of trucks and the open yard gate.',
    st={'Zhao': ('黑色皮背心，香烟夹在手指间', '黑色皮背心，香烟夹在手指间'), 'Biao': ('灰色连帽衫，反戴棒球帽', '灰色连帽衫，反戴棒球帽')})

# ---------------------------------------------------------------------------------------------- 第 4 集
b4 = S.episode('剧本第4集｜山里', '深山里，老护林员抬头看着没有一只鸟的天空说山里不对劲；林峰说整座山他买了。旧防空洞的大厅空荡荡的，地下有清澈的水脉；老人问他图什么，他说修度假村。几天后同一个大厅堆满了货，他第一次把种子按进海绵块、放进水里。赵虎的车队到了山脚想进洞，林峰当面拦住：货到这儿，钱结清，请回。赵虎走后他按下遥控器；山坡上，入口不见了，彪子吓了一跳，赵虎说：把这地方，给我记死了。', 4)

S.T('04-01', '01｜深山里，老护林员抬头看着没有鸟的天，林峰说整座山他买了', 15, OLD,
    [P('ranger_old', 'left', "standing on the dirt trail in profile facing frame-right, leaning on a wooden walking stick, his chin lifted toward the sky", 'obj:the empty pale sky above the pine tops', "his lips pressed thin, his brows drawn together"),
     P('lin_work', 'right', "standing on the trail in profile facing frame-left, his hands at his sides", 'Ranger', "his lips set flat, his brows level")],
    'Medium two-shot, both men from the head to the knees, in the middle third of the frame, on the forest trail.',
    "<ranger_old> gazes up at the empty pale sky above the pine tops and speaks the first line to <lin_work> in a dry, uneasy voice, his lips pressed thin and his brows drawn together. <lin_work> glances up at the sky for a moment, then speaks the second line to <ranger_old> in a calm, firm voice, his lips set flat and his brows level. <ranger_old> stares at him, his jaw slack and his brows drawn together.",
    "老护林员抬头望着松树梢上空荡荡的苍白天空，用干涩不安的声音对林峰说出第一句，嘴唇抿得很薄、眉头拧在一起。林峰抬头看了一眼天，然后用平静坚定的声音对老护林员说出第二句，嘴唇抿平、眉毛平直。老护林员盯着他，下巴松垮、眉头拧在一起。",
    SOUND_FOREST,
    lines=[('ranger_old', "鸟全往南飞了，山里不对劲。", 1.0, 'Lin'), ('lin_work', "整座山，我买了。", 6.0, 'Ranger')],
    bg='Behind them the old concrete shelter portal overgrown with vines stands half open in the hillside at frame-left, and tall pines fill the background.',
    holds='The frame holds Ranger and Lin, the trail, the old shelter portal and the pines.', room={'Ranger', 'Lin'}, new=True,
    st={'Ranger': ('褪色的橄榄绿护林外套，草帽', '褪色的橄榄绿护林外套，草帽'), 'Lin': (SIDE_WORK, SIDE_WORK)})

S.T('04-02', '02｜空荡荡的防空洞大厅：林峰摸地下水脉，老护林员问他图什么', 15, EMPTY,
    [P('lin_work', 'left', "crouching at the edge of the water channel in profile facing frame-right, his fingertips in the clear running water", 'obj:the clear running water in the channel', "his jaw relaxed, his lips set flat, his brows level"),
     P('ranger_old', 'right', "standing at the edge of the channel in profile facing frame-left, a flashlight in one hand and his walking stick in the other", 'Lin', "his brows drawn together in doubt, his lips pressed thin")],
    'Medium-wide shot, both men from the head to the feet, in the middle third of the frame, in the empty concrete hall.',
    "<lin_work> keeps his fingertips in the clear running water and watches it flow, his jaw relaxed and his lips set flat. <ranger_old> sweeps the flashlight beam across the empty hall and speaks the first line to <lin_work> in a doubtful, raspy voice, his brows drawn together and his lips pressed thin. <lin_work> rises slowly to his feet, shakes the water from his fingers and speaks the second line to <ranger_old> in a cold, level voice, his lips set flat and his brows level.",
    "林峰的指尖浸在清澈流动的水里，看着水流过去，下颌放松、嘴唇抿平。老护林员用手电光束扫过空荡荡的大厅，用怀疑而沙哑的声音对林峰说出第一句，眉头拧着、嘴唇抿得很薄。林峰慢慢站起身，甩掉手指上的水，用冰冷平稳的声音对老护林员说出第二句，嘴唇抿平、眉毛平直。",
    voiced('Water trickling along the concrete channel, a faint echo in the huge hall and the click of a flashlight.', '水沿着混凝土水渠淌过的潺潺声、巨大空旷的大厅里微弱的回声和手电筒的一声轻响。'),
    lines=[('ranger_old', "这荒山野洞的，你图什么呀？", 1.5, 'Lin'), ('lin_work', "修度假村。", 6.5, 'Ranger')],
    bg='Behind them the bare walls and rusty railings of the vast empty hall rise into the dark, with pale flashlight beams cutting the dust.',
    holds='The frame holds Lin and Ranger, the water channel and the empty hall.', room={'Ranger', 'Lin'}, new=True,
    st={'Ranger': ('褪色的橄榄绿护林外套，草帽', '褪色的橄榄绿护林外套，草帽'), 'Lin': (SIDE_WORK, SIDE_WORK)})

S.T('04-03', '03｜同一个大厅已经堆满了货：林峰把种子按进海绵块，放进水盆', 15, WORK,
    [P('lin_work', 'center', "standing at the steel workbench in profile facing frame-right, a white foam seeding block in his left hand and a pinch of tiny seeds between the fingers of his right", 'obj:the white foam seeding block in his hand', "his jaw relaxed, his lips set in a calm flat line, his brows soft")],
    'Medium shot, the figure from the head to the waist, in the middle third of the frame, at the workbench.',
    "<lin_work> presses a pinch of tiny seeds into the small holes of the white foam block with his eyes on the block, his jaw relaxed, his lips set in a calm flat line and his brows soft. He sets the block on a white tray with the others and lowers the tray gently into the shallow tub of clear water, and the foam blocks darken slowly as they drink. He rests both palms on the bench and watches the tray, his jaw relaxed and his brows soft.",
    "林峰低头看着手里的白色海绵块，把一小撮细小的种子按进它小小的孔里，下颌放松、嘴唇抿成平静的一条线、眉毛舒展。他把这块放到白色托盘上和其他几块排在一起，轻轻把托盘放进浅浅的清水盆里，海绵块一点点吸水变深。他两手撑在工作台上，看着托盘，下颌放松、眉毛舒展。",
    breathy('Water gently lapping in the tub, the low hum of a generator and the creak of a steel bench.', '水盆里水轻轻荡漾的声音、发电机低低的嗡鸣和钢制工作台轻轻的吱嘎声。'),
    cam=push1('the tray in the water', '水盆里的托盘'),
    bg='Behind him the huge hall is packed with towering stacks of steel crates, pallets of steak boxes, generators and big water tanks under hard white work lamps.',
    holds='The frame holds Lin alone at the workbench, the water tub and the stacked supplies behind him.', room={'Lin'}, new=True,
    st={'Lin': (SIDE_WORK, SIDE_WORK)})

S.T('04-04', '04｜山脚：赵虎想进洞看一眼，林峰当面拦住', 15, TUNNEL,
    [P('lin_work', 'left', "standing in front of the dark tunnel mouth in profile facing frame-right, his right palm raised flat in front of him", 'Zhao', "his lips set flat, his brows level"),
     P('zhao_boss', 'center', "standing on the gravel clearing half a step in front of the box truck in profile facing frame-left, a cigarette hanging from the corner of his mouth", 'Lin', "a greedy sly leer on his lips, his brows lifted")],
    'Medium two-shot, both men from the head to the knees, in the middle third of the frame, on the gravel clearing.',
    "<zhao_boss> steps toward the dark tunnel mouth and speaks the first line to <lin_work> in a wheedling, gravelly voice, a greedy sly leer on his lips and his brows lifted. <lin_work> steps into his path with one palm raised and speaks the second line to <zhao_boss> in a cold, firm voice, his eyes steady on Zhao, his lips set flat and his brows level. <zhao_boss> stops short with his eyes on Lin, his jaw tight, and gives a slow, sour shrug.",
    "赵虎朝黑洞洞的洞口走了一步，用讨好又沙哑的声音对林峰说出第一句，嘴唇挂着狡猾贪婪的邪笑，眉毛上挑。林峰一只手掌竖起，拦在他的路上，用冰冷坚定的声音对赵虎说出第二句，眼睛稳稳看着赵虎，嘴唇抿平、眉毛平直。赵虎停住，眼睛看着林峰，下颌绷紧，慢慢地、不情愿地耸了一下肩。",
    SOUND_TUNNEL,
    lines=[('zhao_boss', "我就进去看一眼，行不行？", 1.0, 'Lin'), ('lin_work', "货到这儿，钱结清，请回。", 5.5, 'Zhao')],
    bg='Behind Zhao the large box truck stands at frame-right on the gravel with its rear door rolled up.',
    holds='The frame holds Lin and Zhao, the dark tunnel mouth and the box truck.', room={'Lin', 'Zhao'}, new=True, trigger='货到这儿，钱结清，请回。',
    st={'Lin': (SIDE_WORK, SIDE_WORK), 'Zhao': ('黑色皮背心，叼着烟', '黑色皮背心，叼着烟')})

S.T('04-05', '05｜赵虎和彪子走向卡车，林峰站在洞口暗处，举起遥控器按下', 15, TUNNEL,
    [P('lin_work', 'left', "standing just inside the dark tunnel mouth in profile facing frame-right, a small black remote in his right hand at his side", 'obj:the two men walking away across the gravel clearing', "his lips set in a cold line, his brows level"),
     P('zhao_boss', 'center', "walking away across the gravel clearing in profile facing frame-right, a cigarette hanging from the corner of his mouth", 'obj:the box truck at frame-right', "a smug set to his lips, his brows lifted"),
     P('biao_thug', 'right', "walking beside Zhao in profile facing frame-right, glancing around the hillside", 'obj:the box truck at frame-right', "his lips parted, his brows pulled up")],
    'Wide shot, all three from the head to the feet, in the middle third of the frame, on the gravel clearing.',
    "<zhao_boss> and <biao_thug> walk away across the gravel clearing toward the box truck at frame-right with their backs mostly to the tunnel; <lin_work> stands just inside the dark tunnel mouth watching them go, then raises the small black remote and presses it with his thumb, his lips set in a cold line and his brows level.",
    "赵虎和彪子背对着隧道口，穿过碎石空地走向画面右边的卡车；林峰站在洞口里面的暗处看着他们走远，然后抬起那个黑色小遥控器，用拇指按下去，嘴唇抿成冷冷的一条线，眉毛平直。",
    breathy('Boots crunching on gravel and a truck engine idling.', '靴子踩在碎石上的嘎吱声和卡车发动机怠速的声音。'),
    enter={'Biao'}, effect='货到这儿，钱结清，请回。', holds='The frame holds Lin just inside the tunnel mouth and Zhao and Biao walking toward the box truck.',
    st={'Lin': (SIDE_WORK, SIDE_WORK), 'Zhao': ('黑色皮背心，叼着烟', '黑色皮背心，叼着烟'), 'Biao': ('灰色连帽衫，反戴棒球帽', '灰色连帽衫，反戴棒球帽')})

S.T('04-06', '06｜同一座山坡：入口不见了，彪子吓一跳，赵虎说记死这地方', 15, HIDDEN,
    [P('biao_thug', 'left', "standing on the gravel clearing in profile facing frame-left, one arm pointing toward the hillside", 'obj:the moss-covered boulder and the dead stump on the hillside at frame-left', "his eyes wide, his brows pulled up, his lips parted"),
     P('zhao_boss', 'right', "standing beside the box truck in profile facing frame-left, a cigarette hanging from the corner of his mouth", 'obj:the moss-covered boulder on the hillside at frame-left', "his jaw tight, his lips pressed flat, his brows low")],
    'Medium two-shot, both men from the head to the knees, in the middle third of the frame, on the gravel clearing.',
    "<biao_thug> points at the hillside with one arm and speaks the first line to <zhao_boss> in a startled voice, his eyes wide and his brows pulled up. <zhao_boss> stares at the moss-covered boulder, then turns his eyes to <biao_thug> and speaks the second line to <biao_thug> in a low sly voice, his jaw tight, his lips pressed flat and his brows low.",
    "彪子伸手指着山坡，用吃惊的声音对赵虎说出第一句，眼睛睁大、眉毛上提。赵虎盯着那块长满青苔的岩石，然后把目光转向彪子，用低沉狡猾的声音对彪子说出第二句，下颌绷紧、嘴唇抿平、眉头压低。",
    SOUND_TUNNEL,
    lines=[('biao_thug', "洞口……没了？", 1.5, 'Zhao'), ('zhao_boss', "把这地方，给我记死了。", 5.5, 'Biao')],
    cam=push('both men', '两人'),
    bg='Behind them the moss-covered boulder and the dead stump sit on the quiet hillside at frame-left where the tunnel mouth was, and the box truck stands at frame-right.',
    holds='The frame holds Biao and Zhao, the boulder and the stump on the hillside, and the box truck.', room={'Zhao', 'Biao'}, new=True)

doc = S.finish()
