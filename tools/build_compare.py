# Japan vs USA comparison infographic (1080x1350). Customs/rules only, hedged; no stereotypes.
import pathlib
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent
F=(R/'tools/fonts').as_uri()
JP=(R/'assets/covers/px-31130296-osaka-safe.jpg').as_uri(); US=(R/'assets/covers/px-11762890-nyc.jpg').as_uri()
ROWS=[('💵','Tipping','Not expected','Usual at sit-down restaurants'),
('🏷️','Price tags','Tax included','Sales tax often added at checkout'),
('👟','Shoes at home','Off at the door','Often kept on'),
('🚗','Driving side','Left','Right'),
('↕️','Escalators','Tokyo: usually stand left','Usually stand right'),
('📱','Calls on trains','Avoided on local trains','More common'),
('🧾','Paying at restaurants','Often at the register','Often at the table'),
('🙇','Greeting','Often a bow','Often a handshake'),
('♨️','Hot spring bath','Usually no swimsuit','Usually a swimsuit'),
('🆘','Emergency','110 police · 119 fire/ambulance','911')]
rows=''.join(f'<div class=r><div class=l>{a}</div><div class=c><span>{e}</span>{t}</div><div class=rr>{b}</div></div>' for e,t,a,b in ROWS)
html=f'''<!doctype html><html><head><meta charset=utf-8><style>
@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
@font-face{{font-family:I;src:url({F}/Inter-Regular.ttf);font-weight:400}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#FFF8EC;font-family:I,'Noto Color Emoji',sans-serif;color:#141B2D;position:relative;overflow:hidden}}
.hd{{display:flex;height:330px;position:relative}}
.hd>.j,.hd>.u{{flex:1;background-size:cover;background-position:center;position:relative;display:flex;align-items:flex-end;padding:0 34px 24px}}
.hd .j{{background-image:linear-gradient(rgba(0,0,0,.1),rgba(214,40,40,.85)),url({JP})}}
.hd .u{{background-image:linear-gradient(rgba(0,0,0,.1),rgba(47,111,214,.88)),url({US});justify-content:flex-end}}
.hd b{{color:#fff;font-weight:800;font-size:64px;text-shadow:0 3px 14px rgba(0,0,0,.4)}}
.vs{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:120px;height:120px;border-radius:50%;background:#FFD43B;border:6px solid #fff;font-weight:800;font-size:48px;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 20px rgba(0,0,0,.3)}}
.tt{{position:absolute;left:0;right:0;top:22px;text-align:center;color:#fff;font-weight:800;font-size:30px;letter-spacing:2px;text-shadow:0 2px 10px rgba(0,0,0,.6)}}
.save{{position:absolute;right:26px;top:18px;background:#FFD43B;color:#141B2D;font-weight:800;font-size:22px;padding:8px 14px;border-radius:10px;transform:rotate(4deg)}}
.list{{padding:14px 26px 0}}
.r{{display:grid;grid-template-columns:1fr 250px 1fr;align-items:center;background:#fff;border-radius:16px;margin-bottom:9px;min-height:78px;box-shadow:0 3px 0 #E7DFD2;overflow:hidden}}
.l,.rr{{font-weight:700;font-size:23px;line-height:1.15;padding:10px 18px}}
.l{{color:#B81F1F;border-left:8px solid #D62828}}
.rr{{color:#1F57B8;text-align:right;border-right:8px solid #2F6FD6}}
.c{{text-align:center;font-weight:800;font-size:20px;background:#141B2D;color:#fff;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:6px 8px;line-height:1.1}}
.c span{{font-size:28px;margin-bottom:3px}}
.note{{position:absolute;left:26px;right:26px;bottom:84px;font-size:15px;color:#6B6F78}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:72px;background:#141B2D;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 30px;font-weight:800;font-size:23px}}
.foot i{{font-style:normal;color:#FFD43B}}
.jp{{display:flex;align-items:center;gap:12px}}.jp b{{width:44px;height:44px;border-radius:50%;background:#D62828;display:flex;align-items:center;justify-content:center;font-size:17px}}
</style></head><body>
<div class=hd><div class=j><b>🇯🇵 JAPAN</b></div><div class=u><b>USA 🇺🇸</b></div><div class=vs>VS</div><div class=tt>10 DIFFERENCES TO KNOW</div><div class=save>📌 SAVE</div></div>
<div class=list>{rows}</div>
<div class=note>General customs — rules vary by place, state and business. In Japan, follow local signs and staff instructions. Photos: Pexels.</div>
<div class=foot><div class=jp><b>JP</b>Japan Like a Local</div><div>Free Japan Quick Start → <i>link in bio</i></div></div>
</body></html>'''
p=R/'tools/_cmp.html'; p.write_text(html)
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350}); pg.goto(p.as_uri()); pg.wait_for_timeout(800)
    print('gap',pg.evaluate("document.querySelector('.note').getBoundingClientRect().top - document.querySelector('.list').getBoundingClientRect().bottom"))
    pg.screenshot(path=str(R/'assets/compare-japan-usa.png')); b.close()
p.unlink()
