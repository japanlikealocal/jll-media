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
cut={k:L(E/f'cut-{k}.png') for k in ['sit-eat','sit-hehe','sit-hatpop','sit-dizzy','sam-before','sam-after']}
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
.bub{{position:absolute;background:#fff;border:6px solid #141B2D;border-radius:40px;padding:18px 34px;font-size:76px;color:#141B2D;letter-spacing:-2px}}
.bub:after{{content:'';position:absolute;left:70px;bottom:-34px;border:18px solid transparent;border-top:22px solid #141B2D}}
.bach{{position:absolute;width:560px;height:360px;display:flex;align-items:center;justify-content:center;font-size:100px;color:#fff;-webkit-text-stroke:6px #141B2D;letter-spacing:-3px;background:#FF4D4D;clip-path:polygon(50% 0,60% 22%,84% 6%,78% 32%,100% 38%,80% 56%,96% 80%,68% 72%,58% 100%,46% 76%,20% 96%,24% 68%,0 62%,20% 46%,4% 20%,32% 28%);transform:rotate(-8deg)}}
'''
JP='<div class=jp><b>JP</b>Japan Like a Local</div>'
DOOR_X=round((941-340)*K)  # door centre after flip ≈ 690
BLOCK=f'''<svg width=1080 height=1920><path d="M{DOOR_X} 1240 C {DOOR_X+40} 1300, {DOOR_X+190} 1420, {DOOR_X+200} 1760" stroke="#fff" stroke-width="16" stroke-dasharray="34 22" fill="none" stroke-linecap="round" opacity=".95"/>
<circle cx="{DOOR_X+150}" cy="1150" r="62" fill="#E5383B" stroke="#fff" stroke-width="8"/><path d="M{DOOR_X+124} 1124 l52 52 M{DOOR_X+176} 1124 l-52 52" stroke="#fff" stroke-width="14" stroke-linecap="round"/></svg>'''
SPEED='''<svg width=1080 height=1920><g stroke="#141B2D" stroke-width="10" stroke-linecap="round" fill="none" opacity=".85">
<path d="M470 700 Q 560 760 600 900"/><path d="M420 740 Q 520 800 560 940"/><path d="M520 660 Q 610 720 650 860"/></g></svg>'''
CHECK='<svg width=1080 height=1920><circle cx="900" cy="1000" r="62" fill="#2BAE66" stroke="#fff" stroke-width="8"/><path d="M870 1002 l22 22 l40 -44" stroke="#fff" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
OV={
 'hook':JP+'<div class=box><h1>POV: you found<br>the perfect<br><em>snack spot</em></h1></div>',
 'hookx':JP+'<div class=box><h1>…right in front<br>of <em>the door.</em></h1></div>'+BLOCK,
 'none':JP,
 'bro':JP+'<div class=bub style="left:70px;top:560px">Bro.</div>',
 'bach':JP+SPEED+'<div class=bach style="left:500px;top:640px">BACHIN!</div>',
 'door':JP+'<div class=bub style="left:40px;top:560px">That’s the door.</div>',
 'bench':JP+'<div class=box><h1>Bench <em>&gt;</em> doorway</h1></div>'+CHECK,
 'end':JP+'<div class=box><h1>Keep shop<br>entrances <em>clear.</em></h1><div class=p style="margin-top:22px">Sumimasen! = Sorry</div></div>',
}
ovl={}; tmp=R/'tools/_e3.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':W,'height':H})
    for k,body in OV.items():
        tmp.write_text(f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>')
        pg.goto(tmp.as_uri()); pg.wait_for_timeout(300); p=R/f'tools/_ov3_{k}.png'; pg.screenshot(path=str(p),omit_background=True); ovl[k]=L(p); p.unlink()
    b.close()
tmp.unlink()
Z=2.2; BZ=BG0.resize((round(BG0.width*K*Z),round(BG0.height*K*Z)),Image.LANCZOS)
OFFY=round(1250-880*K*Z); BZc=Image.new('RGBA',(W,H)); BZc.alpha_composite(BZ,(0,OFFY))
s2=0.49; bench_eat=cut['sit-eat'].resize((round(cut['sit-eat'].width*s2/s),round(cut['sit-eat'].height*s2/s)),Image.LANCZOS)
def shiba(fr,k,t=0):
    sit_shadow(fr,XS); im=cut[k]
    if k=='sit-dizzy':   # wobble around the seat
        a=4*math.sin(t*14); im=im.rotate(a,resample=Image.BICUBIC,center=(470*s,1300*s))
    fr.alpha_composite(im,(XS,YS))
def frame(sc,t):
    if sc=='bench':
        fr=BZc.copy(); x0=round(305-450*s2); y0=round(1250-1300*s2)
        shadow(fr,305,1262,380,60); fr.alpha_composite(bench_eat,(x0,y0)); return fr
    fr=BG.copy()
    if sc in('s1','s1x'): shiba(fr,'sit-eat')
    elif sc=='s2':
        shiba(fr,'sit-eat'); x=XM+round(-640*max(0,1-t/0.3)**2); sam_shadow(fr,x); fr.alpha_composite(cut['sam-before'],(x,YM))
    elif sc=='wind':
        shiba(fr,'sit-eat'); sam_shadow(fr,XM); fr.alpha_composite(cut['sam-after'],(XM,YM))
    elif sc=='hit':
        shiba(fr,'sit-dizzy',t); sam_shadow(fr,XM); fr.alpha_composite(cut['sam-after'],(XM,YM))
    elif sc=='door':
        shiba(fr,'sit-hehe'); x=XM-90; sam_shadow(fr,x); fr.alpha_composite(cut['sam-before'],(x,YM))
    elif sc=='end':
        a=fit(old['samurai-A-bow'],760); c=fit(old['shiba-4-bow'],700)
        shadow(fr,90+a.width/2,GROUND-6,a.width*0.8); fr.alpha_composite(a,(90,GROUND-a.height))
        shadow(fr,600+c.width/2,GROUND-6,c.width*0.8); fr.alpha_composite(c,(600,GROUND-c.height))
    return fr
SC=[('s1','hook',1.5),('s1x','hookx',1.0),('s2','bro',0.9),('wind','none',0.2),('hit','bach',1.2),('door','door',1.4),('bench','bench',1.8),('end','end',2.4)]
out=R/'reels/2026-10-25-samurai-ep1-sitting-v3-silent.mp4'
p=subprocess.Popen(['ffmpeg','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-f','lavfi','-i','anullsrc=r=44100:cl=stereo',
  '-shortest','-c:v','libx264','-profile:v','high','-crf','20','-pix_fmt','yuv420p','-g','60','-c:a','aac','-b:a','128k','-movflags','+faststart',str(out)],stdin=subprocess.PIPE,stderr=subprocess.DEVNULL)
thumbs=[]
for sc,ov,d in SC:
    static=None; n=round(d*FPS)
    for i in range(n):
        t=i/FPS
        if static is None or (sc=='s2' and t<0.35) or sc=='hit':
            base=frame(sc,t)
            if not(sc=='s2' and t<0.3): base.alpha_composite(ovl[ov])
            else: base.alpha_composite(ovl['none'])
            static=base
        fr=static
        if sc=='hit' and t<0.4:
            dx=round(16*math.sin(t*95)); dy=round(12*math.cos(t*85))
            f2=Image.new('RGBA',(W,H),(255,255,255,255)); f2.alpha_composite(static,(dx,dy)); fr=f2
            if t<0.07: fr=Image.blend(fr,Image.new('RGBA',(W,H),(255,255,255,255)),0.7)
        else:
            z=1+0.02*t/d; cw,ch=round(W/z),round(H/z); fr=fr.crop(((W-cw)//2,(H-ch)//2,(W-cw)//2+cw,(H-ch)//2+ch)).resize((W,H),Image.BILINEAR)
        if i==min(10,n-1): thumbs.append(fr.convert('RGB').resize((360,640)))
        p.stdin.write(fr.convert('RGB').tobytes())
p.stdin.close(); p.wait()
sheet=Image.new('RGB',(360*len(thumbs),640)); [sheet.paste(im,(360*k,0)) for k,im in enumerate(thumbs)]
sheet.save(str(out).replace('.mp4','-all-slides.jpg')); print('ok',sum(d for *_,d in SC))
