# Build "JAPAN LIKE A LOCAL – First-Time Visitor Guide" v2 (Updated November 2026)
# Usage: python3 tools/build_paid_guide_v2.py  -> products/paid-guide-v2-2026-11.pdf
import html, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_HTML = ROOT / "tools" / "paid_guide_v2.html"
OUT_PDF = ROOT / "products" / "paid-guide-v2-2026-11.pdf"

def e(s):  # escape, but allow <b>, <i>, <span class=jp> written by us
    return s

# ---------- content ----------
# Each page: dict(kicker, title, body(html)). Cover / contents / end built separately.
P = []

def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def ol(*items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

def box(title, text, cls=""):
    return f'<div class="box {cls}"><div class="bt">{title}</div><p>{text}</p></div>'

def phrase(label, jp, en):
    return f'<div class="phrase"><div class="pl">{label}</div><div class="pj">{jp}</div><div class="pe">{en}</div></div>'

def h2(t):
    return f"<h2>{t}</h2>"

def page(kicker, title, body, new=False):
    P.append(dict(kicker=kicker, title=title, body=body, new=new))

page("Before you land", "Before You Land",
     "<p class=lead>Japan is easy to travel once you know a few unwritten rules. This guide focuses on the details that often surprise first-time visitors.</p>"
     + h2("Your 10-minute setup")
     + ul("Keep some Japanese yen in cash. Cards are common, but cash is still useful.",
          "Set up or buy a rechargeable IC transit card if it works for your route and device.",
          "Save your hotel name and address in both English and Japanese.",
          "Download an offline map area and a translation app.",
          "Carry a small bag for trash; public bins can be limited.",
          "Save emergency numbers: Police 110 / Fire &amp; Ambulance 119.")
     + box("New in November 2026", "Tax-free shopping works differently for purchases from <b>November 1, 2026</b>. You now pay the full price first and get the tax back when you leave. See pages {taxfree}.", "accent")
     + h2("The five things most visitors should remember")
     + ol("Tipping is generally not expected.", "Cash still matters.", "Trash bins may be hard to find.",
          "Trains are quiet spaces.", "“Sumimasen” is one of the most useful words you can learn."))

page("Money", "Money Without Stress",
     "<p class=lead>Japan is much more cashless than it used to be, especially in major cities. Still, some smaller shops, rural businesses, ticket machines and local services may require cash.</p>"
     + h2("A simple payment strategy")
     + '<dl><dt>Card</dt><dd>Use it where accepted for hotels, larger shops and many restaurants.</dd>'
       '<dt>Cash</dt><dd>Keep a backup amount for small businesses, rural areas and places that do not accept your card.</dd>'
       '<dt>IC card</dt><dd>A prepaid transit card such as Suica, PASMO or ICOCA can make trains easier and can also be used at many vending machines, convenience stores and other locations.</dd></dl>'
     + box("Don't panic at the register", "Look for card or IC logos near the register. If you are unsure, show your card and ask: “Kaado, daijoubu desu ka?” (Is card okay?)")
     + phrase("Useful money phrase", "Ikura desu ka?", "How much is it?"))

page("Tax-free shopping", "Tax-Free Shopping: New Rules from Nov 1, 2026",
     "<p class=lead>Japan has changed how tax-free shopping works for visitors. For purchases from <b>November 1, 2026</b>, you pay the full price at the shop and the consumption tax is refunded later, when you leave Japan.</p>"
     + '<div class="compare"><div><div class="ct">Until Oct 31, 2026</div><p>Tax was taken off at the register.</p></div>'
       '<div class="arrow">→</div><div class="now"><div class="ct">From Nov 1, 2026</div><p>Pay the full price, tax included. Get the tax back after Customs confirms at departure.</p></div></div>'
     + h2("What to know")
     + ul("<b>Minimum:</b> 5,000 yen or more (before tax) at one tax-free shop on one day.",
          "<b>Leave within 90 days</b> of the purchase date and do the check when you depart.",
          "Food, drinks and cosmetics <b>no longer need special sealed packaging</b>.",
          "The old 500,000 yen limit on consumables is gone, but buy only what you can personally carry out of Japan.",
          "Items you use, eat or drink in Japan cannot be refunded.",
          "Purchases made up to October 31, 2026 still follow the old system.")
     + box("Ask when you pay", "How the refund reaches you can depend on the shop or the refund service it uses. Ask at checkout whether any fee is deducted, and keep <b>every receipt</b> together with your passport."),
     new=True)

page("Tax-free shopping", "At the Airport: The Tax-Free Check",
     "<p class=lead>The check happens at the airport or seaport where you leave Japan. Do it early.</p>"
     + h2("Step by step")
     + ol("Have your <b>passport, all receipts and the items</b> ready.",
          "<b>Before you check in your bags</b>, use a tax-free procedure terminal in the international departure lobby. At Narita, Haneda, Kansai, Chubu, Fukuoka, New Chitose and Naha you can also use Visit Japan Web. Checked bags cannot be taken back out.",
          "<b>Green</b> result: done, no inspection needed. <b>Red</b> result: take your items to the customs inspection area.",
          "Finish everything, including any inspection, <b>before boarding</b>.")
     + box("One missing item = no refund for that receipt", "Customs checks each receipt as one group. If even one item from a receipt is missing at departure, nothing on that receipt is refunded. If you plan to use something in Japan, it is safer to buy it on a separate receipt.", "warn")
     + ul("If you already used a tax-free item, don't use the terminal. Tell a customs officer at the customs counter.",
          "Leave extra time. Neither Customs nor your airline compensates you for a missed flight.")
     + '<p class="note">Based on Japan Tourism Agency and JNTO information checked in October 2026. Steps may vary by airport; check official guidance before you shop.</p>',
     new=True)

page("Trains", "Trains Like a Local",
     "<p class=lead>Japan's rail system is extensive, but large stations can feel overwhelming. Focus on the line name, direction, platform and final destination shown on signs.</p>"
     + h2("The easy version")
     + ul("Use an IC card for ordinary local travel where accepted: tap in, tap out.",
          "Queue at the floor markings before the train arrives.",
          "Let passengers exit before you board.",
          "Keep phone calls off local trains and keep your voice low.",
          "Move backpacks off your back on crowded trains.",
          "Eating is fine on many long-distance trains such as the Shinkansen, but is generally avoided on local and subway trains.")
     + box("Missed your stop?", "Stay calm. Get off at the next station and use your map, or ask station staff. Staffed gates are your friend when a ticket or IC card does not work.")
     + phrase("Station phrase", "___ wa doko desu ka?", "Where is ___?"))

page("Manners", "Small Manners, Big Difference",
     "<p class=lead>You do not need to memorize hundreds of rules. A few habits cover most situations.</p>"
     + '<dl><dt>No tipping by default</dt><dd>Tipping is generally not expected in restaurants, taxis and hotels. Pay the amount shown unless a service clearly says otherwise.</dd>'
       '<dt>Shoes</dt><dd>Remove shoes when entering homes, many traditional accommodations, and some restaurants or temples. A raised entrance, shoe rack or slippers may mean a shoes-off area. Check signs or ask staff.</dd>'
       '<dt>Queues</dt><dd>People line up for trains, restaurants and shops. Follow floor markings and join the end of the line.</dd>'
       '<dt>Trash</dt><dd>Public trash bins can be limited. Carry a small bag and dispose of trash when you find an appropriate bin.</dd></dl>'
     + box("The golden rule", "Try not to inconvenience the people around you. That one idea explains a lot of everyday etiquette in Japan."))

page("Convenience stores", "Convenience Stores Are Your Friend",
     "<p class=lead>Japanese convenience stores, often called <i>konbini</i>, are useful travel bases, not just snack shops.</p>"
     + h2("What they are useful for")
     + ul("Quick meals, drinks, snacks and basic toiletries.",
          "ATMs at many locations; international card support varies by ATM and network.",
          "Paying with cash, card or IC/e-money, depending on the store and terminal.",
          "A reliable place to regroup, buy water and solve small travel problems.")
     + box("Easy first meal", "If ordering at a restaurant feels intimidating on day one, a konbini is a low-stress way to get familiar with Japanese food labels and prices.")
     + phrase("Useful phrase", "Kore, onegaishimasu.", "This one, please."))

page("Restaurants", "Restaurants Without Anxiety",
     "<p class=lead>Many restaurants display photos, plastic food models, ticket machines or tablet menus. You can often order with very little Japanese.</p>"
     + h2("A simple routine")
     + ul("At the entrance, wait to be seated unless the setup clearly shows self-seating.",
          "Use photos or point politely if language is difficult.",
          "If there is a ticket machine, buy the meal ticket first and hand it to staff.",
          "Do not leave a tip unless the place clearly works differently.",
          "At busy places, avoid lingering long after finishing your meal.")
     + box("Allergy note", "Do not rely only on translation apps for serious food allergies. Prepare a clearly written allergy card in Japanese before your trip and confirm with staff.", "warn")
     + phrase("Menu phrase", "Eigo no menyuu wa arimasu ka?", "Do you have an English menu?"))

# ---- situation guides (new) ----
page("Situation guide · onsen", "Onsen (Hot Springs)",
     "<p class=lead>A hot spring bath is one of the best things to do in Japan. The rules are simple once you know the order.</p>"
     + h2("How it usually works")
     + ol("Change in the changing room. In most traditional baths, you bathe without a swimsuit in baths separated by gender.",
          "<b>Wash and rinse your whole body</b> at the shower stations before you get into the bath.",
          "Keep your small towel <b>out of the water</b>. Many people fold it on their head or leave it beside the bath.",
          "Tie up long hair so it does not touch the water.",
          "Dry off a little before going back into the changing room.")
     + ul("Avoid bathing right after drinking alcohol, and drink water.",
          "Keep your voice low; many people come to relax.")
     + box("Tattoos", "Policies vary a lot. Some baths refuse tattoos, some let you cover a small one with a sticker, and some are tattoo-friendly. Check the facility's website or ask before you go. A private bath (<i>kashikiri</i>) can be an option.", "accent")
     + phrase("Ask first", "Tattoo wa daijoubu desu ka?", "Are tattoos okay?"),
     new=True)

page("Situation guide · toilets", "Japanese Toilets",
     "<p class=lead>Public toilets are common in stations, parks and many shops. The buttons look complicated, but you only need a few.</p>"
     + h2("Good to know")
     + ul("Toilet paper goes <b>into the toilet</b>. Put sanitary products and other items in the small bin.",
          "The flush is often a button on a wall panel or side panel, a lever, or a sensor you wave your hand over.",
          "Common labels: <span class=jp>流す</span> = flush, <span class=jp>大</span> = big flush, <span class=jp>小</span> = small flush.",
          "Do not press the call button (often marked <span class=jp>呼出</span>) unless you need help.",
          "Some toilets have a sound button that plays a flushing sound for privacy.",
          "In homes, ryokan and some restaurants, there are separate toilet slippers. Take them off when you leave.")
     + box("Can't find the flush?", "Stand up and wait a second: many toilets flush automatically. If not, look at the wall beside you before touching the seat panel.")
     + phrase("Most useful question", "Toire wa doko desu ka?", "Where is the restroom?"),
     new=True)

page("Situation guide · taxis & luggage", "Taxis and Luggage",
     h2("Taxis")
     + ul("The rear left door often <b>opens and closes automatically</b>. Let the driver handle it.",
          "Show your destination on your phone, in Japanese if possible.",
          "No tipping. Many taxis take cards or IC cards; look for stickers or ask.",
          "Wear your seat belt, back seat included.",
          "Taxi-hailing apps work in many big cities.")
     + h2("Luggage")
     + ul("<b>Shinkansen</b> (Tokaido, Sanyo, Kyushu, Nishi-Kyushu): a bag with total dimensions over 160 cm, up to 250 cm, needs a reserved “seat with an oversized baggage area”. Without one there is a 1,000 yen fee. Bags over 250 cm are not allowed. Strollers, sports equipment and musical instruments don't need this reservation.",
          "<b>Luggage delivery</b> (<i>takkyuubin</i>) can send bags between hotels or to the airport. Ask your hotel front desk about cut-off times.",
          "Station coin lockers are handy, but large ones fill up fast at busy times.",
          "On crowded trains, hold your bag in front of you or use the rack.")
     + box("Travel light between cities", "Sending your big suitcase ahead and riding with a small day bag makes stations, stairs and crowded trains much easier."),
     new=True)

page("Situation guide · shrines & temples", "Shrines and Temples",
     "<p class=lead>Visitors are welcome at most shrines and temples. A few small gestures show respect.</p>"
     + h2("At a shrine (Shinto)")
     + ol("Bow once at the <i>torii</i> gate and walk slightly to the side, not through the exact center.",
          "At the water basin: hold the ladle in your right hand and rinse your left hand; switch and rinse your right; pour a little water into your left palm, rinse your mouth and spit beside the basin. Don't touch the ladle with your lips.",
          "At the front of most shrines: offer a coin, ring the bell if there is one, <b>bow twice, clap twice</b>, pray, then bow once more.")
     + h2("At a temple (Buddhist)")
     + ul("Pray quietly with your hands together. <b>Don't clap.</b>",
          "Some temples offer incense; many visitors waft the smoke toward themselves.")
     + h2("Everywhere")
     + ul("Follow photo signs, keep your voice low, and step aside for people praying.",
          "You may need to take off your shoes in some buildings.")
     + phrase("Before taking photos", "Shashin, daijoubu desu ka?", "Is it okay to take photos?"),
     new=True)

page("Situation guide · vending machines & escalators", "Vending Machines and Escalators",
     h2("Vending machines")
     + ul("You will find them almost everywhere. Many take cash and IC cards; some take cards or QR payments.",
          "Hot and cold drinks often share one machine: <b>red</b> labels usually mean hot, <b>blue</b> usually mean cold.",
          "The bins next to machines are usually for bottles and cans only. Please don't put other trash in them.")
     + h2("Escalators")
     + ul("In the Tokyo area, people usually stand on the <b>left</b>; in the Osaka area, on the <b>right</b>.",
          "More and more stations ask people to <b>stand still on both sides</b> and not walk. Saitama Prefecture and Nagoya City have local rules asking for this.",
          "Hold the handrail. With a large suitcase, the elevator is often safer.")
     + box("When in doubt", "Copy the people in front of you. Local habits can differ from station to station."),
     new=True)

page("Phrases", "8 Phrases That Do Real Work",
     '<table class="phr">'
     + "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in [
         ("Sumimasen", "Excuse me / Sorry / A polite way to get attention"),
         ("Arigatou gozaimasu", "Thank you very much"),
         ("Onegaishimasu", "Please (when asking for something)"),
         ("Kore, onegaishimasu", "This one, please"),
         ("___ wa doko desu ka?", "Where is ___?"),
         ("Toire wa doko desu ka?", "Where is the restroom?"),
         ("Ikura desu ka?", "How much is it?"),
         ("Daijoubu desu", "I'm okay / No thank you / It's fine (depends on context)")])
     + "</table>"
     + box("If you learn only one", "Learn “Sumimasen.” It can mean excuse me, sorry, or politely getting someone's attention. Extremely useful for travelers."))

