#!/usr/bin/env python3
"""生成《Alpha继兄的笼中吻》第 1 集制作稿（模式 3，h3-production-draft v1）。

按 CLAUDE.md 第 4 节的写稿规则：一个任务一个连续镜头、一人一句短台词、不用镜子、视线有具体目标、
抓人者的手臂入画、姿势放进开场图、镜头固定。台词一字不改，长句按语气拆成几个任务。
用法:  python3 tools/gen_ep1.py      （写出 Alpha继兄的笼中吻/ 下的 JSON 和 txt）
"""
import json, re, copy, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, 'packs', '改进稿_12任务', '改进稿_制作稿.json')
OUT_JSON = os.path.join(ROOT, 'Alpha继兄的笼中吻', '2026-10-08_第1集_制作稿.json')
OUT_TXT = os.path.join(ROOT, 'Alpha继兄的笼中吻', '2026-10-08_第1集_制作稿_全选复制粘贴.txt')

base = json.load(open(BASE, encoding='utf-8'))
d = copy.deepcopy(base)
d['title'] = 'Alpha继兄的笼中吻｜第1集｜禁忌的更衣室（精修版）'
d['dialogue_language'] = 'zh'

# ---- 素材：房间去掉镜子，留出一面空墙用来“壁咚” -------------------------------------------
for a in d['assets']:
    if a['key'] == 'room':
        a['description'] = {
            'en': ("The private VIP fitting room of a high-end bridal boutique: cream walls with gold molding, a heavy dark-wood door with a brass handle in the left wall, "
                   "a rack of long white gowns in garment covers along the back wall, a wide bare stretch of plain cream panelled wall to the right of the gown rack, "
                   "an ivory velvet couch against the right wall and thick carpet, lit warmly by a crystal chandelier and wall sconces. "
                   "The reference fixes the room layout and decor, not any people."),
            'zh': ("高端婚纱店的VIP私人更衣室：奶油色墙面配金色线脚，左墙一扇带黄铜把手的厚重深色木门，后墙挂着一排罩着防尘袋的白色长婚纱，"
                   "婚纱架右边是一大段空白的奶油色护墙板墙面，右墙边有象牙色丝绒沙发和厚地毯，水晶吊灯与壁灯的暖光。"
                   "参考图固定房间布局与陈设，不带入任何人物。")}
        a['generate']['image_prompt'] = (
            "A photorealistic wide shot of an empty luxury VIP fitting room in a high-end bridal boutique: cream walls with gold molding, a heavy dark-wood door with a brass handle on the left wall, "
            "a rack of long white wedding gowns in garment covers along the back wall, a wide bare stretch of plain cream panelled wall to the right of the gown rack, "
            "an ivory velvet couch against the right wall, thick carpet, warm light from a crystal chandelier and wall sconces. No people.")

LEAD = "Live-action, cinematic, photorealistic with natural skin texture, shallow depth of field and warm luxurious lighting, ultra-wide 8:3 cinemascope frame. "
IMG = ("One coherent first frame from a photorealistic live-action romantic thriller, ultra-wide 8:3 cinemascope composition. "
       "Natural skin with visible pores, realistic fabric and materials. The fixed scene reference defines the room, and the character portraits define only the named people. ")
IMGEND = " Warm luxurious light, the fitting room softly blurred behind."
SOUND_DLG_EN = "Quiet room tone and a faint brush of fabric. Voices stay close and clear."
SOUND_DLG_ZH = "安静的房间底噪和轻微的衣料摩擦声。人声近而清楚。"
NOVOICE_EN = "The recording is completely free of voices: no speech, no humming, no sighs, no vocal sounds of any kind."
NOVOICE_ZH = "录音里完全没有人声：没有说话、哼声、叹息或任何发声。"
K = '[[asset:killian]]'; L = '[[asset:lily]]'; R = '[[asset:room]]'

