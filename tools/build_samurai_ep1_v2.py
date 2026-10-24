# Samurai x Shiba ep.1 v2 (10/24): illustrated shop background, aligned pose pairs, light hat flick.
import pathlib,subprocess,math
from PIL import Image,ImageDraw,ImageFilter,ImageOps
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; E=R/'assets/ep1'
W,H,FPS=1080,1920,30
F=(R/'tools/fonts').as_uri(); ACC='#7B3FE4'
def L(p): return Image.open(p).convert('RGBA')
# background (flipped so the door is on the right, bench on the left)
BG0=ImageOps.mirror(L(E/'bg-shop-simple.png'))
K=W/BG0.width                     # 1.148
_b=BG0.resize((W,round(BG0.height*K)),Image.LANCZOS); DY=130
BG=Image.new('RGBA',(W,H)); BG.alpha_composite(_b,(0,DY)); BG.alpha_composite(_b.crop((0,0,W,8)).resize((W,DY+8)),(0,0))
GROUND=1560; s=0.62              # character canvas scale
cut={k:L(E/f'cut-{k}.png') for k in ['sit-eat','sit-hehe','sit-hatpop','sam-before','sam-after']}
cut={k:v.resize((round(v.width*s),round(v.height*s)),Image.LANCZOS) for k,v in cut.items()}
XS,YS=390,round(GROUND-1380*s)     # shiba canvas origin
XM,YM=-20,round(GROUND-1450*s)     # samurai canvas origin
old={k:L(R/f'assets/cutouts/{k}.png') for k in ['samurai-D-laugh','samurai-A-bow','samurai-C-thumbsup','samurai-base-wink','shiba-4-bow','shiba-5-thumbsup']}
def fit(im,h): return im.resize((round(im.width*h/im.height),h),Image.LANCZOS)
def shadow(fr,cx,y,w,a=70):
    sh=Image.new('RGBA',(W,H)); d=ImageDraw.Draw(sh); d.ellipse([cx-w/2,y-w*0.09,cx+w/2,y+w*0.09],fill=(90,60,30,a))
    fr.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
