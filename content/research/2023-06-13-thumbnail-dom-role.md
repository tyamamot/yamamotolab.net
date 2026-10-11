---
title: "カスタマイズ可能なWebページサムネイル生成のためのDOMノード役割推定"
image: "/images/2023-06-2023前田Web用研究サムネイル.png"
wp_id: 342
aliases: ["/archives/2023/06/342/"]   # 旧WordPressのURLからの転送
---

#### 概要

本研究では，HTML文書からWebページに対する評価数や作成日，タイトルなどのWeb ページ自体の属性を抽出することに取り組む．そのためにHTML文書を木構造で表現した DOMを用いてテキストを含むノードを対象とし，Webページ自体の属性を持つノードであるかを分類する．具体的には DOMの各ノードが持つテキストやXPath，class属性値，レイアウト情報などの特徴量を用いてノードの分類を行う．

#### 書誌情報

前田直宏, 山本岳洋: [カスタマイズ可能なWebページサムネイル生成のためのDOMノード役割推定](/papers/2023/kawada.pdf), 第15回データ工学と情報マネジメントに関するフォーラム（DEIM 2023）, 3a-6-4, 2023年3月.

#### スライド

<iframe width="640" height="420" loading="lazy" class="speakerdeck-iframe" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 420;" title="_2023__前田_Web用研究スライド.pdf" src="https://speakerdeck.com/player/1130248f01564ce7828fa34763877eb4" frameborder="0" allowfullscreen="allowfullscreen" data-ratio="1.3333333333333333"></iframe>
