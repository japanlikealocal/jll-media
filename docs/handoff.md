# 引き継ぎメモ（2026-10-18 朝時点）

新しいチャットのClaudeへ：最初にこのファイルと `docs/reel-rules.md`、`docs/metrics.md` を読んでから作業すること。

## 10/18 朝の更新（最新）
- Day27のnote公開済み（https://note.com/jtatgd4/n/n458e6aafb61d）、Xも投稿済み。テーマ「YouTube取り込みを作った→続けて取ったら一時ブロック→間を空ける」。
- 朝ルーティンの新ルール（ゼロ＋パープレ）をルール帳に追加：数字の見方（24時間後で比較）、note/Xの書き方、媒体の役割、Instagramの案内先はGumroadのまま。出力は ①24h記録表 ②noteタイトル3案＋冒頭 ③X ④リール概要欄チェック。
- 朝の気持ち4問：①体調 ②昨日の感想 ③昨日いちばん印象に残ったこと ④今日やりたいこと。
- 数字の記録は docs/metrics.md。リールの再生・リーチ・保存はMetricoolで自動取得できる。プロフィール流入はMetricoolで取れない→インスタのアプリのスクショが必要。
- Firefly：10/18朝の時点で「今日の残り0回」。まだ無料プラン（課金はまだ）。課金ルールと課金タイミングはルール帳の Images / Firefly 参照。
- assets/ フォルダは空。電車の表紙・改札の写真はFireflyの履歴からダウンロードし直しが必要。
- パープレはこっちのルーティンを知らない前提。相談するときは前提（インスタは英語・外国人向け等）を一緒に渡す。
- 宿題：Metricoolでストーリーを自動投稿できるか・料金を調べる（ゼロは毎日4本やりたい→まず1日1本から提案済み）。
- リポジトリは書き込み可（/home/claude/jll-media として接続）。

## プロジェクト
- 「AIで最初の1円を作る挑戦」。ゼロ（45歳・造作大工・AI初心者）が運営。
- 商品：Gumroadの英語の日本旅行ガイド。無料版 https://zeroailog.gumroad.com/l/japan-quick-start
- 発信：note（note.com/jtatgd4、毎日「45歳・AI初心者◯日目。」の日記）、X（@zeroailog）、Pinterest（Japan Like a Local）、Instagram（@japanlikealocal.jp、英語リール）
- 売上：まだ0円（Gumroad無料DL 1件はPinterest経由・日本から。ゼロのGumroadで無料版が「購入済み」表示なので、本人のテストの可能性が高い）

## ゼロとの約束（大事）
- タメ口。説明は短く、PC操作は1操作ずつ。
- ゼロの手作業を最小に。最終的に「完成品にOKを出すだけ」が目標。
- ゼロの気持ちは本人が言ったことだけ使う。作らない。
- 確定と未確定を分けて話す。数字・日付・曜日は記録から書き写す（記憶で書かない）。
- 渡す前に `docs/reel-rules.md` のチェックリストを確認。リール・キャプション・note文は別のClaude（サブエージェント）にチェックさせてから渡す。
- 調べもの：Claudeが公式情報で確認＋パープレキシティ（ゼロが課金済み）でダブルチェック。チャピー（ChatGPT）は解約済み。
- 課金はOKだが、効果が見えるものから1つずつ。月の上限を決める提案済み。
- 個人アカウント連携（Facebook等）はしない方針。

## Instagram自動投稿の仕組み
- 動画を作る → このリポジトリ（public）の reels/ に置く → raw.githubusercontent.com/japanlikealocal/jll-media/<commit>/reels/<file>.mp4 → Metricoolコネクタで createScheduledPost（blogId 7378020, Asia/Tokyo, 21:00, REEL, showReelOnFeed true, autoPublish true）
- AI写真を使うリールは isAiGenerated true。
- git commit は user japanlikealocal / japanlikealocal@users.noreply.github.com。
- Metricool無料プランは月20投稿まで。

## 予約状況（10/17夜）
- 公開済み：10/13 外食、10/15 ゴミ、10/16 温泉、10/17 トイレ（BGM入り、音が鳴るのをゼロが確認）
- 予約済み（全部BGM入りv3、21:00）：10/18 荷物、10/19 タクシー、10/20 コンビニ、10/21 神社・お寺
- 次の枠：10/22 電車、10/23 免税（どちらも作成途中）

## 作成途中
1. 電車リール（plans/trains-plan.md）：表紙と改札はFireflyで作成済み（assets/）。3枚目「車内」の写真が未作成 → 作って完成、BGMを付けて10/22に予約。
2. 免税リール（plans/taxfree-plan.md）：文章はレビュー済み（観光庁・JNTO・大阪税関で確認）。Firefly写真を作って10/23に予約。11/1開始なので急ぎ。
3. Pinterest：今日の免税ピン（assets/japan-taxfree-pin.png）はゼロが10/17夜に投稿済み（リンク先のGumroad無料版も表示OK）。毎日1枚。テーマは公開済み一覧を確認してから選ぶ。

## Firefly（画像）
- ゼロがPCで firefly.adobe.com を使う（アカウント LikeALocal Japan）。モデルは必ず「Firefly Image 5」（Adobe製・商用OK）、縦長9:16。
- 無料は1日3回くらい。ダウンロードは720×1280。
- ゼロは画像をCtrl+Jのダウンロード一覧からチャットへドラッグして送る。PCスクショは Windowsキー+Shift+S → Ctrl+V。
- Adobeコネクタでは文字→画像の生成はできない（生成拡張などのみ）。
- Fireflyの音楽機能でBGMを作る案も試す予定。

## BGM
- tools/music.py で自動生成（著作権なし）。ゼロの評価は「ないよりマシ」。Firefly音楽が良ければ切り替え。