PIN = ("Lily stands with her back flat against the bare cream panelled wall; Killian stands facing her, very close, a head and a half taller, "
       "his right hand holding her left wrist against the wall at shoulder height and his left forearm braced on the wall beside her head. ")

def line_seconds(text):
    """复制插件 dialogue_plan.line_seconds 的中文算法（汉字 / 4 秒 + 标点停顿），让时间窗刚好通过插件预算检查。"""
    han = len(re.findall(r'[\u3400-\u9fff]', text))
    pauses = len(re.findall(r'[，,；;：:]', text)) * .12 + len(re.findall(r'[。！？!?]', text)) * .18
    return max(.35, han / 4.0 + min(pauses, 1.5))

tasks = []
seed = [3000]

def task(title, dur, chars, img, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound, assets=('room', 'lily', 'killian')):
    seed[0] += 1
    sound_en, sound_zh = sound
    s = {'title': title, 'duration_seconds': dur, 'generation_seconds': dur, 'continuity': 'cut', 'depends_on_previous': False,
         'use_previous_episode_state': False, 'characters': chars, 'asset_keys': list(assets), 'image_reference_keys': ['room'],
         'image_prompt': IMG + img + IMGEND, 'visual_zh': vis_zh, 'camera_zh': cam_zh,
         'dialogue': [], 'shots': [], 'sound_en': sound_en, 'sound_zh': sound_zh, 'seed': seed[0], 'dialogue_language': 'zh'}
    if dlg:
        sp, tx, start = dlg
        end = round(start + line_seconds(tx) + 0.05, 2)
        assert end <= dur - 1.0, (title, end, dur)   # 台词后至少留 1 秒（插件最低要求 0.65 秒）
        s['dialogue'].append({'speaker': sp, 'text': tx, 'start_seconds': start, 'end_seconds': end, 'language': 'zh'})
    s['shots'].append({'start_seconds': 0, 'end_seconds': dur, 'visual_en': LEAD + shot_en, 'visual_zh': shot_zh, 'dialogue_indices': [0] if dlg else []})
    tasks.append(s)

def dlg_sound(extra_en='', extra_zh=''):
    return ((extra_en + ' ' if extra_en else '') + SOUND_DLG_EN, (extra_zh + ' ' if extra_zh else '') + SOUND_DLG_ZH)

def silent_sound(sfx_en, sfx_zh):
    return (sfx_en + ' ' + NOVOICE_EN, sfx_zh + ' ' + NOVOICE_ZH)

# 01 拉链声
task('01｜拉链声', 5, ['Lily', 'Killian'],
     "Wide-medium side-on two-shot, both people centered in the middle third of the frame. Lily stands in profile facing frame-left toward the heavy dark-wood door, in the ivory wedding gown with its long back zipper still closed, both hands holding the front of the bodice at her chest. "
     "Killian stands directly behind her, very close, in his black three-piece suit, his left hand with the platinum wristwatch pinching the zipper pull between her shoulder blades, his right arm hanging at his side. Both are fully visible from head to knees. Nobody else is in the frame.",
     "基利安站在莉莉身后，一把拉开婚纱拉链，莉莉惊呼回头。", "0—5秒侧面中景，两人居中，镜头固定。",
     ('Lily', '啊！', 1.4),
     f"A steady wide-medium side-on two-shot opens from the adopted first frame in {R}: {L} in profile with her eyes on the door, {K} close behind her with his left hand on the zipper pull. In one hard, smooth motion he pulls the zipper straight down along her spine to her waist and the back of the gown falls open, baring her back. She gasps and turns only her head toward him, her eyes wide and fixed on his face. The camera holds still.",
     "从开场图继续，侧面中景：莉莉侧身、视线落在门上，基利安紧贴在她身后，左手捏着拉链头。他一把干脆地把拉链沿脊背拉到腰际，婚纱后背敞开。她惊呼，只把头转向他，睁大眼睛盯着他的脸。镜头固定。",
     dlg_sound("A sharp, clear zipper rasp from top to bottom.", "一声清脆的拉链声，从上拉到下。"))

