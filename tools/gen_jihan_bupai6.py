#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》补拍包 6（2026-10-16 夜，hh 23:11：男主死的那一段非常混乱，不知道在讲啥，怎么就必须淹死、明明有大空隙能走开，镜头非常乱）。
替换范围：剧本第 65 集“火球爆炸（65-05 山前雪地）”之后的全部（65-06 起）、第 66 集全部、第 67 集全部。第 65 集 01–05 号、第 64 集、第 68 集不动。
  （第 68 集“水退了、耳麦挂在手轮上、日志放在铁台上”的画面，本包的最后两个任务已经铺好。）

原稿为什么看不懂（我的问题，已记自查清单 74）：
  ① 因果没交代：他为什么出不去（塌方只在台词里说“出口被碎石堵死”，开场图没有强调“完全封死、没有缝”）、
     为什么不能等救援（“我来救你”之后苏清月再没试过，观众不知道救不了）、为什么偏偏要他关（“只认我的手掌”只在第 62 集铺垫过一句）、
     为什么会死（第 67 集“闸门关上、水声停了、水位却还在涨”，自相矛盾）。
  ② 镜头碎：控制室和闸门室每说一两句就来回切，再夹“耳机特写”“墙上扬声器特写”这种只有声音的插镜，同一场戏拆成 40 个小任务，谁在对谁说都看不清。
本包的因果链（每一环都有画面＋一句人话）：
  塌方后门口被碎石完全封死、一点缝都没有（画面反复给）→ 林峰推不动（A-02）→ 苏清月要炸，林峰说炸会震裂闸门、挖通要三天（A-06）
  → 苏清月作为医生自己说出“冰水里撑不过一小时”（A-07）＝救不了 → 洪水改道正冲向生活区、九分钟（A-08 画面＋A-09 台词）
  → 闸门只认他的手掌，手轮在他这一侧（B-01）→ 他留下关闸，关完闸门，他被封在冰水里（C-01）→ 告别、番茄、日志（C-04、C-05）→ 他摘下耳麦挂在手轮上（C-06）→ 水面静止（C-08）。
  苏清月不再喊“不准关”（逻辑上他不关也一样会死、还会连累她），改成“再给我五分钟”：她想救、他告诉她没有时间。
镜头的改法：一个任务只有一个说话人（电话两端各自出镜，说话的人嘴动，听的人在另一个任务里）；删掉所有“只有声音”的插镜（伊甸的播报改成林峰口述洪水时间）；
  闸门室连着拍、控制室只在苏清月说话时切过去；最后一镜用挂在手轮上的耳麦和静止的水面，不再拍气泡（气泡会让人以为是溺水）。
偏离原大纲：不拍尸体和血；他是被封在冰水里留下，不是“淹死”的过程；日志只念不拍字；耳麦挂在手轮上（接第 68 集）。
H3 方面的风险（交稿时单列、不算我的错）：
  · A-01／A-02／A-06 开场图里“门口被碎石完全封死、没有缝”约一成可能不按文字画，会重新画出一个可以走过去的缺口——这是这一段最怕的一件事，请重点看这三个；
  · 水位（脚踝→腰→胸口）约一成画不对；B-05 转手轮（慢而持续的动作）；C-04 吃番茄；C-05 画外独白时嘴可能还是会动；
  · 苏清月和林峰各自对着耳麦说话（对象在画面外，可能多画出一个人，所以每个任务只有一个人）；A-08 洪水走廊；C-06 摘耳麦挂手轮（手部动作）。
放进成片的位置：第 65 集 05（火球）→ A-01…A-10 → B-01…B-05 → C-01…C-08 → 第 68 集。
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
OUT = '补拍/追加版_接在主剧后面_带全剧素材/补拍6_男主之死重写_制作稿_追加'
S = Session('合并稿/026_第55-74集_合并_冰川墓碑到陌生人的声音_制作稿_追加.json', OUT, 99000)
B6.S = S
B7.S = S

# ---------------------------------------------------------------------------------------------- 衣着／对象
LIN_HEAD = "in a charcoal henley with the sleeves pushed up to his forearms and dark cargo trousers, a small headset earpiece in his right ear and a slim microphone clipped at his jaw"
LIN_WET = "in a charcoal henley soaked dark with water and clinging to his shoulders, a small headset earpiece in his right ear and a slim microphone clipped at his jaw, his black hair dripping"
LIN_WET_NOHEAD = "in a charcoal henley soaked dark with water and clinging to his shoulders, his black hair dripping, no headset on him"
SU_HEADSET = "in a cream knit sweater with the sleeves pushed up, black thermal leggings and soft boots, a black over-ear headset with a slim boom microphone on her head, her long black hair tied back"
SU_LD = {'lin_work': ('into the slim boom microphone of her headset', '对着耳机上细细的麦克风')}
LIN_LD = {'su_cozy': ('into the slim microphone clipped at his jaw', '对着别在下巴边的细细麦克风')}
AE = lambda en, zh: (en, zh)
AE_GATE = AE("A red emergency lamp lights the chamber evenly and the black water shows a dull red.", "一盏红色应急灯均匀地照着房间，黑水显出暗红色。")
AE_CTRL = AE("Cool green status lights and a warm amber lamp light her face evenly.", "冷绿色的指示灯和一盏温暖的琥珀色灯均匀地照着她的脸。")

