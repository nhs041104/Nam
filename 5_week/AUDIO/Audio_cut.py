from pydub import AudioSegment

input_file = "C:/Users/남현승/Desktop/programing/etc/AUDIO/sull.wav"

audio = AudioSegment.from_file(input_file)

start_time = 3000
end_time = 5000

cut_audio = audio[start_time:end_time]

output_file = "C:/Users/남현승/Desktop/programing/etc/AUDIO/cut_audio.wav"
cut_audio.export(output_file, format="wav")

from pydub.playback import play
play(cut_audio)
