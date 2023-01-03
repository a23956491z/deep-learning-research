 Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift
 
 *internal covariate shift*
 
 ![](https://i.imgur.com/IyoeroQ.png)
(2014 Inception network)

original inception : 3.1e7 training steps with 72.2% acc
batch norm. before every non-linearity

![](https://i.imgur.com/7ePLHyA.png)

![](https://i.imgur.com/n11i0He.png)
![](https://i.imgur.com/3iFARWo.png)


![](https://i.imgur.com/SUFwFaX.png)

batch_mormalization works on 2 different ways when in **Training & Testing**
1. Training : Calculate mini batch mean in order to normalize the batch
2. Testing : We use moving average mean to calculate the mini batch statistics

 Tips:
* Large learning rate
* don't use with dropout

refer:
[A Gentle Introduction to Batch Normalization for Deep Neural Networks](https://machinelearningmastery.com/batch-normalization-for-training-of-deep-neural-networks/)
[Batch Norm Explained Visually — How it works, and why neural networks need it](https://towardsdatascience.com/batch-norm-explained-visually-how-it-works-and-why-neural-networks-need-it-b18919692739)

[How and why does Batch Normalization use moving averages to track the accuracy of the model as it trains?](https://stats.stackexchange.com/questions/219808/how-and-why-does-batch-normalization-use-moving-averages-to-track-the-accuracy-o)