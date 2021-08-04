---
tags : PM worklog
---
# Personal meeting 8-04
## 上週問題：
無

## 本週問題：

---
## Paper：
### Algortihm
重點是要學習Learning algorithm
而我們學習出來的這個 gradient-based Learning rule
可以快速處理從 $p(\mathcal{T})$  抽出的新task

也就是說，這個Learning rule的model
要對task的變動很敏感，task微小的變動就能使下一次Loss有大量提升
如此才有辦法做到快速適應

根據task 作梯度下降:
* 模型 $f_\theta$ 和參數 $\theta$
* 適應新任務 $\mathcal{T}_i$ (用gradient descent)後，模型的參數變為 $\theta'$
* 學習(適應)新任務時，可以使用多次 gradient descent (multiple gradient update)
	* ![](https://i.imgur.com/sbniOq3.png)
* 此時的目標：最小化 模型對新任務$\mathcal{T}_i$的Loss
	* ![](https://i.imgur.com/vHE4XSl.png)

根據batch作梯度下降：
* 這個步驟也稱之為 meta-optimization
* 利用 Stochastic gradient descent
* 根據整個batch，每一個 $\theta'$產出的Loss之和，作梯度下降
	* ![](https://i.imgur.com/t1GYskv.png)





![](https://i.imgur.com/tzASpfi.png)
* $p(\mathcal{T})$ ：反覆抽出task $\mathcal{T}$所形成的task池（即$D_{meta-train}$中task的分佈）
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

因為 整個學習的過程，需要計算 gradient的gradient
*所以反向傳播時需要額外計算 海塞向量積（Hessian-vector product）*
在實驗中只使用一階 gradient，也就是first-order approximation

 
 Few-shot 監督式學習的分類：
 ![](https://i.imgur.com/QjUcM7d.png)

## Programming：

* Pytorch:
	* Logistic on MNIST
	* Simplified ResNet on Cifar10
	 ![](https://i.imgur.com/nnvmt7D.png)