page("Mistakes", "Common First-Timer Mistakes",
     '<dl class="mist">'
     + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in [
         ("Assuming everywhere takes cards.", "Keep some cash as backup, especially outside major city centers."),
         ("Talking loudly on trains.", "Keep conversations quiet and avoid phone calls on local trains."),
         ("Looking for a trash bin every five minutes.", "Carry your trash until you find an appropriate place for it."),
         ("Tipping automatically.", "In most everyday situations, it is unnecessary."),
         ("Trying to understand the whole station at once.", "Only solve the next step: line, direction, platform, destination."),
         ("Checking in your bags before the tax-free check.", "From Nov 1, 2026, do the tax-free procedure first. Your items need to be with you."),
         ("Overplanning every minute.", "Leave buffer time for large stations, wrong exits and spontaneous discoveries.")])
     + "</dl>"
     + box("Good traveler &gt; perfect traveler", "You will make small mistakes. Be polite, stay observant, and ask for help. That is enough."))

page("Help", "When You Need Help",
     "<p class=lead>Save these before your trip.</p>"
     + '<div class="sos"><div><b>Police</b><span>110</span><small>Urgent police emergencies</small></div>'
       '<div><b>Fire / Ambulance</b><span>119</span><small>Urgent fire or medical emergencies</small></div></div>'
     + h2("Japan Visitor Hotline")
     + "<p>JNTO operates a visitor hotline 24 hours a day, 365 days a year, with support in English, Chinese and Korean.</p><p class=pj>050-3816-2787</p><p>From a non-Japanese phone: +81-50-3816-2787. Check the official JNTO website for any updates before departure.</p>"
     + h2("Lost something?")
     + "<p>Ask station staff, the shop or the hotel first. Lost property is often handled by the facility where it was found before being transferred elsewhere.</p>"
     + h2("Medical needs")
     + "<p>For serious symptoms, use emergency services. For non-emergency care, ask your hotel or an official visitor support service for nearby options that can assist international travelers.</p>")