# 02 五年没见
task('02｜五年没见', 6, ['Lily', 'Killian'],
     "Wide-medium side-on three-quarter two-shot, both people centered in the middle third of the frame. " + PIN +
     "Lily's ivory gown is open at the back; her head is turned away toward the door with her eyes shut. Killian's face is lowered beside her neck with his eyes closed. Both are fully visible from head to knees. Nobody else is in the frame.",
     "基利安把莉莉按在墙上，埋在她颈边深吸一口气，低声说话。", "0—6秒侧面中景，两人居中，镜头固定。",
     ('Killian', '五年没见，我的好妹妹……', 1.5),
     f"A steady wide-medium side-on three-quarter two-shot opens from the adopted first frame in {R}: {L} with her back against the bare cream wall, head turned toward the door, eyes shut; {K} close in front of her, his right hand holding her left wrist at shoulder height, his left forearm braced on the wall beside her head. He draws one slow, deep breath beside her neck, a hand's width from her skin, eyes closed. Still beside her neck, he speaks in a low, husky voice. She keeps her eyes shut and her head turned toward the door. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠空白墙面、头转向门、闭着眼；基利安紧贴在她面前，右手把她的左手腕按在肩高处，左前臂撑在她头旁的墙上。他在她颈边一手宽的距离深吸一口气，闭着眼，然后仍贴着她的颈边低声说话。她始终闭眼、头偏向门。镜头固定。",
     dlg_sound())

# 03 这么让我发疯
task('03｜这么让我发疯', 7, ['Lily', 'Killian'],
     "Tight side-profile two-shot of heads and shoulders, both people centered in the middle third of the frame. Killian's face is lowered beside Lily's neck, his eyes closed; Lily's head is turned away toward the door, her eyes shut and her lips pressed together, her bare shoulder and chestnut hair in the frame. No hands are visible. Nobody else is in the frame.",
     "基利安贴在莉莉颈边，低声说出第二句。", "0—7秒侧面近景，两人头肩居中，镜头固定。",
     ('Killian', '你身上的味道，还是这么让我发疯。', 1.8),
     f"A steady tight side-profile two-shot opens from the adopted first frame in {R}: {K}'s face lowered beside {L}'s neck, eyes closed; {L}'s head turned toward the door, eyes shut, lips pressed together. After a slow breath he opens his eyes, looking at her neck, and speaks in a low, husky voice. She does not move. The camera holds still.",
     "从开场图继续，侧面近景：基利安的脸贴在莉莉颈边、闭着眼；莉莉头偏向门、闭眼、抿着嘴。他缓缓呼吸后睁开眼，看着她的颈侧，低声说话。她一动不动。镜头固定。",
     dlg_sound())

# 04 你放开我
task('04｜你放开我', 7, ['Lily', 'Killian'],
     "Wide-medium side-on three-quarter two-shot, both people centered in the middle third of the frame. " + PIN +
     "Lily's head is tilted up and her eyes are on Killian's face, her brows drawn together and her eyes wet; her right hand rests flat on his chest. Killian looks down at her face with a cold, blank expression. Both are fully visible from head to knees. Nobody else is in the frame.",
     "莉莉抬头看着基利安，压低声音怒斥，右手抵着他的胸口。", "0—7秒侧面中景，两人居中，镜头固定。",
     ('Lily', '基利安！你疯了吗？你放开我！', 1.5),
     f"A steady wide-medium side-on three-quarter two-shot opens from the adopted first frame in {R}: {L} with her back against the bare cream wall, eyes on {K}'s face; {K} close in front of her, his right hand holding her left wrist at shoulder height, his left forearm braced on the wall beside her head. She speaks in a low, shaking, furious voice, her eyes wide and wet; her right hand presses flat against his chest but he does not move. He looks down at her face without expression, his hold on her wrist unchanged. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠空白墙面、眼睛看着基利安的脸；基利安紧贴在她面前，右手按着她的左手腕、左前臂撑在墙上。她用低而发抖的声音愤怒地说话，眼睛睁大发红；右手顶在他胸口，他纹丝不动。他面无表情地低头看着她的脸，按着她手腕的手不变。镜头固定。",
     dlg_sound())

