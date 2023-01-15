
testing on 1080Ti GPU:
* RegVGG 83% faster than Resnet50
* 101 faster than Resnet101

inference with only **3x3 conv** only

mobileNet & ShuffleNet
* using channel shuffle
	* increase memory access cost
	* lack supports of various devices

Multi-branch with shallower model
* e.g. Resnet
* deal with gradient vanishiing problem
* also get better acc

RepVgg using **re-parameterization**
* training in multi-branch
* testing in plain architecture


A extend of RepVGG:
[NON-DEEPNETWORKS](https://arxiv.org/abs/2110.07641#)