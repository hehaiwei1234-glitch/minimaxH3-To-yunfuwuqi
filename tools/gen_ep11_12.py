#!/usr/bin/env python3
"""剧本第 11、12 集（主卧四集的前两集：Luna 血脉、Alpha 的绝对压制）制作稿（2026-10-10）。
后两集和对比测试、合并、说明在 gen_ep13_14.py（它会先 import 本文件，所以只要运行 gen_ep13_14.py 就全部重新生成）。

链式生成：马场合并稿 → 第 11 集（种子 4301–4307）→ 第 12 集（4401–4408）→ 第 13 集（4501–4505）→ 第 14 集（4601–4605）→ B（4701–4703，其中 B1、B2 与正式版同种子做对照）。
新增：场景 corridor；人物 doctor、killian_gold、killian_shirt、killian_beast；
角色 Doctor、GuardFrenzy（用 bodyguard 的图，只出声）、KillianGold、KillianShirt、KillianBeast。

按“Claude 易错点自查清单”写：每个人物每个任务都写表情；没有画外目标；有台词的任务都是 6 秒、≤6 个单词；
承接前段只在同一批人、同一地点、同一景别的相邻任务（每集第一个任务一律关）；最多 2 人；
大冲突的写法按自查清单第 20 条（动作排满整段、不写 stays/remains、无台词片允许呼吸、开场图画动作之前）；亲密戏只到“穿着衣服、非露骨”。
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, silent, voiced, breathy

BASE = '合并稿/合并_第7-10集+10B_制作稿_追加.json'
O11 = '第11集/第11集_制作稿_追加'
O12 = '第12集/第12集_制作稿_追加'
SERIES_TITLE = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))['title']


def maker(batch, zh):
    def T(flag, title, dur, chars, assets, refs, img, end, img_zh, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound):
        s = batch.task(title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound)
        s['depends_on_previous'] = flag
        zh.append(img_zh)
        return s
    return T


BD = '[[asset:bedroom]]'; CO = '[[asset:corridor]]'; LS = '[[asset:lily_shirt]]'; K = '[[asset:killian]]'
KG = '[[asset:killian_gold]]'; KS = '[[asset:killian_shirt]]'; KB = '[[asset:killian_beast]]'
DR = '[[asset:doctor]]'; BGD = '[[asset:bodyguard]]'

LAY_BED = " Fixed stage layout: the huge dark-wood bed with charcoal-grey linen fills the left and center of the frame; the tall dark-wood door with a brass handle is at frame-right; the heavy dark curtains are at the back."
Z_BED = "固定布局：铺着炭灰色亚麻床品的深色木制大床占据画面的左边和中间；带黄铜把手的高大深色木门在画面右边；厚重的深色窗帘在后面。"
END_BED = " Night, low amber lamplight, deep soft shadows in the room."
Z_END_BED = "夜里，低低的琥珀色灯光，房间里是柔和的深深阴影。"
LAY_CO = " Fixed stage layout: the bedroom's tall dark-wood door with a brass handle is set in the long dark-paneled wall at frame-left; amber wall lamps are spaced along the paneling; the corridor runs to frame-right, where a tall arched window shows the night."
Z_CO = "固定布局：卧室里那扇带黄铜把手的高大深色木门嵌在画面左边的深色木板长墙里；琥珀色壁灯沿着护墙板间隔排开；走廊向画面右边延伸，尽头是一扇高高的拱形窗，窗外是夜色。"
END_CO = " Night, warm amber wall lamps, a pale marble floor with a dark runner rug, the corridor deep and dim."
Z_END_CO = "夜里，温暖的琥珀色壁灯，浅色大理石地面铺着深色长条地毯，走廊幽深昏暗。"

a = Batch(BASE, SERIES_TITLE, 4300)
ZH11 = []
T11 = maker(a, ZH11)

# ---------------------------------------------------------------------------------------------------------
# 新素材
# ---------------------------------------------------------------------------------------------------------
a.scene('corridor', '主卧外的走廊',
        "The upstairs corridor of a dark luxurious mansion outside the master bedroom, seen straight on: a long dark-wood paneled wall with a tall dark-wood door with a brass handle set into it at the left, amber wall lamps spaced along the paneling, a pale marble floor with a dark runner rug, and a tall arched window at the far right end showing the night. The reference fixes the layout and decor.",
        "黑暗奢华的庄园里主卧外的二楼走廊，正面看过去：一整面深色木板长墙，左边嵌着一扇带黄铜把手的高大深色木门，琥珀色壁灯沿着护墙板间隔排开，浅色大理石地面铺着深色长条地毯，最右端尽头是一扇高高的拱形窗，窗外是夜色。参考图固定布局与陈设。",
        "A photorealistic ultra-wide 8:3 cinemascope shot of the upstairs corridor of a dark luxurious mansion seen straight on: a long dark-wood paneled wall with a tall dark-wood door with a brass handle set into it at the left, amber wall lamps spaced along the paneling, a pale marble floor with a dark runner rug, a tall arched window at the far right end showing the night sky. "
        "The frame holds the door, the paneled wall, the lamps and the arched window.")
a.person('doctor', '私人医生（狼医）',
         "Doctor, a thin adult man in his fifties with gray hair, wire-rimmed glasses and a lined, worried face, wearing a long white doctor's coat over a gray shirt and a dark tie, a stethoscope around his neck. The portrait fixes his identity and clothes, not staging.",
         "医生，一个五十多岁的瘦削成年男性，灰白头发，戴金属细框眼镜，脸上皱纹很深、神情忧虑，穿长款白大褂，里面是灰衬衫和深色领带，脖子上挂着听诊器。人物图固定身份和衣服，不固定站位。",
         "A photorealistic half-body portrait of a thin adult man in his fifties with gray hair, wire-rimmed glasses and a lined, worried face, wearing a long white doctor's coat over a gray shirt and a dark tie, a stethoscope around his neck. "
         "He faces the camera with a tense, worried expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.")
a.person('killian_gold', '基利安（西装，金瞳狼爪）',
         "Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short swept-back black hair, a sharp jawline and light stubble, wearing a tailored black three-piece suit, a white shirt and a dark tie, a platinum luxury wristwatch on his left wrist; his eyes glow a dark gold, two sharp canine teeth show at the edge of his lips, and long black claws extend from his fingertips. The portrait fixes his identity, clothes and features, not staging.",
         "基利安，和参考图是同一个三十出头、身材极高、肩膀宽阔的成年男性，黑色短发向后梳，下颌线锋利，有浅胡茬，穿合身的黑色三件套西装、白衬衫和深色领带，左手腕戴铂金名表；他的眼睛发出暗金色的光，嘴角露出两颗尖锐的犬齿，指尖长出长长的黑色利爪。人物图固定身份、衣服和特征，不固定站位。",
         "A photorealistic half-body portrait of the same man as in the reference image, short swept-back black hair, sharp jawline, light stubble, wearing a tailored black three-piece suit, a white shirt and a dark tie, his eyes glowing a dark gold, two sharp canine teeth just visible, long black claws on the fingertips of his hands held at his sides. "
         "He faces the camera with an intense, cold expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.",
         ref='killian')
a.person('killian_shirt', '基利安（只穿衬衫）',
         "Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short swept-back black hair, a sharp jawline, light stubble and cold dark-gray eyes, wearing only a white dress shirt with the collar open at the throat and the sleeves rolled to the elbows, a dark tie pulled loose and hanging, dark trousers and a platinum luxury wristwatch on his left wrist, with no jacket and no waistcoat. The portrait fixes his identity and clothes, not staging.",
         "基利安，和参考图是同一个三十出头、身材极高、肩膀宽阔的成年男性，黑色短发向后梳，下颌线锋利，有浅胡茬，眼睛是冷冷的深灰色，只穿一件白色衬衫，领口敞开到喉结，袖子卷到手肘，深色领带扯松了垂着，配深色长裤，左手腕戴铂金名表，没有外套也没有马甲。人物图固定身份和衣服，不固定站位。",
         "A photorealistic half-body portrait of the same man as in the reference image, short swept-back black hair, sharp jawline, light stubble, cold dark-gray eyes, wearing only a white dress shirt with the collar open at the throat and the sleeves rolled to the elbows, a dark tie pulled loose and hanging, a platinum luxury wristwatch on his left wrist. "
         "He faces the camera with a cold, composed expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.",
         ref='killian')
a.person('killian_beast', '基利安（衬衫，竖瞳獠牙）',
         "Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short swept-back black hair, a sharp jawline and light stubble, wearing only a white dress shirt with the collar open at the throat and the sleeves rolled to the elbows, a dark tie pulled loose and hanging, a platinum luxury wristwatch on his left wrist; his eyes glow a dark gold with narrow vertical slit pupils, two long sharp canine teeth show between his parted lips, and long black claws extend from his fingertips. The portrait fixes his identity, clothes and features, not staging.",
         "基利安，和参考图是同一个三十出头、身材极高、肩膀宽阔的成年男性，黑色短发向后梳，下颌线锋利，有浅胡茬，只穿一件白色衬衫，领口敞开到喉结，袖子卷到手肘，深色领带扯松了垂着，左手腕戴铂金名表；他的眼睛发出暗金色的光、瞳孔是细细的竖瞳，微张的嘴唇间露出两颗又长又尖的犬齿，指尖长出长长的黑色利爪。人物图固定身份、衣服和特征，不固定站位。",
         "A photorealistic half-body portrait of the same man as in the reference image, short swept-back black hair, sharp jawline, light stubble, wearing only a white dress shirt with the collar open at the throat and the sleeves rolled to the elbows, a dark tie pulled loose and hanging, his eyes glowing a dark gold with narrow vertical slit pupils, two long sharp canine teeth showing between his parted lips, long black claws on the fingertips of his hands held at his sides. "
         "He faces the camera with an intense, predatory expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.",
         ref='killian')
v = a.d['characters']['KillianWolf']['voice_description']
a.character('KillianGold', 'killian_gold', v['en'], v['zh'])
a.character('KillianBeast', 'killian_beast', v['en'], v['zh'])
v = a.d['characters']['Killian']['voice_description']
a.character('KillianShirt', 'killian_shirt', v['en'], v['zh'])
a.character('Doctor', 'doctor',
            "A middle-aged adult male voice, thin and cracking with terror, speaking clear American English at ordinary conversational volume. Every word is fully voiced and audible.",
            "中年成年男声，因恐惧而发细、发颤，说清楚的美式英语，正常交谈音量。每个字都正常发声、清晰可辨。")
a.character('GuardFrenzy', 'bodyguard',
            "A rough adult male voice, raw and snarling like an animal forcing out words, speaking clear American English, slightly muffled by a thick wooden door yet every word is fully voiced and audible.",
            "粗哑的成年男声，像野兽硬挤出人话，粗暴、带着低吼，说清楚的美式英语，隔着厚厚的木门略显发闷，但每个字都发声、清晰可辨。")

# =========================================================================================================
# 第 11 集 Luna 血脉（主卧，夜）
# =========================================================================================================

# 11-01 高烧的莉莉 ----------------------------------------------------------------------------------------------
T11(False, '01｜高烧的莉莉', 5, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
    "Side-on medium shot of Lily alone, from the head to the waist, lying on her back on the huge dark-wood bed in the middle third of the frame, her head on a pillow and her damp hair spread over the charcoal-grey linen, in the oversized white men's cotton shirt buttoned to the collarbone, "
    "her face flushed and glistening with sweat, her brows drawn together, her lips parted, her eyes closed, her right hand gripping the linen at her side. The frame holds exactly one person, Lily.",
    END_BED + LAY_BED,
    "侧面的中景镜头，只有莉莉一个人，头到腰，仰躺在深色木制大床上，在画面中间三分之一，头枕着枕头，湿漉漉的头发铺散在炭灰色亚麻床品上，穿宽大的白色男式棉衬衫，扣子一直扣到锁骨，脸颊潮红、渗着汗光，眉头皱着，嘴唇微张，眼睛闭着，右手攥着身旁的床单。画面里恰好一个人：莉莉。" + Z_END_BED + Z_BED,
    "莉莉发着高烧，昏迷地躺在大床上，呼吸急促。", "0—5秒侧面中景，镜头固定。", None,
    f"A steady side-on medium shot opens from the adopted first frame in {BD}: {LS} lies on her back on the bed. Her chest rises and falls in ragged breaths, her brows knitting tighter, her lips parting and pressing together, her head turning a little from side to side on the pillow while her fingers clench the linen and let go. The camera holds still.",
    "一个稳定的侧面中景，从已采用的开场图继续，场景是主卧：莉莉仰躺在床上。她的胸口随着急促的呼吸起伏，眉头越皱越紧，嘴唇时而张开时而抿住，头在枕头上微微左右转动，手指攥紧床单又松开。镜头固定不动。",
    breathy("The low hum of the quiet room and the soft rustle of linen.", "安静房间里低低的嗡鸣声，和床单轻轻的摩擦声。"))

# 11-02 医生跪地（台词：Alpha 她不是人类）------------------------------------------------------------------------------
T11(False, '02｜医生跪地', 6, ['Doctor', 'Killian'], ('bedroom', 'doctor', 'killian'), ['bedroom'],
    "Side-on medium two-shot, both men from the head to the knees, in the middle third of the frame, on the dark rug beside the huge bed. "
    "Doctor kneels at frame-left in the long white coat over a gray shirt, his wire-rimmed glasses crooked, his right hand holding a glass test tube of dark-red blood up at chest height, his lips trembling, his brows pulled up, his eyes wide and fixed on Killian's face. "
    "Killian stands at frame-right facing frame-left in the black three-piece suit, his arms rigid at his sides, his fists clenched, his jaw set, his lips pressed flat, his cold eyes hard on Doctor's face. The frame holds exactly two people: Doctor and Killian.",
    END_BED + LAY_BED,
    "侧面的中景双人镜头，两个男人都是头到膝盖，在画面中间三分之一，在大床旁边的深色地毯上。"
    "医生跪在画面左边，穿长款白大褂、里面是灰衬衫，金属细框眼镜歪着，右手在胸口的高度举着一支装着暗红色血液的玻璃试管，嘴唇发抖，眉毛扬起，睁大眼睛盯着基利安的脸。"
    "基利安站在画面右边，侧身朝画面左边，穿黑色三件套西装，双臂僵直垂在身侧，拳头攥紧，下颌紧绷，嘴唇抿成平直的一条线，冷冷的眼睛死死盯着医生的脸。画面里恰好两个人：医生和基利安。" + Z_END_BED + Z_BED,
    "医生跪在地上，举着装血的试管，颤着声音向基利安说话；基利安攥着拳头盯着他。", "0—6秒侧面中景，镜头固定。",
    ('Doctor', "She's not human, Alpha!", 1.0),
    f"A steady side-on medium two-shot opens from the adopted first frame in {BD}: {DR} kneels at frame-left holding the test tube of dark-red blood in his shaking right hand. Doctor speaks in a thin, cracking voice, his lips trembling and his eyes wide on {K}'s face. Killian's jaw tightens and his fists clench harder, his brows lowering as his narrowed eyes drop to the test tube. The camera holds still.",
    "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是主卧：医生跪在画面左边，颤抖的右手举着装暗红色血液的试管。医生用发细、破音的声音说话，嘴唇发抖，睁大眼睛看着基利安的脸。基利安的下颌收紧，拳头攥得更紧，眉头压低，眯起的眼睛落到试管上。镜头固定不动。",
    voiced("A faint clink of glass and the quiet creak of leather shoes.", "玻璃轻轻的叮当声，和皮鞋轻轻的吱嘎声。"))

# 11-03 揪起领子（承接 02：同两个人、同一地点、同一景别）-------------------------------------------------------------
T11(True, '03｜揪起医生的领子', 6, ['Killian', 'Doctor'], ('bedroom', 'killian', 'doctor'), ['bedroom'],
    "Side-on medium two-shot, both men from the head to the knees, in the middle third of the frame, on the dark rug beside the huge bed. "
    "Killian stands at frame-right facing frame-left in the black three-piece suit, his right arm extended with his right fist gripping Doctor's white coat collar at chest height and hauling him half upright, his jaw clenched, his lips pulled back from his teeth, his brows low, his eyes burning on Doctor's face. "
    "Doctor is at frame-left facing frame-right, half rising off his knees, both hands clutching Killian's right forearm, the glass test tube gripped in his fingers, his mouth open, his brows pulled up, his eyes wide with terror. The frame holds exactly two people: Killian and Doctor.",
    END_BED + LAY_BED,
    "侧面的中景双人镜头，两个男人都是头到膝盖，在画面中间三分之一，在大床旁边的深色地毯上。"
    "基利安站在画面右边，侧身朝画面左边，穿黑色三件套西装，右臂伸出，右拳在胸口的高度攥着医生白大褂的领子，把他拽得半站起来，下颌咬紧，嘴唇向后拉开露出牙齿，眉头压低，眼睛燃烧着盯着医生的脸。"
    "医生在画面左边，侧身朝画面右边，膝盖半离地面，双手抓着基利安的右前臂，手指间还攥着那支玻璃试管，嘴巴张着，眉毛扬起，眼睛因恐惧睁得大大的。画面里恰好两个人：基利安和医生。" + Z_END_BED + Z_BED,
    "基利安一把揪住医生的领子把他拽起来，低声逼问；医生吓得手抖。", "0—6秒侧面中景，镜头固定。",
    ('Killian', "Tell me what she is.", 1.0),
    f"A steady side-on medium two-shot opens from the adopted first frame in {BD}: {K} at frame-right hauls {DR} upright by the collar with his right fist until the two men stand chest to chest. Killian speaks in a low, savage voice, his jaw clenched and his eyes burning on Doctor's face. Doctor's hands claw at Killian's forearm, his mouth open and his brows pulled up, the test tube shaking in his fingers. The camera holds still.",
    "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是主卧：基利安在画面右边，用右拳揪着医生的领子把他拽得站直，两人几乎胸口贴胸口。基利安用低沉凶狠的声音说话，下颌咬紧，眼睛燃烧着盯着医生的脸。医生的手抓挠着基利安的前臂，嘴巴张着，眉毛扬起，手指间的试管不停地抖。镜头固定不动。",
    voiced("A faint clink of glass and the rustle of cloth.", "玻璃轻轻的叮当声，和衣料的摩擦声。"))

# 11-04 觉醒发情期（承接 03）-------------------------------------------------------------------------------------------
T11(True, '04｜Luna 与觉醒发情期', 6, ['Doctor', 'Killian'], ('bedroom', 'doctor', 'killian'), ['bedroom'],
    "Side-on medium two-shot, both men from the head to the knees, in the middle third of the frame, on the dark rug beside the huge bed. "
    "Killian stands at frame-right facing frame-left in the black three-piece suit, his right fist locked in Doctor's white coat collar at chest height, his jaw clenched, his lips flat, his brows low, his eyes hard on Doctor's face. "
    "Doctor is at frame-left facing frame-right, held up on his toes by the collar, both hands clutching Killian's right forearm, the glass test tube in one fist, his lips quivering, his brows pulled up, his eyes wide with terror. The frame holds exactly two people: Killian and Doctor.",
    END_BED + LAY_BED,
    "侧面的中景双人镜头，两个男人都是头到膝盖，在画面中间三分之一，在大床旁边的深色地毯上。"
    "基利安站在画面右边，侧身朝画面左边，穿黑色三件套西装，右拳在胸口的高度死死攥着医生白大褂的领子，下颌咬紧，嘴唇平直，眉头压低，眼睛冷硬地盯着医生的脸。"
    "医生在画面左边，侧身朝画面右边，被领子拎得踮起脚尖，双手抓着基利安的右前臂，一只拳头里攥着玻璃试管，嘴唇发颤，眉毛扬起，眼睛因恐惧睁得大大的。画面里恰好两个人：基利安和医生。" + Z_END_BED + Z_BED,
    "医生被拎着领子，哆哆嗦嗦地说出莉莉的血统和“觉醒发情期”；基利安的目光转向床。", "0—6秒侧面中景，镜头固定。",
    ('Doctor', "A Luna! She's in Awakening Heat!", 1.0),
    f"A steady side-on medium two-shot opens from the adopted first frame in {BD}: {DR} gasps out the words in a thin, cracking voice, his eyes wide on {K}'s face and his lips quivering, the test tube shaking in his raised hand. Killian's right fist is locked in the collar, his brows snapping together and his jaw tightening as his narrowed eyes cut to the bed at frame-left. The camera holds still.",
    "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是主卧：医生用发细、破音的声音喘着气说出这句话，睁大眼睛看着基利安的脸，嘴唇发颤，举着的手里试管不停地抖。基利安的右拳死死攥着领子，眉头猛地拧紧，下颌收紧，眯起的眼睛转向画面左边的床。镜头固定不动。",
    voiced("A faint clink of glass and the rustle of cloth.", "玻璃轻轻的叮当声，和衣料的摩擦声。"))

# 11-05 莉莉痛苦弓身（香气爆开用她的反应来演）-----------------------------------------------------------------------------
T11(False, '05｜莉莉痛苦弓身', 5, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
    "Side-on medium shot of Lily alone, from the head to the waist, lying on her back on the huge dark-wood bed in the middle third of the frame, her head on a pillow and her damp hair spread over the charcoal-grey linen, in the oversized white men's cotton shirt buttoned to the collarbone, "
    "her face flushed and glistening with sweat, her brows drawn together, her lips parted, her eyes closed, both fists loosely holding the linen at her sides. The frame holds exactly one person, Lily.",
    END_BED + LAY_BED,
    "侧面的中景镜头，只有莉莉一个人，头到腰，仰躺在深色木制大床上，在画面中间三分之一，头枕着枕头，湿漉漉的头发铺散在炭灰色亚麻床品上，穿宽大的白色男式棉衬衫，扣子一直扣到锁骨，脸颊潮红、渗着汗光，眉头皱着，嘴唇微张，眼睛闭着，两只拳头松松地抓着身侧的床单。画面里恰好一个人：莉莉。" + Z_END_BED + Z_BED,
    "莉莉突然痛苦地弓起身体，倒吸一口气，又重重落回床上。", "0—5秒侧面中景，镜头固定。", None,
    f"A steady side-on medium shot opens from the adopted first frame in {BD}: {LS} suddenly arches her back off the mattress, her fists clenching the linen, her head pressing back into the pillow and her mouth opening in a sharp gasp, her brows pulling together in pain. She sinks back onto the bed, her chest heaving and her lips trembling, her eyes squeezing shut. The camera holds still.",
    "一个稳定的侧面中景，从已采用的开场图继续，场景是主卧：莉莉突然把后背从床垫上弓起来，拳头攥紧床单，头向后顶进枕头，嘴巴张开倒吸一口气，眉头因疼痛拧在一起。她又落回床上，胸口剧烈起伏，嘴唇发抖，眼睛紧紧闭上。镜头固定不动。",
    breathy("A sharp gasp, the rustle of linen and the creak of the bed frame.", "一声急促的倒吸气、床单的摩擦声，和床架的吱嘎声。"))

# 11-06 门被挠（门外保镖的声音：隔着门说话，画面里没有人）---------------------------------------------------------------------
T11(False, '06｜门外的低吼', 6, ['GuardFrenzy'], ('bedroom',), ['bedroom'],
    "Straight-on medium shot of the tall dark-wood door with a brass handle, the closed door in the middle third of the frame and reaching into the right third, set in the dark wall, the foot of the huge bed's charcoal-grey linen at frame-left, amber lamplight on the wood. The frame holds no people.",
    END_BED + LAY_BED,
    "正面的中景镜头，对着那扇带黄铜把手的高大深色木门，紧闭的门在画面中间三分之一、并延伸到右边三分之一，嵌在深色的墙里，大床炭灰色亚麻床品的床尾在画面左边，琥珀色的灯光照在木头上。画面里没有人。" + Z_END_BED + Z_BED,
    "门被门外的人猛烈撞击、抓挠，木头鼓起、裂开；门外传来野兽般的人声。", "0—6秒正面中景，镜头固定。",
    ('GuardFrenzy', "That scent! Give her to me!", 1.0),
    f"A steady medium shot opens from the adopted first frame in {BD}: the tall dark-wood door shudders under heavy blows from the other side, the wood bulging inward, deep claw scratches ripping across its surface and splinters flaking off, the brass handle rattling. The frame holds no people. A man's savage, muffled voice shouts from behind the door. The camera holds still.",
    "一个稳定的中景，从已采用的开场图继续，场景是主卧：高大的深色木门在另一侧的重击下剧烈震动，木头向里鼓起，深深的爪痕在门面上撕开，木屑剥落，黄铜把手哐哐作响。画面里没有人。一个男人凶暴、发闷的声音从门后喊出来。镜头固定不动。",
    ("Heavy blows on thick wood, claws shrieking down the door, and one man's raw, snarling voice shouting from behind it. The words are muffled by the door but fully voiced and clearly audible.",
     "厚木门上沉重的撞击声、利爪在门上刮出的尖啸声，和门后一个男人粗哑、带着低吼的喊声。字词被门挡得有点发闷，但每个字都发声、清晰可辨。"))

# 11-07 基利安猛回头，眼睛点亮（文字让眼睛变金；B1 用金瞳人物图做对照）--------------------------------------------------------
T11(False, '07｜基利安猛回头', 5, ['Killian'], ('bedroom', 'killian'), ['bedroom'],
    "Medium close-up of Killian alone, from the head to the chest, in profile facing frame-left, in the middle third of the frame, beside the huge bed, in the black three-piece suit, "
    "his jaw set, his lips pressed flat, his brows drawn together, his cold dark-gray eyes lowered. The tall dark-wood door with a brass handle is behind him at frame-right. The frame holds exactly one person, Killian.",
    END_BED + LAY_BED,
    "基利安一个人的中近景，头到胸口，侧身朝画面左边，在画面中间三分之一，站在大床旁边，穿黑色三件套西装，下颌紧绷，嘴唇抿成平直的一条线，眉头拧着，冷冷的深灰色眼睛垂着。带黄铜把手的高大深色木门在他身后的画面右边。画面里恰好一个人：基利安。" + Z_END_BED + Z_BED,
    "基利安低头站在床边，门外猛地一声重响，他猛地回头盯向房门，眼睛亮起暗金色的光。", "0—5秒侧面中近景，镜头固定。", None,
    f"A steady medium close-up opens from the adopted first frame in {BD}: {K} lowers his gaze at frame-left, then a heavy blow shakes the door at frame-right and his head snaps toward it. His eyes ignite a blazing dark gold, his lips pulling back from his sharp teeth, his jaw clenching and his nostrils flaring. The camera holds still.",
    "一个稳定的中近景，从已采用的开场图继续，场景是主卧：基利安在画面左边垂着视线，然后画面右边的门被重重一击，他的头猛地转向房门。他的眼睛点亮成炽烈的暗金色，嘴唇向后拉开露出尖牙，下颌咬紧，鼻翼张开。镜头固定不动。",
    breathy("A heavy blow on wood and a deep, rising animal growl from beyond the door.", "木头上一声沉重的撞击，和门外越来越响的一声低沉的野兽低吼。"))

a.finish('第11集｜Luna血脉',
         '主卧，夜。莉莉发着高烧昏迷在大床上。私人医生抽了她的血，吓得跪地说她不是普通人类；基利安揪起他的领子逼问，医生说出她是纯血 Luna，正在“觉醒发情期”。莉莉痛苦地弓起身体，异香在房间里炸开；门外的保镖们闻到香气发狂，撞门抓门，要她；基利安猛地回头，眼睛亮起暗金色。',
         O11)

# =========================================================================================================
# 第 12 集 Alpha 的绝对压制（主卧／走廊，夜）
# =========================================================================================================
b = Batch(O11 + '.json', SERIES_TITLE, 4400)
ZH12 = []
T12 = maker(b, ZH12)

# 12-01 门被撞碎（开场图是门已经裂开的样子，动作是最后一击）--------------------------------------------------------------------
T12(False, '01｜门被撞碎', 6, [], ('bedroom',), ['bedroom'],
    "Straight-on medium shot of the tall dark-wood door with a brass handle in the middle third of the frame, the door closed but deeply dented and split down the middle, long splinters hanging from the cracks, the foot of the huge bed's charcoal-grey linen at frame-left, amber lamplight on the wood. The frame holds no people.",
    END_BED + LAY_BED,
    "正面的中景镜头，对着那扇带黄铜把手的高大深色木门，门在画面中间三分之一，门还关着但已被撞得深深凹陷、从中间裂开，长长的木刺挂在裂缝上，大床炭灰色亚麻床品的床尾在画面左边，琥珀色的灯光照在木头上。画面里没有人。" + Z_END_BED + Z_BED,
    "门挨了最后一击，炸裂开来；一个红着眼睛的保镖踉跄着冲了进来。", "0—6秒正面中景，镜头固定。", None,
    f"A steady medium shot opens from the adopted first frame in {BD}: the cracked dark-wood door takes one last huge blow and bursts inward in a spray of splinters, the torn hinges flying and the door swinging against the wall. A man in a black suit, white shirt and black tie lurches through the gap, his eyes bloodshot and wild, his teeth bared in a snarl, his jaw slack and his chest heaving. The camera holds still.",
    "一个稳定的中景，从已采用的开场图继续，场景是主卧：裂开的深色木门挨了最后一记重击，向里炸开，木屑四溅，扯断的合页飞出，门板甩到墙上。一个穿黑西装、白衬衫、黑领带的男人踉跄着从缺口冲进来，眼睛布满血丝、神色狂乱，龇着牙低吼，下颌松垮，胸口剧烈起伏。镜头固定不动。",
    breathy("A deafening crash of splintering wood as the door bursts open, then ragged animal snarls and heavy breathing.", "木门炸开时震耳欲聋的碎裂声，随后是粗重的野兽低吼和喘息声。"))

# 12-02 守卫扑向床上的莉莉 ---------------------------------------------------------------------------------------
T12(False, '02｜守卫扑向床', 6, ['Bodyguard', 'LilyShirt'], ('bedroom', 'bodyguard', 'lily_shirt'), ['bedroom'],
    "Side-on wide shot, both people from head to toe, in the middle third of the frame, in the bedroom. "
    "Lily lies on her back on the huge dark-wood bed at the left and center of the frame, in the oversized white men's cotton shirt, her damp hair spread on the pillow, her eyes closed, her brows drawn together, her lips parted. "
    "Bodyguard stands in the wrecked doorway at frame-right facing frame-left, in a black suit, white shirt and black tie, crouched forward with both hands curled into claws, his eyes bloodshot and fixed on Lily, his teeth bared, his jaw slack. The splintered door hangs behind him. The frame holds exactly two people: Lily and Bodyguard.",
    END_BED + LAY_BED,
    "侧面的宽景镜头，两个人都是从头到脚，在画面中间三分之一，在卧室里。"
    "莉莉仰躺在画面左边和中间的深色木制大床上，穿宽大的白色男式棉衬衫，湿漉漉的头发铺散在枕头上，眼睛闭着，眉头皱着，嘴唇微张。"
    "保镖站在画面右边残破的门口，侧身朝画面左边，穿黑西装、白衬衫、黑领带，身体前倾蹲伏，双手弯成爪形，布满血丝的眼睛盯着莉莉，龇着牙，下颌松垮。裂开的门板挂在他身后。画面里恰好两个人：莉莉和保镖。" + Z_END_BED + Z_BED,
    "红着眼睛的保镖从破门口扑向床；莉莉昏迷地躺着。", "0—6秒侧面宽景，镜头固定。", None,
    f"A steady side-on wide shot opens from the adopted first frame in {BD}: {BGD} launches himself from the doorway across the room toward the bed at frame-left, both clawed hands reaching out, his teeth bared, his jaw slack, his brows low and his bloodshot eyes locked on Lily. Lily lies unconscious on the bed, her chest rising and falling, her brows drawn together and her lips parted. The camera holds still.",
    "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是主卧：保镖从门口纵身扑过房间，冲向画面左边的床，两只爪形的手向前伸出，龇着牙，下颌松垮，眉头压低，布满血丝的眼睛死死盯着莉莉。莉莉昏迷地躺在床上，胸口起伏，眉头皱着，嘴唇微张。镜头固定不动。",
    breathy("Fast, heavy footfalls and a savage snarl, with the soft creak of the bed.", "又快又重的脚步声和一声凶暴的低吼，夹着床轻轻的吱嘎声。"))

# 12-03 基利安连头都不回，反手一挥 ---------------------------------------------------------------------------------
T12(False, '03｜基利安反手一挥', 5, ['KillianGold'], ('bedroom', 'killian_gold'), ['bedroom'],
    "Side-on medium shot of Killian alone, from the head to the knees, in profile facing frame-left, in the middle third of the frame, standing beside the huge bed with his back toward the wrecked door at frame-right, in the black three-piece suit and dark tie, "
    "his eyes glowing a dark gold, his jaw set, his lips pressed flat, his brows level, his right hand hanging at his side with long black claws on the fingers. The frame holds exactly one person, Killian.",
    END_BED + LAY_BED,
    "侧面的中景镜头，基利安一个人，头到膝盖，侧身朝画面左边，在画面中间三分之一，站在大床旁边，背对着画面右边残破的门，穿黑色三件套西装、系深色领带，眼睛发出暗金色的光，下颌紧绷，嘴唇抿平，眉毛平直，右手垂在身侧，手指上是长长的黑色利爪。画面里恰好一个人：基利安。" + Z_END_BED + Z_BED,
    "基利安头也不回，朝身后反手一挥，一股无形的劲风掀起他的西装和领带。", "0—5秒侧面中景，镜头固定。", None,
    f"A steady side-on medium shot opens from the adopted first frame in {BD}: {KG} keeps his face turned toward frame-left and, without looking back, swings his right arm backward in one hard flick, his clawed hand open with the fingers spread, a violent gust whipping his suit jacket and tie toward frame-left. His eyes blaze dark gold, his jaw clenching and his lips curling back from his teeth. The camera holds still.",
    "一个稳定的侧面中景，从已采用的开场图继续，场景是主卧：基利安的脸一直朝着画面左边，头也不回，右臂朝身后猛地一挥，长着利爪的手张开、五指分开，一股猛烈的劲风把他的西装外套和领带吹向画面左边。他的眼睛炽烈地发出暗金色的光，下颌咬紧，嘴唇向后卷起露出牙齿。镜头固定不动。",
    breathy("A violent whoosh of air and the heavy thud of bodies hitting a wall.", "一声猛烈的呼啸风声，和身体重重撞在墙上的闷响。"))

# 12-04 两个守卫被砸在走廊墙上（结果镜头）-----------------------------------------------------------------------------------
T12(False, '04｜守卫被砸在墙上', 5, ['Bodyguard'], ('corridor', 'bodyguard'), ['corridor'],
    "Straight-on wide shot of the corridor wall, two men in the middle third of the frame, sprawled at the base of the dark-paneled wall where the wood has cracked in a spiderweb of splits. "
    "Bodyguard slumps against the wall in a black suit, white shirt and black tie, his head lolling, his mouth open, his dazed eyes half closed. A second man identical to him in build and clothes lies crumpled beside him, groaning, his jaw slack and his brows pulled together. The splintered bedroom door hangs open at frame-left. The frame holds exactly two people, both bodyguards.",
    END_CO + LAY_CO,
    "正面的宽景镜头，对着走廊的墙，两个男人在画面中间三分之一，瘫倒在深色木板墙根，墙上的木板裂成蜘蛛网一样的裂缝。"
    "保镖靠着墙瘫坐着，穿黑西装、白衬衫、黑领带，脑袋耷拉着，嘴巴张着，发懵的眼睛半睁半闭。另一个和他身材、衣着一模一样的男人蜷着倒在他身旁，哼哼着，下颌松垮，眉头皱在一起。残破的卧室门敞开着，在画面左边。画面里恰好两个人，都是保镖。" + Z_END_CO + Z_CO,
    "两个保镖被砸在走廊的墙上，墙板裂开；他们瘫软地滑落，呻吟。", "0—5秒正面宽景，镜头固定。", None,
    f"A steady straight-on wide shot opens from the adopted first frame in {CO}: {BGD} slides slowly down the cracked paneling to the floor as plaster dust drifts down, his mouth open and his dazed eyes closing. The second man identical to him rolls onto his side, clutching his ribs and groaning, his jaw slack and his brows pulled together as he struggles to lift his head. The camera holds still.",
    "一个稳定的正面宽景镜头，从已采用的开场图继续，场景是主卧外的走廊：保镖顺着裂开的墙板慢慢滑到地上，灰尘飘落，他张着嘴，发懵的眼睛慢慢闭上。和他一模一样的另一个男人翻身侧躺，捂着肋骨呻吟，下颌松垮、眉头皱在一起，挣扎着想抬起头。镜头固定不动。",
    breathy("Plaster dust pattering to the floor, low groans and ragged breathing.", "灰泥簌簌落在地上的声音、低低的呻吟声和粗重的喘息声。"))

# 12-05 基利安走进走廊，面对另一个红眼守卫 --------------------------------------------------------------------------------
T12(False, '05｜基利安走进走廊', 5, ['KillianGold', 'Bodyguard'], ('corridor', 'killian_gold', 'bodyguard'), ['corridor'],
    "Side-on wide shot, both men head to toe, in the middle third of the frame, in the corridor. "
    "Killian stands at frame-left right beside the wrecked bedroom door, facing frame-right, in the black three-piece suit, his arms hanging at his sides, long black claws on both hands, his eyes glowing a dark gold, his jaw set, his lips pressed flat, his chin lifted. "
    "Bodyguard is at frame-right, about twelve feet away along the corridor, facing frame-left, in a black suit, white shirt and black tie, hunched forward in a half crouch, his eyes bloodshot, his teeth bared, his brows low. The frame holds exactly two people: Killian and Bodyguard.",
    END_CO + LAY_CO,
    "侧面的宽景镜头，两个男人都是从头到脚，在画面中间三分之一，在走廊里。"
    "基利安站在画面左边、残破的卧室门旁边，侧身朝画面右边，穿黑色三件套西装，双臂垂在身侧，两只手都是长长的黑色利爪，眼睛发出暗金色的光，下颌紧绷，嘴唇抿平，下巴抬起。"
    "保镖在画面右边，沿着走廊离他大约十二英尺（约三、四米），侧身朝画面左边，穿黑西装、白衬衫、黑领带，身体前倾半蹲着，眼睛布满血丝，龇着牙，眉头压得很低。画面里恰好两个人：基利安和保镖。" + Z_END_CO + Z_CO,
    "基利安迈步走进走廊，朝红着眼睛的保镖一步步逼近；保镖畏缩后退。", "0—5秒侧面宽景，镜头固定。", None,
    f"A steady side-on wide shot opens from the adopted first frame in {CO}: {KG} walks two slow steps along the corridor toward frame-right, his clawed hands loose at his sides, his gold eyes locked on Bodyguard's face and his jaw set. Bodyguard shrinks back a step, his bared teeth trembling, his bloodshot eyes widening and a low whine rising in his throat. The camera holds still.",
    "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是主卧外的走廊：基利安沿着走廊朝画面右边缓缓走了两步，利爪的手松垂着，金色的眼睛死死盯着保镖的脸，下颌紧绷。保镖畏缩地后退一步，龇着的牙在发抖，布满血丝的眼睛越睁越大，喉咙里发出一声低低的呜咽。镜头固定不动。",
    breathy("Slow footsteps on marble and a low, rolling animal growl.", "大理石地面上缓慢的脚步声，和一声低沉、滚动的野兽低吼。"))

# 12-06 一步就死（承接 05：同两个人、同一走廊、同一景别）----------------------------------------------------------------------
T12(True, '06｜再进一步就死', 6, ['KillianGold', 'Bodyguard'], ('corridor', 'killian_gold', 'bodyguard'), ['corridor'],
    "Side-on wide shot, both men head to toe, in the middle third of the frame, in the corridor. "
    "Killian stands at frame-left, facing frame-right, in the black three-piece suit, long black claws on both hands hanging at his sides, his eyes glowing a dark gold, his jaw clenched, his lips pulled back from his teeth, his chin lifted. "
    "Bodyguard is at frame-right, about nine feet away, facing frame-left, in a black suit, white shirt and black tie, hunched back, his bloodshot eyes wide, his teeth bared, his brows pulled up. The frame holds exactly two people: Killian and Bodyguard.",
    END_CO + LAY_CO,
    "侧面的宽景镜头，两个男人都是从头到脚，在画面中间三分之一，在走廊里。"
    "基利安站在画面左边，侧身朝画面右边，穿黑色三件套西装，两只长着黑色利爪的手垂在身侧，眼睛发出暗金色的光，下颌咬紧，嘴唇向后拉开露出牙齿，下巴抬起。"
    "保镖在画面右边，离他大约九英尺（约三米），侧身朝画面左边，穿黑西装、白衬衫、黑领带，身体缩着往后退，布满血丝的眼睛睁得大大的，龇着牙，眉毛扬起。画面里恰好两个人：基利安和保镖。" + Z_END_CO + Z_CO,
    "基利安用低沉的吼声宣布“再进一步就死”；保镖捂住耳朵，痛苦地跪倒。", "0—6秒侧面宽景，镜头固定。",
    ('KillianGold', "One more step, and you die.", 1.0),
    f"A steady side-on wide shot opens from the adopted first frame in {CO}: {KG} speaks in a low, hoarse, savage growl, his gold eyes locked on Bodyguard's face and his jaw clenched. Bodyguard's hands clamp over his ears, his face contorting in pain, his jaw trembling and his eyes squeezing shut, and his knees buckle until he drops to the floor on both knees with his head bowed. The camera holds still.",
    "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是主卧外的走廊：基利安用低沉、沙哑、凶暴的吼声说话，金色的眼睛死死盯着保镖的脸，下颌咬紧。保镖双手捂住耳朵，脸因痛苦扭曲，下颌发抖，眼睛紧闭，膝盖一软，双膝跪倒在地，头低垂着。镜头固定不动。",
    voiced("Footsteps echoing on marble and a deep, low growl under the voice.", "大理石上回响的脚步声，和声音底下一声深沉的低吼。"))

# 12-07 关上残破的门，反锁 -------------------------------------------------------------------------------------------
T12(False, '07｜反锁房门', 5, ['KillianGold'], ('bedroom', 'killian_gold'), ['bedroom'],
    "Side-on medium shot of Killian alone, from the head to the knees, in profile facing frame-right, in the middle third of the frame, standing in the wrecked doorway at frame-right with the splintered door hanging open beside him, in the black three-piece suit, "
    "his eyes glowing a dark gold, his jaw set, his lips pressed flat, his brows level, his left hand gripping the edge of the splintered door, the dark corridor behind him. The frame holds exactly one person, Killian.",
    END_BED + LAY_BED,
    "侧面的中景镜头，基利安一个人，头到膝盖，侧身朝画面右边，在画面中间三分之一，站在画面右边残破的门口，裂开的门板敞开挂在他身旁，穿黑色三件套西装，眼睛发出暗金色的光，下颌紧绷，嘴唇抿平，眉毛平直，左手抓着裂开的门板边缘，身后是黑暗的走廊。画面里恰好一个人：基利安。" + Z_END_BED + Z_BED,
    "基利安把残破的门拖回来关上，推上黄铜插销反锁。", "0—5秒侧面中景，镜头固定。", None,
    f"A steady side-on medium shot opens from the adopted first frame in {BD}: {KG} drags the splintered door shut with his left hand, the broken wood scraping, then slides the heavy brass bolt across with his right hand, a hard metallic clack. His gold eyes narrow, his jaw clenching and his lips pressing flat. He lowers his head for a breath and his shoulders rise and fall. The camera holds still.",
    "一个稳定的侧面中景，从已采用的开场图继续，场景是主卧：基利安用左手把裂开的门板拖回来关上，碎木头刮擦作响，然后用右手把沉重的黄铜插销推过去，发出一声清脆的金属响。他金色的眼睛眯起，下颌咬紧，嘴唇抿平。他低下头喘了一口气，肩膀一起一伏。镜头固定不动。",
    breathy("The scrape of broken wood on the floor and a hard metallic clack of the bolt.", "碎木头刮过地面的声音，和插销一声清脆的金属响。"))

# 12-08 解开领带和衬衫扣子（本集结尾，不写黑屏）------------------------------------------------------------------------------
T12(False, '08｜解开衬衫扣子', 5, ['KillianGold', 'LilyShirt'], ('bedroom', 'killian_gold', 'lily_shirt'), ['bedroom'],
    "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, beside the huge bed. "
    "Lily at frame-left lies on her back on the bed, her damp hair spread on the pillow, in the oversized white men's cotton shirt buttoned to the collarbone, her face flushed, her brows drawn together, her lips parted, her eyes closed. "
    "Killian stands at frame-right beside the bed, facing frame-left, in the black three-piece suit, his eyes glowing a dark gold and lowered on her face, his jaw set, his lips parted, his left hand at his dark tie. The frame holds exactly two people: Lily and Killian.",
    END_BED + LAY_BED,
    "侧面的中景双人镜头，两个人都是头到腰，在画面中间三分之一，在大床旁边。"
    "莉莉在画面左边，仰躺在床上，湿漉漉的头发铺散在枕头上，穿宽大的白色男式棉衬衫，扣子扣到锁骨，脸颊潮红，眉头皱着，嘴唇微张，眼睛闭着。"
    "基利安站在画面右边的床边，侧身朝画面左边，穿黑色三件套西装，发出暗金色光的眼睛垂着看着她的脸，下颌紧绷，嘴唇微张，左手放在深色领带上。画面里恰好两个人：莉莉和基利安。" + Z_END_BED + Z_BED,
    "基利安低头看着床上的莉莉，一把扯松领带，解开白衬衫最上面的扣子。", "0—5秒侧面中景，镜头固定。", None,
    f"A steady side-on medium two-shot opens from the adopted first frame in {BD}: {KG} at frame-right pulls his tie loose with his left hand and unbuttons the top button of his white shirt, his gold eyes burning down on {LS}'s face, his jaw tight and his nostrils flaring. Lily lies on the bed, her chest heaving, her brows pulling together and her lips trembling as her head rolls toward him. The camera holds still.",
    "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是主卧：基利安在画面右边，左手把领带扯松，解开白衬衫最上面的扣子，金色的眼睛燃烧着俯视莉莉的脸，下颌紧绷，鼻翼张开。莉莉躺在床上，胸口剧烈起伏，眉头拧在一起，嘴唇发抖，头朝他那边偏过去。镜头固定不动。",
    breathy("The soft rasp of a silk tie sliding loose, the rustle of linen and slow, heavy breathing.", "丝绸领带松开时轻轻的摩擦声、床单的摩擦声，和缓慢沉重的呼吸声。"))

b.finish('第12集｜Alpha的绝对压制',
         '门被彻底撞碎，红着眼睛的保镖扑向床上昏迷的莉莉。基利安头也不回，反手一挥，无形的力量把守卫们砸在走廊的墙上。他走进走廊，长出黑色利爪，一声低吼，让走廊里发狂的狼人们痛苦地跪倒。他转身回房，拖上残破的门反锁，走到床边，解开了自己的领带和衬衫扣子。',
         O12)
