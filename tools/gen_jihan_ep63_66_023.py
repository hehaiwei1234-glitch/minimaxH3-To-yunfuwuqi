#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 63–66 集，追加稿 023（2026-10-15 夜，hh 挂机，要 20 集；A／B 混用）。
故事见 `剧本/第55-74集_结局版大纲.md`。以 022（第 59–62 集）的 JSON 为底，必须等 022 在插件里全部跑完再追加；追加窗口不要勾每集／总／任务秒数。
写法分配：
  第 63 集 钻机：A（军阀的出场、周宁在囚笼里、“诱饵竖井”的计划，重要、压迫）；
  第 64 集 请君入瓮：前半 B（试音、报深度，快）＋闸门开启 A ＋结果镜头 ＋ B（控制室收尾）；
  第 65 集 军阀的反击：A（裴远山爬出残骸、周宁喊“还有一发”、关闸到一半爆炸、通道塌方、洪水改道）；
  第 66 集 手轮：A（苏清月“不准关”、林峰“外科医生只做最后一刀”、最后的话、转手轮）。
偏离原大纲：军阀士兵只在车队里远远出现、不拍被水冲走的人；冰湖水冲天只拍水柱和翻倒的车；温压弹只拍火球和冲击波；
  不拍林峰被埋；第 66 集不拍他关上（关上在第 67 集）；“B4 闸门”在台词里说“闸门”，不写字母数字。
H3 方面的风险（交稿时单列，不算我的错）：
  · 63-01／64-02／64-05／64-06／65-05 车队、钻机、水柱冲天、火球（大场面特效）；
  · 63-04／65-02 裴远山在画面里对着对讲机说话（嘴动、对讲机）；63-03／65-03 周宁在囚笼里对着藏在衣服里的小对讲机说话；
  · 64-01／64-04／65-04／65-06／66-03／66-06 林峰对着耳麦说话、苏清月在画外的声音（可能被画成画面里多出一个人）；
  · 64-04／65-04／66-07 手轮转动（慢的持续动作，但手轮是机械）；65-06 塌方后的碎石；
  · 66-05 两只手握着手轮、左手手指合不拢；水位升高。
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
OUT = '合并稿/023_第63-66集_钻机请君入瓮军阀的反击手轮_制作稿_追加'
S = Session('合并稿/022_第59-62集_末日橱窗周宁与裴远山冰雪消融的警钟倒灌危机_制作稿_追加.json', OUT, 92000)
B6.S = S
B7.S = S

# ---------------------------------------------------------------------------------------------- 衣着／人物
LIN_HEAD = "in a charcoal henley with the sleeves pushed up to his forearms and dark cargo trousers, a small headset earpiece in his right ear and a slim microphone clipped at his jaw"
LIN_WET = "in a charcoal henley soaked dark with water and clinging to his shoulders, a small headset earpiece in his right ear and a slim microphone clipped at his jaw, his black hair dripping"
SU_HEADSET = "in a cream knit sweater with the sleeves pushed up, black thermal leggings and soft boots, a black over-ear headset with a slim boom microphone on her head, her long black hair tied back"
PEI_COAT = "in a long black wool greatcoat with a thick dark fur collar, black leather gloves, a black radio handset in his right fist, his short silver hair swept back"
PEI_WET = "in a long black wool greatcoat soaked dark and heavy with water, torn at one shoulder, the dark fur collar matted, his short silver hair plastered to his forehead, a black radio handset in his right fist"
NING_CAGE = "in a torn, filthy grey hooded sweatshirt soaked at the hem, bruises on his cheekbone and a split lip, his black hair matted"
look('pei_warlord', 'Pei', PEI_COAT, 'cold grey-brown', 'his', eth='a Chinese man in his fifties')
PEI_EN = "A cold, courteous, unhurried deep middle-aged man's voice, speaking clear Mandarin Chinese." + VT_EN
PEI_ZH = '冷静客气、不紧不慢的低沉中年男声，普通话清楚。' + VT_ZH

# ---------------------------------------------------------------------------------------------- 场景
SIEGE = Scene('siege_field', " Cold pale dawn light over a vast thawing snowfield, thin mist rising from the wet snow and a fading green aurora overhead.",
              " Fixed stage layout: a vast thawing snowfield fills the frame; across the middle of the frame in a long line stand twenty heavy matte-black armoured trucks with steel plough blades, one tall black drilling rig on tracks with a long vertical drill mast raised, and one flatbed truck carrying a rusty iron cage; thin exhaust smoke rises from them; the dark mountain slope rises at the back of the frame; nobody in the scene.")
SIEGE_RIG = Scene('siege_field', SIEGE.end,
                  " Fixed stage layout: the tall black drilling rig stands over a round steel shaft cover set in the grey snow in the middle of the frame, its drill bit pressed against the cover and thin white steam leaking out around the edge of the cover; two matte-black armoured trucks wait parked behind it; the dark mountain slope rises at the back; nobody in the scene.")
SIEGE_GEYSER = Scene('siege_field', SIEGE.end,
                     " Fixed stage layout: a tall column of white water and shattered ice erupts from a round shaft mouth in the middle of the frame and shoots fifty metres into the air; the black drilling rig tilts crookedly beside it and two armoured trucks are thrown on their sides in the churning slush; the dark mountain slope rises at the back; nobody in the scene.")
SIEGE_WRECK = Scene('siege_field', SIEGE.end,
                    " Fixed stage layout: the thawing snowfield is flooded with grey slush and broken ice; the black drilling rig lies toppled on its side in the middle of the frame, armoured trucks lie overturned at angles around it and thin steam rises from the wet metal; the dark mountain slope rises at the back; nobody in the scene.")
SIEGE_FIRE = Scene('siege_field', SIEGE.end,
                   " Fixed stage layout: a white-hot orange fireball swallows a round shaft mouth in the middle of the frame and rolls upward into a dark billowing column of smoke and snow, a ring of flattened snow racing outward across the field; the dark mountain slope rises at the back; nobody in the scene.")
PEI_TRUCK = Scene('siege_field', SIEGE.end,
                  " Fixed stage layout: the flat steel roof of the lead matte-black armoured truck fills the foreground of the frame, the thawing snowfield and the long line of black trucks soft behind it and the dark mountain slope at the back; no other people in the scene.")
PEI_WRECK = Scene('siege_field', SIEGE.end,
                  " Fixed stage layout: a flooded slush field of grey water and broken ice; a smashed overturned matte-black armoured truck with a split cab lies at frame-left, thin steam rising from it; the toppled drilling rig lies far behind in the middle distance; no other people in the scene.")
CAGE = Scene('cage_truck', " Cold pale dawn light falls on the open flatbed of a truck with a rusty iron cage, a grey sky behind.",
             " Fixed stage layout: a rusty iron cage with thick bars fills the middle of the frame on the flatbed of a truck, a dented steel bucket in one corner; the thawing snowfield and a black armoured truck are soft behind it; no other people in the scene.")
GATE_RUBBLE = Scene('gate_room', " A single caged work lamp flickers over a cold concrete chamber and a red emergency strobe pulses through the dust.",
                    " Fixed stage layout: a small concrete chamber with ankle-deep dark water on the floor; the massive round steel gate door with a big black iron hand-wheel at its centre fills the back wall, the rectangular brass plate with a hand-shaped recess set into the wall at frame-right; the doorway at frame-left is sealed by a heap of broken concrete and twisted rebar with dust still falling from it; a cracked ceiling above.")
GATE_HANDS = Scene('gate_room', GATE_RUBBLE.end,
                   " Fixed stage layout: a close view of two hands gripping the rim of the big black iron hand-wheel in the middle of the frame, the left hand's fingers only half curled around the rim, dark water rising around the base of the wheel; the dull steel gate behind; nobody else in the scene.")
FLOOD_CORR = Scene('flood_corridor', " A red emergency strobe pulses in a long concrete corridor filled with the roar of water.",
                   " Fixed stage layout: a long grey concrete corridor recedes down the middle of the frame; dark churning water pours down it from the far end toward the camera, knee-deep and rising; red emergency strobes pulse along the ceiling; a heavy round steel hatch door stands closed at the near end at frame-right; nobody in the scene.")

CULVERT = Scene('flood_corridor', FLOOD_CORR.end,
                " Fixed stage layout: a huge rough-walled stone culvert tunnel recedes down the middle of the frame; a roaring torrent of dark icy water fills its floor and pours away from the camera toward the far end at great speed, white foam on the wave tops; a few dim caged lamps along the wall; nobody in the scene.")