# 05 我是你妹妹
task('05｜我是你妹妹', 6, ['Lily', 'Killian'],
     "Wide-medium side-on three-quarter two-shot, both people centered in the middle third of the frame. " + PIN +
     "Lily's head is tilted up and her eyes are on Killian's face, her lips trembling; her right hand rests flat on his chest. Killian looks down at her face, his expression hard. Both are fully visible from head to knees. Nobody else is in the frame.",
     "莉莉含着泪说“我是你妹妹，而且……”，说不下去。", "0—6秒侧面中景，两人居中，镜头固定。",
     ('Lily', '我是你妹妹，而且……', 1.5),
     f"A steady wide-medium side-on three-quarter two-shot opens from the adopted first frame in {R}: {L} with her back against the bare cream wall, eyes on {K}'s face; {K} close in front of her, his right hand holding her left wrist at shoulder height, his left forearm braced on the wall. She speaks in a low, breaking voice; at the end of her words her lips tremble and she cannot go on, her eyes staying on his face. He looks down at her. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠墙、眼睛看着基利安的脸；基利安紧贴在她面前，右手按着她的左手腕、左前臂撑在墙上。她用低而发颤的声音说话，说到最后嘴唇颤抖、说不下去，眼睛始终看着他的脸。他低头看着她。镜头固定。",
     dlg_sound())

# 06 我马上要嫁给保罗
task('06｜马上要嫁给保罗', 7, ['Lily', 'Killian'],
     "Wide-medium side-on three-quarter two-shot, both people centered in the middle third of the frame. " + PIN +
     "Lily's head is tilted up and her eyes are on Killian's face, tears on her lashes; her right hand rests flat on his chest. Killian looks down at her face, his expression hard. Both are fully visible from head to knees. Nobody else is in the frame.",
     "莉莉含着泪说出“我马上就要嫁给保罗了”，基利安听到名字，整个人一顿。", "0—7秒侧面中景，两人居中，镜头固定。",
     ('Lily', '而且我马上就要嫁给保罗了！', 1.5),
     f"A steady wide-medium side-on three-quarter two-shot opens from the adopted first frame in {R}: {L} with her back against the bare cream wall, eyes on {K}'s face; {K} close in front of her, his right hand holding her left wrist at shoulder height, his left forearm braced on the wall. She speaks in a low, cracking voice through tears, her eyes on his face. While she speaks, his whole body goes still and his eyes harden. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠墙、眼睛看着基利安的脸；基利安紧贴在她面前，右手按着她的左手腕、左前臂撑在墙上。她含着泪、用低而发裂的声音说话，眼睛看着他的脸。说到最后那个名字时，他整个人一顿，眼神变冷。镜头固定。",
     dlg_sound())

# 07 没有血缘
task('07｜没有血缘的妹妹', 7, ['Lily', 'Killian'],
     "Wide-medium side-on three-quarter two-shot, both people centered in the middle third of the frame. " + PIN +
     "Killian's head is lifted and he looks down into Lily's face, his jaw tight, his irises edged with a faint amber-gold glow. Lily looks up at him, afraid, her lips pressed together. Both are fully visible from head to knees. Nobody else is in the frame.",
     "基利安冷冷地看着莉莉，反问“没有任何血缘关系的妹妹”。", "0—7秒侧面中景，两人居中，镜头固定。",
     ('Killian', '妹妹？没有任何血缘关系的妹妹？', 1.8),
     f"A steady wide-medium side-on three-quarter two-shot opens from the adopted first frame in {R}: {L} with her back against the bare cream wall, eyes on {K}'s face; {K} close in front of her, his right hand holding her left wrist at shoulder height, his left forearm braced on the wall. He looks down into her eyes; a short, contemptuous breath leaves his nose, his jaw tight and his eyes darkening. Then he speaks quietly and flatly. She looks up at him, afraid, her lips pressed together. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠墙、眼睛看着基利安的脸；基利安紧贴在她面前，右手按着她的左手腕、左前臂撑在墙上。他低头看进她的眼睛，鼻子里轻轻呼出一口轻蔑的气，下颌收紧、眼神变暗；然后平静而冷淡地说话。她抬头看着他，害怕，抿着嘴。镜头固定。",
     dlg_sound())

