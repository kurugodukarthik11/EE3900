import numpy as np
import matplotlib.pyplot as plt

N = 14
n = np.arange(N)
fn = (-1 / 2) ** n
hn1 = np.pad(fn, (0, 2), 'constant', constant_values=0)
hn2 = np.pad(fn, (2, 0), 'constant', constant_values=0)
h = hn1 + hn2
# print(hn2)
xtemp = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x = np.pad(xtemp, (0, 8), 'constant', constant_values=0)
# print(x)
X = np.zeros(N) + 1j * np.zeros(N)
# print(X)
for k in range(0, N):
    for n in range(0, N):
        X[k] += x[n] * np.exp(-1j * 2 * np.pi * n * k / N)

H = np.zeros(N) + 1j * np.zeros(N)
for k in range(0, N):
    for n in range(0, N):
        H[k] += h[n] * np.exp(-1j * 2 * np.pi * n * k / N)

Y = np.zeros(N) + 1j * np.zeros(N)
for k in range(0, N):
    Y[k] = X[k] * H[k]

plt.stem(range(0, N), np.real(Y))
plt.title('Y(n)')
plt.xlabel('$n$')
plt.ylabel('$Y(n)$')
plt.grid()
plt.show()