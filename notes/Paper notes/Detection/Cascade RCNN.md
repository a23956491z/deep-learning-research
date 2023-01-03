Detector need to solve:
* Recognition : distinguish foreground objects
* Localization : assign accurate bounding boxes to objects

This 2 problems are difficult:
* too many "Close" false positive which means the bounding box is close but not correct
* use Intersection over union (IoU) threshold  $u$ to define positive/negative

IoU:
* typically $u=0.5$, however it's too loose for positives
* A hypotheses is that humans would consider close false positives pass IoU > 0.5
* Examples under $u=0.5$ are diversified and make it difficult to reject close positives


