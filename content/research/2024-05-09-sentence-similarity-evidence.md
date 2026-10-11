---
title: "文章間類似性判定モデルの根拠の抽出"
image: "/images/2024-05-スクリーンショット-2024-05-09-140338.png"
wp_id: 512
aliases: ["/archives/2024/05/512/"]   # 旧WordPressのURLからの転送
---

#### 概要

本研究では,2 つの文の類似性を判定し,「類似」「非類似」という判定の根拠となる文節の抽出に取り組む. まず,類似度が与えられた 2 つの文章ペアのデータに,類似度に応じて「類似」または「非類似」というラベルを付与し,「類似」「非類似」を判定する BERT モデルを作成した.その後,各文を文節に分割し,文節の類似度が高い順に各文から 1 文節ずつを取り出した文節ペアを作成した.最後に,文節ペアをそれぞれマスクした状態で学習した BERT に入力し,類似に分類される確率をマスク前と比較することにより,変化の大きい文節ペアを判定に影響を  
与える根拠として抽出した.その結果,類似文からは類似度の高い文節を共通語として,非類似文からは類似度は高くないものの対応関係を持つ文節を差異として抽出することができた.また,誤分類に影響を与えた文節を抽出することにより,誤って学習している部分や学習が不十分であった部分を発見した.

#### 書誌情報

中井香那子, 河田 友香, 山本 岳洋: [文章間類似性判定モデルの根拠の抽出](/papers/2024/Nakai.pdf), 第16回データ工学と情報マネジメントに関するフォーラム(DEIM 2024) ,T1-A-4-02, 2024年3月  
<iframe width="640" height="420" loading="lazy" class="speakerdeck-iframe" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 315;" title="文章間類似性判定モデルの 根拠の抽出" src="https://speakerdeck.com/player/50138cfcaac64d59a9df03ed626461bc" frameborder="0" allowfullscreen="allowfullscreen" data-ratio="1.7777777777777777"></iframe>
