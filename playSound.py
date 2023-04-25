import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import moviepy.editor as mp
import librosa
import librosa.display
from scipy import fftpack
import scipy.signal as sig
from scipy.ndimage import gaussian_filter1d


def playSound(inputFreq)
    filename = "/Users/abbywongny/Desktop/testing.mp4"

    # read audio file
    audio = mp.AudioFileClip(filename)

    # extract audio data and sample rate
    signal = audio.to_soundarray()
    samplerate = audio.fps

    # calculate signal duration in seconds
    duration = len(signal) / samplerate

    # create time vector
    time = [float(i)/samplerate for i in range(len(signal))]

    X = fftpack.fft(signal)
    freq = fftpack.fftfreq(len(X)) * samplerate

    X = X[freq>0]
    freq = freq[freq >0]

    # Normalize the signals
    X = X / np.max(np.abs(X))

    # Use Gaussian Filter to remove the noise
    x_filtered = gaussian_filter1d(signal, 10)

    # Compute the FFT of the signals
    X_filtered = fftpack.fft(x_filtered)
    # Compute the frequency domain
    freq_filtered = fftpack.fftfreq(len(X_filtered)) * samplerate

    # Convert the frequency domain to positive side and below 50Hz
    X_filtered = X_filtered[freq_filtered > 0]
    freq_filtered = freq_filtered[freq_filtered > 0]


    # Normalize the signals
    X_filtered = X_filtered / np.max(np.abs(X_filtered))

    sr = samplerate # sample rate
    carrier_freq = inputFreq # in Hz
    #mod_freq = freq # in Hz
    amplitude = 0.5 # modulation depth (0-1)

    # create time vector
    time = np.linspace(0, duration, int(sr*duration), endpoint=False)

    # create carrier signal
    carrier_signal = np.sin(2*np.pi*carrier_freq*time)

    # create modulating signal
    #mod_signal = np.sin(2*np.pi*mod_freq*time)

    # create modulated signal using amplitude modulation
    modulated_signal = (1 + amplitude*signal) * carrier_signal

    scaled = np.int16(modulated_signal/np.max(np.abs(modulated_signal)) * 32767)
    wavfile.write('modulated_signal.wav', sr, scaled)

    return