import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

file_path = "C:/Users/남현승/Desktop/programing/etc/AUDIO/sull.wav"

sample_rate, audio_data = wavfile.read(file_path)

plt.figure(figsize=(10, 4))
plt.title("에네르기파")
plt.xlabel("시간 (초)")
plt.ylabel("진폭")
plt.plot(np.arange(len(audio_data)) / sample_rate, audio_data)
plt.grid(True)
plt.show()
