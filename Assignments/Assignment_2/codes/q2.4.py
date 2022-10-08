import matplotlib.pyplot as plt
import numpy as np

x = [1, 1]
for i in range(23):
    x.append(x[i] + x[i + 1])
y = np.add(x[:23], x[2:])
plt.stem(range(23), y)
plt.grid()
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.tight_layout()
plt.show()
plt.savefig('../figs/2_4.pdf')
