#!/usr/bin/env python3
"""剧本第 13、14 集（野兽的真面目、不可逆转的标记）＋ 第 11–14 集对比实验 B ＋ 合并 ＋ 说明（2026-10-10）。
先 import tools/gen_ep11_12.py（会重新生成第 11、12 集），再接着写第 13、14 集。运行本文件 = 全部重新生成。

对比实验 B（3 个任务，放最后，不进成片）：
  B1 = 第 11 集 07 号的对照：同种子，只差“用金瞳人物图、开场图里眼睛一开始就是金色”（A 用普通人物图＋文字让眼睛变金）；
  B2 = 第 14 集 01 号的对照：同种子、同文字，只差“不用上一集最后画面”（A 用 use_previous_episode_state）；
  B3 = 单人被“无形力量”甩飞撞墙（正式版里这个大动作用结果镜头绕开了）。
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_ep11_12 import (a, b, ZH11, ZH12, maker, BD, CO, LS, K, KG, KS, KB, DR, BGD, LAY_BED, Z_BED, END_BED, Z_END_BED,
                         O11, O12, SERIES_TITLE, FOLDER)
from _h3draft import Batch, silent, voiced, breathy

O13 = '第13集/第13集_制作稿_追加'
O14 = '第14集/第14集_制作稿_追加'
OB = '第14集/第11-14集B_对比实验'
OMERGE = '合并稿/合并_第11-14集+B_制作稿_追加'

# =========================================================================================================
# 第 13 集 野兽的真面目（主卧，夜；基利安只穿衬衫）
# =========================================================================================================
c = Batch(O12 + '.json', SERIES_TITLE, 4500)
ZH13 = []
T13 = maker(c, ZH13)

# 13-01 莉莉扯开领口 -------------------------------------------------------------------------------------------
T13(False, '01｜莉莉扯开领口', 6, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
    "Side-on close-up of Lily alone, from the head to the chest, lying on her back on the huge dark-wood bed in the middle third of the frame, her damp hair spread on the pillow, in the oversized white men's cotton shirt buttoned to the collarbone, "
    "her face flushed and glistening with sweat and tears, her brows pulled together, her eyes squeezed shut, her lips parted, both hands gripping the collar of her shirt. The frame holds exactly one person, Lily.",
    END_BED + LAY_BED,
    "侧面的近景镜头，只有莉莉一个人，头到胸口，仰躺在深色木制大床上，在画面中间三分之一，湿漉漉的头发铺散在枕头上，穿宽大的白色男式棉衬衫，扣子扣到锁骨，脸颊潮红、满是汗水和泪水的光，眉头拧在一起，眼睛紧闭，嘴唇微张，双手攥着衬衫的领口。画面里恰好一个人：莉莉。" + Z_END_BED + Z_BED,
    "莉莉烧得神志不清，双手扯开衬衫领口，带着哭腔喊着基利安的名字求救。", "0—6秒侧面近景，镜头固定。",
    ('LilyShirt', "Help me, Killian.", 1.0),
    f"A steady side-on close-up opens from the adopted first frame in {BD}: {LS} pulls her shirt collar open with both hands, the top buttons popping, her collarbone bare. She speaks in a cracked, tearful murmur, her eyes squeezed shut and her lips trembling, tears running toward her temples as her head turns from side to side on the pillow. The camera holds still.",
    "一个稳定的侧面近景，从已采用的开场图继续，场景是主卧：莉莉双手把衬衫领口扯开，最上面的扣子崩开，锁骨露了出来。她用带着哭腔、沙哑的低语说话，眼睛紧闭，嘴唇发抖，泪水流向太阳穴，头在枕头上左右转动。镜头固定不动。",
    voiced("A slow, ragged breath and the rustle of linen.", "缓慢、不稳的呼吸声，和床单的摩擦声。"))

# 13-02 单膝跪在床沿，捧住脸颊 --------------------------------------------------------------------------------------
T13(False, '02｜单膝跪上床沿', 6, ['Killian' + 'Shirt', 'LilyShirt'], ('bedroom', 'killian_shirt', 'lily_shirt'), ['bedroom'],
    "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, at the edge of the huge dark-wood bed. "
    "Lily at frame-left lies on her back on the bed, her damp hair spread on the pillow, in the oversized white men's cotton shirt with the collar open at the collarbone, her face flushed, her brows drawn together, her eyes half open and unfocused, her lips parted. "
    "Killian kneels with one knee on the edge of the bed at frame-right, facing frame-left, in a white dress shirt with the sleeves rolled to the elbows and a loosened dark tie, no jacket, his right hand holding Lily's cheek, his jaw tight, his lips pressed flat, his cold eyes intense on her face. "
    "A black suit jacket lies crumpled on the dark rug in the foreground. The frame holds exactly two people: Lily and Killian.",
    END_BED + LAY_BED,
    "侧面的中景双人镜头，两个人都是头到腰，在画面中间三分之一，在深色木制大床的床沿旁。"
    "莉莉在画面左边，仰躺在床上，湿漉漉的头发铺散在枕头上，穿宽大的白色男式棉衬衫，领口敞开到锁骨，脸颊潮红，眉头皱着，眼睛半睁、目光涣散，嘴唇微张。"
    "基利安在画面右边，单膝跪在床沿上，侧身朝画面左边，穿白色衬衫，袖子卷到手肘，深色领带扯松了，没有外套，右手捧着莉莉的脸颊，下颌紧绷，嘴唇抿成平直的一条线，冷冷的眼睛目光炽烈地看着她的脸。"
    "一件黑色西装外套皱巴巴地丢在前景的深色地毯上。画面里恰好两个人：莉莉和基利安。" + Z_END_BED + Z_BED,
    "基利安单膝跪上床沿，捧住莉莉滚烫的脸颊，低声叫她看着他；她把脸贴向他冰凉的手心。", "0—6秒侧面中景，镜头固定。",
    ('KillianShirt', "Look at me, Lily.", 1.0),
    f"A steady side-on medium two-shot opens from the adopted first frame in {BD}: {KS} at frame-right holds Lily's cheek in his right hand and leans closer to her face. Killian speaks in a low, hoarse voice, his cold eyes boring into hers and his jaw tight. {LS} turns her cheek into his palm, her eyes fluttering half open, her lips parting and her brows easing. The camera holds still.",
    "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是主卧：基利安在画面右边，右手捧着莉莉的脸颊，身体靠近她的脸。基利安用低沉沙哑的声音说话，冷冷的眼睛直直地望进她的眼睛，下颌紧绷。莉莉把脸颊贴向他的手心，眼睑颤动着半睁开，嘴唇张开，眉头舒展了一些。镜头固定不动。",
    voiced("The rustle of linen and slow, heavy breathing.", "床单的摩擦声和缓慢沉重的呼吸声。"))

# 13-03 摸到獠牙（变身靠“切镜”：这一镜的人物图直接是竖瞳獠牙的样子）-------------------------------------------------------
T13(False, '03｜指尖碰到獠牙', 5, ['KillianBeast', 'LilyShirt'], ('bedroom', 'killian_beast', 'lily_shirt'), ['bedroom'],
    "Side-on close-up two-shot, both faces from the head to the shoulders, in the middle third of the frame, a hand's width apart, on the huge dark-wood bed. "
    "Lily at frame-left lies on her back with her head on the pillow, her right hand raised with her fingertips resting on Killian's upper lip, her eyes wide open, her lips parted, her brows pulled up in dawning horror. "
    "Killian at frame-right leans over her facing frame-left, in the white dress shirt with the collar open, his eyes glowing a dark gold with narrow vertical slit pupils, his lips parted showing two long sharp canine teeth, his jaw set, his brows low. The frame holds exactly two people: Lily and Killian.",
    END_BED + LAY_BED,
    "侧面的近景双人镜头，两张脸都是头到肩膀，在画面中间三分之一，相距一只手掌宽，在深色木制大床上。"
    "莉莉在画面左边，仰躺着，头枕在枕头上，右手抬起，指尖搭在基利安的上嘴唇上，眼睛睁得大大的，嘴唇微张，眉毛扬起，露出刚刚醒悟的惊恐。"
    "基利安在画面右边，俯身在她上方，侧身朝画面左边，穿领口敞开的白衬衫，眼睛发出暗金色的光、瞳孔是细细的竖瞳，嘴唇微张，露出两颗又长又尖的犬齿，下颌紧绷，眉头压低。画面里恰好两个人：莉莉和基利安。" + Z_END_BED + Z_BED,
    "莉莉的指尖滑过基利安的嘴唇，碰到一颗尖利的獠牙，惊恐地睁大眼睛，把手猛地缩回。", "0—5秒侧面近景，镜头固定。", None,
    f"A steady side-on close-up two-shot opens from the adopted first frame in {BD}: {LS}'s fingertips slide along {KB}'s upper lip and stop against a long sharp canine. Her eyes snap wide, her lips part in a sharp gasp and her brows shoot up as her hand jerks back from his mouth. Killian's slit-pupil eyes narrow on her face, his lips curling back farther from his fangs, his jaw tight. The camera holds still.",
    "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是主卧：莉莉的指尖沿着基利安的上嘴唇滑过，停在一颗又长又尖的犬齿上。她的眼睛猛地睁大，嘴唇张开倒吸一口气，眉毛飞扬，手从他的嘴边猛地缩回。基利安的竖瞳眼睛眯起，盯着她的脸，嘴唇向后卷得更开，露出獠牙，下颌紧绷。镜头固定不动。",
    breathy("A sharp gasp, a low animal growl and the rustle of linen.", "一声急促的倒吸气、一声低低的野兽低吼，和床单的摩擦声。"))

# 13-04 尖叫“怪物”（承接 03：同两个人、同一景别）--------------------------------------------------------------------------
T13(True, '04｜你是个怪物', 6, ['LilyShirt', 'KillianBeast'], ('bedroom', 'lily_shirt', 'killian_beast'), ['bedroom'],
    "Side-on close-up two-shot, both faces from the head to the shoulders, in the middle third of the frame, on the huge dark-wood bed. "
    "Lily at frame-left, her head pressed back into the pillow, her right hand pushing against Killian's chest, her eyes wide with terror, her mouth open in a scream, her brows pulled up, tears on her cheeks. "
    "Killian at frame-right leans over her facing frame-left, in the white dress shirt with the collar open, his eyes glowing a dark gold with slit pupils and fixed on her face, his lips parted over his fangs, his jaw tight, his brows low. The frame holds exactly two people: Lily and Killian.",
    END_BED + LAY_BED,
    "侧面的近景双人镜头，两张脸都是头到肩膀，在画面中间三分之一，在深色木制大床上。"
    "莉莉在画面左边，头向后顶进枕头，右手抵着基利安的胸口，眼睛因恐惧睁得大大的，嘴巴张开在尖叫，眉毛扬起，脸颊上有泪。"
    "基利安在画面右边，俯身在她上方，侧身朝画面左边，穿领口敞开的白衬衫，发出暗金色光的竖瞳眼睛死死盯着她的脸，嘴唇微张露出獠牙，下颌紧绷，眉头压低。画面里恰好两个人：莉莉和基利安。" + Z_END_BED + Z_BED,
    "莉莉尖叫着骂他是怪物，双手推着他的胸口往枕头后面缩。", "0—6秒侧面近景，镜头固定。",
    ('LilyShirt', "You're a monster! Let me go!", 1.0),
    f"A steady side-on close-up two-shot opens from the adopted first frame in {BD}: {LS} screams the words in a high, cracking voice, her mouth wide open and tears streaming, her hands shoving at Killian's chest as she pushes herself back along the pillow. {KB} lets her shove, his gold slit-pupil eyes narrowing, a muscle jumping in his jaw and his lips closing over his fangs. The camera holds still.",
    "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是主卧：莉莉用高亢、破音的声音尖叫着说出这句话，嘴巴大张，泪水直流，双手推着基利安的胸口，身体沿着枕头往后缩。基利安任由她推，金色的竖瞳眼睛眯起，下颌上一块肌肉跳动，嘴唇合上、盖住獠牙。镜头固定不动。",
    voiced("A cracking scream, the rustle of linen and heavy breathing.", "一声破音的尖叫、床单的摩擦声和沉重的呼吸声。"))

# 13-05 攥住脚踝拖回（本集结尾）---------------------------------------------------------------------------------------
T13(False, '05｜攥住脚踝拖回来', 6, ['KillianBeast', 'LilyShirt'], ('bedroom', 'killian_beast', 'lily_shirt'), ['bedroom'],
    "Side-on wide shot, both people from head to toe, in the middle third of the frame, on the huge dark-wood bed. "
    "Lily at frame-left is half sitting up on the charcoal-grey linen, scrambling away toward frame-left with both hands clawing at the sheet, in the oversized white shirt with the collar open, her hair wild, her mouth open, her eyes wide, her brows pulled up. "
    "Killian kneels on the bed at frame-right facing frame-left, in the white dress shirt with the sleeves rolled and the dark tie hanging loose, his right arm stretched out with his right hand clamped around Lily's left ankle, his eyes glowing a dark gold with slit pupils, his jaw set, his lips parted over his fangs. The frame holds exactly two people: Lily and Killian.",
    END_BED + LAY_BED,
    "侧面的宽景镜头，两个人都是从头到脚，在画面中间三分之一，在深色木制大床上。"
    "莉莉在画面左边，半坐在炭灰色的亚麻床品上，双手抓挠着床单，拼命往画面左边爬，穿宽大的白衬衫、领口敞开，头发凌乱，嘴巴张开，眼睛睁大，眉毛扬起。"
    "基利安跪在画面右边的床上，侧身朝画面左边，穿袖子卷起的白衬衫，深色领带松垂着，右臂伸直，右手紧紧攥着莉莉的左脚踝，眼睛发出暗金色的光、是竖瞳，下颌紧绷，嘴唇微张露出獠牙。画面里恰好两个人：莉莉和基利安。" + Z_END_BED + Z_BED,
    "基利安攥着莉莉的脚踝，一把把她拖回自己身下，低声说“晚了”。", "0—6秒侧面宽景，镜头固定。",
    ('KillianBeast', "It's too late, Lily.", 1.0),
    f"A steady side-on wide shot opens from the adopted first frame in {BD}: {KB} drags {LS} back across the bed by her ankle in one smooth pull, his right shoulder and arm stretched out to her left ankle, until she lies on her back beneath him. Killian speaks in a low, hoarse growl, his gold slit-pupil eyes burning on her face and his jaw set. Lily's hands claw at the sheet as she slides, her mouth open, her eyes wide and her head falling back onto the pillow. The camera holds still.",
    "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是主卧：基利安攥着莉莉的脚踝，一把顺滑地把她拖回床上，他的右肩和右臂一直伸到她的左脚踝，直到她仰面躺在他身下。基利安用低沉沙哑的吼声说话，金色的竖瞳眼睛燃烧着盯着她的脸，下颌紧绷。莉莉滑动时双手抓挠着床单，嘴巴张开，眼睛睁大，头向后落回枕头上。镜头固定不动。",
    voiced("A thick drag of linen and heavy breathing under a low growl.", "床单被拖动的厚重摩擦声，和低吼声底下沉重的呼吸声。"))

c.finish('第13集｜野兽的真面目',
         '门已反锁。烧得神志不清的莉莉扯开衬衫领口，带着哭腔喊基利安救她。基利安脱掉外套，单膝跪上床沿，捧着她的脸叫她看清楚他是谁。莉莉的指尖摸到了他的獠牙，看见他金色的竖瞳，吓得尖叫“怪物”，拼命往后爬；基利安攥住她的脚踝，把她拖回身下：“太晚了。”',
         O13)

# =========================================================================================================
# 第 14 集 不可逆转的标记（主卧，夜）
# =========================================================================================================
d = Batch(O13 + '.json', SERIES_TITLE, 4600)
ZH14 = []
T14 = maker(d, ZH14)

# 14-01 的文字抽出来，A 和 B2 共用（只差 use_previous_episode_state）
A1401 = dict(
    title='01｜钉住手腕', dur=6, chars=['KillianBeast', 'LilyShirt'], assets=('bedroom', 'killian_beast', 'lily_shirt'), refs=['bedroom'],
    img="Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the huge dark-wood bed. "
        "Lily at frame-left lies on her back, her damp hair spread on the pillow, in the oversized white men's cotton shirt with the collar open, both hands pushing against Killian's chest, her mouth open, her brows pulled together, her eyes wide and wet. "
        "Killian at frame-right leans over her facing frame-left, in the white dress shirt with the loosened dark tie hanging, his eyes glowing a dark gold with slit pupils, his lips parted over his fangs, his jaw tight, his brows low. The frame holds exactly two people: Lily and Killian.",
    end=END_BED + LAY_BED,
    img_zh="侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，在深色木制大床上。"
           "莉莉在画面左边，仰躺着，湿漉漉的头发铺散在枕头上，穿领口敞开的宽大白色男式棉衬衫，双手抵着基利安的胸口，嘴巴张着，眉头拧在一起，睁大的眼睛是湿的。"
           "基利安在画面右边，俯身在她上方，侧身朝画面左边，穿白衬衫，松开的深色领带垂着，眼睛发出暗金色的光、是竖瞳，嘴唇微张露出獠牙，下颌紧绷，眉头压低。画面里恰好两个人：莉莉和基利安。" + Z_END_BED + Z_BED,
    vis_zh="莉莉拼命挣扎踢打，基利安一只手把她的两只手腕钉在头顶的枕头上。", cam_zh="0—6秒侧面中近景，镜头固定。",
    shot_en=f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {KB} catches both of Lily's wrists in his right hand and presses them against the pillow above her head, his right shoulder and arm stretched along the bed. Killian's jaw clenches, his gold eyes burning on her face. {LS} writhes and kicks beneath him, her back arching, her mouth open in a ragged gasp, tears at the corners of her wide eyes. The camera holds still.",
    shot_zh="一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安用右手同时抓住莉莉的两只手腕，按在她头顶上方的枕头上，他的右肩和右臂沿着床伸展开。基利安的下颌咬紧，金色的眼睛燃烧着盯着她的脸。莉莉在他身下挣扎踢打，后背弓起，嘴巴张着发出不稳的喘息，睁大的眼睛眼角有泪。镜头固定不动。",
    sound=breathy("The rustle of linen and the creak of the bed frame.", "床单的摩擦声和床架的吱嘎声。"))


def put_1401(T):
    k = dict(A1401)
    return T(False, k['title'], k['dur'], k['chars'], k['assets'], k['refs'], k['img'], k['end'], k['img_zh'], k['vis_zh'], k['cam_zh'],
             None, k['shot_en'], k['shot_zh'], k['sound'])


s1401 = put_1401(T14)
s1401['use_previous_episode_state'] = True        # 跨集：用第 13 集最后采用的画面当位置参考（A）；B2 是对照，不用

# 14-02 十年前的雪地 --------------------------------------------------------------------------------------------------
T14(True, '02｜你把我丢在雪地里', 6, ['KillianBeast', 'LilyShirt'], ('bedroom', 'killian_beast', 'lily_shirt'), ['bedroom'],
    "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the huge dark-wood bed. "
    "Lily at frame-left lies on her back, her wrists pinned against the pillow above her head, her damp hair spread on the pillow, in the oversized white shirt with the collar open, her lips quivering, her brows pulled together, her wet eyes wide on Killian's face. "
    "Killian at frame-right leans over her facing frame-left, his right hand pinning both her wrists, in the white dress shirt with the loosened dark tie hanging, his eyes glowing a dark gold with slit pupils, his lips pulled back from his fangs, his jaw trembling, his brows low. The frame holds exactly two people: Lily and Killian.",
    END_BED + LAY_BED,
    "侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，在深色木制大床上。"
    "莉莉在画面左边，仰躺着，两只手腕被按在头顶上方的枕头上，湿漉漉的头发铺散在枕头上，穿领口敞开的宽大白衬衫，嘴唇发颤，眉头拧在一起，含泪的睁大的眼睛看着基利安的脸。"
    "基利安在画面右边，俯身在她上方，侧身朝画面左边，右手按着她的两只手腕，穿白衬衫，松开的深色领带垂着，眼睛发出暗金色的光、是竖瞳，嘴唇向后拉开露出獠牙，下颌发抖，眉头压低。画面里恰好两个人：莉莉和基利安。" + Z_END_BED + Z_BED,
    "基利安狂热地盯着莉莉，说出“你们把我丢在雪地里”；她含着泪发抖。", "0—6秒侧面中近景，镜头固定。",
    ('KillianBeast', "You left me in the snow.", 1.0),
    f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {KB} speaks in a hoarse, trembling snarl, his gold eyes burning on Lily's face, his jaw shaking and his lips pulled back from his fangs, his right hand pinning her wrists to the pillow. {LS} stares up at him, her lips quivering and her brows pulled together, tears sliding toward her temples, her chest heaving. The camera holds still.",
    "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安用沙哑、发颤的低吼说话，金色的眼睛燃烧着盯着莉莉的脸，下颌发抖，嘴唇向后拉开露出獠牙，右手把她的手腕按在枕头上。莉莉仰头望着他，嘴唇发颤，眉头拧在一起，泪水滑向太阳穴，胸口起伏。镜头固定不动。",
    voiced("The creak of the bed frame and ragged breathing.", "床架的吱嘎声和不稳的呼吸声。"))

# 14-03 手指插进他的头发 ---------------------------------------------------------------------------------------------
T14(True, '03｜手指插进头发', 5, ['KillianBeast', 'LilyShirt'], ('bedroom', 'killian_beast', 'lily_shirt'), ['bedroom'],
    "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the huge dark-wood bed. "
    "Lily at frame-left lies on her back, her wrists pinned against the pillow above her head, her damp hair spread on the pillow, in the oversized white shirt with the collar open, her lips parted, her brows pulled together, her wet eyes on Killian's face. "
    "Killian at frame-right leans over her facing frame-left, his right hand pinning both her wrists, in the white dress shirt with the loosened dark tie hanging, his eyes glowing a dark gold with slit pupils, his lips parted over his fangs, his jaw tight, his brows low. The frame holds exactly two people: Lily and Killian.",
    END_BED + LAY_BED,
    "侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，在深色木制大床上。"
    "莉莉在画面左边，仰躺着，两只手腕被按在头顶上方的枕头上，湿漉漉的头发铺散在枕头上，穿领口敞开的宽大白衬衫，嘴唇微张，眉头拧在一起，含泪的眼睛看着基利安的脸。"
    "基利安在画面右边，俯身在她上方，侧身朝画面左边，右手按着她的两只手腕，穿白衬衫，松开的深色领带垂着，眼睛发出暗金色的光、是竖瞳，嘴唇微张露出獠牙，下颌紧绷，眉头压低。画面里恰好两个人：莉莉和基利安。" + Z_END_BED + Z_BED,
    "基利安松开手，低头靠向她的颈侧；莉莉原本推拒的手指不由自主地插进他的黑发里。", "0—5秒侧面中近景，镜头固定。", None,
    f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {KB} lowers his head toward her neck, his right hand loosening from her wrists, his gold eyes narrowing and his jaw tight. {LS}'s freed hands slide up from the pillow and sink into his black hair, her eyes falling half closed, her lips parting in a soft, shaky breath and her brows easing. The camera holds still.",
    "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安低头靠向她的脖子，右手从她的手腕上松开，金色的眼睛眯起，下颌紧绷。莉莉被松开的双手从枕头上滑上来，插进他的黑发里，眼睛慢慢半闭，嘴唇张开呼出一口轻轻发颤的气，眉头舒展开。镜头固定不动。",
    breathy("Soft, shaky breathing and the rustle of linen and hair.", "轻轻发颤的呼吸声，和床单、头发的摩擦声。"))

# 14-04 标记台词 -----------------------------------------------------------------------------------------------------
T14(True, '04｜一旦被我标记', 6, ['KillianBeast', 'LilyShirt'], ('bedroom', 'killian_beast', 'lily_shirt'), ['bedroom'],
    "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the huge dark-wood bed. "
    "Lily at frame-left lies on her back, both hands buried in Killian's black hair, her damp hair spread on the pillow, in the oversized white shirt with the collar open, her eyes half closed, her lips parted, her brows pulled together. "
    "Killian at frame-right bends over her facing frame-left, his face a hand's width from her cheek, in the white dress shirt with the loosened dark tie hanging, his eyes glowing a dark gold with slit pupils and fixed on her face, his lips parted over his fangs, his jaw clenched, his brows low. The frame holds exactly two people: Lily and Killian.",
    END_BED + LAY_BED,
    "侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，在深色木制大床上。"
    "莉莉在画面左边，仰躺着，双手都埋在基利安的黑发里，湿漉漉的头发铺散在枕头上，穿领口敞开的宽大白衬衫，眼睛半闭，嘴唇微张，眉头拧在一起。"
    "基利安在画面右边，俯身在她上方，侧身朝画面左边，脸离她的脸颊只有一只手掌宽，穿白衬衫，松开的深色领带垂着，发出暗金色光的竖瞳眼睛紧盯着她的脸，嘴唇微张露出獠牙，下颌咬紧，眉头压低。画面里恰好两个人：莉莉和基利安。" + Z_END_BED + Z_BED,
    "基利安嗓音沙哑，说出“一旦被我标记，你就是我的”；莉莉的手指在他的头发里收紧。", "0—6秒侧面中近景，镜头固定。",
    ('KillianBeast', "Once I mark you, you're mine.", 1.0),
    f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {KB} speaks in a ragged, trembling growl, his gold eyes locked on Lily's face and his lips close to her cheek, his jaw clenched. {LS}'s fingers tighten in his hair, her eyes half closed, her lips parted and a tremor running through her shoulders. The camera holds still.",
    "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安用不稳、发颤的低吼说话，金色的眼睛紧盯着莉莉的脸，嘴唇贴近她的脸颊，下颌咬紧。莉莉的手指在他的头发里收紧，眼睛半闭，嘴唇微张，肩膀掠过一阵颤抖。镜头固定不动。",
    voiced("Ragged breathing and the rustle of linen.", "不稳的呼吸声和床单的摩擦声。"))

# 14-05 咬下去（本集结尾；不写黑屏）------------------------------------------------------------------------------------
T14(False, '05｜咬在颈侧', 6, ['KillianBeast', 'LilyShirt'], ('bedroom', 'killian_beast', 'lily_shirt'), ['bedroom'],
    "Side-on close-up two-shot, both people from the head to the shoulders, in the middle third of the frame, on the huge dark-wood bed. "
    "Lily at frame-left lies on her back with her head tilted back on the pillow and her neck bared toward Killian, her right hand buried in his hair, her eyes closed, her lips parted, her brows drawn together. "
    "Killian at frame-right bends over her, his face at the side of her neck, in the white dress shirt with the collar open, his gold eyes narrowed, his jaw tight, his lips an inch from her skin. The frame holds exactly two people: Lily and Killian.",
    END_BED + LAY_BED,
    "侧面的近景双人镜头，两个人都是头到肩膀，在画面中间三分之一，在深色木制大床上。"
    "莉莉在画面左边，仰躺着，头向后仰在枕头上，脖子朝着基利安露出来，右手埋在他的头发里，眼睛闭着，嘴唇微张，眉头拧着。"
    "基利安在画面右边，俯身在她上方，脸凑在她的颈侧，穿领口敞开的白衬衫，金色的眼睛眯起，下颌紧绷，嘴唇离她的皮肤只有一英寸。画面里恰好两个人：莉莉和基利安。" + Z_END_BED + Z_BED,
    "基利安低头在莉莉颈侧咬下；她发出一声短促的、没有字词的叫声，手指抓紧他的头发。", "0—6秒侧面近景，镜头固定。", None,
    f"A steady side-on close-up two-shot opens from the adopted first frame in {BD}: {KB} lowers his mouth to the side of Lily's neck and bites down, his shoulders tensing and his eyes closing, his jaw working. {LS} cries out in one short, ragged, wordless cry, her head pressing back into the pillow, her mouth open and her eyes squeezed shut, her fingers clutching his hair; then her fingers loosen and slide down his shoulder as her breath shudders out. The camera holds still.",
    "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是主卧：基利安把嘴唇压到莉莉的颈侧咬下去，肩膀绷紧，眼睛闭上，下颌用力。莉莉发出一声短促、不稳、没有字词的叫声，头向后顶进枕头，嘴巴张开，眼睛紧闭，手指抓紧他的头发；随后手指松开，沿着他的肩膀滑下，一口气颤抖着呼出。镜头固定不动。",
    breathy("One short, sharp wordless cry from Lily, the rustle of linen and ragged breathing.", "莉莉一声短促尖利、没有字词的叫声，床单的摩擦声，和不稳的呼吸声。"))

d.finish('第14集｜不可逆转的标记',
         '莉莉拼命挣扎，基利安一只手把她的双手手腕钉在枕头上。他嘶哑地说出十年前她家把他丢在雪地里；莉莉体内的 Luna 血脉让她的抗拒松动，手指不由自主地插进他的头发。基利安说“一旦被我标记，你就是我的”，低头咬在她的颈侧，莉莉发出一声短促的叫声。',
         O14)

# =========================================================================================================
# 对比实验 B（放最后，不进成片）
# =========================================================================================================
e = Batch(O14 + '.json', SERIES_TITLE, 4700)
ZHB = []
TB = maker(e, ZHB)

# B1 = 11-07 对照：同种子；人物图直接用金瞳版
s11_07 = a.tasks[6]
sB1 = TB(False, 'B1｜对照：金瞳人物图（对照11-07）', 5, ['KillianGold'], ('bedroom', 'killian_gold'), ['bedroom'],
         "Medium close-up of Killian alone, from the head to the chest, in profile facing frame-left, in the middle third of the frame, beside the huge bed, in the black three-piece suit, "
         "his eyes glowing a dark gold and lowered, his jaw set, his lips pressed flat, his brows drawn together. The tall dark-wood door with a brass handle is behind him at frame-right. The frame holds exactly one person, Killian.",
         END_BED + LAY_BED,
         "基利安一个人的中近景，头到胸口，侧身朝画面左边，在画面中间三分之一，站在大床旁边，穿黑色三件套西装，眼睛发出暗金色的光、垂着，下颌紧绷，嘴唇抿成平直的一条线，眉头拧着。带黄铜把手的高大深色木门在他身后的画面右边。画面里恰好一个人：基利安。" + Z_END_BED + Z_BED,
         "基利安低头站在床边，门外猛地一声重响，他猛地回头盯向房门，金色的眼睛烧得更亮。", "0—5秒侧面中近景，镜头固定。", None,
         f"A steady medium close-up opens from the adopted first frame in {BD}: {KG} lowers his gaze at frame-left, then a heavy blow shakes the door at frame-right and his head snaps toward it. His gold eyes blaze brighter, his lips pulling back from his sharp teeth, his jaw clenching and his nostrils flaring. The camera holds still.",
         "一个稳定的中近景，从已采用的开场图继续，场景是主卧：基利安在画面左边垂着视线，然后画面右边的门被重重一击，他的头猛地转向房门。他金色的眼睛烧得更亮，嘴唇向后拉开露出尖牙，下颌咬紧，鼻翼张开。镜头固定不动。",
         breathy("A heavy blow on wood and a deep, rising animal growl from beyond the door.", "木头上一声沉重的撞击，和门外越来越响的一声低沉的野兽低吼。"))
sB1['seed'] = s11_07['seed']

# B2 = 14-01 对照：同种子、同文字；不用上一集画面
sB2 = put_1401(TB)
sB2['title'] = 'B2｜对照：不用上一集画面（对照14-01）'
sB2['seed'] = s1401['seed']
sB2['use_previous_episode_state'] = False

# B3 单人被无形力量甩飞
TB(False, 'B3｜守卫被无形的力量甩飞', 5, ['Bodyguard'], ('bedroom', 'bodyguard'), ['bedroom'],
   "Side-on wide shot of Bodyguard alone, from head to toe, in the middle third of the frame, in the wrecked doorway at frame-right facing frame-left in a black suit, white shirt and black tie, mid-stride in a lunge with both hands curled into claws, "
   "his eyes bloodshot, his teeth bared, his jaw slack, his brows low. The splintered door hangs open beside him and the bed's charcoal-grey linen is at frame-left, empty. The frame holds exactly one person, Bodyguard.",
   END_BED + LAY_BED,
   "侧面的宽景镜头，保镖一个人，从头到脚，在画面中间三分之一，站在画面右边残破的门口，侧身朝画面左边，穿黑西装、白衬衫、黑领带，正迈出扑击的一步，双手弯成爪形，眼睛布满血丝，龇着牙，下颌松垮，眉头压低。裂开的门板敞开挂在他身旁，大床炭灰色的亚麻床品在画面左边，床上是空的。画面里恰好一个人：保镖。" + Z_END_BED + Z_BED,
   "保镖扑进房间，被一股无形的力量正面击中，倒飞着撞在门边的墙上，墙板开裂，他滑落在地。", "0—5秒侧面宽景，镜头固定。", None,
   f"A steady side-on wide shot opens from the adopted first frame in {BD}: {BGD} lunges one step into the room, then an invisible blast hits him square in the chest and hurls him backward through the air into the dark wall beside the doorway, the wall cracking behind him, and he slides down to the floor. His mouth opens in a shout of shock, his eyes bulging and his brows shooting up. The camera holds still.",
   "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是主卧：保镖朝房间里扑出一步，然后一股无形的冲击正正击中他的胸口，把他向后抛向空中，撞在门边的深色墙上，墙板在他身后开裂，他顺着墙滑到地上。他的嘴巴张开发出一声惊呼，眼睛凸出，眉毛飞扬。镜头固定不动。",
   breathy("A violent whoosh of air, a heavy thud against the wall and a crack of splitting wood.", "一声猛烈的呼啸风声、身体重重撞墙的闷响，和木板开裂的脆响。"))

e.finish('第11-14集B｜对比实验',
         '实验，不进成片：B1 同一个镜头（第 11 集 07 号）改用金瞳人物图；B2 同一个镜头（第 14 集 01 号）不用上一集最后的画面；B3 单人被无形的力量甩飞撞墙。B1、B2 与正式版同种子。',
         OB)

# =========================================================================================================
# 合并、说明
# =========================================================================================================
files = [os.path.join(FOLDER, x + '.json') for x in (O11, O12, O13, O14, OB)]
subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'merge_eps.py'), OMERGE, *files, '--allow-seeds', f"{s11_07['seed']},{s1401['seed']}", '--rename',
                '第11集｜Luna血脉=剧本第11集｜Luna血脉', '第12集｜Alpha的绝对压制=剧本第12集｜Alpha的绝对压制',
                '第13集｜野兽的真面目=剧本第13集｜野兽的真面目', '第14集｜不可逆转的标记=剧本第14集｜不可逆转的标记',
                '第11-14集B｜对比实验=剧本第11-14集B｜对比实验（实验）'], check=True)

SEGS = {k: x.d['episodes'][0]['segments'] for k, x in (('11', a), ('12', b), ('13', c), ('14', d), ('B', e))}
ZHS = {'11': ZH11, '12': ZH12, '13': ZH13, '14': ZH14, 'B': ZHB}
NAMES = {'11': '第 11 集 Luna 血脉', '12': '第 12 集 Alpha 的绝对压制', '13': '第 13 集 野兽的真面目', '14': '第 14 集 不可逆转的标记', 'B': '对比实验 B（3 个）'}


def fmt_table(segs):
    rows = ["| 号 | 名字 | 秒 | 在场 | 承接 | 英语台词 | 种子 |", "|---|---|---|---|---|---|---|"]
    for s in segs:
        dl = f"{s['dialogue'][0]['speaker']}：{s['dialogue'][0]['text']}" if s['dialogue'] else '（无台词）'
        flag = '是' if s['depends_on_previous'] else ('上一集画面' if s.get('use_previous_episode_state') else '否')
        rows.append(f"| {s['title'].split('｜')[0]} | {s['title'].split('｜')[1]} | {s['duration_seconds']} | {len(s['characters'])} | {flag} | {dl} | {s['seed']} |")
    return '\n'.join(rows)


def fmt_prompts(segs, zh):
    out = []
    for i, s in enumerate(segs):
        out.append(f"### {s['title'].split('｜')[0]}｜{s['title'].split('｜')[1]}（{s['duration_seconds']} 秒，种子 {s['seed']}）")
        out.append(f"- **开场图：** {zh[i]}")
        out.append(f"- **视频：** {s['shots'][0]['visual_zh']}")
        out.append(f"- **声音：** {s['sound_zh']}")
        if s['dialogue']:
            out.append(f"- **台词（单独传给插件）：** {s['dialogue'][0]['speaker']}：“{s['dialogue'][0]['text']}”")
        out.append("")
    return '\n'.join(out)


n_tasks = sum(len(v) for v in SEGS.values())
n_sec = sum(s['duration_seconds'] for v in SEGS.values() for s in v)
n_a = sum(len(SEGS[k]) for k in ('11', '12', '13', '14'))
sec_a = sum(s['duration_seconds'] for k in ('11', '12', '13', '14') for s in SEGS[k])
seed_txt = '、'.join(f"{min(s['seed'] for s in v)}–{max(s['seed'] for s in v)}" for k, v in SEGS.items() if k != 'B') + '、' + '、'.join(str(s['seed']) for s in SEGS['B'])
md = []
md.append("# 剧本第 11–14 集（主卧四集）＋对比实验：怎么用（2026-10-10）\n")
md.append(f"**只粘贴一个文件：** `{OMERGE}_全选复制粘贴.txt`。里面 5 段：剧本第 11、12、13、14 集（正式版，{n_a} 个任务、{sec_a} 秒）＋对比实验 B（{len(SEGS['B'])} 个任务、{n_sec - sec_a} 秒，**放在最后，不进成片**）。合计 {n_tasks} 个任务、{n_sec} 秒。种子：{seed_txt}（B1、B2 故意和正式版同种子，做对照）。\n")
md.append("设置照旧：视频/对白共用次数 = 1，对白时间余量 = 0；追加窗口不要勾“每集／总／任务秒数”。**追加必须等上一批全部跑完。**\n")
md.append(f"**预计时间：{n_tasks} 个任务 × 约 7 分钟 ≈ {n_tasks*7//60} 小时 {n_tasks*7%60} 分钟（7 分钟是上限推算，不是实测）。**\n")
md.append("**这批写在剧本第 11–14 集，不含第 15–18 集的原因：** 第 15–18 集换到别墅地下室、阳台、飞机、仓库，并且要出现“大黑狼”“银匕首贴脖子”“被劫持”，全是新地方、新动物、新道具；马场四集的视频（马、两人一马）还没回来，我不想在没有数据时一次写 8 集再返工。主卧四集是同一个房间、同样两个人，素材少、测试点集中。你要我现在也写第 15–18 集，说一声。\n")
md.append("## 零、插件里显示第几集（集标题前面我加了“剧本”二字）\n")
md.append("你 14:10 说马场合并稿已经跑完，补拍包 2 之前没跑。我按这个顺序算：**补拍包 2（5 个任务，现成文件，现在就可以贴）→ 本文件**。\n")
md.append("| 追加顺序 | 内容 | 插件里显示 |\n|---|---|---|")
md.append("| ① 已跑 | 补拍包 1（5 个任务） | 第 10 集 |\n| ② 已跑 | 马场合并稿（剧本第 7、8、9、10、10B） | 第 11–15 集 |\n| ③ 现在贴 | 补拍包 2（5 个任务） | 第 16 集 |\n| ④ 本文件 | 剧本第 11 集 | 第 17 集 |\n| ④ 本文件 | 剧本第 12 集 | 第 18 集 |\n| ④ 本文件 | 剧本第 13 集 | 第 19 集 |\n| ④ 本文件 | 剧本第 14 集 | 第 20 集 |\n| ④ 本文件 | 对比实验 B | 第 21 集 |\n")
md.append("如果你先贴本文件、补拍包 2 放后面，本文件就是第 16–20 集，补拍包 2 是第 21 集。屏幕上的号以你那边为准，集标题里的“剧本第几集”不会错。\n")
md.append("## 一、我对剧本改了什么（先说清楚，你可以否决）\n")
md.append("原则不变：H3 做得稳的是**单人／双人、侧面、手有主人、小动作**；做不稳或没试过的大动作，正式版里**用“结果镜头”绕开**，同时把值得知道的放进 B 里测。亲密戏全程**穿着衣服、非露骨**（美国平台惯例）。\n")
md.append("| 剧本原写 | 我怎么拍（正式版） | 为什么 | 补救／验证 |\n|---|---|---|---|")
md.append("| 11：“全景转中景”，莉莉昏迷、基利安站床边盯着医生 | 11-01 只拍床上的莉莉；11-02 起拍医生和基利安 | 一个镜头最多 2 人 | — |")
md.append("| 11：医生“手抖，吓得跪在地上” | 11-02 开场图里医生已经跪着、举着试管 | 跪下的动作不拍，直接给结果 | — |")
md.append("| 11：基利安“把医生提了起来” | 11-03、11-04：揪着领子把他拽得站直（踮脚），不拎离地面 | 提离地面没试过 | 马场合并稿里 T2 在测“单手提起一个人” |")
md.append("| 11：“异香炸开” | 拍不出来，用 11-05 莉莉弓身倒吸气、11-06 门被撞、11-07 基利安回头来演 | 气味画不出来 | — |")
md.append("| 11：“几个保镖疯狂挠门” | 11-06 画面里只有门，没有人；门后一个男人的声音喊话 | 人群最多 2 人；门挡着正好解释“看不见人” | 声音在门后，是新写法，要听（见第四节） |")
md.append("| 11：“暗金色的瞳孔彻底点亮” | 11-07 用普通基利安人物图，文字写“眼睛点亮”；B1 用金瞳人物图做对照 | 想知道文字能不能让眼睛变金色 | B1 对照 |")
md.append("| 12：“三个失去理智的狼人双眼猩红扑向莉莉” | 12-02 一个守卫＋莉莉；12-05、12-06 里也只有一个守卫在场 | 一个镜头最多 2 人 | 另外几个守卫不拍 |")
md.append("| 12：“基利安反手一挥，巨大的无形力量把三个狼人砸在墙上，墙壁龟裂” | 12-03 基利安反手一挥（只拍他）；12-04 两个守卫瘫在裂开的墙上（结果）；被甩飞的动作本身放进 B3 | 人被“甩飞”没试过 | B3 |")
md.append("| 12：“走廊尽头更多狼人蠢蠢欲动”“所有狼人捂耳朵跪倒” | 12-05、12-06 里一个守卫退缩、捂耳朵、跪下 | 同上 | — |")
md.append("| 12：“震碎玻璃的低吼” | 只有台词 `One more step, and you die.` ＋声音里一声低吼 | 低吼的声音画不出来，靠声音 | — |")
md.append("| 12：“关上残破的门，反锁；解开衬衫扣子；黑屏” | 12-07 反锁；12-08 解领带和最上面的扣子；**不写黑屏** | 黑屏我写了 H3 也不一定做 | — |")
md.append("| 13：“莉莉扯开领口，露出雪白的肌肤和锁骨” | 13-01 只崩开最上面的扣子，露出锁骨 | 非露骨 | — |")
md.append("| 13：“基利安脱下西装外套扔在地上，缓步逼近” | 不拍脱衣服；13-02 开场图里他已经只穿衬衫，外套皱巴巴丢在地毯上 | 脱衣服是大动作，也容易写成露骨 | 新人物图 `killian_shirt`；马甲也去掉了 |")
md.append("| 13：“莉莉摸到獠牙；瞳孔变成竖瞳，指甲变黑” | 13-03 用“切镜变身”：这一镜的人物图 `killian_beast` 本来就是竖瞳、獠牙、黑指甲；莉莉的指尖碰到獠牙 | 让 H3 在一个片段里“变身”没把握，用剪辑做变身最稳 | 看 13-02→13-03 这一刀的脸像不像同一个人 |")
md.append("| 13：“攥住脚踝，狠狠拖回自己身下” | 13-05 照拍（抓人者的肩、臂、手都在画面里） | 这是整批最大的双人动作 | 失败就改成“手握住脚踝”的结果镜头 |")
md.append("| 14：“只手钉住双手手腕”“滚烫的鼻息喷在颈动脉上” | 14-01 钉手腕照拍；“鼻息”不写 | 非露骨 | — |")
md.append("| 14：“十年前你们家把我像狗一样丢在雪地里…”（很长） | `You left me in the snow.` | 台词 ≤6 个单词 | “十年前”“像狗一样”都没了，核心是“雪地” |")
md.append("| 14：“娇吟”“痛苦又欢愉的尖叫”“拉黑” | 14-03 只写呼吸；14-05 只写一声短促的、没有字词的叫声；不写黑屏 | 非露骨；“尖叫”是否变成乱码人声要听 | 见第四节 |")
md.append("| 其他 | 莉莉全程穿 `lily_shirt`（白色男式衬衫，第 5 集的素材）；基利安 11–12 西装、13–14 衬衫；全部侧面机位 | 马场里她穿马术装，到床上换成白衬衫（没拍“被换衣服”） | 如果觉得突兀，可以补一个“基利安抱她进门”的镜头 |\n")
md.append("## 二、接缝检查（自查清单第 13、21 条）\n")
md.append("**故事层：**\n")
md.append("| 接缝 | 上一镜 | 下一镜 | 怎么接 | 风险 |\n|---|---|---|---|---|")
md.append("| 剧本第 10 集末 → 11-01 | 马场，莉莉晕倒在基利安怀里 | 主卧，高烧昏迷 | 硬切；衣服从马术装变成白衬衫 | 观众不知道怎么回的别墅；先不补 |")
md.append("| 11-07 → 12-01 | 门被撞到变形，基利安回头 | 门被撞碎 | 同一扇门、同一个位置（画面右边）；12-01 开场图里门已经裂开 | — |")
md.append("| 12-08 → 13-01 | 基利安解衬衫扣子走向床 | 莉莉扯开领口 | 同一夜同一房间 | 他脱外套没拍；13-02 地毯上有外套 |")
md.append("| 13-05 → 14-01（跨集） | 基利安攥着脚踝把她拖到身下 | 他把她的手腕钉在枕头上 | 同房间、同两个人、同一个镜头方向；**这里用 `use_previous_episode_state`（A）** | 这是第一次用这个开关，见测试表 |")
md.append("| 14-05 → 剧本第 15 集 | 基利安咬下去 | 保罗的别墅地下室 | 硬切到另一个地点 | 咬痕要给第 16 集用：我记下“咬在她脖子靠近镜头的这一侧” |\n")
md.append("**每场戏的结果镜头：** 发现血统（11-04 医生说出 Luna）；危机（11-06 门被撞、11-07 基利安回头）；压制（12-04 守卫瘫在墙上、12-06 守卫跪下）；封门（12-07 反锁）；揭示（13-03 獠牙）；追回（13-05 脚踝）；标记（14-05 咬下去）。\n")
md.append("**关键信息谁第一次说出口：** “她不是人类”——医生 11-02；“Luna／觉醒发情期”——医生 11-04；守卫为什么发狂——守卫在门后喊 `That scent!`（11-06）；他是怪物——莉莉 13-04；他的仇恨——基利安 14-02（`snow`）；标记——基利安 14-04。\n")
md.append("**画面层（相邻镜头逐对列表：人数、手里的东西、位置朝向、地点）：**\n")
md.append("| 接缝 | 人（上一镜→下一镜） | 手里的东西／道具 | 位置朝向 | 要看什么 |\n|---|---|---|---|---|")
md.append("| 11-01→11-02 | 莉莉 1 人 → 医生＋基利安 2 人 | 试管第一次出现（医生举着） | 床在 11-01 是主体，在 11-02 只是左边的背景 | 医生的脸（没有参考脸）|")
md.append("| 11-02→11-03（承接） | 同两人 | 试管一直在医生手里 | 医生跪着 → 被拽得站起；基利安一直在画面右边 | 承接是否保住房间 |")
md.append("| 11-03→11-04（承接） | 同两人 | 同上 | 站直 → 踮脚 | 同上 |")
md.append("| 11-04→11-05 | 2 人 → 莉莉 1 人 | 试管不再出现 | 画面左边的床变成主体 | 莉莉的衬衫扣子扣到锁骨 |")
md.append("| 11-05→11-06 | 1 人 → 0 人 | 门 | 门在画面右边 | **画面里不能冒出人** |")
md.append("| 11-06→11-07 | 0 人 → 基利安 1 人 | 门 | 门在他身后的画面右边 | 门的位置和 11-06 对得上 |")
md.append("| 11-07→12-01 | 基利安 → 0 人 | 门 | 门从鼓起变成裂开 | 门的位置不能换边 |")
md.append("| 12-01→12-02 | 守卫 1 人 → 守卫＋莉莉 2 人 | 无 | 守卫在破门口，莉莉在床上（画面左边和中间） | 莉莉不能被画成坐着或站着 |")
md.append("| 12-02→12-03 | 守卫＋莉莉 → 基利安 1 人 | 无 | 基利安在床边，背对破门（画面右边） | 12-03 里不应有别人 |")
md.append("| 12-03→12-04 | 基利安 → 两个守卫 | 无 | 卧室→走廊（切地点） | 恰好两个人 |")
md.append("| 12-04→12-05 | 两个瘫倒的守卫 → 基利安＋另一个站着的守卫 | 无 | 走廊，卧室门在画面左边 | 12-05 里不应再出现躺着的人 |")
md.append("| 12-05→12-06（承接） | 同两人 | 无 | 守卫退缩 → 跪倒 | 基利安的位置、利爪是否保住 |")
md.append("| 12-06→12-07 | 2 人 → 基利安 1 人 | 无 | 走廊→回到卧室门口（门板挂在画面右边） | 门的位置 |")
md.append("| 12-07→12-08 | 基利安 → 基利安＋莉莉 | 领带 | 门口→床边 | 莉莉躺在床上 |")
md.append("| 12-08→13-01 | 2 人 → 莉莉 1 人 | 衬衫领口 | 西装→无关 | 莉莉的衬衫和 12-08 一致 |")
md.append("| 13-01→13-02 | 莉莉 → 莉莉＋基利安 | 地毯上的外套（第一次出现） | 基利安跪在床沿、画面右边 | 外套不能画成别的东西 |")
md.append("| 13-02→13-03 | 同两人 | 无 | 中景→近景；基利安的脸变成竖瞳獠牙（有意） | 这一刀脸像不像同一个人 |")
md.append("| 13-03→13-04（承接） | 同两人 | 无 | 同一景别 | 承接 |")
md.append("| 13-04→13-05 | 同两人 | 无 | 近景→宽景；莉莉的头在画面左边 | 手脚数量 |")
md.append("| 13-05→14-01（跨集） | 同两人 | 无 | 拖回身下 → 钉手腕 | 位置参考有没有帮上，还是把旧姿势“拷”过来 |")
md.append("| 14-01→14-02→14-03→14-04（承接） | 同两人 | 手腕被按住 → 被松开 → 手在头发里 | 同一景别 | 手有没有多出来 |")
md.append("| 14-04→14-05 | 同两人 | 无 | 中近景→近景，嘴靠近脖子 | 脖子侧面朝向镜头 |\n")
md.append("## 三、做完能得到什么（想测什么、怎么算成功、失败说明什么）\n")
md.append("**这批的总体目的：** 第一次拍“床上的双人戏”（躺、跪、压）、“特征变化”（金瞳、竖瞳、獠牙、利爪）、“隔着门的声音”，以及第一次用 `use_previous_episode_state`（跨集接画面）。前面学到的规矩（每人写表情、不画外、6 秒放台词、大冲突排满整段）在新题材里还成不成立。\n")
md.append("| 任务 | 想测什么 | 算成功 | 失败说明什么 |\n|---|---|---|---|")
md.append("| 11-02～11-04 | 没有参考脸的医生；同两个人连拍三段（承接）；一句话一个说话人 | 医生的脸三段像同一个人，试管在手，台词念完 | 医生换脸：配角以后要给参考脸 |")
md.append("| 11-06 | **门后的声音，画面里没有人**（上次保罗“只有声音”被观众读成缺人，这次有门挡着） | 画面里没有人，台词念完，声音听着是在门后 | 冒出人：门后的声音改成画面里有人；声音不对：改成无台词＋吼声 |")
md.append("| 11-07 vs B1 | **文字能不能让眼睛变金**（A 普通人物图＋“眼睛点亮”；B1 金瞳人物图、开场图里眼睛一开始就是金色）。同种子，只差人物图和开场图里的眼睛颜色 | A 里眼睛真的变金：以后只用文字，省人物图；A 不变、B1 金色：以后“发光”类用专门的人物图 | 两个都不金：眼睛发光放弃，用表情和台词 |")
md.append("| 12-01 | 门炸开＋碎木头；中途冒出一个没有参考脸的人 | 门板飞出，一个人进来 | 碎片乱：门破的画面改成“门已经破了”的结果镜头 |")
md.append("| 12-03 | 单人“反手一挥”（手臂向后挥、劲风吹衣服） | 他的头朝画面左边、手臂向后挥 | 手臂画错：改成手掌特写 |")
md.append("| 12-04 | 同款两人瘫在裂开的墙上（一个素材画两个人，马场 10-01 的同类） | 恰好两个人，墙裂 | 数不对：群像永远两人以内 |")
md.append("| 12-05、12-06 | 走廊新场景；退缩→捂耳朵→跪下的连贯动作（承接）；台词与吼声 | 守卫跪下，台词念完 | 跪不下去：改成“已经跪着”的结果镜头 |")
md.append("| 13-01 | **英语里念基利安的名字**（`Killian`，Q19，之前只有中文版测过一半读偏）；哭腔 | 听着是 Killian（hh 的耳朵） | 读偏：名字以后少放进台词，用 `Alpha` 之类代替 |")
md.append("| 13-02 | 床上的双人：一个躺着，一个单膝跪在床沿捧着脸；衬衫素材 | 姿势对，手有主人，外套在地毯上 | 姿势乱：床上双人以后只拍近景脸 |")
md.append("| 13-03 | **变身靠“切镜”**：这一镜人物图直接是竖瞳獠牙；指尖碰獠牙（小物件＋手） | 竖瞳、獠牙看得出，莉莉缩手 | 獠牙画成牙齿一排：改成嘴部不特写，只写眼睛 |")
md.append("| 13-04 | 承接 13-03；尖叫的台词 | 台词念完，没有乱码尖叫 | 尖叫变乱码：尖叫改成台词＋“声音里的尖叫” |")
md.append("| 13-05 | **抓脚踝往回拖**（双人大动作） | 拖动、手抓在脚踝上、没有多出的手 | 失败：改成结果镜头（手握着脚踝） |")
md.append("| 14-01 vs B2 | **跨集接画面：`use_previous_episode_state`**。同种子、同文字，只差 A 用上一集最后画面、B2 不用 | A 的床、枕头、镜头方向和 13-05 接得更好、姿势仍按文字变成“钉手腕”；B2 作对照 | A 把旧姿势拷过来、不按文字变：这个开关只用在“姿势没变”的接缝 |")
md.append("| 14-02～14-04 | 承接连拍三段（同一个姿势）；对话节奏 | 姿势连得上，手腕被松开的变化能看出 | 姿势跳：长对话合成一个更长的任务 |")
md.append("| 14-03 | **手指插进头发**（手有主人） | 双手从枕头滑到头发里 | 手多出来：改成一只手 |")
md.append("| 14-05 | **咬在颈侧**（非露骨）＋一声没有字词的叫声 | 嘴靠近脖子侧面、叫声不是乱码人话 | 叫声变乱码：叫声去掉；嘴部画乱：改成他的肩膀盖住 |")
md.append("| B3 | 单人被无形力量甩飞撞墙 | 他倒飞、撞墙、滑下 | 画面乱：这类“被甩飞”永远用结果镜头 |\n")
md.append("## 四、跑完以后要回发哪些视频（你让我决定，我只要这些）\n")
md.append("**必发（17 个）：** 11-04、11-06、11-07、B1、12-01、12-03、12-04、12-06、13-01、13-03、13-04、13-05、14-01、B2、14-03、14-05、B3。\n")
md.append("**不用发：** 11-01、11-02、11-03、11-05、12-02、12-05、12-07、12-08、13-02、14-02、14-04。你看了觉得哪个不对，就发那个并写“号码＋大概第几秒”；不确定就不写，我自己查。\n")
md.append("**你的耳朵帮我听三处：** ① 11-06 门后的那句话（听着像不像在门后、念对没有）；② 13-01 里 `Killian` 念对没有；③ 14-05 的叫声是不是乱码人话。\n")
for k in ('11', '12', '13', '14', 'B'):
    md.append(f"## 五-{k}、{NAMES[k]}的任务\n")
    md.append(fmt_table(SEGS[k]))
    md.append("")
md.append("## 六、给 H3 的提示词（中文全译，一个字不漏）\n")
md.append("每个任务的视频提示词前面还会加这句固定的风格话：**“真人实拍，电影感，写实，皮肤有自然质感，浅景深，温暖奢华的光线，超宽 8:3 宽银幕画面。”** 开场图提示词前面也有固定的开头：**“一张来自写实真人浪漫惊悚片的完整首帧，超宽 8:3 宽银幕构图。皮肤自然，能看到毛孔，布料和材质真实。固定的场景参考图决定地点，人物肖像只决定被点名的人。”** 下面不再重复。\n")
md.append("新素材（场景 corridor；人物 doctor、killian_gold、killian_shirt、killian_beast）的图片提示词都在 JSON 里，三个基利安的新装束都用 `ref` 指向原来的基利安以保脸。**医生没有参考脸；11-06 和 12-01 的“门后的人／冲进来的人”没有人物图。**\n")
for k in ('11', '12', '13', '14', 'B'):
    md.append(f"### {NAMES[k]}\n")
    md.append(fmt_prompts(SEGS[k], ZHS[k]))
md.append("## 七、我预计会出问题的地方（没试过，只是判断；按自查清单第 5 条逐项过）\n")
md.append("- **床上的双人（13-02～14-05）**：两个人躺／跪／压在一张床上，手脚数量、身体融在一起、衬衫和床单分不清，是我预计最容易整段作废的地方。看开场图时数手、数脚。\n"
          "- **金瞳、竖瞳、獠牙、利爪（11-07、12-03、12-05、13-03～14-05）**：靠人物图固定；利爪的手指数量、獠牙是不是“一排牙”。\n"
          "- **隔着门的声音（11-06）**：画面里要没有人；有风险是 H3 把喊话的人画出来，或者把声音当成画面里的人说的。11-06 的“说话人”用了只出声的角色 `GuardFrenzy`（图用的是保镖素材，但这一镜的开场图里不放他）。\n"
          "- **门炸开（12-01）、被甩飞（B3）**：碎木头和倒飞的物理，我预计会乱。\n"
          "- **走廊（12-04～12-06）**：新场景；两个同款保镖是同一个素材画两个人；12-05 的守卫“离他十二英尺”，距离感可能被压缩。\n"
          "- **特征变化靠人物图、变身靠切镜（13-02→13-03）**：这一刀脸会不会换人。\n"
          "- **名字读音（Q19）**：13-01 里 `Killian`；基利安自己的名字不出现在他的台词里。\n"
          "- **承接前段的断点（自查清单第 7 条）**：承接只在同两人、同景别、同地点的相邻任务（11-03、11-04、12-06、13-04、14-02、14-03、14-04）；每集第一个任务一律不承接；14-01 是跨集（A）。\n"
          "- **默认微笑（第 2 条）**：每个人物每个任务都写了表情。床上的任务容易被补成“迷离的笑”，看 13-02、14-03、14-04。\n"
          "- **台词位置（第 4 条）**：有台词的任务都是 6 秒、≤6 个单词，仍然要听结尾（11-02、11-03、11-04、11-06、12-06、13-01、13-02、13-04、13-05、14-02、14-04）。11-03→11-04 是连着两个说话人的承接，中间可能有 2–4 秒的无声接缝。\n"
          "- **内容过滤**：13、14 集是“暗黑狼人言情”的亲密戏，我按“穿着衣服、不露骨”写；如果插件或模型拒绝出图，会在 14-01～14-05 里最先出现。\n")
md.append("## 八、开场图检查清单（床上戏专用，每张先看 10 秒）\n")
md.append("① 人数对不对（恰好 1 或 2 人；11-06、12-01 的开场图里应该 0 人）② 每只手都有主人，手腕被按住时只有一只手在按 ③ 每个人的脚／腿数量对 ④ 人是不是在画面中间三分之一 ⑤ 床、门的位置和 `bedroom` 参考图一致（床在左和中，门在右）⑥ 衣服对（莉莉白衬衫；基利安 11–12 西装、13–14 衬衫）⑦ 表情对（没有不想要的笑）⑧ 基利安的眼睛颜色对：11-02～11-07 灰色（B1 例外）、12 集全程金色、13-02 灰色、13-03 起金色竖瞳。\n")
md.append("## 九、和以前几集的区别（已按“Claude 易错点自查清单”）\n")
md.append("- 每个人物每个任务都写了表情；没有“画外的人”；没有“走出画面”的动作；视线都落在画面里的人或物上（床、门、对方的脸）。\n"
          "- 有台词的任务都是 6 秒、≤6 个单词；没有 5 秒任务放台词；台词里没有“短词＋句号＋后半句”的结构（Sorry. I'll … 那种，之前测出短词后会停 2.2–2.4 秒）。\n"
          "- 大冲突（12-01、12-03、12-06、13-03、13-05、14-01、14-05）：动作排满整段；没有 stays／remains 定住句；开场图画动作发生之前的状态；无台词片的声音句改成“没人说话，只有呼吸和动作声”（`breathy`，不再像以前一刀切禁呼吸）。这套新写法在补拍包 2 里有同镜头对照在测，这里是直接用在正片上。\n"
          "- 承接前段只在同人同景别同地点；每集第一个任务一律不承接；唯一的跨集接画面是 14-01（附 B2 对照）。\n"
          "- 小细节（外套、红痕）：外套在 13-02 开场图的地毯上；咬痕留给第 16 集，到时要写明咬在朝向镜头的这一侧。\n")
open(os.path.join(FOLDER, '合并稿/合并_第11-14集+B_说明.md'), 'w', encoding='utf-8').write('\n'.join(md))
print('说明已写', n_tasks, '个任务', n_sec, '秒')
