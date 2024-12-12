# determines the cross correlation and plots it on a graph

from scipy.fftpack import fft
from simulatedSignal import received_signal
from simulatedSignal import t
from simulatedSignal import fs
from simulatedSignal import pulse
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import correlate
correlation = correlate(received_signal, pulse, mode='full')
lags = np.arange(-len(received_signal)+1, len(received_signal))
plt.plot(lags / fs, correlation)
plt.title("Cross-Correlation")
plt.xlabel("Lag (s)")
plt.ylabel("Correlation")
plt.show()
