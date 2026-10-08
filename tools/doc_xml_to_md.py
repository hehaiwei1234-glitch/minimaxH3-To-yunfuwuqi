#!/usr/bin/env python3
"""把 Claude Docs 的 read(view) 结果(JSON,里面有 data.xml)转成 Markdown。
用法: python3 doc_xml_to_md.py <read结果.json> <输出.md>
"""
import sys, json
import xml.etree.ElementTree as ET

def inline(el):
    out = el.text or ''
    for ch in el:
        t = inline(ch)
        if ch.tag == 'bold' and t.strip(): t = f'**{t}**'
        elif ch.tag == 'code' and t: t = f'`{t}`'
        out += t + (ch.tail or '')
    return out

def para_text(p):
    return ''.join(inline(c) + (c.tail or '') if c.tag != 'text' else inline(c) for c in p if c.tag in ('text','bold','code')) or inline(p)

def block(el, indent=''):
    tag = el.tag
    lines = []
    if tag == 'paragraph':
        t = ''.join(inline(c) for c in el)
        h = el.get('heading')
        lines.append(('#' * int(h) + ' ' if h else '') + t)
        lines.append('')
    elif tag == 'list':
        kind = el.get('kind', 'bullet'); n = 0
        for it in el:
            if it.tag != 'listItem': continue
            n += 1
            mark = f'{n}. ' if kind == 'ordered' else ('- [ ] ' if kind == 'check' else '- ')
            first = True
            for c in it:
                if c.tag == 'paragraph':
                    t = ''.join(inline(x) for x in c)
                    if first: lines.append(indent + mark + t); first = False
                    else: lines.append(indent + '    ' + t)
                elif c.tag == 'list':
                    lines.extend(block(c, indent + '    ')[0:-1] if False else [l for l in block(c, indent + '    ') if l != ''])
        lines.append('')
    elif tag == 'table':
        rows = []
        for r in el:
            if r.tag != 'row': continue
            cells = []
            for c in r:
                if c.tag != 'cell': continue
                parts = [''.join(inline(x) for x in p) for p in c if p.tag == 'paragraph']
                cells.append('<br>'.join(parts).replace('|', '\\|').replace('\n', ' '))
            rows.append(cells)
        if rows:
            w = max(len(r) for r in rows)
            rows = [r + [''] * (w - len(r)) for r in rows]
            lines.append('| ' + ' | '.join(rows[0]) + ' |')
            lines.append('|' + '---|' * w)
            for r in rows[1:]: lines.append('| ' + ' | '.join(r) + ' |')
        lines.append('')
    return lines

if __name__ == '__main__':
    j = json.load(open(sys.argv[1], encoding='utf-8'))
    root = ET.fromstring(j['data']['xml'])
    out = []
    for el in root: out.extend(block(el))
    open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out).rstrip() + '\n')
    print('blocks', len(list(root)), 'chars', sum(len(x) for x in out))
