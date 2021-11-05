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


## Related work
inspired by ResNet : Pyramid Vision Transformer

Tokens-to-tokens ViT
* re-tokenization of ouput after each layer
	* aggregating the neighboring tokens to reduced tokens progressively.

## model
similarity between convolution & transformer
* for convolution, mask overlaping normally
* for transformer, covolution is not overlay, but smoothness mask caused by data augmentation
	* when image presented twice, same gradient goes through different filter.


## experiment
preliminary experiment
* **grafting experiments**of DeiT-S
* crop upper of ResNet-50 & reduce the number of DeiT layers
* ResNet produce larger **activation map** than 14x14 activations used by DeiT, need a pooling layer between them, average pooling is best for this experiment
* 

in DeiT
* training DeiT for 1000 epochs improve 2% over 300 epochs

