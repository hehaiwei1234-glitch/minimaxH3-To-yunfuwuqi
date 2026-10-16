#!/usr/bin/env python3
"""把一份“追加稿”裁成可以在新建的剧里单独贴的版本：只留任务实际用到的素材和角色。
用法：python3 tools/make_standalone.py <追加稿.json>  → 同目录写 <名>_单独版.json 和 _全选复制粘贴.txt"""
import json, re, sys
src = sys.argv[1]
d = json.load(open(src, encoding='utf-8'))
assets = {a['key']: a for a in d['assets']}
chars = d['characters']
segs = [s for e in d['episodes'] for s in e['segments']]
keys, names = set(), set()
def scan(o):
    t = json.dumps(o, ensure_ascii=False)
    keys.update(re.findall(r'\[\[asset:([A-Za-z0-9_]+)\]\]', t))
for e in d['episodes']:
    scan({k: v for k, v in e.items() if k != 'segments'})
for s in segs:
    keys.update(s.get('asset_keys', [])); keys.update(s.get('image_reference_keys', []))
    names.update(s.get('characters', [])); names.update(x['speaker'] for x in s.get('dialogue', []))
    scan(s)
names = {n for n in names if n in chars}
for n in names: keys.update(chars[n].get('image_keys', []))
while True:   # 素材生成时引用的参考图也要留
    more = set()
    for k in keys:
        a = assets.get(k)
        if a and 'generate' in a: more.update(a['generate'].get('reference_keys', []))
    if more <= keys: break
    keys |= more
d['assets'] = [a for a in d['assets'] if a['key'] in keys]
d['characters'] = {k: v for k, v in chars.items() if k in names}
import os
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(src))), '单独版_新建一部剧直接贴', os.path.basename(src).replace('.json', '_单独版.json'))
txt = json.dumps(d, ensure_ascii=False, indent=1)
open(out, 'w', encoding='utf-8').write(txt)
open(out.replace('.json', '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(txt)
print('素材', len(d['assets']), '角色', len(d['characters']), '→', out)
