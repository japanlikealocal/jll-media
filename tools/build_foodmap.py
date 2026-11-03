# Paid product: Tokyo food map PDF (48 spots: gyoza, unagi, ramen, yakitori).
# Data: docs/foodmap-data-2026-11-03.json (extracted from docs/*-sources-*.md, checked Oct 29 – Nov 2, 2026).
# Rules: only facts from the sources docs; unverified (user-posted / review) prices are dropped; no AI food images.
import json, pathlib, html, urllib.parse
from playwright.sync_api import sync_playwright
R = pathlib.Path(__file__).resolve().parent.parent
D = json.load(open(R / 'docs/foodmap-data-2026-11-03.json'))
OUT = R / 'products/tokyo-food-map-v1-2026-11.pdf'
for x in D:  # reviewer fixes 2026-11-03
    if x['name_en'] == 'Soranoiro': x['notes'] = 'Ginza main shop moved here on Oct 3, 2025.'
    if x['name_en'] == 'Akasaka Fukinuki': x['notes'] = x['notes'].replace('Widest range of payment options in this list.', 'Widest range of payment options among the unagi shops here.')
    if x['name_en'] == 'Takashimaya': x['name_en'] = 'Takashimaya (unagi shop)'
    x['station'] = x['station'].replace('Tokyo Sta.', 'Tokyo Station')
    for k in ('closed', 'notes', 'price'):
        if x.get(k): x[k] = x[k].replace('Doyo no Ushi day', 'midsummer eel day (Doyo no Ushi)')
SRC_OUT = R / 'products/tokyo-food-map-v1-sources.md'

CAT = {
 'gyoza':   ('Gyoza',   '餃子',   '#c2410c', 'Oct 29, 2026'),
 'unagi':   ('Unagi',   'うなぎ', '#7c4a1e', 'Nov 1, 2026'),
 'ramen':   ('Ramen',   'ラーメン', '#b91c1c', 'Nov 1, 2026'),
 'yakitori':('Yakitori','焼き鳥', '#a16207', 'Nov 2, 2026'),
}
BAD = ('user-posted', 'user listing', 'review', 'may be outdated', 'reference value')

PRICE_FIX = {  # drop user-posted / review prices (not verified)
 'Nodaiwa': 'Classic unaju (Michelin-listed). Price not confirmed — check on arrival.',
 'Rokurinsha': 'Tsukemen (dipping noodles). Price not confirmed — check the ticket machine.',
 'Hyotanya': 'Unadon in the ¥1,000s (Gurunavi listing). Check other prices on arrival.',
}
def clean_price(x):
    p = PRICE_FIX.get(x['name_en'], x['price'] or 'Check prices on arrival.')
    assert not any(b in p.lower() for b in BAD), x['name_en']
    return p

def clean_notes(x):
    n = x.get('notes') or ''
    if x['name_en'] == 'Nodaiwa': n = ''
    return n

AREA = [
 ('Shinjuku & west Tokyo', ['Shinjuku', 'Nishi-Shinjuku', 'Yoyogi', 'Kichijoji', 'Komae']),
 ('Ginza, Tokyo Station & Nihombashi', ['Ginza', 'Higashi-Ginza', 'Yurakucho', 'Kyobashi', 'Tokyo Station', 'Mitsukoshimae', 'Shin-Nihombashi']),
 ('Central: Akasaka, Azabu, Iidabashi', ['Toranomon', 'Akasaka', 'Azabu', 'Akabanebashi', 'Gaiemmae', 'Iidabashi', 'Edogawabashi']),
 ('Asakusa, Ueno & east', ['Asakusa', 'Ueno', 'Uguisudani', 'Kameido', 'Kinshicho', 'Morishita', 'Yotsugi']),
 ('Shibuya, Ebisu & south', ['Shibuya', 'Ebisu', 'Naka-Meguro', 'Sangenjaya', 'Kamata']),
 ('Ikebukuro & north', ['Ikebukuro', 'Otsuka', 'Akabane']),
]
def area_of(st):
    for a, keys in AREA:
        if any(st.startswith(k) for k in keys): return a
    return 'Other'

def maps(x):
    return 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote(x['name_ja'].split('（')[0] + ' ' + (x.get('address_ja') or ''))

