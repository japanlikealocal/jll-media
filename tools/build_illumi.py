# Tokyo Winter Illuminations 2026–27 (IG 1080x1350 + pin 1000x1500).
# Facts: Perplexity check of official sites 2026-10-25 (docs/illumi-sources.md). Art: ChatGPT watercolor grid (assets/illumi/grid.png).
import pathlib
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; A=R/'assets/illumi'; F=(R/'tools/fonts').as_uri()
SAM=(R/'assets/cutouts/samurai-base-wink.png').as_uri()
SPOTS=[ # panel, name, area, dates, extra, paid
 ('p01','Marunouchi','Tokyo Sta.','Nov 12 – Feb 14','Champagne-gold avenue',0),
 ('p02','Hibiya Magic Time','Hibiya','Nov 12 – Feb 28','4 – 11 pm',0),
 ('p03','Roppongi Keyakizaka','Roppongi','Nov 5 – Dec 25','5 – 10 pm · white & blue',0),
 ('p04','Tokyo Midtown','Roppongi','Nov 26 – Dec 25','Hours TBA',0),
 ('p05','Yebisu Garden Place','Ebisu','Nov 14 – Jan 11','Giant chandelier',0),
 ('p06','Tokyo Dome City','Suidobashi','Nov 19 – Feb 28','5 pm – midnight',0),
 ('p07','Tokyo Skytree Town','Oshiage','Nov 5 – Dec 25','5:30 – 10 pm · market',0),
 ('p08','Meguro River','Osaki / Gotanda','Dec 4 – Jan 31','“Winter cherry blossoms”',0),
 ('p10','Tokyo Tower','Akabanebashi','All year','Sunset – midnight',0),
 ('p11','Tokyo Mega Illumination','Oi Keibajo-mae','Oct 31 – Jan 10','FINAL season',1),
 ('p12','Yomiuriland','Inagi','Oct 29 – Apr 4','Fountain show',1),
]
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:WPX;height:HPX;background:#0A1440;font-family:I;color:#fff;overflow:hidden;position:relative}}
.head{{position:relative;height:HEADH;background:url({(A/'p09.jpg').as_uri()}) center 35%/cover;padding:22px 24px 0}}
.head:after{{content:"";position:absolute;inset:0;background:linear-gradient(rgba(10,20,64,.35),rgba(10,20,64,.6) 55%,#0A1440)}}
.head>*{{position:relative;z-index:2}}
.save{{display:inline-block;background:#E5383B;color:#fff;font-weight:800;font-size:26px;padding:7px 18px;border-radius:10px;transform:rotate(-3deg)}}
h1{{font-weight:800;font-size:HSIZE;line-height:.95;letter-spacing:-2.5px;margin-top:10px;text-shadow:0 3px 0 #0A1440,0 6px 16px rgba(0,0,0,.6)}}
h1 em{{font-style:normal;color:#FFD43B;display:block}}
.pill{{display:inline-block;margin-top:10px;background:#fff;color:#0A1440;font-weight:800;font-size:24px;padding:8px 20px;border-radius:40px;border:4px solid #7FB2FF}}
.sam{{position:absolute;right:16px;bottom:-6px;height:SAMH;z-index:3;filter:drop-shadow(0 6px 10px rgba(0,0,0,.5))}}
.bub{{position:absolute;right:SAMR;top:26px;z-index:3;background:#fff;color:#0A1440;font-weight:800;font-size:22px;padding:10px 16px;border-radius:18px;border:3px solid #0A1440}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:8px 22px 0}}
.c{{background:#fff;border-radius:12px;overflow:hidden;color:#0A1440;position:relative;height:CH}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:center}}
.n{{z-index:2;position:absolute;left:7px;top:7px;width:32px;height:32px;border-radius:50%;background:#E5383B;border:3px solid #fff;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:17px}}
.b{{z-index:2;position:absolute;right:7px;top:8px;font-weight:800;font-size:16px;padding:4px 9px;border-radius:7px;background:#FFD43B;color:#0A1440}}
.b.p{{background:#E5383B;color:#fff}}
.tx{{position:absolute;left:0;right:0;bottom:0;padding:26px 9px 7px;line-height:1.12;color:#fff;background:linear-gradient(rgba(5,10,35,0),rgba(5,10,35,.82) 45%)}}
.nm{{font-weight:800;font-size:17px;letter-spacing:-.3px}}
.ar{{display:none}}
.dt{{font-weight:800;font-size:14px;color:#FFD43B;margin-top:2px}}
.ex{{font-weight:700;font-size:12px;opacity:.9}}
.cta{{background:linear-gradient(160deg,#FF3B3B,#B81F1F);color:#fff;padding:14px;display:flex;flex-direction:column;justify-content:center;gap:8px;font-weight:800;font-size:25px;line-height:1.1}}
.cta small{{font-weight:700;font-size:16px}}
.ft{{position:absolute;left:22px;right:22px;bottom:12px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:13px;color:#AFC0E6;gap:12px}}
.jp{{display:flex;align-items:center;gap:8px;color:#fff;font-weight:800;font-size:19px;white-space:nowrap}}
.jp b{{width:32px;height:32px;border-radius:50%;background:#E5383B;display:flex;align-items:center;justify-content:center;font-size:14px}}
'''
def page(Wd,Hd,v):
    cards=''.join(f'<div class=c><div class=ph style="background-image:url({(A/(p+".jpg")).as_uri()})"></div><span class=n>{i+1}</span><span class="b{" p" if paid else ""}">{"PAID" if paid else "FREE"}</span><div class=tx><div class=nm>{nm}</div><div class=ar>{ar}</div><div class=dt>{dt}</div><div class=ex>{ex}</div></div></div>' for i,(p,nm,ar,dt,ex,paid) in enumerate(SPOTS))
    cards+='<div class="c cta">💬 Comment JAPAN<small>Get my free 1-page Japan guide in your DMs</small></div>'
    css=CSS
    for k,val in v.items(): css=css.replace(k,val)
    css=css.replace('WPX',f'{Wd}px').replace('HPX',f'{Hd}px')
    return f'''<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body>
<div class=head><div class=save>📌 SAVE THIS</div><h1>Tokyo Winter<em>Illuminations 2026–27</em></h1><div class=pill>11 spots · 9 free · dates & hours</div>
<div class=bub>Go after dark!</div><img class=sam src="{SAM}"></div>
<div class=grid>{cards}</div>
<div class=ft><span>Checked on official sites, Oct 25, 2026. Dates & hours may change. Illustrations are for reference.</span><span class=jp><b>JP</b>Japan Like a Local</span></div></body></html>'''
tmp=R/'tools/_il.html'
with sync_playwright() as pw:
    b=pw.chromium.launch()
    for name,Wd,Hd,v in [('ig-tokyo-illuminations',1080,1350,{'HEADH':'292px','HSIZE':'66px','SAMH':'230px','SAMR':'200px','CH':'236px','PH':'124px'}),
                         ('pin-tokyo-illuminations',1000,1500,{'HEADH':'318px','HSIZE':'64px','SAMH':'240px','SAMR':'200px','CH':'266px','PH':'146px'})]:
        pg=b.new_page(viewport={'width':Wd,'height':Hd}); tmp.write_text(page(Wd,Hd,v)); pg.goto(tmp.as_uri()); pg.wait_for_timeout(700)
        gap=pg.evaluate("document.querySelector('.ft').getBoundingClientRect().top-Math.max(...[...document.querySelectorAll('.c')].map(e=>e.getBoundingClientRect().bottom))")
        over=pg.evaluate("[...document.querySelectorAll('.tx')].filter(e=>e.scrollHeight>e.parentElement.clientHeight-e.offsetTop+1).length")
        print(name,'gap',round(gap),'overflow',over); pg.screenshot(path=str(R/f'assets/{name}.png'))
    b.close()
tmp.unlink()
