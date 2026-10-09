#!/usr/bin/env python3
"""第 1 集 10、11、12 号替换稿（追加批次，英语台词）。

原因（手册 7.10 O41、O42）：10 号画外敲门声被画面里男主靠墙的手“演”了出来；12 号门把手自己转动，没有手的主人，像鬼片。
改法：10、11、12 改成走廊一侧的镜头，每个镜头只拍保罗一个人（敲门、说话、拧把手的手都是他的，手臂入画）；
室内的两人镜头（10B）里没有任何敲击，手不贴墙。台词原文不变。
追加批次要求（手册 F11）：style、素材 lily/killian/room、角色 Lily/Killian/Paul 逐字复制第 1 集；paul 素材和 PaulOnScreen 角色逐字复制第 2 集；
新增素材 corridor（走廊）。
用法: 先有第 1、2 集 JSON，再  python3 tools/gen_ep1_fix.py
"""
import json, re, copy, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = os.path.join(ROOT, 'Alpha继兄的笼中吻')
BASE = os.path.join(FOLDER, '2026-10-09_第1集_制作稿_英文台词.json')
EP2 = os.path.join(FOLDER, '2026-10-09_第2集_制作稿_英文台词_追加.json')
OUT_JSON = os.path.join(FOLDER, '2026-10-09_第1集_10至12号替换_追加.json')
OUT_TXT = os.path.join(FOLDER, '2026-10-09_第1集_10至12号替换_追加_全选复制粘贴.txt')

d = copy.deepcopy(json.load(open(BASE, encoding='utf-8')))
ep2 = json.load(open(EP2, encoding='utf-8'))
d['title'] = 'Alpha继兄的笼中吻｜第1集｜10至12号替换'

d['assets'].append(next(a for a in ep2['assets'] if a['key'] == 'paul'))
d['characters']['PaulOnScreen'] = copy.deepcopy(ep2['characters']['PaulOnScreen'])
d['assets'].append({
    'key': 'corridor', 'kind': 'image', 'role': 'scene', 'label': '更衣室门外的走廊',
    'description': {
        'en': ("A quiet luxury hotel corridor outside the private fitting room: cream panelled walls with thin gold trim, warm wall sconces, plush beige carpet, "
               "and a single heavy dark-wood door with a brass lever handle, closed, on the right side of the frame. The reference fixes the look of the corridor, not any people."),
        'zh': ("私人更衣室门外安静的豪华酒店走廊：奶油色护墙板配细金边，暖色壁灯，米色厚地毯，画面右侧是一扇关着的单扇深色实木大门，带黄铜压杆把手。参考图固定走廊的样子，不带入任何人物。")},
    'generate': {'image_prompt': (
        "A photorealistic shot of an empty quiet luxury hotel corridor: cream panelled walls with thin gold trim, warm wall sconces, plush beige carpet, "
        "and on the right a single heavy dark-wood door with a brass lever handle, closed. No people."),
        'reference_keys': []}})

LEAD = "Live-action, cinematic, photorealistic with natural skin texture, shallow depth of field and warm luxurious lighting, ultra-wide 8:3 cinemascope frame. "
IMG_C = ("One coherent first frame from a photorealistic live-action romantic thriller, ultra-wide 8:3 cinemascope composition. "
         "Natural skin with visible pores, realistic fabric and materials. The fixed scene reference defines the corridor, and the character portrait defines only the named person. ")
IMG_R = ("One coherent first frame from a photorealistic live-action romantic thriller, ultra-wide 8:3 cinemascope composition. "
         "Natural skin with visible pores, realistic fabric and materials. The fixed scene reference defines the room, and the character portraits define only the named people. ")