# 08 犬齿（无台词）
task('08｜颈侧', 6, ['Lily', 'Killian'],
     "Wide-medium side-on three-quarter two-shot, both people centered in the middle third of the frame. Lily stands with her back flat against the bare cream panelled wall, her head turned away toward the door with her eyes squeezed shut, both hands resting flat on Killian's chest; "
     "Killian stands facing her, very close, his right hand at her waist and his left forearm braced on the wall beside her head, his face a short distance from her neck. Both are fully visible from head to knees. Nobody else is in the frame.",
     "基利安搂紧她的腰，头低到她颈边；莉莉身体一僵、闭眼偏头。（无台词）", "0—6秒侧面中景，两人居中，镜头固定。",
     None,
     f"A steady wide-medium side-on three-quarter two-shot opens from the adopted first frame in {R}: {L} against the bare cream wall, head turned toward the door, eyes shut, her hands flat on {K}'s chest; {K} close in front of her with his right hand at her waist and his left forearm braced on the wall. He steps in, his right hand drawing her body against his and closing the last gap between them, and his head lowers beside her neck, half hidden behind her hair. Her whole body stiffens, her eyes squeezing shut and her head tilting further away, her hands pressing against his chest. Nobody speaks. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠空白墙面、头偏向门、紧闭双眼，双手按在基利安胸口；基利安紧贴在她面前，右手扶在她腰上、左前臂撑在墙上。他上前一步，右手把她的身体揽向自己，贴紧；头低到她颈边，半藏在她的头发后面。她整个身体一僵，眼睛闭得更紧、头更偏开，双手抵着他的胸口。没有人说话。镜头固定。",
     silent_sound("Only the faint rustle of silk and quiet room tone.", "只有丝绸的轻微摩擦声和安静的房间底噪。"))

# 09 他配不上你
task('09｜他配不上你', 7, ['Lily', 'Killian'],
     "Wide-medium side-on three-quarter two-shot, both people centered in the middle third of the frame. Lily stands with her back flat against the bare cream panelled wall, her eyes shut and wincing, the fingertips of her right hand pressed to the side of her neck; "
     "Killian stands facing her, very close, his head lifted from her neck and looking down at her face, his irises edged with a faint amber-gold glow, his right hand at her waist and his left forearm braced on the wall beside her head. Both are fully visible from head to knees. Nobody else is in the frame.",
     "基利安抬起头，冷冷地说“保罗配不上你”；莉莉闭眼皱眉，手按着颈侧。", "0—7秒侧面中景，两人居中，镜头固定。",
     ('Killian', '至于保罗那个废物……他配不上你。', 1.8),
     f"A steady wide-medium side-on three-quarter two-shot opens from the adopted first frame in {R}: {L} against the bare cream wall, eyes shut, wincing, her fingertips pressed to the side of her neck; {K} close in front of her with his right hand at her waist and his left forearm braced on the wall. He slowly lifts his head from her neck and looks into her face, his eyes dark, then speaks in a low, cold voice. She keeps her eyes shut and her fingertips on her neck. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠空白墙面、闭眼皱眉，右手指尖按着颈侧；基利安紧贴在她面前，右手扶着她的腰、左前臂撑在墙上。他缓缓从她颈边抬起头，看着她的脸，眼神很暗，然后用低而冷的声音说话。她一直闭着眼，手指按在颈上。镜头固定。",
     dlg_sound())