page("First 24 hours", "Your First 24 Hours",
     "<p class=lead>Use this as a low-stress landing plan.</p>"
     + '<div class="cols">'
     + "<div>" + h2("At the airport") + ul("Get connected: eSIM, SIM or Wi‑Fi.", "Get cash if needed.", "Set up your IC card or confirm your train or bus ticket.")
     + h2("On the way to the hotel") + ul("Follow the route one transfer at a time.", "Keep your hotel address ready in Japanese.") + "</div>"
     + "<div>" + h2("Near the hotel") + ul("Find the station entrance you will use tomorrow.", "Locate a convenience store and an ATM option.", "Buy water and a simple breakfast or snack.")
     + h2("Before sleeping") + ul("Check tomorrow's weather and first train route.", "Charge your phone and power bank.", "Put a small trash bag, cash and IC card in your day bag.") + "</div></div>"
     + box("Day one goal", "Do not try to conquer Japan on arrival day. Learn your neighborhood, eat something good, and get some sleep."))

page("Cheat sheet", "One-Page Cheat Sheet",
     '<table class="cheat">'
     + "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in [
         ("Money", "Card + some cash + IC card."),
         ("Trains", "Tap in/out. Queue. Let people exit. Keep quiet."),
         ("Tipping", "Usually no tip."),
         ("Trash", "Carry a small bag; bins may be limited."),
         ("Shoes", "Remove if required. Check signs or ask staff."),
         ("Tax-free", "Pay full price. At departure: tax-free check first, then check in bags. Keep every item."),
         ("Onsen", "Wash first. Towel out of the water. Ask about tattoos."),
         ("Shrine", "Most shrines: bow twice, clap twice, bow once. Temple: no clapping."),
         ("Help", "“Sumimasen” = your all-purpose polite opener."),
         ("Emergency", "Police 110 · Fire / Ambulance 119")])
     + "</table>"
     + h2("Three phrases to screenshot")
     + ul("<b>Sumimasen.</b> Excuse me / Sorry.", "<b>Kore, onegaishimasu.</b> This one, please.", "<b>Toire wa doko desu ka?</b> Where is the restroom?")
     + box("Screenshot this page", "Keep it in your Favorites album so you can reach it quickly when your signal is weak."))

