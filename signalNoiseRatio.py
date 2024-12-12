#TODO
#use the fast fourier transform to determine what is just noise and then filter it out.

from scipy.fftpack import fft
from simulatedSignal import received_signal
from simulatedSignal import t
from simulatedSignal import fs
from simulatedSignal import pulse
from simulatedSignal import noise
import numpy as np
import matplotlib.pyplot as plt

signal_power = np.mean(pulse**2)
noise_power = np.mean(noise**2)
snr = 10 * np.log10(signal_power / noise_power)
print(f"Signal-to-Noise Ratio (SNR): {snr:.2f} dB")
