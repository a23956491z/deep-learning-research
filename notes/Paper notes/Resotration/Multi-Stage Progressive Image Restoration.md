balance between **spatial details** and **high-level contextualized**

These methods basically are single stage:
* residual learning
* dilated convolutions
* atention mechanism
* dense connection
* generative method

multi-stage is more effective in
* pose-estimation
* scene parsing
* action segmentation

multi-stage is either **encoder-decoder** or  **single-scale pipeline**
* encoeder-decoder is unreliable in preserving spatial image details
* single-scale pipeline is less smentically reliable.

contirubtion point:
* ***This paper combine both multi-stage method**
* use attention module to refine feature
* aggregate multi-scale feature across stage


## Method

### Multi-stage progressive restoration

* First 2 stage : encoder-decoder subnetwork learns **contextual information**
* last stage : operates on input image?
* not simple cascading multiple stage
	* Add attention module between stages (corss-stage feature fusion)


![](https://i.imgur.com/tHE6ivg.png)


