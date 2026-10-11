# yamamotolab.net（Hugo 版）

旧 WordPress（yamamotolab.net）から移行した研究室サイト。日本語のみ。

## 手元で見る
    hugo server              # → http://localhost:1313/

## 公開
`main` ブランチに push すると GitHub Actions（`.github/workflows/hugo.yaml`）が Hugo でビルドして GitHub Pages に公開する（数分で反映）。
Actions の Hugo は v0.167.0 に固定。手元もこれ以上を使う。

## ファイルの置き場所
| 何を | どこに |
|---|---|
| トップページ | `content/_index.md` |
| 固定ページ（アクセス・学生募集） | `content/access.md`, `content/join.md` |
| 記事 | `content/posts/YYYY-MM-DD-名前.md` → URL `/posts/年/名前/` |
| 研究紹介 | `content/research/YYYY-MM-DD-名前.md` → URL `/research/年/名前/`（一覧はカード表示） |
| メンバー | `data/members.yaml` |
| 研究成果 | `data/publications.yaml`（項目の書式は rerank-lab.org と同じ。年度ごとに表示） |
| 画像 | `static/images/YYYY-MM-ファイル名` → `/images/…`（フォルダ分けしない） |
| 論文PDF | `static/papers/` → `/papers/…` |
| メニュー・サイドバーのリンク | `hugo.toml` |
| デザイン | `layouts/`, `assets/css/main.css`, `assets/css/design-sidebar.css` |

## デザインとトップページ
- デザインは灰背景＋白カード＋右サイドバー（トップページだけサイドバーなし）
- トップページは `layouts/home.html`。研究室の紹介文は `content/_index.md`（キャッチコピーを出したいときは front matter に `tagline:` を書く。今は使っていない）
- トップの住所・地図・連絡先は `hugo.toml` の `params`。最近の記事の件数は `recentNews`
- 画像は幅1200px以下・位置情報なしで保存する（スマホ写真はそのまま入れず、下の `tools/addimg.py` で縮小する）

## 画像の追加（tools/addimg.py）
写真を縮小・向き補正・位置情報削除して `static/images/YYYY-MM-名前.jpg` に保存し、記事に貼る `![](…)` を表示する。
初回だけ `pip install pillow pillow-heif`（pillow-heif は iPhone の HEIC 写真用）。サイトのフォルダで:

    python3 tools/addimg.py 2026-09 ~/Desktop/IMG_1234.HEIC ~/Desktop/IMG_1235.jpg
        → static/images/2026-09-img_1234.jpg などに保存
    python3 tools/addimg.py content/posts/2026-09-18-webdb-summer-2026.md ~/Desktop/*.jpg
        → 記事ファイル名の日付から 2026-09- を付けて保存
    python3 tools/addimg.py 2026-09 original_images
        → フォルダを渡すと、中の画像をまとめて処理
    python3 tools/addimg.py --width 800 2026-09 thumbnail.png    # 長辺を変える（既定1200px）

- 最初の引数（ファイル名の先頭に付ける年月 または 記事ファイル）は必須。記事の日付の年月に合わせる
- JPEG・HEIC などは JPEG（品質80）に、PNG（図・スクリーンショット）は PNG のまま保存
- ファイル名は小文字・空白なしに整える。保存先に同じ名前があればスキップ（上書きしない。何度実行しても重複しない）
- `original_images/` は元の写真の置き場。フォルダだけ git に入り、中身は git で管理しない（`original_images/.gitignore`）。不要になった写真は各自で消してよい
- Windows では `python3` の代わりに `python`

## 記事の追加例
`content/posts/2027-04-07-new-members.md`:

    ---
    title: "研究室に新しく6名の学生が配属されました"
    ---
    本文（Markdown）。写真は ![](/images/2027-04-photo.jpg)

ファイル名の日付と名前から、日付と URL が自動で決まる（date や slug は書かなくてよい）。
名前は半角英小文字・数字・ハイフン。同じ年の中で重ならなければよい。今日より先の日付の記事は、その日まで表示されない。

## 研究紹介の追加例
`content/research/2027-07-10-some-topic.md`:

    ---
    title: "研究テーマの名前"
    image: "/images/2027-07-thumbnail.png"   # 一覧のカードと記事の先頭に出る画像
    ---
    #### 概要
    …

## メンバーの更新（毎年4月）
`data/members.yaml` の `groups` を編集する。グループ（D, M2, M1, B4, 卒業生…）は書いた順に表示。

    - name: M1
      members:
      - ja: 山田 太郎
        en: Taro YAMADA

## 研究成果の追加
`data/publications.yaml` の先頭に追加する。項目の書式は個人サイト rerank-lab.org の `data/publications/*.yaml` と同じなので、
**個人サイトの yaml から項目をそのままコピペ**すればよい（種類ごとのファイル分けはしない）。

    - date: "2027-03"
      authors: 山田太郎, 山本岳洋
      title: 論文タイトル
      venue: 第19回データ工学と情報マネジメントに関するフォーラム（DEIM 2027）, 1A-01, 2027年3月.
      award: 学生プレゼンテーション賞      # あれば。複数なら [A賞, B賞]

- 研究室のページでは `date` から年度（4月始まり）を自動で計算して年度ごとに表示する
  （2027-03 → 2026年度）。年度の中は date の新しい順なので、貼る位置は気にしなくてよい
- 会議名は「DEIM 2027」のように名前と年の間に空白を入れる
- 1件の表示は `layouts/_partials/pubitem.html`（rerank-lab.org と同じファイル）

## 旧URLからの転送
旧 WordPress の URL（`/archives/2025/07/740/`, `/member/`, `/category/…`）は各ページの `aliases:` から新URLへ転送される。
十分な期間が過ぎたら hugo.toml に `disableAliases = true` を足せば転送ページは作られなくなる。

## 移行ツール
`tools/wp2hugo_lab.py` — 旧WordPressのDBダンプから content/ と data/ を生成した移行ツール（もう使わない）。
