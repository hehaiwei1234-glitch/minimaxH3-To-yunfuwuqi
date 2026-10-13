#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 9–12 集，追加稿 006（2026-10-13 夜）。必须接在 005（剧本第 5–8 集）之后追加（以 005 的 JSON 为底，
style／素材／角色逐字复制）；hh 挂机跑的是最后合并出来的那一份（008），不单独贴它。

写法＝004／005 同一套（一个任务一件慢的事；每人看着谁写进开场图；每句台词对谁说且对象在画面里；独白＝一个人在画面里、手上有事、眼睛看着一个具体物件；
3 秒无人插镜；承接前段只在同场景同一批人的相邻任务打开；运镜写“动作＋终点”）。
本稿里直接测的写法：
  · 09-02（11 秒）苏清月对着树桩上的镜头玻璃说三句（等于对着“画面里的一个物件”说话，嘴动、人倒下为结尾动作）；
  · 10-01…10-05 手术一场：两人坐着、一人咬毛巾，没台词的两个任务（10-02 切、10-03 缝）只写慢而细的手上动作；10-04、10-05 各三句；
  · 12-06（12 秒）三句台词＋林峰走出画面（结尾动作）；12-03 手里有事的两人对话（移栽）；
  · 11 集、12 集的“养成链”：水（水泵出水）→光（地下二层亮灯）→苗（移栽）→鸡（孵化箱）。
偏离大纲（交稿时已告诉 hh）：
  · 原大纲第 8、9 集合并成剧本第 9 集：投名状＋入舱＋喝汤；入舱时苏清月被滑道滑进缓冲舱的过程不拍，只拍滑道口（插镜）和她在沙发上醒来；
    消毒舱、除颤都不拍；监控里的脸用“监控屏幕里那张脸”（屏幕套屏幕，H3 风险）；
  · 原大纲第 10 集手术：不拍血肉和刀口，只拍“她低头做细活、他咬毛巾瞪着她”的两人中景；不写“切断你的手筋”以外的威胁；契约文件不写标题字；
  · 第 11 集：苏清月洗澡只拍“蒸汽和玻璃门”的无人插镜（不拍人影）；壁炉改成圆桌上的热红酒（安全屋生活区没有壁炉）；
  · 第 12 集：小鸡只拍孵化箱的无人插镜（不拍破壳过程）；隔音海绵只拍“林峰按住海绵板”；冷库只拍选底料，不拍囤货全景。
H3 方面的风险（交稿时单列，不算我的错）：监控屏幕里的人脸（屏幕套屏幕）；苏清月对着树桩玻璃说话时的视线（会不会看向镜头）；手术一场两人贴得很近、手部动作、
  咬着毛巾的嘴；热红酒的杯子碰杯；鸡（动物第一次出现）；透明水管里的水流；开场图约一成不按文字画；“同一处”场景用参照图（没测过）。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _jihan_base2 import *

OUT = '合并稿/006_第9-12集_投名状手术契约白噪音伊甸园_制作稿_追加'
S = Session('合并稿/005_第5-8集_最后一天降临白雪呼吸求生_制作稿_追加.json', OUT, 35000)

# ---------------------------------------------------------------------------------------------- 新外貌
look('lin_white', 'LinWhite', "in a clean white dress shirt with the sleeves rolled to his forearms and dark trousers, his black hair neatly combed", 'steady dark-brown', 'his', eth=CN30)
look('su_cozy', 'SuCozy', "in an oversized soft cream knit sweater and black thermal leggings, thick grey socks, her long black hair loose over her shoulders", 'soft dark-brown', 'her', eth=CN_F28)
look('su_surgeon', 'SuSurgeon', "in a fitted black long-sleeve thermal top and dark trousers, white surgical gloves, thin gold-rimmed glasses on her nose, her long black hair pinned in a tight bun", 'focused dark-brown', 'her', eth=CN_F28)

# ---------------------------------------------------------------------------------------------- 新场景
SOFA = Scene('bunker_sofa', " Warm amber light from soft recessed lamps fills the cozy underground living area.",
             " Fixed stage layout: a deep brown leather sofa with a thick grey cashmere blanket stands in the middle of the frame facing the room, with a low wooden coffee table in front of it; the open kitchen with the black-and-gold stove is at frame-left; a wall of small security monitors is at center-right behind the sofa; the heavy round steel hatch door is in the right wall at far frame-right.")
MED = Scene('med_room', " Hard white light from a round surgical lamp falls on the small windowless medical room.",
            " Fixed stage layout: a steel operating table covered with a sterile blue drape stands in the middle of the frame under a round surgical lamp; a steel instrument tray with an open silver metal case stands at frame-left; a plain steel chair stands at frame-right; the white-tiled walls fill the background.")
EDENDOOR = Scene('eden_door', " Cool concrete-corridor light with a thin glow of pink-violet leaking through the gap around the door.",
                 " Fixed stage layout: the bare concrete corridor fills the frame; a heavy steel door with a keypad stands at frame-right with a thin line of pink-violet light glowing around its edges.")
PUMP = Scene('pump_room', " Hard white work-lamp light falls on the damp compact concrete pump room.",
             " Fixed stage layout: a huge clear acrylic water tank stands at frame-right; thick transparent pipes run along the left wall to a steel pump station; a control panel with one big green start button stands in the middle of the frame; the floor is damp with a drain.")
BATH = Scene('bathroom', " Warm soft light and thick white steam fill the tiled bathroom.",
             " Fixed stage layout: a frosted-glass shower door with a rainfall shower head behind it stands at frame-center-left; a wooden bench with folded white towels and a folded grey cotton shirt stands at frame-right; the wall is white tile.")
EDEN = Scene('eden', " Rows of pink-violet full-spectrum grow lamps bathe the vast underground farm level in a dreamy glow.",
             " Fixed stage layout: long tiers of white hydroponic channels full of young lettuce and tomato seedlings fill the middle of the frame under rows of hanging pink-violet grow lamps; a warm incubator box with a glass window and a red heat lamp stands at frame-right; a steel staircase rises at frame-left; the concrete walls fill the background.")
COLD = Scene('cold_store', " Frosty cold white light falls on the walk-in cold store.",
             " Fixed stage layout: steel shelving stacked with white boxes of frozen meat, seafood and vegetables fills the left and middle of the frame; a shelf at eye level holds brightly packaged hotpot base boxes in the middle; a heavy insulated door stands at frame-right.")
CHUTE = Scene('snow_stump', " A silent frozen forest under a black sky with a faint green aurora; the white light of the snow glows.",
              " Fixed stage layout: a snow-capped boulder is at frame-left; a dead tree stump with a small round dark glass lens in its side stands at center-left; in the snow in front of the stump a long smooth dark chute slopes down into the ground; snow-laden pines stand in the background.")

# ---------------------------------------------------------------------------------------------- 第 9 集（先建第一个 Batch，新素材都加在它上面）
b9 = S.episode('剧本第9集｜投名状', '安全屋里，林峰在监控里看到苏清月冻僵的脸，一直没有开门；雪地里她把装着抗生素和手术刀的金属盒举向树桩上的镜头，说“你总有一天会生病的”，倒了下去。林峰看着自己发黑的手背，按下红色按钮——雪地裂开一道滑道。苏清月在安全屋的沙发上醒来，二十五度，她说“我还活着？”林峰端来一碗番茄排骨汤：“欢迎来到世界末日。”她大口喝汤，看到他发黑的左手，放下碗：“再不切，你今晚就败血症。”', 9)

new_person(b9, 'lin_white', '林峰（干净的白衬衫，袖子卷到小臂，深色长裤）', 'man',
           'Lin, the same lean, athletic Chinese man in his early thirties as in the reference, with short neatly combed black hair, wearing a clean white dress shirt with the sleeves rolled to his forearms and dark trousers.',
           '林峰，和参考图是同一位三十出头、身形精瘦结实的中国男性，黑色短发梳得整齐，穿着干净的白衬衫、袖子卷到小臂，深色长裤。',
           'short neatly combed black hair, wearing a clean white dress shirt with the sleeves rolled to his forearms and dark trousers',
           'a calm, level expression', ref='lin_studio')
