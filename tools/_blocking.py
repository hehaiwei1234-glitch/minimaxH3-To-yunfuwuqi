"""站位表检查（2026-10-12 起，每份新稿必须先过这一关再交给 hh）。

为什么有它：剧本第 23–24 集 hh 指出的 6 个问题里 5 个是我写错的，全是同一类——
没有逐个镜头核对“谁在画面里、谁看着谁、谁对谁说话、事情的先后”。清单靠“读一遍”遵守做不到，
做成程序检查的错误后来都不再犯，所以把这些写成程序。

每个任务写一张站位表 B(...)：
  room   这一刻在这个地方的人（含不在画面里的）
  frame  画面里的人 {人: '左'/'中'/'右'…}
  gaze   画面里每个人看着谁 {人: 另一个画面里的人 或 'obj:某物'（画面里的东西）或 'closed'}
  says   [(说话人, 对谁说)]，两个人都必须在画面里
  enter / exit  这一镜里走进来／走出去的人（必须在画面里被看见）
  st_in / st_out  画面里每个人这一镜开头／结尾的状态（姿势、衣着、伤、眼睛颜色、在哪儿）
  trigger  这一镜里有一句会“引发动作”的台词 → 被引发的动作不准写在同一镜，写进下一镜的 effect
  effect   这一镜开头执行的是上一镜哪句台词引发的动作
  interrupt [(被打断的动作, 打断的人)] → 打断的人必须从第一帧就在画面里

检查（任何一条不过就报错，不交稿）：
  1 画面里的人都在 room 里；2 画面里每个人都有 gaze，目标在画面里或是 obj；
  3 说话人和听的人都在画面里，且听的人≠说话人；4 room 的变化只能来自 enter/exit；
  5 同一个人在前后两次出镜之间状态要接上（上一镜 st_out == 下一镜 st_in）；
  6 trigger 和 effect 不在同一镜，且 trigger 的下一镜必须写 effect；7 打断的人在画面里；
  8 和制作稿文字对账：开场图里每个人那一段文字必须写出他看着谁（名字）。
"""
import re


def B(**kw):
    kw.setdefault('enter', set()); kw.setdefault('exit', set()); kw.setdefault('says', [])
    kw.setdefault('st_in', {}); kw.setdefault('st_out', {}); kw.setdefault('interrupt', [])
    kw.setdefault('trigger', None); kw.setdefault('effect', None)
    kw['room'] = set(kw['room']); kw['enter'] = set(kw['enter']); kw['exit'] = set(kw['exit'])
    return kw


def check(blocks, names=None, prompts=None):
    """blocks: [(任务编号, B)]（同一场戏按顺序）；names: {人: 开场图里用的英文名}；prompts: {任务编号: 开场图文字}。
    返回问题列表（空 = 通过）。"""
    errs = []
    last_state = {}
    prev = None
    for i, (tid, b) in enumerate(blocks):
        fr = set(b['frame'])
        if not fr <= b['room']:
            errs.append(f'{tid}: 画面里有不在场的人 {fr - b["room"]}')
        for p in fr:
            g = b['gaze'].get(p)
            if not g:
                errs.append(f'{tid}: {p} 没写看着谁')
            elif g not in fr and not g.startswith('obj:') and g != 'closed':
                errs.append(f'{tid}: {p} 看着 {g}，但 {g} 不在画面里')
        for sp, to in b['says']:
            if sp not in fr: errs.append(f'{tid}: 说话的 {sp} 不在画面里')
            if to not in fr: errs.append(f'{tid}: {sp} 对 {to} 说话，但 {to} 不在画面里')
            if to == sp: errs.append(f'{tid}: {sp} 对自己说话')
            if b['gaze'].get(sp) not in (to, None) and not b['gaze'].get(sp, '').startswith('obj:'):
                errs.append(f'{tid}: {sp} 对 {to} 说话，却看着 {b["gaze"].get(sp)}')
        for p in b['enter'] | b['exit']:
            if p not in fr: errs.append(f'{tid}: {p} 进出场没有被拍到（不在画面里）')
        if prev is not None:
            want = (prev['room'] - prev['exit']) | b['enter']
            if b['room'] != want:
                errs.append(f'{tid}: 在场的人变了却没交代进出：多了 {b["room"] - want}，少了 {want - b["room"]}')
            if prev['trigger'] and not b['effect']:
                errs.append(f'{tid}: 上一镜的台词“{prev["trigger"]}”引发的动作没有放在这一镜开头')
        if b['trigger'] and b['effect'] == b['trigger']:
            errs.append(f'{tid}: 台词和它引发的动作写在同一镜（会先动后说）')
        for act, who in b['interrupt']:
            if who not in fr: errs.append(f'{tid}: “{act}”的打断者 {who} 不在画面里（会凭空出现）')
        for p in fr:
            if p in b['st_in'] and p in last_state and last_state[p] != b['st_in'][p]:
                errs.append(f'{tid}: {p} 的状态接不上：上次出镜结尾“{last_state[p]}”，这一镜开头“{b["st_in"][p]}”')
            if p in b['st_out']:
                last_state[p] = b['st_out'][p]
            elif p in b['st_in']:
                last_state[p] = b['st_in'][p]
        if names and prompts and tid in prompts:
            errs += _gaze_in_prompt(tid, b, names, prompts[tid])
        prev = b
    return errs


def _gaze_in_prompt(tid, b, names, text):
    """开场图文字里，每个人的那一句要写出“眼睛…看着/盯着 目标的名字”（或 eyes closed/shut）。"""
    errs = []
    sents = re.split(r'(?<=\.)\s+', text)
    for p in b['frame']:
        n = names.get(p)
        if not n or p in b.get('nogaze', ()): continue
        mine = [s for s in sents if re.match(r'\s*(?:%s)\b' % re.escape(n), s)]
        if not mine:
            errs.append(f'{tid}: 开场图里找不到以 {n} 开头的那句描写'); continue
        g = b['gaze'][p]
        s = ' '.join(mine)
        if g == 'closed':
            if not re.search(r'eyes (?:\w+ )?(?:closed|shut)|eyes squeezed shut', s): errs.append(f'{tid}: 开场图里 {n} 应写闭着眼')
            continue
        target = g[4:] if g.startswith('obj:') else names.get(g, g)
        if not re.search(r'eyes[^.;]{0,60}\b(?:on|at|toward|towards|fixed on|locked on)\b[^.;]{0,40}\b%s' % re.escape(target), s, re.I):
            errs.append(f'{tid}: 开场图里 {n} 没写看着 {target}')
    return errs