# ---------------------------------------------------------------------------------------------- 场景（门口一律写成“完全封死、没有缝”）
SEAL = "at frame-left the only doorway is completely filled from floor to ceiling by a solid mass of broken concrete slabs and bent steel bars, with no gap and no light showing through, and thin trickles of water run out of its seams"
GATE_A = Scene('gate_room', " A single caged work lamp and a red emergency lamp light a cold concrete chamber, the air thick with settling grit.",
               " Fixed stage layout: a small concrete chamber with ankle-deep black water on the floor; the massive round steel gate door two metres tall with a big black iron hand-wheel the size of a car tyre, left stopped half-turned, fills the back wall; a rectangular brass plate with a hand-shaped recess is set into the wall at frame-right beside the gate; " + SEAL + "; a cracked ceiling above.")
GATE_PUSH = Scene('gate_room', GATE_A.end,
                  " Fixed stage layout: a close view of the sealed doorway: a solid wall of broken concrete slabs and bent steel bars with no gap anywhere fills the whole back of the frame, thin trickles of water running out of its seams down into ankle-deep black water at the bottom of the frame.")
GATE_B = Scene('gate_room', " A single caged work lamp and a red emergency lamp light a cold concrete chamber, the black water now knee-deep.",
               " Fixed stage layout: a small concrete chamber with knee-deep black water; the massive round steel gate door with a big black iron hand-wheel stopped half-turned fills the back wall; a rectangular brass plate with a hand-shaped recess is set into the wall at frame-right beside the gate; " + SEAL + ".")
GATE_WAIST = Scene('gate_room', GATE_B.end,
                   " Fixed stage layout: a small concrete chamber with waist-deep black water; the massive round steel gate door with a big black iron hand-wheel fills the back wall; a rectangular brass plate with a hand-shaped recess is set into the wall at frame-right beside the gate; " + SEAL + ".")
GATE_HANDS = Scene('gate_room', GATE_B.end,
                   " Fixed stage layout: a close view of two hands gripping the outer ring of the big black iron hand-wheel in the middle of the frame, the left hand's fingers only half curled around the rim, black water rising around the base of the wheel; the dull steel gate behind; nobody else in the scene.")
GATE_CHEST = Scene('gate_room', " A red emergency lamp lights a flooded concrete chamber, the black water now still.",
                   " Fixed stage layout: a small concrete chamber flooded with chest-deep still black water; the massive round steel gate door, now fully sealed with its big black iron hand-wheel at rest at its centre, fills the back wall; a rusty iron ledge above the waterline runs along the wall beside the wheel at frame-right; " + SEAL + ".")
GATE_LEDGE = Scene('gate_room', GATE_CHEST.end,
                   " Fixed stage layout: a close view of a rusty iron ledge in the middle of the frame, a clear zip-seal plastic bag holding a worn black notebook resting on it just above the black water, the base of the black iron wheel beside it; nobody in the scene.")
GATE_HEADSET = Scene('gate_room', " A last dim red lamp is on over a chamber of still black water.",
                     " Fixed stage layout: a close view of the outer ring of the big black iron hand-wheel at frame-right with a small black headset hanging by its cord from it, a calm black water surface filling the bottom half of the frame; the sealed round steel gate behind; nobody in the scene.")
FLOOD_CORR = Scene('flood_corridor', " A red emergency lamp lights a long concrete corridor filled with the roar of water.",
                   " Fixed stage layout: a long grey concrete corridor recedes down the middle of the frame; dark churning water pours down it from the far end toward the camera, knee-deep and rising; red emergency lamps run along the ceiling; a heavy round steel hatch door stands closed at the near end at frame-right; nobody in the scene.")

# ================================================================================================ 补拍6A 塌方（一个人被封在里面，救不了）
mode('A')
_H.CFG['sfx_loud'] = True
bA = S.episode('补拍6A｜塌方：出口被碎石完全封死，炸不得、挖不通，洪水九分钟后冲到生活区（接在剧本第 65 集火球爆炸之后，替换第 65 集 06 号起）',
               '火球爆炸后闸门室塌方，门口被碎石完全封死没有缝；林峰推不动，苏清月要炸，他说炸会震裂闸门、挖通要三天；她说冰水里撑不过一小时；洪水改道九分钟后冲到生活区；他说你没有五分钟。', 1)

TAA('A-01', '01｜闸门室：爆炸后墙上落着碎石渣，林峰放开转了一半的手轮，慢慢走过脚踝深的黑水，停在被碎石完全封死的门口前', 7, GATE_A,
    [P('lin_work', 'right', "standing in the ankle-deep black water in profile facing frame-left, his right hand just lowered from the half-turned wheel, his head turned toward the doorway", 'obj:the solid wall of broken concrete filling the doorway', "his jaw tight, his eyes wide, his brows pulled together", outfit=LIN_HEAD)],
    'Wide shot of the whole chamber, the man small at frame-right and the sealed doorway at frame-left, in the middle third of the frame.',
    "<lin_work> lowers his hand from the half-turned wheel and walks slowly through the ankle-deep black water toward the doorway, which is completely filled from floor to ceiling with broken concrete and bent steel bars with no gap, and stops in front of it while grit still trickles down from the cracked ceiling.",
    "林峰放开转了一半的手轮，慢慢走过脚踝深的黑水，走向那个从地面到天花板被碎混凝土和扭曲钢筋完全堵死的门口、一点缝都没有，他停在它面前，裂开的天花板上还有碎渣在往下掉。",
    Q('The slow slosh of water around boots, the soft patter of falling grit and a deep low rumble fading in the walls.', '水在靴子边缓缓晃动的声音、碎渣掉落的轻轻噼啪声和墙里渐渐远去的低沉隆隆声。'),
    AE_GATE,
    holds='The frame holds the half-turned wheel, the brass plate, the solid sealed doorway with no gap, and one person: Lin.',
    cam=follow('Lin', '林峰', 'he stops in front of the sealed doorway', '他停在被封死的门口前'))

