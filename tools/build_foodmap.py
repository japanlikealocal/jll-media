# Paid product: Tokyo food map PDF (48 spots: gyoza, unagi, ramen, yakitori).
# Data: docs/foodmap-data-2026-11-03.json (extracted from docs/*-sources-*.md, checked Oct 29 – Nov 2, 2026).
# Rules: only facts from the sources docs; unverified (user-posted / review) prices are dropped; no AI food images.
import json, pathlib, html, urllib.parse
from playwright.sync_api import sync_playwright
R = pathlib.Path(__file__).resolve().parent.parent
D = json.load(open(R / 'docs/foodmap-data-2026-11-03.json'))
OUT = R / 'products/tokyo-food-map-v1-2026-11.pdf'
SRC_OUT = R / 'products/tokyo-food-map-v1-sources.md'

CAT = {
 'gyoza':   ('Gyoza',   '餃子',   '#c2410c', 'Oct 29, 2026'),
 'unagi':   ('Unagi',   'うなぎ', '#7c4a1e', 'Nov 1, 2026'),
 'ramen':   ('Ramen',   'ラーメン', '#b91c1c', 'Nov 1, 2026'),
 'yakitori':('Yakitori','焼き鳥', '#a16207', 'Nov 2, 2026'),
}
BAD = ('user-posted', 'user listing', 'review', 'may be outdated', 'reference value')

def clean_price(x):
    p = x['price'] or ''
    parts = [s.strip() for s in p.replace('; ', ';').split(';')]
    keep = [s for s in parts if not any(b in s.lower() for b in BAD)]
    if len(keep) != len(parts) or not keep:
        base = p.split('.')[0] if any(b in p.lower() for b in BAD) else p
        base = base.split(' Unaju from')[0].split(' Tsukemen from')[0]
        keep = [s for s in keep if s] or []
        txt = '; '.join(keep) if keep else ''
        if not txt or any(b in txt.lower() for b in BAD):
            txt = {'Nodaiwa': 'Classic unaju (Michelin-listed). Price not confirmed — check on arrival.',
                   'Rokurinsha': 'Tsukemen (dipping noodles). Price not confirmed — check the ticket machine.',
                   'Hyotanya': 'Unadon in the ¥1,000s (Gurunavi listing). Check other prices on arrival.'}.get(x['name_en'], 'Check prices on arrival.')
        return txt
    return p

def clean_notes(x):
    n = x.get('notes') or ''
    if x['name_en'] == 'Nodaiwa': n = ''
    return n

AREA = [
 ('Shinjuku & west', ['Shinjuku', 'Nishi-Shinjuku', 'Yoyogi', 'Kichijoji', 'Komae']),
 ('Ginza, Tokyo Station & Nihombashi', ['Ginza', 'Higashi-Ginza', 'Yurakucho', 'Kyobashi', 'Tokyo Sta', 'Mitsukoshimae', 'Shin-Nihombashi', 'Toranomon']),
 ('Asakusa, Ueno & east', ['Asakusa', 'Ueno', 'Uguisudani', 'Kameido', 'Kinshicho', 'Morishita', 'Yotsugi']),
 ('Shibuya, Ebisu & south', ['Shibuya', 'Ebisu', 'Naka-Meguro', 'Sangenjaya', 'Gaiemmae', 'Azabu', 'Akasaka', 'Akabanebashi', 'Kamata']),
 ('Ikebukuro & north', ['Ikebukuro', 'Otsuka', 'Akabane', 'Iidabashi', 'Edogawabashi']),
]
def area_of(st):
    for a, keys in AREA:
        if any(st.startswith(k) for k in keys): return a
    return 'Other'

def maps(x):
    return 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote(x['name_ja'].split('（')[0])

def pay_tag(p):
    pl = p.lower()
    if pl.startswith('cash or qr'): return ('CASH / QR', '#b45309')
    if 'transit ic cards ok' in pl and 'credit' not in pl and 'visa' not in pl: return ('CASH / IC CARD', '#b45309')
    if 'cards only' in pl or 'cashless only' in pl: return ('CARD / PHONE ONLY', '#1d4ed8')
    if 'cash only' in pl: return ('CASH ONLY', '#b91c1c')
    if 'cards ok' in pl or 'cards and e-money ok' in pl: return ('CARDS OK', '#15803d')
    if 'bring cash' in pl: return ('CASH ONLY', '#b91c1c')
    return ('PAYMENT: CHECK', '#6b7280')

