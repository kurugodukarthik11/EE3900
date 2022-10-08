import matplotlib.pyplot as plt

x = [1, 1]
for i in range(23):
    x.append(x[i] + x[i + 1])
plt.stem(range(25), x)
plt.grid()
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.tight_layout()
plt.show()
plt.savefig('../figs/2_2.pdf')
