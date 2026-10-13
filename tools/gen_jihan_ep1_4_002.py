#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 1–4 集，第一批制作稿（新建一部剧，不是追加），编号 002（2026-10-13）。取代 001。

为什么重做（hh 2026-10-13 08:47 / 09:02）：
  ① 001 里所有任务都是 5–10 秒，一共 31 个开场图；hh 看到最早的版本（每个任务 15 秒）最流畅，开场图是最大的不稳定因素。
     现在整部压成 19 个任务 × 15 秒 = 285 秒，开场图 19 张。
  ② 001 把角色全写成了欧美人（我没写人种，名字还美国化），而且台词是英语——这部剧发中国，台词是中文（普通话）。
     现在：人物肖像提示词里写明 Chinese，名字用回林峰／苏清月／赵虎，台词和声音描述都是中文普通话。

写法和 Alpha 第 27–60 集相同（规律文档 v1.9）：一个任务只放一串慢而连续的事；每个人的视线对象写进开场图；每句台词写明对谁说、
对象在画面里；一个任务最多 2 句台词、都排在前半段；背景群体写清楚、不虚化；有名字的人最多 3 个；机械状态变化只拍结果；
画面里不出现读得出的文字；站位表程序检查。台词 ≤13 个汉字；不拿人名开头（名字后会停很久）。

15 秒的塞法：每个任务 = 同一个地点、同一批人、一串 2–3 拍的慢动作＋最多 2 句台词（前一句在 1–2.5 秒，后一句最晚 7 秒）。
  第 1 集 ① 超算大屏：红色曲线断崖下跌，同事唐博士问“九天后就零下八十度？”，林峰答“我的模型不会错”（观众先听懂两个数字）；
         ② 会议室：魏局长骂“你的模型就是垃圾”，林峰摘下工牌放桌上，说“享受你们最后的九天吧”（桌子远端五个专家嗤笑）；
         ③ 广场：他走出大楼被烈日晒得满头汗，走向车边的钱经理，说“我名下所有资产，半价全卖”，钱经理问“你是在躲什么吗”；
         ④ 同一处：他说“九天后钱就没用了”，钱经理愣住，他抬头看着太阳，嘴角冷冷一动，响起收银机的“叮”（本集钩子）。
  第 2 集 ① 豪宅：苏清月（手里捏着黑卡、手压着一张写满字的草稿纸）念“羽绒服、煤炭、育苗灯？”再问“你是不是被害妄想症”；
         ② 林峰接过黑卡塞进口袋，说“多买泡面和羽绒服”“说不定能救你一命”；
         ③ 他拎起背包走进玄关（拍他走出画面的全过程），苏清月转头对助理说“去调气象局全部数据”；
         ④ 她站在落地窗前看烈日，对助理说“把酒窖给我囤满”“他不是妄想，他知道内情”（本集钩子）。
  第 3 集 ① 地下大厅（无人）：物资堆成山，镜头顺着过道慢慢推进；
         ② 隧道口：林峰催卡车卸货“再快点卸货，时间不多了”，递出金条“这是尾款，拿了就走”，赵虎掂着金条；
         ③ 赵虎和小弟彪子走向卡车，林峰站在洞口里面的暗处看着，举起遥控器按下（只拍按，不拍岩石滑动）；
         ④ 同一座山坡（卡车还在右边）：隧道口不见了，只剩一块长满青苔的岩石和枯树桩；彪子说“洞口不见了，老板”，
            赵虎说“有钱的傻子，记住这地方”（给后面埋雷）；
         ⑤ 地下控制台：林峰按下红色总控按钮，三台发电机依次启动、暖黄色灯亮起、红色电子钟亮起。
  第 4 集 ① 夏日烧烤摊：街尾滚来一堵白色雾墙，食客们抬头、站起来；② 同一条街已经冻成冰雕，天空绿色极光；
         ③ 安全屋：林峰光脚煎牛排，背对镜头、嘴不动，念一句独白“他们都说我疯了”（独白测试：脸不入画）；
         ④ 监控墙：陌生男人在暴风雪里倒下，林峰一动不动；⑤ 酒窖：苏清月和助理冻得发抖，“那个疯子现在肯定暖和着呢”“他早就警告过您了”；
         ⑥ 林峰的刀叉停在牛排上，红色警报光闪在脸上（屏幕里排气管口被冰封），他放下刀，抬眼看向通往地表的钢制舱门。
偏离大纲（交稿时告诉 hh）：中介电话改当面；电脑警告语音／屏幕文字不念；五十亿金额不念；苏清月打电话改成当面对助理说；
  “订两吨罐头十台发电机”压成“把酒窖给我囤满”；蒙太奇压成“堆满的大厅＋卸货”；仿生岩石盖住入口只拍结果；赵虎“把坐标记死”压成“记住这地方”；
  人群变冰雕只拍雾墙逼近＋冻结后的静止街景；“变异野狗刨尸体”改成倒下的孤身男人；一氧化碳警告文字不念，改画排气管口冰封；
  001 里的狂风白天（森林）和红色电子钟读秒特写删掉，电子钟只作为控制台背景亮起；苏清月不是一个人（助理陪着，因为台词要有画面里的对象）。
左右方向（每个场景固定）：
  超算大厅：巨大弧形墙屏在画面右半边，服务器机柜在左墙；会议室：魏局长在画面左，林峰在右（靠门），专家们坐在桌子远端；
  广场：玻璃大门在左，轿车在右；豪宅：玻璃餐桌在中间，落地窗在后墙，白沙发在左墙，玄关和三个战术背包在右；
  隧道口：隧道口在左，卡车在右；同一座山坡：岩石和枯树桩在左，卡车在右；控制台：红色按钮在中间，发电机在后墙，红色电子钟在上，舱门在右；
  烧烤摊：烤炉在左，折叠桌在中间，大道通向右边灭点；安全屋生活区：炉灶和大理石台在左，羊毛地毯和圆桌在中间，监控墙在中右，钢制舱门在右墙最右；
  酒窖：酒架在左，罐头和水箱在右，露营灯在中间。
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

OUT = '合并稿/002_第1-4集_十五秒中文版_制作稿'
S = Session(None, OUT, 31000, title='极寒末日：我的隐秘安全屋｜第1–4集｜预言·变卖·囤货·降临', style=STYLE)

# ---------------------------------------------------------------------------------------------- 外貌（全部写明 Chinese）
look('lin_shirt', 'Lin', "in a crisp white dress shirt with the sleeves rolled to his forearms and dark slacks", 'steady dark-brown', 'his', eth='a Chinese man in his early thirties')
look('lin_work', 'LinWork', "in a charcoal henley under a dark olive utility vest with many pockets and dark cargo pants", 'steady dark-brown', 'his', eth='a Chinese man in his early thirties')
look('lin_home', 'LinHome', "in a soft grey cotton long-sleeve henley and loose dark lounge pants, barefoot, his hair damp from a shower", 'steady dark-brown', 'his', eth='a Chinese man in his early thirties')
look('su_suit', 'Su', "in a fitted black silk blouse and a black pencil skirt, thin gold-rimmed glasses on her nose, her long glossy black hair falling straight over one shoulder", 'sharp dark-brown', 'her', eth='a Chinese woman in her late twenties')
look('su_cold', 'SuCold', "bundled in a thick cream down jacket over a black sweater with a grey wool blanket around her shoulders and a knit hat pulled low", 'sharp dark-brown', 'her', eth='a Chinese woman in her late twenties')
look('wen_blazer', 'Wen', "in a navy blazer over a white blouse, her black hair in a neat low ponytail", 'clear dark', 'her', eth='a Chinese woman in her mid-twenties')
look('wen_cold', 'WenCold', "bundled in a bulky red down parka with the hood up and a thick grey scarf", 'clear dark', 'her', eth='a Chinese woman in her mid-twenties')
look('tang_analyst', 'Tang', "in a white lab coat over a grey sweater, round clear-framed glasses on her nose, her black hair pinned up in a tidy bun", 'tired dark', 'her', eth='a Chinese woman in her late twenties')
look('wei_director', 'Wei', "in a grey suit with a loosened blue tie and thin black-framed glasses, his short grey-streaked black hair combed back", 'dark', 'his', eth='a Chinese man in his sixties')
look('qian_broker', 'Qian', "in a navy three-piece suit with a pale yellow tie, his slicked-back black hair damp with sweat", 'tired dark', 'his', eth='a Chinese man in his forties')
look('zhao_boss', 'Zhao', "in a sleeveless black leather vest over a sweat-stained grey t-shirt, a gold chain at his thick neck, his head shaved", 'small dark', 'his', eth='a Chinese man in his fifties')
look('biao_thug', 'Biao', "in a faded grey hoodie and a backwards baseball cap over short black hair, lean and wiry", 'restless dark', 'his', eth='a Chinese man in his twenties')

# ---------------------------------------------------------------------------------------------- 场景（开场图后缀 + 固定布局）
SUPER = Scene('supercomputer_hall', " Cold blue light from the giant wall screen and flashing red alarm lamps wash the dark server hall.",
              " Fixed stage layout: the giant curved wall screen fills the right half of the frame; rows of black server racks with blinking lights line the left wall; the glossy dark floor spreads across the foreground.")