page("Sources", "Official Sources &amp; Updates",
     "<p class=lead>Travel rules, transport products and service details can change. Before departure, verify time-sensitive information with official sources.</p>"
     + h2("Checked for this November 2026 edition")
     + '<dl class="src">'
       '<dt>Japan Tourism Agency (MLIT)</dt><dd>New tax-free system from November 1, 2026 · mlit.go.jp/kankocho/tax-free</dd>'
       '<dt>Japan National Tourism Organization (JNTO)</dt><dd>New tax-free shopping system; tipping, cashless payments, IC cards, rail manners, shrine and temple etiquette, Visitor Hotline · japan.travel</dd>'
       '<dt>JR Central / JR West</dt><dd>Oversized baggage on the Tokaido, Sanyo, Kyushu and Nishi-Kyushu Shinkansen · westjr.co.jp, japanrailpass.net</dd></dl>'
     + box("Important", "This is a practical travel guide, not legal, immigration, customs, medical or emergency advice. Visa, customs, tax-free shopping, transport and entry rules may change, and individual facilities set their own rules. Always verify current requirements with the relevant official authority.", "warn")
     + '<div class="end"><div class="em">JAPAN LIKE A LOCAL</div><div>Know more. Worry less. Enjoy Japan.</div></div>')

# ---------- layout ----------
FIRST = 3  # cover=1, contents=2
for i, p in enumerate(P):
    p["no"] = FIRST + i
