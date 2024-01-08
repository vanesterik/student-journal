---
date: 2024-01-06 15:17:54
title: Monte Carlo Method
tags: statistics, methods
---

The Monte Carlo method is a technique for approximating the value of a function by randomly sampling from the domain of the function. The method is often used to approximate the value of an integral.

Consider the function $f(x) = x^2$ on the interval $[0, 1]$. The area under the curve of this function is equal to $\frac{1}{3}$. We can approximate this value by randomly sampling from the domain of the function and counting the number of samples that fall under the curve. The ratio of the number of samples under the curve to the total number of samples will approximate the area under the curve.

```python
import numpy as np

def f(x):
    """
    Calculate the square of a given number.

    Parameters:
    x (float): The number to be squared.

    Returns:
    float: The square of the input number.
    """
    return x**2

def monte_carlo(f, a, b, n):
    """
    Perform Monte Carlo integration to estimate the area under the curve of a given function.

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower bound of the integration interval.
    b (float): The upper bound of the integration interval.
    n (int): The number of random samples to be generated.

    Returns:
    float: The estimated area under the curve.
    """
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, 1, n)
    return np.sum(y < f(x)) / n

monte_carlo(f, 0, 1, 100000)
```

## References

- https://en.wikipedia.org/wiki/Monte_Carlo_method
- https://www.youtube.com/watch?v=OgO1gpXSUzU