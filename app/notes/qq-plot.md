---
date: 2024-01-07 14:57:52
title: QQ Plot
tags: statistics, plots
---

The QQ plot is a graphical technique (or a [[scatterplot]]) for determining if two data sets come from populations with a common distribution. A QQ plot is a plot of the quantiles of the first data set against the quantiles of the second data set. By a quantile, we mean the fraction (or percent) of points below the given value. That is, the $i$th quantile is the point at which $i$% percent of the data fall below that value.



```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

alpha = 10
n = 1000
rng = np.random.default_rng(42)
data = stats.skewnorm.rvs(a=alpha, size=n, random_state=rng)

stats.probplot(data, plot=plt, dist=stats.norm)

plt.show()
```

![QQ Plot](/images/qq-plot.png)

## References

- https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot
- https://www.youtube.com/watch?v=okjYjClSjOg
