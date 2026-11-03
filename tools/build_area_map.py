# Tokyo area guide map (IG 1080x1350 + pin 1000x1500). Positions from station coordinates (docs/tokyo-areas-sources-2026-11-03.md).
# Drawn from real coordinates (north up). No AI art, so geography stays correct. Coastline NOT drawn (no shape data) — only a soft "Tokyo Bay" hint.
import pathlib, math
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; F=(R/'tools/fonts').as_uri()
SAM=(R/'assets/cutouts/samurai-base-wink.png').as_uri()
LAT0=35.6824; COS=math.cos(math.radians(LAT0))
AREAS=[ # n, name, lat, lon, color, line, time, label side
 (1,'Shinjuku',35.69056,139.69944,'#7C3AED','Nightlife · department stores · Shinjuku Gyoen','~15 min','l'),
 (2,'Shibuya',35.65851,139.70133,'#DB2777','Scramble crossing · SHIBUYA SKY','~25 min','l'),
 (3,'Harajuku',35.67016,139.70269,'#EC4899','Street style · Meiji Jingu · Omotesando','~25–30 min','l'),
 (4,'Asakusa',35.71083,139.79783,'#DC2626','Senso-ji Temple · old shopping streets','~20 min','r'),
 (5,'Ueno',35.71343,139.77672,'#16A34A','Museums · big park · Ameyoko market','~10 min','l'),
 (6,'Akihabara',35.69833,139.77306,'#F59E0B','Electronics · anime · games','~5 min','r'),
 (7,'Ginza',35.67123,139.76500,'#B45309','Luxury shopping · kabuki theatre','~3 min (subway)','l'),
 (8,'Tokyo Sta.',35.68083,139.76694,'#B91C1C','Red-brick station · start point','—','r'),
 (9,'Roppongi',35.66278,139.73139,'#4F46E5','Art museums · nightlife','~25–30 min','r'),
 (10,'Odaiba',35.62589,139.77142,'#0891B2','Bay views · waterfront fun','~30 min','r'),
 (11,'Tsukiji',35.66810,139.77250,'#EA580C','Outer market · sushi · street food','~10–15 min','r'),
 (12,'Toyosu',35.65500,139.79608,'#0E7490','Fish market · teamLab Planets','~20 min','r'),
]
YAMANOTE=[(35.68083,139.76694),(35.6918,139.7709),(35.69833,139.77306),(35.7078,139.7745),(35.71343,139.77672),(35.72759,139.77078),(35.7381,139.7608),(35.7365,139.7470),(35.7312,139.7289),(35.73028,139.71139),(35.7212,139.7066),(35.7128,139.7038),(35.69056,139.69944),(35.6835,139.7020),(35.67016,139.70269),(35.65851,139.70133),(35.6467,139.7101),(35.6339,139.7157),(35.6285,139.7387),(35.6450,139.7475),(35.6555,139.7570),(35.6663,139.7583),(35.6751,139.7630),(35.68083,139.76694)]
PAL=(35.68240,139.75270)
def xy(lat,lon,box):
    x0,x1,y0,y1=139.680,139.815,35.742,35.615
    W,H,pad=box
    sx=(W-2*pad)/((x1-x0)*COS); sy=(H-2*pad)/((y0-y1))
    s=min(sx,sy)
    ox=(W-(x1-x0)*COS*s)/2; oy=(H-(y0-y1)*s)/2
    return ox+(lon-x0)*COS*s, oy+(y0-lat)*s
