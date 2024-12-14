import numpy as np
import matplotlib.pyplot as plt

# t is an array of evenly spaced times between 0 and 1 second. 
# pulse is a pure sin wave that represents the signals sent by the radar.
# echoes are the same signal as pulse but shifted over
# noise is a list of random numbers for each datapoint in pulse
# we add each element from the lists in their corresponding positions. This creates the final signal.

fs = 200  # Sampling frequency
t = np.linspace(0, 1, fs)  # 1 second
pulse = np.sin(2 * np.pi * 50 * t)  # 1 kHz pulse

# Simulated echoes
echo1 = np.roll(pulse, 500) * 0.6  # Delay of 500 samples, scaled amplitude
echo2 = np.roll(pulse, 1000) * 0.3  # Delay of 1000 samples, scaled amplitude

# Add noise and combine
noise = np.random.normal(0, 0.1, len(t))
received_signal = pulse + echo1 + echo2 + noise
