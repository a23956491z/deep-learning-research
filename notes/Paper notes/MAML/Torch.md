
## Dataset
Mini imagenet:
size : 84x84
class: 100 : {training:64, val:16, test:20}
600 imgs per class

Create a dataset:
What we get?
* Images & label file
* label file contains filename and its label

label file example:
```csv
	filename,		label
	img0001.jpg,	n001
	img0002.jpg,	n002
```

1. sort files by label
	* get dictionary like this : 
	```
		{
			'label1' : [
				'img1', 
				'img2',...
			], 
			'label2' : [
				'img3',
				'img4',...
			],...
		}
	```
2. Creating batch : we need `support_set_batch` and `query_set_batch`
3. Looping for batch_size times:
	1. draw `n_way` classes and shuffle
	2. In each class : draw `k_shot` + `k_query` imgs and shuffle, make first `k_shot` imgs to a list and append  to `support_set`  , others also make to list and append to  `query_set`
	3. in every batch, append `support_set` to `support_set_batch`, appned `query_set` to `query_set_batch`


## convt2d
![](https://imgur.com/GOYWq6P.png)

covvt2d is **transposed convolution** aka deconvolution
![](https://imgur.com/pgZ6PTs.png)

## 