tax = [p["no"] for p in P if p["kicker"].startswith("Tax-free")]
taxref = f"{tax[0]}–{tax[-1]}"
for p in P:
    p["body"] = p["body"].replace("{taxfree}", taxref)

FONT = str(ROOT / "tools" / "fonts") + "/"
CSS = f"""
@font-face{{font-family:Inter;src:url(file://{FONT}Inter-Regular.ttf);font-weight:400}}
@font-face{{font-family:Inter;src:url(file://{FONT}Inter-Italic.ttf);font-weight:400;font-style:italic}}
@font-face{{font-family:Inter;src:url(file://{FONT}Inter-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:Inter;src:url(file://{FONT}Inter-Bold.ttf);font-weight:700}}
@font-face{{font-family:Inter;src:url(file://{FONT}Inter-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:JPG;src:url(file:///usr/share/fonts/opentype/ipafont-gothic/ipag.ttf)}}
@page{{size:148mm 210mm;margin:0}}
:root{{--red:#C8382B;--ink:#1F2328;--sub:#5B616B;--cream:#F4EFE7;--line:#E3DCD0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:Inter,JPG,sans-serif;color:var(--ink);font-size:9.4pt;line-height:1.5}}
.jp{{font-family:JPG;font-weight:400;font-size:1.05em}}
.pg{{width:148mm;height:210mm;position:relative;overflow:hidden;page-break-after:always;padding:15mm 13mm 16mm}}
.pg:before{{content:"";position:absolute;top:0;left:0;right:0;height:3mm;background:var(--red)}}
.kick{{text-align:center;font-size:6.8pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--red);margin-bottom:3mm}}
.kick .n{{color:var(--ink)}}
.new{{display:inline-block;background:var(--red);color:#fff;border-radius:2mm;padding:.3mm 1.6mm;margin-left:1.5mm;font-size:6pt;letter-spacing:.08em}}
h1{{font-size:18pt;line-height:1.15;font-weight:800;margin-bottom:3mm;letter-spacing:-.01em}}
h2{{font-size:10.8pt;font-weight:700;margin:3.6mm 0 1.6mm}}
p{{margin-bottom:1.6mm}}
.lead{{color:#3A3F46;font-size:9.6pt}}
ul,ol{{list-style:none;margin:0 0 1.5mm}}
li{{position:relative;padding-left:4.2mm;margin-bottom:1.15mm}}
ul>li:before{{content:"";position:absolute;left:.4mm;top:.62em;width:1.5mm;height:1.5mm;border-radius:50%;background:var(--red);transform:translateY(-50%)}}
ol{{counter-reset:n}}
ol>li{{counter-increment:n;padding-left:5.6mm}}
ol>li:before{{content:counter(n);position:absolute;left:0;top:.1em;width:3.9mm;height:3.9mm;border-radius:50%;background:var(--ink);color:#fff;font-size:6.2pt;font-weight:700;text-align:center;line-height:3.9mm}}
dl dt{{font-weight:700;margin-top:2mm}}
dl dd{{margin-bottom:.5mm}}
dl.mist{{counter-reset:m}}
dl.mist dt{{counter-increment:m}}
dl.mist dt:before{{content:"Mistake " counter(m) ": ";color:var(--red)}}
.box{{background:var(--cream);border-left:1.2mm solid var(--line);border-radius:1mm;padding:2.6mm 3.4mm 1.4mm;margin:3mm 0}}
.box.accent{{border-left-color:var(--red)}}
.box.warn{{border-left-color:#E0A21B;background:#FBF3DF}}
.bt{{font-size:6.8pt;font-weight:800;letter-spacing:.1em;text-transform:uppercase;margin-bottom:1mm}}
.phrase{{border-top:.3mm solid var(--line);padding-top:2.4mm;margin-top:3mm}}
.pl{{font-size:6.6pt;color:var(--sub);text-transform:uppercase;letter-spacing:.1em;font-weight:700}}
.pj{{font-size:12pt;font-weight:700;color:var(--red)}}
.pe{{color:var(--sub)}}
.compare{{display:flex;align-items:stretch;gap:2mm;margin:3mm 0 1mm}}
.compare>div:not(.arrow){{flex:1;border:.3mm solid var(--line);border-radius:1.5mm;padding:2.4mm 3mm 1mm}}
.compare .now{{border-color:var(--red)!important;background:#FCEFEC}}
.compare .arrow{{align-self:center;font-size:14pt;color:var(--red);font-weight:700}}
.ct{{font-weight:800;font-size:7.4pt;text-transform:uppercase;letter-spacing:.06em;margin-bottom:1mm}}
.note{{font-size:6.8pt;color:var(--sub);margin-top:2.5mm}}
table{{width:100%;border-collapse:collapse;margin:2mm 0}}
table th,table td{{text-align:left;vertical-align:top;border-bottom:.3mm solid var(--line);padding:2mm 1.5mm}}
table.phr th{{width:44%;font-weight:700}}
table.phr td{{color:var(--sub)}}
table.cheat th{{width:24%;font-size:7pt;letter-spacing:.08em;text-transform:uppercase;color:var(--red);padding-top:2.2mm}}
.sos{{display:flex;gap:3mm;margin:3mm 0}}
.sos>div{{flex:1;background:var(--cream);border-radius:1.5mm;padding:3mm;text-align:center}}
.sos b{{display:block;font-size:7pt;text-transform:uppercase;letter-spacing:.1em}}
.sos span{{display:block;font-size:22pt;font-weight:800;color:var(--red);line-height:1.2}}
.sos small{{color:var(--sub);font-size:6.8pt}}
.cols{{display:flex;gap:5mm}} .cols>div{{flex:1}}
.src dt{{margin-top:2.4mm}} .src dd{{color:var(--sub)}}
.end{{text-align:center;margin-top:7mm;color:var(--sub)}}
.end .em{{font-weight:800;letter-spacing:.14em;color:var(--ink);font-size:9pt}}
.foot{{position:absolute;left:13mm;right:13mm;bottom:8mm;border-top:.3mm solid var(--line);padding-top:1.6mm;font-size:6.2pt;color:var(--sub);display:flex;justify-content:space-between}}
/* cover */
.cover{{background:var(--cream);text-align:center;padding-top:30mm}}
.cover:before{{display:none}}
.badge{{width:22mm;height:22mm;border-radius:50%;background:var(--red);color:#fff;font-weight:800;font-size:13pt;line-height:22mm;margin:0 auto 12mm}}
.cover .k{{font-size:7.6pt;font-weight:800;letter-spacing:.16em;color:var(--red);margin-bottom:3mm}}
.cover h1{{font-size:30pt;line-height:1.02;letter-spacing:.01em;margin-bottom:4mm}}
.cover .tag{{color:var(--sub);font-size:9pt;max-width:100mm;margin:0 auto 9mm}}
.upd{{display:inline-block;border:.5mm solid var(--red);color:var(--red);font-weight:800;font-size:9pt;letter-spacing:.12em;padding:1.6mm 4mm;border-radius:1mm;margin-bottom:8mm}}
.whatnew{{background:#fff;border-radius:1.5mm;text-align:left;padding:3.4mm 4mm 2mm;margin:0 6mm}}
.whatnew .bt{{color:var(--red)}}
.cover .ed{{position:absolute;left:0;right:0;bottom:10mm;font-size:6.6pt;color:var(--sub);letter-spacing:.1em}}
/* contents */
.toc{{margin-top:2mm}}
.toc a{{display:flex;align-items:baseline;color:inherit;text-decoration:none;padding:1.35mm 0;border-bottom:.25mm dotted var(--line)}}
.toc .t{{flex:1}}
.toc .no{{font-weight:700;width:8mm;text-align:right}}
.toc .new{{font-size:5.6pt}}
"""