# 10 敲门声（无台词）
task('10｜敲门声', 5, ['Lily', 'Killian'],
     "Wide-medium three-quarter two-shot toward the heavy dark-wood door at frame-left, both people centered in the middle third of the frame. Lily stands with her back flat against the bare cream panelled wall; Killian stands facing her, very close, his left forearm braced on the wall beside her head. "
     "They are looking at each other, both still. The closed door with its brass handle is visible at the left of the frame. Both are fully visible from head to knees. Nobody else is in the frame.",
     "门上响起三下敲门声，两人同时僵住，转头看向门。（无台词）", "0—5秒中景两人居中，门在画左，镜头固定。",
     None,
     f"A steady wide-medium three-quarter two-shot opens from the adopted first frame in {R}: {L} against the bare cream wall, {K} close in front of her with his left forearm braced on the wall, the closed door with its brass handle at frame-left. Three sharp knocks sound on the door. At the first knock both go completely still and turn only their heads toward the door, their eyes fixed on it, their bodies frozen. The door stays shut. Nobody speaks. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠空白墙面，基利安紧贴在她面前、左前臂撑在墙上，画左是紧闭的带黄铜把手的木门。门上响起三下清脆的敲门声。第一下响起时，两人同时僵住、只把头转向门，眼睛盯着门，身体不动。门仍然关着。没有人说话。镜头固定。",
     silent_sound("Three sharp knocks on a wooden door, then quiet room tone.", "三下清脆的敲门声，随后是安静的房间底噪。"))

# 11 门外的保罗
task('11｜门外的保罗', 6, [],
     "Medium close-up of the closed heavy dark-wood door with its brass handle, seen from inside the room, the door centered in the middle third of the frame, the room's warm light on the wood. Nobody is in the frame.",
     "紧闭的木门近景，保罗在门外说话，他全程不出现在画面里。", "0—6秒门的中近景，镜头固定。",
     ('Paul', '莉莉？宝贝你换好了吗？', 1.2),
     f"A steady medium close-up opens from the adopted first frame in {R}: the closed heavy dark-wood door with its brass handle, seen from inside the room. A young man named Paul speaks from the corridor outside; his voice reaches the room muffled by the wood, casual and lightly smug, and he is never visible. The handle stays still while he speaks. The camera holds still.",
     "从开场图继续，门的中近景：从房间里看向紧闭的厚重木门和黄铜把手。名叫保罗的年轻男人在门外走廊说话，声音隔着木门略显闷，随意而带点轻浮，他全程不出现在画面里。他说话时把手保持不动。镜头固定。",
     ("A muffled young male voice through the wooden door, with quiet room tone.", "隔着木门的闷闷男声，底下是安静的房间底噪。"), assets=('room',))

# 12 门把手
task('12｜门把手', 6, [],
     "Close-up of the brass door handle on the heavy dark-wood door, seen from inside the room, the handle centered in the middle third of the frame. Nobody is in the frame.",
     "黄铜门把手被缓缓拧动，保罗在门外说“我进来了哦”。", "0—6秒门把手近景，镜头固定。",
     ('Paul', '我进来了哦？', 1.2),
     f"A steady close-up opens from the adopted first frame in {R}: the brass door handle on the heavy dark-wood door, seen from inside the room. A young man named Paul speaks from the corridor; his voice reaches the room muffled by the wood and he is never visible. As he finishes, the handle turns slowly downward with a loud, magnified metallic click and stops against the latch; the door stays shut. The camera holds still.",
     "从开场图继续，近景：从房间里看向厚重木门上的黄铜把手。名叫保罗的年轻男人在门外走廊说话，声音隔着木门略显闷，他全程不出现在画面里。他说完时，把手缓缓向下转动，发出被放大的清晰金属咔哒声，卡在锁舌上停住；门仍然关着。镜头固定。",
     ("A muffled young male voice through the wooden door, then a loud, magnified metallic click as the handle turns.", "隔着木门的闷闷男声，随后是门把手转动时被放大的金属咔哒声。"), assets=('room',))

