---
title: "LLMを用いた多段階クエリ変換によるより具体的な商品レビューの検索"
image: "/images/2025-07-2025福井web用サムネイル.png"
wp_id: 710
aliases: ["/archives/2025/07/710/"]   # 旧WordPressのURLからの転送
---

#### 概要

本研究では，ある商品に対する具体的なレビューを抽象的なレビューをもとに商品レビュー集合から検索する手法を提案する．具体的なレビューは商品に対する理解を深めるのに有益である．しかし，単純な疎検索や密検索では具体性を考慮してレビューを検索することができず，抽象的なレビューから具体的なレビューを検索することが難しいと考えられる．そこで本研究では大規模言語モデル（LLM）を用いて多段階に生成された仮想の具体的なレビューをクエリとしてレビューの検索を行う．これにより，具体的なレビューが持つ特徴を含むレビューを検索できると考えられる．実験では，楽天レビューデータを活用し，提案手法が実際に存在する抽象的なレビューをもとにより具体的なレビューを検索することができるか評価を行った．実験の結果，密検索の実験設定においてLLMを用いた多段階クエリ変換によって平均nDCGが向上した．

#### 書誌情報

福井智矢, 山本岳洋, 湯本高行: [LLMを用いた多段階クエリ変換によるより具体的な商品レビューの検索](/papers/2025/Fukui.pdf), 第17回データ工学と情報マネジメントに関するフォーラム（DEIM 2025）, 5L-04, 2025年3月.

#### スライド

<iframe width="640" height="420" loading="lazy" class="speakerdeck-iframe" frameborder="0" src="https://speakerdeck.com/player/2020889664a144d2b5679efa42547721" title="LLMを用いた多段階クエリ変換によるより具体的な商品レビューの検索" allowfullscreen="true" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 315;" data-ratio="1.7777777777777777"></iframe>
