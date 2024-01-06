---
date: 2024-01-05 13:48:39
title: Boxplot
tags: statistics, plots
---

A boxplot is a standardized way of displaying the distribution of data based on a five number summary (“minimum”, first quartile (Q1), median, third quartile (Q3), and “maximum”). It can tell you about your outliers and what their values are. It can also tell you if your data is symmetrical, how tightly your data is grouped, and if and how your data is skewed.

```python
import numpy as np
import seaborn as sns

np.random.seed(10) # Set a seed for reproducibility

collection_1 = np.random.normal(100, 10, 200)
collection_2 = np.random.normal(80, 30, 200)
collection_3 = np.random.normal(90, 20, 200)
collection_4 = np.random.normal(70, 25, 200)

data = [collection_1, collection_2, collection_3, collection_4]

sns.boxplot(data=data)
```

![Boxplot](/images/boxplot.png)

The boxplot is one of the most useful [[plots]] in Exploratory Data Analysis to understand the distribution of data. The box shows the earlier mentioned quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be “outliers” using a method that is a function of the inter-quartile range.

## References

- [[https://en.wikipedia.org/wiki/Box_plot]]
- [[https://matplotlib.org/3.1.1/gallery/pyplots/boxplot_demo_pyplot.html]]