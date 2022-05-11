## 概覽
近期**去噪去模糊**模型計算量與PSNR的比較：
[Simple Baselines for Image Restoration](https://arxiv.org/pdf/2204.04676.pdf)
![](https://i.imgur.com/BA0odhJ.png)

* 去模糊：UFormer的表現和Restormer相似
* 去噪：Restormer > UFormer
* CNN的代表：[MPRNet](https://openaccess.thecvf.com/content/CVPR2021/papers/Zamir_Multi-Stage_Progressive_Image_Restoration_CVPR_2021_paper.pdf) 需要更大的計算量（MACs）

這篇同時提出了一個Restormer的簡易版，**並達到更高的表現**

![](https://i.imgur.com/G88Goan.png)
* CA是Channel Attention
* SCA是作者提出的 simplfied channel attention

不使用ReLu和ReLu（Non-linear activation free）
![](https://i.imgur.com/vxEsu8d.png)

### RealRain Dataset

非合成雨滴的Derain dataset
* 合成Ground Truth
* 拍攝一段影片，合成每一幀沒有雨滴的pixel

[Spatial Attentive Single-Image Deraining with a High Quality Real Rain Dataset](https://arxiv.org/pdf/1904.01538.pdf)



---


## Super-resolution的代表：SwinIR

ICCV workshop 2021的[SwinIR: Image Restoration Using Swin Transformer](https://openaccess.thecvf.com/content/ICCV2021W/AIM/papers/Liang_SwinIR_Image_Restoration_Using_Swin_Transformer_ICCVW_2021_paper.pdf)

近期SR領域的標杆，幾乎每一篇都會提到它
只需要**20M**的參數量，達到最頂尖的PSNR
![](https://i.imgur.com/6NN1LuQ.png)


架構極其簡單：一直疊Swin Block
![](https://i.imgur.com/RQXX0ly.png)

---

## [Practical Blind Denoising via Swin-Conv-UNet and Data Synthesis](https://arxiv.org/pdf/2203.13278.pdf)
* Denoising & SR
* 更強大的Degraded圖像合成（Deep Blind）
    * Deep Blind：我們無法預先知道noise的種類的程度
    * 先前提到的：[Designing a Practical Degradation Model for Deep Blind Image Super-Resolution](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhang_Designing_a_Practical_Degradation_Model_for_Deep_Blind_Image_Super-Resolution_ICCV_2021_paper.pdf)

實現：在UNet前後串接 **Swin-Conv Block**
* 參考自SwinIR的做法
* **skip connection不是每個階段都有**

![](https://i.imgur.com/qTbe0tV.png)

---

## Swin block + UNet
非常接近我之前Proposal中的架構
（中興大學的paper）

和SCUNet一樣： **skip connection不是每個階段都有**
[SUNet: Swin Transformer UNet for Image Denoising](https://arxiv.org/pdf/2202.14009.pdf)


![](https://i.imgur.com/sKln7Eh.png)

升維的部分結合Binear+pixelshuffle
![](https://i.imgur.com/8LuflY8.png)

---

## Swin-based的模型比較

### 預訓練的Restoration模型：EPT
[On Efficient Transformer-Based Image
Pre-training for Low-Level Vision](https://arxiv.org/pdf/2112.10175.pdf)
![](https://i.imgur.com/SxZ9gt5.png)

升降維前後都是Conv，只有最中間的Transformer Stage是用Swin Block

1. 這個模型有測試Rain100L和Rain100H的Derain任務
    * 原本以爲這兩個Dataset是 multi-resolution
    * 但實際上只有320x480和480x320兩種

### Super resolution：SwinIR
[SwinIR: Image Restoration Using Swin Transformer](https://openaccess.thecvf.com/content/ICCV2021W/AIM/papers/Liang_SwinIR_Image_Restoration_Using_Swin_Transformer_ICCVW_2021_paper.pdf)
一直疊Swin Block

### Denoise：結合Conv+Swin的SCUNet
[Practical Blind Denoising via Swin-Conv-UNet and Data Synthesis](https://arxiv.org/pdf/2203.13278.pdf)

利用不同Branch分別計算Conv和Swin
Concat後再加上1x1 Conv

### Denoise：最接近原始Swin的SUNet

[SUNet: Swin Transformer UNet for Image Denoising](https://arxiv.org/pdf/2202.14009.pdf)



### UFormer

### 總結
|                               | EPT | SwinIR | SCUNet | SUNet | Uformer | Restormer |
|-------------------------------|-----|--------|--------|-------|---------|-----------|
| Shifted Window                | ✔   | ✔      | ✔      | ✔     | ✔       |           |
| Unet架構                      | ✔   |        | ✔      | ✔     | ✔       | ✔         |
| LayerNorm                     | ✔   | ✔      |        | ✔     | ✔       | ✔         |
| 每個Stage都有Skip connection  | ✔   |        |        |       | ✔       | ✔         |
| 連續疊Transformer(沒有升降維) | ✔   | ✔      |        |       |         |           |
| Branch出其他Module            |     |        | ✔      |       | ✔       |           |

|                    |            |    EPT    | SwinIR |   SCUNet  | SUNet |  Uformer  | Restormer |
|--------------------|:----------:|:---------:|:------:|:---------:|:-----:|:---------:|:---------:|
| Denoise(greyscale) | Set12      | -         | 31.01  | **31.09** | -     | -         | 31.04     |
|                    | BSD68      | -         | 29.5   | **29.55** | -     | -         | 29.52     |
| Denoise(color)     | CBSD68     | 31.76     | 31.78  | **31.79** | -     | -         | **31.79** |
|                    | Urban100   | **33.07** | 32.90  | **33.03** | -     | -         | 32.96     |
| Denoise(σ= 50)     | CBSD68     | 28.56     | 28.56  | **28.61** | 27.85 | -         | 28.59     |
| DeBlur             | GoPro      | -         | -      | -         | -     | **32.97** | 32.92     |
|                    | RealBlur-J | -         | -      | -         | -     | **29.06** | 28.96     |
| Derain             | Rain100L   | **42.14** | -      | -         | -     | -         | 38.99     |
|                    | Rain100H   | **33.94** | -      | -         | -     | -         | 31.46     |

---

## EXTRA:略優於MPRNet的HINet

[HINet: Half Instance Normalization Network for Image Restoration](https://arxiv.org/pdf/2105.06086.pdf)

![Uploading file..._48p76bds7]()
![](https://i.imgur.com/yUQftXj.png)

2-stage + half instance normalization

![](https://i.imgur.com/UiD1IkV.png)

---

## 問題

1. 既然SwinIR的效能如此好，能不能利用SwinIR替代Encoder？
    * 有人用這樣的非對稱模型嗎？