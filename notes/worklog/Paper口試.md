
**dynamic Social network prediction就是在做Dynamic Network Link Prediction？**


contribution:
* Consists of two phases to capture features of dynamic social network graphs
* Add  and  to control learning more from BP-LSTM auto-encoder or predictor
* Compare our method with other state-of-the-art model, and BP-LSTM has a better performance than other baselines.

**bi-phase到底是哪兩個phase
是指LSTM encoder的output給decoder和predictor這個特性？**

> Thanks to Unsupervised Learning of Video Representations
using LSTMs [22] have a good performance in feature extraction in video frames.

**Video Representations跟network link prediction有什麼關係？**

LSTM encoder的ouput
會同時給LSTM decoder和predictor
![](https://i.imgur.com/ccuXyXJ.png)

![](https://i.imgur.com/U0PgThc.png)


**為什麼要把原本的${x_1} ... {x_w}$重新產生成$\hat{x_1} ... \hat{x_w}$**
*LSTM decoder的output看起來僅僅只是拿來算Loss而已
不參與prediction*


*paper : 3.2
> Since we use the BP-LSTM auto-encoder model to gain the latent characteristics,
we use latent characteristics to predict the future social network graph

*作者說是為了predict,不懂*
![](https://i.imgur.com/W5eZLRk.png)


![](https://i.imgur.com/HsQhknu.png)

**EP-LSTM是做 object tracking的模型
跟social network prediction的關係是？**

*可能是打錯字？*

實驗：
> LSTM: To validate our model in the metrics, we apply pure LSTM in dynamic
link prediction, to view the pure LSTM performance.

**這裡的pure LSTM是指把decoder拿掉，只留下predictor？**


**GC-LSTM和E-LSTM-D都是用 20個test samples或80個test sample，那這個模型作testing是用多少個sample？**

AUC metric:


![](https://i.imgur.com/rrE9XBu.png)


**GC-LSTM的ENRON的20-sample AUR有 89%，即使是80-sample也有87%，為什麼作者的表格中只剩76%，RADOSLAW也是有98.5%，表格中怎麼只剩78%**

**大家的AUR都只有70幾%(包含state-of-art)，作者這個model卻有90幾%
是用training data去算AUR？**
GC-LSTM：
![](https://i.imgur.com/oivICh7.png)

D-LSTM-N：
![](https://i.imgur.com/GKVImeP.png)

