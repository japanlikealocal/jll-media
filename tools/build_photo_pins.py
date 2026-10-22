# Photo-header pins (1000x1500). Facts only from paid guide v2 / official sources checked 10/20.
import pathlib
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent
F=(R/'tools/fonts').as_uri()
FREE='Free 1-page cheat sheet: Japan Quick Start'
PAID='JAPAN LIKE A LOCAL · 21-page PDF · $4.99'
PINS=[
 ('pin-shinkansen-luggage','px-29058311-shinkansen.jpg','30% 60%','BIG SUITCASE?','Shinkansen luggage: 4 rules',[
   ('Up to 160 cm','No reservation. Use the overhead rack.'),
   ('161–250 cm','Reserve a seat with an oversized baggage area.'),
   ('No reservation?','1,000 yen fee. Staff will show you where.'),
   ('Over 250 cm','Not allowed on board.')],'Tokaido, Sanyo, Kyushu & Nishi-Kyushu lines. Strollers & sports gear are exempt.',FREE),
 ('pin-taxfree-airport','px-2646521.jpg','center 85%','NEW FROM NOV 1, 2026','Tax-free at the airport: step by step',[
   ('Get ready','Passport, every receipt and the items.'),
   ('Check before bags','Use the tax-free terminal before check-in.'),
   ('Green or red?','Green = done. Red = customs inspection.'),
   ('Finish before boarding','Leave extra time.')],'Steps may vary by airport. Full guide: 21-page PDF.',PAID),
 ('pin-order-food','px-12984979.jpg','center 45%','NO JAPANESE? NO PROBLEM','Order food in Japan: 5 tips',[
   ('Wait to be seated','Unless it is clearly self-seating.'),
   ('Point at photos','Menus and food models help.'),
   ('Ticket machine?','Buy the ticket first, hand it to staff.'),
   ('English menu?','Ask: “Eigo no menyuu wa arimasu ka?”'),
   ('Serious allergy?','Carry a written allergy card in Japanese.')],'Rules vary by restaurant. Follow staff instructions.',FREE),
 ('pin-big-station','px-30936433-n700.jpg','center center','BIG STATION?','Lost in a Japanese station? 5 tips',[
   ('One step at a time','Line, direction, platform, destination.'),
   ('Find your final stop','Signs show the train’s final destination.'),
   ('IC card not working?','Go to the staffed gate.'),
   ('Missed your stop?','Stay calm. Get off at the next station.'),
   ('Ask for help','“___ wa doko desu ka?” = Where is ___?')],'Leave buffer time for big stations and wrong exits.',FREE),
 ('pin-guide-inside','px-31130296-osaka-safe.jpg','center 45%','FIRST TRIP TO JAPAN?','What’s inside the 21‑page guide',[
   ('Tax-free rules','New from Nov 1, 2026 + the airport check.'),
   ('5 situation guides','Onsen, toilets, taxis & luggage, shrines, vending & escalators.'),
   ('Money & trains','Cash, IC cards, etiquette, food & konbini.'),
   ('Cheat sheet','First 24 hours + emergency numbers.')],'Updated November 2026 · PDF · $4.99',PAID),
]
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
@font-face{{font-family:I;src:url({F}/Inter-Regular.ttf);font-weight:400}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1000px;height:1500px;background:#FFF8EC;font-family:I,'Noto Color Emoji',sans-serif;color:#141B2D;position:relative;overflow:hidden}}
.hero{{height:640px;background-size:cover;position:relative}}
.hero:after{{content:"";position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,0) 25%,rgba(0,0,0,.78))}}
.ht{{position:absolute;left:56px;right:56px;bottom:34px;z-index:2}}
.tag{{display:inline-block;background:#FFD43B;font-weight:800;font-size:30px;padding:8px 18px;border-radius:10px}}
h1{{color:#fff;font-weight:800;font-size:80px;line-height:1.0;letter-spacing:-2px;margin-top:14px;text-shadow:0 4px 18px rgba(0,0,0,.5)}}
.save{{position:absolute;right:40px;top:36px;z-index:2;background:#D62828;color:#fff;font-weight:800;font-size:28px;padding:10px 18px;border-radius:12px;transform:rotate(4deg)}}
.list{{padding:26px 56px 0}}
.it{{display:flex;gap:22px;align-items:flex-start;padding:16px 0;border-bottom:2px dashed #E7DFD2}}
.n{{flex:0 0 60px;height:60px;border-radius:50%;background:#D62828;color:#fff;font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center}}
.t{{font-weight:800;font-size:44px;line-height:1.1}}
.d{{font-size:31px;color:#3F4450;margin-top:4px;line-height:1.25}}
.note{{margin:20px 56px 0;background:#fbe1e1;color:#B81F1F;font-weight:700;font-size:27px;padding:18px 24px;border-radius:14px;line-height:1.25}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:110px;background:#141B2D;display:flex;align-items:center;gap:22px;padding:0 56px;color:#fff;font-weight:800;font-size:32px}}
.jp{{width:62px;height:62px;border-radius:50%;background:#D62828;display:flex;align-items:center;justify-content:center;font-size:24px}}'''
tmp=R/'tools/_pin.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1000,'height':1500})
    for name,img,pos,tag,title,items,note,foot in PINS:
        url=(R/'assets/covers'/img).as_uri()
        its=''.join(f'<div class=it><div class=n>{i+1}</div><div><div class=t>{t}</div><div class=d>{d}</div></div></div>' for i,(t,d) in enumerate(items))
        tmp.write_text(f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=hero style="background-image:url({url});background-position:{pos}"><div class=save>📌 SAVE</div><div class=ht><div class=tag>{tag}</div><h1>{title}</h1></div></div><div class=list>{its}</div><div class=note>{note}</div><div class=foot><div class=jp>JP</div>{foot}</div></body></html>')
        pg.goto(tmp.as_uri()); pg.wait_for_timeout(500)
        gap=pg.evaluate("document.querySelector('.foot').getBoundingClientRect().top-document.querySelector('.note').getBoundingClientRect().bottom")
        print(name,'gap',round(gap))
        pg.screenshot(path=str(R/f'assets/{name}.png'))
    b.close()
tmp.unlink()
