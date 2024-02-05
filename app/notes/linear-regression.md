---
date: 2024-01-09 10:56:00
title: Linear regression
tags: statistics, models
---

Linear regression is a statistical model that tries to find a linear relationship between a dependent variable a independent variable. The model is defined as:

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon
$$

Where $y$ is the dependent variable, $x_1, x_2, \dots, x_n$ are the independent variables, $\beta_0, \beta_1, \dots, \beta_n$ are the coefficients and $\epsilon$ is the error term.

The coefficients are estimated using the least squares method. This method tries to minimize the sum of the squared errors. The error is defined as the difference between the predicted value and the actual value. The predicted value is calculated using the model.

$$
\epsilon = y - \hat{y}
$$

The model can be used to predict the value of the dependent variable for a given set of independent variables. The predicted value is calculated using the model.

$$
\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n
$$

An example of linear regression in Python:

```python
from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme(style="whitegrid")

a = 0.4  # slope
b = 1.1  # intercept
n = 100  # number of instances

np.random.seed(42)  # set seed for reproducibility

x = np.random.uniform(0, 10, n)
y = b + a * x + np.random.normal(0, 1, n)

model = linregress(x, y)

plt.figure(figsize=(10, 5))
plt.plot(x, x * model.slope + model.intercept, "r-", label="Predictions")
plt.plot(x, y, "b.")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()
```

![Linear regression](/images/linear-regression.png)

## References

- https://en.wikipedia.org/wiki/Linear_regression
- https://www.youtube.com/watch?v=7ArmBVF2dCs
- https://www.kaggle.com/datasets/arejet/simple-linear-regression
