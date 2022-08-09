import numpy as np
import matplotlib.pyplot as plt

file1 = open('abc.dat', 'r')
Lines = file1.readlines()
x = [int(x1) for x1 in list(Lines[0].split())]
y = [float(y1) for y1 in list(Lines[1].split())]

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