def foot(n):
    return f'<div class="foot"><span>JAPAN LIKE A LOCAL · First-Time Visitor Guide · Updated November 2026</span><span>{n}</span></div>'

pages_html = []
n_scenes = sum(1 for p in P if p["kicker"].startswith("Situation"))
pages_html.append(f'''<section class="pg cover">
<div class="badge">JP</div>
<div class="k">FIRST-TIME JAPAN TRAVEL</div>
<h1>JAPAN<br>LIKE A LOCAL</h1>
<p class="tag">A practical pocket guide to money, trains, manners, phrases and the small things that make Japan easier.</p>
<div class="upd">UPDATED NOVEMBER 2026</div>
<div class="whatnew"><div class="bt">New in this edition</div>
<ul><li>Tax-free shopping: the new rules from November 1, 2026, and the airport check step by step</li>
<li>{n_scenes} situation guides: onsen, toilets, taxis &amp; luggage, shrines &amp; temples, vending machines &amp; escalators</li></ul></div>
<div class="ed">FIRST EDITION SEPTEMBER 2026 · {FIRST + len(P) - 1} PAGES</div>
</section>''')

toc = "".join(
    f'<a><span class="t">{p["title"]}{"<span class=new>NEW</span>" if p["new"] else ""}</span><span class="no">{p["no"]}</span></a>'
    for p in P)