MEET = Scene('meeting_room', " Harsh white summer sunlight pours through the tall window into the cool air-conditioned meeting room.",
             " Fixed stage layout: the long polished conference table stretches across the middle of the frame; the floor-to-ceiling window in the back wall shows a white-hot sun over a shimmering city of glass towers; the wooden door is in the right wall at frame-right.")
PLAZA = Scene('bureau_plaza', " Blinding white midday sun beats down on the concrete plaza, heat shimmering off the pavement.",
              " Fixed stage layout: the glass entrance doors of the weather bureau tower are at frame-left; the wide empty white-concrete plaza fills the middle of the frame; a black sedan is parked at the curb at frame-right.")
PENT = Scene('penthouse', " Cool air-conditioned light fills the luxury penthouse while harsh white sunlight glares through the windows.",
             " Fixed stage layout: the glass dining table stands in the middle of the frame; the floor-to-ceiling windows across the back wall show a white-hot city of glass towers under a blazing sun; the white sectional sofa stands against the left wall; the wide entry hall opens at frame-right with three black tactical backpacks lined up on the floor beside it.")
HALL = Scene('bunker_hall', " Hard work lamps cast sharp shadows across the vast concrete underground hall.",
             " Fixed stage layout: a central aisle runs from the foreground to the far wall between towering stacks of steel crates; generators and big water tanks line the walls; hanging work lamps light the hall.")
TUNNEL = Scene('tunnel_mouth', " Hard noon light falls through tall pines onto the gravel clearing in front of the tunnel mouth.",
               " Fixed stage layout: the dark concrete tunnel mouth is cut into the forested hillside at frame-left; the gravel clearing fills the middle of the frame; a large box truck with its rear door rolled up and crates stacked at its back stands at frame-right; tall pine trees fill the background.")
HIDDEN = Scene('hill_hidden', " Hard noon light falls through tall pines onto the quiet forest hillside.",
               " Fixed stage layout: the forested hillside at frame-left holds a moss-covered boulder and a dead tree stump; the gravel clearing fills the middle of the frame; the large box truck stands at frame-right; tall pine trees fill the background.")
CORE = Scene('bunker_core', " Dim emergency light fills the concrete control corner of the underground hideout.",
             " Fixed stage layout: the steel control console with a large red button under a flip-up cover stands at frame-center; three matte-grey silent generators stand in a row against the back wall; a big red digital clock hangs on the wall above the console; a heavy steel hatch door is in the right wall at frame-right.")
STREET = Scene('street_bbq', " Hot bright late-afternoon sunlight falls over a busy summer street barbecue stand, the grill burning orange.",
               " Fixed stage layout: the street barbecue stand with an open charcoal grill is at frame-left; a row of folding tables with plastic stools and diners fills the middle of the frame; the long avenue stretches to the vanishing point at frame-right between tall buildings.")
FROZEN = Scene('street_frozen', " Pale cold light under a green aurora sky falls on the silent frozen street, thick frost on every surface.",
               " Fixed stage layout: the street barbecue stand with its grill frozen into a jagged ice sculpture is at frame-left; the folding tables and stools, covered in frost, fill the middle of the frame; the long avenue stretches to the vanishing point at frame-right.")
LIVING = Scene('bunker_living', " Warm amber light from soft recessed lamps fills the cozy underground living area.",
               " Fixed stage layout: the open kitchen with a black-and-gold stove and a marble counter is at frame-left; a thick cream wool rug and a small round wooden dining table fill the middle of the frame; a wall of small security monitors is at frame-center-right; a heavy round steel hatch door is in the right wall at the far frame-right.")
CELLAR = Scene('wine_cellar', " Cold blue-grey light from a single camping lantern fills the freezing stone wine cellar.",
               " Fixed stage layout: tall wooden wine racks line the left wall; stacks of canned food and crates of bottled water stand against the right wall; a small camping lantern sits on an upturned crate in the middle of the frame; a narrow stone staircase leads up at the back wall.")

# ---------------------------------------------------------------------------------------------- 第 1 集（先建第一个 Batch，新素材都加在它上面）
b1 = S.episode('剧本第1集｜预言：九天后的断崖', '国家气象超算中心里，林峰算出九天后全球气温将断崖式跌到零下八十度；会议室里魏局长嘲笑他的数据，他摘下工牌丢下一句“享受你们最后的九天”；走出大楼，他对等在车边的钱经理说：我名下所有资产半价全卖——因为九天后钱就没用了。', 1)

new_person(b1, 'lin_shirt', '林峰（气象局研究员，白衬衫）', 'man',
           'Lin, a lean, athletic Chinese man in his early thirties with short neat black hair, a clean-shaven angular face and steady dark-brown eyes, wearing a crisp white dress shirt with the sleeves rolled to his forearms and dark slacks.',
           '林峰，三十出头、身形精瘦结实的中国男性，黑色短发整齐，脸颊干净、轮廓分明，沉稳的深褐色眼睛，穿着挺括的白衬衫、袖子卷到小臂，深色西裤。',
           'short neat black hair, a clean-shaven angular face, steady dark-brown eyes, wearing a crisp white dress shirt with the sleeves rolled to his forearms and dark slacks',
           'a calm, level expression', eth='Chinese')
new_person(b1, 'lin_work', '林峰（深灰色亨利衫，橄榄绿多口袋工装背心）', 'man',
           'Lin, the same lean, athletic Chinese man in his early thirties as in the reference, with short black hair and a faint shadow of stubble, steady dark-brown eyes, wearing a charcoal henley under a dark olive utility vest with many pockets and dark cargo pants.',
           '林峰，和参考图是同一位三十出头、身形精瘦结实的中国男性，黑色短发，带一点淡淡的胡茬，沉稳的深褐色眼睛，穿着深灰色亨利衫、外面是深橄榄绿多口袋工装背心，深色工装裤。',
           'short black hair, a faint shadow of stubble, steady dark-brown eyes, wearing a charcoal henley under a dark olive utility vest with many pockets',
           'a calm, level expression', ref='lin_shirt')
new_person(b1, 'lin_home', '林峰（在安全屋里：灰色棉质家居服，光脚）', 'man',
           'Lin, the same lean, athletic Chinese man in his early thirties as in the reference, with short black hair still damp from a shower, steady dark-brown eyes, wearing a soft grey cotton long-sleeve henley and loose dark lounge pants, barefoot.',
           '林峰，和参考图是同一位三十出头、身形精瘦结实的中国男性，黑色短发刚洗过还带着湿气，沉稳的深褐色眼睛，穿着柔软的灰色棉质长袖亨利衫和宽松的深色家居裤，光着脚。',
           'short black hair still damp from a shower, steady dark-brown eyes, wearing a soft grey cotton long-sleeve henley and loose dark lounge pants, barefoot',
           'a relaxed, content expression', ref='lin_shirt', full=True)
new_person(b1, 'su_suit', '苏清月（黑色真丝衬衫，金丝眼镜）', 'woman',
           'Su, an elegant, strikingly beautiful Chinese woman in her late twenties with long glossy black hair falling straight over one shoulder, sharp dark-brown eyes behind thin gold-rimmed glasses, wearing a fitted black silk blouse and a black pencil skirt.',
           '苏清月，二十八岁左右、优雅而极其美丽的中国女性，乌黑的长直发光滑地垂在一边肩上，锐利的深褐色眼睛戴着细细的金丝眼镜，穿着合身的黑色真丝衬衫和黑色铅笔裙。',
           'long glossy black hair falling straight over one shoulder, sharp dark-brown eyes behind thin gold-rimmed glasses, wearing a fitted black silk blouse',
           'a composed, sharp expression', eth='Chinese')
new_person(b1, 'su_cold', '苏清月（酒窖里：奶白色羽绒服，灰色毛毯，针织帽）', 'woman',
           'Su, the same elegant Chinese woman in her late twenties as in the reference, with sharp dark-brown eyes, pale cheeks and lips tinged blue from the cold, wearing a thick cream down jacket over a black sweater, a grey wool blanket around her shoulders and a knit hat pulled low over her black hair.',
           '苏清月，和参考图是同一位二十八岁左右优雅的中国女性，锐利的深褐色眼睛，脸颊苍白、嘴唇冻得发青，穿着厚厚的奶白色羽绒服、里面是黑色毛衣，肩上裹着灰色羊毛毯，针织帽拉得很低盖住黑发。',
           'sharp dark-brown eyes, pale cheeks, lips tinged blue from the cold, wearing a thick cream down jacket over a black sweater, a grey wool blanket around her shoulders and a knit hat pulled low',
           'a pale, shivering expression', ref='su_suit')