new_person(b9, 'su_cozy', '苏清月（宽大的奶白色针织毛衣，黑色保暖打底裤，灰色厚袜子，长发披着）', 'woman',
           'Su, the same elegant Chinese woman in her late twenties as in the reference but without glasses, wearing an oversized soft cream knit sweater, black thermal leggings and thick grey socks, her long black hair loose over her shoulders.',
           '苏清月，和参考图是同一位二十八岁左右、优雅美丽的中国女性，但不戴眼镜，穿着宽大柔软的奶白色针织毛衣、黑色保暖打底裤和灰色厚袜子，乌黑的长发披在肩上。',
           'no glasses, wearing an oversized soft cream knit sweater, black thermal leggings, thick grey socks, long black hair loose over her shoulders',
           'a soft, tired expression', ref='su_suit', full=True)
new_person(b9, 'su_surgeon', '苏清月（黑色贴身长袖打底衫，白色手术手套，金丝眼镜，头发盘成紧紧的发髻）', 'woman',
           'Su, the same elegant Chinese woman in her late twenties as in the reference, with her long black hair pinned in a tight bun and thin gold-rimmed glasses on her nose, wearing a fitted black long-sleeve thermal top, dark trousers and white surgical gloves.',
           '苏清月，和参考图是同一位二十八岁左右、优雅美丽的中国女性，乌黑的长发盘成紧紧的发髻，鼻梁上架着细金丝眼镜，穿着贴身的黑色长袖打底衫、深色长裤，戴着白色手术手套。',
           'long black hair pinned in a tight bun, thin gold-rimmed glasses, wearing a fitted black long-sleeve thermal top, dark trousers and white surgical gloves',
           'a focused, professional expression', ref='su_suit')

new_scene(b9, 'bunker_sofa', '安全屋生活区的沙发角（深棕皮沙发，灰色羊绒毯，矮木茶几）', 'The same cozy underground living area as in the reference image, now showing its sofa corner: a deep brown leather sofa with a thick grey cashmere blanket in the middle of the frame facing the room, a low wooden coffee table in front of it, the open kitchen with the black-and-gold stove at the left, a wall of small security monitors at the center-right behind the sofa, the heavy round steel hatch door in the right wall, warm amber light from soft recessed lamps.',
          '和参考图是同一个温馨的地下生活区，现在拍的是沙发角：画面中间一张朝着房间的深棕色皮沙发、上面铺着厚厚的灰色羊绒毯，前面是一张矮矮的木茶几，左边是开放式厨房和黑金色炉灶，沙发后面中右是一整面小监控屏墙，右墙是厚重的圆形钢制舱门，柔和的嵌灯投下暖琥珀色的光。',
          'the leather sofa with the cashmere blanket, the coffee table, the kitchen, the monitor wall and the hatch')
new_scene(b9, 'med_room', '地下室里的简易手术室（手术无影灯，钢手术台铺着蓝色无菌布，银色金属盒）', 'A small windowless underground medical room with white-tiled walls: a steel operating table covered with a sterile blue drape in the middle under a round surgical lamp, a steel instrument tray with an open silver metal case at the left, a plain steel chair at the right, hard white light.',
          '地下一间没有窗的小手术室，墙面是白瓷砖：中间是一张铺着蓝色无菌布的钢制手术台，上方是一盏圆形手术无影灯，左边是一个钢制器械托盘、上面放着打开的银色金属盒，右边是一把朴素的钢椅，白色的硬质灯光。',
          'the operating table with the blue drape, the surgical lamp, the instrument tray and the steel chair')
new_scene(b9, 'eden_door', '混凝土走廊尽头的钢门（门缝里透出粉紫色的光，门旁有密码键盘）', 'A bare underground concrete corridor ending at a heavy steel door with a keypad on the right, a thin line of pink-violet light glowing around the edges of the door, cool concrete light.',
          '地下光秃秃的混凝土走廊，尽头右边是一扇装着密码键盘的厚重钢门，门缘周围透出一圈细细的粉紫色的光，冷色的混凝土灯光。',
          'the concrete corridor, the steel door with the keypad and the pink-violet glow around its edges')
new_scene(b9, 'pump_room', '水泵房（透明大水箱，透明水管，绿色启动键）', 'A compact damp underground concrete pump room: a huge clear acrylic water tank at the right, thick transparent pipes running along the left wall to a steel pump station, a control panel with one big green start button in the middle, a damp floor with a drain, hard white work-lamp light.',
          '地下潮湿紧凑的混凝土水泵房：右边是一个巨大的透明亚克力水箱，左墙上是一排粗粗的透明水管、通向钢制泵站，中间是一块控制面板、上面一个大大的绿色启动键，地面潮湿、有地漏，白色的硬质工作灯光。',
          'the clear tank, the transparent pipes, the pump station and the control panel with the green button')
new_scene(b9, 'bathroom', '浴室（磨砂玻璃淋浴门，木凳上叠着毛巾和一件灰色棉质长袖衫，蒸汽）', 'A warm tiled underground bathroom: a frosted-glass shower door with a rainfall shower head behind it at center-left, a wooden bench with folded white towels and a folded grey cotton shirt at the right, white tile walls, thick white steam.',
          '地下温暖的瓷砖浴室：中左是一扇磨砂玻璃淋浴门、门后是顶喷花洒，右边是一张木凳、上面叠着白毛巾和一件灰色棉质长袖衫，墙面是白瓷砖，到处是浓浓的白色蒸汽。',
          'the frosted shower door, the bench with the towels and the grey shirt, and the steam')
new_scene(b9, 'eden', '地下二层的“伊甸园”（一排排粉紫色生长灯下的水培架，孵化箱）', 'A vast underground farm level: long tiers of white hydroponic channels full of young lettuce and tomato seedlings under rows of hanging pink-violet full-spectrum grow lamps filling the middle of the frame, a warm incubator box with a glass window and a red heat lamp at the right, a steel staircase at the left, concrete walls.',
          '地下巨大的农场层：画面中间是一排排长长的白色水培槽，里面长着嫩嫩的生菜和番茄苗，头顶吊着一排排粉紫色的全光谱生长灯，右边是一个带玻璃窗和红色保温灯的孵化箱，左边是一道钢楼梯，周围是混凝土墙。',
          'the hydroponic channels with seedlings, the pink-violet grow lamps, the incubator box and the steel staircase')
new_scene(b9, 'cold_store', '冷库（成排的钢货架，火锅底料盒，厚重的保温门）', 'A walk-in underground cold store: steel shelving stacked with white boxes of frozen meat, seafood and vegetables filling the left and middle of the frame, an eye-level shelf with brightly packaged hotpot base boxes in the middle, a heavy insulated door at the right, frosty cold white light.',
          '地下的大型冷库：左边和中间是成排的钢货架、上面堆着一箱箱白色的冷冻肉、海鲜和蔬菜，中间一层与视线齐平的货架上摆着包装鲜艳的火锅底料盒，右边是一扇厚重的保温门，冷冷的白色灯光。',
          'the shelves of white boxes, the hotpot base boxes at eye level and the insulated door')
for _a in b9.d['assets']:
    if _a['key'] == 'bunker_sofa': _a['generate']['reference_keys'] = ['bunker_living']

# ---------------------------------------------------------------------------------------------- 声音
b9.character('LinWhite', 'lin_white', LIN_EN, LIN_ZH)
b9.character('SuCozy', 'su_cozy', SU_EN, SU_ZH)
b9.character('SuSurgeon', 'su_surgeon', SU_EN, SU_ZH)


def insert_task(tid, title, dur, scene, framing, act_en, zh, snd, holds, cam, bg=''):
    return S.T(tid, title, dur, scene, [], framing, act_en, zh, snd, cam=cam, holds=holds, room=set(), new=True, bg=bg)


SOUND_MED = voiced('The faint hum of the surgical lamp, the soft clink of steel instruments and slow breathing.', '手术灯轻微的嗡鸣、钢器械轻轻的碰撞声和缓慢的呼吸声。')
SOUND_BUNKER = voiced('The faint hum of the air system and the low murmur of a generator far away.', '空气系统轻微的嗡鸣和远处发电机低低的运转声。')

