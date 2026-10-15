#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 59–62 集，追加稿 022（2026-10-15 夜，hh 挂机，要 20 集；A／B 两种写法按剧情混用）。
故事见 `剧本/第55-74集_结局版大纲.md`。以 021（第 55–58 集）的 JSON 为底，必须等 021 在插件里全部跑完再追加；追加窗口不要勾每集／总／任务秒数。
写法分配（我的判断）：
  第 59 集 末日橱窗：A（慢、重要：潜望镜看冰雕军阵像展览、第一滴融水、周宁的声音出现）；
  第 60 集 周宁与裴远山：电台对峙 A（三场）＋解冻对策／伊甸警报 B（说明性对话，快速交代）；
  第 61 集 冰雪消融的警钟：B（准备戏：涂防水层、液压撑杆、煮面、伊甸报裂缝，快速推进）；
  第 62 集 倒灌危机：A（水下焊补、耳机里的声音、手动闸门，重要、紧张）。
偏离原大纲：潜望镜工程本身不拍（第 55 集起已经能看到地表）；军阀士兵只在冰雕里出现；水下焊补不拍火焰和水里的人影变化，只拍焊好之后的缝和不再喷水的墙；
  苏清月在控制室用耳机指挥，两人隔着耳机说话（对面的人画外音，不画人）。
H3 方面的风险（交稿时单列，不算我的错）：
  · 59-03／61-01 冰雕军阵里的人群（可能画成真人）、59-05 融水一滴滴往下掉；
  · 59-07／60-01／60-02 收音机画外音（可能被画成屋里多出一个人，或画面里的人张嘴念）；
  · 61-07／62-01 墙缝喷水的水柱、62-02 水里的人和焊枪（等离子火花）、62-02／62-04 耳机两端的画外音；
  · 62-07 手按铜板的细小动作；
  · B 写法的 13 秒任务里 4–5 句台词，后几句开口会不会被挤到片尾。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
import _jihan_base7 as B7
from _jihan_base7 import *
import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407)
OUT = '合并稿/022_第59-62集_末日橱窗周宁与裴远山冰雪消融的警钟倒灌危机_制作稿_追加'
S = Session('合并稿/021_第55-58集_冰川墓碑全自动绿洲荧光稻田舌尖上的避难所_制作稿_追加.json', OUT, 91000)
B6.S = S
B7.S = S

# ---------------------------------------------------------------------------------------------- 衣着
SU_CLINIC = "in a cream knit sweater and black thermal leggings, thick grey socks, her long black hair loose"
LIN_CLINIC = "in a soft grey cotton henley with the left sleeve rolled up to the elbow and loose dark lounge pants"
SU_SLIP = "in a cream knit sweater and black thermal leggings with fluffy white slippers on her feet, her long black hair loose"
SU_WORK = "in a cream knit sweater with the sleeves pushed up to her elbows, black thermal leggings and soft boots, her long black hair tied back in a loose low ponytail"
LIN_WORK = "in a charcoal henley with the sleeves pushed up to his forearms, dark cargo trousers and soft boots"
SU_HEAD = "in a cream knit sweater with the sleeves pushed up, black thermal leggings and soft boots, a black over-ear headset with a slim boom microphone on her head, her long black hair tied back"
LIN_FLOOD_OUT = "in a black neoprene wetsuit with an orange life vest, a dive mask pushed up onto his wet hair and a small headlamp on his forehead, water running down his face and arms"

# ---------------------------------------------------------------------------------------------- 画外音（收音机里的人、耳机另一端的人）
look('radio_ning', 'RadioNing', "a military long-wave radio", 'none', 'its')
look('radio_pei', 'RadioPei', "a military long-wave radio", 'none', 'its')
look('lin_flood', 'LinFlood', LIN_FLOOD_OUT, 'steady dark-brown', 'his', eth=CN30)
RADIO_D = 'the olive-green long-wave radio on the steel side table'
RADIO_DZ = '钢桌上那台橄榄绿的长波收音机'
B7.VOICE_ONLY.update({'radio_ning', 'radio_pei'})
B7.VD['radio_ning'] = (f"the hoarse, frantic man's voice crackling out of {RADIO_D}", f'从{RADIO_DZ}里沙沙传出的嘶哑慌乱的男声')
B7.VD['radio_pei'] = (f"the cold, courteous, deep middle-aged man's voice crackling out of {RADIO_D}", f'从{RADIO_DZ}里沙沙传出的冷静客气、低沉的中年男声')
B7.VD['lin_flood'] = ("Lin's low steady voice heard through the small headset speaker, slightly muffled by water and radio hiss", '林峰低沉平稳的声音，从耳机的小扬声器里传出，带着水声和电流声，略微发闷')
B7.VD['su_cozy'] = ("Su's low smooth voice heard through the small headset speaker, calm and sharp", '苏清月低沉顺滑的声音，从耳机的小扬声器里传出，冷静而锐利')
B7.ZN.update({'radio_ning': '周宁', 'radio_pei': '裴远山', 'lin_flood': '林峰'})
RADIOPEI_EN = "A cold, courteous, unhurried deep middle-aged man's voice heard through crackling radio static, speaking clear Mandarin Chinese." + VT_EN
RADIOPEI_ZH = '隔着收音机沙沙杂音传来的、冷静客气、不紧不慢的低沉中年男声，普通话清楚。' + VT_ZH

# ---------------------------------------------------------------------------------------------- 场景
PERI = Scene('periscope_room', " Cool blue-white light from a round view screen and a faint amber work lamp fill the small round concrete periscope room.",
             " Fixed stage layout: a small circular concrete room; a thick vertical black steel periscope column with a padded rubber eyepiece at chest height stands at frame-left rising into the ceiling; a round view screen the size of a dinner plate glows on the wall at frame-right; a steel wall ladder stands behind; a narrow steel door is at the far frame-right.")
THAW = Scene('ice_army', " A deep blue pre-dawn with a faint green aurora fading, the ice glittering and beginning to run with water.",
             " Fixed stage layout: a vast snowfield under a pale green aurora in deep blue pre-dawn light fills the frame; rows of men in black winter gear and fur hats and a dozen heavy black trucks stand frozen across it, each sheathed in clear glittering ice; thin dark streaks of meltwater run down the ice and dark wet patches show in the snow around the feet of the nearest figures; nobody moves.")
DROP = Scene('ice_army', THAW.end,
             " Fixed stage layout: a close view of the raised arm of one frozen man sheathed in clear ice, a small icicle hanging from his clenched fist in the middle of the frame with a single bright drop of meltwater hanging at its tip and a thin wet shine spreading on the ice below; the ranks of other ice figures soft behind; nobody alive in the scene.")
CONTROL_RADIO = Scene('bunker_control', CONTROL.end, CONTROL.layout + " A steel side table at frame-right holds an olive-green military long-wave radio with a large round dial glowing amber, a pole antenna and a cloth speaker grille.")
RADIO_CLOSE = Scene('bunker_control', CONTROL.end,
                    " Fixed stage layout: a close view of the olive-green long-wave radio on the steel side table filling the middle of the frame, its round dial glowing amber with the needle trembling at one frequency, the pole antenna rising at frame-right; the green status lights of the console blur behind; nobody in the scene.")