pages_html.append(f'''<section class="pg"><div class="kick">Contents</div><h1>What's Inside</h1>
<p class="lead">Read it once before landing, then keep the cheat sheet (page {[p["no"] for p in P if p["kicker"]=="Cheat sheet"][0]}) on your phone.</p>
<div class="toc">{toc}</div>{foot(2)}</section>''')

for p in P:
    newtag = '<span class="new">NEW</span>' if p["new"] else ""
    pages_html.append(f'''<section class="pg"><div class="kick"><span class="n">{p["no"]:02d}</span> / {p["kicker"]}{newtag}</div>
<h1>{p["title"]}</h1>{p["body"]}{foot(p["no"])}</section>''')

doc = f"<!doctype html><html lang=en><head><meta charset=utf-8><title>JAPAN LIKE A LOCAL – First-Time Visitor Guide</title><style>{CSS}</style></head><body>{''.join(pages_html)}</body></html>"
OUT_HTML.write_text(doc, encoding="utf-8")

with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page()
    pg.goto(OUT_HTML.as_uri())
    pg.wait_for_timeout(500)
    # overflow check: content must not run into footer
    over = pg.evaluate("""() => [...document.querySelectorAll('section.pg')].map((s,i)=>{
      const f=s.querySelector('.foot'); if(!f) return null;
      const fr=f.getBoundingClientRect().top; let max=0;
      s.querySelectorAll(':scope > *:not(.foot)').forEach(c=>{max=Math.max(max,c.getBoundingClientRect().bottom)});
      return max>fr-4 ? (i+1)+': overflow '+Math.round(max-fr)+'px' : null}).filter(Boolean)""")
    print("OVERFLOW:", over or "none")
    pg.pdf(path=str(OUT_PDF), prefer_css_page_size=True, print_background=True)
    b.close()
print("pages:", FIRST + len(P) - 1, "->", OUT_PDF)
