#TODO

#impliment code to determine the distance of an object using the echo in the signal

from scipy.fftpack import fft
from simulatedSignal import received_signal
from simulatedSignal import fs

echo_distances = [lag / fs * 343 for lag in peak_lags]
print(f"Echo distances: {echo_distances}")
