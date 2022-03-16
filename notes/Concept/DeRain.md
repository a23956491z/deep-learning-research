
# Semi-supervised Transfer Learning for Image Rain Removal

# Deep Joint Rain Detection and Removal from a Single Image


* binary map to locates rain streak
* comprising rain streak layer & background layer

multi-task
* binary rain streak map
* clean background

problem:
* overlapping between rain steak & background texture pattern
	* over-smoothing
* degradation of rain is complex
	* atmospheric veils (霧氣造成的模糊) is not create
	* different shape & direction of streak
* Most of method use small image patch

method:
* this network is multi-task
	* produce rain streak binary map
	* produce rain-removed background
* proposed contextualized dilated network to enlarge receptive field
* recurrent network to progressively remove

### Data
DATASET!
* Rain100L : one type of rain streak (from BSD200)
* Rain100H : five streak direction (from BSD200)
* Test100 : from ID-CGAN (Image De-raining Using a Conditional Generative  
Adversarial Network)
* test2800(Rain13k) : from deatilNet ([Removing rain from single images via a deep detail network](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8099669)) 1000Image from BSD.... to generate 14k  data

![](https://imgur.com/OEnpNBr.png)
**this figure from [Multi-Scale Progressive Fusion Network for Single Image Deraining](https://www.researchgate.net/publication/343457299_Multi-Scale_Progressive_Fusion_Network_for_Single_Image_Deraining)**
***


Rain100L、Rain100H proposed by Deep Joint Rain Detection and Removal from a Single Image

![](https://i.imgur.com/rMn09Ss.png)

### Rain model
$O = B + \tilde{S}$
* B is background
* S is rain streak
* O is obervation image


assumption:
* without detecting rain & non-rain regions cause over-smooth on the rain-free region
* rain streak has heterogeneous density, so uniform sparsity level assumption is failed

New rain model
$O = B+SR$
* R is region-dependent variable
	* indicate the location of rain streak
	* binary values (like mask)
	* R can get from **hard-thresholding** by $S$

### dilated convolution

enlarge the receptive field : for 3x3 feature map
![](https://i.imgur.com/RxJoc4A.png)
from [Multi-scale context aggregation by dilated convolutions](https://arxiv.org/pdf/1511.07122.pdf)

![](https://i.imgur.com/WUzRz45.png)
conext network structure (from [Multi-scale context aggregation by dilated convolutions](https://arxiv.org/pdf/1511.07122.pdf))

problem of dilated : grdding effect, cannot deal with small size object
![](https://i.imgur.com/QwA35X4.png)
dilation factor from 1 to 3(**from [Understanding Convolution for Semantic Segmentation](https://arxiv.org/pdf/1702.08502.pdf)**)

gridding effect on segmentation
![](https://i.imgur.com/FvIC1HW.png)
ground truth, without hybrid, ResNet-DUC-DHC(**from [Understanding Convolution for Semantic Segmentation](https://arxiv.org/pdf/1702.08502.pdf)**)

Hybrid dilated conv:
![](https://i.imgur.com/n2DBcxR.png)
Structure of DHC + DUC(**from [Understanding Convolution for Semantic Segmentation](https://arxiv.org/pdf/1702.08502.pdf)**)

### contextualized dilated network

$O$

![](https://i.imgur.com/xYCzDp1.png)