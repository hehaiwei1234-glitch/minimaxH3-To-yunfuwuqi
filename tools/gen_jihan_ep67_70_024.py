#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 67–70 集，追加稿 024（2026-10-15 夜，hh 挂机，要 20 集；A 写法为主）。
故事见 `剧本/第55-74集_结局版大纲.md`。以 023（第 63–66 集）的 JSON 为底，必须等 023 在插件里全部跑完再追加；追加窗口不要勾每集／总／任务秒数。
写法分配：这四集是全剧最重的情绪戏，全部用 A（慢、对白任务 11–15 秒、句间 0.9 秒、结尾带动作）。
  第 67 集 最后一道闸门：林峰关上闸门，水到胸口，他吃下口袋里的番茄“很甜，你的书没白读”，在日志最后一页写下画外独白（嘴闭着），水面几个气泡；不拍血、不拍尸体。
  第 68 集 说好会回来：三天后通道抽干，苏清月找到关死的闸门、挂在手轮上的耳麦和塑封的日志，说“你说好会带我回来的”；让伊甸保留他的权限。
  第 69 集 一个人的伊甸：苏清月穿着他的衬衫，一个人煮两杯茶，照他的日志浇水，1 号番茄藤结出最大的一颗，伊甸提醒她体重下降。
  第 70 集 余温：她一个人吃火锅，翻日志旁注（他记着她怕冷、爱吃辣），伊甸放出林峰留下的录音“春天来了，替我去看看”，地表温度升到零度。
偏离原大纲：原大纲写“他的围巾”，这里改成挂在手轮上的耳麦（本剧前面没有围巾）；通道由伊甸的维修机器人清出一个缺口（一句台词交代）；
  林峰的死只拍“水面几个气泡”，不拍身体、不拍血；日志的内容只念，不拍纸上的字（不写画面里读得到的文字）。
H3 方面的风险（交稿时单列，不算我的错）：
  · 67-03 林峰吃番茄（手部＋嘴的动作）；67-04 画外独白时嘴可能还是会动；67-01／67-03 水到胸口的人；67-07 水面气泡；
  · 68-04／68-05／68-06 苏清月在淤泥和铁闸前、手电光；68-05 自言自语；
  · 69-03 自言自语的三句台词；69-07 吃饭时的小口喝汤；70-02／70-04 对着空椅子说话（可能被画成对面坐了个人）；
  · 70-05 墙上扬声器里林峰录音的声音（画外音）。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
import _jihan_base7 as B7
from _jihan_base7 import *
import _jihan_base8 as B8
from _jihan_base8 import *
import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407)
OUT = '合并稿/024_第67-70集_最后一道闸门说好会回来一个人的伊甸余温_制作稿_追加'
S = Session('合并稿/023_第63-66集_钻机请君入瓮军阀的反击手轮_制作稿_追加.json', OUT, 93000)
B6.S = S
B7.S = S

# ---------------------------------------------------------------------------------------------- 衣着／声音
LIN_WET = "in a charcoal henley soaked dark with water and clinging to his shoulders, a small headset earpiece in his right ear and a slim microphone clipped at his jaw, his black hair dripping"
SU_HEADSET = "in a cream knit sweater with the sleeves pushed up, black thermal leggings and soft boots, a black over-ear headset with a slim boom microphone on her head, her long black hair tied back"
SU_HAGGARD = "in a rumpled cream knit sweater with the sleeves pulled down over her hands and black thermal leggings, her long black hair unbrushed and loose, dark shadows under her eyes, a black headset hanging around her neck"
SU_ALONE = "in an oversized charcoal henley that is clearly a man's, the sleeves rolled many times at her wrists, black thermal leggings and thick grey socks, her long black hair tied back loosely"
look('lin_rec', 'LinRec', "a flat wall speaker panel with a thin blue ring", 'none', 'its')
B7.VOICE_ONLY.add('lin_rec')
B7.VD['lin_rec'] = ("the low steady recorded voice of a man, with a faint tape hiss, coming from the flat wall speaker panel with the thin blue ring", '从墙上那块带着一圈细细蓝圈的扁扁扬声器里传出的、带着细细磁带嘶声的一个男人低沉平稳的录音')
B7.ZN['lin_rec'] = '林峰的录音'
LINREC_EN = LIN_EN + ' This is an old recording heard through a small wall speaker with a faint tape hiss, warm and tired.'
LINREC_ZH = LIN_ZH + '这是一段旧录音，通过墙上的小扬声器传出，带着细细的磁带嘶声，温暖而疲惫。'
SU_LD = {'lin_work': ('into the slim boom microphone of her headset', '对着耳机上细细的麦克风')}
LIN_LD = {'su_cozy': ('into the slim microphone clipped at his jaw', '对着别在下巴边的细细麦克风')}

# ---------------------------------------------------------------------------------------------- 场景
GATE_CHEST = Scene('gate_room', " A red emergency strobe pulses slowly over a flooded concrete chamber, the black water rising.",
                   " Fixed stage layout: a small concrete chamber flooded with chest-deep black water; the massive round steel gate door, now fully sealed with its big black iron hand-wheel at rest at its centre, fills the back wall; a rusty iron ledge above the waterline runs along the wall beside the wheel at frame-right; the doorway at frame-left is sealed by a heap of broken concrete.")
GATE_LEDGE = Scene('gate_room', GATE_CHEST.end,
                   " Fixed stage layout: a close view of a rusty iron ledge in the middle of the frame, a clear zip-seal plastic bag holding a worn black notebook resting on it just above the rising black water, the base of the black iron wheel beside it; nobody in the scene.")
GATE_WATER = Scene('gate_room', " A last dim red glow fades over a chamber of still black water.",
                   " Fixed stage layout: a close view of a calm black water surface filling the middle of the frame with a few small bubbles rising to the surface and widening rings of ripples, a dim red glow lying on the water; the sealed round steel gate looms soft behind; nobody in the scene.")
GATE_AFTER = Scene('gate_room', " A cold pale work-lamp light falls on a silent chamber, the water gone.",
                   " Fixed stage layout: a small concrete chamber with the floor covered in wet grey silt and shallow puddles; the massive round steel gate door, sealed, fills the back wall with a small black headset hanging by its cord from the rim of the black iron hand-wheel; the clear zip-seal bag with the worn black notebook rests on the rusty iron ledge beside the wheel at frame-right; at frame-left the doorway has been cleared into a rough opening in the rubble letting in pale light; nobody in the scene.")
GATE_AFTER_SU = Scene('gate_room', GATE_AFTER.end,
                      " Fixed stage layout: a small concrete chamber with the floor covered in wet grey silt; the massive round steel gate door, sealed, fills the back wall with a small black headset hanging by its cord from the rim of the black iron hand-wheel; the clear zip-seal bag with the worn black notebook rests on the rusty iron ledge beside the wheel at frame-right; at frame-left a rough opening in the cleared rubble lets in pale light.")
CORR_DRAINED = Scene('flood_corridor', " A cold pale light falls on a long silent corridor, the water gone.",
                     " Fixed stage layout: a long grey concrete corridor recedes down the middle of the frame, its floor covered in wet grey silt and shallow puddles with tide lines on the walls; a pair of small yellow maintenance robots with grabber arms stand idle at one side; the red strobes along the ceiling are dark; a heavy round steel hatch door stands at the near end at frame-right; nobody in the scene.")
