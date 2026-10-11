#!/usr/bin/env python3
"""一回限り: 研究室サイト WordPress の DB ダンプ → Hugo（content/, data/, static/images/）
usage: python3 tools/wp2hugo_lab.py DUMP.sql FILES.tar.gz
"""
import sys, os, re, subprocess, tarfile, html, yaml
sys.path.insert(0, os.path.dirname(__file__))
from wpparse import rows

DUMP, TAR = sys.argv[1], sys.argv[2]
OLD = r'https?://(?:www\.)?yamamotolab\.net'
UP = re.compile(OLD + r'/wp/wp-content/uploads/(\d{4}/\d{2}/[^"\'\s)<>]+)')

SLUG = {'115':'dbws-2021-best-student-presentation','119':'data-analysis-competition-award','122':'deim-2022','124':'new-members',
'128':'website-launch','195':'welcome-party','207':'bbq','219':'dbws-2022','246':'deim-2023','256':'farewell-party','241':'new-members',
'238':'welcome-party','324':'review-attribute-language-model','342':'thumbnail-dom-role','347':'controversial-topic-opinion',
'357':'museum-question-answering','353':'procedural-query-goal','367':'spoken-search-aspect-suggestion','383':'ipsj-ifat-151',
'390':'sigmod-japan-82','392':'bbq','387':'lab-trip','398':'icadl-2023-accepted','409':'dbws-2023','459':'icadl-2023',
'475':'year-end-party','497':'deim-2024','484':'farewell-party','520':'llm-review-exploration','512':'sentence-similarity-evidence',
'527':'personalized-headline','534':'welcome-party','548':'erdse-2024','559':'bbq','574':'sigir-ap-2024-accepted',
'579':'sigir-ap-2024-best-paper-nominee','581':'idr-forum-2024-award','593':'year-end-party','609':'deim-2025','623':'farewell-party',
'640':'new-members','643':'welcome-party','658':'dawak-2025','666':'deim-2025-best-paper','710':'llm-query-rewriting-reviews',
'709':'llm-review-summarization','711':'review-rating-completion','724':'model-merging-adhoc','733':'sigir-2025-excellent-pc',
'737':'pun-generation','740':'response-length-spoken-search','757':'bbq','750':'ipsj-tod-tobioka','752':'cikm-2025',
'764':'iiwas-2025-accepted','772':'dbws-2025','789':'webdb-summer-2025','805':'sigir-ap-2025-outstanding-reviewer',
'813':'cikm-2025-poster','820':'idr-forum-2025','831':'iiwas-2025','850':'ipsj-tod-tobioka','855':'dbsj-journal-fujii',
'861':'dbsj-young-researcher-award','871':'deim-2026','885':'kamikawa-award','897':'new-members','902':'ecir-2026-outstanding-reviewer',
'904':'ipsj-tod-sasaki','977':'welcome-party','910':'ictir-2026-accepted','959':'ictir-2026','917':'u-hyogo-young-researcher-award',
'958':'bbq','919':'besc-2026','946':'webdb-summer-2026','932':'sigir-ap-2026'}

BLOCK = r'(?:div|ul|ol|li|h[1-6]|table|thead|tbody|tr|td|th|blockquote|pre|p|dl|dt|dd|hr|figure|figcaption|iframe|!--)'
def autop(t):
    t = t.replace('\r\n', '\n')
    t = re.sub(r'(<' + BLOCK + r'[^>]*>)', r'\n\n\1', t)
    t = re.sub(r'(</(?:div|ul|ol|li|h[1-6]|table|tr|blockquote|pre|p|dl|figure|iframe)>|-->)', r'\1\n\n', t)
    out = []
    for para in re.split(r'\n\s*\n', t):
        para = para.strip()
        if not para: continue
        if re.match(r'<' + BLOCK, para) or re.match(r'</', para): out.append(para)
        else: out.append('<p>' + para.replace('\n', '<br />\n') + '</p>')
    return '\n'.join(out)

used = set()
def fix_urls(h):
    def rep(m):
        used.add(m.group(1)); return '/images/' + m.group(1)
    h = UP.sub(rep, h)
    return re.sub(OLD + r'/(?=[a-z])', '/', h)   # サイト内リンクは相対に（旧URLは転送で生きる）

def to_md(h):
    h = re.sub(r'<!--.*?-->', '', h, flags=re.S)
    h = re.sub(r'<hr[^>]*>', '', h)                       # 見出し下の装飾線（CSSで代替）
    h = re.sub(r'</?span[^>]*>', '', h)
    h = re.sub(r'<p>&nbsp;</p>', '', h)
    h = re.sub(r'<(/?)h2>\s*<strong>(.*?)</strong>\s*</h2>', r'<\1h2>\2</h2>', h)
    h = re.sub(r'<h([23])><strong>(.*?)</strong></h\1>', r'<h\1>\2</h\1>', h)
    h = fix_urls(h)
    iframes = []
    def keep(m): iframes.append(m.group(0)); return f'IFRAMEPLACEHOLDER{len(iframes)-1}X'
    h = re.sub(r'<iframe.*?</iframe>', keep, h, flags=re.S)
    md = subprocess.run(['pandoc', '-f', 'html', '-t', 'gfm', '--wrap=none'], input=autop(h),
                        capture_output=True, text=True, check=True).stdout
    md = md.replace('\\\n', '  \n')
    for i, f in enumerate(iframes):
        f = re.sub(r'\s(width|height)="\d+"', '', f).replace('<iframe', '<iframe width="640" height="420" loading="lazy"')
        md = md.replace(f'IFRAMEPLACEHOLDER{i}X', f)
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip() + '\n'

