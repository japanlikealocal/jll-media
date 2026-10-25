# Japan Like a Local — Reel Rule Book

Claude reads this before making every reel. Add a line to "Learnings" after each reel.

## Audience & voice
- First-time foreign visitors to Japan. English only.
- Run by a Japanese local. Never pretend personal experience ("I always…") unless Zero actually said it.
- No overgeneralizing: use "often / many / may", and end with a "rules vary" line.
- Facts that change (prices, rules, card sales, hours) must be checked against an official source before posting.

## Cover colors (Zero 10/24: "3つ同じ色だと前みたくなる")
- Rotate accent color per reel: red → blue → green → purple (tools/build_cover.py ACCENTS, accent=...). Tag box + highlighted word + logo dot use the accent. Never 2 neighbors in the grid with the same accent. Log the accent used in handoff.
- Zero 10/24 (grid screenshot): two dark-photo reels side by side (tax-free & trains, both yellow tag + red word) look the same; the infographic between them saved it. Rule: alternate post TYPES in the grid (photo reel → bright image post [cheat sheet / VS comparison] → photo reel), and alternate photo brightness (dark ↔ bright photo). Never two dark-photo reels with the same accent next to each other.

## Reel format v3 (Zero via Perplexity, 10/22 07:28 — study of popular foreign-facing Japan travel reels; replaces "background image on every slide")
- 15–30 s. First 1–3 s shows the actual place (torii/chozuya, konbini shelves, onsen steam…), never a plain card.
- Cut about every 3 s (title cut → detail cut per tip); never hold one screen long.
- Content = "know before you go" list. Do NOT write "Things I wish I knew" (implies personal experience Zero hasn't stated) → use "Know this before…" style. Add nothing beyond the facts.
- Posting: location tag every time (Tokyo, Japan etc.) — Metricool can't set it → Zero posts in the Instagram app (also adds a different trending song).
- Hashtags: #JapanTravel #VisitJapan #TravelJapan + 2 theme tags (#Onsen #Konbini …) = 5.
- Caption CTA: "Save this for your trip" + keep "link in bio" line.

## Cover / hook (slide 0) — v2 from 10/22 (Zero: old covers "nobody would be interested")
- Vivid, travel-feeling photo (Pexels first). Not commuter backs or plain cream cards.
- Big benefit/loss hook in 2–3 lines (e.g. "Don't lose your tax refund", "3 train mistakes to avoid") + yellow tag + one small line. Text inside y 240–1680 (3:4 grid crop) and above the view counter. Builder: tools/build_cover.py.
- Last slide: what the free guide contains + big red "👉 Free guide: link in bio" (profile visits were 0.8% of views, link taps 0).

## Hook (slide 0)
- One short question to the viewer: "First train ride in Japan?" style.
- Try "Why…?" hooks and "Don't lose money / avoid mistakes" hooks (from saved YouTube learnings).
- The hook must promise exactly what the slides deliver.

## Structure
- 5 slides: hook / 3 tips / "before you go" + CTA. 20–23 s total.
- Each tip: short title + one or two sentences. Where possible add the "why" behind the rule.
- CTA text is fixed: "Save this for your trip! Free 1-page Japan Quick Start: link in bio".

## Visuals
- 1080×1920, brand mark at top, safe area left 90 / right 190 / top 300 / bottom 520.
- Photo slides: Firefly Image 5 (Adobe model, commercially safe), vertical 9:16.
  Prompts must say: no legible text, no logos, blur any signage, people from behind or out of focus.
  Specify Japan-only details (silver train with stripe, yellow tactile paving, flap gates, long bench seats…).
- After generating, check: fake kanji, wrong symbols, finger count, unsafe behavior.
- Text sits on a cream card (rgba 247,243,236,.94) over photos.

## Audio
- Every reel gets background music. **music.py BGM is retired (Zero 10/22: "same song every time, absolutely no").** Use a different Instagram trending track each time (Zero adds it in the Instagram app, or Metricool audioConfiguration if available). Never reuse the same track two reels in a row.

## Posting
- Instagram via Metricool, 21:00 JST, REEL, showReelOnFeed true, autoPublish true.
- isAiGenerated = true when photoreal AI images are used; false for text-only.
- Caption: hook + "3 things to know:" list + rules-vary line + CTA + 5 hashtags (#japantravel #japantips … #firsttimeinjapan).
- Every reel and caption is reviewed by a separate Claude before scheduling.

## Instagram role & links (Zero's rules 5–6, 2026-10-18, agreed with Perplexity)
- Instagram = entry point for first-time foreign visitors. English only.
- The hook makes the tip/problem of THIS video clear. Do NOT use the "45-year-old carpenter / AI beginner" diary angle as the main hook here.
- Never promise content or results the video doesn't cover.
- Instagram always leads to the Gumroad free guide. Keep the bio link as is.
- In captions, point to the bio in English ("Free Japan travel guide — link in bio" style). Never replace it with the Japanese note link.
- Don't imply the free guide contains info it doesn't.

## Media roles (don't add posts, just keep roles)
- Instagram reels: entry for new people (English, foreign visitors) → Gumroad
- note: turns readers into fans (Japanese diary)
- X: small failure memos and talking with readers (Japanese)

## Measuring (Zero's rules 1–3)
- Per-post impressions are cumulative since publishing. Never compare posts of different ages directly.
- note: record impressions/PV at ~24 h after publishing for each article (in docs/metrics.md) and compare with the previous day. Ignore same-day partial numbers.
- Reels: judge by plays (views) and profile visits. Not likes.
  Metricool gives reel views/reach/saves automatically; profile visits are NOT available in Metricool (deprecated) → need a screenshot from the Instagram app.

## note & X (Zero's rule 4)
- Not a status report. Pick ONE "tried / failed / learned" thing from yesterday and put it in the title and opening.
- Title format: 「45歳・AI初心者N日目。【やったこと】をやった結果、○○だった」
- Don't make "views dropped" or "0 yen sales" the main point. Never add experiences or results that aren't recorded.
- ALWAYS add 5 hashtags to every note, written as the LAST line of the body text (Zero pastes them in the body) (base: #AI副業 #45歳からの挑戦 #AI初心者 #日本旅行 + 1 matching the day's theme, e.g. #Instagram / #Pinterest). Keep one main theme, but also add a 「■ ほかにやったこと」 section so the article has real substance (aim ~1,000+ chars). Learned 10/19: Day16/18 (5 tags, ~1,300-1,500 chars) got ~130 impressions; Day27 (no tags, ~250 chars) got 10. Automation must not mean cutting content.
- note STYLE (Zero, 10/20): must NOT look AI-written. Polite です/ます (no タメ口). Open with 「おはようございます、ゼロです。」 and the body condition in Zero's words. Diary prose paragraphs, NO templated ■ headings, few/no bullets, vary sentence length. Close to Day16 style. Zero's feelings only as he said them. 5 hashtags as the last line.
- Morning routine output: ① 24h numbers table ② note title ×3 + opening ③ X post (≤140 chars) ④ reel caption check.

## Images / Firefly (Zero's rules, 2026-10-18 — apply after subscribing to Firefly Standard)
- Currently FREE plan (about 3 generations/day, resets daily). Not subscribed yet.
- Facts Zero checked in Adobe's official credits FAQ (Claude couldn't open the page body to re-check):
  Standard (¥1,580/mo) = unlimited "standard generation" only. Firefly Image 5 = premium, 10 credits each.
  2,000 credits/mo, no rollover → Image 5 ≈ 200/mo. Unlimited campaign = Pro and above only.
- First decide if a standard model is enough. Banners/supporting images → standard model.
- Image 5 only for images that drive results. Reel cover (slide 0) = always Image 5; photos inside reels = Image 5 while credits are plenty, standard when low.
- Log each Image 5 use; report "remaining X/200" every morning. When low, suggest reusing images / standard model first.
- Billing/reset date: Zero said "16th of every month", but it's usually the signup date — confirm on the signup screen.
- When to subscribe (Claude tells Zero): free limit means reels are scheduled only up to tomorrow / one reel stuck 2+ days on redos / reel numbers grow and Zero wants more posts.

## Pins: paid guide test (10/19, Zero agreed)
- From 10/20 the paid guide is v2 = 21 pages (Updated November 2026). Never write "13-page" again.
- Of the 3 daily pins, 1 links DIRECTLY to the paid guide (https://zeroailog.gumroad.com/l/wsqkjk) with a product-style design (tools/pin_paid_guide.html). Never claim anything not on the product page. Compare Gumroad views/sales of the paid product weekly.

## 2-funnel evaluation (Zero via Perplexity, 2026-10-21)
- Foreign funnel: Instagram reels + Pinterest → Gumroad free guide (English). Japanese funnel: note + X → AI challenge diary (fans). Evaluate separately.
- Instagram: per reel views + profile visits (not likes). Gumroad: free downloads (don't claim "from Instagram" unless Gumroad shows it).
- note: impressions + PV at 24h per article, compare with previous day. Build up day by day.
- Rules of thumb:
  - Reel views up 3 in a row → hook style works, keep it for next 3. Flat 3 in a row → change only the hook.
  - Profile visits < 1% of views for several reels → push "link in bio" in reel AND caption every time (already in both; then make it stronger/earlier).
  - note 24h imp below median of last 3 days → rethink title + opening. Above → keep the format.
  - For the first 2 weeks, never conclude "wait and see" from small numbers alone; don't judge sales yet (grow the entry numbers first).
- Compare reels only at the same age (24h), per Zero's rule 1.

## X test plan (Zero + Perplexity research 10/21 → docs/research-x-2026-10-21.md)
- Goal: X impressions (Day29 post showed no view count = ~0). Change ONE thing at a time, post ~07:30 JST every day, compare views at 24h.
- Step 1 (10/21 Day30): note link moved from body to self-reply. Body must be worth reading alone.
- Step 2: add 1 image (a real screenshot of the day's result) — only after Step 1 has 24h data.
- Step 3: first line = the result with a number; "45歳・AI初心者N日目" moves to the end as a name tag.
- Always: end with a short question to readers (replies weigh ~10x likes per public-code analysis). 0–2 hashtags on X.
- Log in metrics.md: views @24h, replies, likes, note PV from X.

## Don'ts
- Don't copy other accounts' topics, wording, or designs. Borrow strategy only.
- Don't post the same template forever — vary format gradually.

## Pre-send checklist (check EVERY time before handing anything to Zero)
- Pinterest alt text must be UNDER 500 characters (10/22 20:00 pin failed: 400 Invalid request, alt text too long). Count with len() before scheduling.
- After scheduling, re-check Metricool status the same day (getScheduledPosts) — ERROR does not notify anyone.
- Pin: image / title / description / alt text / link (Gumroad free) — all five. Check docs/pins.md first so the theme is not a duplicate. Hand them to Zero in the Pinterest form order: title → description → link → alt text.
- Reel: slides / caption / hashtags (5) / isAiGenerated / BGM / date & time 21:00 JST / review by separate Claude.
- note & X: every number re-read from the screenshot or record, never from memory. Dates and weekdays re-checked.
- Counts ("N reels", "N days"): count the actual list before writing.
- Don't assume facts about files/photos (orientation, size) — check with a tool.

## Learnings (add one line per reel)
- 2026-10-21: Hook test from trains reel (10/22): slide 0 = full photo + one big line on dark band + small "3 rules to know" line, photo-only slow zoom 6% over 2.5s (text static, stays in safe area). Reason: 3s+ rate best on konbini 18%/toilets 15% vs taxi 0%/trash 5.7% (few samples, not proven). Compare 3s+ rate at 24h.
- 2026-10-19: Firefly sometimes resets to Gemini model + 'Auto' ratio, and the old prompt stays in the box → always check model, 9:16 and prompt on a screenshot BEFORE pressing generate (lost 1 credit).
- 2026-10-17: Text-only reels felt plain to Zero; silence felt odd → added photos + BGM starting with trains reel.
- 2026-10-17: BGM-embedded mp4 via Metricool → Instagram plays sound (confirmed by Zero on toilets reel).
- 2026-10-17: Several small mistakes (missing alt text, wrong weekday, wrong count, wrong numbers) → added pre-send checklist.

## 写真を暗くしすぎない（10/24 ゼロ「ラーメンが暗くて見づらかった」）
- 写真全体に黒いグラデーションをかけない。暗くするのは文字の後ろだけ（文字の下に白か半透明の帯を敷く方法でもOK）。
- 主役（料理・景色）が写る場所には影を乗せない。もとの写真が暗い時は明るさを少し上げる。
- 書き出したら、主役がはっきり見えるかをスマホの大きさで確認してから渡す。

## 「写真が主役」と「文字が主役」でメリハリ（10/24 ゼロ）
- 場面ごとに、主役を写真か文字のどちらか1つに決める。
- 写真が主役の場面（料理・景色など）：写真は明るいまま大きく見せる。文字は短く（3〜4語）小さめにして、画面の端に小さな帯で置く。表示時間はやや長め。
- 文字が主役の場面（ルール・手順・数字）：写真は大きくぼかすか暗くするか単色の背景にして、文字を大きく真ん中に置く。
- 1本の中で交互に並べる（写真で見せる→文字で教える→写真で見せる）。同じ場面に、大きな文字と見せたい写真を両方入れない。

## 画像投稿はリールにする（10/26 ダッシュボードで判明）
- フォロワー0のうちは、画像投稿（POST）はほぼ誰にも届かない（30日で投稿の閲覧1、Japan vs USA・20 Thingsは0回）。リールは643。
- 一覧画像を作ったら、tools/build_image_reels.py で10秒のリール（ぼかし背景＋ゆっくりズーム＋上に一言＋下に「Save it · Comment JAPAN」）にしてから出す。Metricoolの自動投稿（曲なし）でOK。
- 週1回（日曜朝）、ゼロにインスタのプロフェッショナルダッシュボードのスクショ（ホーム／パフォーマンス2枚／コンテンツ）をもらう。
