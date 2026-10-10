#!/usr/bin/env python3
"""第 6 集“绿茶修罗场”制作稿（追加批次，英语台词，美式口语）+ 第 6 集 B 对比测试（2026-10-09 晚）。

A 正式版：8 个任务 44 秒，种子 3501–3508。承接前段只在 03（接 02）、06（接 05），其余人数或人物一变就关掉（第 3 集：另一个人被移出画面的连续段，房间会冒出原来没有的东西）。
B 对比测试：10 个任务，必须在 A 之后追加，是实验、不进成片（R1、X1、X2 同时是第 3 集 07/13/14 号的补拍候选）：
  S1a/S1b、S2a/S2b、S3a/S3b：同种子、同开场图文字，只差“视频文字里有没有写表情”（验证：没写表情会不会默认笑，笑是在视频阶段才出现的吗）；
  X1、X2：两种“人离开并关门”的站位（验证 H20）；
  X3：宴会厅里背景远处有几个客人，会不会多出前景的人；
  R1：莉莉坐在地上、基利安站着低头看她，两人都入画（验证 H19：用“两人入画”代替“画外的人”）。
基于第 5 集 JSON（style、素材、角色逐字复制，F11），新增：场景 ballroom；人物 lily_red、killian_tux、mary；角色 LilyRed、KillianTux、Mary。
本集已按“Claude 易错点自查清单”写：每个人物每个任务都写表情；没有画外目标；有台词的任务都是 6 秒、≤6 个单词；承接前段只在同一批人同一地点。
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, silent, voiced

BASE = '第05集/第05集_制作稿_追加.json'
OUT_A = '第06集/第06集_制作稿_追加'
OUT_B = '第06集/第06集B_对比测试_表情_退场_背景人群_补拍候选'
SERIES_TITLE = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))['title']


def maker(batch, zh):
    def T(flag, title, dur, chars, assets, refs, img, end, img_zh, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound):
        s = batch.task(title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound)
        s['depends_on_previous'] = flag
        zh.append(img_zh)
        return s
    return T


# =========================================================================================================
# A 正式版
# =========================================================================================================
a = Batch(BASE, SERIES_TITLE, 3500)
ZH_A = []
TA = maker(a, ZH_A)

a.scene('ballroom', '财团晚宴大厅',
        ("A grand gala ballroom: a polished cream marble floor, a dark-red carpet runway down the middle, tall gold-trimmed columns, huge crystal chandeliers, a wide marble staircase on the left and a long banquet table with white linen and champagne towers on the right, warm golden light. The reference fixes the layout and decor."),
        ("盛大的晚宴大厅：抛光的奶油色大理石地面，中间一条深红色的地毯，高大的镶金边柱子，巨大的水晶吊灯，左边是宽阔的大理石楼梯，右边是铺着白桌布、摆着香槟塔的长长的宴会桌，温暖的金色灯光。参考图固定布局与陈设。"),
        ("A photorealistic ultra-wide 8:3 cinemascope shot of a grand gala ballroom: a polished cream marble floor, a dark-red carpet runway down the middle, tall gold-trimmed columns, huge crystal chandeliers, a wide marble staircase on the left and a long banquet table with white linen and champagne towers on the right, warm golden light. "
         "The frame holds the staircase, the carpet, the columns, the chandeliers and the banquet table."))
a.person('lily_red', '莉莉（红色晚礼服）',
         ("Lily, the same adult woman in her mid-twenties as in the reference, with long wavy chestnut-brown hair pinned in a loose low twist with a few strands falling free, fair skin and large hazel-green eyes, "
          "wearing a floor-length red satin evening gown with thin straps and a small beige adhesive bandage on the left side of her neck. The portrait fixes her identity, gown and bandage, not staging."),
         "莉莉，和参考图是同一个二十五岁左右的成年女性，栗棕色长卷发松松地盘成低髻、有几缕散落，白皙皮肤、浅褐绿色大眼睛，穿及地的红色缎面细肩带晚礼服，脖子左侧贴着一块小小的米色创可贴。人物图固定身份、礼服和创可贴，不固定站位。",
         ("A photorealistic half-body portrait of the same woman as in the reference image, long wavy chestnut-brown hair pinned in a loose low twist, wearing a floor-length red satin evening gown with thin straps and a small beige adhesive bandage on the left side of her neck. "
          "She faces the camera with a composed, slightly nervous expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores."),
         ref='lily')
a.person('killian_tux', '基利安（黑色无尾礼服）',
         ("Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short swept-back black hair, a sharp jawline, light stubble and cold dark-gray eyes, "
          "wearing a black tuxedo with a white shirt, a black bow tie and a white silk pocket square, a platinum luxury wristwatch on his left wrist. The portrait fixes his identity and clothes, not staging."),
         "基利安，和参考图是同一个三十出头、身材极高、肩膀宽阔的成年男性，黑色短发向后梳，下颌线锋利，有浅胡茬，眼睛是冷冷的深灰色，穿黑色无尾礼服，配白衬衫、黑色领结和白色丝质胸袋巾，左手腕戴铂金名表。人物图固定身份和衣服，不固定站位。",
         ("A photorealistic half-body portrait of the same man as in the reference image, short swept-back black hair, sharp jawline, light stubble, cold dark-gray eyes, wearing a black tuxedo with a white shirt, a black bow tie and a white silk pocket square, a platinum luxury wristwatch on his left wrist. "
          "He faces the camera with a cold, composed expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores."),
         ref='killian')
a.person('mary', '玛丽（保罗的妹妹）',
         ("Mary, an adult woman in her mid-twenties with sleek honey-blonde hair in an elegant updo, flawless makeup, glossy red lips and sharp green eyes, "
          "wearing a white satin cocktail dress with a sweetheart neckline, a pearl necklace and pearl drop earrings. The portrait fixes her identity and dress, not staging."),
         "玛丽，二十五岁左右的成年女性，光滑的蜜金色头发盘成优雅的发髻，妆容无瑕，嘴唇红亮，一双锐利的绿眼睛，穿白色缎面心形领鸡尾酒裙，戴珍珠项链和珍珠垂坠耳环。人物图固定身份和裙子，不固定站位。",
         ("A photorealistic half-body portrait of an adult woman in her mid-twenties with sleek honey-blonde hair in an elegant updo, flawless makeup, glossy red lips and sharp green eyes, wearing a white satin cocktail dress with a sweetheart neckline, a pearl necklace and pearl drop earrings. "
          "She faces the camera with a sweet, coy expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores."))
v = a.d['characters']['LilyCoat']['voice_description']
a.character('LilyRed', 'lily_red', v['en'], v['zh'])
v = a.d['characters']['KillianRobe']['voice_description']
a.character('KillianTux', 'killian_tux', v['en'], v['zh'])
a.character('Mary', 'mary',
            "A young adult female voice, sugary and syrupy with a coy, breathy lilt, speaking clear American English. Every word is fully voiced and audible.",
            "年轻成年女声，甜得发腻，带着娇滴滴的、有气息的上扬语调，说清楚的美式英语。每个字都正常发声、清晰可辨。")

BR = '[[asset:ballroom]]'; LR = '[[asset:lily_red]]'; KT = '[[asset:killian_tux]]'; MY = '[[asset:mary]]'; PL = '[[asset:paul]]'
LAY = " Fixed stage layout: the wide marble staircase is at frame-left; the long banquet table is at frame-right."
LAY_LK = LAY + " Lily is always at frame-left of Killian."
LAY_KM = LAY + " Mary is always at frame-right of Killian."
Z_LAY = "固定布局：宽阔的大理石楼梯在画面左边；长长的宴会桌在画面右边。"
Z_LK = Z_LAY + "莉莉始终在基利安左边。"
Z_KM = Z_LAY + "玛丽始终在基利安右边。"
END = " Warm golden chandelier light, the ballroom softly blurred behind."
Z_END = "温暖的金色吊灯光，宴会厅在后面柔和虚化。"
QUARTET = ("A string quartet playing softly in the distance and the faint clink of crystal.", "远处弦乐四重奏轻轻的演奏声，和水晶杯轻轻的碰撞声。")

# 01 站在宴会厅（两人都入画，视线落在画面里的宴会桌上）--------------------------------------------------------
TA(False, '01｜站在宴会厅', 5, ['LilyRed', 'KillianTux'], ('ballroom', 'lily_red', 'killian_tux'), ['ballroom'],
   "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, both in profile facing frame-right. "
   "Lily at frame-left in a floor-length red satin gown, a small beige bandage on the side of her neck, her hands folded in front of her, her lips pressed together, her eyes on the long banquet table at frame-right. "
   "Killian at frame-right in the black tuxedo with a white silk pocket square, his hands at his sides, his jaw set, his eyes narrowed on the long banquet table. The frame holds exactly two people: Lily and Killian.",
   END + LAY_LK,
   "侧面的中景双人镜头，两个人都是头到膝盖，在画面中间三分之一，都侧身朝画面右边。莉莉在画面左边，穿及地的红色缎面晚礼服，脖子侧面贴着一块小小的米色创可贴，双手交叠在身前，嘴唇抿紧，眼睛看着画面右边那张长长的宴会桌。"
   "基利安在画面右边，穿黑色无尾礼服，配白色丝质胸袋巾，双手垂在身侧，下颌紧绷，眯着眼看着那张长长的宴会桌。画面里恰好两个人：莉莉和基利安。" + Z_END + Z_LK,
   "莉莉和基利安并肩站在宴会厅里，都侧身朝右，看着长长的宴会桌；莉莉抿紧嘴唇，基利安下颌紧绷。", "0—5秒侧面中景，镜头固定。", None,
   f"A steady side-on medium two-shot opens from the adopted first frame in {BR}: {LR} at frame-left and {KT} at frame-right, both in profile facing frame-right, their eyes on the long banquet table at frame-right. "
   "Lily's lips press tighter and her fingers tighten on each other; Killian's jaw tightens. Both stay where they are. The camera holds still.",
   "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是晚宴大厅：莉莉在画面左边，基利安在画面右边，两人都侧身朝画面右边，眼睛看着画面右边那张长长的宴会桌。莉莉的嘴唇抿得更紧，手指互相攥紧；基利安的下颌收紧。两人都留在原处。镜头固定不动。",
   silent(*QUARTET))

# 02 玛丽贴上来（双人近身 + 台词；玛丽的“甜笑”是想要的表情，所以明确写出来）--------------------------------------
TA(False, '02｜玛丽贴上来', 6, ['Mary', 'KillianTux'], ('ballroom', 'mary', 'killian_tux'), ['ballroom'],
   "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame. "
   "Killian at frame-left in the black tuxedo, in profile facing frame-right, his jaw set, his eyes cold and level on Mary's face. "
   "Mary at frame-right in the white satin cocktail dress, in profile facing frame-left, her shoulder pressed against his upper arm, one hand resting on his sleeve at the elbow, her other hand holding a glass of red wine at chest height, her chin tilted up, a sweet coy smile, her eyes on his face. "
   "The frame holds exactly two people: Killian and Mary.",
   END + LAY_KM,
   "侧面的中景双人镜头，两个人都是头到膝盖，在画面中间三分之一。基利安在画面左边，穿黑色无尾礼服，侧身朝画面右边，下颌紧绷，冷冷地平视着玛丽的脸。"
   "玛丽在画面右边，穿白色缎面鸡尾酒裙，侧身朝画面左边，肩膀贴着他的上臂，一只手搭在他袖子的肘部，另一只手在胸口的高度端着一杯红酒，下巴抬起，露出甜甜的娇笑，眼睛看着他的脸。"
   "画面里恰好两个人：基利安和玛丽。" + Z_END + Z_KM,
   "玛丽端着红酒，肩膀贴着基利安的手臂，甜笑着看着他，开口说话；基利安冷着脸。", "0—6秒侧面中景，镜头固定。",
   ('Mary', "She doesn't belong here, Killian.", 1.0),
   f"A steady side-on medium two-shot opens from the adopted first frame in {BR}: {KT} at frame-left in profile, his eyes cold and level on {MY}'s face; {MY} at frame-right pressed against his arm, one hand on his sleeve, a glass of red wine in her other hand, her eyes on his face. "
   "She speaks in a sugary, coy voice with a sweet smile. His face stays cold and his jaw stays set. The camera holds still.",
   "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是晚宴大厅：基利安在画面左边侧身站着，冷冷地平视着玛丽的脸；玛丽在画面右边贴着他的手臂，一只手搭在他的袖子上，另一只手端着红酒，眼睛看着他的脸。她用甜得发腻的、娇滴滴的声音说话，带着甜甜的笑。他的脸一直冷着，下颌一直紧绷。镜头固定不动。",
   voiced(*QUARTET))

# 03 玛丽挽臂（同一对人、同一地点、人数不变，承接前段）-------------------------------------------------------
TA(True, '03｜玛丽挽臂', 5, ['Mary', 'KillianTux'], ('ballroom', 'mary', 'killian_tux'), ['ballroom'],
   "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame. "
   "Killian at frame-left in the black tuxedo, in profile facing frame-right, his lips a flat line, his jaw tight, his eyes lowered to Mary's hand on his arm. "
   "Mary at frame-right in the white satin cocktail dress, in profile facing frame-left, her hand sliding into the crook of his right arm, a glass of red wine in her other hand, a smug sweet smile, her eyes on his face. "
   "The frame holds exactly two people: Killian and Mary.",
   END + LAY_KM,
   "侧面的中景双人镜头，两个人都是头到膝盖，在画面中间三分之一。基利安在画面左边，穿黑色无尾礼服，侧身朝画面右边，嘴唇抿成一条线，下颌紧绷，眼睛垂着看玛丽放在他胳膊上的手。"
   "玛丽在画面右边，穿白色缎面鸡尾酒裙，侧身朝画面左边，一只手正滑进他右臂的臂弯，另一只手端着一杯红酒，露出得意的甜笑，眼睛看着他的脸。"
   "画面里恰好两个人：基利安和玛丽。" + Z_END + Z_KM,
   "玛丽的手滑进基利安的臂弯，勾住他的胳膊，得意地笑着看他；基利安下颌紧绷，低头看着她的手。", "0—5秒侧面中景，镜头固定。", None,
   f"A steady side-on medium two-shot opens from the adopted first frame in {BR}: {KT} at frame-left in profile, his eyes lowered to {MY}'s hand on his arm; {MY} at frame-right, her hand hooked through the crook of his right arm, a glass of red wine in her other hand, her eyes on his face. "
   "She tightens her hold on his arm and tilts her head toward his shoulder with a smug sweet smile; his jaw clenches. Both stay where they are. The camera holds still.",
   "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是晚宴大厅：基利安在画面左边侧身站着，眼睛垂着看玛丽放在他胳膊上的手；玛丽在画面右边，一只手勾在他右臂的臂弯里，另一只手端着红酒，眼睛看着他的脸。她把他的胳膊勾得更紧，歪头朝他的肩膀靠过去，带着得意的甜笑；他的下颌咬紧。两人都留在原处。镜头固定不动。",
   silent(*QUARTET))

# 04 莉莉低头（单人；视线落在她自己交叠的手上——画面里的东西）--------------------------------------------------
TA(False, '04｜莉莉低头', 5, ['LilyRed'], ('ballroom', 'lily_red'), ['ballroom'],
   "Medium close-up of Lily alone, waist-up, in profile facing frame-right, in the middle third of the frame, in the red satin gown with the small beige bandage on the side of her neck, "
   "her hands clasped at her waist, her lower lip caught between her teeth, her brows drawn together, her eyes on her own clasped hands. The frame holds exactly one person, Lily.",
   END + LAY,
   "莉莉一个人的中近景，腰部以上，侧身朝画面右边，在画面中间三分之一，穿红色缎面晚礼服，脖子侧面贴着小小的米色创可贴，双手交握在腰前，下嘴唇被牙齿咬住，眉头皱起，眼睛看着自己交握的双手。画面里恰好一个人：莉莉。" + Z_END + Z_LAY,
   "莉莉咬着下嘴唇，皱着眉，低下头看着自己交握的双手。", "0—5秒莉莉侧面中近景，镜头固定。", None,
   f"A steady medium close-up opens from the adopted first frame in {BR}: {LR} in profile facing frame-right, her hands clasped at her waist, her eyes on her hands. "
   "She lowers her head, her lower lip caught between her teeth. Her hands stay clasped. The camera holds still.",
   "一个稳定的中近景，从已采用的开场图继续，场景是晚宴大厅：莉莉侧身朝画面右边，双手交握在腰前，眼睛看着自己的手。她低下头，下嘴唇被牙齿咬住。双手一直交握着。镜头固定不动。",
   silent(*QUARTET))

# 05 红酒泼裙（难动作：液体 + 手抓手腕）---------------------------------------------------------------------
TA(False, '05｜红酒泼裙', 6, ['Mary', 'KillianTux'], ('ballroom', 'mary', 'killian_tux'), ['ballroom'],
   "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame. "
   "Killian at frame-left in the black tuxedo, in profile facing frame-right, his right hand closed around Mary's right wrist at chest height, his face cold, his eyes level on her face. "
   "Mary at frame-right in the white satin cocktail dress, in profile facing frame-left, a crystal glass of red wine in her right hand, her mouth open in shock, her eyes wide, her eyes on his hand on her wrist. "
   "The frame holds exactly two people: Killian and Mary.",
   END + LAY_KM,
   "侧面的中景双人镜头，两个人都是头到膝盖，在画面中间三分之一。基利安在画面左边，穿黑色无尾礼服，侧身朝画面右边，右手在胸口的高度握住玛丽的右手腕，脸冷着，眼睛平视着她的脸。"
   "玛丽在画面右边，穿白色缎面鸡尾酒裙，侧身朝画面左边，右手端着一只盛着红酒的水晶杯，张着嘴，睁大眼睛，眼睛看着他抓在她手腕上的手。画面里恰好两个人：基利安和玛丽。" + Z_END + Z_KM,
   "基利安的右手一推玛丽的手腕，她杯里的红酒泼出来，洒在她自己白色的裙子前襟上；她张着嘴，睁大眼睛。", "0—6秒侧面中景，镜头固定。", None,
   f"A steady side-on medium two-shot opens from the adopted first frame in {BR}: {KT} at frame-left, his right hand closed around {MY}'s right wrist, his eyes level on her face; {MY} at frame-right, a glass of red wine in her right hand, her eyes on his hand. "
   "His right hand pushes her wrist toward her own chest; the glass tips and red wine splashes down the front of her white dress. His face stays cold and his jaw stays set. Her mouth hangs open and her eyes stay wide. The camera holds still.",
   "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是晚宴大厅：基利安在画面左边，右手握住玛丽的右手腕，眼睛平视着她的脸；玛丽在画面右边，右手端着一杯红酒，眼睛看着他的手。他的右手把她的手腕推向她自己的胸口；杯子倾倒，红酒泼洒下来，流过她白裙子的前襟。他的脸一直冷着，下颌一直紧绷。她的嘴一直张着，眼睛一直睁大。镜头固定不动。",
   silent("A crystal glass tipping, a splash of wine, and a few drops pattering on the marble floor.", "水晶杯倾倒，一声酒液泼洒，几滴酒落在大理石地面上的声音。"))

# 06 擦手（承接 05：同一对人、同一地点、人数不变）---------------------------------------------------------------
TA(True, '06｜擦手', 6, ['KillianTux', 'Mary'], ('ballroom', 'killian_tux', 'mary'), ['ballroom'],
   "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame. "
   "Killian at frame-left in the black tuxedo, in profile facing frame-right, a white silk handkerchief in his left hand wiping the fingers of his right hand, his lips a flat line, his eyes cold and level on Mary's face. "
   "Mary at frame-right in the white satin cocktail dress with a large red wine stain down the front, in profile facing frame-left, an empty glass hanging from her right hand at her side, her mouth open, her eyes wide on his face. "
   "The frame holds exactly two people: Killian and Mary.",
   END + LAY_KM,
   "侧面的中景双人镜头，两个人都是头到膝盖，在画面中间三分之一。基利安在画面左边，穿黑色无尾礼服，侧身朝画面右边，左手拿着一块白色丝帕擦着右手的手指，嘴唇抿成一条线，冷冷地平视着玛丽的脸。"
   "玛丽在画面右边，穿白色缎面鸡尾酒裙，前襟上一大片红酒渍，侧身朝画面左边，右手垂在身侧，指间挂着一只空杯，张着嘴，睁大眼睛看着他的脸。画面里恰好两个人：基利安和玛丽。" + Z_END + Z_KM,
   "基利安用白丝帕一根根擦着手指，冷冷地看着玛丽，开口说话；玛丽裙子上有一大片酒渍，呆住了。", "0—6秒侧面中景，镜头固定。",
   ('KillianTux', "Your perfume offends my wife.", 1.0),
   f"A steady side-on medium two-shot opens from the adopted first frame in {BR}: {KT} at frame-left wiping his right hand with the white silk handkerchief in his left hand, his eyes cold and level on {MY}'s face; {MY} at frame-right with the wine stain on her dress, an empty glass hanging from her hand, her eyes wide on his face. "
   "He speaks in a low, icy voice. His hands keep wiping. She stands frozen, her mouth open and her eyes wide. The camera holds still.",
   "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是晚宴大厅：基利安在画面左边，用左手的白丝帕擦着右手，冷冷地平视着玛丽的脸；玛丽在画面右边，裙子上有酒渍，指间挂着一只空杯，睁大眼睛看着他的脸。他用低沉冰冷的声音说话。他的手一直在擦。她僵在原地，张着嘴，睁大眼睛。镜头固定不动。",
   voiced(*QUARTET))

# 07 玛丽惨白（单人；视线落在她手里的空杯上——画面里的东西）-----------------------------------------------------
TA(False, '07｜玛丽惨白', 5, ['Mary'], ('ballroom', 'mary'), ['ballroom'],
   "Close-up of Mary alone, chest-up, in profile facing frame-left, in the middle third of the frame, in the white satin dress with a large red wine stain down the front, "
   "her face pale, her mouth open in shock, her eyes wide and glossy, her chin trembling, her eyes on the empty wine glass held at her chest. The frame holds exactly one person, Mary.",
   END + LAY,
   "玛丽一个人的近景，胸部以上，侧身朝画面左边，在画面中间三分之一，穿白色缎面裙，前襟上一大片红酒渍，脸色苍白，张着嘴，睁大湿润的眼睛，下巴发抖，眼睛看着胸前拿着的空酒杯。画面里恰好一个人：玛丽。" + Z_END + Z_LAY,
   "玛丽脸色惨白，张着嘴，下巴发抖，看着手里的空酒杯。", "0—5秒玛丽侧面近景，镜头固定。", None,
   f"A steady close-up opens from the adopted first frame in {BR}: {MY}'s face in profile facing frame-left, her mouth open, her eyes wide and glossy on the empty glass at her chest. "
   "Her lips tremble and her eyes stay wide on the glass. Her head stays where it is. The camera holds still.",
   "一个稳定的近景，从已采用的开场图继续，场景是晚宴大厅：玛丽侧脸朝画面左边，张着嘴，睁大湿润的眼睛看着胸前的空杯。她的嘴唇发抖，眼睛一直睁大盯着杯子。头留在原处。镜头固定不动。",
   silent(*QUARTET))

# 08 保罗大喊（单人；视线落在画面里的红地毯上；台词）-----------------------------------------------------------
TA(False, '08｜保罗大喊', 6, ['PaulOnScreen'], ('ballroom', 'paul'), ['ballroom'],
   "Medium shot of Paul alone, from the head to the waist, in profile facing frame-right, in the middle third of the frame, standing on the dark-red carpet in his navy blazer over a white open-collared shirt, "
   "a gold-trimmed column behind him at frame-left, his eyes wide, his brows pulled up, his mouth open, his eyes fixed down the length of the red carpet at frame-right. The frame holds exactly one person, Paul.",
   END + LAY,
   "保罗一个人的中景，头到腰，侧身朝画面右边，在画面中间三分之一，站在深红色的地毯上，穿藏青色西装外套和白色敞领衬衫，身后画面左边是一根镶金边的柱子，睁大眼睛，眉毛扬起，张着嘴，眼睛盯着画面右边那条红地毯的尽头。画面里恰好一个人：保罗。" + Z_END + Z_LAY,
   "保罗站在红地毯上，睁大眼睛，张着嘴，盯着红地毯的尽头，大喊出声。", "0—6秒保罗侧面中景，镜头固定。",
   ('PaulOnScreen', "Lily! What did he just say?!", 1.0),
   f"A steady medium shot opens from the adopted first frame in {BR}: {PL} on the red carpet in profile facing frame-right, his eyes wide and fixed down the length of the carpet at frame-right. "
   "He shouts in a cracking, outraged voice, his mouth wide open. His body stays where it is. The camera holds still.",
   "一个稳定的中景，从已采用的开场图继续，场景是晚宴大厅：保罗侧身朝画面右边站在红地毯上，睁大眼睛，盯着画面右边那条红地毯的尽头。他用破音的、愤怒的声音大喊，嘴张得很大。身体留在原处。镜头固定不动。",
   voiced(*QUARTET))

a.finish('第6集｜绿茶修罗场',
         '晚宴大厅里，穿红裙、脖子上贴着创可贴的莉莉站在基利安身边。保罗的妹妹玛丽端着红酒贴上来，说莉莉不属于这里，伸手挽住基利安的胳膊；莉莉咬着嘴唇低下头。基利安反手一推，玛丽杯里的红酒泼在她自己白色的裙子上，他用丝帕擦着手说“你的香水熏到我太太了”。玛丽脸色惨白。保罗正好走进大厅，听到“太太”两个字，震惊地大喊。',
         OUT_A)
segs_a = a.d['episodes'][0]['segments']

# =========================================================================================================
# B 对比测试（必须在 A 之后追加；实验，不进成片）
# =========================================================================================================
b = Batch(OUT_A + '.json', SERIES_TITLE, 3600)
ZH_B = []
TB = maker(b, ZH_B)

ROOM = '[[asset:room]]'; LILY = '[[asset:lily]]'; KIL = '[[asset:killian]]'; PAU = '[[asset:paul]]'
LAYR = " Fixed layout: the heavy dark-wood door is at frame-left; the rack of white gowns is at the back wall at frame-right."
Z_LAYR = "固定布局：厚重的深色木门在画面左边；白色婚纱架在后墙的画面右边。"
LAYR_C = " Fixed layout: the heavy dark-wood door is in the back wall just left of the center of the frame; the rack of white gowns is at the back wall at frame-right."
Z_LAYR_C = "固定布局：厚重的深色木门在后墙，稍微偏左于画面中央；白色婚纱架在后墙的画面右边。"
LAYR_LK = LAYR + " Lily is always at frame-left of Killian."
Z_LAYR_LK = Z_LAYR + "莉莉始终在基利安左边。"
END_R = " Warm light from the chandelier and the wall sconces."
Z_END_R = "吊灯和壁灯的暖光。"
HUSH = ("A faint, quiet room tone.", "淡淡的、安静的房间底噪。")


def pair(tag, who, chars, assets, img, img_zh, vid_a, vid_a_zh, expr, expr_zh):
    """一对：a 视频文字里没写表情；b 在同一处只多一句表情。同种子、同开场图文字。"""
    sa = TB(False, f'{tag}a｜表情对照{who}（无表情句）', 5, chars, assets, ['room'], img, END_R + LAYR, img_zh + Z_END_R + Z_LAYR,
            f'{who}站着，没有写任何表情。', "0—5秒，镜头固定。", None,
            vid_a, vid_a_zh, silent(*HUSH))
    sb = TB(False, f'{tag}b｜表情对照{who}（有表情句）', 5, chars, assets, ['room'], img, END_R + LAYR, img_zh + Z_END_R + Z_LAYR,
            f'{who}站着，写了明确的表情。', "0—5秒，镜头固定。", None,
            vid_a.replace(' She breathes', ' ' + expr + ' She breathes').replace(' He breathes', ' ' + expr + ' He breathes'),
            vid_a_zh.replace('她吸了一口气', expr_zh + '她吸了一口气').replace('他吸了一口气', expr_zh + '他吸了一口气'), silent(*HUSH))
    assert sa['shots'][0]['visual_en'] != sb['shots'][0]['visual_en'], tag
    sb['seed'] = sa['seed']


pair('S1', '莉莉', ['Lily'], ('room', 'lily'),
     "Medium close-up of Lily alone, waist-up, standing with her back against the cream wall, in the middle third of the frame, in the ivory silk wedding gown, both hands pressed flat against the wall behind her, her eyes on the closed heavy dark-wood door at frame-left. The frame holds exactly one person, Lily.",
     "莉莉一个人的中近景，腰部以上，背靠奶油色的墙站着，在画面中间三分之一，穿象牙色丝质婚纱，双手平按在身后的墙上，眼睛看着画面左边那扇关着的厚重深色木门。画面里恰好一个人：莉莉。",
     f"A steady medium close-up opens from the adopted first frame in {ROOM}: {LILY} stands with her back against the wall, both hands pressed flat on the wall behind her, her eyes on the door at frame-left. She breathes in once and her chest rises. Her body stays where it is. The camera holds still.",
     f"一个稳定的中近景，从已采用的开场图继续，场景是试衣间：莉莉背靠着墙站着，双手平按在身后的墙上，眼睛看着画面左边的门。她吸了一口气，胸口抬起。身体留在原处。镜头固定不动。",
     "Her lips are pressed tightly together and her brows are drawn together.", "她的嘴唇紧紧抿着，眉头皱着。")
pair('S2', '基利安', ['Killian'], ('room', 'killian'),
     "Close-up of Killian alone, chest-up, in profile facing frame-left, in the middle third of the frame, in the black three-piece suit and dark tie, his eyes on the closed heavy dark-wood door at frame-left. The frame holds exactly one person, Killian.",
     "基利安一个人的近景，胸部以上，侧身朝画面左边，在画面中间三分之一，穿黑色三件套西装、深色领带，眼睛看着画面左边那扇关着的厚重深色木门。画面里恰好一个人：基利安。",
     f"A steady close-up opens from the adopted first frame in {ROOM}: {KIL}'s face in profile facing frame-left, his eyes on the door at frame-left. He breathes in once and his chest rises. His head stays where it is. The camera holds still.",
     f"一个稳定的近景，从已采用的开场图继续，场景是试衣间：基利安侧脸朝画面左边，眼睛看着画面左边的门。他吸了一口气，胸口抬起。头留在原处。镜头固定不动。",
     "His lips are a flat line and his jaw is tight.", "他的嘴唇抿成一条线，下颌紧绷。")
pair('S3', '保罗', ['PaulOnScreen'], ('room', 'paul'),
     "Medium shot of Paul alone, from the head to the waist, in profile facing frame-right, in the middle third of the frame, in his navy blazer over a white open-collared shirt, his right hand resting on the brass lever handle of the heavy dark-wood door at frame-left, his eyes on the rack of white gowns at frame-right. The frame holds exactly one person, Paul.",
     "保罗一个人的中景，头到腰，侧身朝画面右边，在画面中间三分之一，穿藏青色西装外套和白色敞领衬衫，右手搭在画面左边那扇厚重深色木门的黄铜压杆把手上，眼睛看着画面右边那排白色婚纱。画面里恰好一个人：保罗。",
     f"A steady medium shot opens from the adopted first frame in {ROOM}: {PAU} stands in profile facing frame-right with his right hand on the door handle, his eyes on the rack of gowns at frame-right. He breathes in once and his shoulders rise. His body stays where it is. The camera holds still.",
     f"一个稳定的中景，从已采用的开场图继续，场景是试衣间：保罗侧身朝画面右边站着，右手搭在门把手上，眼睛看着画面右边那排婚纱。他吸了一口气，肩膀抬起。身体留在原处。镜头固定不动。",
     "His brows are drawn together and his lips are pressed together.", "他的眉头皱着，嘴唇抿着。")

# X1 退场1：人在门口、背对镜头，走出去并把门带上 ------------------------------------------------------------
TB(False, 'X1｜退场1：背对镜头走出去关门', 6, ['PaulOnScreen'], ('room', 'paul'), ['room'],
   "Medium shot from inside the fitting room, Paul alone, seen from behind, full body, in the middle third of the frame, standing in the open doorway set in the back wall just left of the center with his back to the camera, in his navy blazer, "
   "his right hand on the edge of the heavy dark-wood door, the dim corridor ahead of him; the rack of white gowns stands at the back wall at frame-right. The frame holds exactly one person, Paul.",
   END_R + LAYR_C,
   "从试衣间里拍的中景，保罗一个人，从背后看，全身，在画面中间三分之一，站在后墙稍偏左于中央的敞开门口，背对镜头，穿藏青色西装外套，右手扶着厚重深色木门的边缘，面前是昏暗的走廊；白色婚纱架在后墙的画面右边。画面里恰好一个人：保罗。" + Z_END_R + Z_LAYR_C,
   "保罗背对镜头站在门口，走出去，用右手把门在身后拉上。", "0—6秒背影中景，镜头固定。", None,
   f"A steady medium shot opens from the adopted first frame in {ROOM}: {PAU} seen from behind in the open doorway just left of center. "
   "He steps forward through the doorway, away from the camera, his right hand drawing the heavy dark-wood door closed behind him until it latches. The fitting room is left empty. The camera holds still.",
   "一个稳定的中景，从已采用的开场图继续，场景是试衣间：保罗在稍偏左于中央的敞开门口，从背后看。他向前迈过门口，走离镜头，右手把厚重的深色木门在身后拉上，直到锁舌扣上。试衣间里空了。镜头固定不动。",
   silent("The heavy door closing and the bolt clicking home.", "沉重的门关上，锁舌咔哒扣上的声音。"))

# X2 退场2：人在门外的走廊里，从外面把门拉上 ---------------------------------------------------------------
TB(False, 'X2｜退场2：人在门外把门拉上', 6, ['PaulOnScreen'], ('room', 'paul'), ['room'],
   "Medium shot from inside the fitting room: through the open doorway set in the back wall just left of the center, Paul alone stands in the middle third of the frame in the dim corridor on the far side of the threshold, facing into the room, in his navy blazer, "
   "his right hand on the outer handle of the heavy dark-wood door, his lips pressed together, his eyes on the rack of white gowns at the back wall at frame-right. The frame holds exactly one person, Paul.",
   END_R + LAYR_C,
   "从试衣间里拍的中景：透过后墙稍偏左于中央的敞开门口，保罗一个人在画面中间三分之一，站在门槛外昏暗的走廊里，面朝房间里，穿藏青色西装外套，右手握着厚重深色木门外侧的把手，嘴唇抿紧，眼睛看着后墙画面右边那排白色婚纱。画面里恰好一个人：保罗。" + Z_END_R + Z_LAYR_C,
   "保罗站在门外的走廊里，把门朝自己拉上，门关严，他被门挡住。", "0—6秒中景，镜头固定。", None,
   f"A steady medium shot opens from the adopted first frame in {ROOM}: {PAU} stands in the corridor outside the open doorway just left of center, his right hand on the outer door handle, his jaw set. "
   "He pulls the heavy dark-wood door closed toward himself; it swings across the doorway and latches, hiding him. The camera holds still.",
   "一个稳定的中景，从已采用的开场图继续，场景是试衣间：保罗站在稍偏左于中央的敞开门外的走廊里，右手握着门外侧的把手，下颌紧绷。他把厚重的深色木门朝自己拉上；门摆过门口，锁舌扣上，把他挡住。镜头固定不动。",
   silent("The heavy door closing and the bolt clicking home.", "沉重的门关上，锁舌咔哒扣上的声音。"))

# X3 背景人群：远处有几个客人，会不会多出前景的人 ------------------------------------------------------------
TB(False, 'X3｜背景远处有客人', 6, ['LilyRed', 'KillianTux'], ('ballroom', 'lily_red', 'killian_tux'), ['ballroom'],
   "Wide side-on two-shot, both people full body, in the middle third of the frame, standing side by side in profile facing frame-right: Lily at frame-left in the red satin gown, her lips pressed together, her eyes on the long banquet table; "
   "Killian at frame-right in the black tuxedo, his jaw set, his eyes on the long banquet table. A few guests in formal wear stand far away at the banquet table, small and out of focus. The frame holds exactly two people in the foreground: Lily and Killian.",
   END + LAY_LK,
   "宽景的侧面双人镜头，两个人都是全身，在画面中间三分之一，并肩侧身朝画面右边站着：莉莉在画面左边，穿红色缎面晚礼服，嘴唇抿紧，眼睛看着那张长长的宴会桌；基利安在画面右边，穿黑色无尾礼服，下颌紧绷，眼睛看着那张长长的宴会桌。宴会桌旁很远的地方站着几个穿正装的客人，很小，焦点不在他们身上。画面前景里恰好两个人：莉莉和基利安。" + Z_END + Z_LK,
   "莉莉和基利安并肩站着，远处宴会桌旁有几个小小的客人。", "0—6秒宽景侧面双人镜头，镜头固定。", None,
   f"A steady wide side-on two-shot opens from the adopted first frame in {BR}: {LR} at frame-left and {KT} at frame-right, both in profile facing frame-right, their eyes on the banquet table, the few far-off guests at the table. "
   "Lily's lips press tighter; Killian's jaw tightens. The guests stay small and far away. The camera holds still.",
   "一个稳定的宽景侧面双人镜头，从已采用的开场图继续，场景是晚宴大厅：莉莉在画面左边，基利安在画面右边，两人都侧身朝画面右边，眼睛看着宴会桌，桌边是远处的几个客人。莉莉的嘴唇抿得更紧；基利安的下颌收紧。客人一直又小又远。镜头固定不动。",
   silent(*QUARTET))

# R1 第 3 集 13/14 号的补拍候选：两人都入画，代替“画外的人” ---------------------------------------------------
TB(False, 'R1｜结尾补拍候选：两人入画', 6, ['Lily', 'Killian'], ('room', 'lily', 'killian'), ['room'],
   "Side-on medium two-shot in the fitting room, both people in the middle third of the frame. Lily at frame-left sits on the carpet with her back against the cream wall, a document folder held against her chest, her eyes lifted to Killian's face, her eyes glistening, her lips pressed tightly together. "
   "Killian at frame-right stands over her in the black three-piece suit, looking down at her, his chin lowered, his eyes narrowed, his jaw set, warm chandelier light catching his eyes. The frame holds exactly two people: Lily and Killian.",
   END_R + LAYR_LK,
   "试衣间里侧面的中景双人镜头，两个人都在画面中间三分之一。莉莉在画面左边，背靠奶油色的墙坐在地毯上，文件夹抱在胸前，眼睛抬起看着基利安的脸，眼里含着泪光，嘴唇紧紧抿着。基利安在画面右边，穿黑色三件套西装，站在她上方低头看着她，下巴压低，眯着眼睛，下颌紧绷，吊灯的暖光落在他的眼里。画面里恰好两个人：莉莉和基利安。" + Z_END_R + Z_LAYR_LK,
   "莉莉坐在地上抬头看着基利安，含着泪，抿紧嘴唇；基利安站着，低头盯着她，眼里有冷光。", "0—6秒侧面中景，莉莉在左、基利安在右，镜头固定。", None,
   f"A steady side-on medium two-shot opens from the adopted first frame in {ROOM}: {LILY} seated at frame-left with the folder against her chest, her eyes lifted to his face; {KIL} standing at frame-right looking down at her. "
   "The chandelier light glints in his narrowed eyes; her eyes shine with tears and her chest rises once. Both stay where they are. The camera holds still.",
   "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是试衣间：莉莉坐在画面左边，文件夹抱在胸前，眼睛抬起看着他的脸；基利安站在画面右边，低头看着她。吊灯的光在他眯起的眼里闪动；她的眼里泛着泪光，胸口起伏了一下。两人都留在原处。镜头固定不动。",
   silent(*HUSH))

b.finish('第6集B｜对比测试',
         '实验，不进成片：三组“有没有写表情”的对照（莉莉、基利安、保罗），两种“人离开并关门”的站位，一个宴会厅背景远处有客人的画面，以及第 3 集结尾（13/14 号）的补拍候选。',
         OUT_B)
segs_b = b.d['episodes'][0]['segments']

# =========================================================================================================
# 说明
# =========================================================================================================
def fmt_table(segs):
    rows = ["| 号 | 名字 | 秒 | 在场 | 承接 | 英语台词 | 种子 |", "|---|---|---|---|---|---|---|"]
    for s in segs:
        dl = f"{s['dialogue'][0]['speaker']}：{s['dialogue'][0]['text']}" if s['dialogue'] else '（无台词）'
        rows.append(f"| {s['title'].split('｜')[0]} | {s['title'].split('｜')[1]} | {s['duration_seconds']} | {len(s['characters'])} | {'是' if s['depends_on_previous'] else '否'} | {dl} | {s['seed']} |")
    return '\n'.join(rows)


def fmt_prompts(segs, zh):
    out = []
    for i, s in enumerate(segs):
        out.append(f"### {s['title'].split('｜')[0]}｜{s['title'].split('｜')[1]}（{s['duration_seconds']} 秒）")
        out.append(f"- **开场图：** {zh[i]}")
        out.append(f"- **视频：** {s['shots'][0]['visual_zh']}")
        out.append(f"- **声音：** {s['sound_zh']}")
        if s['dialogue']:
            out.append(f"- **台词（单独传给插件）：** {s['dialogue'][0]['speaker']}：“{s['dialogue'][0]['text']}”")
        out.append("")
    return '\n'.join(out)


total_a = sum(s['duration_seconds'] for s in segs_a)
total_b = sum(s['duration_seconds'] for s in segs_b)
md = []
md.append("# 第 6 集（英语台词、追加批次）：怎么用（2026-10-09 晚）\n")
md.append(f"两份文件，**先跑 A，A 全部跑完再追加 B**（追加必须等上一份跑完）：\n\n- **A 正式版**：`{OUT_A}_全选复制粘贴.txt`，{len(segs_a)} 个任务，合计 {total_a} 秒，种子 3501–3508。接在第 5 集之后追加。\n- **B 对比测试**：`{OUT_B}_全选复制粘贴.txt`，{len(segs_b)} 个任务，合计 {total_b} 秒，种子 3601–3610。**实验，不进成片**（R1、X1、X2 同时是第 3 集 13/14、07 号的补拍候选，你觉得好就换上去）。\n")
md.append(f"设置照旧：视频/对白共用次数 = 1，对白时间余量 = 0。追加窗口不要勾“每集／总／任务秒数”。**{len(segs_a)+len(segs_b)} 个任务按每个约 7 分钟估算要 {(len(segs_a)+len(segs_b))*7//60} 小时 {(len(segs_a)+len(segs_b))*7%60} 分钟（7 分钟是上限推算，不是实测——你告诉我机器实际一个任务几分钟，我再调。）**\n")
md.append("## 一、做完能得到什么（每个任务想测什么、怎么算成功、失败说明什么）\n")
md.append("A 的总体目的：把第 3 集分析出的新规矩用在一整集上，看“按规矩写”的合格率。具体：每个人物每个任务都写了表情（预期没有不想要的笑）；没有“画外的人”（预期没有陌生人冒出来）；有台词的任务都是 6 秒、≤6 个单词（看台词是否念完）；承接前段只用在同一对人同一地点的 03、06。\n")
md.append("| 号 | 想测什么 | 算成功 | 失败说明什么 |\n|---|---|---|---|")
md.append("| A01 | 两人都入画；视线目标是画面里的宴会桌；两人都写了表情 | 没有笑、没有多出的人 | 如果还笑：“写了表情也会笑”，规律 3 要改 |")
md.append("| A02 | 玛丽的“甜笑”是想要的表情，明确写了；肩贴手臂的近身双人；台词 | 玛丽笑、基利安冷脸不笑；台词念完；每只手有主人 | 基利安也跟着笑：笑会“传染”给同画面的人 |")
md.append("| A03（承接 02） | 承接前段：同一对人、同一地点、人数不变 | 站位、姿势接上 02（第 3 集同类 5/5） | 接不上：承接前段的适用范围要收窄 |")
md.append("| A04 | 单人、视线落在自己交握的手上 | 莉莉不笑，没有陌生人 | 单人没有画外目标也冒人：规律 3 的“画外”解释不够 |")
md.append("| A05 | 难动作：红酒泼洒 + 手抓手腕 | 酒泼在玛丽自己的裙子上 | 酒不泼/泼歪：H3 不擅长液体，以后用剪辑代替 |")
md.append("| A06（承接 05） | 同一对人、同一地点；台词 | 接得上；台词念完 | 同 A03 |")
md.append("| A07 | 单人换人（不承接）；视线落在自己手里的空杯 | 不笑，没有陌生人 | 同 A04 |")
md.append("| A08 | 单人；视线落在画面里的红地毯上；台词 | 台词念完，没有陌生人 | 同 A04 |\n")
md.append("B 是对照实验：")
md.append("| 号 | 想测什么 | 怎么看 | 结论 |\n|---|---|---|---|")
md.append("| S1a/b、S2a/b、S3a/b | **同种子、同开场图文字，只差视频文字里有没有写表情**（莉莉、基利安、保罗各一对） | 看每个 a 笑不笑、对应的 b 笑不笑；注意看**最后两秒**（第 3 集 13 号是前 3 秒平静、后面才笑起来的） | a 三个都笑、b 三个都不笑：“没写表情就默认笑”确认，规律 3 的这一半从“中”升到“强”；a 不笑：这一半降级，第 3 集的笑另有原因 |")
md.append("| X1 | 人离开并关门，站位 1：人在门口、**背对镜头**走出去 | 看人是不是真的走出画面、门是不是在他身后关上、房间是不是空了 | 成功：H20 的“背对镜头”写法可用，07 号可以换成它 |")
md.append("| X2 | 人离开并关门，站位 2：人**在门外走廊**，从外面把门拉上 | 看他是不是留在门外、门是不是关严 | 成功：H20 的“把人放在门外一侧”写法可用；X1 X2 都失败：H3 做不了“离场”，以后用“下一个任务里这个人不在”来表现 |")
md.append("| X3 | 背景远处有几个客人，会不会多出前景的人（以后宴会、马场用得上） | 数前景有几个人、远处客人有没有走到前景 | 前景多人：以后别在提示词里写背景人群 |")
md.append("| R1 | **用“两人入画”代替“画外的人”**：莉莉坐在地上抬头、基利安站着低头看她，两人都写了表情 | 莉莉是不是不笑、基利安的眼神是不是冷、有没有陌生人 | 成功：H19 的“让对方入画”可以进规律；还能直接替换第 3 集 13/14 号 |\n")
md.append("## 二、A 的 8 个任务\n")
md.append(fmt_table(segs_a))
md.append("\n## 三、B 的 10 个任务\n")
md.append(fmt_table(segs_b))
md.append("\n## 四、给 H3 的提示词（中文全译，一个字不漏）\n")
md.append("每个任务的视频提示词前面还会加这句固定的风格话：**“真人实拍，电影感，写实，皮肤有自然质感，浅景深，温暖奢华的光线，超宽 8:3 宽银幕画面。”** 开场图提示词前面也有一段固定的开头：**“一张来自写实真人浪漫惊悚片的完整首帧，超宽 8:3 宽银幕构图。皮肤自然，能看到毛孔，布料和材质真实。固定的场景参考图决定地点，人物肖像只决定被点名的人。”** 下面不再重复。\n")
md.append("### A 正式版\n")
md.append(fmt_prompts(segs_a, ZH_A))
md.append("### B 对比测试\n")
md.append("S1a/S1b、S2a/S2b、S3a/S3b 每一对的开场图提示词完全相同，视频提示词只差一句表情（b 里多的那句）。**开场图每次会重新生成，a 和 b 的开场图不会一模一样：先看每张开场图的脸，如果开场图本身就在笑，这一对不算数，请在号码后写“开场图就笑”；开场图是平静的，才看视频里笑不笑。**（开场图提示词里故意没写表情，好让“没写表情”真的没写。）\n")
md.append(fmt_prompts(segs_b, ZH_B))
md.append("## 五、我预计会出问题的地方（没试过，只是判断）\n")
md.append("- **A05 红酒泼裙**：液体加手抓手腕，可能酒不泼、杯子穿手，或泼到别处。\n- **A02、A03 玛丽贴近基利安**：近身双人，可能手臂穿插；玛丽的笑可能“传染”给基利安。\n- **A08 保罗大喊**：喊叫时嘴型和台词能不能对上（第 3 集 6/7 句对得上）。\n- **玛丽是新人物（没有参考图）**，A02 以后每个任务里她的脸是否一致要看。\n- **B 的 X1、X2** 是第 3 集 07 号失败后的两种新写法，可能仍然失败，这本身是有用的结论。\n- **台词**照旧：声音常常到片尾才结束，验收时听结尾（A02、A06、A08）。\n")
md.append("## 六、和第 3 集的区别（已按“Claude 易错点自查清单”）\n")
md.append("- 每个人物每个任务都写了表情；没有“画外的人”，视线目标都在画面里。\n- 有台词的任务都是 6 秒、≤6 个单词；没有 5 秒任务放台词。\n- 承接前段只在同一对人、同一地点、人数不变的 03、06；人数一变（A04、A05、A07、A08）就关掉。\n- 没有“人走出画面”的动作；离场写法放进 B 的 X1、X2 单独测。\n")
open(os.path.join(FOLDER, '第06集/第06集_说明.md'), 'w', encoding='utf-8').write('\n'.join(md))
print('说明已写')
