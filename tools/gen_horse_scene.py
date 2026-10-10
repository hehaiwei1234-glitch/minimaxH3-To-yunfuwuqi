#!/usr/bin/env python3
"""马场一场“完整过程”重写测试稿（2026-10-10，hh 16:42 同意）。

目的：hh 看了总片，说镜头之间像变魔术（动作没做完、没交代就切到下一场）。
这份把剧本第 7–8 集那一场（买通 → 逼她上马 → 扎针 → 失控 → 基利安赶去 → 救下 → 吻）
写成有过程的版本：每一步都有起因、动作、反应、收尾，不再用“已经在马上／已经坐在地上”的结果镜头。
20 个镜头、110 秒。有 13 个直接复制马场合并稿里已有的任务（提示词一字不改），7 个是新写的。
素材／人物／style 以马场合并稿为底逐字复制（补拍包 2 没有新增素材），追加到补拍包 2 之后，插件里显示第 17 集。
种子 4801–4820（和库里所有稿子不重复）。
"""
import copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, silent, voiced

BASE = '合并稿/合并_第7-10集+10B_制作稿_追加.json'
OUT = '合并稿/马场一场_完整过程重写_制作稿_追加'
SRC = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))
EP = {e['title'].split('｜')[0]: e for e in SRC['episodes']}

a = Batch(BASE, SRC['title'], 4800)


def C(ep, n, title, dep):
    """复制马场合并稿里已有的任务（提示词不改），只换标题、种子、承接前段开关。"""
    s = copy.deepcopy(EP['剧本第%s集' % ep]['segments'][n - 1])
    a.seed += 1
    s['seed'] = a.seed
    s['title'] = title
    s['depends_on_previous'] = dep
    s['continuity'] = 'cut'
    a.tasks.append(s)
    return s


def N(dep, title, dur, chars, assets, refs, img, end, img_zh, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound):
    """新写的任务（img_zh 只是给人看的开场图中文，不进 JSON）。"""
    s = a.task(title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound)
    s['depends_on_previous'] = dep
    return s


RN = '[[asset:ranch]]'; WE = '[[asset:woods_edge]]'; KC = '[[asset:killian_coat]]'; LR = '[[asset:lily_riding]]'
MR = '[[asset:mary_riding]]'; TR = '[[asset:trainer]]'; HS = '[[asset:black_horse]]'

LAY_RN = " Fixed stage layout: the raised wooden grandstand is at frame-left; the white fence and the green field are at frame-right; dark pine trees line the far edge."
Z_RN = "固定布局：凸起的木制看台在画面左边；白色围栏和绿色跑马场在画面右边；远处边缘是一排深色松树。"
END_RN = " Bright midday sunlight, a clear blue sky, the ranch softly blurred behind."
Z_END_RN = "明亮的正午阳光，晴朗的蓝天，跑马场在后面柔和虚化。"
LAY_RIDE = (" Fixed stage layout: the open meadow with a dirt path is at frame-left; the rough wooden fence with sharp pointed posts and the dark pine forest are at frame-right."
            " Killian always sits behind Lily, at frame-left of her.")
Z_RIDE = "固定布局：开阔的草地和一条土路在画面左边；带尖桩的粗木栅栏和深色松林在画面右边。基利安始终坐在莉莉身后，在她的画面左边。"
END_WE = " Bright afternoon sunlight, a clear blue sky, the meadow softly blurred behind."
Z_END_WE = "明亮的午后阳光，晴朗的蓝天，草地在后面柔和虚化。"
GALLOP = ("Fast, pounding hoofbeats on dry earth and the creak of leather.", "急促沉重的马蹄声踏在干土上，和皮革马具的吱嘎声。")

# 01 看台上打电话（复制 7-01）
C(7, 1, '01｜看台上打电话', False)
# 02 玛丽买通驯马师（复制 7-02）
C(7, 2, '02｜玛丽买通驯马师', False)
# 03 驯马师牵马到莉莉面前（复制 7-03）
C(7, 3, '03｜驯马师牵马过来', False)

