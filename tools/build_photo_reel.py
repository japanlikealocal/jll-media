# Photo-background reel prototype (Zero 11/25: "text tables all look the same").
# 3 slides, 1080x1920, real photo (Pexels, see assets/covers) + few big words. Usage: python3 tools/build_photo_reel.py resto
import pathlib, subprocess, sys
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; F=(R/'tools/fonts').as_uri()
J={'resto':dict(photo='assets/covers/px-31393431.jpg',accent='#F97316',out='reels/2026-11-proto-resto-photo.mp4',
  slides=[('WHAT STAFF ASK YOU · #2','Eating out<br>in Japan? 🍽️','Know these 3 phrases',None),
          ('THEY ASK','“Nanmei-sama<br>desu ka?”','How many people?','Say: Futari desu (two)'),
          ('THEY SAY','“Otōshi desu.”','A small starter + cover charge<br>(about ¥200–1,000 at izakaya)','Ask first: Otōshi wa ikura desu ka?'),
          ('THEY ASK','“Betsubetsu<br>desu ka?”','Paying separately?','Say: Issho de (together)'),
          ('SAVE IT FOR YOUR TRIP','➕ Follow for #3:<br>hotel check-in','💬 Comment JAPAN<br>for my free guide',None)])}
D=J[sys.argv[1] if sys.argv[1:] else 'resto']; P=(R/D['photo']).as_uri(); A=D['accent']
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;overflow:hidden;font-family:I,'Noto Color Emoji',sans-serif;color:#fff;position:relative}}
.bg{{position:absolute;inset:0;background:url({P}) center/cover}}.sh{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.1) 35%,rgba(0,0,0,.8) 75%,rgba(0,0,0,.9) 100%)}}
.c{{position:absolute;left:80px;right:80px;bottom:330px}}.t{{display:inline-block;background:{A};font-weight:800;font-size:34px;letter-spacing:3px;padding:10px 22px;border-radius:10px}}
.h{{font-weight:800;font-size:118px;line-height:1.02;margin-top:28px;text-shadow:0 6px 30px rgba(0,0,0,.6)}}.s{{font-weight:700;font-size:54px;line-height:1.2;margin-top:28px}}
.a{{display:inline-block;margin-top:34px;background:#fff;color:#111;font-weight:800;font-size:44px;padding:18px 30px;border-radius:50px}}'''
fr=[]
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for i,(t,h,s,a) in enumerate(D['slides']):
        html=f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=bg></div><div class=sh></div><div class=c><span class=t>{t}</span><div class=h>{h}</div><div class=s>{s}</div>{f"<div class=a>{a}</div>" if a else ""}</div></body></html>'
        tmp=R/'tools/_pr.html'; tmp.write_text(html); pg.goto(tmp.as_uri()); pg.wait_for_timeout(500)
        f=f'/tmp/pr{i}.png'; pg.screenshot(path=f); fr.append(f)
    b.close(); tmp.unlink()
# each slide 2.6s, 0.4s crossfade
dur=2.6; inp=[];
for f in fr: inp+=['-loop','1','-t',str(dur),'-i',f]
fc=''; last='[0]'
for i in range(1,len(fr)):
    off=round(i*(dur-0.4),2); fc+=f'{last}[{i}]xfade=transition=fade:duration=0.4:offset={off}[x{i}];'; last=f'[x{i}]'
fc+=f'{last}format=yuv420p,fps=30[v]'
tot=round(len(fr)*(dur-0.4)+0.4,2)
subprocess.run(['ffmpeg','-y',*inp,'-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-filter_complex',fc,'-map','[v]','-map',f'{len(fr)}:a','-t',str(tot),'-c:v','libx264','-crf','20','-c:a','aac','-movflags','+faststart',str(R/D['out'])],check=True,capture_output=True)
from PIL import Image
ims=[Image.open(f).resize((270,480)) for f in fr]; c=Image.new('RGB',(270*len(ims)+10*(len(ims)-1),480),'white')
for i,im in enumerate(ims): c.paste(im,(i*280,0))
c.save('/tmp/proto-resto.png'); print('ok',D['out'],tot,'s')
