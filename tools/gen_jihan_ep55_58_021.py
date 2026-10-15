#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 55–58 集，追加稿 021（2026-10-15 夜，hh 挂机，要 20 集；A／B 两种写法按剧情混用）。
故事见 `剧本/第55-74集_结局版大纲.md`。以 020（第 51–54 集，A 写法）的 JSON 为底，必须等 020 在插件里全部跑完再追加；追加窗口不要勾每集／总／任务秒数。
写法分配（我的判断）：
  第 55 集 天然的冰川墓碑：A（慢、重要：五百冰雕的震撼、“只要不开就用不着关”的伏笔、林峰左手合不拢）；
  第 56 集 全自动的绿洲：B（日常琐事：吃喝、拌嘴、母鸡下蛋，快速完成）；
  第 57 集 荧光稻田：前半 A（发现的惊奇）＋收割 B ＋“镰刀脱手”A（伏笔）；
  第 58 集 舌尖上的避难所：诊断 A（情绪）＋吃饭／警报 B。
偏离原大纲：原 55 集“冬眠”台词不用（不写爵士乐）；原 56 集葡萄汁＋接吻改成额头；原 57 集“松茸＋盲鱼”前面已拍（第 39–40 集），这里改成长出“荧光稻”（新进展：稻米），
  苏清月“干呕、怀孕”整条线不要；原 58 集“潜望镜工程”挪到第 59 集；新增：林峰左手神经冻伤的诊断（给结局埋伏笔）、水位浮标开始升。
H3 方面的风险（交稿时单列，不算我的错）：
  · 55-01 几百个冰雕的雪原（人群太多、冰雕可能画成真人）、55-02 冰里的人脸；55-06 手指只弯一半（细小手部动作）；
  · 56-01 机械臂剪葡萄；56-02／56-03 十五秒多句（B 写法塞 5 句，后几句可能被挤到片尾）；56-03 母鸡和篮子里的蛋；
  · 57 荧光稻会发光（文字可能不发光）；57-04 镰刀从左手滑落（掉落动作）；57-05 两只手握在一起；
  · 58-01 手电照手掌的细小动作；58-03 米饭热气；58-06 水位浮标的细小升高；
  · B 写法 15 秒塞 5 句台词，开口会不会更早、语速会不会真的变快，是这批要看的。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
import _jihan_base7 as B7
from _jihan_base7 import *
import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407)
OUT = '合并稿/021_第55-58集_冰川墓碑全自动绿洲荧光稻田舌尖上的避难所_制作稿_追加'
S = Session('合并稿/020_第51-54集_天崩地裂体温底线黑暗手术重见光明_制作稿_追加.json', OUT, 90000)
B6.S = S
B7.S = S

# ---------------------------------------------------------------------------------------------- 衣着
SU_WORK = "in a cream knit sweater with the sleeves pushed up to her elbows, black thermal leggings and soft boots, her long black hair tied back in a loose low ponytail"
LIN_WORK = "in a charcoal henley with the sleeves pushed up to his forearms, dark cargo trousers and soft boots"
SU_CLINIC = "in a cream knit sweater and black thermal leggings, thick grey socks, her long black hair loose"
LIN_CLINIC = "in a soft grey cotton henley with the left sleeve rolled up to the elbow and loose dark lounge pants"

# ---------------------------------------------------------------------------------------------- 场景（Scene 对象）
SOFA_SCREEN = Scene('bunker_sofa', SOFA.end,
                    " Fixed stage layout: seen from the front of the room, the deep brown leather sofa stands in the middle of the frame facing the wall of small security monitors at the far end of the room behind the camera; a thick grey cashmere blanket lies over the sofa; a low wooden coffee table in front of it holds two white mugs; the open kitchen with the black-and-gold stove glows at frame-left.")
SOFA_HAND = Scene('bunker_sofa', SOFA.end,
                  " Fixed stage layout: a close low view of a man's knee on the deep brown leather sofa filling the middle of the frame, his left hand resting palm-down on his knee; the grey cashmere blanket and the edge of a coffee table are soft blurs behind.")
ICE_ARMY = Scene('ice_army', " A black night with a blood-red full moon and a faint green aurora, the ice glittering on every surface.",
                 " Fixed stage layout: a vast open snowfield under a blood-red full moon fills the frame; hundreds of men in black winter gear and fur hats stand frozen in violent running and shouting poses across the whole field, each one fully sheathed in clear glittering ice, among a dozen heavy black tracked trucks and mortar tubes also sheathed in ice; nothing moves.")
ICE_CHIEF = Scene('ice_chief', " A black night with a blood-red full moon, the ice glittering with red and green light.",
                  " Fixed stage layout: a close view of one frozen man filling the middle of the frame, encased in clear ice from head to boots, a black leather patch over his left eye, his right arm raised with a black radio handset clenched in his fist, his mouth open in a scream, frost on his lashes; the ranks of other ice figures standing sharp and still behind him; nobody alive in the scene.")
GRAPE = Scene('eden', EDEN.end,
              " Fixed stage layout: a long overhead trellis hung with heavy bunches of dark purple grapes fills the middle of the frame under rows of hanging pink-violet grow lamps; a slim steel robotic arm on a ceiling rail reaches in from the top of the frame with a small blade; a clear washing tray stands at frame-right; the white hydroponic channels stand behind.")
