---
date: 2023-12-28 17:07:06
title: Beta Distribution
tags: statistics, probability
---

The Beta distribution is a continuous probability distribution with two parameters, $\alpha$ and $\beta$, and is defined on the interval $[0, 1]$. The Beta distribution is often used as a prior distribution for the parameter $p$ of a [[Bernoulli distribution]] or [[Binomial distribution]].

The probability density function of the Beta distribution is given by:

$$
f(x) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)}
$$

where $B(\alpha, \beta)$ is the Beta function.

The mean and variance of the Beta distribution are given by:

$$
\begin{align}
\mu &= \frac{\alpha}{\alpha + \beta} \\
\sigma^2 &= \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}
\end{align}
$$

The Beta distribution is often used as a prior distribution for the parameter $p$ of a [[Bernoulli distribution]] or [[Binomial distribution]]. The Beta distribution is the conjugate prior of the Bernoulli distribution, meaning that the posterior distribution is also a Beta distribution.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

a, b = 2, 8 # Parameters of the beta distribution (alpha and beta)
x = np.linspace(beta.ppf(0.01, a, b), beta.ppf(0.99, a, b), 100)
plt.plot(x, beta.pdf(x, a, b), color="r")
plt.show()
```

![Beta Distribution](/images/beta-distribution.png)

## References

- https://en.wikipedia.org/wiki/Beta_distribution
- 