# ---------------------------------------------------------------------------------------------- 第 9 集
S.T('09-01', '01｜控制室：监控里是苏清月冻僵的脸，林峰低声念出她的名字', 9, CONTROL,
    [P('lin_home', 'center', "standing before the wall of monitors in profile facing frame-left, a screwdriver in his right hand and his left hand wrapped in white gauze held against his chest", 'obj:the biggest monitor at frame-left showing the frost-covered face of a young woman in a ski hat and goggles', "his jaw set, his lips pressed flat, his brows drawn low")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the control room.',
    "<lin_home> stands alone before the monitor wall with his eyes on the biggest monitor where a frost-covered woman's face lies frozen on the screen with her eyes shut, then murmurs one line to himself in a low voice, talking to nobody, his lips moving softly, then a second short line, his jaw set and his brows drawn low, and turns the screwdriver once in his fingers. Nobody else is in the room.",
    "林峰一个人站在监控墙前，眼睛盯着最大的那块屏幕——屏幕里是一张覆满冰霜的女人的脸，正仰望着镜头，然后他低声自言自语了一句，不是对任何人说的，嘴唇轻轻动着，接着又是一句很短的，下颌绷紧、眉头压低，手里的螺丝刀在指间转了一下。房间里没有别人。",
    voiced('A low electric hum from the console, a faint alarm beep and his low murmur.', '控制台低低的电流嗡鸣、一声轻轻的警报哔声和他低低的自语。'),
    vo=[('lin_home', "苏清月……", 2.0, 'Lin'), ('lin_home', "她真的来了。", 4.6, 'Lin')], cam=push1('Lin and the monitor', '林峰和监控屏幕'),
    bg='At frame-left the biggest of the six small monitors shows the frost-covered face of a young woman in a ski hat and goggles; the red digital clock hangs on the back wall.',
    holds='The frame holds Lin alone before the monitor wall, the console and the steel door.', room={'Lin'}, new=True,
    st={'Lin': ('灰色棉质家居服，左手缠着白纱布，手里拿着螺丝刀', '灰色棉质家居服，左手缠着白纱布')})

S.T('09-02', '02｜雪地树桩前：苏清月把金属盒举向镜头，说你总有一天会生病的，倒进雪里', 11, STUMP,
    [P('su_trek', 'center', "kneeling in the snow in profile facing frame-left in front of the dead stump, holding an open silver metal case up in both hands toward the small round glass lens on the stump, her face blue-white with cold", 'obj:the small round glass lens set in the side of the stump', "her lips cracked and trembling, her brows drawn tight")],
    'Medium shot, the figure from the head to the knees at the center, with the stump at the left of the middle third of the frame, on the snowy hillside.',
    "<su_trek> kneels before the stump and lifts the open silver case toward the small glass lens, her eyes locked on the glass, and speaks the first line up toward the lens as if to herself, nobody else in the frame, her lips cracked and trembling, then the second line in a cracking voice, her brows drawn tight, then a whispered third word, and her eyes close and she sags slowly forward into the snow. Nobody else is on the hillside.",
    "苏清月跪在树桩前，把打开的银色金属盒举向那块小小的玻璃镜头，眼睛死死盯着玻璃，朝着镜头说出第一句，像是自言自语，画面里没有别人，嘴唇干裂发抖；接着用快要裂开的声音说出第二句，眉头紧蹙；然后低低吐出第三个词，眼睛闭上，慢慢向前倒进雪里。山坡上没有别人。",
    voiced('A thin steady wind over the snow, her ragged breathing and her hoarse voice.', '风吹过雪地细细而持续的声音、她粗重的喘息和她嘶哑的声音。'),
    vo=[('su_trek', "我是主刀医生。", 0.9, 'Su'), ('su_trek', "你总有一天，会生病的。", 3.6, 'Su'), ('su_trek', "开门……", 7.0, 'Su')], cam=push1('Su and the stump', '苏清月和树桩'),
    bg='The dead stump with the small round dark glass lens stands at center-left, the snow-capped boulder at frame-left, and a faint green aurora hangs in the black sky.',
    holds='The frame holds Su alone kneeling before the stump with the glass lens.', room={'Su'}, new=True,
    st={'Su': ('三层羽绒服，背着登山包，护目镜推在额头上', '三层羽绒服，倒在雪里')})

S.T('09-03', '03｜控制室：林峰缠着纱布看着自己发黑的手，低声说她倒下了，按下红色按钮', 11, CONTROL,
    [P('lin_home', 'center', "standing at the steel console in profile facing frame-right, slowly unwinding the stained gauze from the back of his left hand with his right hand, the skin beneath dark and swollen", 'obj:the dark swollen back of his own left hand', "his jaw clenched, his lips pressed in a hard line, his brows low")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, at the console.',
    "<lin_home> unwinds the stained gauze from his left hand, his eyes on the dark swollen skin, then murmurs one line to himself in a low voice, talking to nobody, his lips moving softly, then a second short line, his jaw clenched and his brows low, and presses the big red button under its open cover with his right thumb. Nobody else is in the room.",
    "林峰一圈一圈解开左手上沾着污渍的纱布，眼睛盯着下面发黑肿胀的皮肤，然后低声自言自语了一句，不是对任何人说的，嘴唇轻轻动着，接着又是一句很短的，下颌咬紧、眉头压低，然后用右手拇指按下了保护盖下那个大红色按钮。房间里没有别人。",
    voiced('A low electric hum from the console, the soft rasp of gauze and his low murmur.', '控制台低低的电流嗡鸣、纱布轻轻的摩擦声和他低低的自语。'),
    vo=[('lin_home', "她倒下了。", 1.6, 'Lin'), ('lin_home', "我的手，也等不起。", 4.0, 'Lin')], cam=push1('Lin and his hand', '林峰和他的手'),
    bg='High on the back wall behind him the large red digital clock glows, and the wall of small monitors stands at frame-left.',
    holds='The frame holds Lin alone at the console, the red button and the monitors.', room={'Lin'}, new=True,
    st={'Lin': ('灰色棉质家居服，左手缠着白纱布', '灰色棉质家居服，纱布解开，手背发黑')})

insert_task('09-04', '04｜插镜：雪地裂开了一道光滑的黑色滑道，口边落着一圈新雪', 4, CHUTE,
    'Wide establishing shot of the snowy hillside, the stump and the chute in the middle third of the frame, nobody in the scene.',
    "In the snow in front of the stump a long smooth dark chute now slopes down into the ground with a small drift of fresh powder at its lip, and a faint wind moves the snow across the slope. Nothing else moves.",
    "雪地里，树桩前面裂开了一道光滑的黑色滑道、斜斜通向地下，滑道口边有一小圈新落下的雪粉，微风把雪从坡上吹过。别的什么都不动。",
    breathy('A low mechanical rumble fading away and the wind blowing snow across the slope.', '低沉的机械隆隆声渐渐远去，风把雪吹过山坡。'),
    'The frame holds the dead stump with the glass lens, the dark chute in the snow, the snow-capped boulder and the pines, and nobody in the scene.',
    push('the dark chute', '黑色滑道'))

S.T('09-05', '05｜安全屋沙发上：苏清月醒来，发现暖得不像真的，低声说我还活着', 10, SOFA,
    [P('su_cozy', 'center', "lying on the deep brown leather sofa under a thick grey cashmere blanket, her head turned slightly toward frame-right, her hair damp and loose, one hand pulling the blanket up under her chin", 'obj:the warm amber ceiling lamp above her', "her lips parted, her brows slowly lifting")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, on the sofa.',
    "<su_cozy> lies on the sofa with her eyes on the warm amber lamp above her, her eyes slowly opening wider as she pulls the cashmere blanket up under her chin, then murmurs one line to herself in a hushed voice, talking to nobody, her lips moving softly, then a second short line, her lips parted and her brows lifting. Nobody else is in the room.",
    "苏清月躺在沙发上，眼睛看着头顶暖黄色的灯，眼睛慢慢睁大，一边把羊绒毯拉到下巴下面，然后用轻轻的声音自言自语了一句，不是对任何人说的，嘴唇轻轻动着，接着又是一句很短的，嘴唇微张、眉毛慢慢上扬。房间里没有别人。",
    voiced('The faint hum of the air system, a low simmer from the kitchen and her hushed murmur.', '空气系统轻微的嗡鸣、厨房里低低的炖煮声和她轻轻的自语。'),
    vo=[('su_cozy', "二十五度……", 2.4, 'Su'), ('su_cozy', "我，还活着？", 5.0, 'Su')], cam=push1('Su', '苏清月'),
    bg='Behind the sofa the wall of small security monitors shows a white blizzard, and the open kitchen glows warm at frame-left.',
    holds='The frame holds Su alone on the sofa, the kitchen and the monitor wall.', room={'Su'}, new=True,
    st={'Su': ('奶白色毛衣，躺在沙发上盖着灰色羊绒毯', '奶白色毛衣，在沙发上盖着灰色羊绒毯')})

S.T('09-06', '06｜安全屋沙发旁：林峰端来番茄排骨汤，说欢迎来到世界末日，苏清月看到他发黑的左手', 13, SOFA,
    [P('su_cozy', 'left', "sitting up on the sofa in profile facing frame-right with the grey cashmere blanket around her shoulders, tears on her cheeks", 'Lin', "her lips trembling, her brows drawn together"),
     P('lin_white', 'right', "standing beside the sofa in profile facing frame-left, a white porcelain bowl of steaming tomato-and-rib soup held out in his right hand, his left hand wrapped in stained gauze at his side with the skin at its edges dark and blackened", 'Su', "his lips set flat, his brows level")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the sofa.',
    "<lin_white> holds the steaming bowl out to <su_cozy> and speaks the first line to <su_cozy> in a flat quiet voice, then speaks the second line to <su_cozy> in the same voice, his lips set flat and his brows level. <su_cozy> takes the bowl in both hands and drinks, tears running down her cheeks, her lips trembling and her brows drawn together, then her eyes fall on his blackened left hand, and she lowers the bowl and speaks the third line to <lin_white> in a sharp professional voice, her eyes narrowing, and reaches for his left wrist.",
    "林峰把冒着热气的汤碗递到苏清月面前，用平静低沉的声音对苏清月说出第一句，接着用同样的声音对苏清月说出第二句，嘴唇抿平、眉毛平直。苏清月双手接过碗喝了起来，眼泪顺着脸颊往下流，嘴唇发抖、眉头拧在一起，然后她的目光落在他发黑的左手上，放下碗，用锐利专业的声音对林峰说出第三句，眼睛眯起，伸手去抓他的左手腕。",
    SOUND_BUNKER,
    lines=[('lin_white', "喝了它。", 0.8, 'Su'), ('lin_white', "欢迎来到世界末日。", 2.8, 'Su'), ('su_cozy', "再不切，你今晚就败血症。", 7.6, 'Lin')],
    bg='Behind them the wall of small security monitors shows a white blizzard, and the glass-topped coffee table stands in front of the sofa.',
    holds='The frame holds Su on the sofa and Lin standing beside it, the coffee table and the monitor wall.', room={'Su', 'Lin'}, enter={'Lin'},
    st={'Su': ('奶白色毛衣，在沙发上盖着灰色羊绒毯', None), 'Lin': ('白衬衫，端着汤碗，左手缠着发黑的纱布', None)})

# ---------------------------------------------------------------------------------------------- 第 10 集
b10 = S.episode('剧本第10集｜手术与契约', '手术室里没有麻药，苏清月对林峰说会很疼、敢乱动就切断他的手筋；林峰咬住毛巾，眼睛一直盯着她；她下刀、清创、缝合，他一声不吭。缝完，她剪断线，他拿出一份早就准备好的《地下避难所绝对共存协议》推到她面前：“你证明了你的价值。”她签字，问：“我的加入，要不要庆祝？”他带她走到一扇装着密码键盘的钢门前，门缝里透出粉紫色的光：“带你去看看，我们的伊甸园。”', 10)

S.T('10-01', '01｜手术室：苏清月说会很疼，林峰说动手吧，她警告他别乱动，他咬住毛巾', 11, MED,
    [P('su_surgeon', 'left', "sitting on a stool at the end of the steel table in profile facing frame-right, a scalpel held ready in her right hand over the open silver case", 'Lin', "her lips pressed in a thin line, her brows level, her eyes sharp"),
     P('lin_white', 'right', "sitting on the steel chair at the other end of the table in profile facing frame-left, his left hand laid palm-down on the sterile blue drape with the back of it dark and swollen, a rolled white towel in his right hand", 'Su', "his jaw set, his lips set flat, his brows level")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the medical room.',
    "<su_surgeon> speaks the first line to <lin_white> in a cool even voice, her lips pressed in a thin line and her brows level. <lin_white> speaks the second line to <su_surgeon> in a low steady voice, his jaw set and his brows level. <su_surgeon> speaks the third line to <lin_white> in a cold flat voice, her eyes sharp on his, and <lin_white> puts the rolled towel between his teeth and bites down slowly, his eyes steady on <su_surgeon>.",
    "苏清月用冷静平稳的声音对林峰说出第一句，嘴唇抿成一条细线、眉毛平直。林峰用低沉稳当的声音对苏清月说出第二句，下颌绷紧、眉毛平直。苏清月用冰冷平淡的声音对林峰说出第三句，眼睛锐利地盯着他的眼睛，林峰把卷好的毛巾放进齿间，慢慢咬紧，眼睛稳稳看着苏清月。",
    SOUND_MED,
    lines=[('su_surgeon', "会很疼。", 0.8, 'Lin'), ('lin_white', "动手吧。", 2.8, 'Su'), ('su_surgeon', "敢乱动，我就切断你的手筋。", 5.0, 'Lin')],
    bg='Between them the steel table is draped in sterile blue cloth under the round surgical lamp, and the open silver case with the instruments stands at frame-left.',
    holds='The frame holds Su and Lin, the draped table, the surgical lamp and the instrument tray.', room={'Su', 'Lin'}, new=True,
    st={'Su': ('黑色打底衫，白色手术手套，拿着手术刀', '黑色打底衫，白色手术手套，拿着手术刀'), 'Lin': ('白衬衫，左手放在蓝色无菌布上，手里拿着卷好的毛巾', '白衬衫，左手放在蓝色无菌布上，咬着毛巾')})

S.T('10-02', '02｜手术室：苏清月低头做细活，林峰咬着毛巾，眼睛一直看着她', 9, MED,
    [P('su_surgeon', 'left', "bending over his left hand in profile facing frame-right, a scalpel in her right hand working carefully at the dark skin on the back of his hand", 'obj:the back of his left hand under the sterile blue drape', "her lips pressed in a thin line, her brows low in concentration"),
     P('lin_white', 'right', "sitting on the steel chair in profile facing frame-left, his left hand under her working hands, a rolled white towel clamped between his teeth", 'Su', "his jaw clamped hard, sweat on his brow, his brows drawn together")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the medical room.',
    "<su_surgeon> works carefully at his hand with the scalpel in slow steady strokes, her eyes on the hand, her lips pressed in a thin line and her brows low. <lin_white> sits rigid with the towel clamped between his teeth, a bead of sweat running down his temple, his eyes locked on <su_surgeon>'s face, his jaw clamped hard and his brows drawn together, and does not make a sound.",
    "苏清月握着手术刀，一下一下缓慢而稳地处理他的手，眼睛看着那只手，嘴唇抿成一条细线、眉头专注地压低。林峰僵直地坐着，毛巾咬在齿间，一滴汗顺着太阳穴流下来，眼睛死死盯着苏清月的脸，下颌咬紧、眉头拧在一起，一声也不出。",
    breathy('The faint hum of the surgical lamp, the soft clink of steel and slow heavy breathing through a clenched jaw.', '手术灯轻微的嗡鸣、钢器械轻轻的碰撞声和咬紧牙关时缓慢沉重的呼吸声。'),
    dep=True, cam=push('both of them', '两人'),
    bg='The steel table is draped in sterile blue cloth under the round surgical lamp, and the instrument tray stands at frame-left.',
    holds='The frame holds Su and Lin, the draped table and the surgical lamp.',
    st={'Su': ('黑色打底衫，白色手术手套，拿着手术刀', '黑色打底衫，白色手术手套，拿着手术刀'), 'Lin': ('白衬衫，左手放在蓝色无菌布上，咬着毛巾', '白衬衫，左手放在蓝色无菌布上，咬着毛巾')})

S.T('10-03', '03｜手术室：苏清月用弯针缝合，林峰额头冒汗，一动不动', 9, MED,
    [P('su_surgeon', 'left', "bending over his left hand in profile facing frame-right, a curved needle held in a needle driver in her right hand pulling a dark thread through the skin", 'obj:the back of his left hand under the sterile blue drape', "her lips pressed in a thin line, her brows low in concentration"),
     P('lin_white', 'right', "sitting on the steel chair in profile facing frame-left, his left hand under her working hands, a rolled white towel clamped between his teeth", 'Su', "his jaw clamped hard, sweat beading on his forehead, his brows drawn together")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the medical room.',
    "<su_surgeon> pulls the dark thread through slowly, one careful stitch after another, her eyes on the hand, her lips pressed in a thin line and her brows low. <lin_white> sits perfectly still with the towel in his teeth, sweat beading on his forehead and his chest rising and falling slowly, his eyes locked on <su_surgeon>, his jaw clamped hard and his brows drawn together.",
    "苏清月缓慢地把黑色的线拉过去，一针接着一针，眼睛看着那只手，嘴唇抿成一条细线、眉头专注地压低。林峰一动不动地坐着，毛巾咬在齿间，额头上渗出一层汗，胸口缓慢地起伏，眼睛死死盯着苏清月，下颌咬紧、眉头拧在一起。",
    breathy('The faint hum of the surgical lamp, a soft pull of thread and slow heavy breathing through a clenched jaw.', '手术灯轻微的嗡鸣、线被轻轻拉过去的声音和咬紧牙关时缓慢沉重的呼吸声。'),
    dep=True, cam=push('both of them', '两人'),
    bg='The steel table is draped in sterile blue cloth under the round surgical lamp, and the instrument tray stands at frame-left.',
    holds='The frame holds Su and Lin, the draped table and the surgical lamp.',
    st={'Su': ('黑色打底衫，白色手术手套，拿着手术刀', '黑色打底衫，白色手术手套，拿着弯针')})

S.T('10-04', '04｜手术室：苏清月剪断缝合线说好了，林峰取下毛巾夸她，推出一份协议', 12, MED,
    [P('su_surgeon', 'left', "sitting on the stool in profile facing frame-right, a pair of small scissors in her right hand just clipping the end of the thread over his neatly stitched and bandaged left hand", 'Lin', "her lips softening, her brows relaxing"),
     P('lin_white', 'right', "sitting on the steel chair in profile facing frame-left, the rolled towel just dropped from his mouth into his right hand, his pale forehead damp with sweat", 'Su', "a faint tired curve at one corner of his mouth, his brows loosening")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the medical room.',
    "<su_surgeon> clips the end of the thread, sets the scissors down and speaks the first line to <lin_white> in a quiet, tired voice, her lips softening and her brows relaxing. <lin_white> takes the towel out of his mouth and speaks the second line to <su_surgeon> in a hoarse low voice, a faint tired curve at one corner of his mouth and his brows loosening. <lin_white> draws a thin stapled document from the drawer of the table with his right hand and pushes it across the drape toward <su_surgeon> and speaks the third line to <su_surgeon> in a level voice, and <su_surgeon> pulls the document toward her.",
    "苏清月剪断线头，放下剪刀，用安静疲惫的声音对林峰说出第一句，嘴唇放松、眉毛舒展。林峰把毛巾从嘴里拿出来，用沙哑低沉的声音对苏清月说出第二句，嘴角挂着一丝疲倦的弧度、眉头舒展。林峰用右手从桌子的抽屉里抽出一份订起来的薄文件，沿着蓝色无菌布推到苏清月面前，用平稳的声音对苏清月说出第三句，苏清月把文件拉到自己面前。",
    SOUND_MED,
    lines=[('su_surgeon', "好了。", 0.8, 'Lin'), ('lin_white', "手艺，不错。", 2.6, 'Su'), ('lin_white', "你证明了你的价值。", 5.2, 'Su')], dep=True,
    bg='The steel table is draped in sterile blue cloth under the round surgical lamp, and the open silver case and instruments stand at frame-left.',
    holds='The frame holds Su and Lin, the draped table with the stitched hand and the surgical lamp.',
    st={'Su': ('黑色打底衫，白色手术手套，拿着弯针', '黑色打底衫，白色手术手套，手边是那份文件'), 'Lin': ('白衬衫，左手放在蓝色无菌布上，咬着毛巾', '白衬衫，左手缠着白纱布，手里空着')})

S.T('10-05', '05｜手术室：苏清月签下名字，问我的加入要不要庆祝，林峰说当然', 11, MED,
    [P('su_surgeon', 'left', "sitting on the stool in profile facing frame-right, signing the last page of the thin stapled document with a pen in her right hand, her white gloves off and lying on the table", 'Lin', "a smug smile curving her lips, one brow arched"),
     P('lin_white', 'right', "sitting on the steel chair in profile facing frame-left, his bandaged left hand resting on the drape, his right hand open on the table", 'Su', "his jaw relaxed, a faint tired curve at one corner of his mouth, his brows level")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the medical room.',
    "<su_surgeon> finishes signing, lifts her eyes to <lin_white> and speaks the first line to <lin_white> in a teasing, low voice, then the second line to <lin_white>, a smug smile curving her lips and one brow arched. <lin_white> looks back at her with a long steady gaze and speaks the third line to <su_surgeon> in a low, warm voice, his jaw relaxed and his brows level.",
    "苏清月签完字，抬起眼睛看着林峰，用带点戏谑的低声对林峰说出第一句，接着对林峰说出第二句，嘴角带着得意的笑意、一边眉毛挑起。林峰长久而稳定地回看着她，用低沉温和的声音对苏清月说出第三句，下颌放松、眉毛平直。",
    SOUND_MED,
    lines=[('su_surgeon', "林老板。", 0.8, 'Lin'), ('su_surgeon', "我的加入，要不要庆祝？", 2.4, 'Lin'), ('lin_white', "当然。", 6.3, 'Su')], dep=True,
    bg='The steel table is draped in sterile blue cloth under the round surgical lamp, with the signed document lying open on it.',
    holds='The frame holds Su and Lin, the draped table with the signed document and the surgical lamp.',
    st={'Su': ('黑色打底衫，白色手术手套，手边是那份文件', '黑色打底衫，手套摘下，手里拿着笔'), 'Lin': ('白衬衫，左手缠着白纱布，手里空着', '白衬衫，左手缠着白纱布，手里空着')})

S.T('10-06', '06｜钢门前：林峰说带你去看看我们的伊甸园，推开门，粉紫色的光涌出来', 10, EDENDOOR,
    [P('lin_white', 'center', "standing in front of the steel door in profile facing frame-right, his right hand on the door handle, his left hand wrapped in white gauze at his side", 'Su', "his jaw relaxed, a faint pleased curve at one corner of his mouth, his brows lifting"),
     P('su_cozy', 'left', "standing beside him in profile facing frame-right with her arms folded in the oversized cream sweater", 'Lin', "one brow arched, her lips parted in curiosity")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the concrete corridor.',
    "<lin_white> speaks the first line to <su_cozy> in a quiet voice, a faint pleased curve at one corner of his mouth. <su_cozy> speaks the second line to <lin_white>, one brow arched and her lips parted in curiosity. <lin_white> speaks the third line to <su_cozy> and pushes the steel door open with his right hand until pink-violet light pours across both their faces.",
    "林峰用安静的声音对苏清月说出第一句，嘴角带着一丝满意的弧度。苏清月对林峰说出第二句，一边眉毛挑起、嘴唇因好奇微张。林峰对苏清月说出第三句，同时用右手把钢门推开，粉紫色的光涌出来洒在两人的脸上。",
    voiced('The deep thunk of a heavy steel bolt, a low hum from beyond the door and soft footsteps.', '粗重钢门栓的一声闷响、门后低低的嗡鸣和轻轻的脚步声。'),
    lines=[('lin_white', "带你去看看。", 0.8, 'Su'), ('su_cozy', "看什么？", 3.0, 'Lin'), ('lin_white', "我们的伊甸园。", 4.8, 'Su')],
    bg='The heavy steel door with the keypad stands at frame-right with a thin line of pink-violet light glowing around its edges.',
    holds='The frame holds Lin and Su, the concrete corridor and the steel door with the keypad.', room={'Lin', 'Su'}, new=True,
    st={'Lin': ('白衬衫，左手缠着白纱布', '白衬衫，左手缠着白纱布'), 'Su': ('奶白色毛衣，抱着手臂', '奶白色毛衣，抱着手臂')})

# ---------------------------------------------------------------------------------------------- 第 11 集
b11 = S.episode('剧本第11集｜生命的白噪音', '林峰按下水泵房的绿色按钮，清澈的地下水哗哗涌进透明大水箱；苏清月说：零下八十度，这里居然有活水。浴室的玻璃门上是浓浓的蒸汽。她洗完澡，穿着他宽大的衣服坐在圆桌边，他递给她一杯热红酒：水只是第一步。她替他检查手上的伤口，叮嘱他别碰水。他说：明天带你去地下二层，我要在那里造一个春天。', 11)

S.T('11-01', '01｜水泵房：林峰按下绿色启动键，苏清月说零下八十度这里居然有活水', 10, PUMP,
    [P('lin_home', 'left', "standing at the control panel in profile facing frame-right, his right thumb on the big green start button, his left hand wrapped in white gauze at his side", 'obj:the big green start button on the panel in front of him', "his jaw relaxed, his lips set flat, his brows level"),
     P('su_cozy', 'right', "standing beside the clear tank in profile facing frame-left with her arms wrapped around herself in the oversized cream sweater", 'Lin', "her lips parted, her brows lifting")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the pump room.',
    "<lin_home> speaks the first line to <su_cozy> in a low quiet voice, his jaw relaxed and his brows level, and presses the green start button with his right thumb. <su_cozy> listens with her lips parted, then speaks the second line to <lin_home> in a hushed voice, her brows lifting, then speaks the third line to <lin_home> in an awed whisper.",
    "林峰用低低安静的声音对苏清月说出第一句，下颌放松、眉毛平直，同时用右手拇指按下绿色启动键。苏清月嘴唇微张听着，然后用屏住呼吸的声音对林峰说出第二句，眉毛上扬，接着用惊叹的低语对林峰说出第三句。",
    voiced('A deep electric motor humming to life, the gurgle of water in pipes and soft echoes in the concrete room.', '低沉的电机嗡鸣着转起来、水在管道里的咕咕声和混凝土房间里轻轻的回响。'),
    lines=[('lin_home', "按下去，听。", 0.8, 'Su'), ('su_cozy', "零下八十度。", 3.4, 'Lin'), ('su_cozy', "这里居然有活水。", 5.0, 'Lin')],
    bg='Behind them the huge clear acrylic tank stands at frame-right and thick transparent pipes run along the left wall to the pump station.',
    holds='The frame holds Lin and Su, the control panel with the green button and the clear tank.', room={'Lin', 'Su'}, new=True,
    st={'Lin': ('灰色棉质家居服，左手缠着白纱布，站在控制面板前', '灰色棉质家居服，左手缠着白纱布'), 'Su': ('奶白色毛衣，抱着手臂', '奶白色毛衣，抱着手臂')})

insert_task('11-02', '02｜插镜：清澈的水哗哗涌过透明水管，灌进大水箱', 5, PUMP,
    'Wide establishing shot of the empty pump room, the clear tank and the pipes in the middle third of the frame, nobody in the room.',
    "Clear water gushes steadily through the transparent pipes along the wall and pours into the huge acrylic tank in thick bubbling sheets, the water level rising slowly behind the glass. Nothing else moves.",
    "空荡荡的水泵房：清澈的水哗哗地涌过墙边的透明水管，大片大片冒着气泡灌进巨大的亚克力水箱，水位在玻璃后面慢慢升高。别的什么都不动。",
    breathy('The steady rush and gurgle of clear water, a deep electric hum and soft echoes in the concrete room.', '清水稳定的哗哗和咕咕声、低沉的电机嗡鸣和混凝土房间里轻轻的回响。'),
    'The frame holds the huge clear tank filling with water, the transparent pipes along the wall and the pump station, and nobody in the room.',
    push('the water pouring into the tank', '灌进水箱的水'))

insert_task('11-03', '03｜插镜：浴室的磨砂玻璃门上是浓浓的蒸汽，木凳上叠着干净的衣服', 5, BATH,
    'Wide establishing shot of the empty bathroom, the frosted shower door in the middle third of the frame, nobody in the room.',
    "Thick white steam clouds the frosted-glass shower door while water streams steadily behind it, and on the wooden bench a folded grey cotton shirt waits beside the folded white towels. Nothing else moves.",
    "空无一人的浴室：磨砂玻璃淋浴门上是浓浓的白色蒸汽，门后水流不停，木凳上叠着一件灰色棉质长袖衫，旁边是叠好的白毛巾。别的什么都不动。",
    breathy('The steady patter of hot water, a soft hiss of steam and a faint warm echo in the tiles.', '热水稳定的淅沥声、蒸汽轻轻的嘶声和瓷砖间一点温暖的回响。'),
    'The frame holds the steaming frosted shower door and the bench with the folded shirt and towels, and nobody in the room.',
    push('the steaming glass door', '蒙着蒸汽的玻璃门'))

S.T('11-04', '04｜安全屋圆桌边：林峰倒热红酒，苏清月说像做梦，林峰说水只是第一步，两人碰杯', 11, LIVING,
    [P('lin_home', 'left', "seated at the small round wooden dining table in profile facing frame-right, pouring steaming red wine from a small copper pot into a glass with his right hand, his left hand wrapped in white gauze", 'Su', "his jaw relaxed, his lips set in a calm flat line, his brows soft"),
     P('su_cozy', 'right', "seated at the table in profile facing frame-left in the oversized cream sweater with her damp hair loose, both hands around a glass", 'Lin', "her lips parted in a soft look, her brows relaxed")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dining table.',
    "<lin_home> speaks the first line to <su_cozy> in a low warm voice and hands her the steaming glass, his jaw relaxed and his brows soft. <su_cozy> takes a sip, closes her eyes for a moment and speaks the second line to <lin_home> in a dreamy voice, her lips parted and her brows relaxed. <lin_home> speaks the third line to <su_cozy> in a quiet voice, then they touch their glasses together lightly.",
    "林峰用低低温和的声音对苏清月说出第一句，把冒着热气的杯子递给她，下颌放松、眉毛舒展。苏清月抿了一口，闭了一会儿眼睛，用梦呓般的声音对林峰说出第二句，嘴唇微张、眉毛放松。林峰用安静的声音对苏清月说出第三句，然后两人轻轻碰了一下杯子。",
    voiced('The faint hum of the air system, the gentle clink of glass and the soft bubbling of the copper pot.', '空气系统轻微的嗡鸣、玻璃杯轻轻的碰撞声和铜锅里轻轻冒泡的声音。'),
    lines=[('lin_home', "热红酒，趁热喝。", 0.8, 'Su'), ('su_cozy', "二十五度……像做梦。", 3.2, 'Lin'), ('lin_home', "水，只是第一步。", 6.0, 'Su')],
    bg='Between them on the table a small copper pot of steaming mulled wine and two glasses stand, and the open kitchen glows warm at frame-left.',
    holds='The frame holds Lin and Su, the dining table with the copper pot and the kitchen behind them.', room={'Lin', 'Su'}, new=True,
    st={'Lin': ('灰色棉质家居服，左手缠着白纱布，坐在圆桌边', '灰色棉质家居服，左手缠着白纱布，坐在圆桌边'), 'Su': ('奶白色毛衣，头发披着，坐在圆桌边', '奶白色毛衣，头发披着，坐在圆桌边')})

S.T('11-05', '05｜同一张圆桌：苏清月拆开他手上的纱布检查伤口，叮嘱他别碰水', 10, LIVING,
    [P('su_cozy', 'right', "seated at the table in profile facing frame-left, gently unwinding the gauze from his left hand held in both of hers", 'obj:the stitched back of his left hand in her hands', "her lips pressed in a thin focused line, her brows low"),
     P('lin_home', 'left', "seated at the table in profile facing frame-right, his left hand held out to her over the table", 'Su', "his jaw relaxed, a faint pleased curve at one corner of his mouth, his brows soft")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dining table.',
    "<su_cozy> inspects the neat black stitches on the back of his hand, her eyes on the hand, and speaks the first line to <lin_home> in a stern low voice, her lips pressed in a thin focused line and her brows low. <lin_home> answers with the second line to <su_cozy> in an amused voice, a faint pleased curve at one corner of his mouth. <su_cozy> speaks the third line to <lin_home> in a softer voice as she winds the clean gauze back around his hand.",
    "苏清月看着他手背上整齐的黑色缝线，眼睛看着那只手，用严厉低沉的声音对林峰说出第一句，嘴唇抿成专注的一条线、眉头压低。林峰用带笑意的声音对苏清月说出第二句，嘴角挂着一丝满意的弧度。苏清月一边把干净的纱布重新缠回他的手上，一边用柔和一点的声音对林峰说出第三句。",
    voiced('The faint hum of the air system, the soft rasp of gauze and a small clink of glass on the table.', '空气系统轻微的嗡鸣、纱布轻轻的摩擦声和桌上玻璃杯一声轻响。'),
    lines=[('su_cozy', "别碰水，听见没？", 0.8, 'Lin'), ('lin_home', "知道了，医生。", 3.6, 'Su'), ('su_cozy', "伤口，长得不错。", 6.0, 'Lin')], dep=True,
    bg='Between them on the table stand two glasses of mulled wine and the small copper pot, and the open kitchen glows warm at frame-left.',
    holds='The frame holds Lin and Su, the dining table with the glasses and the kitchen behind them.',
    st={'Lin': ('灰色棉质家居服，左手缠着白纱布，坐在圆桌边', '灰色棉质家居服，左手重新缠好白纱布'), 'Su': ('奶白色毛衣，头发披着，坐在圆桌边', '奶白色毛衣，头发披着，坐在圆桌边')})

S.T('11-06', '06｜同一张圆桌：林峰说明天带你去地下二层，造一个春天，苏清月说她等着看', 10, LIVING,
    [P('lin_home', 'left', "seated at the table in profile facing frame-right, leaning back in his chair with his rewrapped left hand resting on the table", 'Su', "his jaw relaxed, his lips set in a calm flat line, his brows soft"),
     P('su_cozy', 'right', "seated at the table in profile facing frame-left, both hands around her glass, her cheeks flushed", 'Lin', "her lips parted in a soft look, her brows lifted")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dining table.',
    "<lin_home> leans back and speaks the first line to <su_cozy> in a quiet voice, then the second line to <su_cozy> in a lower, warmer voice, his jaw relaxed and his brows soft. <su_cozy> holds her glass in both hands, her cheeks flushed, and speaks the third line to <lin_home> in a soft eager voice, her lips parted and her brows lifted.",
    "林峰往后靠在椅子上，用安静的声音对苏清月说出第一句，接着用更低更温暖的声音对苏清月说出第二句，下颌放松、眉毛舒展。苏清月双手捧着杯子，脸颊泛红，用轻轻而期待的声音对林峰说出第三句，嘴唇微张、眉毛上扬。",
    voiced('The faint hum of the air system and the soft clink of a glass set down on the table.', '空气系统轻微的嗡鸣和玻璃杯放在桌上的一声轻响。'),
    lines=[('lin_home', "明天，带你去地下二层。", 0.8, 'Su'), ('lin_home', "我要造一个春天。", 4.0, 'Su'), ('su_cozy', "我，等着看。", 6.6, 'Lin')], dep=True,
    bg='Between them on the table stand two glasses of mulled wine and the small copper pot, and the open kitchen glows warm at frame-left.',
    holds='The frame holds Lin and Su, the dining table with the glasses and the kitchen behind them.',
    st={'Lin': ('灰色棉质家居服，左手重新缠好白纱布', '灰色棉质家居服，左手重新缠好白纱布'), 'Su': ('奶白色毛衣，头发披着，坐在圆桌边', '奶白色毛衣，头发披着，坐在圆桌边')})

# ---------------------------------------------------------------------------------------------- 第 12 集
b12 = S.episode('剧本第12集｜地下伊甸园', '第二天林峰推开钢门，地下二层亮着粉紫色的生长灯，一排排水培槽里长满嫩苗，苏清月惊呆了；两人换上手套，他教她把苗移栽进水培槽，她说像缝合一样。角落里的孵化箱里，小鸡刚刚破壳，她惊喜地喊出声，林峰立刻让她小声点，用厚厚的隔音海绵板把孵化箱围住。他说：农场开业，今晚吃火锅，去选底料。她一个人站在冷库的货架前，两盒底料拿不定主意：都要。', 12)

insert_task('12-01', '01｜插镜：地下二层，一排排粉紫色的生长灯下，水培槽里长满嫩苗', 5, EDEN,
    'Wide establishing shot of the underground farm level, the hydroponic channels in the middle third of the frame, nobody in the scene.',
    "Rows of pink-violet grow lamps glow over the long white hydroponic channels where young lettuce and tomato seedlings stand in neat lines, and a faint mist of nutrient water hangs in the warm air. Nothing else moves.",
    "地下二层空无一人：一排排粉紫色的生长灯照着长长的白色水培槽，嫩生菜和番茄苗整整齐齐地站成一行行，暖湿的空气里飘着一层淡淡的营养液水汽。别的什么都不动。",
    breathy('A soft hum of grow lamps, the gentle trickle of nutrient water in the channels and a warm quiet hush.', '生长灯轻轻的嗡鸣、水培槽里营养液轻轻流淌的声音和温暖的寂静。'),
    'The frame holds the long hydroponic channels with the seedlings under the pink-violet lamps, the incubator box and the steel staircase, and nobody in the scene.',
    push('the rows of seedlings', '一排排嫩苗'))

S.T('12-02', '02｜地下二层：苏清月看呆了，问这是真的吗，林峰说造一个春天，她问他还藏了什么', 10, EDEN,
    [P('su_cozy', 'left', "standing at the end of a hydroponic row in profile facing frame-right with both hands pressed to her chest, her eyes wide", 'Lin', "her lips parted in awe, her brows lifted"),
     P('lin_home', 'right', "standing in the aisle in profile facing frame-left with his arms folded and his left hand wrapped in white gauze", 'Su', "his jaw relaxed, a faint pleased curve at one corner of his mouth, his brows soft")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the underground farm level.',
    "<su_cozy> looks along the glowing rows and speaks the first line to <lin_home> in an awed whisper, her lips parted in awe and her brows lifted. <lin_home> speaks the second line to <su_cozy> in a quiet voice, a faint pleased curve at one corner of his mouth and his brows soft. <su_cozy> turns back to him and speaks the third line to <lin_home> with a disbelieving breath.",
    "苏清月看着发光的一排排水培槽，用屏住呼吸的惊叹声对林峰说出第一句，嘴唇因惊叹微张、眉毛上扬。林峰用安静的声音对苏清月说出第二句，嘴角带着一丝满意的弧度、眉毛舒展。苏清月转回头看着他，带着难以置信的一口气对林峰说出第三句。",
    voiced('A soft hum of grow lamps, the gentle trickle of nutrient water and soft echoes in the concrete hall.', '生长灯轻轻的嗡鸣、营养液轻轻流淌的声音和混凝土大厅里轻轻的回响。'),
    lines=[('su_cozy', "这是，真的吗？", 0.8, 'Lin'), ('lin_home', "我说过，造一个春天。", 3.2, 'Su'), ('su_cozy', "你还藏了什么？", 6.4, 'Lin')],
    bg='Behind them the long hydroponic channels full of seedlings glow under the pink-violet lamps, and the incubator box stands at frame-right.',
    holds='The frame holds Su and Lin, the hydroponic rows and the incubator box behind them.', room={'Su', 'Lin'}, new=True,
    st={'Su': ('奶白色毛衣，站在水培槽一端', '奶白色毛衣，站在水培槽一端'), 'Lin': ('灰色棉质家居服，左手缠着白纱布', '灰色棉质家居服，左手缠着白纱布')})

S.T('12-03', '03｜水培槽边：林峰教苏清月把嫩苗移栽进水培槽，她说像缝合一样', 11, EDEN,
    [P('lin_home', 'left', "standing at a hydroponic channel in profile facing frame-right, holding a tray of tiny seedlings in his right hand, his left hand wrapped in white gauze at his side", 'Su', "his jaw relaxed, his lips set in a calm flat line, his brows soft"),
     P('su_cozy', 'right', "standing at the channel in profile facing frame-left in thin work gloves, holding a tiny seedling by its leaf in her fingers and lowering its root plug toward a hole in the channel", 'obj:the hole in the channel where the seedling root plug is going in', "her lips pressed in a focused line, her brows low")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the hydroponic channel.',
    "<lin_home> speaks the first line to <su_cozy> in a quiet voice, his jaw relaxed and his brows soft. <su_cozy> lowers the seedling's root plug into the hole with careful fingers, her eyes on the hole, and speaks the second line to <lin_home> in a low, absorbed voice, her lips pressed in a focused line and her brows low. <lin_home> speaks the third line to <su_cozy> in a warm voice as she presses the seedling in.",
    "林峰用安静的声音对苏清月说出第一句，下颌放松、眉毛舒展。苏清月用小心的手指把幼苗的根块放进孔里，眼睛看着那个孔，用低低专注的声音对林峰说出第二句，嘴唇抿成专注的一条线、眉头压低。林峰在她把幼苗按稳的时候，用温暖的声音对苏清月说出第三句。",
    voiced('A soft hum of grow lamps, the gentle trickle of nutrient water and the faint squeak of wet gloves.', '生长灯轻轻的嗡鸣、营养液轻轻流淌的声音和湿手套轻轻的吱吱声。'),
    lines=[('lin_home', "根朝下，轻一点。", 0.8, 'Su'), ('su_cozy', "像缝合一样。", 3.4, 'Lin'), ('lin_home', "对，一样细。", 5.8, 'Su')], dep=True,
    bg='Behind them the long hydroponic channels full of seedlings glow under the pink-violet lamps.',
    holds='The frame holds Lin and Su, the hydroponic channel with the seedlings and the grow lamps.',
    st={'Su': ('奶白色毛衣，站在水培槽一端', '奶白色毛衣，戴着薄工作手套，站在水培槽边'), 'Lin': ('灰色棉质家居服，左手缠着白纱布', '灰色棉质家居服，左手缠着白纱布')})

insert_task('12-04', '04｜插镜：孵化箱的玻璃窗里，三只毛茸茸的小鸡在稻草上摇摇晃晃', 5, EDEN,
    'Close shot of the incubator box at the right of the underground farm level, the glass window in the middle third of the frame, nobody in the scene.',
    "Inside the warm incubator box under the red heat lamp, three fluffy yellow chicks stumble unsteadily across the straw beside a cracked eggshell, one of them tilting its beak up to peep. Nothing else moves.",
    "孵化箱的玻璃窗里，红色保温灯下，三只毛茸茸的黄色小鸡在稻草上摇摇晃晃地走，旁边是一只裂开的蛋壳，其中一只仰起小嘴叫了一声。别的什么都不动。",
    breathy('Tiny high peeping from the chicks, the soft hum of the heat lamp and a warm hush.', '小鸡细细的叽叽声、保温灯轻轻的嗡鸣和温暖的寂静。'),
    'The frame holds the glass window of the incubator box with the three chicks on the straw, and nobody in the scene.',
    push('the three chicks', '三只小鸡'))

S.T('12-05', '05｜孵化箱旁：苏清月喊出声说是活的，林峰让她小声点，按住隔音海绵板围住孵化箱', 10, EDEN,
    [P('su_cozy', 'left', "standing beside the incubator box in profile facing frame-right, both hands clapped over her mouth, her eyes bright", 'obj:the chicks in the incubator box window at frame-right', "her eyes wide, her lips behind her hands, her brows lifted high"),
     P('lin_home', 'right', "standing at the side of the incubator box in profile facing frame-left, a thick sheet of grey soundproof foam pressed against the side of the box with his right hand, one finger of his bandaged left hand raised to his lips", 'Su', "his jaw tight, his lips pressed to his finger, his brows low")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, beside the incubator box.',
    "<su_cozy> speaks the first line to <lin_home> in a thrilled whisper-shout, her hands clapped over her mouth, her eyes wide and her brows lifted high. <lin_home> raises one finger to his lips and speaks the second line to <su_cozy> in a low urgent voice, his jaw tight and his brows low, then speaks the third line to <su_cozy> as he presses the thick sheet of grey foam against the side of the incubator box.",
    "苏清月用兴奋的、压着嗓子的惊呼对林峰说出第一句，双手捂着嘴，眼睛睁大、眉毛高高挑起。林峰把一根手指竖到唇边，用低低而急迫的声音对苏清月说出第二句，下颌绷紧、眉头压低，然后一边把厚厚的灰色隔音海绵板按在孵化箱侧面，一边对苏清月说出第三句。",
    voiced('A soft hum of the heat lamp, faint peeping from the incubator box and the soft squeak of foam.', '保温灯轻轻的嗡鸣、孵化箱里微弱的叽叽声和海绵轻轻的摩擦声。'),
    lines=[('su_cozy', "是活的！", 0.8, 'Lin'), ('lin_home', "小声点。", 2.8, 'Su'), ('lin_home', "叫声，是催命符。", 4.6, 'Su')],
    bg='At frame-right the warm incubator box with its glass window and red heat lamp stands beside them, the chicks small and yellow behind the glass.',
    holds='The frame holds Su and Lin, the incubator box and the foam sheet.', room={'Su', 'Lin'}, new=True,
    st={'Su': ('奶白色毛衣，站在孵化箱旁', '奶白色毛衣，站在孵化箱旁'), 'Lin': ('灰色棉质家居服，左手缠着白纱布', '灰色棉质家居服，左手缠着白纱布')})

S.T('12-06', '06｜地下二层：林峰说农场开业今晚吃火锅，苏清月说火锅，他让她去选底料，转身走向楼梯', 12, EDEN,
    [P('lin_home', 'center', "standing in the aisle in profile facing frame-left, a clean towel in his right hand wiping his fingers, his left hand wrapped in white gauze", 'Su', "his jaw relaxed, a faint pleased curve at one corner of his mouth, his brows soft"),
     P('su_cozy', 'left', "standing beside the hydroponic row in profile facing frame-right, one hand still on a seedling tray", 'Lin', "her lips parted, her brows lifted")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the underground farm level.',
    "<lin_home> speaks the first line to <su_cozy> in a quiet warm voice, his jaw relaxed and his brows soft. <su_cozy> speaks the second line to <lin_home> in a delighted, disbelieving voice, her lips parted and her brows lifted. <lin_home> speaks the third line to <su_cozy>, then turns and walks to the steel staircase at frame-left and goes up it until the staircase is empty. <su_cozy> watches him go with a bright pleased look.",
    "林峰用安静温暖的声音对苏清月说出第一句，下颌放松、眉毛舒展。苏清月用惊喜而难以置信的声音对林峰说出第二句，嘴唇微张、眉毛上扬。林峰对苏清月说出第三句，然后转身走向画面左边的钢楼梯，走上楼梯，直到楼梯上空无一人。苏清月带着明亮满意的神情目送他。",
    voiced('A soft hum of grow lamps, footsteps on a steel staircase fading upward and a warm hush.', '生长灯轻轻的嗡鸣、渐渐往楼上远去的钢楼梯上的脚步声和温暖的寂静。'),
    lines=[('lin_home', "农场开业，今晚吃火锅。", 0.8, 'Su'), ('su_cozy', "火锅？！", 4.0, 'Lin'), ('lin_home', "去选底料吧。", 5.8, 'Su')], room={'Su', 'Lin'}, new=True, exit={'Lin'},
    bg='Behind them the long hydroponic channels full of seedlings glow under the pink-violet lamps, and the steel staircase rises at frame-left.',
    holds='The frame holds Lin and Su, the hydroponic rows and the steel staircase.',
    st={'Su': ('奶白色毛衣，站在水培槽边', '奶白色毛衣，站在水培槽边'), 'Lin': ('灰色棉质家居服，左手缠着白纱布', None)})

S.T('12-07', '07｜冷库：苏清月一个人站在货架前，两盒火锅底料拿不定主意，低声说都要', 10, COLD,
    [P('su_cozy', 'center', "standing in front of the eye-level shelf in profile facing frame-left, a red box of hotpot base in one hand and a yellow box in the other, her breath faintly clouding", 'obj:the two hotpot base boxes in her hands', "her lips pursed in thought, her brows drawn together playfully")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the cold store.',
    "<su_cozy> holds the red box and the yellow box up side by side, her eyes going back and forth between them, her lips pursed in thought and her brows drawn together, then murmurs one line to herself in a hushed voice, talking to nobody, her lips moving softly, then a second short line, and tucks both boxes under her arm. Nobody else is in the cold store.",
    "苏清月把红色的盒子和黄色的盒子并排举起来，眼睛在两盒之间来回看，嘴唇抿着思考、眉头玩笑般皱着，然后用轻轻的声音自言自语了一句，不是对任何人说的，嘴唇轻轻动着，接着又是一句很短的，然后把两盒都夹到了腋下。冷库里没有别人。",
    voiced('A low hum of the refrigeration, a faint draft and her hushed murmur.', '制冷机组低低的嗡鸣、一丝冷风和她轻轻的自语。'),
    vo=[('su_cozy', "辣的，还是菌汤？", 2.2, 'Su'), ('su_cozy', "……都要。", 5.4, 'Su')], cam=push1('Su and the boxes', '苏清月和两盒底料'),
    bg='Behind her the steel shelves are stacked with white boxes of frozen meat, seafood and vegetables, and the heavy insulated door stands at frame-right.',
    holds='The frame holds Su alone in the cold store, the shelves and the hotpot base boxes.', room={'Su'}, new=True,
    st={'Su': ('奶白色毛衣，站在货架前', '奶白色毛衣，站在货架前')})

doc = S.finish()
