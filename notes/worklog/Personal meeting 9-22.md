---
tags : PM, worklog
---
# Personal meeting 9-22

# Table of content
[TOC]

# Overview
Topic:
1. MAML Pytorch Code Review
2. Transfer Learning

Papers:
1. Big Transfer (BiT):General Visual Representation Learning
2. EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks
3. Exploring the Limits of Weakly Supervised Pretraining
4. Batch Normalization: Accelerating Deep Network Training byReducing Internal Covariate Shift

Pytorch:
1. mini-imagenet : make query-set & support set
2. MAML PyTorch
 
---
# Paper notes

## Batch Normalization
**I found batch norm. have parameters to train!**

![](https://i.imgur.com/SUFwFaX.png)

[note detail]()

---

# PyTorch

## MAML code structure
![](https://i.imgur.com/O1zMMHI.png)

## MAML code notes

[meta.py code note](https://app.luminpdf.com/viewer/61499892fd1b720011f71c25)

preview of note:
![](https://i.imgur.com/pSXTJC2.png)

the difference between `self.net.vars` & `self.net.parameters()`
in first forward : `vars=None`
in second forward : `vars = self.net.parameters()`  & with `torch.no_grad()`
in third forward(after first update) : `vars = fast_weights` & with `torch.no_grad()`

---

# Future work & Summary
1. I have studied the pyTorch code of MAML, though I didn't build the MAML myself, it still enough to configuring the concept of MAML.
2. In paper works, trying to figure out the importance of pretrain & the limit of pretrain, and the conclusion is **modern models need pretrain**.
3. In the next week, I would start to building **Vision Transformer** with pyTorch.

old schedule
![](https://i.imgur.com/IMXlNGP.png)
