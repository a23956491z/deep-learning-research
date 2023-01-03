---
tags : PM worklog
---
# Personal meeting 6-10
## 上週問題：
20個樣本組合成一個task
是用什麼方式組成的？concatenate？

## 本週問題：
這篇paper涉及的概念太多
短時間(兩個禮拜)內讀不完

相關概念：
1. few-shot learning
2. Meta-Learning
3. Markov chain & Markov decision

observation distribution是什麼

---
## Paper：

### Algortihm
![](https://i.imgur.com/tzASpfi.png)
* $p(t)$ ：反覆抽出task$\mathcal{T}$所形成的task池（即$D_{meta-train}$中task的分佈）
* $\alpha, \beta$ 是學習率(二重梯度)

二重梯度：gradient by gradient
第一重梯度：根據每個task做梯度下降
第二重梯度：根據每個batch做梯度下降


Step 1： 隨機初始化模型參數
Step 2～9： 迴圈（一個iteration）
Step 3： sample出數個task形成一個batch
Step 4～7： 從任務$(\mathcal{L}_\mathcal{T_i})$中sample出 K個data，也就是K-shot learning，並根據這個任務loss的梯度，做gradient descent後得出$\theta'$，用於後面更新模型參數
Step 8：以$\theta'$作爲model的參數，計算出整個batch loss總和的梯度，並以其更新model參數

訓練完後得到 $M_{meta}$

* 新模型會利用$M_{meta}$初始化參數（具體怎麼做？）
* $M_{fine-tune}$ 學習時，不需要二重梯度更新

 
### Experiment

圖像分類：
![](https://i.imgur.com/BzanEoo.png)

nearest-neighbor baseline：用KNN做1-shot 5-shot圖像分類
如果KNN加上特徵提取：
[SimpleShot: Revisiting Nearest-Neighbor Classification for Few-Shot Learning](https://arxiv.org/abs/1911.04623)(2019年)

複雜的特徵提取網路+KNN在few-shot learning的表現
甚至可以超過諸多設計複雜的state-of-art Meta-Learning模型

### REFER
#### Markov decision process

#### K-shot learning
(paper 2.1)
從distribution $p(\mathcal{T})$中抽(draw)出K個samples
並用它產生feedback
![](https://i.imgur.com/I7T02EG.png)

參考資料：
0. [MAML paper本人](https://arxiv.org/pdf/1706.03762.pdf)
1. [演算法： Learning to learn Meta learning](https://biic.ee.nthu.edu.tw/blog-post/learning-to-learn-meta-learning)
2. [Model-Agnostic Meta-Learning （MAML）模型介绍及算法详解](https://zhuanlan.zhihu.com/p/57864886)
3. [\[meta-learning\] 对MAML的深度解析](https://zhuanlan.zhihu.com/p/181709693)
4. [MAML pytorch實做](https://github.com/dragen1860/MAML-Pytorch)
5. [MAML 原作者實做(tensorflow)](https://github.com/cbfinn/maml)
6. [SimpleShot 論文](https://arxiv.org/abs/1911.04623)(2019年)
7. [李宏毅 Youtube：MAML](https://www.youtube.com/watch?v=EkAqYbpCYAc&t=44s)

---

## Programming：
1. PyTorch ：Linear regression

DATA:
![](https://i.imgur.com/68Iqz0N.png)


### Handcraft

![](https://i.imgur.com/QyQrSKY.png)
![](https://i.imgur.com/mCZ8DCf.png)
![](https://i.imgur.com/9e42AAT.png)


### Built-in

![](https://i.imgur.com/mXJn8lm.png)
![](https://i.imgur.com/bGHSVql.png)
![](https://i.imgur.com/bUiDJoZ.png)
![](https://i.imgur.com/LzVdhYR.png)
![](https://i.imgur.com/hgH9Jwu.png)


---

## 下週進度：
讀完MAML
[Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks](https://arxiv.org/pdf/1706.03762.pdf)

FORWARD:
**Matching Networks for One-Shot Learning**https://arxiv.org/pdf/1606.04080.pdf (important!)