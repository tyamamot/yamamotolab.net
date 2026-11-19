---
title: "大規模言語モデルによるレビューの対照型集約にもとづく商品比較表の作成"
image: "/images/2026-11-nakai-thumbnail.png"
---

#### 概要

本研究では，大規模言語モデル(LLM)を用いてレビューを集約することで，2つの商品に共通する評価や商品固有の評価を対照的に整理した比較表を作成する手法を提案する．比較表とは，2つの商品の各観点に対して共通する評価が何件あるかや各商品固有の評価が何件あるかを一覧することのできる表である．LLMを用いることで，オンデマンドで表を作成し，商品に応じて比較する観点を変更することができる．提案手法では，LLMを用いてレビューから観点と評価を抽出し，観点ごとに要約文を生成，要約文を共通と固有に分類し，1つの比較表にまとめる．共通・固有要約文の精度評価では，比較手法であるAACSumの精度を上回った．一方で，共通・固有を考慮しない比較表を比較手法として行ったユーザ実験では，2つの比較表に大きな差は見られず，本研究で実現したLLMを用いたレビュー集約による比較表の精度においては共通・固有を考慮することはユーザの商品決定に大きな影響はないことが示唆された．

#### 書誌情報

中井 香那子，山本 岳洋，大島 裕明：[大規模言語モデルによるレビューの対照型集約にもとづく商品比較表の作成](/papers/2026/Nakai.pdf)  
第18回データ工学と情報マネジメントに関するフォーラム（DEIM 2026）, 6B-02, 2026年3月.

#### スライド

<iframe loading="lazy" class="speakerdeck-iframe" src="https://speakerdeck.com/player/49aea97d7c2541079683889e212128ad" title="大規模言語モデルによるレビューの対照型集約にもとづく商品比較表の作成" allowfullscreen="allowfullscreen" allow="web-share" frameborder="0" style="border:0;width:100%;height:auto;aspect-ratio:560/315" data-ratio="1.7777777777777777"></iframe>

[Speaker Deck で見る](https://speakerdeck.com/yamamotolab/toukouyou-deim-happyou-shiryou-nakaisan)
