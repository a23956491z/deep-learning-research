---
tags: unsupervised, meta-learning
---
* Learn a learning procedure,  without supervision.
* Transfer prior experience to learn 
* enable few-shot learning of new tasks without needing any labeld data

emdedding learning
everage unsupervised embeddings to propose tasks

Oracle in Experiemnt means **Supervised**

Preliminary:
* Unsupervised embedding learning:
	* take unlabeled dataset $\mathcal D = \{x_i\}$ as input
	* outputs mapping from $\{x_i\}$ to $\{z_i\}$
* Task
	* $M$-way $K$-shot
	* classification task $\mathcal T$  consists of $K$ training datapoints and labels $\{(x_k, l_k)\}$ per class used for learning a classifier
	* $Q$  query datapoints and labels per class to evaluate.
	* so a task is $K+Q = R$ for each of the $M$ classes
* Meta-learning
	* Supervised meta-leanring algorithm $\mathcal M$ takes a set of supervised meta-training task $\{\mathcal T_t\}$ as input
	* Produces a leanring procedure $\mathcal F$, which can injest the supervised training data of a task to produce a classifier $f$
* Task generation for meta-learning
	* 

Meta learning alg:
* MAML to learn initial parameters that make a classifier leart a effective generalization from a few gradient steps. 
* ProtoNets aim to meta-learn a representation in which a class is effcetively identified by its prototype, which is the **mean** of the class's training examples.

