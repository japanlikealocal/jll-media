# Japan Like a Local — Reel Rule Book

Claude reads this before making every reel. Add a line to "Learnings" after each reel.

## Audience & voice
- First-time foreign visitors to Japan. English only.
- Run by a Japanese local. Never pretend personal experience ("I always…") unless Zero actually said it.
- No overgeneralizing: use "often / many / may", and end with a "rules vary" line.
- Facts that change (prices, rules, card sales, hours) must be checked against an official source before posting.

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
- Every reel gets background music. Default: Claude's generated BGM (music.py). Firefly soundtrack to be tested.

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

## Don'ts
- Don't copy other accounts' topics, wording, or designs. Borrow strategy only.
- Don't post the same template forever — vary format gradually.

## Pre-send checklist (check EVERY time before handing anything to Zero)
- Pin: image / title / description / alt text / link (Gumroad free) — all five. Check docs/pins.md first so the theme is not a duplicate.
- Reel: slides / caption / hashtags (5) / isAiGenerated / BGM / date & time 21:00 JST / review by separate Claude.
- note & X: every number re-read from the screenshot or record, never from memory. Dates and weekdays re-checked.
- Counts ("N reels", "N days"): count the actual list before writing.
- Don't assume facts about files/photos (orientation, size) — check with a tool.

## Learnings (add one line per reel)
- 2026-10-17: Text-only reels felt plain to Zero; silence felt odd → added photos + BGM starting with trains reel.
- 2026-10-17: BGM-embedded mp4 via Metricool → Instagram plays sound (confirmed by Zero on toilets reel).
- 2026-10-17: Several small mistakes (missing alt text, wrong weekday, wrong count, wrong numbers) → added pre-send checklist.
