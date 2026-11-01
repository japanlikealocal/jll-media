# Coconala service thumbnail (1220x1240). Shows the fictional sample pages. No AI illustrations/photos.
import pathlib, subprocess
from playwright.sync_api import sync_playwright
H = pathlib.Path(__file__).resolve().parent
subprocess.run(['pdftoppm', '-r', '110', '-png', str(H/'sample-english-menu.pdf'), str(H/'_mp')], check=True)
P1, P2 = (H/'_mp-1.png').as_uri(), (H/'_mp-2.png').as_uri()
C = '#9E2B25'
html = f'''<!doctype html><html lang=ja><head><meta charset=utf-8><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1220px;height:1240px;background:#FBF7F1;font-family:"Noto Sans CJK JP";color:#2B2622;position:relative;overflow:hidden}}
.top{{padding:64px 70px 0}}
.kick{{display:inline-block;background:{C};color:#fff;font-weight:700;font-size:34px;padding:10px 26px;border-radius:12px}}
h1{{font-weight:900;font-size:86px;line-height:1.18;margin-top:26px;letter-spacing:.01em}}
h1 em{{font-style:normal;color:{C}}}
.pages{{position:absolute;left:70px;right:70px;top:470px;height:560px}}
.pg{{position:absolute;width:396px;box-shadow:0 18px 40px rgba(60,30,10,.22);border:1px solid #E5DBCF}}
.p1{{left:40px;top:10px;transform:rotate(-4deg)}} .p2{{left:330px;top:40px;transform:rotate(3deg)}}
.list{{position:absolute;right:70px;top:500px;width:330px;display:grid;gap:22px}}
.it{{background:#fff;border-left:12px solid {C};border-radius:14px;padding:20px 22px;font-weight:700;font-size:34px;line-height:1.25}}
.it small{{display:block;font-size:24px;color:#6B625A;font-weight:500;margin-top:4px}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:150px;background:#2B2622;color:#fff;display:flex;align-items:center;justify-content:center;gap:40px;font-weight:700;font-size:40px}}
.foot b{{color:#FFD43B;font-size:64px}}
.note{{position:absolute;right:70px;top:440px;font-size:22px;color:#8A8077}}
</style></head><body>
<div class=top><span class=kick>訪日のお客様に伝わる</span>
<h1>日本語メニューを<br><em>英語メニュー</em>にします</h1></div>
<div class=pages><img class="pg p1" src="{P1}"><img class="pg p2" src="{P2}"></div>
<div class=list><div class=it>A4・2ページ<small>30品まで・PDF納品</small></div>
<div class=it>修正2回込み<small>料理名＋短い説明</small></div>
<div class=it>初稿4日以内<small>アレルギーはお店確認の情報のみ</small></div></div>
<div class=note>※画像は架空の制作見本です</div>
<div class=foot><span>居酒屋・食堂・カフェに</span><b>5,000円</b></div>
</body></html>'''
tmp = H/'_thumbm.html'; tmp.write_text(html, encoding='utf-8')
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={'width':1220,'height':1240})
    pg.goto(tmp.as_uri()); pg.wait_for_timeout(500); pg.screenshot(path=str(H/'thumb-menu.png')); b.close()
tmp.unlink()
for f in H.glob('_mp-*.png'): f.unlink()
print('ok thumb-menu.png')
