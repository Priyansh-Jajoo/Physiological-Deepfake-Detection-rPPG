import numpy as np
from scipy.fft import fft

def calculate_snr(signal, fs=30):
    """Calculates Biological SNR using FFT within the human heart rate window."""
    n = len(signal)
    fft_values = np.abs(fft(signal - np.mean(signal))) # Detrending
    freqs = np.fft.fftfreq(n, 1/fs)
    
    # Filter: 0.7Hz (42 BPM) to 4Hz (240 BPM)
    valid_range = (freqs >= 0.7) & (freqs <= 4.0)
    power_spectrum = fft_values[valid_range]
    
    if len(power_spectrum) == 0: return 0
    return np.max(power_spectrum) / np.mean(fft_values)
