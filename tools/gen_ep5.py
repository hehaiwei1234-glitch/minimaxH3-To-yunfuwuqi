#!/usr/bin/env python3
"""生成《Alpha继兄的笼中吻》第 5 集“信息素失控”制作稿（追加批次，英语台词，美式口语）。
基于第 4 集 JSON（style、素材、角色逐字复制），新增：场景 bedroom；人物 lily_shirt、killian_wolf（用 lily/killian 作参考图）；角色 LilyShirt、KillianWolf。
基利安清醒时用第 4 集的 KillianRobe；“失控”之后用 KillianWolf（人物图里就是暗金色发光的眼睛、尖牙、深色利爪，声音描述是野兽般的低吼），
这样眼睛和牙不用在片内变化。亲密场面保持不露骨：全程穿着衣服，只有按住手腕、贴近颈侧；咬下去的瞬间由剪辑黑屏。
验证的假设同第 3 集（手册 7.10 的 H14–H16，7.11）。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, silent, voiced

b = Batch('2026-10-09_第4集_制作稿_英文台词_追加.json', 'Alpha继兄的笼中吻｜第5集｜信息素失控', 3400)

b.scene('bedroom', '庄园主卧',
        ("The master bedroom of a dark luxurious mansion: a huge dark-wood bed with charcoal-grey linen against the left wall, a tall single dark-wood door with a brass handle in the right wall, "
         "floor-to-ceiling windows with heavy dark curtains at the back, a dark rug, bedside lamps giving a low amber light, and a small bar cart with crystal glasses near the door. The reference fixes the layout and decor, not any people."),
        ("阴暗奢华的庄园主卧：左墙边是一张巨大的深色实木床，配炭灰色床品；右墙有一扇带黄铜把手的高大单扇深色木门；后面是落地窗和厚重的深色窗帘；深色地毯，床头灯发出低低的琥珀色光；门边有一个放着水晶杯的小酒车。参考图固定布局与陈设，不带入任何人物。"),
        ("A photorealistic wide shot of an empty master bedroom of a dark luxurious mansion: a huge dark-wood bed with charcoal-grey linen against the left wall, a tall single dark-wood door with a brass handle in the right wall, "
         "floor-to-ceiling windows with heavy dark curtains at the back, a dark rug, bedside lamps giving a low amber light, a small bar cart with crystal glasses near the door. No people."))
b.person('lily_shirt', '莉莉（宽大男士衬衫）',
         ("Lily, the same adult woman in her mid-twenties as in the reference, with long wavy chestnut-brown hair damp and loose around her shoulders, fair skin and large hazel-green eyes, no makeup, "
          "wearing an oversized white men's cotton dress shirt that falls to mid-thigh with the sleeves too long, buttoned to the collarbone. The portrait fixes her identity and clothes, not staging."),
         "莉莉，和参考图是同一个二十五岁左右的成年女性，栗棕色长卷发半湿地披在肩上，白皙皮肤、浅褐绿色大眼睛，没化妆，穿一件宽大的白色男士棉质衬衫，下摆到大腿中部，袖子太长，扣子扣到锁骨。人物图固定身份与衣服，不固定站位。",
         ("A photorealistic half-body portrait of the same woman as in the reference image, long wavy chestnut-brown hair damp and loose around her shoulders, no makeup, "
          "wearing an oversized white men's cotton dress shirt buttoned to the collarbone with sleeves too long. She faces the camera with a nervous expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores."),
         ref='lily')
b.person('killian_wolf', '基利安（失控）',
         ("Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short black hair, a sharp jawline and light stubble, wearing a black silk robe tied at the waist, "
          "his eyes now glowing a dark gold, with slightly elongated sharp canine teeth and dark claw-like nails. The portrait fixes his identity, clothes and features, not staging."),
         "基利安，和参考图是同一个三十出头、身材极高、肩膀宽阔的成年男性，黑色短发，下颌线锋利，有浅胡茬，穿黑色真丝睡袍、腰间系带，这次眼睛发出暗金色的光，犬齿略长而尖，指甲像深色的利爪。人物图固定身份、衣服和特征，不固定站位。",
         ("A photorealistic half-body portrait of the same man as in the reference image, short black hair, sharp jawline, light stubble, wearing a black silk robe tied at the waist, "
          "his eyes glowing a dark gold, slightly elongated sharp canine teeth just visible, dark claw-like nails. He faces the camera with an intense, barely restrained expression. "
          "Soft even studio light, plain neutral gray background, natural skin texture with visible pores."),
         ref='killian')
b.character('LilyShirt', 'lily_shirt',
            "A young adult female voice, light and slightly breathy, speaking clear American English. Every word is fully voiced and audible, tight and trembling with fear; her voice rises sharply when she is frightened.",
            "年轻成年女声，轻而略带气息，说清楚的美式英语。每个字都正常发声、清晰可辨，声音紧绷发颤、带着恐惧；受惊时声音会猛地拔高。")
b.character('KillianWolf', 'killian_wolf',
            "A mature adult male voice, extremely deep and rough, like a low animal growl shaped into words, speaking clear American English, hoarse and shaking with barely held restraint. Every word is fully voiced and audible.",
            "成熟成年男声，极其低沉粗糙，像野兽的低吼被压成了字句，说清楚的美式英语，沙哑、因勉强压住的克制而发抖。每个字都正常发声、清晰可辨。")

BD = '[[asset:bedroom]]'; LS = '[[asset:lily_shirt]]'; KR = '[[asset:killian_robe]]'; KW = '[[asset:killian_wolf]]'
# H15：固定方位
LAY = " Fixed stage layout: the huge dark-wood bed is at frame-left; the single dark-wood door is at frame-right; Lily is always at frame-left of Killian."
END = " Low amber lamp light, the bedroom softly blurred behind."
BED = ('bedroom',)

# 01 莉莉坐在床沿
b.task('01｜床沿', 6, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
       "Medium shot of Lily alone, full body, sitting on the edge of the huge dark-wood bed at frame-left, centered in the middle third of the frame, in profile facing frame-right, "
       "in the oversized white men's shirt, her damp hair loose, both hands pressed between her knees, her eyes on the dark door at frame-right. Nobody else is in the frame." + LAY,
       END,
       "莉莉刚洗完澡，穿着宽大的男士衬衫，紧张地坐在大床边缘，看着右边的门。", "0—6秒莉莉侧面中景，镜头固定。",
       None,
       f"A steady medium shot opens from the adopted first frame in {BD}: {LS} alone on the edge of the bed, in profile facing frame-right, her hands pressed between her knees, her eyes on the door at frame-right. "
       "She swallows and her shoulders rise slightly. Her body stays where it is. The camera holds still.",
       "从开场图继续，莉莉中景：一个人坐在床沿，侧脸朝右，双手夹在膝盖之间，目光落在右边的门上。她咽了一下，肩膀微微抬起。身体不动。镜头固定。",
       silent("Quiet room tone and a faint hum of the night outside.", "安静的房间底噪和窗外夜里轻微的嗡声。"))

# 02 基利安站在门口
b.task('02｜门口', 6, ['KillianRobe'], ('bedroom', 'killian_robe'), ['bedroom'],
       "Medium shot of Killian alone, full body, standing just inside the open doorway at frame-right, centered in the middle third of the frame, in profile facing frame-left, in the black silk robe, "
       "a crystal whiskey tumbler in his right hand, his left hand resting on the edge of the open door, his eyes fixed on a woman sitting at frame-left, just outside the frame. Nobody else is in the frame." + LAY,
       END,
       "基利安站在打开的门口，左手扶着门，右手端着威士忌杯，目光落在左边画面外的莉莉身上。", "0—6秒基利安侧面中景，镜头固定。",
       None,
       f"A steady medium shot opens from the adopted first frame in {BD}: {KR} in profile facing frame-left in the open doorway, the tumbler in his right hand, his left hand on the door edge, his eyes fixed on the woman at frame-left, just outside the frame. "
       "He stands motionless and only his jaw tightens. Nobody speaks. The camera holds still.",
       "从开场图继续，基利安中景：侧脸朝左站在打开的门口，右手端着酒杯，左手扶着门边，目光盯着左边画面外的女人。他一动不动，只有下颌收紧。无人说话。镜头固定。",
       silent("A heavy, low stillness in the room, the faint clink of ice in the glass.", "房间里沉重的、低低的静，杯中冰块轻轻的碰撞声。"))

# 03 莉莉僵住
b.task('03｜僵住', 5, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
       "Medium close-up of Lily alone, chest-up, in profile facing frame-right, centered in the middle third of the frame, in the oversized white men's shirt, her lips parted, her fingers gripping the edge of the mattress at the bottom of the frame, "
       "her eyes fixed on a man standing at frame-right, just outside the frame. Nobody else is in the frame." + LAY,
       END,
       "莉莉僵在床边，手指抓紧床沿，嘴唇微张，看着右边画面外的基利安。", "0—5秒莉莉侧面中近景，镜头固定。",
       None,
       f"A steady medium close-up opens from the adopted first frame in {BD}: {LS} in profile facing frame-right, her fingers gripping the mattress edge, her eyes fixed on the man at frame-right, just outside the frame. "
       "She goes completely still, only her chest rising and falling fast. Nobody speaks. The camera holds still.",
       "从开场图继续，莉莉近景：侧脸朝右，手指抓着床沿，目光盯着右边画面外的男人。她彻底僵住，只有胸口起伏很快。无人说话。镜头固定。",
       silent("A heavy, low stillness in the room.", "房间里沉重的、低低的静。"))

# 04 闻到香气
b.task('04｜深吸一口气', 5, ['KillianRobe'], ('bedroom', 'killian_robe'), ['bedroom'],
       "Close-up of Killian's face alone, chest-up, in profile facing frame-left, centered in the middle third of the frame, in the black silk robe, his eyes closed, his nostrils slightly flared, his jaw tight. Nobody else is in the frame." + LAY,
       END,
       "基利安闭着眼，鼻翼微张，深深吸了一口气。", "0—5秒基利安侧面近景，镜头固定。",
       None,
       f"A steady close-up opens from the adopted first frame in {BD}: {KR}'s face in profile facing frame-left, his eyes closed. "
       "His chest rises slowly with one deep breath and his jaw tightens further. His eyes stay closed. Nobody speaks. The camera holds still.",
       "从开场图继续，基利安面部近景：侧脸朝左，闭着眼。他的胸口随一次深呼吸慢慢抬起，下颌收得更紧。眼睛一直闭着。无人说话。镜头固定。",
       silent("A heavy, low stillness in the room.", "房间里沉重的、低低的静。"))

# 05 暗金色的瞳孔（用 KillianWolf 的人物图，眼睛在开场图里就是发光的）
b.task('05｜暗金色的眼睛', 5, ['KillianWolf'], ('bedroom', 'killian_wolf'), ['bedroom'],
       "Close-up of Killian's face alone, chest-up, in profile facing frame-left, centered in the middle third of the frame, his eyes open and glowing a dark gold, his jaw tight, his lips pressed together, "
       "his gaze fixed on a woman at frame-left, just outside the frame. Nobody else is in the frame." + LAY,
       END,
       "基利安睁开眼，瞳孔变成发光的暗金色，盯着左边画面外的莉莉。", "0—5秒基利安侧面近景，镜头固定。",
       None,
       f"A steady close-up opens from the adopted first frame in {BD}: {KW}'s face in profile facing frame-left, his eyes glowing a dark gold, fixed on the woman at frame-left, just outside the frame. "
       "His gaze does not waver and his nostrils flare once. Nobody speaks. The camera holds still.",
       "从开场图继续，基利安面部近景：侧脸朝左，眼睛发出暗金色的光，盯着左边画面外的女人。目光一动不动，鼻翼张了一下。无人说话。镜头固定。",
       silent("A low, trembling stillness in the room.", "房间里低低的、发颤的静。"))

# 06 酒杯碎裂（手和手臂入画）
b.task('06｜酒杯碎裂', 5, ['KillianWolf'], ('bedroom', 'killian_wolf'), ['bedroom'],
       "Close-up of Killian's right hand holding a crystal whiskey tumbler at chest height, centered in the middle third of the frame, long dark claw-like nails pressing into the glass, "
       "the black silk sleeve, his forearm and part of his chest in the frame so the hand clearly belongs to him. Nobody else is in the frame." + LAY,
       END,
       "基利安右手握着威士忌杯，深色的利爪压进玻璃，杯子裂开、碎掉，酒流下他的手指。", "0—5秒基利安的手和酒杯特写，手臂和胸口入画，镜头固定。",
       None,
       f"A steady close-up opens from the adopted first frame in {BD}: {KW}'s right hand around the crystal tumbler, the dark claws pressing into the glass. "
       "The glass cracks across, bursts into pieces and falls, and amber whiskey runs over his fingers. His hand stays clenched. Nobody speaks. The camera holds still.",
       "从开场图继续，基利安的右手握着水晶酒杯，深色利爪压进玻璃。杯子裂开，碎成几块落下，琥珀色的酒流过他的手指。手一直握紧。无人说话。镜头固定。",
       silent("One sharp crack, then crystal glass shattering and the patter of whiskey on the floor.", "一声尖锐的裂响，然后水晶玻璃碎裂，酒液滴落在地上的声音。"))

# 07 莉莉尖叫缩向床头
b.task('07｜你的眼睛', 6, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
       "Medium close-up of Lily alone, chest-up, pressed back against the dark headboard of the bed at frame-left, centered in the middle third of the frame, in profile facing frame-right, "
       "in the oversized white men's shirt, both hands clutching the collar closed at her throat, her knees drawn up, her eyes wide with terror on a man at frame-right, just outside the frame. Nobody else is in the frame." + LAY,
       END,
       "莉莉缩在床头，双手揪紧衬衫领口，吓得睁大眼睛，看着右边画面外的基利安，喊出声。", "0—6秒莉莉侧面中近景，镜头固定。",
       ('LilyShirt', "Killian! Your eyes!", 0.8),
       f"A steady medium close-up opens from the adopted first frame in {BD}: {LS} pressed back against the headboard, her hands clutching her collar, her eyes wide with terror on the man at frame-right, just outside the frame. "
       "She cries out in a high, shaking voice. Her body stays pressed back. The camera holds still.",
       "从开场图继续，莉莉近景：背紧贴着床头，双手揪着领口，吓得睁大眼睛，盯着右边画面外的男人。她用又高又抖的声音喊出来。身体一直紧贴着床头。镜头固定。",
       voiced("Quiet room tone.", "安静的房间底噪。"))

# 08 压在身下（扑上来的动作由剪辑省掉，起始姿势放进开场图；全程穿着衣服）
b.task('08｜按在床上', 6, ['LilyShirt', 'KillianWolf'], ('bedroom', 'lily_shirt', 'killian_wolf'), ['bedroom'],
       "Medium two-shot from the side, both people centered in the middle third of the frame. Lily lies on her back on the charcoal bedding with her head at frame-left, her chestnut hair spread on the pillow, in the oversized white men's shirt, her eyes wide and fixed on Killian's face; "
       "Killian kneels over her at frame-right in the black silk robe, both his hands pressing her wrists into the mattress on either side of her head, both his whole arms in the frame, his glowing dark-gold eyes fixed on her face. Nobody else is in the frame." + LAY,
       END,
       "基利安已经压在莉莉身上，双手把她的手腕按在床垫上，发光的暗金色眼睛盯着她。她睁大眼睛看着他。", "0—6秒侧面中景，两人居中，莉莉在左、基利安在右，镜头固定。",
       None,
       f"A steady medium two-shot opens from the adopted first frame in {BD}: {LS} on her back on the bed, her wrists pinned to the mattress by {KW}, her eyes wide and fixed on his face; his glowing dark-gold eyes fixed on hers. "
       "Neither changes position. Her chest rises and falls fast; his shoulders heave with each heavy breath. Nobody speaks. The camera holds still.",
       "从开场图继续，侧面中景：莉莉仰躺在床上，手腕被基利安按在床垫上，睁大眼睛盯着他的脸；他发光的暗金色眼睛盯着她的眼睛。两人姿势都不变。她的胸口起伏很快；他的肩膀随着粗重的呼吸起伏。无人说话。镜头固定。",
       silent("The slow creak of bedsprings settling, then a heavy silence.", "床垫慢慢落定的吱呀声，然后沉重的寂静。"))

# 09 野兽低吼（上半句）
b.task('09｜你好香', 5, ['LilyShirt', 'KillianWolf'], ('bedroom', 'lily_shirt', 'killian_wolf'), ['bedroom'],
       "Tight side-profile two-shot of heads and shoulders, both people centered in the middle third of the frame. Killian's face at frame-right is lowered beside Lily's neck, his lips an inch from her skin, his glowing dark-gold eyes open; "
       "Lily at frame-left lies with her head turned away on the pillow, her eyes squeezed shut. No hands are visible. Nobody else is in the frame." + LAY,
       END,
       "基利安低头贴近莉莉的颈侧，用野兽般的低吼开口，莉莉闭紧眼睛。", "0—5秒侧面近景，两人头肩居中，莉莉在左、基利安在右，镜头固定。",
       ('KillianWolf', "You smell so good.", 0.8),
       f"A steady tight side-profile two-shot opens from the adopted first frame in {BD}: {KW}'s face beside {LS}'s neck, his lips an inch from her skin, his eyes glowing dark gold. "
       "He speaks in a deep, rough, growling voice. She does not move; her eyes stay squeezed shut. The camera holds still.",
       "从开场图继续，侧面近景：基利安的脸贴在莉莉颈边，嘴唇离她的皮肤只有一寸，眼睛发出暗金色的光。他用低沉粗糙的、野兽般的声音说话。她不动，眼睛一直紧闭。镜头固定。",
       voiced("A low, trembling stillness in the room.", "房间里低低的、发颤的静。"))

# 10 野兽低吼（下半句）；牙抵在脖子上（不破皮）
b.task('10｜五年', 6, ['LilyShirt', 'KillianWolf'], ('bedroom', 'lily_shirt', 'killian_wolf'), ['bedroom'],
       "Tight side-profile two-shot of heads and shoulders, both people centered in the middle third of the frame. Killian's face at frame-right is lowered at the side of Lily's throat, his lips drawn back from sharp canine teeth that rest against her skin without breaking it, his glowing dark-gold eyes open; "
       "Lily at frame-left lies with her chin tilted up and her eyes squeezed shut. No hands are visible. Nobody else is in the frame." + LAY,
       END,
       "基利安的尖牙抵在莉莉的脖子上，没有刺破，用低吼说出下半句。", "0—6秒侧面近景，两人头肩居中，莉莉在左、基利安在右，镜头固定。",
       ('KillianWolf', "Five years dreaming of devouring you.", 1.0),
       f"A steady tight side-profile two-shot opens from the adopted first frame in {BD}: {KW}'s sharp teeth resting against the side of {LS}'s throat, his eyes glowing dark gold, her chin tilted up, her eyes squeezed shut. "
       "He speaks in the same deep, rough, growling voice, his teeth never breaking her skin. She does not move. The camera holds still.",
       "从开场图继续，侧面近景：基利安的尖牙抵在莉莉脖子的一侧，眼睛发出暗金色的光；她下巴抬起，眼睛紧闭。他用同样低沉粗糙的、野兽般的声音说话，牙齿始终没有刺破她的皮肤。她不动。镜头固定。",
       voiced("A low, trembling stillness in the room.", "房间里低低的、发颤的静。"))

# 11 莉莉闭眼流泪
b.task('11｜一滴泪', 5, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
       "Close-up of Lily's face alone, lying with her head on the pillow at frame-left, centered in the middle third of the frame, her eyes closed, tears on her lashes, her lips pressed together, her chestnut hair spread on the pillow. Nobody else is in the frame." + LAY,
       END,
       "莉莉的脸特写，闭着眼，一滴泪从眼角滑落。", "0—5秒莉莉面部特写，镜头固定。",
       None,
       f"A steady close-up opens from the adopted first frame in {BD}: {LS}'s face on the pillow, her eyes closed, tears on her lashes. "
       "A single tear runs from the corner of her eye down her temple into her hair. Her face stays still. Nobody speaks. The camera holds still.",
       "从开场图继续，莉莉面部特写：脸靠在枕头上，闭着眼，睫毛上有泪。一滴泪从眼角滑下，经过太阳穴滑进头发里。脸不动。无人说话。镜头固定。",
       silent("A low, trembling stillness in the room.", "房间里低低的、发颤的静。"))

# 12 低头（成片里在这里黑屏、接重音效）
b.task('12｜低下头', 5, ['LilyShirt', 'KillianWolf'], ('bedroom', 'lily_shirt', 'killian_wolf'), ['bedroom'],
       "Tight side-profile two-shot of heads and shoulders, both people centered in the middle third of the frame. Killian's face at frame-right is a hand's width above the side of Lily's throat, his lips drawn back from sharp canine teeth, his glowing dark-gold eyes open; "
       "Lily at frame-left lies with her chin tilted up and her eyes squeezed shut, a tear on her temple. No hands are visible. Nobody else is in the frame." + LAY,
       END,
       "基利安的头压向莉莉的脖子，她下巴抬起、闭紧眼睛。（成片里在这里黑屏、接重音效）", "0—5秒侧面近景，两人头肩居中，莉莉在左、基利安在右，镜头固定。",
       None,
       f"A steady tight side-profile two-shot opens from the adopted first frame in {BD}: {KW}'s face a hand's width above the side of {LS}'s throat, his eyes glowing dark gold, her eyes squeezed shut. "
       "His head lowers the last few centimetres toward her neck and her chin tilts further up and away. Nobody speaks. The camera holds still.",
       "从开场图继续，侧面近景：基利安的脸在莉莉脖子一侧上方一掌宽的地方，眼睛发出暗金色的光，她闭紧眼睛。他的头朝她的脖子又低下最后几厘米，她的下巴抬得更高、偏向一边。无人说话。镜头固定。",
       silent("A low, trembling stillness, then dead silence.", "房间里低低的、发颤的静，然后死寂。"))

b.finish('第5集｜信息素失控',
         '主卧里，刚洗完澡、穿着基利安宽大衬衫的莉莉紧张地坐在床边。基利安走进来，闻到她身上的香味，眼睛变成发光的暗金色，指甲长成利爪，捏碎了手里的酒杯。莉莉尖叫着缩向床头，他像野兽一样扑上来按住她，用低吼说出“五年了，我每天都在想把你吞下去”，尖牙抵在她的脖子上。她绝望地闭上眼，一滴泪滑落；他的头压了下去。',
         '2026-10-09_第5集_制作稿_英文台词_追加')
