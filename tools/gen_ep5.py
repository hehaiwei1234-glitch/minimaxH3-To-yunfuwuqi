#!/usr/bin/env python3
"""第 5 集“信息素失控”制作稿（追加批次，英语台词，美式口语）——按 8 条通用规律重写，并缩短到 10 个任务（2026-10-09 18:xx）。

为什么短：hh 要用这一集让云服务器在“我分析第 4 集、写第 6 集”的时候有事可做，长度按我的预计耗时定（见说明）。
比旧版（12 个任务 65 秒）去掉：莉莉僵住（03）、莉莉流泪（11，泪并进最后一个任务的开场图）。情节、人物、台词不变。
基于第 4 集 A 版 JSON（style、素材、角色逐字复制，F11），新增：场景 bedroom；人物 lily_shirt、killian_wolf；角色 LilyShirt、KillianWolf。
基利安清醒时用 KillianRobe（第 4 集已有）；“失控”之后用 KillianWolf（人物图里就是发光的暗金色眼睛、尖牙、深色利爪），眼睛和牙不用在片内变化。
亲密场面保持不露骨：全程穿着衣服，只有按住手腕、贴近颈侧；咬下去的瞬间由剪辑黑屏。
承接前段只在“同一批人、同一地点”时打开（02→03→04→05 都是基利安；07→08→09→10 是同一对人）。
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, silent, voiced

BASE = '2026-10-09_第4集_制作稿_英文台词_追加.json'
OUT = '2026-10-09_第5集_制作稿_英文台词_追加'
SERIES_TITLE = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))['title']
b = Batch(BASE, SERIES_TITLE, 3400)

# ---- 新素材、新角色（提示词里去掉了 No people / not any people / slightly 这类写法）-----------------------------
b.scene('bedroom', '庄园主卧',
        ("The master bedroom of a dark luxurious mansion: a huge dark-wood bed with charcoal-grey linen against the left wall, a tall single dark-wood door with a brass handle in the right wall, "
         "floor-to-ceiling windows with heavy dark curtains at the back, a dark rug, bedside lamps giving a low amber light, and a small bar cart with crystal glasses near the door. The reference fixes the layout and decor."),
        ("阴暗奢华的庄园主卧：左墙边是一张巨大的深色实木床，配炭灰色床品；右墙有一扇带黄铜把手的高大单扇深色木门；后面是落地窗和厚重的深色窗帘；深色地毯，床头灯发出低低的琥珀色光；门边有一个放着水晶杯的小酒车。参考图固定布局与陈设。"),
        ("A photorealistic ultra-wide 8:3 cinemascope shot of the master bedroom of a dark luxurious mansion: a huge dark-wood bed with charcoal-grey linen against the left wall, a tall single dark-wood door with a brass handle in the right wall, "
         "floor-to-ceiling windows with heavy dark curtains at the back, a dark rug, bedside lamps giving a low amber light, a small bar cart with crystal glasses near the door. The frame holds the bed, the door, the windows and the bar cart."))
b.person('lily_shirt', '莉莉（宽大男士衬衫）',
         ("Lily, the same adult woman in her mid-twenties as in the reference, with long wavy chestnut-brown hair damp and loose around her shoulders, fair skin and large hazel-green eyes, a bare face, "
          "wearing an oversized white men's cotton dress shirt that falls to mid-thigh with the sleeves too long, buttoned to the collarbone. The portrait fixes her identity and clothes, not staging."),
         "莉莉，和参考图是同一个二十五岁左右的成年女性，栗棕色长卷发半湿地披在肩上，白皙皮肤、浅褐绿色大眼睛，素颜，穿一件宽大的白色男士棉质衬衫，下摆到大腿中部，袖子太长，扣子扣到锁骨。人物图固定身份与衣服，不固定站位。",
         ("A photorealistic half-body portrait of the same woman as in the reference image, long wavy chestnut-brown hair damp and loose around her shoulders, a bare face, "
          "wearing an oversized white men's cotton dress shirt buttoned to the collarbone with sleeves too long. She faces the camera with a nervous expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores."),
         ref='lily')
b.person('killian_wolf', '基利安（失控）',
         ("Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short black hair, a sharp jawline and light stubble, wearing a black silk robe tied at the waist, "
          "his eyes glowing a dark gold, with sharp canine teeth and dark claw-like nails. The portrait fixes his identity, clothes and features, not staging."),
         "基利安，和参考图是同一个三十出头、身材极高、肩膀宽阔的成年男性，黑色短发，下颌线锋利，有浅胡茬，穿黑色真丝睡袍、腰间系带，这次眼睛发出暗金色的光，犬齿尖利，指甲像深色的利爪。人物图固定身份、衣服和特征，不固定站位。",
         ("A photorealistic half-body portrait of the same man as in the reference image, short black hair, sharp jawline, light stubble, wearing a black silk robe tied at the waist, "
          "his eyes glowing a dark gold, sharp canine teeth just visible, dark claw-like nails. He faces the camera with an intense, barely restrained expression. "
          "Soft even studio light, plain neutral gray background, natural skin texture with visible pores."),
         ref='killian')
b.character('LilyShirt', 'lily_shirt',
            "A young adult female voice, light and slightly breathy, speaking clear American English. Every word is fully voiced and audible, tight and trembling with fear; her voice rises sharply when she is frightened.",
            "年轻成年女声，轻而略带气息，说清楚的美式英语。每个字都正常发声、清晰可辨，声音紧绷发颤、带着恐惧；受惊时声音会猛地拔高。")
b.character('KillianWolf', 'killian_wolf',
            "A mature adult male voice, extremely deep and rough, like a low animal growl shaped into words, speaking clear American English, hoarse and shaking with barely held restraint. Every word is fully voiced and audible.",
            "成熟成年男声，极其低沉粗糙，像野兽的低吼被压成了字句，说清楚的美式英语，沙哑、因勉强压住的克制而发抖。每个字都正常发声、清晰可辨。")

BD = '[[asset:bedroom]]'; LS = '[[asset:lily_shirt]]'; KR = '[[asset:killian_robe]]'; KW = '[[asset:killian_wolf]]'
LAY_R = " Fixed stage layout: the huge dark-wood bed is at frame-left; the single dark-wood door is at frame-right."
LAY_LK = LAY_R + " Lily is always at frame-left of Killian."
END = " Low amber lamp light, the bedroom softly blurred behind."
Z_END = "低低的琥珀色灯光，卧室在后面柔和虚化。"
Z_R = "固定布局：巨大的深色实木床在画面左边；单扇深色木门在画面右边。"
Z_LK = Z_R + "莉莉始终在基利安左边。"
BED = ('bedroom',)
ZH = []


def T(flag, title, dur, chars, assets, refs, img, end, img_zh, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound):
    s = b.task(title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound)
    s['depends_on_previous'] = flag
    ZH.append(img_zh)


# 01 莉莉坐在床沿 ---------------------------------------------------------------------------------------
T(False, '01｜床沿', 6, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
  "Medium shot of Lily alone, full body, sitting on the edge of the huge dark-wood bed at frame-left, in the middle third of the frame, in profile facing frame-right, "
  "in the oversized white men's shirt, her damp hair loose, both hands pressed between her knees, her eyes on the dark door at frame-right. The frame holds exactly one person, Lily.",
  END + LAY_R,
  "莉莉一个人的中景，全身，坐在画面左边那张巨大的深色实木床的床沿，在画面中间三分之一，侧身朝画面右边，穿宽大的白色男士衬衫，半湿的头发披散着，双手夹在两膝之间，眼睛看着画面右边的深色木门。画面里恰好一个人：莉莉。" + Z_END + Z_R,
  "莉莉刚洗完澡，穿着宽大的男士衬衫，紧张地坐在大床边缘，看着右边的门。", "0—6秒莉莉侧面中景，镜头固定。", None,
  f"A steady medium shot opens from the adopted first frame in {BD}: {LS} alone on the edge of the bed, in profile facing frame-right, her hands pressed between her knees, her eyes on the door at frame-right. "
  "She swallows and her shoulders rise. Her body stays where it is. The camera holds still.",
  "一个稳定的中景，从已采用的开场图继续，场景是主卧：莉莉一个人坐在床沿，侧身朝画面右边，双手夹在膝盖之间，眼睛看着画面右边的门。她咽了一下，肩膀抬起。身体留在原处。镜头固定不动。",
  silent("Quiet room tone and a faint hum of the night outside.", "安静的房间底噪和窗外夜里轻微的嗡声。"))

# 02 基利安站在门口 -------------------------------------------------------------------------------------
T(False, '02｜门口', 6, ['KillianRobe'], ('bedroom', 'killian_robe'), ['bedroom'],
  "Medium shot of Killian alone, full body, standing just inside the open doorway at frame-right, in the middle third of the frame, in profile facing frame-left, in the black silk robe, "
  "a crystal whiskey tumbler in his right hand, his left hand resting on the edge of the open door, his eyes fixed on a woman sitting at frame-left, just outside the frame. The frame holds exactly one person, Killian.",
  END + LAY_R,
  "基利安一个人的中景，全身，站在画面右边敞开的门口里面一点，在画面中间三分之一，侧身朝画面左边，穿黑色真丝睡袍，右手端着水晶威士忌杯，左手搭在敞开的门边上，眼睛盯着坐在画面左边、画面之外的女人。画面里恰好一个人：基利安。" + Z_END + Z_R,
  "基利安站在打开的门口，左手扶着门，右手端着威士忌杯，目光落在左边画面外的莉莉身上。", "0—6秒基利安侧面中景，镜头固定。", None,
  f"A steady medium shot opens from the adopted first frame in {BD}: {KR} in profile facing frame-left in the open doorway, the tumbler in his right hand, his left hand on the door edge, his eyes fixed on the woman at frame-left, just outside the frame. "
  "He stands motionless and his jaw tightens. The camera holds still.",
  "一个稳定的中景，从已采用的开场图继续，场景是主卧：基利安侧身朝画面左边站在敞开的门口，右手端着酒杯，左手扶着门边，眼睛盯着画面左边、画面之外的女人。他一动不动，下颌收紧。镜头固定不动。",
  silent("A heavy, low stillness in the room and the faint clink of ice in the glass.", "房间里沉重的、低低的静，杯中冰块轻轻的碰撞声。"))

# 03 闻到香气（同一个人、同一个地点，承接前段）------------------------------------------------------------
T(True, '03｜深吸一口气', 5, ['KillianRobe'], ('bedroom', 'killian_robe'), ['bedroom'],
  "Close-up of Killian alone, chest-up, in profile facing frame-left, in the middle third of the frame, in the black silk robe, his eyes closed, his nostrils flared, his jaw tight. The frame holds exactly one person, Killian.",
  END + LAY_R,
  "基利安一个人的近景，胸部以上，侧身朝画面左边，在画面中间三分之一，穿黑色真丝睡袍，闭着眼，鼻翼张开，下颌紧绷。画面里恰好一个人：基利安。" + Z_END + Z_R,
  "基利安闭着眼，鼻翼张开，深深吸了一口气。", "0—5秒基利安侧面近景，镜头固定。", None,
  f"A steady close-up opens from the adopted first frame in {BD}: {KR}'s face in profile facing frame-left, his eyes closed. "
  "His chest rises with one slow deep breath and his jaw tightens. His eyes stay closed. The camera holds still.",
  "一个稳定的近景，从已采用的开场图继续，场景是主卧：基利安侧脸朝画面左边，闭着眼。他的胸口随一次缓慢的深呼吸抬起，下颌收紧。眼睛一直闭着。镜头固定不动。",
  silent("A heavy, low stillness in the room.", "房间里沉重的、低低的静。"))

# 04 暗金色的瞳孔（用 KillianWolf 的人物图，眼睛在开场图里就是发光的）--------------------------------------------
T(True, '04｜暗金色的眼睛', 5, ['KillianWolf'], ('bedroom', 'killian_wolf'), ['bedroom'],
  "Close-up of Killian alone, chest-up, in profile facing frame-left, in the middle third of the frame, his eyes open and glowing a dark gold, his jaw tight, his lips pressed together, "
  "his gaze fixed on a woman at frame-left, just outside the frame. The frame holds exactly one person, Killian.",
  END + LAY_R,
  "基利安一个人的近景，胸部以上，侧身朝画面左边，在画面中间三分之一，睁着眼，眼睛发出暗金色的光，下颌紧绷，嘴唇抿紧，目光盯着画面左边、画面之外的女人。画面里恰好一个人：基利安。" + Z_END + Z_R,
  "基利安睁开眼，瞳孔变成发光的暗金色，盯着左边画面外的莉莉。", "0—5秒基利安侧面近景，镜头固定。", None,
  f"A steady close-up opens from the adopted first frame in {BD}: {KW}'s face in profile facing frame-left, his eyes glowing a dark gold, fixed on the woman at frame-left, just outside the frame. "
  "His gaze holds steady and his nostrils flare once. The camera holds still.",
  "一个稳定的近景，从已采用的开场图继续，场景是主卧：基利安侧脸朝画面左边，眼睛发出暗金色的光，盯着画面左边、画面之外的女人。目光稳稳不动，鼻翼张了一下。镜头固定不动。",
  silent("A low, trembling stillness in the room.", "房间里低低的、发颤的静。"))

# 05 酒杯碎裂（手和手臂入画）---------------------------------------------------------------------------
T(True, '05｜酒杯碎裂', 5, ['KillianWolf'], ('bedroom', 'killian_wolf'), ['bedroom'],
  "Close-up of Killian's right hand holding a crystal whiskey tumbler at chest height, in the middle third of the frame, long dark claw-like nails pressing into the glass, "
  "the black silk sleeve, his forearm and part of his chest in the frame so the hand clearly belongs to him. The frame holds exactly one person, Killian.",
  END + LAY_R,
  "基利安右手握着水晶威士忌杯的特写，手在胸口的高度，在画面中间三分之一，深色的利爪压在玻璃上，黑色真丝袖子、前臂和一部分胸口都在画面里，一看就知道这只手是他的。画面里恰好一个人：基利安。" + Z_END + Z_R,
  "基利安右手握着威士忌杯，深色的利爪压进玻璃，杯子裂开、碎掉，酒流下他的手指。", "0—5秒基利安的手和酒杯特写，手臂和胸口入画，镜头固定。", None,
  f"A steady close-up opens from the adopted first frame in {BD}: {KW}'s right hand around the crystal tumbler, the dark claws pressing into the glass. "
  "The glass cracks across, bursts into pieces and falls, and amber whiskey runs over his fingers. His hand stays clenched. The camera holds still.",
  "一个稳定的特写，从已采用的开场图继续，场景是主卧：基利安的右手握着水晶酒杯，深色利爪压进玻璃。杯子裂开，碎成几块落下，琥珀色的酒流过他的手指。手一直握紧。镜头固定不动。",
  silent("One sharp crack, then crystal glass shattering and the patter of whiskey on the floor.", "一声尖锐的裂响，然后水晶玻璃碎裂，酒液滴落在地上的声音。"))

# 06 莉莉尖叫缩向床头 ----------------------------------------------------------------------------------
T(False, '06｜你的眼睛', 6, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
  "Medium close-up of Lily alone, chest-up, pressed back against the dark headboard of the bed at frame-left, in the middle third of the frame, in profile facing frame-right, "
  "in the oversized white men's shirt, both hands clutching the collar closed at her throat, her knees drawn up, her eyes wide with terror on a man at frame-right, just outside the frame. The frame holds exactly one person, Lily.",
  END + LAY_R,
  "莉莉一个人的中近景，胸部以上，背紧贴着画面左边床的深色床头板，在画面中间三分之一，侧身朝画面右边，穿宽大的白色男士衬衫，双手揪紧喉咙处的领口，膝盖蜷起，吓得睁大眼睛，看着画面右边、画面之外的男人。画面里恰好一个人：莉莉。" + Z_END + Z_R,
  "莉莉缩在床头，双手揪紧衬衫领口，吓得睁大眼睛，看着右边画面外的基利安，喊出声。", "0—6秒莉莉侧面中近景，镜头固定。",
  ('LilyShirt', "Killian! Your eyes!", 0.8),
  f"A steady medium close-up opens from the adopted first frame in {BD}: {LS} pressed back against the headboard, her hands clutching her collar, her eyes wide with terror on the man at frame-right, just outside the frame. "
  "She cries out in a high, shaking voice. Her body stays pressed back. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是主卧：莉莉背紧贴着床头，双手揪着领口，吓得睁大眼睛，盯着画面右边、画面之外的男人。她用又高又抖的声音喊出来。身体一直紧贴着床头。镜头固定不动。",
  voiced("Quiet room tone.", "安静的房间底噪。"))

# 07 压在床上（扑上来的动作由剪辑省掉，起始姿势放进开场图；全程穿着衣服）--------------------------------------
HANDS = ("his right hand holding her wrist pressed into the mattress beside her head, his left hand braced flat on the mattress beside her shoulder, both his whole forearms in the frame")
HANDS_ZH = "他的右手把她的手腕按在她头旁的床垫上，左手平撑在她肩旁的床垫上，两条前臂都完整在画面里"
T(False, '07｜按在床上', 6, ['LilyShirt', 'KillianWolf'], ('bedroom', 'lily_shirt', 'killian_wolf'), ['bedroom'],
  "Medium two-shot from the side, both people in the middle third of the frame. Lily lies on her back on the charcoal bedding with her head at frame-left, her chestnut hair spread on the pillow, in the oversized white men's shirt, her eyes wide and fixed on Killian's face, her free hand open on the pillow; "
  f"Killian kneels over her at frame-right in the black silk robe, {HANDS}, his glowing dark-gold eyes fixed on her face. The frame holds exactly two people: Lily and Killian.",
  END + LAY_LK,
  f"侧面的中景双人镜头，两个人都在画面中间三分之一。莉莉仰躺在炭灰色床品上，头在画面左边，栗棕色的头发散在枕头上，穿宽大的白色男士衬衫，睁大眼睛盯着基利安的脸，没被按住的那只手摊开放在枕头上；基利安穿黑色真丝睡袍，跪在画面右边俯身压着她，{HANDS_ZH}，发光的暗金色眼睛盯着她的脸。画面里恰好两个人：莉莉和基利安。" + Z_END + Z_LK,
  "基利安已经压在莉莉身上，一只手把她的手腕按在床垫上，发光的暗金色眼睛盯着她。她睁大眼睛看着他。", "0—6秒侧面中景，两人居中，莉莉在左、基利安在右，镜头固定。", None,
  f"A steady medium two-shot opens from the adopted first frame in {BD}: {LS} on her back on the bed, her wrist held to the mattress by {KW}'s right hand, her eyes wide and fixed on his face; his glowing dark-gold eyes fixed on hers. "
  "Her chest rises and falls fast; his shoulders heave with each heavy breath. Both stay in place. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是主卧：莉莉仰躺在床上，手腕被基利安的右手按在床垫上，睁大眼睛盯着他的脸；他发光的暗金色眼睛盯着她的眼睛。她的胸口起伏很快；他的肩膀随着粗重的呼吸起伏。两人都留在原处。镜头固定不动。",
  silent("The slow creak of bedsprings settling, then a heavy silence.", "床垫慢慢落定的吱呀声，然后沉重的寂静。"))

# 08 野兽低吼（上半句）-----------------------------------------------------------------------------------
T(True, '08｜你好香', 5, ['LilyShirt', 'KillianWolf'], ('bedroom', 'lily_shirt', 'killian_wolf'), ['bedroom'],
  "Tight side-profile two-shot, chest-up, both people in the middle third of the frame. Killian's face at frame-right is lowered beside Lily's neck, his lips an inch from her skin, his glowing dark-gold eyes open, "
  f"{HANDS}; Lily at frame-left lies with her head turned away on the pillow, her eyes squeezed shut, her free hand open on the pillow. The frame holds exactly two people: Lily and Killian.",
  END + LAY_LK,
  f"侧面的近景双人镜头，胸部以上，两个人都在画面中间三分之一。基利安在画面右边，脸低下贴近莉莉的颈侧，嘴唇离她的皮肤只有一寸，发光的暗金色眼睛睁着，{HANDS_ZH}；莉莉在画面左边躺着，头转向一边靠在枕头上，眼睛紧闭，没被按住的那只手摊开放在枕头上。画面里恰好两个人：莉莉和基利安。" + Z_END + Z_LK,
  "基利安低头贴近莉莉的颈侧，用野兽般的低吼开口，莉莉闭紧眼睛。", "0—5秒侧面近景，两人居中，莉莉在左、基利安在右，镜头固定。",
  ('KillianWolf', "You smell so good.", 0.8),
  f"A steady tight side-profile two-shot opens from the adopted first frame in {BD}: {KW}'s face beside {LS}'s neck, his lips an inch from her skin, his eyes glowing dark gold. "
  "He speaks in a deep, rough, growling voice. Her eyes stay squeezed shut. The camera holds still.",
  "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是主卧：基利安的脸贴在莉莉颈边，嘴唇离她的皮肤只有一寸，眼睛发出暗金色的光。他用低沉粗糙的、野兽般的声音说话。她的眼睛一直紧闭。镜头固定不动。",
  voiced("A low, trembling stillness in the room.", "房间里低低的、发颤的静。"))

# 09 野兽低吼（下半句）；牙抵在脖子上 -------------------------------------------------------------------
T(True, '09｜五年', 6, ['LilyShirt', 'KillianWolf'], ('bedroom', 'lily_shirt', 'killian_wolf'), ['bedroom'],
  "Tight side-profile two-shot, chest-up, both people in the middle third of the frame. Killian's face at frame-right is lowered at the side of Lily's throat, his lips drawn back from sharp canine teeth that rest against her skin, his glowing dark-gold eyes open, "
  f"{HANDS}; Lily at frame-left lies with her chin tilted up and her eyes squeezed shut, her free hand open on the pillow. The frame holds exactly two people: Lily and Killian.",
  END + LAY_LK,
  f"侧面的近景双人镜头，胸部以上，两个人都在画面中间三分之一。基利安在画面右边，脸低下贴在莉莉喉咙一侧，嘴唇向后掀开，露出尖利的犬齿抵在她的皮肤上，发光的暗金色眼睛睁着，{HANDS_ZH}；莉莉在画面左边躺着，下巴抬起，眼睛紧闭，没被按住的那只手摊开放在枕头上。画面里恰好两个人：莉莉和基利安。" + Z_END + Z_LK,
  "基利安的尖牙抵在莉莉的脖子上，用低吼说出下半句。", "0—6秒侧面近景，两人居中，莉莉在左、基利安在右，镜头固定。",
  ('KillianWolf', "Five years dreaming of devouring you.", 1.0),
  f"A steady tight side-profile two-shot opens from the adopted first frame in {BD}: {KW}'s sharp teeth resting against the side of {LS}'s throat, his eyes glowing dark gold, her chin tilted up, her eyes squeezed shut. "
  "He speaks in the same deep, rough, growling voice, his teeth resting on her skin. She stays still. The camera holds still.",
  "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是主卧：基利安的尖牙抵在莉莉脖子的一侧，眼睛发出暗金色的光；她下巴抬起，眼睛紧闭。他用同样低沉粗糙的、野兽般的声音说话，牙齿一直抵在她的皮肤上。她一动不动。镜头固定不动。",
  voiced("A low, trembling stillness in the room.", "房间里低低的、发颤的静。"))

# 10 低头（成片里在这里黑屏、接重音效；莉莉的泪并进开场图）-------------------------------------------------
T(True, '10｜低下头', 5, ['LilyShirt', 'KillianWolf'], ('bedroom', 'lily_shirt', 'killian_wolf'), ['bedroom'],
  "Tight side-profile two-shot, chest-up, both people in the middle third of the frame. Killian's face at frame-right is a hand's width above the side of Lily's throat, his lips drawn back from sharp canine teeth, his glowing dark-gold eyes open, "
  f"{HANDS}; Lily at frame-left lies with her chin tilted up and her eyes squeezed shut, a tear on her temple, her free hand open on the pillow. The frame holds exactly two people: Lily and Killian.",
  END + LAY_LK,
  f"侧面的近景双人镜头，胸部以上，两个人都在画面中间三分之一。基利安在画面右边，脸在莉莉喉咙一侧上方一掌宽的地方，嘴唇向后掀开露出尖利的犬齿，发光的暗金色眼睛睁着，{HANDS_ZH}；莉莉在画面左边躺着，下巴抬起，眼睛紧闭，太阳穴上有一滴泪，没被按住的那只手摊开放在枕头上。画面里恰好两个人：莉莉和基利安。" + Z_END + Z_LK,
  "基利安的头压向莉莉的脖子，她下巴抬起、闭紧眼睛，一滴泪滑进头发。（成片里在这里黑屏、接重音效）", "0—5秒侧面近景，两人居中，莉莉在左、基利安在右，镜头固定。", None,
  f"A steady tight side-profile two-shot opens from the adopted first frame in {BD}: {KW}'s face a hand's width above the side of {LS}'s throat, his eyes glowing dark gold, her eyes squeezed shut. "
  "His head lowers the last few centimetres toward her neck and her chin tilts up and away; a tear runs from the corner of her eye into her hair. The camera holds still.",
  "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是主卧：基利安的脸在莉莉脖子一侧上方一掌宽的地方，眼睛发出暗金色的光，她闭紧眼睛。他的头朝她的脖子又低下最后几厘米，她的下巴抬起、偏向一边；一滴泪从她的眼角滑进头发里。镜头固定不动。",
  silent("A low, trembling stillness, then dead silence.", "房间里低低的、发颤的静，然后死寂。"))

b.finish('第5集｜信息素失控',
         '主卧里，刚洗完澡、穿着基利安宽大衬衫的莉莉紧张地坐在床边。基利安走进来，闻到她身上的香味，眼睛变成发光的暗金色，指甲长成利爪，捏碎了手里的酒杯。莉莉尖叫着缩向床头，他像野兽一样扑上来按住她，用低吼说出“五年了，我每天都在想把你吞下去”，尖牙抵在她的脖子上。她绝望地闭上眼，一滴泪滑落；他的头压了下去。',
         OUT)

# ---- 说明 -------------------------------------------------------------------------------------------------
segs = b.d['episodes'][0]['segments']
total = sum(s['duration_seconds'] for s in segs)
md = []
md.append("# 第 5 集（英语台词、追加批次）：怎么用（2026-10-09，按 8 条通用规律重写，缩短版）\n")
md.append(f"文件：`{OUT}_全选复制粘贴.txt`（和同名 `.json` 内容一样）。**{len(segs)} 个任务，8:3 宽屏，合计 {total} 秒，种子 3401–3410。** 这一版**替换**旧的 12 个任务版（写在规律整理之前，请不要再用）。\n")
md.append("## 一、为什么只有这么长\n")
md.append(f"这一集是用来让云服务器在我分析第 4 集、写第 6 集的时候有事可做。我估计从你传回第 4 集视频到我交出第 6 集，大约要 70–90 分钟（分析 30–40 分钟 + 你看我列的问题点 10–15 分钟 + 写第 6 集 25–30 分钟）。按每个任务约 7 分钟估（这个数只是上限推算：第 2 集 12 个任务，从你重新提交到你反馈不到 1.5 小时；不是实测），{len(segs)} 个任务约 {len(segs)*7} 分钟。**你机器跑一个任务实际要几分钟，告诉我一个数，我可以加任务或减任务。**\n")
md.append("## 二、怎么跑\n")
md.append("1. 接在第 4 集 A 版之后追加（素材和角色沿用第 4 集 A，和它的声明逐字相同）。如果你也跑了第 4 集的 B、C，放在它们前面或后面都行，但每一份要等上一份全部跑完才能追加。\n2. 设置照旧：视频/对白共用次数 = 1，对白时间余量 = 0。追加窗口不要勾“每集／总／任务秒数”。\n3. 承接前段只在“同一批人、同一地点”时打开（见下表“承接”一列），换人时关掉。\n4. 重做某一段，会连带重做它后面“承接”的段落。\n")
md.append("## 三、10 个任务\n")
md.append("| 号 | 名字 | 秒 | 在场 | 承接 | 英语台词 | 种子 |\n|---|---|---|---|---|---|---|")
for i, s in enumerate(segs):
    dl = f"{s['dialogue'][0]['speaker']}：{s['dialogue'][0]['text']}" if s['dialogue'] else '（无台词）'
    md.append(f"| {i+1:02d} | {s['title'].split('｜')[1]} | {s['duration_seconds']} | {len(s['characters'])} | {'是' if s['depends_on_previous'] else '否'} | {dl} | {s['seed']} |")
md.append("\n## 四、给 H3 的提示词（中文全译，一个字不漏）\n")
md.append("每个任务的视频提示词前面还会加这句固定的风格话：**“真人实拍，电影感，写实，皮肤有自然质感，浅景深，温暖奢华的光线，超宽 8:3 宽银幕画面。”** 开场图提示词前面也有一段固定的开头：**“一张来自写实真人浪漫惊悚片的完整首帧，超宽 8:3 宽银幕构图。皮肤自然，能看到毛孔，布料和材质真实。固定的场景参考图决定地点，人物肖像只决定被点名的人。”** 下面不再重复。\n")
for i, s in enumerate(segs):
    md.append(f"### {i+1:02d}｜{s['title'].split('｜')[1]}（{s['duration_seconds']} 秒）")
    md.append(f"- **开场图：** {ZH[i]}")
    md.append(f"- **视频：** {s['shots'][0]['visual_zh']}")
    md.append(f"- **声音：** {s['sound_zh']}")
    if s['dialogue']:
        md.append(f"- **台词（单独传给插件）：** {s['dialogue'][0]['speaker']}：“{s['dialogue'][0]['text']}”")
    md.append("")
md.append("## 五、和旧版的区别\n")
md.append("- 去掉“莉莉僵住”和“莉莉流泪”两个任务（泪并进最后一个任务的开场图），情节、台词不变。\n- 不再写 “Nobody else / No hands are visible”，人数写成 “exactly N people”；去掉 slightly / only 这类程度词。\n- 贴身镜头每只手都写清楚：基利安的右手按着她的手腕、左手平撑床垫，莉莉的另一只手摊开在枕头上。\n- 亲密场面保持不露骨：全程穿着衣服，只有按住手腕、牙齿贴着脖子；咬下去的一瞬由成片里的黑屏表现。\n- “扑上床”的动作不拍（H3 做不稳），起始姿势直接放进开场图。\n")
md.append("## 六、我预计会出问题的地方（没试过，只是判断）\n")
md.append("- **05 号酒杯碎裂**要靠 H3 把“利爪压进玻璃”做对，可能是杯子自己碎或手穿过杯子。\n- **04 号**用另一张人物图（失控版），承接前段的位置参考来自闭着眼的 03 号，眼睛颜色是否对要看开场图。\n- **07–10 号**是贴身镜头，没有试验数据；尖牙抵脖子这一类可能出现牙齿或手变形。\n- **台词**照旧：声音常常到片尾才结束，验收时听结尾（06、08、09 号）。\n")
open(os.path.join(FOLDER, '2026-10-09_第5集_说明_英文台词_追加.md'), 'w', encoding='utf-8').write('\n'.join(md))
print('说明已写')
