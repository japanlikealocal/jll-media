# Samurai x Shiba ep.2 (onsen): swimsuit -> BACHIN!, towel in water -> BACHIN!!, towel on head = correct.
import pathlib,subprocess,math
from PIL import Image,ImageDraw,ImageFilter
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; E1=R/'assets/ep1'; E=R/'assets/ep2'
W,H,FPS=1080,1920,30
F=(R/'tools/fonts').as_uri(); ACC='#7B3FE4'
def L(p): return Image.open(p).convert('RGBA')
B0=L(E/'bg-onsen.png'); K=W/B0.width; BG=B0.resize((W,round(B0.height*K)),Image.LANCZOS).crop((0,0,W,H))
GROUND=1580; s=0.62; SB=0.8; WL=1015; WATER_Y=1062   # canvas waterline in bath images -> screen y
def sc(im,f=s): return im.resize((round(im.width*f),round(im.height*f)),Image.LANCZOS)
cut={k:sc(L(E/f'cut-{k}.png')) for k in ['shiba-swim','shiba-swim-dizzy']}
for k in ['shiba-bath-towel','shiba-bath-happy']:
    im=L(E/f'cut-{k}.png'); a=im.getchannel('A'); d=ImageDraw.Draw(a); d.rectangle([0,WL,im.width,im.height],fill=0); im.putalpha(a); cut[k]=sc(im,SB)
sam={k:sc(L(E1/f'cut-{k}.png')) for k in ['sam-before','sam-after']}
old={k:L(R/f'assets/cutouts/{k}.png') for k in ['samurai-C-thumbsup']}
def fit(im,h): return im.resize((round(im.width*h/im.height),h),Image.LANCZOS)
XS,YS=400,round(GROUND-1430*s)        # standing shiba origin
XB,YB=380,round(WATER_Y-WL*SB)          # bathing shiba origin
XM,YM=-20,round(GROUND-1450*s)        # samurai origin
def shadow(fr,cx,y,w,a=80):
    sh=Image.new('RGBA',(W,H)); ImageDraw.Draw(sh).ellipse([cx-w/2,y-w*0.09,cx+w/2,y+w*0.09],fill=(90,70,50,a)); fr.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
def ripples(fr,t):
    lay=Image.new('RGBA',(W,H)); d=ImageDraw.Draw(lay); cx=XB+470*SB
    for k,(w,h,a) in enumerate([(560,46,170),(700,64,110),(840,84,60)]):
        w2=w+18*math.sin(t*4+k); d.ellipse([cx-w2/2,WATER_Y-h/2,cx+w2/2,WATER_Y+h/2],outline=(255,255,255,a),width=6)
    fr.alpha_composite(lay.filter(ImageFilter.GaussianBlur(1.2)))
