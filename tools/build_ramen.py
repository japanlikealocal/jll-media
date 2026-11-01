# 12 Ramen Shops to Try in Tokyo (IG 1080x1350 + pin 1000x1500).
# Facts: Perplexity check 2026-10-29 (docs/ramen-sources-2026-11-01.md). Only confirmed prices / payment / English menus.
# Art: ChatGPT watercolor grid (assets/gyoza/grid.png -> p01..p12). Panels p05 (white lace wings) and p08 (cilantro)
# are NOT tied to any shop (style not confirmed). Okei + PAIRON use plain grilled art (new01/new02 when ready).
import pathlib
from PIL import Image, ImageOps
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; A=R/'assets/gyoza'; F=(R/'tools/fonts').as_uri()
SAM=(R/'assets/cutouts/samurai-base-wink.png').as_uri()
def art(name, fallback):
    p=A/f'{name}.jpg'
    if p.exists(): return p
    q=A/f'{name}-tmp.jpg'; ImageOps.mirror(Image.open(A/f'{fallback}.jpg')).save(q,quality=90); return q
A=R/'assets/ramen'
CASH,EN,NOCASH,BOOK,H24,BRING='cash','en','nocash','book','h24','bring'
SHOPS=[ # art, name, japanese, station, dish (confirmed price only), badges
 (A/'p01.jpg','Ichiran','一蘭 渋谷店','Shibuya · 3 min','Tonkotsu ramen ¥1,180',[H24]),
 (A/'p11.jpg','AFURI','AFURI 恵比寿','Ebisu · near station','Yuzu shio ramen',[EN,NOCASH]),
 (A/'e01.jpg','Rokurinsha','六厘舎 東京駅','Tokyo Sta. · Ramen Street','Tsukemen (dipping noodles)',[]),
 (A/'p02.jpg','Ginza Hachigo','銀座 八五','Higashi-Ginza · 3 min','Chuka soba · Michelin-listed',[EN,BOOK]),
 (A/'e02.jpg','Fu-unji','新宿 風雲児','Shinjuku · 1–5 min','Tsukemen ¥1,000',[]),
 (A/'e03.jpg','Soranoiro','ソラノイロ 銀座本店','Higashi-Ginza · 3 min','Vegan veggie soba',[]),
 (A/'p03.jpg','Kuroki','饗 くろ㐂','Asakusabashi · 2 min','Shio soba ¥1,400',[CASH]),
 (A/'p05.jpg','Nakiryu','創作麺工房 鳴龍','Otsuka · 4 min','Tantanmen ¥850',[BOOK,BRING]),
 (A/'p10.jpg','Shibata','中華そば しば田','Komae · 1 min','Chuka soba ¥1,300',[BRING]),
 (A/'p04.jpg','Ramen-ya Shima','らぁ麺や 嶋','Nishi-Shinjuku-5 · 5 min','Shoyu & shio ramen',[BOOK,BRING]),
 (A/'p07.jpg','Gokan','Japanese Ramen 五感','Ikebukuro East · 9 min','Premium shio ¥2,200',[BOOK,BRING]),
 (A/'p12.jpg','Te-uchi Ren','手打ち 蓮','Morishita · 6 min','Handmade noodles',[BRING]),
]
BADGE={CASH:'<i class="bd cs">💵 CASH ONLY</i>',BRING:'<i class="bd cs">💵 BRING CASH</i>',EN:'<i class="bd e">EN MENU</i>',NOCASH:'<i class="bd e">💳 NO CASH</i>',BOOK:'<i class="bd e">📅 BOOK AHEAD</i>',H24:'<i class="bd e">🕐 OPEN 24H</i>'}
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:WPX;height:HPX;background:#FFF4E2;font-family:I,"Noto Sans CJK JP";color:#3A1E10;overflow:hidden;position:relative}}
.head{{position:relative;height:HEADH;padding:22px 24px 0;background:linear-gradient(#FFE3B8,#FFF4E2)}}
.save{{display:inline-block;background:#D62828;color:#fff;font-weight:800;font-size:26px;padding:7px 18px;border-radius:10px;transform:rotate(-3deg)}}
h1{{font-weight:800;font-size:HSIZE;line-height:.95;letter-spacing:-2.5px;margin-top:12px}}
h1 em{{font-style:normal;color:#D62828;display:block}}
.pill{{display:inline-block;margin-top:12px;background:#3A1E10;color:#FFD43B;font-weight:800;font-size:23px;padding:8px 20px;border-radius:40px}}
.sam{{position:absolute;right:16px;bottom:-6px;height:SAMH;z-index:3;filter:drop-shadow(0 6px 10px rgba(0,0,0,.25))}}
.bub{{position:absolute;right:SAMR;top:28px;z-index:3;background:#fff;font-weight:800;font-size:22px;padding:10px 16px;border-radius:18px;border:3px solid #3A1E10}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:8px 22px 0}}
.c{{border-radius:12px;overflow:hidden;position:relative;height:CH;background:#fff}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:center 40%}}
.n{{z-index:2;position:absolute;left:7px;top:7px;width:32px;height:32px;border-radius:50%;background:#D62828;border:3px solid #fff;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:17px}}
.bds{{z-index:2;position:absolute;right:7px;top:8px;display:flex;flex-direction:column;align-items:flex-end;gap:4px}}
.bd{{font-style:normal;font-weight:800;font-size:13px;padding:4px 8px;border-radius:7px}}
.bd.cs{{background:#FFD43B;color:#3A1E10}} .bd.e{{background:#1D4ED8;color:#fff}}
.tx{{position:absolute;left:0;right:0;bottom:0;padding:24px 9px 7px;line-height:1.15;color:#fff;background:linear-gradient(rgba(40,15,5,0),rgba(40,15,5,.84) 42%)}}
.nm{{font-weight:800;font-size:18px;letter-spacing:-.3px}}
.jp{{font-family:"Noto Sans CJK JP";font-weight:700;font-size:12px;opacity:.85}}
.st{{font-weight:700;font-size:13px;opacity:.95}}
.ds{{font-weight:800;font-size:14px;color:#FFD43B;margin-top:1px}}
.ft{{position:absolute;left:22px;right:22px;bottom:10px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:12.5px;color:#7A5A48;gap:12px;line-height:1.25}}
.cta{{display:flex;align-items:center;gap:8px;background:#D62828;color:#fff;font-weight:800;font-size:17px;padding:8px 14px;border-radius:30px;white-space:nowrap}}
'''
def page(Wd,Hd,v):
    cards=''.join(f'<div class=c><div class=ph style="background-image:url({a.as_uri()})"></div><span class=n>{i+1}</span><span class=bds>{"".join(BADGE[b] for b in bd)}</span><div class=tx><div class=nm>{nm}</div><div class=jp>{jp}</div><div class=st>🚉 {st}</div><div class=ds>{ds}</div></div></div>' for i,(a,nm,jp,st,ds,bd) in enumerate(SHOPS))
    css=CSS
    for k,val in v.items(): css=css.replace(k,val)
    css=css.replace('WPX',f'{Wd}px').replace('HPX',f'{Hd}px')
    return f'''<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body>
<div class=head><div class=save>📌 SAVE THIS</div><h1>12 Ramen Shops<em>to Try in Tokyo</em></h1><div class=pill>Near stations · prices where confirmed</div>
<div class=bub>Show staff the 日本語 name!</div><img class=sam src="{SAM}"></div>
<div class=grid>{cards}</div>
<div class=ft><span>Checked Nov 1, 2026. Prices, hours, booking & payment can change; tax may not be included. AI illustrations for reference only.</span><span class=cta>💬 Comment JAPAN</span></div></body></html>'''
tmp=R/'tools/_ra.html'
with sync_playwright() as pw:
    b=pw.chromium.launch()
    for name,Wd,Hd,v in [('ig-tokyo-ramen',1080,1350,{'HEADH':'262px','HSIZE':'64px','SAMH':'220px','SAMR':'210px','CH':'248px'}),
                         ('pin-tokyo-ramen',1000,1500,{'HEADH':'300px','HSIZE':'64px','SAMH':'240px','SAMR':'210px','CH':'274px'})]:
        pg=b.new_page(viewport={'width':Wd,'height':Hd}); tmp.write_text(page(Wd,Hd,v)); pg.goto(tmp.as_uri()); pg.wait_for_timeout(800)
        gap=pg.evaluate("document.querySelector('.ft').getBoundingClientRect().top-Math.max(...[...document.querySelectorAll('.c')].map(e=>e.getBoundingClientRect().bottom))")
        over=pg.evaluate("[...document.querySelectorAll('.tx div')].filter(e=>e.scrollWidth>e.clientWidth+1).length")
        print(name,'gap',round(gap),'overflow',over); pg.screenshot(path=str(R/f'assets/{name}.png'))
    b.close()
tmp.unlink()
