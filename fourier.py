import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq
from scipy.io import wavfile
from scipy.misc import derivative
from sys import getsizeof


def read_wav(file_name):
    sample_rate, data = wavfile.read(file_name)
    duration = data.shape[0] / sample_rate
    time = np.linspace(0., duration, data.shape[0])
    amp_by_time = data if len(data.shape) == 1 else data[:, 0]
    samples_count = data.shape[0]
    return amp_by_time, time, sample_rate, duration, samples_count


def plot_sound(amp_by_time, time):
    plt.plot(time, amp_by_time)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()


def plot_fourier_diagram(amp_by_time, samples_count, sample_rate):
    yf = np.abs(rfft(amp_by_time))
    xf = rfftfreq(samples_count, 1 / sample_rate)
    plt.plot(xf, yf)
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.show()


def plot_spectrogram(amp_by_time, sample_rate):
    spectrum, frequencies, times, im = plt.specgram(amp_by_time, NFFT=int(sample_rate / 50), Fs=sample_rate)
    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrum))
    plt.show()
    index_of_freq = int(800 / 50)
    freq = frequencies[index_of_freq]
    y = spectrum[index_of_freq]
    x = times
    #poly = np.poly1d(np.polyfit(x, y, 10))
    plt.plot(x, y)
    plt.xlabel("Time [s]")

    plt.ylabel(f"Amplitude of {freq} Hz")
    plt.show()


def plot_wav_file(file_name):
    amp_by_time, time, sample_rate, duration, samples_count = read_wav(file_name)
    plot_sound(amp_by_time, time)


def plot_fourier_diagram_of_wav(file_name):
    amp_by_time, time, sample_rate, duration, samples_count = read_wav(file_name)
    plot_fourier_diagram(amp_by_time, samples_count, sample_rate)


def plot_spectrogram_of_wav(file_name):
    amp_by_time, time, sample_rate, duration, samples_count = read_wav(file_name)
    plot_spectrogram(amp_by_time, sample_rate)


def plot_everything_about_wav(file_name):
    plot_wav_file(file_name)
    plot_fourier_diagram_of_wav(file_name)
    plot_spectrogram_of_wav(file_name)


plot_everything_about_wav('3.wav')
""""

MAX = np.amax(spectrum)
ZERO = np.amin(spectrum)

freq = frequencies[300]
y = spectrum[300]
print(y)
x = times
plt.plot(x, y)
plt.xlabel("Time [s]")

plt.ylabel(f"Amplitude of {freq} Hz")
plt.show()
"""
