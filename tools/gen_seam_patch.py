#!/usr/bin/env python3
"""接缝补镜头测试（2026-10-10 23:42，hh 指出马场重写测试里几处“变戏法”）。

重写测试成片（实际片长）里的断点：
  08→09  玛丽扎针后，马没有任何反应；下一镜头是马立起，玛丽没了（09 的开场图写了“恰好一个人：莉莉”，把她删了）
  11→12  11 整段是听电话的同一个姿势，没有“抬头”；12 开头电话已在胸前、约 1 秒就捏碎，之后不动 → 没有触发、没有升级
  13→14→15  13 约 2.5 秒翻栏杆出画后空镜 1.5 秒；14 莉莉狂奔；15 开头他已经在马旁，中间没有他赶过去的路程
补法：每个断点补 1–2 个 3 秒的“过渡拍”（反应／在场的人／在途）。5 个任务，全部 3 秒，无台词。
  补1 马被扎后抽腿、玛丽退开（接 08 之后）      补2 莉莉在鞍上被吓到（接 补1）
  补3 玛丽退到看台边看着（接 09 之后）          补4 基利安脸色变、放下电话（替换 11）
  补5 基利安在草地上全速冲刺（接 14 之后）
剪辑顺序：…08, 补1, 补2, 09, 补3, 10, 补4, 12, 13(只留前 3 秒), 14, 补5, 15, 16…
素材／人物／style 以马场合并稿为底逐字复制，没有新增素材。种子 4911–4915。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json
from _h3draft import Batch, FOLDER, breathy

BASE = '合并稿/合并_第7-10集+10B_制作稿_追加.json'
OUT = '合并稿/接缝补镜头测试_制作稿_追加'
SRC = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))
a = Batch(BASE, SRC['title'], 4910)

RN = '[[asset:ranch]]'; WE = '[[asset:woods_edge]]'
KC = '[[asset:killian_coat]]'; LR = '[[asset:lily_riding]]'; MR = '[[asset:mary_riding]]'; HS = '[[asset:black_horse]]'
LAY_RN = " Fixed stage layout: the raised wooden grandstand is at frame-left; the white fence and the green field are at frame-right; dark pine trees line the far edge."
Z_RN = "固定布局：凸起的木制看台在画面左边；白色围栏和绿色跑马场在画面右边；远处边缘是一排深色松树。"
END_RN = " Bright midday sunlight, a clear blue sky, the ranch softly blurred behind."
Z_END_RN = "明亮的正午阳光，晴朗的蓝天，跑马场在后面柔和虚化。"
LAY_WE = " Fixed stage layout: the open meadow with a dirt path is at frame-left; the rough wooden fence with sharp pointed posts and the dark pine forest are at frame-right."
END_WE = " Bright afternoon sunlight, a clear blue sky, the meadow softly blurred behind."


def T(title, chars, assets, refs, img, end, vis_zh, cam_zh, shot_en, shot_zh, sound, seed):
    s = a.task(title, 3, chars, assets, refs, img, end, vis_zh, cam_zh, None, shot_en, shot_zh, sound)
    s['seed'] = seed
    s['depends_on_previous'] = False
    return s


# 补1 马被扎后抽腿、玛丽退开：和 08 同一个构图（玛丽在画面左边、马的后半身在右边），接 08 的结尾
T('01｜补1 马被扎后抽腿、玛丽退开', ['MaryRiding'], ('ranch', 'mary_riding', 'black_horse'), ['ranch'],
  "Side-on medium shot, in the middle third of the frame, on the packed-earth track. Mary stands at frame-left from the head to the knees in profile facing frame-right, in the ivory riding jacket and white riding breeches, "
  "her right hand just pulled back from the glossy black rump of the horse at frame-right, the thin silver needle between her fingers, her lips pressed into a thin satisfied line, her eyes on the horse's rump. "
  "The frame ends at the back edge of the saddle and holds only the hindquarters and tail of a tall jet-black horse at frame-right. The frame holds exactly one person, Mary, and the rear half of one black horse.",
  END_RN + LAY_RN,
  "玛丽的手刚从马臀上抽回来，马猛地一抽、后蹄向后一踢，尾巴甩起；玛丽向画面左边退开两步，眼睛盯着马的后腿。", "0—3秒侧面中景，镜头固定。",
  f"A steady side-on medium shot opens from the adopted first frame in {RN}: the hindquarters of {HS} jerk hard, one hind hoof kicks back and its tail whips up, "
  f"and {MR} jumps back two quick steps toward frame-left, the needle held against her chest, her lips pressed into a tight line and her eyes on the horse's hind legs. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是私人跑马场：黑马的臀部猛地一抽，一只后蹄向后踢出，尾巴甩起；玛丽向画面左边快退两步，银针按在胸前，嘴唇抿成一条紧线，眼睛盯着马的后腿。镜头固定不动。",
  breathy("A sharp stamp and a hoof thudding, and the creak of leather.", "一声尖锐的跺蹄声、一下蹄子的闷响和皮革的吱嘎声。"), 4911)

# 补2 莉莉在鞍上被吓到：单人＋马头（和 07 同一个构图）
T('02｜补2 莉莉在鞍上被吓到', ['LilyRiding'], ('ranch', 'lily_riding', 'black_horse'), ['ranch'],
  "Side-on medium shot, in the middle third of the frame, on the packed-earth track. The tall jet-black horse stands in profile facing frame-right, its head and neck at frame-right. "
  "Lily sits in the saddle on its back in profile facing frame-right, in the cream blouse and tan riding breeches, both hands gripping the reins at the horse's neck, her back rigid, her lips parted, her brows drawn together, her eyes wide on the horse's ears. "
  "The frame holds exactly one person, Lily, and one black horse.",
  END_RN + LAY_RN,
  "马猛地甩头、横着跨出一步，莉莉整个人被带得向前一冲又向后一仰，双手猛抓缰绳，眼睛睁大，嘴张开。", "0—3秒侧面中景，镜头固定。",
  f"A steady side-on medium shot opens from the adopted first frame in {RN}: {HS} throws its head up and takes a sharp step sideways, and {LR} is jolted forward and then back in the saddle, "
  f"her hands snatching at the reins, her mouth opening and her eyes wide on the horse's ears. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是私人跑马场：黑马猛地甩起头、横着跨出一步，莉莉在鞍上被带得向前一冲又向后一仰，双手猛抓缰绳，嘴张开，睁大眼睛看着马耳朵。镜头固定不动。",
  breathy("Hooves scuffing the dirt and the creak of leather.", "马蹄蹭过泥土的声音和皮革的吱嘎声。"), 4912)

# 补3 玛丽退到看台边看着：单人，看台在画面左边，视线落在画面里的绿色跑马场上
T('03｜补3 玛丽退到看台边看着', ['MaryRiding'], ('ranch', 'mary_riding'), ['ranch'],
  "Side-on medium shot, in the middle third of the frame, at the foot of the raised wooden grandstand stairs at frame-left. Mary stands alone from the head to the knees in profile facing frame-right, in the ivory riding jacket and white riding breeches, "
  "her left hand resting on the stair railing, the thin silver needle between the fingers of her right hand at her waist, her chin lifted, her lips pressed into a thin satisfied line, her eyes narrowed on the green field at frame-right. "
  "The frame holds exactly one person, Mary.",
  END_RN + LAY_RN,
  "玛丽站在看台台阶脚下，一只手扶着栏杆，另一手捏着银针放在腰边，下巴抬起，嘴唇抿成一条得意的细线，眼睛眯起看着画面右边的绿色跑马场。", "0—3秒侧面中景，镜头固定。",
  f"A steady side-on medium shot opens from the adopted first frame in {RN}: {MR} draws one slow breath and her chin lifts higher, her right hand slipping the needle into her jacket pocket, "
  f"her lips pressed into a thin satisfied line and her narrowed eyes fixed on the green field at frame-right. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是私人跑马场：玛丽缓缓吸了一口气，下巴抬得更高，右手把银针塞进外套口袋，嘴唇抿成一条得意的细线，眯起的眼睛盯着画面右边的绿色跑马场。镜头固定不动。",
  breathy("A light breeze and, far away, hooves pounding.", "轻轻的风声，和很远处急促的马蹄声。"), 4913)

# 补4 基利安脸色变、放下电话（替换 11）：没有任何“stays/remains”定住句
T('04｜补4 基利安脸色变放下电话', ['KillianCoat'], ('ranch', 'killian_coat'), ['ranch'],
  "Medium close-up of Killian alone, from the head to the waist, in profile facing frame-right, in the middle third of the frame, at the railing of the raised wooden grandstand in the long charcoal overcoat over a black shirt, "
  "the gold smartphone held at his right ear, his lips relaxed and slightly parted, his jaw loose, his eyes lowered on the railing. The frame holds exactly one person, Killian.",
  END_RN + LAY_RN,
  "基利安听着电话，猛地抬起头看向画面右边的松树，眉头一下拧紧，把手机从耳边慢慢放到胸前，下颌绷紧，左手攥住栏杆。", "0—3秒侧面中近景，镜头固定。",
  f"A steady medium close-up opens from the adopted first frame in {RN}: {KC} lifts his head sharply toward the dark pine trees at frame-right, his brows snapping together and his eyes narrowing, "
  f"lowers the gold phone from his ear to his chest and clenches his jaw, his left hand closing hard on the railing. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是私人跑马场：基利安猛地抬起头看向画面右边的深色松树，眉头一下拧紧、眼睛眯起，把金色手机从耳边放到胸前，下颌绷紧，左手死死攥住栏杆。镜头固定不动。",
  breathy("A light breeze and the creak of the wooden railing under his grip.", "轻轻的风声，和他手下木栏杆被攥得吱嘎作响的声音。"), 4914)

# 补5 基利安在草地上全速冲刺：单人，侧面，朝画面右边，视线落在前方的土路上（画面里的东西）
T('05｜补5 基利安全速冲过草地', ['KillianCoat'], ('woods_edge', 'killian_coat'), ['woods_edge'],
  "Side-on wide shot, in the middle third of the frame, on the dirt path along the meadow. Killian runs alone at full speed along the path in profile facing frame-right, in the long charcoal overcoat flaring behind him, "
  "his arms driving, his jaw set hard, his lips pulled back from his teeth, his eyes on the dirt path ahead of him. Dust rises behind his boots. The frame holds exactly one person, Killian.",
  END_WE + LAY_WE,
  "基利安在草地边的土路上全速冲刺，大衣在身后翻飞，双臂用力摆动，下颌咬紧，眼睛盯着前方的土路，靴子后面扬起尘土。", "0—3秒侧面宽景，镜头固定。",
  f"A steady side-on wide shot opens from the adopted first frame in {WE}: {KC} sprints along the dirt path toward frame-right, his arms driving and his overcoat flaring behind him, "
  f"his jaw set hard and his eyes on the path ahead, dust kicking up from every footfall. The camera holds still.",
  "一个稳定的侧面宽景，从已采用的开场图继续，场景是树林边缘的草地：基利安沿着土路朝画面右边冲刺，双臂用力摆动，大衣在身后翻飞，下颌咬紧，眼睛盯着前方的路，每一步都踢起尘土。镜头固定不动。",
  breathy("Boots pounding the dirt fast and a rush of wind.", "靴子飞快地踏着泥土的声音和呼啸的风声。"), 4915)

a.finish('剧本第7–8集｜接缝补镜头测试', '在马场重写测试的断点处补 3 秒的过渡拍：马被扎后的反应、在场的人、基利安听电话时的脸色变化、他冲向马的路程。', OUT)
