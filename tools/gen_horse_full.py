#!/usr/bin/env python3
"""马场四集（剧本第 7–10 集）场景级改编版（2026-10-11，hh 09:47 说“你没为剧本内容费半点心”之后重做）。

做法：不再“一句剧本一个镜头”，而是先问“观众必须看懂哪几件事、每件事由哪个镜头传达、上一镜头为什么引出下一镜头”，
再写镜头。原剧本是大纲，有 10 个逻辑缺口，这里补成镜头：
  1 莉莉为什么肯骑一匹吓人的马 → 玛丽当众激她，莉莉点头
  2 谁动了手脚、谁知道 → 观众亲眼看到玛丽扎针、马的反应、玛丽得意（只有观众和玛丽知道）
  3 驯马师是不是同谋 → 他收钱、牵马、松手后退时低头
  4 基利安怎么知道出事 → 听到喊声：猛抬头→捏碎手机→翻栏杆冲出（原剧本直接“一跃而下”）
  5 “晚一秒就死”凭什么成立 → 先拍尖桩栅栏的特写，再拍莉莉被甩向栅栏
  6 他怎么追上马 → 冲刺（在途）→ 翻身上马（过程）→ 勒缰绳人立→ 马停
  7 保罗为什么出现 → 他在林边一路喊着找她，再撞见他们
  8 “一块钱买下婚约”没有铺垫 → 第 7 集开头基利安电话里先说“把他们的股份全买下”
  9 莉莉听到婚约被买走没有反应 → 补她的反应镜头
 10 玛丽整段没有后果 → 她的得意在基利安冲出去时僵住（后续处罚留给之后的集）
方向统一：骑马、追赶、保罗出现的方向都是“马朝画面右边，保罗从右边来、朝左边走”，不需要把马掉头。
49 个任务、约 216 秒；其中 11 个是复制已有任务（文字一字不改，只换标题、种子、承接开关，个别改时长），其余 38 个全部新写。
素材／人物／style 以马场合并稿为底逐字复制，没有新增素材。种子 5001–5312（和库里所有稿子不重复）。
"""
import copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, breathy, voiced

BASE = '合并稿/旧合并稿/合并_第7-10集+10B_制作稿_追加.json'
OUT = '合并稿/旧合并稿/马场四集_场景级改编_制作稿_追加'
SRC = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))
EP = {e['title'].split('｜')[0]: e for e in SRC['episodes']}
REWRITE = json.load(open(os.path.join(FOLDER, '合并稿/旧合并稿/马场一场_完整过程重写_制作稿_追加.json'), encoding='utf-8'))['episodes'][0]['segments']
DUR = json.load(open(os.path.join(FOLDER, '合并稿/旧合并稿/时长测试_奔跑_人立_上马_制作稿_追加.json'), encoding='utf-8'))['episodes'][0]['segments']
SEAM = json.load(open(os.path.join(FOLDER, '合并稿/旧合并稿/接缝补镜头测试_制作稿_追加.json'), encoding='utf-8'))['episodes'][0]['segments']

b7, b8, b9, b10 = (Batch(BASE, SRC['title'], s) for s in (5000, 5100, 5200, 5300))

RN = '[[asset:ranch]]'; WE = '[[asset:woods_edge]]'; KC = '[[asset:killian_coat]]'; LR = '[[asset:lily_riding]]'
MR = '[[asset:mary_riding]]'; TR = '[[asset:trainer]]'; HS = '[[asset:black_horse]]'; PL = '[[asset:paul]]'; BG = '[[asset:bodyguard]]'

LAY_RN = " Fixed stage layout: the raised wooden grandstand is at frame-left; the white fence and the green field are at frame-right; dark pine trees line the far edge."
END_RN = " Bright midday sunlight, a clear blue sky, the ranch softly blurred behind."
LAY_RIDE = (" Fixed stage layout: the open meadow with a dirt path is at frame-left; the rough wooden fence with sharp pointed posts and the dark pine forest are at frame-right."
            " Killian always sits behind Lily, at frame-left of her.")
LAY_WE = " Fixed stage layout: the open meadow with a dirt path is at frame-left; the rough wooden fence with sharp pointed posts and the dark pine forest are at frame-right."
END_WE = " Bright afternoon sunlight, a clear blue sky, the meadow softly blurred behind."
GALLOP = ("Fast, pounding hoofbeats on dry earth and the creak of leather.", "急促沉重的马蹄声踏在干土上，和皮革马具的吱嘎声。")


def T(b, title, dur, chars, assets, refs, img, end, vis_zh, dlg, act_en, act_zh, sound, dep=False):
    """新写的任务。镜头固定；vis_zh 是一句话中文摘要，act_zh 是镜头文字的中文。"""
    s = b.task(title, dur, chars, assets, refs, img, end, vis_zh, '0—%d秒，镜头固定。' % dur, dlg, act_en, act_zh, sound)
    s['depends_on_previous'] = dep
    return s


def C(b, src, title, dep=False, dur=None, sound=None):
    """复制已有任务（文字一字不改），只换标题、种子、承接开关；可改时长和声音句。"""
    s = copy.deepcopy(src)
    b.seed += 1
    s['seed'] = b.seed
    s['title'] = title
    s['depends_on_previous'] = dep
    s['continuity'] = 'cut'
    if dur:
        s['duration_seconds'] = dur; s['generation_seconds'] = dur
        for sh in s['shots']:
            sh['end_seconds'] = dur
    if sound:
        s['sound_en'], s['sound_zh'] = sound
    b.tasks.append(s)
    return s


def episode(b, title, summary):
    lines = []
    for t in b.tasks:
        lines.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
        for x in t['dialogue']:
            lines.append(f"{x['speaker']}：“{x['text']}”")
    return {'title': title, 'summary': summary, 'script': '\n'.join(lines), 'segments': b.tasks, 'dialogue_language': 'en'}


# ===================================================================== 第 7 集：致命危机
# 观众要看懂：① 基利安远在看台上谈生意，说一不二（电话里一句伏笔：买下他们的股份）② 玛丽恨莉莉，花钱买通驯马师
# ③ 马明显很野 ④ 莉莉怕，被玛丽当众激将，点头 ⑤ 她上马，驯马师松手 ⑥ 观众亲眼看到玛丽扎针 ⑦ 马发狂 ⑧ 莉莉喊救命
# ⑨ 玛丽得意 ⑩ 基利安听到→脸色变→捏碎手机→冲出去 ⑪ 玛丽的笑僵住

T(b7, '01｜基利安在看台上谈生意', 6, ['KillianCoat'], ('ranch', 'killian_coat'), ['ranch'],
  "Medium shot of Killian alone, from the head to the waist, in profile facing frame-right, in the middle third of the frame, at the railing of the raised wooden grandstand at frame-left, in the long charcoal overcoat over a black shirt, "
  "the gold smartphone held at his right ear, his left hand resting on the top rail, his jaw set, his lips flat, his eyes on the green field at frame-right. The frame holds exactly one person, Killian.",
  END_RN + LAY_RN, "基利安一个人站在看台栏杆边打电话，低声下令。",
  ('KillianCoat', "Buy every share they own.", 1.0),
  f"A steady medium shot opens from the adopted first frame in {RN}: {KC} speaks into the gold phone in a low, flat, commanding voice, his jaw set and his lips barely moving, his eyes on the green field at frame-right. His left forefinger taps once on the railing. The camera holds still.",
  "一个稳定的中景，从已采用的开场图继续，场景是私人跑马场：基利安用低沉平板、不容反驳的声音对着金色手机说话，下颌绷紧，嘴唇几乎不动，眼睛看着画面右边的绿色跑马场。他的左手食指在栏杆上敲了一下。镜头固定不动。",
  voiced("A light breeze, distant voices and the creak of the wooden railing.", "轻轻的风声、远处的人声和木栏杆的吱嘎声。"))

