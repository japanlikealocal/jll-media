# Carpenter's pre-handover checklist reel (Zero's own job: interior finish carpenter for new condos).
# Facts: items = Zero's stated common punch-list items (2026-11-03). Buyer walkthrough -> fix -> re-check, and
# wallpaper-vs-paint (qualitative) per docs/research-housing-japan-vs-west-2026-11-03.md. No AI images.
import pathlib,subprocess
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; OUT=R/'assets/carpenter-checks'; REEL=R/'reels/2026-11-06-carpenter-checks-reel.mp4'
S=[ # (kicker, title, body, icon)
 ('POV: your Japanese apartment','I’m a carpenter for new apartments in Japan.','Here’s what gets checked<br>before you get the keys.','🔑'),
 ('Check 1','The door','It has to close smoothly.<br>No rubbing. No drifting open.','🚪'),
 ('Check 2','The gaps','Even lines all around<br>the door and frame.','📏'),
 ('Check 3','The squeaks','Floors, walls, ceilings.<br>If it creaks, we fix it.','👂'),
 ('Check 4','The shoe closet','Adjustable shelves<br>can’t wobble. Not even a little.','👟'),
 ('Check 5','The window trim','Every screw in place.<br>Miss one, and I’m coming back.','🔩'),
 ('Then','The buyer walks through','They list anything off.<br>We fix it. They check again.','📝'),
 ('Bonus','Wallpaper, not paint','Most Japanese homes have<br>wallpaper on the walls.<br>Next time, look closely.','🏠'),
 ('Now you know','That’s why it feels so neat.','💬 Comment JAPAN<br>for my free 1-page Japan guide','🇯🇵'),
]
CSS='''*{box-sizing:border-box}body{margin:0;width:1080px;height:1920px;font-family:Inter,"Noto Sans CJK JP",sans-serif;
background:linear-gradient(160deg,#2a1d14,#4a3222 55%,#6b4a2f);color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 90px;position:relative}
.grain{position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.025) 0 3px,transparent 3px 22px)}
.ic{font-size:210px;margin-bottom:40px}.k{font-size:46px;font-weight:700;color:#f2c14e;letter-spacing:2px;text-transform:uppercase}
.t{font-size:104px;font-weight:800;line-height:1.05;margin:22px 0 40px}.b{font-size:60px;line-height:1.3;color:#f3e7d6}
.n{position:absolute;top:120px;left:90px;font-size:38px;font-weight:700;opacity:.8}
.f{position:absolute;bottom:150px;left:90px;right:90px;font-size:34px;opacity:.75;display:flex;justify-content:space-between}'''
OUT.mkdir(parents=True,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1920})
    for i,(k,t,bd,ic) in enumerate(S):
        pg.set_content(f'<style>{CSS}</style><div class=grain></div><div class=n>A carpenter’s checklist 🔨</div><div class=ic>{ic}</div><div class=k>{k}</div><div class=t>{t}</div><div class=b>{bd}</div><div class=f><span>Japan Like a Local</span><span>{i+1}/{len(S)}</span></div>')
        pg.wait_for_timeout(150); pg.screenshot(path=str(OUT/f'c{i+1:02d}.png'))
    b.close()
D=[3.2]+[2.8]*(len(S)-2)+[3.6]; ins=[]; parts=[]
for i,d in enumerate(D):
    ins+=['-i',str(OUT/f'c{i+1:02d}.png')]  # single frame; zoompan d= makes the duration
    parts.append(f"[{i}]scale=1080:1920,zoompan=z='1+0.02*on/{int(d*30)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(d*30)}:s=1080x1920:fps=30,format=yuv420p,setsar=1[v{i}]")
n=len(D); fc=';'.join(parts)+';'+''.join(f'[v{i}]' for i in range(n))+f'concat=n={n}:v=1:a=0[v]'
subprocess.run(['ffmpeg','-y',*ins,'-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-filter_complex',fc,'-map','[v]','-map',f'{n}:a','-t',str(sum(D)),
 '-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-movflags','+faststart',str(REEL)],check=True,capture_output=True)
print('ok',REEL.name,sum(D))
