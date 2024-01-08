---
date: 2023-12-28 17:14:06
title: Poisson Distribution
tags: statistics, probability
---

The Poisson distribution is a discrete probability distribution with one parameter, $\lambda$, and is defined on the interval $[0, \infty)$. The Poisson distribution is often used to model the number of events occurring in a fixed period of time, given the average number of times the event occurs over that time period. The Poisson distribution is a limiting case of the [[Binomial distribution]] where $n \to \infty$ and $p \to 0$ such that $np = \lambda$.

The probability mass function of the Poisson distribution is given by:

$$
f(k, \lambda) = \Pr(k; \lambda) = \Pr(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

where $k$ is the number of events, and $\lambda$ is the average number of events.

The mean and variance of the Poisson distribution are given by:

$$
\begin{align}
\mu &= \lambda \\
\sigma^2 &= \lambda
\end{align}
$$

An example of a Poisson distribution in Python:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

mu = 2.6 # Parameter of the poisson distribution (lambda)
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
plt.scatter(x, poisson.pmf(x, mu), color="r")
plt.show()
```

![Poisson Distribution](/images/poisson-distribution.png)

## References

- https://en.wikipedia.org/wiki/Poisson_distribution