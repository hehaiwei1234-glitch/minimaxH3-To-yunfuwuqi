#!/usr/bin/env python3
"""把生成脚本里每集任务的编号（'56-03b'、标题里的“03｜”）按出现顺序重排成 01、02、03…  用法：python3 tools/_renum.py <脚本>"""
import re, sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
cnt = {}
def f(m):
    fn, ep = m.group(1), m.group(2)
    cnt[ep] = cnt.get(ep, 0) + 1
    n = '%02d' % cnt[ep]
    return f"{fn}('{ep}-{n}', '{n}｜"
s = re.sub(r"(DL|INS|TAA|TA|TAV|insert2)\('(\d\d)-\w+', '\d\d｜", f, s)
open(p, 'w', encoding='utf-8').write(s)
print(cnt)