# ================================================================================================ 第 63 集（A）
mode('A')
b63 = S.episode('剧本第63集｜钻机', '潜望镜里，黑色装甲车队载着高高的钻机和一辆囚笼卡车开到山前，苏清月认出笼子里的周宁；裴远山站在头车车顶用对讲机说给十二个小时，开门交出补给和人，不然钻机替你开；林峰说那就让他钻错地方，那口诱饵竖井在冰碛湖下面；林峰去闸门室，苏清月守控制室，让他不准摘耳机。', 63)
new_scene(b63, 'siege_field', '被军阀围困的雪原（正在融化的雪地，二十辆黑色装甲车、一台高高的黑色履带钻机和一辆载着铁笼的平板卡车排成一线）',
          'A vast thawing snowfield at dawn with a line of twenty matte-black armoured trucks, a tall black tracked drilling rig and a flatbed truck carrying an iron cage standing across it.',
          '黎明时一片正在融化的广阔雪原，二十辆哑光黑的装甲车、一台高高的黑色履带钻机和一辆载着铁笼的平板卡车排成一线。',
          'the line of armoured trucks and the drilling rig')
new_scene(b63, 'cage_truck', '卡车平板上的铁笼（锈迹斑斑的粗铁栏杆，笼角有一只凹陷的钢桶）',
          'The open flatbed of a truck carrying a rusty iron cage with thick bars and a dented steel bucket in one corner.',
          '卡车的平板上载着一个锈迹斑斑的铁笼，栏杆很粗，笼角有一只凹陷的钢桶。',
          'the iron cage')
new_scene(b63, 'flood_corridor', '被洪水灌满的长走廊（灰色混凝土走廊，黑色的水从远端涌来，红色应急频闪，近端一扇关着的圆形钢舱门）',
          'A long grey concrete corridor with dark churning water pouring down it from the far end, red emergency strobes pulsing along the ceiling and a heavy round steel hatch door closed at the near end.',
          '一条长长的灰色混凝土走廊，黑色的水从远端翻涌过来，天花板上红色应急灯频闪，近端有一扇关着的厚重圆形钢舱门。',
          'the flooded corridor and the hatch door')
new_person(b63, 'pei_warlord', '裴远山（军阀）', 'man',
           'A cold-eyed Chinese man in his fifties with short swept-back silver hair and a lean lined face, in a long black wool greatcoat with a thick dark fur collar and black leather gloves.',
           '一个五十来岁、眼神冰冷的中国男人，银灰色的短发向后梳，脸瘦削有皱纹，穿黑色长款羊毛大衣、厚厚的深色毛领，戴黑色皮手套。',
           'in a long black wool greatcoat with a thick dark fur collar and black leather gloves, short silver hair swept back, a lean lined face',
           'a cold, level, unreadable expression', eth='a Chinese man in his fifties')
b63.character('Pei', 'pei_warlord', PEI_EN, PEI_ZH)

INS('63-01', '01｜潜望镜里的雪原：黎明的冷光里，二十辆黑色装甲车、一台高高的钻机和一辆载着铁笼的卡车排成一线，停在山前正在融化的雪地上', 8, SIEGE,
    'Wide shot of the whole line, the trucks and the rig in the middle third of the frame, nobody in the scene.',
    "At dawn twenty matte-black armoured trucks, a tall black drilling rig with its mast raised and a flatbed truck carrying a rusty iron cage stand in a long line across the wet thawing snowfield, thin exhaust smoke rising from them. Nothing moves.",
    "黎明时，二十辆哑光黑的装甲车、一台立着钻杆的高高的黑色钻机和一辆载着锈铁笼的平板卡车排成一长列，停在湿漉漉正在融化的雪地上，它们身上升着细细的尾气。一动不动。",
    Q('A long low howl of wind over the wet snow and the deep idle rumble of many engines far away.', '风掠过湿雪长长的低啸和远处很多发动机深沉的怠速轰鸣。'),
    'The frame holds the line of trucks and the drilling rig, and nobody in the scene.',
    slide('toward frame-right', '右', 'the tall drilling rig fills the middle third of the frame', '高高的钻机占满画面中间三分之一'),
    AE("Pale cold dawn light glints on the wet matte-black armour, thin exhaust smoke curls up into the fading green aurora and a pearly mist lies low over the thawing snow.",
       "苍白冰冷的晨光在湿漉漉的哑光黑装甲上闪着，细细的尾气卷着升进渐渐淡去的绿色极光里，一层珍珠色的薄雾低低地贴在正在融化的雪上。"))

