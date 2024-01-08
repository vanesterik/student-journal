---
date: 2024-01-07 14:49:56
title: L1 Regularization
tags: statistics, methods
---

The L1 regularization adds a penalty equal to the sum of the absolute value of the coefficients. In other words, it limits the size of the coefficients. The L1 regularization is also known as Lasso Regression.

The mathematical equation for L1 regularization is:

$$L = \frac{1}{n} \sum_i (y_i - \hat{y}_i)^2 + \alpha \sum_j |\beta_j|$$

where $\alpha$ is the regularization parameter and $\beta_j$ is the $j$th coefficient.

The L1 regularization is useful when we want to select the most important features of our data. It is also useful when we want to discard some features that are correlated, as the L1 regularization will select only one feature among the correlated ones.

It does this due the fact that the L1 norm is the sum of the absolute values of the coefficients. This means that the L1 regularization will select only features that are not zero and therefore will discard insignificant features.

## References

- https://en.wikipedia.org/wiki/Lasso_(statistics)
- https://www.youtube.com/watch?v=NGf0voTMlcs