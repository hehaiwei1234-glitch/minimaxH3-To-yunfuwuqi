#!/usr/bin/env python3
"""时长测试稿（2026-10-10，hh 22:40 说“开始时长测试吧”）。

问题：hh 怀疑“任务时长设得太长，动作才偏慢”（16:28），马的奔跑、人立也慢了约 4 倍。
做法：同一段文字、同一个种子，只改任务时长，看动作是不是变快、能不能在时间内做完。
  G：黑马载着莉莉奔跑（文字与马场批 7-07 完全相同）× 2 / 3 / 5 秒
  R：黑马人立再落地（无台词；起身→前蹄抬高→落回四蹄）× 2 / 3 / 5 秒
  M：莉莉上马（文字与重写测试 06 完全相同）× 3 秒（那次是 5 秒）
7 个任务、合计 23 秒。同一组三个任务用同一个种子；开场图每个任务都会重新生成，
所以组内除了“时长”外还混有“开场图不同”（看视频前先看三张开场图是否基本一样）。
素材／人物／style 以马场合并稿为底逐字复制，没有新增素材。种子 4901–4903（和库里所有稿子不重复）。
"""
import copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, silent

BASE = '合并稿/合并_第7-10集+10B_制作稿_追加.json'
OUT = '合并稿/时长测试_奔跑_人立_上马_制作稿_追加'
SRC = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))
EP = {e['title'].split('｜')[0]: e for e in SRC['episodes']}

a = Batch(BASE, SRC['title'], 4900)


def retime(s, dur):
    s['duration_seconds'] = dur
    s['generation_seconds'] = dur
    for sh in s['shots']:
        sh['end_seconds'] = dur
    return s


def G(dur, seed):
    """奔跑：复制马场合并稿 7-07（文字一字不改），只改时长、种子。"""
    s = copy.deepcopy(EP['剧本第7集']['segments'][6])
    s['seed'] = seed
    s['title'] = '%02d｜奔跑%d秒' % (len(a.tasks) + 1, dur)
    s['depends_on_previous'] = False
    s['continuity'] = 'cut'
    retime(s, dur)
    a.tasks.append(s)


RN = '[[asset:ranch]]'; LR = '[[asset:lily_riding]]'; HS = '[[asset:black_horse]]'
LAY_RN = " Fixed stage layout: the raised wooden grandstand is at frame-left; the white fence and the green field are at frame-right; dark pine trees line the far edge."
Z_RN = "固定布局：凸起的木制看台在画面左边；白色围栏和绿色跑马场在画面右边；远处边缘是一排深色松树。"
END_RN = " Bright midday sunlight, a clear blue sky, the ranch softly blurred behind."
Z_END_RN = "明亮的正午阳光，晴朗的蓝天，跑马场在后面柔和虚化。"


def R(dur, seed):
    """人立再落地：开场图是动作之前（四蹄着地、头甩起），文字写完整的 起身→抬高→落回。"""
    s = a.task('%02d｜马人立%d秒' % (len(a.tasks) + 1, dur), dur, ['LilyRiding'], ('ranch', 'lily_riding', 'black_horse'), ['ranch'],
        "Side-on wide shot, in the middle third of the frame, on the packed-earth track. The tall jet-black horse stands in profile facing frame-right on all four hooves, its head thrown up, its ears pinned back, its nostrils flared. "
        "Lily on its back is leaning forward with both arms wrapped around the horse's neck, in the cream blouse and tan riding breeches, her lips pressed tight, her brows pulled up, her eyes squeezed shut. "
        "The frame holds exactly one person, Lily, and one black horse.",
        END_RN + LAY_RN,
        "黑马猛地后腿站起，前蹄抬高，然后重重落回四蹄；莉莉抱紧马脖子。", "0—%d秒侧面宽景，镜头固定。" % dur, None,
        f"A steady side-on wide shot opens from the adopted first frame in {RN}: {HS} rears up on its hind legs with its front hooves raised high, then comes down hard on all four hooves, "
        f"while {LR} clings to its neck with both arms, her eyes squeezed shut and her lips pressed tight. The camera holds still.",
        "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是私人跑马场：黑马后腿站起、前蹄高高抬起，然后重重落回四蹄，莉莉双臂抱紧它的脖子，眼睛紧闭，嘴唇抿紧。镜头固定不动。",
        silent("Hooves scraping the dirt and the creak of leather.", "马蹄刨地声和皮革的吱嘎声。"))
    s['seed'] = seed
    s['depends_on_previous'] = False


def M(dur, seed):
    """上马：复制重写测试 06（文字一字不改），只改时长、种子。"""
    h = json.load(open(os.path.join(FOLDER, '合并稿/马场一场_完整过程重写_制作稿_追加.json'), encoding='utf-8'))
    s = copy.deepcopy(h['episodes'][0]['segments'][5])
    assert '上马' in s['title'], s['title']
    s['seed'] = seed
    s['title'] = '%02d｜上马%d秒' % (len(a.tasks) + 1, dur)
    s['depends_on_previous'] = False
    s['continuity'] = 'cut'
    retime(s, dur)
    a.tasks.append(s)


for d in (2, 3, 5):
    G(d, 4901)
for d in (2, 3, 5):
    R(d, 4902)
M(3, 4903)

a.finish('剧本第7–8集｜时长测试（奔跑／马人立／上马）',
         '同样的文字，只改任务时长：奔跑、马人立各 2／3／5 秒，上马 3 秒；看动作会不会变快、能不能在时间内做完。',
         OUT)
