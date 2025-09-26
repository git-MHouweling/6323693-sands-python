import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def create_sine_signal(A, F, S, E, S_R):                    # Amplitude, Frequency, Start function, End function, Sample_rate
	N = int((E - S) * S_R)                                  # Total number of samples
	t = np.linspace(S, E, N)                                # Time
	y= A*np.sin(2*np.pi*F*t)
	return t,y

def create_square_signal(A, F,S, E, S_R):                   # Amplitude,Frequency,Start function, End function, sample_rate
	N = int((E - S) * S_R)                                  # Total number of samples
	t = np.linspace(S, E, N)                                # Time
	y = A*signal.square( np.pi*F* t)
	return t,y

def create_sawtooth_signal(A,F, S, E, S_R):                 # Amplitude,Frequency, Start function, End function, sample_rate
	N = int((E - S) * S_R)                                  # Total number of samples
	t = np.linspace(S, E, N)                                # Time
	y=A*signal.sawtooth( np.pi*F* t)
	return t,y

def create_unitstep_signal(A,T,S,E,S_R):                    # Amplitude,Time of step, Start function, End function, sample_rate
	N = int((E - S) * S_R)                                  # Total number of samples
	t = np.linspace(S, E, N)                                # Time
	y = A*(t>=T)
	return t,y

def create_unitpulse_signal(A,T,L, S,E,S_R):                # Amplitude,Time of step, Start function, End function, sample_rate
    N = int((E - S) * S_R))                                 # Total number of samples
	t = np.linspace(S, E, N)                               # Time
    y= A*()