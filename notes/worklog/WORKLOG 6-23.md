---
tags : PM worklog
---
# Personal meeting 6-23
## 上週問題：
無

## 本週問題：

---
## Paper：

Meta-Learn 出自一本書名為Learning to Learn(1998)
https://link.springer.com/chapter/10.1007/978-1-4615-5529-2_1



### Learning to learn by gradient descent by gradient descent
https://arxiv.org/pdf/1606.04474v2.pdf 
> Goal: construct a learning alg. which performs well on particular class of optimization problem


$\mathcal L(\phi)$: Loss
$\phi$: optimizaer parameters
$\theta^*(f,\phi)$: optimizee parameters
$\mathbb E_f()$: 期望值
![](https://i.imgur.com/KvdatmS.png)

如何得到optimizer的參數?

$g_t$: update step
![](https://i.imgur.com/7j8OnjO.png)

Computing Gradient:
![](https://i.imgur.com/Xy8wxhL.png)

---

## Programming：
幫實驗室的電腦裝深度學習的環境:
* NVIDIA 驅動
* CuDNN
* CUDA

---

## 下週進度：
Paper：繼續讀Learning to learn by gradient descent
by gradient descent(應該能讀完)

PyTorch：Logistic regression