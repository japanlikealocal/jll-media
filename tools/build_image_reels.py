# Turn 4:5 image posts into ~10s silent reels (image posts get ~0 reach at 0 followers; reels get ~100).
import pathlib,subprocess,sys
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; F=(R/'tools/fonts').as_uri()
JOBS=[('compare-japan-uk','Visiting Japan<br>from the UK? 🇬🇧','reels/2026-10-26-japan-vs-uk-reel.mp4'),
      ('ig-free-tokyo-views-v2','Why pay ¥2,000<br>for a view?','reels/2026-10-27-free-views-reel.mp4'),
      ('ig-tokyo-illuminations','Tokyo lights up<br>this winter ✨','reels/2026-10-28-illuminations-reel.mp4')]
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:I;background:transparent}}
.t{{position:absolute;left:60px;right:60px;top:70px;height:160px;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff;font-size:68px;line-height:1.02;letter-spacing:-2px;text-shadow:0 4px 18px rgba(0,0,0,.7)}}
.b{{position:absolute;left:0;right:0;bottom:236px;text-align:center}}
.b span{{display:inline-block;background:#fff;color:#141B2D;font-size:40px;padding:16px 30px;border-radius:40px}}'''
with sync_playwright() as pw:
    br=pw.chromium.launch(); pg=br.new_page(viewport={'width':1080,'height':1920})
    for img,hook,out in JOBS:
        src=R/f'assets/{img}.png'; tmp=R/'tools/_ir.html'
        tmp.write_text(f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=t>{hook}</div><div class=b><span>📌 Save it · 💬 Comment JAPAN for a free guide</span></div></body></html>')
        pg.goto(tmp.as_uri()); pg.wait_for_timeout(400); ov=R/'tools/_ir_ov.png'; pg.screenshot(path=str(ov),omit_background=True); tmp.unlink()
        # bg: blurred, darkened image filling 1080x1920; fg: image 1080 wide, slow zoom
        fc=("[0]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3,eq=brightness=-0.18[bg];"
            "[0]scale=2160:-1,zoompan=z='1+0.05*on/300':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=300:s=1080x1350:fps=30[fg];"
            "[bg]fps=30,loop=300:1:0[bgl];[bgl][fg]overlay=0:240:shortest=1[v1];[v1][1]overlay=0:0,format=yuv420p[v]")
        subprocess.run(['ffmpeg','-y','-loop','1','-t','10','-i',str(src),'-loop','1','-t','10','-i',str(ov),'-f','lavfi','-i','anullsrc=r=44100:cl=stereo',
            '-filter_complex',fc,'-map','[v]','-map','2:a','-t','10','-c:v','libx264','-profile:v','high','-crf','19','-g','60','-c:a','aac','-b:a','128k','-movflags','+faststart',str(R/out)],check=True,capture_output=True)
        subprocess.run(['ffmpeg','-v','error','-y','-ss','0.2','-i',str(R/out),'-frames:v','1','-vf','scale=360:-1',str(R/out).replace('.mp4','-f0.jpg')],check=True)
        ov.unlink(); print('ok',out)
    br.close()