# 13 哀求（无台词）
task('13｜哀求', 5, ['Lily', 'Killian'],
     "Medium close two-shot, waist-up, both people centered in the middle third of the frame. Lily stands with her back flat against the bare cream panelled wall, her head tilted up, her eyes wide and fixed on Killian's face; Killian stands facing her, very close, looking down at her with a cold blank expression, his left forearm braced on the wall beside her head and his right hand still at her waist. Nobody else is in the frame.",
     "莉莉睁大眼睛看着基利安，哀求地快速摇头。（无台词）", "0—5秒侧面中近景，两人居中，镜头固定。",
     None,
     f"A steady medium close two-shot opens from the adopted first frame in {R}: {L} against the bare cream wall, her eyes wide and fixed on {K}'s face; {K} close in front of her, looking down at her, his left forearm braced on the wall and his right hand at her waist. Her eyes are pleading and her head shakes in tiny rapid movements, her lips pressed tightly together. He watches her without expression and does not move. Nobody speaks. The camera holds still.",
     "从开场图继续，侧面中近景：莉莉背靠空白墙面，睁大眼睛盯着基利安的脸；基利安紧贴在她面前、低头看着她，左前臂撑在墙上、右手仍扶在她腰上。她的眼神哀求，脑袋做着细小而急促的摇动，嘴唇紧紧抿住。他面无表情地看着她，一动不动。没有人说话。镜头固定。",
     silent_sound("Quiet room tone and a faint brush of silk.", "安静的房间底噪和轻微的丝绸摩擦声。"))

# 14 猜猜看
task('14｜猜猜看', 7, ['Lily', 'Killian'],
     "Medium two-shot, waist-up, both people centered in the middle third of the frame. Lily stands with her back flat against the bare cream panelled wall; Killian stands facing her, very close, his right hand under her chin tilting her face up toward his, his left forearm braced on the wall beside her head. Their faces are about a hand's width apart. Her eyes are locked on his. Nobody else is in the frame.",
     "基利安捏住莉莉的下巴逼她看着自己，低声说“猜猜看，如果他现在推开门”。", "0—7秒侧面中景，两人居中，镜头固定。",
     ('Killian', '猜猜看，如果他现在推开门，', 1.8),
     f"A steady medium two-shot opens from the adopted first frame in {R}: {L} against the bare cream wall; {K} close in front of her, his right hand under her chin and his left forearm braced on the wall beside her head, their faces about a hand's width apart. His hand tightens on her chin and slowly turns her face fully toward his. Her eyes are locked on his, trembling, her lips pressed together. He speaks in a low whisper, his eyes on her face. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠空白墙面；基利安紧贴在她面前，右手托在她下巴下，左前臂撑在她头旁的墙上，两人的脸相距一手宽。他托着她下巴的手收紧，慢慢把她的脸完全转向自己。她的眼睛死死看着他，发颤，嘴唇抿紧。他低声耳语，眼睛看着她的脸。镜头固定。",
     dlg_sound())

# 15 纯洁的未婚妻
task('15｜纯洁的未婚妻', 6, ['Lily', 'Killian'],
     "Medium two-shot, waist-up, both people centered in the middle third of the frame. Lily stands with her back flat against the bare cream panelled wall; Killian stands facing her, very close, his right hand under her chin holding her face toward his, his left forearm braced on the wall beside her head. Their faces are a short hand's width apart. A tear shines on her cheek and her eyes are locked on his. Nobody else is in the frame.",
     "基利安继续低语“看到他纯洁的未婚妻”，莉莉流着泪看着他。", "0—6秒侧面中景，两人居中，镜头固定。",
     ('Killian', '看到他纯洁的未婚妻，', 1.5),
     f"A steady medium two-shot opens from the adopted first frame in {R}: {L} against the bare cream wall, a tear on her cheek, her eyes locked on {K}'s; {K} close in front of her, his right hand under her chin and his left forearm braced on the wall. He speaks in a low whisper, his eyes on her face, his hold unchanged. Her tear runs down and her lips tremble. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠空白墙面，脸颊上有一滴泪，眼睛死死看着基利安；基利安紧贴在她面前，右手托着她的下巴、左前臂撑在墙上。他低声耳语，眼睛看着她的脸，手不变。她的泪滑下来，嘴唇发颤。镜头固定。",
     dlg_sound())

