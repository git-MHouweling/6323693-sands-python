import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def create_sine_signal(A, F, D, S_R):                  #Amplitude, Frequency, Duration, Sample_rate
	t=np.linspace(0, D, int(S_R))
	return np.sin(2*np.pi*F*t)

def create_square_signal(A, F, D, S_R):     #Amplitude,Frequency, duration, sample_rate
    t=np.linspace(0, D, int(S_R))
    return A*signal.square( np.pi*F* t)

def create_sawtooth_signal(A,F, D, S_R):     #Amplitude,Frequency, duration, sample_rate
    t=np.linspace(0, D, int(S_R))
    return A*signal.sawtooth( np.pi*F* t)

