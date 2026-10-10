#!/usr/bin/env python3
"""生成《Alpha继兄的笼中吻》第 2 集“门后的狂想”制作稿（模式 3，追加批次，英语台词，美式口语）。

和 gen_ep1.py 同一套规则（CLAUDE.md 第 4 节）。追加批次的要求（手册 F11）：
  - style、素材 lily / killian / room、角色 Lily / Killian / Paul 必须和第 1 批逐字相同 —— 这里直接从第 1 集的 JSON 复制；
  - 新增内容另设新键：素材 alcove（婚纱架后的小隔间）、paul（保罗的人物图），角色 PaulOnScreen（保罗，有脸有声音）。
    第 1 集的 Paul 没有人物图，不能改，所以第 2 集起保罗出镜用 PaulOnScreen。
用法:  先有第 1 集的 JSON，再  python3 tools/gen_ep2.py
"""
import json, re, copy, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = os.path.join(ROOT, 'Alpha继兄的笼中吻')
BASE = os.path.join(FOLDER, '第01集/第01集_制作稿.json')
OUT_JSON = os.path.join(FOLDER, '第02集/第02集_制作稿_追加.json')
OUT_TXT = os.path.join(FOLDER, '第02集/第02集_制作稿_追加_全选复制粘贴.txt')

base = json.load(open(BASE, encoding='utf-8'))
d = copy.deepcopy(base)
d['title'] = 'Alpha继兄的笼中吻｜第2集｜门后的狂想'

# ---- 新素材、新角色（旧的原样保留，不改一个字） ------------------------------------------------
d['assets'].append({
    'key': 'alcove', 'kind': 'image', 'role': 'scene', 'label': '更衣室婚纱架后的隔间',
    'description': {
        'en': ("A narrow dressing alcove at the back of the private fitting room: a dense row of long white gowns in garment covers hanging close together on a rail along one side, "
               "and a heavy cream floor-length velvet curtain on a ceiling track, drawn half open across the front. Dim warm light with soft shadows. "
               "The reference fixes the look of the alcove, not any people."),
        'zh': ("更衣室最里面的狭窄隔间：一侧是紧挨着挂在横杆上、罩着防尘袋的白色长婚纱，正面是一道挂在顶轨上的奶油色厚重丝绒落地帘，拉开了一半。光线昏暗温暖，阴影柔和。"
               "参考图固定隔间的样子，不带入任何人物。")},
    'generate': {'image_prompt': (
        "A photorealistic shot of an empty narrow dressing alcove at the back of a luxury fitting room: a dense row of long white gowns in garment covers hanging close together on a rail along one side, "
        "a heavy cream floor-length velvet curtain on a ceiling track drawn half open across the front, dim warm light with soft shadows, thick carpet. No people."),
        'reference_keys': []}})
d['assets'].append({
    'key': 'paul', 'kind': 'image', 'role': 'character', 'label': '保罗',
    'description': {
        'en': ("Paul, an adult man in his late twenties with neatly combed light-brown hair, a clean-shaven friendly boyish face and warm brown eyes, of average build, "
               "wearing a navy blazer over a white open-collared shirt. He is a head shorter than Killian. The portrait fixes his identity and clothes, not staging."),
        'zh': ("保罗，二十八岁左右的成年男性，浅棕色头发梳得整齐，脸干净、友善、带点孩子气，暖棕色眼睛，身材普通，穿海军蓝西装外套配白色敞领衬衫。比基利安矮一个头。人物图固定身份与衣服，不固定站位。")},
    'generate': {'image_prompt': (
        "A photorealistic half-body portrait of an adult man in his late twenties with neatly combed light-brown hair, a clean-shaven friendly boyish face and warm brown eyes, "
        "wearing a navy blazer over a white open-collared shirt. He faces the camera with a mild, relaxed expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores."),
        'reference_keys': []}})
