"""第 4 集起共用的制作稿小工具（gen_ep4.py、gen_ep5.py 用）。
追加批次规则（手册 F11）：style、已有素材、已有角色从上一集的 JSON 逐字复制；新东西另设新键。
"""
import json, re, copy, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = os.path.join(ROOT, 'Alpha继兄的笼中吻')

LEAD = "Live-action, cinematic, photorealistic with natural skin texture, shallow depth of field and warm luxurious lighting, ultra-wide 8:3 cinemascope frame. "
IMG = ("One coherent first frame from a photorealistic live-action romantic thriller, ultra-wide 8:3 cinemascope composition. "
       "Natural skin with visible pores, realistic fabric and materials. The fixed scene reference defines the place, and the character portraits define only the named people. ")
# 项目配置：写新剧时用 configure() 改文件夹和风格词；旧剧（Alpha）不调用，行为完全不变。
CFG = {'folder': FOLDER, 'img': IMG, 'lead': LEAD, 'lang': 'en', 'smooth': False, 'fixed_seed': None, 'cap': None,
       'pace': 1.0, 'fast_text': False, 'gap': 0.25, 'start': 0.6, 'need_k': 1.4, 'floors': {1: 6, 2: 7}, 'sfx_loud': False}   # lang: 台词语言，旧剧 en；新剧《极寒末日》发中国，用 zh


def configure(folder=None, img=None, lead=None, lang=None, smooth=None, fixed_seed=None, cap=None, fast=None):
    if fast:   # 快节奏写法（hh 2026-10-15：29–44 集太慢、现场音太弱）：台词窗口不能短于插件的自然语速（插件会拒收），所以提速只写进文字；句间更紧、对白任务地板降低、现场音写响
        CFG.update(fast_text=True, gap=0.1, start=0.4, need_k=1.25, floors={1: 5, 2: 6}, sfx_loud=True)
    if smooth is not None: CFG['smooth'] = smooth       # 台词顺滑写法（2026-10-14）：去句内标点、任务按台词长度收紧、加“一口气”说明
    if cap is not None: CFG['cap'] = cap   # 任务时长上限（秒）；2026-10-15 15 秒任务让 sage attention 崩溃，改成 12
    if fixed_seed is not None: CFG['fixed_seed'] = fixed_seed   # 全批视频固定一个种子（hh 2026-10-14）
    if lang: CFG['lang'] = lang
    if folder: CFG['folder'] = folder
    if img: CFG['img'] = img
    if lead: CFG['lead'] = lead


NOVOICE_EN = "The recording is completely free of voices: no speech, no humming, no sighs, no breathing sounds, no vocal sounds of any kind."
NOVOICE_ZH = "录音里完全没有人声：没有说话、哼声、叹息、呼吸声或任何发声。"