KITCH_MORN = Scene('bunker_living', LIVING.end,
                   " Fixed stage layout: the open kitchen with the black-and-gold stove and a long marble counter is at frame-left, a clear glass jug and a cutting board of green and purple grapes on the counter; a thick cream wool rug and the small round wooden dining table fill the middle of the frame; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
EGGS = Scene('eden', EDEN.end,
             " Fixed stage layout: long tiers of white hydroponic channels full of lettuce and tomato plants fill the middle of the frame under rows of hanging pink-violet grow lamps; a small straw-lined hen pen with four plump brown hens stands at frame-left in front of the steel staircase; the warm incubator box with its red heat lamp stands at frame-right.")
PADDY_WIDE = Scene('paddy_cave', " Soft blue moss light and warm turquoise water light fill a vast steaming natural cavern.",
                   " Fixed stage layout: a vast natural cavern of dark rock covered in softly glowing blue moss; along the near edge of a steaming turquoise hot spring pool stands a wide terraced paddy of knee-high rice stalks whose heavy grain heads glow pale gold-green; a narrow dark tunnel mouth is at frame-left.")
PADDY_EDGE = Scene('paddy_cave', PADDY_WIDE.end,
                   " Fixed stage layout: a flat rock path runs along the front of the frame; behind it a dense terraced paddy of rice stalks as tall as a man's waist with heavy glowing pale-gold grain heads fills the middle of the frame; the steaming turquoise pool and the blue moss wall are at the back.")
PADDY_CLOSE = Scene('paddy_cave', PADDY_WIDE.end,
                    " Fixed stage layout: a close view of two hands clasped together in the middle of the frame against a blurred background of glowing rice stalks and steam; nobody else in the scene.")
LIV_DINNER = Scene('bunker_living', LIVING.end,
                   " Fixed stage layout: the open kitchen with the black-and-gold stove is at frame-left; the small round wooden dining table fills the middle of the frame laid with two white bowls of glistening white rice, a clay pot of milky white fish soup, a plate of golden fried eggs and two pairs of chopsticks; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
LIV_TABLE = Scene('bunker_living', LIVING.end,
                  " Fixed stage layout: the open kitchen with the black-and-gold stove is at frame-left; two people's places at the small round wooden dining table fill the middle of the frame with bowls of white rice and a clay pot of fish soup; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
BUOY = Scene('pump_room', " Cool white light from a work lamp falls on the clear tank and pipes of the small pump room.",
             " Fixed stage layout: a tall clear water tank fills the middle of the frame with a red float marker bobbing on the water inside it beside a vertical white scale with painted tick marks; clear water pipes run along the wall at frame-left; the green start key on a steel panel is at frame-right; nobody in the scene.")

# ---------------------------------------------------------------------------------------------- 光和空气
AE = lambda en, zh: (en, zh)

# ================================================================================================ 第 55 集（A）
mode('A')
b55 = S.episode('剧本第55集｜天然的冰川墓碑', '监控里，血色的满月和绿色的极光下，雪原上整整齐齐站满了冻成冰雕的五百个暴徒，独眼统帅还举着对讲机惊恐地张着嘴；林峰说温压弹是他们逃跑时自己引爆的，冲击波震塌了我们，也冻住了他们；苏清月问现在是不是地球上唯一的绿洲，林峰说是我们的家；伊甸报告泄洪总闸的电动机构受损只能手动，手轮锁只认林峰的手掌，林峰说只要不开就用不着关，他悄悄握了握左手，五根手指只能合到一半。', 55)
new_scene(b55, 'ice_army', '冻成冰雕的五百人的雪原（血红的满月和绿色极光，密密麻麻的人形和卡车全裹在透明的冰里）',
          'A vast night snowfield under a blood-red full moon and a faint green aurora, hundreds of men in black winter gear and fur hats and a dozen heavy black tracked trucks all sheathed in clear glittering ice, frozen in violent poses.',
          '血红的满月和淡淡的绿色极光下，一望无际的雪原上，几百个穿黑色冬装、戴毛皮帽的男人和十几辆黑色履带卡车全都裹在闪亮的透明冰里，凝固在狂乱的姿势里。',
          'the field of ice-sheathed men and trucks')
new_scene(b55, 'ice_chief', '冰雕统帅的特写（左眼戴黑色眼罩的男人从头到脚裹在透明的冰里，举着对讲机，嘴张开像在尖叫，睫毛上挂着霜）',
          'A close view of a frozen man with a black eye patch encased in clear ice from head to boots, a black radio handset clenched in his raised fist, his mouth open in a scream, frost on his lashes, ranks of ice figures standing sharp and still behind.',
          '一个左眼戴黑色眼罩的男人从头到脚裹在透明的冰里，高举的拳头里攥着黑色对讲机，嘴张开像在尖叫，睫毛上挂着霜，背后是模糊的一排排冰雕。',
          'the iced man with the radio handset')

INS('55-01', '01｜地表雪原：血红的满月和绿色的极光下，几百个裹在透明冰里的人和卡车凝固在雪原上，一动不动，冰面闪着红绿的光', 9, ICE_ARMY,
    'Wide high shot of the whole snowfield, the field of ice figures filling the middle third of the frame, nobody alive in the scene.',
    "Under a blood-red full moon and a faint green aurora, hundreds of men and a dozen heavy trucks stand sheathed in clear ice across the whole snowfield, frozen in violent poses, the ice glittering red and green. Nothing moves.",
    "血红的满月和淡淡的绿色极光下，几百个男人和十几辆重型卡车裹在透明的冰里，凝固在狂乱的姿势里，冰面闪着红绿的光，铺满整片雪原。一动不动。",
    Q('A long low howl of wind over a dead white plain and the faint glassy tick of ice.', '风吹过死寂的白色平原长长的低啸和冰细细的玻璃般的嘀嗒声。'),
    'The frame holds the snowfield of ice figures and trucks, and nobody alive in the scene.',
    rise('the whole frozen army below the red moon', '红色满月下整支冻住的军队'),
    AE("The blood-red moon bathes the glittering ice in red while a green aurora ripples overhead and fine snow crystals drift through the beams of light.",
       "血红的月光把闪亮的冰面染成红色，绿色的极光在头顶流动，细细的雪晶在光柱里飘。"))

INS('55-02', '02｜冰雕特写：左眼戴黑色眼罩的独眼统帅从头到脚裹在冰里，高举着对讲机，嘴巴张开，睫毛上挂着霜', 8, ICE_CHIEF,
    'Close shot of the iced man, his face in the middle third of the frame, nobody alive in the scene.',
    "A man with a black eye patch stands sheathed in clear ice from head to boots with a black radio handset clenched in his raised fist and his mouth open in a scream, frost clinging to his lashes. Nothing moves.",
    "一个左眼戴黑色眼罩的男人从头到脚裹在透明的冰里，高举的拳头里攥着黑色对讲机，嘴巴张开像在尖叫，睫毛上挂着霜。一动不动。",
    Q('A deep hush, the faint creak of settling ice and a thin wind.', '深深的寂静、冰层落定时轻轻的吱嘎声和一缕细细的风。'),
    'The frame holds the iced man with the radio handset, and nobody alive in the scene.',
    push1('the frozen face and the raised handset', '冻住的脸和高举的对讲机'),
    AE("Red moonlight glows through the clear ice like a lamp, the green aurora glints on the black eye patch and tiny ice crystals sparkle on the raised handset.",
       "红色的月光像一盏灯一样透过透明的冰，绿色的极光在黑色眼罩上闪着，高举的对讲机上细小的冰晶闪闪发光。"))

DL('55-03', '03｜监控室沙发：林峰和苏清月裹着毯子坐在沙发上看监控墙，苏清月问外面五百个人是不是真的都在，林峰说都在、温压弹是他们自己引爆的，她说所以山才会裂开，他说冲击波震塌了我们、也冻住了他们，然后把热牛奶递给她', SOFA_SCREEN,
   [P('su_cozy', 'left', "sitting curled on the deep brown leather sofa in three-quarter profile facing frame-right, the grey cashmere blanket over her knees, her head turned toward him", 'Lin', "her lips parted, her eyes wide and uneasy, her brows pulled together", outfit=SU_CLINIC),
    P('lin_home', 'right', "sitting beside her in profile facing frame-left, one arm along the back of the sofa behind her, a white mug on the coffee table in front of him, his head turned toward her", 'Su', "his jaw easy, his eyes calm and dark, his brows level", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, on the sofa.',
   [('su_cozy', "那五百个人，真的都在？", 'lin_home', 'low uneasy', '低沉不安'),
    ('lin_home', "都在。温压弹被自己人引爆了。", 'su_cozy', 'low calm', '低沉平静'),
    ('su_cozy', "所以山才会裂开。", 'lin_home', 'quiet realizing', '安静而恍然'),
    ('lin_home', "震塌我们，也冻住他们。", 'su_cozy', 'low steady', '低沉平稳')],
   V('The soft crackle of the stove and the faint hum of the monitor wall.', '炉灶轻轻的噼啪声和监控墙微弱的嗡鸣。'),
   AE("Warm amber lamp light lies across the blanket while the cold white-blue glow of the monitor wall washes over their faces from the front, a rich teal-and-orange contrast, and steam curls from a white mug.",
      "温暖的琥珀色灯光落在毯子上，监控墙冷冷的白蓝色光从前面洗过他们的脸，形成浓郁的青橙对比，一只白色马克杯里热气卷着。"),
   pre_en='The cold glow of the monitor wall plays over their faces.', pre_zh='监控墙冷冷的光在他们的脸上流动。',
   post_en='after the last line <lin_home> lifts the white mug from the coffee table and puts it into her hands',
   post_zh='最后一句之后，林峰从茶几上拿起那只白色马克杯，放进她的手里',
   cam=slide('toward frame-right', '右', 'the two of them fill the middle third of the frame', '两人占满画面中间三分之一'),
   bg='Behind the camera the monitor wall glows and the black-and-gold stove glows ember-orange at frame-left.')

DL('55-04', '04｜监控室沙发：苏清月捧着热牛奶靠在林峰肩上问这里是不是现在地球上唯一的绿洲，林峰说不只是绿洲，她问那还是什么，他说是我们的家', SOFA_SCREEN,
   [P('su_cozy', 'left', "sitting on the sofa in profile facing frame-right, both hands around a white mug of hot milk, her head resting on his shoulder and tilted up toward him", 'Lin', "her lips curving in a small tired sweet smile, her eyes soft and bright, her brows relaxed", outfit=SU_CLINIC),
    P('lin_home', 'right', "sitting beside her in profile facing frame-left, one arm around her shoulders, his head bent toward her", 'Su', "his jaw loosening, one corner of his mouth lifting, his eyes dark and warm, his brows soft", outfit=LIN_CLINIC)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, on the sofa.',
   [('su_cozy', "我们这里，是不是唯一的绿洲了？", 'lin_home', 'soft tired', '轻轻疲惫'),
    ('lin_home', "不只是绿洲。", 'su_cozy', 'low warm', '低沉温暖'),
    ('su_cozy', "那还是什么？", 'lin_home', 'soft curious', '轻轻好奇'),
    ('lin_home', "是我们的家。", 'su_cozy', 'low gentle', '低沉温柔')],
   V('The soft crackle of the stove and the quiet hush of a warm room.', '炉灶轻轻的噼啪声和温暖屋子里安静的低语。'),
   AE("Honey-gold lamp light wraps the sofa in warmth, steam from the hot milk curls up past her cheek and the cold blue monitor glow only grazes the edge of the frame.",
      "蜂蜜般的金色灯光把沙发裹进暖意里，热牛奶的热气从她脸颊旁卷上去，监控墙冷蓝色的光只擦过画面边缘。"),
   post_en='after the last line she rests her head on his chest and he lays his cheek against her hair',
   post_zh='最后一句之后，她把头靠在他的胸口，他把脸颊贴在她的头发上',
   cam=push('both of them', '两人'), bg='Behind them the black-and-gold stove glows ember-orange at frame-left.')

DL('55-05', '05｜监控室沙发：伊甸报告泄洪总闸的电动机构受损，现在只能手动，苏清月说那就别用它，林峰说只要不开就用不着关，伊甸说手轮锁只认林先生的手掌', SOFA_SCREEN,
   [P('su_cozy', 'left', "sitting on the sofa in profile facing frame-right, the white mug in her hands, her head lifted from his shoulder toward the wall speaker", 'Lin', "her lips parting, her eyes sharp and alert, her brows pulled together", outfit=SU_CLINIC),
    P('lin_home', 'right', "sitting beside her in profile facing frame-left, his left hand resting on his knee, his head turned toward her", 'Su', "his jaw set, his eyes calm and dark, his brows level", outfit=LIN_CLINIC)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, on the sofa.',
   [('eden_voice', "泄洪总闸电动机构受损，只能手动。", 'lin_home', 'soft calm', '轻柔平静'),
    ('su_cozy', "那就别用它。", 'lin_home', 'firm quiet', '坚定安静'),
    ('lin_home', "只要不开，就用不着关。", 'su_cozy', 'low calm', '低沉平静'),
    ('eden_voice', "手轮锁只认林先生的手掌。", 'lin_home', 'soft calm', '轻柔平静')],
   V('A soft electronic chime from the wall, the crackle of the stove and a quiet breath.', '墙上一声轻轻的电子提示音、炉灶的噼啪声和一声安静的呼吸。'),
   AE("The thin blue ring of the wall speaker glows above the sofa, amber lamp light lies on their faces and the cold monitor glow outlines their shoulders.",
      "沙发上方墙上扬声器那圈细细的蓝光亮着，琥珀色的灯光落在他们脸上，监控墙冷冷的光描出他们肩膀的轮廓。"),
   post_en='after the last line <lin_home> slowly closes his left hand on his knee and looks down at it',
   post_zh='最后一句之后，林峰把放在膝盖上的左手慢慢攥起来，低头看着它',
   cam=lowrise('the two of them on the sofa', '沙发上的两个人'), bg='On the wall above the sofa a flat speaker panel with a thin glowing blue ring glows.')

INS('55-06', '06｜沙发：林峰放在膝盖上的左手慢慢蜷起，五根手指只能合到一半就停住了，指尖微微发抖', 7, SOFA_HAND,
    'Close shot of his left hand on his knee, the fingers in the middle third of the frame, nobody else in the scene.',
    "A man's left hand rests on his knee and the five fingers curl slowly inward but stop halfway and tremble faintly at the tips. Nothing else moves.",
    "一只男人的左手放在膝盖上，五根手指慢慢往里蜷，只蜷到一半就停住，指尖微微发抖。别的什么都不动。",
    Q('A deep hush and the soft crackle of a stove far behind.', '深深的寂静和远处炉灶轻轻的噼啪声。'),
    'The frame holds the left hand on the knee, and nobody else in the scene.',
    push1('the half-closed fingers', '只合了一半的手指'),
    AE("Warm amber lamp light lies on the knuckles while a thin cold-blue rim from the monitor wall outlines the pale fingertips.",
       "温暖的琥珀色灯光落在指关节上，监控墙一圈薄薄的冷蓝色边光描出苍白的指尖。"))

# ================================================================================================ 第 56 集（B）
mode('B')
b56 = S.episode('剧本第56集｜全自动的绿洲', '地下二层，机械臂剪下一串串紫葡萄放进清洗槽；苏清月穿着林峰的白衬衫榨葡萄汁，林峰穿着睡衣打着哈欠走进来，伊甸说葡萄已洗净，苏清月说我们是废土上最闲的人，林峰说闲是末日最顶级的奢侈品；农场里母鸡下了八个蛋，苏清月高兴得喊，林峰说它们比我们会过日子；林峰煎牛排，伊甸忽然报告地热溶洞出现异常生长，溶洞里长出了会发光的稻田。', 56)

INS('56-01', '01｜地下二层农场：一串串紫色的葡萄挂在棚架上，头顶轨道上的机械臂悄无声息地滑过来，咔嚓一下剪下一串，放进下面的清洗槽', 6, GRAPE,
    'Medium shot of the trellis and the robotic arm, the hanging grapes in the middle third of the frame, nobody in the scene.',
    "Heavy bunches of dark purple grapes hang from the trellis and a slim steel robotic arm glides in along its ceiling rail, snips one bunch with a small blade and lowers it into the clear washing tray. Nothing else moves.",
    "一串串深紫色的葡萄挂在棚架上，头顶轨道上一条纤细的钢制机械臂滑过来，用小刀咔嚓剪下一串，放进下面透明的清洗槽。别的什么都不动。",
    Q('The smooth whir of a servo motor, the crisp snip of a blade and a splash of water.', '伺服电机顺滑的嗡嗡声、小刀清脆的咔嚓声和一声水花。'),
    'The frame holds the grape trellis and the robotic arm, and nobody in the scene.',
    follow('the robotic arm', '机械臂', 'the washed grapes glisten in the tray', '洗好的葡萄在槽里闪着水光'),
    AE("Pink-violet grow-lamp light glows through the dark purple grapes and bright droplets from the washing tray fly through the beam.",
       "粉紫色的生长灯光透过深紫色的葡萄发亮，洗槽里溅起的水珠在光柱里闪着。"))

DL('56-02', '02｜厨房：苏清月穿着林峰的白衬衫、赤着脚在台面上榨葡萄汁，林峰穿着睡衣打着哈欠走进来，伊甸说葡萄已洗净，苏清月说我们是废土上最闲的人，林峰说闲是末日最顶级的奢侈品，她问中午吃什么', KITCH_MORN,
   [P('su_cozy', 'left', "standing at the marble counter in three-quarter profile facing frame-right, pouring dark purple juice from a glass jug into a tall glass, her head turned toward him", 'Lin', "her lips curving in a lazy bright sweet smile, her eyes sparkling, her brows lifted", outfit=SU_SHIRT),
    P('lin_home', 'right', "leaning on the end of the counter in profile facing frame-left, one hand rubbing the back of his neck, his head turned toward her", 'Su', "his lips parting in a yawn then easing into a sleepy half sweet smile, his eyes heavy and warm, his brows soft", outfit=LIN_PJ)],
   'Medium two-shot, both from the head to the thighs, in the middle third of the frame, at the kitchen counter.',
   [('eden_voice', "早安。葡萄已采摘洗净。", 'su_cozy', 'soft bright', '轻柔明亮'),
    ('su_cozy', "伊甸把循环全修好了。", 'lin_home', 'lazy bright', '慵懒明亮'),
    ('su_cozy', "我们是废土上最闲的人。", 'lin_home', 'playful', '俏皮'),
    ('lin_home', "闲，是末日最顶级的奢侈品。", 'su_cozy', 'low sleepy', '低沉带睡意'),
    ('su_cozy', "那中午吃什么？", 'lin_home', 'bright teasing', '明亮逗弄')],
   V('The gentle gurgle of juice into a glass, the soft hum of the stove and a sleepy yawn.', '果汁倒进杯子的轻轻汩汩声、炉灶轻轻的嗡鸣和一声睡意蒙眬的哈欠。'),
   AE("Soft morning-gold lamp light spills across the marble counter, the dark purple juice glows like wine in the glass and warm steam curls past their faces.",
      "柔和的晨金色灯光洒在大理石台面上，深紫色的果汁在杯子里像红酒一样发亮，温暖的蒸汽从他们的脸旁卷过。"),
   post_en='after the last line <lin_home> takes the tall glass of juice out of her hand and drinks it',
   post_zh='最后一句之后，林峰把她手里那只高杯的果汁拿过去喝了',
   cam=slide('toward frame-right', '右', 'the two of them fill the middle third of the frame', '两人占满画面中间三分之一'),
   bg='Behind them the black-and-gold stove glows ember-orange at frame-left and the wall of monitors is dark.')

DL('56-03', '03｜地下二层农场：苏清月提着一篮子鸡蛋跑过来，说母鸡下蛋了、八个，林峰说它们比我们会过日子，她说今天煎蛋明天蒸蛋，他问后天呢，她说后天煎蛋', EGGS,
   [P('su_cozy', 'left', "hurrying along the tier of green plants in profile facing frame-right, holding a wicker basket of eight brown eggs out in front of her, her head turned toward him", 'Lin', "her lips open in a delighted grin, her eyes shining, her brows lifted", outfit=SU_WORK),
    P('lin_home', 'right', "standing by the hydroponic channel in profile facing frame-left, a small watering can in his hand, his head bent toward the basket", 'Su', "his lips pressed into a dry amused sweet smile, his eyes warm, his brows lifted", outfit=LIN_WORK)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, between the hydroponic tiers.',
   [('su_cozy', "八个！母鸡下蛋了！", 'lin_home', 'delighted bright', '欣喜明亮'),
    ('lin_home', "它们比我们会过日子。", 'su_cozy', 'dry amused', '干干地带笑'),
    ('su_cozy', "今天煎蛋，明天蒸蛋。", 'lin_home', 'bright planning', '明亮盘算'),
    ('lin_home', "后天呢？", 'su_cozy', 'low teasing', '低沉逗弄'),
    ('su_cozy', "后天煎蛋！", 'lin_home', 'bright laughing', '明亮带笑')],
   V('The soft clucking of hens, the trickle of water in the channels and a warm laugh.', '母鸡轻轻的咕咕声、水槽里细细的流水声和一声温暖的笑。'),
   AE("Pink-violet grow-lamp light haloes her loose hair and the brown eggs in the basket glow like warm stones, while mist from the channels drifts across the beam.",
      "粉紫色的生长灯光在她散开的头发上描出光晕，篮子里的棕色鸡蛋像温暖的石头一样发亮，水槽里的雾气在光柱里飘过。"),
   post_en='after the last line she lifts one brown egg from the basket and holds it up to his face',
   post_zh='最后一句之后，她从篮子里拿起一个棕色的鸡蛋，举到他的脸前',
   cam=follow('Su', '苏清月', 'she stops in front of him in the middle third of the frame', '她停在他面前、占满画面中间三分之一'), bg='Behind them the straw-lined hen pen and the steel staircase stand at frame-left.')

DL('56-04', '04｜地下二层农场：苏清月用平板指挥机械臂再剪一串葡萄，说伊甸再来一串，伊甸说好的，她说它比我会剪，林峰说比我也会，她说我们要失业了，伊甸说二位永远有工作，吃饭', GRAPE,
   [P('su_cozy', 'left', "standing under the trellis in profile facing frame-right, a slim tablet in her left hand and a purple grape between her right fingers, her head tipped back toward the robotic arm", 'obj:the robotic arm above the trellis', "her lips curving in an amused grin, her eyes bright, her brows lifted", outfit=SU_WORK),
    P('lin_home', 'right', "standing beside her in profile facing frame-left, his arms crossed, his head turned toward her", 'Su', "his lips pressed into a dry amused sweet smile, his eyes warm, his brows lifted", outfit=LIN_WORK)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, under the trellis.',
   [('su_cozy', "伊甸，再来一串。", 'eden_voice', 'bright', '明亮'),
    ('eden_voice', "好的，苏女士。", 'su_cozy', 'soft polite', '轻柔礼貌'),
    ('su_cozy', "它比我会剪。", 'lin_home', 'amused', '带笑'),
    ('lin_home', "比我也会。", 'su_cozy', 'dry', '干干地'),
    ('su_cozy', "我们要失业了。", 'lin_home', 'bright mock-alarmed', '明亮假装惊慌'),
    ('eden_voice', "二位永远有工作：吃饭。", 'lin_home', 'soft dry', '轻柔干干地')],
   V('The smooth whir of a servo arm, the crisp snip of a blade and a bright laugh.', '伺服机械臂顺滑的嗡嗡声、小刀清脆的咔嚓声和一声明亮的笑。'),
   AE("Pink-violet grow-lamp light glows through the grapes above them, a dark purple bunch descends on the arm into the beam and droplets sparkle as it passes.",
      "粉紫色的生长灯光透过他们头顶的葡萄发亮，一串深紫色的葡萄被机械臂放下来落进光柱里，经过时水珠闪着光。"),
   post_en='after the last line the robotic arm lowers a dark purple bunch of grapes into her open hand',
   post_zh='最后一句之后，机械臂把一串深紫色的葡萄放进她摊开的手里',
   cam=tilt('the robotic arm and the grapes above them', '头顶的机械臂和葡萄'), bg='Behind them the white hydroponic channels glow under the pink-violet lamps and a flat speaker panel with a thin glowing blue ring is on the pillar.')

DL('56-05', '05｜厨房：林峰在灶台前煎牛排，苏清月靠在台边吃葡萄，他说今天不拆管道不打架，她说那就好好吃饭，她说你切给我，他把切好的一小块插在叉子上说张嘴，送进她嘴里', KITCH_MORN,
   [P('lin_home', 'left', "standing at the stove in profile facing frame-right, a fork with a cut piece of steak in his right hand and a black pan sizzling behind it, his head bent toward her", 'Su', "his lips easing into a relaxed half sweet smile, his eyes warm, his brows soft", outfit=LIN_CLINIC),
    P('su_cozy', 'right', "leaning against the marble counter in three-quarter profile facing frame-left, a grape between her fingers, her head tilted up toward him", 'Lin', "her lips curving in a contented sweet smile, her eyes bright, her brows relaxed", outfit=SU_SHIRT)],
   'Medium two-shot, both from the head to the thighs, in the middle third of the frame, at the stove.',
   [('lin_home', "今天不拆管道，不打架。", 'su_cozy', 'low relaxed', '低沉放松'),
    ('su_cozy', "那就好好吃饭。你切给我。", 'lin_home', 'bright lazy', '明亮慵懒'),
    ('lin_home', "张嘴。", 'su_cozy', 'low soft', '低沉轻柔')],
   V('The loud sizzle of a steak in a hot pan, the soft clink of a fork on porcelain and the warm crackle of the stove.', '热锅里牛排响亮的滋滋声、叉子碰到瓷盘轻轻的响声和炉灶温暖的噼啪声。'),
   AE("Warm amber stove light flickers on their faces, golden grease flares in the pan and a curl of savory smoke drifts through the beam of the lamps.",
      "温暖的琥珀色炉火在他们脸上闪动，锅里金色的油星一闪，一缕喷香的烟气在灯光的光柱里飘过。"),
   post_en='after the last line she opens her mouth and he slides the piece of steak in',
   post_zh='最后一句之后，她张开嘴，他把那块牛排送进去',
   cam=arc('the two of them', '两个人', 'they fill the middle third of the frame', '他们占满画面中间三分之一'), bg='Behind them the black-and-gold stove glows ember-orange at frame-left.')

DL('56-06', '06｜厨房：伊甸忽然说地热溶洞出现异常生长，林峰放下叉子说又来了，苏清月说走去看看，他说先吃完，她说我等不及', KITCH_MORN,
   [P('lin_home', 'left', "standing at the stove in profile facing frame-right, one hand on the pan handle, his head lifted toward the wall speaker", 'obj:the wall speaker above the counter', "his jaw easing into a dry half sweet smile, his eyes alert and dark, his brows lifted", outfit=LIN_CLINIC),
    P('su_cozy', 'right', "standing at the marble counter in three-quarter profile facing frame-left, a grape in her hand, her head lifted toward the wall speaker", 'obj:the wall speaker above the counter', "her lips parting in curious delight, her eyes bright, her brows lifted", outfit=SU_SHIRT)],
   'Medium two-shot, both from the head to the thighs, in the middle third of the frame, at the stove.',
   [('eden_voice', "地热溶洞，出现异常生长。", 'lin_home', 'soft calm', '轻柔平静'),
    ('lin_home', "又来了。", 'su_cozy', 'low amused', '低沉带笑'),
    ('su_cozy', "走，去看看！", 'lin_home', 'bright eager', '明亮急切'),
    ('lin_home', "先吃完。", 'su_cozy', 'low dry', '低沉干干地'),
    ('su_cozy', "我等不及！", 'lin_home', 'bright laughing', '明亮带笑')],
   V('A soft electronic chime, the sizzle of the pan fading and a bright laugh.', '一声轻轻的电子提示音、锅里滋滋声渐渐小下去和一声明亮的笑。'),
   AE("The thin blue ring of the wall speaker glows above the counter, amber stove light warms their faces and a last wisp of steak smoke curls past the lamps.",
      "灶台上方墙上扬声器那圈细细的蓝光亮着，琥珀色的炉火暖着他们的脸，最后一缕牛排的烟气卷过灯光。"),
   post_en='after the last line <lin_home> switches off the heat and <su_cozy> is already pulling him by the sleeve toward the hatch door',
   post_zh='最后一句之后，林峰关了火，苏清月已经拽着他的袖子往舱门那边拉',
   cam=slide('toward frame-left', '左', 'the two of them fill the middle third of the frame', '两人占满画面中间三分之一'), bg='On the wall above the counter a flat speaker panel with a thin glowing blue ring glows.')

INS('56-07', '07｜溶洞：温泉池边的岩台上长出一整片半人高的稻子，沉甸甸的稻穗发着淡淡的金绿色荧光，水雾在稻田上飘着', 8, PADDY_WIDE,
    'Wide shot of the paddy beside the pool, the glowing rice in the middle third of the frame, nobody in the scene.',
    "A wide terraced paddy of knee-high rice stalks stands beside the steaming turquoise pool with heavy grain heads glowing a pale gold-green while white mist drifts slowly over the stalks. Nothing else moves.",
    "温泉池边的岩台上一整片梯田一样的半人高稻子，沉甸甸的稻穗发着淡淡的金绿色荧光，白色的水雾慢慢从稻子上飘过。别的什么都不动。",
    Q('The gentle bubbling of the pool, the soft rustle of stalks and a faint drip of water.', '水池轻轻的咕嘟声、稻秆轻轻的沙沙声和一声细细的滴水声。'),
    'The frame holds the glowing paddy beside the pool, and nobody in the scene.',
    slide('toward frame-right', '右', 'the glowing grain heads fill the middle third of the frame', '发光的稻穗占满画面中间三分之一'),
    AE("A soft pale gold-green glow breathes from every grain head, blue moss light shimmers on the wet rock and white mist glitters as it drifts through the glow.",
       "每一个稻穗都散出柔和的淡金绿色光，蓝色的苔藓光在湿漉漉的岩石上闪着，白色的水雾飘过光里闪闪发亮。"))

# ================================================================================================ 第 57 集（A＋B）
mode('A')
b57 = S.episode('剧本第57集｜荧光稻田', '林峰和苏清月沿着岩石小路走进溶洞，温泉边长出一整片会发光的稻田，苏清月不敢相信这是稻子，林峰说是他随手撒过一把种子，被地热和苔藓的光养活了；两人动手收割，苏清月说手术刀也能割稻子；割着割着，林峰左手里的镰刀忽然滑落，他说手滑了、泡冷水泡久了，苏清月看见他的手在发抖，一把用两只手握住了它，脸色变了。', 57)
new_scene(b57, 'paddy_cave', '溶洞里的荧光稻田（温泉池边的梯田，半人高的稻子，沉甸甸的稻穗发着淡淡的金绿色光，蓝色苔藓石壁，白色水雾）',
          'A vast steaming natural cavern with walls of softly glowing blue moss, a turquoise hot spring pool and along its edge a terraced paddy of waist-high rice stalks with heavy grain heads glowing a pale gold-green.',
          '一个冒着热气的巨大天然溶洞，石壁上长满发着柔和蓝光的苔藓，中间是碧绿的温泉池，池边是梯田一样的半人高稻子，沉甸甸的稻穗发着淡淡的金绿色光。',
          'the terraced glowing paddy beside the pool')

INS('57-01', '01｜溶洞：一条光滑的岩石小路穿过发光的稻田，稻秆在温暖的水汽里微微摇着，沉甸甸的稻穗一粒粒闪着金绿色的光', 8, PADDY_EDGE,
    'Wide low shot of the path and the paddy, the glowing grain heads in the middle third of the frame, nobody in the scene.',
    "A smooth rock path runs along the front of a dense paddy of waist-high rice, the heavy grain heads glowing pale gold-green and the stalks swaying faintly in the warm steam. Nothing else moves.",
    "一条光滑的岩石小路沿着一大片密密的半人高稻田，沉甸甸的稻穗发着淡淡的金绿色光，稻秆在温暖的水汽里微微摇着。别的什么都不动。",
    Q('A soft whisper of stalks in warm air, the gentle bubbling of the pool and a distant drip.', '稻秆在暖风里轻轻的沙沙声、水池轻轻的咕嘟声和远处一声滴水。'),
    'The frame holds the path and the glowing paddy, and nobody in the scene.',
    descend('the glowing grain heads along the path', '路边发光的稻穗'),
    AE("Each swaying grain head breathes a warm gold-green glow, blue moss light shimmers on the damp rock and tiny sparks of pollen drift upward through the steam.",
       "每一穗摇动的稻穗都散出温暖的金绿色光，蓝色的苔藓光在潮湿的岩石上闪着，细小的花粉星点穿过水汽往上飘。"))

DL('57-02', '02｜稻田边：苏清月和林峰走到稻田前停住，苏清月不敢相信地问这是稻子，林峰说是变异的野生稻吸了地热和苔藓的光，她问怎么来的，他说是我随手撒过一把种子，然后她蹲下去碰了碰那个发光的稻穗', PADDY_EDGE,
   [P('su_cozy', 'left', "standing on the rock path in three-quarter profile facing frame-right, one hand half raised toward the rice, her head turned toward him", 'Lin', "her lips falling open, her eyes wide and shining, her brows lifted high", outfit=SU_WORK),
    P('lin_home', 'right', "standing beside her in profile facing frame-left, his hands in his trouser pockets, his head turned toward her", 'Su', "his lips easing into a faint pleased sweet smile, his eyes warm and dark, his brows level", outfit=LIN_WORK)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, on the path.',
   [('su_cozy', "这是……稻子？", 'lin_home', 'awed soft', '惊叹而轻'),
    ('lin_home', "变异野生稻，吃了地热的光。", 'su_cozy', 'low calm', '低沉平静'),
    ('su_cozy', "它是怎么长出来的？", 'lin_home', 'bright curious', '明亮好奇'),
    ('lin_home', "我随手撒过一把种子。", 'su_cozy', 'low amused', '低沉带笑')],
   V('A soft whisper of stalks, the gentle bubbling of the pool and a hushed breath.', '稻秆轻轻的沙沙声、水池轻轻的咕嘟声和一声压低的呼吸。'),
   AE("The pale gold-green glow of the rice lights her upturned face from below, blue moss light outlines his shoulders and warm steam drifts across the frame.",
      "稻子淡淡的金绿色光从下面照亮她仰起的脸，蓝色的苔藓光描出他肩膀的轮廓，温暖的水汽从画面里飘过。"),
   post_en='after the last line <su_cozy> crouches and touches one glowing grain head with her fingertips',
   post_zh='最后一句之后，苏清月蹲下去，用指尖碰了碰一个发光的稻穗',
   cam=lowrise('the glowing rice and the two of them', '发光的稻子和两个人'), bg='Behind them the steaming turquoise pool and the wall of blue moss fill the cavern.')

mode('B')
DL('57-03', '03｜稻田：林峰弯腰割稻，苏清月拿着捆稻的草绳，她说镰刀给我我也来，他说你的手是拿手术刀的，她说手术刀也能割稻子，他说那你割这一排', PADDY_EDGE,
   [P('su_cozy', 'left', "bending at the edge of the paddy in profile facing frame-right, a coil of straw rope over her shoulder, one hand held out toward him, her head turned toward him", 'Lin', "her lips curving in a bright challenging sweet smile, her eyes sparkling, her brows lifted", outfit=SU_WORK),
    P('lin_home', 'right', "bending among the rice stalks in profile facing frame-left, a curved sickle in his right hand and a bundle of cut stalks in his left, his head turned toward her", 'Su', "his lips easing into a dry sweet smile, his eyes warm, his brows soft", outfit=LIN_WORK)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the edge of the paddy.',
   [('su_cozy', "镰刀给我，我也来。", 'lin_home', 'bright challenging', '明亮带挑战'),
    ('lin_home', "你的手是拿手术刀的。", 'su_cozy', 'dry amused', '干干地带笑'),
    ('su_cozy', "手术刀也能割稻子。", 'lin_home', 'bright playful', '明亮俏皮'),
    ('lin_home', "行，你割这一排。", 'su_cozy', 'low amused', '低沉带笑')],
   V('The crisp swish of a sickle through stalks, the soft rustle of cut rice and a warm laugh.', '镰刀割过稻秆清脆的唰唰声、割下的稻子轻轻的沙沙声和一声温暖的笑。'),
   AE("The gold-green glow of the rice bundles in his arm lights their faces from below while blue moss light shimmers on the wet rock and warm steam drifts past.",
      "他臂弯里那捆稻子的金绿色光从下面照亮他们的脸，蓝色的苔藓光在湿岩石上闪着，温暖的水汽从旁边飘过。"),
   post_en='after the last line <lin_home> hands the sickle across to her with the handle first',
   post_zh='最后一句之后，林峰把镰刀柄朝前递给她',
   cam=track('the two of them', '他们两个'), bg='Behind them the glowing paddy and the steaming turquoise pool fill the cavern.')

mode('A')
DL('57-04', '04｜稻田：林峰割着稻，左手里的镰刀忽然滑落掉在石头上当啷一响，苏清月问怎么了，他说手滑了，她说你的手在发抖，他说泡冷水泡久了缓缓就好，然后她一把握住他的左手', PADDY_EDGE,
   [P('su_cozy', 'left', "standing on the rock path in profile facing frame-right, her head turned toward his left hand", 'Lin', "her lips parting, her eyes sharp and worried, her brows pulled together", outfit=SU_WORK),
    P('lin_home', 'right', "standing at the edge of the paddy in profile facing frame-left, his left hand held in front of his chest with the fingers half curled, a bundle of cut stalks at his feet and a sickle lying on the rock, his head bent toward the hand", 'obj:his own trembling left hand', "his jaw tightening, his eyes dark and steady, his brows low", outfit=LIN_WORK)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, on the path.',
   [('su_cozy', "怎么了？", 'lin_home', 'quick worried', '急急担心'),
    ('lin_home', "手滑了。", 'su_cozy', 'low light', '低沉轻描淡写'),
    ('su_cozy', "你的手，在发抖。", 'lin_home', 'low tight', '低沉发紧'),
    ('lin_home', "泡冷水泡久了，缓缓就好。", 'su_cozy', 'low calm', '低沉平静')],
   V('The clang of a sickle on stone, the soft rustle of stalks and a held breath.', '镰刀掉在石头上的当啷声、稻秆轻轻的沙沙声和一声屏住的呼吸。'),
   AE("The gold-green glow of the rice lights the underside of his raised hand and the pale tremor of his fingers while blue moss light cools the edges of their faces.",
      "稻子的金绿色光从下面照亮他抬起的手和手指苍白的颤抖，蓝色的苔藓光让他们的脸的边缘冷了下去。"),
   pre_en='A sickle slips from his left hand and clangs on the rock.', pre_zh='一把镰刀从他的左手里滑落，当啷一声掉在石头上。',
   post_en='after the last line <su_cozy> steps in and takes his left hand in both of hers',
   post_zh='最后一句之后，苏清月走上前，用两只手握住他的左手',
   tail=2.5, cam=push('both of them', '两人'), bg='Behind them the glowing paddy and the steaming turquoise pool fill the cavern.')

INS('57-05', '05｜稻田：苏清月温暖的两只手紧紧握着林峰苍白冰凉的左手，他的手指在她的手心里微微发颤，背景是模糊的发光稻穗', 7, PADDY_CLOSE,
    'Close shot of the clasped hands, the hands in the middle third of the frame, nobody else in the scene.',
    "Two warm hands hold a pale, cold left hand tightly between them while its fingers tremble faintly against her palms, the glowing rice a soft blur behind. Nothing else moves.",
    "两只温暖的手紧紧握着一只苍白冰凉的左手，那只手的手指在她的手心里微微发颤，背后是模糊的发光稻穗。别的什么都不动。",
    Q('A deep hush, the gentle bubbling of the pool and a held breath.', '深深的寂静、水池轻轻的咕嘟声和一声屏住的呼吸。'),
    'The frame holds the clasped hands, and nobody else in the scene.',
    push1('the clasped hands', '握在一起的手'),
    AE("Soft gold-green rice glow lights the pale knuckles from below, a warm amber rim falls on her fingers and drifting steam catches the light.",
       "柔和的金绿色稻光从下面照亮苍白的指关节，一圈温暖的琥珀色边光落在她的手指上，飘着的水汽映着光。"))

DL('57-06', '06｜稻田：苏清月握着他的手抬起头看着他的眼睛，说回去让我检查，他说好，她说现在就回去，他点点头，两人一起把割好的稻子装进篮子里', PADDY_EDGE,
   [P('su_cozy', 'left', "standing facing him in profile facing frame-right, both hands still around his left hand, her chin lifted", 'Lin', "her lips pressed into a firm line, her eyes steady and bright with worry, her brows level", outfit=SU_WORK),
    P('lin_home', 'right', "standing facing her in profile facing frame-left, his left hand held in hers, his head bent toward her", 'Su', "his jaw easing, his eyes dark and gentle, his brows soft", outfit=LIN_WORK)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, on the path.',
   [('su_cozy', "回去让我检查。", 'lin_home', 'firm quiet', '坚定安静'),
    ('lin_home', "好。", 'su_cozy', 'low gentle', '低沉温柔'),
    ('su_cozy', "现在就回去。", 'lin_home', 'firm', '坚定'),
    ('lin_home', "听你的。", 'su_cozy', 'low soft', '低沉轻柔')],
   V('The soft bubbling of the pool and a quiet shared breath.', '水池轻轻的咕嘟声和两人安静的呼吸。'),
   AE("Gold-green rice light and cool blue moss light meet on their faces in a soft teal-and-gold rim and steam curls slowly between them.",
      "金绿色的稻光和冷冷的蓝色苔藓光在他们脸上交汇成柔和的青金色边光，水汽在两人之间慢慢卷着。"),
   post_en='after the last line she lets go of his hand and bends to lift the full basket of rice onto her arm',
   post_zh='最后一句之后，她松开他的手，弯腰把装满稻子的篮子挎到手臂上',
   cam=pull('their faces', '两人的脸', 'the two of them and the glowing paddy behind', '两人和身后发光的稻田'), bg='Behind them the glowing rice paddy and the steaming pool fill the cavern.')

INS('57-07', '07｜稻田边：割下来的金绿色稻穗整整齐齐地铺在一块白布上，一粒粒饱满的稻谷在暖光下发着微光', 7, PADDY_EDGE,
    'Close low shot of the cloth of cut rice, the glowing grain heads in the middle third of the frame, nobody in the scene.',
    "Cut sheaves of gold-green rice lie in neat rows on a white cloth beside the path and each plump grain glows faintly in the warm steam. Nothing else moves.",
    "割下来的金绿色稻穗整整齐齐地铺在小路边的一块白布上，每一粒饱满的稻谷都在温暖的水汽里发着微光。别的什么都不动。",
    Q('The soft rustle of dry stalks, the gentle bubbling of the pool and a quiet drip.', '干稻秆轻轻的沙沙声、水池轻轻的咕嘟声和一声安静的滴水。'),
    'The frame holds the cloth of cut rice, and nobody in the scene.',
    slide('toward frame-right', '右', 'the glowing grains fill the middle third of the frame', '发光的稻谷占满画面中间三分之一'),
    AE("A warm gold-green glow lifts off the plump grains, blue moss light shimmers on the rock behind and tiny motes of dust drift up through the steam.",
       "温暖的金绿色光从饱满的稻谷上升起来，后面岩石上蓝色的苔藓光闪着，细小的尘粒穿过水汽往上飘。"))

# ================================================================================================ 第 58 集（A＋B）
b58 = S.episode('剧本第58集｜舌尖上的避难所', '医疗室里，苏清月用手电照着林峰的左手，说是神经冻伤、越冷越没知觉，林峰说只要还能关阀门，她说你以为我在说阀门，他说我知道，她用温毛巾裹住他的手；晚上桌上摆着第一锅用荧光稻煮的新米饭、盲鱼汤和煎蛋，苏清月说香得不像末日，让他别用左手；伊甸忽然报告地表温度零下九度还在上升，林峰筷子停在半空说要来了；泵房里水位浮标往上升了一格。', 58)

DL('58-01', '01｜医疗室：林峰坐在钢椅上，苏清月握着他的左手用小手电照着，问有没有感觉，他说一点点，她说是神经冻伤了、越冷越没知觉，他说只要还能关阀门', MED,
   [P('su_cozy', 'left', "sitting on a stool facing him in profile facing frame-right, his left hand cradled palm-up in her left hand and a small pen torch in her right, her head bent over his hand", 'obj:his open left palm', "her lips pressed into a thin line, her eyes narrowed and fixed, her brows low", outfit=SU_CLINIC),
    P('lin_home', 'right', "sitting on the steel chair in profile facing frame-left, his left sleeve rolled to the elbow and his hand laid in hers, his head turned toward her face", 'Su', "his jaw set, his eyes dark and calm, his brows level", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the medical room.',
   [('su_cozy', "这样呢，有感觉吗？", 'lin_home', 'quiet clinical', '安静而专业'),
    ('lin_home', "一点点。", 'su_cozy', 'low flat', '低沉平淡'),
    ('su_cozy', "神经冻伤了，越冷越没知觉。", 'lin_home', 'low tight', '低沉发紧'),
    ('lin_home', "只要还能关阀门。", 'su_cozy', 'low calm', '低沉平静')],
   V('A quiet click of a pen torch, a long slow breath and the faint hum of the surgical lamp.', '手电轻轻的一声咔嗒、一声长长的缓慢呼吸和手术灯轻微的嗡鸣。'),
   AE("A hard white beam from the pen torch lights the pale lines of his palm while the soft white surgical lamp makes a clean clinical glow on their faces.",
      "手电一道硬朗的白光照亮他手掌上苍白的纹路，柔和的白色手术灯在他们脸上洒下干净的医疗光。"),
   post_en='after the last line she drops the pen torch onto the instrument tray and stares at him',
   post_zh='最后一句之后，她把手电丢进器械盘里，直直地看着他',
   cam=push('their hands and faces', '手和两张脸'), bg='Behind them the white-tiled wall and the steel instrument tray stand under the round surgical lamp.')

DL('58-02', '02｜医疗室：苏清月说你以为我在说阀门，林峰说我知道你在说什么，她说那就别逞强，他说好，然后她用热毛巾把他的左手裹起来握在手里', MED,
   [P('su_cozy', 'left', "sitting on the stool facing him in profile facing frame-right, a steaming white towel in both hands wrapping his left hand, her head lifted toward his face", 'Lin', "her lips trembling then pressed firm, her eyes wet and fierce, her brows pulled together", outfit=SU_CLINIC),
    P('lin_home', 'right', "sitting on the steel chair in profile facing frame-left, his left hand resting in the towel in her lap, his head bent toward her", 'Su', "his lips easing into a faint apologetic sweet smile, his eyes dark and tender, his brows soft", outfit=LIN_CLINIC)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, in the medical room.',
   [('su_cozy', "你以为我在说阀门？", 'lin_home', 'low trembling', '低沉发颤'),
    ('lin_home', "我知道你在说什么。", 'su_cozy', 'low gentle', '低沉温柔'),
    ('su_cozy', "那就别逞强。", 'lin_home', 'low fierce', '低沉凶狠'),
    ('lin_home', "好。", 'su_cozy', 'low soft', '低沉轻柔')],
   V('The soft rustle of a towel, a shaky breath and the faint hum of the surgical lamp.', '毛巾轻轻的摩擦声、一声发颤的呼吸和手术灯轻微的嗡鸣。'),
   AE("Warm steam rises from the towel into the cool white light of the lamp, her wet lashes glitter and the white glow softens to a gentle gold around their joined hands.",
      "热毛巾冒起的蒸汽升进手术灯冷冷的白光里，她湿润的睫毛闪着光，白色的光在他们握在一起的手周围软成柔和的金色。"),
   post_en='after the last line she lowers her forehead to rest on the back of his wrapped hand',
   post_zh='最后一句之后，她把额头轻轻抵在他裹着毛巾的手背上',
   tail=2.5, cam=push1('the two bent heads and the wrapped hand', '两个低下来的头和裹着毛巾的手'), bg='Behind them the white-tiled wall fills the background under the round surgical lamp.')

mode('B')
DL('58-03', '03｜厨房：苏清月第一次用荧光稻煮饭，她问水放多少，林峰说一比一点二，她问你怎么记得，他说我写在笔记里了，她说笔记借我看，他说看可以，别笑我字丑', KITCH_WARM,
   [P('su_cozy', 'left', "standing at the stove in profile facing frame-right, a small copper pot with a lid in both hands, her head turned toward him", 'Lin', "her lips curving in a curious sweet smile, her eyes bright, her brows lifted", outfit=SU_CLINIC),
    P('lin_home', 'right', "leaning on the marble counter in profile facing frame-left, a worn black notebook open in his right hand, his head turned toward her", 'Su', "his lips pressed into a dry half sweet smile, his eyes warm, his brows soft", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the stove.',
   [('su_cozy', "水放多少？", 'lin_home', 'bright curious', '明亮好奇'),
    ('lin_home', "一比一点二。", 'su_cozy', 'low steady', '低沉平稳'),
    ('su_cozy', "你怎么记得？", 'lin_home', 'bright teasing', '明亮逗弄'),
    ('lin_home', "我写在笔记里了。", 'su_cozy', 'low dry', '低沉干干地'),
    ('su_cozy', "借我看看。", 'lin_home', 'bright', '明亮')],
   V('The soft hiss of a pot coming to a simmer, the rustle of notebook pages and a warm hum of the stove.', '锅里渐渐煮开的轻轻嘶嘶声、笔记本翻页的沙沙声和炉灶温暖的嗡鸣。'),
   AE("Warm amber stove light rims their faces, a curl of steam rises from the copper pot into the lamps and the notebook pages glow a soft cream.",
      "温暖的琥珀色炉火勾出他们脸的轮廓，铜锅里升起一缕热气卷进灯光里，笔记本的纸页泛着柔和的奶油色。"),
   post_en='after the last line <lin_home> closes the notebook and slides it across the counter to her',
   post_zh='最后一句之后，林峰合上笔记本，从台面上推到她面前',
   cam=slide('toward frame-left', '左', 'the two of them fill the middle third of the frame', '两人占满画面中间三分之一'), bg='Behind them the open kitchen with the black-and-gold stove glows warmly.')

INS('58-04', '04｜餐厅：圆木桌上摆着两碗亮晶晶冒着热气的白米饭、一砂锅奶白色的鱼汤和一盘金黄的煎蛋，热气一缕缕往上卷', 7, LIV_DINNER,
    'Medium high shot of the dining table, the bowls and the pot in the middle third of the frame, nobody in the scene.',
    "Two white bowls of glistening white rice steam on the round wooden table beside a clay pot of milky fish soup and a plate of golden fried eggs, the steam rising in slow curls. Nothing else moves.",
    "圆木桌上两碗亮晶晶的白米饭冒着热气，旁边是一砂锅奶白色的鱼汤和一盘金黄的煎蛋，热气一缕缕慢慢往上卷。别的什么都不动。",
    Q('The soft bubbling of the clay pot, the crackle of the stove and the faint tick of porcelain.', '砂锅轻轻的咕嘟声、炉灶的噼啪声和瓷器轻轻的嘀嗒声。'),
    'The frame holds the laid table with the rice, the soup and the eggs, and nobody in the scene.',
    descend('the steaming rice bowls', '冒着热气的米饭碗'),
    AE("Honey-gold lamp light makes the rice glisten like pearls, the milky soup glows and thin curls of steam turn gold as they rise through the beam.",
       "蜂蜜般的金色灯光让米饭像珍珠一样发亮，奶白色的鱼汤泛着光，一缕缕薄薄的热气升进光柱里变成金色。"))

DL('58-05', '05｜餐厅：苏清月和林峰面对面坐在桌边，她夹起一口新米饭说第一口新米饭，他问怎么样，她说香得不像末日，他说那多吃点，她说你也吃但别用左手', LIV_TABLE,
   [P('su_cozy', 'left', "sitting at the round dining table in profile facing frame-right, chopsticks lifting a mouthful of rice to her lips, her head turned toward him", 'Lin', "her lips curving in a blissful sweet smile, her eyes closing then opening bright, her brows lifted", outfit=SU_CLINIC),
    P('lin_home', 'right', "sitting across the table in profile facing frame-left, a pair of chopsticks in his right hand and his left hand resting wrapped in a thin bandage on the table, his head turned toward her", 'Su', "his lips pressed into a pleased half sweet smile, his eyes warm, his brows soft", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the chest, in the middle third of the frame, at the dining table.',
   [('su_cozy', "新米饭，第一口。", 'lin_home', 'bright eager', '明亮期待'),
    ('lin_home', "怎么样？", 'su_cozy', 'low curious', '低沉好奇'),
    ('su_cozy', "香得不像末日。", 'lin_home', 'bright blissful', '明亮满足'),
    ('lin_home', "那多吃点。", 'su_cozy', 'low warm', '低沉温暖'),
    ('su_cozy', "你也吃，别用左手。", 'lin_home', 'bright firm', '明亮坚定')],
   V('The soft clink of chopsticks on a bowl, a quiet sip of soup and the warm hum of the stove.', '筷子碰碗轻轻的响声、轻轻啜一口汤的声音和炉灶温暖的嗡鸣。'),
   AE("Honey-gold lamp light glows on the rice bowls, rising steam softens the edges of their faces and the amber stove glow lies warm across the table.",
      "蜂蜜般的金色灯光落在饭碗上，升起的热气让他们脸的边缘变得柔和，炉灶琥珀色的光暖暖地铺在桌面上。"),
   post_en='after the last line <lin_home> switches the chopsticks to his right hand and picks up a piece of fried egg for her',
   post_zh='最后一句之后，林峰把筷子换到右手，夹起一块煎蛋放进她的碗里',
   cam=slide('toward frame-right', '右', 'the two of them fill the middle third of the frame', '两人占满画面中间三分之一'), bg='Behind them the black-and-gold stove glows ember-orange at frame-left.')

DL('58-06', '06｜餐厅：伊甸忽然说地表温度零下九度，苏清月说昨天不是零下四十吗，伊甸说温度仍在上升，林峰的筷子停在半空，低声说要来了', LIV_TABLE,
   [P('su_cozy', 'left', "sitting at the table in profile facing frame-right, a bowl in her hands, her head lifted toward the wall speaker", 'obj:the wall speaker above the table', "her lips parting, her eyes wide and alert, her brows pulled together", outfit=SU_CLINIC),
    P('lin_home', 'right', "sitting across the table in profile facing frame-left, his chopsticks frozen in the air above his bowl, his head lifted toward the wall speaker", 'obj:the wall speaker above the table', "his jaw going still, his eyes sharp and dark, his brows low", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the chest, in the middle third of the frame, at the dining table.',
   [('eden_voice', "地表温度，零下九度。", 'lin_home', 'soft calm', '轻柔平静'),
    ('su_cozy', "昨天不是零下四十吗？", 'lin_home', 'tense quick', '紧张急促'),
    ('eden_voice', "温度仍在上升。", 'lin_home', 'soft calm', '轻柔平静'),
    ('lin_home', "要来了。", 'su_cozy', 'low grave', '低沉凝重')],
   V('A soft electronic chime, the quiet clink of a bowl set down and the hum of the stove.', '一声轻轻的电子提示音、碗放下时轻轻的碰响和炉灶的嗡鸣。'),
   AE("The thin blue ring of the wall speaker glows above them, warm lamp light on the food turns cooler on their faces and the steam hangs motionless over the table.",
      "头顶墙上扬声器那圈细细的蓝光亮着，食物上温暖的灯光落到他们脸上变冷了，热气一动不动地悬在桌子上方。"),
   pre_en='The steam over the bowls hangs still.', pre_zh='碗上的热气停住不动。',
   post_en='after the last line <su_cozy> slowly sets her bowl down on the table',
   post_zh='最后一句之后，苏清月慢慢把碗放回桌上',
   cam=pull('the frozen chopsticks', '停在半空的筷子', 'the two tense faces at the table', '桌边两张紧绷的脸'), bg='On the wall above the table a flat speaker panel with a thin glowing blue ring glows.')

INS('58-07', '07｜泵房：透明大水箱里，一个红色的浮标在水面上轻轻往上浮了一格，旁边白色标尺上的刻度线在灯光下一闪', 7, BUOY,
    'Medium shot of the tank and its scale, the red float in the middle third of the frame, nobody in the scene.',
    "Inside the tall clear water tank a red float marker rises slowly by one notch beside the vertical white scale, the water rippling faintly around it. Nothing else moves.",
    "高高的透明水箱里，一个红色的浮标在白色竖直标尺旁慢慢上浮了一格，周围的水面泛起细细的波纹。别的什么都不动。",
    Q('A single soft drip, the faint gurgle of water in a pipe and a deep hush.', '一声轻轻的滴水、管子里细细的水流声和深深的寂静。'),
    'The frame holds the water tank with the red float and the scale, and nobody in the scene.',
    push1('the red float and the scale marks', '红色浮标和标尺刻度'),
    AE("Cool white work-lamp light glints on the water and the red float glows like a warning lamp while a bright ring of ripples spreads out on the surface.",
       "冷白色的工作灯光在水面上闪着，红色的浮标像一盏警示灯一样发亮，一圈明亮的波纹在水面上扩散。"))

report()
doc = S.finish()
