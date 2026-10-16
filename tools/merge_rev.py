#!/usr/bin/env python3
"""把“修订版”的几份追加稿合并成一份（2026-10-16）：素材／人物取并集（同名必须逐字相同），集按给定顺序拼起来。
用法（在仓库根目录）: python3 tools/merge_rev.py 输出路径(不含扩展名) 稿1.json 稿2.json ...
修订版的每份稿都以同一份底稿（026）为底，只有“新增的素材／人物”（耳机）不同，所以不能用 merge_eps.py（它要求后一份是前一份的超集）。"""
import json, sys
out, files = sys.argv[1], sys.argv[2:]
docs = [json.load(open(f, encoding='utf-8')) for f in files]
base = docs[0]
assets = {a['key']: a for a in base['assets']}
order = [a['key'] for a in base['assets']]
chars = dict(base['characters'])
for f, d in zip(files, docs):
    assert d['title'] == base['title'] and d['style'] == base['style'] and d['dialogue_language'] == base['dialogue_language'], f
    for a in d['assets']:
        if a['key'] in assets: assert assets[a['key']] == a, (f, '素材不一致', a['key'])
        else: assets[a['key']] = a; order.append(a['key'])
    for k, c in d['characters'].items():
        if k in chars: assert chars[k] == c, (f, '人物不一致', k)
        else: chars[k] = c
eps = [e for d in docs for e in d['episodes']]
for e in eps:
    for s in e['segments']:
        for k in s['asset_keys']: assert k in assets, (s['title'], k)
        for c in s['characters']: assert c in chars, (s['title'], c)
merged = dict(base); merged['assets'] = [assets[k] for k in order]; merged['characters'] = chars; merged['episodes'] = eps
txt = json.dumps(merged, ensure_ascii=False, indent=1)
open(out + '.json', 'w', encoding='utf-8').write(txt)
open(out + '_全选复制粘贴.txt', 'w', encoding='utf-8').write(txt)
n = sum(len(e['segments']) for e in eps); sec = sum(s['duration_seconds'] for e in eps for s in e['segments'])
print(f'{len(eps)} 集、{n} 个任务、约 {sec} 秒；素材 {len(assets)}、人物 {len(chars)}；文件 {len(txt.encode())/1024:.0f} KB')
