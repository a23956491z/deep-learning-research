---
tags : paper
---
## intro
雖然 DL 在各個領域都有大幅度的成長，但是總是需要大量的資料輔佐。
如果我們的資料量很少，雖然可以用資料增強和正規化的技巧減輕overfitting，但並沒有從根本上解決問題。

再來，基於大量參數的模型，learning的速度是很慢的，如果我們多了一些資料，就可能需要重train整個模型浪費大量時間，然而，很多非參數(non-parametric)的模型用這些沒見過的(novel)的樣本卻還能達到快速收斂(如KNN)。

這篇的model，試着把 參數型model和非參數型model的特色結合：對全新樣本的快速學習，且有更好的泛化能力

這篇提出的model叫作：Matching Nets，