END_C = " Warm dim light, the corridor softly blurred behind."
END_R = " Warm luxurious light, the fitting room softly blurred behind."
NOVOICE_EN = "The recording is completely free of voices: no speech, no humming, no sighs, no vocal sounds of any kind."
NOVOICE_ZH = "录音里完全没有人声：没有说话、哼声、叹息或任何发声。"
K = '[[asset:killian]]'; L = '[[asset:lily]]'; P = '[[asset:paul]]'; R = '[[asset:room]]'; C = '[[asset:corridor]]'


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
         'image_prompt': (IMG_C if refs == ['corridor'] else IMG_R) + img + end, 'visual_zh': vis_zh, 'camera_zh': cam_zh,
         'dialogue': [], 'shots': [], 'sound_en': sound[0], 'sound_zh': sound[1], 'seed': seed[0], 'dialogue_language': 'en'}
    if dlg:
        sp, tx, start = dlg
        end_t = round(start + line_seconds(tx) + 0.05, 2)
        assert end_t <= dur - 1.0, (title, end_t, dur)
        s['dialogue'].append({'speaker': sp, 'text': tx, 'start_seconds': start, 'end_seconds': end_t, 'language': 'en'})
    s['shots'].append({'start_seconds': 0, 'end_seconds': dur, 'visual_en': LEAD + shot_en, 'visual_zh': shot_zh, 'dialogue_indices': [0] if dlg else []})
    tasks.append(s)


# 10A 走廊一侧，保罗敲门（无台词）
task('10A｜走廊敲门', 5, ['PaulOnScreen'], ('corridor', 'paul'), ['corridor'],
     "Medium side-on shot of Paul alone, waist-up, in profile facing frame-right, centered in the middle third of the frame, in the corridor in front of a single heavy dark-wood door with a brass lever handle at frame-right. "
     "His right fist is raised at chest height just in front of the door, his left hand in his trouser pocket, his eyes on the door, his face relaxed and patient. His right arm, shoulder and whole fist are in the frame. Nobody else is in the frame.",
     END_C,
     "走廊里，保罗站在门前，右手握拳抬到胸口，敲门三下。门没有开。", "0—5秒保罗侧面中景，镜头固定。",
     None,
     f"A steady medium side-on shot opens from the adopted first frame in {C}: {P} alone in the corridor, in profile facing frame-right toward the closed single dark-wood door, his right fist raised at chest height in front of it. "
     "He knocks on the door three times, slowly and evenly, his whole right forearm moving, his eyes on the door. The door stays shut. Nobody speaks. The camera holds still.",
     "从开场图继续，保罗侧面中景：站在走廊里，侧脸朝右、面对关着的单扇深色木门，右拳抬到胸口、在门前。他缓慢均匀地敲门三下，整条右前臂在动，目光落在门上。门没有开。无人说话。镜头固定。",
     (f"Exactly three knocks on a heavy wooden door, slow and evenly spaced, about three-quarters of a second apart, the first after a short pause. {NOVOICE_EN}",
      f"厚重木门上恰好三声敲门声，缓慢均匀，每声间隔约四分之三秒，第一声前先停一小会儿。{NOVOICE_ZH}"))

# 10B 室内两人僵住（无台词，没有任何敲击，手不贴墙）
task('10B｜两人僵住', 5, ['Lily', 'Killian'], ('room', 'lily', 'killian'), ['room'],
     "Wide-medium three-quarter two-shot toward the single heavy dark-wood door at frame-left, both people centered in the middle third of the frame. "
     "Lily stands with her back flat against the bare cream panelled wall, between the door and Killian; Killian stands facing her, very close, both his arms hanging at his sides, no hand touching the wall or her. "
     "They are looking at each other, both still. The closed door with its brass handle is visible at the left of the frame. Both are fully visible from head to knees. Nobody else is in the frame.",
     END_R,
     "室内，两人听见门外的动静，同时僵住，只把头转向门。没有敲击声，手不贴墙。", "0—5秒室内三分之二侧面中景，两人居中，门在左，镜头固定。",
     None,
     f"A steady wide-medium three-quarter two-shot opens from the adopted first frame in {R}: {L} against the bare cream wall, {K} facing her very close with both arms hanging at his sides, the closed single door with its brass handle at frame-left. "
     "Both go completely still and turn only their heads toward the door, their eyes fixed on it. Neither touches the wall. The door stays shut. Nobody speaks. The camera holds still.",
     "从开场图继续，室内三分之二侧面中景：莉莉背靠空白的奶油色墙，基利安紧贴着她面对她，双臂垂在身侧；关着的单扇门在画面左边。两人同时僵住，只把头转向门，眼睛盯着门。谁的手都不碰墙。门一直关着。无人说话。镜头固定。",
     (f"The room is completely quiet, only a faint hush of room tone. {NOVOICE_EN}", f"房间里一片安静，只有极轻的底噪。{NOVOICE_ZH}"))

