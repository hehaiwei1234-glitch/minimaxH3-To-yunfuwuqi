#!/usr/bin/env python3
"""修订版任务号对照：原稿第 X 集第 NN 号 → 修订版第几号（按任务标题文字匹配；匹配不上的是新增的插镜或改写过标题的任务）。
用法：python3 tools/map_old_new.py [集号]      不写集号就打印全部（第 29–74 集）
原稿：29–44 集用 017 合并稿；45–46 集用 018 十二秒版；47–50 集用 019 十二秒版；51–54 集用 020；55–74 集用 026。"""
import json, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '极寒末日_隐秘安全屋', '合并稿')
def load(p):
    d = json.load(open(p, encoding='utf-8'))
    return {e['title'].split('｜')[0]: [s['title'] for s in e['segments']] for e in d['episodes']}
def one(pat): return glob.glob(os.path.join(D, pat))[0]
olds = {}
for p in (one('017_*.json'), one('018_第45-46集_十二秒版*追加.json'), one('019_第47-50集_十二秒版*追加.json'), one('020_*追加.json'), one('026_*追加.json')):
    for k, v in load(p).items(): olds[k] = v      # 后面的覆盖前面的（026 里没有 29–54 集，不冲突）
news = {}
for p in (os.path.join(D, '修订版', '第29-44集_修订合并_制作稿_追加.json'), os.path.join(D, '修订版', '第45-74集_修订合并_制作稿_追加.json')):
    news.update(load(p))
def txt(t): return re.sub(r'^\d+｜', '', t)
want = sys.argv[1] if len(sys.argv) > 1 else None
for ep in sorted(news, key=lambda k: int(re.search(r'\d+', k).group())):
    if want and re.search(r'\d+', ep).group() != want: continue
    o = olds.get(ep, []); ot = {txt(t): i + 1 for i, t in enumerate(o)}
    print(f'{ep}：原 {len(o)} 个 → 新 {len(news[ep])} 个')
    for i, t in enumerate(news[ep], 1):
        j = ot.get(txt(t))
        print(f'  新第{i:02d}号 ← ' + (f'原第{j:02d}号' if j else '新增／改写') + '：' + txt(t)[:44])
