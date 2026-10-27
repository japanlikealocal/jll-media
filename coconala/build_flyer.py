# Coconala sample: fictional cooking-class trial flyer, A4 x 2 pages, PDF.
# Data-driven so date/price/name swaps are one-line changes. Usage: python3 build_flyer.py [data.json] [out.pdf]
import json, sys, pathlib, html
from playwright.sync_api import sync_playwright
H = pathlib.Path(__file__).resolve().parent
D = json.loads((H / (sys.argv[1] if len(sys.argv) > 1 else 'sample.json')).read_text(encoding='utf-8'))
OUT = H / (sys.argv[2] if len(sys.argv) > 2 else 'sample-cooking-class.pdf')
e = html.escape
C = D.get('color', '#C2552D')
CSS = f'''
@page{{size:A4;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:"Noto Sans CJK JP",sans-serif;word-break:auto-phrase;text-wrap:pretty;color:#2B2622;font-size:10.5pt;line-height:1.75}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;background:#FBF7F1;page-break-after:always}}
.pg:last-child{{page-break-after:auto}}
.band{{height:9mm;background:{C}}}
.mock{{position:absolute;right:12mm;top:12mm;border:1.2px solid {C};color:{C};font-size:8pt;font-weight:700;padding:1mm 3mm;border-radius:2mm;background:#fff}}
.wrap{{padding:14mm 16mm 0}}
.kick{{color:{C};font-weight:700;font-size:11pt;letter-spacing:.12em}}
h1{{font-size:30pt;line-height:1.25;font-weight:900;margin:3mm 0 3mm;letter-spacing:.02em}}
.lead{{font-size:12pt;color:#5A524B;margin-bottom:8mm}}
.circle{{position:absolute;right:-30mm;top:40mm;width:110mm;height:110mm;border-radius:50%;background:{C};opacity:.09}}
.grid{{display:grid;grid-template-columns:30mm 1fr;border-top:2px solid #2B2622}}
.grid div{{padding:4.2mm 0;border-bottom:1px solid #DDD3C7}}
.grid .k{{font-weight:700;color:{C}}}
.grid .v b{{font-size:15pt}}
.note{{font-size:9pt;color:#6B625A}}
.apply{{margin-top:9mm;background:#fff;border:2px solid {C};border-radius:4mm;padding:6mm 7mm}}
.apply h2{{font-size:13pt;margin-bottom:2mm}}
.apply ol{{padding-left:5mm}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:16mm;background:#2B2622;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 16mm;font-size:9.5pt}}
h2.sec{{font-size:15pt;font-weight:900;margin:0 0 3mm;padding-left:3.5mm;border-left:2.2mm solid {C}}}
.about{{margin-bottom:9mm}}
table{{width:100%;border-collapse:collapse;margin-bottom:9mm}}
th,td{{text-align:left;padding:3mm 3.5mm;border-bottom:1px solid #DDD3C7;vertical-align:top}}
th{{width:28mm;color:#fff;background:{C};font-weight:700;border-bottom:1px solid #fff}}
.qa{{display:grid;gap:3mm}}
.q{{font-weight:700}} .q:before{{content:"Q. ";color:{C}}}
.a:before{{content:"A. ";font-weight:700;color:#8A8077}}
.qa .item{{background:#fff;border-radius:3mm;padding:3.5mm 4.5mm}}
'''
def rows(items): return ''.join(f'<div class=k>{e(k)}</div><div class=v>{v}</div>' for k, v in items)
p1 = f'''<section class=pg><div class=band></div><div class=circle></div><span class=mock>架空の制作見本</span>
<div class=wrap><div class=kick>{e(D["kicker"])}</div><h1>{e(D["title"]).replace(chr(10),"<br>")}</h1><p class=lead>{e(D["lead"])}</p>
<div class=grid>{rows([("日時", f'<b>{e(D["date"])}</b><br>{e(D["time"])}'), ("場所", f'{e(D["place"])}<br><span class=note>{e(D["access"])}</span>'),
 ("料金", f'<b>{e(D["price"])}</b><br><span class=note>{e(D["price_note"])}</span>'), ("定員", e(D["capacity"])), ("持ち物", e(D["bring"]))])}</div>
<div class=apply><h2>お申し込み方法</h2><ol>{''.join(f"<li>{e(x)}</li>" for x in D["apply"])}</ol><p class=note style="margin-top:2mm">{e(D["deadline"])}</p></div></div>
<div class=foot><span>{e(D["org"])}</span><span>{e(D["contact"])}</span></div></section>'''
p2 = f'''<section class=pg><div class=band></div><span class=mock>架空の制作見本</span>
<div class=wrap style="padding-top:16mm"><div class=about><h2 class=sec>教室について</h2><p>{e(D["about"])}</p></div>
<h2 class=sec>当日の流れ</h2><table>{''.join(f"<tr><th>{e(t)}</th><td>{e(x)}</td></tr>" for t, x in D["flow"])}</table>
<h2 class=sec>よくある質問</h2><div class=qa>{''.join(f'<div class=item><p class=q>{e(q)}</p><p class=a>{e(a)}</p></div>' for q, a in D["faq"])}</div></div>
<div class=foot><span>{e(D["org"])}</span><span>{e(D["contact"])}</span></div></section>'''
tmp = H / '_flyer.html'
tmp.write_text(f'<!doctype html><html lang=ja><head><meta charset=utf-8><style>{CSS}</style></head><body>{p1}{p2}</body></html>', encoding='utf-8')
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(); pg.goto(tmp.as_uri()); pg.wait_for_timeout(500)
    over = pg.evaluate("[...document.querySelectorAll('.pg')].map(p=>{const f=p.querySelector('.foot').getBoundingClientRect().top;return Math.round(f-Math.max(...[...p.querySelectorAll('.wrap > *')].map(x=>x.getBoundingClientRect().bottom)))})")
    print('space above footer (px):', over)
    pg.pdf(path=str(OUT), format='A4', print_background=True, prefer_css_page_size=True); b.close()
tmp.unlink(); print('ok', OUT.name)
