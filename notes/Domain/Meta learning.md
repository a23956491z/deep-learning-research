# Course takedown
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