def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
def write(path, fm, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lines = ['---'] + [f'{k}: {v}' for k, v in fm.items()] + ['---', '']
    open(path, 'w', encoding='utf-8').write('\n'.join(lines) + '\n' + body)

sql = open(DUMP, encoding='utf-8', errors='replace').read()
P = {r[0]: r for r in rows(sql, 'wp_posts')}
T = {r[0]: r[1] for r in rows(sql, 'wp_terms')}
TT = {r[0]: (r[1], r[2]) for r in rows(sql, 'wp_term_taxonomy')}
cats = {}
for r in rows(sql, 'wp_term_relationships'):
    if TT.get(r[1], ('', ''))[1] == 'category': cats.setdefault(r[0], []).append(T[TT[r[1]][0]])
thumb = {r[1]: r[3] for r in rows(sql, 'wp_postmeta') if r[2] == '_thumbnail_id'}

# ---- 投稿 ----
for r in P.values():
    if r[7] != 'publish' or r[20] != 'post': continue
    pid, date, title = r[0], r[2], html.unescape(r[5]).strip()
    sec = 'research' if '研究紹介' in cats.get(pid, []) else 'posts'
    fm = {'title': q(title)}
    if pid in thumb and thumb[pid] in P:
        m = UP.search(P[thumb[pid]][18])
        if m: used.add(m.group(1)); fm['image'] = q('/images/' + m.group(1))
    fm['wp_id'] = pid
    y, mo = date[:4], date[5:7]
    fm['aliases'] = f'["/archives/{y}/{mo}/{pid}/"]   # 旧WordPressのURLからの転送'
    write(f'content/{sec}/{date[:10]}-{SLUG[pid]}.md', fm, to_md(r[4]))

# ---- 固定ページ ----
home = P['39'][4]
write('content/_index.md', {'title': q('山本研究室へようこそ')}, to_md(home))
write('content/access.md', {'title': q('アクセス'), 'aliases': '["/access/"]'}, to_md(P['35'][4]))
write('content/join.md', {'title': q('学生募集')}, to_md(P['44'][4]))
write('content/research/_index.md', {'title': q('研究紹介'),
      'aliases': '["/%e7%a0%94%e7%a9%b6%e7%b4%b9%e4%bb%8b/", "/category/%e7%a0%94%e7%a9%b6%e7%b4%b9%e4%bb%8b/"]'},
      '山本研究室の学生による研究を紹介します。\n')
write('content/posts/_index.md', {'title': q('記事'), 'aliases': '["/news/", "/category/%e8%a8%98%e4%ba%8b/"]'}, '')
write('content/members.md', {'title': q('メンバー'), 'aliases': '["/member/"]'},
      '<!-- メンバーは data/members.yaml に書く -->\n{{< members >}}\n')
write('content/publications.md', {'title': q('研究成果'), 'aliases': '["/publications/"]'},
      '山本岳洋個人の業績リストは[こちら](https://rerank-lab.org/publication/)もご参照ください．\n\n'
      '<!-- 研究成果は data/publications.yaml に書く -->\n{{< publications >}}\n')

# ---- メンバー → data/members.yaml ----
m = P['33'][4]
groups = []
for h, body in re.findall(r'<h[23]>\s*<strong>(.*?)</strong>\s*</h[23]>(.*?)(?=<h[23]>|\Z)', m, re.S):
    items = []
    for li in re.findall(r'<li>(.*?)</li>', body, re.S):
        url = re.search(r'href="([^"]+)"', li)
        t = html.unescape(re.sub(r'<[^>]+>', '', li)).strip()
        mm = re.match(r'(.*?)\s*[（(]\s*([^）)]+?)\s*[)）]\s*$', t)
        it = {'ja': mm.group(1).strip(), 'en': mm.group(2).strip()} if mm else {'ja': t}
        if url: it['url'] = url.group(1)
        items.append(it)
    if items: groups.append({'name': h.strip(), 'members': items})
with open('data/members.yaml', 'w', encoding='utf-8') as f:
    f.write('# メンバー一覧。毎年4月に学年を更新する。groups の順に表示される。\n\n')
    yaml.dump({'groups': groups}, f, allow_unicode=True, sort_keys=False, width=1000)

# ---- 研究成果 → data/publications.yaml ----
p = P['671'][4]
pubs = []
for fy, body in re.findall(r'<h2>\s*<strong>(\d{4})年度</strong>\s*</h2>(.*?)(?=<h2>|\Z)', p, re.S):
    for li in re.findall(r'<li>(.*?)</li>', body, re.S):
        lines = [l.strip() for l in li.replace('\r', '').strip().split('\n') if l.strip()]
        lines = [html.unescape(re.sub(r'</?em>', '', l)) for l in lines]
        e = {'fy': int(fy), 'authors': lines[0], 'title': lines[1], 'venue': ' '.join(lines[2:])}
        pubs.append(e)
with open('data/publications.yaml', 'w', encoding='utf-8') as f:
    f.write('# 研究成果。fy は年度（4月始まり）。年度ごとに見出しが付き、年度内は書いた順に表示。新しいものは先頭に追加。\n\n')
    yaml.dump({'items': pubs}, f, allow_unicode=True, sort_keys=False, width=1000)

# ---- 画像 ----
with tarfile.open(TAR) as tf:
    names = set(tf.getnames())
    miss = []
    for u in sorted(used):
        src = 'www-lab/wp/wp-content/uploads/' + u
        if src not in names: miss.append(u); continue
        dst = 'static/images/' + u
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with tf.extractfile(src) as fi, open(dst, 'wb') as fo: fo.write(fi.read())
print('images', len(used), 'missing', miss)
print('members', [(g['name'], len(g['members'])) for g in groups], 'pubs', len(pubs))
