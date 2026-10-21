# New reel cover: vivid photo + benefit hook. Text kept inside the 3:4 grid crop (y 240-1680) and above the view counter.
import sys,pathlib
from playwright.sync_api import sync_playwright
ROOT=pathlib.Path(__file__).resolve().parent.parent
F=(ROOT/'tools/fonts').as_uri()
def cover(photo,pos,tag,big,small,out,overlay_only=False):
    img=(ROOT/photo).as_uri()
    html=f'''<!doctype html><html><head><meta charset=utf-8><style>
@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:R;src:url({F}/Inter-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:{'transparent' if overlay_only else f'url({img}) {pos}/cover no-repeat'};font-family:I,sans-serif;font-weight:800;position:relative;overflow:hidden}}
.g{{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.0) 30%,rgba(0,0,0,.72) 72%,rgba(0,0,0,.3))}}
.jp{{position:absolute;left:90px;top:300px;display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.94);border-radius:60px;padding:12px 28px 12px 14px;font-size:34px;color:#141B2D}}
.jp b{{width:56px;height:56px;border-radius:50%;background:#D62828;color:#fff;display:flex;align-items:center;justify-content:center;font-size:24px}}
.tag{{position:absolute;left:90px;top:860px;background:#FFD43B;color:#141B2D;font-size:48px;padding:12px 26px;border-radius:10px}}
h1{{position:absolute;left:84px;right:70px;top:950px;color:#fff;font-size:132px;line-height:.98;letter-spacing:-3px;text-shadow:0 6px 30px rgba(0,0,0,.6)}}
h1 em{{font-style:normal;color:#FF5A4E}}
.s{{position:absolute;left:90px;right:90px;top:1400px;color:#fff;font-family:R;font-weight:700;font-size:46px;line-height:1.25;text-shadow:0 3px 14px rgba(0,0,0,.7)}}
</style></head><body><div class=g></div><div class=jp><b>JP</b>Japan Like a Local</div><div class=tag>{tag}</div><h1>{big}</h1><div class=s>{small}</div></body></html>'''
    p=ROOT/'tools/_cover.html'; p.write_text(html)
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920}); pg.goto(p.as_uri()); pg.wait_for_timeout(600)
        pg.screenshot(path=str(ROOT/out),omit_background=overlay_only)
        if overlay_only:
            p.write_text(f'<html><body style="margin:0;width:1080px;height:1920px;background:url({img}) {pos}/cover no-repeat"></body></html>'); pg.goto(p.as_uri()); pg.wait_for_timeout(500); pg.screenshot(path=str(ROOT/out).replace('.png','-bg.png'))
        b.close()
    p.unlink()
if __name__=='__main__':
    cover('assets/covers/px-31130296-osaka.jpg','center 40%','NEW FROM NOV 1','Don’t lose your <em>tax refund</em>','Shopping in Japan? 3 new rules to get your money back.','assets/covers/cover-taxfree.png')
    cover('assets/covers/px-29058311-shinkansen.jpg','28% center','FIRST TRAIN RIDE?','3 train mistakes <em>to avoid</em>','Avoid them on your first day in Japan.','assets/covers/cover-trains.png')
