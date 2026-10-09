#!/usr/bin/env python3
"""剧本第 7–10 集（马场四集）制作稿 + 第 10 集 B“大动作实验”（2026-10-10）。

链式生成（每一份以前一份的 JSON 为底，style／素材／角色逐字复制，再追加新东西）：
  补拍包 → 第 7 集（种子 3801–3809）→ 第 8 集（3901–3908）→ 第 9 集（4001–4008）→ 第 10 集（4101–4107）→ 第 10 集 B（4201–4204，实验，放最后）
新增：场景 ranch、woods_edge；人物 killian_coat、lily_riding、mary_riding、trainer、bodyguard；动物（role=prop）black_horse；
角色 KillianCoat、LilyRiding、MaryRiding、Trainer、Bodyguard。

按“Claude 易错点自查清单”写：每个人物每个任务都写表情；没有画外目标；有台词的任务都是 6 秒、≤6 个单词；
承接前段只在同一批人、同一地点、同一景别的相邻任务（每集第一个任务一律关）；没有“人走出画面”；最多 2 人（只有 B 的 T3 故意违反）。
合并和说明由本脚本末尾完成。
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, silent, voiced

BASE = '2026-10-09_补拍包_接缝补镜头_追加.json'
O7 = '2026-10-10_第7集_制作稿_英文台词_追加'
O8 = '2026-10-10_第8集_制作稿_英文台词_追加'
O9 = '2026-10-10_第9集_制作稿_英文台词_追加'
O10 = '2026-10-10_第10集_制作稿_英文台词_追加'
O10B = '2026-10-10_第10集B_大动作实验'
OMERGE = '2026-10-10_第7-10集+10B_合并_制作稿_追加'
SERIES_TITLE = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))['title']


def maker(batch, zh):
    def T(flag, title, dur, chars, assets, refs, img, end, img_zh, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound):
        s = batch.task(title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound)
        s['depends_on_previous'] = flag
        zh.append(img_zh)
        return s
    return T


RN = '[[asset:ranch]]'; WE = '[[asset:woods_edge]]'; KC = '[[asset:killian_coat]]'; LR = '[[asset:lily_riding]]'
MR = '[[asset:mary_riding]]'; TR = '[[asset:trainer]]'; HS = '[[asset:black_horse]]'; PL = '[[asset:paul]]'; BG = '[[asset:bodyguard]]'

LAY_RN = " Fixed stage layout: the raised wooden grandstand is at frame-left; the white fence and the green field are at frame-right; dark pine trees line the far edge."
Z_RN = "固定布局：凸起的木制看台在画面左边；白色围栏和绿色跑马场在画面右边；远处边缘是一排深色松树。"
END_RN = " Bright midday sunlight, a clear blue sky, the ranch softly blurred behind."
Z_END_RN = "明亮的正午阳光，晴朗的蓝天，跑马场在后面柔和虚化。"
LAY_WE = " Fixed stage layout: the open meadow with a dirt path is at frame-left; the rough wooden fence with sharp pointed posts and the dark pine forest are at frame-right."
Z_WE = "固定布局：开阔的草地和一条土路在画面左边；带尖桩的粗木栅栏和深色松林在画面右边。"
LAY_RIDE = LAY_WE + " Killian always sits behind Lily, at frame-left of her."
Z_RIDE = Z_WE + "基利安始终坐在莉莉身后，在她的画面左边。"
END_WE = " Bright afternoon sunlight, a clear blue sky, the meadow softly blurred behind."
Z_END_WE = "明亮的午后阳光，晴朗的蓝天，草地在后面柔和虚化。"
RANCH_SND = ("A light breeze, distant birdsong and the creak of leather.", "轻轻的风声、远处的鸟叫，和皮革马具轻轻的吱嘎声。")
GALLOP = ("Fast, pounding hoofbeats on dry earth and the creak of leather.", "急促沉重的马蹄声踏在干土上，和皮革马具的吱嘎声。")
WALK = ("Slow, steady hoofbeats on dirt and the creak of leather.", "缓慢平稳的马蹄声踏在泥土上，和皮革马具的吱嘎声。")
BREEZE = ("A light breeze over the meadow and the creak of leather.", "草地上轻轻的风声，和皮革马具的吱嘎声。")

# =========================================================================================================
# 第 7 集 致命危机（场景：私人跑马场）
# =========================================================================================================
a = Batch(BASE, SERIES_TITLE, 3800)
ZH7 = []
T7 = maker(a, ZH7)

a.scene('ranch', '私人跑马场',
        "A private equestrian ranch on a bright sunny day: a raised wooden grandstand with a roof and a railing on the left, a long white wooden fence and a wide green riding field on the right, a packed-earth track in front, dark pine trees along the far edge, a clear blue sky. The reference fixes the layout and decor.",
        "晴朗明亮的一天里的私人马术跑马场：左边是带屋顶和栏杆的凸起木制看台，右边是长长的白色木栅栏和开阔的绿色跑马场，前面是一条夯实的泥土跑道，远处边缘是深色的松树，晴朗的蓝天。参考图固定布局与陈设。",
        "A photorealistic ultra-wide 8:3 cinemascope shot of a private equestrian ranch on a bright sunny day: a raised wooden grandstand with a roof and a railing on the left, a long white wooden fence and a wide green riding field on the right, a packed-earth track in front, dark pine trees along the far edge, a clear blue sky with a few white clouds. "
        "The frame holds the grandstand, the white fence, the green field and the pine trees.")
a.person('killian_coat', '基利安（炭灰长大衣）',
         "Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short swept-back black hair, a sharp jawline, light stubble and cold dark-gray eyes, wearing a long charcoal-gray wool overcoat over a black shirt, black trousers and black leather riding boots. The portrait fixes his identity and clothes, not staging.",
         "基利安，和参考图是同一个三十出头、身材极高、肩膀宽阔的成年男性，黑色短发向后梳，下颌线锋利，有浅胡茬，眼睛是冷冷的深灰色，穿长款炭灰色羊毛大衣，里面是黑衬衫，配黑色长裤和黑色皮质马靴。人物图固定身份和衣服，不固定站位。",
         "A photorealistic half-body portrait of the same man as in the reference image, short swept-back black hair, sharp jawline, light stubble, cold dark-gray eyes, wearing a long charcoal-gray wool overcoat over a black shirt. "
         "He faces the camera with a cold, composed expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.",
         ref='killian')
a.person('lily_riding', '莉莉（马术装）',
         "Lily, the same adult woman in her mid-twenties as in the reference, with long wavy chestnut-brown hair tied back in a low ponytail, fair skin and large hazel-green eyes, wearing a fitted cream blouse, tan riding breeches, tall brown leather riding boots and a thin brown belt. The portrait fixes her identity and clothes, not staging.",
         "莉莉，和参考图是同一个二十五岁左右的成年女性，栗棕色长卷发在脑后扎成低马尾，白皙皮肤、浅褐绿色大眼睛，穿合身的奶油色衬衫、棕黄色马裤、高筒棕色皮质马靴，系一条细棕色皮带。人物图固定身份和衣服，不固定站位。",
         "A photorealistic half-body portrait of the same woman as in the reference image, long wavy chestnut-brown hair tied back in a low ponytail, wearing a fitted cream blouse and a thin brown belt. "
         "She faces the camera with a composed, slightly nervous expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.",
         ref='lily')
a.person('mary_riding', '玛丽（马术装）',
         "Mary, the same adult woman in her mid-twenties as in the reference, with sleek honey-blonde hair in a tight low bun, flawless makeup, glossy red lips and sharp green eyes, wearing a fitted ivory riding jacket over a white blouse, white riding breeches, tall black leather riding boots and small pearl earrings. The portrait fixes her identity and clothes, not staging.",
         "玛丽，和参考图是同一个二十五岁左右的成年女性，光滑的蜜金色头发在脑后盘成紧实的低髻，妆容无瑕，嘴唇红亮，一双锐利的绿眼睛，穿合身的象牙色马术外套、里面是白衬衫，配白色马裤、高筒黑色皮质马靴，戴小小的珍珠耳环。人物图固定身份和衣服，不固定站位。",
         "A photorealistic half-body portrait of the same woman as in the reference image, sleek honey-blonde hair in a tight low bun, glossy red lips, sharp green eyes, wearing a fitted ivory riding jacket over a white blouse and small pearl earrings. "
         "She faces the camera with a sweet, coy expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.",
         ref='mary')
a.person('trainer', '驯马师',
         "Trainer, a stocky adult man in his late forties with a tanned, lined face, short gray-brown stubble and small shrewd eyes, wearing a worn brown leather vest over a rolled-sleeve plaid shirt, dark jeans, leather work boots and a flat tweed cap. The portrait fixes his identity and clothes, not staging.",
         "驯马师，一个四十多岁、敦实的成年男性，晒得黝黑、满是皱纹的脸，短短的灰褐色胡茬，精明的小眼睛，穿磨旧的棕色皮背心、里面是卷起袖子的格子衬衫，配深色牛仔裤、皮质工作靴和一顶平顶花呢帽。人物图固定身份和衣服，不固定站位。",
         "A photorealistic half-body portrait of a stocky adult man in his late forties with a tanned, lined face, short gray-brown stubble and small shrewd eyes, wearing a worn brown leather vest over a rolled-sleeve plaid shirt and a flat tweed cap. "
         "He faces the camera with a flat, guarded expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.")
a.prop('black_horse', '纯黑烈马',
       "A tall, powerfully built jet-black stallion with a glossy coat, a thick black mane, wide flared nostrils and a wild white-ringed eye, wearing a plain brown leather bridle with brown reins and a plain brown leather English saddle with stirrups. The portrait fixes the horse's coat, build and tack, not staging.",
       "一匹高大、强壮的纯黑种马，皮毛油亮，鬃毛浓密，鼻孔宽大张开，眼睛带一圈白、透着野性，戴着朴素的棕色皮质笼头和棕色缰绳，背上是朴素的棕色皮质英式马鞍和马镫。人物图固定马的毛色、体型和马具，不固定站位。",
       "A photorealistic full-body side-profile photograph of a tall, powerfully built jet-black stallion with a glossy coat, a thick black mane, wide flared nostrils and a wild white-ringed eye, wearing a plain brown leather bridle with brown reins and a plain brown leather English saddle with stirrups, standing on bare ground. "
       "Soft even studio light, plain neutral gray background, natural coat texture, four legs clearly visible.")
v = a.d['characters']['LilyRed']['voice_description']
a.character('LilyRiding', 'lily_riding', v['en'], v['zh'])
v = a.d['characters']['KillianTux']['voice_description']
a.character('KillianCoat', 'killian_coat', v['en'], v['zh'])
v = a.d['characters']['Mary']['voice_description']
a.character('MaryRiding', 'mary_riding', v['en'], v['zh'])
a.character('Trainer', 'trainer',
            "A middle-aged adult male voice, gravelly and flat with a rural American drawl, a little nervous, speaking clear American English at ordinary conversational volume. Every word is fully voiced and audible.",
            "中年成年男声，沙哑平淡，带乡村美式拖腔，有一点紧张，说清楚的美式英语，正常交谈音量。每个字都正常发声、清晰可辨。")

# 7-01 看台上的基利安 ------------------------------------------------------------------------------------------
T7(False, '01｜看台上打电话', 5, ['KillianCoat'], ('ranch', 'killian_coat'), ['ranch'],
   "Medium shot of Killian alone, from the head to the waist, in profile facing frame-right, in the middle third of the frame, standing at the railing of the raised wooden grandstand in the long charcoal overcoat over a black shirt, "
   "a gold smartphone held to his right ear with his right hand, his left hand resting on the railing, his lips pressed into a flat line, his jaw set, his eyes on the green riding field at frame-right. The frame holds exactly one person, Killian.",
   END_RN + LAY_RN,
   "基利安一个人的中景，头到腰，侧身朝画面右边，在画面中间三分之一，站在凸起的木制看台的栏杆边，穿长款炭灰色呢大衣、里面是黑衬衫，右手把一部金色手机举在右耳边，左手搭在栏杆上，嘴唇抿成一条线，下颌紧绷，眼睛看着画面右边那片绿色的跑马场。画面里恰好一个人：基利安。" + Z_END_RN + Z_RN,
   "基利安站在看台栏杆边，用金色手机听一个重要的电话，神情冷淡。", "0—5秒侧面中景，镜头固定。", None,
   f"A steady medium shot opens from the adopted first frame in {RN}: {KC} in profile facing frame-right at the grandstand railing, the gold smartphone at his right ear, his eyes on the green field at frame-right. He listens to the call, his jaw tight and his lips pressed into a flat line. His body stays where it is. The camera holds still.",
   "一个稳定的中景，从已采用的开场图继续，场景是私人跑马场：基利安侧身朝画面右边站在看台栏杆边，金色手机贴在右耳，眼睛看着画面右边的绿色跑马场。他听着电话，下颌紧绷，嘴唇抿成一条线。身体留在原处。镜头固定不动。",
   silent("A light breeze, distant birdsong and the faint clink of tack from the field.", "轻轻的风声、远处的鸟叫，和跑马场那边马具隐约的叮当声。"))

# 7-02 玛丽买通驯马师（玛丽自己说出“买通”这件事）-------------------------------------------------------------
T7(False, '02｜玛丽买通驯马师', 6, ['MaryRiding', 'Trainer'], ('ranch', 'mary_riding', 'trainer'), ['ranch'],
   "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, standing close on the packed-earth track and facing each other in profile. "
   "Mary at frame-left in the ivory riding jacket and white riding breeches, facing frame-right, a thick brown envelope held out in her right hand at chest height, her chin tilted up, a sweet coy smile, her eyes on Trainer's face. "
   "Trainer at frame-right in the worn brown leather vest and flat tweed cap, facing frame-left, his left hand taking the envelope, his lips pressed together, his brows drawn together, his eyes lowered to the envelope. The frame holds exactly two people: Mary and Trainer.",
   END_RN + LAY_RN,
   "侧面的中景双人镜头，两个人都是头到膝盖，在画面中间三分之一，近近地站在夯实的泥土跑道上，侧身面对面。玛丽在画面左边，穿象牙色马术外套和白色马裤，侧身朝画面右边，右手在胸口的高度递出一个厚厚的棕色信封，下巴抬起，露出甜甜的娇笑，眼睛看着驯马师的脸。"
   "驯马师在画面右边，穿磨旧的棕色皮背心，戴平顶花呢帽，侧身朝画面左边，左手正接过信封，嘴唇抿紧，眉头皱着，眼睛垂着看着信封。画面里恰好两个人：玛丽和驯马师。" + Z_END_RN + Z_RN,
   "玛丽把一个厚厚的信封递给驯马师，甜甜地笑着低声吩咐；驯马师低头看着信封，伸手接过。", "0—6秒侧面中景，镜头固定。",
   ('MaryRiding', "Give her the wildest one.", 1.0),
   f"A steady side-on medium two-shot opens from the adopted first frame in {RN}: {MR} at frame-left holding out the thick envelope in her right hand, {TR} at frame-right taking it with his left hand. She speaks in a sugary, coy voice with a sweet smile, her eyes on his face. His eyes stay on the envelope, his brows drawn together and his lips pressed. The camera holds still.",
   "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是私人跑马场：玛丽在画面左边递出手里的厚信封，驯马师在画面右边用左手接过。她用甜得发腻的、娇滴滴的声音说话，带着甜甜的笑，眼睛看着他的脸。他的眼睛一直盯着信封，眉头皱着，嘴唇抿紧。镜头固定不动。",
   voiced("A light breeze and distant birdsong.", "轻轻的风声和远处的鸟叫。"))

# 7-03 驯马师牵马到莉莉面前 -------------------------------------------------------------------------------------
T7(False, '03｜驯马师牵马过来', 6, ['Trainer', 'LilyRiding'], ('ranch', 'trainer', 'lily_riding', 'black_horse'), ['ranch'],
   "Side-on wide shot, the people from the head to the knees and the whole horse in view, in the middle third of the frame, on the packed-earth track. "
   "The tall jet-black horse stands at frame-left in profile facing frame-right, its head tossing, its ears pinned back, its nostrils flared. "
   "Trainer stands at the center beside the horse's head in the worn brown leather vest and flat tweed cap, in profile facing frame-right, his right hand holding the horse's bridle at the cheek, his lips flat, his eyes on Lily's face. "
   "Lily stands at frame-right in the cream blouse and tan riding breeches with tall brown boots, in profile facing frame-left, her hands clasped at her waist, her lips parted, her brows drawn together, her eyes wide on the horse's head. The frame holds exactly two people, Trainer and Lily, and one black horse.",
   END_RN + LAY_RN,
   "侧面的宽景镜头，人物是头到膝盖、整匹马都在画面里，在画面中间三分之一，在夯实的泥土跑道上。高大的纯黑烈马站在画面左边，侧身朝画面右边，头不停甩动，耳朵向后压平，鼻孔张大。"
   "驯马师站在画面中央、马头旁边，穿磨旧的棕色皮背心，戴平顶花呢帽，侧身朝画面右边，右手握着马脸颊旁的笼头，嘴唇平直，眼睛看着莉莉的脸。"
   "莉莉站在画面右边，穿奶油色衬衫、棕黄色马裤和高筒棕靴，侧身朝画面左边，双手交握在腰前，嘴唇微张，眉头皱着，睁大眼睛看着马头。画面里恰好两个人和一匹黑马：驯马师和莉莉。" + Z_END_RN + Z_RN,
   "驯马师牵着一匹躁动的黑马来到莉莉面前，开口说话；莉莉睁大眼睛看着马头，有些害怕。", "0—6秒侧面宽景，镜头固定。",
   ('Trainer', "This one's for you, Miss.", 1.0),
   f"A steady side-on wide shot opens from the adopted first frame in {RN}: {HS} at frame-left in profile facing frame-right, {TR} beside its head holding the bridle in his right hand, {LR} at frame-right facing him. Trainer speaks in a flat, gravelly voice, his lips barely moving and his eyes on Lily's face. Lily's eyes stay wide on the horse's head and her lips stay parted. The horse tosses its head and its tail swishes. The camera holds still.",
   "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是私人跑马场：黑马在画面左边，侧身朝画面右边；驯马师在马头旁边，右手握着笼头；莉莉在画面右边面对他。驯马师用平淡沙哑的声音说话，嘴唇几乎不动，眼睛看着莉莉的脸。莉莉的眼睛一直睁大看着马头，嘴唇一直微张。马甩着头，尾巴来回扫动。镜头固定不动。",
   voiced("A light breeze, the creak of leather and a horse stamping its hoof.", "轻轻的风声、皮革马具的吱嘎声，和马蹄跺地的声音。"))

# 7-04 莉莉已经坐在马上（踩马镫、跨上去的动作不拍，直接给结果）-----------------------------------------------------
T7(False, '04｜莉莉坐在马背上', 5, ['LilyRiding', 'Trainer'], ('ranch', 'lily_riding', 'trainer', 'black_horse'), ['ranch'],
   "Side-on wide shot, in the middle third of the frame, on the packed-earth track. The tall jet-black horse stands in profile facing frame-right. "
   "Lily sits in the saddle on its back in profile facing frame-right, in the cream blouse and tan riding breeches, both hands gripping the reins at the horse's neck, her back straight, her lower lip caught between her teeth, her brows drawn together, her eyes wide on the horse's ears. "
   "Trainer stands at frame-right of the horse's head in profile facing frame-left, in the brown leather vest and flat tweed cap, his right hand on the bridle at the horse's cheek, his lips flat, his eyes on the bridle. The frame holds exactly two people, Lily and Trainer, and one black horse.",
   END_RN + LAY_RN,
   "侧面的宽景镜头，在画面中间三分之一，在夯实的泥土跑道上。高大的纯黑烈马站着，侧身朝画面右边。"
   "莉莉坐在马背的马鞍上，侧身朝画面右边，穿奶油色衬衫和棕黄色马裤，双手握着马脖子上的缰绳，背挺直，下嘴唇被牙齿咬住，眉头皱着，睁大眼睛看着马的耳朵。"
   "驯马师站在马头的画面右边，侧身朝画面左边，穿棕色皮背心，戴平顶花呢帽，右手按在马脸颊旁的笼头上，嘴唇平直，眼睛看着笼头。画面里恰好两个人和一匹黑马：莉莉和驯马师。" + Z_END_RN + Z_RN,
   "莉莉已经坐在马背上，双手紧握缰绳，咬着下嘴唇，害怕地看着马耳朵；驯马师扶着笼头。", "0—5秒侧面宽景，镜头固定。", None,
   f"A steady side-on wide shot opens from the adopted first frame in {RN}: {LR} sits in the saddle of {HS} in profile facing frame-right, both hands tight on the reins, her eyes on the horse's ears; {TR} at the horse's head holds the bridle in his right hand, his eyes on the bridle. Her lower lip trembles and her brows draw together. His lips stay flat. The horse shifts its weight and its ears twitch. The camera holds still.",
   "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是私人跑马场：莉莉侧身朝画面右边坐在黑马的马鞍上，双手紧握缰绳，眼睛看着马的耳朵；驯马师在马头旁，右手握着笼头，眼睛看着笼头。她的下嘴唇发抖，眉头皱紧。他的嘴唇一直平直。马挪动着重心，耳朵抽动。镜头固定不动。",
   silent("A light breeze, the creak of leather and a horse stamping its hoof.", "轻轻的风声、皮革马具的吱嘎声，和马蹄跺地的声音。"))

# 7-05 玛丽扎针（明着拍：手按在马屁股上）-------------------------------------------------------------------------
T7(False, '05｜玛丽扎马屁股', 6, ['MaryRiding', 'LilyRiding'], ('ranch', 'mary_riding', 'lily_riding', 'black_horse'), ['ranch'],
   "Side-on wide shot, in the middle third of the frame, on the packed-earth track. The tall jet-black horse stands in profile facing frame-right. "
   "Lily sits in the saddle on its back in profile facing frame-right, both hands gripping the reins, her lips pressed tight, her brows drawn together, her eyes wide on the horse's ears. "
   "Mary stands at frame-left beside the horse's hindquarters in profile facing frame-right, in the ivory riding jacket and white riding breeches, her right hand holding a thin silver needle against the horse's rump, her chin tilted up, a sweet coy smile, her eyes on Lily's back. The frame holds exactly two people, Lily and Mary, and one black horse.",
   END_RN + LAY_RN,
   "侧面的宽景镜头，在画面中间三分之一，在夯实的泥土跑道上。高大的纯黑烈马站着，侧身朝画面右边。"
   "莉莉坐在马背的马鞍上，侧身朝画面右边，双手握紧缰绳，嘴唇紧紧抿着，眉头皱着，睁大眼睛看着马的耳朵。"
   "玛丽站在画面左边、马的臀部旁边，侧身朝画面右边，穿象牙色马术外套和白色马裤，右手拿着一根细细的银针抵在马屁股上，下巴抬起，露出甜甜的娇笑，眼睛看着莉莉的背。画面里恰好两个人和一匹黑马：莉莉和玛丽。" + Z_END_RN + Z_RN,
   "玛丽甜笑着，把一根细银针按进黑马的屁股；马的耳朵猛地向后压，尾巴甩起；莉莉坐在马上抓紧缰绳。", "0—6秒侧面宽景，镜头固定。", None,
   f"A steady side-on wide shot opens from the adopted first frame in {RN}: {MR} at frame-left presses the thin silver needle into the rump of {HS} with her right hand, a sweet coy smile on her lips and her eyes on Lily's back; {LR} in the saddle grips the reins, her eyes on the horse's ears and her lips pressed tight. The horse's ears snap back and its tail whips up. The camera holds still.",
   "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是私人跑马场：玛丽在画面左边，右手把细银针按进黑马的屁股，嘴角挂着甜甜的娇笑，眼睛看着莉莉的背；莉莉坐在马鞍上握紧缰绳，眼睛看着马的耳朵，嘴唇紧紧抿着。马的耳朵猛地向后压，尾巴甩起。镜头固定不动。",
   silent("A sharp stamp of hooves and the creak of leather.", "马蹄猛地一跺的声音，和皮革马具的吱嘎声。"))

# 7-06 马人立 + 呼救 ---------------------------------------------------------------------------------------------
T7(False, '06｜马人立而起', 6, ['LilyRiding'], ('ranch', 'lily_riding', 'black_horse'), ['ranch'],
   "Side-on wide shot, in the middle third of the frame, on the packed-earth track. The tall jet-black horse is in profile facing frame-right, rearing up on its hind legs with its front hooves raised high. "
   "Lily on its back is leaning forward with both arms wrapped around the horse's neck, in the cream blouse and tan riding breeches, her mouth wide open in a scream, her eyes squeezed shut, her brows pulled up. The frame holds exactly one person, Lily, and one black horse.",
   END_RN + LAY_RN,
   "侧面的宽景镜头，在画面中间三分之一，在夯实的泥土跑道上。高大的纯黑烈马侧身朝画面右边，后腿站立、前蹄高高扬起。莉莉在马背上身体前倾，双臂紧紧抱住马脖子，穿奶油色衬衫和棕黄色马裤，嘴巴大张在尖叫，眼睛紧闭，眉毛高高扬起。画面里恰好一个人和一匹黑马：莉莉。" + Z_END_RN + Z_RN,
   "黑马后腿站起、前蹄扬起；莉莉抱紧马脖子，大声呼救。", "0—6秒侧面宽景，镜头固定。",
   ('LilyRiding', "Help! Somebody help me!", 1.0),
   f"A steady side-on wide shot opens from the adopted first frame in {RN}: {HS} rears on its hind legs with {LR} clinging to its neck, her arms tight around it. She screams for help in a high, cracking voice, her mouth wide open and her eyes squeezed shut. The camera holds still.",
   "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是私人跑马场：黑马后腿站起，莉莉紧紧抱着它的脖子。她用尖利、破音的声音呼救，嘴巴大张，眼睛紧闭。镜头固定不动。",
   voiced("Hooves scraping the dirt and the creak of leather.", "马蹄刨着泥土的声音，和皮革马具的吱嘎声。"))

# 7-07 狂奔（朝着右边的松树）-------------------------------------------------------------------------------------
T7(False, '07｜黑马狂奔', 5, ['LilyRiding'], ('ranch', 'lily_riding', 'black_horse'), ['ranch'],
   "Side-on wide shot, in the middle third of the frame, on the green riding field. The tall jet-black horse is in profile facing frame-right in a full gallop, all four hooves off the ground, dust rising behind it. "
   "Lily on its back is low over its neck, in the cream blouse and tan riding breeches, both hands tangled in the black mane, her face pale, her lips pressed tight, her eyes squeezed shut. The dark pine trees line the far edge at frame-right. The frame holds exactly one person, Lily, and one black horse.",
   END_RN + LAY_RN,
   "侧面的宽景镜头，在画面中间三分之一，在绿色的跑马场上。高大的纯黑烈马侧身朝画面右边全速飞奔，四蹄腾空，身后扬起灰尘。莉莉伏在马脖子上，穿奶油色衬衫和棕黄色马裤，双手缠在黑色的鬃毛里，脸色苍白，嘴唇紧紧抿着，眼睛紧闭。画面右边远处的边缘是一排深色松树。画面里恰好一个人和一匹黑马：莉莉。" + Z_END_RN + Z_RN,
   "黑马载着伏在马脖子上的莉莉，朝着右边的松树狂奔。", "0—5秒侧面宽景，镜头固定。", None,
   f"A steady side-on wide shot opens from the adopted first frame in {RN}: {HS} gallops across the green field toward the dark pine trees at frame-right with {LR} low over its neck, her hands tangled in the mane, her face pale and her lips pressed tight. The horse keeps galloping. The camera holds still.",
   "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是私人跑马场：黑马载着伏在脖子上的莉莉，朝着画面右边的深色松树奔过绿色的跑马场，她的双手缠在鬃毛里，脸色苍白，嘴唇紧紧抿着。马一直在奔跑。镜头固定不动。",
   silent(*GALLOP))

# 7-08 基利安猛抬头 --------------------------------------------------------------------------------------------
T7(False, '08｜基利安猛抬头', 5, ['KillianCoat'], ('ranch', 'killian_coat'), ['ranch'],
   "Medium close-up of Killian alone, from the head to the waist, in profile facing frame-right, in the middle third of the frame, at the railing of the raised wooden grandstand in the long charcoal overcoat over a black shirt, "
   "the gold smartphone held at his right ear, his lips relaxed and slightly parted, his jaw loose, his eyes lowered on the railing. The frame holds exactly one person, Killian.",
   END_RN + LAY_RN,
   "基利安一个人的中近景，头到腰，侧身朝画面右边，在画面中间三分之一，在凸起的木制看台的栏杆边，穿长款炭灰色呢大衣、里面是黑衬衫，金色手机举在右耳边，嘴唇放松、微微张开，下颌松弛，眼睛垂着看着栏杆。画面里恰好一个人：基利安。" + Z_END_RN + Z_RN,
   "基利安听着电话，突然猛地抬头，盯向右边的松树，眉头拧紧。", "0—5秒侧面中近景，镜头固定。", None,
   f"A steady medium close-up opens from the adopted first frame in {RN}: {KC} in profile facing frame-right at the grandstand railing, the gold smartphone at his right ear, his eyes on the railing. His head snaps up and his eyes fix on the dark pine trees at frame-right, his brows snapping together and his jaw tightening. The phone stays at his ear. His body stays where it is. The camera holds still.",
   "一个稳定的中近景，从已采用的开场图继续，场景是私人跑马场：基利安侧身朝画面右边站在看台栏杆边，金色手机贴在右耳，眼睛看着栏杆。他猛地抬头，眼睛盯住画面右边的深色松树，眉头猛地拧紧，下颌收紧。手机一直贴在耳边。身体留在原处。镜头固定不动。",
   silent("A light breeze and distant birdsong.", "轻轻的风声和远处的鸟叫。"))

# 7-09 捏碎手机（承接 08：同一个人、同一地点、同一景别）---------------------------------------------------------------
T7(True, '09｜捏碎手机', 5, ['KillianCoat'], ('ranch', 'killian_coat'), ['ranch'],
   "Medium close-up of Killian alone, from the head to the waist, in profile facing frame-right, in the middle third of the frame, at the railing of the raised wooden grandstand in the long charcoal overcoat over a black shirt, "
   "his right fist raised at chest height, closed around the gold smartphone, the gold casing bent and cracked in his grip, his jaw clenched hard, his lips pulled back from his teeth, his eyes narrowed with a dark-gold glint on the dark pine trees at frame-right. The frame holds exactly one person, Killian.",
   END_RN + LAY_RN,
   "基利安一个人的中近景，头到腰，侧身朝画面右边，在画面中间三分之一，在凸起的木制看台的栏杆边，穿长款炭灰色呢大衣、里面是黑衬衫，右拳举在胸口的高度，攥着那部金色手机，金色的外壳在他手里弯折开裂，下颌咬得死紧，嘴唇向后拉开露出牙齿，眯着眼睛，眼里闪着暗金色的光，盯着画面右边的深色松树。画面里恰好一个人：基利安。" + Z_END_RN + Z_RN,
   "基利安盯着松树，右拳攥紧，金色手机在他手里被捏得变形开裂。", "0—5秒侧面中近景，镜头固定。", None,
   f"A steady medium close-up opens from the adopted first frame in {RN}: {KC} in profile facing frame-right, his right fist closed around the gold smartphone at chest height, his eyes on the dark pine trees at frame-right. His fist tightens and the gold casing bends and cracks in his grip, his jaw clenching hard and his eyes narrowing with a dark-gold glint. His body stays where it is. The camera holds still.",
   "一个稳定的中近景，从已采用的开场图继续，场景是私人跑马场：基利安侧身朝画面右边，右拳在胸口的高度攥着金色手机，眼睛盯着画面右边的深色松树。他的拳头收紧，金色的外壳在他手里弯折开裂，下颌咬紧，眯起的眼里闪着暗金色的光。身体留在原处。镜头固定不动。",
   silent("A sharp crack of bending metal and glass.", "金属和玻璃弯折碎裂的一声脆响。"))

a.finish('第7集｜致命危机',
         '几天后的马术聚会。基利安在看台上接重要的电话。玛丽为报复晚宴，把一个厚信封塞给驯马师，要他给莉莉最烈的马。驯马师牵来一匹纯黑烈马，莉莉害怕，还是被迫骑了上去；玛丽暗中把针扎进马屁股，黑马人立而起，载着尖叫呼救的莉莉冲向松林。远处的基利安听到尖叫，猛地抬头，把金色手机捏变了形。',
         O7)

# =========================================================================================================
# 第 8 集 极致共骑（场景：树林边缘）
# =========================================================================================================
b = Batch(O7 + '.json', SERIES_TITLE, 3900)
ZH8 = []
T8 = maker(b, ZH8)
b.scene('woods_edge', '树林边缘的草地',
        "The edge of a pine forest beside a wide sunlit meadow: tall green grass with a dirt path on the left, a rough wooden fence with sharp pointed posts on the right, a dense wall of dark pine trees behind the fence, a clear blue sky. The reference fixes the layout and decor.",
        "阳光下的开阔草地旁边的松林边缘：左边是高高的绿草和一条土路，右边是带尖桩的粗木栅栏，栅栏后面是一整排密密的深色松树，晴朗的蓝天。参考图固定布局与陈设。",
        "A photorealistic ultra-wide 8:3 cinemascope shot of the edge of a pine forest beside a wide sunlit meadow: tall green grass and a dirt path on the left, a rough wooden fence with sharp pointed posts on the right, a dense wall of dark pine trees behind the fence, a clear blue sky with a few white clouds. "
        "The frame holds the meadow, the path, the fence and the pine forest.")

# 8-01 莉莉在狂奔的马上快被甩下来 -----------------------------------------------------------------------------------
T8(False, '01｜莉莉快被甩下马', 5, ['LilyRiding'], ('woods_edge', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on wide shot, in the middle third of the frame, on the dirt path along the meadow. The tall jet-black horse is in profile facing frame-right in a full gallop, all four hooves off the ground, grass and dust flying. "
   "Lily on its back is bouncing hard in the saddle, her body slipping sideways, in the cream blouse and tan riding breeches, one hand gripping the black mane and the other hand loose in the air, her face pale, her mouth open, her eyes wide on the sharp fence posts at frame-right. The frame holds exactly one person, Lily, and one black horse.",
   END_WE + LAY_WE,
   "侧面的宽景镜头，在画面中间三分之一，在草地边的土路上。高大的纯黑烈马侧身朝画面右边全速飞奔，四蹄腾空，草屑和灰尘飞扬。莉莉在马背上被颠得上下弹动，身体向一侧滑落，穿奶油色衬衫和棕黄色马裤，一只手抓着黑色鬃毛，另一只手在空中松开，脸色苍白，张着嘴，睁大眼睛看着画面右边带尖桩的栅栏。画面里恰好一个人和一匹黑马：莉莉。" + Z_END_WE + Z_WE,
   "黑马载着莉莉朝尖桩栅栏狂奔，她被颠得身体歪向一侧，快要摔下来。", "0—5秒侧面宽景，镜头固定。", None,
   f"A steady side-on wide shot opens from the adopted first frame in {WE}: {HS} gallops along the dirt path toward the sharp fence posts at frame-right with {LR} bouncing hard in the saddle, one hand gripping the black mane and her body slipping sideways, her mouth open and her eyes wide on the fence posts. The camera holds still.",
   "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是树林边缘的草地：黑马沿土路朝画面右边带尖桩的栅栏狂奔，莉莉在马鞍上被颠得上下弹动，一只手抓着黑色鬃毛，身体向一侧滑落，张着嘴，睁大眼睛看着栅栏的尖桩。镜头固定不动。",
   silent("Fast, pounding hoofbeats and the creak of leather.", "急促沉重的马蹄声，和皮革马具的吱嘎声。"))

# 8-02 基利安已在她身后（腾空跃上马背的动作不拍，直接给结果）-----------------------------------------------------------
T8(False, '02｜基利安已在她身后', 5, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on wide-medium shot, both riders from the head to the waist and the whole horse, in the middle third of the frame, on the dirt path along the meadow. The tall jet-black horse is in profile facing frame-right, galloping. "
   "Killian sits in the saddle behind Lily, at frame-left of her, in the long charcoal overcoat flaring behind him, his left hand holding the reins at the horse's neck, his right arm wrapped around her waist, his jaw set, his lips pressed together, his eyes on the sharp fence posts at frame-right. "
   "Lily sits in front of him, at frame-right, her back against his chest, both hands gripping the black mane, her mouth open, her eyes wide. The frame holds exactly two people, Killian and Lily, and one black horse.",
   END_WE + LAY_RIDE,
   "侧面的宽中景镜头，两个骑手都是头到腰、整匹马都在画面里，在画面中间三分之一，在草地边的土路上。高大的纯黑烈马侧身朝画面右边飞奔。"
   "基利安坐在莉莉身后的马鞍上，在她的画面左边，穿长款炭灰色呢大衣，大衣在身后飘起，左手握着马脖子上的缰绳，右臂环住她的腰，下颌紧绷，嘴唇抿紧，眼睛看着画面右边带尖桩的栅栏。"
   "莉莉坐在他前面，在画面右边，背靠着他的胸口，双手抓着黑色鬃毛，张着嘴，睁大眼睛。画面里恰好两个人和一匹黑马：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "基利安已经坐在莉莉身后，左手拉缰绳，右臂紧紧环住她的腰，两人一起骑着飞奔的黑马。", "0—5秒侧面宽中景，镜头固定。", None,
   f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {KC} sits behind {LR} on {HS}, his left hand on the reins and his right arm tight around her waist, his jaw set and his eyes on the sharp fence posts at frame-right. She presses back against his chest, her hands in the mane, her mouth open and her eyes wide. The horse gallops on. The camera holds still.",
   "一个稳定的侧面宽中景镜头，从已采用的开场图继续，场景是树林边缘的草地：基利安坐在黑马上、莉莉的身后，左手拉着缰绳，右臂紧紧环住她的腰，下颌紧绷，眼睛看着画面右边带尖桩的栅栏。她向后靠在他的胸口，双手抓着鬃毛，张着嘴，睁大眼睛。马继续飞奔。镜头固定不动。",
   silent(*GALLOP))

# 8-03 勒缰绳，马人立（承接 02：同两个人、同一匹马、同一地点、同一景别）-----------------------------------------------------
T8(True, '03｜勒缰绳马人立', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on wide-medium shot, both riders from the head to the waist and the whole horse, in the middle third of the frame, on the dirt path along the meadow. The tall jet-black horse is in profile facing frame-right, rearing on its hind legs with its front hooves raised and its head pulled up. "
   "Killian sits behind Lily, at frame-left of her, in the long charcoal overcoat, leaning back, his left hand pulling the reins hard, his right arm wrapped around her waist, his jaw clenched, his teeth set, his eyes on the horse's head. "
   "Lily sits in front of him, at frame-right, her back against his chest, both hands gripping the black mane, her eyes squeezed shut, her lips pressed tight. The frame holds exactly two people, Killian and Lily, and one black horse.",
   END_WE + LAY_RIDE,
   "侧面的宽中景镜头，两个骑手都是头到腰、整匹马都在画面里，在画面中间三分之一，在草地边的土路上。高大的纯黑烈马侧身朝画面右边，后腿站立、前蹄扬起、头被拉高。"
   "基利安坐在莉莉身后，在她的画面左边，穿长款炭灰色呢大衣，身体后仰，左手用力拉缰绳，右臂环住她的腰，下颌咬紧，牙关紧闭，眼睛看着马头。"
   "莉莉坐在他前面，在画面右边，背靠着他的胸口，双手抓着黑色鬃毛，眼睛紧闭，嘴唇紧紧抿着。画面里恰好两个人和一匹黑马：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "基利安身体后仰，左手猛拉缰绳，黑马后腿站起、前蹄扬起；莉莉紧闭双眼靠在他胸口。", "0—6秒侧面宽中景，镜头固定。", None,
   f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {HS} rears on its hind legs as {KC} leans back and pulls the reins hard with his left hand, his right arm tight around {LR}'s waist, his jaw clenched and his eyes on the horse's head. She presses back against his chest, her eyes squeezed shut and her lips pressed tight. The camera holds still.",
   "一个稳定的侧面宽中景镜头，从已采用的开场图继续，场景是树林边缘的草地：黑马后腿站起，基利安身体后仰，左手用力拉缰绳，右臂紧紧环着莉莉的腰，下颌咬紧，眼睛看着马头。她向后靠在他的胸口，眼睛紧闭，嘴唇紧紧抿着。镜头固定不动。",
   silent("Hooves scraping the dirt and the creak of leather.", "马蹄刨着泥土的声音，和皮革马具的吱嘎声。"))

# 8-04 紧贴（近景）-------------------------------------------------------------------------------------------------
T8(False, '04｜紧贴在耳边', 5, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, both in profile facing frame-right on the horse's back, the horse's black neck and ears at frame-right. "
   "Lily at frame-right, her back against Killian's chest, her eyes half closed, her lips parted, her brows drawn together. "
   "Killian directly behind her at frame-left in the long charcoal overcoat, his right arm around her waist, his lips close to her ear, his jaw tight, his eyes narrowed on the horse's ears at frame-right. The frame holds exactly two people: Killian and Lily.",
   END_WE + LAY_RIDE,
   "侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，都在马背上侧身朝画面右边，画面右边是黑马的脖子和耳朵。"
   "莉莉在画面右边，背靠着基利安的胸口，眼睛半闭，嘴唇微张，眉头皱着。"
   "基利安紧挨在她身后，在画面左边，穿长款炭灰色呢大衣，右臂环着她的腰，嘴唇贴近她的耳朵，下颌紧绷，眯着眼睛看着画面右边的马耳朵。画面里恰好两个人：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "基利安把莉莉紧紧搂在胸前，嘴唇凑在她的耳边；她半闭着眼睛，微微发抖。", "0—5秒侧面中近景，镜头固定。", None,
   f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} at frame-left holds {LR} against his chest with his right arm and leans his head close to her ear, his jaw tight and his eyes on the horse's ears at frame-right. She shivers, her eyes half closed and her lips parted. Both stay on the horse. The camera holds still.",
   "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘的草地：基利安在画面左边，右臂把莉莉搂在胸前，头凑近她的耳边，下颌紧绷，眼睛看着画面右边的马耳朵。她微微发抖，眼睛半闭，嘴唇微张。两人都留在马上。镜头固定不动。",
   silent("Slow, heavy hoofbeats on dry earth and the creak of leather.", "缓慢沉重的马蹄声踏在干土上，和皮革马具的吱嘎声。"))

# 8-05 马被逼停，莉莉瘫软发抖 ----------------------------------------------------------------------------------------
T8(False, '05｜马被逼停', 5, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on wide-medium shot, both riders from the head to the waist and the whole horse, in the middle third of the frame, on the dirt path along the meadow. The tall jet-black horse stands in profile facing frame-right, tossing its head, its flanks heaving. "
   "Killian sits behind Lily, at frame-left of her, in the long charcoal overcoat, his left hand holding the reins short, his right arm around her waist, his jaw tight, his lips pressed together, his eyes lowered on her face. "
   "Lily sits in front of him, at frame-right, slumped back against his chest, her shoulders shaking, her eyes half closed, her lips parted and trembling. The frame holds exactly two people, Killian and Lily, and one black horse.",
   END_WE + LAY_RIDE,
   "侧面的宽中景镜头，两个骑手都是头到腰、整匹马都在画面里，在画面中间三分之一，在草地边的土路上。高大的纯黑烈马站着，侧身朝画面右边，甩着头，两肋起伏。"
   "基利安坐在莉莉身后，在她的画面左边，穿长款炭灰色呢大衣，左手把缰绳勒短，右臂环着她的腰，下颌紧绷，嘴唇抿紧，眼睛垂着看着她的脸。"
   "莉莉坐在他前面，在画面右边，瘫软地向后靠在他胸口，肩膀发抖，眼睛半闭，嘴唇微张、不停发颤。画面里恰好两个人和一匹黑马：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "黑马被勒停，喘着粗气甩头；莉莉瘫软地靠在基利安怀里发抖，他低头看着她的脸。", "0—5秒侧面宽中景，镜头固定。", None,
   f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {HS} stands still, tossing its head, as {KC} holds the reins short in his left hand with his right arm around {LR}, his eyes lowered on her face and his jaw tight. She sags against his chest, trembling, her eyes half closed and her lips quivering. The camera holds still.",
   "一个稳定的侧面宽中景镜头，从已采用的开场图继续，场景是树林边缘的草地：黑马站定，不停甩头；基利安左手把缰绳勒短，右臂环着莉莉，眼睛垂着看着她的脸，下颌紧绷。她瘫软地靠在他胸口发抖，眼睛半闭，嘴唇颤动。镜头固定不动。",
   silent("Slow hoofbeats settling on dry earth and the creak of leather.", "缓慢的马蹄声渐渐落定在干土上，和皮革马具的吱嘎声。"))

# 8-06 台词（承接 05）----------------------------------------------------------------------------------------------
T8(True, '06｜如果我晚来一秒', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on wide-medium shot, both riders from the head to the waist and the whole horse, in the middle third of the frame, on the dirt path along the meadow. The tall jet-black horse stands in profile facing frame-right. "
   "Killian sits behind Lily, at frame-left of her, in the long charcoal overcoat, his left hand holding the reins short, his right arm around her waist, his jaw tight, his lips set, his eyes on her face. "
   "Lily sits in front of him, at frame-right, slumped back against his chest, her lips parted and trembling, her eyes half closed and lowered on his hand at her waist. The frame holds exactly two people, Killian and Lily, and one black horse.",
   END_WE + LAY_RIDE,
   "侧面的宽中景镜头，两个骑手都是头到腰、整匹马都在画面里，在画面中间三分之一，在草地边的土路上。高大的纯黑烈马站着，侧身朝画面右边。"
   "基利安坐在莉莉身后，在她的画面左边，穿长款炭灰色呢大衣，左手把缰绳勒短，右臂环着她的腰，下颌紧绷，嘴唇紧闭，眼睛看着她的脸。"
   "莉莉坐在他前面，在画面右边，瘫软地向后靠在他胸口，嘴唇微张、不停发颤，眼睛半闭，垂着看着他放在她腰上的手。画面里恰好两个人和一匹黑马：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "基利安用沙哑凶狠的声音质问莉莉；她瘫软地靠在他胸口，嘴唇发颤。", "0—6秒侧面宽中景，镜头固定。",
   ('KillianCoat', "One second later, you'd be dead.", 1.0),
   f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {KC} speaks in a low, hoarse, savage voice, his eyes on {LR}'s face and his jaw tight. She stays slumped against his chest, her lips quivering and her eyes lowered on his hand at her waist. The horse stands still. The camera holds still.",
   "一个稳定的侧面宽中景镜头，从已采用的开场图继续，场景是树林边缘的草地：基利安用低沉、沙哑、凶狠的声音说话，眼睛看着莉莉的脸，下颌紧绷。她一直瘫软地靠在他胸口，嘴唇颤动，眼睛垂着看着他放在她腰上的手。马站着不动。镜头固定不动。",
   voiced(*BREEZE))

# 8-07 捏住下巴（景别从宽中景变成中近景，所以不承接前段；08 再承接 07）----------------------------------------------------------
T8(False, '07｜捏住下巴扳过脸', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the horse's back, the horse's black neck at frame-right. "
   "Killian at frame-left in profile facing frame-right in the long charcoal overcoat, his right hand holding Lily's chin, his jaw tight, his lips set, his eyes on her lips. "
   "Lily at frame-right, her body facing frame-right and her face turned back toward him in profile facing frame-left, her chin held in his hand, her eyes wide on his eyes, her lips parted. Their faces are a hand's width apart. The frame holds exactly two people: Killian and Lily.",
   END_WE + LAY_RIDE,
   "侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，在马背上，画面右边是黑马的脖子。"
   "基利安在画面左边，侧身朝画面右边，穿长款炭灰色呢大衣，右手捏着莉莉的下巴，下颌紧绷，嘴唇紧闭，眼睛看着她的嘴唇。"
   "莉莉在画面右边，身体朝画面右边，脸向后转向他、侧脸朝画面左边，下巴被他的手捏着，睁大眼睛看着他的眼睛，嘴唇微张。两张脸相距一个手掌宽。画面里恰好两个人：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "基利安捏住莉莉的下巴，把她的脸扳向自己，眼睛盯着她的嘴唇；她睁大眼睛看着他。", "0—6秒侧面中近景，镜头固定。", None,
   f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC}'s right hand holds {LR}'s chin and draws her face closer to his, his eyes on her lips and his jaw tight. Her eyes go wide on his eyes and her lips part. Both stay on the horse. The camera holds still.",
   "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘的草地：基利安的右手捏着莉莉的下巴，把她的脸拉近自己的脸，眼睛看着她的嘴唇，下颌紧绷。她睁大眼睛看着他的眼睛，嘴唇微张。两人都留在马上。镜头固定不动。",
   silent(*BREEZE))

# 8-08 吻（承接 07）------------------------------------------------------------------------------------------------
T8(True, '08｜吻', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the horse's back against a clear blue sky. "
   "Killian at frame-left in profile facing frame-right in the long charcoal overcoat, his lips pressed hard against Lily's lips, his right hand firm on her jaw, his eyes closed, his brows drawn together. "
   "Lily at frame-right, her face turned back toward him in profile facing frame-left, her eyes wide open, her left hand on his forearm. The frame holds exactly two people: Killian and Lily.",
   END_WE + LAY_RIDE,
   "侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，在马背上，背后是晴朗的蓝天。"
   "基利安在画面左边，侧身朝画面右边，穿长款炭灰色呢大衣，嘴唇用力压在莉莉的嘴唇上，右手稳稳扣住她的下颌，闭着眼睛，眉头皱着。"
   "莉莉在画面右边，脸向后转向他、侧脸朝画面左边，眼睛睁得大大的，左手搭在他的前臂上。画面里恰好两个人：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "基利安用力吻住莉莉；她睁大眼睛，左手无力地推着他的前臂。", "0—6秒侧面中近景，镜头固定。", None,
   f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} presses his lips hard against {LR}'s lips, his right hand firm on her jaw and his eyes closed. Her eyes stay wide open and her left hand pushes weakly against his forearm. Both stay on the horse. The camera holds still.",
   "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘的草地：基利安把嘴唇用力压在莉莉的嘴唇上，右手稳稳扣住她的下颌，闭着眼睛。她的眼睛一直睁得大大的，左手无力地推着他的前臂。两人都留在马上。镜头固定不动。",
   silent(*BREEZE))

b.finish('第8集｜极致共骑',
         '黑马在树林边缘狂奔，莉莉被颠得快要摔向尖桩栅栏。基利安已经坐到她身后，一手勒缰绳，一臂把她紧紧箍在怀里；黑马人立而起又被他强行勒停。莉莉瘫软发抖，他沙哑地说“晚一秒你就死了”，捏住她的下巴把她的脸扳过来，重重吻了下去。',
         O8)

# =========================================================================================================
# 第 9 集 马背上的惩罚（场景：树林边缘）
# =========================================================================================================
c = Batch(O8 + '.json', SERIES_TITLE, 4000)
ZH9 = []
T9 = maker(c, ZH9)

# 9-01 吻结束（紧接上集：每集第一个任务关承接，开场图文字写成上集结尾的姿势）---------------------------------------------------
T9(False, '01｜吻结束', 5, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the horse's back against a clear blue sky. "
   "Killian at frame-left in profile facing frame-right in the long charcoal overcoat, his face a hand's width from hers, his jaw tight, his lips set, his eyes on her lips. "
   "Lily at frame-right, her face turned back toward him in profile facing frame-left, her lips red and swollen, her mouth open, her eyes wide and glossy, her right palm flat against his chest. The frame holds exactly two people: Killian and Lily.",
   END_WE + LAY_RIDE,
   "侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，在马背上，背后是晴朗的蓝天。"
   "基利安在画面左边，侧身朝画面右边，穿长款炭灰色呢大衣，脸离她的脸一个手掌宽，下颌紧绷，嘴唇紧闭，眼睛看着她的嘴唇。"
   "莉莉在画面右边，脸向后转向他、侧脸朝画面左边，嘴唇红肿，嘴微张，眼睛睁大、湿润发亮，右手掌平按在他的胸口。画面里恰好两个人：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "吻结束了，基利安把脸抬开一个手掌宽，盯着她红肿的嘴唇；莉莉的手无力地抵在他胸口。", "0—5秒侧面中近景，镜头固定。", None,
   f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} lifts his face away from {LR}'s until it is a hand's width from hers, his eyes on her lips and his jaw tight. Her right hand pushes weakly against his chest, her mouth open and her eyes glossy. Both stay on the horse. The camera holds still.",
   "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘的草地：基利安把脸从莉莉脸边抬开，直到离她一个手掌宽，眼睛看着她的嘴唇，下颌紧绷。她的右手无力地推着他的胸口，嘴微张，眼睛湿润发亮。两人都留在马上。镜头固定不动。",
   silent(*BREEZE))

# 9-02 “你疯了！放我下去！”（承接 01）------------------------------------------------------------------------------
T9(True, '02｜你疯了放我下去', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the horse's back against a clear blue sky. "
   "Killian at frame-left in profile facing frame-right in the long charcoal overcoat, a cold smirk, his jaw set, his eyes on her face. "
   "Lily at frame-right, her face turned back toward him in profile facing frame-left, her lips red and swollen, her brows drawn together, tears on her lashes, her eyes on his face, her right hand pushing against his chest. The frame holds exactly two people: Killian and Lily.",
   END_WE + LAY_RIDE,
   "侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，在马背上，背后是晴朗的蓝天。"
   "基利安在画面左边，侧身朝画面右边，穿长款炭灰色呢大衣，一抹冷笑，下颌紧绷，眼睛看着她的脸。"
   "莉莉在画面右边，脸向后转向他、侧脸朝画面左边，嘴唇红肿，眉头皱着，睫毛上挂着泪，眼睛看着他的脸，右手推着他的胸口。画面里恰好两个人：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "莉莉带着哭腔喊他疯子、要他放她下去；基利安冷笑着，一点没松手。", "0—6秒侧面中近景，镜头固定。",
   ('LilyRiding', "You're insane! Let me down!", 1.0),
   f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {LR} speaks in a shaky, tearful voice, her brows drawn together and her eyes glossy on his face, her right hand pushing against his chest. {KC} stays close, a cold smirk on his lips and his eyes on her face. Both stay on the horse. The camera holds still.",
   "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘的草地：莉莉用颤抖、带哭腔的声音说话，眉头皱着，湿润的眼睛看着他的脸，右手推着他的胸口。基利安靠得很近，嘴角一抹冷笑，眼睛看着她的脸。两人都留在马上。镜头固定不动。",
   voiced(*BREEZE))

# 9-03 拉大衣裹住她（承接 02）------------------------------------------------------------------------------------
T9(True, '03｜大衣裹住她', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the horse's back against a clear blue sky. "
   "Killian at frame-left in profile facing frame-right, his left hand drawing the front of his long charcoal overcoat across Lily's shoulders, his right hand holding the reins, a cold smirk, his eyes on her face. "
   "Lily at frame-right, her face turned back toward him in profile facing frame-left, her hair tumbling loose, the collar of her cream blouse slipped off one shoulder, her lips red and swollen, her eyes lowered, her brows drawn together. The frame holds exactly two people: Killian and Lily.",
   END_WE + LAY_RIDE,
   "侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，在马背上，背后是晴朗的蓝天。"
   "基利安在画面左边，侧身朝画面右边，左手把长款炭灰色呢大衣的前襟拉过莉莉的肩膀，右手握着缰绳，一抹冷笑，眼睛看着她的脸。"
   "莉莉在画面右边，脸向后转向他、侧脸朝画面左边，头发散乱垂下，奶油色衬衫的领口滑下一边肩膀，嘴唇红肿，眼睛垂着，眉头皱着。画面里恰好两个人：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "基利安冷笑着，用左手把大衣前襟拉过来，把莉莉整个裹进怀里；她不再推他，垂下眼睛。", "0—6秒侧面中近景，镜头固定。", None,
   f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} draws the front of his long charcoal coat across {LR}'s shoulders with his left hand, a cold smirk on his lips and his eyes on her face, his right hand holding the reins. She stops pushing, her lips trembling and her eyes lowered, and the coat closes around her. The camera holds still.",
   "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘的草地：基利安用左手把长款炭灰色大衣的前襟拉过莉莉的肩膀，嘴角一抹冷笑，眼睛看着她的脸，右手握着缰绳。她不再推他，嘴唇发颤，眼睛垂下，大衣在她身周合拢。镜头固定不动。",
   silent("The soft rustle of heavy wool and the creak of leather.", "厚呢子大衣轻轻的摩擦声，和皮革马具的吱嘎声。"))

# 9-04 耳边低语 1（承接 03）----------------------------------------------------------------------------------------
T9(True, '04｜耳边低语一', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the horse's back against a clear blue sky. "
   "Killian at frame-left in profile facing frame-right, his head lowered so his lips are close to her ear, his jaw tight, his eyes narrowed on her ear. "
   "Lily at frame-right, wrapped in his long charcoal overcoat, her hair loose, her eyes closed, her lips trembling, her brows drawn together. The frame holds exactly two people: Killian and Lily.",
   END_WE + LAY_RIDE,
   "侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，在马背上，背后是晴朗的蓝天。"
   "基利安在画面左边，侧身朝画面右边，低着头，嘴唇贴近她的耳朵，下颌紧绷，眯着眼睛看着她的耳朵。"
   "莉莉在画面右边，被他的长款炭灰色呢大衣裹着，头发散着，眼睛闭着，嘴唇发颤，眉头皱着。画面里恰好两个人：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "基利安低头凑到莉莉耳边低声说话；她被大衣裹着，闭着眼睛，嘴唇发颤。", "0—6秒侧面中近景，镜头固定。",
   ('KillianCoat', "You should have run, Lily.", 1.0),
   f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} lowers his head until his lips are close to {LR}'s ear and speaks in a low, husky whisper, his jaw tight and his eyes narrowed on her ear. She stays wrapped in his coat, her eyes closed and her lips trembling. The camera holds still.",
   "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘的草地：基利安低下头，直到嘴唇贴近莉莉的耳朵，用低沉沙哑的气声说话，下颌紧绷，眯着眼睛看着她的耳朵。她一直被大衣裹着，眼睛闭着，嘴唇发颤。镜头固定不动。",
   voiced(*BREEZE))

# 9-05 耳边低语 2（承接 04）----------------------------------------------------------------------------------------
T9(True, '05｜耳边低语二', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the horse's back against a clear blue sky. "
   "Killian at frame-left in profile facing frame-right, his lips close to her ear, his jaw tight, his eyes narrowed with a dark-gold glint. "
   "Lily at frame-right, wrapped in his long charcoal overcoat, her hair loose, her eyes closed, her lips trembling, her brows drawn together. The frame holds exactly two people: Killian and Lily.",
   END_WE + LAY_RIDE,
   "侧面的中近景双人镜头，两个人都是头到胸口，在画面中间三分之一，在马背上，背后是晴朗的蓝天。"
   "基利安在画面左边，侧身朝画面右边，嘴唇贴近她的耳朵，下颌紧绷，眯着眼睛，眼里闪着暗金色的光。"
   "莉莉在画面右边，被他的长款炭灰色呢大衣裹着，头发散着，眼睛闭着，嘴唇发颤，眉头皱着。画面里恰好两个人：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "基利安贴着莉莉的耳边继续低声说话，眼里闪着暗金色的光；她被裹在大衣里，闭着眼睛。", "0—6秒侧面中近景，镜头固定。",
   ('KillianCoat', "No one touches you. Ever.", 1.0),
   f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} stays close to {LR}'s ear and speaks in a low, husky whisper, his jaw tight and his eyes narrowed with a dark-gold glint. She stays wrapped in his coat, her eyes closed and her lips trembling. The camera holds still.",
   "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘的草地：基利安一直凑在莉莉的耳边，用低沉沙哑的气声说话，下颌紧绷，眯起的眼里闪着暗金色的光。她一直被大衣裹着，眼睛闭着，嘴唇发颤。镜头固定不动。",
   voiced(*BREEZE))

# 9-06 骑马沿小路往回走 ----------------------------------------------------------------------------------------------
T9(False, '06｜骑马沿小路走', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on wide shot, both riders and the whole horse, in the middle third of the frame, on the dirt path along the meadow. The tall jet-black horse walks in profile facing frame-right, its head level. "
   "Killian sits behind Lily, at frame-left of her, his left hand on the reins, his jaw set, his lips flat, his eyes on the path ahead at frame-right. "
   "Lily sits in front of him, at frame-right, his open charcoal overcoat wrapped around her as she leans back against his chest, her hair loose, her eyes lowered, her lips parted. The frame holds exactly two people, Killian and Lily, and one black horse.",
   END_WE + LAY_RIDE,
   "侧面的宽景镜头，两个骑手和整匹马都在画面里，在画面中间三分之一，在草地边的土路上。高大的纯黑烈马侧身朝画面右边，头平稳地走着。"
   "基利安坐在莉莉身后，在她的画面左边，左手握着缰绳，下颌紧绷，嘴唇平直，眼睛看着画面右边前方的小路。"
   "莉莉坐在他前面，在画面右边，他敞开的炭灰色呢大衣裹着她，她向后靠在他胸口，头发散着，眼睛垂着，嘴唇微张。画面里恰好两个人和一匹黑马：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "黑马慢慢沿着草地边的小路走着；莉莉被大衣裹着靠在基利安胸口，他看着前方的路。", "0—6秒侧面宽景，镜头固定。", None,
   f"A steady side-on wide shot opens from the adopted first frame in {WE}: {HS} walks slowly along the dirt path toward frame-right with {KC} behind {LR}, his left hand on the reins, his jaw set and his eyes on the path ahead at frame-right. She leans against his chest wrapped in his coat, her eyes lowered and her lips parted. The camera holds still.",
   "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是树林边缘的草地：黑马慢慢沿土路朝画面右边走，基利安坐在莉莉身后，左手握着缰绳，下颌紧绷，眼睛看着画面右边前方的路。她裹在他的大衣里靠着他的胸口，眼睛垂着，嘴唇微张。镜头固定不动。",
   silent(*WALK))

# 9-07 保罗怒吼（保罗单独入画，视线落在画面左边的小路上；带来的人不拍）------------------------------------------------------
T9(False, '07｜保罗怒吼', 6, ['PaulOnScreen'], ('woods_edge', 'paul'), ['woods_edge'],
   "Medium shot of Paul alone, from the head to the waist, in profile facing frame-left, in the middle third of the frame, standing on the dirt path in his navy blazer over a white open-collared shirt, the blazer dusty and the collar crooked, his chest heaving, "
   "his eyes wide and red-rimmed, his jaw clenched, his mouth open, his eyes fixed down the dirt path at frame-left. The rough wooden fence stands behind him at frame-right. The frame holds exactly one person, Paul.",
   END_WE + LAY_WE,
   "保罗一个人的中景，头到腰，侧身朝画面左边，在画面中间三分之一，站在土路上，穿藏青色西装外套和白色敞领衬衫，外套沾着灰，衣领歪着，胸口剧烈起伏，睁大发红的眼睛，下颌咬紧，张着嘴，眼睛盯着画面左边土路的远处。粗木栅栏在他身后的画面右边。画面里恰好一个人：保罗。" + Z_END_WE + Z_WE,
   "保罗站在土路上，睁大发红的眼睛，盯着路的远处，怒吼出声。", "0—6秒保罗侧面中景，镜头固定。",
   ('PaulOnScreen', "Put her down! She's my fiancé!", 1.0),
   f"A steady medium shot opens from the adopted first frame in {WE}: {PL} on the dirt path in profile facing frame-left, his eyes fixed down the path at frame-left. He shouts in a cracking, furious voice, his mouth wide open and his jaw clenched. His body stays where it is. The camera holds still.",
   "一个稳定的中景，从已采用的开场图继续，场景是树林边缘的草地：保罗侧身朝画面左边站在土路上，眼睛盯着画面左边土路的远处。他用破音的、暴怒的声音大喊，嘴张得很大，下颌咬紧。身体留在原处。镜头固定不动。",
   voiced("A light breeze over the meadow.", "草地上轻轻的风声。"))

# 9-08 响指（视线落在画面里的小路上）------------------------------------------------------------------------------
T9(False, '08｜响指', 5, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
   "Side-on wide-medium shot, both riders from the head to the waist and the whole horse, in the middle third of the frame, on the dirt path. The tall jet-black horse stands in profile facing frame-right. "
   "Killian sits behind Lily, at frame-left of her, his left hand holding the reins, his right hand raised to shoulder height with his thumb pressed against his middle finger, ready to snap, his lips flat, his half-lidded eyes cold on the path ahead at frame-right. "
   "Lily sits in front of him, at frame-right, wrapped in his long charcoal overcoat and leaning against his chest, her eyes closed, her lips parted. The frame holds exactly two people, Killian and Lily, and one black horse.",
   END_WE + LAY_RIDE,
   "侧面的宽中景镜头，两个骑手都是头到腰、整匹马都在画面里，在画面中间三分之一，在土路上。高大的纯黑烈马站着，侧身朝画面右边。"
   "基利安坐在莉莉身后，在她的画面左边，左手握着缰绳，右手举到肩膀的高度，拇指按在中指上，准备打响指，嘴唇平直，半垂的眼睛冷冷地看着画面右边前方的小路。"
   "莉莉坐在他前面，在画面右边，裹在他的长款炭灰色呢大衣里，靠着他的胸口，眼睛闭着，嘴唇微张。画面里恰好两个人和一匹黑马：基利安和莉莉。" + Z_END_WE + Z_RIDE,
   "基利安居高临下地看着前面的路，抬起右手打了一个响指；莉莉裹在大衣里闭着眼睛。", "0—5秒侧面宽中景，镜头固定。", None,
   f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {KC} snaps the fingers of his raised right hand, his lips flat and his half-lidded eyes cold on the path ahead at frame-right. {LR} stays wrapped in his coat against his chest, her eyes closed. The camera holds still.",
   "一个稳定的侧面宽中景镜头，从已采用的开场图继续，场景是树林边缘的草地：基利安抬起右手打了一个响指，嘴唇平直，半垂的眼睛冷冷地看着画面右边前方的小路。莉莉一直裹在他的大衣里靠着他的胸口，眼睛闭着。镜头固定不动。",
   silent("A single sharp finger snap and the creak of leather.", "一声清脆的响指，和皮革马具的吱嘎声。"))

c.finish('第9集｜马背上的惩罚',
         '紧接上集：吻结束，莉莉的嘴唇红肿，无力地推着基利安的胸口，哭着骂他疯子、要他放她下去。基利安冷笑，拉过大衣把她整个裹进怀里，贴着她的耳朵低声说“你本该逃的”“从现在起没人能碰你”。黑马沿着草地边的小路慢慢往回走，保罗灰头土脸地赶来，怒吼“把她放下，她是我未婚妻”；基利安居高临下，抬手打了一个响指。',
         O9)

# =========================================================================================================
# 第 10 集 碾压式打脸（场景：马场边缘）
# =========================================================================================================
d = Batch(O9 + '.json', SERIES_TITLE, 4100)
ZH10 = []
T10 = maker(d, ZH10)
d.person('bodyguard', '黑衣保镖',
         "Bodyguard, a tall, broad-shouldered adult man in his thirties with a shaved head and a stern, impassive face, wearing a black suit, a white shirt, a black tie and a clear coiled earpiece. The portrait fixes his identity and clothes, not staging.",
         "黑衣保镖，一个三十多岁、身材高大、肩膀宽阔的成年男性，剃着光头，面容严厉、毫无表情，穿黑色西装、白衬衫、黑领带，戴一只透明的螺旋线耳机。人物图固定身份和衣服，不固定站位。",
         "A photorealistic half-body portrait of a tall, broad-shouldered adult man in his thirties with a shaved head and a stern, impassive face, wearing a black suit, a white shirt, a black tie and a clear coiled earpiece. "
         "He faces the camera with a stern, impassive expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.")
d.character('Bodyguard', 'bodyguard',
            "A deep adult male voice, flat and calm, speaking clear American English. Every word is fully voiced and audible.",
            "低沉的成年男声，平淡冷静，说清楚的美式英语。每个字都正常发声、清晰可辨。")

# 10-01 响指的结果：黑衣保镖就位 ---------------------------------------------------------------------------------
T10(False, '01｜黑衣保镖就位', 5, ['Bodyguard'], ('ranch', 'bodyguard'), ['ranch'],
    "Side-on medium two-shot, two men from the head to the knees, in the middle third of the frame, standing shoulder to shoulder on the packed-earth track, both in profile facing frame-right. "
    "Bodyguard at frame-left in a black suit, a white shirt, a black tie and a clear coiled earpiece, his hands clasped in front of him, his jaw set, his lips flat, his eyes on the white fence at frame-right. "
    "A second man identical to him in build and clothes stands at frame-right of him, his hands clasped in front, his jaw set, his lips flat, his eyes on the white fence. The frame holds exactly two people: two bodyguards.",
    END_RN + LAY_RN,
    "侧面的中景双人镜头，两个男人都是头到膝盖，在画面中间三分之一，并肩站在夯实的泥土跑道上，都侧身朝画面右边。"
    "保镖在画面左边，穿黑西装、白衬衫、黑领带，戴透明螺旋线耳机，双手交握在身前，下颌紧绷，嘴唇平直，眼睛看着画面右边的白色栅栏。"
    "第二个男人和他身材、衣着一模一样，站在他的画面右边，双手交握在身前，下颌紧绷，嘴唇平直，眼睛看着白色栅栏。画面里恰好两个人：两个保镖。" + Z_END_RN + Z_RN,
    "两个黑衣保镖并肩站着，双手交握，一动不动，盯着前面的白色栅栏。", "0—5秒侧面中景，镜头固定。", None,
    f"A steady side-on medium two-shot opens from the adopted first frame in {RN}: two bodyguards who both look like {BG} stand shoulder to shoulder in profile facing frame-right, their hands clasped in front of them and their eyes on the white fence at frame-right. Their jaws stay set and their lips stay flat. They stay motionless. The camera holds still.",
    "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是私人跑马场：两个长得都像参考图保镖的男人并肩侧身朝画面右边站着，双手交握在身前，眼睛看着画面右边的白色栅栏。他们的下颌一直紧绷，嘴唇一直平直。两人一动不动。镜头固定不动。",
    silent("A light breeze and the soft creak of leather shoes on packed earth.", "轻轻的风声，和皮鞋踩在夯实泥土上轻轻的吱嘎声。"))

# 10-02 护在身后 ----------------------------------------------------------------------------------------------
T10(False, '02｜护在身后', 5, ['KillianCoat', 'LilyRiding'], ('ranch', 'killian_coat', 'lily_riding'), ['ranch'],
    "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, standing on the packed-earth track, both in profile facing frame-right. "
    "Lily at frame-left, half a step behind Killian, in the cream blouse with her hair loose, her left hand gripping his coat sleeve at the elbow, her lips parted, her brows drawn together, her eyes lowered on her hand on his sleeve. "
    "Killian at frame-right in the long charcoal overcoat, his right arm held out low at his side as a barrier, his jaw set, his lips flat, his eyes on the white fence at frame-right. The frame holds exactly two people: Lily and Killian.",
    END_RN + LAY_RN,
    "侧面的中景双人镜头，两个人都是头到膝盖，在画面中间三分之一，站在夯实的泥土跑道上，都侧身朝画面右边。"
    "莉莉在画面左边，站在基利安身后半步，穿奶油色衬衫，头发散着，左手抓着他大衣袖子的肘部，嘴唇微张，眉头皱着，眼睛垂着看着自己抓在他袖子上的手。"
    "基利安在画面右边，穿长款炭灰色呢大衣，右臂低低地横在身侧挡着，下颌紧绷，嘴唇平直，眼睛看着画面右边的白色栅栏。画面里恰好两个人：莉莉和基利安。" + Z_END_RN + Z_RN,
    "基利安站在前面，伸出手臂把莉莉挡在身后；她抓着他的袖子，低着头。", "0—5秒侧面中景，镜头固定。", None,
    f"A steady side-on medium two-shot opens from the adopted first frame in {RN}: {KC} at frame-right stands with his arm out in front of {LR} as a barrier, his jaw set and his eyes on the white fence at frame-right. She stands half a step behind him at frame-left, her hand gripping his sleeve, her lips parted and her eyes on her hand. Both stay where they are. The camera holds still.",
    "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是私人跑马场：基利安在画面右边，伸出手臂挡在莉莉前面，下颌紧绷，眼睛看着画面右边的白色栅栏。她站在他身后半步的画面左边，手抓着他的袖子，嘴唇微张，眼睛看着自己的手。两人都留在原处。镜头固定不动。",
    silent(*RANCH_SND))

# 10-03 抓领子 + 台词 -------------------------------------------------------------------------------------------
T10(False, '03｜抓住保罗的领子', 6, ['KillianCoat', 'PaulOnScreen'], ('ranch', 'killian_coat', 'paul'), ['ranch'],
    "Side-on medium two-shot, both men from the head to the waist, in the middle third of the frame, face to face in profile on the packed-earth track. "
    "Killian at frame-left, facing frame-right, in the long charcoal overcoat, his right arm straight, his right hand gripping Paul's jacket collar at chest height, his jaw set, his lips flat, his eyes cold and level on Paul's face. "
    "Paul at frame-right, facing frame-left, in the navy blazer, both of his hands gripping Killian's right wrist, his mouth open, his brows pulled up, his eyes wide and fixed on Killian's face. The frame holds exactly two people: Killian and Paul.",
    END_RN + LAY_RN,
    "侧面的中景双人镜头，两个男人都是头到腰，在画面中间三分之一，在夯实的泥土跑道上侧身面对面。"
    "基利安在画面左边，侧身朝画面右边，穿长款炭灰色呢大衣，右臂伸直，右手在胸口的高度抓着保罗外套的领子，下颌紧绷，嘴唇平直，冷冷地平视着保罗的脸。"
    "保罗在画面右边，侧身朝画面左边，穿藏青色西装外套，双手一起抓着基利安的右手腕，张着嘴，眉毛扬起，睁大眼睛盯着基利安的脸。画面里恰好两个人：基利安和保罗。" + Z_END_RN + Z_RN,
    "基利安一手抓着保罗的外套领子，冷冷地说话；保罗双手抓着他的手腕，张着嘴，睁大眼睛。", "0—6秒侧面中景，镜头固定。",
    ('KillianCoat', "Your father sold you. One dollar.", 1.0),
    f"A steady side-on medium two-shot opens from the adopted first frame in {RN}: {KC} at frame-left holds {PL}'s jacket collar in his right hand, his arm straight, and speaks in a low, icy voice, his jaw set and his eyes cold and level on Paul's face. Paul grips Killian's wrist with both hands, his mouth open and his eyes wide. Both stay where they are. The camera holds still.",
    "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是私人跑马场：基利安在画面左边，右手抓着保罗外套的领子，手臂伸直，用低沉冰冷的声音说话，下颌紧绷，冷冷地平视着保罗的脸。保罗双手抓着基利安的手腕，张着嘴，睁大眼睛。两人都留在原处。镜头固定不动。",
    voiced(*RANCH_SND))

# 10-04 保罗坐在地上（被甩开的结果）--------------------------------------------------------------------------------
T10(False, '04｜保罗坐在地上', 5, ['KillianCoat', 'PaulOnScreen'], ('ranch', 'killian_coat', 'paul'), ['ranch'],
    "Side-on medium two-shot, in the middle third of the frame, on the packed-earth track. "
    "Killian at frame-left, standing, from the head to the knees, facing frame-right, in the long charcoal overcoat, his hands at his sides, his jaw set, his lips flat, his cold eyes lowered on Paul's face. "
    "Paul at frame-right, sitting on the ground, leaning back on both hands, in the navy blazer with the jacket collar crumpled, his mouth open, his brows pulled up, his eyes wide on Killian's face. The frame holds exactly two people: Killian and Paul.",
    END_RN + LAY_RN,
    "侧面的中景双人镜头，在画面中间三分之一，在夯实的泥土跑道上。"
    "基利安在画面左边，站着，头到膝盖，侧身朝画面右边，穿长款炭灰色呢大衣，双手垂在身侧，下颌紧绷，嘴唇平直，冰冷的眼睛垂着看着保罗的脸。"
    "保罗在画面右边，坐在地上，双手撑在身后向后仰着，穿藏青色西装外套，衣领被揉皱，张着嘴，眉毛扬起，睁大眼睛看着基利安的脸。画面里恰好两个人：基利安和保罗。" + Z_END_RN + Z_RN,
    "保罗跌坐在地上，仰头看着基利安；基利安垂着手，冷冷地低头看着他。", "0—5秒侧面中景，镜头固定。", None,
    f"A steady side-on medium two-shot opens from the adopted first frame in {RN}: {KC} at frame-left stands over {PL}, his hands at his sides, his lips flat and his cold eyes lowered on Paul's face. Paul sits on the ground leaning on both hands, his mouth open and his eyes wide on Killian's face. Both stay where they are. The camera holds still.",
    "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是私人跑马场：基利安在画面左边，站在保罗上方，双手垂在身侧，嘴唇平直，冰冷的眼睛垂着看着保罗的脸。保罗坐在地上，双手撑着身体，张着嘴，睁大眼睛看着基利安的脸。两人都留在原处。镜头固定不动。",
    silent(*RANCH_SND))

# 10-05 公主抱 + 台词（动作不拍，开场图里已经抱起）--------------------------------------------------------------------
T10(False, '05｜公主抱宣示', 6, ['KillianCoat', 'LilyRiding'], ('ranch', 'killian_coat', 'lily_riding'), ['ranch'],
    "Side-on medium shot, from the head of the man to below the knees of the woman in his arms, in the middle third of the frame, on the packed-earth track. "
    "Killian stands in profile facing frame-right in the long charcoal overcoat, carrying Lily in both arms across his chest, his right arm under her knees and his left arm behind her back, his jaw set, his lips flat, his cold eyes on the white fence at frame-right. "
    "Lily lies in his arms with her head resting against his shoulder, her left arm hanging loose, her lips parted, her dazed half-open eyes looking up at his jaw. The frame holds exactly two people: Killian and Lily.",
    END_RN + LAY_RN,
    "侧面的中景镜头，从男人的头到他怀里女人的膝盖以下，在画面中间三分之一，在夯实的泥土跑道上。"
    "基利安侧身朝画面右边站着，穿长款炭灰色呢大衣，双臂把莉莉横抱在胸前，右臂托着她的膝弯，左臂托着她的后背，下颌紧绷，嘴唇平直，冰冷的眼睛看着画面右边的白色栅栏。"
    "莉莉躺在他怀里，头靠着他的肩膀，左臂松松垂着，嘴唇微张，失神的半睁着的眼睛仰望着他的下颌。画面里恰好两个人：基利安和莉莉。" + Z_END_RN + Z_RN,
    "基利安把莉莉横抱在怀里，冷冷地宣布她是他的；她吓傻了，仰头看着他的下颌。", "0—6秒侧面中景，镜头固定。",
    ('KillianCoat', "Lily Swan belongs to me.", 1.0),
    f"A steady side-on medium shot opens from the adopted first frame in {RN}: {KC} holds {LR} in his arms across his chest and speaks in a low, steely voice, his jaw set and his cold eyes on the white fence at frame-right. She lies against his shoulder, her lips parted and her dazed eyes half open, looking up at his jaw. Both stay where they are. The camera holds still.",
    "一个稳定的侧面中景镜头，从已采用的开场图继续，场景是私人跑马场：基利安把莉莉横抱在胸前，用低沉、像钢一样冷硬的声音说话，下颌紧绷，冰冷的眼睛看着画面右边的白色栅栏。她靠着他的肩膀躺着，嘴唇微张，失神的眼睛半睁着，仰望着他的下颌。两人都留在原处。镜头固定不动。",
    voiced(*RANCH_SND))

# 10-06 台词 2（承接 05）---------------------------------------------------------------------------------------
T10(True, '06｜谁敢碰她', 6, ['KillianCoat', 'LilyRiding'], ('ranch', 'killian_coat', 'lily_riding'), ['ranch'],
    "Side-on medium shot, from the head of the man to below the knees of the woman in his arms, in the middle third of the frame, on the packed-earth track. "
    "Killian stands in profile facing frame-right in the long charcoal overcoat, carrying Lily in both arms across his chest, his jaw set, his lips flat, his eyes narrowed with a dark-gold glint on the white fence at frame-right. "
    "Lily lies in his arms with her head resting against his shoulder, her left arm hanging loose, her lips parted, her dazed eyes half open. The frame holds exactly two people: Killian and Lily.",
    END_RN + LAY_RN,
    "侧面的中景镜头，从男人的头到他怀里女人的膝盖以下，在画面中间三分之一，在夯实的泥土跑道上。"
    "基利安侧身朝画面右边站着，穿长款炭灰色呢大衣，双臂把莉莉横抱在胸前，下颌紧绷，嘴唇平直，眯着眼睛，眼里闪着暗金色的光，看着画面右边的白色栅栏。"
    "莉莉躺在他怀里，头靠着他的肩膀，左臂松松垂着，嘴唇微张，失神的眼睛半睁着。画面里恰好两个人：基利安和莉莉。" + Z_END_RN + Z_RN,
    "基利安抱着莉莉，眼里闪着暗金色的光，继续低声警告所有人。", "0—6秒侧面中景，镜头固定。",
    ('KillianCoat', "Touch her, and you're all dead.", 1.0),
    f"A steady side-on medium shot opens from the adopted first frame in {RN}: {KC} holds {LR} in his arms and speaks in a low, steely voice, his jaw set and his eyes narrowed with a dark-gold glint on the white fence at frame-right. She lies against his shoulder, her lips parted and her eyes half open. Both stay where they are. The camera holds still.",
    "一个稳定的侧面中景镜头，从已采用的开场图继续，场景是私人跑马场：基利安抱着莉莉，用低沉、像钢一样冷硬的声音说话，下颌紧绷，眯起的眼里闪着暗金色的光，看着画面右边的白色栅栏。她靠着他的肩膀躺着，嘴唇微张，眼睛半睁着。两人都留在原处。镜头固定不动。",
    voiced(*RANCH_SND))

# 10-07 莉莉晕倒 + “Lily!”（承接 06）---------------------------------------------------------------------------
T10(True, '07｜莉莉晕倒', 6, ['KillianCoat', 'LilyRiding'], ('ranch', 'killian_coat', 'lily_riding'), ['ranch'],
    "Side-on medium shot, from the head of the man to below the knees of the woman in his arms, in the middle third of the frame, on the packed-earth track. "
    "Killian stands in profile facing frame-right in the long charcoal overcoat, carrying Lily in both arms across his chest, his brows pulled up, his mouth open, his eyes wide on her face. "
    "Lily lies in his arms with her head tipped back over his arm, her eyes closed, her lips parted, her left arm hanging loose. The frame holds exactly two people: Killian and Lily.",
    END_RN + LAY_RN,
    "侧面的中景镜头，从男人的头到他怀里女人的膝盖以下，在画面中间三分之一，在夯实的泥土跑道上。"
    "基利安侧身朝画面右边站着，穿长款炭灰色呢大衣，双臂把莉莉横抱在胸前，眉毛高高扬起，张着嘴，睁大眼睛看着她的脸。"
    "莉莉躺在他怀里，头向后仰在他的手臂上，眼睛闭着，嘴唇微张，左臂松松垂着。画面里恰好两个人：基利安和莉莉。" + Z_END_RN + Z_RN,
    "莉莉在他怀里晕过去，头向后仰；基利安脸色大变，喊她的名字。", "0—6秒侧面中景，镜头固定。",
    ('KillianCoat', "Lily!", 1.0),
    f"A steady side-on medium shot opens from the adopted first frame in {RN}: {KC} looks down at {LR}'s face and calls her name in a cracking, urgent voice, his brows pulled up, his mouth open and his eyes wide. She goes limp, her head tipping back over his arm, her eyes closed and her lips parted. The camera holds still.",
    "一个稳定的侧面中景镜头，从已采用的开场图继续，场景是私人跑马场：基利安低头看着莉莉的脸，用破音、焦急的声音喊她的名字，眉毛高高扬起，张着嘴，睁大眼睛。她瘫软下来，头向后仰在他的手臂上，眼睛闭着，嘴唇微张。镜头固定不动。",
    voiced(*RANCH_SND))

d.finish('第10集｜碾压式打脸',
         '基利安的响指之后，黑衣保镖就位。他把莉莉护在身后，一把抓住保罗的外套领子，冷冷地说“你父亲把你卖了，一块钱”，把保罗甩坐在地上。他把吓傻的莉莉横抱起来，当众宣布“莉莉·斯旺是我的”“谁敢碰她，你们全都得死”。莉莉在他怀里晕了过去，他脸色大变，喊她的名字。',
         O10)

# =========================================================================================================
# 第 10 集 B：大动作实验（放在最后；剧本里这几个动作我在 A 里都绕开了，这里原样试一次）
# =========================================================================================================
e = Batch(O10 + '.json', SERIES_TITLE, 4200)
ZH10B = []
T10B = maker(e, ZH10B)

T10B(False, 'T1｜翻过看台栏杆', 5, ['KillianCoat'], ('ranch', 'killian_coat'), ['ranch'],
     "Medium shot of Killian alone, from the head to the knees, in profile facing frame-right, in the middle third of the frame, at the railing of the raised wooden grandstand in the long charcoal overcoat, both hands gripping the top rail, his knees bent and his weight forward, "
     "his jaw clenched, his lips pulled back from his teeth, his eyes narrowed with a dark-gold glint on the dark pine trees at frame-right. The frame holds exactly one person, Killian.",
     END_RN + LAY_RN,
     "基利安一个人的中景，头到膝盖，侧身朝画面右边，在画面中间三分之一，在凸起的木制看台的栏杆边，穿长款炭灰色呢大衣，双手抓着栏杆顶上的横杆，膝盖弯曲，重心前倾，下颌咬紧，嘴唇向后拉开露出牙齿，眯着眼睛，眼里闪着暗金色的光，盯着画面右边的深色松树。画面里恰好一个人：基利安。" + Z_END_RN + Z_RN,
     "基利安双手撑着栏杆，一跃翻过栏杆，落到下面的草地上。", "0—5秒侧面中景，镜头固定。", None,
     f"A steady medium shot opens from the adopted first frame in {RN}: {KC} in profile facing frame-right at the grandstand railing, both hands on the top rail, his eyes on the dark pine trees at frame-right. He pushes off, vaults over the railing with both hands on the top rail and drops down to the grass below, his coat flying, his jaw clenched and his eyes narrowed. The camera holds still.",
     "一个稳定的中景，从已采用的开场图继续，场景是私人跑马场：基利安侧身朝画面右边站在看台栏杆边，双手抓着栏杆顶上的横杆，眼睛看着画面右边的深色松树。他蹬地一跃，双手撑着横杆翻过栏杆，落到下面的草地上，大衣飞扬，下颌咬紧，眯着眼睛。镜头固定不动。",
     silent("A heavy thud of boots landing on grass.", "靴子重重落在草地上的闷响。"))

T10B(False, 'T2｜单手提起保罗的领子', 6, ['KillianCoat', 'PaulOnScreen'], ('ranch', 'killian_coat', 'paul'), ['ranch'],
     "Side-on medium two-shot, both men from the head to the knees, in the middle third of the frame, face to face in profile on the packed-earth track. "
     "Killian at frame-left, facing frame-right, in the long charcoal overcoat, his right arm straight, his right hand gripping Paul's jacket collar at chest height, his jaw set, his lips flat, his eyes cold and level on Paul's face. "
     "Paul at frame-right, facing frame-left, in the navy blazer, both of his hands gripping Killian's right wrist, his mouth open, his brows pulled up, his eyes wide and fixed on Killian's face. The frame holds exactly two people: Killian and Paul.",
     END_RN + LAY_RN,
     "侧面的中景双人镜头，两个男人都是头到膝盖，在画面中间三分之一，在夯实的泥土跑道上侧身面对面。"
     "基利安在画面左边，侧身朝画面右边，穿长款炭灰色呢大衣，右臂伸直，右手在胸口的高度抓着保罗外套的领子，下颌紧绷，嘴唇平直，冷冷地平视着保罗的脸。"
     "保罗在画面右边，侧身朝画面左边，穿藏青色西装外套，双手一起抓着基利安的右手腕，张着嘴，眉毛扬起，睁大眼睛盯着基利安的脸。画面里恰好两个人：基利安和保罗。" + Z_END_RN + Z_RN,
     "基利安单手把保罗提离地面，保罗双脚乱蹬。", "0—6秒侧面中景，镜头固定。", None,
     f"A steady side-on medium two-shot opens from the adopted first frame in {RN}: {KC} at frame-left lifts {PL} by the jacket collar with his right arm until Paul's heels leave the ground, his arm straight and his eyes cold and level on Paul's face. Paul grips Killian's wrist with both hands, his mouth open and his eyes wide, his feet kicking. The camera holds still.",
     "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是私人跑马场：基利安在画面左边，用右臂抓着保罗外套的领子把他提起，直到保罗的脚后跟离开地面，手臂伸直，冷冷地平视着保罗的脸。保罗双手抓着基利安的手腕，张着嘴，睁大眼睛，双脚乱蹬。镜头固定不动。",
     silent(*RANCH_SND))

T10B(False, 'T3｜保罗被五个人围住（群像）', 5, ['PaulOnScreen', 'Bodyguard'], ('ranch', 'paul', 'bodyguard'), ['ranch'],
     "Side-on wide shot of the packed-earth track, five men in the middle third of the frame. "
     "Paul stands in the center in his navy blazer, very still, his hands slightly raised, his mouth open, his eyes wide and darting along the ring of men around him. "
     "Bodyguard at frame-left and three more men identical to him in build and clothes stand around Paul in a half circle, all in black suits, white shirts and black ties, their hands clasped in front of them, their jaws set, their lips flat, their eyes on Paul. The frame holds exactly five people: Paul and four bodyguards.",
     END_RN + LAY_RN,
     "侧面的宽景镜头，夯实的泥土跑道上，五个男人在画面中间三分之一。"
     "保罗站在正中，穿藏青色西装外套，一动不动，双手微微举起，张着嘴，睁大的眼睛不安地扫过围着他的一圈人。"
     "保镖在画面左边，另外三个和他身材、衣着一模一样的男人，在保罗周围围成半圈，都穿黑西装、白衬衫、黑领带，双手交握在身前，下颌紧绷，嘴唇平直，眼睛盯着保罗。画面里恰好五个人：保罗和四个保镖。" + Z_END_RN + Z_RN,
     "四个黑衣保镖围成半圈，保罗站在中间，不安地看着他们。", "0—5秒侧面宽景，镜头固定。", None,
     f"A steady side-on wide shot opens from the adopted first frame in {RN}: {PL} stands in the center with four bodyguards ({BG}) around him in a half circle, all four with their hands clasped in front of them and their eyes on Paul. Paul's eyes dart along the ring of men, his mouth open. The four bodyguards ({BG}) keep their jaws set and their lips flat. The camera holds still.",
     "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是私人跑马场：保罗站在中间，四个保镖在他周围围成半圈，四个人都双手交握在身前，眼睛盯着保罗。保罗的眼睛不安地扫过这一圈人，张着嘴。保镖们的下颌一直紧绷，嘴唇一直平直。镜头固定不动。",
     silent("A light breeze and the soft creak of leather shoes on packed earth.", "轻轻的风声，和皮鞋踩在夯实泥土上轻轻的吱嘎声。"))

T10B(False, 'T4｜把莉莉横抱起来', 6, ['KillianCoat', 'LilyRiding'], ('ranch', 'killian_coat', 'lily_riding'), ['ranch'],
     "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, on the packed-earth track. "
     "Lily at frame-left, standing and swaying, in the cream blouse with her hair loose, her left hand resting on Killian's chest, her lips parted, her brows drawn together, her eyes half closed. "
     "Killian at frame-right, in profile facing frame-left, in the long charcoal overcoat, bending slightly, his right arm behind her back and his left arm behind her knees, about to lift her, his jaw set, his lips flat, his eyes on her face. The frame holds exactly two people: Lily and Killian.",
     END_RN + LAY_RN,
     "侧面的中景双人镜头，两个人都是头到膝盖，在画面中间三分之一，在夯实的泥土跑道上。"
     "莉莉在画面左边，站着、身体摇晃，穿奶油色衬衫，头发散着，左手搭在基利安的胸口，嘴唇微张，眉头皱着，眼睛半闭。"
     "基利安在画面右边，侧身朝画面左边，穿长款炭灰色呢大衣，微微弯腰，右臂绕到她背后，左臂伸到她膝弯后面，准备把她抱起，下颌紧绷，嘴唇平直，眼睛看着她的脸。画面里恰好两个人：莉莉和基利安。" + Z_END_RN + Z_RN,
     "基利安一把把莉莉横抱起来，她的脚离开地面，头靠在他肩上。", "0—6秒侧面中景，镜头固定。", None,
     f"A steady side-on medium two-shot opens from the adopted first frame in {RN}: {KC} sweeps {LR} up into his arms, his right arm behind her back and his left arm under her knees, until her feet leave the ground and her head falls against his shoulder, his eyes on her face and his jaw set. Her eyes close and her lips part. The camera holds still.",
     "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是私人跑马场：基利安右臂托着莉莉的后背、左臂托着她的膝弯，一把把她横抱起来，直到她的脚离开地面、头靠在他的肩上，眼睛看着她的脸，下颌紧绷。她的眼睛闭上，嘴唇微张。镜头固定不动。",
     silent(*RANCH_SND))

e.finish('第10集B｜大动作实验',
         '实验，不进成片：四个剧本里写了、但我在正式版里绕开的动作原样试一次——基利安翻过看台栏杆；单手提起保罗的领子；保罗被四个保镖围成半圈（五个人的群像）；把站着的莉莉横抱起来。',
         O10B)

# =========================================================================================================
# 合并、说明
# =========================================================================================================
files = [os.path.join(FOLDER, x + '.json') for x in (O7, O8, O9, O10, O10B)]
subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'merge_eps.py'), OMERGE, *files, '--rename',
                '第7集｜致命危机=剧本第7集｜致命危机', '第8集｜极致共骑=剧本第8集｜极致共骑', '第9集｜马背上的惩罚=剧本第9集｜马背上的惩罚',
                '第10集｜碾压式打脸=剧本第10集｜碾压式打脸', '第10集B｜大动作实验=剧本第10集B｜大动作实验（实验）'], check=True)

SEGS = {k: x.d['episodes'][0]['segments'] for k, x in (('7', a), ('8', b), ('9', c), ('10', d), ('10B', e))}
ZHS = {'7': ZH7, '8': ZH8, '9': ZH9, '10': ZH10, '10B': ZH10B}
NAMES = {'7': '第 7 集 致命危机', '8': '第 8 集 极致共骑', '9': '第 9 集 马背上的惩罚', '10': '第 10 集 碾压式打脸', '10B': '第 10 集 B 大动作实验'}


def fmt_table(segs):
    rows = ["| 号 | 名字 | 秒 | 在场 | 承接 | 英语台词 | 种子 |", "|---|---|---|---|---|---|---|"]
    for s in segs:
        dl = f"{s['dialogue'][0]['speaker']}：{s['dialogue'][0]['text']}" if s['dialogue'] else '（无台词）'
        rows.append(f"| {s['title'].split('｜')[0]} | {s['title'].split('｜')[1]} | {s['duration_seconds']} | {len(s['characters'])} | {'是' if s['depends_on_previous'] else '否'} | {dl} | {s['seed']} |")
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
n_a = sum(len(SEGS[k]) for k in ('7', '8', '9', '10'))
sec_a = sum(s['duration_seconds'] for k in ('7', '8', '9', '10') for s in SEGS[k])
md = []
md.append("# 剧本第 7–10 集（马场四集）＋大动作实验：怎么用（2026-10-10）\n")
md.append(f"**只粘贴一个文件：** `{OMERGE}_全选复制粘贴.txt`。里面 5 集：剧本第 7、8、9、10 集（正式版，{n_a} 个任务、{sec_a} 秒）＋剧本第 10 集 B（{len(SEGS['10B'])} 个任务、{n_sec - sec_a} 秒的实验，**放在最后，不进成片**，你想省时间可以不等它）。合计 {n_tasks} 个任务、{n_sec} 秒。种子：3801–3809、3901–3908、4001–4008、4101–4107、4201–4204。\n")
md.append("设置照旧：视频/对白共用次数 = 1，对白时间余量 = 0；追加窗口不要勾“每集／总／任务秒数”。**追加必须等上一批全部跑完。**\n")
md.append(f"**预计时间：{n_tasks} 个任务 × 约 7 分钟 ≈ {n_tasks*7//60} 小时 {n_tasks*7%60} 分钟（7 分钟是上限推算，不是实测——你告诉我机器一个任务实际几分钟，我再调）。**\n")
md.append("## 零、插件里会显示第几集（集标题前面我加了“剧本”二字）\n")
md.append("| 剧本 | 如果**先追加补拍包、再追加本文件** | 如果**先追加本文件、再追加补拍包** |\n|---|---|---|")
md.append("| 补拍包 | 第 10 集 | 第 15 集 |\n| 剧本第 7 集 | 第 11 集 | 第 10 集 |\n| 剧本第 8 集 | 第 12 集 | 第 11 集 |\n| 剧本第 9 集 | 第 13 集 | 第 12 集 |\n| 剧本第 10 集 | 第 14 集 | 第 13 集 |\n| 剧本第 10 集 B（实验） | 第 15 集 | 第 14 集 |\n")
md.append("两种顺序都能用（本文件的素材和补拍包的素材是同名同内容的超集）。屏幕上的号以你那边为准，集标题里的“剧本第几集”不会错。\n")
md.append("## 一、我对剧本改了什么（先说清楚，你可以否决）\n")
md.append("原则：H3 做得稳的是**单人／双人、侧面、手有主人、小动作**；做不稳或没试过的大动作，正式版里**绕开，用“结果镜头”代替**，同时把原样的大动作放进 B 实验里测一次。\n")
md.append("| 剧本原写 | 我怎么拍（正式版） | 为什么 | 补救／验证 |\n|---|---|---|---|")
md.append("| 第 7 集：基利安“从几米高的看台一跃而下” | 7-08 他猛地抬头盯向松树，7-09 把金色手机捏变形；第 8 集一开头直接是莉莉在狂奔的马上 | 人跳跃、走出画面都没试过（H20 退场还没结论） | B 的 T1 原样试“翻过栏杆”；成功就把 T1 插在 7-09 和 8-01 之间 |")
md.append("| 第 7 集：玛丽“暗中”扎针；莉莉“踩马镫、跨上马背”；“玛丽等人的嘲笑声” | 7-05 明着拍：玛丽甜笑着把针按在马屁股上；7-04 莉莉已经坐在马上；嘲笑只用玛丽一个人的甜笑 | H3 画不出“暗中”；上马是大动作；人群最多 2 人 | 买通驯马师改成玛丽自己说出口（7-02），让“谁干的”有人说出来 |")
md.append("| 第 8 集：“一道黑影在草地上狂飙”，基利安“腾空跃上马背” | 8-02 他已经坐在莉莉身后 | 同上，而且马上要同时有两人一马 | 跃上马背太难，不测 |")
md.append("| 第 9 集：“骑马走出树林”“保罗带着人”赶来 | 9-06 沿草地边的小路往回走；保罗一个人入画（9-07） | 最多 2 人规则；马和树林的方向会乱 | 带来的人不拍 |")
md.append("| 第 10 集：几十个荷枪实弹的保镖围住保罗和随从 | 10-01 两个空手的黑衣保镖就位 | 人群会多出陌生人、枪是危险道具 | B 的 T3 试“四个保镖围住保罗”（五个人） |")
md.append("| 第 10 集：“翻身下马，把莉莉抱下来”；“一把掐住脖子，单手提到半空”；“像丢垃圾一样扔在地上”；“打横抱起” | 10-02 两人已在地上；10-03 抓住外套领子；10-04 保罗已坐在地上；10-05 开场图里已经抱着 | 提人、扔人、抱人都是双人的大动作 | B 的 T2 试“单手提领子”，T4 试“把站着的莉莉横抱起来” |")
md.append("| 基利安的衣服 | 全程穿同一件炭灰色长大衣（第 7 集在看台上就穿着） | 第 9 集“拉过大衣把她裹在怀里”才成立；少一个素材 | — |")
md.append("| 台词 | 英语短句，一个任务一句、一个说话人、≤6 个单词；保罗的台词合并成 `Put her down! She's my fiancé!`；基利安的长台词拆成 10-03、10-05、10-06 三个任务 | 台词规则 | “他昨天已经把婚约和股份作价一块钱卖给我”压缩成 `Your father sold you. One dollar.`，细节不要了 |\n")
md.append("## 二、接缝检查（第 7 集起写稿前必做）\n")
md.append("| 接缝 | 上一镜的状态 | 下一镜 | 怎么接 | 风险 |\n|---|---|---|---|---|")
md.append("| 第 6 集 → 第 7 集 | 宴会厅里保罗大喊“莉莉！他在说什么？！” | 几天后的马场 | 硬切到新场景；保罗的问题到第 10 集 10-03 才有回应（“你父亲把你卖了，一块钱”）——这是剧本的设计 | 观众不知道“几天后”：画面里没有字幕。如果 hh 觉得需要，可以以后补一个“莉莉在车上收到马术邀请”的镜头 |")
md.append("| 7-09 → 8-01 | 基利安捏碎手机、盯着右边的松树 | 莉莉在狂奔的马上 | 两边都朝画面右边（松树／尖桩栅栏），马一直朝右跑 | 少了“他怎么赶到的”：B 的 T1 是备选 |")
md.append("| 8-01 → 8-02 | 莉莉一个人在马上快被甩下 | 基利安已在她身后 | 同一匹马、同一方向、同一排尖桩栅栏都在画面右边 | 人突然多出一个；看开场图里是否只有两人 |")
md.append("| 8-08 → 9-01（跨集） | 基利安吻住莉莉 | 吻结束 | 9-01 开场图文字写成 8-08 的同一个姿势、两人距离一个手掌宽 | 每集第一个任务关“承接前段”，姿势靠文字写出来 |")
md.append("| 9-08 → 10-01 | 基利安打响指 | 黑衣保镖就位 | “响指→保镖”是因果：10-01 的开场图里保镖看着画面右边的白色栅栏（同一个朝向） | 保镖只有 2 个，观众可能觉得“就这点人？”（T3 是备选） |")
md.append("| 10-07 → 第 11 集（剧本） | 莉莉晕倒在基利安怀里 | 剧本第 11 集：莉莉昏迷躺在床上 | 自然衔接，不需要补 | — |\n")
md.append("**每场戏结束时看得见的结果镜头：** 买通（7-02 驯马师接过信封）；上马（7-04 她已坐在马上）；扎针（7-05 马耳朵向后压）；失控（7-07 狂奔）；求援（7-08/09 基利安捏碎手机）；救援（8-02 他已在她身后）；制服（8-03/8-05 马被勒停）；吻（8-08）；占有（9-03 大衣裹住她）；打脸（10-03 抓领子、10-04 保罗坐在地上）；宣示（10-05）；晕倒（10-07）。\n")
md.append("**关键信息谁第一次说出口：** 买通——玛丽说“给她最野的那匹”（7-02）；恐吓——基利安 9-04、9-05、10-06；婚约被卖——基利安 10-03（“你父亲把你卖了，一块钱”）；“莉莉是我的”——10-05。\n")
md.append("## 三、做完能得到什么（想测什么、怎么算成功、失败说明什么）\n")
md.append("**这批的总体目的：** 第一次拍“马”。要知道 H3 画马（四条腿、马头、缰绳、鞍）靠不靠谱；人在马上的动作（抓缰绳、环腰、人立）稳不稳；以及前面学到的规矩（表情、不画外、6 秒放台词）在新题材里还成不成立。\n")
md.append("| 任务 | 想测什么 | 算成功 | 失败说明什么 |\n|---|---|---|---|")
md.append("| 7-03 | 人＋人＋马同框（两人一马）；马头有没有对上、驯马师手是否握着笼头 | 恰好两个人一匹马，马四条腿、手有主人 | 多出人／马多腿：马场戏以后只拍人和马的局部 |")
md.append("| 7-04 | 人坐在马上；另一个人扶着笼头 | 莉莉坐在鞍上，手握缰绳 | 人和马融在一起：骑马戏要靠近景 |")
md.append("| 7-05 | 玛丽的手把针按在马屁股上（小物件＋动物反应） | 看得出她的手按在马的臀部、马耳朵向后压 | 看不出针：以后“暗害”类动作用表情和结果代替 |")
md.append("| 7-06 | 马人立＋人抱马脖子＋呼救 | 马后腿站起、莉莉抱着马脖子，呼救念完 | 马的后腿画乱：人立不要再拍 |")
md.append("| 7-07、8-01 | 固定机位下的狂奔（马从左往右跑）；人颠簸 | 马的腿看得过去、人没有被甩出画面 | 画面乱：狂奔戏用“马在原地前蹄刨地”代替 |")
md.append("| 7-08、7-09 | 单人表情变化＋手机变形（承接 07-08→09） | 他抬头盯向松树；手机变形 | 手机没变形：物体变形别写，用手背青筋和表情代替 |")
md.append("| 8-02、8-03 | 两人一马（后面的人环腰、勒缰绳）；承接前段 | 两人一马，手有主人，人立时人不被画散 | 两个人骑一匹马是否混在一起，是这批最大的风险 |")
md.append("| 8-04～8-06 | 近景贴身；台词在马背上 | 台词念完，没有多出的手 | 近景手乱：以后骑马的近景只拍脸 |")
md.append("| 8-07、8-08 | 捏下巴和吻（用侧面近景）；承接 07→08 | 两张脸侧面贴近，没有融合 | 脸融合：吻戏要用遮挡（侧脸＋头发）或用剪辑代替 |")
md.append("| 9-02～9-05 | 同一个姿势连拍 4 个任务（承接 01→05）；对话节奏 | 姿势和大衣的位置连得上 | 姿势跳：长对话要合成一个更长的任务，而不是 4 个短任务 |")
md.append("| 9-07 | 保罗单人怒吼；视线落在画面里的小路上 | 没有陌生人，嘴型和台词对得上 | 同第 3 集的结论 |")
md.append("| 10-01 | 两个同款保镖（一个素材画两个人） | 两个长得差不多的人、手有主人 | 一个素材只能画一个人：群像要多个素材 |")
md.append("| 10-03 | 双人抓领子（H3 的“抓人”写法：抓人者的肩、臂、手都在画面里）＋台词 | 手抓在领子上，没有多出的手，台词念完 | 抓领子失败：双人冲突以后用肩膀相对＋台词代替 |")
md.append("| 10-05～10-07 | 开场图里已经是“横抱”；承接 05→06→07 | 抱的姿势一致、手有主人；莉莉的头向后仰 | 横抱姿势乱：以后抱人只拍胸口以上 |")
md.append("| T1（B） | 单人大动作：翻过栏杆跳下 | 他翻过去了、没有变形 | 失败：跳跃不用，剧本里的“一跃而下”用结果镜头代替（现在就是这样） |")
md.append("| T2（B） | 双人大动作：单手提起一个人，脚离地 | 保罗的脚后跟离地、手有主人 | 失败：用“抓住领子＋台词”（10-03）就够了 |")
md.append("| T3（B） | 群像：五个人，其中四个同款 | 恰好五个人，保罗在中间 | 数不对／脸乱：群像以后一律拍两个人，其余用声音和影子代替 |")
md.append("| T4（B） | 双人大动作：把站着的人横抱起来 | 莉莉双脚离地、头靠在他肩上 | 失败：10-05 开场图里“已经抱着”的写法保留 |\n")
for k in ('7', '8', '9', '10', '10B'):
    md.append(f"## 四-{k}、{NAMES[k]}的任务\n")
    md.append(fmt_table(SEGS[k]))
    md.append("")
md.append("## 五、给 H3 的提示词（中文全译，一个字不漏）\n")
md.append("每个任务的视频提示词前面还会加这句固定的风格话：**“真人实拍，电影感，写实，皮肤有自然质感，浅景深，温暖奢华的光线，超宽 8:3 宽银幕画面。”** 开场图提示词前面也有固定的开头：**“一张来自写实真人浪漫惊悚片的完整首帧，超宽 8:3 宽银幕构图。皮肤自然，能看到毛孔，布料和材质真实。固定的场景参考图决定地点，人物肖像只决定被点名的人。”** 下面不再重复。\n")
md.append("新素材（场景 ranch、woods_edge；人物 killian_coat、lily_riding、mary_riding、trainer、bodyguard；马 black_horse）的图片提示词都在 JSON 里，换装人物都用 `ref` 指向原人物以保脸（莉莉＝lily，基利安＝killian，玛丽＝mary）。**驯马师、保镖没有参考脸；马是第一次。**\n")
for k in ('7', '8', '9', '10', '10B'):
    md.append(f"### {NAMES[k]}\n")
    md.append(fmt_prompts(SEGS[k], ZHS[k]))
md.append("## 六、我预计会出问题的地方（没试过，只是判断；按自查清单第 5 条逐项过）\n")
md.append("- **马本身（第一次）**：腿的数量、马头和身体的比例、缰绳有没有穿过手、鞍和人的接合处。看开场图时数腿。\n- **两个人骑一匹马（8-02 起）**：后面的人环腰的那只手会不会长到前面人身上；两个人会不会融成一个。这是我预计最容易整段作废的地方。\n- **人立（7-06、8-03）和狂奔（7-07、8-01）**：固定机位下马的运动幅度大，可能出画或变形；人颠簸时手会不会离开鬃毛。\n- **进出画／视线（自查清单第 1、3 条）**：没有“走出画面”的动作；视线目标都在画面里（栅栏、松树、马耳朵、对方的脸）。唯一有一点悬的是 9-07（保罗看着画面左边“土路的远处”，是画面里的东西，但可能被画成左边出现一个人）。\n- **表情（第 2 条）**：每个人物每个任务都写了。马上的人在晃动时可能还是被补成微笑，看 7-04、8-02。\n- **台词位置（第 4 条）**：有台词的任务都是 6 秒、≤6 个单词；仍然要听结尾（7-02、7-03、7-06、8-06、9-02、9-04、9-05、9-07、10-03、10-05、10-06、10-07）。9-04 与 9-05 连着两个任务都是耳边低语，中间会有大约 2–4 秒的无声接缝（开口晚的老问题）。\n- **承接前段的断点（第 7 条）**：承接只用在同两个人、同一匹马、同一景别的相邻任务（7-09、8-03、8-06、8-08、9-02～9-05、10-06、10-07）。8-07 没承接，因为景别从宽中景变成中近景。\n- **人数变化**：7-02（2 人）→7-03（2 人＋马）→7-04（2 人＋马）→7-05（2 人＋马，换了一个人）都不承接。\n- **名字读音（Q19）**：9-04 `Lily`、10-05 `Lily Swan`、10-07 `Lily!` 的人名在台词里；基利安的名字这批没有出现在台词里（保罗的 `Killian!` 我拿掉了），不测。\n- **亲密戏**：8-07、8-08、9-01 是“近距离、非露骨”的侧面近景，按美国平台惯例保持不露骨。\n- **台词里的“fiancé”**：9-07 的单词计数我按 6 个算；念不念得出法语音调是个小风险。\n")
md.append("## 七、开场图检查清单（马场专用，每张先看 10 秒）\n")
md.append("① 人数对不对（马不算人）② 马有没有四条腿、头和身体对不对 ③ 每只手都有主人、缰绳握在谁手里 ④ 人是不是在画面中间三分之一 ⑤ 有没有镜子／倒影 ⑥ 表情对不对（没有不想要的笑）⑦ 两个人骑一匹马时，后面的人在不在前面人的画面左边。\n")
md.append("## 八、和以前几集的区别（已按“Claude 易错点自查清单”）\n")
md.append("- 每个人物每个任务都写了表情（马不算）；没有“画外的人”；没有“走出画面”的动作。\n- 有台词的任务都是 6 秒、≤6 个单词；没有 5 秒任务放台词。\n- 承接前段只在同人同景别同地点；每集第一个任务一律不承接。\n- 剧本里的跳跃、提人、抱起、人群，正式版里都用“结果镜头”绕开，原样的放进 B。\n- 新素材：玛丽有 `ref` 保脸，驯马师、保镖没有；黑马第一次出现。\n")
open(os.path.join(FOLDER, '2026-10-10_第7-10集_合并_说明.md'), 'w', encoding='utf-8').write('\n'.join(md))
print('说明已写', n_tasks, '个任务', n_sec, '秒')
