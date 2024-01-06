---
date: 2023-10-02 10:00:00
title: Normal Distribution
tags: statistics, probability
---

A normal distribution is a distribution that is symmetric around the mean, showing that data near the mean are more frequent in occurrence than data far from the mean. In graph form, normal distribution will appear as a bell curve.

The probability density function of the normal distribution is given by:

$$
f(x \mid \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

where $\mu$ is the mean and $\sigma^2$ is the variance.

The mean and variance of the normal distribution are given by:

$$
\begin{align}
\mu &= \mu \\
\sigma^2 &= \sigma^2
\end{align}
$$

An example of a normal distribution in Python:

```python
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()
```

![Normal Distribution](/images/normal-distribution.png)

The normal distribution is the most important probability distribution in statistics because it fits many natural phenomena. For example, heights, blood pressure, measurement error, and IQ scores follow the normal distribution. It is also known as the Gaussian distribution and the bell curve.

The mean and standard deviation are required to create a normal distribution curve. The standard deviation is the measure of how spread out numbers are and is calculated as the square root of the variance. The variance is calculated as the average of the squared differences from the mean.

Another distribution which features a bell-shaped curve is the Students t-distribution, but has larger tails than the normal distribution. The t-distribution is used when the sample size is small, and the population standard deviation is unknown.

## References

- https://en.wikipedia.org/wiki/Normal_distribution
- https://www.youtube.com/watch?v=rzFX5NWojp0