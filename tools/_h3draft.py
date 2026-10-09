"""第 4 集起共用的制作稿小工具（gen_ep4.py、gen_ep5.py 用）。
追加批次规则（手册 F11）：style、已有素材、已有角色从上一集的 JSON 逐字复制；新东西另设新键。
"""
import json, re, copy, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = os.path.join(ROOT, 'Alpha继兄的笼中吻')

LEAD = "Live-action, cinematic, photorealistic with natural skin texture, shallow depth of field and warm luxurious lighting, ultra-wide 8:3 cinemascope frame. "
IMG = ("One coherent first frame from a photorealistic live-action romantic thriller, ultra-wide 8:3 cinemascope composition. "
       "Natural skin with visible pores, realistic fabric and materials. The fixed scene reference defines the place, and the character portraits define only the named people. ")
NOVOICE_EN = "The recording is completely free of voices: no speech, no humming, no sighs, no breathing sounds, no vocal sounds of any kind."
NOVOICE_ZH = "录音里完全没有人声：没有说话、哼声、叹息、呼吸声或任何发声。"


def line_seconds(text):
    """复制插件 dialogue_plan.line_seconds 的英语算法（单词数 / 2 秒 + 标点停顿）。"""
    words = len(re.findall(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)*", text))
    pauses = len(re.findall(r'[,;:]', text)) * .12 + len(re.findall(r'[!?]', text)) * .18
    return max(.35, words / 2.0 + min(pauses, 1.5))


def silent(sfx_en, sfx_zh):
    return (sfx_en + ' ' + NOVOICE_EN, sfx_zh + ' ' + NOVOICE_ZH)


def voiced(extra_en, extra_zh):
    return (extra_en + ' Voices stay close and clear.', extra_zh + '人声近而清楚。')


class Batch:
    def __init__(self, base_json, title, seed0):
        self.d = copy.deepcopy(json.load(open(os.path.join(FOLDER, base_json), encoding='utf-8')))
        self.d['title'] = title
        self.tasks = []
        self.seed = seed0

    def scene(self, key, label, en, zh, prompt):
        self.d['assets'].append({'key': key, 'kind': 'image', 'role': 'scene', 'label': label,
                                 'description': {'en': en, 'zh': zh}, 'generate': {'image_prompt': prompt, 'reference_keys': []}})

    def person(self, key, label, en, zh, prompt, ref=None):
        self.d['assets'].append({'key': key, 'kind': 'image', 'role': 'character', 'label': label,
                                 'description': {'en': en, 'zh': zh}, 'generate': {'image_prompt': prompt, 'reference_keys': [ref] if ref else []}})

    def character(self, name, image_key, voice_en, voice_zh):
        self.d['characters'][name] = {'image_keys': [image_key], 'voice_description': {'en': voice_en, 'zh': voice_zh}}

    def task(self, title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound):
        self.seed += 1
        s = {'title': title, 'duration_seconds': dur, 'generation_seconds': dur, 'continuity': 'cut', 'depends_on_previous': False,
             'use_previous_episode_state': False, 'characters': chars, 'asset_keys': list(assets), 'image_reference_keys': list(refs),
             'image_prompt': IMG + img + end, 'visual_zh': vis_zh, 'camera_zh': cam_zh,
             'dialogue': [], 'shots': [], 'sound_en': sound[0], 'sound_zh': sound[1], 'seed': self.seed, 'dialogue_language': 'en'}
        if dlg:
            sp, tx, start = dlg
            end_t = round(start + line_seconds(tx) + 0.05, 2)
            assert end_t <= dur - 1.0, (title, end_t, dur)   # 台词后至少留 1 秒
            s['dialogue'].append({'speaker': sp, 'text': tx, 'start_seconds': start, 'end_seconds': end_t, 'language': 'en'})
        s['shots'].append({'start_seconds': 0, 'end_seconds': dur, 'visual_en': LEAD + shot_en, 'visual_zh': shot_zh, 'dialogue_indices': [0] if dlg else []})
        self.tasks.append(s)

    def finish(self, ep_title, summary, out_name):
        lines = []
        for t in self.tasks:
            lines.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
            for x in t['dialogue']:
                lines.append(f"{x['speaker']}：“{x['text']}”")
        self.d['episodes'] = [{'title': ep_title, 'summary': summary, 'script': '\n'.join(lines), 'segments': self.tasks, 'dialogue_language': 'en'}]
        out_json = os.path.join(FOLDER, out_name + '.json')
        json.dump(self.d, open(out_json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        open(os.path.join(FOLDER, out_name + '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(json.dumps(self.d, ensure_ascii=False, indent=1))
        print(f'{len(self.tasks)} 个任务，合计约 {sum(t["duration_seconds"] for t in self.tasks)} 秒 → {out_json}')
