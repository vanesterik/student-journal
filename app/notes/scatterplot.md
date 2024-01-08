---
date: 2024-01-06 13:17:12
title: Scatterplot
tags: statistics, plots
---

The Scatterplot is a type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables for a set of data. If the points are color-coded, one additional variable can be displayed. The data is displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis.

Scatterplots are used to observe relationships between variables. The data is displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis.

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

sns.scatterplot(
    data=sns.load_dataset("tips"),
    x="total_bill",
    y="tip",
    hue="time",
)
```

![Scatterplot](/images/scatterplot.png)

## References

- https://en.wikipedia.org/wiki/Scatter_plot
- https://seaborn.pydata.org/generated/seaborn.scatterplot.html