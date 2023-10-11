from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_file("C:/Users/남현승/Desktop/programing/etc/AUDIO/sull.wav")

sample_rate = audio.frame_rate
print(f"샘플링 레이트: {sample_rate} Hz")

duration_in_seconds = len(audio) / 1000
print(f"재생 시간(초): {duration_in_seconds} 초")

duration_in_minutes = duration_in_seconds / 60
print(f"재생 시간(분): {duration_in_minutes} 분")

play(audio)
