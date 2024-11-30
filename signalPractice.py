import numpy as np
import matplotlib.pyplot as plt

fs = 100  # Sampling frequency
t = np.linspace(0, 1, fs)  # 1 second
pulse = np.sin(2 * np.pi * 1000 * t)  # 1 kHz pulse

# Simulated echoes
echo1 = np.roll(pulse, 500) * 0.6  # Delay of 500 samples, scaled amplitude
echo2 = np.roll(pulse, 1000) * 0.3  # Delay of 1000 samples, scaled amplitude

# Add noise and combine
noise = np.random.normal(0, 0.1, len(t))
received_signal = pulse + echo1 + echo2 + noise

plt.plot(t, received_signal)
plt.title("Simulated Sonar Echo Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
