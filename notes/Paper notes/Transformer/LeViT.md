# What the key point in my opinion

What they want to deal with:
* can we stacking transformer on prunned ResNet & compare the performance?
* make DeiT faster & discuss with speed-accuracy tradeoff(never have been discussed in transformer)


Contribution?
* this paper provide a **grafting experiment** to compare the performance when ResNet combine with transformer
	* makes us to clear the idea of stacking convolution with transformer.

interseting ideas:
* the way they see **inductive bias**, see a non-overlay mask + data augmentation as a sliding windows mask
* 


## Preview
can we build a network for testing on CPU even ARM hardwares?

pyramid with pooling similar  to *LeNet*
and based on DeiT, so it also have distillation mechanisim.

transformer is faster than convolutional architecutres for given computational complexity
* accelerators are optimized to perform **large matrix multiplications**

contribution:
* attention as downsampling mechanism
* efficient patch descriptor
* attention bias places positional embedding
* redesigned attention-MLP block

similarity between convolution & transformer
* for convolution, mask overlaping normally
* for transformer, covolution is not overlay, but smoothness mask caused by data augmentation
	* when image presented twice, same gradient goes through different filter.


## Related work
inspired by ResNet : Pyramid Vision Transformer

Tokens-to-tokens ViT
* re-tokenization of ouput after each layer
	* aggregating the neighboring tokens to reduced tokens progressively.

## model
ViT architecture & DeiT training method

using convolution component which is useful in CNN.
* to get a compatible representation
![](https://i.imgur.com/5QGRrpz.png)

**optimized for compute** not to minimize the number of parameters
* ResNet design are more efficient than VGG, because strong resolution reduction in early layers with small computation budge
* so LeViT Use 4 layers of 3x3 convolution to perform resolution reduction

## experiment
preliminary experiment
* **grafting experiments**of DeiT-S
* crop upper of ResNet-50 & reduce the number of DeiT layers
* ResNet produce larger **activation map** than 14x14 activations used by DeiT, need a pooling layer between them, average pooling is best for this experiment


only 300 epochs not 1000 epochs:
![](https://i.imgur.com/pMmEXLN.png)

![](https://i.imgur.com/3fnxmQY.png)

convergence speed on grafting exp
- convolution layer have the ability to learn representation of low-level inforamtion in ealier layers efficiently by **inductive bias**.
	- in another word, convolution have a stronger(meaningful) patch embedding?
	- *can we use transformer to learn the low-level infor?* 
	* *can we use transformer to get the indcutive bias?* 

**combine transformer & convolution is better!**
* most of research focus on transformer stack


in DeiT
* training DeiT for 1000 epochs improve 2% over 300 epochs

