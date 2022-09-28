import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

fft_time = np.loadtxt('fft_time.txt', dtype=float)
conv_time = np.loadtxt('conv_time.txt', dtype=float)

N = np.logspace(1, len(fft_time), num=len(fft_time), base=2)

fft_fit = optimize.curve_fit(lambda x, a: a * x * np.log(x), N, fft_time)[0]
conv_fit = optimize.curve_fit(lambda x, a: a * x * x, N, conv_time)[0]

plt.plot(N, fft_fit * N * np.log(N))
plt.plot(N, conv_fit * N * N)
plt.plot(N, fft_time, 'o', label='FFT/IFFT')
plt.plot(N, conv_time, 'o', label='Convolution')
plt.xlabel('Size of input')
plt.legend()
plt.grid()
plt.savefig('../figs/7_13.pdf')
plt.show()
