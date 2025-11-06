# thatを使った表現 - プレゼンテーションスライド

## 概要
このスライドセットは、英語の「that」を使った6つの重要な表現パターンを教えるためのインタラクティブなプレゼンテーションです。

## ファイル構成
```
expressions-using-"that"/
├── index.html (ランディングページ)
├── slide1.html (タイトルスライド)
├── slide2.html (thatの様々な使い方 - 概要)
├── slide3.html (Pattern 1: 強調構文・目的語)
├── slide4.html (Pattern 2: 強調構文・主語)
├── slide5.html (Pattern 3: 強調構文・副詞節)
├── slide6.html (Pattern 4: so...that構文)
├── slide7.html (Pattern 5: such...that構文)
├── slide8.html (Pattern 6: 同格のthat - 基本)
├── slide9.html (Pattern 6-2: 同格のthatを使える名詞（1）思考・感情)
├── slide10.html (Pattern 6-3: 同格のthatを使える名詞（2）情報・事実)
├── slide11.html (Pattern 6-4: 同格のthatを使える名詞（3）発言・提案)
├── slide12.html (Pattern 6-5: 同格のthat vs 関係代名詞のthat)
├── slide13.html (まとめ)
├── css/
│   ├── styles.css (共通スタイル)
│   ├── slide1-styles.css
│   ├── slide2-styles.css
│   ├── pattern-slides.css (Pattern 3-12のスタイル - 拡張版)
│   └── slide9-styles.css
├── assets/
└── README.md

../common/
└── presentation.js (共通スライドナビゲーション - 自動カウント機能付き)
```

## 技術仕様
- HTML5 + CSS3
- JavaScript (Vanilla)
- Lucide Icons (CDN経由)
- Google Fonts: Noto Sans JP
- スライドサイズ: 1280x720px
- **共通presentation.js**: 全スライドセットで共有、自動的にスライド数を検出

## スライド内容の特徴

### Pattern 6（同格のthat）の拡張
Pattern 6（同格のthat）は、内容が充実しているため**5つのスライド**に分割されています：

1. **slide8.html** - 同格のthatの基本概念
   - イコール（=）の働きをする接続詞としての説明
   - 名詞 + that + S + V の構造
   - 基本例文（fact, idea）

2. **slide9.html** - 同格のthatを使える名詞（1）思考・感情
   - belief（信念）、idea（考え）、thought（考え）、hope（希望）、fear（恐れ）
   - 2つの例文で理解を深める
   - 1スライド1カテゴリーで学習しやすく

3. **slide10.html** - 同格のthatを使える名詞（2）情報・事実
   - fact（事実）、news（知らせ）、information（情報）、truth（真実）、evidence（証拠）
   - 2つの例文で理解を深める

4. **slide11.html** - 同格のthatを使える名詞（3）発言・提案
   - suggestion（提案）、proposal（提案）、claim（主張）、request（要求）、advice（助言）
   - 2つの例文で理解を深める
   - 使えない名詞の注意点も記載

5. **slide12.html** - 同格のthat vs 関係代名詞のthat
   - 2つのthatの違いを視覚的に比較
   - 見分け方のポイント（完全な文 vs 不完全な文）
   - 実践的な見分け方のヒント

### 強調構文の平常文比較
Patterns 1-3（強調構文）では、平常文と強調構文を並べて比較表示することで、
文法構造の違いを明確に理解できるようにしています。

### 教育的配慮
生徒が初めて学習する内容であることを考慮し、以下の工夫をしています：

- **1スライド1カテゴリー**: 情報量を適切に制限し、認知負荷を軽減
- **各カテゴリー2例文**: 複数の例文で理解を深めながら、過多にならないバランス
- **段階的な学習**: 基本概念 → 使える名詞（3カテゴリー）→ 比較・見分け方
- **プレゼンテーションモード対応**: 全てのコンテンツが1280x720px（16:9）に収まる設計
- **視覚的な区別**: カテゴリーごとに番号付きヘッダーで明確に分類

## カスタマイズ
- 各HTMLファイルを編集して内容を変更
- css/フォルダ内のCSSファイルで色やレイアウトを調整
- スライドを追加・削除しても、共通presentation.jsが自動的に総スライド数を検出

## 参考
このスライドセットは、inanimate-subject スライドのスタイルを基に作成されました。
同格のthatの内容は、[イングリッシュおさるの記事](https://englishosaru-officialsite.co.jp/englishosarublog/appositive-that/)を参考にしています。