TAA('A-02', '02｜闸门室：林峰用两只手掌和肩膀拼命顶那堵碎石墙，碎石一点不动，没有任何缝，他喘着气把额头抵在冰冷的混凝土上', 6, GATE_PUSH,
    [P('lin_work', 'center', "standing in front of the wall of rubble in profile facing frame-left, both palms flat against the broken slabs and his shoulder driving into them, his headset earpiece in his right ear", 'obj:the solid wall of rubble', "his teeth clenched, his eyes narrowed, his brows low", outfit=LIN_HEAD)],
    'Medium shot, the man from the head to the waist, in the middle third of the frame, in front of the rubble wall.',
    "<lin_work> shoves both palms and his shoulder against the solid wall of broken slabs with all his strength, but nothing moves and no gap opens; then he stops, breathing hard, and rests his forehead against the cold concrete.",
    "林峰用两只手掌和肩膀拼命顶那堵实心的碎石墙，可是一点不动，也没有任何缝；然后他停下来，喘着气，把额头抵在冰冷的混凝土上。",
    Q('The grunt of effort, the scrape of palms on rough concrete, the slosh of water and a deep hush behind the rubble.', '用力的闷哼声、手掌擦过粗糙混凝土的声音、水的晃动声和碎石后面深深的寂静。'),
    AE_GATE,
    holds='The frame holds the solid wall of rubble with no gap, and one person: Lin.',
    cam=push1('his hands and the rubble', '他的手和碎石墙'), bg='Behind him nothing but the solid wall of broken concrete with no gap anywhere.')

DL('A-03', '03｜控制室：苏清月站起来按住耳机，对着麦克风喊林峰听得见吗，回答我', CONTROL_C,
   [P('su_cozy', 'center', "standing up fast from the black swivel chair at the control console in profile facing frame-right, one hand pressing the headset earpiece to her ear and the other flat on the console, her head turned toward the monitor wall", 'obj:the wall of small monitors', "her lips parting, her eyes wide and wet, her brows pulled together", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "林峰，听得见吗？", 'lin_work', 'sharp breathless', '锐利喘着气'),
    ('su_cozy', "回答我！", 'lin_work', 'sharp', '锐利')],
   V('The faint crackle of radio static in an earpiece, the hum of the console and a quick breath.', '耳机里电流细细的沙沙声、控制台的嗡鸣和一声急促的呼吸。'),
   AE_CTRL,
   post_en='after the last line she stays rigid, listening with her eyes fixed on the monitor wall',
   post_zh='最后一句之后，她僵着身子，眼睛盯着监控墙，听着',
   cam=push1('her face and the headset', '她的脸和耳机'), bg='Behind her the wall of small monitors glows.', room={'Su'}, ld=SU_LD)

DL('A-04', '04｜闸门室：林峰按着耳机，对苏清月说通道塌了我出不去，闸门只关了一半', GATE_A,
   [P('lin_work', 'center', "standing in the ankle-deep black water in profile facing frame-left, one hand pressed to the earpiece of his headset, his back to the half-turned wheel, his head turned toward the sealed wall of rubble", 'obj:the solid wall of rubble', "his jaw tight, his eyes steady and wet, his brows drawn together", outfit=LIN_HEAD)],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the gate chamber.',
   [('lin_work', "通道塌了，我出不去。", 'su_cozy', 'low rough', '低沉沙哑'),
    ('lin_work', "闸门只关了一半。", 'su_cozy', 'low grim', '低沉凝重')],
   V('The slow slosh of water, the crackle of radio static in an earpiece and a low breath.', '水缓缓晃动的声音、耳机里电流的沙沙声和一声低低的呼吸。'),
   AE_GATE,
   post_en='after the last line he turns his head and looks at the half-turned wheel behind him',
   post_zh='最后一句之后，他转头看了一眼身后转了一半的手轮',
   cam=push1('his face and the earpiece', '他的脸和耳机'), bg='Behind him the sealed wall of rubble fills the frame-left and the massive round steel gate with its half-turned wheel fills the back wall.',
   room={'Lin'}, ld=LIN_LD)

DL('A-05', '05｜控制室：苏清月一巴掌拍在控制台上，说我来炸开它', CONTROL_C,
   [P('su_cozy', 'center', "standing at the control console in profile facing frame-right, one hand pressing the headset to her ear and the other fist pressed flat on the console, her head turned toward the monitor wall", 'obj:the wall of small monitors', "her teeth bared, her eyes fierce and wet, her brows low", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "我来炸开它！", 'lin_work', 'sharp fierce', '锐利凶狠')],
   V('The crackle of radio static in an earpiece, the thump of a fist on a console and a ragged breath.', '耳机里电流的沙沙声、拳头砸在控制台上的闷响和一声粗重的喘息。'),
   AE_CTRL,
   post_en='after the last line she grips the console tightly until her knuckles whiten',
   post_zh='最后一句之后，她攥紧控制台的边缘，指节发白',
   cam=push1('her fist and her face', '她的拳头和脸'), bg='Behind her the wall of small monitors glows.', room={'Su'}, ld=SU_LD)