new_person(b1, 'wen_blazer', '文助理（苏清月的助理，藏青色西装外套）', 'woman',
           'Wen, a brisk young Chinese woman in her mid-twenties with black hair in a neat low ponytail, clear dark eyes and a smooth fair face, wearing a navy blazer over a white blouse.',
           '文助理，二十五岁左右干练的年轻中国女性，黑色头发扎成利落的低马尾，清亮的深色眼睛，皮肤白净，穿着藏青色西装外套、里面是白衬衫。',
           'black hair in a neat low ponytail, clear dark eyes, a smooth fair face, wearing a navy blazer over a white blouse',
           'an attentive, alert expression', eth='Chinese')
new_person(b1, 'wen_cold', '文助理（酒窖里：红色厚羽绒服，灰围巾）', 'woman',
           'Wen, the same young Chinese woman in her mid-twenties as in the reference, with clear dark eyes, pale cheeks and lips tinged blue from the cold, wearing a bulky red down parka with the hood up and a thick grey scarf.',
           '文助理，和参考图是同一位二十五岁左右的年轻中国女性，清亮的深色眼睛，脸颊苍白、嘴唇冻得发青，穿着鼓鼓囊囊的红色羽绒服、戴着兜帽，围着厚厚的灰围巾。',
           'clear dark eyes, pale cheeks, lips tinged blue from the cold, wearing a bulky red down parka with the hood up and a thick grey scarf',
           'a pale, shivering expression', ref='wen_blazer')
new_person(b1, 'tang_analyst', '唐博士（气象局研究员，白大褂，圆框眼镜）', 'woman',
           'Dr. Tang, a worried Chinese woman in her late twenties with black hair pinned up in a tidy bun, tired dark eyes behind round clear-framed glasses and a pale tense face, wearing a white lab coat over a grey sweater.',
           '唐博士，二十八岁左右、满脸忧虑的中国女性，黑色头发在脑后盘成整齐的发髻，疲惫的深色眼睛戴着圆形透明镜框眼镜，脸色苍白紧绷，穿着白大褂、里面是灰色毛衣。',
           'black hair pinned up in a tidy bun, tired dark eyes behind round clear-framed glasses, a pale tense face, wearing a white lab coat over a grey sweater',
           'a worried, tense expression', eth='Chinese')
new_person(b1, 'wei_director', '魏局长（气象局领导，灰西装，黑框眼镜）', 'man',
           'Director Wei, an older Chinese man in his sixties with short grey-streaked black hair combed back, a lined stern face and dark eyes behind thin black-framed glasses, wearing a grey suit with a loosened blue tie.',
           '魏局长，六十多岁的年长中国男性，黑中夹灰的短发向后梳，一张有皱纹的严厉的脸，深色眼睛戴着细黑框眼镜，穿着灰色西装、蓝领带松松地挂着。',
           'short grey-streaked black hair combed back, a lined stern face, dark eyes behind thin black-framed glasses, wearing a grey suit with a loosened blue tie',
           'a stern, condescending expression', eth='Chinese')
new_person(b1, 'qian_broker', '钱经理（林峰的资产经理，藏青三件套）', 'man',
           'Manager Qian, a nervous Chinese man in his forties with slicked-back black hair damp with sweat, tired dark eyes and a soft round face, wearing a navy three-piece suit with a pale yellow tie.',
           '钱经理，四十多岁、神情紧张的中国男性，向后梳的黑发被汗水打湿，疲惫的深色眼睛，一张圆润的脸，穿着藏青色三件套西装、淡黄色领带。',
           'slicked-back black hair damp with sweat, tired dark eyes, a soft round face, wearing a navy three-piece suit with a pale yellow tie',
           'a worried, sweaty expression', eth='Chinese')
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

new_scene(b1, 'supercomputer_hall', '国家气象超算中心大厅', 'A dark national weather supercomputer hall: a giant curved wall screen fills the right half of the hall showing a global temperature map and a red temperature curve, rows of black server racks with blinking lights line the left wall, a glossy dark floor, cold blue light with flashing red alarm lamps.',
          '国家气象超算中心昏暗的大厅：右半边是一整面巨大的弧形墙屏，显示着全球气温图和一条红色气温曲线，左墙边是一排排闪着指示灯的黑色服务器机柜，光亮的深色地面，冷蓝色的光里闪着红色警报灯。',
          'the giant wall screen, the server racks and the dark floor')
new_scene(b1, 'meeting_room', '气象局会议室（外面是烈日）', 'A conference room in a weather bureau tower in a Chinese city: a long polished conference table stretches across the middle of the frame with leather chairs along both sides, the floor-to-ceiling window in the back wall shows a white-hot summer sun over a shimmering city of glass towers, a wooden door in the right wall, cool white air-conditioned light.',
          '中国某城市气象局大楼里的会议室：中间横着一张长长的抛光会议桌、两侧是皮椅，后墙是落地窗，窗外是白热的夏日太阳和热浪扭曲的玻璃幕墙城市，右墙一扇木门，冷白色的空调光。',
          'the conference table, the window with the blazing sun and the door')
new_scene(b1, 'bureau_plaza', '气象局大楼前的广场（正午烈日）', 'The sunlit concrete plaza in front of a glass weather bureau tower in a Chinese city at midday: the glass entrance doors at the left, a wide empty plaza of white concrete in the middle with heat shimmering off it, a black sedan parked at the curb at the right, a few trees with limp leaves, a blinding white sun in a cloudless sky.',
          '正午阳光下中国某城市气象局玻璃大楼前的水泥广场：左边是玻璃大门，中间是一大片白色水泥广场、热浪从地面升起，右边路边停着一辆黑色轿车，几棵叶子蔫了的树，万里无云的天空里是一颗刺眼的白色太阳。',
          'the glass entrance doors, the plaza, the sedan and the blinding sun')
new_scene(b1, 'penthouse', '市中心豪华大平层（冷气很足，窗外是烈日）', 'A luxury penthouse living room in a Chinese city: a glass dining table in the middle of the room, floor-to-ceiling windows across the back wall showing a white-hot skyline of glass towers under a blazing sun, a white sectional sofa against the left wall, a wide entry hall at the right with three black tactical backpacks lined up on the floor beside it, cool air-conditioned light.',
          '中国某城市的豪华大平层客厅：房间中间是一张玻璃餐桌，后墙是落地窗、窗外是烈日下白热的玻璃幕墙天际线，左墙边是白色组合沙发，右边是宽敞的玄关、旁边地上并排放着三个黑色战术背包，冷色的空调光。',
          'the glass table, the windows, the sofa and the entry hall with the backpacks')
new_scene(b1, 'bunker_hall', '地下防空洞大厅（囤货堆成山）', 'A vast underground concrete hall of an abandoned civil-defense shelter, packed with supplies: a central aisle runs from the foreground to the far wall between towering stacks of steel crates and pallets of steak boxes, crates of lobsters on ice, rows of generators, big water tanks and white medical cases along the walls, hanging work lamps casting hard light, a forklift parked in the aisle.',
          '废弃防空洞的巨大地下混凝土大厅，里面堆满了物资：一条中央过道从前景通到尽头的墙，两边是高高的钢箱和托盘、成箱的牛排、冰上的龙虾箱，沿墙是一排排发电机、巨大的水箱和白色医疗箱，吊着的工作灯投下硬光，过道上停着一辆叉车。',
          'the aisle, the stacked crates, the generators and the water tanks')
new_scene(b1, 'tunnel_mouth', '深山里的隧道口（入口敞开）', 'A forested mountain hillside in summer in China: a dark concrete tunnel mouth cut into the hillside at the left, a gravel clearing in the middle, a large box truck with its rear door rolled up and crates stacked at its back at the right, tall pine trees all around, hard noon light.',
          '夏天中国的深山树林山坡：左边山坡上开着一个黑洞洞的混凝土隧道口，中间是一片碎石空地，右边停着一辆后门卷起、后面堆着箱子的大型厢式卡车，四周是高高的松树，正午的硬光。',
          'the tunnel mouth, the gravel clearing, the box truck and the pines')
new_scene(b1, 'hill_hidden', '同一座山坡（入口已被伪装，只剩青苔岩石和枯树桩，卡车还在右边）', 'The same forested mountain hillside in summer as in the reference image, now with no tunnel mouth: a moss-covered boulder and a dead tree stump sit on the slope at the left where the tunnel mouth was, a gravel clearing in the middle, the same large box truck still standing at the right, tall pine trees all around, hard noon light.',
          '和参考图是同一座夏天的深山树林山坡，只是隧道口不见了：左边坡上原本是隧道口的位置现在是一块长满青苔的岩石和一截枯树桩，中间是碎石空地，右边还是那辆大型厢式卡车，四周是高高的松树，正午的硬光。',
          'the boulder, the stump, the clearing, the truck and the pines')
new_scene(b1, 'bunker_core', '地下安全屋的控制角落（发电机与红色总控按钮）', 'The concrete control corner of an underground hideout in dim emergency light: a steel control console with a large red button under a flip-up cover at the center, three matte-grey silent generators in a row against the back wall, a big red digital clock on the wall above the console, a heavy steel hatch door in the right wall.',
          '地下藏身处混凝土的控制角落，昏暗的应急灯光：中间是钢制控制台、上面一个带翻盖的大红按钮，后墙边并排放着三台哑光灰色的静音发电机，控制台上方墙上是一个大红色电子钟，右墙是一扇厚重的钢制舱门。',
          'the console with the red button, the three generators, the red clock and the hatch')
