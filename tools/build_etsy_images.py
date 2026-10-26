# Etsy listing images (3000x2250, 4:3) from the paid guide v2 pages.
import pathlib
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; P=R/'assets/etsy/pages'; F=(R/'tools/fonts').as_uri()
def pg(n): return (P/f'p-{n:02d}.png').as_uri()
BG=(R/'assets/covers/px-31409473-safe.jpg').as_uri()
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:3000px;height:2250px;font-family:I;position:relative;overflow:hidden;background:#F6F1EA;color:#141B2D}}
.pg{{position:absolute;background:#fff;box-shadow:0 30px 70px rgba(0,0,0,.28);border-radius:10px}}
.tag{{display:inline-block;background:#D62828;color:#fff;font-weight:800;font-size:64px;padding:16px 36px;border-radius:16px}}
h1{{font-weight:800;font-size:170px;line-height:.98;letter-spacing:-5px}}
h1 em{{font-style:normal;color:#D62828}}
.sub{{font-weight:700;font-size:72px;line-height:1.25;color:#3F4450;margin-top:40px}}
.chips{{display:flex;flex-wrap:wrap;gap:26px;margin-top:60px}}
.chip{{background:#fff;border:6px solid #141B2D;border-radius:60px;font-weight:800;font-size:58px;padding:18px 40px}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:150px;background:#141B2D;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 120px;font-weight:800;font-size:56px}}
.foot b{{color:#FFD43B}}
'''
FOOT='<div class=foot><span>JAPAN LIKE A LOCAL</span><span><b>Instant PDF download</b> · phone, tablet or print</span></div>'
IMGS={
'1-hero':f'''<div style="position:absolute;inset:0;background:url({BG}) center/cover;filter:brightness(.9)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(246,241,234,.97) 46%,rgba(246,241,234,.2))"></div>
<div style="position:absolute;left:130px;top:190px;width:1500px"><div class=tag>UPDATED NOVEMBER 2026</div>
<h1 style="margin-top:50px">Japan Travel<br>Guide for<br><em>First-Time</em><br>Visitors</h1>
<div class=sub>21-page printable PDF</div>
<div class=chips><span class=chip>New tax-free rules</span><span class=chip>Onsen · Toilets · Taxis</span><span class=chip>Cheat sheet</span></div></div>
<img class=pg src="{pg(5)}" style="left:1880px;top:330px;width:880px;transform:rotate(7deg)">
<img class=pg src="{pg(3)}" style="left:1700px;top:300px;width:880px;transform:rotate(-2deg)">
<img class=pg src="{pg(1)}" style="left:1560px;top:250px;width:900px;transform:rotate(-8deg)">'''+FOOT,
'2-inside':f'''<div style="position:absolute;left:130px;top:170px;width:1250px"><div class=tag>WHAT'S INSIDE</div>
<h1 style="margin-top:50px;font-size:150px">21 pages,<br>everything a<br><em>first-timer</em><br>needs</h1>
<div class=sub style="font-size:62px">Money · trains · restaurants · konbini · manners · 8 phrases · first 24 hours · emergency numbers</div></div>
<img class=pg src="{pg(2)}" style="left:1530px;top:150px;width:1300px">'''+FOOT,
'3-taxfree':f'''<div style="position:absolute;left:130px;top:170px;width:1150px"><div class=tag>NEW FROM NOV 1, 2026</div>
<h1 style="margin-top:50px;font-size:150px">Japan's<br><em>new tax-free</em><br>rules, step<br>by step</h1>
<div class=sub style="font-size:62px">What changed, the airport check, and the mistakes that cost your refund.</div></div>
<img class=pg src="{pg(5)}" style="left:1380px;top:200px;width:780px;transform:rotate(-3deg)">
<img class=pg src="{pg(6)}" style="left:2130px;top:220px;width:780px;transform:rotate(3deg)">'''+FOOT,
'4-situations':f'''<div style="position:absolute;left:120px;top:120px"><div class=tag>SITUATION GUIDES</div>
<h1 style="margin-top:36px;font-size:120px">Know what to do <em>before</em> you get there</h1></div>
'''+''.join(f'<img class=pg src="{pg(n)}" style="left:{110+i*705}px;top:430px;width:670px"><div class=chip style="position:absolute;left:{110+i*705}px;top:1430px;width:670px;text-align:center">{t}</div>' for i,(n,t) in enumerate([(11,'Onsen'),(12,'Toilets'),(13,'Taxis & luggage'),(14,'Shrines & temples')]))+'<div class=sub style="position:absolute;left:120px;top:1640px;font-size:66px">Plus vending machines, escalators, restaurants, konbini and trains.</div>'+FOOT,
'5-cheatsheet':f'''<div style="position:absolute;left:130px;top:170px;width:1250px"><div class=tag>SAVE IT ON YOUR PHONE</div>
<h1 style="margin-top:50px;font-size:150px">One-page<br><em>cheat sheet</em><br>+ phrases that<br>actually help</h1>
<div class=sub style="font-size:62px">Screenshot it, or print it and keep it in your bag.</div></div>
<img class=pg src="{pg(16)}" style="left:1430px;top:220px;width:740px;transform:rotate(-3deg)">
<img class=pg src="{pg(20)}" style="left:2130px;top:200px;width:740px;transform:rotate(3deg)">'''+FOOT,
}
out=R/'assets/etsy'; tmp=R/'tools/_etsy.html'
with sync_playwright() as p:
    b=p.chromium.launch(); page=b.new_page(viewport={'width':3000,'height':2250})
    for k,body in IMGS.items():
        tmp.write_text(f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>')
        page.goto(tmp.as_uri()); page.wait_for_timeout(700); page.screenshot(path=str(out/f'etsy-{k}.jpg'),type='jpeg',quality=90); print(k)
    b.close()
tmp.unlink()
