import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

file_path = "C:/Users/남현승/Desktop/programing/etc/AUDIO/sull.wav"

sample_rate, audio_data = wavfile.read(file_path)

frequencies, times, spectrogram_data = spectrogram(audio_data, fs=sample_rate)

plt.figure(figsize=(10, 4))
plt.title("Spectrogram of Audio")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.imshow(10 * np.log10(spectrogram_data), aspect='auto', cmap='inferno')
plt.colorbar(label='Intensity (dB)')
plt.show()
