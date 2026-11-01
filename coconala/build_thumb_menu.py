# Coconala service thumbnail (1220x1240). Shows the fictional sample pages. No AI illustrations/photos.
import pathlib, subprocess
from playwright.sync_api import sync_playwright
H = pathlib.Path(__file__).resolve().parent
subprocess.run(['pdftoppm', '-r', '110', '-png', str(H/'sample-english-menu.pdf'), str(H/'_mp')], check=True)
P1, P2 = (H/'_mp-1.png').as_uri(), (H/'_mp-2.png').as_uri()
C = '#9E2B25'
html = f'''<!doctype html><html lang=ja><head><meta charset=utf-8><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1220px;height:1240px;font-family:"Noto Sans CJK JP";color:#fff;position:relative;overflow:hidden;
background:radial-gradient(circle at 85% 10%,#E8483A 0,#C62828 35%,#8E1414 100%)}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.08) 2px,transparent 2px);background-size:34px 34px}}
.top{{position:relative;padding:58px 70px 0}}
.kick{{display:inline-block;background:#FFD43B;color:#7A1010;font-weight:900;font-size:36px;padding:10px 28px;border-radius:40px;transform:rotate(-2deg)}}
h1{{font-weight:900;font-size:92px;line-height:1.14;margin-top:22px;letter-spacing:.01em;text-shadow:0 6px 0 rgba(0,0,0,.18)}}
h1 em{{font-style:normal;color:#FFD43B}}
.ba{{position:absolute;left:70px;top:430px;display:flex;align-items:center;gap:18px}}
.chip{{background:#fff;color:#2B2622;border-radius:18px;padding:16px 24px;font-weight:900;font-size:38px;box-shadow:0 10px 24px rgba(0,0,0,.25)}}
.chip small{{display:block;font-size:22px;color:#8A8077;font-weight:700}}
.chip.en{{color:#B71C1C}}
.arrow{{font-size:56px;font-weight:900;color:#FFD43B}}
.pages{{position:absolute;left:40px;top:600px;width:720px;height:520px}}
.pg{{position:absolute;width:370px;box-shadow:0 22px 44px rgba(0,0,0,.4);border-radius:6px}}
.p1{{left:30px;top:10px;transform:rotate(-5deg)}} .p2{{left:320px;top:30px;transform:rotate(4deg)}}
.list{{position:absolute;right:60px;top:610px;width:360px;display:grid;gap:20px}}
.it{{background:#fff;color:#2B2622;border-radius:18px;padding:20px 24px;font-weight:900;font-size:36px;line-height:1.2;box-shadow:0 10px 24px rgba(0,0,0,.25)}}
.it small{{display:block;font-size:23px;color:#6B625A;font-weight:700;margin-top:4px}}
.it b{{color:#C62828}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:150px;background:#1E1412;display:flex;align-items:center;justify-content:center;gap:40px;font-weight:900;font-size:40px}}
.foot b{{color:#FFD43B;font-size:72px}}
.note{{position:absolute;right:60px;top:1030px;font-size:22px;color:rgba(255,255,255,.75)}}
</style></head><body><div class=dots></div>
<div class=top><span class=kick>🍺 外国人のお客様、増えてませんか？</span>
<h1>そのメニュー、<br><em>英語</em>で伝わる形に。</h1></div>
<div class=ba><div class=chip>唐揚げ<small>日本語メニュー</small></div><div class=arrow>→</div>
<div class=chip en>Japanese Fried Chicken<small>Karaage · 唐揚げ</small></div></div>
<div class=pages><img class="pg p1" src="{P1}"><img class="pg p2" src="{P2}"></div>
<div class=list><div class=it><b>30品</b>まで<small>A4・2ページのPDF</small></div>
<div class=it>修正<b>2回</b>込み<small>料理名＋短い説明つき</small></div>
<div class=it>初稿<b>4日</b>以内<small>アレルギーはお店確認分のみ</small></div></div>
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
