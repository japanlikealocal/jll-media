# 4:5 "problem-solving" how-to images (ticket | konbini | train). Facts: docs/howto-3reels-sources-2026-11-17.md (Perplexity, checked 11/17).
# Unverified items are hedged ("often", "some shops", "varies"). Each reel has its own 2-3 color theme (style-refs color rules).
import pathlib, sys
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent; F=(R/'tools/fonts').as_uri()
J={
'ticket':dict(out='ig-howto-ticket',tag='FIRST RAMEN IN JAPAN?',title='How to use a ramen<br>ticket machine 🎫',
 th=('#B91C1C','#FFF7ED','#2A0E0E','#FECACA','#F5D0C5'),
 rows=[('Buy before you sit','At most ramen shops you pay first at the machine — usually near the door. Some shops take orders from staff.',''),
       ('Have cash ready','Cash still works best. More machines now take IC cards (Suica) and QR. ¥1,000 bills and coins are the safe bet.',''),
       ('Press your bowl','Put money in, then press the button for your ramen, drinks or sides.',''),
       ('Extras = more tickets','Toppings or a large size often have their own buttons.',''),
       ('Hand the ticket over','Take your change and give the ticket to staff. Some shops ask you to leave it on the counter.',''),
       ('Noodle firmness?','Some shops let you choose — on a sheet or by asking.','Katame = firm · Futsuu = regular · Yawarakame = soft')],
 note='General tips · checked Nov 2026 (JNTO, shop sites) · every shop is a little different'),
'konbini':dict(out='ig-howto-konbini',tag='JAPANESE CONVENIENCE STORES',title='What the konbini staff<br>will ask you 🏪',
 th=('#0F766E','#ECFDF5','#0B2E2B','#FDBA74','#C7EADF'),
 rows=[('“Atatamemasu ka?”','Shall I heat it up? Bento, noodles and many ready meals can be heated in the store.','Yes: Hai, onegaishimasu · No: Daijoubu desu'),
       ('“Fukuro irimasu ka?”','Do you need a bag? Plastic bags are paid since July 2020 — usually a few yen (each store sets the price).','Yes: Hai · No: Daijoubu desu'),
       ('“Ohashi otsuke shimasu ka?”','Do you need chopsticks? At some stores you take cutlery yourself.','Spoon = supuun · Chopsticks = ohashi'),
       ('Paying','Big chains take IC cards (Suica, PASMO) and major credit cards. A few items are exceptions.',''),
       ('Need cash?','Seven Bank ATMs (in 7-Eleven) accept many overseas cards, in 12 languages. Some cards may not work; fees vary.',''),
       ('Where’s the trash?','Street bins are rare — the #1 problem visitors report. Carry a small bag; don’t bring home trash to store bins.','')],
 note='General tips · checked Nov 2026 (7-Eleven, Seven Bank, METI, Japan Tourism Agency) · varies by store'),
'train':dict(out='ig-howto-train',tag='FIRST TIME ON TOKYO TRAINS?',title='6 train mistakes<br>first-timers make 🚇',
 th=('#4C1D95','#F5F3FF','#1E1235','#FACC15','#DDD6FE'),
 rows=[('Gate won’t open','Your IC card balance is too low. Use the fare adjustment machine next to the gates (cash only there).','Fare adjustment machine = Seisanki'),
       ('Wrong exit','Big stations have many exits. Check the exit number on the yellow signs (Tokyo Metro).',''),
       ('Missed the last train','Last trains leave between midnight and about 1 a.m., by line. Yamanote from Tokyo Sta: 0:38 / 0:46.',''),
       ('Riding at 8 a.m.','Weekday rush is worst around 7:30–8:30. Travel later if you can, especially with big bags.',''),
       ('Women-only car','Some lines have women-only cars on weekday mornings. Check the platform signs for the car position.',''),
       ('Phone near priority seats','When crowded, turn your phone off near priority seats. Elsewhere: silent mode, no calls.','')],
 note='Checked Nov 2026 (JR East, Tokyo Metro, MLIT) · times and rules vary by line — check Google Maps'),
'finds':dict(out='ig-finds-tokyo',tag='ONLY-IN-JAPAN FINDS',title='6 things visitors love<br>to buy in Tokyo 🛍️',
 th=('#1D4ED8','#EFF6FF','#0F1E46','#F9A8D4','#BFDBFE'),
 rows=[('FamilyMart line socks','The classic white pair with blue & green lines is listed at ¥429. Most FamilyMart stores; stock varies.','Shown on Japanese TV as a visitor favorite'),
       ('Clay-pot sweet potato','Ginza Tsubo Yakiimo · Ginza Sta 3 min. Small ¥450 · half ¥650 · whole ¥1,200 (listed 2026). Closed Mon.','銀座つぼやきいも'),
       ('Train souvenirs','GENERAL STORE RAILYARD, outside JR Akihabara Station (Showa-dori gate). Melody keychains, station-sign goods.',''),
       ('Model trains','Popondetta Akihabara (Sotokanda) for N-gauge trains and parts.',''),
       ('A custom-made pillow','Nihonbashi Nishikawa main store · Nihonbashi Sta C2. From ¥33,000. English booking page — book ahead.',''),
       ('Japanese snacks','Sweets are the top category visitors say they were happiest buying (Japan Tourism Agency 2025).','')],
 note='Checked Nov 18, 2026 (shop sites, Japan Tourism Agency) · prices, hours and stock can change',ml='➕ Follow for a Japan tip every day'),
'potato':dict(out='ig-sweet-potato',tag='WINTER SNACK',title='Sweet potato:<br>Japan vs the world 🍠',
 th=('#9F1239','#FFF7ED','#3B0A1A','#FDE68A','#FBCFE8'),
 rows=[('🇯🇵 Japan · yaki-imo','Slow-roasted on hot stones, or hung in a clay pot over charcoal (tsubo-yaki). Sweetness depends on the variety.','Try: Ginza Tsubo Yakiimo'),
       ('🇺🇸 USA','Sweet potato casserole is a Thanksgiving favorite, especially in the South.',''),
       ('🇦🇺 Australia · 🇬🇧 UK','Oven-baked sweet potato wedges are a popular home recipe.',''),
       ('🇳🇿 New Zealand · kūmara','Often roasted. Māori traditionally cooked kūmara in hot ashes.',''),
       ('🇵🇭 Philippines · kamote cue','Fried, coated in caramelized brown sugar and served on a stick.',''),
       ('🇰🇷 Korea · 🇨🇳 China','Roasted sweet potatoes are a classic winter street snack (gungoguma / kǎo hóng shǔ).','')],
 note='Examples, not the only way · checked Nov 18, 2026 (Te Ara, Korea.net, USDA, shop sites) · varies by home',ml='💬 How do you eat it?'),
'book':dict(out='ig-tokyo-booking',tag='SAVE BEFORE YOU BOOK FLIGHTS',title='Tokyo hits: when to book<br>& when to go 🎟️',
 th=('#1F2937','#FFF7ED','#111827','#FB923C','#FED7AA'),
 rows=[('Ghibli Museum','Tickets only in advance — none at the door. Next month goes on sale the 10th at 10:00 Japan time.','Closed most Tuesdays'),
       ('Tokyo Disney','Buy a dated ticket first — parks don’t sell tickets at the gate. Sales open 2 months ahead, 14:00 Japan time.','Check which park: closing times can differ'),
       ('teamLab Borderless','Timed tickets. A month’s dates open around the 1st, two months before. Same-day only if left.',''),
       ('Shibuya Sky','Dated tickets open 2 weeks ahead at 0:00. If sold out online, adult tickets are sold out at the counter too.','Rooftop can close in bad weather'),
       ('Tokyo Skytree','Same-day tickets are fine. Quietest right after opening: weekdays 10am, weekends 9am. Busy 4–7pm.',''),
       ('Harry Potter Studio Tour','Book a time slot ahead — popular slots sell out. Plan 3–4 hours.',''),
       ('No booking needed','Senso-ji (hall 6:30–17:00) · Meiji Jingu (Nov: gates close 16:10) · Tsukiji Outer Market (best 9:00–14:00)','')],
 note='Checked Nov 22, 2026 on official sites · hours and sale dates change — check before you go',ml='📌 Save for your trip'),
'resto':dict(out='ig-ask-restaurant',tag='WHAT STAFF WILL ASK YOU · #2 OF 4',title='What restaurant staff<br>will ask you 🍽️',
 th=('#C2410C','#FFFBEB','#3A1A06','#A7F3D0','#FED7AA'),
 rows=[('“Nanmei-sama desu ka?”','How many people? Hold up fingers, or say it.','Two: Futari desu · One: Hitori desu'),
       ('“Otōshi desu.”','At izakaya, a small starter often comes with a cover charge — about ¥200–1,000 per person. Ask before ordering.','How much? Otōshi wa ikura desu ka?'),
       ('“Go-chūmon wa okimari desu ka?”','Ready to order? Point at the menu. Some shops use QR ordering.','Yes: Kore o onegai shimasu · Not yet: Mada desu'),
       ('A call button on the table','Some restaurants ask you to press a bell to call staff. No bell? Say “Sumimasen!”',''),
       ('“Rasuto ōdā desu.”','Last call for orders — not “please leave” yet. Food and drinks can end at different times.',''),
       ('“Go-issho desu ka? Betsubetsu?”','Paying together or separately? Some shops can’t split the bill.','Together: Issho de · Separately: Betsubetsu de')],
 note='Checked Nov 23, 2026 (MEXT, GO TOKYO, chain FAQs) · indoor smoking mostly banned since 2020 · varies by shop',ml='➕ Follow for #3: hotels'),
'hotel':dict(out='ig-ask-hotel',tag='WHAT STAFF WILL ASK YOU · #3 OF 4',title='What the front desk<br>will ask you 🏨',
 th=('#0E7490','#F0F9FF','#082F49','#FDE047','#BAE6FD'),
 rows=[('“Pasupōto o misete itadakemasu ka?”','May I see your passport? Visitors without a Japan address are asked for passport details — hotels often copy it.','Here you go: Hai, dōzo'),
       ('“Shukuhakuzei ga kakarimasu.”','An accommodation tax applies. Tokyo (Nov 2026): ¥0 under ¥10,000/night, ¥100–200 above. Other cities differ.','Included? Yoyaku ryōkin ni fukumarete imasu ka?'),
       ('Check-in & check-out','Check-in is often from 2–3 p.m., check-out around 10–11 a.m. Your booking is what counts.',''),
       ('“Chōshoku wa o-tsuke shimasu ka?”','Would you like to add breakfast? Some hotels include it free.','Yes: Onegai shimasu · No: Kekkō desu'),
       ('“O-nimotsu o o-azukari shimashō ka?”','Shall we keep your luggage? Many hotels hold bags before check-in or after check-out.','Yes please: Onegai shimasu'),
       ('Didn’t catch that?','Ask them to repeat, slowly.','Mō ichido, yukkuri onegai shimasu')],
 note='Checked Nov 23, 2026 (MHLW, Tokyo Tax Bureau, hotel FAQs) · rules vary by hotel and city',ml='➕ Follow for #4: drugstores'),
'drug':dict(out='ig-ask-drugstore',tag='WHAT STAFF WILL ASK YOU · #4 OF 4',title='What drugstore staff<br>will ask you 💊',
 th=('#6D28D9','#FAF5FF','#2E1065','#86EFAC','#DDD6FE'),
 rows=[('“Menzei ni nasaimasu ka?”','Tax-free? New since Nov 1, 2026: pay full price with your passport, get the tax back after customs when you leave.','Usually ¥5,000+ (before tax), same shop, same day'),
       ('At the airport','Do the customs check before you check in your bags — and keep every item from that purchase. Used items don’t qualify.',''),
       ('“Pointo kādo wa omochi desu ka?”','Do you have a point card?','No: Motte imasen'),
       ('“Fukuro wa go-riyō desu ka?”','Need a bag? Plastic bags cost a few yen.','No bag: Fukuro wa irimasen'),
       ('“O-shiharai wa?”','How will you pay? Say the method in one word.','Cash: Genkin de · Card: Kādo de'),
       ('Not sure your card works?','Ask first — accepted payments vary by shop.','Kādo wa tsukaemasu ka?')],
 note='Checked Nov 23, 2026 (Japan Tourism Agency, Customs, METI) · varies by shop',ml='➕ Follow for more Japan tips'),
}
A=sys.argv[1] if sys.argv[1:] else 'ticket'; D=J[A]; C1,BG,TX,AC,SH2=D['th']
rows=''.join(f'''<div class=r><i>{n+1}</i><div class=tx><div class=h>{h}</div><div class=d>{d}</div>{f'<div class=p>{p}</div>' if p else ''}</div></div>''' for n,(h,d,p) in enumerate(D['rows']))
CSS=f'''@font-face{{font-family:I;src:url({F}/Inter-ExtraBold.ttf);font-weight:800}}@font-face{{font-family:I;src:url({F}/Inter-Bold.ttf);font-weight:700}}@font-face{{font-family:I;src:url({F}/Inter-Regular.ttf);font-weight:400}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;background:{BG};font-family:I,'Noto Sans CJK JP','Noto Color Emoji',sans-serif;color:{TX};overflow:hidden;position:relative;display:flex;flex-direction:column}}
.hd{{background:{C1};color:#fff;padding:30px 56px 24px}}.hd small{{font-weight:800;font-size:24px;letter-spacing:3px;color:{AC}}}.hd h1{{font-weight:800;font-size:58px;line-height:1.04;margin-top:6px}}
.list{{flex:1;padding:16px 40px 0;margin-bottom:128px;display:flex;flex-direction:column;gap:12px}}
.r{{display:flex;gap:20px;background:#fff;border-radius:22px;padding:12px 22px;box-shadow:0 3px 0 {SH2};flex:1;align-items:center}}
.r i{{flex:none;width:58px;height:58px;border-radius:50%;background:{C1};color:#fff;font-style:normal;font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center}}
.tx{{flex:1}}.h{{font-weight:800;font-size:32px;line-height:1.1}}.d{{font-size:22px;line-height:1.28;margin-top:3px;color:#3f3f46}}
.p{{display:inline-block;margin-top:6px;background:{AC};color:{TX};font-weight:700;font-size:21px;padding:5px 14px;border-radius:20px}}
.note{{position:absolute;left:40px;right:40px;bottom:88px;font-size:18px;color:#71717a}}
.ft{{position:absolute;left:40px;right:40px;bottom:24px;display:flex;justify-content:space-between;align-items:center}}
.ft .m{{font-weight:800;font-size:24px}}.ft .c{{background:{C1};color:#fff;font-weight:800;font-size:25px;padding:14px 24px;border-radius:40px;white-space:nowrap}}'''
HTML=f'''<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=hd><small>{D['tag']}</small><h1>{D['title']}</h1></div>
<div class=list>{rows}</div><div class=note>{D['note']}</div>
<div class=ft><div class=m>{D.get('ml','📌 Save for your trip')}</div><div class=c>💬 Comment JAPAN for my free guide</div></div></body></html>'''
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350}); t=R/'tools/_ht.html'; t.write_text(HTML); pg.goto(t.as_uri()); pg.wait_for_timeout(600)
    h=pg.evaluate("document.querySelector('.list').getBoundingClientRect().bottom"); pg.screenshot(path=str(R/f"assets/{D['out']}.png")); b.close(); t.unlink(); print('ok',A,'list bottom',h)