new_scene(b1, 'street_bbq', '夏日午后的街头烧烤摊', 'A busy summer Chinese street barbecue stand in hot bright late-afternoon sunlight: an open charcoal grill with skewers burning orange at the left, a row of folding tables with small plastic stools and diners holding beer bottles in the middle, a long city avenue stretching to the vanishing point at the right between tall buildings.',
          '炎热明亮的夏日午后热闹的中国街头烧烤摊：左边是烧得橙红、串着肉串的敞口炭烤炉，中间一排折叠桌和小塑料凳、食客们举着啤酒瓶，右边是一条长长的城市大道、通向两侧高楼之间的灭点。',
          'the grill, the tables with diners and the long avenue')
new_scene(b1, 'street_frozen', '同一条街被冰封之后（极光）', 'The same street barbecue stand and avenue as in the reference image, same buildings and same table layout, after the freeze, silent and white: the grill frozen into a jagged ice sculpture at the left, frost-covered folding tables and stools in the middle with life-size ice statues of diners frozen mid-gesture, a long avenue to the vanishing point at the right, a green aurora across the dark sky, pale cold light.',
          '和参考图是同一个烧烤摊、同一条大道（楼房和桌子位置不变），被冻住之后寂静而苍白：左边烤炉冻成一座参差的冰雕，中间是覆满白霜的折叠桌和小凳、桌边是保持着动作被冻住的真人大小的食客冰雕，右边是通向灭点的长街，漆黑的天空里一道绿色极光，苍冷的光。',
          'the frozen grill, the frosted tables with the ice statues and the aurora')
new_scene(b1, 'bunker_living', '安全屋的生活区（暖黄灯，25℃）', 'The cozy living area of an underground hideout: an open kitchen with a black-and-gold stove and a marble counter at the left, a thick cream wool rug and a small round wooden dining table in the middle, a wall of small security monitors at the center-right, a heavy round steel hatch door in the right wall, warm amber light from soft recessed lamps.',
          '地下藏身处温馨的生活区：左边是开放式厨房、黑金色炉灶和大理石台面，中间是厚厚的奶白色羊毛地毯和一张小小的圆形木餐桌，中右是一整面小监控屏墙，右墙是一扇厚重的圆形钢制舱门，柔和的嵌灯投下暖琥珀色的光。',
          'the kitchen, the rug, the dining table, the monitor wall and the hatch')
# 前后两组场景：后一张用前一张当参照图，让“同一处”真的是同一处（没测过：风险是旧图里的卡车／火光盖过新状态）
for _a in b1.d['assets']:
    if _a['key'] == 'hill_hidden': _a['generate']['reference_keys'] = ['tunnel_mouth']
    if _a['key'] == 'street_frozen': _a['generate']['reference_keys'] = ['street_bbq']

new_scene(b1, 'wine_cellar', '苏清月豪宅的地下酒窖（冻得发抖）', 'A freezing stone wine cellar: tall wooden wine racks along the left wall, stacks of canned food and crates of bottled water against the right wall, a small camping lantern on an upturned crate in the middle, a narrow stone staircase leading up at the back wall, cold blue-grey light.',
          '冰冷的石头酒窖：左墙边是高高的木头酒架，右墙边是一摞摞罐头和成箱的瓶装水，中间一只倒扣的木箱上放着一盏小露营灯，后墙是一道通往上面的窄石阶，冷蓝灰色的光。',
          'the wine racks, the cans and water crates, the lantern and the staircase')

# ---------------------------------------------------------------------------------------------- 声音（中文普通话）
VT_EN = ' Every word is fully voiced and audible.'
VT_ZH = '每个字都正常发声、清晰可辨。'
LIN_EN = 'A mature adult male voice, calm and level with a dry cold edge, speaking clear Mandarin Chinese. He never raises his voice.' + VT_EN
LIN_ZH = '成熟成年男声，平稳镇定，带一点干冷的质感，普通话清楚。他从不提高音量。' + VT_ZH
for nm, key in (('Lin', 'lin_shirt'), ('LinWork', 'lin_work'), ('LinHome', 'lin_home')):
    b1.character(nm, key, LIN_EN, LIN_ZH)
b1.character('Su', 'su_suit', "A confident adult woman's voice, low, smooth and slightly husky, speaking clear Mandarin Chinese with a sharp, measured edge." + VT_EN,
             '自信的成年女声，低沉、顺滑、略带沙哑，普通话清楚，带着锐利而有分寸的质感。' + VT_ZH)
b1.character('SuCold', 'su_cold', "A confident adult woman's voice, low and slightly husky, shaky from the cold with faintly chattering teeth, speaking clear Mandarin Chinese." + VT_EN,
             '自信的成年女声，低沉、略带沙哑，因为寒冷而发抖、牙齿微微打颤，普通话清楚。' + VT_ZH)
b1.character('Wen', 'wen_blazer', "A young adult woman's voice, brisk and attentive, speaking clear Mandarin Chinese." + VT_EN, '年轻成年女声，干练、专注，普通话清楚。' + VT_ZH)
b1.character('WenCold', 'wen_cold', "A young adult woman's voice, thin and shaky from the cold, speaking clear Mandarin Chinese." + VT_EN, '年轻成年女声，因为寒冷而发细发抖，普通话清楚。' + VT_ZH)
b1.character('Tang', 'tang_analyst', "A young adult woman's voice, tight and shaky with dread, speaking clear Mandarin Chinese." + VT_EN, '年轻成年女声，因为恐惧而紧绷发颤，普通话清楚。' + VT_ZH)
b1.character('Wei', 'wei_director', 'An older adult male voice, gruff and condescending, speaking clear Mandarin Chinese.' + VT_EN, '年长成年男声，粗哑、居高临下，普通话清楚。' + VT_ZH)
b1.character('Qian', 'qian_broker', 'A middle-aged adult male voice, smooth but strained and nervous, speaking clear Mandarin Chinese.' + VT_EN, '中年成年男声，本来圆滑、此刻紧绷而紧张，普通话清楚。' + VT_ZH)
b1.character('Zhao', 'zhao_boss', 'A heavy adult male voice, gravelly and smug, speaking clear Mandarin Chinese.' + VT_EN, '粗重的成年男声，沙砾般粗糙、得意，普通话清楚。' + VT_ZH)
b1.character('Biao', 'biao_thug', 'A young adult male voice, nasal and eager, speaking clear Mandarin Chinese.' + VT_EN, '年轻成年男声，带鼻音、急切，普通话清楚。' + VT_ZH)

BADGE = 'a white ID badge clipped to his shirt pocket'
W_BADGE = '白衬衫，胸前别着工牌'
W_NOBADGE = '白衬衫，没有工牌，额头有汗'
SOUND_MEET = voiced('A quiet air-conditioned meeting room with a faint hum and a few low chuckles.', '安静的、开着空调的会议室，有轻微的嗡鸣和几声低低的嗤笑。')
SOUND_PLAZA = voiced('Cicadas droning in the heat and the distant hiss of traffic.', '知了在热浪里不停地叫，远处是车流的嘶嘶声。')
SOUND_PENT = voiced('The faint hum of the air conditioner and the distant murmur of the city.', '空调轻微的嗡鸣和远处城市的低语。')
SOUND_TUNNEL = voiced('A truck engine idling, crates thudding onto gravel and birds in the pines.', '卡车发动机怠速的声音、箱子砸在碎石上的闷响和松林里的鸟叫。')


def push(who_en, who_zh):
    return (f'The camera pushes in slowly until {who_en} fill the middle third of the frame.', f'镜头慢慢推近，直到{who_zh}占满画面中间三分之一。')


# ---- 第 1 集
S.T('01-01', '01｜超算大屏上的气温曲线断崖式暴跌，唐博士和林峰对话', 15, SUPER,
    [P('tang_analyst', 'left', "standing at left of center in profile facing frame-right, a tablet hugged to her chest", 'Lin', "her lips parted in dread, her brows pulled together"),
     P('lin_shirt', 'center', "standing in profile facing frame-right, his shoulders squared toward the giant wall screen, his arms at his sides", 'obj:the red temperature curve on the giant wall screen', "his jaw set hard, his brows pulled low", extra=BADGE)],
    'Medium-wide shot, both from the head to the knees, in the middle third of the frame, in the dark supercomputer hall.',
    "<lin_shirt> stands very still, his eyes fixed on the red temperature curve as it falls straight down like a cliff on the giant wall screen while red alarm lights pulse across the dark hall, his jaw set hard and his brows pulled low. <tang_analyst> turns her head toward <lin_shirt> and speaks the first line to <lin_shirt> in a shaky voice, her lips parted in dread and her brows pulled together. <lin_shirt> then turns his head about 45 degrees toward <tang_analyst> and speaks the second line to <tang_analyst> in a calm level voice, his jaw set hard and his brows low.",
    "林峰一动不动地站着，眼睛死死盯着巨大墙屏上那条像悬崖一样直直落下的红色气温曲线，红色警报灯在昏暗的大厅里一明一暗，他下颌绷紧、眉头压低。唐博士转头看向林峰，用发颤的声音对林峰说出第一句，嘴唇微张满是恐惧，眉头拧在一起。林峰接着把头转向唐博士约四十五度，用平稳镇定的声音对唐博士说出第二句，下颌绷紧，眉头压低。",
    voiced('A harsh electronic alarm pulsing over the low hum of the server racks.', '刺耳的电子警报声有节奏地响着，盖过服务器机柜低低的嗡鸣。'),
    lines=[('tang_analyst', "九天后就零下八十度？", 1.5, 'Lin'), ('lin_shirt', "我的模型不会错。", 6.0, 'Tang')],
    cam=push('both of them', '两人'), holds='The frame holds Tang and Lin in front of the giant wall screen.', room={'Lin', 'Tang'}, new=True,
    st={'Lin': (W_BADGE, W_BADGE), 'Tang': ('白大褂，抱着平板', '白大褂，抱着平板')})

