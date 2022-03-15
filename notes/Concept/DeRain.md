Classic : 
* Deep Joint Rain Detection and Removal from a Single Image

Semi-supervised Transfer Learning for Image Rain Removal

* binary map to locates rain streak
* comprising rain streak layer & background layer

multi-task
* binary rain streak map
* clean background

problem:
* overlapping between rain steak & background texture pattern
	* over-smoothing
* degradation of rain is complex
	* atmospheric veils (霧氣造成的模糊)is not create
	* different shape & direction of streak
* Most of method use small image patch 

method:
* region-dependent rain model
	* rain-streak binary map
	* 