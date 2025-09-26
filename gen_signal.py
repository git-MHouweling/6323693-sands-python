import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def create_sine_signal(A, F, S, E, S_R):
    """
    :param A: Amplitude
    :param F: Frequency
    :param S: Start function
    :param E: End function
    :param S_R: Sample rate
    :return: t,y
    """
    N = int((E - S) * S_R)                                  # Total number of samples
    t = np.linspace(S, E, N)                                # Time
    y= A*np.sin(2*np.pi*F*t)
    return t,y

def create_square_signal(A, F,S, E, S_R):
    """
    :param A: Amplitude
    :param F: Frequency
    :param S: Start function
    :param E: End function
    :param S_R: Sample rate
    :return: t,y
    """
    N = int((E - S) * S_R)
    t = np.linspace(S, E, N)
    y = A*signal.square( np.pi*F* t)
    return t,y

def create_sawtooth_signal(A,F, S, E, S_R):
    """
    :param A: Amplitude
    :param F: Frequency
    :param S: Start function
    :param E: End function
    :param S_R: Sample rate
    :return: t,y
    """
	N = int((E - S) * S_R)
	t = np.linspace(S, E, N)
	y=A*signal.sawtooth( np.pi*F* t)
	return t,y

def create_unitstep_signal(A,T,S,E,S_R):
    """"
    :param A: Amplitude
    :param T: Time of the step
    :param S: Start function
    :param E: End function
    :param S_R: Sample rate
    :return: t,y
    """
	N = int((E - S) * S_R)
	t = np.linspace(S, E, N)
	y = A*(t>=T)
	return t,y

def create_unitpulse_signal(A,T,L, S,E,S_R):
    """"
    :param A: Amplitude
    :param T: Time of the pulse
    :param L: Length of the pulse
    :param S: Start function
    :param E: End function
    :param S_R: Sample rate
    :return: t,y
    """
    N = int((E - S) * S_R)
    t = np.linspace(S, E, N)
    y = A * ((t >= (T - L / 2)) & (t < (T + L / 2)))        #returns A*1 when t is in the area of the pulse and 0 when it is outside
    return t,y

def create_sinc_signal(A, F, S, E, S_R):
    """"
    :param A: Amplitude
    :param F: Frequency
    :param S: Start function
    :param E: End function
    :param S_R: Sample rate
    :return: t,y
    """
    N = int((E - S) * S_R)
    t = np.linspace(S, E, N)
    y=A*((np.sin(np.pi*F*t))/(np.pi*t))
    return t,y

