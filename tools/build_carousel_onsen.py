# Carousel test (10/30): "Onsen in 5 steps" — 7 slides 1080x1350. Facts from paid guide v2 p.11.
import pathlib
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; F=(R/'tools/fonts').as_uri()
BG=(R/'assets/covers/px-8606805.jpg').as_uri()
OUT=R/'assets/carousel-onsen'; OUT.mkdir(exist_ok=True)
C='#D62828'
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:I;position:relative;overflow:hidden;background:#FFF8EC;color:#141B2D}}
.ph{{position:absolute;inset:0;background:url({BG}) center/cover}}
.ph:after{{content:"";position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.05) 30%,rgba(0,0,0,.72))}}
.cov{{position:absolute;left:70px;right:70px;bottom:120px;color:#fff;z-index:2}}
.tag{{display:inline-block;background:#FFD43B;color:#141B2D;font-weight:800;font-size:38px;padding:10px 22px;border-radius:12px}}
.cov h1{{font-size:116px;line-height:.98;letter-spacing:-3px;margin-top:22px;text-shadow:0 4px 20px rgba(0,0,0,.5)}}
.cov p{{font-weight:700;font-size:44px;margin-top:22px}}
.swipe{{position:absolute;right:60px;bottom:50px;z-index:2;color:#fff;font-weight:800;font-size:34px}}
.top{{height:300px;background:url({BG}) center 45%/cover;position:relative}}
.top:after{{content:"";position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,0),rgba(0,0,0,.35))}}
.n{{position:absolute;left:70px;top:230px;width:150px;height:150px;border-radius:50%;background:{C};color:#fff;font-weight:800;font-size:84px;display:flex;align-items:center;justify-content:center;border:8px solid #FFF8EC;z-index:2}}
.body{{padding:120px 70px 0}}
.body h2{{font-size:98px;line-height:1.02;letter-spacing:-2px}}
.body p{{font-weight:700;font-size:54px;line-height:1.3;color:#3F4450;margin-top:34px}}
.tip{{margin-top:44px;background:#fff;border-left:14px solid {C};border-radius:18px;padding:34px 38px;font-weight:700;font-size:48px;line-height:1.3}}
.tip b{{color:{C}}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:96px;background:#141B2D;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 60px;font-weight:800;font-size:30px}}
.foot span:last-child{{color:#FFD43B}}
.end{{padding:150px 70px 0;text-align:center}}
.end h2{{font-size:92px;line-height:1.05;letter-spacing:-2px}}
.end p{{font-weight:700;font-size:50px;line-height:1.35;color:#3F4450;margin-top:34px}}
.btn{{display:inline-block;margin-top:56px;background:{C};color:#fff;font-weight:800;font-size:52px;padding:34px 48px;border-radius:28px}}
.small{{font-weight:700;font-size:32px;color:#6B7080;margin-top:44px}}
'''
FOOT=lambda i:f'<div class=foot><span>JAPAN LIKE A LOCAL</span><span>{i}/7 →</span></div>'
STEPS=[('Change in the changing room','In most traditional baths you bathe without a swimsuit, in baths separated by gender.','<b>Tip:</b> avoid bathing right after drinking alcohol, and drink water.'),
 ('Wash before you soak','Wash and rinse your whole body at the shower stations before you get in.','<b>Tip:</b> rinse off all the soap and shampoo first.'),
 ('Towel stays out of the water','Many people fold the small towel on their head or leave it beside the bath.','<b>Tip:</b> never wring it out into the bath.'),
 ('Tie up long hair','Hair should not touch the water. Keep your voice low too.','<b>Tip:</b> dry off a little before going back to the changing room.'),
 ('Tattoos? Ask first','Policies vary a lot. Some refuse, some allow a cover sticker, some are tattoo-friendly.','<b>Ask:</b> "Tattoo wa daijoubu desu ka?" (Are tattoos okay?)')]
SL=[f'<div class=ph></div><div class=cov><div class=tag>FIRST ONSEN?</div><h1>Onsen in<br>5 steps</h1><p>No awkward moments. Save this 📌</p></div><div class=swipe>Swipe →</div>']
SL+=[f'<div class=top></div><div class=n>{i+1}</div><div class=body><h2>{h}</h2><p>{p}</p><div class=tip>{t}</div></div>'+FOOT(i+2) for i,(h,p,t) in enumerate(STEPS)]
SL+=['<div class=end><h2>Rules vary by facility.<br>Check signs or ask staff.</h2><p>Want onsen, toilets, taxis, tax-free and more on one page?</p><div class=btn>💬 Comment JAPAN</div><p class=small>I’ll DM you my free 1-page Japan Quick Start.</p></div>'+FOOT(7)]
tmp=R/'tools/_car.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,body in enumerate(SL,1):
        tmp.write_text(f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>')
        pg.goto(tmp.as_uri()); pg.wait_for_timeout(400); pg.screenshot(path=str(OUT/f'onsen-{i}.jpg'),type='jpeg',quality=92)
    b.close()
tmp.unlink(); print('ok',len(SL))