d['characters']['PaulOnScreen'] = {
    'image_keys': ['paul'],
    'voice_description': {
        'en': "A young adult male voice, light, casual and slightly smug, speaking clear American English at ordinary conversational volume.",
        'zh': "年轻成年男声，轻松随意、略带轻浮，说清楚的美式英语，正常交谈音量。"}}

# ---- 写稿用的常量和小工具（和 gen_ep1.py 相同） -------------------------------------------------
LEAD = "Live-action, cinematic, photorealistic with natural skin texture, shallow depth of field and warm luxurious lighting, ultra-wide 8:3 cinemascope frame. "
IMG = ("One coherent first frame from a photorealistic live-action romantic thriller, ultra-wide 8:3 cinemascope composition. "
       "Natural skin with visible pores, realistic fabric and materials. The fixed scene reference defines the room, and the character portraits define only the named people. ")
IMGEND = " Warm dim light, the alcove softly blurred behind."
NOVOICE_EN = "The recording is completely free of voices: no speech, no humming, no sighs, no vocal sounds of any kind."
NOVOICE_ZH = "录音里完全没有人声：没有说话、哼声、叹息或任何发声。"
K = '[[asset:killian]]'; L = '[[asset:lily]]'; P = '[[asset:paul]]'; R = '[[asset:room]]'; A = '[[asset:alcove]]'


