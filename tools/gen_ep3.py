#!/usr/bin/env python3
"""第 3 集“更衣室惊魂”制作稿（追加批次，英语台词）——按 8 条通用规律重写（2026-10-09 16:40）。
替换掉原来的 15 任务版（那版写在规律整理之前）。素材和角色从第 2 集 JSON 复制（手册 F11），没有新素材。

这一版用到的规律（对话里 hh 看过的那 8 条）：
 1 只写想要的，不提不想要的（不写 Nobody speaks / no mirror；人数写成 exactly N people）
 2 H3 只认动词不认程度词（不写 slightly / only / small）
 3 开场图决定一切（人数、位置、手、门全写进开场图；固定布局句子；承接前段只在“同一批人、同一地点”时打开）
 4 每个动作和声音要有看得见的来源（关门、拿文件夹都写出是谁的手）
 5 声音不听画面的话（台词后留 1 秒以上；一个任务一句）
 6 提示词里除了台词不放像话的句子（动作描述不转述台词）
 7 一个任务一个镜头
 8 稳的写法：侧面中景、双方身体入画、手的位置写清楚
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, silent, voiced

BASE = '2026-10-09_第2集_制作稿_英文台词_追加.json'
OUT = '2026-10-09_第3集_制作稿_英文台词_追加'
b = Batch(BASE, json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))['title'], 3200)

K = '[[asset:killian]]'; L = '[[asset:lily]]'; P = '[[asset:paul]]'; R = '[[asset:room]]'; A = '[[asset:alcove]]'
LAY_DOOR = " Fixed stage layout: the heavy dark-wood door is at frame-left."
LAY_PAIR = " Fixed stage layout: Lily is always at frame-left of Killian, Killian at frame-right."
LAY_ROOM = " Fixed stage layout: the heavy dark-wood door is at frame-left; Lily is always at frame-left of Killian."
END_ROOM = " Warm light from the chandelier and wall sconces."
END_ALC = " Warm dim light, the layers of white gowns softly blurred behind them."
ZH = []      # 每个任务开场图提示词的中文全译（写进说明）
CHAIN = []   # 每个任务是否承接前段


def T(flag, title, dur, chars, assets, refs, img, end, img_zh, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound):
    b.task(title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound)
    b.tasks[-1]['depends_on_previous'] = flag
    ZH.append(img_zh); CHAIN.append(flag)


# 01 ------------------------------------------------------------------------------------------------
T(False, '01｜门把手转动，保罗进屋', 6, ['PaulOnScreen'], ('room', 'paul'), ['room'],
  "Wide shot from inside the fitting room: the closed heavy dark-wood door with its brass lever handle at frame-left, seen at an angle, the rack of long white gowns in garment covers along the back wall, the ivory velvet couch at frame-right, thick carpet in the foreground. The frame holds the room, the door and the gowns.",
  END_ROOM + LAY_DOOR,
  "试衣间里的广角镜头：画面左边是关着的厚重深色木门，铜色压杆门把手清晰可见，门斜着入画；靠后墙是一排装在防尘罩里的长白婚纱，画面右边是象牙色丝绒沙发，前景是厚地毯。画面里是房间、门和婚纱。吊灯和壁灯的暖光。固定布局：厚重深色木门在画面左边。",
  "门把手压下，门被推开，保罗走进来，叫莉莉。", "0—6秒广角固定镜头，门在画面左边。",
  ('PaulOnScreen', 'Lily? Where are you?', 2.4),
  f"A steady wide shot opens from the adopted first frame in {R}: the closed heavy dark-wood door at frame-left with its brass lever handle in view, the rack of white gowns at the back wall. The handle presses down and the door swings inward; {P} steps through the doorway in his navy blazer, his right hand on the handle, his eyes on the room. The camera holds still.",
  "一个稳定的广角镜头，从已采用的开场图继续，场景是试衣间：画面左边是关着的厚重深色木门，铜色压杆门把手清晰可见，后墙是一排白色婚纱。门把手压下，门向里打开；保罗穿着藏青色西装外套走进门口，右手还握在门把手上，眼睛看着房间。镜头固定不动。",
  voiced("The brass handle clicks and the door swings open; soft footsteps on thick carpet.", "铜把手咔哒一声，门打开；脚步轻轻落在厚地毯上。"))

# 02 ------------------------------------------------------------------------------------------------
T(True, '02｜保罗环顾房间', 5, ['PaulOnScreen'], ('room', 'paul'), ['room'],
  "Medium shot of Paul standing on the carpet at the centre of the fitting room, centered in the middle third of the frame, in profile facing frame-right, in his navy blazer, his brows drawn together, his eyes on the rack of long white gowns at the back wall. The heavy dark-wood door stands open at frame-left behind him. The frame holds exactly one person, Paul.",
  END_ROOM + LAY_DOOR,
  "中景：保罗站在试衣间中央的地毯上，在画面中间三分之一，侧身朝画面右边，穿藏青色西装外套，眉头皱起，眼睛看着后墙那排长白婚纱。厚重深色木门敞开着，在他身后的画面左边。画面里恰好一个人：保罗。吊灯和壁灯的暖光。固定布局：门在画面左边。",
  "保罗站在房间中央，皱着眉环顾，目光扫过婚纱架。", "0—5秒中景固定镜头。", None,
  f"A steady medium shot opens from the adopted first frame in {R}: {P} in profile on the carpet, brows drawn together, his eyes on the rack of long white gowns at the back wall. His eyes travel along the rack from one end to the other and his jaw tightens. The camera holds still.",
  "一个稳定的中景，从已采用的开场图继续，场景是试衣间：保罗侧身站在地毯上，眉头皱起，眼睛看着后墙那排长白婚纱。他的目光沿着婚纱架从一头扫到另一头，下颌收紧。镜头固定不动。",
  silent("Faint room tone and the soft hum of the chandelier.", "淡淡的房间底噪和吊灯的轻响。"))

# 03 ------------------------------------------------------------------------------------------------
T(False, '03｜缝隙里的两人', 5, ['Lily', 'Killian'], ('alcove', 'lily', 'killian'), ['alcove'],
  "Side-on medium two-shot in a narrow gap between rows of huge hanging white gowns, both people centered in the middle third of the frame. Lily stands with her back against the cream wall at frame-left in the ivory wedding gown with its back open, her eyes wide and fixed on Killian's face. Killian stands facing her at frame-right in his black three-piece suit, his right hand over her mouth and his left arm around her waist, his eyes lowered on her. Both are fully visible from head to knees. The frame holds exactly two people: Lily and Killian.",
  END_ALC + LAY_PAIR,
  "侧面中景双人镜头，在一排排巨大的悬挂白婚纱之间的狭窄缝隙里，两个人都在画面中间三分之一。莉莉背靠奶油色的墙站在画面左边，穿象牙色露背婚纱，睁大眼睛看着基利安的脸。基利安面对她站在画面右边，穿黑色三件套西装，右手捂住她的嘴，左臂搂着她的腰，眼睛垂下看着她。两人从头到膝盖完整出镜。画面里恰好两个人：莉莉和基利安。暖色昏暗的光，层层白婚纱在他们身后柔和虚化。固定布局：莉莉始终在基利安左边，基利安在右边。",
  "基利安把莉莉按在墙上，右手捂住她的嘴，左臂搂着她的腰；莉莉睁大眼睛，胸口剧烈起伏。", "0—5秒侧面中景，两人居中，镜头固定。", None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {A}: {L} with her back against the cream wall at frame-left, her eyes wide and fixed on {K}'s face; {K} at frame-right, his right hand over her mouth and his left arm around her waist, his eyes lowered on her. Her chest rises and falls fast and her right hand grips his left forearm. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是更衣隔间：莉莉背靠奶油色的墙在画面左边，睁大眼睛看着基利安的脸；基利安在画面右边，右手捂着她的嘴，左臂搂着她的腰，眼睛垂下看着她。她的胸口剧烈起伏，右手抓住他的左前臂。镜头固定不动。",
  silent("Soft rustling of heavy fabric.", "厚重布料的轻轻摩擦声。"))

# 04 ------------------------------------------------------------------------------------------------
T(True, '04｜气声警告一', 6, ['Lily', 'Killian'], ('alcove', 'lily', 'killian'), ['alcove'],
  "Tight side-profile two-shot of heads and shoulders in the gap between the hanging gowns, both people centered in the middle third of the frame. Lily at frame-left with her back against the cream wall, her eyes wide and wet, Killian's right hand over her mouth. Killian at frame-right, his head lowered beside her ear, his eyes on her face. The frame holds exactly two people: Lily and Killian.",
  END_ALC + LAY_PAIR,
  "头肩的侧面近景双人镜头，在悬挂的婚纱之间的缝隙里，两个人都在画面中间三分之一。莉莉在画面左边背靠奶油色的墙，睁大湿润的眼睛，基利安的右手捂着她的嘴。基利安在画面右边，头低下贴在她耳边，眼睛看着她的脸。画面里恰好两个人：莉莉和基利安。暖色昏暗的光，层层白婚纱在他们身后柔和虚化。固定布局：莉莉始终在基利安左边，基利安在右边。",
  "基利安贴着莉莉的耳朵，用极低的气声说话，右手仍捂着她的嘴。", "0—6秒侧面近景，两人居中，镜头固定。",
  ('Killian', 'Make one sound.', 1.0),
  f"A steady tight side-profile two-shot opens from the adopted first frame in {A}: {K}'s head lowered beside {L}'s ear, his right hand over her mouth; {L}'s eyes wide and wet, fixed on his face. He speaks in a very low, breathy whisper, his eyes on her face. The camera holds still.",
  "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是更衣隔间：基利安的头低下贴在莉莉耳边，右手捂着她的嘴；莉莉睁大湿润的眼睛，看着他的脸。他用极低的气声说话，眼睛看着她的脸。镜头固定不动。",
  voiced("He speaks in a very low, breathy whisper close to her ear.", "他贴着她的耳朵，用极低的气声说话。"))

# 05 ------------------------------------------------------------------------------------------------
T(True, '05｜气声警告二', 6, ['Lily', 'Killian'], ('alcove', 'lily', 'killian'), ['alcove'],
  "Tight side-profile two-shot of heads and shoulders in the gap between the hanging gowns, both people centered in the middle third of the frame. Lily at frame-left with her back against the cream wall, her eyes squeezed shut, a tear on her cheek, Killian's right hand over her mouth. Killian at frame-right, his head lowered beside her ear, his eyes on her closed eyes. The frame holds exactly two people: Lily and Killian.",
  END_ALC + LAY_PAIR,
  "头肩的侧面近景双人镜头，在悬挂的婚纱之间的缝隙里，两个人都在画面中间三分之一。莉莉在画面左边背靠奶油色的墙，紧紧闭着眼睛，脸颊上有一滴泪，基利安的右手捂着她的嘴。基利安在画面右边，头低下贴在她耳边，眼睛看着她紧闭的双眼。画面里恰好两个人：莉莉和基利安。暖色昏暗的光，层层白婚纱在他们身后柔和虚化。固定布局：莉莉始终在基利安左边，基利安在右边。",
  "莉莉紧闭双眼，一滴泪滑下脸颊，肩膀发抖；基利安贴着她的耳朵低声说话。", "0—6秒侧面近景，两人居中，镜头固定。",
  ('Killian', "I'll take you in front of him.", 1.0),
  f"A steady tight side-profile two-shot opens from the adopted first frame in {A}: {K}'s head lowered beside {L}'s ear, his right hand over her mouth; {L}'s eyes squeezed shut and a tear running down her cheek. He speaks in a very low, breathy whisper. Her shoulders shake. The camera holds still.",
  "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是更衣隔间：基利安的头低下贴在莉莉耳边，右手捂着她的嘴；莉莉紧闭双眼，一滴泪滑下脸颊。他用极低的气声说话。她的肩膀发抖。镜头固定不动。",
  voiced("He speaks in a very low, breathy whisper close to her ear.", "他贴着她的耳朵，用极低的气声说话。"))

# 06 ------------------------------------------------------------------------------------------------
T(False, '06｜保罗嘟囔', 5, ['PaulOnScreen'], ('room', 'paul'), ['room'],
  "Medium shot of Paul in profile facing frame-right, standing in the open doorway at frame-left in his navy blazer, his right hand on the edge of the door, his brows drawn together, his eyes moving over the fitting room at frame-right. The frame holds exactly one person, Paul.",
  END_ROOM + LAY_DOOR,
  "中景：保罗侧身朝画面右边，站在画面左边敞开的门口，穿藏青色西装外套，右手扶着门的边缘，眉头皱起，眼睛扫视着画面右边的试衣间。画面里恰好一个人：保罗。吊灯和壁灯的暖光。固定布局：门在画面左边。",
  "保罗站在门口，皱着眉看房间，嘟囔了一句。", "0—5秒中景固定镜头。",
  ('PaulOnScreen', "Where'd she go?", 0.8),
  f"A steady medium shot opens from the adopted first frame in {R}: {P} in profile in the open doorway at frame-left, his right hand on the edge of the door, his brows drawn together, his eyes on the fitting room at frame-right. He speaks with a puzzled frown, his eyes moving over the room. The camera holds still.",
  "一个稳定的中景，从已采用的开场图继续，场景是试衣间：保罗侧身站在画面左边敞开的门口，右手扶着门的边缘，眉头皱起，眼睛看着画面右边的试衣间。他带着困惑的皱眉说话，目光在房间里移动。镜头固定不动。",
  voiced("Soft room tone.", "轻轻的房间底噪。"))

# 07 ------------------------------------------------------------------------------------------------
T(True, '07｜保罗关门离开', 5, ['PaulOnScreen'], ('room', 'paul'), ['room'],
  "Medium shot of Paul in profile in the doorway at frame-left, his right hand on the edge of the open heavy dark-wood door, one foot on the threshold, his eyes on the fitting room at frame-right. The frame holds exactly one person, Paul.",
  END_ROOM + LAY_DOOR,
  "中景：保罗侧身站在画面左边的门口，右手扶着敞开的厚重深色木门的边缘，一只脚踩在门槛上，眼睛看着画面右边的试衣间。画面里恰好一个人：保罗。吊灯和壁灯的暖光。固定布局：门在画面左边。",
  "保罗退出门外，用手把门拉上。", "0—5秒中景固定镜头。", None,
  f"A steady medium shot opens from the adopted first frame in {R}: {P} in profile in the doorway at frame-left, his right hand on the edge of the open door. He steps backward out through the doorway and pulls the heavy dark-wood door closed with his right hand until it shuts. The camera holds still.",
  "一个稳定的中景，从已采用的开场图继续，场景是试衣间：保罗侧身站在画面左边的门口，右手扶着敞开的门的边缘。他向后退出门外，右手把厚重的深色木门拉上，直到关严。镜头固定不动。",
  silent("The door shuts with a solid latch click.", "门关上，锁舌发出沉实的咔哒声。"))

# 08 ------------------------------------------------------------------------------------------------
T(False, '08｜莉莉瘫坐在地', 6, ['Lily', 'Killian'], ('room', 'killian', 'lily'), ['room'],
  "Side-on medium two-shot in the fitting room, both people centered in the middle third of the frame. Lily stands with her back against the cream wall at frame-left in the ivory wedding gown, her shoulders heaving, her eyes wide. Killian stands facing her at frame-right in his black three-piece suit, his right hand at his side and his eyes lowered on her. The closed heavy dark-wood door is at the far left edge of the frame. Both are fully visible from head to knees. The frame holds exactly two people: Lily and Killian.",
  END_ROOM + LAY_ROOM,
  "试衣间里的侧面中景双人镜头，两个人都在画面中间三分之一。莉莉背靠奶油色的墙站在画面左边，穿象牙色露背婚纱，肩膀剧烈起伏，睁大眼睛。基利安面对她站在画面右边，穿黑色三件套西装，右手垂在身侧，眼睛垂下看着她。关着的厚重深色木门在画面最左边缘。两人从头到膝盖完整出镜。画面里恰好两个人：莉莉和基利安。吊灯和壁灯的暖光。固定布局：门在画面左边，莉莉始终在基利安左边。",
  "门关上后，莉莉脱力，顺着墙滑坐到地毯上，大口喘气；基利安站着看着她。", "0—6秒侧面中景，两人居中，镜头固定。", None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {R}: {L} with her back against the cream wall at frame-left, shoulders heaving, {K} at frame-right with his eyes lowered on her. {L} slides down the wall until she sits on the carpet, her gown spreading around her, her chest heaving, her eyes on the floor; {K} stays standing at frame-right, his eyes following her down. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是试衣间：莉莉背靠奶油色的墙在画面左边，肩膀剧烈起伏，基利安在画面右边，眼睛垂下看着她。莉莉顺着墙滑下去，坐在地毯上，婚纱在她周围铺开，胸口剧烈起伏，眼睛看着地面；基利安仍站在画面右边，目光跟着她落下去。镜头固定不动。",
  silent("The soft rustle of a heavy gown settling on the carpet.", "厚重婚纱落在地毯上的轻轻摩擦声。"))

# 09 ------------------------------------------------------------------------------------------------
T(True, '09｜三千万美金', 6, ['Lily', 'Killian'], ('room', 'killian', 'lily'), ['room'],
  "Side-on medium two-shot in the fitting room, both people centered in the middle third of the frame. Lily sits on the carpet at frame-left with her back against the cream wall, her palms on the carpet, her eyes lifted to Killian. Killian stands at frame-right looking down at her in his black three-piece suit, his right hand at his tie, a document folder held in his left hand at his side. Both are fully visible. The frame holds exactly two people: Lily and Killian.",
  END_ROOM + LAY_ROOM,
  "试衣间里的侧面中景双人镜头，两个人都在画面中间三分之一。莉莉坐在画面左边的地毯上，背靠奶油色的墙，手掌按在地毯上，眼睛抬起看着基利安。基利安站在画面右边，穿黑色三件套西装，低头看着她，右手放在领带上，左手垂在身侧拿着一个文件夹。两人完整出镜。画面里恰好两个人：莉莉和基利安。吊灯和壁灯的暖光。固定布局：门在画面左边，莉莉始终在基利安左边。",
  "基利安居高临下整理领带，松手把文件夹丢在莉莉面前的地毯上，说出债务。", "0—6秒侧面中景，两人居中，镜头固定。",
  ('Killian', 'Your foster parents owe me thirty million.', 1.2),
  f"A steady side-on medium two-shot opens from the adopted first frame in {R}: {K} stands at frame-right looking down at {L}, his right hand straightening his tie, a document folder in his left hand; {L} sits on the carpet at frame-left, her palms on the carpet, her eyes lifted to his face. His left hand opens and the folder drops onto the carpet in front of her. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是试衣间：基利安站在画面右边低头看着莉莉，右手整理领带，左手拿着一个文件夹；莉莉坐在画面左边的地毯上，手掌按着地毯，眼睛抬起看着他的脸。他的左手松开，文件夹掉在她面前的地毯上。镜头固定不动。",
  voiced("A soft thud as the folder lands on the carpet.", "文件夹落在地毯上，发出一声轻响。"))

# 10 ------------------------------------------------------------------------------------------------
T(True, '10｜搬进我的别墅', 6, ['Killian'], ('room', 'killian'), ['room'],
  "Medium close-up of Killian alone, in profile facing frame-left, centered in the middle third of the frame, in his black three-piece suit, his right hand in his trouser pocket, his eyes lowered on a woman sitting on the carpet at frame-left, just outside the frame, his face cold and unreadable. Behind him the cream panelled wall. The frame holds exactly one person, Killian.",
  END_ROOM + LAY_ROOM,
  "中近景：基利安一个人，侧身朝画面左边，在画面中间三分之一，穿黑色三件套西装，右手插在裤兜里，眼睛垂下看着坐在地毯上的女人（在画面左边、画面之外），脸冷淡、看不出情绪。他身后是奶油色的镶板墙。画面里恰好一个人：基利安。吊灯和壁灯的暖光。固定布局：门在画面左边，莉莉始终在基利安左边。",
  "基利安冷冷地低头看着地上的莉莉，说出要求。", "0—6秒中近景固定镜头。",
  ('Killian', 'Move into my villa. Starting today.', 1.0),
  f"A steady medium close-up opens from the adopted first frame in {R}: {K} in profile facing frame-left, one hand in his trouser pocket, his eyes lowered on the woman sitting on the carpet at frame-left, just outside the frame, his jaw tight. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是试衣间：基利安侧身朝画面左边，一只手插在裤兜里，眼睛垂下看着坐在地毯上的女人（在画面左边、画面之外），下颌收紧。镜头固定不动。",
  voiced("Cold, controlled room tone.", "冷静克制的房间底噪。"))

# 11 ------------------------------------------------------------------------------------------------
T(True, '11｜保罗会失去一切', 6, ['Killian'], ('room', 'killian'), ['room'],
  "Medium close-up of Killian alone, in profile facing frame-left, centered in the middle third of the frame, in his black three-piece suit, his right hand in his trouser pocket, his chin lifted, his eyes narrowed and fixed on a woman sitting on the carpet at frame-left, just outside the frame. Behind him the cream panelled wall. The frame holds exactly one person, Killian.",
  END_ROOM + LAY_ROOM,
  "中近景：基利安一个人，侧身朝画面左边，在画面中间三分之一，穿黑色三件套西装，右手插在裤兜里，下巴抬起，眯着眼睛盯着坐在地毯上的女人（在画面左边、画面之外）。他身后是奶油色的镶板墙。画面里恰好一个人：基利安。吊灯和壁灯的暖光。固定布局：门在画面左边，莉莉始终在基利安左边。",
  "基利安抬着下巴、眯着眼，说出最后通牒。", "0—6秒中近景固定镜头。",
  ('Killian', 'Or Paul loses everything by morning.', 1.0),
  f"A steady medium close-up opens from the adopted first frame in {R}: {K} in profile facing frame-left, one hand in his trouser pocket, his chin lifted, his eyes narrowed and fixed on the woman sitting on the carpet at frame-left, just outside the frame. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是试衣间：基利安侧身朝画面左边，一只手插在裤兜里，下巴抬起，眯着眼睛盯着坐在地毯上的女人（在画面左边、画面之外）。镜头固定不动。",
  voiced("Cold, controlled room tone.", "冷静克制的房间底噪。"))

# 12 ------------------------------------------------------------------------------------------------
T(False, '12｜颤抖着捡起文件', 5, ['Lily'], ('room', 'lily'), ['room'],
  "Medium close-up of Lily alone, in profile facing frame-right, centered in the middle third of the frame, sitting on the carpet in the ivory wedding gown, both hands holding an open document folder at chest height, her eyes on the page, her lips trembling. Behind her the cream panelled wall. The frame holds exactly one person, Lily.",
  END_ROOM + LAY_DOOR,
  "中近景：莉莉一个人，侧身朝画面右边，在画面中间三分之一，穿象牙色露背婚纱坐在地毯上，双手在胸前拿着一份翻开的文件夹，眼睛看着纸页，嘴唇发抖。她身后是奶油色的镶板墙。画面里恰好一个人：莉莉。吊灯和壁灯的暖光。固定布局：门在画面左边。",
  "莉莉颤抖着拿起文件夹，翻开，看着上面的内容。", "0—5秒中近景固定镜头。", None,
  f"A steady medium close-up opens from the adopted first frame in {R}: {L} in profile facing frame-right on the carpet, both hands holding the open document folder at chest height, her eyes on the page. Her hands tremble and her eyes move across the page. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是试衣间：莉莉侧身朝画面右边坐在地毯上，双手在胸前拿着翻开的文件夹，眼睛看着纸页。她的手在发抖，目光在纸页上移动。镜头固定不动。",
  silent("Faint paper rustle and quiet room tone.", "淡淡的纸张摩擦声和安静的房间底噪。"))

# 13 ------------------------------------------------------------------------------------------------
T(True, '13｜莉莉抬头', 5, ['Lily'], ('room', 'lily'), ['room'],
  "Medium close-up of Lily alone, in profile facing frame-right, centered in the middle third of the frame, the document folder held against her chest, her eyes lifted to a man standing above her at frame-right, just outside the frame, tears on her lashes. The frame holds exactly one person, Lily.",
  END_ROOM + LAY_DOOR,
  "中近景：莉莉一个人，侧身朝画面右边，在画面中间三分之一，文件夹抱在胸前，眼睛抬起看着站在她上方的男人（在画面右边、画面之外），睫毛上挂着泪。画面里恰好一个人：莉莉。吊灯和壁灯的暖光。固定布局：门在画面左边。",
  "莉莉抬起头，含泪看向基利安。", "0—5秒中近景固定镜头。", None,
  f"A steady medium close-up opens from the adopted first frame in {R}: {L} in profile facing frame-right, the folder held against her chest. Her chin lifts and her eyes rise from the page to the man above her at frame-right, just outside the frame; tears gather on her lower lashes. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是试衣间：莉莉侧身朝画面右边，文件夹抱在胸前。她的下巴抬起，目光从纸页上升起，看向站在她上方的男人（在画面右边、画面之外）；泪水聚在她的下睫毛上。镜头固定不动。",
  silent("Quiet room tone.", "安静的房间底噪。"))

# 14 ------------------------------------------------------------------------------------------------
T(False, '14｜掠夺的眼神', 5, ['Killian'], ('room', 'killian'), ['room'],
  "Close-up of Killian's face alone, in profile facing frame-left, centered in the middle third of the frame, his eyes fixed on the woman on the carpet at frame-left, just outside the frame, a cold glint in his eyes, his lips pressed together. The frame holds exactly one person, Killian.",
  END_ROOM + LAY_ROOM,
  "特写：基利安的脸，只有他一个人，侧面朝画面左边，在画面中间三分之一，眼睛盯着地毯上的女人（在画面左边、画面之外），眼里一道冷光，嘴唇抿紧。画面里恰好一个人：基利安。吊灯和壁灯的暖光。固定布局：门在画面左边，莉莉始终在基利安左边。",
  "基利安的特写，眼神带着掠夺的光。（成片里在这里黑屏）", "0—5秒面部特写，镜头固定。", None,
  f"A steady close-up opens from the adopted first frame in {R}: {K}'s face in profile facing frame-left, his eyes fixed on the woman at frame-left, just outside the frame. His eyes narrow and the warm chandelier light catches them. The camera holds still.",
  "一个稳定的特写，从已采用的开场图继续，场景是试衣间：基利安的侧脸朝画面左边，眼睛盯着画面左边、画面之外的女人。他的眼睛眯起，吊灯的暖光落在他眼里。镜头固定不动。",
  silent("A low, tense hum of room tone.", "低沉紧绷的房间底噪。"))

# ---- 汇总 -----------------------------------------------------------------------------------------
b.finish('第3集｜更衣室惊魂',
         '保罗推门进来找莉莉，基利安捂住她的嘴躲在婚纱缝隙里，用气声威胁她。保罗找不到人，嘟囔着关门离开。莉莉瘫坐在地，基利安丢下一份文件：你养父母欠我三千万，搬进我的别墅，否则保罗明天就会失去一切。',
         OUT)

# ---- 说明（含每个任务英文提示词的中文全译）-----------------------------------------------------------
d = b.d
segs = d['episodes'][0]['segments']
md = []
md.append("# 第 3 集制作稿（英语台词、追加批次）：怎么用（2026-10-09 16:40，按 8 条通用规律重写）\n")
md.append(f"文件：`{OUT}_全选复制粘贴.txt`（和同名 `.json` 内容一样）。**14 个任务，8:3 宽屏，合计 {sum(s['duration_seconds'] for s in segs)} 秒，种子 3201–3214。** 这一版**替换**了之前的 15 任务版（那版写在规律整理之前，请不要再用）。\n")
md.append("## 一、怎么跑\n")
md.append("1. 接在第 2 集之后追加，素材和角色沿用第 2 集（没有新素材，和第 2 集的声明逐字相同）。\n2. 设置照旧：视频/对白共用次数 = 1，对白时间余量 = 0。追加窗口不要勾“每集／总／任务秒数”。\n3. 这一集里有 8 个任务打开了“承接前段”（见下表“承接”一列）：**只在“前一个任务和这一个是同一批人、同一个地点”时才打开**，换人或换地点时关掉，避免把上一段的人带进来；这样链条也短，重做时连带重做的段落少。**承接前段是否有用，还在等第 2 集重跑的结果。**\n4. 重做某一段，会连带重做它后面“承接”的段落。\n")
md.append("## 二、14 个任务\n")
md.append("| 号 | 名字 | 秒 | 在场 | 承接 | 英语台词 | 种子 |\n|---|---|---|---|---|---|---|")
for i, s in enumerate(segs):
    dl = f"{s['dialogue'][0]['speaker']}：{s['dialogue'][0]['text']}" if s['dialogue'] else '（无台词）'
    md.append(f"| {i+1:02d} | {s['title'].split('｜')[1]} | {s['duration_seconds']} | {len(s['characters'])} | {'是' if CHAIN[i] else '否'} | {dl} | {s['seed']} |")
md.append("\n## 三、给 H3 的提示词（中文全译，一个字不漏）\n")
md.append("每个任务的视频提示词前面还会加这句固定的风格话：**“真人实拍，电影感，写实，皮肤有自然质感，浅景深，温暖奢华的光线，超宽 8:3 宽银幕画面。”** 开场图提示词前面也有一段固定的开头：**“一张来自写实真人浪漫惊悚片的完整首帧，超宽 8:3 宽银幕构图。皮肤自然，能看到毛孔，布料和材质真实。固定的场景参考图决定地点，人物肖像只决定被点名的人。”** 下面不再重复。\n")
for i, s in enumerate(segs):
    md.append(f"### {i+1:02d}｜{s['title'].split('｜')[1]}（{s['duration_seconds']} 秒）")
    md.append(f"- **开场图：** {ZH[i]}")
    md.append(f"- **视频：** {s['shots'][0]['visual_zh']}")
    md.append(f"- **声音：** {s['sound_zh']}")
    if s['dialogue']:
        md.append(f"- **台词（单独传给插件）：** {s['dialogue'][0]['speaker']}：“{s['dialogue'][0]['text']}”")
    md.append("")
md.append("## 四、这一版写法上和旧版的区别（对应 8 条规律）\n")
md.append("- 不再写 “Nobody speaks / Nobody else is in the frame”，人数改写成 “The frame holds exactly N people”。\n- 不再写 “slightly / only / small” 这类程度词。\n- 保罗进屋并入 01 号（门把手压下、门打开、保罗走进来是同一个镜头），保罗关门（07 号）写明是他的右手拉上的；旧版里没有人的“关门声”任务已去掉。\n- 原剧本里“把她整个人提起来、双脚悬空”的动作没有拍（H3 做不稳），改成她背靠墙、被捂住嘴；亲密威胁按美国平台惯例保持暗示。\n- 威胁那句原来拆成两个任务，改成两句完整的话：“Make one sound.” 和 “I'll take you in front of him.”。\n- 开场图里把门的位置、两人的左右位置都写成固定布局。\n")
md.append("## 五、我预计会出问题的地方（没试过，只是判断）\n")
md.append("- **08 号“顺着墙滑坐到地上”**是整集最难的动作，可能出现身体穿插或下落不自然。\n- **01 号**开场图里没有保罗，保罗的脸来自他的人物图，进门后是否像他要看。\n- **同一批 6 秒的台词任务**，声音常常到片尾才结束，验收时听结尾（04、05、09、10、11 号）。\n- **承接前段**的效果还没验证，如果开场图里被带进了不该有的人，请告诉我号码。\n")
open(os.path.join(FOLDER, '2026-10-09_第3集_说明_英文台词_追加.md'), 'w', encoding='utf-8').write('\n'.join(md))
print('说明已写')