DL('A-06', '06｜闸门室：林峰说别炸闸门一震就裂，说挖通要三天他等不到', GATE_A,
   [P('lin_work', 'center', "standing in the ankle-deep black water in profile facing frame-left, one hand pressed to the earpiece of his headset, his other hand raised palm-out in a calming gesture, his head turned toward the sealed wall of rubble", 'obj:the solid wall of rubble', "his jaw tight, his eyes steady and wet, his brows drawn together", outfit=LIN_HEAD)],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the gate chamber.',
   [('lin_work', "别炸，闸门一震就会裂。", 'su_cozy', 'low steady', '低沉平稳'),
    ('lin_work', "挖通要三天，我等不到。", 'su_cozy', 'low gentle', '低沉温柔')],
   V('The slow slosh of water, the crackle of radio static in an earpiece and a low breath.', '水缓缓晃动的声音、耳机里电流的沙沙声和一声低低的呼吸。'),
   AE_GATE,
   post_en='after the last line he lowers his raised hand and looks down at the black water around his boots',
   post_zh='最后一句之后，他放下举着的手，低头看着靴子周围的黑水',
   cam=push1('his face and the earpiece', '他的脸和耳机'), bg='Behind him the sealed wall of rubble fills the frame-left and the massive round steel gate fills the back wall.',
   room={'Lin'}, ld=LIN_LD)

DL('A-07', '07｜控制室：苏清月慢慢松开拳头，低声说我知道，冰水里撑不过一小时', CONTROL_C,
   [P('su_cozy', 'center', "standing at the control console in profile facing frame-right, both hands pressing the headset to her ears, her head slowly bowing", 'obj:the console', "her lips trembling, her eyes streaming, her brows pulled up", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "我知道。", 'lin_work', 'low breaking', '低沉发颤'),
    ('su_cozy', "冰水里，撑不过一小时。", 'lin_work', 'low shaking', '低沉发抖')],
   V('A thin electronic hiss in an earpiece, the hum of the console and a shaky breath.', '耳机里细细的电子嘶声、控制台的嗡鸣和一声发颤的呼吸。'),
   AE_CTRL,
   post_en='after the last line she closes her eyes and a tear runs down her cheek',
   post_zh='最后一句之后，她闭上眼睛，一滴眼泪顺着脸颊流下来',
   cam=push1('her face and the headset', '她的脸和耳机'), bg='Behind her the wall of small monitors glows.', room={'Su'}, ld=SU_LD, tail=2.5)

INS('A-08', '08｜生活区走廊：黑色的洪水从长走廊远端翻涌过来，水位越涨越高，近端那扇圆形钢舱门紧紧关着', 7, FLOOD_CORR,
    'Wide shot of the corridor, the churning water in the middle third of the frame, nobody in the scene.',
    "Dark churning water pours down the long grey concrete corridor from the far end toward the camera, the level rising steadily, red emergency lamps running along the ceiling and a heavy round steel hatch door standing closed at the near end. Nothing else moves.",
    "黑色的洪水从长长的灰色混凝土走廊远端翻涌着朝镜头涌来，水位一点点上涨，天花板上一排红色应急灯亮着，近端一扇厚重的圆形钢舱门紧紧关着。别的什么都不动。",
    Q('The thundering roar of rushing water, the metallic ring of a sealed hatch and a steady alarm tone.', '洪水奔涌的雷鸣般的轰响、封死的舱门金属的回响和一声持续的警报。'),
    'The frame holds the flooded corridor and the hatch door, and nobody in the scene.',
    follow('the front of the flood', '洪水的前锋', 'the dark water reaches the hatch door at the near end', '黑色的水涌到近端的舱门'),
    AE("Red emergency lamps light the corridor evenly and the black water shows a dull red.", "红色应急灯均匀地照着走廊，黑水显出暗红色。"))

DL('A-09', '09｜闸门室：林峰说洪水改道了，九分钟后就冲到你那里，我算过了', GATE_B,
   [P('lin_work', 'center', "standing in the knee-deep black water in profile facing frame-left, one hand pressed to the earpiece of his headset and the other resting on the rim of the half-turned wheel, his head turned toward the sealed wall of rubble", 'obj:the solid wall of rubble', "his jaw set, his eyes steady and wet, his brows level", outfit=LIN_HEAD)],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the gate chamber.',
   [('lin_work', "洪水改道了，九分钟后就到你那里。", 'su_cozy', 'low steady', '低沉平稳'),
    ('lin_work', "我算过了。", 'su_cozy', 'low gentle', '低沉温柔')],
   V('The slow slosh of rising water, the crackle of radio static in an earpiece and a low breath.', '上涨的水缓缓晃动的声音、耳机里电流的沙沙声和一声低低的呼吸。'),
   AE_GATE,
   post_en='after the last line he looks down at his left hand on the wheel and bends its fingers slowly',
   post_zh='最后一句之后，他低头看着放在手轮上的左手，慢慢蜷起手指',
   cam=push1('his face and the earpiece', '他的脸和耳机'), bg='Behind him the sealed wall of rubble fills the frame-left and the massive round steel gate fills the back wall.',
   room={'Lin'}, ld=LIN_LD)

