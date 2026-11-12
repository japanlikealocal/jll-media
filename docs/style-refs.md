# 参考アカウントの「型」メモ（ゼロが見つけた投稿、10/25）
※他人の画像はリポジトリ（公開）に置かない。ここには「型」だけ文章で残す。画像・文章の流用はしない。

## tokyo_hacklife（東京ハック）— 日本人向け「保存版 〇〇選」
見た投稿と反応（いいね/シェア、10/25時点）：ラーメン28選 1,699/490、イルミ15選 1,502/495、蕎麦25選 849/33、和食18選、うどん25選 409/34、土産15選 402/23、休憩スポット24選 322/26、チル25選 181/28、雨の日10選 81、秋さんぽ6選 11、占い10選 2
→ 伸びるのは「食べ物」「季節イベント」。数が多い（15〜28）ほど保存・シェアが多い。占い・公園は弱い。

### 型
- タイトル：「保存版」バッジ＋「東京の〇〇 N選」＋サブ1行（例「頼む一品つき」「エリアごと」）。数字は大きく赤。
- 絵：AIの水彩イラストで全コマ統一（実写真なし）。「イラストはイメージです」と明記。
- コマ：3〜5列の番号付きカード。中身は「店名／エリア（色付きタグ）／推しの一品か一言」。写真が主役、文字は小さく。
- エリア別の色見出し（新宿・渋谷…）で区切るタイプもある。
- マスコット（東京くん）を見出しの角に。吹き出しで一言。
- 下：「保存して、次の〇〇に。」＋アカウント名＋「◯月◯日確認／ランキングではありません／最新情報は公式へ」。
- 季節で背景を変える（雨・紅葉・雪・星空）。

## yononaka_tier — 「0円の絶景スポット12選」
- 「◯◯円払わなくてもいい!?」という損得の切り口。黄色いギザギザの「0円」マーク。夜景写真×濃紺×赤×黄。

## うちでの使い方（外国人向け英語版）
- タイトル：「📌 SAVE THIS」＋「Tokyo 〇〇: N spots」＋サブ1行。
- 絵：ChatGPTに「12コマ（3×4）、白いすき間、文字なし」で1枚に描かせ、Claudeが切り分け（tools/build_illumi.py が見本）。
- マスコット：侍を見出しの角に小さく（子供っぽくならないよう大きくしない）。
- 必ず：確認日、Illustrations are for reference、FREE/PAID、💬 Comment JAPAN のマス。
- Pinterestは同じ素材を 1000x1500 で作る（build_illumi.py が両方出す）。

## 次の候補（伸びた順に）
1. Tokyo Souvenirs（お土産）— 免税とつなげられる
2. Tokyo Ramen by area（外国人に一番人気。店名は公式確認が必須）
3. Rainy day in Tokyo（屋内スポット）
4. Free rest spots in Tokyo（休憩スポット）— 歩き疲れた旅行者向け

## 2026-11-01 Zero's saved tokyo.hack posts (all the same 4x4/4x5 watercolor list format)
- 東京の名店うなぎ屋16選 — **466 likes, 55 shares** (best) / 寿司の名店20選 — 199 likes, 16 reposts / 和食屋16選 — 21 likes / 会社帰り飲食店16選 — 8 / ラーメン名店12選 — 8 / うどん20選 — 10 / 工場見学20選 — 16.
- Pick for us: **Unagi spots (historic shops, near stations)** next; ramen after. Sushi list = mostly high-end/hard-to-book → not useful for first-timers. Factory tours = reservation/Japanese-only issues.

## 2026-11-02 Zero's saved posts (22 screenshots) — likes
- **関東VS関西 食べ方の違い8選 (shittopi817) 1,600 likes / 225 reposts / 187 shares** ← biggest. Comparison format + "comment your region" CTA.
- 東京の焼き鳥百名店15選 (tokyo_lux_gourmet) 776 / 53 / 163 shares. 中国料理百名店15選 359. 天ぷら百名店12選 199. Elegant beige watercolor, "百名店" authority.
- おしゃれカフェ16選 (tokyo.hack) 161. グルメinfo 東京ランチ10選 137. ミシュラン7選 132. おでん12選 73. 1000円台ランチ 65.
- jiha_gourmet dark/red "駅おすすめ6〜8選" with tabelog score: 6–99 likes (weak). Kids/pancake/date lists: 2 likes.
- Takeaways for us: (1) yakitori / tempura / cafe are strong next topics; (2) **comparison format "Tokyo vs Osaka: 8 eating differences" for foreigners** — comment-bait ("which side are you?"); (3) authority words (Michelin/百名店) lift saves, but only if verified.

## 2026-11-09 Zero's saved IG posts (20 screenshots) — patterns only, do not copy designs
- Biggest numbers: free factory tours "見学0円" 12 picks (4,037 likes / 1,313 shares) > onsen-town TIER list SSS/SS/S/A (1,302 / 281 shares) > "Beyond Tokyo" day-trip carousel 20 slides (1,133) > "Tokyo 100 things" carousel 11 slides (630).
- Common format: big title with a number (12/15/16/20) + "2026 / 保存版", numbered grid, each cell = name + station + price range + one-line reason, small disclaimer "AI illustration / check official info / checked on DATE". Many label themselves "AIコンテンツ".
- Hooks that spread: FREE (0円), ranking/tier list, "once in a lifetime", series split across many slides ("100 things" parts 1–11), a mascot character.
- Several big accounts post in Traditional Chinese for Taiwan/Hong Kong visitors (maison.shirley, fattsai, crystal_hongkong) → TW/HK is an active audience we don't serve yet (we are English-only).
- Ideas for us: (1) "FREE in Tokyo" lists, (2) tier lists (ramen, onsen towns near Tokyo), (3) a Traditional Chinese test version of our best post (translation checked by Perplexity), (4) a numbered series ("50 things in Tokyo" part 1/5…). Avoid brand logos/characters in our art.
- Batch 2 (same day): **Kanto vs Kansai food differences 8 (part 2) = 1,579 likes / 155 reposts — top of all saved posts** → confirms our comparison format; "part 2" sequels work; ends with "tell us your region in the comments". Hotel free services 12 (1,147, all "0円/無料"). Shrine tier list 25 (SS–C). Daily series "Yamanote line gourmet Day1, Day2…" (16 shops per station). English "12 must-visit Japanese chain restaurants" (330 likes, 133 shares) → chain-restaurant guide for foreigners is a proven topic (we must not use brand logos; names + our own art only). "Common manner myths 8 — 実は…" format with true/false answer. Skip posts that spread unverified health claims.

## 2026-11-13 ゼロの保存投稿（9本）から
- 最多：tokyo.experiences「5 DAYS IN TOKYO」英語の路線図風ルートマップ（いいね1,398・リポスト64、カルーセル7枚、外国人向け）→ うちの客層に一番近い。
- 多国グリッド型が強い：「世界の武術図鑑 15選」376、「こんなものが本当にない国」382、「世界12か国のネットの笑い方」309、「世界三大〇〇10選」168。1枚に国旗＋国名＋1行で多くの国を並べる。
- 日本の地域差「日本の謎文化8選」250（国内向け）。
- 使わない：実在の政治家・指導者の顔を使った軍事比較（政治・実在人物はやらない）、有名人に似せたAI人物。
- 次の案：①英語の「Tokyo in 3/5 days」路線図風マップ（食べ歩きマップへ誘導）②「Japan vs the world」多国グリッド（例：チップ・緊急番号・プラグを12か国並べる→1本で多くの国の人に刺さる）③「Things Japan doesn't have / does differently」。どれも事実確認（Perplexity）してから。
