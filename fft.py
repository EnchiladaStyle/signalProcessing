# impliments the fast furiour transform to gat the frequency data of a signal

from scipy.fftpack import fft
from simulatedSignal import received_signal
from simulatedSignal import t
from simulatedSignal import fs
import numpy as np
import matplotlib.pyplot as plt

freqs = np.fft.fftfreq(len(t), d=1/fs)
fft_values = fft(received_signal)
plt.plot(freqs[:len(freqs)//2], np.abs(fft_values)[:len(fft_values)//2])
plt.title("Frequency Spectrum of the Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()
