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
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

a = 0.4 # slope
b = 1.1 # intercept

x = np.random.uniform(0, 10, 100)
y = a * x + b + np.random.normal(0, 1, 100)

lrmodel = LinearRegression()
lrmodel.fit(x.reshape(-1, 1), y) # reshape(-1, 1) is needed because sklearn expects a 2D array

slope = lrmodel.coef_[0]
intercept = lrmodel.intercept_

plt.figure(figsize=(9, 5))

plt.plot(x, slope * x + intercept,'r-', label='fitted linear model')
plt.scatter(x, y)

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title(f"Linear model, slope = {slope}, intercept = {intercept}")
plt.show()
```

![Linear regression](/images/linear-regression.png)

Below a summary providing key information about the model's fit, significance of the overall model, and the estimated coefficients for each independent variable.

```text
                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:                      y   R-squared (uncentered):                   0.973
Model:                            OLS   Adj. R-squared (uncentered):              0.973
Method:                 Least Squares   F-statistic:                              3555.
Date:                Fri, 12 Jan 2024   Prob (F-statistic):                    2.17e-79
Time:                        14:16:28   Log-Likelihood:                         -80.918
No. Observations:                 100   AIC:                                      163.8
Df Residuals:                      99   BIC:                                      166.4
Df Model:                           1                                                  
Covariance Type:            nonrobust                                                  
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1             0.5663      0.009     59.623      0.000       0.547       0.585
==============================================================================
Omnibus:                       29.982   Durbin-Watson:                   1.476
Prob(Omnibus):                  0.000   Jarque-Bera (JB):                6.568
Skew:                          -0.230   Prob(JB):                       0.0375
Kurtosis:                       1.832   Cond. No.                         1.00
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

Here's how to interpret each part of the table:

### Header Information:

- **Dep. Variable**: The dependent variable in the regression analysis is denoted as "y."
- **R-squared (uncentered)**: The coefficient of determination (R-squared) measures the proportion of the variance in the dependent variable that is predictable from the independent variable(s). In this case, it is 0.973, indicating a high level of explained variance.
- **Model**: Indicates the type of regression model used (OLS - Ordinary Least Squares).
- **Method**: Specifies the method used for estimation (Least Squares).
- **Date and Time**: Timestamp indicating when the analysis was conducted.
- **No. Observations**: The number of observations (data points) in the analysis is 100.

### Regression Results:

- **coef (Coefficient)**: The estimated coefficient for the independent variable (x1) is 0.5663.
- **std err (Standard Error)**: The standard error associated with the coefficient estimate.
- **t ([[t-statistic]])**: The t-statistic measures the number of standard deviations the coefficient estimate is from zero. Here, it is 59.623.
- **P>|t| (P-value)**: The p-value associated with the t-statistic. A low p-value (< 0.05) suggests that the coefficient is statistically significant.
- **[0.025, 0.975]**: The 95% confidence interval for the coefficient estimate.

### Model Fit Statistics:

- **[[F-statistic]]**: A measure of overall model significance. A higher F-statistic with a low p-value indicates a statistically significant regression model.
- **Prob (F-statistic)**: The probability associated with the F-statistic. A low value (2.17e-79) indicates that the overall model is statistically significant.
- **Log-Likelihood**: The log-likelihood value, often used in comparing models.
- **AIC (Akaike Information Criterion)**: A measure of model fit that penalizes models with more parameters.
- **BIC (Bayesian Information Criterion)**: Similar to AIC but with a stronger penalty for additional parameters.

This information helps in assessing the significance and reliability of each variable in predicting the dependent variable in the regression model.

## References

- https://en.wikipedia.org/wiki/Linear_regression
- https://www.youtube.com/watch?v=7ArmBVF2dCs
- https://www.kaggle.com/datasets/arejet/simple-linear-regression
