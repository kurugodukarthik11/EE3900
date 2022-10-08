import numpy as np

alpha = (1 + np.sqrt(5)) / 2
beta = (1 - np.sqrt(5)) / 2
n = 50

lh1 = (1 / (alpha - beta)) * ((alpha * ((alpha ** n) - 1) / (alpha - 1)) - (beta * ((beta ** n) - 1) / (beta - 1)))
rh1 = (alpha ** (n + 2) - beta ** (n + 2)) / (alpha - beta)
print(np.allclose(lh1, rh1 - 1))

k = np.linspace(1, n, n)
lh2 = ((alpha ** k - beta ** k) / (alpha - beta)) / (10 ** k)
print(abs(np.sum(lh2) - (10 / 89)) < 1e-6)

b = [1]
a = ((alpha ** k - beta ** k) / (alpha - beta))
for i in range(1, n - 1):
    b.append(a[i - 1] + a[i + 1])
rh3 = alpha ** k + beta ** k
print(np.allclose(b, rh3[:n - 1]))

k1 = k[:n - 1]
lh4 = b / (10 ** k1)
print(abs(np.sum(lh4)-(8/89)) < 1e-6)
