# Personal meeting 6-17
## 上週問題：
few-shot 的意思：一個類別只用少量個標註sample做訓練

## 本週問題：

---
## Paper：

Meta learning 的幾篇重要paper：
起源：
* [Learning to learn by gradient descentby gradient descent (NeurlPS 2016)](https://arxiv.org/pdf/1606.04474v2.pdf)
找架構：
 * [Searching for Efficient Multi-Scale Architectures for Dense Image Prediction(NeurlPS 2018)](https://paperswithcode.com/paper/searching-for-efficient-multi-scale)
 * [Progressive Neural Architecture Search (ECCV 2018)](https://paperswithcode.com/paper/progressive-neural-architecture-search)
* [Neural Architecture Search with Reinforcement Learning (2016)](https://paperswithcode.com/paper/neural-architecture-search-with-reinforcement)
 * [Learning Transferable Architectures for Scalable Image Recognition (CVPR 2018)](https://paperswithcode.com/paper/learning-transferable-architectures-for)
* [DARTS: Differentiable Architecture Search (ICLR 2019)](https://paperswithcode.com/paper/darts-differentiable-architecture-search)
 Few-shot：
* [A Closer Look at Few-shot Classification (ICLR 2019)](https://paperswithcode.com/paper/a-closer-look-at-few-shot-classification-1)
* [Matching Networks for One Shot Learning (NeurlPS 2016)](https://paperswithcode.com/paper/matching-networks-for-one-shot-learning)

---
* 李宏毅的Meta learning：
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

---
先暫停 MAML
開始看：Matching Networks for One Shot Learning





---

## Programming：
1. PyTorch ：Load MNIST

下載MNIST
![](https://i.imgur.com/xyhk9Th.png)

把MNIST 轉換成 pytorch可以用的tensor
![](https://i.imgur.com/S1NAWkv.png)

分成 training dataset 和 validation dataset
並用DataLoader 分batch

![](https://i.imgur.com/pwdFEn7.png)



---

## 下週進度：
Paper：繼續讀 Matching Networks for One Shot Learning
PyTorch：Logistic regression