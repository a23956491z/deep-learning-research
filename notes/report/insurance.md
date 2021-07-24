Dataset
![](https://i.imgur.com/KLQ3vTk.png)

保險價格分布區間
![](https://i.imgur.com/dfp7pJn.png)

BMI和保險價格關係圖
![](https://i.imgur.com/x7BcP8r.png)

性別與保險價格
![](https://i.imgur.com/19XHAgG.png)

吸煙與保險價格
![](https://i.imgur.com/N9QgfnB.png)


小孩數量與保險價格
![](https://i.imgur.com/eDYYxFD.png)

地區與保險價格
![](https://i.imgur.com/ApfGfEr.png)

![](https://i.imgur.com/5wz839U.png)

dataset去除性別和地區，batch=128, lr=0.0003 perform pretty good
![](https://i.imgur.com/XaDb9SF.png)
with smaller batch
data converge faster
And learning rate should be smaller
batch=32
![](https://i.imgur.com/J88qPOx.png)
 
 
利用 pretrain 到 loss = 3.5M的model
皆有降低Batch number和lr試圖再精修模型，然而失敗
![](https://i.imgur.com/d3mxaFc.png)

3.5M是難以突破的Loss牆
![](https://i.imgur.com/UfHZxNS.png)

完整特徵
batch=128 lr=`3*1e-3` train 2k epoch
batch=32 lr=`3*1e-3` train 1k epoch
batch=32 lr=`1*1e-4` train 1k epoch
batch=8 lr=`1*1e-4` train 1k epoch
batch=8 lr=`1*1e-5` train 1k epoch

仍然無法突破 3.5M Loss牆
![](https://i.imgur.com/3uBoC6x.png)

## 最終loss
卡在3.5M loss牆
![](https://i.imgur.com/q40PwB9.png)

代表保險價格的預測，平均誤差大概在6k

## 單筆測試
![](https://i.imgur.com/TP2jjLq.png)
