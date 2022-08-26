import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 2, 1])
y = np.loadtxt('abc.dat', dtype='double')
plt.subplot(2, 1, 1)
plt.stem(range(0, 6), x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(range(0, 20), y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.show()