def swirl_eyes(fr):   # draw dizzy eyes over the towel image eyes (canvas coords)
    lay=Image.new('RGBA',(W,H)); d=ImageDraw.Draw(lay)
    for ex,ey in [(365,612),(565,620)]:
        x=XB+ex*SB; y=YB+ey*SB; r=44; d.ellipse([x-r,y-r,x+r,y+r],fill=(255,250,240,255))
        pts=[(x+ (2+i*0.7)*math.cos(i*0.35), y+(2+i*0.7)*math.sin(i*0.35)) for i in range(0,56)]
        d.line(pts,fill=(70,40,25,255),width=6)
    for k,(dx,dy) in enumerate([(-140,-250),(0,-300),(140,-250)]):
        x=XB+470*SB+dx; y=YB+330*SB+dy; R5=[(x+ (26 if j%2==0 else 11)*math.cos(math.pi/2+j*math.pi/5), y-(26 if j%2==0 else 11)*math.sin(math.pi/2+j*math.pi/5)) for j in range(10)]
        d.polygon(R5,fill=(255,210,40,255),outline=(120,80,20,255))
    fr.alpha_composite(lay)
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:B;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;font-family:I;font-weight:800;position:relative;overflow:hidden;background:transparent}}
.jp{{position:absolute;left:70px;top:150px;display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.95);border-radius:60px;padding:10px 26px 10px 12px;font-size:32px;color:#141B2D}}
.jp b{{width:52px;height:52px;border-radius:50%;background:{ACC};color:#fff;display:flex;align-items:center;justify-content:center;font-size:22px}}
.box{{position:absolute;left:70px;right:70px;top:236px}}
h1{{color:#141B2D;font-size:96px;line-height:1;letter-spacing:-3px;text-shadow:0 0 22px rgba(255,255,255,.95),0 0 6px rgba(255,255,255,.9)}}
h1 em{{font-style:normal;color:{ACC}}}
.p{{background:rgba(255,255,255,.93);border-radius:22px;padding:20px 28px;color:#141B2D;font-family:B;font-weight:700;font-size:54px;line-height:1.2;display:inline-block}}
.q{{display:inline-block;background:{ACC};color:#fff;font-size:58px;padding:22px 34px;border-radius:24px;margin-top:20px}}
.bub{{position:absolute;background:#fff;border:6px solid #141B2D;border-radius:40px;padding:18px 34px;font-size:76px;color:#141B2D;letter-spacing:-2px;white-space:nowrap}}
.bub:after{{content:'';position:absolute;left:70px;bottom:-34px;border:18px solid transparent;border-top:22px solid #141B2D}}
.bub.r:after{{left:auto;right:80px}}
.bach{{position:absolute;display:flex;align-items:center;justify-content:center;color:#fff;-webkit-text-stroke:6px #141B2D;letter-spacing:-3px;background:#FF4D4D;
 clip-path:polygon(50% 0,60% 22%,84% 6%,78% 32%,100% 38%,80% 56%,96% 80%,68% 72%,58% 100%,46% 76%,20% 96%,24% 68%,0 62%,20% 46%,4% 20%,32% 28%)}}
svg{{position:absolute;inset:0}}
'''
JP='<div class=jp><b>JP</b>Japan Like a Local</div>'
SPEED='''<svg width=1080 height=1920><g stroke="#141B2D" stroke-width="10" stroke-linecap="round" fill="none" opacity=".85"><path d="M470 700 Q 560 760 600 900"/><path d="M420 740 Q 520 800 560 940"/><path d="M520 660 Q 610 720 650 860"/></g></svg>'''
OV={
 'hook':JP+'<div class=box><h1>POV: your<br><em>first onsen</em></h1></div>',
 'none':JP,
 'bro':JP+'<div class=bub style="left:70px;top:560px">Bro.</div>',
 'bach':JP+SPEED+'<div class=bach style="left:500px;top:600px;width:560px;height:360px;font-size:100px;transform:rotate(-8deg)">BACHIN!</div>',
 'wash':JP+'<div class=bub r style="left:430px;top:300px">Laundry time~</div>',
 'bro2':JP+'<div class=bub style="left:70px;top:560px">…Bro.</div>',
 'bach2':JP+SPEED+'<div class=bach style="left:300px;top:250px;width:640px;height:420px;font-size:116px;transform:rotate(7deg)">BACHIN!!</div>',
 'good':JP+'<div class=box><h1>Towel on<br>your <em>head.</em></h1></div>',
 'end':JP+'<div class=box><div class=p>No swimsuits.<br>Wash before you soak.<br>Towel stays out of the water.</div><br><div class=q>Would you try it?</div></div>',
}
ovl={}; tmp=R/'tools/_e2.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':W,'height':H})
    for k,body in OV.items():
        tmp.write_text(f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body.replace("class=bub r","class=\'bub r\'")}</body></html>')
        pg.goto(tmp.as_uri()); pg.wait_for_timeout(300); p=R/f'tools/_ov2_{k}.png'; pg.screenshot(path=str(p),omit_background=True); ovl[k]=L(p); p.unlink()
    b.close()
tmp.unlink()
def slide_x(t): return XM+round(-640*max(0,1-t/0.3)**2)
def frame(scn,t):
    fr=BG.copy()
    if scn in('s1','s2','wind','hit'):
        k='shiba-swim-dizzy' if scn=='hit' else 'shiba-swim'; im=cut[k]
        if scn=='hit': im=im.rotate(4*math.sin(t*14),resample=Image.BICUBIC,center=(470*s,1430*s))
        shadow(fr,XS+470*s,GROUND-10,520); fr.alpha_composite(im,(XS,YS))
        if scn!='s1':
            x=slide_x(t) if scn=='s2' else XM; shadow(fr,x+370*s,GROUND-8,400)
            fr.alpha_composite(sam['sam-after' if scn in('wind','hit') else 'sam-before'],(x,YM))
    else:
        k='shiba-bath-happy' if scn in('good','end') else 'shiba-bath-towel'
        fr.alpha_composite(cut[k],(XB,YB)); ripples(fr,t)
        if scn=='hit2': swirl_eyes(fr)
        if scn in('bro2','wind2','hit2'):
            x=(slide_x(t) if scn=='bro2' else XM)-60; shadow(fr,x+370*s,GROUND-8,400)
            fr.alpha_composite(sam['sam-after' if scn in('wind2','hit2') else 'sam-before'],(x,YM))
        if scn=='good':
            a=fit(old['samurai-C-thumbsup'],720); shadow(fr,40+a.width/2,GROUND-6,a.width*0.8); fr.alpha_composite(a,(40,GROUND-a.height))
    return fr
SC=[('s1','hook',1.6),('s2','bro',0.8),('wind','none',0.2),('hit','bach',1.1),('wash','wash',1.8),('bro2','bro2',0.8),('wind2','none',0.15),('hit2','bach2',1.3),('good','good',1.8),('end','end',2.8)]
out=R/'reels/2026-10-26-samurai-ep2-onsen-v1-silent.mp4'
p=subprocess.Popen(['ffmpeg','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-f','lavfi','-i','anullsrc=r=44100:cl=stereo',
  '-shortest','-c:v','libx264','-profile:v','high','-crf','20','-pix_fmt','yuv420p','-g','60','-c:a','aac','-b:a','128k','-movflags','+faststart',str(out)],stdin=subprocess.PIPE,stderr=subprocess.DEVNULL)
thumbs=[]; animated={'hit','hit2','wash','good','end'}
for scn,ov,d in SC:
    static=None; n=round(d*FPS)
    for i in range(n):
        t=i/FPS
        if static is None or scn in animated or (scn in('s2','bro2') and t<0.35):
            base=frame(scn,t); base.alpha_composite(ovl['none'] if scn in('s2','bro2') and t<0.3 else ovl[ov]); static=base
        fr=static; strong=scn=='hit2'
        if scn in('hit','hit2') and t<0.45:
            A=24 if strong else 16; dx=round(A*math.sin(t*95)); dy=round(A*0.75*math.cos(t*85))
            f2=Image.new('RGBA',(W,H),(255,255,255,255)); f2.alpha_composite(static,(dx,dy)); fr=f2
            if t<0.08: fr=Image.blend(fr,Image.new('RGBA',(W,H),(255,255,255,255)),0.7)
        else:
            z=1+0.02*t/d; cw,ch=round(W/z),round(H/z); fr=fr.crop(((W-cw)//2,(H-ch)//2,(W-cw)//2+cw,(H-ch)//2+ch)).resize((W,H),Image.BILINEAR)
        if i==min(12,n-1): thumbs.append(fr.convert('RGB').resize((360,640)))
        p.stdin.write(fr.convert('RGB').tobytes())
p.stdin.close(); p.wait()
sheet=Image.new('RGB',(360*len(thumbs),640)); [sheet.paste(im,(360*k,0)) for k,im in enumerate(thumbs)]
sheet.save(str(out).replace('.mp4','-all-slides.jpg')); print('ok',sum(d for *_,d in SC))
