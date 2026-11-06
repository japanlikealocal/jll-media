# 1-page A4 flyer to hand to restaurants in person: "I make English menus".
# Usage: python3 build_shop_flyer.py  -> shop-flyer.pdf + shop-flyer.png
import pathlib, subprocess, base64
from playwright.sync_api import sync_playwright
H = pathlib.Path(__file__).resolve().parent
C = '#9E2B25'
subprocess.run(['pdftoppm', '-f', '1', '-l', '1', '-r', '110', '-png', '-singlefile',
                str(H / 'sample-english-menu.pdf'), '/tmp/_jll_menu_p1'], check=True)
IMG = base64.b64encode(pathlib.Path('/tmp/_jll_menu_p1.png').read_bytes()).decode()

HTML = f'''<!doctype html><html><head><meta charset=utf-8><style>
@page{{size:A4;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:"Noto Sans CJK JP",sans-serif;color:#2A211C;font-size:10.5pt;line-height:1.6;word-break:auto-phrase}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;background:#FBF6EE}}
.band{{height:8mm;background:{C}}}
.wrap{{padding:11mm 15mm 0}}
.kick{{color:{C};font-weight:700;letter-spacing:.12em;font-size:10.5pt}}
h1{{font-size:27pt;line-height:1.3;font-weight:900;margin:2mm 0 2mm}}
.lead{{font-size:11.5pt;color:#5A4D43}}
.ba{{display:grid;grid-template-columns:1fr 9mm 1.35fr;align-items:center;margin:7mm 0 6mm}}
.box{{background:#fff;border-radius:3mm;padding:4mm 5mm;border:1px solid #DCCFBF;height:100%}}
.box .lb{{font-size:8.5pt;font-weight:700;color:#8A7B6E;letter-spacing:.1em;margin-bottom:1.5mm}}
.before .nm{{font-size:15pt;font-weight:700}}
.after{{border:2px solid {C}}}
.after .lb{{color:{C}}}
.en{{font-size:13.5pt;font-weight:700;line-height:1.3}}
.ro{{font-size:9pt;color:#6A5D53}}
.ds{{font-size:9.6pt;margin-top:1mm}}
.pr{{font-weight:700;color:{C}}}
.arr{{text-align:center;font-size:20pt;color:{C};font-weight:900}}
.mid{{display:grid;grid-template-columns:1fr 62mm;gap:7mm}}
h2{{font-size:13pt;font-weight:900;margin:0 0 2mm;padding-left:3mm;border-left:2mm solid {C}}}
ul{{list-style:none;margin-bottom:5mm}}
li{{padding:1.4mm 0 1.4mm 5.5mm;position:relative;border-bottom:1px solid #E6DBCD}}
li:before{{content:"";position:absolute;left:0;top:3.4mm;width:2.4mm;height:2.4mm;background:{C};border-radius:50%}}
.thumb{{background:#fff;border:1px solid #DCCFBF;border-radius:2mm;padding:2mm;text-align:center}}
.thumb img{{width:100%;display:block}}
.thumb p{{font-size:8pt;color:#6A5D53;margin-top:1mm}}
.price{{background:{C};color:#fff;border-radius:4mm;padding:5mm 7mm;display:flex;align-items:center;justify-content:space-between;margin:2mm 0 5mm}}
.price .t{{font-size:10.5pt;font-weight:700}}
.price .t small{{display:block;font-weight:400;font-size:9pt;opacity:.92}}
.price .n{{font-size:28pt;font-weight:900;line-height:1}}
.price .n small{{font-size:11pt;font-weight:700}}
.price .o{{font-size:9.5pt;text-align:right;opacity:.92}}
.note{{font-size:8.8pt;color:#5A4D43;line-height:1.55}}
.note li{{border:none;padding:.4mm 0 .4mm 4mm}}
.note li:before{{width:1.6mm;height:1.6mm;top:2.2mm;background:#8A7B6E}}
.foot{{position:absolute;left:15mm;right:15mm;bottom:14mm;background:#fff;border:1.5px solid #2A211C;border-radius:3mm;padding:6mm 7mm;display:flex;justify-content:space-between;align-items:flex-end;font-size:11pt}}
.foot .ct{{display:inline-block;border-bottom:1px solid #2A211C;width:95mm;height:7mm;vertical-align:bottom}}
</style></head><body><section class=pg><div class=band></div><div class=wrap>
<div class=kick>飲食店さま向け</div>
<h1>外国人のお客さまに、<br>「何の料理か」伝わるメニューを。</h1>
<p class=lead>今の日本語メニューをもとに、英語メニュー（A4・2ページ／30品まで）をPDFで作ります。</p>

<div class=ba>
 <div class="box before"><div class=lb>今のメニュー</div><div class=nm>鶏の唐揚げ</div><div class=pr>680円</div></div>
 <div class=arr>→</div>
 <div class="box after"><div class=lb>英語メニュー</div>
  <div class=en>Japanese Fried Chicken <span class=pr>¥680</span></div>
  <div class=ro>Karaage・鶏の唐揚げ</div>
  <div class=ds>Crispy marinated chicken, served with lemon.</div></div>
</div>

<div class=mid><div>
 <h2>メニューに入るもの</h2>
 <ul>
  <li>英語の料理名＋ローマ字の読み＋日本語名<br><span class=ro>→ 外国人のお客さまが指さしで注文できます</span></li>
  <li>何の料理か分かる、英語の短い説明</li>
  <li>価格と「税込」の表記、お通し・支払い方法などの案内（ご希望の場合）</li>
  <li>アレルギー表示（お店で確認した内容だけ）</li>
 </ul>
 <h2>流れ</h2>
 <ul>
  <li>今のメニューの写真をいただく（手書きでもOK）</li>
  <li>4日以内に初稿 → 修正2回まで</li>
  <li>PDFでお渡し（お店のプリンターで印刷できます）</li>
 </ul>
</div>
<div class=thumb><img src="data:image/png;base64,{IMG}"><p>見本（架空の居酒屋）</p></div></div>

<div class=price><div class=t>11月30日までの特別価格<small>最初の3店舗さままで</small></div>
 <div class=n>3,000<small>円</small></div><div class=o>通常 5,000円<br>30品・修正2回込み</div></div>

<ul class=note>
 <li>翻訳とレイアウトにAI（Claude）を補助的に使い、品数・価格・内容は私が日本語メニューと照らし合わせて確認します。</li>
 <li>料理名・価格・アレルギー情報は、お店で確定したものをお知らせください。最終確認はお店でお願いします。</li>
 <li>ネイティブの校閲や認証翻訳ではありません。写真やイラストの作成は含みません。</li>
</ul>
</div>
<div class=foot><span>作成：ゼロ</span><span>ご連絡先：<span class=ct>&nbsp;</span></span></div>
</section></body></html>'''

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.set_content(HTML, wait_until='load')
    pg.pdf(path=str(H / 'shop-flyer.pdf'), format='A4', print_background=True)
    b.close()
subprocess.run(['pdftoppm', '-r', '110', '-png', '-singlefile', str(H / 'shop-flyer.pdf'), str(H / 'shop-flyer')], check=True)
print('ok')