# 16 她的哥哥
task('16｜她的哥哥', 6, ['Lily', 'Killian'],
     "Medium two-shot, waist-up, both people centered in the middle third of the frame. Lily stands with her back flat against the bare cream panelled wall; Killian stands facing her, very close, his right hand under her chin holding her face toward his, his left forearm braced on the wall beside her head. Their faces are a short hand's width apart. Her eyes are locked on his. Nobody else is in the frame.",
     "基利安的脸逼近到几乎碰到她的嘴唇，说出没说完的“她的哥哥……”。", "0—6秒侧面中景，两人居中，镜头固定。",
     ('Killian', '正在被她的哥哥……', 1.5),
     f"A steady medium two-shot opens from the adopted first frame in {R}: {L} against the bare cream wall, her eyes locked on {K}'s; {K} close in front of her, his right hand under her chin and his left forearm braced on the wall. He leans in until his lips are an inch from hers and stops there, his eyes on her face, and speaks in a low whisper that trails off. Her eyes squeeze shut. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠空白墙面，眼睛死死看着基利安；基利安紧贴在她面前，右手托着她的下巴、左前臂撑在墙上。他把脸凑近到离她的嘴唇只有一寸，停在那里，眼睛看着她的脸，低声说话、话音拖住没说完。她闭上眼睛。镜头固定。",
     dlg_sound())

# 17 门开了（无台词）
task('17｜门被推开', 5, [],
     "Medium shot of the closed heavy dark-wood door with its brass handle, seen from inside the room, the door centered in the middle third of the frame, the handle still. Nobody is in the frame.",
     "门被缓缓推开一道缝，走廊的冷光涌进来。（无台词，成片里在这里黑屏、接重音效）", "0—5秒门的中景，镜头固定。",
     None,
     f"A steady medium shot opens from the adopted first frame in {R}: the closed heavy dark-wood door with its brass handle, seen from inside the room. The door swings slowly inward a hand's width with a long, low creak, and bright cold light from the corridor spills across the carpet. Nobody is visible in the gap. The camera holds still.",
     "从开场图继续，中景：从房间里看向紧闭的厚重木门和黄铜把手。门缓缓向里推开一手宽，发出长而低的吱呀声，走廊里明亮的冷光涌到地毯上。缝隙里看不到任何人。镜头固定。",
     silent_sound("A long, low wooden creak of a door swinging open.", "门被推开时长而低的木头吱呀声。"), assets=('room',))

# ---- 汇总 -----------------------------------------------------------------------------------------
lines = []
for t in tasks:
    lines.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
    for x in t['dialogue']:
        lines.append(f"{x['speaker']}：“{x['text']}”")
d['episodes'] = [{'title': '第1集｜禁忌的更衣室', 'summary': '高端婚纱店VIP更衣室里，基利安当着门外未婚夫的面逼近莉莉，敲门声、门把手转动，最后一秒门被推开。',
                  'script': '\n'.join(lines), 'segments': tasks, 'dialogue_language': 'zh'}]
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
json.dump(d, open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(OUT_TXT, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
total = sum(t['duration_seconds'] for t in tasks)
print(f'{len(tasks)} 个任务，合计约 {total} 秒（含原始尾部更长）→ {OUT_JSON}')
