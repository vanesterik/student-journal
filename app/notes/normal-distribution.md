---
date: 2023-10-02 10:00:00
title: Normal Distribution
tags: statistics, probability
---

A normal distribution is a distribution that is symmetric around the mean, showing that data near the mean are more frequent in occurrence than data far from the mean. In graph form, normal distribution will appear as a bell curve.

The probability density function of the normal distribution is given by:

$$ f(x;\mu,\sigma) =
\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

where $\mu$ is the mean and $\sigma$ is the standard deviation.

An example of a normal distribution in Python:

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


norm = stats.norm
x = np.linspace(-3, 3, 100)

plt.figure(figsize=(9,5))
plt.plot(x, norm.pdf(x), c="red")
```

![Normal Distribution](/images/normal-distribution.png)

The normal distribution is the most important probability distribution in statistics because it fits many natural phenomena. For example, heights, blood pressure, measurement error, and IQ scores follow the normal distribution. It is also known as the Gaussian distribution and the bell curve.

The mean and standard deviation are required to create a normal distribution curve. The standard deviation is the measure of how spread out numbers are and is calculated as the square root of the variance. The variance is calculated as the average of the squared differences from the mean.

Another distribution which features a bell-shaped curve is the [[Students t-distribution]], but has larger tails than the normal distribution. The t-distribution is used when the sample size is small, and the population standard deviation is unknown.

## References

- https://en.wikipedia.org/wiki/Normal_distribution
- https://www.youtube.com/watch?v=rzFX5NWojp0