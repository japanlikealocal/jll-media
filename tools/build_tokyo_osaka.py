# Tokyo vs Osaka: 8 Food Traditions (IG 1080x1350 + pin 1000x1500). Facts: docs/tokyo-osaka-sources-2026-11-03.md. Art: Gemini 4x4.
import pathlib
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; A=R/'assets/tokyo-osaka'; F=(R/'tools/fonts').as_uri()
SAM=(R/'assets/cutouts/samurai-base-wink.png').as_uri()
PAIRS=[('Udon broth','Dark soy','Pale dashi'),('Rolled omelette','Sweeter','Savory dashi'),
 ('Sakuramochi','Crepe wrap','Grainy rice'),('Inari sushi','Oblong','Triangle'),
 ('Unagi','Steamed, soft','Grilled, crisp'),('Home curry','Pork','Beef'),
 ('Okonomiyaki cut','Wedges','Squares'),('"Tanuki" soba','Tempura bits','Fried tofu')]
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:WPX;height:HPX;background:#FFF6E8;font-family:I;color:#2A1A10;overflow:hidden;position:relative}}
.head{{position:relative;height:HEADH;padding:20px 24px 0;background:linear-gradient(90deg,#1D4ED8 0 50%,#D62828 50% 100%)}}
.save{{display:inline-block;background:#FFD43B;color:#2A1A10;font-weight:800;font-size:24px;padding:6px 16px;border-radius:10px;transform:rotate(-3deg)}}
h1{{color:#fff;font-weight:800;font-size:HSIZE;line-height:.95;letter-spacing:-2px;margin-top:10px;text-shadow:0 3px 0 rgba(0,0,0,.25)}}
h1 em{{font-style:normal;color:#FFD43B;display:block}}
.sub{{color:#fff;font-weight:700;font-size:22px;margin-top:8px;opacity:.95}}
.sam{{position:absolute;right:14px;bottom:-4px;height:SAMH;z-index:3;filter:drop-shadow(0 6px 10px rgba(0,0,0,.35))}}
.bub{{position:absolute;right:SAMR;top:200px;z-index:3;background:#fff;font-weight:800;font-size:21px;padding:9px 14px;border-radius:16px;border:3px solid #2A1A10}}
.cols{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:8px 18px 4px}}
.cols div{{text-align:center;font-weight:800;font-size:20px;color:#fff;border-radius:8px;padding:4px 0}}
.t{{background:#1D4ED8}} .o{{background:#D62828}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding:2px 18px 0}}
.pair{{background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 2px 6px rgba(0,0,0,.08)}}
.pt{{display:flex;align-items:center;gap:8px;padding:6px 10px;font-weight:800;font-size:19px}}
.pt b{{width:28px;height:28px;border-radius:50%;background:#2A1A10;color:#FFD43B;display:flex;align-items:center;justify-content:center;font-size:15px}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:4px}}
.c{{position:relative;height:CH;background-size:cover;background-position:center}}
.lab{{position:absolute;left:0;right:0;bottom:0;padding:16px 6px 5px;color:#fff;font-weight:800;font-size:16px;text-align:center;background:linear-gradient(rgba(0,0,0,0),rgba(0,0,0,.72) 50%)}}
.tag{{position:absolute;left:5px;top:5px;font-weight:800;font-size:12px;color:#fff;padding:2px 7px;border-radius:6px}}
.ft{{position:absolute;left:18px;right:18px;bottom:10px;display:flex;justify-content:space-between;align-items:center;gap:12px;font-weight:700;font-size:12.5px;color:#6E5A4C;line-height:1.25}}
.cta{{background:#D62828;color:#fff;font-weight:800;font-size:17px;padding:8px 14px;border-radius:30px;white-space:nowrap}}
'''
def page(Wd,Hd,v):
    cells=''
    for i,(name,tk,os_) in enumerate(PAIRS):
        a=(A/f'p{2*i+1:02d}.jpg').as_uri(); b=(A/f'p{2*i+2:02d}.jpg').as_uri()
        cells+=f'''<div class=pair><div class=pt><b>{i+1}</b>{name}</div><div class=two>
<div class=c style="background-image:url({a})"><span class="tag t">TOKYO</span><div class=lab>{tk}</div></div>
<div class=c style="background-image:url({b})"><span class="tag o">OSAKA</span><div class=lab>{os_}</div></div></div></div>'''
    css=CSS
    for k,val in v.items(): css=css.replace(k,val)
    css=css.replace('WPX',f'{Wd}px').replace('HPX',f'{Hd}px')
    return f'''<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body>
<div class=head><div class=save>📌 SAVE THIS</div><h1>Tokyo vs Osaka<em>8 Food Traditions</em></h1><div class=sub>Same dish, different style — which side are you?</div>
<div class=bub>Comment TOKYO or OSAKA!</div><img class=sam src="{SAM}"></div>
<div class=grid>{cells}</div>
<div class=ft><span>Regional traditions, not strict rules — styles vary by shop and family. Okonomiyaki: Otafuku Sauce survey, 2023. AI illustrations for reference only.</span><span class=cta>💬 Comment JAPAN</span></div></body></html>'''
tmp=R/'tools/_to.html'
with sync_playwright() as pw:
    b=pw.chromium.launch()
    for name,Wd,Hd,v in [('ig-tokyo-vs-osaka',1080,1350,{'HEADH':'288px','HSIZE':'62px','SAMH':'220px','SAMR':'200px','CH':'196px'}),
                         ('pin-tokyo-vs-osaka',1000,1500,{'HEADH':'310px','HSIZE':'62px','SAMH':'240px','SAMR':'200px','CH':'230px'})]:
        pg=b.new_page(viewport={'width':Wd,'height':Hd}); tmp.write_text(page(Wd,Hd,v)); pg.goto(tmp.as_uri()); pg.wait_for_timeout(800)
        gap=pg.evaluate("document.querySelector('.ft').getBoundingClientRect().top-Math.max(...[...document.querySelectorAll('.pair')].map(e=>e.getBoundingClientRect().bottom))")
        print(name,'gap',round(gap)); pg.screenshot(path=str(R/f'assets/{name}.png'))
    b.close()
tmp.unlink()
