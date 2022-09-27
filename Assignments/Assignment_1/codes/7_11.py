import numpy as np
from numpy.fft import fft


x = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
k = fft(np.eye(len(x)))
X = x @ k
print(X)
