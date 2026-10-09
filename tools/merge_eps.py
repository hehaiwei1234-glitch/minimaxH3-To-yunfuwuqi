#!/usr/bin/env python3
"""把几份“追加”制作稿合并成一份（一次粘贴、一次跑完）。
用法: python3 tools/merge_eps.py 输出名(不含扩展名) 稿1.json 稿2.json ... [--rename 原集标题=新集标题 ...]
要求：靠后的稿是靠前的稿的“超集”（素材/人物是以前一份为底再追加的）；本脚本逐项核对，对不上就报错。
合并结果的素材/人物/风格取最后一份；episodes 按顺序拼起来。"""
import json, os, sys
FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Alpha继兄的笼中吻')
args = sys.argv[1:]
ren = {}
if '--rename' in args:
    i = args.index('--rename')
    for kv in args[i + 1:]:
        a, b = kv.split('=', 1); ren[a] = b
    args = args[:i]
out, files = args[0], args[1:]
docs = [json.load(open(f, encoding='utf-8')) for f in files]
last = docs[-1]
akey = {a['key']: a for a in last['assets']}
for f, d in zip(files, docs):
    assert d['title'] == last['title'], f'{f}: 总标题不同'
    assert d['style'] == last['style'], f'{f}: style 不同'
    assert d['dialogue_language'] == last['dialogue_language'], f'{f}: 台词语言不同'
    for a in d['assets']:
        assert akey.get(a['key']) == a, f'{f}: 素材 {a["key"]} 和最后一份不一致'
    for k, c in d['characters'].items():
        assert last['characters'].get(k) == c, f'{f}: 人物 {k} 和最后一份不一致'
eps, seeds = [], []
per_file = []
for d in docs:
    per_file.append({s['seed'] for e in d['episodes'] for s in e['segments']})
    for e in d['episodes']:
        e = dict(e)
        e['title'] = ren.get(e['title'], e['title'])
        eps.append(e)
        for s in e['segments']:
            seeds.append(s['seed'])
            for k in s['asset_keys']: assert k in akey, f'{s["title"]}: 素材 {k} 不存在'
for i in range(len(per_file)):
    for j in range(i + 1, len(per_file)):
        assert not (per_file[i] & per_file[j]), f'不同稿之间种子重复：{per_file[i] & per_file[j]}'
# 同一份稿内重复是允许的（第6集B 的对照组故意同种子）
merged = dict(last); merged['episodes'] = eps
txt = json.dumps(merged, ensure_ascii=False, indent=1)
open(os.path.join(FOLDER, out + '.json'), 'w', encoding='utf-8').write(txt)
open(os.path.join(FOLDER, out + '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(txt)
n = sum(len(e['segments']) for e in eps); sec = sum(s['duration_seconds'] for e in eps for s in e['segments'])
print(f'{len(eps)} 集、{n} 个任务、约 {sec} 秒；文件大小 {len(txt.encode())/1024:.0f} KB')
for e in eps: print('  ', e['title'], len(e['segments']), '个任务')
