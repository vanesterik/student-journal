---
date: 2024-01-06 13:20:09
title: Violinplot
tags: statistics, plots
---

The Violinplot is a combination of a [[boxplot]] and a density plot. It shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared. Unlike a box plot, in which all of the plot components correspond to actual datapoints, the violin plot features a kernel density estimation of the underlying distribution.

The advantage of violin plots over boxplots is that they show the full distribution of the data. In addition, their shapes are easier to interpret and compare between groups.

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

sns.violinplot(
    data=sns.load_dataset("titanic"),
    x="age",
    y="sex",
    hue="alive",
    split=True,
    inner="quart",
)

```

![Violinplot](/images/violinplot.png)

## References

- https://en.wikipedia.org/wiki/Violin_plot
- https://seaborn.pydata.org/generated/seaborn.violinplot.html