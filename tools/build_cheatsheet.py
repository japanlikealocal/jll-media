# "Save this" infographic (Instagram feed 4:5 / Pinterest). Facts only from paid guide v2 (official sources checked 10/20).
import pathlib
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent
F=(R/'tools/fonts').as_uri()
SECTIONS=[
 ('MONEY','#E8A317','💴','px-3907161.jpg','center 40%',[('Carry some cash','Yen as backup. Small shops may be cash only.'),('Get an IC card','Suica / PASMO / ICOCA for trains & konbini.'),('No tipping','Pay the amount shown.'),('Tax-free from Nov 1','Pay full price. Refund after customs check.')]),
 ('TRAINS','#2F6FD6','🚃','px-29058311-shinkansen.jpg','30% 60%',[('Tap in, tap out','Touch your IC card at both gates.'),('Let people off first','Line up where marked.'),('No phone calls','Keep your voice low on local trains.'),('Big suitcase?','Tokaido/Sanyo Shinkansen: over 160 cm needs a reserved seat with space.')]),
 ('MANNERS','#D62828','🙇','px-31193736.jpg','center 55%',[('Shoes off','Look for a raised entrance or slippers.'),('Carry your trash','Public bins are rare.'),('Escalators','Usually Tokyo: stand left. Osaka: right.'),('At a shrine','Most: bow 2, clap 2, bow 1. Temples: no clap.')]),
 ('FOOD & KONBINI','#1E9E6A','🍜','px-12984979.jpg','center 45%',[('Ticket machine','Some ramen shops: buy a ticket first.'),('Free water','Water & oshibori are often free.'),('Konbini','Meals, ATMs, many take cards & IC.'),('Pay at the register','At many restaurants.')]),
 ('ONSEN & TOILETS','#7A4FD1','♨️','px-8606805.jpg','center 55%',[('Wash first','Then get in. Towel stays out of the water.'),('Tattoos?','Rules vary. Ask before you go.'),('Toilet paper','Goes in the toilet. Other items in the bin.'),('Flush','流す = flush. 大 big · 小 small.')]),
]
def card(n,t,d,c): return f'<div class=it><b style="background:{c}">{n:02d}</b><div><h3>{t}</h3><p>{d}</p></div></div>'
blocks='';n=1
for name,col,emo,img,pos,items in SECTIONS:
    cards=''.join(card(n+i,t,d,col) for i,(t,d) in enumerate(items)); n+=len(items)
    url=(R/'assets/covers'/img).as_uri()
    blocks+=f'<section style="--c:{col}"><h2 style="background-image:linear-gradient(90deg,{col}f0 0%,{col}b0 26%,rgba(0,0,0,0) 52%),url({url});background-position:center,{pos};background-size:cover"><span>{emo}</span>{name}</h2>{cards}</section>'
html=f'''<!doctype html><html><head><meta charset=utf-8><style>
@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
@font-face{{font-family:I;src:url({F}/Inter-Regular.ttf);font-weight:400}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#FFF8EC;font-family:I,'Noto Color Emoji','IPAGothic',sans-serif;color:#141B2D;position:relative;overflow:hidden}}
.top{{background:#141B2D;color:#fff;padding:24px 44px 18px;position:relative}}
.save{{position:absolute;right:40px;top:30px;background:#FFD43B;color:#141B2D;font-weight:800;font-size:28px;padding:10px 20px;border-radius:12px;transform:rotate(4deg)}}
.k{{color:#FF8A80;font-weight:800;font-size:26px;letter-spacing:2px}}
h1{{font-weight:800;font-size:62px;line-height:1.02;letter-spacing:-1.5px;margin-top:6px}}
h1 em{{font-style:normal;color:#FFD43B}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:14px 28px 0}}
section{{background:#fff;border-radius:18px;border:3px solid var(--c);padding:0 14px 4px;box-shadow:0 4px 0 var(--c);overflow:hidden}}
section:last-child{{grid-column:1/3;display:grid;grid-template-columns:1fr 1fr;column-gap:18px}}
section:last-child h2{{grid-column:1/3}}
h2{{font-weight:800;font-size:27px;color:#fff;display:flex;align-items:center;gap:8px;margin:0 -14px 4px;padding:0 16px;height:96px;letter-spacing:.5px;text-shadow:0 2px 8px rgba(0,0,0,.35)}}
h2 span{{font-size:30px}}
.it{{display:flex;gap:10px;align-items:flex-start;padding:4px 0;border-top:1.5px dashed #E7DFD2}}
section h2+.it{{border-top:none}}
.it b{{flex:0 0 38px;height:38px;border-radius:50%;color:#fff;font-weight:800;font-size:19px;display:flex;align-items:center;justify-content:center;margin-top:2px}}
h3{{font-weight:800;font-size:22px;line-height:1.1}}
p{{font-weight:400;font-size:18px;line-height:1.18;color:#3D4250;margin-top:2px}}
.sos{{margin:12px 28px 0;background:#D62828;color:#fff;border-radius:16px;padding:12px 20px;display:flex;justify-content:space-between;align-items:center;font-weight:800;font-size:25px}}
.sos small{{font-weight:700;font-size:19px;opacity:.9}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:78px;background:#141B2D;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 32px;font-weight:800;font-size:24px}}
.foot i{{font-style:normal;color:#FFD43B}}
.jp{{display:flex;align-items:center;gap:12px}}
.jp b{{width:46px;height:46px;border-radius:50%;background:#D62828;display:flex;align-items:center;justify-content:center;font-size:18px}}
.note{{position:absolute;left:28px;right:28px;bottom:86px;font-size:15px;color:#6B6F78}}
</style></head><body>
<div class=top><div class=save>📌 SAVE THIS</div><div class=k>FIRST TRIP TO JAPAN?</div><h1>20 things to know<br><em>before you land</em></h1></div>
<div class=grid>{blocks}</div>
<div class=sos><span>🆘 Police 110 · Fire/Ambulance 119</span><small>JNTO Visitor Hotline 24/7: 050-3816-2787</small></div>
<div class=note>Rules vary by place. Follow local signs and staff instructions. Checked with official sources (JNTO, Japan Tourism Agency, JR), Oct 2026. Photos: Pexels.</div>
<div class=foot><div class=jp><b>JP</b>Japan Like a Local</div><div>Full 21-page guide → <i>link in bio</i></div></div>
</body></html>'''
p=R/'tools/_cs.html'; p.write_text(html)
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350}); pg.goto(p.as_uri()); pg.wait_for_timeout(800)
    h=pg.evaluate("document.querySelector('.note').getBoundingClientRect().top - document.querySelector('.sos').getBoundingClientRect().bottom")
    print('gap above note',h)
    pg.screenshot(path=str(R/'assets/cheatsheet-20-things.png')); b.close()
p.unlink()
