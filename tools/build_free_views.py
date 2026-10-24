# "Skip the ¥2,000 observation deck: 7 FREE Tokyo views" grid (IG 1080x1350 + pin 1000x1500).
# Facts: Perplexity check of official sites, 2026-10-25 (see docs/free-views-sources.md). Photos: Pexels.
import pathlib
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; A=R/'assets/freeviews'; F=(R/'tools/fonts').as_uri()
# soften shop signs in the Ginza photo
g=Image.open(A/'px-28486324.jpg'); g.filter(ImageFilter.GaussianBlur(5)).save(A/'ginza-soft.jpg')
c=Image.open(A/'px-6659300.jpg'); w,h=c.size; c.crop((int(w*0.35),0,w,h)).save(A/'bridge-crop.jpg')
SPOTS=[
 ('px-29502545.jpg','center 60%','Tokyo Metropolitan Gov’t','45F · 202 m · Shinjuku','South deck till 10 pm'),
 ('bridge-crop.jpg','center center','Caretta Shiodome','46F · ~200 m','Tokyo Bay & Rainbow Bridge'),
 ('px-31558042.jpg','center 60%','Yebisu Garden Place','38F · ~160 m','Tokyo Tower view'),
 ('px-31268104.jpg','center 55%','KITTE Garden','6F rooftop','Tokyo Station up close'),
 ('ginza-soft.jpg','center 40%','GINZA SIX Rooftop','Rooftop garden','Open 7 am – 11 pm'),
 ('px-20060367.jpg','center 55%','Haneda T1 & T2 Decks','Planes up close','6:30 am – 10 pm'),
 ('px-30978801.jpg','center 70%','Nakano City Hall','11F rooftop garden','Weekdays only'),
]
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:WPX;height:HPX;background:#0B1736;font-family:I;color:#fff;overflow:hidden;position:relative}}
.top{{padding:34px 34px 0;text-align:center}}
.k{{display:inline-block;background:#FFD43B;color:#0B1736;font-weight:800;font-size:30px;padding:8px 20px;border-radius:10px;transform:rotate(-2deg)}}
h1{{font-weight:800;font-size:HSIZE;line-height:.98;letter-spacing:-2px;margin-top:14px;text-shadow:0 4px 0 #000}}
h1 em{{font-style:normal;color:#FF3B3B;-webkit-text-stroke:2px #fff}}
.pill{{display:inline-block;margin-top:14px;background:#fff;color:#0B1736;font-weight:800;font-size:28px;padding:10px 26px;border-radius:40px;border:4px solid #1F6FEB}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:22px 30px 0}}
.c{{background:#fff;border-radius:16px;overflow:hidden;color:#0B1736;position:relative;height:CH}}
.ph{{height:PH;background-size:cover;position:relative}}
.nm{{position:absolute;left:0;right:0;top:0;padding:8px 10px;background:linear-gradient(rgba(0,0,0,.75),rgba(0,0,0,0));color:#fff;font-weight:800;font-size:24px;line-height:1.05;display:flex;gap:8px;align-items:flex-start}}
.n{{flex:0 0 34px;height:34px;border-radius:50%;background:#E5383B;border:3px solid #fff;display:flex;align-items:center;justify-content:center;font-size:19px}}
.fr{{position:absolute;right:8px;bottom:-26px;width:92px;height:92px;background:#FFD43B;color:#E5383B;font-weight:800;font-size:26px;display:flex;align-items:center;justify-content:center;transform:rotate(-10deg);
 clip-path:polygon(50% 0,61% 13%,77% 7%,80% 24%,96% 28%,90% 44%,100% 57%,86% 67%,88% 84%,71% 84%,61% 98%,50% 88%,37% 98%,28% 84%,11% 84%,13% 67%,0 57%,10% 44%,4% 28%,20% 24%,23% 7%,39% 13%)}}
.tx{{padding:12px 12px 0;font-weight:700;font-size:21px;line-height:1.25}}
.tx b{{display:block;font-weight:800;font-size:22px}}
.tip{{background:#1F6FEB;color:#fff;padding:18px 16px;display:flex;flex-direction:column;justify-content:center;font-weight:800;font-size:27px;line-height:1.2;gap:10px}}
.tip small{{font-weight:700;font-size:20px;opacity:.9}}
.cta{{background:#E5383B;color:#fff;padding:18px 16px;display:flex;flex-direction:column;justify-content:center;font-weight:800;font-size:27px;line-height:1.15;gap:10px}}
.cta small{{font-weight:700;font-size:20px}}
.ft{{position:absolute;left:30px;right:30px;bottom:18px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:16px;color:#B9C3DA}}
.jp{{display:flex;align-items:center;gap:10px;color:#fff;font-weight:800;font-size:22px}}
.jp b{{width:38px;height:38px;border-radius:50%;background:#E5383B;display:flex;align-items:center;justify-content:center;font-size:16px}}
'''
def page(Wd,Hd,hsize,ch,ph):
    cards=''.join(f'<div class=c><div class=ph style="background-image:url({(A/f).as_uri()});background-position:{pos}"><div class=nm><span class=n>{i+1}</span>{n}</div><div class=fr>FREE</div></div><div class=tx><b>{a}</b>{b}</div></div>' for i,(f,pos,n,a,b) in enumerate(SPOTS))
    cards+='<div class="c tip">No ticket.<br>No booking.<small>May close for bad weather or events.</small></div>'
    cards+='<div class="c cta">Comment JAPAN<small>for my free 1-page Japan guide in your DMs</small></div>'
    css=CSS.replace('WPX',f'{Wd}px').replace('HPX',f'{Hd}px').replace('HSIZE',hsize).replace('CH',ch).replace('PH',ph)
    return f'''<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body>
<div class=top><div class=k>SKIP THE ¥2,000 OBSERVATION DECK</div><h1><em>FREE</em> Tokyo views<br>you can just walk into</h1><div class=pill>7 spots · night views · Tokyo Tower · planes</div></div>
<div class=grid>{cards}</div>
<div class=ft><span>Checked on official sites, Oct 2026. Hours change, check before you go. Photos are illustrative.</span><span class=jp><b>JP</b>Japan Like a Local</span></div></body></html>'''
tmp=R/'tools/_fv.html'
with sync_playwright() as pw:
    b=pw.chromium.launch()
    for name,Wd,Hd,hs,ch,ph in [('ig-free-tokyo-views',1080,1350,'70px','300px','196px'),('pin-free-tokyo-views',1000,1500,'72px','350px','236px')]:
        pg=b.new_page(viewport={'width':Wd,'height':Hd}); tmp.write_text(page(Wd,Hd,hs,ch,ph)); pg.goto(tmp.as_uri()); pg.wait_for_timeout(600)
        gap=pg.evaluate("document.querySelector('.ft').getBoundingClientRect().top-Math.max(...[...document.querySelectorAll('.c')].map(e=>e.getBoundingClientRect().bottom))")
        print(name,'gap',round(gap)); pg.screenshot(path=str(R/f'assets/{name}.png'))
    b.close()
tmp.unlink()
