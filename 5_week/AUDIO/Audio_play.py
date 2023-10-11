from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_file("C:/Users/남현승/Desktop/programing/etc/AUDIO/sull.wav")

play(audio)