def svg(W,H):
    box=(W,H,10)
    pts=' '.join(f'{xy(a,b,box)[0]:.1f},{xy(a,b,box)[1]:.1f}' for a,b in YAMANOTE)
    px,py=xy(*PAL,box)
    bx,by=xy(35.628,139.800,box)
    out=[f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',
     f'<rect width="{W}" height="{H}" rx="22" fill="#F4ECDD"/>',
     f'<ellipse cx="{bx:.0f}" cy="{by+40:.0f}" rx="{W*0.2:.0f}" ry="{H*0.16:.0f}" fill="#BFE3F2" opacity=".8"/>',
     f'<text x="{bx+70:.0f}" y="{by+62:.0f}" font-family="I" font-weight="700" font-size="18" fill="#3B82A6" font-style="italic">Tokyo Bay →</text>',
     f'<polyline points="{pts}" fill="none" stroke="#9BC53D" stroke-width="9" stroke-linejoin="round" opacity=".85"/>',
     f'<ellipse cx="{px:.0f}" cy="{py:.0f}" rx="34" ry="28" fill="#A7C98B"/>',
     f'<text x="{px:.0f}" y="{py+5:.0f}" text-anchor="middle" font-family="I" font-weight="700" font-size="14" fill="#2F4F1F">Imperial</text>',
     f'<text x="{px:.0f}" y="{py+20:.0f}" text-anchor="middle" font-family="I" font-weight="700" font-size="14" fill="#2F4F1F">Palace</text>']
    lx,ly=xy(35.7375,139.6880,box)
    out.append(f'<text x="{lx:.0f}" y="{ly:.0f}" font-family="I" font-weight="800" font-size="17" fill="#6B8E23">● JR Yamanote Line (loop)</text>')
    cx,cy=W-50,52
    out.append(f'<g transform="translate({cx},{cy})"><circle r="26" fill="#fff" stroke="#2A1A10" stroke-width="2"/><path d="M0,-18 L7,4 L0,0 L-7,4Z" fill="#D62828"/><text y="17" text-anchor="middle" font-family="I" font-weight="800" font-size="12">N</text></g>')
    for n,name,la,lo,c,_,_,side in AREAS:
        x,y=xy(la,lo,box)
        tw=len(name)*11.5+38
        tx=x+16 if side=='r' else x-16-tw
        out.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{tx+(0 if side=="r" else tw):.0f}" y2="{y:.0f}" stroke="{c}" stroke-width="2.5"/>')
        out.append(f'<rect x="{tx:.0f}" y="{y-17:.0f}" width="{tw:.0f}" height="34" rx="17" fill="{c}"/>')
        out.append(f'<circle cx="{tx+17:.0f}" cy="{y:.0f}" r="12" fill="#fff"/><text x="{tx+17:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="I" font-weight="800" font-size="14" fill="{c}">{n}</text>')
        out.append(f'<text x="{tx+33:.0f}" y="{y+6:.0f}" font-family="I" font-weight="800" font-size="18" fill="#fff">{name}</text>')
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="#fff" stroke="{c}" stroke-width="5"/>')
    out.append('</svg>'); return ''.join(out)
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:WPX;height:HPX;background:#FFF8EE;font-family:I;color:#2A1A10;overflow:hidden;position:relative}}
.head{{position:relative;height:HEADH;padding:20px 26px 0;background:#1E3A5F}}
.save{{display:inline-block;background:#FFD43B;font-weight:800;font-size:23px;padding:6px 16px;border-radius:10px;transform:rotate(-3deg)}}
h1{{color:#fff;font-weight:800;font-size:HSIZE;line-height:.98;letter-spacing:-2px;margin-top:10px}}
h1 em{{font-style:normal;color:#FFD43B;display:block}}
.sub{{color:#CFE0F5;font-weight:700;font-size:21px;margin-top:8px}}
.sam{{position:absolute;right:14px;bottom:-4px;height:SAMH;z-index:3}}
.bub{{position:absolute;right:SAMR;top:26px;z-index:3;background:#fff;font-weight:800;font-size:20px;padding:9px 14px;border-radius:16px;border:3px solid #2A1A10}}
.map{{padding:12px 18px 0}}
.list{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px 10px;padding:10px 18px 0}}
.it{{display:flex;gap:8px;align-items:flex-start;background:#fff;border-radius:10px;padding:6px 8px}}
.it b{{flex:none;width:24px;height:24px;border-radius:50%;color:#fff;font-size:13px;display:flex;align-items:center;justify-content:center;margin-top:2px}}
.nm{{font-weight:800;font-size:15.5px;line-height:1.1}}
.ds{{font-weight:700;font-size:11.5px;color:#5C4A3E;line-height:1.2;margin-top:1px}}
.tm{{font-weight:800;font-size:11.5px;color:#1E3A5F}}
.ft{{position:absolute;left:18px;right:18px;bottom:10px;display:flex;justify-content:space-between;align-items:center;gap:10px;font-weight:700;font-size:11.5px;color:#7A6658;line-height:1.25}}
.cta{{background:#D62828;color:#fff;font-weight:800;font-size:16px;padding:8px 14px;border-radius:30px;white-space:nowrap}}
'''
def page(Wd,Hd,v,mh):
    items=''.join(f'<div class=it><b style="background:{c}">{n}</b><div><div class=nm>{name}</div><div class=ds>{d}</div><div class=tm>🚃 {"From Tokyo Sta. "+t if t!="—" else "Start here"}</div></div></div>' for n,name,_,_,c,d,t,_ in AREAS)
    css=CSS
    for k,val in v.items(): css=css.replace(k,val)
    css=css.replace('WPX',f'{Wd}px').replace('HPX',f'{Hd}px')
    return f'''<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body>
<div class=head><div class=save>📌 SAVE THIS</div><h1>First time in Tokyo?<em>12 areas on one map</em></h1><div class=sub>Where each area is — and what it's known for</div>
<div class=bub>Which area first?</div><img class=sam src="{SAM}"></div>
<div class=map>{svg(Wd-36,mh)}</div><div class=list>{items}</div>
<div class=ft><span>Pins = main stations, not exact boundaries. Times are approximate (Nov 2026). Check official sites for hours & closures.</span><span class=cta>💬 Comment JAPAN</span></div></body></html>'''
tmp=R/'tools/_am.html'
with sync_playwright() as pw:
    b=pw.chromium.launch()
    for name,Wd,Hd,v,mh in [('ig-tokyo-area-map',1080,1350,{'HEADH':'250px','HSIZE':'58px','SAMH':'190px','SAMR':'170px'},740),
                            ('pin-tokyo-area-map',1000,1500,{'HEADH':'240px','HSIZE':'54px','SAMH':'200px','SAMR':'170px'},880)]:
        pg=b.new_page(viewport={'width':Wd,'height':Hd}); tmp.write_text(page(Wd,Hd,v,mh)); pg.goto(tmp.as_uri()); pg.wait_for_timeout(700)
        gap=pg.evaluate("document.querySelector('.ft').getBoundingClientRect().top-Math.max(...[...document.querySelectorAll('.it')].map(e=>e.getBoundingClientRect().bottom))")
        print(name,'gap',round(gap)); pg.screenshot(path=str(R/f'assets/{name}.png'))
    b.close()
tmp.unlink()
