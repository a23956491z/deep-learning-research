BiT is very effective when little downstream data is available.
![](https://i.imgur.com/8mGjyzM.png)

## Model
ResNet 152x4
widen the hidden layer by 4



## Batch Norm is detrimental for BiT
* batch norm depends on batch size, but in transfering, when batch size changed. batch norm. would cause damage.
* using Group norm + Weight Standardizaiton

Normalization vs Standardization:
* Norm : $\cfrac{X-X_{min}}{X_{max}-X_{min}}$, [0,1]
* Stand : $\cfrac{X-X_{mean}}{\sigma}$ [-1,1]

## HyperRule
in multi-task problem(e.g. VTAB):
seperate epoches by samples of task