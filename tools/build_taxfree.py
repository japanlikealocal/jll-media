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
.jp b{{width:56px;height:56px;border-radius:50%;background:#D62828;color:#fff;display:flex;align-items:center;justify-content:center;font-size:24px}}
.box{{position:absolute;left:90px;right:190px;bottom:520px}}
.tag{{display:inline-block;background:#FFD43B;color:#141B2D;font-size:48px;padding:12px 26px;border-radius:10px;margin-bottom:26px}}
.num{{width:130px;height:130px;border-radius:50%;background:#D62828;color:#fff;font-size:76px;display:flex;align-items:center;justify-content:center;margin-bottom:30px}}
h1{{color:#fff;font-size:124px;line-height:.98;letter-spacing:-3px;text-shadow:0 4px 24px rgba(0,0,0,.75),0 0 3px #000}}
h1 em{{font-style:normal;color:#FF5A4E}}
.p{{color:#fff;font-family:B;font-weight:700;font-size:64px;line-height:1.18;margin-top:34px;text-shadow:0 3px 16px rgba(0,0,0,.85),0 0 3px #000}}
.p span{{display:block;margin-top:10px}}
.cta{{display:inline-block;background:#fbe1e1;color:#D62828;font-size:58px;line-height:1.2;padding:34px 40px;border-radius:24px;margin-top:36px}}
'''
def html(body): return f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=g></div><div class=jp><b>JP</b>Japan Like a Local</div>{body}</body></html>'
S=[  # (photo, css position, body, seconds)
 ('assets/covers/px-31130296-osaka.jpg','center 40%','<div class=box><div class=tag>NEW FROM NOV 1</div><h1>Don’t lose your <em>tax refund</em></h1><div class=p>How to shop tax-free in Japan</div></div>',3.0),
 ('assets/covers/px-3907161.jpg','center center','<div class=box><div class=num>1</div><h1>Pay the full price</h1><div class=p><span>Tax included at the shop.</span><span>Tax back after you leave.</span></div></div>',4.5),
 ('assets/covers/px-6726195.jpg','center center','<div class=box><div class=num>2</div><h1>Check first, then bags</h1><div class=p><span>Leave within 90 days.</span><span>Do the tax-free check</span><span>before checking in bags.</span></div></div>',4.5),
 ('assets/covers/px-5868730.jpg','center center','<div class=box><div class=num>3</div><h1>Keep every item</h1><div class=p><span>One item missing?</span><span>No refund for that receipt.</span></div></div>',4.0),
 ('assets/covers/px-31130296-osaka.jpg','center 70%','<div class=box><div class=p style="margin-top:0">Rules may vary by airport.</div><div class=cta>Save this for your trip!<br>Free 1-page<br>Japan Quick Start:<br>link in bio</div></div>',4.0),
]
D=[s[3] for s in S]
tmp=R/'tools/_tf.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for n,(ph,pos,body,_) in enumerate(S):
        tmp.write_text(html(body)); pg.goto(tmp.as_uri()); pg.wait_for_timeout(400); pg.screenshot(path=f'tf_o{n}.png',omit_background=True)
        tmp.write_text(f'<html><body style="margin:0;width:1080px;height:1920px;background:url({(R/ph).as_uri()}) {pos}/cover no-repeat"></body></html>'); pg.goto(tmp.as_uri()); pg.wait_for_timeout(400); pg.screenshot(path=f'tf_b{n}.png')
    b.close()
tmp.unlink()
ins=[];fc=''
for n,d in enumerate(D):
    ins+=['-loop','1','-t',str(d),'-i',f'tf_b{n}.png','-loop','1','-t',str(d),'-i',f'tf_o{n}.png']
    fr=int(d*30)
    fc+=f"[{2*n}]scale=2160:3840,zoompan=z='1+0.05*on/{fr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1080x1920:fps=30,setsar=1[b{n}];[{2*n+1}]fps=30,format=rgba[o{n}];[b{n}][o{n}]overlay=0:0:shortest=1,setsar=1[v{n}];"
fc+=''.join(f'[v{n}]' for n in range(len(D)))+f'concat=n={len(D)}:v=1:a=0,format=yuv420p[v]'
out='reels/2026-10-23-taxfree-reel-v1-silent.mp4'
subprocess.run(['ffmpeg','-y']+ins+['-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-filter_complex',fc,'-map','[v]','-map',f'{2*len(D)}:a','-t',str(sum(D)),'-c:v','libx264','-profile:v','high','-crf','20','-g','60','-c:a','aac','-b:a','128k','-movflags','+faststart',out],check=True,capture_output=True)
T=[0.1]+[sum(D[:k])+0.5 for k in range(1,len(D))]
for k,t in enumerate(T): subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',out,'-frames:v','1',f'tf_p{k}.png'],check=True)
subprocess.run(['ffmpeg','-v','error','-y']+sum([['-i',f'tf_p{k}.png'] for k in range(len(T))],[])+['-filter_complex',''.join(f'[{k}]scale=432:-1[a{k}];' for k in range(len(T)))+''.join(f'[a{k}]' for k in range(len(T)))+f'hstack={len(T)}','-frames:v','1',out.replace('.mp4','-all-slides.jpg')],check=True)
for f in glob.glob('tf_*.png'): os.remove(f)
print('ok',sum(D))
