# Harajuku -> Omotesando -> Aoyama walking route (schematic, NOT to scale). Facts: docs/harajuku-walk-sources-2026-11-03.md
import pathlib, math
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; F=(R/'tools/fonts').as_uri()
SAM=(R/'assets/cutouts/samurai-base-wink.png').as_uri()
COS=math.cos(math.radians(35.668))
P={'sta':(35.67016,139.70269),'tke':(35.6712,139.7055),'jse':(35.6694,139.7010),'hall':(35.6764,139.6993),
   'jx':(35.6687,139.7055),'cat':(35.6676,139.7083),'cats':(35.6662,139.7077),'hills':(35.66722,139.70889),
   'ox':(35.6654,139.7124),'nezu':(35.6622,139.7172),'a5':(35.6649,139.7135)}
ROUTE=['sta','tke','sta','jse','hall','jse','jx','cat','cats','cat','hills','ox','nezu','a5']
STOPS=[(1,'sta','Harajuku Sta.','Takeshita Exit — start','','#1E3A5F','r'),
 (2,'tke','Takeshita Street','Youth fashion & colourful snacks','5–10 min','#EC4899','r'),
 (3,'hall','Meiji Jingu','Shrine in a big forest · free · gates close 16:10 (Nov)','20–30 min','#15803D','r'),
 (4,'jx','Omotesando Ave.','Tree-lined avenue from Jingumae crossing','20–25 min','#B45309','l'),
 (5,'cats','Cat Street','Backstreet shops — short loop south','3–5 min','#7C3AED','l'),
 (6,'hills','Omotesando Hills','Tadao Ando-designed shopping complex','3–5 min','#0891B2','r'),
 (7,'ox','Miyuki-dori turn','Turn toward Aoyama at Omotesando crossing','7–10 min','#64748B','l'),
 (8,'nezu','Nezu Museum','Japanese art + garden · ¥1,600 online · closed Nov 2, 9, 16, 24–30','8–12 min','#DC2626','l'),
 (9,'a5','Omotesando Sta.','Exit A5 — finish (Ginza/Chiyoda/Hanzomon lines)','~8 min','#1E3A5F','r')]
