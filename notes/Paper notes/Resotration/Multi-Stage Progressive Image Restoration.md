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
* 