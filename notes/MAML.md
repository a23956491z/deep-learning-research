[Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks](https://arxiv.org/pdf/1703.03400.pdf)



## BASIC
* Learning to learn

meta learning:
1. **learning good weight initialization**
2. generate parameters of other model
3. learning transferable optimizaer

model-agnostic: is a **Framework**

## MAML
### Prerequest
1. N-way K-shot
few-shot learning的配置
N-way：訓練集中有N個類別
K-shot：每個類別有K個已標記數據

2. Task

用MAML訓練出一個模型 $M_{fine-tune}$，用於分類未標籤的資料
$M_{fine-tune}$的類別有五個 $P_1$~$P_5$，每個類別用5個樣本訓練，15個樣本測試，這樣的配置成爲 5-way 5-shot

另外還有十個類別$C_1$~$C_{10}$（每個類別30個樣本），用於訓練$M_{meta}$

MAML會利用 $C_1$~$C_{10}$去訓練$M_{meta}$
再利用 $P_1$~$P_5$ 去fine tune  $M_{meta}$
而最後fine tune完的模型就稱爲 $M_{fine-tune}$

 $C_1$~$C_{10}$ 稱爲 **meta-train classes**
$P_1$~$P_5$ 稱爲 **meta-test classes**

訓練$M_{meta}$：
因爲我們是 5-way 5-shot的配置
先從meta-train classes $C_1$~$C_{10}$ 隨機取5個類別，每個類別隨機取20個已標註樣本（meta-test classes每個class都有20個樣本)，組成一個task $\mathcal{T}$，並把那20個樣本中，抽出5個作爲support set，其餘15個作爲query set。

![](https://i.imgur.com/6DZ8Pfs.png)

一個task $\mathcal{T}$ 相當於一筆data
所以我們需要好幾個task才能組成一個batch

### 概念
>The primary contribution of this work is a simple model-
and task-agnostic algorithm for meta-learning that trains
a model’s parameters such that a small number of gradi-
ent updates will lead to fast learning on a new task.

新的Task進來，只需要更新幾次就能適應那些資料

### 目標
>The goal of few-shot meta-learning is to train a model that
can quickly adapt to a new task using only a few datapoints
and training iterations. 

讓model能快速適應新的任務（task）

> Since we would like to apply our frame-
work to a variety of learning problems, from classifica-
tion to reinforcement learning, 

並且應該要能勝任各種Learning的問題：諸如classification，reinforcement learning

利用meta-learn 學出一個非常好的初始化參數
讓訓練不需要使用太多樣本，即可在模型中快速收斂

### TASK
![](https://i.imgur.com/jlws7yR.png)

* the model is $\mathcal{f}$, turns input $x$ to outputs $a$
* $\mathcal{L}(x_1, a_1, ...,x_H,a_H)$：Loss function
	- task-specific的回饋：例如loss（classification）或 cost function（MDP）
* $\mathcal{T}$：單一Task
* $q(x_1)$：distribution over initial observation
* $q(x_t+1 | x_t,a_t)$：transition distribution
* $H$：episode length
	- supervised problem length $H = 1$

考慮目標task(用來更新的資料)的distribution $p(\mathcal{T})$
task $(\mathcal{L}_\mathcal{T_i})$從distribution $p(\mathcal{T})$中取樣，並用新的sample做test

不同的task間，可能存在大量重複
不過task間只需要有**些許差異**，不需要到完全不同

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
* 
* $M_{fine-tune}$ 學習時，不需要二重梯度更新

 
## Experiment

圖像分類：
![](https://i.imgur.com/BzanEoo.png)

nearest-neighbor baseline：用KNN做1-shot 5-shot圖像分類
如果KNN加上特徵提取：
[SimpleShot: Revisiting Nearest-Neighbor Classification for Few-Shot Learning](https://arxiv.org/abs/1911.04623)(2019年)

複雜的特徵提取網路+KNN在few-shot learning的表現
甚至可以超過諸多設計複雜的state-of-art Meta-Learning模型

## REFER
### Markov decision process

### K-shot learning
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
## 問題
20個樣本組合成一個task
是用什麼方式組成的？concatenate？