DL('A-10', '10｜控制室：苏清月对着麦克风说不准关，再给我五分钟', CONTROL_C,
   [P('su_cozy', 'center', "leaning over the control console in profile facing frame-right, both hands gripping the console and the headset on her head, her head lifted toward the monitor wall", 'obj:the wall of small monitors', "her lips pulled tight, her eyes wide and streaming, her brows pulled together", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "不准关！", 'lin_work', 'sharp breaking', '锐利发颤'),
    ('su_cozy', "再给我五分钟！", 'lin_work', 'sharp pleading', '锐利恳求')],
   V('The crackle of radio static in an earpiece, the hum of the console and a ragged breath.', '耳机里电流的沙沙声、控制台的嗡鸣和一声粗重的喘息。'),
   AE_CTRL,
   post_en='after the last line she holds her breath, her eyes fixed on the monitor wall',
   post_zh='最后一句之后，她屏住呼吸，眼睛盯着监控墙',
   cam=push1('her face and the headset', '她的脸和耳机'), bg='Behind her the wall of small monitors glows.', room={'Su'}, ld=SU_LD)

# ================================================================================================ 补拍6B 手轮
bB = S.episode('补拍6B｜手轮：闸门只认他的手掌，他对她说你没有五分钟，告别，转手轮（替换剧本第 66 集）',
               '林峰说你没有五分钟，外科医生只做最后一刀，把右手按进铜板；两只手握住手轮，左手手指合不拢；他对她说遇见你是我最好的决定；苏清月说我来接你；他用全身的力气转动手轮，水涨到腰。', 2)

DL('B-01', '01｜闸门室：林峰说你没有五分钟，外科医生只做最后一刀，然后把右手按进黄铜板的手掌凹槽', GATE_B,
   [P('lin_work', 'right', "standing in the knee-deep black water in profile facing frame-left, one hand pressed to the earpiece of his headset, his head turned toward the black iron hand-wheel at the gate", 'obj:the black iron hand-wheel', "his jaw set, his eyes steady and wet, his brows soft", outfit=LIN_HEAD)],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the gate chamber.',
   [('lin_work', "你没有五分钟。", 'su_cozy', 'low steady', '低沉平稳'),
    ('lin_work', "外科医生，只做最后一刀。", 'su_cozy', 'low gentle', '低沉温柔')],
   V('The slow slosh of rising water, the crackle of radio static in an earpiece and the soft click of a brass plate.', '上涨的水缓缓晃动的声音、耳机里电流的沙沙声和铜板轻轻的一声咔哒。'),
   AE_GATE,
   post_en='after the last line he lowers his hand from the earpiece and presses his right palm flat into the hand-shaped recess of the brass plate on the wall',
   post_zh='最后一句之后，他把手从耳机上放下来，把右手掌平平按进墙上黄铜板的手掌凹槽里',
   cam=push1('his hand and the brass plate', '他的手和黄铜板'), bg='Behind him the massive round steel gate with its black iron hand-wheel fills the back wall and the brass plate is on the wall at frame-right.',
   room={'Lin'}, ld=LIN_LD, tail=2.5)

INS('B-02', '02｜闸门室：两只手握着黑铁手轮的边缘，右手握得很紧，左手的五根手指只能蜷到一半，黑水慢慢漫上手轮的底座', 6, GATE_HANDS,
    'Close shot of the two hands on the wheel in the middle third of the frame, nobody else in the scene.',
    "Two hands grip the outer ring of the big black iron hand-wheel, the right hand gripping tight and the left hand's five fingers only half bent and trembling, black water slowly rising around the base of the wheel. Nothing else moves.",
    "两只手握着黑铁大手轮的边缘，右手握得很紧，左手的五根手指只能蜷到一半，在微微发抖，黑色的水慢慢漫上手轮的底座。别的什么都不动。",
    Q('The slow slosh of rising water against iron and a deep hush.', '上涨的水拍着铁手轮的缓慢声音和深深的寂静。'),
    'The frame holds the two hands and the wheel, and nobody else in the scene.',
    push1('the half-bent left hand', '蜷到一半的左手'),
    AE("A red emergency lamp lights the wet iron and the pale knuckles evenly.", "红色应急灯均匀地照着湿漉漉的铁和苍白的指关节。"))

DL('B-03', '03｜闸门室：林峰握着手轮，流着泪对苏清月说遇见你是我最好的决定，好好吃饭别熬夜', GATE_WAIST,
   [P('lin_work', 'right', "standing in the waist-deep black water in profile facing frame-left, both hands gripping the outer ring of the black iron hand-wheel, his headset earpiece in his right ear, his head turned toward the wheel", 'obj:the black iron hand-wheel', "his lips curving in a faint tender sweet smile, his eyes wet with tears running down his cheeks, his brows soft", outfit=LIN_WET)],
   'Medium close shot, the man from the head to the chest, in the middle third of the frame, in the flooded gate chamber.',
   [('lin_work', "遇见你，是我最好的决定。", 'su_cozy', 'low warm', '低沉温暖'),
    ('lin_work', "好好吃饭，别熬夜。", 'su_cozy', 'low gentle', '低沉温柔')],
   V('The slow slosh of waist-deep water, the crackle of radio static in an earpiece and a soft shaky breath.', '齐腰深的水缓缓晃动的声音、耳机里电流的沙沙声和一声轻轻发抖的呼吸。'),
   AE_GATE,
   post_en='after the last line he lifts his eyes to the heavy steel gate and sets his jaw',
   post_zh='最后一句之后，他抬起眼睛望向那扇厚重的钢闸门，咬紧牙关',
   cam=push1('his face and the wheel', '他的脸和手轮'), bg='Behind him the massive round steel gate fills the back wall.',
   room={'Lin'}, ld=LIN_LD, tail=2.5)

