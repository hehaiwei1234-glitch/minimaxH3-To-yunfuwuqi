#!/usr/bin/env python3
"""补拍包 2：大冲突表演重拍（2026-10-10，hh 10:17 反馈第 5 集 04→05、第 6 集 05 的表演呆滞、动作缓慢、接不上）。

基于合并稿（第 5 集＋第 6 集 A＋第 6 集 B）的 JSON（素材、人物逐字复制，F11），不新增素材。3 个任务各 6 秒，种子 3711–3713。
  补9   第 5 集 04 重拍：两人入画（不再把“画外的女人”当视线目标），杯子在基利安手里，从头到尾有呼吸声
  补10  第 5 集 05 重拍：捏碎酒杯，整段 6 秒都有动作和反应，允许低吼和喘息（不许说话）
  补11  第 6 集 05 重拍：红酒泼裙，由基利安的手把酒杯打在她身上，开场图画“动作之前”，她猛地后仰、倒吸气
和原稿相比一次改了 5 处（见说明“改了什么”），所以这次是“整套新写法 vs 旧写法”，不是单变量对照。
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER

BASE = '合并稿/合并_第5集+第6集A+第6集B_制作稿_追加.json'
OUT = '补拍/补拍包2_大冲突表演重拍_追加'
SERIES_TITLE = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))['title']

b = Batch(BASE, SERIES_TITLE, 3710)
ZH = []


def T(title, dur, chars, assets, refs, img, end, img_zh, vis_zh, cam_zh, shot_en, shot_zh, sound):
    s = b.task(title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, None, shot_en, shot_zh, sound)
    s['depends_on_previous'] = False
    ZH.append(img_zh)
    return s


BED = '[[asset:bedroom]]'; LS = '[[asset:lily_shirt]]'; KW = '[[asset:killian_wolf]]'
BR = '[[asset:ballroom]]'; KT = '[[asset:killian_tux]]'; MY = '[[asset:mary]]'
END_B = " Low amber lamp light, the bedroom softly blurred behind. Fixed stage layout: the huge dark-wood bed is at frame-left; the single dark-wood door is at frame-right."
Z_END_B = "床头灯低低的琥珀色光，卧室在后面柔和虚化。固定布局：巨大的深色木床在画面左边；唯一的一扇深色木门在画面右边。"
END_R = " Warm golden chandelier light, the ballroom softly blurred behind. Fixed stage layout: the wide marble staircase is at frame-left; the long banquet table is at frame-right. Mary is always at frame-right of Killian."
Z_END_R = "温暖的金色吊灯光，宴会厅在后面柔和虚化。固定布局：宽阔的大理石楼梯在画面左边；长长的宴会桌在画面右边。玛丽始终在基利安右边。"

# 补9：第 5 集 04 重拍 ------------------------------------------------------------------------------------------
T('补9｜第5集04重拍：两人入画', 6, ['LilyShirt', 'KillianWolf'], ('bedroom', 'lily_shirt', 'killian_wolf'), ['bedroom'],
  "Medium side-on two-shot, both people from the head to the knees, in the middle third of the frame. "
  "Lily at frame-left sits pressed back against the dark headboard of the huge bed in the oversized white shirt, in profile facing frame-right, both hands clutching her collar, her eyes wide with fear on his face, her lips trembling. "
  "Killian at frame-right stands beside the bed in the black silk robe, in profile facing frame-left, a crystal whiskey tumbler in his right hand at hip height, his shoulders rigid, his jaw clenched, his eyes glowing a dark gold and fixed on her face. "
  "The frame holds exactly two people: Lily and Killian.",
  END_B,
  "侧面中景双人镜头，两个人都是头到膝盖，在画面中间三分之一。莉莉在画面左边，穿宽大的白衬衫，背紧贴着巨大的床的深色床头板坐着，侧身朝画面右边，双手揪着衣领，睁大惊恐的眼睛看着他的脸，嘴唇发抖。"
  "基利安在画面右边，穿黑色丝绸睡袍站在床边，侧身朝画面左边，右手在胯部高度拿着一只水晶威士忌杯，肩膀僵硬，下颌咬紧，眼睛发着暗金色的光、盯着她的脸。画面里恰好两个人：莉莉和基利安。" + Z_END_B,
  "莉莉缩在床头，揪着衣领，惊恐地看着他；基利安站在床边，杯子拿在手里，金色的眼睛盯着她，喘着粗气。", "0—6秒侧面中景双人，镜头固定。",
  f"A steady side-on medium two-shot opens from the adopted first frame in {BED}: {LS} at frame-left presses back against the headboard in profile facing frame-right, her eyes on his face; "
  f"{KW} at frame-right stands in profile facing frame-left, the tumbler in his right hand, his jaw clenched, his gold eyes on her face. "
  "He drags in a ragged breath through flared nostrils and his shoulders heave, his knuckles whitening around the tumbler. "
  "She flinches and her hands clutch her collar tighter, her lips trembling. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是庄园主卧：莉莉在画面左边，背紧贴床头板，侧身朝画面右边，眼睛看着他的脸；基利安在画面右边，侧身朝画面左边站着，右手拿着酒杯，下颌咬紧，金色的眼睛盯着她的脸。"
  "他从张开的鼻孔里拖进一口粗重的气，肩膀起伏，指节在酒杯上攥得发白。她猛地一缩，双手把衣领揪得更紧，嘴唇发抖。镜头固定不动。",
  ("Heavy ragged breathing close by, a faint trembling gasp and the soft creak of the bed. No words are spoken.",
   "近处沉重、粗糙的呼吸声，一声微微发颤的倒吸气，床轻轻吱嘎一声。没有人说话。"))

# 补10：第 5 集 05 重拍 -----------------------------------------------------------------------------------------
T('补10｜第5集05重拍：捏碎酒杯', 6, ['KillianWolf'], ('bedroom', 'killian_wolf'), ['bedroom'],
  "Medium close-up of Killian alone, chest-up, in profile facing frame-left, in the middle third of the frame, in the black silk robe, "
  "his right hand at chest height around a crystal whiskey tumbler, long dark claw-like nails pressing against the glass, his hand, forearm and sleeve in the frame so the hand clearly belongs to him, "
  "his eyes glowing a dark gold and fixed on the glass, his jaw clenched, his lips pulled tight. The frame holds exactly one person, Killian.",
  END_B,
  "基利安一个人的中近景，胸部以上，侧身朝画面左边，在画面中间三分之一，穿黑色丝绸睡袍，右手在胸口高度握着一只水晶威士忌杯，又长又黑的爪子状指甲压在玻璃上，手、前臂和袖子都在画面里，所以手明确属于他，眼睛发着暗金色的光、盯着酒杯，下颌咬紧，嘴唇绷紧。画面里恰好一个人：基利安。" + Z_END_B,
  "基利安盯着手里的酒杯，一下捏碎；他猛地抬头，露出尖牙低吼，肩膀随着粗重的呼吸起伏。", "0—6秒中近景，镜头固定。",
  f"A steady medium close-up opens from the adopted first frame in {BED}: {KW} in profile facing frame-left, his gold eyes on the tumbler in his right hand. "
  "His fist snaps shut; the glass cracks, bursts, and shards and amber whiskey spray over his hand and onto the floor. "
  "His head jerks up, his lips curl back from sharp fangs in a snarl, and his shoulders heave with each hard breath. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是庄园主卧：基利安侧身朝画面左边，金色的眼睛盯着右手里的酒杯。他的拳头猛地攥紧；酒杯裂开、炸成碎片，碎片和琥珀色的威士忌喷在他手上、溅到地上。"
  "他猛地抬头，嘴唇向后拉开，露出尖牙，发出低吼，肩膀随着每一口粗重的呼吸起伏。镜头固定不动。",
  ("A sharp crack, crystal shattering and whiskey spattering on the floor, then a low guttural snarl and heavy ragged breathing. No words are spoken.",
   "一声清脆的裂响，水晶玻璃碎裂、威士忌溅在地上，接着是低沉的喉音低吼和沉重粗糙的呼吸。没有人说话。"))

# 补11：第 6 集 05 重拍 -----------------------------------------------------------------------------------------
T('补11｜第6集05重拍：红酒泼裙', 6, ['Mary', 'KillianTux'], ('ballroom', 'mary', 'killian_tux'), ['ballroom'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame. "
  "Killian at frame-left in the black tuxedo, in profile facing frame-right, his right hand at his side, his face cold, his jaw set, his eyes level on Mary's face. "
  "Mary at frame-right in the white satin cocktail dress, in profile facing frame-left, a crystal glass of red wine in her right hand at chest height, her left hand reaching toward his sleeve, a sweet smug smile, her eyes on his face. "
  "The frame holds exactly two people: Killian and Mary.",
  END_R,
  "侧面中景双人镜头，两个人都是头到膝盖，在画面中间三分之一。基利安在画面左边，穿黑色燕尾礼服，侧身朝画面右边，右手垂在身侧，脸色冰冷，下颌绷紧，眼睛平视着玛丽的脸。"
  "玛丽在画面右边，穿白色缎面鸡尾酒裙，侧身朝画面左边，右手在胸口高度端着一杯红酒，左手伸向他的袖子，带着甜腻得意的笑，眼睛看着他的脸。画面里恰好两个人：基利安和玛丽。" + Z_END_R,
  "玛丽端着红酒、甜笑着去挽基利安；他手一抬，把酒杯猛地打在她胸口，红酒泼了她一裙子；她猛地后仰、倒吸一口气，他冷冷瞪着她。", "0—6秒侧面中景双人，镜头固定。",
  f"A steady side-on medium two-shot opens from the adopted first frame in {BR}: {KT} at frame-left, his eyes on her face; "
  f"{MY} at frame-right, a glass of red wine in her right hand, her left hand reaching for his sleeve, her sweet smug smile. "
  "His right hand snaps up and knocks the glass hard against her chest; red wine sloshes out and splashes down the front of her white dress. "
  "She jerks back with a sharp gasp, her mouth wide open and her eyes wide; he lowers his hand and glares at her, his face cold, his jaw set. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是晚宴大厅：基利安在画面左边，眼睛看着她的脸；玛丽在画面右边，右手端着一杯红酒，左手伸向他的袖子，带着甜腻得意的笑。"
  "他的右手猛地抬起，把酒杯重重打在她胸口；红酒泼出来，顺着她白裙子的前襟泼下去。她猛地向后仰，倒吸一口气，嘴巴张得老大、眼睛睁大；他放下手瞪着她，脸色冰冷，下颌绷紧。镜头固定不动。",
  ("A sharp gasp, a crystal glass knocking hard, wine splashing and a few drops pattering on the marble floor. No words are spoken.",
   "一声尖锐的倒吸气，水晶杯被重重撞了一下，红酒泼溅，几滴落在大理石地面上。没有人说话。"))

b.finish('剧本补拍包2｜大冲突表演重拍', '大冲突表演重拍 3 个（第 5 集 04、05，第 6 集 05），写法与原稿不同，用来对照呆滞／动作过慢／接不上的原因', OUT)
segs = b.tasks

md = []
md.append("# 补拍包 2：大冲突表演重拍（3 个任务，各 6 秒，种子 3711–3713）\n")
md.append("2026-10-10 写。起因：你 10:17 说第 5 集 04→05、第 6 集 05 的“大冲突”表演很假：呆滞、没有呼吸声、动作缓慢、前后镜头接不上（04 冒出金发女人、05 开场手里突然有杯子；红酒是女人自己倒的）。我重看之后，这几处确实是**我的写法造成的**，所以重拍。\n")
md.append("## 零、怎么追加、插件里显示第几集（＝剧本第几集）\n")
md.append("| 追加顺序 | 文件 | 插件里显示 |\n|---|---|---|")
md.append("| ① | 补拍包 1（8 个任务，上一条回复给的） | 第 10 集 |")
md.append("| ② | **补拍包 2（本文件，3 个任务）** | **第 11 集：剧本补拍包2｜大冲突表演重拍** |")
md.append("| ③ | 第 7–10 集合并稿 | 剧本第 7/8/9/10/10B 集 = 插件第 12/13/14/15/16 集（不是以前说的 11–15） |\n")
md.append("**建议你先跑完①②，看完补9、补10、补11 这三个片，再把③贴进去**：马场四集里有同样的写法（见回复第 8 点），看完这三个片我可以当轮按结果改马场稿。设置照旧：视频/对白共用次数 = 1，对白时间余量 = 0，追加窗口不要勾“每集／总／任务秒数”。预计 3 × 7 = 21 分钟（上限推算）。\n")
md.append("## 一、做完能得到什么\n")
md.append("三个片都**不放台词**，整段 6 秒都排满动作和反应。和原稿相比一次改了 5 处（所以这是“整套新写法 vs 旧写法”，不是单变量对照；如果好了，以后再拆开看是哪一处起作用）：\n")
md.append("1. **整段排满**：原稿的动作只占前 1–2 秒，后面 3–4 秒写的是“手一直攥着、两人留在原处”；新写法写成 起因→结果→反应→余波，整 6 秒都有可看的动作。")
md.append("2. **不写“定住句”**：去掉了 “His hand stays clenched / Both stay where they are” 这类句子。")
md.append("3. **声音句允许呼吸、喘息、低吼，只禁说话**：原稿写的是“没有呼吸声、没有任何发声”，结果近乎静音。")
md.append("4. **开场图画“动作发生之前”**：原稿 06-05 的开场图里玛丽已经张着嘴震惊了，等于先画了结果。")
md.append("5. **动词用猛的、写明是一下子完成的**（snaps、knocks hard、jerks），反应也写成身体反应（后仰、倒吸气、肩膀起伏）。\n")
md.append("| 补拍 | 替换哪里 | 做完怎么算成功 |\n|---|---|---|")
md.append("| 补9 | 第 5 集 04 号 | 莉莉和基利安**两个人都在画面里**，没有金发陌生女人；杯子在基利安手里；能听到粗重呼吸；两个人都在动 |")
md.append("| 补10 | 第 5 集 05 号 | 一下子捏碎酒杯（不是慢慢裂开）；碎片、酒液溅出；之后他有抬头、低吼、肩膀起伏，不是定格；声音里有碎裂声和低吼／呼吸 |")
md.append("| 补11 | 第 6 集 05 号（**补拍包 1 里的补7 作废**：补7 是原稿原样重拍，会再出现同样的动作问题，只是黑边的对照） | **基利安的手把酒杯打到她身上**（不是她自己倒）；速度是“一下”；她后仰、倒吸气；他不再是麻木的脸 |\n")
md.append("**剪辑位置：** 第 5 集：5-03 → 补9 → 补10 → 5-06；第 6 集：6A 的 04 → 补11 → 6A 的 06。\n")
md.append("## 二、全部提示词中文全译\n")
for s, zh in zip(segs, ZH):
    md.append(f"### {s['title']}（{s['duration_seconds']} 秒，种子 {s['seed']}，无台词）\n")
    md.append(f"- **开场图提示词：** {zh}")
    md.append(f"- **视频文字：** {s['shots'][0]['visual_zh']}")
    md.append(f"- **声音：** {s['sound_zh']}\n")
md.append("## 三、预计会出问题的地方\n")
md.append("- **补11：** “手把杯子打在她胸口”是近身接触动作，H3 可能还是画成她自己倒、或者手没碰到杯子；红酒可能不泼在裙子上。开场图先看：玛丽必须在笑、基利安的手垂在身侧。\n- **补10：** 杯子碎裂可能还是慢；尖牙是不是出现（上次出现了）；**这次写了允许低吼，可能会出现像说话的声音**，验收时听。\n- **补9：** 床头板、门的位置每次都可能变；两个人的朝向（莉莉朝右、基利安朝左）看开场图。\n- 写法检查报了 3 条“无台词片没写完全没有人声”：**是故意的**（这次要测允许呼吸声）。\n- 三个片的开场图都是重新生成的，**脸和房间可能和原来略有不同**，拼起来不顺眼就不要。\n")
open(os.path.join(FOLDER, '补拍/补拍包2_说明.md'), 'w', encoding='utf-8').write('\n'.join(md))
print('说明已写')
