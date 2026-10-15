#!/usr/bin/env python3
"""每集时长预算检查：python3 tools/check_budget.py <json> [最低秒数=66]
列出每集计划秒数和任务数，低于预算的集标 ✗ 并以非 0 退出。写新批次时必须先过这一关。"""
import json,sys
f=sys.argv[1]; need=float(sys.argv[2]) if len(sys.argv)>2 else 66
bad=0;tot=0
for e in json.load(open(f,encoding='utf-8'))['episodes']:
    s=sum(x['duration_seconds'] for x in e['segments']);tot+=s
    ok=s>=need;bad+=not ok
    print(('✓' if ok else '✗'),e['title'].split('｜')[1] if '｜' in e['title'] else e['title'],round(s),'秒',len(e['segments']),'个任务')
print('合计',round(tot),'秒，平均',round(tot/len(json.load(open(f,encoding='utf-8'))['episodes']),1),'秒/集；预算',need)
sys.exit(1 if bad else 0)