DL('B-04', '04｜控制室：苏清月哭着对麦克风喊闭嘴我来接你，你说好会回来的', CONTROL_C,
   [P('su_cozy', 'center', "standing at the control console in profile facing frame-right, both hands pressing the headset to her ears, her head bowed over the console", 'obj:the console', "her lips trembling, her eyes streaming, her brows pulled up", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "闭嘴，我来接你！", 'lin_work', 'sharp breaking', '锐利发颤'),
    ('su_cozy', "你说好会回来的！", 'lin_work', 'sharp sobbing', '锐利带着哭腔')],
   V('The crackle of radio static in an earpiece, the hum of the console and a sobbing breath.', '耳机里电流的沙沙声、控制台的嗡鸣和一声带着哭腔的呼吸。'),
   AE_CTRL,
   post_en='after the last line she slumps over the console with her forehead against it',
   post_zh='最后一句之后，她整个人伏在控制台上，额头抵着台面',
   cam=push1('her face and the headset', '她的脸和耳机'), bg='Behind her the wall of small monitors glows.', room={'Su'}, ld=SU_LD)

TAA('B-05', '05｜闸门室：林峰用全身的力气一圈一圈转动沉重的手轮，水涨到他的腰，最后手轮停住不动', 8, GATE_WAIST,
    [P('lin_work', 'right', "standing in the waist-deep black water in profile facing frame-left, both hands gripping the outer ring of the heavy black iron hand-wheel and turning it with his whole body, his headset earpiece in his right ear", 'obj:the black iron hand-wheel', "his teeth clenched, his eyes narrowed and wet, his brows low", outfit=LIN_WET)],
    'Medium shot, the man from the head to the waist, in the middle third of the frame, in the flooded gate chamber.',
    "<lin_work> turns the heavy black iron hand-wheel with his whole body, one slow full turn after another, the muscles of his arms and shoulders tensing; at the end the wheel stops against its stop and does not move any more, and he holds on to it with both hands, breathing hard.",
    "林峰用全身的力气转动沉重的黑铁手轮，一圈接着一圈，手臂和肩膀的肌肉绷紧；最后手轮转到头停住，再也转不动，他用两只手扶着它，大口喘气。",
    Q('The heavy grinding groan of the iron wheel turning, a deep low rumble of water behind the gate and a ragged laboured breathing that ends in a dull heavy thud.', '铁手轮沉重的吱呀碾磨声、闸门后水深沉的低低轰响和吃力粗重的喘息，最后是一声闷重的撞击。'),
    AE_GATE,
    holds='The frame holds the wheel and the gate, and one person: Lin.',
    cam=push1('his hands on the wheel', '他握着手轮的手'), bg='Behind him the massive round steel gate fills the back wall.')

# ================================================================================================ 补拍6C 最后一道闸门
bC = S.episode('补拍6C｜最后一道闸门：闸门关死，水声停了，他吃番茄、写日志、摘下耳麦挂在手轮上（替换剧本第 67 集）',
               '闸门关死，林峰靠着它，水到胸口；苏清月听见水声停了，他说关好了我在这儿；他掏出口袋里的番茄吃了，说很甜你的书没白读；他在日志最后一页写字，画外独白；他摘下耳麦挂在手轮上；苏清月叫他，没人回答；水面静止，耳麦挂在手轮上。', 3)

TAA('C-01', '01｜闸门室：林峰的手从手轮上滑落，整个人靠在彻底关死的圆形钢闸门上，水漫到胸口，他头向后仰，闭上眼睛长长地吐出一口气', 8, GATE_CHEST,
    [P('lin_work', 'right', "leaning back against the sealed round steel gate chest-deep in still black water in profile facing frame-left, his hands dropping from the outer ring of the black iron hand-wheel and dropping into the water, his head tipped back against the gate", 'closed', "his jaw loosening, his lips parting in a long slow breath, his brows easing", outfit=LIN_WET, shut='gently closed')],
    'Medium shot, the man from the head to the chest, in the middle third of the frame, in the flooded gate chamber.',
    "<lin_work> lets his hands fall from the outer ring of the black iron hand-wheel and leans back against the sealed round gate with the still black water at his chest, his head tipping back and his eyes closing as he lets out one long slow breath that shows white in the cold air.",
    "林峰的手从黑铁手轮的边上滑下来，靠在彻底关死的圆形闸门上，平静的黑水漫到胸口，头向后仰，眼睛闭上，长长地缓缓吐出一口气，在冰冷的空气里呼出一团白气。",
    Q('The slow slosh of black water settling, a deep hush behind the sealed gate and one long exhale.', '黑水缓缓平息的声音、关死的闸门后深深的寂静和一声长长的呼气。'),
    AE_GATE,
    holds='The frame holds the sealed gate, and one person: Lin.',
    cam=push1('his closed eyes and the long breath', '他闭着的眼睛和长长的呼气'))

