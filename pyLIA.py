__version__ = '0.3'
import numpy as np

def LIA(data,sampling_freq,load_freq):
    """
    Function to obtain magnitude and phase of a thermal signal usign a lock-in analyzer
    
    Arguments:
        data {np.array} -- Sequence of thermal images [frames, height, width]
        sampling_freq {float} -- Sampling frequency of thermal video [Hz]
        load_freq {float} -- Frequency of excitaiton load [Hz]
    
    Returns:
        mag -- Magnitude of locked-in signal [units of thermal video]
        ph -- Phase of locked-in signal [deg -- degrees]
    """
    t = np.linspace(0, data.shape[0]/sampling_freq, data.shape[0], endpoint = True) # Time vector
    sine = np.sin(load_freq * t * 2 * np.pi) # Sine wave at the expected thermal frequency (i.e. the load frequency)
    cosine = np.cos(load_freq * t * 2 * np.pi) # Cosine wave at the expected thermal frequency (i.e. the load frequency)

    S = (np.ones((data.shape[0], data.shape[1], data.shape[2])).T*sine).T 
    C = (np.ones((data.shape[0], data.shape[1], data.shape[2])).T*cosine).T 

    L1 = S * data # sine matrix * data matrix
    L2 = C * data # cosine matrix * data matrix
    Re = 2 * np.trapz(L1, axis = 0)/data.shape[0] # real part
    Img = 2 * np.trapz(L2, axis = 0)/data.shape[0] #imaginary part
    
    mag = np.sqrt(Re**2 + Img**2) # magnitude
    ph = np.arctan(Img/Re) * 180/np.pi #phase in degrees

    return mag, ph
