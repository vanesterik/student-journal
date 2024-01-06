---
date: 2023-10-02 10:00:00
title: Binomial Distribution
tags: statistics, probability
---

The Binomial distribution is a discrete probability distribution with two parameters, $n$ and $p$, and is defined on the interval $[0, n]$. The Binomial distribution is often used to model the number of successes in a sequence of $n$ independent experiments, each asking a yes–no question, and each with its own boolean-valued outcome: success/yes/true/one (with probability $p$) or failure/no/false/zero (with probability $q = 1 - p$), which is defined as an [[Bernoulli distribution]]. The Binomial distribution is the sum of $n$ independent Bernoulli random variables.

The probability mass function of the Binomial distribution is given by:

$$
f(k, n, p) = \Pr(k; n, p) = \Pr(X = k) = \binom{n}{k}p^k(1 - p)^{n - k}
$$

where $k$ is the number of successes, $n$ is the number of trials, and $p$ is the probability of success.

The mean and variance of the Binomial distribution are given by:

$$
\begin{align}
\mu &= np \\
\sigma^2 &= np(1 - p)
\end{align}
$$

An example of a Binomial distribution in Python:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n, p = 400, 0.5 # Parameters of the binomial distribution (n and p)
x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
plt.scatter(x, binom.pmf(x, n, p), color="r")
plt.show()
```

![Binomial Distribution](/images/binomial-distribution.png)

## References

- https://en.wikipedia.org/wiki/Binomial_distribution
- https://www.youtube.com/watch?v=J8jNoF-K8E8