e = html.escape
def card(i, x):
    t, col = pay_tag(x['payment'])
    hrs = ' · '.join(s for s in [x.get('hours') or '', ('Closed: ' + x['closed']) if x.get('closed') else ''] if s)
    en = x['english_menu'] or 'Unknown'
    notes = clean_notes(x)
    return f'''<div class="card"><div class="top"><span class="no">{i}</span><div class="nm">{e(x['name_en'])}</div><span class="pt" style="background:{col}">{t}</span></div>
<div class="ja">{e(x['name_ja'])}</div>
<div class="st">🚉 {e(x['station'])} &nbsp; <a href="{maps(x)}">📍 Open in Google Maps</a></div>
<table>
<tr><th>Eat</th><td>{e(clean_price(x))}</td></tr>
<tr><th>Pay</th><td>{e(x['payment'])}</td></tr>
<tr><th>Book</th><td>{e(x['booking'])}</td></tr>
<tr><th>English menu</th><td>{e(en)}</td></tr>
{f'<tr><th>Hours</th><td>{e(hrs)}</td></tr>' if hrs else ''}
{f'<tr><th>Tip</th><td>{e(notes)}</td></tr>' if notes else ''}
</table></div>'''

CSS = '''@page{size:A4;margin:0}*{box-sizing:border-box}
body{margin:0;font-family:Inter,"Noto Sans CJK JP",sans-serif;color:#1f1a17;font-size:11.5px}
.pg{width:210mm;height:297mm;padding:14mm 13mm 12mm;position:relative;page-break-after:always;background:#fffdf8;overflow:hidden}
.ft{position:absolute;bottom:6mm;left:13mm;right:13mm;font-size:9px;color:#8a7f74;display:flex;justify-content:space-between}
h1{font-size:40px;line-height:1.05;margin:0}h2{font-size:24px;margin:0 0 4mm}h3{font-size:15px;margin:5mm 0 2mm}
.cover{background:#1f1a17;color:#fff;display:flex;flex-direction:column;justify-content:center}
.cover .k{color:#f2c14e;font-weight:700;letter-spacing:2px;font-size:14px}
.cover .chips span{display:inline-block;border:1.5px solid #f2c14e;color:#f2c14e;border-radius:20px;padding:4px 12px;margin:0 6px 6px 0;font-weight:700;font-size:13px}
.cover p{font-size:15px;line-height:1.5;color:#efe6d8;max-width:150mm}
.sec{border-radius:8px;color:#fff;padding:3mm 5mm;margin-bottom:4mm;display:flex;justify-content:space-between;align-items:baseline}
.sec b{font-size:22px}.sec span{font-family:"Noto Sans CJK JP";font-size:16px}
.card{border:1px solid #e3d8c8;border-radius:8px;padding:3mm 4mm;margin-bottom:3.2mm;background:#fff;break-inside:avoid}
.top{display:flex;align-items:center;gap:3mm}.no{background:#1f1a17;color:#fff;border-radius:50%;width:7mm;height:7mm;display:inline-flex;align-items:center;justify-content:center;font-weight:700;font-size:11px;flex:none}
.nm{font-weight:800;font-size:15px;flex:1}.pt{color:#fff;font-weight:700;font-size:9px;border-radius:4px;padding:2px 6px;white-space:nowrap}
.ja{font-family:"Noto Sans CJK JP";font-weight:700;font-size:19px;margin:1.2mm 0 .6mm}
.st{font-size:10.5px;color:#5b5047;margin-bottom:1.5mm}.st a{color:#1d4ed8;text-decoration:none;font-weight:600}
table{border-collapse:collapse;width:100%}th{text-align:left;vertical-align:top;width:24mm;color:#7a6d60;font-weight:600;font-size:10px;padding:.6mm 0}td{font-size:10.5px;padding:.6mm 0;line-height:1.35}
.box{background:#f6efe3;border-radius:8px;padding:4mm 5mm;margin-bottom:4mm;line-height:1.5;font-size:12px}
.box b{color:#7a1f16}
.ph{display:grid;grid-template-columns:1fr 1fr;gap:3mm}.ph div{background:#fff;border:1px solid #e3d8c8;border-radius:8px;padding:3mm 4mm}
.ph .j{font-family:"Noto Sans CJK JP";font-size:20px;font-weight:700}.ph .r{color:#7a1f16;font-weight:700}.ph .m{font-size:10.5px;color:#5b5047}
ul{margin:1mm 0 0 5mm;padding:0}li{margin-bottom:1mm}
.idx td,.idx th{font-size:9.5px;padding:.35mm 1mm;border-bottom:1px solid #eee3d3}.idx th{width:auto;color:#1f1a17}
'''

