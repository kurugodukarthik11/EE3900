import numpy as np


def h(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return -0.5
    else:
        return ((-0.5) ** n) + ((-0.5) ** (n - 2))


def sum():
    return h(0) / (1 - (h(0) / h(1)))


s = sum()
print(s < np.inf)
