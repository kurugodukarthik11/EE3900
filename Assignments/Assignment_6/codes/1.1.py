import numpy as np
from matplotlib import pyplot as plt



A = 12
f = 50
t = np.linspace(0, 2 / f, 1000)
plt.plot(t, np.abs(A * np.sin(2 * np.pi * f * t)))
plt.grid()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.savefig('../figs/1.1.pdf')
plt.show()
import shlex
import subprocess
subprocess.run(shlex.split("termux-open ../figs/1.1.pdf"))
