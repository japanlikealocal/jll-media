# Tax-free reel (10/23): photo background on every slide, short phrases (<=6 words), white text with shadow.
import pathlib,subprocess,glob,os
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent
F=(R/'tools/fonts').as_uri()
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:B;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;font-family:I,sans-serif;font-weight:800;position:relative;overflow:hidden;background:transparent}}
.g{{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.15),rgba(0,0,0,.35) 35%,rgba(0,0,0,.75) 80%)}}
.jp{{position:absolute;left:90px;top:300px;display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.94);border-radius:60px;padding:12px 28px 12px 14px;font-size:34px;color:#141B2D}}
.jp b{{width:56px;height:56px;border-radius:50%;background:#1F6FEB;color:#fff;display:flex;align-items:center;justify-content:center;font-size:24px}}
.box{{position:absolute;left:100px;right:190px;bottom:520px}}
.tag{{display:inline-block;background:#1F6FEB;color:#fff;font-size:48px;padding:12px 26px;border-radius:10px;margin-bottom:26px}}
.num{{width:130px;height:130px;border-radius:50%;background:#1F6FEB;color:#fff;font-size:76px;display:flex;align-items:center;justify-content:center;margin-bottom:30px}}
h1{{color:#fff;font-size:124px;line-height:.98;letter-spacing:-3px;text-shadow:0 4px 24px rgba(0,0,0,.75),0 0 3px #000}}
h1 em{{font-style:normal;color:#7FBFFF}}
.p{{color:#fff;font-family:B;font-weight:700;font-size:76px;line-height:1.18;margin-top:34px;text-shadow:0 3px 16px rgba(0,0,0,.85),0 0 3px #000}}
.p span{{display:block;margin-top:10px}}
.cta{{display:inline-block;background:#E3EEFF;color:#1F57B8;font-size:58px;line-height:1.2;padding:34px 40px;border-radius:24px;margin-top:36px}}
'''
def html(body): return f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=g></div><div class=jp><b>JP</b>Japan Like a Local</div>{body}</body></html>'
R0='assets/covers/px-12984979.jpg'; E='assets/covers/px-31409473-safe.jpg'; K='assets/covers/px-31393431.jpg'
S=[  # accent BLUE, bright first photo
 (R0,'center 45%','<div class=box><div class=tag>HUNGRY IN JAPAN?</div><h1>Order food <em>without Japanese</em></h1><div class=p>3 tips for your first meal</div></div>',3.0),
 (E,'center 60%','<div class=box><div class=num>1</div><h1>Wait to be seated</h1></div>',2.5),
 (E,'40% 70%','<div class=box><div class=p style="margin-top:0"><span>Staff may ask “How many?”</span><span>Hold up fingers.</span></div></div>',2.5),
 (K,'center center','<div class=box><div class=num>2</div><h1>Ticket machine?</h1></div>',2.5),
 (K,'35% center','<div class=box><div class=p style="margin-top:0"><span>Buy a ticket first.</span><span>Hand it to staff.</span></div></div>',2.5),
 (R0,'70% center','<div class=box><div class=num>3</div><h1>Point and ask</h1></div>',2.5),
 (R0,'30% 60%','<div class=box><div class=p style="margin-top:0"><span>Point at photos.</span><span>English menu?</span><span>“Eigo no menyuu wa arimasu ka?”</span></div></div>',3.0),
 (E,'center 50%','<div class=box><div class=p style="margin-top:0">No tipping. Rules vary by restaurant.</div><div class=cta>Save this for your trip!<br>Free 1-page<br>Japan Quick Start:<br>link in bio</div></div>',3.0),
]
D=[s[3] for s in S]
tmp=R/'tools/_fd.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for n,(ph,pos,body,_) in enumerate(S):
        tmp.write_text(html(body)); pg.goto(tmp.as_uri()); pg.wait_for_timeout(400); pg.screenshot(path=f'fd_o{n}.png',omit_background=True)
        tmp.write_text(f'<html><body style="margin:0;width:1080px;height:1920px;background:url({(R/ph).as_uri()}) {pos}/cover no-repeat"></body></html>'); pg.goto(tmp.as_uri()); pg.wait_for_timeout(400); pg.screenshot(path=f'fd_b{n}.png')
    b.close()
tmp.unlink()
ins=[];fc=''
for n,d in enumerate(D):
    ins+=['-loop','1','-t',str(d),'-i',f'fd_b{n}.png','-loop','1','-t',str(d),'-i',f'fd_o{n}.png']
    fr=int(d*30)
    fc+=f"[{2*n}]scale=2160:3840,zoompan=z='1+0.05*on/{fr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1080x1920:fps=30,setsar=1[b{n}];[{2*n+1}]fps=30,format=rgba[o{n}];[b{n}][o{n}]overlay=0:0:shortest=1,setsar=1[v{n}];"
fc+=''.join(f'[v{n}]' for n in range(len(D)))+f'concat=n={len(D)}:v=1:a=0,format=yuv420p[v]'
out='reels/2026-10-24-food-reel-v1-silent.mp4'
subprocess.run(['ffmpeg','-y']+ins+['-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-filter_complex',fc,'-map','[v]','-map',f'{2*len(D)}:a','-t',str(sum(D)),'-c:v','libx264','-profile:v','high','-crf','20','-g','60','-c:a','aac','-b:a','128k','-movflags','+faststart',out],check=True,capture_output=True)
T=[0.1]+[sum(D[:k])+0.4 for k in range(1,len(D))]
for k,t in enumerate(T): subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',out,'-frames:v','1',f'fd_p{k}.png'],check=True)
subprocess.run(['ffmpeg','-v','error','-y']+sum([['-i',f'fd_p{k}.png'] for k in range(len(T))],[])+['-filter_complex',''.join(f'[{k}]scale=432:-1[a{k}];' for k in range(len(T)))+''.join(f'[a{k}]' for k in range(len(T)))+f'hstack={len(T)}','-frames:v','1',out.replace('.mp4','-all-slides.jpg')],check=True)
for f in glob.glob('fd_*.png'): os.remove(f)
print('ok',sum(D))