def line_seconds(text):
    """复制插件 dialogue_plan.line_seconds 的英语算法（单词数 / 2 秒 + 标点停顿）。"""
    words = len(re.findall(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)*", text))
    pauses = len(re.findall(r'[,;:]', text)) * .12 + len(re.findall(r'[!?]', text)) * .18
    return max(.35, words / 2.0 + min(pauses, 1.5))


tasks = []
seed = [3100]


def task(title, dur, chars, assets, refs, img, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound):
    seed[0] += 1
    s = {'title': title, 'duration_seconds': dur, 'generation_seconds': dur, 'continuity': 'cut', 'depends_on_previous': False,
         'use_previous_episode_state': False, 'characters': chars, 'asset_keys': list(assets), 'image_reference_keys': list(refs),
         'image_prompt': IMG + img + IMGEND, 'visual_zh': vis_zh, 'camera_zh': cam_zh,
         'dialogue': [], 'shots': [], 'sound_en': sound[0], 'sound_zh': sound[1], 'seed': seed[0], 'dialogue_language': 'en'}
    if dlg:
        sp, tx, start = dlg
        end = round(start + line_seconds(tx) + 0.05, 2)
        assert end <= dur - 1.0, (title, end, dur)   # 台词后至少留 1 秒
        s['dialogue'].append({'speaker': sp, 'text': tx, 'start_seconds': start, 'end_seconds': end, 'language': 'en'})
    s['shots'].append({'start_seconds': 0, 'end_seconds': dur, 'visual_en': LEAD + shot_en, 'visual_zh': shot_zh, 'dialogue_indices': [0] if dlg else []})
    tasks.append(s)


def silent(sfx_en, sfx_zh):
    return (sfx_en + ' ' + NOVOICE_EN, sfx_zh + ' ' + NOVOICE_ZH)


def voiced(extra_en, extra_zh):
    return (extra_en + ' Voices stay close and clear.', extra_zh + '人声近而清楚。')


ALC = ('room', 'alcove', 'lily', 'killian')

# 01 躲进婚纱架（无台词）
task('01｜躲进婚纱架', 6, ['Lily', 'Killian'], ALC, ['alcove'],
     "Wide-medium side-on two-shot at the edge of the rack of hanging gowns, both people centered in the middle third of the frame. A strip of cold bright light from the open door at frame-left lies across the carpet. "
     "Lily stands in profile in the ivory wedding gown with its back open, both hands holding the front of the bodice at her chest, her eyes on the door at frame-left; "
     "Killian stands directly behind her, very close, in his black three-piece suit, his right arm around her waist and his left hand at his side. The long white gowns in garment covers hang close behind them. Both are fully visible from head to knees. Nobody else is in the frame.",
     "门被推开，冷光射进来。基利安搂住莉莉的腰，带着她退一步躲进婚纱堆里。", "0—6秒侧面中景，两人居中，镜头固定。",
     None,
     f"A steady wide-medium side-on two-shot opens from the adopted first frame in {A}: {L} in profile with her eyes on the open door at frame-left, {K} directly behind her with his right arm around her waist, a strip of cold light across the carpet. "
     "In one smooth movement he draws her one step backward into the row of hanging gowns, and the heavy white garment covers swing together in front of them until only the white gowns are visible. Nobody speaks. The camera holds still.",
     "从开场图继续，侧面中景：莉莉侧身、眼睛看着左边敞开的门，基利安紧贴在她身后，右臂搂着她的腰，地毯上有一道冷光。他一气呵成地带着她向后退一步，进到成排的婚纱里，厚重的白色防尘袋晃动合拢，把两人挡住，最后只剩白色婚纱。无人说话。镜头固定。",
     silent("Heavy fabric rustling as the garment covers swing closed.", "厚重的衣料晃动合拢的沙沙声。"))

# 02 捂住嘴 + 保罗画外音
task('02｜捂住嘴', 6, ['Lily', 'Killian'], ALC, ['alcove'],
     "Medium two-shot, waist-up, in profile inside a narrow dim dressing alcove between long white gowns in garment covers, both people centered in the middle third of the frame. "
     "Lily stands with her back against the hanging gowns, her ivory gown open at the back and held at her chest by her left hand, her eyes wide and fixed on Killian's face; "
     "Killian stands facing her, very close, his right hand pressed over her mouth and his left arm around her back, his eyes on her face. Nobody else is in the frame.",
     "基利安捂住莉莉的嘴，另一只手圈着她。莉莉睁大眼睛看着他。门外传来保罗的声音。", "0—6秒侧面中景，两人居中，镜头固定。",
     ('PaulOnScreen', "Lily? Where'd you go? Still changing?", 1.2),
     f"A steady medium two-shot in profile opens from the adopted first frame in {A}: {L} with her back against the hanging gowns, her eyes wide and fixed on {K}'s face; {K} close in front of her, his right hand over her mouth and his left arm around her back. "
     "Her breathing is fast and she does not move. A young man named Paul speaks from the fitting room outside the drapes; his voice is casual, muffled by the heavy fabric, and he is never visible. "
     "Killian's eyes stay on her face, narrowed, one brow lifting slightly. The camera holds still.",
     "从开场图继续，侧面中景：莉莉背靠成排的婚纱，眼睛睁大、盯着基利安的脸；基利安紧贴在她面前，右手捂着她的嘴，左臂圈着她的背。她呼吸很快，一动不动。保罗在帘外的更衣室里说话，声音随意、被厚布隔得发闷，他全程不出现。基利安的眼睛一直看着她的脸，微微眯起，一边眉毛轻轻抬起。镜头固定。",
     voiced("Soft rustle of heavy fabric. The man's voice outside is muffled by thick drapes.", "厚重衣料的轻微摩擦声。帘外男人的声音被厚布隔得发闷。"))

# 03 惊恐的眼睛（无台词）
task('03｜惊恐的眼睛', 5, ['Lily', 'Killian'], ALC, ['alcove'],
     "Tight side-profile two-shot of heads and shoulders inside the dim alcove, both people centered in the middle third of the frame. "
     "Lily's eyes are wide with fear and fixed on Killian's face above his large right hand covering her mouth, his forearm and shoulder in the frame; "
     "Killian's face is a hand's width from hers, his eyes narrowed on her face, his jaw tight. Nobody else is in the frame.",
     "特写：莉莉惊恐睁大的眼睛，基利安近在咫尺的眼睛。帘外有脚步声。", "0—5秒侧面近景，两人头肩居中，镜头固定。",
     None,
     f"A steady tight side-profile two-shot opens from the adopted first frame in {A}: {L}'s eyes wide and fixed on {K}'s face above his right hand over her mouth; {K} a hand's width from her, his eyes narrowed on her face, his jaw tight. "
     "Her eyes shine and her chest rises fast. His eyes stay on her face, unhurried. Slow footsteps move across the carpet outside the drapes. Nobody speaks. The camera holds still.",
     "从开场图继续，侧面近景：莉莉睁大眼睛盯着基利安的脸，他的右手捂在她嘴上；基利安离她只有一掌宽，眼睛眯起看着她的脸，下颌收紧。她眼睛发亮，胸口起伏很快。他的目光不慌不忙地停在她脸上。帘外的地毯上传来缓慢的脚步声。无人说话。镜头固定。",
     silent("Slow, soft footsteps on carpet outside the drapes.", "帘外地毯上缓慢轻柔的脚步声。"))

# 04 耳边的呼吸（无台词）
task('04｜耳边的呼吸', 6, ['Lily', 'Killian'], ALC, ['alcove'],
     "Tight side-profile two-shot of heads and shoulders inside the dim alcove, both people centered in the middle third of the frame. "
     "Killian's head is lowered beside Lily's ear with his lips an inch from it, his right hand still over her mouth, his forearm in the frame; "
     "Lily's eyes are squeezed shut, tears on her lashes, her cheeks flushed. Nobody else is in the frame.",
     "基利安低头贴近莉莉的耳边，莉莉闭紧眼睛，流下眼泪。（暗示，不露骨）", "0—6秒侧面近景，两人头肩居中，镜头固定。",
     None,
     f"A steady tight side-profile two-shot opens from the adopted first frame in {A}: {K}'s head lowered beside {L}'s ear, his right hand over her mouth; {L}'s eyes squeezed shut, tears on her lashes. "
     "He lowers his face the last inch until his breath brushes her ear. A shudder runs through her whole body; her eyes squeeze tighter and a tear rolls down her cheek, her jaw tightening against his palm. He does not move. Nobody speaks. The camera holds still.",
     "从开场图继续，侧面近景：基利安的头低在莉莉耳边，右手捂着她的嘴；莉莉紧闭双眼，睫毛上有泪。他把脸再靠近最后一寸，呼吸拂过她的耳朵。她全身一颤，眼睛闭得更紧，一滴泪滑下脸颊，下颌在他掌心下绷紧。他一动不动。无人说话。镜头固定。",
     silent("Slow footsteps outside the drapes and a faint rustle of silk.", "帘外缓慢的脚步声和轻微的丝绸摩擦声。"))

# 05 保罗起疑 + 画外音
task('05｜保罗起疑', 6, ['Lily', 'Killian'], ALC, ['alcove'],
     "Tight side-profile two-shot of heads and shoulders inside the dim alcove, both people centered in the middle third of the frame. "
     "Killian's head is lifted slightly from Lily's ear, his eyes on the reddened corner of her eye, his throat visible above his collar, his right hand still over her mouth; "
     "Lily's eyes are shut, a tear on her cheek, her shoulders shaking. Nobody else is in the frame.",
     "基利安抬起一点头，看着莉莉发红的眼角，喉结滚动。帘外保罗起了疑心。", "0—6秒侧面近景，两人头肩居中，镜头固定。",
     ('PaulOnScreen', "Weird. I swear I heard something.", 1.5),
     f"A steady tight side-profile two-shot opens from the adopted first frame in {A}: {K}'s head slightly lifted, his eyes on the reddened corner of {L}'s closed eye, his right hand over her mouth. "
     "His throat moves once as he swallows. A young man named Paul speaks from outside the drapes, muffled by the heavy fabric, sounding impatient; he is never visible. "
     "Her eyes stay shut and her shoulders shake. The camera holds still.",
     "从开场图继续，侧面近景：基利安的头微微抬起，眼睛看着莉莉紧闭的、发红的眼角，右手捂着她的嘴。他的喉结滚动了一下。保罗在帘外说话，声音被厚布隔得发闷，听起来不耐烦，他全程不出现。她始终闭着眼，肩膀在发抖。镜头固定。",
     voiced("Soft rustle of heavy fabric. The man's voice outside is muffled by thick drapes.", "厚重衣料的轻微摩擦声。帘外男人的声音被厚布隔得发闷。"))

# 06 帘外的手影（无台词，没有人入画，只有影子）
task('06｜帘外的手影', 5, [], ('alcove',), ['alcove'],
     "Medium shot from inside the alcove looking at the closed heavy cream floor-length curtain, lit brightly from behind, the curtain centered in the middle third of the frame. "
     "On the curtain, the dark silhouette of a man's shoulder and arm, his hand raised toward the edge of the drape. Nobody else is in the frame.",
     "从隔间里看帘子：帘子上出现保罗伸手的剪影。", "0—5秒帘子中景，镜头固定。",
     None,
     f"A steady medium shot opens from the adopted first frame in {A}: the closed heavy cream curtain lit brightly from behind, the dark silhouette of a man's arm and shoulder on the fabric. "
     "The silhouetted hand reaches slowly toward the edge of the curtain and its fingers close on the fabric. Nobody speaks. The camera holds still.",
     "从开场图继续，中景：从隔间里看向紧闭的奶油色厚帘，帘后有强光，布上有一个男人手臂和肩膀的黑色剪影。剪影的手缓缓伸向帘子边缘，手指抓住了布。无人说话。镜头固定。",
     silent("The soft rasp of a hand brushing velvet, then a single footstep stopping.", "手掌擦过丝绒的轻响，然后一声脚步停住。"))

# 07 拉开帘子（无台词，保罗入画）
task('07｜拉开帘子', 6, ['PaulOnScreen', 'Killian'], ('alcove', 'paul', 'killian'), ['alcove'],
     "Medium shot from outside the alcove, side-on, Paul centered in the middle third of the frame. Paul stands in profile in his navy blazer, frowning, his right hand gripping the edge of the closed heavy cream floor-length velvet curtain at shoulder height, his eyes on the curtain. Nobody else is in the frame.",
     "保罗皱着眉抓住帘子，一把拉开，帘后站着衣冠楚楚的基利安，莉莉看不见。", "0—6秒侧面中景，镜头固定。",
     None,
     f"A steady medium shot opens from the adopted first frame in {A}: {P} in profile, frowning, his right hand gripping the edge of the closed cream curtain at shoulder height. "
     f"He sweeps the curtain aside along its ceiling track with one hard pull of his arm, and bright light falls into the alcove: {K} stands there alone, upright and composed in his black suit, his right fingers adjusting the cuff at his left wrist, his eyes on Paul's face. "
     "Paul freezes, his eyes widening. Nobody speaks. The camera holds still.",
     "从开场图继续，中景：保罗侧身、皱着眉，右手在肩高处抓着紧闭的奶油色厚帘的边缘。他用力一拉，把帘子沿顶轨拉到一边，亮光照进隔间：基利安一个人站在那里，穿着黑西装，笔挺从容，右手整理左手腕的袖口，眼睛看着保罗的脸。保罗僵住，眼睛越睁越大。无人说话。镜头固定。",
     silent("A sharp rasp of the curtain rings sliding along a metal track.", "窗帘环在金属轨道上猛地滑过的刺啦声。"))

# 08 保罗：你什么时候回国的
task('08｜保罗吓一跳', 6, ['PaulOnScreen'], ('room', 'paul'), ['room'],
     "Medium close-up of Paul alone, waist-up, in profile facing frame-right, centered in the middle third of the frame, in his navy blazer, "
     "his eyes wide and fixed on a man standing in front of him at frame-right, just outside the frame, his mouth slightly open. Nobody else is in the frame.",
     "保罗倒退半步，结结巴巴地问基利安什么时候回来的。", "0—6秒保罗侧面中近景，镜头固定。",
     ('PaulOnScreen', "Killian? When did you get back?", 1.2),
     f"A steady medium close-up opens from the adopted first frame in {R}: {P} in profile facing frame-right, his eyes wide and fixed on the man in front of him at frame-right, just outside the frame. "
     "He takes half a step back and speaks haltingly, his voice thin with shock. The camera holds still.",
     "从开场图继续，保罗中近景：侧脸朝右，眼睛睁大，盯着右边画面外站在他面前的男人。他向后退半步，结结巴巴地说话，声音因为震惊发虚。镜头固定。",
     voiced("Quiet room tone and a faint brush of fabric.", "安静的房间底噪和轻微的衣料摩擦声。"))

# 09 保罗：你怎么在莉莉的更衣室
task('09｜你怎么在这里', 6, ['PaulOnScreen', 'Killian'], ('alcove', 'paul', 'killian'), ['alcove'],
     "Wide-medium side-on two-shot, both people centered in the middle third of the frame. Paul stands at frame-left in profile in his navy blazer, half a step back, his eyes on Killian's face; "
     "Killian stands at frame-right in the opening of the alcove in his black three-piece suit, composed, his right fingers at his left cuff, his eyes on Paul's face, "
     "the cream curtain pulled fully to one side behind him and the dark space between the hanging gowns empty behind him. Both are fully visible from head to knees. Nobody else is in the frame.",
     "保罗追问基利安为什么在莉莉的更衣室里。基利安不动声色。", "0—6秒侧面中景，两人居中，镜头固定。",
     ('PaulOnScreen', "Why are you in Lily's fitting room?", 1.2),
     f"A steady wide-medium side-on two-shot opens from the adopted first frame in {A}: {P} at frame-left in profile, half a step back, his eyes on {K}'s face; {K} at frame-right in the opening of the alcove, composed, his right fingers at his left cuff, his eyes on Paul. "
     "Paul speaks, his voice rising with confusion. Killian does not move and does not answer. The camera holds still.",
     "从开场图继续，侧面中景：保罗在左边，侧身、后退半步，眼睛看着基利安的脸；基利安在右边，站在隔间口，从容，右手指尖碰着左手袖口，眼睛看着保罗。保罗说话，声音因为困惑而拔高。基利安不动，也不回答。镜头固定。",
     voiced("Quiet room tone and a faint brush of fabric.", "安静的房间底噪和轻微的衣料摩擦声。"))

# 10 基利安：刚下飞机
task('10｜刚下飞机', 5, ['Killian'], ('alcove', 'killian'), ['alcove'],
     "Medium shot of Killian alone, waist-up, in profile facing frame-left, centered in the middle third of the frame, composed in his black three-piece suit, his right hand finishing the adjustment of the cuff at his left wrist, "
     "his eyes lowered on a man standing in front of him at frame-left, just outside the frame, his face cold and unreadable, his lips pressed together. Behind him the dark alcove between the hanging gowns. Nobody else is in the frame.",
     "基利安低头看着保罗，冷冷地回答。", "0—5秒基利安侧面中景，镜头固定。",
     ('Killian', "Just landed.", 1.4),
     f"A steady medium shot opens from the adopted first frame in {A}: {K} in profile facing frame-left, finishing the adjustment of his cuff, his eyes lowered on the man in front of him at frame-left, just outside the frame. "
     "He speaks flatly and without hurry, his voice low and cold. His hands stay still. The camera holds still.",
     "从开场图继续，基利安中景：侧脸朝左，整理完袖口，目光低下去看着左边画面外站在他面前的男人。他平平淡淡、不慌不忙地开口，声音低而冷。手不再动。镜头固定。",
     voiced("Quiet room tone and a faint brush of fabric.", "安静的房间底噪和轻微的衣料摩擦声。"))

# 11 基利安：来接我的……未婚妻
task('11｜来接我的未婚妻', 6, ['Killian'], ('alcove', 'killian'), ['alcove'],
     "Medium shot of Killian alone, waist-up, in profile facing frame-left, centered in the middle third of the frame, in his black three-piece suit, his hands at his sides, "
     "his eyes lowered on a man standing in front of him at frame-left, just outside the frame, his face cold and unreadable, his jaw tight. Behind him the dark alcove between the hanging gowns. Nobody else is in the frame.",
     "基利安居高临下地看着保罗，慢慢说出最后一句，眼角往自己身后的西装下摆扫了一眼。", "0—6秒基利安侧面中景，镜头固定。",
     ('Killian', "Came to pick up my... fiancée.", 1.3),
     f"A steady medium shot opens from the adopted first frame in {A}: {K} in profile facing frame-left, his hands at his sides, his eyes on the man in front of him at frame-left, just outside the frame. "
     "He speaks slowly and quietly, and while he speaks his eyes flick once sideways toward the hem of his own jacket behind him, then return to the man at frame-left; his expression does not change. The camera holds still.",
     "从开场图继续，基利安中景：侧脸朝左，双手垂在身侧，目光看着左边画面外站在他面前的男人。他慢慢地、压低声音说话，说话时目光往自己身后的西装下摆扫了一下，又回到左边的男人身上；表情不变。镜头固定。",
     voiced("Quiet room tone and a faint brush of fabric.", "安静的房间底噪和轻微的衣料摩擦声。"))

# 12 保罗错愕（无台词；成片里在这里黑屏、接重音效）
task('12｜保罗错愕', 5, ['PaulOnScreen'], ('room', 'paul'), ['room'],
     "Close-up of Paul's face alone, centered in the middle third of the frame, his brows raised and his mouth slightly open, his eyes wide and fixed on a man at frame-right, just outside the frame. Nobody else is in the frame.",
     "保罗错愕的特写。（无台词，成片里在这里黑屏、接重音效）", "0—5秒保罗面部特写，镜头固定。",
     None,
     f"A steady close-up opens from the adopted first frame in {R}: {P}'s face, his brows raised, his mouth slightly open, his eyes wide and fixed on the man at frame-right, just outside the frame. "
     "His eyes widen further and his face loses its colour. He does not speak. The camera holds still.",
     "从开场图继续，保罗面部特写：眉毛抬起，嘴微张，睁大眼睛盯着右边画面外的男人。他的眼睛睁得更大，脸色发白。他不说话。镜头固定。",
     silent("Tense, near-silent room tone.", "紧绷、几乎无声的房间底噪。"))

# ---- 承接前段（手册 F13 / Q35）---------------------------------------------------------------------
# 试验 Q35：同一份稿子、同一批种子，只改这一项。第 1 个任务必须是 false（插件规定）；
# 第 2–12 个任务全在同一间更衣室（婚纱架前、隔间、帘外），都写 true，
# 让每个开场图参考上一段最后一帧里的人物位置、门、衣架、帘子。其余内容一个字没动。
for t in tasks[1:]:
    t['depends_on_previous'] = True

# ---- 汇总 -----------------------------------------------------------------------------------------
lines = []
for t in tasks:
    lines.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
    for x in t['dialogue']:
        lines.append(f"{x['speaker']}：“{x['text']}”")
d['episodes'] = [{'title': '第2集｜门后的狂想',
                  'summary': '门被推开的瞬间，基利安带着莉莉躲进婚纱堆后的隔间，捂住她的嘴。保罗在帘外走近、起疑、一把拉开帘子，看到的只有衣冠楚楚的基利安——他说，他是来接他的“未婚妻”。',
                  'script': '\n'.join(lines), 'segments': tasks, 'dialogue_language': 'en'}]
json.dump(d, open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(OUT_TXT, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
total = sum(t['duration_seconds'] for t in tasks)
print(f'{len(tasks)} 个任务，合计约 {total} 秒 → {OUT_JSON}')
