---
title: "特定選手に注目した試合結果記事見出しのパーソナライズ"
image: "/images/2024-05-2024佐々木Web用サムネイル.png"
wp_id: 527
aliases: ["/archives/2024/05/527/"]   # 旧WordPressのURLからの転送
---

#### 概要

本研究では,試合結果記事における特定選手に注目した見出しを生成する手法を提案する.見出しの生成には T5 という文生成モデルを用いる.記事全文を入力として,T5 に見出しの最初の文字を注目している選手名にする制約をかけた単純な手法では,注目していない選手の活躍を,注目している選手の活躍のように見出し生成してしまうという問題がある.そこで我々は,試合結果記事から記事の主題に関する文,注目している選手の活躍に関する文のみを抽出して,T5 に入力する手法を提案する.このアプローチにより,指定した選手に注目した自然で事実に基づいた見出しを生成させる.評価実験により,提案手法は,記事全文を入力する単純な手法よりも,特定選手に注目した見出し生成の精度が良いことが示された.

#### 書誌情報

佐々木泰河, 工家昂之, 山本岳洋, 莊司慶行: [特定選手に注目した試合結果記事見出しのパーソナライズ](/papers/2024/sasaki.pdf), 第16回データ工学と情報マネジメントに関するフォーラム（DEIM 2024）, T1-B-6-04, 2024年3月.

#### スライド

<iframe width="640" height="420" loading="lazy" class="speakerdeck-iframe" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 420;" title="特定選手に注目した試合結果記事見出しのパーソナライズ" src="https://speakerdeck.com/player/71bd4705ee3f4bd79c102301f398b24d" frameborder="0" allowfullscreen="allowfullscreen" data-ratio="1.3333333333333333">﻿</iframe>
