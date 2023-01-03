regression networks

metric-learning based method : *prototypical networks*
metric-learning are **leanring to compare**

nueral embedding dimensions are high (e.g. 1600 for *conv-4)*
So in high dimensional embedding spaces the **direction** of data gen-  
erally contains richer information than **magnitude**.

Network comparsion:
* MatchingNet leverages directional information only
* ProtoNet & RelationNet improve by comparing with aggregated class representation
* Regression networks combined both


embedded points by regressing the closest approximation in every class subspace  
while using the regression error as a distance metric