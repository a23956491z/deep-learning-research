Swin is a gerneral purpose backbone

Problem of ViT:
* for Transformer-based models, tokens are all of a fixed size, unsuitable for dense prediction
* feature map is single resolution
* quadratic computational complexity to image size !

How swin achive **linear computational complexiy to image size**
* shift of window between consecutive self-attentions
* computing self-attention locally within windows
* the patches in each windows is fixed

shift window != sliding window
* sliding window have more latency
* all-MLP architecutres also benifit from shifted window


dense prediction task
* semantic segmentation