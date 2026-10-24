# Samurai x Shiba ep.1 (10/24): "Don't sit outside shops". Cutout characters on a blurred Osaka shop-street photo.
import pathlib,subprocess,glob,os
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent
F=(R/'tools/fonts').as_uri(); C=(R/'assets/cutouts').as_uri()
BG=(R/'assets/covers/px-31130296-osaka-safe.jpg').as_uri()
ACC='#7B3FE4'  # purple (rotation red->blue->green->purple)
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:B;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;font-family:I,sans-serif;font-weight:800;position:relative;overflow:hidden;background:#222}}
.bg{{position:absolute;inset:-30px;background:url({BG}) center 55%/cover;filter:BLUR brightness(.8)}}
.g{{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,.15) 40%,rgba(0,0,0,0) 60%,rgba(0,0,0,.35))}}
.jp{{position:absolute;left:90px;top:210px;display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.94);border-radius:60px;padding:12px 28px 12px 14px;font-size:34px;color:#141B2D}}
.jp b{{width:56px;height:56px;border-radius:50%;background:{ACC};color:#fff;display:flex;align-items:center;justify-content:center;font-size:24px}}
.box{{position:absolute;left:90px;right:90px;top:330px}}
.tag{{display:inline-block;background:{ACC};color:#fff;font-size:46px;padding:12px 26px;border-radius:10px;margin-bottom:22px}}
h1{{color:#fff;font-size:108px;line-height:1;letter-spacing:-3px;text-shadow:0 4px 24px rgba(0,0,0,.8),0 0 3px #000}}
h1 em{{font-style:normal;color:#C9A8FF}}
.p{{color:#fff;font-family:B;font-weight:700;font-size:68px;line-height:1.18;text-shadow:0 3px 16px rgba(0,0,0,.9),0 0 3px #000}}
.p span{{display:block;margin-top:8px}}
.c{{position:absolute;bottom:330px;filter:drop-shadow(0 18px 24px rgba(0,0,0,.45))}}
.pon{{position:absolute;left:560px;top:520px;width:470px;height:320px;display:flex;align-items:center;justify-content:center;font-size:92px;color:#fff;letter-spacing:-1px;padding-right:10px;
 background:#FFC83D;clip-path:polygon(50% 0,60% 22%,84% 6%,78% 32%,100% 38%,80% 56%,96% 80%,68% 72%,58% 100%,46% 76%,20% 96%,24% 68%,0 62%,20% 46%,4% 20%,32% 28%);-webkit-text-stroke:6px #141B2D;transform:rotate(8deg)}}
.cta{{display:inline-block;background:#F1E8FF;color:#5A24B8;font-size:56px;line-height:1.2;padding:30px 38px;border-radius:24px;margin-top:30px}}
'''
def ch(name,h,left,flip=False):
    t='transform:scaleX(-1);' if flip else ''
    return f'<img class=c src="{C}/{name}.png" style="height:{h}px;left:{left}px;{t}">'
SAM_L=lambda n,h=1000:ch('samurai-'+n,h,40)
def SHI(n,h=900,left=560): return ch('shiba-'+n,h,left)
S=[ # (blur, html, duration, shake)
 ('blur(2px)', '<div class=box><div class=tag>JAPAN TRAVEL TIP</div><h1>Sitting outside <em>shops?</em></h1></div>'+ch('shiba-6-sit-onigiri',760,160),3.0,0),
 ('blur(6px)', '<div class=box><h1>Wait a sec…</h1></div>'+SAM_L('B-shocked',1000)+SHI('6-sit-onigiri',620,520),2.0,0),
 ('blur(6px)', SAM_L('E-swing',1000)+SHI('6-sit-onigiri',620,520),1.0,0),
 ('blur(6px)', ch('shiba-2-hat-pop',1100,150)+'<div class=pon>PON!</div>',1.6,1),
 ('blur(6px)', '<div class=box><div class=p><span>Sitting by a shop door</span><span>blocks the entrance</span><span>and the street.</span></div></div>'+SAM_L('D-laugh',900)+SHI('3-hehe',880,560),3.2,0),
 ('blur(6px)', '<div class=box><div class=tag>DO THIS</div><div class=p><span>Eat inside if</span><span>there’s seating,</span><span>or find a bench.</span></div></div>'+SAM_L('base-wink',840)+SHI('3-hehe',880,560),3.2,0),
 ('blur(6px)', '<div class=box><h1>“Sumimasen!”</h1><div class=p style="margin-top:20px">= Excuse me / Sorry</div></div>'+ch('samurai-A-bow',900,90)+SHI('4-bow',860,580),2.6,0),
 ('blur(8px)', '<div class=box><div class=p>Save this for your trip!</div><div class=cta>Free 1-page<br>Japan Quick Start:<br>link in bio</div></div>'+SAM_L('C-thumbsup',880)+SHI('5-thumbsup',860,560),3.2,0),
]
tmp=R/'tools/_s1.html'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for n,(bl,body,_,_) in enumerate(S):
        tmp.write_text(f'<!doctype html><html><head><meta charset=utf-8><style>{CSS.replace("BLUR",bl)}</style></head><body><div class=bg></div><div class=g></div><div class=jp><b>JP</b>Japan Like a Local</div>{body}</body></html>')
        pg.goto(tmp.as_uri()); pg.wait_for_timeout(500); pg.screenshot(path=f's1_{n}.png')
    b.close()
tmp.unlink()
D=[s[2] for s in S]; ins=[]; fc=''
for n,(_,_,d,sh) in enumerate(S):
    ins+=(['-loop','1','-t',str(d)] if sh else [])+['-i',f's1_{n}.png']; fr=int(d*30)
    if sh: fc+=f"[{n}]fps=30,scale=1140:2027,crop=1080:1920:'30+18*sin(t*70)':'53+14*cos(t*63)',fade=in:st=0:d=0.12:color=white,setsar=1[v{n}];"
    else: fc+=f"[{n}]scale=2160:3840,zoompan=z='1+0.03*on/{fr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1080x1920:fps=30,setsar=1[v{n}];"
fc+=''.join(f'[v{n}]' for n in range(len(S)))+f'concat=n={len(S)}:v=1:a=0,format=yuv420p[v]'
out='reels/2026-10-25-samurai-ep1-sitting-v1-silent.mp4'
subprocess.run(['ffmpeg','-y']+ins+['-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-filter_complex',fc,'-map','[v]','-map',f'{len(S)}:a','-t',str(sum(D)),'-c:v','libx264','-profile:v','high','-crf','20','-g','60','-c:a','aac','-b:a','128k','-movflags','+faststart',out],check=True,capture_output=True)
T=[0.1]+[sum(D[:k])+0.3 for k in range(1,len(D))]
for k,t in enumerate(T): subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',out,'-frames:v','1',f's1_p{k}.png'],check=True)
subprocess.run(['ffmpeg','-v','error','-y']+sum([['-i',f's1_p{k}.png'] for k in range(len(T))],[])+['-filter_complex',''.join(f'[{k}]scale=360:-1[a{k}];' for k in range(len(T)))+''.join(f'[a{k}]' for k in range(len(T)))+f'hstack={len(T)}','-frames:v','1',out.replace('.mp4','-all-slides.jpg')],check=True)
for f in glob.glob('s1_*.png'): os.remove(f)
print('ok',sum(D))
