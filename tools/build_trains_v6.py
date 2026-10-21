import base64,subprocess
from playwright.sync_api import sync_playwright
CSS=open('/home/claude/jll-media/tools/reel.css').read()
BR='<div class="brand"><div class="jp">JP</div>Japan Like a Local</div>'
def b64(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
A='/home/claude/jll-media/assets/'
COVER=b64(A+'trains-1-cover.png'); GATE=b64(A+'trains-2-gate.png'); INSIDE=b64(A+'trains-3-interior.png')
X='''.card{background:rgba(247,243,236,.94);border-radius:36px;padding:56px 56px 60px;box-shadow:0 12px 40px rgba(0,0,0,.18)}
.safe.bottom{justify-content:flex-end}
.brandbox{position:absolute;top:130px;left:70px;background:rgba(247,243,236,.92);border-radius:60px;padding:14px 30px 14px 20px}
.brandbox .brand{position:static}
.t{font-size:80px}.d{font-size:50px}.num{width:120px;height:120px;font-size:68px;margin-bottom:36px}'''
def page(bg,inner,shade=''):
  bgcss=f'body{{background:url({bg}) center/cover no-repeat}}' if bg else ''
  return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{X}{bgcss}{shade}</style></head><body>{"<div class=brandbox>"+BR+"</div>" if bg else BR}{inner}</body></html>'
shade='.shade{position:absolute;left:0;right:0;top:0;height:1050px;background:linear-gradient(rgba(247,243,236,.85),rgba(247,243,236,.55) 70%,rgba(247,243,236,0))}.safe.ttop{justify-content:flex-start;padding-top:60px}'
items=[("Tap in &amp; tap out","Tap your IC card (Suica, PASMO, etc.) on the reader when you enter and when you exit.",GATE),
       ("Line up, let people off","Line up where marked, and let people off first.",COVER),
       ("Keep it quiet","Set your phone to silent, avoid calls, and keep your voice down.",INSIDE)]
hook='.hook{position:absolute;left:0;right:0;top:330px;background:rgba(20,27,45,.82);padding:52px 90px 58px;color:#fff;font-size:118px;font-weight:800;line-height:1.02;letter-spacing:-2px}'
pages=[f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}html,body{{background:transparent!important}}{hook}.hook small{{display:block;font-size:56px;font-weight:700;color:#ffd6d6;letter-spacing:0;margin-top:22px}}</style></head><body><div class="brandbox" style="position:absolute;top:130px;left:70px;background:rgba(247,243,236,.92);border-radius:60px;padding:14px 30px 14px 20px">{BR.replace('class="brand"','class="brand" style="position:static"')}</div><div class="hook">First train<br>ride in Japan?<small>3 rules to know 👇</small></div></body></html>']
for i,(t,d,bg) in enumerate(items,1):
  card=f'<div class="num">{i}</div><div class="t">{t}</div><div class="d">{d}</div>'
  pages.append(page(bg,f'<div class="safe bottom"><div class="card">{card}</div></div>') if bg else page(None,f'<div class="safe">{card}</div>'))
pages.append(page(None,'<div class="safe"><div class="tag">FREE PDF · 1 PAGE</div><h1 style="font-size:92px">Money, trains, manners &amp; 6 phrases on one page.</h1><div class="cta" style="font-size:72px;background:#D62828;color:#fff;margin-top:50px">👉 Free guide:<br>link in bio</div><div class="sub" style="margin-top:36px;font-size:40px">Rules may vary by line and station. Send this to your travel buddy 👋</div></div>'))
D=[3.0,5.0,4.5,4.5,4.0]
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
  for n,h in enumerate(pages):
    pg.set_content(h); pg.wait_for_timeout(200); pg.screenshot(path=f'trains_s{n}.png',omit_background=(n==0))
  pg.set_content(f'<html><body style="margin:0;width:1080px;height:1920px;background:url({COVER}) center/cover no-repeat"></body></html>'); pg.wait_for_timeout(200); pg.screenshot(path='trains_bg0.png')
  b.close()
Z=1
with open('trains_list.txt','w') as f:
  for i,x in enumerate(D): f.write(f"file 'trains_s{i}.png'\nduration {x}\n")
  f.write("file 'trains_s4.png'\n")
ins=[]
for n,d in enumerate(D): ins+=['-loop','1','-t',str(d),'-i',f'trains_s{n}.png']
import sys; sys.path.insert(0,'tools'); from build_cover import cover
cover('assets/covers/px-29058311-shinkansen.jpg','28% center','FIRST TRAIN RIDE?','3 train mistakes <em>to avoid</em>','Avoid them on your first day in Japan.','trains_s0.png',overlay_only=True)
import shutil; shutil.move('trains_s0-bg.png','trains_bg0.png')
ins+=['-loop','1','-t',str(D[0]),'-i','trains_bg0.png']
fr=int(D[0]*30)
fc=(f"[{len(D)}]scale=2160:3840,zoompan=z='1+0.06*on/{fr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1080x1920:fps=30,setsar=1[bg];[0]fps=30,format=rgba[ov];[bg][ov]overlay=0:0:shortest=1,setsar=1[v0];"
    +''.join(f"[{n}]fps=30,scale=1080:1920,setsar=1[v{n}];" for n in range(1,len(D)))
    +''.join(f"[v{n}]" for n in range(len(D)))+f"concat=n={len(D)}:v=1:a=0,format=yuv420p[v]")
subprocess.run(['ffmpeg','-y']+ins+['-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-filter_complex',fc,'-map','[v]','-map',f'{len(D)+1}:a','-t',str(sum(D)),'-c:v','libx264','-profile:v','high','-crf','20','-g','60','-c:a','aac','-b:a','128k','-movflags','+faststart','reels/trains-reel-v6-silent.mp4'],check=True,capture_output=True)
T=[0.1]+[sum(D[:k])+0.3 for k in range(1,len(D))]
for k,t in enumerate(T): subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i','reels/trains-reel-v6-silent.mp4','-frames:v','1',f'prev{k}.png'],check=True)
subprocess.run(['ffmpeg','-v','error','-y']+sum([['-i',f'prev{k}.png'] for k in range(len(T))],[])+['-filter_complex',''.join(f'[{k}]scale=432:-1[a{k}];' for k in range(len(T)))+''.join(f'[a{k}]' for k in range(len(T)))+f'hstack={len(T)}','-frames:v','1','reels/trains-reel-v6-silent-all-slides.jpg'],check=True)
import glob,os
for f in glob.glob('prev*.png')+glob.glob('trains_s*.png')+['trains_bg0.png','trains_list.txt']:
  if os.path.exists(f): os.remove(f)
