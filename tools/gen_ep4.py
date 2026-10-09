#!/usr/bin/env python3
"""生成《Alpha继兄的笼中吻》第 4 集“羊入虎口”制作稿（追加批次，英语台词，美式口语）。
基于第 3 集 JSON（style、素材、角色逐字复制），新增：场景 villa_front；人物 butler、lily_coat（用 lily 作参考图）、killian_robe（用 killian 作参考图）；
角色 Butler、LilyCoat、KillianRobe。验证的假设同第 3 集（手册 7.10 的 H14–H16，7.11）。
为保证场景连贯：原剧本里基利安站在“二楼环形阶梯”，而莉莉一直在门外车旁，这里改成“门厅上方二楼阳台”，情节不变。
原剧本“周围全是黑衣保镖”不入画（一个画面最多两人）。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, silent, voiced

b = Batch('2026-10-09_第3集_制作稿_英文台词_追加.json', 'Alpha继兄的笼中吻｜第4集｜羊入虎口', 3300)

# ---- 新素材、新角色 ---------------------------------------------------------------------------------
b.scene('villa_front', '半山庄园门前',
        ("The gravel forecourt of a gloomy luxurious hillside mansion at dusk: a dark stone facade with tall narrow windows, a wide flight of stone entrance steps on the right, "
         "a second-floor stone balcony with a balustrade above the entrance, tall black iron gates and dark pine trees behind, a black Maybach sedan parked on the gravel on the left, "
         "cold blue dusk light with warm lamps glowing in the windows. The reference fixes the layout and decor, not any people."),
        ("黄昏时阴森奢华的半山庄园门前碎石场地：深色石头外墙配高窄窗，右边是宽阔的石头台阶，台阶上方二楼有一座带栏杆的石头阳台，后面是高大的黑色铁门和深色松树，"
         "左边碎石地上停着一辆黑色迈巴赫轿车，冷蓝的暮色里窗内亮着暖灯。参考图固定布局与陈设，不带入任何人物。"),
        ("A photorealistic wide shot of the empty gravel forecourt of a gloomy luxurious hillside mansion at dusk: a dark stone facade with tall narrow windows, a wide flight of stone entrance steps on the right, "
         "a second-floor stone balcony with a balustrade above the entrance, tall black iron gates and dark pine trees behind, a black Maybach sedan parked on the gravel on the left, "
         "cold blue dusk light with warm lamps in the windows. No people."))
b.person('butler', '老管家',
         ("The butler, an elderly man in his sixties with neatly combed silver hair, a lined, dignified face and kind pale-blue eyes, wearing a black tailcoat, white shirt, grey waistcoat, black tie and white gloves. "
          "The portrait fixes his identity and clothes, not staging."),
         "老管家，六十多岁的老人，银发梳得整齐，脸上有皱纹、端庄，眼睛是温和的浅蓝色，穿黑色燕尾服、白衬衫、灰色马甲、黑领带，戴白手套。人物图固定身份与衣服，不固定站位。",
         ("A photorealistic half-body portrait of an elderly man in his sixties with neatly combed silver hair, a lined, dignified face and kind pale-blue eyes, wearing a black tailcoat, white shirt, grey waistcoat, black tie and white gloves. "
          "He faces the camera with a calm, courteous expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores."))
b.person('lily_coat', '莉莉（旅途装）',
         ("Lily, the same adult woman in her mid-twenties as in the reference, with long wavy chestnut-brown hair pulled into a low loose ponytail held by a small silver hair clip, fair skin and large hazel-green eyes, "
          "now wearing a faded grey wool coat over a plain navy dress, tired but proud. The portrait fixes her identity and clothes, not staging."),
         "莉莉，和参考图是同一个二十五岁左右的成年女性，栗棕色长卷发低低地扎成松散的马尾，用一枚小银发卡固定，白皙皮肤、浅褐绿色大眼睛，这次穿褪色的灰色羊毛外套配朴素的藏青连衣裙，疲惫却倔强。人物图固定身份与衣服，不固定站位。",
         ("A photorealistic half-body portrait of the same woman as in the reference image, long wavy chestnut-brown hair pulled into a low loose ponytail held by a small silver hair clip, "
          "wearing a faded grey wool coat over a plain navy dress. She faces the camera with a tired but proud expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores."),
         ref='lily')
b.person('killian_robe', '基利安（黑丝绸睡袍）',
         ("Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short swept-back black hair, a sharp jawline, light stubble and cold dark-gray eyes, "
          "now wearing a black silk robe tied at the waist over dark trousers, the collar open at the base of the throat, a platinum luxury wristwatch on his left wrist. The portrait fixes his identity and clothes, not staging."),
         "基利安，和参考图是同一个三十出头、身材极高、肩膀宽阔的成年男性，黑色短发向后梳，下颌线锋利，有浅胡茬，眼睛是冷冽的深灰色，这次穿黑色真丝睡袍，腰间系带，里面是深色长裤，领口开到喉咙下方，左腕戴铂金色名表。人物图固定身份与衣服，不固定站位。",
         ("A photorealistic half-body portrait of the same man as in the reference image, short swept-back black hair, sharp jawline, light stubble and cold dark-gray eyes, "
          "wearing a black silk robe tied at the waist, the collar open at the base of the throat, a platinum luxury wristwatch on his left wrist. He faces the camera with a cold, composed expression. "
          "Soft even studio light, plain neutral gray background, natural skin texture with visible pores."),
         ref='killian')

b.character('Butler', 'butler',
            "An elderly adult male voice, courteous, measured and warm, speaking clear American English at ordinary conversational volume with careful politeness.",
            "年迈的成年男声，彬彬有礼、不急不缓、带着温和，说清楚的美式英语，正常交谈音量，措辞谨慎有礼。")
b.character('LilyCoat', 'lily_coat',
            "A young adult female voice, light and slightly breathy, speaking clear American English. Every word is fully voiced and audible, tight and shaky with nerves, alarm and wounded pride.",
            "年轻成年女声，轻而略带气息，说清楚的美式英语。每个字都正常发声、清晰可辨，声音紧绷发颤，带着紧张、惊慌和受伤的自尊。")
b.character('KillianRobe', 'killian_robe',
            "A mature adult male voice in a deep chest register, low and unhurried with a husky edge, speaking clear American English in a quiet, controlled, menacing tone. He never shouts, and every word is fully voiced and audible.",
            "成熟成年男声，深沉的胸腔音，低缓不急，带沙哑质感，说清楚的美式英语。语气安静、克制、带压迫感，从不喊叫，每个字都正常发声、清晰可辨。")

V = '[[asset:villa_front]]'; LC = '[[asset:lily_coat]]'; KR = '[[asset:killian_robe]]'; BU = '[[asset:butler]]'
# H15：固定方位
LAY = " Fixed stage layout: the black Maybach is at frame-left; the mansion's entrance steps and the balcony above them are at frame-right; Lily is always at frame-left of Killian and of the butler."
END = " Cold blue dusk light with warm window lamps, the forecourt softly blurred behind."
VIL = ('villa_front',)

# 01 迈巴赫驶入（无人入画）
b.task('01｜驶入庄园', 5, [], VIL, ['villa_front'],
       "Wide shot of the gravel forecourt of the dark hillside mansion at dusk, the black Maybach centered in the middle third of the frame, stopped on the gravel with its headlights on, the mansion's entrance steps at frame-right. Nobody is visible." + LAY,
       END,
       "黄昏，黑色迈巴赫开进阴森的半山庄园，慢慢停在碎石地上。没有人入画。", "0—5秒庄园门前全景，镜头固定。",
       None,
       f"A steady wide shot opens from the adopted first frame in {V}: the black Maybach rolling the last few metres across the gravel and coming to a stop, its headlights lighting the stones, the dark mansion at frame-right. Nobody is visible. The camera holds still.",
       "从开场图继续，全景：黑色迈巴赫在碎石地上滑完最后几米，停下，车灯照亮碎石，深色庄园在右边。没有人入画。镜头固定。",
       silent("A low engine idling down to silence and tyres crunching slowly on gravel.", "低沉的引擎声渐渐熄灭，轮胎在碎石上缓慢碾过。"))

# 02 莉莉下车站定
b.task('02｜旧行李箱', 6, ['LilyCoat'], ('villa_front', 'lily_coat'), ['villa_front'],
       "Medium shot of Lily alone, full body, standing on the gravel beside the open rear door of the black Maybach, centered in the middle third of the frame, in profile facing frame-right, "
       "a battered brown leather suitcase in her right hand, her eyes on the mansion's entrance at frame-right. Nobody else is in the frame." + LAY,
       END,
       "莉莉一个人站在车旁，提着旧行李箱，看着右边庄园的大门。", "0—6秒莉莉侧面中景，镜头固定。",
       None,
       f"A steady medium shot opens from the adopted first frame in {V}: {LC} alone on the gravel in profile facing frame-right, the battered suitcase in her right hand, her eyes on the mansion's entrance at frame-right. "
       "Wind stirs her hair and her knuckles whiten on the suitcase handle. Her feet do not move. The camera holds still.",
       "从开场图继续，莉莉中景：一个人站在碎石地上，侧脸朝右，右手提着旧行李箱，目光落在右边的庄园大门上。风吹动她的头发，握着行李箱把手的指节发白。脚不动。镜头固定。",
       silent("Cold wind in the pine trees and a faint creak of leather.", "冷风吹过松林的声音，皮革轻轻的吱呀声。"))

# 03 老管家迎上来
b.task('03｜老管家', 6, ['Butler', 'LilyCoat'], ('villa_front', 'butler', 'lily_coat'), ['villa_front'],
       "Medium two-shot, waist-up, in profile, both people centered in the middle third of the frame. Lily stands at frame-left in profile facing frame-right, her battered brown suitcase on the gravel at her feet; "
       "the elderly butler in his black tailcoat and white gloves stands at frame-right facing her, his hands clasped in front of him, his eyes on her face. Nobody else is in the frame." + LAY,
       END,
       "老管家站在莉莉面前，双手交叠，恭敬地开口。莉莉愣愣地看着他。", "0—6秒侧面中景，两人居中，莉莉在左、管家在右，镜头固定。",
       ('Butler', "Madam, your room is ready.", 1.0),
       f"A steady medium two-shot in profile opens from the adopted first frame in {V}: {LC} at frame-left, the suitcase at her feet; {BU} at frame-right facing her, his gloved hands clasped in front of him. "
       "He speaks with a courteous, measured politeness and inclines only his head slightly. She stares at him, startled. His hands stay clasped. The camera holds still.",
       "从开场图继续，侧面中景：莉莉在左，行李箱放在脚边；管家在右面对她，戴着白手套的双手交叠在身前。他有礼、不急不缓地说话，只把头微微一低。她吃惊地看着他。他的手一直交叠。镜头固定。",
       voiced("Cold wind and a faint rustle of cloth.", "冷风声和轻微的衣料沙沙声。"))

# 04 莉莉慌乱纠正
b.task('04｜我不是女主人', 6, ['LilyCoat'], ('villa_front', 'lily_coat'), ['villa_front'],
       "Medium close-up of Lily alone, chest-up, in profile facing frame-right, centered in the middle third of the frame, in the faded grey wool coat, her eyes on an old man standing at frame-right, just outside the frame, "
       "her brows drawn together, her lips parted. Nobody else is in the frame." + LAY,
       END,
       "莉莉慌乱地看着右边画面外的管家，开口纠正。", "0—6秒莉莉侧面中近景，镜头固定。",
       ('LilyCoat', "No, I'm not the mistress. I'm just...", 0.8),
       f"A steady medium close-up opens from the adopted first frame in {V}: {LC} in profile facing frame-right, her eyes on the old man at frame-right, just outside the frame. "
       "She speaks in a flustered, shaky voice and her words trail off. Her hand stays on the suitcase handle. The camera holds still.",
       "从开场图继续，莉莉近景：侧脸朝右，目光落在右边画面外的老人身上。她慌乱地、声音发颤地说话，话说到一半断了。手一直握着行李箱把手。镜头固定。",
       voiced("Cold wind and a faint rustle of cloth.", "冷风声和轻微的衣料沙沙声。"))

# 05 基利安在二楼阳台
b.task('05｜二楼的基利安', 6, ['KillianRobe'], ('villa_front', 'killian_robe'), ['villa_front'],
       "Medium shot of Killian alone, waist-up, standing at the stone balustrade of the second-floor balcony above the entrance steps, centered in the middle third of the frame, in profile facing frame-left, "
       "a crystal whiskey tumbler in his right hand, in the black silk robe tied at the waist, his eyes lowered on a woman standing below at frame-left, just outside the frame, his face cold and unreadable. Nobody else is in the frame." + LAY,
       END,
       "基利安穿着黑色真丝睡袍，端着威士忌，站在二楼阳台上，冷冷地低头看着楼下画面外的莉莉，开口。", "0—6秒基利安侧面中景，镜头固定。",
       ('KillianRobe', "She is. Take her to my room.", 1.0),
       f"A steady medium shot opens from the adopted first frame in {V}: {KR} in profile facing frame-left at the stone balustrade, the whiskey tumbler in his right hand, his eyes lowered on the woman below at frame-left, just outside the frame. "
       "He speaks slowly and without hurry, his voice low and cold. The glass stays still in his hand. The camera holds still.",
       "从开场图继续，基利安中景：侧脸朝左站在石栏杆边，右手端着威士忌杯，目光低下去看着左边画面外楼下的女人。他慢慢地、不急不缓地开口，声音低而冷。酒杯在手里不动。镜头固定。",
       voiced("Cold wind and a faint clink of ice in the glass.", "冷风声和杯中冰块轻轻的碰撞声。"))

# 06 莉莉猛地抬头
b.task('06｜协议里没说', 6, ['LilyCoat'], ('villa_front', 'lily_coat'), ['villa_front'],
       "Medium close-up of Lily alone, chest-up, in profile facing frame-right, centered in the middle third of the frame, in the faded grey wool coat, her chin lifted and her eyes fixed on a man on the balcony above at frame-right, just outside the frame, "
       "her eyes wide and her lips parted. Nobody else is in the frame." + LAY,
       END,
       "莉莉抬起头，瞪大眼睛看着右上方画面外阳台上的基利安，说话。", "0—6秒莉莉侧面中近景，镜头固定。",
       ('LilyCoat', "Your room? The contract never said that!", 0.8),
       f"A steady medium close-up opens from the adopted first frame in {V}: {LC} in profile facing frame-right, her chin lifted, her eyes fixed on the man above at frame-right, just outside the frame. "
       "She speaks sharply, her voice shaking with alarm and anger. Only her head and lips move. The camera holds still.",
       "从开场图继续，莉莉近景：侧脸朝右，下巴抬起，目光盯着右上方画面外的男人。她尖声说话，声音因惊慌和愤怒而发颤。只有头和嘴唇在动。镜头固定。",
       voiced("Cold wind.", "冷风声。"))

# 07 阳台上空了（用剪辑表现“瞬间消失”）
b.task('07｜阳台空了', 5, [], VIL, ['villa_front'],
       "Medium shot of the empty second-floor stone balcony above the entrance steps, the stone balustrade centered in the middle third of the frame, a crystal whiskey tumbler with amber whiskey standing on the balustrade, nobody there." + LAY,
       END,
       "二楼阳台上已经没有人了，石栏杆上只留着那只威士忌酒杯。", "0—5秒空阳台中景，镜头固定。",
       None,
       f"A steady medium shot opens from the adopted first frame in {V}: the empty stone balcony, the whiskey tumbler standing on the balustrade. "
       "The glass stays perfectly still. Cold wind stirs the dark pine trees behind. Nobody is visible. The camera holds still.",
       "从开场图继续，中景：空的石头阳台，威士忌酒杯放在栏杆上。酒杯一动不动。冷风吹动后面的深色松树。没有人入画。镜头固定。",
       silent("Cold wind in the pine trees, then a sudden low rush of air.", "冷风吹过松林，然后一阵突然的低沉气流声。"))

# 08 逼到车门（大姿势在开场图里）
b.task('08｜你抵押的全部', 6, ['LilyCoat', 'KillianRobe'], ('villa_front', 'lily_coat', 'killian_robe'), ['villa_front'],
       "Medium two-shot, waist-up, in profile, both people centered in the middle third of the frame. Lily stands at frame-left with her back flat against the black door of the Maybach, her eyes wide and fixed on Killian's face, her battered suitcase on the gravel at her feet; "
       "Killian stands at frame-right facing her, very close, in the black silk robe, his right forearm braced on the car roof above and beside her head, his whole right arm in the frame, his left hand at his side, his eyes lowered on her face. Nobody else is in the frame." + LAY,
       END,
       "基利安已经站在莉莉面前，把她逼到车门上，一只手撑在车顶，低头看着她，开口。", "0—6秒侧面中景，两人居中，莉莉在左、基利安在右，镜头固定。",
       ('KillianRobe', "Read it again. You pledged everything.", 1.0),
       f"A steady medium two-shot in profile opens from the adopted first frame in {V}: {LC} with her back against the car door, her eyes wide and fixed on {KR}'s face; {KR} close in front of her, his right forearm braced on the car roof. "
       "He speaks low and slowly, his eyes on her face. She does not move. The camera holds still.",
       "从开场图继续，侧面中景：莉莉背靠车门，睁大眼睛盯着基利安的脸；基利安紧贴在她面前，右前臂撑在车顶。他低声缓慢地说话，目光落在她脸上。她不动。镜头固定。",
       voiced("Cold wind and a faint creak of the car body.", "冷风声和车身轻微的吱呀声。"))

# 09 抽走发卡（无台词）
b.task('09｜抽走发卡', 6, ['LilyCoat', 'KillianRobe'], ('villa_front', 'lily_coat', 'killian_robe'), ['villa_front'],
       "Tight side-profile two-shot of heads and shoulders, both people centered in the middle third of the frame. Lily at frame-left has her back against the black car door, her low ponytail held by a small silver hair clip, her eyes fixed on Killian's face; "
       "Killian at frame-right faces her very close, his right hand raised to the silver clip behind her ear, his whole right forearm in the frame, his eyes on her face. Nobody else is in the frame." + LAY,
       END,
       "基利安伸手把莉莉发间的发卡抽走，她的长发散落下来。", "0—6秒侧面近景，两人头肩居中，莉莉在左、基利安在右，镜头固定。",
       None,
       f"A steady tight side-profile two-shot opens from the adopted first frame in {V}: {KR}'s right hand at the silver clip in {LC}'s hair, her eyes fixed on his face. "
       "He draws the clip out between two fingers and her long hair falls loose around her shoulders. Her eyes stay on his. Nobody speaks. The camera holds still.",
       "从开场图继续，侧面近景：基利安的右手在莉莉发间的银发卡上，她的眼睛盯着他的脸。他用两根手指把发卡抽出来，她的长发散落在肩上。她的目光一直停在他眼睛上。无人说话。镜头固定。",
       silent("A tiny click of the clip and the soft rustle of hair falling.", "发卡轻轻的咔哒声和头发散落的沙沙声。"))

# 10 埋进颈窝（成片里在这里切断）
b.task('10｜颈窝', 6, ['LilyCoat', 'KillianRobe'], ('villa_front', 'lily_coat', 'killian_robe'), ['villa_front'],
       "Tight side-profile two-shot of heads and shoulders, both people centered in the middle third of the frame. Killian's face at frame-right is lowered into the curve of Lily's neck, his eyes closed; "
       "Lily at frame-left has her long loose chestnut hair around her shoulders and her eyes wide, her head turned slightly away. No hands are visible. Nobody else is in the frame." + LAY,
       END,
       "基利安低头埋进莉莉的颈窝，深深吸了一口气，再睁开眼，眼神变得极其危险。（成片里在这里切断）", "0—6秒侧面近景，两人头肩居中，莉莉在左、基利安在右，镜头固定。",
       None,
       f"A steady tight side-profile two-shot opens from the adopted first frame in {V}: {KR}'s face lowered into the curve of {LC}'s neck, his eyes closed, her loose hair around her shoulders. "
       "He draws one long slow breath, then his eyes open, dark and intent, his face still against her neck. She does not move. Nobody speaks. The camera holds still.",
       "从开场图继续，侧面近景：基利安的脸埋在莉莉的颈窝里，闭着眼，她的长发散在肩上。他慢慢吸了一口长气，然后睁开眼，眼神深沉而危险，脸仍贴在她的颈边。她不动。无人说话。镜头固定。",
       silent("Faint rustle of hair and cloth, then near silence.", "头发和衣料轻轻的沙沙声，然后几乎无声。"))

b.finish('第4集｜羊入虎口',
         '黑色迈巴赫驶入阴森的半山庄园，莉莉提着旧行李箱下车。老管家称她“女主人”，她慌乱地纠正；二楼阳台上的基利安说“她就是”，要她住进他的房间。她抗议协议里没写，他却转眼出现在她面前，把她逼到车门上，说她抵押的是“全部”，抽走她的发卡，低头埋进她的颈窝。',
         '2026-10-09_第4集_制作稿_英文台词_追加')
