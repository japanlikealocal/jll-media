import base64,subprocess
from playwright.sync_api import sync_playwright
CSS=open('/home/claude/reel2/make.py').read().split('CSS = """')[1].split('"""')[0]
BR='<div class="brand"><div class="jp">JP</div>Japan Like a Local</div>'
def b64(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
COVER=b64('trains_cover_src.png'); GATE=b64('trains_gate_src.png')
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
       ("Keep it quiet","Set your phone to silent, avoid calls, and keep your voice down.",None)]
pages=[f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}body{{background:url({COVER}) center/cover no-repeat}}{shade}</style></head><body><div class="shade"></div>{BR}<div class="safe ttop"><div class="tag">TRAINS</div><h1>First train ride in Japan?</h1><div class="sub">3 things to know 👇</div></div></body></html>']
for i,(t,d,bg) in enumerate(items,1):
  card=f'<div class="num">{i}</div><div class="t">{t}</div><div class="d">{d}</div>'
  pages.append(page(bg,f'<div class="safe bottom"><div class="card">{card}</div></div>') if bg else page(None,f'<div class="safe">{card}</div>'))
pages.append(page(None,'<div class="safe"><div class="tag">BEFORE YOU GO</div><h1 style="font-size:96px">Rules may vary by line and station.</h1><div class="cta">Save this for your trip!<br>Free 1-page<br>Japan Quick Start:<br>link in bio</div></div>'))
D=[3.0,5.0,4.5,4.5,4.0]
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
  for n,h in enumerate(pages):
    pg.set_content(h); pg.wait_for_timeout(200); pg.screenshot(path=f'trains_s{n}.png')
  b.close()
with open('trains_list.txt','w') as f:
  for i,x in enumerate(D): f.write(f"file 'trains_s{i}.png'\nduration {x}\n")
  f.write("file 'trains_s4.png'\n")
subprocess.run(['ffmpeg','-y','-f','concat','-safe','0','-i','trains_list.txt','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-t',str(sum(D)),'-vf','fps=30,format=yuv420p','-c:v','libx264','-profile:v','high','-crf','20','-g','60','-c:a','aac','-b:a','128k','-use_editlist','0','-movflags','+faststart','trains-reel-v1.mp4'],check=True,capture_output=True)
subprocess.run(['ffmpeg','-v','error','-y']+sum([['-i',f'trains_s{i}.png'] for i in range(5)],[])+['-filter_complex',''.join(f'[{i}]scale=432:-1[a{i}];' for i in range(5))+''.join(f'[a{i}]' for i in range(5))+'hstack=5','-frames:v','1','trains-reel-v1-all-slides.jpg'],check=True)
