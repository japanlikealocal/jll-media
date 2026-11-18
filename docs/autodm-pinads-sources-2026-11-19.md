# Instagramコメント自動DMとPinterest広告：日本アカウントの事実確認

確認日：2026年11月19日。公開の公式資料を優先した。個別アカウントでのログイン、配信、購入、課金は行っていない。「一部違う」は想定している条件をそのまま言い切れない場合、「確認できない」は公開資料で数字や対象範囲を確定できなかった場合。

## Instagramのコメントから自動DMを送る

### 特定の言葉に反応して無料でDMできるか

**判定：正しい。** ManychatのFreeは、Instagramの投稿・リールへのコメントを起点に会話を始める自動化に対応する。Quick Automationの「Auto-DM Links from comments」では対象の投稿・リールを選び、コメントに含まれる語を `JAPAN` などに指定できる。「すべてのコメント」に反応させる必要はない ([ManychatのFreeプラン](https://help.manychat.com/hc/en-us/articles/25800197498652-Free-plan)、[コメントから自動DMの設定](https://help.manychat.com/en/articles/17742037-quick-automation-auto-dm-links-from-comments))。

最初のDMでリンクを渡すだけなら、Quick AutomationでOpening DMをオフにして、リンク付きのメインDMを最初に送る設定がある。Opening DMをオンにした場合は、受信者がそのボタンを押してからリンク付きの本編が届く。Metaの仕様ではコメントへの最初の非公開返信は1通で、相手の反応なしに追加DMを続けられない。フォローしていない相手にはメッセージリクエストに入る場合があるので、別アカウントで受信もテストするとよい ([Manychatの設定ガイド](https://help.manychat.com/en/articles/17742037-quick-automation-auto-dm-links-from-comments)、[MetaのPrivate Replies仕様](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies))。

### 無料の上限と有料プランの月額

**判定：正しい（現行Freeは25人／月）。** Freeは **1請求サイクルに最大25 Active Contacts**、**同時に最大4件の公開中の自動化**。25はDMの通数ではなく、Manychatを通じてやり取りした人の数。同じ人が同じ月に何度反応しても1人で、カウントは請求サイクルの開始時にリセットされる。初回メッセージにはManychatのブランド表示が入る ([Freeプラン](https://help.manychat.com/hc/en-us/articles/25800197498652-Free-plan)、[Active Contactsの定義](https://help.manychat.com/en/articles/17742213-active-contacts))。

2026年3月2日導入の新料金体系の公式表示は下記の通り（米ドル）。年払い欄は月あたり換算で、実際は1年分を前払い。表示価格と、自分のアカウントで選べるプラン・税や従量料金を含む最終請求額は別 ([料金表](https://manychat.com/pricing)、[プラン比較と地域差](https://help.manychat.com/en/articles/17742215-manychat-subscription-how-to-choose-the-right-one-for-you))。

| プラン | 月払い | 年払いの月換算 | 含まれる人数／月 |
|---|---:|---:|---:|
| Essential | US$17 | US$14 | 250人 ([Essential公式](https://help.manychat.com/en/articles/17742191-essential-plan)) |
| Pro | US$39 | US$29 | 2,500人 ([Pro公式](https://help.manychat.com/hc/en-us/articles/25800228332572-Pro-plan)) |
| Business | US$99 | US$69 | 7,500人 ([Business公式](https://help.manychat.com/hc/en-us/articles/25800254159900-Business-plan)) |
| Advanced | US$199 | US$139 | 25,000人 ([Advanced公式](https://help.manychat.com/en/articles/17742209-advanced-plan)) |

**旧情報との違い：** 「Freeは1,000 contacts」「Proは月US$15から」は旧体系の説明。最新のFree専用ヘルプは**旧登録分を含めFreeはすでに新プランへ移行済み**と明記。一方、旧有料プランの移行・新有料プランの表示はアカウントや地域によるため、既存ユーザーは `Settings → Billing` を優先する。有料プランは含まれる人数を超えると従量料金が発生しうるので、アップグレード時は上限設定も確認 ([Freeプラン](https://help.manychat.com/hc/en-us/articles/25800197498652-Free-plan)、[旧体系のBilling FAQ](https://help.manychat.com/en/articles/17742090-billing-faq)、[プラン比較](https://help.manychat.com/en/articles/17742215-manychat-subscription-how-to-choose-the-right-one-for-you)、[Active Contactsと従量料金](https://help.manychat.com/en/articles/17742213-active-contacts))。

### 日本在住・日本のInstagramアカウント

**判定：正しい（利用を始められる。個別の機能・料金は場合による）。** 日本向けApp StoreにManychatの公式アプリが掲載されており、Instagram接続要件に日本のプロアカウントを除外する記載はない。ただし、日本に関する全機能・全プランの提供保証や、個別アカウントでの動作までは確認していない。日本向けApp Storeにあることと、日本語UI対応は別で、iPhone版の対応言語欄には日本語の記載がない ([日本のApp Store](https://apps.apple.com/jp/app/manychat/id1460129210)、[ManychatのInstagram接続要件](https://help.manychat.com/en/articles/17741886-how-to-connect-instagram-to-manychat)、[地域によるプラン差](https://help.manychat.com/en/articles/17742215-manychat-subscription-how-to-choose-the-right-one-for-you))。

### プロアカウントとFacebookページ

**判定：一部違う。** Instagramは**クリエイター／ビジネスのどちらでも可**。個人アカウントは不可。Facebookページは常時必須ではなく、接続方法を **Via Instagram** にすればMeta BusinessアカウントやFacebookページを前提としない。**Via Meta** はMeta Business Portfolioが必要、**Via Meta Business Suite** は連携済みFacebookページとそのフルコントロール権限などが必要。接続方法によって高度な機能に差がある ([ManychatのInstagram接続ガイド](https://help.manychat.com/en/articles/17741886-how-to-connect-instagram-to-manychat))。

### スマホだけで設定できるか

**判定：正しい（今回の基本設定ならPC必須ではない）。** Manychat公式のiOS／Androidアプリでは、Instagramのコメント自動返信などを新規作成できる。高度な設定にはWeb版が必要な場合があるため、細かな条件分岐などを足す場合はWeb版を使う ([Manychatモバイルアプリの公式ヘルプ](https://help.manychat.com/en/articles/17742025-manychat-mobile-app))。

### Meta公式の無料機能で代用できるか

**判定：確認できない（日本のInstagramリールで同じ動作をするか）。** Meta Business Suiteのデスクトップ版には、投稿へのコメントをきっかけにメッセージを送る **Comment to message** の公式案内がある。別の公式説明ではハッシュタグと説明されており、日本のInstagramリールで `JAPAN` という単語だけを条件に使えるかは、公開ヘルプでは明確でない。Metaは日本・欧州で一部のメッセージ関連機能を利用できない場合があるとも案内している。一方、**Custom keywords／自動返信**は先に届いたメッセージへの返信であり、リールのコメントをDMに変える機能とは別。試すならデスクトップ版の「受信箱 → 自動化」で、対象テンプレートとInstagramが選べるかを見る ([Metaの自動化作成ガイド](https://business.facebook.com/business/help/318238182723007/)、[Metaの受信箱自動化の説明](https://secure.facebook.com/business/help/395965998733706/))。

### Manychat以外の無料ツール

**判定：正しい（提供元が無料枠を明示する候補あり。日本での個別動作は未確認）。** **SuperProfile** は特定のInstagram投稿・リールに1キーワードを設定し、リンク付きDMを返す機能を無料と明記。料金表には投稿・リールへのAutoDMは無制限とあるが、Lead Magnet機能で集められるリードは10件まで。全投稿に一括適用する方式とは別で、外部ツールの無料枠がMeta側の送信制約を取り除くわけではない ([SuperProfile料金表](https://superprofile.bio/pricing)、[無料キーワードDM公式ガイド](https://superprofile.bio/guides/free-instagram-auto-dm)、[Metaの返信仕様](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies))。

**別候補：LinkDM。** 公式料金表では無料でInstagram 1アカウント、月1,000DM。投稿・リール単位のキーワードトリガー自体も公式ヘルプに載るが、無料プランの説明ではキーワード条件まで含むか明示されていないため、完全な代替としては未確定 ([LinkDM料金表](https://www.linkdm.com/pricing)、[LinkDMのトリガー解説](https://www.linkdm.com/help/trigger-types))。

## Pinterest広告：日本の広告アカウント

### 最低日額・最低総額

**判定：確認できない（日本円の一律の最低額）。** 1日予算と配信期間全体の予算は別に設定できるが、確認した公式資料には、日本の広告アカウントの最低日額・最低総額の具体的な円表示がない。各国・目的などに応じた**最低入札額**は存在するが、それは日額や期間総額ではない。広告マネージャーの下書きで配信国・目的・入札方法を入れたうえで、予算欄の表示を確認するのが確実 ([広告グループ公式設定](https://help.pinterest.com/en/business/article/create-ad-group)、[予算設定](https://help.pinterest.com/en/business/article/set-up-campaign-budgets)、[最低入札額](https://help.pinterest.com/en/business/article/set-your-bid))。

### 日本円と使えるカード

**判定：正しい。** JPYは対応請求通貨で、日本発行のカードは対象。公式の対応カードには **Visa、Mastercard、JCB（日本）** が掲載され、**American Expressは国・通貨による**。プリペイドカードとPayPalは非対応。請求通貨を変更するには正しい国・通貨の広告アカウントを新規作成する必要があるため、初期設定時にJapan／JPYを確認する ([Pinterestの対応支払い方法](https://help.pinterest.com/ja/business/article/accepted-payments)、[広告アカウント作成](https://help.pinterest.com/en/business/article/create-an-advertiser-account))。

### 配信国（米国・豪州・ニュージーランド）

**判定：一部違う。** **広告マネージャーの手動キャンペーンでは国別ターゲティングができる**。公式ヘルプでは初期値が事業所在地の国で、個別の国を指定する操作や複数国を選ぶ例がある。一方、**Quick Promoteは自国内を自動で対象**にするので、海外向けの初回テストには使わない。日本アカウントで米国・豪州・ニュージーランドの3か国を個別に選べるかを示す国別対応表までは確認できないため、下書きで候補に表示されるか確認する ([Pinterestの地域ターゲティング](https://help.pinterest.com/en/business/article/location-language-device-and-gender-targeting)、[複数国の入札例](https://help.pinterest.com/en/business/article/set-your-bid)、[Quick Promote公式](https://help.pinterest.com/ja/business/article/quick-promote))。

### 初心者の少額テスト

**判定：正しい（設定は公式仕様、金額・期間は提案）。** 英語の無料マップやガイドのページに誘導するなら、**手動キャンペーン → 比較検討（Consideration）→ 外部クリック（Outbound clicks）→ Performance+入札**。Pinterest内でピンを開くクリックではなく、外部ページに向かうクリックを見たいから。公式では外部クリック最適化にPerformance+入札が必要 ([Pinterestのキャンペーン目的](https://help.pinterest.com/en/business/article/campaign-objectives)、[入札設定](https://help.pinterest.com/en/business/article/set-your-bid))。

**提案：最初は1か国、英語のピン1〜2本、7日間。** たとえば総額3,500円を自分の上限にして、管理画面でその金額が受け付けられる場合だけ試す。これは公式最低額でも、成果が出る予算の保証でもない。総額を守りたいならキャンペーンの **Lifetime spend limit** も確認する。Performance+の日別予算は平均額であり、日によって設定額を最大25%超えて使う場合がある。初回は表示数だけでなく、外部クリック数・1クリックあたりの費用・リンク先での登録を確認する ([支出上限の公式ヘルプ](https://help.pinterest.com/en/business/article/manage-your-spend)、[日別予算の公式ヘルプ](https://help.pinterest.com/en/business/article/set-up-campaign-budgets)、[外部クリックの説明](https://help.pinterest.com/en/business/article/campaign-objectives))。

### 広告審査

**判定：正しい（24時間ほどが公式の目安）。** Pinterestの日本語ヘルプでは初回審査に約24時間かかる場合があると案内。提出後にターゲティングや広告説明文を編集すると再審査となり、さらに24時間かかる場合がある。締切のある配信は前日ぎりぎりに提出しない ([Pinterest日本語版・広告審査](https://help.pinterest.com/ja/business/article/ad-review))。

### 消費税とカード請求

**判定：一部違う（「国内広告だからカード明細に消費税が自動で加算される」とは限らない）。** Pinterestによると、日本拠点の事業者への広告提供元はアイルランドの **Pinterest Europe Limited** で、同社の請求額に日本の消費税は含まれない。国外事業者からのB2Bデジタルサービスとして、購入者がリバースチャージ方式で申告する場合がある。全員が追加納税する意味ではなく、国税庁は一般課税で課税売上割合95%以上、または簡易課税などの取扱いを案内。個別の扱いは自身の課税区分を税理士等に確認する ([Pinterestの日本消費税案内](https://help.pinterest.com/en/business/article/vat)、[国税庁・リバースチャージの申告対象](https://www.nta.go.jp/law/shitsugi/shohi/26/02.htm))。

**カード請求のタイミング：** 通常は広告費が請求基準額に達した時点か翌月1日の早いほう。公式に出てくるUS$50は請求基準額の例であり、最低出稿額ではない。カード決済が成功すると、Pinterestは通常48時間以内に登録した請求先メールへ請求書を送ると案内している。広告費の記録に備えて請求先情報とメールを確認し、請求書を保存する ([Pinterestの請求の仕組み](https://help.pinterest.com/en/business/article/how-billing-works)、[請求書の案内](https://help.pinterest.com/en/business/article/vat))。
