# Coconala sample #2: fictional izakaya English menu, A4 x 2 pages PDF (+ PNG previews).
# Style: English name first, romaji in (), short description, price tax-included, allergens ONLY as given by the (fictional) shop.
import json, pathlib, html, subprocess
from playwright.sync_api import sync_playwright
H = pathlib.Path(__file__).resolve().parent
D = json.loads((H/'menu-sample.json').read_text(encoding='utf-8'))
e = html.escape
C = '#9E2B25'
AL = {'egg':'Egg','milk':'Milk','wheat':'Wheat','shrimp':'Shrimp','crab':'Crab','soba':'Buckwheat','peanut':'Peanut','walnut':'Walnut','soy':'Soy','fish':'Fish','sesame':'Sesame'}
CSS = f'''@page{{size:A4;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:"Noto Sans CJK JP",sans-serif;color:#2A211C;font-size:9.6pt;line-height:1.4}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;background:#FBF6EE;page-break-after:always;padding:13mm 14mm 0}}
.pg:last-child{{page-break-after:auto}}
.mock{{position:absolute;right:12mm;top:8mm;border:1.2px solid {C};color:{C};font-size:7.5pt;font-weight:700;padding:.6mm 2.5mm;border-radius:2mm;background:#fff}}
.hd{{text-align:center;border-bottom:2.4px solid {C};padding-bottom:3mm;margin-bottom:4mm}}
.hd .jp{{font-size:10pt;color:{C};font-weight:700;letter-spacing:.3em}}
.hd h1{{font-size:26pt;font-weight:900;letter-spacing:.04em;line-height:1.1;margin-top:1mm}}
.hd p{{font-size:9pt;color:#6A5D53;margin-top:1.5mm}}
h2{{font-size:14pt;font-weight:900;color:#fff;background:{C};display:inline-block;padding:.8mm 4mm;border-radius:1.5mm;margin:5mm 0 2mm}}
h2 small{{font-weight:500;font-size:9pt;margin-left:2mm;opacity:.9}}
.grid{{display:grid;grid-template-columns:1fr 1fr;column-gap:7mm}}
.it{{padding:3.2mm 0;border-bottom:1px dotted #CDBFAF;break-inside:avoid}}
.row{{display:flex;justify-content:space-between;gap:3mm;align-items:baseline}}
.en{{font-weight:700;font-size:11.6pt}}
.pr{{font-weight:700;color:{C};white-space:nowrap}}
.ro{{font-size:9pt;color:#6A5D53}}
.ds{{font-size:9.4pt;margin-top:.6mm}}
.tg{{margin-top:.8mm;display:flex;flex-wrap:wrap;gap:1mm}}
.tg i{{font-style:normal;font-size:7.2pt;border:1px solid #B9A896;border-radius:1mm;padding:0 1.5mm;color:#5A4D43}}
.tg i.v{{border-color:#3F7D3A;color:#3F7D3A}}
.note{{margin-top:8mm;line-height:1.6;background:#fff;border-left:3mm solid {C};padding:4mm 5mm;font-size:9.4pt;border-radius:1.5mm}}
.note b{{color:{C}}} .note p+p{{margin-top:2mm}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:11mm;background:#2A211C;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 14mm;font-size:8.4pt}}
'''
def item(x):
    tags = ''.join(f'<i>{AL[a]}</i>' for a in x.get('allergens',[]))
    if x.get('veg'): tags += '<i class=v>Vegetarian</i>'
    return f'''<div class=it><div class=row><span class=en>{e(x["en"])}</span><span class=pr>¥{x["price"]:,}</span></div>
<div class=ro>{e(x["romaji"])}・{e(x["ja"])}</div><div class=ds>{e(x["desc"])}</div>{f"<div class=tg>{tags}</div>" if tags else ""}</div>'''
def sec(s): return f'<h2>{e(s["en"])}<small>{e(s["ja"])}</small></h2><div class=grid>{"".join(item(x) for x in s["items"])}</div>'
head = f'<div class=hd><div class=jp>{e(D["shop_ja"])}</div><h1>{e(D["shop_en"])}</h1><p>{e(D["tagline"])}</p></div>'
foot = f'<div class=foot><span>{e(D["shop_en"])} · {e(D["shop_ja"])}</span><span>All prices include tax.</span></div>'
p1 = f'<section class=pg><span class=mock>Sample / 架空の制作見本</span>{head}{"".join(sec(s) for s in D["sections"][:2])}{foot}</section>'
notes = ''.join(f'<p>{x}</p>' for x in D['notes'])
p2 = f'<section class=pg><span class=mock>Sample / 架空の制作見本</span>{"".join(sec(s) for s in D["sections"][2:])}<div class=note>{notes}</div>{foot}</section>'
tmp = H/'_menu.html'; tmp.write_text(f'<!doctype html><html lang=en><head><meta charset=utf-8><style>{CSS}</style></head><body>{p1}{p2}</body></html>', encoding='utf-8')
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(); pg.goto(tmp.as_uri()); pg.wait_for_timeout(500)
    sp = pg.evaluate("[...document.querySelectorAll('.pg')].map(p=>{const f=p.querySelector('.foot').getBoundingClientRect().top;return Math.round(f-Math.max(...[...p.querySelectorAll('.it,.note')].map(x=>x.getBoundingClientRect().bottom)))})")
    print('space above footer (px):', sp)
    pg.pdf(path=str(H/'sample-english-menu.pdf'), format='A4', print_background=True, prefer_css_page_size=True); b.close()
tmp.unlink()
subprocess.run(['pdftoppm','-r','80','-png',str(H/'sample-english-menu.pdf'),str(H/'menu-preview')],check=True)
print('ok')