# 04 莉莉不敢（新）：单人＋马头入画，视线落在画面里的马眼上
N(False, '04｜莉莉不敢骑', 6, ['LilyRiding'], ('ranch', 'lily_riding', 'black_horse'), ['ranch'],
  "Side-on medium close-up, in the middle third of the frame, on the packed-earth track. Lily stands at frame-right from the head to the waist in profile facing frame-left, in the cream blouse and tan riding breeches, "
  "her hands clasped tight at her waist, her shoulders drawn in, her lips parted, her brows pulled together, her eyes wide on the black horse's eye. "
  "The head and neck of the tall jet-black horse fill the frame-left edge in profile facing frame-right, its ears pinned back, its nostrils flared. The frame holds exactly one person, Lily, and one black horse.",
  END_RN + LAY_RN,
  "侧面的中近景，在画面中间三分之一，在夯实的泥土跑道上。莉莉站在画面右边，头到腰，侧身朝画面左边，穿奶油色衬衫和棕黄色马裤，双手紧紧交握在腰前，肩膀缩着，嘴唇微张，眉头拧紧，睁大眼睛看着黑马的眼睛。"
  "高大的纯黑烈马的头和脖子占满画面左边缘，侧身朝画面右边，耳朵向后压平，鼻孔张大。画面里恰好一个人和一匹黑马：莉莉。" + Z_END_RN + Z_RN,
  "莉莉怕得往后缩，小声说这匹马太野了。", "0—6秒侧面中近景，镜头固定。",
  ('LilyRiding', "He looks too wild for me.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {RN}: {LR} in profile facing frame-left, her eyes on the black horse's eye at the frame-left edge. "
  f"She speaks in a thin, shaky voice and leans her shoulders back away from the horse, her hands clutching tighter at her waist, her brows pulling together. {HS} tosses its head, its ears pinned back. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是私人跑马场：莉莉侧身朝画面左边，眼睛看着画面左边缘黑马的眼睛。她用细细发颤的声音说话，肩膀向后缩着躲开那匹马，双手在腰前攥得更紧，眉头越拧越紧。黑马甩着头，耳朵向后压平。镜头固定不动。",
  voiced("A light breeze, the creak of leather and a horse stamping its hoof.", "轻轻的风声、皮革的吱嘎声和马蹄刨地声。"))

# 05 玛丽催驯马师（新）：双人，驯马师点头收尾
N(False, '05｜玛丽催驯马师', 6, ['MaryRiding', 'Trainer'], ('ranch', 'mary_riding', 'trainer'), ['ranch'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, standing close on the packed-earth track and facing each other in profile. "
  "Mary at frame-left in the ivory riding jacket and white riding breeches, facing frame-right, her arms loosely folded under her chest, her chin tilted up, a sweet coy smile, her eyes on Trainer's face. "
  "Trainer at frame-right in the worn brown leather vest and flat tweed cap, facing frame-left, his right hand tucking the thick brown envelope into the inside of his vest, his lips pressed together, his brows drawn together, his eyes on Mary's face. "
  "The frame holds exactly two people: Mary and Trainer.",
  END_RN + LAY_RN,
  "侧面的中景双人镜头，两个人都是头到膝盖，在画面中间三分之一，近近地站在夯实的泥土跑道上，侧身面对面。玛丽在画面左边，穿象牙色马术外套和白色马裤，侧身朝画面右边，双臂松松地抱在胸下，下巴抬起，露出甜甜的娇笑，眼睛看着驯马师的脸。"
  "驯马师在画面右边，穿磨旧的棕色皮背心，戴平顶花呢帽，侧身朝画面左边，右手把厚厚的棕色信封塞进背心里面，嘴唇抿紧，眉头皱着，眼睛看着玛丽的脸。画面里恰好两个人：玛丽和驯马师。" + Z_END_RN + Z_RN,
  "玛丽甜笑着吩咐驯马师扶莉莉上马；驯马师收好信封，点了一下头。", "0—6秒侧面中景，镜头固定。",
  ('MaryRiding', "Help her up, she's just shy.", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {RN}: {MR} at frame-left speaks in a sugary, coy voice with a sweet smile, her eyes on his face. "
  f"{TR} at frame-right finishes tucking the envelope into his vest, then gives one short nod and touches two fingers to the brim of his cap, his lips pressed together and his brows drawn together. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是私人跑马场：玛丽在画面左边用甜得发腻的、娇滴滴的声音说话，带着甜甜的笑，眼睛看着他的脸。驯马师在画面右边把信封塞好，然后短促地点了一下头，用两根手指碰了碰帽檐，嘴唇抿紧，眉头皱着。镜头固定不动。",
  voiced("A light breeze and distant birdsong.", "轻轻的风声和远处的鸟叫。"))

# 06 莉莉上马（新）：开场图里脚已经踩在马镫上、双手抓着马鞍
N(False, '06｜莉莉被迫上马', 5, ['LilyRiding'], ('ranch', 'lily_riding', 'black_horse'), ['ranch'],
  "Side-on wide shot, in the middle third of the frame, on the packed-earth track. The tall jet-black horse stands in profile facing frame-right. "
  "Lily stands on the ground at its left side, in profile facing frame-right, in the cream blouse and tan riding breeches, her left boot in the stirrup, her left knee bent, both hands gripping the saddle, "
  "her lips pressed tight, her brows drawn together, her eyes lowered on the saddle. The frame holds exactly one person, Lily, and one black horse.",
  END_RN + LAY_RN,
  "侧面的宽景镜头，在画面中间三分之一，在夯实的泥土跑道上。高大的纯黑烈马站着，侧身朝画面右边。莉莉站在地上、马的左侧，侧身朝画面右边，穿奶油色衬衫和棕黄色马裤，左脚已经踩进马镫，左膝弯曲，双手抓着马鞍，"
  "嘴唇抿紧，眉头皱着，眼睛垂着看着马鞍。画面里恰好一个人和一匹黑马：莉莉。" + Z_END_RN + Z_RN,
  "莉莉咬着牙，抓着马鞍把自己撑上马背。", "0—5秒侧面宽景，镜头固定。", None,
  f"A steady side-on wide shot opens from the adopted first frame in {RN}: {LR} pulls herself up with both hands on the saddle, her left leg straightening in the stirrup, swings her right leg over the horse's back and drops into the saddle, her hands sliding to the reins. "
  f"Her lips press tight and her eyes widen on the horse's ears. {HS} shifts its weight. The camera holds still.",
  "一个稳定的侧面宽景，从已采用的开场图继续，场景是私人跑马场：莉莉双手抓着马鞍把自己撑起来，左腿在马镫里蹬直，右腿跨过马背，落坐在马鞍上，双手滑向缰绳。她嘴唇抿紧，眼睛睁大看着马耳朵。黑马挪了挪重心。镜头固定不动。",
  silent("A light breeze, the creak of leather and a horse stamping its hoof.", "轻轻的风声、皮革的吱嘎声和马蹄刨地声。"))

# 07 莉莉坐在马上发抖（新）：单人，上一镜的结尾姿势
N(True, '07｜莉莉坐在马上发抖', 5, ['LilyRiding'], ('ranch', 'lily_riding', 'black_horse'), ['ranch'],
  "Side-on wide shot, in the middle third of the frame, on the packed-earth track. The tall jet-black horse stands in profile facing frame-right. "
  "Lily sits in the saddle on its back in profile facing frame-right, in the cream blouse and tan riding breeches, both hands gripping the reins at the horse's neck, her back rigid, her lower lip caught between her teeth, her brows drawn together, her eyes wide on the horse's ears. "
  "The frame holds exactly one person, Lily, and one black horse.",
  END_RN + LAY_RN,
  "侧面的宽景镜头，在画面中间三分之一，在夯实的泥土跑道上。高大的纯黑烈马站着，侧身朝画面右边。莉莉坐在马背的鞍上，侧身朝画面右边，穿奶油色衬衫和棕黄色马裤，双手握着马脖子上的缰绳，背挺得僵直，下嘴唇被牙齿咬住，眉头皱着，睁大眼睛看着马耳朵。"
  "画面里恰好一个人和一匹黑马：莉莉。" + Z_END_RN + Z_RN,
  "莉莉坐在马背上，双手死死抓着缰绳，咬着嘴唇发抖。", "0—5秒侧面宽景，镜头固定。", None,
  f"A steady side-on wide shot opens from the adopted first frame in {RN}: {LR} sits in the saddle of {HS}, both hands tight on the reins, her lower lip trembling. "
  f"She draws one shaky breath and her grip tightens, her eyes on the horse's ears. The horse tosses its head and stamps one hoof. The camera holds still.",
  "一个稳定的侧面宽景，从已采用的开场图继续，场景是私人跑马场：莉莉坐在黑马的鞍上，双手紧握缰绳，下嘴唇发抖。她抖着吸了一口气，手攥得更紧，眼睛看着马耳朵。马甩了甩头，刨了一下蹄子。镜头固定不动。",
  silent("A light breeze, the creak of leather and a horse stamping its hoof.", "轻轻的风声、皮革的吱嘎声和马蹄刨地声。"))

# 08 玛丽下针（新）：单人＋马臀，不把莉莉放进画面（避免两个白衣女人同框）
N(False, '08｜玛丽把针扎进马屁股', 5, ['MaryRiding'], ('ranch', 'mary_riding', 'black_horse'), ['ranch'],
  "Side-on medium shot, in the middle third of the frame, on the packed-earth track. Mary stands at frame-left from the head to the knees in profile facing frame-right, in the ivory riding jacket and white riding breeches, "
  "her right hand holding a thin silver needle between her thumb and forefinger a hand's width from the glossy black rump of the horse at frame-right, her chin tilted up, a sweet coy smile, her eyes lowered on the needle. "
  "The frame ends at the back edge of the saddle and holds only the hindquarters and tail of a tall jet-black horse at frame-right. The frame holds exactly one person, Mary, and the rear half of one black horse.",
  END_RN + LAY_RN,
  "侧面的中景，在画面中间三分之一，在夯实的泥土跑道上。玛丽站在画面左边，头到膝盖，侧身朝画面右边，穿象牙色马术外套和白色马裤，"
  "右手的拇指和食指捏着一根细银针，停在画面右边那匹黑马油亮的臀部前一只手掌宽的地方，下巴抬起，露出甜甜的娇笑，眼睛垂着看着针。"
  "画面到马鞍后缘为止，画面右边只有一匹高大纯黑烈马的后半身和尾巴。画面里恰好一个人和半匹黑马：玛丽。" + Z_END_RN + Z_RN,
  "玛丽甜笑着，把一根细银针扎进黑马的屁股；马的臀部一抽，尾巴甩起。", "0—5秒侧面中景，镜头固定。", None,
  f"A steady side-on medium shot opens from the adopted first frame in {RN}: {MR} presses the thin silver needle into the rump of {HS} with her right hand, her sweet coy smile widening and her eyes on the needle. "
  f"The horse's hindquarters flinch and its tail whips up. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是私人跑马场：玛丽用右手把细银针扎进黑马的臀部，甜甜的娇笑笑得更开，眼睛看着针。马的臀部一抽，尾巴甩了起来。镜头固定不动。",
  silent("A sharp stamp of hooves and the creak of leather.", "一声尖锐的蹄子跺地声和皮革的吱嘎声。"))

# 09 马人立（复制 7-06）、10 狂奔（复制 7-07）、11 基利安猛抬头（复制 7-08）、12 捏碎手机（复制 7-09）
C(7, 6, '09｜马人立而起', False)
C(7, 7, '10｜黑马狂奔', False)
C(7, 8, '11｜基利安猛抬头', False)
C(7, 9, '12｜捏碎手机', True)

# 13 基利安翻栏杆冲出去（新）：开场图是 12 的姿势（拉远），出画方向和结尾空镜都写明
N(False, '13｜基利安翻过栏杆冲出去', 5, ['KillianCoat'], ('ranch', 'killian_coat'), ['ranch'],
  "Wide shot, in the middle third of the frame. Killian stands alone at the railing of the raised wooden grandstand at frame-left in profile facing frame-right, in the long charcoal overcoat over a black shirt, "
  "his right hand gripping the top of the railing, the cracked gold phone in his left hand, his body leaning forward, his jaw clenched hard, his lips pulled back from his teeth, his eyes narrowed on the dark pine trees at frame-right. "
  "The frame holds exactly one person, Killian.",
  END_RN + LAY_RN,
  "宽景镜头，在画面中间三分之一。基利安一个人站在画面左边凸起的木制看台的栏杆边，侧身朝画面右边，穿长款炭灰色呢大衣、里面是黑衬衫，"
  "右手抓着栏杆顶，左手握着裂开的金色手机，身体前倾，下颌咬紧，嘴唇咧开露出牙齿，眯着眼睛盯着画面右边的深色松树。画面里恰好一个人：基利安。" + Z_END_RN + Z_RN,
  "基利安扔下手机，翻过栏杆，朝右边狂奔出画。", "0—5秒侧面宽景，镜头固定。", None,
  f"A steady side-on wide shot opens from the adopted first frame in {RN}: {KC} drops the broken phone, vaults over the railing in one motion, lands on the packed-earth track and sprints toward frame-right along the white fence, his overcoat flaring behind him, his jaw clenched hard and his lips pulled back from his teeth, and runs out of the frame at the right edge. "
  "In the last second the frame holds only the empty track, the white fence and the green field. The camera holds still.",
  "一个稳定的侧面宽景，从已采用的开场图继续，场景是私人跑马场：基利安扔下坏掉的手机，一下翻过栏杆，落在夯实的泥土跑道上，沿着白色围栏朝画面右边冲刺，大衣在身后翻飞，下颌咬紧，嘴唇咧开露出牙齿，从画面右边缘跑出画。最后一秒画面里只剩空的跑道、白色围栏和绿色的跑马场。镜头固定不动。",
  silent("Boots hitting the packed earth fast, then fading, and a light breeze.", "靴子飞快踏在夯实的泥土上，然后渐渐远去，和轻轻的风声。"))

# 14 莉莉快被甩下马（复制 8-01）
C(8, 1, '14｜莉莉快被甩下马', False)

# 15 基利安翻身上马（新）：开场图里他已经跑到马旁、手抓着马鞍后缘
N(False, '15｜基利安翻身上马', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  "Side-on wide-medium shot, the whole horse and both people, in the middle third of the frame, on the dirt path along the meadow. The tall jet-black horse is in profile facing frame-right in a full gallop, all four hooves off the ground, dust flying. "
  "Lily sits in the saddle low over its neck, in the cream blouse and tan riding breeches, both hands tangled in the black mane, her mouth open, her eyes wide on Killian. "
  "Killian runs at full speed on the ground beside the horse's flank, at frame-left of Lily, in the long charcoal overcoat flaring behind him, his right hand gripping the back edge of the saddle, his body stretched low, his jaw set, his lips pressed together, his eyes on Lily's face. "
  "The frame holds exactly two people, Killian and Lily, and one black horse.",
  END_WE + LAY_RIDE,
  "侧面的宽中景，整匹马和两个人都在画面里，在画面中间三分之一，在草地边的土路上。高大的纯黑烈马侧身朝画面右边全速狂奔，四蹄腾空，尘土飞扬。"
  "莉莉坐在鞍上、伏得很低，穿奶油色衬衫和棕黄色马裤，双手缠在黑色鬃毛里，嘴巴张着，睁大眼睛看着基利安。"
  "基利安在地上全速跑在马身旁、莉莉的画面左边，长款炭灰色呢大衣在身后翻飞，右手抓着马鞍后缘，身体伸得很低，下颌绷紧，嘴唇抿紧，眼睛看着莉莉的脸。画面里恰好两个人和一匹黑马：基利安和莉莉。" + Z_END_WE + Z_RIDE,
  "基利安追上狂奔的黑马，抓着马鞍翻身坐到莉莉身后，一臂搂住她的腰。", "0—6秒侧面宽中景，镜头固定。", None,
  f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {KC} pushes off the ground with his right foot, pulls himself up by the back edge of the saddle and swings his right leg over the horse's back, landing in the saddle behind {LR}. "
  "His right arm closes around her waist and his left hand takes the reins at the horse's neck, his jaw set and his eyes on her face. She jerks and looks back at him, her eyes wide. The horse gallops on without slowing. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是树林边缘：基利安右脚蹬地，抓着马鞍后缘把自己拉上去，右腿跨过马背，落坐在莉莉身后。他的右臂环住她的腰，左手接过马脖子上的缰绳，下颌绷紧，眼睛看着她的脸。她猛地一颤，回头看着他，睁大了眼睛。黑马没有减速，继续狂奔。镜头固定不动。",
  silent(*GALLOP))

# 16 勒缰绳马人立（复制 8-03）、17 马被逼停（复制 8-05）、18 如果我晚来一秒（复制 8-06）、19 捏下巴（复制 8-07）、20 吻（复制 8-08）
C(8, 3, '16｜勒缰绳马人立', True)
C(8, 5, '17｜马被逼停', False)
C(8, 6, '18｜如果我晚来一秒', True)
C(8, 7, '19｜捏住下巴扳过脸', False)
C(8, 8, '20｜吻', True)

a.finish('剧本第7–8集｜马场完整过程（重写测试）',
         '把“买通驯马师→逼莉莉上马→扎针→失控→基利安赶去→救下→吻”写成有过程的一场：每一步都有起因、动作、反应、收尾，不再用“已经在马上”的结果镜头。',
         OUT)