def pay_tag(p):
    pl = p.lower()
    if pl.startswith('cash or qr'): return ('CASH / QR', '#b45309')
    if 'transit ic cards ok' in pl and 'visa' not in pl: return ('CASH / IC CARD', '#b45309')
    if 'cards only' in pl: return ('CARDS ONLY · NO CASH', '#1d4ed8')
    if 'cashless only' in pl: return ('NO CASH', '#1d4ed8')
    if pl.strip() == 'cash only': return ('CASH ONLY', '#b91c1c')
    if 'cards ok' in pl or 'cards and e-money ok' in pl: return ('CARDS OK', '#15803d')
    if 'bring cash' in pl or 'no cards' in pl: return ('NO CARDS · BRING CASH', '#b91c1c')
    return ('PAYMENT: CHECK', '#6b7280')

e = html.escape
def fmt_closed(c):
    if not c or c.lower().startswith('not stated'): return ''
    cl = c.lower()
    if cl.startswith('none'): return 'Open daily'
    if cl.startswith(('open daily', 'no regular', 'unclear', 'irregular', 'tabelog', 'monday per tabelog')): return c
    return 'Closed: ' + c
def card(i, x):
    t, col = pay_tag(x['payment'])
    hrs = ' · '.join(s for s in [x.get('hours') or '', fmt_closed(x.get('closed'))] if s)
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
.ph{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm}.ph .j{line-height:1.25}.ph>div{background:#fff;border:1px solid #e3d8c8;border-radius:8px;padding:3mm 4mm}
.ph .j{font-family:"Noto Sans CJK JP";font-size:20px;font-weight:700}.ph .r{color:#7a1f16;font-weight:700}.ph .m{font-size:10.5px;color:#5b5047}
ul{margin:1mm 0 0 5mm;padding:0}li{margin-bottom:1mm}
.idx td:last-child{white-space:nowrap}.idx td,.idx th{font-size:9.5px;padding:.35mm 1mm;border-bottom:1px solid #eee3d3}.idx th{width:auto;color:#1f1a17}
'''

def page(inner, n, cls=''):
    return f'<div class="pg {cls}">{inner}<div class="ft"><span>Tokyo Food Map · 48 local spots · Japan Like a Local</span><span>{n}</span></div></div>'

pages = []
PH = R / 'assets/foodmap-photos'
COVER_TILES = [('gyoza', '12 GYOZA', 'center 55%'), ('ramen', '12 RAMEN', 'center 50%'), ('unagi', '12 UNAGI', 'center 60%'), ('yakitori', '12 YAKITORI', '45% 55%')]
def cover_html(w, h, landscape=False):
    tiles = ''.join(f'<div class="t" style="background-image:url({(PH/(n+'.jpg')).as_uri()});background-position:{pos}"><span>{lab}</span></div>' for n, lab, pos in COVER_TILES)
    if not landscape:
        return f'''<div class="cv"><div class="brand">JAPAN LIKE A LOCAL</div><div class="grid">{tiles}</div>
<div class="band"><div class="ttl">TOKYO FOOD MAP</div><div class="sub">48 local spots for gyoza, ramen, unagi &amp; yakitori</div>
<div class="use">Cash or card · Booking rules · Google Maps links</div>
<div class="meta"><span>Checked Oct 29 – Nov 2, 2026</span><span class="note">Photos are illustrative, not from the listed shops.</span></div></div></div>'''
    return f'''<div class="cvl"><div class="grid">{tiles}</div><div class="band"><div class="brand2">JAPAN LIKE A LOCAL</div>
<div class="ttl">TOKYO<br>FOOD MAP</div><div class="sub">48 local spots for gyoza, ramen, unagi &amp; yakitori</div>
<div class="use">Cash or card · Booking rules<br>Google Maps links</div><div class="meta">PDF guide · Checked Nov 2026<br><span class="note">Photos are illustrative, not from the listed shops.</span></div></div></div>'''
COVER_CSS = '''.cv{width:210mm;height:297mm;background:#1f1a17;display:flex;flex-direction:column;page-break-after:always;overflow:hidden}
.cv .brand{background:#f6efe3;color:#1f1a17;font-weight:800;letter-spacing:4px;font-size:13px;text-align:center;padding:3.2mm 0}
.grid{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:2px;background:#1f1a17}
.cv .grid{height:184mm}
.t{background-size:cover;position:relative}
.t span{position:absolute;left:4mm;bottom:4mm;background:#f2c14e;color:#1f1a17;font-weight:800;font-size:17px;letter-spacing:1px;padding:1.5mm 3.5mm;border-radius:4px}
.cv .band{flex:1;padding:10mm 13mm 7mm;color:#fff;display:flex;flex-direction:column}
.cv .ttl{font-size:78px;font-weight:800;letter-spacing:1px;line-height:1}
.cv .sub{font-size:26px;color:#efe6d8;margin-top:5mm;line-height:1.3}
.cv .use{font-size:21px;color:#f2c14e;font-weight:700;margin-top:6mm}
.cv .meta{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:12px;color:#d9cdbd}.note{background:#f6efe3;color:#1f1a17;font-weight:600;border-radius:4px;padding:1.4mm 3mm}
.cvl{width:1280px;height:720px;background:#1f1a17;display:flex}
.cvl .grid{width:720px;height:720px}
.cvl .t span{font-size:24px;left:16px;bottom:16px;padding:6px 14px}
.cvl .band{flex:1;padding:52px 44px 34px;color:#fff;display:flex;flex-direction:column;font-family:Inter,sans-serif}
.cvl .brand2{color:#f2c14e;font-weight:800;letter-spacing:3px;font-size:17px}
.cvl .ttl{font-size:76px;font-weight:800;line-height:.98;margin-top:26px}
.cvl .sub{font-size:25px;color:#efe6d8;margin-top:22px;line-height:1.3}
.cvl .use{font-size:22px;color:#f2c14e;font-weight:700;margin-top:24px;line-height:1.4}
.cvl .meta{margin-top:auto;font-size:16px;color:#d9cdbd;line-height:1.5}.cvl .note{display:inline-block;margin-top:8px;font-size:17px;padding:5px 10px}'''
pages.append(cover_html(0, 0))

pages.append(page('''<h2>How to use this guide</h2>
<div class="box"><b>1. Pick a spot near where you are.</b> Use the area index on the next page, or browse by food.<br>
<b>2. Check the Pay and Book lines first.</b> Many small shops in Tokyo take cash only, and some popular ramen shops only work with timed tickets or online booking.<br>
<b>3. Tap “Open in Google Maps”.</b> It searches the shop’s Japanese name and address. Check that the branch name matches before you go.<br>
<b>4. At the door, point to the Japanese name.</b> Staff can read it instantly.</div>
<h3>Reading each card</h3>
<div class="box"><b>CASH ONLY</b> — the shop says cash only. <b>NO CARDS · BRING CASH</b> — cards, e-money and QR are not accepted, so bring yen. <b>CARDS ONLY · NO CASH</b> / <b>NO CASH</b> — bring a card or phone payment. <b>CARDS OK</b> — at least some cards accepted (brands listed). <b>CASH / QR</b>, <b>CASH / IC CARD</b> — cash plus that method; credit cards not confirmed. <b>PAYMENT: CHECK</b> — not published; bring both.<br>
<b>English menu</b> — “Yes” means the shop or its listing says it has one. “Online only” means we found an English menu online but could not confirm one in the shop. “Unknown” means we could not confirm either way — it does not mean there is none.<br>
<b>Unknown</b> anywhere means the information was not published. We never guessed.</div>
<h3>Good to know</h3>
<div class="box">• Prices are the ones published by the shop or its listing when we checked. “Tax included” is only written where the source said so.<br>
• Some izakaya-style shops add a small table charge (<i>otoshi</i>) per person. Where the shop lists one, it is on the card.<br>
• Shops change hours, prices and payment without notice. Check the shop’s page or Google Maps on the day, especially for closing days marked “confirm”.<br>
• This guide was researched with the help of AI tools. Every fact on a card comes from the shop’s official page or its restaurant listing (sources list included), and the guide was checked a second time before release. It is independent: no shop paid to be included.</div>''', 2))

# area index
rows = {}
num = {}
k = 0
for c in CAT:
    for x in [y for y in D if y['category'] == c]:
        k += 1; num[id(x)] = k
        rows.setdefault(area_of(x['station']), []).append((k, x))
idx = ''; idx_pages = []
for ai, (a, _) in enumerate(AREA + [('Other', [])]):
    if ai == 3: idx_pages.append(idx); idx = ''
    if a not in rows: continue
    idx += f'<h3 style="margin:3mm 0 1mm;font-size:13px">{a}</h3><table class="idx">' + ''.join(f'<tr><td style="width:8mm"><b>{n}</b></td><td style="width:42mm">{e(x["name_en"])}</td><td style="width:22mm">{CAT[x["category"]][0]}</td><td>{e(x["station"])}</td><td style="width:30mm">{pay_tag(x["payment"])[0]}</td></tr>' for n, x in rows[a]) + '</table>'
idx_pages.append(idx)
for ii, ip in enumerate(idx_pages): pages.append(page(('<h2>Find food near you</h2>' if ii == 0 else '<h2>Find food near you (cont.)</h2>') + ip, 3 + ii))

pn = 3 + len(idx_pages)
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
<div><div class="j">2人です</div><div class="r">Futari desu</div><div class="m">“Two people.” Hold up fingers for your group size.</div></div>
<div><div class="j">これをください</div><div class="r">Kore o kudasai</div><div class="m">“This one, please.” Point at the menu.</div></div>
<div><div class="j">カードは使えますか？</div><div class="r">Kaado wa tsukaemasu ka?</div><div class="m">“Can I use a card?” Ask before you sit down.</div></div>
<div><div class="j">お会計お願いします</div><div class="r">Okaikei onegaishimasu</div><div class="m">“The bill, please.”</div></div>
<div><div class="j">予約しています</div><div class="r">Yoyaku shite imasu</div><div class="m">“I have a reservation.” Show the booking on your phone.</div></div>
<div><div class="j">英語のメニューは<br>ありますか？</div><div class="r">Eigo no menyuu wa arimasu ka?</div><div class="m">“Do you have an English menu?”</div></div>
<div><div class="j">ごちそうさまでした</div><div class="r">Gochisousama deshita</div><div class="m">“Thank you for the meal.” Say it on the way out.</div></div>
<div><div class="j">アレルギーがあります</div><div class="r">Arerugii ga arimasu</div><div class="m">“I have an allergy.” Then show the ingredient written in Japanese.</div></div>
</div>
<h3>Before you go</h3>
<div class="box">• Carry some yen cash every day — several spots in this guide take cash only.<br>• No tipping in Japan. Just pay the bill.<br>• Queues are normal at popular shops. Line up quietly and wait to be called.<br>• Allergy information is not given in this guide. Always ask the shop directly.</div>
<h3>Menu words</h3><div class="box" style="font-size:10.5px"><b>Unaju</b> eel on rice in a box · <b>kabayaki</b> eel grilled with sweet sauce · <b>shirayaki</b> eel grilled plain · <b>umaki</b> omelette rolled around eel · <b>chuka soba</b> classic soy-sauce ramen · <b>shio / shoyu</b> salt / soy sauce broth · <b>tsukemen</b> noodles you dip in soup · <b>kamameshi</b> rice cooked in a small iron pot · <b>negima</b> chicken &amp; leek skewer · <b>momo</b> thigh · <b>tsukune</b> chicken meatball · <b>nankotsu</b> cartilage · <b>kaiseki</b> multi-course meal · <b>omakase</b> chef’s choice</div>
<h3>Updates</h3><div class="box">Version 1 · facts checked Oct 29 – Nov 2, 2026. Each card’s facts come from the shop’s official page or its restaurant listing (sources list included with your download).</div>
<p style="font-size:13px;font-weight:700;margin-top:3mm">Enjoy Tokyo — and eat like a local. 🍜<br><span style="font-weight:400;font-size:11px">Japan Like a Local · zeroailog.gumroad.com</span></p>''', pn))

html_doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Tokyo Food Map — 48 local spots (Japan Like a Local)</title><style>{CSS}{COVER_CSS}</style></head><body>{"".join(pages)}</body></html>'
(R / 'tools/foodmap.html').write_text(html_doc)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page()
    pg.goto((R / 'tools/foodmap.html').as_uri()); pg.wait_for_timeout(800)
    pg.pdf(path=str(OUT), format='A4', print_background=True); b.close()
src = '# Tokyo Food Map v1 — sources (checked Oct 29 – Nov 2, 2026)\n\n' + ''.join(f'- {num[id(x)]}. {x["name_en"]} ({x["name_ja"]}): {x["source_url"]}\n' for c in CAT for x in D if x['category'] == c)
SRC_OUT.write_text(src)
with sync_playwright() as p:  # Gumroad cover 1280x720
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1280, 'height': 720})
    cf = R / 'tools/foodmap-cover.html'
    cf.write_text(f'<html><head><meta charset="utf-8"><style>body{{margin:0;font-family:Inter,sans-serif}}{COVER_CSS}</style></head><body>{cover_html(0,0,True)}</body></html>')
    pg.goto(cf.as_uri())
    pg.wait_for_timeout(800); pg.screenshot(path=str(R / 'assets/foodmap-cover-1280x720.jpg'), quality=92, type='jpeg'); b.close()
print('ok', OUT.name, pn, 'pages')