def page(inner, n, cls=''):
    return f'<div class="pg {cls}">{inner}<div class="ft"><span>Tokyo Food Map · 48 local spots · Japan Like a Local</span><span>{n}</span></div></div>'

pages = []
pages.append(f'''<div class="pg cover"><div class="k">JAPAN LIKE A LOCAL · TOKYO FOOD MAP</div>
<h1 style="margin:6mm 0">48 Tokyo food spots<br>you can actually walk into</h1>
<div class="chips"><span>12 Gyoza</span><span>12 Ramen</span><span>12 Unagi</span><span>12 Yakitori</span></div>
<p>For every spot: the Japanese name to show staff, nearest station, what to order, <b>cash or card</b>, <b>booking rules</b>, English menu, opening days — plus a one-tap Google Maps link.</p>
<p>Facts checked against official and store pages, Oct 29 – Nov 2, 2026.</p></div>''')

pages.append(page('''<h2>How to use this guide</h2>
<div class="box"><b>1. Pick a spot near where you are.</b> Use the area index on the next page, or browse by food.<br>
<b>2. Check the Pay and Book lines first.</b> Many small shops in Tokyo take cash only, and some popular ramen shops only work with timed tickets or online booking.<br>
<b>3. Tap “Open in Google Maps”.</b> It searches the shop’s Japanese name, so you land on the right branch.<br>
<b>4. At the door, point to the Japanese name.</b> Staff can read it instantly.</div>
<h3>Reading each card</h3>
<div class="box"><b>CASH ONLY</b> — bring yen. <b>CARD / PHONE ONLY</b> — the shop does not take cash. <b>CARDS OK</b> — at least some cards accepted (brands listed).<br>
<b>English menu</b> — “Yes” means the shop or its listing says it has one. “Online only” means we found an English menu online but could not confirm one in the shop. “Unknown” means we could not confirm either way — it does not mean there is none.<br>
<b>Unknown</b> anywhere means the information was not published. We never guessed.</div>
<h3>Good to know</h3>
<div class="box">• Prices are the ones published by the shop or its listing when we checked. “Tax included” is only written where the source said so.<br>
• Some izakaya-style shops add a small table charge (<i>otoshi</i>) per person. Where the shop lists one, it is on the card.<br>
• Shops change hours, prices and payment without notice. Check the shop’s page or Google Maps on the day, especially for closing days marked “confirm”.<br>
• This guide was researched with the help of AI tools, then checked against the shops’ official and listing pages by me. It is independent: no shop paid to be included.</div>''', 2))

# area index
rows = {}
num = {}
k = 0
for c in CAT:
    for x in [y for y in D if y['category'] == c]:
        k += 1; num[id(x)] = k
        rows.setdefault(area_of(x['station']), []).append((k, x))
idx = ''
for a, _ in AREA + [('Other', [])]:
    if a not in rows: continue
    idx += f'<h3 style="margin:3mm 0 1mm;font-size:13px">{a}</h3><table class="idx">' + ''.join(f'<tr><td style="width:8mm"><b>{n}</b></td><td style="width:42mm">{e(x["name_en"])}</td><td style="width:22mm">{CAT[x["category"]][0]}</td><td>{e(x["station"])}</td><td style="width:30mm">{pay_tag(x["payment"])[0].title()}</td></tr>' for n, x in rows[a]) + '</table>'
pages.append(page('<h2>Find food near you</h2>' + idx, 3))