PLAN = Scene('bunker_living', LIVING.end,
             " Fixed stage layout: the open kitchen with the black-and-gold stove is at frame-left; the small round wooden dining table fills the middle of the frame covered by a large hand-drawn paper map of mountains with a red pencil circle around a small blue lake and a steel ruler on it; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
FLOOD_DRY = Scene('flood_bay', " Cold white work-lamp light fills the long concrete flood-control bay and a few red emergency strobes pulse far down it.",
                  " Fixed stage layout: a long narrow concrete bay with a dry floor; a huge grey titanium wall panel with riveted seams fills the left half of the frame; thick silver pipes run along the ceiling; a steel ladder stands at frame-right; cans of grey sealant, a paint roller tray and a coil of hose stand on the floor.")
FLOOD_BRACE = Scene('flood_bay', FLOOD_DRY.end,
                    " Fixed stage layout: a long narrow concrete bay with a dry floor; the huge grey titanium wall panel with riveted seams fills the left half of the frame freshly coated in matte grey sealant; a row of heavy hydraulic steel brace jacks spans from the wall to the concrete pillars; thick silver pipes run along the ceiling; a steel ladder stands at frame-right.")
LIV_NOODLE = Scene('bunker_living', LIVING.end,
                   " Fixed stage layout: the open kitchen with the black-and-gold stove is at frame-left, a steaming pot on it; the small round wooden dining table fills the middle of the frame set with two white bowls of steaming noodles in clear broth topped with golden fried eggs and green leaves, two pairs of chopsticks beside them; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
BUOY2 = Scene('pump_room', " Cool white light from a work lamp falls on the clear tank and pipes of the small pump room.",
              " Fixed stage layout: a tall clear water tank fills the middle of the frame with a red float marker bobbing high on the water inside it beside a vertical white scale with painted tick marks, the water level now two notches higher than before; clear water pipes run along the wall at frame-left; nobody in the scene.")
FLOOD_JET = Scene('flood_bay', " Cold white work-lamp light and a pulsing red emergency strobe fill the long concrete flood-control bay, mist hanging in the air.",
                  " Fixed stage layout: a long narrow concrete bay; the huge grey titanium wall panel fills the left half of the frame with a hairline crack running down the middle of it, a thin high-pressure jet of clear water spraying sideways out of the crack across the bay in a long white blade of spray; the floor is wet and shining; thick silver pipes run along the ceiling; a steel ladder stands at frame-right; nobody in the scene.")
FLOOD_PLANK = Scene('flood_bay', FLOOD_JET.end,
                    " Fixed stage layout: a long narrow concrete bay; the titanium wall panel at frame-left has a hairline crack from which a thin white jet of water sprays across the frame; a pale wooden plank lies cut cleanly in two halves on the wet floor in the middle of the frame where the jet struck it, water pooling around the halves; nobody in the scene.")
FLOOD_WATER = Scene('flood_bay', " Cold white work-lamp light and a pulsing red emergency strobe fill the long concrete bay, water spraying and mist hanging in the air.",
                    " Fixed stage layout: a long narrow concrete bay with the floor flooded knee-deep in dark water; the huge grey titanium wall panel with riveted seams and a hairline crack down its middle fills the left half of the frame, a thin jet of water spraying out of the crack; thick silver pipes run along the ceiling; a steel ladder stands at frame-right; floating wooden planks and a yellow plastic crate drift on the water.")
FLOOD_WELD = Scene('flood_bay', " Cold white work-lamp light falls on the long concrete bay, the water calm and the mist thinning.",
                   " Fixed stage layout: a long narrow concrete bay with the floor flooded knee-deep in still dark water; the titanium wall panel fills the left half of the frame and down its middle runs a fresh bright seam of weld, glowing orange-white and cooling, with no water spraying; thick silver pipes run along the ceiling; nobody in the scene.")
FLOOD_DONE = Scene('flood_bay', " Cold white work-lamp light falls on the long concrete bay, the water now only ankle deep and still; a low muffled roar of water comes through the wall.",
                   " Fixed stage layout: a long narrow concrete bay with the floor covered by ankle-deep still water; the titanium wall panel at frame-left with a clean grey seam down its middle, perfectly dry; a steel ladder stands at frame-right; a white towel hangs from the lowest rung.")
GATE = Scene('gate_room', " A single caged work lamp lights a cold bare concrete chamber and dust hangs in the beam.",
             " Fixed stage layout: a small bare concrete chamber whose back wall is filled by a massive round steel gate door two metres tall with a big black iron hand-wheel the size of a car tyre at its centre; a rectangular brass plate with a hand-shaped recess is set into the wall at frame-right beside the gate; a rusty ladder stands at frame-left.")
GATE_CLOSE = Scene('gate_room', GATE.end,
                   " Fixed stage layout: a close view of the big black iron hand-wheel filling the middle of the frame with the dull steel gate door behind it and the rectangular brass plate with a hand-shaped recess at frame-right; nobody in the scene.")
CONVOY_FAR = Scene('snow_field', FIELD.end,
                   " Fixed stage layout: a vast dark snowfield seen from far away fills the frame; along the far horizon at the back of the frame a long chain of tiny white headlights crawls slowly along a ridge road; a faint green aurora hangs above; nobody in the scene.")

AE = lambda en, zh: (en, zh)

# ================================================================================================ 第 59 集（A）
mode('A')
b59 = S.episode('剧本第59集｜末日橱窗', '苏清月和林峰来到潜望镜室，镜头里极光下五百个冰雕军阵像一座巨大的橱窗展览，苏清月说我穿着拖鞋看着他们，林峰说是运气和准备；一滴融水从冰雕的拳头上落下，伊甸报告地表温度零下三度、水位浮标升了两格，化冻开始了；收音机忽然传来周宁的声音，问他们还有没有暖气。', 59)
new_scene(b59, 'periscope_room', '潜望镜室（小小的圆形混凝土房间，一根粗黑的钢制潜望镜立柱，橡胶目镜，墙上有个盘子大的圆形屏幕）',
          'A small circular concrete room with a thick vertical black steel periscope column rising into the ceiling and a padded rubber eyepiece at chest height, and a round view screen the size of a dinner plate glowing on the wall.',
          '一间小小的圆形混凝土房间，一根粗粗的黑色钢制潜望镜立柱升进天花板，胸口高度有橡胶目镜，墙上有一块盘子大小发亮的圆形屏幕。',
          'the periscope column and the round view screen')
new_scene(b59, 'flood_bay', 'B3 泄洪舱（又长又窄的混凝土舱，左边是巨大的灰色钛合金墙板，铆钉接缝，银色管道，钢梯）',
          'A long narrow concrete flood-control bay with a huge grey titanium wall panel with riveted seams filling its left side, thick silver pipes along the ceiling and a steel ladder at the far end.',
          '一个又长又窄的混凝土泄洪舱，左边是巨大的灰色钛合金墙板，铆钉接缝，天花板上有粗粗的银色管道，远端有一架钢梯。',
          'the titanium wall panel and the ladder')
new_scene(b59, 'gate_room', 'B4 手动闸门室（朴素的混凝土小房间，后墙是两米高的圆形钢闸门，门中央一个车轮大的黑铁手轮，旁边墙上嵌着一块有手掌凹槽的黄铜板）',
          'A small bare concrete chamber whose back wall is filled by a massive round steel gate door with a big black iron hand-wheel at its centre and a rectangular brass plate with a hand-shaped recess set into the wall beside it.',
          '一个朴素的混凝土小房间，后墙被一扇巨大的圆形钢闸门占满，门中央是一个黑铁大手轮，旁边墙上嵌着一块有手掌凹槽的长方形黄铜板。',
          'the round gate, the hand-wheel and the brass plate')
new_person(b59, 'lin_flood', '林峰（潜水服）', 'man',
           'The same man in a black neoprene wetsuit with an orange life vest, a dive mask pushed up onto his wet hair and a small headlamp on his forehead, water running down his face.',
           '同一个男人，穿黑色氯丁橡胶潜水服和橙色救生背心，潜水面罩推到湿漉漉的头发上，额头上戴着小头灯，水顺着脸往下淌。',
           'in a black neoprene wetsuit with an orange life vest, a dive mask pushed up onto his wet hair and a small headlamp on his forehead, water running down his face',
           'a calm focused expression', ref='lin_work')
b59.character('LinFlood', 'lin_flood', LIN_EN, LIN_ZH)
b59.character('RadioPei', 'radio_set', RADIOPEI_EN, RADIOPEI_ZH)

INS('59-01', '01｜潜望镜室：圆形的小房间里，一根粗黑的钢潜望镜立柱升进天花板，橡胶目镜亮着微光，旁边墙上的圆形屏幕映着淡绿色的极光', 7, PERI,
    'Medium shot of the periscope room, the column and the round screen in the middle third of the frame, nobody in the scene.',
    "A thick black steel periscope column rises through the ceiling of the small round concrete room with its padded eyepiece glowing faintly, and the round screen on the wall shows a pale green aurora. Nothing else moves.",
    "小小的圆形混凝土房间里，一根粗粗的黑色钢制潜望镜立柱升进天花板，橡胶目镜微微发亮，墙上的圆形屏幕映着淡绿色的极光。别的什么都不动。",
    Q('A deep low hum of ventilation and the faint tick of cooling steel.', '通风系统深沉的低鸣和钢铁冷却时细细的嘀嗒声。'),
    'The frame holds the periscope room, and nobody in the scene.',
    slide('toward frame-right', '右', 'the glowing round screen fills the middle third of the frame', '发亮的圆形屏幕占满画面中间三分之一'),
    AE("Cool blue-white light from the round screen washes the curved concrete wall while a thin amber work-lamp glow rims the black steel column and fine dust turns in the light.",
       "圆形屏幕冷冷的蓝白色光洗过弧形的混凝土墙，一线琥珀色的工作灯光勾出黑色钢柱的边，细尘在光里慢慢转。"))

DL('59-02', '02｜潜望镜室：苏清月把眼睛贴在目镜上，林峰站在她身后，她说他们站成了橱窗，他说你是第一个看客，她说这展品我不想买，他说它们也不卖', PERI,
   [P('su_cozy', 'left', "leaning forward at the periscope column in profile facing frame-right with one eye at the padded eyepiece and one hand on the steel handle, her head tilted toward him", 'obj:the periscope eyepiece', "her lips parted in awe, her eyes narrowed with a cold fascination, her brows lifted", outfit=SU_SLIP),
    P('lin_home', 'right', "standing close behind her in profile facing frame-left, one hand resting on the steel column, his head turned toward her", 'Su', "his jaw easy, his eyes dark and calm, his brows level", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the thighs, in the middle third of the frame, at the periscope column.',
   [('su_cozy', "他们站成了橱窗。", 'lin_home', 'low awed', '低沉惊叹'),
    ('lin_home', "你是第一个看客。", 'su_cozy', 'low dry', '低沉干干地'),
    ('su_cozy', "这展品，我不想买。", 'lin_home', 'low wry', '低沉带讽'),
    ('lin_home', "它们也不卖。", 'su_cozy', 'low dry', '低沉干干地')],
   V('A deep low hum of ventilation, the faint squeak of a rubber eyepiece and a quiet breath.', '通风系统深沉的低鸣、橡胶目镜轻轻的吱吱声和一声安静的呼吸。'),
   AE("Cool blue-white light from the round screen at the back lays a pale rim along her cheek and his shoulder while a thin amber lamp warms the black steel column between them.",
      "后面圆形屏幕冷冷的蓝白色光在她的脸颊和他的肩头勾出一圈淡淡的边，一线琥珀色的灯光暖着他们之间的黑色钢柱。"),
   post_en='after the last line she lifts her eye from the eyepiece and turns to look straight at him',
   post_zh='最后一句之后，她把眼睛从目镜上抬起来，转过头直直地看着他',
   cam=push('both of them', '两人'), bg='Behind them the round view screen glows on the curved concrete wall at frame-right.')

INS('59-03', '03｜潜望镜里的雪原：淡绿色极光下，几百个裹在冰里的人和卡车一排排立在蓝色的黎明前微光里，冰面上有细细的深色水痕往下淌', 8, THAW,
    'Wide high shot of the whole snowfield, the rows of ice figures filling the middle third of the frame, nobody alive in the scene.',
    "Under a pale green aurora in deep blue pre-dawn light, rows of men and heavy trucks stand sheathed in clear ice across the snowfield, thin dark streaks of meltwater running down the ice and dark wet patches around the feet of the nearest figures. Nothing moves.",
    "淡绿色的极光下，蓝色的黎明前微光里，几百个裹在透明冰里的男人和重型卡车一排排立在雪原上，冰面上有细细的深色融水痕往下淌，最近的几个人脚边的雪上有深色的湿痕。一动不动。",
    Q('A long low howl of wind over the white plain and the faint glassy tick of ice.', '风掠过白色平原长长的低啸和冰细细的玻璃般的嘀嗒声。'),
    'The frame holds the snowfield of ice figures and trucks, and nobody alive in the scene.',
    rise('the whole frozen army under the fading aurora', '渐渐淡去的极光下整支冻住的军队'),
    AE("The fading green aurora slides a cold shimmer over the wet ice, pale blue dawn light glints on thin streams of meltwater and fine snow crystals drift through the air.",
       "渐渐淡去的绿色极光在湿漉漉的冰面上滑过一层冷冷的微光，淡蓝色的晨光在细细的融水流上闪着，细小的雪晶在空气里飘。"))

DL('59-04', '04｜潜望镜室：苏清月穿着毛绒拖鞋站在潜望镜旁，说她穿着拖鞋看着他们，林峰说他们在外面我们在里面，她问这就是活着的差别吗，他说是运气和准备', PERI,
   [P('su_cozy', 'left', "standing beside the periscope column in profile facing frame-right, her feet in fluffy white slippers and one hand resting on the steel handle, her head turned toward him", 'Lin', "her lips pressed into a thoughtful line, her eyes steady and a little haunted, her brows low", outfit=SU_SLIP),
    P('lin_home', 'right', "standing beside her in profile facing frame-left, his hands in the pockets of his lounge pants, his head turned toward her", 'Su', "his jaw set, his eyes dark and steady, his brows level", outfit=LIN_CLINIC)],
   'Medium wide two-shot, both from the head to the feet, in the middle third of the frame, at the periscope column.',
   [('su_cozy', "我穿着拖鞋，看着他们。", 'lin_home', 'low wondering', '低沉感慨'),
    ('lin_home', "他们在外面，我们在里面。", 'su_cozy', 'low calm', '低沉平静'),
    ('su_cozy', "这就是活着的差别？", 'lin_home', 'quiet probing', '安静试探'),
    ('lin_home', "是运气，和准备。", 'su_cozy', 'low steady', '低沉平稳')],
   V('A deep low hum of ventilation and a long quiet breath.', '通风系统深沉的低鸣和一声长长的安静的呼吸。'),
   AE("The blue-white glow of the round screen lights the soft white slippers on the concrete floor and draws a long pale rim down the two figures while a thin amber lamp warms the steel column.",
      "圆形屏幕蓝白色的光照亮水泥地上柔软的白色拖鞋，在两个人身上拉出一道长长的淡边，一线琥珀色的灯光暖着钢柱。"),
   post_en='after the last line <su_cozy> leans her shoulder against his arm and they both look at the round screen',
   post_zh='最后一句之后，苏清月把肩膀靠在他的手臂上，两人一起看着那块圆形屏幕',
   cam=pull('their faces', '两人的脸', 'the two of them and the glowing round screen behind', '两人和身后发亮的圆形屏幕'), bg='Behind them the round view screen glows on the curved concrete wall at frame-right.')

INS('59-05', '05｜冰雕特写：一个冻住的男人高举的拳头上挂着一根小冰棱，一滴明亮的融水从冰棱尖上落下，冰面上泛起一层薄薄的水光', 6, DROP,
    'Close shot of the iced fist and the icicle, the fist in the middle third of the frame, nobody alive in the scene.',
    "A single bright drop of meltwater hangs from a small icicle on a frozen man's clenched fist, falls and lands on the ice below, a thin wet shine spreading on the surface. Nothing else moves.",
    "一个冻住的男人紧握的拳头上挂着一根小冰棱，冰棱尖上一滴明亮的融水落下来，掉在下面的冰上，冰面上漫开一层薄薄的水光。别的什么都不动。",
    Q('A single clear drip and the faint creak of ice, then a deep hush.', '一声清脆的滴水和冰轻轻的吱嘎声，然后一片深深的寂静。'),
    'The frame holds the iced fist with the icicle, and nobody alive in the scene.',
    push1('the drop at the tip of the icicle', '冰棱尖上的那滴水'),
    AE("Cold pale dawn light glows through the clear ice like glass, the green aurora glints in the bright drop as it falls and a tiny ring of ripples spreads on the wet shine.",
       "冷冷的晨光像穿过玻璃一样透过透明的冰，绿色的极光在落下的那滴水里一闪，湿亮的冰面上漾开一圈细小的波纹。"))

DL('59-06', '06｜控制室：伊甸说地表温度零下三度，苏清月问冰是不是开始化了，伊甸说水位浮标上升两格，林峰说化冻开始了', CONTROL_RADIO,
   [P('su_cozy', 'left', "standing at the control console in profile facing frame-right, one hand on its edge, her head lifted toward the wall speaker", 'obj:the wall speaker above the console', "her lips parting, her eyes wide and alert, her brows pulled together", outfit=SU_CLINIC),
    P('lin_home', 'right', "standing beside the steel side table in profile facing frame-left, his arms crossed, his head lifted toward the wall speaker", 'obj:the wall speaker above the console', "his jaw tightening, his eyes dark and sharp, his brows low", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the console.',
   [('eden_voice', "地表温度，零下三度。", 'su_cozy', 'soft calm', '轻柔平静'),
    ('su_cozy', "冰，开始化了？", 'lin_home', 'tense low', '紧张低沉'),
    ('eden_voice', "水位浮标，上升两格。", 'lin_home', 'soft calm', '轻柔平静'),
    ('lin_home', "化冻开始了。", 'su_cozy', 'low grave', '低沉凝重')],
   V('A soft electronic chime, the hum of the console and a held breath.', '一声轻轻的电子提示音、控制台的嗡鸣和一声屏住的呼吸。'),
   AE("Cool green status-light glow rims their faces from the console, the thin blue ring of the wall speaker glows above them and warm amber light from the side table falls across Lin's shoulder.",
      "控制台冷冷的绿色指示灯光勾出他们脸的轮廓，头顶扬声器那圈细细的蓝光亮着，侧桌上温暖的琥珀色灯光落在林峰的肩上。"),
   post_en='after the last line <su_cozy> slowly closes her hand into a fist on the console edge',
   post_zh='最后一句之后，苏清月慢慢把放在控制台边的手攥成拳头',
   cam=lowrise('the two of them at the console', '控制台边的两个人'), bg='On the wall above the console a flat speaker panel with a thin glowing blue ring glows.',
   extra_assets=('radio_set',))

DL('59-07', '07｜控制室：收音机忽然沙沙响起周宁的声音，说他是周宁问他们还有没有暖气，林峰对苏清月说是周宁，苏清月问要不要回应，林峰说先听', CONTROL_RADIO,
   [P('su_cozy', 'left', "standing at the control console in profile facing frame-right, her head turned toward the radio", 'obj:the olive-green radio on the side table', "her lips pressed together, her eyes sharp and wary, her brows pulled together", outfit=SU_CLINIC),
    P('lin_home', 'right', "standing beside the steel side table in profile facing frame-left, one hand reaching toward the round volume knob of the radio, his head turned toward it", 'obj:the olive-green radio on the side table', "his jaw clenched, his eyes dark and unreadable, his brows low", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the console.',
   [('radio_ning', "是我，周宁。", 'lin_home', 'hoarse frantic', '嘶哑慌乱'),
    ('lin_home', "是周宁。", 'su_cozy', 'low flat', '低沉平淡'),
    ('radio_ning', "你们那儿，还有暖气吗？", 'lin_home', 'hoarse pleading', '嘶哑哀求'),
    ('su_cozy', "你要回应吗？", 'lin_home', 'low quick', '低沉急促'),
    ('lin_home', "先听。", 'su_cozy', 'low steady', '低沉平稳')],
   V('Crackling radio static with a thin tuning whistle and the hum of the control room.', '收音机沙沙的杂音、细细的调频啸叫和控制室的嗡鸣。'),
   AE("The amber dial of the radio glows warm on the side table and throws a small flickering light across Lin's reaching hand while the cool green console glow rims her face.",
      "收音机琥珀色的调谐盘在侧桌上发着暖光，把一小片闪烁的光洒在林峰伸出的手上，冷冷的绿色控制台光勾着她的脸。"),
   post_en='after the last line <lin_home> turns the volume knob up one notch and the static grows louder',
   post_zh='最后一句之后，林峰把音量旋钮往上拧了一格，杂音变大了',
   cam=push('both of them', '两人'), bg='On the steel side table at frame-right the olive-green long-wave radio glows with its amber dial.',
   extra_assets=('radio_set',))

# ================================================================================================ 第 60 集（A＋B）
b60 = S.episode('剧本第60集｜周宁与裴远山', '周宁在收音机里哀求，说他被一支军队抓住了；军阀裴远山接过话筒，说林先生，您的暖气在雪地里像一盏灯，三天后钻机到您门口；苏清月说他是饵也是人，林峰说我想先活下来；林峰在地图上圈出三公里外的冰碛湖，苏清月说你想用水，林峰说水比子弹公平；伊甸报告十二公里外有外部振动，是钻机。', 60)
mode('A')

DL('60-01', '01｜控制室：收音机里周宁哀求说他知道林峰在听，说他被一支军队抓住了，他们逼他说出林峰的位置，苏清月低声说别回答', CONTROL_RADIO,
   [P('su_cozy', 'left', "standing at the control console in profile facing frame-right, her hand tight on the console edge, her head turned toward the radio", 'obj:the olive-green radio on the side table', "her lips pressed into a white line, her eyes cold and sharp, her brows low", outfit=SU_CLINIC),
    P('lin_home', 'right', "standing beside the steel side table in profile facing frame-left, one hand hovering over the microphone of the radio without touching it, his head turned toward it", 'obj:the olive-green radio on the side table', "his jaw clenched, his eyes dark and still, his brows low", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the console.',
   [('radio_ning', "我知道你在听！", 'lin_home', 'hoarse pleading', '嘶哑哀求'),
    ('radio_ning', "我被一支军队抓住了！", 'lin_home', 'hoarse frantic', '嘶哑慌乱'),
    ('radio_ning', "他们逼我说出你的位置！", 'lin_home', 'hoarse breaking', '嘶哑发颤'),
    ('su_cozy', "别回答。", 'lin_home', 'low firm', '低沉坚定')],
   V('Crackling radio static, a thin tuning whistle and the hum of the control room.', '收音机沙沙的杂音、细细的调频啸叫和控制室的嗡鸣。'),
   AE("The radio's amber dial flickers across his hovering hand and her clenched knuckles while cool green console light rims both their profiles and the static makes the light tremble.",
      "收音机琥珀色的调谐盘光在他悬着的手和她攥紧的指节上闪动，冷冷的绿色控制台光勾着两人的侧脸，杂音让光微微颤抖。"),
   post_en='after the last line <lin_home> slowly draws his hand back from the microphone and closes it into a fist',
   post_zh='最后一句之后，林峰慢慢把手从话筒上收回来，攥成了拳头',
   cam=push1('his hovering hand and the radio', '他悬着的手和收音机'), bg='On the steel side table at frame-right the olive-green long-wave radio glows with its amber dial.',
   extra_assets=('radio_set',))

DL('60-02', '02｜控制室：收音机里换成一个冷静客气的男人的声音，说他是裴远山，说冰一化，林先生的暖气在雪地里像一盏灯，三天后钻机就到他门口', CONTROL_RADIO,
   [P('su_cozy', 'left', "standing at the control console in profile facing frame-right, her arms folded tight across her chest, her head turned toward the radio", 'obj:the olive-green radio on the side table', "her lips thin, her eyes narrowed and cold, her brows low", outfit=SU_CLINIC),
    P('lin_home', 'right', "standing beside the steel side table in profile facing frame-left, one hand flat on the steel table beside the radio, his head turned toward it", 'obj:the olive-green radio on the side table', "his jaw set hard, his eyes dark and dangerous, his brows low", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the console.',
   [('radio_pei', "我是裴远山，林先生。", 'lin_home', 'cold courteous', '冷静客气'),
    ('radio_pei', "冰一化，您的暖气像盏灯。", 'lin_home', 'slow courteous', '不紧不慢客气'),
    ('radio_pei', "三天后，钻机到您门口。", 'lin_home', 'cold patient', '冰冷耐心')],
   V('Crackling radio static, a faint metallic click and the hum of the control room.', '收音机沙沙的杂音、一声细细的金属咔嗒和控制室的嗡鸣。'),
   AE("The radio's amber dial throws a small flickering glow onto Lin's hard jaw while cool green console light cuts a sharp rim along her folded arms and a thin line of static shivers over the speaker grille.",
      "收音机琥珀色的调谐盘在林峰紧绷的下颌上洒下一小片闪烁的光，冷冷的绿色控制台光沿着她交叠的手臂勾出一道锐利的边，一线细细的杂音在扬声器布面上颤动。"),
   post_en='after the last line <lin_home> reaches out and switches the radio off with one finger',
   post_zh='最后一句之后，林峰伸出一根手指，把收音机关掉',
   cam=pull('the radio dial', '收音机的调谐盘', 'the two of them stand in the middle third of the frame', '两人站在画面中间三分之一'), bg='On the steel side table at frame-right the olive-green long-wave radio glows with its amber dial.',
   extra_assets=('radio_set',))

DL('60-03', '03｜控制室：收音机关掉后，苏清月说周宁在他们手里，林峰说他是饵也是人，她问你想救他吗，他说我想先活下来', CONTROL_RADIO,
   [P('su_cozy', 'left', "standing at the control console in profile facing frame-right, her arms loosely crossed, her head turned toward him", 'Lin', "her lips pressed together, her eyes fierce and searching, her brows pulled together", outfit=SU_CLINIC),
    P('lin_home', 'right', "standing beside the steel side table in profile facing frame-left, his hand resting beside the dark radio, his head turned toward her", 'Su', "his jaw hard, his eyes dark and tired, his brows low", outfit=LIN_CLINIC)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, at the console.',
   [('su_cozy', "周宁在他们手里。", 'lin_home', 'low tight', '低沉发紧'),
    ('lin_home', "他是饵，也是人。", 'su_cozy', 'low flat', '低沉平淡'),
    ('su_cozy', "你想救他吗？", 'lin_home', 'quiet probing', '安静试探'),
    ('lin_home', "我想先活下来。", 'su_cozy', 'low steady', '低沉平稳')],
   V('A deep low hum of the control room and a long quiet breath.', '控制室深沉的低鸣和一声长长的安静的呼吸。'),
   AE("Cool green console light rims her cheek and the dark radio on the table sheds no glow, so a thin warm amber lamp from behind lays a gold edge on his shoulder.",
      "冷冷的绿色控制台光勾着她的脸颊，桌上暗下去的收音机不再发光，身后一线温暖的琥珀色灯光在他的肩上镀了一道金边。"),
   post_en='after the last line <su_cozy> lowers her eyes and lets out one slow breath',
   post_zh='最后一句之后，苏清月垂下眼睛，缓缓呼出一口气',
   cam=push('both of them', '两人'), bg='On the steel side table at frame-right the olive-green long-wave radio sits dark and silent.',
   extra_assets=('radio_set',))

mode('B')
DL('60-04', '04｜餐桌：林峰和苏清月围着铺满桌面的手绘地图，他用红笔圈出三公里外一座小湖，说那是冰碛湖，她问你想用水，他说水比子弹公平，她问那闸门呢，他说只认我的手', PLAN,
   [P('su_cozy', 'left', "leaning over the round dining table in profile facing frame-right, both hands on the edge of a large hand-drawn map, her head turned toward him", 'Lin', "her lips parted, her eyes sharp and quick, her brows lifted", outfit=SU_CLINIC),
    P('lin_home', 'right', "leaning over the table in profile facing frame-left, a red pencil in his right hand circling a small blue lake on the map, his head turned toward her", 'Su', "his jaw set, his eyes dark and certain, his brows level", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, over the map on the dining table.',
   [('lin_home', "三公里外，有座冰碛湖。", 'su_cozy', 'low steady', '低沉平稳'),
    ('su_cozy', "你想用水？", 'lin_home', 'quick sharp', '急促锐利'),
    ('lin_home', "水比子弹公平。", 'su_cozy', 'low dry', '低沉干干地'),
    ('su_cozy', "那闸门呢？", 'lin_home', 'quick', '急促'),
    ('lin_home', "只认我的手。", 'su_cozy', 'low calm', '低沉平静')],
   V('The scratch of a red pencil on paper, the soft rustle of the map and the hum of the stove.', '红铅笔划过纸面的沙沙声、地图轻轻的摩擦声和炉灶的嗡鸣。'),
   AE("Warm amber lamp light falls on the creased map and the red circle glows like a fresh wound while the cold blue of the monitor wall rims their shoulders.",
      "温暖的琥珀色灯光落在起了折痕的地图上，那个红圈像新鲜的伤口一样醒目，监控墙冷冷的蓝光勾着他们的肩膀。"),
   post_en='after the last line <lin_home> taps the red circle twice with the pencil',
   post_zh='最后一句之后，林峰用铅笔在那个红圈上点了两下',
   cam=tilt('the red circle on the map', '地图上的红圈'), bg='Behind them the black-and-gold stove glows ember-orange at frame-left.')

DL('60-05', '05｜餐桌：伊甸报告十二公里外检测到外部振动，林峰说是钻机，苏清月问这么快，伊甸说正以每小时一公里靠近', PLAN,
   [P('su_cozy', 'left', "standing at the dining table in profile facing frame-right, one hand on the map, her head lifted toward the wall speaker", 'obj:the wall speaker above the table', "her lips parting, her eyes wide and alert, her brows pulled together", outfit=SU_CLINIC),
    P('lin_home', 'right', "standing at the dining table in profile facing frame-left, the red pencil frozen in his fingers, his head lifted toward the wall speaker", 'obj:the wall speaker above the table', "his jaw going still, his eyes sharp and dark, his brows low", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dining table.',
   [('eden_voice', "外部振动，十二公里外。", 'lin_home', 'soft calm', '轻柔平静'),
    ('lin_home', "是钻机。", 'su_cozy', 'low grave', '低沉凝重'),
    ('su_cozy', "这么快？", 'lin_home', 'tense quick', '紧张急促'),
    ('eden_voice', "正以每小时一公里靠近。", 'su_cozy', 'soft calm', '轻柔平静')],
   V('A soft electronic chime, a deep low tremor in the floor and a held breath.', '一声轻轻的电子提示音、地板深处低低的震颤和一声屏住的呼吸。'),
   AE("The thin blue ring of the wall speaker glows above them, warm lamp light turns cold on their faces and the red pencil lines on the map tremble slightly with the vibration.",
      "头顶墙上扬声器那圈细细的蓝光亮着，温暖的灯光落到他们脸上变冷了，地图上红铅笔的线条随着震动微微发颤。"),
   post_en='after the last line the mugs on the table shiver and <lin_home> lays the pencil down on the map',
   post_zh='最后一句之后，桌上的杯子微微发颤，林峰把铅笔放在地图上',
   cam=lowrise('the two of them at the table', '桌边的两个人'), bg='On the wall above the table a flat speaker panel with a thin glowing blue ring glows.')

INS('60-06', '06｜控制室：橄榄绿的收音机特写，大圆调谐盘的琥珀色光里，指针停在一个频率上微微发抖，杂音沙沙', 6, RADIO_CLOSE,
    'Close shot of the radio dial, the round dial in the middle third of the frame, nobody in the scene.',
    "An olive-green long-wave radio sits on a steel table with its large round dial glowing amber and the needle trembling at one frequency while the cloth speaker grille faintly vibrates. Nothing else moves.",
    "一台橄榄绿的长波收音机放在钢桌上，大大的圆形调谐盘亮着琥珀色的光，指针停在一个频率上微微发抖，布面扬声器轻轻震动。别的什么都不动。",
    Q('Crackling radio static and a thin tuning whistle, then a deep hush.', '收音机沙沙的杂音和细细的调频啸叫，然后一片深深的寂静。'),
    'The frame holds the radio dial, and nobody in the scene.',
    push1('the trembling needle', '发抖的指针'),
    AE("The amber dial glows like a small sun, the green console lights blur behind in bokeh and a faint haze of dust glitters in the light of the dial.",
       "琥珀色的调谐盘像一轮小太阳，后面控制台的绿色指示灯虚成光斑，调谐盘的光里有一层淡淡的尘雾闪着。"),
    extra_assets=('radio_set',))

# ================================================================================================ 第 61 集（B）
b61 = S.episode('剧本第61集｜冰雪消融的警钟', '雪原上的冰开始大面积融化，泄洪舱里林峰和苏清月给钛合金墙涂防水层、装液压撑杆，两人拿旧诱饵井斗嘴；晚上林峰煮了面，苏清月问他今天怎么这么殷勤，他说怕你冷；泵房里水位浮标又升了两格；伊甸报告B3外壁出现零点二毫米的微裂，林峰赶去看，裂缝里喷出一条高压的细水柱。', 61)
mode('B')

INS('61-01', '01｜地表雪原：黎明前的蓝色微光里，冰雕们身上的冰在融化，雪地里汇出一道道细细的深色水流，慢慢流向低处', 7, THAW,
    'Wide low shot of the snowfield, the ice figures and the streams in the middle third of the frame, nobody alive in the scene.',
    "In deep blue dawn light thin dark streams of meltwater run down the ice of the frozen figures and gather into rivulets across the snow, flowing slowly toward lower ground. Nothing else moves.",
    "黎明前深蓝色的微光里，冰雕们身上的冰在融化，细细的深色融水顺着冰往下淌，在雪地里汇成一道道细流，慢慢流向低处。别的什么都不动。",
    Q('The soft trickle of running water over ice and the faint creak of settling snow.', '融水淌过冰面轻轻的潺潺声和积雪落定时轻轻的吱嘎声。'),
    'The frame holds the snowfield of ice figures and the meltwater streams, and nobody alive in the scene.',
    descend('the meltwater streams between the ice figures', '冰雕之间的融水细流'),
    AE("Pale dawn light glints on the running water and the wet ice, a thin mist of vapor lifts from the thawing snow and the last green of the aurora ripples in the streams.",
       "淡淡的晨光在流动的水和湿漉漉的冰面上闪着，融化的雪地里升起一层薄薄的水汽，极光最后的一点绿色在细流里漾着。"))

DL('61-02', '02｜泄洪舱：苏清月拿滚筒给钛合金墙涂防水层，林峰蹲在旁边递涂料桶，她问刷哪边，他说左边刷两遍，她说你怎么不说请，他说请，刷两遍', FLOOD_DRY,
   [P('su_cozy', 'left', "standing at the titanium wall in profile facing frame-left, a paint roller loaded with grey sealant in both hands rolling it up the wall, her head turned toward him", 'Lin', "her lips curving in a teasing sweet smile, her eyes bright, her brows lifted", outfit=SU_WORK),
    P('lin_home', 'right', "crouching beside a can of grey sealant in profile facing frame-left, one hand holding the paint tray up toward her, his head turned toward her", 'Su', "his lips pressed into a dry amused sweet smile, his eyes warm, his brows soft", outfit=LIN_WORK)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the titanium wall.',
   [('su_cozy', "防水层，我刷哪边？", 'lin_home', 'bright', '明亮'),
    ('lin_home', "左边，刷两遍。", 'su_cozy', 'low dry', '低沉干干地'),
    ('su_cozy', "你怎么不说请？", 'lin_home', 'bright teasing', '明亮逗弄'),
    ('lin_home', "请，刷两遍。", 'su_cozy', 'low amused', '低沉带笑'),
    ('su_cozy', "这还差不多。", 'lin_home', 'bright satisfied', '明亮满意')],
   V('The soft wet slap of a paint roller on metal, the clink of a tray and a warm laugh.', '滚筒滚过金属墙面湿润的啪嗒声、涂料盘的叮当声和一声温暖的笑。'),
   AE("Cold white work-lamp light glints on the wet grey sealant as the roller leaves a bright stripe up the titanium wall and a thin mist of solvent drifts through the beam.",
      "冷白色的工作灯光在湿漉漉的灰色涂料上闪着，滚筒在钛合金墙上留下一道明亮的条纹，一层薄薄的溶剂雾气在光柱里飘。"),
   post_en='after the last line <su_cozy> dabs a dot of grey sealant on his nose with the tip of the roller',
   post_zh='最后一句之后，苏清月用滚筒尖在他的鼻尖上点了一点灰色涂料',
   cam=slide('toward frame-left', '左', 'the two of them fill the middle third of the frame', '两人占满画面中间三分之一'), bg='Behind them the long concrete bay stretches away under thick silver pipes.')

INS('61-03', '03｜泄洪舱：一排液压撑杆顶着刚涂好的灰色墙面，压力表的指针稳稳停在绿色区域', 6, FLOOD_BRACE,
    'Medium shot of the brace jacks and a gauge, the row of rams in the middle third of the frame, nobody in the scene.',
    "A row of heavy hydraulic steel rams stands braced hard against the freshly sealed grey wall and the needle of a round pressure gauge on the nearest ram rests steadily in the green zone. Nothing else moves.",
    "一排厚重的液压钢撑杆死死顶着刚涂好的灰色墙面，最近那根撑杆上圆形压力表的指针稳稳停在绿色区域。别的什么都不动。",
    Q('A soft hydraulic hiss that fades and the faint tick of settling steel.', '液压轻轻的嘶嘶声渐渐消失和钢铁落定时细细的嘀嗒声。'),
    'The frame holds the brace jacks and the pressure gauge, and nobody in the scene.',
    slide('toward frame-right', '右', 'the green zone of the gauge fills the middle third of the frame', '压力表的绿色区域占满画面中间三分之一'),
    AE("Cold white work-lamp light gleams along the polished rams and the green zone of the gauge glows like a small emerald while a thin mist of dust floats in the beams.",
       "冷白色的工作灯光沿着抛光的撑杆闪着，压力表的绿色区域像一颗小小的祖母绿一样发亮，薄薄的尘雾在光柱里浮着。"))

DL('61-04', '04｜泄洪舱：涂好的墙边一排液压撑杆已经装好，苏清月说十二根都装好了，林峰问诱饵井那边呢，她说排气口封了只剩假的，他说假的才是最好的饵', FLOOD_BRACE,
   [P('su_cozy', 'left', "standing beside the row of hydraulic brace jacks in profile facing frame-right, a slim tablet in her left hand, her head turned toward him", 'Lin', "her lips curving in a wry sweet smile, her eyes bright and tired, her brows lifted", outfit=SU_WORK),
    P('lin_home', 'right', "standing beside a brace jack in profile facing frame-left, a long wrench in his right hand resting on his shoulder, his head turned toward her", 'Su', "his lips pressed into a dry half sweet smile, his eyes warm and dark, his brows level", outfit=LIN_WORK)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, beside the brace jacks.',
   [('su_cozy', "撑杆装好了，十二根。", 'lin_home', 'bright tired', '明亮带疲惫'),
    ('lin_home', "诱饵井那边呢？", 'su_cozy', 'low curious', '低沉好奇'),
    ('su_cozy', "排气口封了，只剩假的。", 'lin_home', 'quick wry', '利落带讽'),
    ('lin_home', "假的，才是最好的饵。", 'su_cozy', 'low dry', '低沉干干地')],
   V('The metallic clank of a wrench on a steel jack, a soft hiss of hydraulics and a tired laugh.', '扳手碰在钢制撑杆上的叮当声、液压轻轻的嘶嘶声和一声疲惫的笑。'),
   AE("Cold white work-lamp light gleams along the polished hydraulic rams in a long row, the fresh grey seal on the wall glows matte and dust floats in the beams.",
      "冷白色的工作灯光沿着一长排抛光的液压杆闪着光，墙上新涂的灰色涂层泛着哑光，尘埃在光柱里浮着。"),
   post_en='after the last line <lin_home> raps the wrench twice against the nearest brace jack',
   post_zh='最后一句之后，林峰用扳手在最近的一根撑杆上敲了两下',
   cam=track('the two of them', '他们两个'), bg='Behind them the row of hydraulic brace jacks recedes down the long concrete bay.')

DL('61-05', '05｜餐桌：苏清月用平板算出湖水三天就会涨满，林峰问够用几次，她说一次，只够一次，他说一次就够', PLAN,
   [P('su_cozy', 'left', "sitting at the round dining table in profile facing frame-right, a slim tablet in both hands showing a rising blue curve, her head turned toward him", 'Lin', "her lips pressed together, her eyes sharp and tired, her brows low", outfit=SU_CLINIC),
    P('lin_home', 'right', "sitting across the table in profile facing frame-left, one hand flat on the hand-drawn map, his head turned toward her", 'Su', "his jaw set, his eyes dark and certain, his brows level", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the chest, in the middle third of the frame, at the dining table.',
   [('su_cozy', "按这个融速，湖水三天满。", 'lin_home', 'quick sharp', '利落锐利'),
    ('lin_home', "够我们用几次？", 'su_cozy', 'low curious', '低沉好奇'),
    ('su_cozy', "一次。只够一次。", 'lin_home', 'low tight', '低沉发紧'),
    ('lin_home', "一次就够。", 'su_cozy', 'low calm', '低沉平静')],
   V('The soft tap of a finger on a tablet, the rustle of paper and the hum of the stove.', '手指轻点平板的轻响、纸张的沙沙声和炉灶的嗡鸣。'),
   AE("The cool blue glow of the tablet lights her chin and the rising curve while warm amber lamp light falls across the creased map and his hand.",
      "平板冷冷的蓝光照亮她的下巴和那条上升的曲线，温暖的琥珀色灯光落在起了折痕的地图和他的手上。"),
   post_en='after the last line <su_cozy> turns the tablet around and slides it across the map to him',
   post_zh='最后一句之后，苏清月把平板转过来，从地图上推到他面前',
   cam=push('both of them', '两人'), bg='Behind them the black-and-gold stove glows ember-orange at frame-left.')

DL('61-06', '06｜餐桌：桌上两碗冒着热气的面，林峰把一碗推到苏清月面前，她问他今天怎么这么殷勤，他说怕你冷，她说这里二十六度，他说我说的不是这里', LIV_NOODLE,
   [P('su_cozy', 'left', "sitting at the round dining table in profile facing frame-right, chopsticks lifting a tangle of noodles, her head turned toward him", 'Lin', "her lips curving in a suspicious sweet smile, her eyes bright, her brows lifted", outfit=SU_CLINIC),
    P('lin_home', 'right', "sitting across the table in profile facing frame-left, one hand pushing a steaming bowl toward her, his head turned toward her", 'Su', "his lips pressed into a quiet half sweet smile, his eyes soft and dark, his brows soft", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the chest, in the middle third of the frame, at the dining table.',
   [('su_cozy', "你今天好殷勤。", 'lin_home', 'bright suspicious', '明亮带怀疑'),
    ('lin_home', "怕你冷。", 'su_cozy', 'low soft', '低沉轻柔'),
    ('su_cozy', "这里二十六度。", 'lin_home', 'bright wry', '明亮带讽'),
    ('lin_home', "我说的，不是这里。", 'su_cozy', 'low gentle', '低沉温柔')],
   V('The soft slurp of noodles, the clink of chopsticks on porcelain and the warm crackle of the stove.', '面条轻轻的吸溜声、筷子碰瓷碗的响声和炉灶温暖的噼啪声。'),
   AE("Honey-gold lamp light makes the broth glow and the fried eggs shine, steam rises in slow curls between them and the amber stove glow lies warm across the table.",
      "蜂蜜般的金色灯光让汤发亮、煎蛋闪着光，热气在他们之间慢慢卷着往上升，炉灶琥珀色的光暖暖地铺在桌面上。"),
   post_en='after the last line she goes quiet and slowly sets her chopsticks down on the rim of the bowl',
   post_zh='最后一句之后，她安静下来，慢慢把筷子搁在碗沿上',
   cam=push('both of them', '两人'), bg='Behind them the black-and-gold stove glows ember-orange at frame-left.')

INS('61-07', '07｜泵房：透明水箱里，红色浮标又往上浮了两格，白色标尺的刻度线被水面漫过，水面泛着细细的波纹', 6, BUOY2,
    'Medium shot of the tank and its scale, the red float in the middle third of the frame, nobody in the scene.',
    "Inside the tall clear water tank the red float marker has risen two more notches along the vertical white scale, the water rippling faintly around it. Nothing else moves.",
    "高高的透明水箱里，红色的浮标沿着白色竖直标尺又往上浮了两格，周围的水面泛起细细的波纹。别的什么都不动。",
    Q('A single soft drip, the faint gurgle of water in a pipe and a deep hush.', '一声轻轻的滴水、管子里细细的水流声和深深的寂静。'),
    'The frame holds the water tank with the red float and the scale, and nobody in the scene.',
    push1('the red float high on the scale', '标尺高处的红色浮标'),
    AE("Cool white work-lamp light glints on the rising water, the red float glows like a warning lamp and a bright ring of ripples spreads out across the surface.",
       "冷白色的工作灯光在上升的水面上闪着，红色的浮标像一盏警示灯一样发亮，一圈明亮的波纹在水面上扩散开。"))

DL('61-08', '08｜控制室：红灯忽然闪烁，伊甸报告B3外壁出现微裂，苏清月问多宽，伊甸说零点二毫米，林峰说马上去看', CONTROL_BTN,
   [P('su_cozy', 'left', "standing at the control console in profile facing frame-right, both hands on the console, her head lifted toward the wall speaker", 'obj:the wall speaker above the console', "her lips parting, her eyes wide and alert, her brows pulled together", outfit=SU_CLINIC),
    P('lin_home', 'right', "standing beside her in profile facing frame-left, one hand already on the strap of a toolbag on his shoulder, his head lifted toward the wall speaker", 'obj:the wall speaker above the console', "his jaw tightening, his eyes sharp and dark, his brows low", outfit=LIN_WORK)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the console.',
   [('eden_voice', "三号舱外壁，出现微裂。", 'lin_home', 'soft urgent', '轻柔急切'),
    ('su_cozy', "多宽？", 'lin_home', 'tense quick', '紧张急促'),
    ('eden_voice', "零点二毫米。", 'su_cozy', 'soft calm', '轻柔平静'),
    ('lin_home', "马上去看。", 'su_cozy', 'low firm', '低沉坚定')],
   V('A sharp rising electronic alarm, the hum of the console and a quick breath.', '一声尖锐渐强的电子警报、控制台的嗡鸣和一声急促的呼吸。'),
   AE("A pulsing red glow floods the console and paints a hard red rim along both faces while the thin blue ring of the wall speaker glows above them.",
      "一阵脉动的红光洒满控制台，在两张脸上勾出硬朗的红边，头顶墙上扬声器那圈细细的蓝光亮着。"),
   post_en='after the last line <lin_home> swings the toolbag onto his shoulder and strides out through the steel door at frame-right',
   post_zh='最后一句之后，林峰把工具包甩到肩上，大步走出右边的钢门',
   cam=slide('toward frame-right', '右', 'the two of them fill the middle third of the frame', '两人占满画面中间三分之一'), bg='On the wall above the console a flat speaker panel with a thin glowing blue ring glows.',
   exit=('Lin',))

INS('61-09', '09｜泄洪舱：灰色钛合金墙板上一道头发丝一样细的裂缝，一条高压的细水柱从缝里横着喷过来，白色的水雾弥漫在空气里', 7, FLOOD_JET,
    'Medium shot of the wall and the jet, the crack and the spray in the middle third of the frame, nobody in the scene.',
    "A thin high-pressure jet of clear water sprays sideways out of a hairline crack in the grey titanium wall and across the bay in a long white blade, white mist hanging in the air and the wet floor shining below. Nothing else moves.",
    "灰色的钛合金墙板上有一道头发丝一样细的裂缝，一条高压的细水柱从缝里横着喷出来，划过整个舱，白色的水雾飘在空气里，下面湿漉漉的地面闪着光。别的什么都不动。",
    Q('A hard hissing spray of water, a pulsing electronic alarm far away and a deep rumble in the wall.', '水猛烈喷出的嘶嘶声、远处脉动的电子警报和墙里深沉的隆隆声。'),
    'The frame holds the cracked wall and the jet of water, and nobody in the scene.',
    push1('the hairline crack and the jet', '头发丝一样的裂缝和水柱'),
    AE("The white jet glitters in the cold work-lamp light like a blade of glass, red emergency strobes pulse through the mist and fine droplets sparkle in the air.",
       "白色的水柱在冷冷的工作灯光里像一把玻璃刀一样闪着光，红色的应急频闪穿过水雾脉动，细小的水珠在空气里闪烁。"),
    )

# ================================================================================================ 第 62 集（A）
b62 = S.episode('剧本第62集｜倒灌危机', '裂缝喷出的水柱把一块木板切成两半；林峰穿上潜水服下到泄洪舱，用等离子焊枪补缝，苏清月在控制室戴着耳机指挥他；焊好后水位下降，林峰湿淋淋地被苏清月用毛巾裹住，墙外传来撞墙的水声，他说外面的水在撞墙，她说里面滴水不漏；他带她去看B4手动闸门，手轮锁只认他的手掌，她说你最好永远别开，他说我答应你；潜望镜里，远处雪原上亮起一长串白色的车灯。', 62)
mode('A')

INS('62-01', '01｜泄洪舱：细水柱把一块立在地上的木板拦腰切成了两半，两半木板倒在湿地上，水柱依旧喷着，积水漫过地面', 8, FLOOD_PLANK,
    'Medium low shot of the cut plank on the wet floor and the jet beyond it, the two halves in the middle third of the frame, nobody in the scene.',
    "A pale wooden plank lies cut cleanly in two halves on the wet floor where the thin white jet struck it, the jet still spraying across the bay behind it and water pooling around the halves. Nothing else moves.",
    "一块浅色的木板被细白的水柱拦腰切成两半，倒在湿漉漉的地上，水柱依旧在它后面横着喷过整个舱，水在两半木板周围积起来。别的什么都不动。",
    Q('A hard hissing spray of water, the drip of a pooling puddle and a deep rumble in the wall.', '水猛烈喷出的嘶嘶声、积水滴落的声音和墙里深沉的隆隆声。'),
    'The frame holds the cut plank and the jet, and nobody in the scene.',
    follow('the line of the jet', '水柱的方向', 'the two halves of the plank lie in the middle third of the frame', '两半木板落在画面中间三分之一'),
    AE("Red emergency strobes pulse through the mist and flash on the white blade of the jet while the cut ends of the plank show pale and clean in the cold work-lamp light.",
       "红色的应急频闪穿过水雾，在白色的水柱上一闪一闪，木板的断口在冷冷的工作灯光里显得浅色而整齐。"))

DL('62-02', '02｜泄洪舱：穿着黑色潜水服的林峰站在齐膝深的黑水里，举着焊枪对着墙缝，通过耳机和苏清月说话，苏清月让他听见吗，他说水到腰了，她说她来念参数，他说念吧', FLOOD_WATER,
   [P('lin_flood', 'right', "standing knee-deep in dark water in profile facing frame-left, a plasma welding torch in his right hand held toward the hairline crack, a thin jet of water spraying past his shoulder, his head turned toward the crack", 'obj:the hairline crack in the titanium wall', "his jaw clenched, his eyes narrowed under the headlamp beam, his brows low")],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the flooded bay.',
   [('su_cozy', "听得见吗？", 'lin_flood', 'calm sharp', '冷静锐利'),
    ('lin_flood', "听得见。水到腰了。", 'su_cozy', 'low steady', '低沉平稳'),
    ('su_cozy', "我念参数，你听着。", 'lin_flood', 'calm firm', '冷静坚定'),
    ('lin_flood', "念吧。", 'su_cozy', 'low calm', '低沉平静')],
   V('A hard hissing spray of water, the slosh of knee-deep water and the crackle of radio static in an earpiece.', '水猛烈喷出的嘶嘶声、齐膝深的水哗啦的晃动声和耳机里电流的沙沙声。'),
   AE("The white beam of his headlamp cuts through the drifting mist and glints on the black wetsuit, red emergency strobes pulse on the water and the spraying jet glitters blue-white in the light.",
      "他头灯的白色光束划开飘着的水雾，在黑色潜水服上闪着，红色的应急频闪在水面上脉动，喷出的水柱在光里闪着蓝白色。"),
   pre_en='A small headset speaker crackles beside his ear.', pre_zh='他耳边的小耳机里沙沙响着。',
   post_en='after the last line he pulls the dive mask down over his eyes and raises the torch to the crack',
   post_zh='最后一句之后，他把潜水面罩拉下来罩住眼睛，把焊枪举向墙缝',
   cam=push1('his masked face and the torch', '他戴上面罩的脸和焊枪'), bg='Behind him the titanium wall with its hairline crack fills frame-left.',
   vd={'su_cozy': B7.VD['su_cozy']}, ld={'lin_flood': ('into the headset microphone clipped at his jaw', '对着别在下巴边的耳麦')})

INS('62-03', '03｜泄洪舱：钛合金墙板上那道裂缝已经被一条明亮的焊缝封住，橙白色的焊缝在慢慢变暗，水柱消失了，水珠一滴一滴落进水里', 6, FLOOD_WELD,
    'Medium shot of the wall and the weld, the glowing seam in the middle third of the frame, nobody in the scene.',
    "A fresh bright seam of weld runs down the grey titanium wall where the crack was, glowing orange-white and slowly cooling to dull grey, no water spraying now, only a few drops falling into the still dark water. Nothing else moves.",
    "灰色的钛合金墙板上，原来裂缝的地方有一条崭新的焊缝，橙白色的光慢慢暗下去变成哑灰色，不再喷水，只有几滴水珠落进黑色的静水里。别的什么都不动。",
    Q('The soft tick of cooling metal, a few slow drips into water and a deep hush.', '金属冷却时细细的嘀嗒声、几声缓慢的滴水和一片深深的寂静。'),
    'The frame holds the weld seam on the wall, and nobody in the scene.',
    pull('the glowing weld seam', '发光的焊缝', 'the whole quiet bay and the calm water', '整个安静下来的舱和平静的水面'),
    AE("The orange-white glow of the weld lays a warm shimmer on the still black water and a thin curl of steam rises from the cooling metal into the cold white lamp light.",
       "焊缝橙白色的光在黑色的静水上铺开一层暖暖的微光，一缕细细的蒸汽从冷却的金属上升进冷白色的灯光里。"))

DL('62-04', '04｜控制室：苏清月戴着耳机坐在控制台前，对着麦克风说水位在降你焊上了，耳机里林峰说听着你的声音手就稳，她说回来我给你热毛巾，他说马上', CONTROL_C,
   [P('su_cozy', 'center', "sitting forward on the black swivel chair at the control console in profile facing frame-right, one hand pressing the earpiece of the headset to her ear and the other flat on the console, her head turned toward the monitor wall", 'obj:the wall of small monitors', "her lips parted in relief, her eyes bright and wet, her brows lifted", outfit=SU_HEAD)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "水位在降，你焊上了！", 'lin_flood', 'bright relieved', '明亮如释重负'),
    ('lin_flood', "听着你的声音，手就稳。", 'su_cozy', 'low warm', '低沉温暖'),
    ('su_cozy', "回来，我给你热毛巾。", 'lin_flood', 'soft firm', '轻柔坚定'),
    ('lin_flood', "马上。", 'su_cozy', 'low gentle', '低沉温柔')],
   V('The faint crackle of radio static in an earpiece, the hum of the console and a shaky laugh.', '耳机里电流细细的沙沙声、控制台的嗡鸣和一声发颤的笑。'),
   AE("Cool green status-light glow rims her wet lashes and the black headset, a warm amber lamp lays a gold edge along her shoulder and the screens flicker on the wall behind her.",
      "冷冷的绿色指示灯光勾出她湿润的睫毛和黑色耳机，一盏温暖的琥珀色灯在她的肩头镀了一道金边，身后墙上的屏幕闪动。"),
   post_en='after the last line she lets her forehead drop onto her hand on the console and breathes out',
   post_zh='最后一句之后，她让额头落在放在控制台上的手背上，长长地呼出一口气',
   cam=push1('her face and the headset', '她的脸和耳机'), bg='Behind her the wall of small monitors glows.',
   vd={'lin_flood': B7.VD['lin_flood']}, ld={'lin_flood': ('into the slim boom microphone of her headset', '对着耳机上细细的麦克风')}, room={'Su'})

DL('62-05', '05｜泄洪舱：水退到脚踝深，林峰湿淋淋地坐在梯子最下一级，苏清月把毛巾裹在他头上使劲擦，他说听外面的水在撞墙，她说里面滴水不漏，他说这就是家的意思，她说别说教先擦干', FLOOD_DONE,
   [P('su_cozy', 'left', "standing in the ankle-deep water in profile facing frame-right, a white towel held in both hands over his wet hair, rubbing it hard, her head bent toward him", 'Lin', "her lips pressed into a fierce soft line, her eyes bright with relief, her brows low", outfit=SU_WORK),
    P('lin_flood', 'right', "sitting on the lowest rung of the steel ladder in profile facing frame-left, his dive mask pulled down around his neck and his wet head bent under her towel, his head turned toward her", 'Su', "his lips easing into a tired half sweet smile, his eyes warm and dark, his brows soft")],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the foot of the ladder.',
   [('lin_flood', "听，外面的水在撞墙。", 'su_cozy', 'low calm', '低沉平静'),
    ('su_cozy', "里面，滴水不漏。", 'lin_flood', 'firm quiet', '坚定安静'),
    ('lin_flood', "这就是家的意思。", 'su_cozy', 'low gentle', '低沉温柔'),
    ('su_cozy', "别说教，先擦干。", 'lin_flood', 'bright fierce', '明亮带凶')],
   V('A deep muffled roar of water pounding on the far side of the wall, the soft rustle of a towel and a tired breath.', '墙外水猛烈撞击的深沉闷响、毛巾轻轻的摩擦声和一声疲惫的呼吸。'),
   AE("Cold white work-lamp light glints on the wet black wetsuit and the white towel, thin steam lifts from his shoulders and the still water at their ankles carries a soft gold from the weld seam behind.",
      "冷白色的工作灯光在湿漉漉的黑色潜水服和白毛巾上闪着，他的肩上升起薄薄的蒸汽，他们脚踝边的静水映着身后焊缝柔和的金光。"),
   post_en='after the last line she wraps the towel around his neck and tugs it tight under his chin',
   post_zh='最后一句之后，她把毛巾绕在他的脖子上，在他下巴下面拉紧',
   cam=push('both of them', '两人'), bg='Behind them the grey titanium wall with its clean weld seam fills frame-left.')

INS('62-06', '06｜B4闸门室：黑铁手轮特写，车轮那么大的手轮卡在厚重的圆形钢闸门前，旁边墙上嵌着一块有手掌凹槽的黄铜板，铜板亮着一点暗淡的光', 6, GATE_CLOSE,
    'Close shot of the wheel and the brass plate, the wheel in the middle third of the frame, nobody in the scene.',
    "A big black iron hand-wheel sits against the dull steel gate door and beside it a brass plate with a hand-shaped recess glints dully in the wall. Nothing else moves.",
    "一个黑铁的大手轮贴在暗沉的圆形钢闸门前，旁边墙上嵌着的黄铜板，手掌形的凹槽泛着暗暗的光。别的什么都不动。",
    Q('A deep low hush with the faint tick of cooling steel.', '深沉的低低寂静和钢铁冷却时细细的嘀嗒声。'),
    'The frame holds the hand-wheel and the brass plate, and nobody in the scene.',
    slide('toward frame-right', '右', 'the brass plate with its hand-shaped recess fills the middle third of the frame', '带手掌凹槽的黄铜板占满画面中间三分之一'),
    AE("A single caged work lamp throws a hard white light that glints on the worn rim of the wheel and gleams softly in the brass hollow while dust hangs still in the beam.",
       "一盏笼式工作灯投下硬朗的白光，在手轮磨旧的边缘上闪着，在黄铜的凹槽里泛出柔和的光，尘埃静静悬在光柱里。"))

DL('62-07', '07｜B4闸门室：苏清月说这就是那道手动闸门，林峰说手轮锁只认他的手掌，她说他最好永远别开，他说我答应你，然后他把右手按在黄铜板上，她把手覆在他的手背上', GATE,
   [P('su_cozy', 'left', "standing in front of the huge round gate in profile facing frame-right, her arms tight around herself, her head turned toward him", 'Lin', "her lips pressed together, her eyes serious and wet, her brows pulled together", outfit=SU_WORK),
    P('lin_home', 'right', "standing at the brass plate in profile facing frame-left, his right hand flat against the brass plate in the wall, his head turned toward her", 'Su', "his jaw set, his eyes dark and gentle, his brows soft", outfit=LIN_WORK)],
   'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the gate chamber.',
   [('su_cozy', "这就是那道手动闸门。", 'lin_home', 'low quiet', '低沉安静'),
    ('lin_home', "手轮锁，只认我的手掌。", 'su_cozy', 'low steady', '低沉平稳'),
    ('su_cozy', "你最好永远别开。", 'lin_home', 'low fierce', '低沉凶狠'),
    ('lin_home', "我答应你。", 'su_cozy', 'low gentle', '低沉温柔')],
   V('A deep low hush, the faint tick of cooling steel and a quiet breath.', '深沉的低低寂静、钢铁冷却时细细的嘀嗒声和一声安静的呼吸。'),
   AE("A single caged work lamp throws a hard white light across the round steel gate and a thin warm glow from the brass plate lays a gold edge along his hand and her cheek.",
      "一盏笼式工作灯把硬朗的白光洒在圆形的钢闸门上，黄铜板一线温暖的光在他的手和她的脸颊上镀了一道金边。"),
   post_en='after the last line <su_cozy> steps in and lays her hand over the back of his on the brass plate',
   post_zh='最后一句之后，苏清月走上前，把手覆在他按在黄铜板上的手背上',
   cam=push('both of them', '两人'), bg='Behind them the massive round steel gate door with its black iron hand-wheel fills the back wall of the chamber.')

INS('62-08', '08｜潜望镜里的远方：漆黑的雪原尽头，一长串细小的白色车灯沿着山脊上的路缓缓爬动，头顶淡淡的极光在抖', 6, CONVOY_FAR,
    'Wide shot of the far horizon, the chain of lights in the middle third of the frame, nobody in the scene.',
    "At the far edge of a dark snowfield a long chain of tiny white headlights crawls slowly along a ridge road, a faint green aurora trembling above them. Nothing else moves.",
    "漆黑的雪原尽头，一长串细小的白色车灯沿着山脊上的路缓缓爬动，头顶淡淡的绿色极光在抖。别的什么都不动。",
    Q('A thin howl of wind over the snow and a faint far-off rumble of engines.', '风掠过雪面细细的呼啸和远处发动机隐隐的轰鸣。'),
    'The frame holds the far ridge with the chain of lights, and nobody in the scene.',
    push1('the crawling chain of lights', '缓缓爬动的那串车灯'),
    AE("The tiny white headlights glitter like a string of stars on the black ridge, a faint green aurora trembles above and fine blown snow glints in their beams.",
       "细小的白色车灯像一串星星一样在漆黑的山脊上闪着，淡淡的绿色极光在上面颤动，被风吹起的细雪在灯束里闪烁。"))

report()
doc = S.finish()
