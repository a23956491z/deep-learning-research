---
tags : PM worklog
---
# Personal meeting 6-3
## 上週問題：

## 本週問題：
目前沒有

---
## Paper：
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


參考資料：
0.[MAML paper本人](https://arxiv.org/pdf/1706.03762.pdf)
1.[演算法： Learning to learn Meta learning](https://biic.ee.nthu.edu.tw/blog-post/learning-to-learn-meta-learning)
2.[Model-Agnostic Meta-Learning （MAML）模型介绍及算法详解](https://zhuanlan.zhihu.com/p/57864886)

---

## Programming：
1. 開始學PyTorch ：
   PyTorch可能會成爲未來趨勢，但LAB內沒人熟悉
   雖然我TensorFlow沒有到很熟，不過我想先從Torch切入
   
[Youtube PyTorch教學](https://www.youtube.com/watch?v=GIsg-ZUy0MY)

---

## 下週進度：
讀完MAML
[Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks](https://arxiv.org/pdf/1706.03762.pdf)