def sit_shadow(fr,xo): shadow(fr,xo+470*s,GROUND-25,820*s,80)
def sam_shadow(fr,xo): shadow(fr,xo+370*s,GROUND-8,640*s,80)
# overlays (text, arrows, burst) rendered with Playwright, transparent
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:B;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;font-family:I;font-weight:800;position:relative;overflow:hidden;background:transparent}}
.jp{{position:absolute;left:70px;top:150px;display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.95);border-radius:60px;padding:10px 26px 10px 12px;font-size:32px;color:#141B2D}}
.jp b{{width:52px;height:52px;border-radius:50%;background:{ACC};color:#fff;display:flex;align-items:center;justify-content:center;font-size:22px}}
.box{{position:absolute;left:70px;right:70px;top:236px}}
.tag{{display:inline-block;background:{ACC};color:#fff;font-size:40px;padding:10px 22px;border-radius:10px;margin-bottom:16px}}
h1{{color:#141B2D;font-size:96px;line-height:1;letter-spacing:-3px;text-shadow:0 0 18px rgba(255,248,235,.9)}}
h1 em{{font-style:normal;color:{ACC}}}
.p{{background:rgba(255,255,255,.92);border-radius:22px;padding:22px 28px;color:#141B2D;font-family:B;font-weight:700;font-size:60px;line-height:1.18;display:inline-block}}
.cta{{display:inline-block;background:{ACC};color:#fff;font-size:54px;line-height:1.2;padding:28px 36px;border-radius:24px;margin-top:20px}}
.pon{{position:absolute;width:400px;height:280px;display:flex;align-items:center;justify-content:center;font-size:84px;color:#fff;-webkit-text-stroke:5px #141B2D;background:#FFC83D;
 clip-path:polygon(50% 0,60% 22%,84% 6%,78% 32%,100% 38%,80% 56%,96% 80%,68% 72%,58% 100%,46% 76%,20% 96%,24% 68%,0 62%,20% 46%,4% 20%,32% 28%);transform:rotate(-6deg)}}
svg{{position:absolute;inset:0}}
'''
JP='<div class=jp><b>JP</b>Japan Like a Local</div>'
DOOR_X=round((941-340)*K)  # door centre after flip ≈ 690
BLOCK=f'''<svg width=1080 height=1920><path d="M{DOOR_X} 1240 C {DOOR_X+40} 1300, {DOOR_X+190} 1420, {DOOR_X+200} 1760" stroke="#fff" stroke-width="16" stroke-dasharray="34 22" fill="none" stroke-linecap="round" opacity=".95"/>
<circle cx="{DOOR_X+150}" cy="1150" r="62" fill="#E5383B" stroke="#fff" stroke-width="8"/><path d="M{DOOR_X+124} 1124 l52 52 M{DOOR_X+176} 1124 l-52 52" stroke="#fff" stroke-width="14" stroke-linecap="round"/></svg>'''
OK_PATH='''<svg width=1080 height=1920><path d="M760 1080 C 780 1300, 820 1450, 830 1760" stroke="#2BAE66" stroke-width="16" stroke-dasharray="34 22" fill="none" stroke-linecap="round"/>
<circle cx="860" cy="1000" r="62" fill="#2BAE66" stroke="#fff" stroke-width="8"/><path d="M830 1002 l22 22 l40 -44" stroke="#fff" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
OV={
 'hook':JP+'<div class=box><div class=tag>JAPAN MANNERS</div><h1>Snack time<br><em>right here?</em></h1></div>',
 'hookx':JP+'<div class=box><div class=tag>JAPAN MANNERS</div><h1>Snack time<br><em>right here?</em></h1></div>'+BLOCK,
 'none':JP,
 'pon':JP+'<div class=pon style="left:600px;top:700px">PON!</div>',
 'rule':JP+'<div class=box><h1>Keep shop<br>entrances <em>clear.</em></h1></div>',
 'bench':JP+'<div class=box><div class=tag>DO THIS</div><div class=p>Eat inside if there’s seating,<br>or find a bench.</div></div><svg width=1080 height=1920><circle cx="900" cy="1000" r="62" fill="#2BAE66" stroke="#fff" stroke-width="8"/><path d="M870 1002 l22 22 l40 -44" stroke="#fff" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'bow':JP+'<div class=box><h1>“Sumimasen!”</h1><div class=p style="margin-top:18px">= Excuse me / Sorry</div></div>',
 'cta':JP+'<div class=box><div class=p>Save this for your trip!</div><br><div class=cta>Free 1-page Japan Quick Start:<br>link in bio</div></div>',
}
ovl={}; tmp=R/'tools/_e1.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':W,'height':H})
    for k,body in OV.items():
        tmp.write_text(f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>')
        pg.goto(tmp.as_uri()); pg.wait_for_timeout(300); p=R/f'tools/_ov_{k}.png'; pg.screenshot(path=str(p),omit_background=True); ovl[k]=L(p); p.unlink()
    b.close()
tmp.unlink()
# bench close-up background (zoom on the bench, now on the left)
Z=2.2; BZ=BG0.resize((round(BG0.width*K*Z),round(BG0.height*K*Z)),Image.LANCZOS)
seat_y=880*K*Z; OFFY=round(1250-seat_y); BZc=Image.new('RGBA',(W,H)); BZc.alpha_composite(BZ,(0,OFFY))
s2=0.49; bench_eat=cut['sit-eat'].resize((round(cut['sit-eat'].width*s2/s),round(cut['sit-eat'].height*s2/s)),Image.LANCZOS)
def frame(sc,t):
    fr=(BZc if sc=='bench' else BG).copy() if sc=='bench' else Image.new('RGBA',(W,H))
    if sc!='bench': fr.alpha_composite(BG,(0,0))
    if sc in('s1','s1x','s2','s3','s4'):
        sk={'s3':'sit-hatpop','s4':'sit-hehe'}.get(sc,'sit-eat')
        sit_shadow(fr,XS); fr.alpha_composite(cut[sk],(XS,YS))
        if sc in('s2','s3','s4'):
            if sc=='s2': x=XM+round(-640*max(0,1-t/0.35)**2)
            else: x=XM
            if sc=='s4':
                a=fit(old['samurai-D-laugh'],720); shadow(fr,40+a.width/2,GROUND-6,a.width*0.8); fr.alpha_composite(a,(40,GROUND-a.height))
            else: sam_shadow(fr,x); fr.alpha_composite(cut['sam-after' if sc=='s3' else 'sam-before'],(x,YM))
    elif sc=='bench':
        x0=round(305-450*s2); y0=round(1250-1300*s2)
        shadow(fr,305,1262,380,60); fr.alpha_composite(bench_eat,(x0,y0))
    elif sc in('bow','cta'):
        sa,sh_=('samurai-A-bow','shiba-4-bow') if sc=='bow' else ('samurai-C-thumbsup','shiba-5-thumbsup')
        a=fit(old[sa],760); c=fit(old[sh_],700)
        shadow(fr,90+a.width/2,GROUND-6,a.width*0.8); fr.alpha_composite(a,(90,GROUND-a.height))
        shadow(fr,600+c.width/2,GROUND-6,c.width*0.8); fr.alpha_composite(c,(600,GROUND-c.height))
    return fr
SC=[('s1','hook',1.2),('s1x','hookx',1.3),('s2','none',1.0),('s3','pon',1.0),('s4','rule',2.0),('bench','bench',2.8),('bow','bow',2.0),('cta','cta',2.8)]
out=R/'reels/2026-10-25-samurai-ep1-sitting-v2-silent.mp4'
p=subprocess.Popen(['ffmpeg','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-f','lavfi','-i','anullsrc=r=44100:cl=stereo',
  '-shortest','-c:v','libx264','-profile:v','high','-crf','20','-pix_fmt','yuv420p','-g','60','-c:a','aac','-b:a','128k','-movflags','+faststart',str(out)],stdin=subprocess.PIPE,stderr=subprocess.DEVNULL)
thumbs=[]
for sc,ov,d in SC:
    static=None
    for i in range(round(d*FPS)):
        t=i/FPS
        if sc=='s2' and t<0.4 or static is None:
            base=frame(sc,t); base.alpha_composite(ovl[ov]); static=base
        fr=static
        z=1+0.02*t/d
        if sc=='s3' and t<0.35:   # light shake + white flash
            dx=round(10*math.sin(t*90)); dy=round(8*math.cos(t*80))
            fr=Image.new('RGBA',(W,H),(255,255,255,255)); fr.alpha_composite(static,(dx,dy))
            if t<0.07: fr=Image.blend(fr,Image.new('RGBA',(W,H),(255,255,255,255)),0.6)
        else:
            cw,ch=round(W/z),round(H/z); fr=fr.crop(((W-cw)//2,(H-ch)//2,(W-cw)//2+cw,(H-ch)//2+ch)).resize((W,H),Image.BILINEAR)
        if i==min(9,round(d*FPS)-1): thumbs.append(fr.convert('RGB').resize((360,640)))
        p.stdin.write(fr.convert('RGB').tobytes())
p.stdin.close(); p.wait()
sheet=Image.new('RGB',(360*len(thumbs),640)); [sheet.paste(im,(360*k,0)) for k,im in enumerate(thumbs)]
sheet.save(str(out).replace('.mp4','-all-slides.jpg')); print('ok',sum(d for *_,d in SC))
