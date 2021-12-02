import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq
from scipy.io import wavfile
from scipy.misc import derivative


sample_rate, data = wavfile.read('4.wav')


duration = data.shape[0] / sample_rate
time = np.linspace(0., duration, data.shape[0])


# Fourier transform P(f)
yf = rfft(data[:, 0])
xf = rfftfreq(data.shape[0], 1 / sample_rate)
plt.plot(xf, np.abs(yf))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
# plt.savefig('foo1.png')

# P(t)
y = data[:, 0]
x = time

plt.show()
plt.plot(x, y)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
# plt.savefig('foo2.png')
plt.show()