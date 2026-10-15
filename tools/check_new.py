#!/usr/bin/env python3
"""一键检查一份追加稿：python3 tools/check_new.py <新.json> <底.json> [每集最低秒数=66]
检查：写法检查(lint) → 每集预算 → 与底稿 style／旧素材／旧角色逐项相同 → 素材≤200、角色≤100、文件≤3MB → 种子全 37407 → 插件格式校验。"""
import json, os, subprocess, sys
new, base = sys.argv[1], sys.argv[2]
need = sys.argv[3] if len(sys.argv) > 3 else '66'
S = '/tmp/claude-0/-home-claude-minimaxh3-to-yunfuwuqi/62e44c31-630b-5947-ac4b-f3d3c75433c7/scratchpad'
ok = True
r = subprocess.run([sys.executable, 'tools/lint_draft.py', new], capture_output=True, text=True)
print((r.stdout + r.stderr).strip()[-1800:])
ok &= r.returncode == 0
r = subprocess.run([sys.executable, 'tools/check_budget.py', new, need], capture_output=True, text=True)
print(r.stdout.strip()); ok &= r.returncode == 0
n = json.load(open(new, encoding='utf-8')); b = json.load(open(base, encoding='utf-8'))
same = n['style'] == b['style']
na = {a['key']: a for a in n['assets']}
for a in b['assets']:
    if na.get(a['key']) != a: same = False; print('  ✗ 旧素材不一致', a['key'])
for k, c in b['characters'].items():
    if n['characters'].get(k) != c: same = False; print('  ✗ 旧角色不一致', k)
print('底稿逐项一致：', '通过' if same else '✗'); ok &= same
print('素材', len(n['assets']), '/200；角色', len(n['characters']), '/100；文件 %.0f KB' % (os.path.getsize(new) / 1024))
ok &= len(n['assets']) <= 200 and len(n['characters']) <= 100 and os.path.getsize(new) < 3 * 1024 * 1024
seeds = {s['seed'] for e in n['episodes'] for s in e['segments']}
print('种子：', seeds); ok &= seeds == {37407}
txt = new.replace('.json', '_全选复制粘贴.txt')
if os.path.exists(S + '/validate.py'):
    r = subprocess.run([sys.executable, S + '/validate.py', S + '/plugin/ComfyUI-H3-AutoDrama-Standalone', txt], capture_output=True, text=True)
    print('插件格式校验：', (r.stdout + r.stderr).strip()[-300:]); ok &= r.returncode == 0
print('全部通过' if ok else '有未通过项')
sys.exit(0 if ok else 1)
