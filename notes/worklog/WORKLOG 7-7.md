---
tags : PM worklog
---

# Personal meeting 7-7
## 上週問題：
無

## 本週問題：

---
## Paper：
### No Free Lunch Theorem
不同的Optimization function 間，面對「所有」optimization problems的平均表現都相同。

> Roughly speaking we show that for both static and time dependent optimization problems the average performance of any pair of algorithms across all possible problems is exactly identical.

 — [No Free Lunch Theorems For Optimization](https://ieeexplore.ieee.org/abstract/document/585893), 1997.
 
也就是說，如果有一個Optimization function對於特定問題的表現比較好，那其餘問題的表現必定比較差。
> If one algorithm performs better than another algorithm on one class of problems, then it will perform worse on another class of problems

— Page 6, [Algorithms for Optimization](https://amzn.to/34Nb7nv), 2019.

### Define gradient descent
而gradient descent就是一個最佳化的方式(approach)

* 基本的(vanilla)Gradient descent:
$f$ 模型本身
$\theta$ 模型的參數(parameter)
$\alpha$ learning rate
![](https://i.imgur.com/VUPQpwM.png)


* 更General的表達方式：
$f$ 模型本身
$\theta$ 模型的參數(parameter)
$\phi$ parameter set
$g_t$ optimizer
optimizer 是一個更新參數的function
人為撰寫的optimizer例如：Adam, SGD
而這裡我們希望能train出這個optimizer
![](https://i.imgur.com/raYojwh.png)

### Previous work
[Learning To Learn Using Gradient Descent](https://www.researchgate.net/publication/225182080_Learning_To_Learn_Using_Gradient_Descent)
2001年的paper，是1990後meta learning的突破點

subordinate system就是我們一般的model
只不過我們的learning algortithm不再是原本的gradient descent，也不會計算loss，就僅僅藉由 $x(j), y(j), y(j-1)$來調整參數

而因為我們的 subordinate和RNN的結構相同，於是乎只要是RNN的架構，都可以透過這個方式建構出meta learning。

而原本的$x(j), y(j), y(j-1)$再加上ground truth$\hat{y}(j)$，會用來改進leanring algorithm，也就是說，suboridnate的模型並不會用到ground truth，ground truth只用來優化 leanring algorithm
![](https://i.imgur.com/Bl6Uzrg.png)


---

## Programming：
Linux：
* 如何使用man page和info page
* 如何正確關機，shutdown/poweroff/halt
* 如何讀懂一個檔案的權限


所有的使用者資訊都在 /etc/passwd 內
密碼記錄在 /etc/shadow內

使用`ls -al` 看目錄內，所有檔案的詳細權限
`-a`表示顯示隱藏檔案
linux系統內，以`.`開頭檔案就是隱藏檔

![](https://i.imgur.com/NtrOoHJ.png)


![](https://i.imgur.com/hAyHQpt.png)

檔案類型：
* `d` 是目錄
* `-` 是檔案
* `l` 是連結檔
* `b` 是可儲存資料的設備
* `c` 周邊設備

`rwx` 的順序不會改變
如果沒有權限則用`-`表示，如`--x`
* `r` 可讀
* `w` 可寫
* `x` 可執行

`ls -l`，如果檔案修改時間太久遠，會省略
`ls -l --full-time` 可以顯示完整時間

目錄的權限如果沒有 `x`可執行，則不可進入該目錄

---

## 未來進度：

meta learning基本功：
Matching Network for one shot learning
MAML
Learning to Learn by gradient descent by gradient descent


Pytorch 學到能讀懂MAML的code