T(b7, '02｜玛丽把信封塞给驯马师', 6, ['MaryRiding', 'Trainer'], ('ranch', 'mary_riding', 'trainer'), ['ranch'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, standing close on the packed-earth track and facing each other in profile. "
  "Mary at frame-left in the ivory riding jacket and white riding breeches, facing frame-right, holding out a thick brown envelope in her right hand at waist height, a sweet coy smile, her chin tilted up, her eyes on Trainer's face. "
  "Trainer at frame-right in a worn brown leather vest and a flat tweed cap, facing frame-left, his right hand reaching for the envelope, his lips pressed together, his brows drawn together, his eyes lowered on the envelope. "
  "The frame holds exactly two people: Mary and Trainer.",
  END_RN + LAY_RN, "玛丽甜笑着把厚信封塞给驯马师，吩咐他给莉莉最野的那匹马；驯马师收下，皱着眉。",
  ('MaryRiding', "Give her the wildest one.", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {RN}: {MR} at frame-left presses the thick envelope into {TR}'s hand and speaks in a sugary, hushed voice, her sweet coy smile widening and her eyes on his face. "
  f"{TR} at frame-right takes the envelope and tucks it inside his vest, his lips pressed together, his brows drawn together and his eyes lowered on the envelope. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是私人跑马场：画面左边的玛丽把厚信封塞进驯马师手里，用甜得发腻的压低声音说话，甜甜的娇笑笑得更开，眼睛看着他的脸。画面右边的驯马师接过信封塞进背心里，嘴唇抿紧，眉头皱着，眼睛垂着看信封。镜头固定不动。",
  voiced("A light breeze and distant birdsong.", "轻轻的风声和远处的鸟叫。"))

T(b7, '03｜驯马师牵着黑马走到莉莉面前', 6, ['Trainer', 'LilyRiding'], ('ranch', 'trainer', 'lily_riding', 'black_horse'), ['ranch'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, on the packed-earth track. "
  "Lily at frame-left in the cream blouse and tan riding breeches, facing frame-right, her hands clasped at her waist, her lips parted, her brows pulled up, her eyes wide on the black horse's head at frame-right. "
  "Trainer in the middle in the worn brown leather vest and flat tweed cap, facing frame-left, holding a leather lead rope in his right hand, his lips pressed into a thin line, his brows drawn together, his eyes lowered on the rope. "
  "At the frame-right edge the head and neck of the tall jet-black horse in profile facing frame-left, its head thrown up, its ears pinned back, its nostrils flared, the lead rope running from its halter to Trainer's hand. "
  "The frame holds exactly two people: Lily and Trainer, and one black horse.",
  END_RN + LAY_RN, "驯马师把一匹明显很野的黑马牵到莉莉面前，说这匹是给她的；莉莉往后退了半步。",
  ('Trainer', "This one's for you, Miss.", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {RN}: {TR} holds the lead rope out toward Lily and speaks in a flat, stiff voice, his lips pressed into a thin line and his eyes lowered on the rope. "
  f"{LR} looks up at the horse and takes half a step back, her lips parting and her brows pulling up, her hands tightening at her waist. {HS} tosses its head and stamps one hoof, its ears pinned back. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是私人跑马场：驯马师把牵马绳递向莉莉，用平板僵硬的声音说话，嘴唇抿成细线，眼睛垂着看绳子。莉莉抬头看着那匹马，往后退了半步，嘴唇微张，眉头抬起，双手在腰前攥紧。黑马甩着头、刨了一下蹄子，耳朵向后压平。镜头固定不动。",
  voiced("A light breeze, a horse snorting and the creak of leather.", "轻轻的风声、马的喷鼻声和皮革的吱嘎声。"))

# 04 莉莉不敢（复制重写测试里的 04：莉莉说“He looks too wild for me.”）
C(b7, REWRITE[3], '04｜莉莉不敢骑')

T(b7, '05｜玛丽当众激莉莉，莉莉点头', 6, ['MaryRiding', 'LilyRiding'], ('ranch', 'mary_riding', 'lily_riding'), ['ranch'],
  "Side-on medium two-shot, both women from the head to the waist, in the middle third of the frame, facing each other in profile on the packed-earth track. "
  "Mary at frame-left in the ivory riding jacket, facing frame-right, her arms loosely folded, her chin tilted up, a sweet coy smile, her eyes on Lily's face. "
  "Lily at frame-right in the cream blouse, facing frame-left, her hands clasped tight at her chest, her lips pressed together, her brows pulled up, her eyes lowered. "
  "The frame holds exactly two people: Mary and Lily.",
  END_RN + LAY_RN, "玛丽当着众人的面激莉莉，莉莉咬住嘴唇，抬头点了一下头。",
  ('MaryRiding', "Everyone's watching, so don't be shy.", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {RN}: {MR} at frame-left speaks in a sugary, mocking voice, her sweet coy smile widening, her chin tilting higher and her eyes on Lily's face. "
  f"{LR} at frame-right flinches, her lips pressing tight and her brows pulling together; she draws one breath, her jaw tightening, lifts her eyes to Mary's face and gives one small nod. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是私人跑马场：画面左边的玛丽用甜腻嘲弄的声音说话，甜甜的娇笑笑得更开，下巴抬得更高，眼睛看着莉莉的脸。画面右边的莉莉缩了一下，嘴唇抿紧，眉头拧起；她吸了一口气，下颌绷紧，抬眼看着玛丽的脸，轻轻点了一下头。镜头固定不动。",
  voiced("A light breeze and a few guests chuckling softly in the distance.", "轻轻的风声，和远处几位宾客压低的轻笑声。"))

T(b7, '06｜莉莉被迫上马', 3, ['LilyRiding', 'Trainer'], ('ranch', 'lily_riding', 'trainer', 'black_horse'), ['ranch'],
  "Side-on wide shot, in the middle third of the frame, on the packed-earth track. The tall jet-black horse stands in profile facing frame-right. "
  "Lily stands on the ground at its left side, in profile facing frame-right, in the cream blouse and tan riding breeches, her left boot in the stirrup, her left knee bent, both hands gripping the saddle, her lips pressed tight, her brows drawn together, her eyes lowered on the saddle. "
  "Trainer stands at the horse's head at frame-right in the worn brown leather vest and flat tweed cap, his right hand holding the bridle, his lips pressed together, his brows drawn together, his eyes on the horse's eye. "
  "The frame holds exactly two people: Lily and Trainer, and one black horse.",
  END_RN + LAY_RN, "莉莉咬着牙抓着马鞍撑上马背，驯马师扶着马头。",
  None,
  f"A steady side-on wide shot opens from the adopted first frame in {RN}: {LR} pulls herself up with both hands on the saddle, her left leg straightening in the stirrup, swings her right leg over the horse's back and drops into the saddle, her hands sliding to the reins, her lips pressing tight and her eyes widening on the horse's ears. "
  f"{TR} keeps hold of the bridle, his lips pressed together and his brows drawn together. {HS} shifts its weight. The camera holds still.",
  "一个稳定的侧面宽景，从已采用的开场图继续，场景是私人跑马场：莉莉双手抓着马鞍把自己撑起来，左腿在马镫里蹬直，右腿跨过马背落坐在鞍上，双手滑向缰绳，嘴唇抿紧，眼睛睁大看着马耳朵。驯马师一直抓着马笼头，嘴唇抿紧，眉头皱着。黑马挪了挪重心。镜头固定不动。",
  breathy("A light breeze, the creak of leather and a horse stamping its hoof.", "轻轻的风声、皮革的吱嘎声和马蹄刨地声。"))

T(b7, '07｜驯马师松手后退，莉莉发抖', 4, ['LilyRiding', 'Trainer'], ('ranch', 'lily_riding', 'trainer', 'black_horse'), ['ranch'],
  "Side-on wide shot, in the middle third of the frame, on the packed-earth track. The tall jet-black horse stands in profile facing frame-right. "
  "Lily sits in the saddle on its back in profile facing frame-right, in the cream blouse and tan riding breeches, both hands gripping the reins, her back rigid, her lower lip caught between her teeth, her brows drawn together, her eyes wide on the horse's ears. "
  "Trainer stands at the horse's head at frame-right in the worn brown leather vest and flat tweed cap, his right hand holding the bridle, his lips pressed together, his brows drawn together, his eyes lowered. "
  "The frame holds exactly two people: Lily and Trainer, and one black horse.",
  END_RN + LAY_RN, "驯马师松开马笼头、低着头后退；马甩头刨蹄，莉莉抖着抓紧缰绳。",
  None,
  f"A steady side-on wide shot opens from the adopted first frame in {RN}: {TR} lets go of the bridle and takes two quick steps back, his lips pressed together, his brows drawn together and his eyes lowered. "
  f"{HS} tosses its head and stamps one hoof. {LR} draws one shaky breath, her lower lip trembling, her brows pulling together and her hands tightening on the reins. The camera holds still.",
  "一个稳定的侧面宽景，从已采用的开场图继续，场景是私人跑马场：驯马师松开马笼头快步退了两步，嘴唇抿紧，眉头皱着，眼睛垂着。黑马甩着头、刨了一下蹄子。莉莉抖着吸了一口气，下嘴唇发颤，眉头拧起，双手把缰绳攥得更紧。镜头固定不动。",
  breathy("A light breeze, the creak of leather and a horse stamping its hoof.", "轻轻的风声、皮革的吱嘎声和马蹄刨地声。"))

# 08 玛丽把针扎进马屁股（复制重写测试 08，改成 4 秒，声音改新写法）
C(b7, REWRITE[7], '08｜玛丽把针扎进马屁股', dur=4,
  sound=breathy("A sharp stamp of hooves and the creak of leather.", "一声尖锐的蹄子跺地声和皮革的吱嘎声。"))
# 09 马被扎后抽腿、玛丽退开（复制接缝补镜头 补1）
C(b7, SEAM[0], '09｜马被扎后抽腿，玛丽退开')
# 10 莉莉在鞍上被吓到（复制接缝补镜头 补2）
C(b7, SEAM[1], '10｜莉莉在鞍上被吓到')
# 11 马人立 2 秒：开场图是四蹄着地（复制时长测试 马人立2秒）
C(b7, DUR[3], '11｜马人立再落地')
# 12 狂奔 3 秒（复制时长测试 奔跑3秒，文字与旧 7-07 相同）
C(b7, DUR[1], '12｜黑马狂奔')

T(b7, '13｜莉莉在奔马上尖叫求救', 6, ['LilyRiding'], ('ranch', 'lily_riding', 'black_horse'), ['ranch'],
  "Side-on close-up of Lily alone, from the head to the shoulders, in profile facing frame-right, in the middle third of the frame, low over the neck of the galloping horse, her hair streaming back, both hands tangled in the black mane at the frame-right edge, "
  "her mouth open in a scream, her brows pulled up, her eyes wide and wet with tears. Dark pine trees and a white fence streak past behind her. The frame holds exactly one person, Lily.",
  END_RN + LAY_RN, "莉莉伏在狂奔的马背上，用尽力气喊救命。",
  ('LilyRiding', "Help! Somebody help me!", 1.0),
  f"A steady side-on close-up opens from the adopted first frame in {RN}: {LR} screams for help, her mouth wide open, her brows pulled up and tears streaming back across her cheeks, her hair whipping behind her. The black mane lashes at the frame-right edge. The camera holds still.",
  "一个稳定的侧面特写，从已采用的开场图继续，场景是私人跑马场：莉莉大声呼救，嘴张得很大，眉头高高抬起，眼泪被风吹得向后淌过脸颊，头发在身后狂甩。黑色的马鬃在画面右边缘抽打。镜头固定不动。",
  voiced("Fast, pounding hoofbeats and a rush of wind.", "急促沉重的马蹄声和呼啸的风声。"))

# 14 玛丽看着，得意（复制接缝补镜头 补3）
C(b7, SEAM[2], '14｜玛丽退到看台边看着')
# 15 基利安听到→猛抬头、脸色变、放下电话（复制接缝补镜头 补4）
C(b7, SEAM[3], '15｜基利安猛抬头放下电话')

T(b7, '16｜基利安捏碎手机', 3, ['KillianCoat'], ('ranch', 'killian_coat'), ['ranch'],
  "Medium close-up of Killian alone, from the head to the chest, in profile facing frame-right, in the middle third of the frame, at the grandstand railing in the long charcoal overcoat over a black shirt, "
  "his right fist closed around the gold smartphone at chest height, his jaw clenched, his lips pulled back from his teeth, his eyes narrowed on the dark pine trees at frame-right. The frame holds exactly one person, Killian.",
  END_RN + LAY_RN, "基利安的拳头攥紧，金色手机被捏得变形裂开，眼里闪过金光，他松手让手机掉下去。",
  None,
  f"A steady medium close-up opens from the adopted first frame in {RN}: {KC}'s fist tightens until the gold casing bends and cracks and the glass splinters, his jaw clenching harder and his eyes flaring with a dark-gold glint. "
  "He opens his hand and the ruined phone drops to the boards. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是私人跑马场：基利安的拳头越攥越紧，金色的机身弯曲开裂、玻璃碎开，下颌咬得更紧，眼睛里闪过暗金色的光。他松开手，坏掉的手机掉在木板上。镜头固定不动。",
  breathy("A sharp crack of bending metal and glass.", "金属弯曲和玻璃碎裂的一声脆响。"), dep=True)

T(b7, '17｜基利安翻过栏杆冲出去', 4, ['KillianCoat'], ('ranch', 'killian_coat'), ['ranch'],
  "Wide shot, in the middle third of the frame. Killian stands alone at the railing of the raised wooden grandstand at frame-left in profile facing frame-right, in the long charcoal overcoat over a black shirt, "
  "his right hand gripping the top of the railing, his body leaning forward, his jaw clenched hard, his lips pulled back from his teeth, his eyes narrowed on the dark pine trees at frame-right. The frame holds exactly one person, Killian.",
  END_RN + LAY_RN, "基利安翻过栏杆，朝画面右边冲过跑马场，越跑越小。",
  None,
  f"A steady side-on wide shot opens from the adopted first frame in {RN}: {KC} vaults over the railing in one motion, lands on the packed-earth track and sprints toward frame-right along the white fence, his overcoat flaring behind him, his jaw clenched hard and his lips pulled back from his teeth, "
  "dust kicking up from every stride, growing smaller as he crosses the field. The camera holds still.",
  "一个稳定的侧面宽景，从已采用的开场图继续，场景是私人跑马场：基利安一下翻过栏杆，落在夯实的泥土跑道上，沿着白色围栏朝画面右边冲刺，大衣在身后翻飞，下颌咬紧，嘴唇咧开露出牙齿，每一步都踢起尘土，穿过跑马场时越跑越小。镜头固定不动。",
  breathy("Boots hitting the packed earth fast, then fading, and a light breeze.", "靴子飞快踏在夯实的泥土上，然后渐渐远去，和轻轻的风声。"))

T(b7, '18｜玛丽的笑僵住', 3, ['MaryRiding'], ('ranch', 'mary_riding'), ['ranch'],
  "Side-on medium close-up of Mary alone, from the head to the waist, in profile facing frame-right, in the middle third of the frame, at the foot of the raised wooden grandstand stairs at frame-left, in the ivory riding jacket, "
  "a smug smile, her chin lifted, her eyes on the green field at frame-right, her left hand resting on the stair railing. The frame holds exactly one person, Mary.",
  END_RN + LAY_RN, "玛丽看见基利安冲过来，得意的笑慢慢褪掉，往后退了一步。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {RN}: {MR}'s smug smile drains away, her lips parting, her brows pulling up and her eyes widening on the green field at frame-right. "
  "She takes one step back and presses her right hand against her chest, her jaw trembling. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是私人跑马场：玛丽得意的笑慢慢褪掉，嘴唇张开，眉头抬起，眼睛睁大看着画面右边的绿色跑马场。她往后退了一步，一只手按在胸口，下颌发抖。镜头固定不动。",
  breathy("A light breeze and, far away, hooves pounding.", "轻轻的风声，和很远处急促的马蹄声。"))

# ===================================================================== 第 8 集：极致共骑
# 观众要看懂：① 莉莉快被甩出去，前面是尖桩栅栏（会死）② 基利安从后面追来（冲刺，比人快）③ 他翻上马背抱住她
# ④ 马被勒得人立、被逼停 ⑤ 他喘着气贴在她耳边 ⑥ 他说“晚一秒你就死了”⑦ 捏下巴 ⑧ 吻
K2 = "Side-on wide-medium shot, both riders from the head to the waist and the whole horse, in the middle third of the frame, on the dirt path along the meadow. "
K2C = "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the horse's back against a clear blue sky. "
FIX2 = "The frame holds exactly two people, Killian and Lily, and one black horse."

C(b8, EP['剧本第8集']['segments'][0], '01｜莉莉在奔马上快被甩向栅栏', dur=4, sound=breathy(*GALLOP))

T(b8, '02｜尖桩栅栏飞速掠过', 2, [], ('woods_edge',), ['woods_edge'],
  "Close-up of the rough wooden fence at frame-right, in the middle third of the frame: a row of sharp pointed wooden posts with splintered grey tips, the dirt path and the meadow grass at frame-left, the dark pine forest beyond. No people are in the frame.",
  END_WE + LAY_WE, "一排尖尖的木桩从画面右边飞速掠过，草和尘土被风吹起；画面里没有人。",
  None,
  f"A steady close-up opens from the adopted first frame in {WE}: the sharp pointed fence posts stream past from frame-right to frame-left in a rush of speed, grass and dust whipping across the dirt path in front of them. No people appear. The camera holds still.",
  "一个稳定的特写，从已采用的开场图继续，场景是树林边缘的草地：带尖的木桩快速地从画面右边向左边掠过，草和尘土在前面的土路上被吹得乱飞。画面里没有人出现。镜头固定不动。",
  breathy("Fast, pounding hoofbeats close by and a rush of wind.", "很近处急促沉重的马蹄声和呼啸的风声。"))

C(b8, SEAM[4], '03｜基利安全速冲过草地')
C(b8, REWRITE[14], '04｜基利安翻身上马', sound=breathy(*GALLOP))

T(b8, '05｜勒紧缰绳，马人立而起又落下', 3, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2 + "The tall jet-black horse is in profile facing frame-right on all four hooves, mid-stride, its head hauled up by the reins, its ears pinned back, its nostrils flared. "
  "Killian sits behind Lily, at frame-left of her, in the long charcoal overcoat, leaning back, his left hand pulling the reins hard, his right arm wrapped around her waist, his jaw clenched, his teeth bared, his eyes on the horse's head. "
  "Lily sits in front of him, at frame-right, her back against his chest, both hands gripping the black mane, her eyes squeezed shut, her lips pressed tight. " + FIX2,
  END_WE + LAY_RIDE, "基利安猛地勒紧缰绳，马人立起来又重重落下，莉莉紧闭着眼被他抱住。",
  None,
  f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {KC} hauls back on the reins with his left hand, his right arm tight around {LR}'s waist, his jaw clenched and his teeth bared. "
  f"{HS} rears up on its hind legs with its front hooves raised high, then comes down hard on all four hooves and slows, tossing its head. {LR} presses back against his chest, her eyes squeezed shut and her lips pressed tight. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是树林边缘：基利安用左手猛地往后勒紧缰绳，右臂紧紧箍着莉莉的腰，下颌咬紧，龇着牙。黑马后腿站起、前蹄高高抬起，然后重重落回四蹄，速度慢了下来，甩着头。莉莉向后贴紧他的胸口，眼睛紧闭，嘴唇抿紧。镜头固定不动。",
  breathy("Hooves scraping the dirt, a horse's snort and the creak of leather.", "马蹄刨地声、马的喷鼻声和皮革的吱嘎声。"), dep=True)

T(b8, '06｜他喘着气贴在她耳边', 4, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2C + "Both in profile facing frame-right, the horse's black neck and ears at frame-right. Lily at frame-right, her back against Killian's chest, her hair loose and tangled, her eyes half closed, her lips parted, her brows drawn together. "
  "Killian directly behind her at frame-left in the long charcoal overcoat, his right arm tight around her waist, his lips close to her ear, his jaw tight, his eyes narrowed on the horse's ears at frame-right. The frame holds exactly two people: Killian and Lily.",
  END_WE + LAY_RIDE, "基利安的胸膛贴着她的后背，粗重的呼吸喷在她耳边；她打了个颤。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} pulls {LR} tighter against his chest with his right arm and lowers his head until his lips brush her ear, his chest rising and falling hard, his jaw tight and his eyes narrowed on the horse's ears. "
  "She shivers, her lips parting, her eyes sliding half shut and her brows drawing together. The horse's stride slows beneath them. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘：基利安用右臂把莉莉往胸口搂得更紧，低下头直到嘴唇擦过她的耳朵，胸口剧烈起伏，下颌绷紧，眯着眼睛看着马耳朵。她打了个颤，嘴唇微张，眼睛半闭，眉头拧起。马的步子在他们身下慢了下来。镜头固定不动。",
  breathy("Heavy breathing close by, slowing hoofbeats and the creak of leather.", "很近处粗重的呼吸声、渐渐放慢的马蹄声和皮革的吱嘎声。"))

T(b8, '07｜马被逼停，莉莉瘫软发抖', 4, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2 + "The tall jet-black horse is in profile facing frame-right at a slow walk, tossing its head, its flanks heaving. "
  "Killian sits behind Lily, at frame-left of her, in the long charcoal overcoat, his left hand holding the reins short, his right arm around her waist, his jaw tight, his lips pressed together, his eyes lowered on her face. "
  "Lily sits in front of him, at frame-right, slumping back against his chest, her shoulders shaking, her eyes half closed, her lips parted and trembling. " + FIX2,
  END_WE + LAY_RIDE, "马慢慢停下，打着响鼻；莉莉瘫在他怀里发抖，基利安低头看着她。",
  None,
  f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {HS} slows to a halt and stands blowing hard, tossing its head. {KC} holds the reins short in his left hand with his right arm around {LR}, his eyes lowered on her face and his jaw tight. "
  "She sags against his chest, trembling, her eyes half closed and her lips quivering. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是树林边缘：黑马慢下来，停住，呼呼喘着气甩着头。基利安左手把缰绳握短，右臂搂着莉莉，眼睛低下来看着她的脸，下颌绷紧。她瘫软地靠在他胸口发抖，眼睛半闭，嘴唇颤抖。镜头固定不动。",
  breathy("Slow hoofbeats settling on dry earth, a horse blowing hard and the creak of leather.", "渐渐落定的蹄声、马的粗重喘息和皮革的吱嘎声。"))

T(b8, '08｜如果我晚来一秒', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2 + "The tall jet-black horse stands in profile facing frame-right. "
  "Killian sits behind Lily, at frame-left of her, in the long charcoal overcoat, his left hand holding the reins short, his right arm around her waist, his jaw tight, his lips set, his eyes on her face. "
  "Lily sits in front of him, at frame-right, slumping back against his chest, her lips parted and trembling, her eyes half closed and lowered on his hand at her waist. " + FIX2,
  END_WE + LAY_RIDE, "基利安用嘶哑狠戾的声音说：晚一秒你就死了。",
  ('KillianCoat', "One second later, you'd be dead.", 1.0),
  f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {KC} speaks in a low, hoarse, savage voice, his eyes on {LR}'s face and his jaw tight, his right hand closing harder at her waist. "
  "She sags against his chest, her lips quivering and her eyes lowered on his hand. The horse shifts its hooves. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是树林边缘：基利安用低沉嘶哑、狠戾的声音说话，眼睛看着莉莉的脸，下颌绷紧，右手在她腰上攥得更紧。她瘫在他胸口，嘴唇颤抖，眼睛垂着看他的手。马挪了挪蹄子。镜头固定不动。",
  voiced("A light breeze over the meadow and the creak of leather.", "草地上轻轻的风声和皮革的吱嘎声。"), dep=True)

T(b8, '09｜捏住下巴扳过她的脸', 4, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2C + "Killian at frame-left in profile facing frame-right in the long charcoal overcoat, his right hand on Lily's jaw, his jaw tight, his lips set, his eyes on her face. "
  "Lily at frame-right, her body facing frame-right and her face turning back toward him, her eyes wide on his eyes, her lips parted. The horse's black neck at frame-right. The frame holds exactly two people: Killian and Lily.",
  END_WE + LAY_RIDE, "基利安捏住她的下巴把她的脸扳过来，眼睛盯着她的嘴唇；她睁大眼睛看着他。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC}'s right hand grips {LR}'s chin and turns her face back toward his, his eyes dropping to her lips and his jaw tight. "
  "Her eyes go wide on his eyes, her lips part and her hands rise to his forearm. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘：基利安的右手捏住莉莉的下巴，把她的脸扳向自己，眼睛落到她的嘴唇上，下颌绷紧。她睁大眼睛看着他的眼睛，嘴唇微张，双手抬起搭上他的前臂。镜头固定不动。",
  breathy("A light breeze over the meadow and the creak of leather.", "草地上轻轻的风声和皮革的吱嘎声。"))

T(b8, '10｜吻', 4, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2C + "Killian at frame-left in profile facing frame-right in the long charcoal overcoat, his face a hand's width from Lily's, his right hand firm on her jaw, his jaw tight, his eyes on her lips. "
  "Lily at frame-right, her face turned back toward him in profile facing frame-left, her eyes wide open, her lips parted, her left hand on his forearm. The frame holds exactly two people: Killian and Lily.",
  END_WE + LAY_RIDE, "基利安狠狠吻住她；她睁大眼睛推了推他的手臂，然后眼睛慢慢半闭。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} presses his lips hard against {LR}'s lips, his right hand firm on her jaw, his brows drawn together and his eyes closed. "
  "Her eyes stay wide open and her left hand pushes weakly against his forearm, then her eyes slowly flutter half shut. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘：基利安把嘴唇狠狠压在莉莉的嘴唇上，右手牢牢扣着她的下颌，眉头拧着，眼睛闭上。她的眼睛睁得大大的，左手无力地推着他的前臂，然后眼睛慢慢半闭。镜头固定不动。",
  breathy("A light breeze over the meadow, the creak of leather and a muffled sound from her.", "草地上轻轻的风声、皮革的吱嘎声，和她被堵住的一声闷响。"), dep=True)

# ===================================================================== 第 9 集：马背上的惩罚
# 观众要看懂：① 吻结束，她喘气 ② 她骂他疯子要下马，他不放 ③ 他用大衣裹住她 ④ 两句耳边的话：你本该逃的／没人能碰你
# ⑤ 保罗在林边一路喊着找她（观众知道他来了）⑥ 他们沿路走，基利安眼神一冷（看见了什么）⑦ 保罗看见→怒吼 ⑧ 基利安居高临下，响指
T(b9, '01｜吻结束，她喘着气', 4, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2C + "Killian at frame-left in profile facing frame-right in the long charcoal overcoat, his face a hand's width from hers, his jaw tight, his lips set, his eyes on her lips. "
  "Lily at frame-right, her face turned back toward him in profile facing frame-left, her lips red and swollen, her mouth open, her eyes wide and glossy, her right palm flat against his chest. The frame holds exactly two people: Killian and Lily.",
  END_WE + LAY_RIDE, "他把脸移开一掌宽，两个人都喘着气；她的嘴唇红肿，手抵在他胸口。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} lifts his face away from {LR}'s until it is a hand's width from hers, his chest heaving, his eyes on her lips and his jaw tight. "
  "She gasps, her right hand pressing against his chest, her lips red and swollen and her eyes glossy. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘：基利安把脸从莉莉脸上移开，直到离她一掌宽，胸口起伏，眼睛看着她的嘴唇，下颌绷紧。她倒吸着气，右手抵住他的胸口，嘴唇红肿，眼睛湿亮。镜头固定不动。",
  breathy("Two people breathing hard, a light breeze and the creak of leather.", "两个人急促的喘息声、轻轻的风声和皮革的吱嘎声。"))

T(b9, '02｜你疯了，放我下去', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2C + "Killian at frame-left in profile facing frame-right in the long charcoal overcoat, a cold smirk, his jaw set, his eyes on her face. "
  "Lily at frame-right, her face turned back toward him in profile facing frame-left, her lips red and swollen, her brows drawn together, tears on her lashes, her eyes on his face, her right hand pushing against his chest. The frame holds exactly two people: Killian and Lily.",
  END_WE + LAY_RIDE, "莉莉带着哭腔骂他疯子、要他放她下去，他冷笑着不松手。",
  ('LilyRiding', "You're insane! Let me down!", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {LR} cries out in a shaky, tearful voice, her brows drawn together and her glossy eyes on his face, both hands pushing against his chest. "
  f"{KC} leans back a little with a cold smirk, his jaw set and his eyes on her face, his right arm not letting go of her waist. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘：莉莉用发抖带哭腔的声音喊出来，眉头拧着，湿亮的眼睛看着他的脸，双手抵着他的胸口推。基利安微微后仰，露出冷笑，下颌绷紧，眼睛看着她的脸，右臂没有松开她的腰。镜头固定不动。",
  voiced("A light breeze over the meadow and the creak of leather.", "草地上轻轻的风声和皮革的吱嘎声。"), dep=True)

T(b9, '03｜他用大衣把她裹进怀里', 5, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2C + "Killian at frame-left in profile facing frame-right, his left hand drawing the front of his long charcoal overcoat across Lily's shoulders, his right hand holding the reins, a cold smirk, his eyes on her face. "
  "Lily at frame-right, her face turned back toward him in profile facing frame-left, her hair tumbling loose, the collar of her cream blouse slipped off one shoulder, her lips red and swollen, her eyes lowered, her brows drawn together. The frame holds exactly two people: Killian and Lily.",
  END_WE + LAY_RIDE, "他把大衣拉过来裹住她，把她按回胸口；她不再推，嘴唇发颤，眼睛垂下。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} draws the front of his long charcoal coat across {LR}'s shoulders with his left hand and pulls her back against his chest, a cold smirk on his lips and his eyes on her face. "
  "Her hands stop pushing, her lips tremble and her eyes lower as the coat closes around her. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘：基利安用左手把长长的炭灰大衣前襟拉过莉莉的肩膀，把她拉回自己胸口，嘴角带着冷笑，眼睛看着她的脸。她的手不再推了，嘴唇发颤，眼睛垂下，大衣在她身上合拢。镜头固定不动。",
  breathy("The soft rustle of heavy wool and the creak of leather.", "厚呢子大衣的轻响和皮革的吱嘎声。"), dep=True)

T(b9, '04｜耳边低语一', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2C + "Killian at frame-left in profile facing frame-right, his head lowered so his lips are close to her ear, his jaw tight, his eyes narrowed on her ear. "
  "Lily at frame-right, wrapped in his long charcoal overcoat, her hair loose, her eyes closed, her lips trembling, her brows drawn together. The frame holds exactly two people: Killian and Lily.",
  END_WE + LAY_RIDE, "基利安贴着她的耳朵，用沙哑的声音低语：你本该逃的。",
  ('KillianCoat', "You should have run, Lily.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} lowers his head until his lips are close to {LR}'s ear and speaks in a low, husky whisper, his jaw tight and his eyes narrowed on her ear. "
  "She shudders inside his coat, her eyes closing tighter and her lips trembling. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘：基利安低下头，直到嘴唇贴近莉莉的耳朵，用低沉沙哑的声音耳语，下颌绷紧，眯着眼睛看着她的耳朵。她在他的大衣里一颤，眼睛闭得更紧，嘴唇发颤。镜头固定不动。",
  voiced("A light breeze over the meadow and the creak of leather.", "草地上轻轻的风声和皮革的吱嘎声。"), dep=True)

T(b9, '05｜耳边低语二', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2C + "Killian at frame-left in profile facing frame-right, his lips close to her ear, his jaw tight, his eyes narrowed with a dark-gold glint. "
  "Lily at frame-right, wrapped in his long charcoal overcoat, her hair loose, her eyes closed, her lips trembling, her brows drawn together. The frame holds exactly two people: Killian and Lily.",
  END_WE + LAY_RIDE, "他继续低语：没人能碰你；眼睛里闪着暗金色。",
  ('KillianCoat', "No one touches you. Ever.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {KC} speaks against {LR}'s ear in a low, husky whisper, his jaw tight and his eyes narrowed with a dark-gold glint. "
  "She trembles inside his coat, her lips parting and her eyes squeezed shut. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘：基利安贴着莉莉的耳朵用低沉沙哑的声音耳语，下颌绷紧，眯着的眼睛里闪着暗金色。她在他的大衣里发抖，嘴唇微张，眼睛紧闭。镜头固定不动。",
  voiced("A light breeze over the meadow and the creak of leather.", "草地上轻轻的风声和皮革的吱嘎声。"), dep=True)

T(b9, '06｜保罗在林边一路喊着找她', 6, ['PaulOnScreen'], ('woods_edge', 'paul'), ['woods_edge'],
  "Medium shot of Paul alone, from the head to the waist, in profile facing frame-left, in the middle third of the frame, jogging along the dirt path in his navy blazer over a white open-collared shirt, the blazer dusty and the collar crooked, "
  "his chest heaving, his brows pulled up, his lips parted, his eyes wide and darting along the path at frame-left. The rough wooden fence stands behind him at frame-right. The frame holds exactly one person, Paul.",
  END_WE + LAY_WE, "保罗气喘吁吁地沿着土路朝左边跑，一边喊莉莉的名字。",
  ('PaulOnScreen', "Where are you, Lily?", 1.0),
  f"A steady medium shot opens from the adopted first frame in {WE}: {PL} runs a few strides along the dirt path toward frame-left and shouts, his mouth wide open, his brows pulled up and his eyes wide and darting along the path, then slows with his chest heaving. The camera holds still.",
  "一个稳定的中景，从已采用的开场图继续，场景是树林边缘：保罗沿着土路朝画面左边跑了几步，大声喊着，嘴张得很大，眉头抬起，睁大的眼睛在路上四处扫，然后慢下来，胸口剧烈起伏。镜头固定不动。",
  voiced("A light breeze and his boots scuffing the dirt.", "轻轻的风声和他的靴子蹭过泥土的声音。"))

T(b9, '07｜他们沿着小路往前走，基利安眼神一冷', 4, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  "Side-on wide shot, both riders and the whole horse, in the middle third of the frame, on the dirt path along the meadow. The tall jet-black horse walks in profile facing frame-right, its head level. "
  "Killian sits behind Lily, at frame-left of her, his left hand on the reins, his jaw set, his lips flat, his eyes on the path ahead at frame-right. "
  "Lily sits in front of him, at frame-right, his open charcoal overcoat wrapped around her as she leans back against his chest, her hair loose, her eyes lowered, her lips parted. " + FIX2,
  END_WE + LAY_RIDE, "黑马驮着两人慢慢沿着土路往前走，基利安盯着前面的路，眼神慢慢变冷。",
  None,
  f"A steady side-on wide shot opens from the adopted first frame in {WE}: {HS} walks slowly along the dirt path toward frame-right with {KC} behind {LR}, his left hand on the reins and his eyes on the path ahead. "
  "His eyes narrow and a cold smirk curls his lips. She leans against his chest wrapped in his coat, her eyes lowered and her lips parted. The camera holds still.",
  "一个稳定的侧面宽景，从已采用的开场图继续，场景是树林边缘：黑马载着两人沿着土路朝画面右边慢慢走，基利安坐在莉莉身后，左手握缰绳，眼睛看着前面的路。他的眼睛眯了起来，嘴角慢慢浮出一抹冷笑。她裹在他的大衣里靠着他的胸口，眼睛垂着，嘴唇微张。镜头固定不动。",
  breathy("Slow, steady hoofbeats on dirt and the creak of leather.", "泥土路上缓慢平稳的马蹄声和皮革的吱嘎声。"))

T(b9, '08｜保罗看见他们，怒吼', 6, ['PaulOnScreen'], ('woods_edge', 'paul'), ['woods_edge'],
  "Medium shot of Paul alone, from the head to the waist, in profile facing frame-left, in the middle third of the frame, standing on the dirt path in his navy blazer over a white open-collared shirt, the blazer dusty and the collar crooked, "
  "his chest heaving, his brows pulled up, his lips parted, his eyes wide and fixed down the dirt path at frame-left. The rough wooden fence stands behind him at frame-right. The frame holds exactly one person, Paul.",
  END_WE + LAY_WE, "保罗猛地站住，脸上的松口气一下变成暴怒，红着眼睛吼出来。",
  ('PaulOnScreen', "Put her down! She's my fiancé!", 1.5),
  f"A steady medium shot opens from the adopted first frame in {WE}: {PL} stops dead on the dirt path, his eyes widening on the path ahead at frame-left, then narrowing, his brows crashing together and his jaw clenching. "
  "He shouts in a cracking, furious voice, his mouth wide open and his eyes red-rimmed. The camera holds still.",
  "一个稳定的中景，从已采用的开场图继续，场景是树林边缘：保罗猛地在土路上站住，睁大的眼睛看着画面左边前方的路，然后眯起来，眉头一下拧在一起，下颌咬紧。他用发颤暴怒的声音吼出来，嘴张得很大，眼眶发红。镜头固定不动。",
  voiced("A light breeze over the meadow.", "草地上轻轻的风声。"))

T(b9, '09｜基利安居高临下，打了个响指', 5, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  K2 + "The tall jet-black horse stands in profile facing frame-right. "
  "Killian sits behind Lily, at frame-left of her, his left hand holding the reins, his right hand raised to shoulder height with his thumb pressed against his middle finger, ready to snap, his lips flat, his half-lidded eyes cold on the path ahead at frame-right. "
  "Lily sits in front of him, at frame-right, wrapped in his long charcoal overcoat and leaning against his chest, her eyes closed, her lips parted. " + FIX2,
  END_WE + LAY_RIDE, "基利安居高临下看着前面，抬起右手，打了一个响指。",
  None,
  f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {KC} snaps the fingers of his raised right hand, a cold smirk on his lips and his half-lidded eyes cold on the path ahead at frame-right. "
  f"{LR} stirs against his chest, her eyes opening slowly and her lips parting. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是树林边缘：基利安打响了举起的右手的手指，嘴角带着冷笑，半垂的冷眼看着画面右边前方的路。莉莉在他胸口动了动，眼睛慢慢睁开，嘴唇微张。镜头固定不动。",
  breathy("A single sharp finger snap and the creak of leather.", "一声清脆的响指和皮革的吱嘎声。"))

# ===================================================================== 第 10 集：碾压式打脸
# 观众要看懂：① 响指之后保罗被保镖围住（原剧本几十人，这里 2 人）② 基利安下马，把莉莉放到身后，朝保罗走去
# ③ 他揪住保罗：你爸把婚约卖了，一块钱 ④ 莉莉听到，震惊 ⑤ 他推开保罗（保罗摔在地上）⑥ 他把莉莉抱起来
# ⑦ 当众宣誓：莉莉·斯旺是我的；谁碰她都得死 ⑧ 莉莉承受不住晕倒，他喊她的名字
DISM = ("Side-on wide-medium shot, both people and the whole horse, in the middle third of the frame, on the dirt path along the meadow. The tall jet-black horse stands in profile facing frame-right. ")

T(b10, '01｜保镖围住保罗', 5, ['PaulOnScreen', 'Bodyguard'], ('woods_edge', 'paul', 'bodyguard'), ['woods_edge'],
  "Side-on wide shot, three men in the middle third of the frame, on the dirt path along the meadow. Paul stands in the center facing frame-left, in the navy blazer over a white open-collared shirt, the blazer dusty, his hands slightly raised, his mouth open, his brows pulled up, his eyes wide and darting. "
  "Bodyguard stands one pace from him at frame-left, facing frame-right, in a black suit, a white shirt, a black tie and a clear coiled earpiece, his hands clasped in front of him, his jaw set, his lips flat, his eyes on Paul. "
  "A second man identical to him in build and clothes stands one pace from Paul at frame-right, facing frame-left, his hands clasped in front of him, his jaw set, his lips flat, his eyes on Paul. The frame holds exactly three people: Paul and two bodyguards.",
  END_WE + LAY_WE, "响指之后，两个黑衣保镖从两边逼近保罗，保罗吓得往后退。",
  None,
  f"A steady side-on wide shot opens from the adopted first frame in {WE}: two bodyguards who both look like {BG} take one slow step each toward {PL}, closing in from both sides, their hands clasped in front of them, their jaws set and their lips flat. "
  f"{PL} backs up half a step with his hands rising higher, his mouth open, his brows pulled up and his eyes darting between them. The camera holds still.",
  "一个稳定的侧面宽景，从已采用的开场图继续，场景是树林边缘：两个都长得像保镖素材的黑衣保镖各向保罗迈了一步，从两边逼近，双手交握在身前，下颌绷紧，嘴唇平直。保罗往后退了半步，双手举得更高，嘴张着，眉头抬起，眼睛在两个人之间乱转。镜头固定不动。",
  breathy("Leather shoes crunching on the dirt path and a light breeze.", "皮鞋踩在土路上的嘎吱声和轻轻的风声。"))

T(b10, '02｜基利安翻身下马', 3, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  DISM + "Killian sits behind Lily, at frame-left of her, his left hand on the reins, his right arm around her waist, his jaw set, his lips flat, his eyes on the path ahead at frame-right. "
  "Lily sits in front of him, at frame-right, wrapped in his long charcoal overcoat, her eyes half open, her lips parted, her brows drawn together. " + FIX2,
  END_WE + LAY_RIDE, "基利安从马背上翻下来，落在马身旁，一只手仍扶着莉莉的腰。",
  None,
  f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {KC} lifts his right arm from her waist, swings his right leg back over the horse and drops to the ground at the horse's flank, one hand staying at her waist, his jaw set and his eyes on her face. "
  f"{LR} sways and is steadied by his hand, her lips parting and her eyes widening. {HS} stands still. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是树林边缘：基利安把右臂从她腰上抬开，右腿向后跨过马背，落在马身旁的地上，一只手仍扶在她腰上，下颌绷紧，眼睛看着她的脸。莉莉晃了一下，被他的手扶稳，嘴唇微张，眼睛睁大。黑马站着不动。镜头固定不动。",
  breathy("Boots landing on dirt, a horse blowing and the creak of leather.", "靴子落在泥土上的声音、马的喷鼻声和皮革的吱嘎声。"))

T(b10, '03｜他把莉莉抱下马，护到身后', 3, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding', 'black_horse'), ['woods_edge'],
  DISM + "Killian stands on the ground at the horse's flank at frame-left, in the long charcoal overcoat, both hands rising to Lily's waist, his jaw set, his lips flat, his eyes on her face. "
  "Lily sits in the saddle above him, at frame-right of him, wrapped in his coat, her hands resting on his shoulders, her lips parted, her brows drawn together, her eyes on his face. " + FIX2,
  END_WE + LAY_RIDE, "基利安双手托住莉莉的腰把她抱下马，让她站在自己身后。",
  None,
  f"A steady side-on wide-medium shot opens from the adopted first frame in {WE}: {KC} grips {LR} by the waist with both hands, lifts her out of the saddle and sets her on her feet, then draws her behind his shoulder, his jaw set and his eyes on her face. "
  "She steadies herself with one hand on his arm, her lips parting and her brows drawing together. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是树林边缘：基利安双手握住莉莉的腰，把她从鞍上抱起来放在地上，然后把她拉到自己肩后，下颌绷紧，眼睛看着她的脸。她一只手扶着他的手臂站稳，嘴唇微张，眉头拧起。镜头固定不动。",
  breathy("Boots on dirt, a soft rustle of wool and a horse shifting its hooves.", "靴子踩在泥土上的声音、呢子大衣的轻响和马挪动蹄子的声音。"), dep=True)

T(b10, '04｜他慢慢走向保罗', 4, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding'), ['woods_edge'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, walking on the dirt path, both in profile facing frame-right. "
  "Killian at frame-right in the long charcoal overcoat, his right arm held out low at his side as a barrier, his jaw set, his lips flat, his eyes on the dirt path ahead at frame-right. "
  "Lily at frame-left, half a step behind him, in the cream blouse with her hair loose, her left hand gripping his coat sleeve at the elbow, her lips parted, her brows drawn together, her eyes lowered on her hand. The frame holds exactly two people: Lily and Killian.",
  END_WE + LAY_WE, "基利安慢条斯理地沿着土路向前走，一只手臂挡在莉莉前面；莉莉抓着他的袖子跟在后面。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {WE}: {KC} walks slowly along the dirt path toward frame-right with his arm out in front of {LR}, his jaw set and his eyes on the path ahead. "
  "She walks half a step behind him, her hand gripping his sleeve, her lips parted and her brows drawn together. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是树林边缘：基利安沿着土路朝画面右边慢慢地走，一条手臂挡在莉莉前面，下颌绷紧，眼睛看着前面的路。她落后他半步走着，手抓着他的袖子，嘴唇微张，眉头拧起。镜头固定不动。",
  breathy("Slow footsteps on the dirt path and a light breeze.", "土路上缓慢的脚步声和轻轻的风声。"))

_COLLAR = ("Side-on medium two-shot, both men from the head to the waist, in the middle third of the frame, face to face in profile on the dirt path. "
           "Killian at frame-left, facing frame-right, in the long charcoal overcoat, his right arm straight, his right hand gripping Paul's jacket collar at chest height, his jaw set, his lips flat, his eyes cold and level on Paul's face. "
           "Paul at frame-right, facing frame-left, in the navy blazer, both of his hands gripping Killian's right wrist, his mouth open, his brows pulled up, his eyes wide and fixed on Killian's face. "
           "The frame holds exactly two people: Killian and Paul.")

T(b10, '05｜揪住保罗的领子：你爸把婚约卖了', 6, ['KillianCoat', 'PaulOnScreen'], ('woods_edge', 'killian_coat', 'paul'), ['woods_edge'],
  _COLLAR, END_WE + LAY_WE, "基利安揪着保罗的领子，冷冷地说：你爸把你的婚约卖了。",
  ('KillianCoat', "Your father sold your engagement.", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {WE}: {KC} at frame-left holds {PL}'s jacket collar in his right hand, his arm straight, and speaks in a low, icy voice, his jaw set and his eyes cold and level on Paul's face. "
  f"{PL} grips Killian's wrist with both hands, his mouth open, his brows pulled up and his eyes wide, his heels scrabbling at the dirt. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是树林边缘：画面左边的基利安右手揪着保罗的外套领子，手臂伸直，用低沉冰冷的声音说话，下颌绷紧，冷冷平视着保罗的脸。保罗双手抓着基利安的手腕，嘴张着，眉头抬起，眼睛睁大，脚后跟在泥地上乱蹬。镜头固定不动。",
  voiced("A light breeze over the meadow and the creak of leather.", "草地上轻轻的风声和皮革的吱嘎声。"))

T(b10, '06｜一块钱', 6, ['KillianCoat', 'PaulOnScreen'], ('woods_edge', 'killian_coat', 'paul'), ['woods_edge'],
  _COLLAR, END_WE + LAY_WE, "基利安接着说：价钱是一块钱；保罗的脸一下垮了。",
  ('KillianCoat', "The price was one dollar.", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {WE}: {KC} speaks in a low, icy voice with a cold smirk, his jaw set and his eyes cold and level on Paul's face, his arm still straight. "
  f"{PL}'s mouth falls wider open, his brows crumpling and his eyes going glassy as his hands loosen on Killian's wrist. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是树林边缘：基利安用低沉冰冷的声音说话，嘴角带着冷笑，下颌绷紧，冷冷平视着保罗的脸，手臂依然伸直。保罗的嘴张得更大，眉头皱成一团，眼神发直，抓着基利安手腕的手慢慢松开。镜头固定不动。",
  voiced("A light breeze over the meadow and the creak of leather.", "草地上轻轻的风声和皮革的吱嘎声。"), dep=True)

T(b10, '07｜莉莉听到，震惊', 3, ['LilyRiding'], ('woods_edge', 'lily_riding'), ['woods_edge'],
  "Side-on medium close-up of Lily alone, from the head to the waist, in profile facing frame-right, in the middle third of the frame, standing on the dirt path in the cream blouse with her hair loose, her hands clasped tight at her chest, her lips parted, her brows pulled up, her eyes wide on the dirt path ahead at frame-right. The frame holds exactly one person, Lily.",
  END_WE + LAY_WE, "莉莉听到婚约被一块钱买走，倒吸一口气，攥紧了手。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {WE}: {LR}'s eyes widen further and her lips part in a small gasp, her brows pulling up, then her brows draw together as she swallows, her clasped hands pressing harder against her chest. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是树林边缘：莉莉的眼睛睁得更大，嘴唇张开倒吸一口气，眉头抬起，然后咽了一下口水，眉头拧在一起，交握的双手更用力地按在胸口。镜头固定不动。",
  breathy("A light breeze and a small sharp breath.", "轻轻的风声和一声短促的吸气。"))

T(b10, '08｜他推开保罗，保罗摔在地上', 3, ['KillianCoat', 'PaulOnScreen'], ('woods_edge', 'killian_coat', 'paul'), ['woods_edge'],
  _COLLAR, END_WE + LAY_WE, "基利安一把推开保罗，保罗踉跄后退，摔坐在泥地上。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {WE}: {KC} shoves {PL} away and lets go of the collar, his arm snapping straight, his jaw set and his lips flat. "
  f"{PL} staggers back two steps, his arms flailing, his mouth open and his eyes wide, and drops onto the dirt, landing sitting and leaning back on both hands. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是树林边缘：基利安一把把保罗推开、松开领子，手臂一下伸直，下颌绷紧，嘴唇平直。保罗踉跄着后退了两步，双臂乱挥，嘴张着，眼睛睁大，摔坐在泥地上，双手向后撑着。镜头固定不动。",
  breathy("A grunt of effort, boots scuffing and a heavy thud on dirt.", "一声用力的闷哼、靴子的蹭地声和落在泥地上的沉闷一响。"))

T(b10, '09｜他把莉莉横抱起来', 3, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding'), ['woods_edge'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, on the dirt path. "
  "Lily at frame-left, standing and swaying, in the cream blouse with her hair loose, her left hand resting on Killian's chest, her lips parted, her brows drawn together, her eyes half closed. "
  "Killian at frame-right, in profile facing frame-left, in the long charcoal overcoat, bending slightly, his right arm behind her back and his left arm behind her knees, about to lift her, his jaw set, his lips flat, his eyes on her face. The frame holds exactly two people: Lily and Killian.",
  END_WE + LAY_WE, "基利安转身，一把把站不稳的莉莉横抱起来。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {WE}: {KC} sweeps {LR} up in his arms in one smooth motion, his right arm behind her back and his left arm under her knees, his jaw set and his eyes on her face. "
  "Her head tips against his shoulder and she gasps, her lips parting and her eyes widening, her hand gripping his collar. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是树林边缘：基利安一个连贯的动作把莉莉横抱起来，右臂托着她的背，左臂托着她的膝弯，下颌绷紧，眼睛看着她的脸。她的头靠上他的肩膀，倒吸一口气，嘴唇微张，眼睛睁大，手抓住他的衣领。镜头固定不动。",
  breathy("A soft rustle of wool and a small gasp.", "呢子大衣的轻响和一声小小的抽气。"))

_CARRY = ("Side-on medium shot, from the head of the man to below the knees of the woman in his arms, in the middle third of the frame, on the dirt path. "
          "Killian stands in profile facing frame-left in the long charcoal overcoat, carrying Lily in both arms across his chest, {K}. "
          "Lily lies in his arms with her head resting against his shoulder, her left arm hanging loose, {L}. The frame holds exactly two people: Killian and Lily.")

T(b10, '10｜莉莉·斯旺是我的', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding'), ['woods_edge'],
  _CARRY.format(K="his jaw set, his lips flat, his cold eyes on the dirt path at frame-left", L="her lips parted, her dazed half-open eyes looking up at his jaw"),
  END_WE + LAY_WE, "基利安抱着莉莉，当众宣布：莉莉·斯旺是我的。",
  ('KillianCoat', "Lily Swan belongs to me.", 1.0),
  f"A steady side-on medium shot opens from the adopted first frame in {WE}: {KC} holds {LR} in his arms and speaks in a low, steely voice, his jaw set, his chin lifting and his cold eyes sweeping along the dirt path at frame-left. "
  "She lies against his shoulder, her lips parted, her dazed eyes half open and looking up at his jaw. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是树林边缘：基利安抱着莉莉，用低沉如钢的声音说话，下颌绷紧，下巴抬起，冷冷的眼睛沿着画面左边的土路扫过去。她靠在他的肩上，嘴唇微张，恍惚的半睁着眼睛抬头看着他的下颌。镜头固定不动。",
  voiced("A light breeze over the meadow and the creak of leather.", "草地上轻轻的风声和皮革的吱嘎声。"), dep=True)

T(b10, '11｜谁碰她，你们全都得死', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding'), ['woods_edge'],
  _CARRY.format(K="his jaw set, his lips flat, his eyes narrowed with a dark-gold glint on the dirt path at frame-left", L="her lips parted, her eyes half open"),
  END_WE + LAY_WE, "基利安眼里闪着暗金色，一字一句地威胁所有人。",
  ('KillianCoat', "Touch her, and you're all dead.", 1.0),
  f"A steady side-on medium shot opens from the adopted first frame in {WE}: {KC} speaks in a low, steely voice, his jaw set and his eyes narrowed with a dark-gold glint, his gaze sweeping slowly along the dirt path at frame-left. "
  f"{LR} lies against his shoulder, her lips parted and her eyelids sinking lower. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是树林边缘：基利安用低沉如钢的声音说话，下颌绷紧，眯起的眼睛里闪着暗金色，目光慢慢沿着画面左边的土路扫过去。莉莉靠在他的肩上，嘴唇微张，眼皮越垂越低。镜头固定不动。",
  voiced("A light breeze over the meadow and the creak of leather.", "草地上轻轻的风声和皮革的吱嘎声。"), dep=True)

T(b10, '12｜莉莉晕倒，他喊她的名字', 6, ['KillianCoat', 'LilyRiding'], ('woods_edge', 'killian_coat', 'lily_riding'), ['woods_edge'],
  _CARRY.format(K="his jaw set, his lips flat, his cold eyes on the dirt path at frame-left", L="her lips parted, her eyelids heavy"),
  END_WE + LAY_WE, "莉莉眼睛一闭，头向后仰倒在他臂弯里；基利安脸色大变，喊她的名字。",
  ('KillianCoat', "Lily!", 2.0),
  f"A steady side-on medium shot opens from the adopted first frame in {WE}: {LR}'s eyes flutter shut and her head tips back over his arm, her lips parting and her left arm dropping loose. "
  f"{KC} looks down at her face, his brows pulling up, his mouth opening and his eyes going wide, and calls her name in a cracking, urgent voice. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是树林边缘：莉莉的眼睛一闭，头向后仰倒在他的臂弯上，嘴唇微张，左臂软软垂下。基利安低头看着她的脸，眉头抬起，嘴张开，眼睛睁大，用发颤急切的声音喊她的名字。镜头固定不动。",
  voiced("A light breeze over the meadow and the creak of leather.", "草地上轻轻的风声和皮革的吱嘎声。"), dep=True)

# ===================================================================== 合成一份
doc = copy.deepcopy(b7.d)
doc['episodes'] = [
    episode(b7, '剧本第7集｜致命危机（场景级改编）', '买通驯马师、激将、上马、扎针、发狂、基利安听到后冲出去。'),
    episode(b8, '剧本第8集｜极致共骑（场景级改编）', '快被甩向栅栏、基利安冲刺追上、翻身上马、勒停、吻。'),
    episode(b9, '剧本第9集｜马背上的惩罚（场景级改编）', '吻后、大衣、耳边低语、保罗找来、怒吼、响指。'),
    episode(b10, '剧本第10集｜碾压式打脸（场景级改编）', '保镖围住保罗、一块钱、宣誓、莉莉晕倒。'),
]
txt = json.dumps(doc, ensure_ascii=False, indent=1)
open(os.path.join(FOLDER, OUT + '.json'), 'w', encoding='utf-8').write(txt)
open(os.path.join(FOLDER, OUT + '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(txt)
n = sum(len(e['segments']) for e in doc['episodes']); sec = sum(s['duration_seconds'] for e in doc['episodes'] for s in e['segments'])
print(f'{len(doc["episodes"])} 集、{n} 个任务、约 {sec} 秒；文件 {len(txt.encode())/1024:.0f} KB')
for e in doc['episodes']:
    print('  ', e['title'], len(e['segments']), '个任务', sum(s['duration_seconds'] for s in e['segments']), '秒')
