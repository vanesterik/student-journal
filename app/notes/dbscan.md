---
date: 2024-01-13 13:20:28
title: DBSCAN
tags: statistics, models, clustering
---

DBSCAN stands for Density-Based Spatial Clustering of Applications with Noise. The DBSCAN algorithm is a density-based clustering algorithm, which means that it will cluster points together based on their density. The algorithm will start with a random point and find all the points within the `epsilon` radius. If the number of points is greater than or equal to the `min_samples`, then the algorithm will create a cluster. If the number of points is less than the min_samples, then the algorithm will mark the point as noise. The algorithm will then repeat the process for all the points in the cluster and continue until all points have been visited.

The DBSCAN algorithm has two parameters: `epsilon` and `min_samples`. The `epsilon` parameter is the radius of the cluster. The `min_samples` parameter is the minimum number of points that must be within the `epsilon` radius for the algorithm to create a cluster.

```python
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

X, y = make_moons(n_samples=1000, noise=0.05)

eps = 0.2
min_samples = 5

dbscan = DBSCAN(eps=eps, min_samples=min_samples)
dbscan.fit(X)

plt.figure(figsize=(9, 5))
plt.title(f"DBSCAN: eps={eps}, min_samples={min_samples}")
plt.scatter(X[:, 0], X[:, 1], c=dbscan.labels_, cmap="Spectral")
plt.show()
```

![DBSCAN eps=0.05 min_samples=5](/images/dbscan-suboptimal.png)

![DBSCAN eps=0.2 min_samples=5](/images/dbscan-optimal.png)



## References

- https://en.wikipedia.org/wiki/DBSCAN
- https://www.youtube.com/watch?v=RDZUdRSDOok