S.T('01-02', '02｜会议室里魏局长嘲笑林峰的模型，林峰摘下工牌放在桌上', 15, MEET,
    [P('wei_director', 'left', "standing at the head of the table in profile facing frame-right, one hand flat on the table, leaning toward Lin", 'Lin', "his upper lip curled in contempt, his brows lifted high"),
     P('lin_shirt', 'right', "standing in profile facing frame-left with his arms at his sides", 'Wei', "his lips set in a calm flat line, his brows level", extra=BADGE)],
    'Medium-wide shot, both men from the head to the knees, in the middle third of the frame, in the meeting room.',
    "<wei_director> leans toward <lin_shirt> and speaks the first line to <lin_shirt> in a sneering voice, his upper lip curled in contempt and his brows lifted high. <lin_shirt> unclips the white ID badge from his shirt pocket and sets it flat on the polished table, then speaks the second line to <wei_director> in a cold level voice, his eyes on Wei, his lips set in a cold flat line and his brows level; <wei_director> stares back, his jaw slack and his brows drawn together.",
    "魏局长向林峰倾过身，用嘲讽的声音对林峰说出第一句，上唇鄙夷地卷起、眉毛高高挑起。林峰把胸前的白色工牌摘下来、平放在抛光的桌面上，然后用冰冷平稳的声音对魏局长说出第二句，眼睛看着魏局长，嘴唇抿成冷冷的一条线，眉毛平直；魏局长瞪着他，下巴松垮、眉头拧在一起。",
    SOUND_MEET,
    lines=[('wei_director', "你的模型就是垃圾！", 1.0, 'Lin'), ('lin_shirt', "享受你们最后的九天吧。", 6.5, 'Wei')],
    bg='Behind them five Chinese experts in business clothes sit along the far side of the long table, sneering at Lin, clearly visible and in sharp focus.',
    holds='The frame holds Wei, Lin and five seated experts behind the table.',
    groups=[('Experts', '后', 'Lin')], room={'Lin', 'Wei', 'Experts'}, new=True,
    st={'Lin': (W_BADGE, '白衬衫，工牌放在桌上'), 'Wei': ('灰西装，站在桌首', '灰西装，站在桌首')})

S.T('01-03', '03｜林峰走出大楼被烈日晒得满头汗，走向车边的钱经理，要变卖资产', 15, PLAZA,
    [P('lin_shirt', 'left', "stepping out of the glass entrance doors in profile facing frame-right, one hand raised to shade his eyes", 'Qian', "his eyes narrowed against the glare, his lips pressed flat", extra='sweat beading on his forehead'),
     P('qian_broker', 'right', "standing beside the black sedan in profile facing frame-left, a leather folder held against his chest", 'Lin', "his lips parted in puzzlement, his brows knit")],
    'Medium-wide shot, both men from the head to the knees, in the middle third of the frame, on the sunlit plaza.',
    "<lin_shirt> walks out through the glass entrance doors into the blinding sun and crosses the plaza toward <qian_broker>, one hand shading his brow, sweat beading on his forehead, his eyes narrowed and his lips pressed flat. <lin_shirt> stops in front of <qian_broker> and speaks the first line to <qian_broker> in a flat, certain voice; <qian_broker> listens with his eyes on Lin and then speaks the second line to <lin_shirt> in a tense, nervous voice, his lips parted in puzzlement and his brows knit.",
    "林峰从玻璃大门里走出来，走进刺眼的太阳，穿过广场走向钱经理，一只手遮在额前，额头上冒着汗珠，眼睛被强光晃得眯起，嘴唇抿平。林峰在钱经理面前站住，用平淡而笃定的声音对钱经理说出第一句；钱经理眼睛看着林峰听着，然后用紧绷而紧张的声音对林峰说出第二句，嘴唇微张是困惑，眉头紧皱。",
    SOUND_PLAZA,
    lines=[('lin_shirt', "我名下所有资产，半价全卖。", 2.5, 'Qian'), ('qian_broker', "你是在躲什么吗？", 7.0, 'Lin')],
    bg='The black sedan stands at the curb behind Qian under the blinding sun.', holds='The frame holds Lin, Qian and the parked black sedan.',
    room={'Lin', 'Qian'}, new=True,
    st={'Lin': ('白衬衫，没有工牌', W_NOBADGE), 'Qian': ('藏青三件套，抱着文件夹', '藏青三件套，抱着文件夹')})

S.T('01-04', '04｜林峰告诉钱经理钱很快就没用了，然后抬头看着烈日冷笑', 15, PLAZA,
    [P('lin_shirt', 'left', "standing in profile facing frame-right with his arms at his sides", 'Qian', "his lips set in a cold flat line, his brows level", extra='sweat beading on his forehead'),
     P('qian_broker', 'right', "standing beside the black sedan in profile facing frame-left, the leather folder held against his chest", 'Lin', "his mouth hanging open, his brows pulled up")],
    'Medium two-shot, both men from the head to the knees, in the middle third of the frame, on the sunlit plaza.',
    "<lin_shirt> speaks the line to <qian_broker> in a quiet, certain voice, his eyes steady on Qian, his lips set in a cold flat line and his brows level. <qian_broker> stares at him frozen, his eyes on Lin, his mouth hanging open and his brows pulled up. Then <lin_shirt> tilts his head back and looks up at the blazing white sun, his eyes narrowed against the glare, a cold smirk pulling at one corner of his mouth.",
    "林峰用安静而笃定的声音对钱经理说出那句话，眼睛稳稳地看着钱经理，嘴唇抿成冷冷的一条线，眉毛平直。钱经理愣愣地盯着他，眼睛看着林峰，嘴巴半张，眉毛上提。然后林峰仰起头，望着白晃晃的烈日，眼睛被强光晃得眯起，嘴角冷冷地向上一拉。",
    voiced('Cicadas droning in the heat, then a single bright cash register chime.', '知了在热浪里不停地叫，然后是一声清脆的收银机“叮”。'),
    lines=[('lin_shirt', "九天后钱就没用了。", 1.0, 'Qian')],
    cam=push('both men', '两人'), bg='The black sedan stands at the curb behind Qian under the blinding sun.', holds='The frame holds Lin, Qian and the parked black sedan.', dep=True,
    st={'Lin': ('白衬衫，没有工牌，额头有汗', W_NOBADGE), 'Qian': ('藏青三件套，抱着文件夹', '藏青三件套，抱着文件夹')})

# ---------------------------------------------------------------------------------------------- 第 2 集
b2 = S.episode('剧本第2集｜变卖：致命接盘侠', '林峰的豪宅被苏清月买下，签约时她看到他桌上那张写满字的草稿纸，问他是不是被害妄想；他给了两句医嘱：买泡面和羽绒服，说不定能救你一命。他走后，苏清月让助理查气象局的全部数据、把酒窖囤满，对着窗外的烈日说：他不是妄想，他知道内情。', 2)

