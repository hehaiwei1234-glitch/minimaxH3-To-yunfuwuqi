#!/usr/bin/env python3
"""人立腿部动作测试（2026-10-10 23:00，hh 指出人立的马“双腿立起来不动、像悬浮”）。

原因判断（假设 H，n=2）：两个人立镜头的开场图画的就是“已经立到最高点”，文字只写 rears（立起），
H3 没有起点可动，就把这个姿势定住了整个任务。时长测试里的 R 组已改成“开场图四蹄着地→立起→落回”，
这里再测两件事：
  P1  把腿的动作写成动词：前蹄交替在空中蹬踏（上、下），后蹄在地上碎步踩着保持平衡，然后前蹄落地（3 秒、5 秒各一个，同文字同种子）
  P2  干脆不拍马腿：中近景只有莉莉上半身和马的脖子、头，马身在画面下方被切掉，写“头颈向上向后甩、鬃毛飞起、莉莉上身前后颠”（4 秒）
素材／人物／style 以马场合并稿为底逐字复制，没有新增素材。种子 4904、4905（和库里所有稿子不重复）。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json
from _h3draft import Batch, FOLDER, silent

BASE = '合并稿/合并_第7-10集+10B_制作稿_追加.json'
OUT = '合并稿/人立腿部动作测试_制作稿_追加'
SRC = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))
a = Batch(BASE, SRC['title'], 4900)

RN = '[[asset:ranch]]'; LR = '[[asset:lily_riding]]'; HS = '[[asset:black_horse]]'
LAY_RN = " Fixed stage layout: the raised wooden grandstand is at frame-left; the white fence and the green field are at frame-right; dark pine trees line the far edge."
END_RN = " Bright midday sunlight, a clear blue sky, the ranch softly blurred behind."
SND = silent("Hooves scraping and stamping the dirt and the creak of leather.", "马蹄刨地、踩地的声音和皮革的吱嘎声。")


def P1(dur, seed):
    s = a.task('%02d｜人立前蹄蹬踏%d秒' % (len(a.tasks) + 1, dur), dur, ['LilyRiding'], ('ranch', 'lily_riding', 'black_horse'), ['ranch'],
        "Side-on wide shot, in the middle third of the frame, on the packed-earth track. The tall jet-black horse stands in profile facing frame-right on all four hooves, its head thrown up, its ears pinned back, its nostrils flared. "
        "Lily on its back is leaning forward with both arms wrapped around the horse's neck, in the cream blouse and tan riding breeches, her lips pressed tight, her brows pulled up, her eyes squeezed shut. "
        "The frame holds exactly one person, Lily, and one black horse.",
        END_RN + LAY_RN,
        "黑马猛地立起，前蹄交替在空中一上一下地蹬踏，后蹄在地上碎步踩着保持平衡，然后前蹄落地；莉莉抱紧马脖子，身体随着颠簸晃动。",
        "0—%d秒侧面宽景，镜头固定。" % dur, None,
        f"A steady side-on wide shot opens from the adopted first frame in {RN}: {HS} lifts its front hooves off the ground and rears up on its hind legs, its front legs pawing the air one after the other, up and down, "
        f"while its hind hooves shuffle and stamp the dirt to keep its balance; then it drops its front hooves back to the ground. "
        f"{LR} clings to its neck with both arms, her body swaying with every jolt, her eyes squeezed shut and her lips pressed tight. The camera holds still.",
        "一个稳定的侧面宽景镜头，从已采用的开场图继续，场景是私人跑马场：黑马把前蹄抬离地面、后腿站起，前腿交替在空中一上一下地蹬踏，后蹄在地上碎步踩着保持平衡；然后前蹄落回地面。"
        "莉莉双臂抱紧它的脖子，身体随着每一下颠簸晃动，眼睛紧闭，嘴唇抿紧。镜头固定不动。",
        SND)
    s['seed'] = seed
    s['depends_on_previous'] = False


def P2(dur, seed):
    s = a.task('%02d｜人立不拍马腿%d秒' % (len(a.tasks) + 1, dur), dur, ['LilyRiding'], ('ranch', 'lily_riding', 'black_horse'), ['ranch'],
        "Side-on medium close-up, in the middle third of the frame, on the packed-earth track. Lily from the head to the waist leans forward on the back of the tall jet-black horse, in the cream blouse, both arms wrapped around the horse's neck, "
        "her lips pressed tight, her brows pulled up, her eyes squeezed shut. The horse's neck and head are in profile facing frame-right, its ears pinned back, its nostrils flared; its body is cut off by the bottom edge of the frame. "
        "The frame holds exactly one person, Lily, and one black horse.",
        END_RN + LAY_RN,
        "黑马的头和脖子向上、向后猛甩，鬃毛飞起；莉莉的上半身被带得向后仰、再向前扑，双臂抱紧马脖子。（镜头里看不到马腿）",
        "0—%d秒侧面中近景，镜头固定。" % dur, None,
        f"A steady side-on medium close-up opens from the adopted first frame in {RN}: {HS}'s head and neck swing up and back, its mane flying, its head tossing wildly, "
        f"and {LR}'s whole upper body is jerked backward, then thrown forward again, her arms clinging to its neck, her eyes squeezed shut and her lips pressed tight. The camera holds still.",
        "一个稳定的侧面中近景，从已采用的开场图继续，场景是私人跑马场：黑马的头和脖子向上、向后猛甩，鬃毛飞起，头乱甩；莉莉的整个上半身被拽得向后仰，随即又被甩向前，双臂紧抱着马脖子，眼睛紧闭，嘴唇抿紧。镜头固定不动。",
        SND)
    s['seed'] = seed
    s['depends_on_previous'] = False


P1(3, 4904)
P1(5, 4904)
P2(4, 4905)
a.finish('剧本第7–8集｜人立腿部动作测试', '同一匹马的人立，换三种写法：腿的动作写成动词（3 秒、5 秒）、只拍头颈和莉莉上身不拍腿（4 秒）。', OUT)