DL('C-02', '02｜控制室：苏清月听着耳机里一片寂静，低声说水声停了，林峰你说话', CONTROL_C,
   [P('su_cozy', 'center', "sitting forward on the black swivel chair at the control console in profile facing frame-right, one hand pressing the headset earpiece to her ear and the other flat on the console, her head turned toward the monitor wall", 'obj:the wall of small monitors', "her lips parting, her eyes wide and wet, her brows pulled together", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "水声停了。", 'lin_work', 'low trembling', '低沉发颤'),
    ('su_cozy', "林峰，你说话。", 'lin_work', 'low breaking', '低沉发颤')],
   V('A deep hush in the control room, the faint crackle of radio static in an earpiece and a shaky breath.', '控制室深深的寂静、耳机里电流细细的沙沙声和一声发颤的呼吸。'),
   AE_CTRL,
   post_en='after the last line she closes her eyes and presses the earpiece harder against her ear',
   post_zh='最后一句之后，她闭上眼睛，把耳机更用力地按在耳朵上',
   cam=push1('her face and the headset', '她的脸和耳机'), bg='Behind her the wall of small monitors glows.', room={'Su'}, ld=SU_LD)

DL('C-03', '03｜闸门室：林峰靠着关死的闸门，闭着眼睛轻声说关好了，我在这儿', GATE_CHEST,
   [P('lin_work', 'right', "leaning back against the sealed gate chest-deep in still black water in profile facing frame-left, his head resting against the gate and one hand lifted weakly to the earpiece of his headset", 'closed', "his lips curving in a faint tender sweet smile, his brows soft", outfit=LIN_WET, shut='gently closed')],
   'Medium close shot, the man from the head to the chest, in the middle third of the frame, in the flooded gate chamber.',
   [('lin_work', "关好了。", 'su_cozy', 'low soft', '低沉轻柔'),
    ('lin_work', "我在这儿。", 'su_cozy', 'low gentle', '低沉温柔')],
   V('The slow slosh of still water, the crackle of radio static in an earpiece and a soft breath.', '平静的水缓缓晃动的声音、耳机里电流的沙沙声和一声轻轻的呼吸。'),
   AE_GATE,
   post_en='after the last line he lowers his hand from the earpiece into the water',
   post_zh='最后一句之后，他把手从耳机上放下，垂进水里',
   cam=push1('his face', '他的脸'), bg='Behind him the massive sealed round steel gate fills the back wall.',
   room={'Lin'}, ld=LIN_LD)

DL('C-04', '04｜闸门室：林峰从湿透的胸口口袋里掏出一颗红色的小番茄，对苏清月说口袋里还有一颗番茄，咬了一口，说很甜，你的书没白读', GATE_CHEST,
   [P('lin_work', 'right', "leaning back against the sealed gate chest-deep in still black water in profile facing frame-left, a small bright red tomato held up in his right hand in front of his face, his headset earpiece in his right ear, his head turned toward the tomato", 'obj:the small red tomato in his hand', "his lips curving in a faint tender sweet smile, his eyes wet and bright, his brows soft", outfit=LIN_WET)],
   'Medium close shot, the man from the head to the chest, in the middle third of the frame, in the flooded gate chamber.',
   [('lin_work', "口袋里，还有一颗番茄。", 'su_cozy', 'low gentle', '低沉温柔'),
    ('lin_work', "很甜。你的书，没白读。", 'su_cozy', 'low warm', '低沉温暖')],
   V('The slow slosh of still water, the crackle of radio static in an earpiece and a soft wet bite.', '平静的水缓缓晃动的声音、耳机里电流的沙沙声和一声轻轻的湿润的咬东西的声音。'),
   AE("A red emergency lamp lights the chamber evenly and the small tomato shows a vivid red in his wet hand.", "红色应急灯均匀地照着房间，他湿漉漉的手里那颗小番茄显出鲜红色。"),
   pre_en='He takes a small red tomato out of the chest pocket of his soaked henley.', pre_zh='他从湿透的亨利衫胸口的口袋里掏出一颗红色的小番茄。',
   post_en='after the last line he takes one slow bite of the tomato',
   post_zh='最后一句之后，他缓缓咬了一口番茄',
   cam=push1('his face and the tomato', '他的脸和那颗番茄'), bg='Behind him the massive sealed round steel gate fills the back wall.',
   room={'Lin'}, ld=LIN_LD, tail=2.5)

