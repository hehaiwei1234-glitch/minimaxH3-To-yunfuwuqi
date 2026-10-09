#!/usr/bin/env python3
"""生成《Alpha继兄的笼中吻》第 3 集“更衣室惊魂”制作稿（模式 3，追加批次，英语台词，美式口语）。

规则同 CLAUDE.md 第 4 节。追加批次（手册 F11）：style、素材、角色逐字复制第 2 集 JSON（它又复制自第 1 集）；本集没有新素材、没有新角色。
本集用来验证手册 7.10 的假设（写稿时当作要验证的写法，不是已证实的规则）：
  H14 画外的声音不要放在“有人的手在附近”的画面里（脚步声等放在人不动的镜头里）；
  H15 每个开场图提示词写死方位：门在画面左边，莉莉在左、基利安在右（近景也一样）；
  H16 门把手、门的镜头：门明确关着，门板占满画面，不露出门后的房间。
用法: 先有第 2 集的 JSON，再  python3 tools/gen_ep3.py
"""
import json, re, copy, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = os.path.join(ROOT, 'Alpha继兄的笼中吻')
BASE = os.path.join(FOLDER, '2026-10-09_第2集_制作稿_英文台词_追加.json')
OUT_JSON = os.path.join(FOLDER, '2026-10-09_第3集_制作稿_英文台词_追加.json')
OUT_TXT = os.path.join(FOLDER, '2026-10-09_第3集_制作稿_英文台词_追加_全选复制粘贴.txt')

d = copy.deepcopy(json.load(open(BASE, encoding='utf-8')))
d['title'] = 'Alpha继兄的笼中吻｜第3集｜更衣室惊魂'

LEAD = "Live-action, cinematic, photorealistic with natural skin texture, shallow depth of field and warm luxurious lighting, ultra-wide 8:3 cinemascope frame. "
IMG = ("One coherent first frame from a photorealistic live-action romantic thriller, ultra-wide 8:3 cinemascope composition. "
       "Natural skin with visible pores, realistic fabric and materials. The fixed scene reference defines the place, and the character portraits define only the named people. ")
# H15：固定方位（每个开场图提示词都带）
LAY_ROOM = " Fixed stage layout: the single heavy dark-wood door is at frame-left; Lily is always at frame-left of Killian."
LAY_ALC = " Fixed stage layout: the cream velvet curtain is at frame-left; Lily is always at frame-left of Killian, Killian at frame-right."
END_ROOM = " Warm luxurious light, the fitting room softly blurred behind."
END_ALC = " Warm dim light, the alcove softly blurred behind."
END_DOOR = " Warm luxurious light on the wood."
NOVOICE_EN = "The recording is completely free of voices: no speech, no humming, no sighs, no breathing sounds, no vocal sounds of any kind."
NOVOICE_ZH = "录音里完全没有人声：没有说话、哼声、叹息、呼吸声或任何发声。"
K = '[[asset:killian]]'; L = '[[asset:lily]]'; P = '[[asset:paul]]'; R = '[[asset:room]]'; A = '[[asset:alcove]]'