pn = 4
for c, (en, ja, col, date) in CAT.items():
    xs = [y for y in D if y['category'] == c]
    for j in range(0, 12, 3):
        head = f'<div class="sec" style="background:{col}"><b>{en} {"" if j==0 else "(cont.)"}</b><span>{ja} · checked {date}</span></div>'
        if j == 0:
            tip = {
             'gyoza': 'Gyoza come pan-fried (<i>yaki</i>), boiled (<i>sui</i>) or steamed. Many old-school shops are cash only and do not take bookings — go early.',
             'unagi': 'Unaju = grilled eel on rice in a lacquered box; unadon = in a bowl. Grades (e.g. Ume / Take / Matsu) usually mean more eel. Many top shops take bookings — use them.',
             'ramen': 'Many ramen shops use a ticket machine: pay first, hand the ticket to staff. Some famous shops only seat you with a timed ticket or online booking — check the Book line.',
             'yakitori': 'Order by the skewer or as a set. Salt (<i>shio</i>) or sauce (<i>tare</i>) is your choice. Izakaya-style places may add a table charge (<i>otoshi</i>).'}[c]
            head += f'<div class="box" style="font-size:11px;padding:3mm 4mm">{tip}</div>'
        pages.append(page(head + ''.join(card(num[id(x)], x) for x in xs[j:j+3]), pn))
        pn += 1

pages.append(page('''<h2>Point-and-say phrases</h2>
<div class="ph">
<div><div class="j">２人です</div><div class="r">Futari desu</div><div class="m">“Two people.” Hold up fingers for your group size.</div></div>
<div><div class="j">これをください</div><div class="r">Kore o kudasai</div><div class="m">“This one, please.” Point at the menu.</div></div>
<div><div class="j">カードは使えますか？</div><div class="r">Kādo wa tsukaemasu ka?</div><div class="m">“Can I use a card?” Ask before you sit down.</div></div>
<div><div class="j">お会計お願いします</div><div class="r">Okaikei onegaishimasu</div><div class="m">“The bill, please.”</div></div>
<div><div class="j">予約しています</div><div class="r">Yoyaku shite imasu</div><div class="m">“I have a reservation.” Show the booking on your phone.</div></div>
<div><div class="j">英語のメニューはありますか？</div><div class="r">Eigo no menyū wa arimasu ka?</div><div class="m">“Do you have an English menu?”</div></div>
<div><div class="j">ごちそうさまでした</div><div class="r">Gochisōsama deshita</div><div class="m">“Thank you for the meal.” Say it on the way out.</div></div>
<div><div class="j">アレルギーがあります</div><div class="r">Arerugī ga arimasu</div><div class="m">“I have an allergy.” Then show the ingredient written in Japanese.</div></div>
</div>
<h3>Before you go</h3>
<div class="box">• Carry some yen cash every day — several spots in this guide take cash only.<br>• No tipping in Japan. Just pay the bill.<br>• Queues are normal at popular shops. Line up quietly and wait to be called.<br>• Allergy information is not given in this guide. Always ask the shop directly.</div>
<h3>Updates</h3><div class="box">Version 1 · facts checked Oct 29 – Nov 2, 2026. Each card’s facts come from the shop’s official page or its restaurant listing (sources list included with your download).</div>
<p style="font-size:14px;font-weight:700;margin-top:6mm">Enjoy Tokyo — and eat like a local. 🍜<br><span style="font-weight:400;font-size:11px">Japan Like a Local · zeroailog.gumroad.com</span></p>''', pn))

html_doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
(R / 'tools/foodmap.html').write_text(html_doc)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page()
    pg.goto((R / 'tools/foodmap.html').as_uri()); pg.wait_for_timeout(800)
    pg.pdf(path=str(OUT), format='A4', print_background=True); b.close()
src = '# Tokyo Food Map v1 — sources (checked Oct 29 – Nov 2, 2026)\n\n' + ''.join(f'- {num[id(x)]}. {x["name_en"]} ({x["name_ja"]}): {x["source_url"]}\n' for c in CAT for x in D if x['category'] == c)
SRC_OUT.write_text(src)
print('ok', OUT.name, pn, 'pages')