MONO('C-05', '05｜闸门室：林峰一只手把日志举在水面上，另一只手握着铅笔，在最后一页上写字，他的嘴唇闭着，画外传来他的内心独白：你读到这页，门已关好，别怪这扇门，也别怪我，往后的春天，都归你', GATE_CHEST,
     [P('lin_work', 'right', "leaning back against the sealed gate chest-deep in still black water in profile facing frame-left, a worn black notebook held open above the water on his left palm and a short pencil in his right hand writing on its last page, his head bowed toward the page", 'obj:the open notebook in his hand', "his jaw relaxed, his lips closed, his eyes calm and wet, his brows soft", outfit=LIN_WET)],
     'Medium close shot, the man from the head to the chest, in the middle third of the frame, in the flooded gate chamber.',
     "<lin_work> holds the worn black notebook open above the still black water on his left palm and writes slowly on its last page with a short pencil, his head bowed over the page, his jaw relaxed, his lips closed and his brows soft, a thin tear running down his cheek.",
     "林峰用左手托着那本磨旧的黑色日志举在平静的黑水上面，右手握着短铅笔在最后一页慢慢写字，头低着，下颌放松，嘴唇闭着，眉头舒展，一道细细的泪痕顺着脸颊流下来。",
     V('The slow slosh of still water, the faint scratch of a pencil on paper and only his calm inner voice-over spoken.', '平静的水缓缓晃动的声音、铅笔在纸上细细的沙沙声，只有他平静的内心独白在说话。'),
     AE_GATE,
     [ "你读到这页，门已关好。", "别怪这扇门，也别怪我。", "往后的春天，都归你。" ],
     holds='The frame holds the sealed gate, and one person: Lin.',
     cam=push1('the pencil and the page', '铅笔和那一页纸'), mind=11, tail=1.5)

TAA('C-06', '06｜闸门室：林峰把日志装进透明塑封袋放到铁台上，然后抬手摘下头上的耳麦，挂在手轮的边上，手慢慢垂进水里', 8, GATE_CHEST,
    [P('lin_work', 'right', "leaning back against the sealed gate chest-deep in still black water in profile facing frame-left, one hand lifting the small headset off his ear and hanging it by its cord on the outer ring of the black iron hand-wheel beside him, his head turned toward the wheel", 'obj:the black iron hand-wheel', "his lips curving in a faint tired sweet smile, his eyes wet and calm, his brows soft", outfit=LIN_WET)],
    'Medium close shot, the man from the head to the chest, in the middle third of the frame, in the flooded gate chamber.',
    "<lin_work> slips the worn notebook into a clear zip-seal bag and sets it on the rusty iron ledge above the water beside the wheel, then lifts the small headset off his ear and hangs it by its cord on the outer ring of the black iron hand-wheel, and lets his hand sink slowly into the water.",
    "林峰把磨旧的日志装进透明塑封袋，放在手轮旁高出水面的一块锈铁台上，然后抬手摘下耳朵上的小耳麦，用线挂在黑铁手轮的边上，手慢慢垂进水里。",
    Q('The slow slosh of still water, the soft rustle of plastic and a faint click of a cord on iron.', '平静的水缓缓晃动的声音、塑料袋轻轻的窸窣声和线挂在铁上细细的一声咔哒。'),
    AE_GATE,
    holds='The frame holds the sealed gate, the wheel and the ledge, and one person: Lin.',
    cam=push1('his hand and the wheel', '他的手和手轮'), bg='Beside him the black iron hand-wheel and a rusty iron ledge above the waterline.')

DL('C-07', '07｜控制室：苏清月对着耳机叫林峰，耳机里一片死寂，她慢慢把耳机从耳朵上拿下来抱在胸口', CONTROL_C,
   [P('su_cozy', 'center', "sitting forward on the black swivel chair at the control console in profile facing frame-right, both hands pressing the headset to her ears, her head bowed toward the console", 'obj:the console', "her lips trembling, her eyes wide and streaming, her brows pulled up", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "林峰。", 'lin_work', 'low breaking', '低沉发颤'),
    ('su_cozy', "你说话啊。", 'lin_work', 'low shaking', '低沉发抖')],
   V('A thin electronic hiss that drops to silence, the hum of the console and a shaky breath.', '一声细细的电子嘶声渐渐掉进寂静里、控制台的嗡鸣和一声发颤的呼吸。'),
   AE_CTRL,
   post_en='after the last line she lowers the headset slowly from her ears and holds it against her chest',
   post_zh='最后一句之后，她把耳机慢慢从耳朵上拿下来，抱在胸口',
   cam=push1('her face and the headset', '她的脸和耳机'), bg='Behind her the wall of small monitors glows.', room={'Su'}, ld=SU_LD, tail=2.5)

INS('C-08', '08｜闸门室：黑色的水面静静地不动，一副小耳麦挂在黑铁手轮的边上轻轻晃着，暗红色的灯光慢慢暗下去', 8, GATE_HEADSET,
    'Close shot of the outer ring of the wheel and the water, the hanging headset in the middle third of the frame, nobody in the scene.',
    "A small black headset hangs by its cord from the outer ring of the big black iron hand-wheel and sways a little, above a calm black water surface; the dim red light slowly fades to darkness. Nothing else moves.",
    "一副黑色的小耳麦用线挂在黑铁大手轮的边上，轻轻晃着，下面是一片平静的黑色水面；暗红色的灯光慢慢暗成一片黑。别的什么都不动。",
    Q('The faint creak of a cord on iron, one soft drip of water and a long deep hush.', '线在铁上细细的一声吱嘎、一声轻轻的滴水声和一片长长的深深的寂静。'),
    'The frame holds the hanging headset, the outer ring of the wheel and the water, and nobody in the scene.',
    descend('the hanging headset and the still water', '挂着的耳麦和静止的水面'),
    AE("The last dim red light fades slowly from the chamber until only black remains.", "最后一点暗红色的灯光慢慢从房间里退去，只剩下一片黑。"))

doc = S.finish()
report()