S.T('02-01', '01｜苏清月递出黑卡，扫了一眼草稿纸，质问林峰', 15, PENT,
    [P('su_suit', 'left', "seated at the glass table in profile facing frame-right, holding a black card out between two fingers, her other hand resting on a crumpled sheet of handwritten lines", 'Lin', "one brow arched, her lips pressed in a thin sharp line"),
     P('lin_shirt', 'right', "standing across the table in profile facing frame-left with his arms at his sides", 'Su', "his lips set flat, his brows level")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the penthouse living room.',
    "<su_suit> glances down at the crumpled sheet under her hand and speaks the first line to <lin_shirt> in a sharp, amused voice, then lifts her eyes to his face and speaks the second line to <lin_shirt>, one brow arched and her lips pressed in a thin sharp line. <lin_shirt> stands with his eyes on Su, his lips set flat and his brows level.",
    "苏清月低头扫了一眼压在她手下的那张皱巴巴的草稿纸，用锐利带笑意的声音对林峰说出第一句，然后抬起眼睛看着他的脸，对林峰说出第二句，一边眉毛挑起，嘴唇抿成一条细而锐利的线。林峰站着，眼睛看着苏清月，嘴唇抿平，眉毛平直。",
    SOUND_PENT,
    lines=[('su_suit', "羽绒服、煤炭、育苗灯？", 1.0, 'Lin'), ('su_suit', "你是不是被害妄想症？", 5.5, 'Lin')],
    bg='On the glass table beside her lie a signed contract and the crumpled sheet covered in dense handwritten lines, and the floor-to-ceiling windows behind them glare with the white-hot city.',
    holds='The frame holds Su and Lin, the glass table with the contract and the crumpled sheet, and the windows behind them.',
    room={'Su', 'Lin', 'Wen'}, new=True,
    st={'Su': ('黑色真丝衬衫，坐在玻璃桌边', '黑色真丝衬衫，手伸出去递黑卡'), 'Lin': ('白衬衫，站在桌对面', '白衬衫，站在桌对面')})

S.T('02-02', '02｜林峰接过黑卡塞进口袋，给了苏清月两句忠告', 15, PENT,
    [P('su_suit', 'left', "seated at the glass table in profile facing frame-right with her hand still half-extended", 'Lin', "her eyes narrowed, her lips pressed in a thin line"),
     P('lin_shirt', 'right', "standing across the table in profile facing frame-left, taking the black card from her fingers with his right hand", 'Su', "a faint knowing smirk at one corner of his mouth, his brows level")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the penthouse living room.',
    "<lin_shirt> takes the black card from her fingers and tucks it into his shirt pocket, speaks the first line to <su_suit> in a calm, almost gentle voice, then speaks the second line to <su_suit>, a faint knowing smirk at one corner of his mouth and his brows level. <su_suit> watches him, her eyes narrowed and her lips pressed in a thin line.",
    "林峰从她的手指间接过黑卡、塞进衬衫口袋，用平静、近乎温和的声音对苏清月说出第一句，再对苏清月说出第二句，嘴角挂着一丝意味深长的冷笑，眉毛平直。苏清月看着他，眼睛眯起，嘴唇抿成一条细线。",
    SOUND_PENT,
    lines=[('lin_shirt', "多买泡面和羽绒服。", 2.0, 'Su'), ('lin_shirt', "说不定能救你一命。", 6.5, 'Su')],
    bg='On the glass table beside her lie the signed contract and the crumpled sheet, and the floor-to-ceiling windows behind them glare with the white-hot city.',
    holds='The frame holds Su and Lin, the glass table with the contract and the crumpled sheet, and the windows behind them.', dep=True,
    st={'Su': ('黑色真丝衬衫，手伸出去递黑卡', '黑色真丝衬衫，坐在玻璃桌边'), 'Lin': ('白衬衫，站在桌对面', '白衬衫，黑卡在口袋里')})

S.T('02-03', '03｜林峰拎起背包走进玄关，苏清月转头吩咐助理', 15, PENT,
    [P('wen_blazer', 'left', "standing behind Su's chair in profile facing frame-right, the tablet hugged to her chest", 'Lin', "her brows lifted, her lips parted"),
     P('su_suit', 'center', "seated at the glass table in profile facing frame-right with her hands folded on the contract", 'obj:Lin walking away toward the entry hall at frame-right', "her eyes narrowed, her lips pressed in a thin line"),
     P('lin_shirt', 'right', "walking away from the table toward the entry hall in profile facing frame-right", 'obj:the entry hall at frame-right', "his lips set flat, his brows level")],
    'Medium-wide shot, all three from the head to the knees, in the middle third of the frame, in the penthouse living room.',
    "<lin_shirt> walks away from the table toward the entry hall at frame-right, picks up a black backpack from beside the entry and carries it on through the hall until the hall is empty, his lips set flat and his brows level. <su_suit> watches him go, her eyes narrowed and her lips pressed in a thin line, then turns her head toward <wen_blazer> and speaks the line to <wen_blazer> in a low, urgent voice. <wen_blazer> listens and nods once, her brows lifted and her lips pressed together.",
    "林峰离开桌子走向画面右边的玄关，从玄关边拎起一个黑色背包，拿着它继续往里走，直到玄关里空无一人，嘴唇抿平、眉毛平直。苏清月目送他离开，眼睛眯起，嘴唇抿成一条细线，然后转头看向文助理，用低沉而急促的声音对文助理说出那句话。文助理听着，点了一下头，眉毛上提，嘴唇抿紧。",
    voiced('The faint hum of the air conditioner and soft receding footsteps on the floor.', '空调轻微的嗡鸣和渐渐远去的轻轻脚步声。'),
    lines=[('su_suit', "去调气象局全部数据。", 7.0, 'Wen')],
    bg='The three black tactical backpacks stand lined up beside the entry hall at frame-right.', holds='The frame holds Wen, Su and Lin, the glass table and the entry hall with the backpacks.',
    exit={'Lin'},
    st={'Su': ('黑色真丝衬衫，坐在玻璃桌边', '黑色真丝衬衫，坐在玻璃桌边'), 'Lin': ('白衬衫，黑卡在口袋里', None), 'Wen': ('藏青西装外套，站在她身后', '藏青西装外套，站在她身后')})

S.T('02-04', '04｜苏清月站在落地窗前看着烈日，对助理下令并说出判断', 15, PENT,
    [P('wen_blazer', 'left', "standing beside Su in profile facing frame-right, the tablet hugged to her chest", 'Su', "her brows lifted, her lips pressed together"),
     P('su_suit', 'center', "standing at the floor-to-ceiling window in profile facing frame-right with her arms folded", 'obj:the blazing sun in the window at frame-right', "her eyes narrowed, her lips pressed in a thin line")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in front of the floor-to-ceiling window.',
    "<su_suit> stands at the window with her arms folded and speaks the first line to <wen_blazer> in a low, firm voice, her eyes narrowed and her lips pressed in a thin line. <wen_blazer> listens and nods, her eyes on Su, her brows lifted and her lips pressed together. <su_suit> turns her eyes back to the blazing sun in the window and speaks the second line to <wen_blazer> in a low voice, her eyes narrowed and her lips pressed in a thin line.",
    "苏清月抱着双臂站在窗前，用低沉而坚定的声音对文助理说出第一句，眼睛眯起，嘴唇抿成一条细线。文助理听着，点了点头，眼睛看着苏清月，眉毛上提，嘴唇抿紧。苏清月把目光转回窗里那轮烈日，低声对文助理说出第二句，眼睛眯起，嘴唇抿成一条细线。",
    SOUND_PENT,
    lines=[('su_suit', "把酒窖给我囤满。", 1.0, 'Wen'), ('su_suit', "他不是妄想，他知道内情。", 5.5, 'Wen')],
    cam=push('Su', '苏清月'), bg='Behind them the floor-to-ceiling window glares with the white-hot city, the blazing sun hanging in the glass at frame-right.',
    holds='The frame holds Wen and Su in front of the glaring window.',
    st={'Su': ('黑色真丝衬衫，坐在玻璃桌边', '黑色真丝衬衫，站在落地窗前'), 'Wen': ('藏青西装外套，站在她身后', '藏青西装外套，站在她旁边')})

# ---------------------------------------------------------------------------------------------- 第 3 集
b3 = S.episode('剧本第3集｜囤货：隐秘的地下小镇', '深山里的废弃防空洞被林峰搬空了整座冷库：大厅里的物资堆成了山；他在隧道口催卡车卸货，把一根金条递给物流老板赵虎打发走；赵虎和小弟彪子往卡车走，林峰站在洞口里面按下遥控器；山坡上的入口消失，只剩一块长满青苔的岩石；赵虎说“有钱的傻子，记住这地方”；林峰按下红色总控按钮，发电机一台台启动。', 3)

S.T('03-01', '01｜无人镜头：地下大厅里的物资堆成了山', 15, HALL, [],
    'Wide shot down the central aisle of the vast underground hall, in the middle third of the frame, no person in the frame.',
    "Under the hard work lamps the vast concrete hall is stacked high with steel crates, pallets of steak boxes, crates of lobsters on ice, rows of generators, big water tanks and white medical cases, dust drifting through the lamp beams, a forklift standing idle in the aisle.",
    "硬朗的工作灯下，巨大的混凝土大厅里堆满了高高的钢箱、成托盘的牛排箱、冰上的龙虾箱、一排排发电机、巨大的水箱和白色医疗箱，灰尘在灯光里飘着，过道上停着一辆没人开的叉车。",
    breathy('The low hum of a generator and the echo of dripping water in a huge concrete hall.', '一台发电机低低的嗡鸣，和巨大混凝土大厅里滴水的回声。'),
    cam=('The camera pushes in slowly down the central aisle until the far wall fills the frame.', '镜头顺着中央过道慢慢推近，直到远处的墙占满画面。'),
    holds='The frame holds the stacked crates, the generators and the aisle, and no person.', room=set(), new=True)

S.T('03-02', '02｜隧道口，林峰催卡车卸货，递出金条打发赵虎', 15, TUNNEL,
    [P('lin_work', 'left', "standing at the tunnel mouth in profile facing frame-right, a heavy gold bar held in his right hand at his side", 'Zhao', "his lips set flat, his brows level"),
     P('zhao_boss', 'right', "standing beside the open back of the box truck in profile facing frame-left, his thumbs hooked in his vest", 'Lin', "a greedy sly leer on his lips, his brows lifted")],
    'Medium two-shot, both men from the head to the knees, in the middle third of the frame, on the gravel clearing.',
    "<lin_work> speaks the first line to <zhao_boss> in a flat, impatient voice, his eyes steady on Zhao, his lips set flat and his brows level. <zhao_boss> watches him, a greedy sly leer on his lips and his brows lifted, then gives a slow nod. <lin_work> holds out the heavy gold bar and speaks the second line to <zhao_boss> in a cold voice; <zhao_boss> takes the gold bar in both hands and weighs it, his eyes on the bar, his lips parted in greed.",
    "林峰用平淡而不耐烦的声音对赵虎说出第一句，眼睛稳稳看着赵虎，嘴唇抿平，眉毛平直。赵虎把拇指勾在背心上看着他，嘴唇挂着贪婪狡猾的邪笑，眉毛上挑，然后慢慢点了点头。林峰把那根沉甸甸的金条递出去，用冰冷的声音对赵虎说出第二句；赵虎用双手接过金条掂了掂，眼睛盯着金条，贪婪地张着嘴。",
    SOUND_TUNNEL,
    lines=[('lin_work', "再快点卸货，时间不多了！", 1.0, 'Zhao'), ('lin_work', "这是尾款，拿了就走。", 7.0, 'Zhao')],
    bg="Behind Zhao the box truck's open rear is packed with steel crates.", holds='The frame holds Lin and Zhao, the tunnel mouth and the box truck behind them.',
    room={'Lin', 'Zhao', 'Biao'}, new=True,
    st={'Lin': ('深灰亨利衫和工装背心，手里拿着金条', '深灰亨利衫和工装背心，金条已递出'), 'Zhao': ('黑色皮背心，站在卡车旁', '黑色皮背心，金条在手里')})

S.T('03-03', '03｜赵虎和彪子走向卡车，林峰站在洞口里面的暗处，举起遥控器按下', 15, TUNNEL,
    [P('lin_work', 'left', "standing just inside the dark tunnel mouth in profile facing frame-right, a small black remote in his right hand at his side", 'obj:the two men walking away across the gravel clearing', "his lips set in a cold line, his brows level"),
     P('zhao_boss', 'center', "walking away across the gravel clearing in profile facing frame-right, the gold bar tucked under his arm", 'obj:the box truck at frame-right', "a smug set to his lips, his brows lifted"),
     P('biao_thug', 'right', "walking beside Zhao in profile facing frame-right, glancing around the hillside", 'obj:the box truck at frame-right', "his lips parted, his brows pulled up")],
    'Wide shot, all three from the head to the feet, in the middle third of the frame, on the gravel clearing.',
    "<zhao_boss> and <biao_thug> walk away across the gravel clearing toward the box truck at frame-right with their backs mostly to the tunnel; <lin_work> stands just inside the dark tunnel mouth watching them go, then raises the small black remote and presses it with his thumb, his lips set in a cold line and his brows level.",
    "赵虎和彪子背对着隧道口，穿过碎石空地走向画面右边的卡车；林峰站在洞口里面的暗处看着他们走远，然后抬起那个黑色小遥控器，用拇指按下去，嘴唇抿成冷冷的一条线，眉毛平直。",
    breathy('Boots crunching on gravel and a truck engine idling.', '靴子踩在碎石上的嘎吱声和卡车发动机怠速的声音。'),
    holds='The frame holds Lin just inside the tunnel mouth and Zhao and Biao walking toward the box truck.',
    st={'Lin': ('深灰亨利衫和工装背心，金条已递出', '深灰亨利衫和工装背心，站在洞口里面，手里拿着遥控器'), 'Zhao': ('黑色皮背心，金条在手里', '黑色皮背心，金条夹在腋下')})

S.T('03-04', '04｜同一座山坡：入口不见了，只剩青苔岩石和枯树桩，彪子和赵虎说话', 15, HIDDEN,
    [P('biao_thug', 'left', "standing on the gravel clearing in profile facing frame-left, one arm pointing toward the hillside", 'obj:the moss-covered boulder and the dead stump on the hillside at frame-left', "his eyes wide, his brows pulled up, his lips parted"),
     P('zhao_boss', 'right', "standing beside the box truck in profile facing frame-left, the gold bar tucked under his arm", 'Biao', "a sly greedy leer on his lips, his brows lifted")],
    'Medium two-shot, both men from the head to the knees, in the middle third of the frame, on the gravel clearing.',
    "<biao_thug> points at the hillside with one arm and turns his head toward <zhao_boss> to speak the first line to <zhao_boss> in a startled voice, his eyes wide and his brows pulled up. <zhao_boss> glances at the hillside, then turns his eyes back to <biao_thug> and speaks the second line to <biao_thug> in a low sly voice, a sly greedy leer on his lips and his brows lifted.",
    "彪子伸手指着山坡，转头看向赵虎，用吃惊的声音对赵虎说出第一句，眼睛睁大、眉毛上提。赵虎朝山坡瞥了一眼，然后把目光转回彪子，用低沉狡猾的声音对彪子说出第二句，嘴唇挂着狡猾贪婪的邪笑，眉毛上挑。",
    SOUND_TUNNEL,
    lines=[('biao_thug', "洞口不见了，老板！", 1.5, 'Zhao'), ('zhao_boss', "有钱的傻子，记住这地方。", 6.0, 'Biao')],
    bg='Behind them the moss-covered boulder and the dead stump sit on the quiet hillside at frame-left where the tunnel mouth was, and the box truck stands at frame-right.',
    holds='The frame holds Biao and Zhao, the boulder and the stump on the hillside, and the box truck.',
    room={'Zhao', 'Biao'}, new=True,
    st={'Zhao': ('黑色皮背心，金条夹在腋下', '黑色皮背心，金条夹在腋下')})

S.T('03-05', '05｜地下控制台：林峰按下红色总控按钮，发电机依次启动，灯亮起来', 15, CORE,
    [P('lin_work', 'center', "standing at the steel console in profile facing frame-left, his right thumb on the red button under the opened flip cover", 'obj:the red button on the console', "his jaw set, his lips pressed flat")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the control corner.',
    "<lin_work> presses the red button with his thumb, his eyes on the button, his jaw set and his lips pressed flat; the three matte-grey generators behind him rumble to life one after another, warm yellow lamps come on across the concrete walls and the big red clock above the console glows red.",
    "林峰用拇指按下红色按钮，眼睛盯着按钮，下颌绷紧，嘴唇抿平；他身后三台哑光灰色的发电机一台接一台地启动，混凝土墙上的暖黄色灯一盏盏亮起来，控制台上方那只大红色电子钟亮起红光。",
    breathy('Three heavy generators starting up one after another into a smooth low hum and a relay clicking on the console.', '三台沉重的发电机一台接一台地启动、汇成平稳低沉的嗡鸣，控制台上继电器咔哒一声。'),
    cam=push('Lin and the console', '林峰和控制台'),
    holds='The frame holds Lin alone at the console, the three generators and the red clock behind him.', room={'Lin'}, new=True,
    st={'Lin': ('深灰亨利衫和工装背心', '深灰亨利衫和工装背心')})

# ---------------------------------------------------------------------------------------------- 第 4 集
b4 = S.episode('剧本第4集｜降临：地狱降临与极致反差', '夏日午后的烧烤摊，一堵白色雾墙从街尾滚来，人们抬头；下一个画面，同一条街已经被冻成冰雕，天空挂着绿色极光。地下安全屋里林峰光脚煎牛排，心里说“他们都说我疯了”；监控屏上一个陌生男人在暴风雪里倒下；酒窖里苏清月和助理裹着被子发抖；排气管口被冰封，红灯闪起，林峰的刀叉停在牛排上——他必须去地表。', 4)

S.T('04-01', '01｜夏日午后烧烤摊：街尾滚来一堵白色雾墙，食客们抬头、站起来', 15, STREET, [],
    'Wide shot of the street barbecue stand and the long avenue, in the middle third of the frame, no named person in the frame.',
    "The Chinese diners on plastic stools at the folding tables lift their heads and stare toward the far end of the avenue, where a towering wall of pale white mist rolls slowly toward them, their mouths open and their brows pulled up; the cook at the grill freezes with his tongs in mid-air above the glowing coals; the diners rise from their stools one by one, still staring at the mist.",
    "坐在折叠桌边塑料凳上的食客们抬起头，望向大道尽头——一堵高耸的苍白雾墙正慢慢朝他们滚过来，他们张着嘴、眉毛上提；烤炉边的摊主举着夹子停在炭火上方；食客们一个接一个从凳子上站起来，眼睛仍盯着那堵雾墙。",
    breathy('A low rising roar of wind, the grill crackling and a nervous murmur of crowd noise.', '低低上涨的风的轰鸣、烤炉噼啪作响，和人群不安的嘈杂声。'),
    cam=('The camera pushes in slowly until the wall of mist fills the middle third of the frame.', '镜头慢慢推近，直到雾墙占满画面中间三分之一。'),
    bg='At the far end of the avenue a towering wall of pale white mist rolls toward the street, and the diners at the folding tables lift their heads toward it, clearly visible and in sharp focus.',
    holds='The frame holds the grill, the diners at the folding tables and the wall of white mist at the far end of the avenue.',
    groups=[('Crowd', '中', 'obj:the wall of white mist at the far end of the avenue')], room={'Crowd'}, new=True)

S.T('04-02', '02｜同一条街已经被冻成冰雕，天空挂着绿色极光', 15, FROZEN, [],
    'Wide shot of the frozen street, in the middle third of the frame, no living person in the frame.',
    "Every surface is sheathed in thick white frost under a green aurora: life-size ice statues of diners sit frozen at the tables mid-gesture, one raising a beer bottle, the grill's flames frozen into a jagged orange-white ice sculpture, snow dust drifting across the silent street.",
    "所有的表面都覆着厚厚的白霜，头顶是绿色极光：食客们的真人大小的冰雕保持着动作坐在桌边，其中一个举着啤酒瓶，烤炉的火焰冻成参差的橙白色冰雕，雪沫在寂静的街上飘过。",
    breathy('A deep hollow wind howling over the silent street and the faint creak of ice.', '深沉空洞的风声在寂静的街上呼啸，和冰层轻轻的吱嘎声。'),
    cam=('The camera pushes in slowly until the frozen figure holding the beer bottle fills the frame.', '镜头慢慢推近，直到举着啤酒瓶的冰雕占满画面。'),
    holds='The frame holds the frozen street, the ice sculptures and the aurora sky, and no living person.', room=set(), new=True)

S.T('04-03', '03｜地下安全屋：林峰光脚站在炉灶前翻动黄油里的牛排，一句内心独白', 15, LIVING,
    [P('lin_home', 'left', "standing at the stove seen mostly from behind in a three-quarter back view, his head bowed over the pan, turning a thick steak in a sizzling pan with a pair of tongs", 'obj:the thick steak sizzling in the pan', "his jaw relaxed, his lips closed, his brows soft")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, at the kitchen stove.',
    "<lin_home> turns the thick steak over in the sizzling butter with a pair of tongs, his eyes on the pan, his face turned down toward it, his bare feet on the soft cream rug, his jaw relaxed, his lips closed and his brows soft; butter foams and steam curls up from the pan. The line is his inner voice-over, heard over the scene while his lips stay closed and do not move.",
    "林峰用夹子把厚厚的牛排在滋滋作响的黄油里翻面，眼睛看着锅，脸朝下对着锅，光脚踩在柔软的奶白色地毯上，下颌放松、嘴唇闭着、眉毛舒展；黄油冒着泡，锅里升起热气。那句台词是他的内心独白，在画面上方响起，他的嘴唇一直闭着、一动不动。",
    breathy('Butter sizzling in the pan and the quiet hum of the air system.', '黄油在锅里滋滋作响，和空气循环系统安静的嗡鸣。'),
    cam=push('Lin and the pan', '林峰和平底锅'),
    holds='The frame holds Lin alone at the stove.', room={'Lin'}, new=True, vo=[('lin_home', "他们都说我疯了。", 3.0, 'Lin')],
    st={'Lin': ('灰色棉质家居服，光脚，在炉灶前', '灰色棉质家居服，光脚，在炉灶前')})

S.T('04-04', '04｜监控墙：一个穿薄外套的男人在暴风雪里倒下，林峰一动不动', 15, LIVING,
    [P('lin_home', 'left', "standing before the wall of monitors in profile facing frame-right with his arms folded", 'obj:the center monitor showing a man in the blizzard', "his jaw tight, his lips pressed flat, his brows low")],
    'Medium-wide shot, the figure from the head to the knees, in the middle third of the frame, in front of the monitor wall.',
    "<lin_home> stands before the wall of monitors with his arms folded, his eyes on the center screen where a lone man in a thin jacket staggers through the blizzard and falls face-down in the snow; <lin_home> does not move, his jaw tight, his lips pressed flat and his brows low.",
    "林峰抱着双臂站在监控墙前，眼睛盯着中间那块屏幕——一个穿薄外套的男人在暴风雪里踉踉跄跄地走着，然后脸朝下倒在雪里；林峰一动不动，下颌绷紧，嘴唇抿平，眉头压低。",
    breathy('The howl of wind from a monitor speaker and the faint crackle of ice on a camera lens.', '监控喇叭里传出的风的呼啸，和摄像头镜头上冰层轻微的碎裂声。'),
    cam=push("the center monitor and Lin's profile", '中间那块监控屏和林峰的侧脸'),
    bg='On the wall of security monitors the center screen shows a white blizzard where a lone man in a thin jacket staggers forward through deep snow with frost on his face, and the other screens show the buried forest and drifts of snow and ice.',
    holds='The frame holds Lin alone in front of the monitor wall.',
    st={'Lin': ('灰色棉质家居服，光脚，在炉灶前', '灰色棉质家居服，光脚，站在监控墙前')})

S.T('04-05', '05｜酒窖里苏清月和文助理冻得发抖，互相说话', 15, CELLAR,
    [P('su_cold', 'left', "sitting on an upturned crate in profile facing frame-right, her arms wrapped around herself, her breath fogging", 'Wen', "her lips blue-purple and trembling, her brows drawn together"),
     P('wen_cold', 'right', "sitting beside her on a stack of water crates in profile facing frame-left, her gloved hands pressed under her arms, her breath fogging", 'Su', "her lips pressed tight and shaking, her brows lifted")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the freezing cellar.',
    "<su_cold> shivers under the blanket and speaks the first line to <wen_cold> through chattering teeth, her breath fogging, her lips blue-purple and trembling and her brows drawn together. <wen_cold> turns her head toward Su and speaks the second line to <su_cold>, her breath fogging, her lips pressed tight and shaking and her brows lifted.",
    "苏清月在毯子下发抖，牙齿打着颤对文助理说出第一句，呼出的气凝成白雾，嘴唇发青发抖，眉头拧在一起。文助理转头看向苏清月，对苏清月说出第二句，呼出白雾，嘴唇抿紧发抖，眉毛上提。",
    voiced('A faint howl of wind through the stone walls above and the soft click of chattering teeth.', '上面石墙缝里传来的风的呼啸，和牙齿打颤轻轻的咔嗒声。'),
    lines=[('su_cold', "那个疯子现在肯定暖和着呢。", 1.0, 'Wen'), ('wen_cold', "他早就警告过您了。", 5.5, 'Su')],
    bg='Behind them stacks of canned food and crates of bottled water stand against the right wall, and their breath fogs in the lantern light.',
    holds='The frame holds Su and Wen on their crates, with the lantern and the stacks of supplies around them.', room={'Su', 'Wen'}, new=True,
    st={'Su': ('奶白色羽绒服，裹着毯子，坐在木箱上', '奶白色羽绒服，裹着毯子，坐在木箱上'), 'Wen': ('红色羽绒服，坐在水箱上', '红色羽绒服，坐在水箱上')})

S.T('04-06', '06｜林峰的刀叉停在牛排上，红光闪在脸上，他放下刀，看向通往地表的舱门', 15, LIVING,
    [P('lin_home', 'left', "sitting at the small round dining table in profile facing frame-right, a knife and fork resting over a plated steak", 'obj:the pulsing red monitor on the wall at frame-right', "his jaw tight, his lips pressed flat, his brows low")],
    'Medium shot, the figure from the head to the waist, in the middle third of the frame, at the dining table.',
    "<lin_home> stops with the knife and fork resting over the steak, his eyes on the pulsing red monitor on the wall, red light washing over his face, and slowly lays the knife down on the plate, then lifts his eyes to the heavy round steel hatch door in the right wall, his jaw tight, his lips pressed flat and his brows low.",
    "林峰停住，刀叉悬在牛排上，眼睛盯着墙上一明一暗的红色监控屏，红光在他脸上扫过，他慢慢把刀放在盘子上，然后抬眼看向右墙上那扇厚重的圆形钢制舱门，下颌绷紧，嘴唇抿平，眉头压低。",
    breathy('The rhythmic red alarm beeping over the faint clink of a knife settling on a plate.', '有节奏的红色警报滴声，盖过刀轻轻搁在盘子上的一声叮。'),
    cam=push('Lin', '林峰'),
    bg='The wall monitor at frame-right shows the exhaust pipe tip on a snowy hillside crusted over with thick white ice, a red frame flashing around the screen and a red warning lamp pulsing beside it, washing red light across the room, and the heavy round steel hatch door stands in the right wall beyond it.',
    holds='The frame holds Lin alone at the dining table, the red monitor and the steel hatch door.', room={'Lin'}, new=True,
    st={'Lin': ('灰色棉质家居服，光脚，坐在圆桌边', '灰色棉质家居服，光脚，坐在圆桌边')})

doc = S.finish()