DL('63-02', '02｜潜望镜室：苏清月把眼睛贴在目镜上，数出二十辆装甲车和一台钻机，林峰说他们走了三天，她说囚笼里是周宁，他说我看见了', PERI,
   [P('su_cozy', 'left', "leaning forward at the periscope column in profile facing frame-right with one eye at the padded eyepiece and one hand tight on the steel handle, her head tilted toward him", 'obj:the periscope eyepiece', "her lips pressed into a hard line, her eyes narrowed and cold, her brows low", outfit=SU_SLIP),
    P('lin_home', 'right', "standing close behind her in profile facing frame-left, one hand on the steel column, his head turned toward her", 'Su', "his jaw clenched, his eyes dark and still, his brows low", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the thighs, in the middle third of the frame, at the periscope column.',
   [('su_cozy', "二十辆装甲车，还有钻机。", 'lin_home', 'low cold', '低沉冰冷'),
    ('lin_home', "他们走了三天。", 'su_cozy', 'low flat', '低沉平淡'),
    ('su_cozy', "囚笼里的，是周宁。", 'lin_home', 'low tight', '低沉发紧'),
    ('lin_home', "我看见了。", 'su_cozy', 'low grim', '低沉凝重')],
   V('A deep low hum of ventilation, the faint squeak of a rubber eyepiece and a held breath.', '通风系统深沉的低鸣、橡胶目镜轻轻的吱吱声和一声屏住的呼吸。'),
   AE("Cool blue-white light from the round screen at the back lays a pale rim along her cheek and his jaw while a thin amber lamp warms the black steel column between them.",
      "后面圆形屏幕冷冷的蓝白色光在她的脸颊和他的下颌勾出一圈淡淡的边，一线琥珀色的灯光暖着他们之间的黑色钢柱。"),
   post_en='after the last line <su_cozy> lifts her eye from the eyepiece and her knuckles whiten on the steel handle',
   post_zh='最后一句之后，苏清月把眼睛从目镜上抬起来，握着钢柄的指节发白',
   cam=push('both of them', '两人'), bg='Behind them the round view screen glows on the curved concrete wall at frame-right.')

TAA('63-03', '03｜铁笼：浑身是伤的周宁抓着铁笼的两根粗栏杆，额头抵在栏杆上，眼睛望着远处的山', 7, CAGE,
    [P('ning_partner', 'center', "standing inside the iron cage in profile facing frame-right, both bruised hands gripping two thick bars and his forehead pressed against the bars, his head turned toward the distant mountain", 'obj:the distant mountain beyond the bars', "his lips trembling and split, his eyes red and hollow and fixed on the mountain, his brows pulled up", outfit=NING_CAGE)],
    'Medium shot, the man from the head to the waist, in the middle third of the frame, in the cage.',
    "<ning_partner> stands inside the rusty iron cage gripping two thick bars with both bruised hands, his forehead against the bars and his hollow eyes fixed on the distant mountain, a thin tremor running through his shoulders. Nothing else moves.",
    "周宁站在锈迹斑斑的铁笼里，两只带着淤青的手抓着两根粗栏杆，额头抵在栏杆上，空洞的眼睛望着远处的山，肩膀上有细细的颤抖。别的什么都不动。",
    Q('A thin howl of wind, the faint creak of rusty iron and a shaky breath.', '风细细的呼啸、锈铁轻轻的吱嘎声和一声发颤的呼吸。'),
    AE("Pale cold dawn light slants through the iron bars and lays dark stripes across his bruised face while a pearly mist drifts low over the snowfield behind him.",
       "苍白冰冷的晨光斜斜地穿过铁栏杆，在他带着淤青的脸上投下一道道暗影，他身后的雪原上低低地飘着一层珍珠色的薄雾。"),
    holds='The frame holds the cage, and one person: Ning.',
    cam=push1('his bruised face between the bars', '栏杆间他带着淤青的脸'))

DL('63-04', '04｜头车车顶：裴远山站在黑色装甲车的车顶，对着手里的黑色对讲机说，给您十二个小时，开门，交出补给和人，不然钻机替您开', PEI_TRUCK,
   [P('pei_warlord', 'center', "standing on the steel roof of the lead armoured truck in three-quarter profile facing frame-right, a black radio handset raised to his lips in his gloved right fist, his coat hem lifting in the wind, his head turned toward the dark mountain", 'obj:the dark mountain slope', "his lips thin and calm, his eyes cold and unblinking, his brows level")],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, on the truck roof.',
   [('pei_warlord', "我给您十二个小时。", 'lin_home', 'cold courteous', '冰冷客气'),
    ('pei_warlord', "开门，交出补给和人。", 'lin_home', 'slow patient', '不紧不慢耐心'),
    ('pei_warlord', "不然，我的钻机替您开。", 'lin_home', 'cold soft', '冰冷轻柔')],
   V('A thin howl of wind, the crackle of a radio handset and the deep idle rumble of engines.', '风细细的呼啸、对讲机的沙沙声和发动机深沉的怠速轰鸣。'),
   AE("Pale cold dawn light rims his silver hair and the black fur collar while his coat hem snaps in the wind and a pearly mist drifts low over the line of armoured trucks behind him.",
      "苍白冰冷的晨光勾着他的银发和黑色的毛领，大衣下摆在风里猎猎作响，身后那一列装甲车上低低地飘着一层珍珠色的薄雾。"),
   post_en='after the last line he lowers the handset slowly and looks toward the mountain without blinking',
   post_zh='最后一句之后，他慢慢放下对讲机，一眨不眨地望着那座山',
   cam=push1('his face and the raised handset', '他的脸和举着的对讲机'),
   bg='Behind him the long line of matte-black armoured trucks and the tall drilling rig recede across the thawing snowfield.',
   ld={'lin_home': ('into the black radio handset in his fist', '对着手里黑色的对讲机')}, room={'Pei'})

DL('63-05', '05｜潜望镜室：苏清月说十二小时他不会等，林峰说那就让他钻错地方，她问诱饵竖井，他说它在湖的下面', PERI,
   [P('su_cozy', 'left', "standing beside the periscope column in profile facing frame-right, one hand on the steel handle, her head turned toward him", 'Lin', "her lips parting, her eyes sharp and searching, her brows lifted", outfit=SU_SLIP),
    P('lin_home', 'right', "standing beside her in profile facing frame-left, his arms crossed, his head turned toward her", 'Su', "his jaw easing, his eyes dark and calculating, his brows level", outfit=LIN_CLINIC)],
   'Medium two-shot, both from the head to the thighs, in the middle third of the frame, at the periscope column.',
   [('su_cozy', "十二小时，他不会等。", 'lin_home', 'low tight', '低沉发紧'),
    ('lin_home', "那就让他钻错地方。", 'su_cozy', 'low calm', '低沉平静'),
    ('su_cozy', "诱饵竖井？", 'lin_home', 'quiet probing', '安静试探'),
    ('lin_home', "它在湖的下面。", 'su_cozy', 'low steady', '低沉平稳')],
   V('A deep low hum of ventilation and a long quiet breath.', '通风系统深沉的低鸣和一声长长的安静的呼吸。'),
   AE("The blue-white glow of the round screen draws a cold rim along his folded arms and her cheek while a thin amber lamp warms the steel column and fine dust turns in the light.",
      "圆形屏幕蓝白色的光沿着他交叠的手臂和她的脸颊勾出一道冷边，一线琥珀色的灯光暖着钢柱，细尘在光里慢慢转。"),
   post_en='after the last line <su_cozy> slowly nods and a hard bright look comes into her eyes',
   post_zh='最后一句之后，苏清月慢慢点头，眼睛里亮起一点坚硬的光',
   cam=pull('their faces', '两人的脸', 'the two of them and the glowing round screen behind', '两人和身后发亮的圆形屏幕'), bg='Behind them the round view screen glows on the curved concrete wall at frame-right.')

DL('63-06', '06｜控制室：林峰背上工具包，苏清月帮他把耳麦调好，他说我去闸门室你守控制室，她说耳机别摘，他说摘了你也能找到我，她说少贫嘴', CONTROL_RADIO,
   [P('su_cozy', 'left', "standing facing him in profile facing frame-right, both hands adjusting the slim microphone clipped at his jaw, her head tilted up toward him", 'Lin', "her lips pressed into a firm line, her eyes bright with worry, her brows pulled together", outfit=SU_CLINIC),
    P('lin_home', 'right', "standing facing her in profile facing frame-left, a canvas toolbag over his shoulder and a headset earpiece in his right ear, his head bent toward her", 'Su', "his jaw easing, his eyes dark and warm, his brows soft", outfit=LIN_WORK)],
   'Medium close two-shot, both from the head to the chest, in the middle third of the frame, at the console.',
   [('lin_home', "我去闸门室，你守控制室。", 'su_cozy', 'low steady', '低沉平稳'),
    ('su_cozy', "耳机别摘。", 'lin_home', 'firm quiet', '坚定安静'),
    ('lin_home', "摘了，你也能找到我。", 'su_cozy', 'low gentle', '低沉温柔'),
    ('su_cozy', "少贫嘴。", 'lin_home', 'low fierce soft', '低沉带凶又软')],
   V('The soft click of a clip being fastened, a faint crackle of a headset and a quiet shared breath.', '夹子扣上轻轻的咔嗒声、耳机细细的沙沙声和两人安静的呼吸。'),
   AE("Cool green console light rims her cheek and his shoulder while a warm amber lamp from behind lays a gold edge on the toolbag strap and the tiny mic glints between her fingers.",
      "冷冷的绿色控制台光勾着她的脸颊和他的肩膀，身后一盏温暖的琥珀色灯在工具包的背带上镀了一道金边，她指间的小麦克风闪着光。"),
   post_en='after the last line she straightens the collar of his henley with both hands and pats his chest once',
   post_zh='最后一句之后，她用两只手把他亨利衫的领口整理好，在他胸口拍了一下',
   cam=push('both of them', '两人'), bg='Behind them the wall of small monitors glows at frame-left.')

INS('63-07', '07｜山前雪地：高高的钻机立在一个圆形钢井盖上，钻头压着井盖，井盖边缘漏出一缕缕白色的蒸汽', 6, SIEGE_RIG,
    'Medium shot of the rig and the shaft cover, the cover and the drill bit in the middle third of the frame, nobody in the scene.',
    "A tall black drilling rig stands over a round steel shaft cover in the grey snow with its drill bit pressed against the cover, thin white steam leaking out around the edge of the cover. Nothing else moves.",
    "一台高高的黑色钻机立在灰色的雪地里一个圆形钢井盖上，钻头压着井盖，井盖边缘漏出一缕缕白色的蒸汽。别的什么都不动。",
    Q('The deep idle rumble of a diesel engine, a faint hiss of steam and a thin wind.', '柴油发动机深沉的怠速轰鸣、蒸汽轻轻的嘶嘶声和细细的风。'),
    'The frame holds the drilling rig and the shaft cover, and nobody in the scene.',
    push1('the drill bit on the steel cover', '钢井盖上的钻头'),
    AE("Pale cold dawn light glints on the polished drill bit and the thin white steam from the shaft cover curls up through the beam, the wet snow around it shimmering.",
       "苍白冰冷的晨光在抛光的钻头上闪着，井盖漏出的细细白色蒸汽卷着升进光束里，四周湿漉漉的雪面泛着微光。"))

# ================================================================================================ 第 64 集（B＋A＋B）
b64 = S.episode('剧本第64集｜请君入瓮', '林峰戴着耳麦来到闸门室，苏清月在控制室报钻机离竖井三百米；钻头压在诱饵竖井的井盖上往下钻，苏清月报深度四十米、五十米、六十米；林峰把右手按在黄铜板上、两手握住手轮开闸，冰碛湖的水从地下冲进竖井，冲天而起，钻机翻倒、车队被冲散；苏清月说钻机翻了、车队散了，林峰说我现在关闸，伊甸警告有高热源正在逼近竖井，苏清月说他还活着。', 64)
mode('B')

DL('64-01', '01｜闸门室：林峰戴着耳麦站在圆形钢闸门前，苏清月在耳机里试音，说钻机离竖井三百米，他说收到，说他已经到闸门前了', GATE,
   [P('lin_work', 'right', "standing at the brass plate in profile facing frame-left, one hand resting on the black iron hand-wheel and a headset earpiece in his right ear with a slim microphone at his jaw, his head turned toward the wheel", 'obj:the black iron hand-wheel', "his jaw set, his eyes dark and focused, his brows level", outfit=LIN_HEAD)],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the gate chamber.',
   [('su_cozy', "试音，听得见吗？", 'lin_work', 'calm sharp', '冷静锐利'),
    ('lin_work', "听得见。", 'su_cozy', 'low steady', '低沉平稳'),
    ('su_cozy', "钻机离竖井，三百米。", 'lin_work', 'calm quick', '冷静利落'),
    ('lin_work', "收到。我到闸门前了。", 'su_cozy', 'low calm', '低沉平静')],
   V('A deep low hush with the faint tick of cooling steel and the crackle of radio static in an earpiece.', '深沉的低低寂静、钢铁冷却时细细的嘀嗒声和耳机里电流的沙沙声。'),
   AE("A single caged work lamp throws a hard white light on the round steel gate and a thin warm glow from the brass plate lays a gold edge along his jaw.",
      "一盏笼式工作灯把硬朗的白光洒在圆形钢闸门上，黄铜板一线温暖的光在他的下颌上镀了一道金边。"),
   post_en='after the last line he lifts his right hand from the wheel and lays it flat against the brass plate',
   post_zh='最后一句之后，他把右手从手轮上抬起来，平放在黄铜板上',
   cam=push1('his face and the iron wheel', '他的脸和黑铁手轮'), bg='Behind him the massive round steel gate door with its black iron hand-wheel fills the back wall of the chamber.',
   ld={'su_cozy': ('into the slim microphone clipped at his jaw', '对着别在下巴边的细细麦克风')})

INS('64-02', '02｜山前雪地：钻头压在圆形钢井盖上缓缓往下沉，井盖边缘漏出的白色蒸汽一股一股变浓，旁边装甲车静静停着', 7, SIEGE_RIG,
    'Medium shot of the rig and the shaft cover, the cover and the drill bit in the middle third of the frame, nobody in the scene.',
    "The tall black drilling rig stands over the round steel shaft cover with its drill bit sunk into the cover, thick white steam pouring out around the edge of the cover and drifting across the grey snow. Nothing else moves.",
    "高高的黑色钻机立在圆形钢井盖上，钻头已经嵌进井盖里，浓浓的白色蒸汽从井盖边缘涌出来，在灰色的雪地上飘散。别的什么都不动。",
    Q('The deep grinding rumble of a drill, a loud hiss of steam and a thin wind.', '钻机深沉的碾磨轰鸣、蒸汽响亮的嘶嘶声和细细的风。'),
    'The frame holds the drilling rig and the shaft cover, and nobody in the scene.',
    push1('the steaming shaft cover', '冒着蒸汽的井盖'),
    AE("Pale cold dawn light turns the drifting steam to pearl and the polished drill bit throws small sparks of light while the wet black armour glints behind.",
       "苍白冰冷的晨光把飘动的蒸汽染成珍珠色，抛光的钻头溅出小小的光点，后面湿漉漉的黑色装甲闪着光。"))

DL('64-03', '03｜控制室：苏清月戴着耳机盯着监控屏，对着麦克风报钻头进洞四十米，耳机里林峰说再等，她报五十米，他说还不够，她报六十米', CONTROL_C,
   [P('su_cozy', 'center', "sitting forward on the black swivel chair at the control console in profile facing frame-right, one hand pressing the headset earpiece to her ear and the other flat on the console, her head turned toward the monitor wall", 'obj:the wall of small monitors', "her lips pressed together, her eyes sharp and fixed, her brows low", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "钻头进洞了，四十米。", 'lin_work', 'calm quick', '冷静利落'),
    ('lin_work', "再等。", 'su_cozy', 'low steady', '低沉平稳'),
    ('su_cozy', "五十米。", 'lin_work', 'calm tight', '冷静发紧'),
    ('lin_work', "还不够。", 'su_cozy', 'low calm', '低沉平静'),
    ('su_cozy', "六十米！", 'lin_work', 'sharp quick', '锐利急促')],
   V('The faint crackle of radio static in an earpiece, the hum of the console and the quick tap of one finger on the desk.', '耳机里电流细细的沙沙声、控制台的嗡鸣和手指在桌面上急促的轻敲。'),
   AE("Cool green status-light glow rims her cheek and the black headset, a warm amber lamp lays a gold edge along her shoulder and the screens behind her flicker.",
      "冷冷的绿色指示灯光勾出她的脸颊和黑色耳机，一盏温暖的琥珀色灯在她的肩头镀了一道金边，身后的屏幕闪动。"),
   post_en='after the last line her finger stops tapping and she holds her breath',
   post_zh='最后一句之后，她敲桌面的手指停住，屏住了呼吸',
   cam=push1('her face and the headset', '她的脸和耳机'), bg='Behind her the wall of small monitors glows.',
   room={'Su'})

mode('A')
DL('64-04', '04｜闸门室：林峰把右手按在黄铜板上，两只手握住手轮，问钻头够深了吗，苏清月在耳机里说六十米就是现在，他说开闸，她说我在听，手轮被他慢慢拧动了一圈', GATE,
   [P('lin_work', 'right', "standing at the gate in profile facing frame-left, his right palm pressed against the brass plate and his left hand gripping the rim of the black iron hand-wheel, his headset earpiece in his right ear, his head turned toward the wheel", 'obj:the black iron hand-wheel', "his jaw clenched, his eyes dark and burning, his brows low", outfit=LIN_HEAD)],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the gate chamber.',
   [('lin_work', "钻头够深了吗？", 'su_cozy', 'low tight', '低沉发紧'),
    ('su_cozy', "六十米，就是现在。", 'lin_work', 'calm firm', '冷静坚定'),
    ('lin_work', "开闸。", 'su_cozy', 'low grave', '低沉凝重'),
    ('su_cozy', "我在听。", 'lin_work', 'soft steady', '轻柔平稳')],
   V('A deep low hush, the faint tick of cooling steel and the crackle of radio static in an earpiece, then the heavy grinding groan of the iron wheel.', '深沉的低低寂静、钢铁冷却时细细的嘀嗒声和耳机里电流的沙沙声，然后是铁手轮沉重的吱呀碾磨声。'),
   AE("A single caged work lamp throws a hard white light across the round steel gate while a thin warm glow from the brass plate lays a gold edge along his pressed palm and dust shivers in the beam.",
      "一盏笼式工作灯把硬朗的白光洒在圆形钢闸门上，黄铜板一线温暖的光在他按着的手掌上镀了一道金边，尘埃在光束里发颤。"),
   post_en='after the last line he turns the iron wheel slowly through a full circle with both hands, his arms tensing',
   post_zh='最后一句之后，他用两只手把铁手轮慢慢转了一整圈，手臂绷紧',
   cam=push1('his hands on the wheel', '他握着手轮的手'), bg='Behind him the massive round steel gate door with its black iron hand-wheel fills the back wall of the chamber.',
   ld={'su_cozy': ('into the slim microphone clipped at his jaw', '对着别在下巴边的细细麦克风')})

INS('64-05', '05｜地下涵洞：粗糙的石头涵洞里，一股冰冷的黑水带着白色的浪沫轰鸣着往远处的竖井方向冲去', 7, CULVERT,
    'Wide shot of the culvert, the torrent in the middle third of the frame, nobody in the scene.',
    "A roaring torrent of dark icy water rushes down the floor of a huge rough-walled stone culvert away from the camera toward the far end, white foam on the wave tops and spray flying off the walls. Nothing else moves except the water.",
    "一个巨大的粗糙石头涵洞里，一股冰冷的黑水带着白色的浪沫轰鸣着顺着洞底往远端冲去，水雾从石壁上飞溅。除了水以外，别的什么都不动。",
    Q('A thundering roar of rushing water echoing through stone and the crash of spray.', '洪水在石头里回荡的雷鸣般的轰响和水花的撞击声。'),
    'The frame holds the culvert and the torrent, and nobody in the scene.',
    follow('the front of the torrent', '水流的前锋', 'the rushing water vanishes into the far dark end', '奔涌的水消失在远端的黑暗里'),
    AE("The dim caged lamps along the wall flash on the white foam and the flying spray glitters in their light like scattered glass.",
       "沿着石壁的几盏昏暗的笼灯在白色的浪沫上闪着，飞溅的水雾在灯光里像散落的玻璃一样闪烁。"))

INS('64-06', '06｜山前雪地：圆形的井口里冲出一根几十米高的白色水柱，夹着碎冰冲上天空，歪斜的钻机倒向一边，两辆装甲车被掀翻在翻滚的泥水里', 8, SIEGE_GEYSER,
    'Wide shot of the shaft mouth and the rig, the column of water in the middle third of the frame, nobody in the scene.',
    "A tall column of white water and shattered ice erupts from the round shaft mouth fifty metres into the air while the black drilling rig tilts crookedly beside it and two armoured trucks lie thrown on their sides in the churning slush. Nothing else moves except the water.",
    "一根几十米高的白色水柱夹着碎冰从圆形的井口冲上天空，黑色的钻机歪斜着倒向一边，两辆装甲车被掀翻在翻滚的泥水里。除了水以外，别的什么都不动。",
    Q('A thundering roar of water, the crack of breaking ice and the heavy crash of metal.', '水雷鸣般的轰响、冰裂开的脆响和金属沉重的撞击声。'),
    'The frame holds the geyser, the toppling rig and the overturned trucks, and nobody in the scene.',
    rise('the top of the roaring column of water', '轰鸣的水柱顶端'),
    AE("The rising sun glints on the white column of water and a rainbow glitters in the spray while shattered ice glitters as it tumbles through the air.",
       "初升的太阳在白色的水柱上闪着，水雾里浮起一道细细的彩虹，碎冰翻落时在空气里闪闪发亮。"))

INS('64-07', '07｜山前雪地：水柱落下后，雪地变成一片灰色的泥水和碎冰，钻机横倒在中间，装甲车歪歪斜斜地翻在四周，湿漉漉的金属上冒着蒸汽', 7, SIEGE_WRECK,
    'Wide shot of the flooded field, the toppled rig in the middle third of the frame, nobody in the scene.',
    "Grey slush and broken ice cover the field where the black drilling rig lies toppled on its side and armoured trucks lie overturned at angles around it, thin steam rising from the wet metal. Nothing moves.",
    "水柱落下以后，雪地变成一片灰色的泥水和碎冰，黑色的钻机横倒在中间，装甲车歪歪斜斜地翻在四周，湿漉漉的金属上冒着细细的蒸汽。一动不动。",
    Q('The soft trickle of draining water, the creak of settling metal and a thin wind.', '积水退去轻轻的潺潺声、金属落定时的吱嘎声和细细的风。'),
    'The frame holds the flooded field and the wrecked vehicles, and nobody in the scene.',
    descend('the toppled drilling rig', '横倒的钻机'),
    AE("Pale cold dawn light glints on the wet slush and the steam from the wrecked trucks drifts through it in pearly threads while shards of ice glitter.",
       "苍白冰冷的晨光在湿漉漉的泥水上闪着，被毁的车辆上的蒸汽像珍珠色的丝线在光里飘，碎冰片闪闪发亮。"))

mode('B')
DL('64-08', '08｜控制室：苏清月看着屏幕说钻机翻了车队散了，耳机里林峰说好我现在关闸，她让他快回来，伊甸警告有高热源正逼近竖井，她说他还活着', CONTROL_C,
   [P('su_cozy', 'center', "sitting forward on the black swivel chair at the control console in profile facing frame-right, one hand pressing the headset earpiece to her ear, her head turned toward the monitor wall", 'obj:the wall of small monitors', "her lips parting in cautious relief, her eyes bright and wide, her brows lifted", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "钻机翻了，车队散了。", 'lin_work', 'bright relieved', '明亮如释重负'),
    ('lin_work', "好。我现在关闸。", 'su_cozy', 'low calm', '低沉平静'),
    ('su_cozy', "快回来。", 'lin_work', 'soft firm', '轻柔坚定'),
    ('eden_voice', "警告，高热源逼近竖井。", 'su_cozy', 'soft urgent', '轻柔急切'),
    ('su_cozy', "他还活着。", 'lin_work', 'low cold', '低沉冰冷')],
   V('The faint crackle of radio static in an earpiece, a soft electronic chime and the hum of the console.', '耳机里电流细细的沙沙声、一声轻轻的电子提示音和控制台的嗡鸣。'),
   AE("Cool green status-light glow rims her cheek and the black headset while a sudden red pulse from the wall alarm lays a hard red rim along her profile.",
      "冷冷的绿色指示灯光勾出她的脸颊和黑色耳机，墙上警报灯突然一闪的红光沿着她的侧脸勾出一道硬朗的红边。"),
   post_en='after the last line her hand curls into a fist on the console and she leans closer to the screen',
   post_zh='最后一句之后，她放在控制台上的手攥成拳头，身体向屏幕凑近',
   cam=push1('her face and the screen glow', '她的脸和屏幕的光'), bg='On the wall above the console a flat speaker panel with a thin glowing blue ring glows and a small red alarm lamp is above it.',
   room={'Su'})

# ================================================================================================ 第 65 集（A）
b65 = S.episode('剧本第65集｜军阀的反击', '裴远山浑身湿透地从翻倒的装甲车里爬出来，用对讲机说您的水淹不死我、我手里还有一发、对准您的暖气井；囚笼里的周宁用藏在衣服里的小对讲机喊还有一发温压弹、对准竖井了快躲；林峰在闸门室转着手轮关闸，苏清月在耳机里喊周宁说还有一发，他说转了一半，火球吞掉竖井口，冲击波震塌了闸门室的通道；林峰被困在手轮这一侧，苏清月在控制室喊要去救他，伊甸说洪水改道正涌向生活区，只剩九分钟。', 65)
mode('A')

TAA('65-01', '01｜山前泥水里：浑身湿透的裴远山从翻倒的装甲车破裂的驾驶室里手脚并用爬出来，爬到湿冰上，银发贴在额头上，眼睛里烧着火', 8, PEI_WRECK,
    [P('pei_warlord', 'center', "crawling out of the split cab of the overturned truck on his hands and knees onto the wet ice in profile facing frame-right, his soaked greatcoat dragging, his head lifted toward the mountain", 'obj:the dark mountain slope', "his teeth bared, his eyes burning and fixed ahead, his brows low", outfit=PEI_WET)],
    'Medium low shot, the man from the head to the knees, in the middle third of the frame, in the flooded field.',
    "<pei_warlord> crawls out of the split cab of the smashed overturned truck on his hands and knees onto the wet ice, his soaked greatcoat dragging behind him and water streaming from his silver hair, then pushes himself up onto one knee with his eyes burning at the mountain.",
    "裴远山手脚并用地从被撞烂翻倒的装甲车裂开的驾驶室里爬出来，爬到湿冰上，湿透的大衣在身后拖着，水顺着银发往下淌，然后用手撑着地面跪起一条腿，眼睛烧着火望着那座山。",
    Q('A thin howl of wind, the trickle of draining water, labored ragged breathing and the scrape of boots on ice.', '风细细的呼啸、积水退去的潺潺声、吃力粗重的喘息和靴子刮过冰面的声音。'),
    AE("Pale cold dawn light glints on the water streaming from his silver hair and the sodden fur collar while pearly steam drifts from the wrecked truck behind him.",
       "苍白冰冷的晨光在他银发上流下的水和湿透的毛领上闪着，身后被毁的装甲车上飘着珍珠色的蒸汽。"),
    holds='The frame holds the smashed truck, and one person: Pei.',
    cam=follow('Pei', '裴远山', 'he rises onto one knee in the middle third of the frame', '他跪起一条腿、停在画面中间三分之一'))

DL('65-02', '02｜泥水里：裴远山跪着举起对讲机，说您的水淹不死我，说我手里还有一发，说对准您的暖气井', PEI_WRECK,
   [P('pei_warlord', 'center', "kneeling on one knee on the wet ice in profile facing frame-right, the black radio handset raised to his lips in his gloved fist and water dripping from his hair, his head turned toward the mountain", 'obj:the dark mountain slope', "his lips curling in a cold thin smug smile, his eyes burning, his brows level", outfit=PEI_WET)],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the flooded field.',
   [('pei_warlord', "您的水，淹不死我。", 'lin_home', 'cold soft', '冰冷轻柔'),
    ('pei_warlord', "我手里，还有一发。", 'lin_home', 'slow patient', '不紧不慢耐心'),
    ('pei_warlord', "对准您的暖气井。", 'lin_home', 'cold courteous', '冰冷客气')],
   V('A thin howl of wind, the crackle of a radio handset and the trickle of draining water.', '风细细的呼啸、对讲机的沙沙声和积水退去的潺潺声。'),
   AE("Pale cold dawn light glints on the water running from his silver hair and the wet fur collar while pearly steam drifts from the wrecked trucks behind him.",
      "苍白冰冷的晨光在他银发上淌下的水和湿透的毛领上闪着，身后被毁的车辆上飘着珍珠色的蒸汽。"),
   post_en='after the last line he lowers the handset and rises slowly to his feet',
   post_zh='最后一句之后，他放下对讲机，慢慢站起身',
   cam=push1('his face and the raised handset', '他的脸和举着的对讲机'), bg='Behind him the smashed truck and the toppled drilling rig lie in the flooded slush.',
   ld={'lin_home': ('into the black radio handset in his fist', '对着手里黑色的对讲机')}, room={'Pei'})

DL('65-03', '03｜铁笼：周宁蜷在笼角，从湿透的卫衣里掏出一个小对讲机，压低声音说他们还有一发，说对准竖井了，让林峰快躲', CAGE,
   [P('ning_partner', 'center', "crouching in the corner of the iron cage in profile facing frame-left, a small black hand radio pulled from inside his soaked sweatshirt and pressed to his split lips, his head turned toward the guards beyond the bars", 'obj:the dark armoured truck beyond the bars', "his lips trembling around the radio, his eyes wide and red, his brows pulled up", outfit=NING_CAGE)],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the cage.',
   [('ning_partner', "他们还有一发！", 'lin_home', 'hoarse urgent', '嘶哑急切'),
    ('ning_partner', "对准竖井了，快躲！", 'lin_home', 'hoarse breaking', '嘶哑发颤')],
   V('A thin howl of wind, the crackle of a tiny radio and the creak of rusty iron.', '风细细的呼啸、小对讲机的沙沙声和锈铁的吱嘎声。'),
   AE("Pale cold dawn light slants through the iron bars and lays dark stripes across his bruised face while the tiny radio glints in his shaking hand.",
      "苍白冰冷的晨光斜斜地穿过铁栏杆，在他带着淤青的脸上投下一道道暗影，发抖的手里小对讲机闪着光。"),
   post_en='after the last line he pushes the radio back inside his sweatshirt and flattens himself against the floor of the cage',
   post_zh='最后一句之后，他把对讲机塞回卫衣里面，整个人趴平在笼子的地板上',
   cam=push1('his face and the hidden radio', '他的脸和藏着的对讲机'), bg='Behind him the thick rusty bars of the cage fill the frame.',
   ld={'lin_home': ('into a small black hand radio pressed to his lips', '对着贴在嘴边的小黑对讲机')}, room={'Ning'}, mind=6)

DL('65-04', '04｜闸门室：林峰握着手轮往回转着关闸，苏清月在耳机里喊周宁说还有一发，他说我在关，她喊快，他说转了一半', GATE,
   [P('lin_work', 'right', "standing at the gate in profile facing frame-left, both hands gripping the rim of the black iron hand-wheel and turning it back with his arms tensing, his headset earpiece in his right ear, his head turned toward the wheel", 'obj:the black iron hand-wheel', "his jaw clenched, his eyes burning and fixed, his brows low", outfit=LIN_HEAD)],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the gate chamber.',
   [('su_cozy', "周宁说，还有一发！", 'lin_work', 'sharp urgent', '锐利急切'),
    ('lin_work', "我在关闸。", 'su_cozy', 'low labored', '低沉吃力'),
    ('su_cozy', "快！", 'lin_work', 'sharp', '锐利'),
    ('lin_work', "转了一半。", 'su_cozy', 'low labored', '低沉吃力')],
   V('The heavy grinding groan of the iron wheel, a deep low rumble of water behind the gate and the crackle of radio static in an earpiece.', '铁手轮沉重的吱呀碾磨声、闸门后水深沉的低低轰响和耳机里电流的沙沙声。'),
   AE("A single caged work lamp throws a hard white light across his tensing shoulders while a thin warm glow from the brass plate lays a gold edge along his jaw and dust shivers in the beam.",
      "一盏笼式工作灯把硬朗的白光洒在他绷紧的肩膀上，黄铜板一线温暖的光在他的下颌上镀了一道金边，尘埃在光束里发颤。"),
   post_en='after the last line he drives his shoulder into the wheel and it grinds another quarter turn',
   post_zh='最后一句之后，他用肩膀顶着手轮，手轮又吱呀着转了四分之一圈',
   cam=push1('his hands on the wheel', '他握着手轮的手'), bg='Behind him the massive round steel gate door with its black iron hand-wheel fills the back wall of the chamber.',
   ld={'su_cozy': ('into the slim microphone clipped at his jaw', '对着别在下巴边的细细麦克风')})

INS('65-05', '05｜山前雪地：一团白热的橙色火球吞掉了圆形的井口，翻滚着升成一根黑色的烟雪柱，一圈被压平的雪浪向四周的雪原飞快扩散', 8, SIEGE_FIRE,
    'Wide shot of the shaft mouth and the fireball, the rising column in the middle third of the frame, nobody in the scene.',
    "A white-hot orange fireball swallows the round shaft mouth and rolls upward into a dark billowing column of smoke and snow while a ring of flattened snow races outward across the field. Nothing else moves except the blast.",
    "一团白热的橙色火球吞掉了圆形的井口，翻滚着升成一根浓黑的烟雪柱，一圈被压平的雪浪向四周的雪原飞快扩散。除了爆炸以外，别的什么都不动。",
    Q('A single colossal thunderous blast that rolls away, then the long ring of a deep hush.', '一声巨大的雷鸣般的爆炸向远处滚去，然后是一片长长的深深的寂静。'),
    'The frame holds the fireball and the shockwave, and nobody in the scene.',
    rise('the top of the rising column of smoke', '升起的烟柱顶端'),
    AE("The white-orange fireball lights the underside of the dark smoke with a fierce glow, a bright shockwave ring races over the snow and flying ice glitters in the glare.",
       "白橙色的火球把黑烟的底部照得通亮，一圈明亮的冲击波在雪面上飞快扩散，飞起的碎冰在强光里闪烁。"))

DL('65-06', '06｜闸门室：塌方后的黑暗里，林峰扶着手轮站在齐踝深的水里，身后的出口被碎石堵死，他问苏清月听得见吗，她说听得见你在哪，他说通道塌了，她说我来救你', GATE_RUBBLE,
   [P('lin_work', 'right', "standing in the ankle-deep water in profile facing frame-left, one hand braced on the black iron hand-wheel and the other pressed to the earpiece of his headset, dust and small grit falling over his shoulders and hair, his head turned toward the heap of rubble sealing the doorway", 'obj:the heap of broken concrete sealing the doorway', "his jaw tight, his eyes wide and dark with dust, his brows pulled together", outfit=LIN_WET)],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the collapsed gate chamber.',
   [('lin_work', "听得见吗？", 'su_cozy', 'low rough', '低沉沙哑'),
    ('su_cozy', "听得见！你在哪？", 'lin_work', 'sharp breathless', '锐利喘着气'),
    ('lin_work', "通道塌了。", 'su_cozy', 'low grim', '低沉凝重'),
    ('su_cozy', "我来救你！", 'lin_work', 'sharp fierce', '锐利凶狠')],
   V('The falling patter of grit and chips of concrete, the slosh of water around his boots and the crackle of radio static in an earpiece.', '碎石渣和混凝土碎片掉落的噼啪声、水在他靴子边晃动的声音和耳机里电流的沙沙声。'),
   AE("A red emergency strobe pulses through the swirling dust and paints a hard red rim along his wet profile while the flickering work lamp throws white shards of light across the heap of rubble.",
      "一盏红色应急灯在飞舞的尘土里频闪，沿着他湿漉漉的侧脸勾出一道硬朗的红边，忽明忽暗的工作灯把一片片白光洒在碎石堆上。"),
   post_en='after the last line he looks down at his half-turned hand on the wheel and sets his jaw',
   post_zh='最后一句之后，他低头看了一眼放在手轮上转了一半的手，咬紧牙关',
   cam=push1('his face and the earpiece', '他的脸和耳机'), bg='Behind him the massive round steel gate door with its black iron hand-wheel fills the back wall and the doorway at frame-left is sealed by a heap of rubble.',
   ld={'su_cozy': ('into the slim microphone clipped at his jaw', '对着别在下巴边的细细麦克风')})

INS('65-07', '07｜生活区走廊：黑色的洪水从长走廊远端翻涌过来，水位越涨越高，红色应急灯频闪，近端那扇圆形钢舱门紧紧关着', 7, FLOOD_CORR,
    'Wide shot of the corridor, the churning water in the middle third of the frame, nobody in the scene.',
    "Dark churning water pours down the long grey concrete corridor from the far end toward the camera, the level rising steadily, red emergency strobes pulsing along the ceiling and a heavy round steel hatch door standing closed at the near end. Nothing else moves.",
    "黑色的洪水从长长的灰色混凝土走廊远端翻涌着朝镜头涌来，水位一点点上涨，天花板上红色应急灯频闪，近端一扇厚重的圆形钢舱门紧紧关着。别的什么都不动。",
    Q('The thundering roar of rushing water, the metallic ring of a sealed hatch and a pulsing alarm.', '洪水奔涌的雷鸣般的轰响、封死的舱门金属的回响和脉动的警报。'),
    'The frame holds the flooded corridor and the hatch door, and nobody in the scene.',
    follow('the front of the flood', '洪水的前锋', 'the dark water reaches the hatch door at the near end', '黑色的水涌到近端的舱门'),
    AE("Red emergency strobes flash across the churning black water and turn the foam crimson while a few drifting sparks of light skip along the wet concrete.",
       "红色应急灯的频闪掠过翻涌的黑水，把白沫染成深红，几点飘飞的光斑沿着湿漉漉的混凝土跳动。"))

DL('65-08', '08｜控制室：伊甸报告洪水已改道正涌向生活区，苏清月问多久，伊甸说九分钟，她说他还在闸门室', CONTROL_C,
   [P('su_cozy', 'center', "standing up from the black swivel chair at the control console in profile facing frame-right, both hands flat on the console and the headset on her head, her head lifted toward the wall speaker", 'obj:the wall speaker above the console', "her lips parting in horror, her eyes wide and wet, her brows pulled together", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('eden_voice', "洪水改道，正涌向生活区。", 'su_cozy', 'soft urgent', '轻柔急切'),
    ('su_cozy', "多久？", 'eden_voice', 'sharp quick', '锐利急促'),
    ('eden_voice', "九分钟。", 'su_cozy', 'soft calm', '轻柔平静'),
    ('su_cozy', "他还在闸门室。", 'eden_voice', 'low breaking', '低沉发颤')],
   V('A sharp rising electronic alarm, the hum of the console and a quick breath.', '一声尖锐渐强的电子警报、控制台的嗡鸣和一声急促的呼吸。'),
   AE("A pulsing red glow floods the console and paints a hard red rim along her profile while the thin blue ring of the wall speaker glows above her.",
      "一阵脉动的红光洒满控制台，在她的侧脸勾出一道硬朗的红边，头顶墙上扬声器那圈细细的蓝光亮着。"),
   post_en='after the last line she grips the edge of the console until her knuckles whiten',
   post_zh='最后一句之后，她攥紧控制台的边缘，指节发白',
   cam=push1('her face and the red glow', '她的脸和红光'), bg='On the wall above the console a flat speaker panel with a thin glowing blue ring glows.',
   room={'Su'})

# ================================================================================================ 第 66 集（A）
b66 = S.episode('剧本第66集｜手轮', '伊甸说通道塌方已无法进入、所有路径都封死了，苏清月说那就炸开；闸门室里林峰说手轮还在他这一侧，苏清月说不准关，他说关了水就进不了生活区；控制室里她说不准关我来想办法，他说没时间了，她说你答应过我，他说外科医生只做最后一刀；他握着手轮，左手手指只能合一半；他说遇见你是我最好的决定，她说闭嘴我来接你，他说好好吃饭别熬夜，她说我不要听；他用尽全身力气转动了手轮。', 66)

DL('66-01', '01｜控制室：伊甸说通道塌方已无法进入，苏清月说那就绕路，伊甸说所有路径均已封死，她说我炸开它', CONTROL_C,
   [P('su_cozy', 'center', "standing at the control console in profile facing frame-right, both fists on the console and the headset on her head, her head lifted toward the wall speaker", 'obj:the wall speaker above the console', "her jaw clenched, her eyes wet and furious, her brows low", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('eden_voice', "通道塌方，已无法进入。", 'su_cozy', 'soft calm', '轻柔平静'),
    ('su_cozy', "那就绕路。", 'eden_voice', 'sharp quick', '锐利急促'),
    ('eden_voice', "所有路径，均已封死。", 'su_cozy', 'soft calm', '轻柔平静'),
    ('su_cozy', "那我炸开它。", 'eden_voice', 'low fierce', '低沉凶狠')],
   V('A sharp rising electronic alarm, the hum of the console and the dull thud of a fist on metal.', '一声尖锐渐强的电子警报、控制台的嗡鸣和拳头砸在金属上的闷响。'),
   AE("A pulsing red glow floods the console and paints a hard red rim along her wet cheek while cool green status lights flicker at the edge of the frame.",
      "一阵脉动的红光洒满控制台，在她湿润的脸颊上勾出一道硬朗的红边，画面边缘冷冷的绿色指示灯闪动。"),
   post_en='after the last line she slams her fist onto the console and the small status lights jump',
   post_zh='最后一句之后，她一拳砸在控制台上，小小的指示灯跳了一下',
   cam=push1('her face and the red glow', '她的脸和红光'), bg='On the wall above the console a flat speaker panel with a thin glowing blue ring glows.',
   room={'Su'})

INS('66-02', '02｜闸门室：塌方后的小房间里，红色应急灯频闪，齐踝深的黑水慢慢涨高，黑铁手轮停在转了一半的位置，旁边墙上的黄铜板泛着暗光', 7, GATE_RUBBLE,
    'Medium shot of the wheel and the water, the wheel in the middle third of the frame, nobody in the scene.',
    "In the collapsed chamber dark water creeps higher around the base of the big black iron hand-wheel stopped halfway through its turn, the brass plate glinting dully in the wall and a heap of rubble sealing the doorway. Nothing else moves.",
    "塌方后的小房间里，黑色的水慢慢漫高，围着转到一半停住的黑铁大手轮，墙上的黄铜板泛着暗光，门口被一堆碎石堵死。别的什么都不动。",
    Q('The slow rising slosh of dark water, a pulsing alarm far away and the drip of dust from the ceiling.', '黑水缓缓上涨的晃动声、远处脉动的警报和天花板上掉落的尘土滴答声。'),
    'The frame holds the hand-wheel and the rising water, and nobody in the scene.',
    push1('the half-turned wheel', '转了一半的手轮'),
    AE("A red emergency strobe pulses over the black water and flashes on the worn rim of the wheel while the flickering work lamp throws white shards of light and dust glitters in the beam.",
       "红色应急灯的频闪掠过黑水，在手轮磨旧的边缘上一闪一闪，忽明忽暗的工作灯投下一片片白光，尘埃在光束里闪烁。"))

DL('66-03', '03｜闸门室：林峰靠在手轮上说手轮卡在他这一侧，苏清月在耳机里喊不准关，他说关了水就进不了生活区，她喊我不准', GATE_RUBBLE,
   [P('lin_work', 'right', "standing in the ankle-deep water in profile facing frame-left, one hand braced on the black iron hand-wheel and the other pressed to the earpiece of his headset, dust falling over his shoulders, his head turned toward the rubble", 'obj:the heap of broken concrete sealing the doorway', "his jaw set, his eyes dark and steady, his brows low", outfit=LIN_WET)],
   'Medium shot, the man from the head to the knees, in the middle third of the frame, in the collapsed gate chamber.',
   [('lin_work', "手轮还卡在这一边。", 'su_cozy', 'low steady', '低沉平稳'),
    ('su_cozy', "不准关！", 'lin_work', 'sharp breaking', '锐利发颤'),
    ('lin_work', "关了，水就进不了生活区。", 'su_cozy', 'low calm', '低沉平静'),
    ('su_cozy', "我不准！", 'lin_work', 'sharp breaking', '锐利发颤')],
   V('The slosh of water around his boots, the faint patter of grit and the crackle of radio static in an earpiece.', '水在他靴子边晃动的声音、碎石渣细细的噼啪声和耳机里电流的沙沙声。'),
   AE("A red emergency strobe pulses through the dust and paints a hard red rim along his wet profile while the flickering work lamp throws white shards of light across the water.",
      "一盏红色应急灯在尘土里频闪，沿着他湿漉漉的侧脸勾出一道硬朗的红边，忽明忽暗的工作灯把一片片白光洒在水面上。"),
   post_en='after the last line he closes his eyes for one slow breath and opens them again',
   post_zh='最后一句之后，他闭上眼睛缓缓呼吸了一次，又睁开',
   cam=push1('his face and the earpiece', '他的脸和耳机'), bg='Behind him the massive round steel gate door with its black iron hand-wheel fills the back wall and the doorway at frame-left is sealed by a heap of rubble.',
   ld={'su_cozy': ('into the slim microphone clipped at his jaw', '对着别在下巴边的细细麦克风')})

DL('66-04', '04｜控制室：苏清月双手撑着控制台说不准关我来想办法，耳机里林峰说没时间了，她说你答应过我，他说外科医生只做最后一刀', CONTROL_C,
   [P('su_cozy', 'center', "standing at the control console in profile facing frame-right, both hands pressed flat on the console and the headset on her head, her head bowed toward the console speaker", 'obj:the console speaker', "her lips trembling and pressed together, her eyes streaming, her brows pulled up", outfit=SU_HEADSET)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the console.',
   [('su_cozy', "不准关，我来想办法！", 'lin_work', 'sharp breaking', '锐利发颤'),
    ('lin_work', "没时间了。", 'su_cozy', 'low gentle', '低沉温柔'),
    ('su_cozy', "你答应过我！", 'lin_work', 'sharp breaking', '锐利发颤'),
    ('lin_work', "外科医生，只做最后一刀。", 'su_cozy', 'low steady', '低沉平稳')],
   V('The faint crackle of radio static in an earpiece, a pulsing alarm and a shaky breath.', '耳机里电流细细的沙沙声、脉动的警报和一声发颤的呼吸。'),
   AE("A pulsing red glow rims her wet cheek and the black headset while cool green status lights flicker at the edge of the frame and a single tear catches the light.",
      "一阵脉动的红光勾着她湿润的脸颊和黑色耳机，画面边缘冷冷的绿色指示灯闪动，一滴眼泪在光里闪了一下。"),
   post_en='after the last line she presses her trembling fingers hard against the headset earpiece and her shoulders shake',
   post_zh='最后一句之后，她用发抖的手指用力按住耳机的耳罩，肩膀在颤抖',
   cam=push1('her face and the headset', '她的脸和耳机'), bg='Behind her the wall of small monitors glows and a small red alarm lamp flashes.',
   room={'Su'}, tail=2.5)

INS('66-05', '05｜闸门室：两只手握着黑铁手轮的边缘，右手握得很紧，左手的五根手指只能蜷到一半，黑水慢慢漫上手轮的底座', 6, GATE_HANDS,
    'Close shot of the hands on the wheel, the hands in the middle third of the frame, nobody else in the scene.',
    "Two hands grip the rim of the big black iron hand-wheel, the right hand clamped tight and the left hand's five fingers curling only halfway around the rim and trembling, dark water creeping up around the base of the wheel. Nothing else moves.",
    "两只手握着黑铁大手轮的边缘，右手握得很紧，左手的五根手指只能蜷到一半，在微微发抖，黑色的水慢慢漫上手轮的底座。别的什么都不动。",
    Q('The slow slosh of dark water, a pulsing alarm far away and a labored breath.', '黑水缓缓晃动的声音、远处脉动的警报和一声吃力的呼吸。'),
    'The frame holds the hands on the wheel, and nobody else in the scene.',
    push1('the half-curled left hand', '只蜷了一半的左手'),
    AE("A red emergency strobe flashes over the wet iron and the pale knuckles while the flickering work lamp throws a white edge along the rim and the black water glitters.",
       "红色应急灯的频闪掠过湿漉漉的铁和苍白的指关节，忽明忽暗的工作灯沿着轮缘投下一道白边，黑色的水面闪闪发亮。"))

DL('66-06', '06｜闸门室：林峰握着手轮对苏清月说遇见你是我最好的决定，她在耳机里喊闭嘴我来接你，他说好好吃饭别熬夜，她说我不要听', GATE_RUBBLE,
   [P('lin_work', 'right', "standing in the knee-deep water in profile facing frame-left, both hands on the rim of the black iron hand-wheel and the earpiece of his headset in his right ear, his head bowed toward the wheel", 'obj:the black iron hand-wheel', "his lips easing into a faint tender sweet smile, his eyes wet and calm, his brows soft", outfit=LIN_WET)],
   'Medium close shot, the man from the head to the chest, in the middle third of the frame, in the collapsed gate chamber.',
   [('lin_work', "遇见你，是我最好的决定。", 'su_cozy', 'low gentle', '低沉温柔'),
    ('su_cozy', "闭嘴！我来接你！", 'lin_work', 'sharp breaking', '锐利发颤'),
    ('lin_work', "好好吃饭，别熬夜。", 'su_cozy', 'low soft', '低沉轻柔'),
    ('su_cozy', "我不要听！", 'lin_work', 'sharp sobbing', '锐利带着哭腔')],
   V('The slow slosh of water around his chest, the faint crackle of radio static in an earpiece and a shaky breath.', '水在他胸前缓缓晃动的声音、耳机里电流细细的沙沙声和一声发颤的呼吸。'),
   AE("A red emergency strobe pulses through the thin dust and lays a crimson rim on his wet cheek while a thin warm gold from the brass plate glows along his pressed hand.",
      "红色应急灯的频闪穿过薄薄的尘土，在他湿润的脸颊上勾出一圈深红色的边，黄铜板一线温暖的金光落在他按着的手上。"),
   post_en='after the last line he lifts his eyes slowly to the heavy gate and tightens both hands around the wheel',
   post_zh='最后一句之后，他慢慢抬起眼睛望向那扇厚重的闸门，两只手握紧了手轮',
   cam=push1('his face and the earpiece', '他的脸和耳机'), bg='Behind him the massive round steel gate door with its black iron hand-wheel fills the back wall of the chamber.',
   ld={'su_cozy': ('into the slim microphone clipped at his jaw', '对着别在下巴边的细细麦克风')}, tail=2.5)

TAA('66-07', '07｜闸门室：林峰咬紧牙，用尽全身力气转动手轮，额头青筋暴起，手轮在他手里一点一点吱呀着转动，水漫到他的腰', 7, GATE_RUBBLE,
    [P('lin_work', 'right', "standing waist-deep in black water in profile facing frame-left, both hands on the rim of the black iron hand-wheel and every muscle in his arms and shoulders tensing as he drives it round, his head bowed toward the wheel", 'obj:the black iron hand-wheel', "his teeth clenched, his eyes squeezed half shut and burning, his brows low", outfit=LIN_WET)],
    'Medium shot, the man from the head to the waist, in the middle third of the frame, in the collapsed gate chamber.',
    "<lin_work> drives the heavy black iron hand-wheel round with both hands and every muscle tensing, his veins standing out on his forehead, the wheel grinding round little by little and the dark water rising to his waist around him.",
    "林峰用两只手拼命转动沉重的黑铁手轮，全身的肌肉都绷紧，额头上青筋暴起，手轮一点一点吱呀着转动，黑色的水在他周围涨到腰际。",
    Q('The heavy grinding groan of the iron wheel, the roar of rising water and a ragged labored breathing.', '铁手轮沉重的吱呀碾磨声、上涨的水的轰响和吃力粗重的喘息。'),
    AE("A red emergency strobe flashes across the black water and the wet iron of the wheel and paints a hard crimson rim along his tensing shoulders while white shards of flickering work-lamp light glitter on the rising surface.",
       "红色应急灯的频闪掠过黑色的水面和湿漉漉的铁手轮，在他绷紧的肩上勾出一道硬朗的深红边，忽明忽暗的工作灯的白光碎片在上涨的水面上闪烁。"),
    holds='The frame holds the wheel, and one person: Lin.',
    cam=push1('his tensing face and the wheel', '他绷紧的脸和手轮'))

report()
doc = S.finish()