# 11 走廊一侧，保罗隔门说话
task('11｜门外的保罗', 6, ['PaulOnScreen'], ('corridor', 'paul'), ['corridor'],
     "Medium side-on shot of Paul alone, waist-up, in profile facing frame-right, centered in the middle third of the frame, in the corridor in front of a single heavy dark-wood door with a brass lever handle at frame-right, "
     "both hands at his sides, his eyes on the door, his face relaxed, his brows slightly raised. Nobody else is in the frame.",
     END_C,
     "走廊里，保罗对着关着的门说话，双手垂在身侧。", "0—6秒保罗侧面中景，镜头固定。",
     ('PaulOnScreen', "Lily? Baby, are you done changing?", 1.2),
     f"A steady medium side-on shot opens from the adopted first frame in {C}: {P} alone in the corridor, in profile facing frame-right toward the closed single dark-wood door, both hands at his sides. "
     "He speaks to the door in a casual, lightly smug voice, his eyes on the door, his lips moving with the words. His hands stay at his sides. The door stays shut. The camera holds still.",
     "从开场图继续，保罗侧面中景：站在走廊里，侧脸朝右、面对关着的单扇深色木门，双手垂在身侧。他对着门说话，声音随意、略带轻浮，目光落在门上，嘴唇随着说话在动。手不动。门没有开。镜头固定。",
     ("Quiet corridor room tone. Voices stay close and clear.", "安静的走廊底噪。人声近而清楚。"))

# 12 走廊一侧，保罗的手按下把手
task('12｜门把手', 6, ['PaulOnScreen'], ('corridor', 'paul'), ['corridor'],
     "Medium side-on shot of Paul alone, waist-up, in profile facing frame-right, centered in the middle third of the frame, in the corridor in front of a single heavy dark-wood door with a brass lever handle at frame-right. "
     "His right hand rests on the lever handle, his whole right arm and shoulder in the frame, his left hand at his side, his eyes on the door. Nobody else is in the frame.",
     END_C,
     "走廊里，保罗的右手搭在门把手上，说话，然后把把手慢慢按到底，门没开。", "0—6秒保罗侧面中景，镜头固定。",
     ('PaulOnScreen', "I'm coming in, okay?", 0.8),
     f"A steady medium side-on shot opens from the adopted first frame in {C}: {P} alone in the corridor, in profile facing frame-right, his right hand on the brass lever handle of the closed single dark-wood door. "
     "He speaks to the door in a casual voice, his eyes on it. Then his right hand presses the lever slowly downward with a loud, magnified metallic click and holds it against the latch. The door stays shut. The camera holds still.",
     "从开场图继续，保罗侧面中景：站在走廊里，侧脸朝右，右手搭在关着的单扇深色木门的黄铜压杆把手上。他对着门随意地说话，目光落在门上。然后右手把压杆慢慢按下，发出响亮的、被放大的金属咔哒声，停在锁舌上。门没有开。镜头固定。",
     ("Quiet corridor room tone, then one loud metallic click of the lever. Voices stay close and clear.", "安静的走廊底噪，然后一声响亮的压杆金属咔哒声。人声近而清楚。"))

lines = []
for t in tasks:
    lines.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
    for x in t['dialogue']:
        lines.append(f"{x['speaker']}：“{x['text']}”")
d['episodes'] = [{'title': '第1集｜10至12号替换（走廊一侧拍保罗）',
                  'summary': '替换第 1 集的 10、11、12 号：保罗在走廊里敲门、说话、拧门把手（人和手都入画）；室内两人听见后僵住（没有敲击声，手不贴墙）。',
                  'script': '\n'.join(lines), 'segments': tasks, 'dialogue_language': 'en'}]
json.dump(d, open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(OUT_TXT, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
print(f'{len(tasks)} 个任务，合计约 {sum(t["duration_seconds"] for t in tasks)} 秒 → {OUT_JSON}')