def svg(W,H):
    x0,x1,y0,y1=139.6960,139.7195,35.6775,35.6612
    pad=40; s=min((W-2*pad)/((x1-x0)*COS),(H-2*pad)/(y0-y1))
    ox=(W-(x1-x0)*COS*s)/2; oy=(H-(y0-y1)*s)/2
    xy=lambda k:(ox+(P[k][1]-x0)*COS*s, oy+(y0-P[k][0])*s)
    hx,hy=xy('hall')
    o=[f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg"><rect width="{W}" height="{H}" rx="22" fill="#F4ECDD"/>',
       f'<ellipse cx="{hx-10:.0f}" cy="{hy+40:.0f}" rx="{W*0.17:.0f}" ry="{H*0.33:.0f}" fill="#BFD9A8"/>',
       f'<text x="{hx-150:.0f}" y="{hy+60:.0f}" font-family="I" font-weight="800" font-size="17" fill="#3F6B2A">Meiji Jingu forest</text>']
    a,b=xy('jx'),xy('ox')
    o.append(f'<line x1="{a[0]-40:.0f}" y1="{a[1]-12:.0f}" x2="{b[0]+30:.0f}" y2="{b[1]+8:.0f}" stroke="#D9C9A8" stroke-width="22" stroke-linecap="round"/>')
    o.append(f'<text x="{(a[0]+b[0])/2-60:.0f}" y="{(a[1]+b[1])/2-20:.0f}" font-family="I" font-weight="700" font-size="15" fill="#8A6A3A" font-style="italic">Omotesando avenue</text>')
    pts=' '.join(f'{xy(k)[0]:.1f},{xy(k)[1]:.1f}' for k in ROUTE)
    o.append(f'<polyline points="{pts}" fill="none" stroke="#D62828" stroke-width="5" stroke-dasharray="10 8" stroke-linejoin="round" stroke-linecap="round"/>')
    o.append(f'<g transform="translate({W-48},48)"><circle r="24" fill="#fff" stroke="#2A1A10" stroke-width="2"/><path d="M0,-16 L6,4 L0,0 L-6,4Z" fill="#D62828"/><text y="16" text-anchor="middle" font-family="I" font-weight="800" font-size="11">N</text></g>')
    for n,k,name,_,_,c,side in STOPS:
        x,y=xy(k); tw=len(name)*10.5+40
        tx=x+18 if side=='r' else x-18-tw
        o.append(f'<rect x="{tx:.0f}" y="{y-16:.0f}" width="{tw:.0f}" height="32" rx="16" fill="{c}"/><circle cx="{tx+16:.0f}" cy="{y:.0f}" r="11" fill="#fff"/>')
        o.append(f'<text x="{tx+16:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="I" font-weight="800" font-size="13" fill="{c}">{n}</text><text x="{tx+32:.0f}" y="{y+6:.0f}" font-family="I" font-weight="800" font-size="16" fill="#fff">{name}</text>')
        o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="#fff" stroke="{c}" stroke-width="5"/>')
    o.append(f'<text x="20" y="{H-16}" font-family="I" font-weight="700" font-size="14" fill="#8A7A6A">Schematic · not to scale</text></svg>'); return ''.join(o)
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:WPX;height:HPX;background:#FFF8EE;font-family:I;color:#2A1A10;overflow:hidden;position:relative}}
.head{{position:relative;height:HEADH;padding:20px 26px 0;background:#14532D}}
.save{{display:inline-block;background:#FFD43B;font-weight:800;font-size:23px;padding:6px 16px;border-radius:10px;transform:rotate(-3deg)}}
h1{{color:#fff;font-weight:800;font-size:HSIZE;line-height:.98;letter-spacing:-2px;margin-top:10px}}
h1 em{{font-style:normal;color:#FFD43B;display:block}}
.sub{{color:#D3F0C2;font-weight:700;font-size:21px;margin-top:8px}}
.sam{{position:absolute;right:14px;bottom:-4px;height:SAMH;z-index:3}}
.bub{{position:absolute;right:SAMR;top:26px;z-index:3;background:#fff;font-weight:800;font-size:20px;padding:9px 14px;border-radius:16px;border:3px solid #2A1A10}}
.map{{padding:12px 18px 0}}
.list{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px 10px;padding:10px 18px 0}}
.it{{display:flex;gap:8px;background:#fff;border-radius:10px;padding:6px 8px}}
.it b{{flex:none;width:24px;height:24px;border-radius:50%;color:#fff;font-size:13px;display:flex;align-items:center;justify-content:center;margin-top:2px}}
.nm{{font-weight:800;font-size:15px;line-height:1.1}} .ds{{font-weight:700;font-size:11.3px;color:#5C4A3E;line-height:1.2;margin-top:1px}} .tm{{font-weight:800;font-size:11.3px;color:#14532D}}
.ft{{position:absolute;left:18px;right:18px;bottom:10px;display:flex;justify-content:space-between;align-items:center;gap:10px;font-weight:700;font-size:11.5px;color:#7A6658;line-height:1.25}}
.cta{{background:#D62828;color:#fff;font-weight:800;font-size:16px;padding:8px 14px;border-radius:30px;white-space:nowrap}}
'''
def page(Wd,Hd,v,mh):
    items=''.join(f'<div class=it><b style="background:{c}">{n}</b><div><div class=nm>{name}</div><div class=ds>{d}</div>{f"<div class=tm>🚶 {t} walk</div>" if t else ""}</div></div>' for n,_,name,d,t,c,_ in STOPS)
    css=CSS
    for k,val in v.items(): css=css.replace(k,val)
    css=css.replace('WPX',f'{Wd}px').replace('HPX',f'{Hd}px')
    return f'''<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body>
<div class=head><div class=save>📌 SAVE THIS</div><h1>Harajuku → Aoyama<em>Half-day walking route</em></h1><div class=sub>9 stops · ~6 km · allow 5–6 hours with breaks</div>
<div class=bub>Shrine in the morning!</div><img class=sam src="{SAM}"></div>
<div class=map>{svg(Wd-36,mh)}</div><div class=list>{items}</div>
<div class=ft><span>Walk times are estimates. Some backtracking. Nezu Museum garden & café need museum admission. Checked Nov 3, 2026 — check opening dates before you go.</span><span class=cta>💬 Comment JAPAN</span></div></body></html>'''
tmp=R/'tools/_hw.html'
with sync_playwright() as pw:
    b=pw.chromium.launch()
    for name,Wd,Hd,v,mh in [('ig-harajuku-walk',1080,1350,{'HEADH':'250px','HSIZE':'58px','SAMH':'190px','SAMR':'170px'},760),
                            ('pin-harajuku-walk',1000,1500,{'HEADH':'250px','HSIZE':'54px','SAMH':'200px','SAMR':'170px'},900)]:
        pg=b.new_page(viewport={'width':Wd,'height':Hd}); tmp.write_text(page(Wd,Hd,v,mh)); pg.goto(tmp.as_uri()); pg.wait_for_timeout(700)
        gap=pg.evaluate("document.querySelector('.ft').getBoundingClientRect().top-Math.max(...[...document.querySelectorAll('.it')].map(e=>e.getBoundingClientRect().bottom))")
        print(name,'gap',round(gap)); pg.screenshot(path=str(R/f'assets/{name}.png'))
    b.close()
tmp.unlink()