def line_seconds(text):
    """复制插件 dialogue_plan.line_seconds 的算法。英语：单词数 / 2 秒 + 标点停顿；中文：汉字数 / 4 秒（CPS=4.0）+ 标点停顿。"""
    if CFG['lang'] == 'zh':
        han = len(re.findall(r'[\u3400-\u9fff]', text))
        pauses = len(re.findall(r'[、，,；;：:]', text)) * .12 + len(re.findall(r'[。！？!?]', text)) * .18
        return max(.35, han / 4.0 / CFG['pace'] + min(pauses, 1.5))
    words = len(re.findall(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)*", text))
    pauses = len(re.findall(r'[,;:]', text)) * .12 + len(re.findall(r'[!?]', text)) * .18
    return max(.35, words / 2.0 / CFG['pace'] + min(pauses, 1.5))


def silent(sfx_en, sfx_zh):
    return (sfx_en + ' ' + NOVOICE_EN, sfx_zh + ' ' + NOVOICE_ZH)


NOWORD_EN = "No one speaks and no words are heard: only breathing, small sounds of movement and the sounds listed here."
NOWORD_ZH = "没有人说话，也听不到任何字词：只有呼吸声、细小的动作声和上面写的这些声音。"


LOUD_EN = "Every on-set sound effect is loud, crisp and close to the microphone, as prominent as the voices: footsteps, impacts, doors, wind, ice, machinery and fabric are all clearly heard. No music."
LOUD_ZH = "所有现场音效都响亮、清脆、贴近话筒，和人声一样突出：脚步、撞击、开关门、风声、冰裂、机械和衣料摩擦都听得清清楚楚。没有配乐。"
_WEAK = [('faint ', 'clear '), ('soft ', 'crisp '), ('gentle ', 'clear '), ('quiet ', 'distinct '), ('thin ', 'sharp '), ('muffled ', 'heavy '), ('light ', 'crisp '), ('Faint ', 'Clear '), ('Soft ', 'Crisp '), ('Gentle ', 'Clear ')]


def _loud(sfx_en):
    for a, b in _WEAK: sfx_en = sfx_en.replace(a, b)
    return sfx_en


def breathy(sfx_en, sfx_zh):
    """无台词片的新写法（第 11 集起）：只禁说话和字词，不禁呼吸／喘息／低吼。
    旧写法 silent() 连呼吸也禁；“禁呼吸 → 近乎静音”是假设 H（补拍包 2 在测），这里按新写法排。"""
    if CFG['sfx_loud']: return (_loud(sfx_en) + ' ' + NOWORD_EN + ' ' + LOUD_EN, sfx_zh + ' ' + NOWORD_ZH + LOUD_ZH)
    return (sfx_en + ' ' + NOWORD_EN, sfx_zh + ' ' + NOWORD_ZH)


def voiced(extra_en, extra_zh):
    if CFG['sfx_loud']: return (_loud(extra_en) + ' ' + LOUD_EN + ' The voices are clear.', extra_zh + LOUD_ZH + '人声清楚。')
    return (extra_en + ' Voices stay close and clear.', extra_zh + '人声近而清楚。')


class Batch:
    def __init__(self, base_json, title, seed0, style=None):
        if base_json is None:      # 新剧的第一批：从空白文档开始（style 必须给）
            self.d = {'schema': 'h3-production-draft', 'version': 1, 'title': title, 'dialogue_language': CFG['lang'],
                      'style': style, 'assets': [], 'characters': {}, 'episodes': []}
        else:
            self.d = copy.deepcopy(json.load(open(os.path.join(CFG['folder'], base_json), encoding='utf-8')))
        self.d['title'] = title
        self.tasks = []
        self.seed = seed0

    def scene(self, key, label, en, zh, prompt):
        self.d['assets'].append({'key': key, 'kind': 'image', 'role': 'scene', 'label': label,
                                 'description': {'en': en, 'zh': zh}, 'generate': {'image_prompt': prompt, 'reference_keys': []}})

    def person(self, key, label, en, zh, prompt, ref=None):
        self.d['assets'].append({'key': key, 'kind': 'image', 'role': 'character', 'label': label,
                                 'description': {'en': en, 'zh': zh}, 'generate': {'image_prompt': prompt, 'reference_keys': [ref] if ref else []}})

    def prop(self, key, label, en, zh, prompt, ref=None):
        """道具／动物（第 7 集起的黑马）。role='prop'，写法检查不查它的表情。"""
        self.d['assets'].append({'key': key, 'kind': 'image', 'role': 'prop', 'label': label,
                                 'description': {'en': en, 'zh': zh}, 'generate': {'image_prompt': prompt, 'reference_keys': [ref] if ref else []}})

    def character(self, name, image_key, voice_en, voice_zh):
        self.d['characters'][name] = {'image_keys': [image_key], 'voice_description': {'en': voice_en, 'zh': voice_zh}}

    def task(self, title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound,
             lines=None, shots=None, frame=None, cont=False):
        """dlg = (说话人, 台词, 开口秒) 或 None（老用法）。
        可选：lines=[(说话人, 台词, 开口秒), ...] 一个任务多句台词（对比测试用）；
              shots=[(起, 止, 英文, 中文, [台词序号]), ...] 一个任务多个镜头（对比测试用，此时 shot_en/shot_zh 不用）；
              frame='素材键' 用现成图片当开场图（opening_frame_key）；cont=True 为续接（continue，同时必须承接前段）。"""
        self.seed += 1
        if CFG.get('fixed_seed'): self.seed = CFG['fixed_seed']
        s = {'title': title, 'duration_seconds': dur, 'generation_seconds': dur, 'continuity': 'continue' if cont else 'cut',
             'depends_on_previous': bool(cont), 'use_previous_episode_state': False, 'characters': chars,
             'asset_keys': list(assets), 'image_reference_keys': list(refs),
             'image_prompt': CFG['img'] + img + end, 'visual_zh': vis_zh, 'camera_zh': cam_zh,
             'dialogue': [], 'shots': [], 'sound_en': sound[0], 'sound_zh': sound[1], 'seed': self.seed, 'dialogue_language': CFG['lang']}
        if frame:
            s['opening_frame_key'] = frame
        spoken = list(lines) if lines else ([dlg] if dlg else [])
        for sp, tx, start in spoken:
            end_t = round(start + line_seconds(tx) + 0.05, 2)
            assert end_t <= dur - 1.0, (title, end_t, dur)   # 台词后至少留 1 秒
            s['dialogue'].append({'speaker': sp, 'text': tx, 'start_seconds': start, 'end_seconds': end_t, 'language': CFG['lang']})
        if shots:
            for a, z, en, zh, idx in shots:
                s['shots'].append({'start_seconds': a, 'end_seconds': z, 'visual_en': CFG['lead'] + en, 'visual_zh': zh, 'dialogue_indices': idx})
        else:
            s['shots'].append({'start_seconds': 0, 'end_seconds': dur, 'visual_en': CFG['lead'] + shot_en, 'visual_zh': shot_zh,
                               'dialogue_indices': list(range(len(spoken)))})
        self.tasks.append(s)
        return s

    def finish(self, ep_title, summary, out_name):
        lines = []
        for t in self.tasks:
            lines.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
            for x in t['dialogue']:
                lines.append(f"{x['speaker']}：“{x['text']}”")
        self.d['episodes'] = [{'title': ep_title, 'summary': summary, 'script': '\n'.join(lines), 'segments': self.tasks, 'dialogue_language': CFG['lang']}]
        out_json = os.path.join(CFG['folder'], out_name + '.json')
        json.dump(self.d, open(out_json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        open(os.path.join(CFG['folder'], out_name + '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(json.dumps(self.d, ensure_ascii=False, indent=1))
        print(f'{len(self.tasks)} 个任务，合计约 {sum(t["duration_seconds"] for t in self.tasks)} 秒 → {out_json}')
