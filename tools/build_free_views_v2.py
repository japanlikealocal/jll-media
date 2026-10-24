# v2: closer to the "flyer" feel Zero liked — skyline photo header, huge 3D headline, vivid photos, big FREE bursts.
import pathlib
from PIL import Image, ImageFilter, ImageEnhance
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; A=R/'assets/freeviews'; F=(R/'tools/fonts').as_uri()
def vivid(src,out,blur=0,crop=None):
    im=Image.open(A/src).convert('RGB')
    if crop: w,h=im.size; im=im.crop((int(w*crop[0]),int(h*crop[1]),int(w*crop[2]),int(h*crop[3])))
    if blur: im=im.filter(ImageFilter.GaussianBlur(blur))
    im=ImageEnhance.Color(im).enhance(1.45); im=ImageEnhance.Contrast(im).enhance(1.15); im=ImageEnhance.Brightness(im).enhance(1.08)
    im.save(A/out,quality=92); return out
SPOTS=[
 (vivid('px-31558042.jpg','v-tmg.jpg',crop=(0,.15,.7,1)),'center 55%','Tokyo Metropolitan Gov’t','45F · 202 m','Night views till 10 pm'),
 (vivid('px-6659300.jpg','v-bridge.jpg',crop=(.38,0,1,1)),'center center','Caretta Shiodome','46F · ~200 m','Tokyo Bay night view'),
 (vivid('px-4410426.jpg','v-tower.jpg'),'center 60%','Yebisu Garden Place','38F · ~160 m','Tokyo Tower view'),
 (vivid('px-31268104.jpg','v-station.jpg'),'center 55%','KITTE Garden','6F rooftop','Tokyo Station below'),
 (vivid('px-28486324.jpg','v-ginza.jpg',blur=3),'center 40%','GINZA SIX Rooftop','Rooftop garden','Open 7 am – 11 pm'),
 (vivid('px-20060367.jpg','v-haneda.jpg'),'center 55%','Haneda T1 & T2','Observation decks','Planes up close'),
 (vivid('px-30978801.jpg','v-nakano.jpg'),'center 72%','Nakano City Hall','11F rooftop garden','Weekdays only'),
]
HEAD=(A/vivid('px-29502545.jpg','v-head.jpg')).as_uri()
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:WPX;height:HPX;background:#081233;font-family:I;color:#fff;overflow:hidden;position:relative}}
.head{{position:relative;height:HEADH;background:url({HEAD}) center 40%/cover;text-align:center;padding-top:26px}}
.head:after{{content:"";position:absolute;inset:0;background:linear-gradient(rgba(8,18,51,.25),rgba(8,18,51,.55) 60%,#081233)}}
.head>*{{position:relative;z-index:2}}
.k{{display:inline-block;background:#FFD43B;color:#081233;font-weight:800;font-size:30px;padding:8px 22px;border-radius:10px;transform:rotate(-2deg);box-shadow:0 4px 0 #B8860B}}
h1{{font-weight:800;font-size:HSIZE;line-height:.95;letter-spacing:-3px;margin-top:12px;color:#fff;
 text-shadow:0 3px 0 #081233,0 6px 0 #081233,3px 3px 0 #081233,-3px 3px 0 #081233,0 10px 18px rgba(0,0,0,.6)}}
h1 .y{{color:#FF2D2D;-webkit-text-stroke:3px #fff;font-size:1.25em}}
h1 .g{{color:#FFD43B}}
.pill{{display:inline-block;margin-top:12px;background:#fff;color:#081233;font-weight:800;font-size:27px;padding:9px 24px;border-radius:40px;border:4px solid #1F6FEB}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:6px 26px 0}}
.c{{background:#fff;border-radius:14px;overflow:hidden;color:#081233;position:relative;height:CH;border:3px solid #fff}}
.ph{{height:PH;background-size:cover;position:relative}}
.nm{{position:absolute;left:0;right:0;top:0;padding:7px 9px 18px;background:linear-gradient(rgba(0,0,0,.8),rgba(0,0,0,0));color:#fff;font-weight:800;font-size:23px;line-height:1.05;display:flex;gap:7px;align-items:flex-start}}
.n{{flex:0 0 34px;height:34px;border-radius:50%;background:#E5383B;border:3px solid #fff;display:flex;align-items:center;justify-content:center;font-size:19px}}
.fr{{position:absolute;right:4px;bottom:-34px;width:118px;height:118px;background:#FFD43B;color:#E5383B;font-weight:800;font-size:31px;letter-spacing:-1px;display:flex;align-items:center;justify-content:center;transform:rotate(-10deg);
 clip-path:polygon(50% 0,61% 13%,77% 7%,80% 24%,96% 28%,90% 44%,100% 57%,86% 67%,88% 84%,71% 84%,61% 98%,50% 88%,37% 98%,28% 84%,11% 84%,13% 67%,0 57%,10% 44%,4% 28%,20% 24%,23% 7%,39% 13%);filter:drop-shadow(0 3px 0 #B8860B)}}
.tx{{padding:10px 11px 0;font-weight:700;font-size:20px;line-height:1.25;padding-right:96px}}
.tx b{{display:block;font-weight:800;font-size:22px;color:#1F57B8}}
.tip,.cta{{padding:16px 14px;display:flex;flex-direction:column;justify-content:center;font-weight:800;font-size:28px;line-height:1.15;gap:10px;color:#fff}}
.tip{{background:linear-gradient(160deg,#1F6FEB,#0B3FA8)}} .cta{{background:linear-gradient(160deg,#FF3B3B,#B81F1F)}}
.tip small,.cta small{{font-weight:700;font-size:19px;opacity:.95}}
.big{{font-size:44px;line-height:1}}
.ft{{position:absolute;left:26px;right:26px;bottom:14px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:15px;color:#AFC0E6}}
.jp{{display:flex;align-items:center;gap:9px;color:#fff;font-weight:800;font-size:21px;white-space:nowrap}}
.jp b{{width:36px;height:36px;border-radius:50%;background:#E5383B;display:flex;align-items:center;justify-content:center;font-size:15px}}
'''
def page(Wd,Hd,hsize,headh,ch,ph):
    cards=''.join(f'<div class=c><div class=ph style="background-image:url({(A/f).as_uri()});background-position:{pos}"><div class=nm><span class=n>{i+1}</span>{n}</div><div class=fr>FREE</div></div><div class=tx><b>{a}</b>{b}</div></div>' for i,(f,pos,n,a,b) in enumerate(SPOTS))
    cards+='<div class="c tip"><span class=big>¥0</span>No ticket.<br>No booking.<small>May close for bad weather or events.</small></div>'
    cards+='<div class="c cta"><span class=big>💬</span>Comment JAPAN<small>Get my free 1-page Japan guide in your DMs</small></div>'
    css=CSS.replace('WPX',f'{Wd}px').replace('HPX',f'{Hd}px').replace('HSIZE',hsize).replace('HEADH',headh).replace('CH',ch).replace('PH',ph)
    return f'''<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body>
<div class=head><div class=k>WHY PAY ¥2,000 FOR A VIEW?</div><h1><span class=y>FREE</span> Tokyo views<br><span class=g>you can just walk into</span></h1><div class=pill>7 spots · night views · Tokyo Tower · planes</div></div>
<div class=grid>{cards}</div>
<div class=ft><span>Checked on official sites, Oct 2026. Hours change, check before you go. Photos are illustrative.</span><span class=jp><b>JP</b>Japan Like a Local</span></div></body></html>'''
tmp=R/'tools/_fv2.html'
with sync_playwright() as pw:
    b=pw.chromium.launch()
    for name,Wd,Hd,hs,hh,ch,ph in [('ig-free-tokyo-views-v2',1080,1350,'68px','330px','300px','196px'),('pin-free-tokyo-views-v2',1000,1500,'70px','360px','344px','232px')]:
        pg=b.new_page(viewport={'width':Wd,'height':Hd}); tmp.write_text(page(Wd,Hd,hs,hh,ch,ph)); pg.goto(tmp.as_uri()); pg.wait_for_timeout(700)
        gap=pg.evaluate("document.querySelector('.ft').getBoundingClientRect().top-Math.max(...[...document.querySelectorAll('.c')].map(e=>e.getBoundingClientRect().bottom))")
        print(name,'gap',round(gap)); pg.screenshot(path=str(R/f'assets/{name}.png'))
    b.close()
tmp.unlink()
