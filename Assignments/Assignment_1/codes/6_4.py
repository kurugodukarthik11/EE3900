import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 2, 1])
x = np.pad(x, (0, 9), 'constant', constant_values=0)
# print(x)
# print(x.shape[0])
N = 15


def hn(n):
    if n < 0:
        return 0
    if 0 <= n < 2:
        return (-1 / 2) ** n
    else:
        return (-1 / 2) ** n + (-1 / 2) ** (n - 2)


xk = fft(x)
h_1 = np.array([hn(i) for i in range(N)])
hk = fft(h_1)
yk = xk * hk
yn = ifft(yk)
n_1 = np.array(list(range(N)))
print(xk)
print(hk)
print(yk)
plt.stem(n_1, yn, label="IFFT")
plt.grid()
plt.legend()
plt.show()
