## Course takedown
Train Example(dataset) -> Learning algorithm
用dataset 丟進學習的演算法，輸出可以得到一個classifier
![](https://i.imgur.com/OyQDct6.png)

而Learning algorithm能不能被學出來？
一樣也是用machine learning三步驟

什麼東西是 **Learnable**(for learning alg.)
1. Net architecture
2. Initial parameter
3. learning rate

### Define loss fucntion
$L(\phi)$ : Loss function

訓練資料：任務(Task)
如果要訓練二元分類器，我們應該要有很多二元分類的任務
![](https://i.imgur.com/5pKMsMg.png)

Training Tasks：包含Train data和Test data

define Loss function:
Task 1 ->  Learning alg $L(\phi)$ -> classifier $f_{\theta^{1*}}$ -> loss to classifier

Classifier 跑 Task 內的 Test data (有標註)
就可以用 Test data 的 ground truth 和 prediciton 計算loss 

![](https://i.imgur.com/NsVEIvA.png)

在原本的ML中，loss用 training data 計算
而在meta learning中，loss 中 test data 計算
但是我們是訓練「任務」，所以可以使用在 任務中使用 test data

### Training
![](https://i.imgur.com/aiEm6hX.png)

最小化 meta Learning model 的 Loss
如果可以微分，就使用 gradient descent
不行的話，也可以使用 RL

![](https://i.imgur.com/wlIPUBK.png)

Testing Task != Test data in Training Task

### Compares to ML
![](https://i.imgur.com/zCirIgu.png)

![](https://i.imgur.com/5iIQ0fM.png)

用Test task得到的 model，就是最後實際使用的 classifier

### Few-shot image classification
Each class only has a few images
N-ways K-shot classification: In each task, there are **N classes**, each has **K exmaples**


[META Learning 概覽](https://lilianweng.github.io/lil-log/2018/11/30/meta-learning.html)

# Learning to learn by gradient descent by gradient descent 

[](https://arxiv.org/pdf/1606.04474v2.pdf 
> Goal: construct a learning alg. which performs well on particular class of optimization problem

## Gradient descent
機器學習就是最佳化目標function的過程
![](https://i.imgur.com/O5BNEKP.png)

### No Free Lunch Theorem
不同的Optimization function 間，面對「所有」optimization problems的平均表現都相同。

> Roughly speaking we show that for both static and time dependent optimization problems the average performance of any pair of algorithms across all possible problems is exactly identical.

 — [No Free Lunch Theorems For Optimization](https://ieeexplore.ieee.org/abstract/document/585893), 1997.
 
也就是說，如果有一個Optimization function對於特定問題的表現比較好，那其餘問題的表現必定比較差。
> If one algorithm performs better than another algorithm on one class of problems, then it will perform worse on another class of problems

— Page 6, [Algorithms for Optimization](https://amzn.to/34Nb7nv), 2019.

> known as the “no free lunch” theorem, sets a limit on how good a learner can be. The limit is pretty low: no learner can be better than random guessing!

— Page 63, [The Master Algorithm](https://amzn.to/3lKKGFX), 2018.

不過我們只在乎我們面對的這幾個特定問題
> We don’t care about all possible worlds, only the one we live in. If we know something about the world and incorporate it into our learner, it now has an advantage over random guessing.

— Page 63, [The Master Algorithm](https://amzn.to/3lKKGFX), 2018.

當面臨的問題足夠廣泛時，用 cross validation來選learning algortihm，跟不用其實沒差。
> an algorithm that uses cross validation to choose amongst a prefixed set of learning algorithms does no better on average than one that does not.

— [The Supervised Learning No-Free-Lunch Theorems](https://link.springer.com/chapter/10.1007/978-1-4471-0123-9_3), 2002.

也就是說，不同機器學習演算法間具備不同的優勢，是來自於其「假設」或是先輩知識不同。

所以，在脫離具體問題，空泛的談哪個演算法比較好，是毫無意義的。


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

只不過我們的learning algortithm不再是原本的gradient descent，也不會計算loss，就僅僅藉由 $x(j), y(j), y(j-1)$來調整參數

而因為我們的 subordinate和RNN的結構相同，於是乎只要是RNN的架構，都可以透過這個方式建構出meta learning。

而原本的$x(j), y(j), y(j-1)$再加上ground truth$\hat{y}(j)$，會用來改進leanring algorithm，也就是說，suboridnate的模型並不會用到ground truth，ground truth只用來優化 leanring algorithm
![](https://i.imgur.com/Bl6Uzrg.png)


### Learn to Learn with RNN
Notation:
$\phi$: optimizaer parameters
$\theta^*(f,\phi)$: optimizee parameters

如何判斷optimizer好不好？Loss：
$f$ : distribtuion of functions
$\mathcal L(\phi)$: Loss
$\mathbb E_f()$: 期望值
![](https://i.imgur.com/KvdatmS.png)

如何得到optimizer的參數?
RNN model $m$ 的output 便是update step $g_t$ 
而RNN model的狀態(state) $h_t$ 後面LTSM會用到
$\phi$ 則是 $m$ 的參數


![](https://i.imgur.com/7j8OnjO.png)
* $w_t$ 作為控制步長(time-step)的超參數，每一個 $t$都可以有一個 $w_t$，我們可以手動控制不同時間點的Loss大小，來加速學習的過程
* $t = T$時設 $w_t=1$ ，這個Loss的式子就跟上面的相同。
* 單單只設 $w_t=1[t=T]$，而忽略其他的$w_t$會導致Backpropagation Through Time(BPTT)的效果很差，所以在Paper的實驗中，$w_t=1$ for every $t$.

> Here $w_t \in \mathbb{R} \geq 0$ are arbitary weights associated with each time-step and we will also use the notation $\nabla t= \nabla_{\theta}f(\theta_t)$


而我們只要對 $\phi$ (potimizer parameter) 用gradient descent ，就可以最小化 optimizer的Loss：
1. 從function distribution中抽樣一個ramdom funtion $f$，也就是random initialize
2. 計算該function的 Loss的偏導數  $\cfrac{\partial\mathcal L(\phi)}{\partial \phi}$ 
3. 並利用該偏導數，在計算圖中反向傳播，得到梯度
4. 利用梯度更新參數

>*Flash back，什麼是計算圖*：
![](https://i.imgur.com/rRHWVyT.png)

計算圖:
* 反向傳播時，導數隨着實線傳播，而drop掉虛線上的導數
* 因為虛線上的導數被忽略了，所以optimizee的梯度不會被optimizer影響到
![](https://i.imgur.com/Xy8wxhL.png)

## refer
1. 免費午餐定理： 
	* [No Free Lunch Theorem](https://machinelearningmastery.com/no-free-lunch-theorem-for-machine-learning/)
	* [带你了解机器学习(一): 机器学习中的“哲学” ](https://zhuanlan.zhihu.com/p/27680090)
	* [NFL(No Free Lunch Theorems) 沒有免費的午餐定理](https://blog.maxkit.com.tw/2019/07/nflno-free-lunch-theorems.html)
2. Gradient descent：
	* [Learning To Learn Using Gradient Descent](https://www.researchgate.net/publication/225182080_Learning_To_Learn_Using_Gradient_Descent)
3. by gradient descent by gradient descent：
	* [Learning to learn by gradient descent by gradient descent ](https://arxiv.org/abs/1606.04474)
	* [Learning to learn by gradient descent by gradient descent 筆記](https://www.twblogs.net/a/5b8d060b2b71771883396f4a)