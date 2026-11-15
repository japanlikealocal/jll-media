# Gumroad/Etsy preview images for the Tokyo Food Map (1280x1280), from real PDF pages.
# Copy based on buyer reviews of similar guides (docs/food-guide-market-perplexity-2026-11-14.md).
import pathlib, base64, subprocess
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; T=R/'tools/_tmp'; F=(R/'tools/fonts').as_uri()
PDF=R/'products/tokyo-food-map-v1-2026-11.pdf'
def page(n,dpi=150):
    subprocess.run(['pdftoppm','-r',str(dpi),'-png','-f',str(n),'-l',str(n),'-singlefile',str(PDF),str(T/f'pg{n}')],check=True,stderr=subprocess.DEVNULL)
    return T/f'pg{n}.png'
def b64(p): return 'data:image/png;base64,'+base64.b64encode(pathlib.Path(p).read_bytes()).decode()
cover=b64(page(1,80)); p3=b64(page(3,80)); p6=b64(page(6,80)); p21=b64(page(21,80))
card=b64(T/'card.png'); near=b64(T/'near.png'); phr=b64(T/'phr.png')
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}@font-face{{font-family:I;src:url({F}/Inter-Regular.ttf);font-weight:400}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1280px;height:1280px;background:#FFF8EC;font-family:I,'Noto Sans CJK JP','Noto Color Emoji',sans-serif;color:#1c1917;position:relative;overflow:hidden}}
.top{{background:#1c1917;color:#fff;padding:54px 64px 46px}}.kick{{color:#FFB547;font-weight:800;font-size:26px;letter-spacing:3px}}h1{{font-weight:800;font-size:66px;line-height:1.05;margin-top:12px}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:86px;background:#c2410c;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 64px;font-weight:800;font-size:28px}}
.shot{{border-radius:14px;box-shadow:0 10px 30px rgba(0,0,0,.18);border:1px solid #e7dfd2;background:#fff}}'''
P={}
P['1-whats-inside']=f'''<div class=top><div class=kick>TOKYO FOOD MAP · PDF</div><h1>Skip the research.<br>Eat where locals eat.</h1></div>
<div style="display:flex;gap:40px;padding:50px 64px">
<div style="flex:1;display:flex;flex-direction:column;gap:34px;font-size:34px;line-height:1.25">
<div>🍜 <b>48 food spots</b><br><span style="color:#57534e;font-size:26px">gyoza · ramen · unagi · yakitori</span></div>
<div>🚉 <b>Sorted by area</b><br><span style="color:#57534e;font-size:26px">pick a place near where you're sightseeing</span></div>
<div>🗣️ <b>Japanese names</b><br><span style="color:#57534e;font-size:26px">point at the screen — staff can read it</span></div>
<div>💳 <b>Cash or card? Booking?</b><br><span style="color:#57534e;font-size:26px">checked against shop pages & listings, Oct–Nov 2026</span></div>
<div>📍 <b>Google Maps link</b> for every spot</div></div>
<div style="width:470px;position:relative"><img class=shot src="{cover}" style="width:390px;position:absolute;left:-20px;top:0;transform:rotate(-4deg)"><img class=shot src="{p6}" style="width:330px;position:absolute;right:-30px;top:380px;transform:rotate(4deg)"></div></div>
<div class=foot><span>21-page PDF · instant download</span><span>Japan Like a Local</span></div>'''
P['2-every-spot']=f'''<div class=top><div class=kick>WHAT EACH SPOT LOOKS LIKE</div><h1>Everything you need<br>before you walk in.</h1></div>
<div style="padding:60px 64px 0"><img class=shot src="{card}" style="width:100%"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px 40px;padding:44px 80px;font-size:28px;font-weight:700">
<div>✅ Japanese name to show staff</div><div>✅ Nearest station + walk time</div><div>✅ Cash only or cards OK</div><div>✅ Can you book? English menu?</div><div>✅ Price where officially listed</div><div>✅ Local tip (table charge etc.)</div></div>
<div class=foot><span>48 spots like this · real page from the guide</span><span>Japan Like a Local</span></div>'''
P['3-find-near-you']=f'''<div class=top><div class=kick>PLAN BY NEIGHBORHOOD</div><h1>Hungry in Shinjuku?<br>Asakusa? Ginza?</h1></div>
<div style="display:flex;gap:36px;padding:56px 64px 0;align-items:flex-start">
<div style="flex:1.25"><img class=shot src="{near}" style="width:100%"><div style="font-size:24px;color:#57534e;margin-top:14px;font-weight:700">Every spot sorted by area and station</div></div>
<div style="flex:1"><img class=shot src="{phr}" style="width:100%"><div style="font-size:24px;color:#57534e;margin-top:14px;font-weight:700">Point-and-say phrases for ordering & paying</div></div></div>
<div class=foot><span>Save hours of planning · use it on your phone</span><span>Japan Like a Local</span></div>'''
out=R/'assets/foodmap-previews'; out.mkdir(exist_ok=True)
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':1280})
    for k,v in P.items():
        pg.set_content(f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{v}</body></html>',wait_until='load'); pg.wait_for_timeout(500)
        pg.screenshot(path=str(out/f'{k}.png')); print('ok',k)
    b.close()
