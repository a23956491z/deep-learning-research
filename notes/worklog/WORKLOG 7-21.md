---
tags : PM
---
# Personal meeting 7-21
## 上週問題：
無

## 本週問題：

---
## Paper：

[](https://arxiv.org/pdf/1606.044+74v2.pdf 
## Experiment
Optimizer:
* 2-layer LSTMs with 20 hidden units in each layer
* truncated BPTT

*Loss 是Training的Loss還是 validation or testing?
只有Loss沒有Acc?*


![](https://i.imgur.com/o4MX8Pe.png)

### Optimize problem : Quadratic function
minimizing : 10-dimensional quadratic functions
![](https://i.imgur.com/4RheNkF.png)

* W is 10x10 matrices
* y is 10-dimensional vectors


### Optimize problem : small MLP
* Small MLP with 1 hidden layer of 20 units
* activation : Sigmoid
* loss : cross entropy


Different Learning alg. compares:
* 40 units : 1 hidden layer of 40 units
* 2 layer : 2 hidden layers of 20 units
* ReLU : achnge the activation from Sigmoid to ReLU
	(The optimizer trained on MLP with sigmoid)
![](https://i.imgur.com/3Ei1RUm.png)

Different MLP compares:
![](https://i.imgur.com/gUCTvYN.png)



## Programming：
1. Pytorch: Logistic regression
用Linear regression 做Logistic

計算整個batch的loss
![](https://i.imgur.com/URRdic9.png)

用剛剛的function算Loss
並用metric function檢驗模型 (這裡用acc作metric)
![](https://i.imgur.com/YJsOAVp.png)

檢驗剛初始化完的模型：acc只有6%
![](https://i.imgur.com/X99981C.png)
![](https://i.imgur.com/giTRNJq.png)

剛剛的檢驗函式可以得到 loss，並用之訓練模型
![](https://i.imgur.com/THx4hfX.png)

訓練 5 個epochs
以corss_entropy作loss
SGD作optimizer
metric是acc
最後得到 ~80%的acc
![](https://i.imgur.com/MtVxIek.png)
![](https://i.imgur.com/aBHi2KP.png)