KITCH_TEA = Scene('bunker_living', LIVING.end,
                  " Fixed stage layout: the open kitchen with the black-and-gold stove is at frame-left, a copper kettle steaming on it; the small round wooden dining table fills the middle of the frame set with two white teacups side by side and a small plate of dried red dates; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
EDEN_NOTE = Scene('eden', EDEN.end,
                  " Fixed stage layout: long tiers of white hydroponic channels full of lettuce and tomato plants fill the middle of the frame under rows of hanging pink-violet grow lamps; a small wooden lectern at frame-left holds an open black notebook; a tall tomato vine heavy with red fruit stands at frame-right beside a metal watering can; the steel staircase stands behind.")
TOMATO_CLOSE = Scene('eden', EDEN.end,
                     " Fixed stage layout: a close view of a tomato vine in the middle of the frame with one large ripe deep-red tomato hanging heavy among smaller green ones, a drop of water on its skin; pink-violet grow-lamp light glows behind and the hydroponic channels blur; nobody in the scene.")
HOTPOT = Scene('bunker_living', LIVING.end,
               " Fixed stage layout: the open kitchen with the black-and-gold stove is at frame-left; the small round wooden dining table fills the middle of the frame with a bubbling copper hotpot of red broth in its centre, plates of thin sliced lamb, mushrooms, greens and tofu around it, and two chairs facing each other across it, one of them empty with a white bowl and a pair of chopsticks laid in front of it; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
EMPTY_SEAT = Scene('bunker_living', LIVING.end,
                   " Fixed stage layout: a close view of an empty wooden chair at the small round dining table in the middle of the frame, a white bowl and a pair of chopsticks laid neatly in front of it, steam from the copper hotpot drifting past; nobody in the scene.")

AE = lambda en, zh: (en, zh)

# ================================================================================================ 第 67 集（A）
mode('A')
b67 = S.episode('剧本第67集｜最后一道闸门', '林峰转动手轮把闸门彻底关死，水漫到他的胸口；苏清月在控制室听见水声停了，他说关好了，她说你说话别停；他从胸口的口袋里掏出一颗红番茄，说你的书没白读，咬了一口，说很甜；他把日志写完最后一页，画外独白说你读到这页门已关好、别怪这扇门也别怪我、番茄记得浇水、往后的春天都归你；他把日志装进塑封袋放在高处的铁台上；控制室里耳麦信号中断，苏清月说他会回来的；闸门室里水面静下来，只有几个气泡浮上来。', 67)
b67.character('LinRec', 'radio_set', LINREC_EN, LINREC_ZH)

TAA('67-01', '01｜闸门室：林峰的手从手轮上滑落，整个人靠在彻底关死的圆形钢闸门上，水漫到胸口，他头向后仰，闭上眼睛长长地吐出一口气', 8, GATE_CHEST,
    [P('lin_work', 'right', "leaning back against the sealed round steel gate chest-deep in black water in profile facing frame-left, his hands sliding off the rim of the black iron hand-wheel and dropping into the water, his head tipped back against the gate", 'closed', "his jaw loosening, his lips parting in a long slow breath, his brows easing", outfit=LIN_WET, shut='gently closed')],
    'Medium shot, the man from the head to the chest, in the middle third of the frame, in the flooded gate chamber.',
    "<lin_work> lets his hands slide off the rim of the black iron hand-wheel and leans back against the sealed round gate with the black water at his chest, his head tipping back and his eyes closing as he lets out one long slow breath; the red strobe pulses on the water.",
    "林峰的手从黑铁手轮的边上滑下来，靠在彻底关死的圆形闸门上，黑色的水漫到胸口，头向后仰，眼睛闭上，长长地缓缓吐出一口气；红色应急灯在水面上一闪一闪。",
    Q('The slow slosh of black water, a deep hush behind the gate and one long exhale.', '黑水缓缓晃动的声音、闸门后深深的寂静和一声长长的呼气。'),
    AE("A slow red emergency strobe pulses over the black water and lays a crimson rim along his wet cheek and jaw while thin white dust drifts down through the flicker.",
       "一盏缓慢的红色应急灯在黑色的水面上脉动，在他湿润的脸颊和下颌上勾出一圈深红边，薄薄的白色尘土在闪烁里飘下来。"),
    holds='The frame holds the sealed gate, and one person: Lin.',
    cam=push1('his closed eyes and the long breath', '他闭着的眼睛和长长的呼气'))

DL('67-02', '02｜控制室：苏清月戴着耳机说水声停了，耳机里林峰说关好了，她说你说话别停，他说我在这儿', CONTROL_C,
   [P('su_cozy', 'center', "sitting forward on the black swivel chair at the control console in profile facing frame-right, one hand pressing the headset earpiece to her ear and the other flat on the console, her head turned toward the monitor wall", 'obj:the wall of small monitors', "her lips parting, her eyes wide and wet, her brows pulled together", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "水声停了。", 'lin_work', 'low trembling', '低沉发颤'),
    ('lin_work', "关好了。", 'su_cozy', 'low soft', '低沉轻柔'),
    ('su_cozy', "你说话，别停。", 'lin_work', 'low breaking', '低沉发颤'),
    ('lin_work', "我在这儿。", 'su_cozy', 'low gentle', '低沉温柔')],
   V('The faint crackle of radio static in an earpiece, a deep hush in the control room and a shaky breath.', '耳机里电流细细的沙沙声、控制室深深的寂静和一声发颤的呼吸。'),
   AE("Cool green status-light glow rims her wet cheek and the black headset while a warm amber lamp lays a gold edge along her shoulder and the screens flicker faintly behind her.",
      "冷冷的绿色指示灯光勾着她湿润的脸颊和黑色耳机，一盏温暖的琥珀色灯在她的肩头镀了一道金边，身后的屏幕微微闪动。"),
   post_en='after the last line she closes her eyes and presses the earpiece harder against her ear',
   post_zh='最后一句之后，她闭上眼睛，把耳机更用力地按在耳朵上',
   cam=push1('her face and the headset', '她的脸和耳机'), bg='Behind her the wall of small monitors glows.',
   room={'Su'}, ld=SU_LD)

DL('67-03', '03｜闸门室：林峰从湿透的胸口口袋里掏出一颗红色的小番茄，对苏清月说口袋里还有一颗番茄，她说你现在吃什么番茄，他说很甜你的书没白读，她说你别吓我，他咬了一口', GATE_CHEST,
   [P('lin_work', 'right', "leaning back against the sealed gate chest-deep in black water in profile facing frame-left, a small bright red tomato held up in his right hand in front of his face, his headset earpiece in his right ear, his head turned toward the tomato", 'obj:the small red tomato in his hand', "his lips curving in a faint tender sweet smile, his eyes wet and bright, his brows soft", outfit=LIN_WET)],
   'Medium close shot, the man from the head to the chest, in the middle third of the frame, in the flooded gate chamber.',
   [('lin_work', "口袋里，还有一颗番茄。", 'su_cozy', 'low gentle', '低沉温柔'),
    ('su_cozy', "你现在吃什么番茄！", 'lin_work', 'sharp breaking', '锐利发颤'),
    ('lin_work', "很甜。你的书，没白读。", 'su_cozy', 'low warm', '低沉温暖'),
    ('su_cozy', "你别吓我。", 'lin_work', 'low sobbing', '低沉带着哭腔')],
   V('The slow slosh of black water, the crackle of radio static in an earpiece and a soft wet bite.', '黑水缓缓晃动的声音、耳机里电流的沙沙声和一声轻轻的湿润的咬东西的声音。'),
   AE("A slow red emergency strobe pulses over the black water and the small tomato glows a vivid red in his wet hand like a lantern while a thin warm gold from the brass plate lays an edge on his cheek.",
      "缓慢的红色应急灯在黑水上脉动，他湿漉漉的手里那颗小番茄像一盏灯笼一样鲜红发亮，黄铜板一线温暖的金光落在他的脸颊上。"),
   pre_en='He takes a small red tomato out of the chest pocket of his soaked henley.', pre_zh='他从湿透的亨利衫胸口的口袋里掏出一颗红色的小番茄。',
   post_en='after the last line he lifts the tomato and takes one slow bite',
   post_zh='最后一句之后，他把番茄举起来，缓缓咬了一口',
   cam=push1('his face and the tomato', '他的脸和那颗番茄'), bg='Behind him the massive sealed round steel gate door fills the back wall of the chamber.',
   ld=LIN_LD, tail=2.5)

MONO('67-04', '04｜闸门室：林峰一只手把日志举在水面上，另一只手握着铅笔，在最后一页上写字，他的嘴唇闭着，画外传来他的内心独白：你读到这页门已关好，别怪这扇门也别怪我，番茄记得浇水，往后的春天都归你', GATE_CHEST,
     [P('lin_work', 'right', "leaning back against the sealed gate chest-deep in black water in profile facing frame-left, a worn black notebook held open above the water on his left palm and a short pencil in his right hand writing on its last page, his head bowed toward the page", 'obj:the open notebook in his hand', "his jaw relaxed, his lips closed, his eyes calm and wet, his brows soft", outfit=LIN_WET)],
     'Medium close shot, the man from the head to the chest, in the middle third of the frame, in the flooded gate chamber.',
     "<lin_work> holds the worn black notebook open above the black water on his left palm and writes slowly on its last page with a short pencil, his head bowed over the page, the red strobe pulsing over the water, his jaw relaxed, his lips closed and his brows soft, a thin tear running down his cheek.",
     "林峰用左手托着那本磨旧的黑色日志举在黑水上面，右手握着短铅笔在最后一页慢慢写字，头低着，红色应急灯在水面上脉动，下颌放松，嘴唇闭着，眉头舒展，一道细细的泪痕顺着脸颊流下来。",
     V('The slow slosh of black water, the faint scratch of a pencil on paper and only his calm inner voice-over spoken.', '黑水缓缓晃动的声音、铅笔在纸上细细的沙沙声，只有他平静的内心独白在说话。'),
     AE("A slow red emergency strobe pulses over the black water and the pale page glows like a small lamp in his hands, throwing a soft warm light up onto his wet face.",
        "缓慢的红色应急灯在黑水上脉动，那页苍白的纸在他手里像一盏小灯一样发亮，把柔和温暖的光投在他湿润的脸上。"),
     [ "你读到这页，门已关好。", "别怪这扇门，也别怪我。", "番茄，记得浇水。", "往后的春天，都归你。" ],
     holds='The frame holds the sealed gate, and one person: Lin.',
     cam=push1('the pencil and the page', '铅笔和那一页纸'), mind=13)

INS('67-05', '05｜闸门室：一个透明的塑封袋，里面装着那本黑色日志，放在手轮旁边一块锈铁台上，黑色的水刚好漫到铁台下沿', 6, GATE_LEDGE,
    'Close shot of the ledge and the bag, the bag in the middle third of the frame, nobody in the scene.',
    "A clear zip-seal bag holding a worn black notebook rests on a rusty iron ledge just above the rising black water beside the base of the black iron wheel, the water lapping at the edge of the ledge. Nothing else moves.",
    "一个透明的塑封袋，里面装着那本磨旧的黑色日志，放在黑铁手轮底座旁一块锈铁台上，黑色的水正漫到铁台的下沿，轻轻拍着。别的什么都不动。",
    Q('The slow slosh of black water against iron and a deep hush.', '黑水缓缓拍打铁台的声音和深深的寂静。'),
    'The frame holds the ledge and the bag, and nobody in the scene.',
    push1('the clear bag with the notebook', '装着日志的透明袋'),
    AE("A slow red emergency strobe pulses over the black water and glints on the clear plastic of the bag while a thin warm gold from the brass plate lays a soft line along the worn cover.",
       "缓慢的红色应急灯在黑水上脉动，在透明的塑料袋上闪着，黄铜板一线温暖的金光在磨旧的封面上落下一条柔和的线。"))

DL('67-06', '06｜控制室：苏清月对着耳机说你说话啊，伊甸说耳麦信号已中断，她说他会回来的', CONTROL_C,
   [P('su_cozy', 'center', "sitting forward on the black swivel chair at the control console in profile facing frame-right, both hands pressing the headset to her ears, her head bowed toward the console", 'obj:the console', "her lips trembling, her eyes wide and streaming, her brows pulled up", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "你说话啊。", 'lin_work', 'low breaking', '低沉发颤'),
    ('eden_voice', "耳麦信号，已中断。", 'su_cozy', 'soft calm', '轻柔平静'),
    ('su_cozy', "他会回来的。", 'eden_voice', 'low shaking', '低沉发抖')],
   V('A thin electronic hiss that drops to silence, the hum of the console and a shaky breath.', '一声细细的电子嘶声渐渐掉进寂静里、控制台的嗡鸣和一声发颤的呼吸。'),
   AE("Cool green status-light glow rims her wet cheeks and the black headset while the thin blue ring of the wall speaker glows above her and a single tear catches the light.",
      "冷冷的绿色指示灯光勾着她湿润的脸颊和黑色耳机，头顶墙上扬声器那圈细细的蓝光亮着，一滴眼泪在光里闪了一下。"),
   post_en='after the last line she lowers the headset slowly from her ears and holds it against her chest',
   post_zh='最后一句之后，她把耳机慢慢从耳朵上拿下来，抱在胸口',
   cam=push1('her face and the headset', '她的脸和耳机'), bg='On the wall above the console a flat speaker panel with a thin blue ring glows.',
   room={'Su'}, ld=SU_LD, tail=2.5)

INS('67-07', '07｜闸门室：黑色的水面渐渐安静下来，几个细小的气泡一个接一个浮到水面上，漾开一圈圈涟漪，暗红色的光在水面上慢慢暗下去', 8, GATE_WATER,
    'Close shot of the water surface, the bubbles and rings in the middle third of the frame, nobody in the scene.',
    "A calm black water surface fills the frame as a few small bubbles rise one after another and break, widening rings of ripples across it, the dim red glow lying on the water slowly fading to darkness. Nothing else moves.",
    "一片平静的黑色水面，几个细小的气泡一个接一个浮上来破开，水面上漾开一圈圈涟漪，倒映在水里的暗红色光慢慢暗成一片黑。别的什么都不动。",
    Q('A few soft pops of bubbles and a long deep hush.', '几声轻轻的气泡破开的声音和一片长长的深深的寂静。'),
    'The frame holds the black water surface, and nobody in the scene.',
    descend('the water surface and the last rings', '水面和最后的涟漪'),
    AE("The last dim red glow slides over the water and fades while pale rings of ripple glint in it and a silver bubble catches the light as it rises.",
       "最后一点暗红色的光从水面上滑过、渐渐消失，淡淡的涟漪圈在光里闪着，一个银色的气泡在上升时映着光。"))

# ================================================================================================ 第 68 集（A）
b68 = S.episode('剧本第68集｜说好会回来', '三天后，伊甸报告通道积水已抽干，苏清月问过去多久、伊甸说七十一小时，她说我去接他；走廊里水退了只剩淤泥，闸门室里闸门紧闭、他的耳麦挂在手轮上、塑封的日志放在铁台上；苏清月站在被机器人清开的缺口前，跪下来抱着日志，说你说好会带我回来的，你说话不算数，我不原谅你；她靠着闸门读日志；回到控制室，伊甸问是否保留林先生的权限，她说保留，说他的番茄需要浇水，她说我去。', 68)

DL('68-01', '01｜控制室：憔悴的苏清月坐在转椅里，伊甸说通道积水已抽干，她问过去多久了，伊甸说七十一小时，她说我去接他', CONTROL_C,
   [P('su_cozy', 'center', "sitting on the black swivel chair at the control console in profile facing frame-right, the headset hanging around her neck and her hands loose in her lap, her head lifted toward the wall speaker", 'obj:the wall speaker above the console', "her lips dry and parted, her eyes hollow and red-rimmed, her brows low", outfit=SU_HAGGARD)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('eden_voice', "通道积水，已抽干。", 'su_cozy', 'soft calm', '轻柔平静'),
    ('su_cozy', "过去多久了？", 'eden_voice', 'low hoarse', '低沉沙哑'),
    ('eden_voice', "七十一小时。", 'su_cozy', 'soft calm', '轻柔平静'),
    ('su_cozy', "我去接他。", 'eden_voice', 'low firm', '低沉坚定')],
   V('A soft electronic chime, the hum of the console and a long dry breath.', '一声轻轻的电子提示音、控制台的嗡鸣和一声长长的干涩的呼吸。'),
   AE("Cool green status-light glow rims her hollow cheek while the thin blue ring of the wall speaker glows above her and a pale grey morning-like wash from the screens falls across her loose hair.",
      "冷冷的绿色指示灯光勾着她凹陷的脸颊，头顶墙上扬声器那圈细细的蓝光亮着，屏幕一片淡淡的灰白色光落在她散着的头发上。"),
   post_en='after the last line she stands up slowly from the chair with one hand on the console',
   post_zh='最后一句之后，她一只手扶着控制台，慢慢从转椅里站起来',
   cam=lowrise('her face and the wall speaker above', '她的脸和头顶的扬声器'), bg='On the wall above the console a flat speaker panel with a thin blue ring glows.',
   room={'Su'}, tail=2.5)

INS('68-02', '02｜生活区走廊：洪水退去后的长走廊，地上是湿漉漉的灰色淤泥和浅浅的水洼，墙上留着一道水线，两个黄色的小维修机器人静静停在一边', 7, CORR_DRAINED,
    'Wide shot of the corridor, the silt floor in the middle third of the frame, nobody in the scene.',
    "A long grey concrete corridor lies silent after the flood, its floor covered in wet grey silt and shallow puddles, a dark tide line along the walls and two small yellow maintenance robots standing idle at one side. Nothing moves.",
    "洪水退去后，一条长长的灰色混凝土走廊一片寂静，地上是湿漉漉的灰色淤泥和浅浅的水洼，墙上留着一道深色的水线，两个黄色的小维修机器人静静地停在一边。一动不动。",
    Q('A deep hush, the slow drip of water from the ceiling and the faint tick of drying concrete.', '深深的寂静、天花板上缓慢的滴水声和混凝土变干时细细的嘀嗒声。'),
    'The frame holds the silent corridor and the two robots, and nobody in the scene.',
    follow('the long corridor floor', '长长的走廊地面', 'the far end of the corridor fills the middle third of the frame', '走廊远端占满画面中间三分之一'),
    AE("A cold pale work-lamp light lies along the wet silt and glints in the shallow puddles while a thin drifting haze hangs in the still air and the yellow robots glow dull gold.",
       "冷冷的淡淡的工作灯光沿着湿淤泥铺开，在浅水洼里闪着，静止的空气里挂着薄薄的雾气，黄色的机器人泛着暗金色的光。"))

INS('68-03', '03｜闸门室：水退之后的小房间，地上是灰色的淤泥，关死的圆形钢闸门前，手轮上挂着一副黑色的耳麦，旁边铁台上放着装着日志的塑封袋', 8, GATE_AFTER,
    'Medium shot of the gate and the wheel, the wheel with the headset in the middle third of the frame, nobody in the scene.',
    "In the silent chamber a small black headset hangs by its cord from the rim of the black iron hand-wheel in front of the sealed round gate, the clear bag with the worn black notebook resting on the iron ledge beside it, the floor covered in wet grey silt. Nothing moves.",
    "安静的小房间里，关死的圆形闸门前，一副小小的黑色耳麦用线挂在黑铁手轮的边上，旁边铁台上放着装着磨旧黑色日志的透明塑封袋，地上是湿漉漉的灰色淤泥。一动不动。",
    Q('A deep hush, one slow drip of water and the faint tick of cooling steel.', '深深的寂静、一声缓慢的滴水和钢铁冷却时细细的嘀嗒声。'),
    'The frame holds the sealed gate, the wheel with the headset and the ledge with the bag, and nobody in the scene.',
    push1('the headset hanging on the wheel', '挂在手轮上的耳麦'),
    AE("A cold pale light from the cleared opening lays a long soft line across the silt and the sealed gate and glints on the clear plastic bag while dust hangs motionless in the still air.",
       "从被清开的缺口照进来的冷冷的淡光，在淤泥和关死的闸门上拉出一条长长的柔和的线，在透明的塑料袋上闪着，尘埃一动不动地悬在静止的空气里。"))

TAA('68-04', '04｜闸门室门口：憔悴的苏清月站在被清开的碎石缺口前，手电的光束照在关死的闸门上，她用一只手捂住嘴，眼睛看着手轮上挂着的耳麦', 8, GATE_AFTER_SU,
    [P('su_cozy', 'left', "standing in the cleared opening in the rubble in profile facing frame-right, a torch in her left hand pointing its beam at the sealed gate and her right hand pressed over her mouth, her head turned toward the headset on the wheel", 'obj:the small black headset hanging on the wheel', "her lips pressed behind her hand, her eyes wide and flooding, her brows pulled up", outfit=SU_HAGGARD)],
    'Medium shot, the woman from the head to the knees, in the middle third of the frame, in the cleared doorway.',
    "<su_cozy> stands in the cleared opening of the rubble with a torch in her left hand pointing at the sealed gate and her right hand pressed over her mouth, her wide eyes fixed on the small black headset hanging from the wheel, her shoulders beginning to shake. Nothing else moves.",
    "苏清月站在被清开的碎石缺口里，左手拿着手电，光束照着关死的闸门，右手捂着嘴，睁大的眼睛盯着手轮上挂着的小小的黑色耳麦，肩膀开始发抖。别的什么都不动。",
    Q('A deep hush, one slow drip of water and a muffled shaky breath.', '深深的寂静、一声缓慢的滴水和一声被捂住的发颤的呼吸。'),
    AE("The white beam of her torch cuts through the hanging dust and glints on the sealed gate while a cold pale light from behind her lays a thin rim along her loose hair and her wet cheek.",
       "她手电的白色光束划开悬着的尘埃，在关死的闸门上闪着，身后冷冷的淡光在她散着的头发和湿润的脸颊上勾出一圈薄边。"),
    holds='The frame holds the cleared doorway and the sealed gate, and one person: Su.',
    cam=push1('her face and the beam of the torch', '她的脸和手电的光束'))

DL('68-05', '05｜闸门室：苏清月跪在手轮前，把耳麦抱在手里，对着空荡荡的房间说你说好，会带我回来的，你说话不算数，我不原谅你，然后把日志塑封袋抱在胸口、额头抵在冰冷的闸门上', GATE_AFTER_SU,
   [P('su_cozy', 'left', "kneeling in the grey silt in front of the wheel in profile facing frame-right, the small black headset held in both hands and the clear bag with the notebook in her lap, her head bowed toward the headset", 'obj:the small black headset in her hands', "her lips trembling, her eyes streaming, her brows pulled up", outfit=SU_HAGGARD)],
   'Medium close shot, the woman from the head to the waist, in the middle third of the frame, in front of the gate.',
   [('su_cozy', "你说好，会带我回来的。", 'su_cozy', 'low breaking', '低沉发颤'),
    ('su_cozy', "你说话，不算数。", 'su_cozy', 'low sobbing', '低沉带着哭腔'),
    ('su_cozy', "我不原谅你。", 'su_cozy', 'low shaking', '低沉发抖')],
   V('A deep hush, the faint creak of cooling steel and a ragged sobbing breath.', '深深的寂静、钢铁冷却时轻轻的吱嘎声和一声参差不齐的哭泣的呼吸。'),
   AE("A cold pale light from the cleared opening glints on the tears on her cheek and the small headset in her hands while a thin warm line of gold from the old brass plate lies along the edge of the notebook bag.",
      "从被清开的缺口照进来的冷冷的淡光在她脸颊的泪水和手里的小耳麦上闪着，旧黄铜板一线温暖的金光落在日志袋的边沿。"),
   post_en='after the last line she presses the bag with the notebook to her chest and rests her forehead against the cold sealed gate',
   post_zh='最后一句之后，她把装着日志的塑封袋紧紧抱在胸口，把额头抵在冰冷的闸门上',
   cam=push1('her face and the headset', '她的脸和耳麦'), bg='Behind her the massive sealed round steel gate door with its black iron hand-wheel fills the back wall of the chamber.',
   room={'Su'}, tail=2.5)

TAA('68-06', '06｜闸门室：苏清月背靠着关死的闸门坐在淤泥里，腿上摊开那本日志，用指尖慢慢划过最后一页，一滴眼泪落在纸页的边上', 8, GATE_AFTER_SU,
    [P('su_cozy', 'left', "sitting on the silt-covered floor with her back against the sealed gate in profile facing frame-right, the black notebook open on her knees and one fingertip resting on the last page, her head bowed over the page", 'obj:the open notebook on her knees', "her lips pressed together and trembling, her eyes streaming, her brows soft", outfit=SU_HAGGARD)],
    'Medium shot, the woman from the head to the knees, in the middle third of the frame, in front of the gate.',
    "<su_cozy> sits on the silt-covered floor with her back against the sealed gate and the black notebook open on her knees, drawing one fingertip slowly across the last page while a single tear falls onto the edge of the paper. Nothing else moves.",
    "苏清月背靠着关死的闸门坐在淤泥地上，膝盖上摊开那本黑色日志，用一根指尖慢慢划过最后一页，一滴眼泪落在纸页的边上。别的什么都不动。",
    Q('A deep hush, the soft rustle of a page and a quiet shaky breath.', '深深的寂静、纸页轻轻的沙沙声和一声安静的发颤的呼吸。'),
    AE("A cold pale light from the cleared opening lays a soft line across the open page and her bowed head while a thin warm gold from the old brass plate catches the tear as it falls.",
       "从被清开的缺口照进来的冷冷的淡光在摊开的那一页和她低垂的头上拉出一条柔和的线，旧黄铜板一线温暖的金光映着落下的那滴眼泪。"),
    holds='The frame holds the sealed gate, and one person: Su.',
    cam=pull('the page and her fingertip', '纸页和她的指尖', 'the whole small chamber with her small figure against the gate', '整间小房间和靠着闸门小小的她'))

DL('68-07', '07｜控制室：苏清月站在控制台前，伊甸问是否保留林先生的权限，她说保留，伊甸说他的番茄需要浇水，她说我去', CONTROL_C,
   [P('su_cozy', 'center', "standing at the control console in profile facing frame-right with the black notebook held against her chest, her head lifted toward the wall speaker", 'obj:the wall speaker above the console', "her lips pressed together, her eyes red but steady, her brows level", outfit=SU_HAGGARD)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('eden_voice', "是否保留林先生的权限？", 'su_cozy', 'soft gentle', '轻柔温和'),
    ('su_cozy', "保留。", 'eden_voice', 'low steady', '低沉平稳'),
    ('eden_voice', "他的番茄，需要浇水。", 'su_cozy', 'soft gentle', '轻柔温和'),
    ('su_cozy', "我去。", 'eden_voice', 'low firm', '低沉坚定')],
   V('A soft electronic chime, the hum of the console and a long slow breath.', '一声轻轻的电子提示音、控制台的嗡鸣和一声长长的缓慢的呼吸。'),
   AE("Cool green status-light glow rims her cheek while the thin blue ring of the wall speaker glows above her and a warm amber lamp lays a soft gold edge along the notebook in her arms.",
      "冷冷的绿色指示灯光勾着她的脸颊，头顶墙上扬声器那圈细细的蓝光亮着，一盏温暖的琥珀色灯在她怀里的日志边上镀了一道柔和的金边。"),
   post_en='after the last line she wipes her cheek with the back of her hand and walks out through the steel door at frame-right with the notebook against her chest',
   post_zh='最后一句之后，她用手背擦了一下脸颊，抱着日志大步走出右边的钢门',
   cam=push1('her face and the wall speaker', '她的脸和墙上的扬声器'), bg='On the wall above the console a flat speaker panel with a thin blue ring glows.',
   room={'Su'}, exit=('Su',), tail=2.5)

# ================================================================================================ 第 69 集（A）
b69 = S.episode('剧本第69集｜一个人的伊甸', '清晨，苏清月穿着他的亨利衫煮了两杯茶，伊甸说林先生不在，她说我知道放着就好；她在农场的小讲台上翻开他的日志照着浇水，自言自语念着他写的字；1号番茄藤结出最大的一颗番茄，伊甸问是否采摘，她说不留着；伊甸提醒她体重下降了三公斤，她说我知道，让伊甸念他留下的食谱；傍晚她照食谱煮了番茄鸡蛋，一个人尝了一口。', 69)

INS('69-01', '01｜地下二层农场：一排排白色水培槽里的生菜和番茄在粉紫色的生长灯下静静地长着，叶子上挂着细细的水珠，一切井井有条，没有一个人', 7, EDEN_NOTE,
    'Wide shot of the farm level, the tiers of plants in the middle third of the frame, nobody in the scene.',
    "Long tiers of white hydroponic channels full of lettuce and tomato plants grow quietly under rows of hanging pink-violet lamps, fine drops of water clinging to the leaves, a black notebook open on a small wooden lectern at frame-left. Nothing moves.",
    "一排排白色水培槽里的生菜和番茄在一排排粉紫色的生长灯下静静地长着，叶子上挂着细细的水珠，左边小讲台上摊开着一本黑色日志。一动不动。",
    Q('The faint trickle of water in the channels and the soft hum of the grow lamps.', '水槽里细细的流水声和生长灯轻轻的嗡鸣。'),
    'The frame holds the farm tiers and the notebook on the lectern, and nobody in the scene.',
    slide('toward frame-right', '右', 'the tall tomato vine heavy with red fruit fills the middle third of the frame', '挂满红果的高高的番茄藤占满画面中间三分之一'),
    AE("Pink-violet grow-lamp light glows through the leaves and fine droplets glitter on them while thin mist drifts through the beams and a single red tomato glows warm at the edge.",
       "粉紫色的生长灯光透过叶子发亮，叶子上细小的水珠闪着光，薄薄的雾气在光柱里飘，边上一颗红色的番茄发着暖光。"))

DL('69-02', '02｜厨房：苏清月穿着林峰的亨利衫站在灶台前煮茶，把两只白瓷杯放在桌上，伊甸说早安，她说两杯热茶，伊甸说林先生不在，她说我知道放着就好', KITCH_TEA,
   [P('su_cozy', 'center', "standing at the round dining table in profile facing frame-right, a steaming copper kettle in her right hand pouring tea into the second of two white teacups, her head lifted toward the wall speaker", 'obj:the wall speaker above the table', "her lips pressed into a gentle thin line, her eyes tired and soft, her brows level", outfit=SU_ALONE)],
   'Medium shot, the woman from the head to the thighs, in the middle third of the frame, at the dining table.',
   [('eden_voice', "早安，苏女士。", 'su_cozy', 'soft gentle', '轻柔温和'),
    ('su_cozy', "两杯热茶。", 'eden_voice', 'low quiet', '低沉安静'),
    ('eden_voice', "林先生不在。", 'su_cozy', 'soft careful', '轻柔小心'),
    ('su_cozy', "我知道。放着就好。", 'eden_voice', 'low steady', '低沉平稳')],
   V('The gentle gurgle of tea into a cup, the soft crackle of the stove and a quiet breath.', '茶倒进杯子轻轻的汩汩声、炉灶轻轻的噼啪声和一声安静的呼吸。'),
   AE("Soft morning-gold lamp light lies across the table and the two white cups glow like pearls while steam from the kettle curls past her cheek and the amber stove glow warms the edge of the frame.",
      "柔和的晨金色灯光铺在桌面上，两只白瓷杯像珍珠一样发亮，壶里的热气卷过她的脸颊，炉灶琥珀色的光暖着画面的边缘。"),
   post_en='after the last line she sets the kettle down and slides the second cup an inch toward the empty chair',
   post_zh='最后一句之后，她放下茶壶，把第二只杯子朝空椅子那边推了一寸',
   cam=push1('her face and the two cups', '她的脸和两只杯子'), bg='On the wall above the table a flat speaker panel with a thin blue ring glows and the black-and-gold stove glows ember-orange at frame-left.',
   room={'Su'}, tail=2.5)

DL('69-03', '03｜地下二层农场：苏清月站在小讲台前照着日志浇水，自言自语念着他写的字，说三号槽每天浇一次水，说番茄不要见光太久，说他连字都写得这么凶', EDEN_NOTE,
   [P('su_cozy', 'left', "standing at the small wooden lectern in profile facing frame-right, a metal watering can in her right hand tipped over the nearest channel and the open black notebook under her left hand, her head bowed toward the notebook", 'obj:the open notebook on the lectern', "her lips curving in a small sad sweet smile, her eyes soft and wet, her brows lifted", outfit=SU_ALONE)],
   'Medium shot, the woman from the head to the knees, in the middle third of the frame, at the lectern.',
   [('su_cozy', "三号槽，每天浇一次水。", 'su_cozy', 'low reading', '低沉念着'),
    ('su_cozy', "番茄，不要见光太久。", 'su_cozy', 'low reading', '低沉念着'),
    ('su_cozy', "他连字，都写得这么凶。", 'su_cozy', 'low rueful', '低沉带着苦笑')],
   V('The gentle trickle of water from a watering can, the faint rustle of leaves and a quiet breath.', '洒水壶里细细的流水声、叶子轻轻的沙沙声和一声安静的呼吸。'),
   AE("Pink-violet grow-lamp light haloes her loose hair and falls across the open page while droplets from the can glitter in the beam and thin mist drifts through the leaves.",
      "粉紫色的生长灯光在她散着的头发上描出光晕，落在摊开的纸页上，洒水壶里落下的水珠在光柱里闪着，薄薄的雾气从叶子间飘过。"),
   post_en='after the last line she turns a page of the notebook with one finger and tips the can over the next channel',
   post_zh='最后一句之后，她用一根手指翻过一页日志，把洒水壶移到下一条水槽上',
   cam=slide('toward frame-right', '右', 'she fills the middle third of the frame with the tomato vine behind her', '她占满画面中间三分之一、身后是番茄藤'), bg='Behind her the tall tomato vine heavy with red fruit stands at frame-right beside the hydroponic channels.',
   room={'Su'}, tail=2.5)

INS('69-04', '04｜番茄藤特写：粉紫色的灯光下，一颗很大的深红色番茄沉甸甸地挂在藤上，旁边是几颗青色的小番茄，红番茄的表皮上挂着一滴水珠', 7, TOMATO_CLOSE,
    'Close shot of the tomato vine, the big red tomato in the middle third of the frame, nobody in the scene.',
    "One large ripe deep-red tomato hangs heavy among smaller green ones on the vine under pink-violet lamps, a single bright drop of water on its skin slowly swelling. Nothing else moves.",
    "粉紫色的灯光下，一颗很大的、熟透的深红色番茄沉甸甸地挂在藤上，旁边是几颗青色的小番茄，红番茄的表皮上有一滴明亮的水珠慢慢鼓起来。别的什么都不动。",
    Q('The faint trickle of water in the channels and the soft hum of the grow lamps.', '水槽里细细的流水声和生长灯轻轻的嗡鸣。'),
    'The frame holds the tomato vine, and nobody in the scene.',
    push1('the big red tomato', '那颗大红番茄'),
    AE("Pink-violet grow-lamp light glows through the translucent skin of the tomato and the water drop on it holds a tiny bright dot of the lamp rows while the green leaves blur softly behind.",
       "粉紫色的生长灯光透过番茄半透明的表皮发亮，皮上那颗水珠里映着一小排灯的倒影，后面绿色的叶子虚成柔和的一片。"))

DL('69-05', '05｜地下二层农场：苏清月停在番茄藤前，伊甸说一号番茄藤结出了最大的一颗，她说那是他种的第一棵，伊甸问是否采摘，她说不，留着', EDEN_NOTE,
   [P('su_cozy', 'right', "standing in front of the tall tomato vine in profile facing frame-left, one hand lifted to touch the large red tomato without picking it, her head lifted toward the wall speaker", 'obj:the wall speaker above the lectern', "her lips parting in a trembling sweet smile, her eyes soft and wet, her brows lifted", outfit=SU_ALONE)],
   'Medium shot, the woman from the head to the knees, in the middle third of the frame, in front of the tomato vine.',
   [('eden_voice', "一号藤，结出了最大的一颗。", 'su_cozy', 'soft gentle', '轻柔温和'),
    ('su_cozy', "那是他种的，第一棵。", 'eden_voice', 'low tender', '低沉温柔'),
    ('eden_voice', "是否采摘？", 'su_cozy', 'soft careful', '轻柔小心'),
    ('su_cozy', "不。留着。", 'eden_voice', 'low firm', '低沉坚定')],
   V('The gentle trickle of water in the channels, a soft electronic chime and the faint rustle of leaves.', '水槽里细细的流水声、一声轻轻的电子提示音和叶子轻轻的沙沙声。'),
   AE("Pink-violet grow-lamp light glows through the leaves and lays a soft rim along her cheek and her lifted fingers while the red tomato glows like a small lantern beside her.",
      "粉紫色的生长灯光透过叶子发亮，在她的脸颊和抬起的手指上勾出一圈柔和的边，身边那颗红番茄像一盏小灯笼一样发着光。"),
   post_en='after the last line she lets her hand drop and leaves the tomato hanging',
   post_zh='最后一句之后，她把手放下来，让那颗番茄继续挂在藤上',
   cam=push1('her face and the red tomato', '她的脸和红番茄'), bg='On the wall behind the lectern a flat speaker panel with a thin blue ring glows.',
   room={'Su'}, tail=2.5)

DL('69-06', '06｜控制室：伊甸说苏清月的体重下降了三公斤，她说我知道，伊甸说林先生留下了食谱，她说念给我听', CONTROL_C,
   [P('su_cozy', 'center', "sitting on the black swivel chair at the control console in profile facing frame-right, her knees drawn up under his oversized henley and her hands wrapped around a white mug, her head lifted toward the wall speaker", 'obj:the wall speaker above the console', "her lips curving in a tired thin sweet smile, her eyes soft and hollow, her brows level", outfit=SU_ALONE)],
   'Medium shot, the woman from the head to the knees, in the middle third of the frame, at the console.',
   [('eden_voice', "您的体重，下降三公斤。", 'su_cozy', 'soft careful', '轻柔小心'),
    ('su_cozy', "我知道。", 'eden_voice', 'low tired', '低沉疲惫'),
    ('eden_voice', "林先生留下了食谱。", 'su_cozy', 'soft gentle', '轻柔温和'),
    ('su_cozy', "念给我听。", 'eden_voice', 'low quiet', '低沉安静')],
   V('A soft electronic chime, the hum of the console and the faint tick of a mug on the desk.', '一声轻轻的电子提示音、控制台的嗡鸣和马克杯放在桌面上细细的嘀嗒声。'),
   AE("Cool green status-light glow rims her cheek and the steam of the mug curls through it while a warm amber lamp lays a soft gold edge along the oversized sleeve and the blue ring of the wall speaker glows above.",
      "冷冷的绿色指示灯光勾着她的脸颊，杯子里的热气在光里卷着，一盏温暖的琥珀色灯在那件宽大的袖子上镀了一道柔和的金边，头顶扬声器的蓝光亮着。"),
   post_en='after the last line she wraps both hands tighter around the mug and rests her cheek on her knee',
   post_zh='最后一句之后，她两只手把杯子握得更紧，把脸颊靠在膝盖上',
   cam=push1('her face and the mug', '她的脸和马克杯'), bg='On the wall above the console a flat speaker panel with a thin blue ring glows.',
   room={'Su'}, tail=2.5)

TAA('69-07', '07｜厨房：傍晚，苏清月一个人站在灶台前，把煮好的番茄鸡蛋盛进碗里，尝了一小口，慢慢咽下去，轻轻点了点头，眼眶红了', 8, KITCH_TEA,
    [P('su_cozy', 'center', "standing at the stove in profile facing frame-right, a small white bowl of golden scrambled egg and tomato in her left hand and a spoon raised to her lips in her right, her head bowed toward the bowl", 'obj:the small white bowl in her hand', "her lips closing slowly around the spoon, her eyes wet and soft, her brows easing", outfit=SU_ALONE)],
    'Medium shot, the woman from the head to the thighs, in the middle third of the frame, at the stove.',
    "<su_cozy> takes a small spoonful of tomato and egg from the white bowl, swallows slowly and gives one small nod, her eyes filling with tears while steam from the pot rises past her cheek. Nothing else moves.",
    "苏清月从白瓷小碗里舀了一小勺番茄鸡蛋放进嘴里，慢慢咽下去，轻轻点了一下头，眼眶里盈满了泪水，锅里的热气从她脸颊旁升起。别的什么都不动。",
    Q('The soft crackle of the stove, the faint clink of a spoon on porcelain and a quiet breath.', '炉灶轻轻的噼啪声、勺子碰瓷碗轻轻的叮当声和一声安静的呼吸。'),
    AE("Warm amber stove light flickers on her wet cheek and the golden egg glows in the bowl while steam curls up past her face and the honey-gold lamp light softens the edge of the frame.",
       "温暖的琥珀色炉火在她湿润的脸颊上闪动，碗里金黄的鸡蛋发着光，热气卷着升过她的脸，蜂蜜般的金色灯光让画面的边缘变得柔和。"),
    holds='The frame holds the stove and the bowl, and one person: Su.',
    cam=push1('her face and the spoon', '她的脸和勺子'), bg='Behind her the black-and-gold stove glows ember-orange at frame-left.')

# ================================================================================================ 第 70 集（A）
b70 = S.episode('剧本第70集｜余温', '苏清月一个人煮了一锅火锅，对着对面的空椅子说话，说汤底辣了点、你说过一个人吃饭最难、我没哭是辣的；她翻日志的旁注，发现他记着她怕冷、记着她爱吃辣；伊甸说有一段林先生留下的录音，她说放，录音里他说春天来了替我去看看；她把手放在扬声器上；伊甸报告地表温度升到零度、冰面开始裂开，她说我知道了。', 70)

INS('70-01', '01｜厨房：一口红汤的铜火锅在圆木桌中间咕嘟咕嘟地冒泡，周围摆着切得薄薄的羊肉、蘑菇、青菜和豆腐，对面一张空椅子前放着一个碗和一双筷子', 7, HOTPOT,
    'Medium high shot of the dining table, the hotpot in the middle third of the frame, nobody in the scene.',
    "A copper hotpot of red broth bubbles in the middle of the round wooden table, plates of thin sliced lamb, mushrooms, greens and tofu around it, and across it an empty chair with a white bowl and a pair of chopsticks laid neatly before it. Nothing else moves.",
    "圆木桌中间一口红汤的铜火锅咕嘟咕嘟冒着泡，四周摆着切得薄薄的羊肉、蘑菇、青菜和豆腐，对面一张空椅子前整整齐齐放着一个白碗和一双筷子。别的什么都不动。",
    Q('The loud rolling bubble of a boiling hotpot, the soft crackle of the stove and the faint tick of porcelain.', '火锅沸腾响亮的翻滚声、炉灶轻轻的噼啪声和瓷器轻轻的嘀嗒声。'),
    'The frame holds the hotpot and the empty chair, and nobody in the scene.',
    descend('the bubbling red broth', '翻滚的红汤'),
    AE("Honey-gold lamp light makes the red broth glow like molten amber, thick steam rises in slow curls through the beam and the empty bowl waits in the soft light.",
       "蜂蜜般的金色灯光让红汤像熔化的琥珀一样发亮，浓浓的热气在光柱里一缕缕往上卷，空碗在柔和的灯光里静静等着。"))

DL('70-02', '02｜厨房：苏清月一个人坐在火锅边，夹着一片羊肉涮进红汤里，对着对面的空椅子说汤底辣了点，说你说过一个人吃饭最难，说我没哭是辣的', HOTPOT,
   [P('su_cozy', 'left', "sitting at the round dining table in profile facing frame-right, chopsticks lowering a slice of lamb into the bubbling red broth, her head lifted toward the empty chair across the table", 'obj:the empty chair across the table', "her lips curving in a wobbly small sweet smile, her eyes red and wet, her brows lifted", outfit=SU_ALONE)],
   'Medium shot, the woman from the head to the chest, in the middle third of the frame, at the dining table.',
   [('su_cozy', "汤底，辣了点。", 'su_cozy', 'low rueful', '低沉带着苦笑'),
    ('su_cozy', "你说过，一个人吃饭最难。", 'su_cozy', 'low soft', '低沉轻柔'),
    ('su_cozy', "我没哭，是辣的。", 'su_cozy', 'low breaking', '低沉发颤')],
   V('The loud rolling bubble of a boiling hotpot, the soft clink of chopsticks and a quiet shaky breath.', '火锅沸腾响亮的翻滚声、筷子轻轻的碰响和一声安静的发颤的呼吸。'),
   AE("Honey-gold lamp light and the red glow of the broth warm her wet cheek while thick steam curls up between her and the empty chair and the amber stove glow rims her hair.",
      "蜂蜜般的金色灯光和红汤的红光暖着她湿润的脸颊，浓浓的热气在她和空椅子之间卷着升起，炉灶琥珀色的光勾着她的头发。"),
   post_en='after the last line she lifts the cooked slice of lamb to her bowl and then sets her chopsticks down on the rim',
   post_zh='最后一句之后，她把涮好的羊肉夹进自己的碗里，然后把筷子搁在碗沿上',
   cam=push1('her face and the steam', '她的脸和热气'), bg='Across the table the empty chair stands with a white bowl and a pair of chopsticks laid before it.',
   room={'Su'}, tail=2.5)

INS('70-03', '03｜厨房：对面那张空椅子特写，椅子前整整齐齐摆着干净的白碗和筷子，火锅的热气从旁边慢慢飘过', 6, EMPTY_SEAT,
    'Close shot of the empty chair, the chair and the bowl in the middle third of the frame, nobody in the scene.',
    "An empty wooden chair stands at the round table with a clean white bowl and a pair of chopsticks laid neatly before it while steam from the hotpot drifts slowly past. Nothing else moves.",
    "圆桌边一张空木椅，前面整整齐齐摆着一个干净的白碗和一双筷子，火锅的热气慢慢从旁边飘过。别的什么都不动。",
    Q('The soft rolling bubble of a hotpot far behind and a deep hush.', '身后远处火锅轻轻的翻滚声和深深的寂静。'),
    'The frame holds the empty chair and the bowl, and nobody in the scene.',
    push1('the clean white bowl', '那只干净的白碗'),
    AE("Honey-gold lamp light lies softly on the empty chair and the clean bowl glows like a pearl while thin steam drifts through the beam.",
       "蜂蜜般的金色灯光柔柔地铺在空椅子上，干净的白碗像珍珠一样发亮，薄薄的热气在光柱里飘过。"))

DL('70-04', '04｜厨房：苏清月边吃边翻日志的旁注，自言自语地念，说第十二页写着我怕冷，说第三十页写着我爱吃辣，说他连我的口味都记着', HOTPOT,
   [P('su_cozy', 'left', "sitting at the round dining table in profile facing frame-right, the black notebook propped open against the hotpot tray and her chopsticks in her right hand, her head bowed toward the notebook", 'obj:the open notebook on the table', "her lips curving in a wet small sweet smile, her eyes shining with tears, her brows lifted", outfit=SU_ALONE)],
   'Medium shot, the woman from the head to the chest, in the middle third of the frame, at the dining table.',
   [('su_cozy', "第十二页，写着我怕冷。", 'su_cozy', 'low reading', '低沉念着'),
    ('su_cozy', "第三十页，写着我爱吃辣。", 'su_cozy', 'low reading', '低沉念着'),
    ('su_cozy', "他连我的口味，都记着。", 'su_cozy', 'low breaking', '低沉发颤')],
   V('The loud rolling bubble of a boiling hotpot, the soft rustle of a turning page and a quiet breath.', '火锅沸腾响亮的翻滚声、翻页轻轻的沙沙声和一声安静的呼吸。'),
   AE("Honey-gold lamp light and the red glow of the broth warm the open page and her wet cheek while steam curls up past the notebook and the amber stove glow rims her hair.",
      "蜂蜜般的金色灯光和红汤的红光暖着摊开的纸页和她湿润的脸颊，热气卷着升过日志，炉灶琥珀色的光勾着她的头发。"),
   post_en='after the last line she presses her fingertip to the margin of the page and holds it there',
   post_zh='最后一句之后，她把指尖按在那一页的页边上，停在那里',
   cam=slide('toward frame-left', '左', 'she fills the middle third of the frame with the open notebook', '她和摊开的日志占满画面中间三分之一'), bg='Behind her the black-and-gold stove glows ember-orange at frame-left.',
   room={'Su'}, tail=2.5)

DL('70-05', '05｜控制室：伊甸说有一段林先生留下的录音，苏清月说放，墙上的扬声器里传出林峰的声音说春天来了替我去看看，她说好', CONTROL_C,
   [P('su_cozy', 'center', "standing at the control console in profile facing frame-right, her hands pressed flat on the console and the black notebook beside them, her head lifted toward the wall speaker", 'obj:the wall speaker above the console', "her lips parted and trembling, her eyes wide and wet, her brows pulled up", outfit=SU_ALONE)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('eden_voice', "有一段林先生的录音。", 'su_cozy', 'soft gentle', '轻柔温和'),
    ('su_cozy', "放。", 'eden_voice', 'low quiet', '低沉安静'),
    ('lin_rec', "春天来了，替我去看看。", 'su_cozy', 'low warm tired', '低沉温暖疲惫'),
    ('su_cozy', "好。", 'lin_rec', 'low breaking', '低沉发颤')],
   V('A soft electronic chime, a faint tape hiss and the hum of the console.', '一声轻轻的电子提示音、细细的磁带嘶声和控制台的嗡鸣。'),
   AE("Cool green status-light glow rims her wet cheek while the thin blue ring of the wall speaker glows above her and a warm amber lamp lays a soft gold edge along her trembling hands.",
      "冷冷的绿色指示灯光勾着她湿润的脸颊，头顶墙上扬声器那圈细细的蓝光亮着，一盏温暖的琥珀色灯在她发抖的手上镀了一道柔和的金边。"),
   post_en='after the last line she lays her palm flat against the wall below the speaker and closes her eyes',
   post_zh='最后一句之后，她把手掌平平地按在扬声器下面的墙上，闭上眼睛',
   cam=push1('her face and the wall speaker', '她的脸和墙上的扬声器'), bg='On the wall above the console a flat speaker panel with a thin blue ring glows.',
   room={'Su'}, tail=2.5, extra_assets=())

TAA('70-06', '06｜控制室：苏清月把额头靠在扬声器下面的墙上，手掌贴着墙，肩膀轻轻颤抖，闭着眼睛，眼泪顺着脸颊流下来，嘴角却微微弯起', 8, CONTROL_C,
    [P('su_cozy', 'center', "standing close to the wall below the speaker in profile facing frame-right, her forehead resting against the wall and one palm flat beside it, the black notebook held in her other arm", 'closed', "the corners of her mouth curving faintly through her tears, her eyes closed, her brows pulled up", outfit=SU_ALONE, shut='gently closed')],
    'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the wall.',
    "<su_cozy> rests her forehead against the wall below the speaker with her palm flat beside it and her eyes closed, her shoulders trembling gently while tears run down her cheek and the corners of her mouth curve faintly. Nothing else moves.",
    "苏清月把额头靠在扬声器下面的墙上，手掌平平地贴在旁边，闭着眼睛，肩膀轻轻颤抖，眼泪顺着脸颊流下来，嘴角却微微弯起。别的什么都不动。",
    Q('A deep hush, the faint hum of the console and a quiet shaky breath.', '深深的寂静、控制台轻微的嗡鸣和一声安静的发颤的呼吸。'),
    AE("The thin blue ring of the wall speaker glows above her and lays a cool line along her cheek while a warm amber lamp turns the edge of her hair to gold and a tear catches both lights.",
       "头顶墙上扬声器那圈细细的蓝光在她的脸颊上拉出一条冷线，一盏温暖的琥珀色灯把她头发的边缘染成金色，一滴眼泪映着两种光。"),
    holds='The frame holds the wall, and one person: Su.',
    cam=pull('her closed eyes', '她闭着的眼睛', 'she and the wall with the glowing speaker above', '她和墙上发着蓝光的扬声器'))

DL('70-07', '07｜控制室：伊甸报告地表温度升到零度，苏清月擦了擦脸问冰面呢，伊甸说冰面开始裂开，她说我知道了', CONTROL_C,
   [P('su_cozy', 'center', "standing at the control console in profile facing frame-right, one hand wiping her cheek and the other on the black notebook, her head lifted toward the wall speaker", 'obj:the wall speaker above the console', "her lips pressed into a steady line, her eyes red but clear, her brows level", outfit=SU_ALONE)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('eden_voice', "地表温度，零度。", 'su_cozy', 'soft calm', '轻柔平静'),
    ('su_cozy', "冰面呢？", 'eden_voice', 'low quick', '低沉急促'),
    ('eden_voice', "冰面，开始裂开。", 'su_cozy', 'soft calm', '轻柔平静'),
    ('su_cozy', "我知道了。", 'eden_voice', 'low steady', '低沉平稳')],
   V('A soft electronic chime, the hum of the console and a long slow breath.', '一声轻轻的电子提示音、控制台的嗡鸣和一声长长的缓慢的呼吸。'),
   AE("Cool green status-light glow rims her cheek while the thin blue ring of the wall speaker glows above her and a pale grey-white wash from the screens falls across the notebook.",
      "冷冷的绿色指示灯光勾着她的脸颊，头顶墙上扬声器那圈细细的蓝光亮着，屏幕一片淡淡的灰白色光落在日志上。"),
   post_en='after the last line she lifts her chin and tucks the notebook under her arm',
   post_zh='最后一句之后，她抬起下巴，把日志夹在胳膊底下',
   cam=lowrise('her face and the wall speaker', '她的脸和墙上的扬声器'), bg='On the wall above the console a flat speaker panel with a thin blue ring glows.',
   room={'Su'}, tail=2.5)

report()
doc = S.finish()