## YouTube取り込み
- ゼロがリンクを貼る → tools/grab.sh で字幕取得（yt-dlpはGitHubのreleasesから取得：github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp）→ サブエージェントで要約 → メモリの /topics/saved-youtube.md に追記。
- 連続取得するとYouTubeに一時ブロックされる。間を空ける。androidクライアントで通ることがある。
- 許可ドメインに *.youtube.com, youtu.be, *.googlevideo.com, *.ytimg.com, *.adobe.com, *.adobe.io, *.amazonaws.com, *.pexels.com を追加済み。

## 調査・ネタ
- docs/topic-bank.md：ネタ100本（上位14本が次の2週間の候補）
- docs/research-2026-10-17.md：訪日系の調査（免税の変更、JR Pass値上げ、よくある悩み など）
- YouTubeからの学び：ルール帳を育てる／小さいアカウントの異常値を探す／「なぜ？」「損しない」フック／ファン化

## 明日（10/18）やること
1. 朝：Day27のnoteとX。ゼロに気持ちを4つ聞く（体調、昨日の感想など）。昨日（Day26）の主な出来事：YouTube取り込みの自動化、Fireflyで写真2枚、BGM付け替え、ルール帳・ネタ帳・調査、免税ネタ発見、チャピー解約→パープレ課金。
2. Firefly 3回：電車の車内、免税の写真、BGM。
3. 電車（10/22）・免税（10/23）を完成→チェック→予約。
4. ピン1枚。

## ツール
- tools/ にスクリプト一式。build系はCSSを tools/reel.css から読むようにパスを直して使う。

## Metricoolストーリー調査（10/18夜）
- 公式ガイド：Instagramストーリーの自動投稿はできる（写真・動画とも）。ビジネスプロフィールが必要。
- できないこと：投票・質問・リンクなどの「スタンプ」付きストーリーは自動投稿できない（InstagramのAPIの制限）。スタンプを使う場合は、自動投稿をオフにして通知を受け取り、手で投稿する。
- 料金（公式・税抜）：Free 0円（1ブランド・予約投稿 月20件）／Starter 月€20・$25（年払いだと月€16・$20）予約投稿無制限（フェアユースあり）。
- 未確認：無料プランでストーリーの自動投稿が使えるか／ストーリーも月20件に数えられるか／月20件のリセット日。
- 注意：リールを毎日1本出すと月30件前後になり、無料の月20件を超える。11月はStarterにするか、本数を減らす判断が必要。
- 出典：https://metricool.com/schedule-instagram-stories/ ・ https://metricool.com/pricing/
- 決定（10/18）：Metricool課金は10月中にリールの数字を見てから決める。10/28朝にClaudeから「課金するかリールを減らすか」を提案する（このチャットに予約メッセージあり）。課金した方がいいタイミングになったらClaudeから伝える。
- 確認済み（10/18夜）：有料版「JAPAN LIKE A LOCAL - First-Time Visitor Guide」($4.99, zeroailog.gumroad.com/l/wsqkjk, 販売0)は公開中。無料版の商品説明の最後と、無料版PDFの下部の両方に有料版への案内・リンクがすでに入っている。→ 導線はある。課題は流入数（Gumroad閲覧 月26回）。
- 注意：WebFetchでGumroadの商品ページを読むと説明文が途中までしか取れない。「載っていない」と判断する前に、ゼロの編集画面のスクショで確認する。
- 決定・実行（10/18 21:07）：Metricool Starter 5（月払い 25 USD、日本で税0）に課金済み。次回支払い 11/18。予約投稿は無制限（フェアユースあり）。10/28のリマインドは不要になったので取り消し。
- Pinterest（Business account zeroailog45 = Japan Like a Local）をMetricoolに接続済み。方針：ピンを1日3枚にして、Claudeが作成→別Claudeでチェック→Metricoolで予約・自動投稿。ゼロの作業はなし。テーマは docs/pins.md で重複確認。
- ゼロの依頼（10/18）：Instagramの数字はClaudeが毎朝把握して改善する。毎朝Metricoolから前日リールの24時間後の数字（再生・リーチ・保存・シェア・平均視聴秒数・3秒以上視聴率）を取って docs/metrics.md に記録し、朝ルーティンの①で報告する。週1回（日曜の朝）、数字をもとに「次に試すこと」を1つ提案する（フック・表紙・長さ・投稿時間など）。プロフィールへの流入はMetricoolで取れないので、必要な時だけゼロにスクショを頼む。
- 10/18時点のフォロワーは0（Metricool画面で確認）。
- 音楽のお試し（10/18決定）：ゼロの希望で、流行りの曲をインスタのアプリ内で付ける回を試す。有名曲をmp4に埋め込むのは著作権の理由でやらない。ビジネスアカウントでもアプリ内で曲を付けられることは確認済み（「NEON」A2O を選べた）。やり方：電車リール（10/22）を音なしで作ってチャットに送る→ゼロがスマホに保存→インスタのアプリで曲を付けて21時に手動投稿→自動BGMの回と再生数を比べる。
- MetricoolのiPhoneアプリはインストール・ログイン済み。ただし「Device settings」で名前を入れてもSaveが押せず、手動投稿の通知設定は未完了。お試しは上のやり方なら通知設定なしでできる。
- 10/19：ピン3枚をMetricoolで予約（12:00 靴、17:00 エスカレーター、22:00 落とし物）。ボード「First Trip to Japan」= boardId 1123507506982290704。画像は raw.githubusercontent.com/japanlikealocal/jll-media/<commit>/assets/… を使う。文章は docs/pins_YYYY-MM-DD.json。自動でちゃんと出たかは次回確認する（初めての自動ピン）。
