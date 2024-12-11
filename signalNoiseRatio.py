#TODO
#use the fast fourier transform to determine what is just noise and then filter it out.

from scipy.fftpack import fft
from simulatedSignal import received_signal
from simulatedSignal import t
from simulatedSignal import fs
import numpy as np
import matplotlib.pyplot as plt