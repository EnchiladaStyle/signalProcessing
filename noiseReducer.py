#TODO
# remove noise from the signal

from scipy.fftpack import fft
from simulatedSignal import received_signal
from simulatedSignal import t
from simulatedSignal import fs
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import butter, filtfilt
b, a = butter(4, 0.1, btype='low')  # 0.1 is normalized cutoff frequency
denoised_signal = filtfilt(b, a, received_signal)
plt.plot(t, denoised_signal)
plt.title("Denoised Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
