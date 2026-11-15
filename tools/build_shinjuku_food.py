# 4:5 list image: 5 food spots near Shinjuku, from the fact-checked food map data (checked Oct 29 - Nov 2, 2026).
# Theme: orange x cream (style-refs 11/15 color rules). CTA: Comment JAPAN (IG analysis 11/15).
import pathlib, json
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; F=(R/'tools/fonts').as_uri(); P=R/'assets/foodmap-photos'
ROWS=[('gyoza.jpg','GYOZA','Gyoza no Fukuho','餃子の福包 新宿店','Shinjuku-gyoemmae · 2 min','Pan-fried & boiled · Cards OK'),
('gyoza.jpg','GYOZA','Rouhen Gyozakan','老辺餃子舘 新宿本店','Shinjuku South · 1 min','Steamed · English touch-panel ordering'),
('ramen.jpg','RAMEN','Fu-unji','新宿 風雲児','Shinjuku · 1–5 min','Tsukemen ¥1,000 · ends when soup sells out'),
('yakitori.jpg','YAKITORI','Torikizoku','鳥貴族 新宿靖国通り店','Shinjuku-sanchome · 1 min','All items ¥390 (tax incl.) · open late'),
('yakitori-negima.jpg','YAKITORI','Torien','鳥園（思い出横丁）','Shinjuku West · 3 min','English menu · ¥330 table charge')]
rows=''.join(f'''<div class=r><div class=ph style="background-image:url({(P/ph).as_uri()})"><i>{i+1}</i></div><div class=tx><div class=k>{k}</div><div class=n>{n}</div>
<div class=j>{j}</div><div class=s>🚉 {s}</div><div class=f>{f}</div></div></div>''' for i,(ph,k,n,j,s,f) in enumerate(ROWS))
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}@font-face{{font-family:I;src:url({F}/Inter-Regular.ttf);font-weight:400}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;background:#FFF4E6;font-family:I,'Noto Sans CJK JP','Noto Color Emoji',sans-serif;color:#2B1A0E;overflow:hidden;position:relative}}
.hd{{background:#EA580C;color:#fff;padding:38px 56px 30px}}.hd small{{font-weight:800;font-size:24px;letter-spacing:3px;color:#FFE3C2}}.hd h1{{font-weight:800;font-size:64px;line-height:1.02;margin-top:6px}}
.list{{padding:20px 40px 0;display:flex;flex-direction:column;gap:12px}}
.r{{display:flex;gap:22px;background:#fff;border-radius:22px;padding:12px;box-shadow:0 3px 0 #F3D3B0;height:166px}}
.ph{{width:200px;border-radius:16px;background-size:cover;background-position:center;position:relative;flex:none}}
.ph i{{position:absolute;left:10px;top:10px;width:48px;height:48px;border-radius:50%;background:#EA580C;color:#fff;font-style:normal;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center}}
.tx{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:3px}}.k{{font-weight:800;font-size:18px;letter-spacing:2px;color:#EA580C}}
.n{{font-weight:800;font-size:36px;line-height:1.05}}.j{{font-size:24px;color:#7C4A1E;font-weight:700}}.s{{font-size:23px;font-weight:700}}.f{{font-size:22px;color:#57534e}}
.ft{{position:absolute;left:40px;right:40px;bottom:26px;display:flex;justify-content:space-between;align-items:center}}
.ft .m{{font-weight:800;font-size:24px;white-space:nowrap}}.ft .m b{{color:#EA580C}}.ft .c{{background:#2B1A0E;color:#FFD08A;font-weight:800;font-size:24px;padding:14px 22px;border-radius:40px;white-space:nowrap}}
.note{{position:absolute;left:40px;bottom:92px;font-size:18px;color:#8a7b6e}}'''
HTML=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=hd><small>TOKYO FOOD MAP · SHINJUKU</small><h1>Hungry in Shinjuku?<br>5 spots near the station</h1></div>
<div class=list>{rows}</div><div class=note>Checked Oct 29 – Nov 2, 2026 on shop pages & listings. Hours and prices can change. Photos are illustrative.</div>
<div class=ft><div class=m><b>+43 more</b> in the Tokyo Food Map</div><div class=c>💬 Comment JAPAN for a free guide</div></div></body></html>'''
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350}); t=R/'tools/_sf.html'; t.write_text(HTML); pg.goto(t.as_uri()); pg.wait_for_timeout(600)
    pg.screenshot(path=str(R/'assets/ig-shinjuku-food.png')); b.close(); t.unlink(); print('ok')
