---
title: "アドホック検索におけるモデルマージによる破滅的忘却の抑制"
image: "/images/2026-10-taniguchi-thumbnail.png"
---

#### 概要

本研究では，アドホック検索タスクにおけるモデルマージを用いた破滅的忘却の抑制効果を検証する．モデルマージは，複数の学習済みモデルのパラメータを統合し，追加の訓練コストを抑えながら各モデルの利点を兼ね備えた新しいモデルを構築する技術である．我々は，追加学習で生じる破滅的忘却という課題をモデルマージによって抑制することで，既存の検索能力を保持したまま追加学習が実現できると考えた．そこで本研究では，まず汎用的な埋め込みモデル(ベースモデル)と，それを代表的なアドホック検索データセットでファインチューニングしたドメイン特化モデルを構築し，両者をモデルマージしたマージモデルとの性能を比較検証した．nDCG@10 による評価の結果，ドメイン特化モデルでは多くの学習対象外ドメインで破滅的忘却が観測されたが，マージモデルではこの低下したすべてのドメインで nDCG@10 スコアが回復した．さらに，一部のドメインではマージモデルが学習対象ドメイン自体の性能も向上させ，モデルマージがアドホック検索タスクにおける破滅的忘却の抑制に有効な手段であることを実証した．

#### 書誌情報

谷口 壮平，佐々木 泰河，山本 岳洋，大島 裕明，藤田 澄男：[アドホック検索におけるモデルマージによる破滅的忘却の抑制](/papers/2026/Taniguchi.pdf)  
第18回データ工学と情報マネジメントに関するフォーラム（DEIM 2026）, 1F-02, 2026年3月.

#### スライド

<iframe loading="lazy" class="speakerdeck-iframe" frameborder="0" src="https://speakerdeck.com/player/aa4be9b1875a429ca1d7846301662f31" title="アドホック検索における モデルマージによる破滅的忘却の抑制" allowfullscreen="true" allow="web-share" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 315;" data-ratio="1.7777777777777777"></iframe>

[Speaker Deck で見る](https://speakerdeck.com/yamamotolab/adohokku-kensaku-niokeru-moderu-maji-niyoru-hametsuteki-boukyaku-no-yokusei)