def line_seconds(text):
    words = len(re.findall(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)*", text))
    pauses = len(re.findall(r'[,;:]', text)) * .12 + len(re.findall(r'[!?]', text)) * .18
    return max(.35, words / 2.0 + min(pauses, 1.5))


tasks = []
seed = [3200]


def task(title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound):
    seed[0] += 1
    s = {'title': title, 'duration_seconds': dur, 'generation_seconds': dur, 'continuity': 'cut', 'depends_on_previous': False,
         'use_previous_episode_state': False, 'characters': chars, 'asset_keys': list(assets), 'image_reference_keys': list(refs),
         'image_prompt': IMG + img + end, 'visual_zh': vis_zh, 'camera_zh': cam_zh,
         'dialogue': [], 'shots': [], 'sound_en': sound[0], 'sound_zh': sound[1], 'seed': seed[0], 'dialogue_language': 'en'}
    if dlg:
        sp, tx, start = dlg
        end_t = round(start + line_seconds(tx) + 0.05, 2)
        assert end_t <= dur - 1.0, (title, end_t, dur)   # 台词后至少留 1 秒
        s['dialogue'].append({'speaker': sp, 'text': tx, 'start_seconds': start, 'end_seconds': end_t, 'language': 'en'})
    s['shots'].append({'start_seconds': 0, 'end_seconds': dur, 'visual_en': LEAD + shot_en, 'visual_zh': shot_zh, 'dialogue_indices': [0] if dlg else []})
    tasks.append(s)


def silent(sfx_en, sfx_zh):
    return (sfx_en + ' ' + NOVOICE_EN, sfx_zh + ' ' + NOVOICE_ZH)


def voiced(extra_en, extra_zh):
    return (extra_en + ' Voices stay close and clear.', extra_zh + '人声近而清楚。')


ROOM = ('room', 'killian', 'lily')
ALC = ('alcove', 'lily', 'killian')
ROOMP = ('room', 'paul')

# 01 门把手（H16：门明确关着、门板占满画面；门外的人不入画，只有把手在动）
task('01｜门把手', 5, [], ('room',), ['room'],
     "Close-up of the middle of the closed heavy dark-wood door, seen from inside the room. The dark wood panel fills the whole frame edge to edge with nothing else visible, no wall, no floor, no ceiling, no room beside it. "
     "The brass lever handle is centered in the middle third of the frame, level.",
     END_DOOR,
     "门板占满整个画面，门关着。门把手慢慢被压下，咔哒一声，停住。", "0—5秒门板近景，镜头固定。",
     None,
     f"A steady close-up opens from the adopted first frame in {R}: the closed dark-wood door filling the whole frame, the brass lever handle in the centre. "
     "The lever presses slowly downward with a loud, magnified metallic click and holds against the latch. The door stays shut. Nothing else moves. The camera holds still.",
     "从开场图继续，近景：关着的深色木门占满整个画面，黄铜压杆把手在正中。把手慢慢被压下，发出响亮的、被放大的金属咔哒声，停在锁舌上。门一直关着。其他什么都不动。镜头固定。",
     silent("One loud metallic click of a door lever.", "一声响亮的门把手金属咔哒声。"))

# 02 保罗进屋找人
task('02｜保罗进屋', 6, ['PaulOnScreen'], ROOMP, ['room'],
     "Wide-medium shot of Paul alone, full body, standing in the middle of the empty fitting room, centered in the middle third of the frame, in profile facing frame-right, "
     "his eyes on the rack of white gowns at frame-right. The heavy dark-wood door is at frame-left behind him. Nobody else is in the frame." + LAY_ROOM,
     END_ROOM,
     "保罗一个人站在空荡荡的更衣室中央，看着右边的婚纱架，喊莉莉。", "0—6秒保罗侧面中景，镜头固定。",
     ('PaulOnScreen', "Lily? Where are you?", 1.2),
     f"A steady wide-medium shot opens from the adopted first frame in {R}: {P} alone in the middle of the empty fitting room, in profile facing frame-right, his eyes on the rack of gowns at frame-right. "
     "He calls out in a casual, puzzled voice, turning only his head slightly to look along the rack. His body stays where it is. The camera holds still.",
     "从开场图继续，保罗中景：一个人站在空荡荡的更衣室中央，侧脸朝右，目光落在右边的婚纱架上。他随意而疑惑地喊着，只把头微微转动、沿着婚纱架看过去。身体不动。镜头固定。",
     voiced("Quiet room tone, a faint creak of the floor.", "安静的房间底噪，地板轻微的吱呀声。"))

# 03 婚纱后的缝隙：基利安把莉莉按在墙上
task('03｜缝隙里的两人', 5, ['Lily', 'Killian'], ALC, ['alcove'],
     "Medium two-shot, waist-up, in profile inside a narrow dim gap behind a wall of enormous layered ivory gown skirts hanging from a rail, both people centered in the middle third of the frame. "
     "Lily stands with her back flat against the wall at frame-left, her eyes wide and fixed on Killian's face, her hands at her sides; "
     "Killian stands facing her at frame-right, very close, in his black three-piece suit, his right hand pressed flat on her shoulder pinning her to the wall, his whole right arm in the frame, his left hand at his side. Nobody else is in the frame." + LAY_ALC,
     END_ALC,
     "婚纱裙摆后面狭窄的缝隙里，基利安一只手按着莉莉的肩，把她压在墙上。", "0—5秒侧面中景，两人居中，莉莉在左、基利安在右，镜头固定。",
     None,
     f"A steady medium two-shot in profile opens from the adopted first frame in {A}: {L} with her back against the wall, her eyes wide and fixed on {K}'s face; {K} facing her very close, his right hand pressed flat on her shoulder. "
     "Neither moves. Her chest rises and falls fast. His eyes stay on her face. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠墙，睁大眼睛盯着基利安的脸；基利安紧贴着她面对她，右手按在她的肩上。两人都不动。她的胸口起伏很快。他的目光一直停在她脸上。镜头固定。",
     silent("Faint rustle of heavy fabric settling.", "厚重衣料轻轻落定的沙沙声。"))

# 04 捂嘴、揽腰、提起来（大姿势放进开场图，文字只写“不动”）
task('04｜捂住嘴', 6, ['Lily', 'Killian'], ALC, ['alcove'],
     "Medium two-shot, waist-up, in profile inside the narrow dim gap behind the enormous layered ivory gown skirts, both people centered in the middle third of the frame. "
     "Killian at frame-right holds Lily at frame-left against the wall: his left arm is around her waist lifting her so that her toes only just touch the floor, his right hand is over her mouth, both his arms fully in the frame; "
     "her hands are pressed flat against his chest and her eyes are wide and fixed on his face. Nobody else is in the frame." + LAY_ALC,
     END_ALC,
     "基利安一手捂住莉莉的嘴，一手揽着她的腰把她提起来，她的脚尖刚刚碰到地。门外是保罗的脚步声。", "0—6秒侧面中景，两人居中，莉莉在左、基利安在右，镜头固定。",
     None,
     f"A steady medium two-shot in profile opens from the adopted first frame in {A}: {K} holding {L} against the wall, his right hand over her mouth and his left arm around her waist, her hands flat on his chest, her eyes wide and fixed on his face. "
     "Neither changes position. Her breathing is fast against his hand. His eyes stay on her face. The camera holds still.",
     "从开场图继续，侧面中景：基利安抱着莉莉靠在墙上，右手捂着她的嘴，左臂揽着她的腰，她的双手平按在他胸口，睁大眼睛盯着他的脸。两人姿势都不变。她的呼吸在他手下很快。他的目光一直停在她脸上。镜头固定。",
     silent("Slow footsteps on carpet a short distance away, outside the gowns.", "不远处、婚纱外面地毯上缓慢的脚步声。"))

# 05 气声（上半句）
task('05｜贴着耳朵的气声', 6, ['Lily', 'Killian'], ALC, ['alcove'],
     "Tight side-profile two-shot of heads and shoulders inside the dim gap, both people centered in the middle third of the frame. "
     "Killian's head at frame-right is lowered beside Lily's ear with his lips an inch from it, his right hand still over her mouth, his forearm in the frame; "
     "Lily at frame-left has her eyes wide and her chest rising fast. Nobody else is in the frame." + LAY_ALC,
     END_ALC,
     "基利安把嘴唇贴近莉莉的耳边，压低声音说话。", "0—6秒侧面近景，两人头肩居中，莉莉在左、基利安在右，镜头固定。",
     ('Killian', "One sound, and I'll take you here,", 1.0),
     f"A steady tight side-profile two-shot opens from the adopted first frame in {A}: {K}'s lips an inch from {L}'s ear, his right hand over her mouth. "
     "He speaks in a very low, breathy whisper, his eyes lowered. She does not move; her eyes stay wide. The camera holds still.",
     "从开场图继续，侧面近景：基利安的嘴唇离莉莉的耳朵只有一寸，右手捂着她的嘴。他用极低的气声说话，目光低垂。她不动，眼睛一直睁大。镜头固定。",
     voiced("Quiet fabric rustle. The whisper is very low and breathy.", "安静的衣料摩擦声。耳语极低，带气声。"))

# 06 气声（下半句）
task('06｜当着他的面', 5, ['Lily', 'Killian'], ALC, ['alcove'],
     "Tight side-profile two-shot of heads and shoulders inside the dim gap, both people centered in the middle third of the frame. "
     "Killian's head at frame-right is lowered beside Lily's ear with his lips an inch from it, his right hand still over her mouth, his forearm in the frame; "
     "Lily at frame-left has her eyes squeezed shut, tears on her lashes. Nobody else is in the frame." + LAY_ALC,
     END_ALC,
     "基利安继续贴着耳朵说下半句，莉莉闭紧眼睛，眼泪流下来。", "0—5秒侧面近景，两人头肩居中，莉莉在左、基利安在右，镜头固定。",
     ('Killian', "in front of him.", 0.8),
     f"A steady tight side-profile two-shot opens from the adopted first frame in {A}: {K}'s lips an inch from {L}'s ear, his right hand over her mouth. "
     "He speaks in the same very low, breathy whisper. A tear runs down her cheek and her eyes stay squeezed shut. The camera holds still.",
     "从开场图继续，侧面近景：基利安的嘴唇离莉莉的耳朵只有一寸，右手捂着她的嘴。他用同样极低的气声说话。一滴眼泪从她脸颊滑下，她的眼睛一直紧闭。镜头固定。",
     voiced("Quiet fabric rustle. The whisper is very low and breathy.", "安静的衣料摩擦声。耳语极低，带气声。"))

# 07 保罗嘟囔（只转头）
task('07｜去哪了', 5, ['PaulOnScreen'], ROOMP, ['room'],
     "Medium shot of Paul alone, waist-up, in profile facing frame-right, centered in the middle third of the frame, in the fitting room, one hand scratching the back of his neck, "
     "his brows drawn together, his eyes on the rack of white gowns at frame-right. The heavy dark-wood door is at frame-left behind him. Nobody else is in the frame." + LAY_ROOM,
     END_ROOM,
     "保罗一只手挠着后颈，皱着眉，嘟囔了一句。", "0—5秒保罗侧面中景，镜头固定。",
     ('PaulOnScreen', "Where'd she go?", 0.8),
     f"A steady medium shot opens from the adopted first frame in {R}: {P} in profile facing frame-right, one hand at the back of his neck, his brows drawn together, his eyes on the rack of gowns at frame-right. "
     "He mutters the words, then turns only his head toward the door at frame-left. His body stays where it is. The camera holds still.",
     "从开场图继续，保罗中景：侧脸朝右，一只手放在后颈，眉头皱着，目光落在右边的婚纱架上。他嘟囔着说话，然后只把头转向左边的门。身体不动。镜头固定。",
     voiced("Quiet room tone.", "安静的房间底噪。"))

# 08 关着的门（H16：门板占满画面；关门的瞬间用剪辑交代，只留一声锁舌轻响）
task('08｜门关上了', 5, [], ('room',), ['room'],
     "Close-up of the middle of the closed heavy dark-wood door, seen from inside the room. The dark wood panel fills the whole frame edge to edge with nothing else visible, no wall, no floor, no ceiling, no room beside it. "
     "The brass lever handle is centered in the middle third of the frame, level and still.",
     END_DOOR,
     "门已经关上，门板占满画面，门把手不动。一声轻轻的锁舌声，然后安静。", "0—5秒门板近景，镜头固定。",
     None,
     f"A steady close-up opens from the adopted first frame in {R}: the closed dark-wood door filling the whole frame, the brass lever handle in the centre, still. "
     "After a moment a soft latch click is heard, then silence. Nothing moves. The camera holds still.",
     "从开场图继续，近景：关着的深色木门占满整个画面，黄铜压杆把手在正中，不动。片刻之后听到一声轻轻的锁舌声，然后安静。什么都不动。镜头固定。",
     silent("One soft latch click, then silence.", "一声轻轻的锁舌声，然后安静。"))

# 09 脱力滑落（姿势在开场图里：莉莉已经坐在地上）
task('09｜瘫坐在地', 6, ['Lily', 'Killian'], ROOM, ['room'],
     "Wide-medium two-shot, both people fully visible, centered in the middle third of the frame. "
     "Lily sits on the carpet with her back against the bare cream wall at frame-left, her ivory gown pooled around her, one hand at her throat, her eyes on the floor in front of her; "
     "Killian stands a step away at frame-right in his black three-piece suit, both hands at the knot of his tie, straightening it, his eyes lowered on her. Nobody else is in the frame." + LAY_ROOM,
     END_ROOM,
     "莉莉脱力地坐在地上，背靠着墙，手按着脖子。基利安站在旁边，整理领带，低头看她。", "0—6秒两人中景，莉莉在左、基利安在右，镜头固定。",
     None,
     f"A steady wide-medium two-shot opens from the adopted first frame in {R}: {L} sitting on the carpet against the wall, one hand at her throat, her eyes on the floor; {K} standing a step away, both hands at his tie. "
     "Her shoulders rise and fall with fast breaths. He finishes straightening the knot, his eyes on her. The camera holds still.",
     "从开场图继续，两人中景：莉莉坐在地毯上靠着墙，一只手按着脖子，目光落在地面；基利安站在一步之外，双手在领带结上。她的肩膀随着急促的呼吸起伏。他把领带结整理好，目光一直在她身上。镜头固定。",
     silent("Faint fabric rustle and the soft tick of a tie being straightened.", "轻微的衣料摩擦声，领带被理好的细响。"))

# 10-12 基利安的三句话（原长句拆开）
task('10｜三千万美金', 6, ['Lily', 'Killian'], ROOM, ['room'],
     "Wide-medium two-shot, both people fully visible, centered in the middle third of the frame. "
     "Lily sits on the carpet against the bare cream wall at frame-left, her ivory gown pooled around her, her eyes on a thick cream document folder lying on the carpet in front of her knees; "
     "Killian stands a step away at frame-right in his black three-piece suit, his right hand in his trouser pocket and his left hand at his side, his eyes lowered on her. Nobody else is in the frame." + LAY_ROOM,
     END_ROOM,
     "莉莉坐在地上，面前地毯上放着一份厚厚的文件。基利安站在旁边，低头看着她，开口。", "0—6秒两人中景，莉莉在左、基利安在右，镜头固定。",
     ('Killian', "Your foster parents owe me thirty million.", 1.2),
     f"A steady wide-medium two-shot opens from the adopted first frame in {R}: {L} sitting on the carpet, her eyes on the document folder in front of her knees; {K} standing a step away, his eyes on her. "
     "He speaks flatly and without hurry, his voice low and cold, his hands staying where they are. She does not look up. The camera holds still.",
     "从开场图继续，两人中景：莉莉坐在地毯上，目光落在膝前的文件夹上；基利安站在一步之外，目光落在她身上。他平平淡淡、不慌不忙地开口，声音低而冷，手不动。她没有抬头。镜头固定。",
     voiced("Quiet room tone.", "安静的房间底噪。"))

task('11｜搬进我的别墅', 6, ['Killian'], ('room', 'killian'), ['room'],
     "Medium shot of Killian alone, waist-up, in profile facing frame-left, centered in the middle third of the frame, in his black three-piece suit, one hand in his trouser pocket, "
     "his eyes lowered on a woman sitting on the floor at frame-left, just outside the frame, his face cold and unreadable, his jaw tight. Nobody else is in the frame." + LAY_ROOM,
     END_ROOM,
     "基利安一个人入画，侧脸朝左，低头看着画面外坐在地上的莉莉，继续说。", "0—6秒基利安侧面中景，镜头固定。",
     ('Killian', "Move into my villa. Starting today.", 1.0),
     f"A steady medium shot opens from the adopted first frame in {R}: {K} in profile facing frame-left, one hand in his trouser pocket, his eyes lowered on the woman sitting on the floor at frame-left, just outside the frame. "
     "He speaks slowly and quietly, his voice low and cold. His hands stay still. The camera holds still.",
     "从开场图继续，基利安中景：侧脸朝左，一只手插在裤兜里，目光低下去看着左边画面外坐在地上的女人。他慢慢地、压低声音说话，声音低而冷。手不动。镜头固定。",
     voiced("Quiet room tone.", "安静的房间底噪。"))

task('12｜保罗会失去一切', 6, ['Killian'], ('room', 'killian'), ['room'],
     "Medium close-up of Killian alone, chest-up, in profile facing frame-left, centered in the middle third of the frame, in his black three-piece suit, "
     "his eyes lowered on a woman sitting on the floor at frame-left, just outside the frame, his face cold and unreadable, his jaw tight. Nobody else is in the frame." + LAY_ROOM,
     END_ROOM,
     "基利安的侧脸近一点，目光还是落在画面外的莉莉身上，说出最后一句。", "0—6秒基利安侧面中近景，镜头固定。",
     ('Killian', "Or Paul loses everything by morning.", 1.0),
     f"A steady medium close-up opens from the adopted first frame in {R}: {K} in profile facing frame-left, his eyes lowered on the woman sitting on the floor at frame-left, just outside the frame. "
     "He speaks slowly and quietly, his voice low and cold. Only his lips move. The camera holds still.",
     "从开场图继续，基利安中近景：侧脸朝左，目光低下去看着左边画面外坐在地上的女人。他慢慢地、压低声音说话，声音低而冷。只有嘴唇在动。镜头固定。",
     voiced("Quiet room tone.", "安静的房间底噪。"))

# 13 莉莉拿着文件
task('13｜颤抖的文件', 5, ['Lily'], ('room', 'lily'), ['room'],
     "Medium close-up of Lily alone, chest-up, sitting against the bare cream wall, centered in the middle third of the frame, in the ivory wedding gown, "
     "both hands holding a thick cream document folder open at chest height, her whole forearms in the frame, her eyes lowered on the page, her lips pressed together. Nobody else is in the frame." + LAY_ROOM,
     END_ROOM,
     "莉莉双手捧着打开的文件，低头看，手在发抖。", "0—5秒莉莉近景，镜头固定。",
     None,
     f"A steady medium close-up opens from the adopted first frame in {R}: {L} holding the open document folder in both hands at chest height, her eyes on the page. "
     "Her hands tremble and the page shivers. Her eyes move once along the page and stop. The camera holds still.",
     "从开场图继续，莉莉近景：双手在胸口高度捧着打开的文件夹，目光落在纸页上。她的手在发抖，纸页跟着颤。她的视线沿着纸页移动一下就停住了。镜头固定。",
     silent("Faint rustle of paper.", "纸张轻轻的沙沙声。"))

# 14 莉莉抬头
task('14｜抬起头', 5, ['Lily'], ('room', 'lily'), ['room'],
     "Medium close-up of Lily alone, chest-up, in profile facing frame-right, centered in the middle third of the frame, in the ivory wedding gown, "
     "the document folder held against her chest in both hands, her head lifted and her eyes fixed on a man standing above her at frame-right, just outside the frame, her eyes wet, her lips parted. Nobody else is in the frame." + LAY_ROOM,
     END_ROOM,
     "莉莉抱着文件抬起头，眼睛湿着，盯着右边画面外的基利安。", "0—5秒莉莉侧面近景，镜头固定。",
     None,
     f"A steady medium close-up opens from the adopted first frame in {R}: {L} in profile facing frame-right, the folder held against her chest, her eyes fixed on the man above her at frame-right, just outside the frame. "
     "Her eyes shine and a tear gathers and runs down. Her hands stay holding the folder. The camera holds still.",
     "从开场图继续，莉莉近景：侧脸朝右，文件夹抱在胸前，目光盯着右边画面外站在她上方的男人。她的眼睛发亮，一滴泪聚起来滑下。双手一直抱着文件夹。镜头固定。",
     silent("Faint fabric rustle, then near silence.", "轻微的衣料摩擦声，然后几乎无声。"))

# 15 基利安的眼神（成片里在这里黑屏）
task('15｜掠夺的眼神', 5, ['Killian'], ('room', 'killian'), ['room'],
     "Close-up of Killian's face alone, in profile facing frame-left, centered in the middle third of the frame, his eyes lowered on a woman sitting on the floor at frame-left, just outside the frame, "
     "his eyes narrowed and unblinking, his jaw tight, his lips pressed together. Nobody else is in the frame." + LAY_ROOM,
     END_ROOM,
     "基利安的侧脸特写，眼睛眯起，目光落在画面外的莉莉身上。（成片里在这里黑屏）", "0—5秒基利安侧面特写，镜头固定。",
     None,
     f"A steady close-up opens from the adopted first frame in {R}: {K}'s face in profile facing frame-left, his eyes narrowed and fixed on the woman on the floor at frame-left, just outside the frame. "
     "His gaze does not waver and his jaw tightens slowly. He does not speak. The camera holds still.",
     "从开场图继续，基利安面部特写：侧脸朝左，眼睛眯起，盯着左边画面外坐在地上的女人。目光一动不动，下颌慢慢收紧。他不说话。镜头固定。",
     silent("Tense, near-silent room tone.", "紧绷、几乎无声的房间底噪。"))

lines = []
for t in tasks:
    lines.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
    for x in t['dialogue']:
        lines.append(f"{x['speaker']}：“{x['text']}”")
d['episodes'] = [{'title': '第3集｜更衣室惊魂',
                  'summary': '保罗推门进来找莉莉，更衣室中央空无一人。基利安把莉莉按在婚纱裙摆后面狭窄的缝隙里，捂住她的嘴，用气声威胁。保罗嘟囔着离开、关上门，莉莉脱力坐倒。基利安丢下一份《债务重组及个人抵押协议》，要她搬进别墅，否则保罗明天就会破产。',
                  'script': '\n'.join(lines), 'segments': tasks, 'dialogue_language': 'en'}]
json.dump(d, open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(OUT_TXT, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
print(f'{len(tasks)} 个任务，合计约 {sum(t["duration_seconds"] for t in tasks)} 秒 → {OUT_JSON}')
