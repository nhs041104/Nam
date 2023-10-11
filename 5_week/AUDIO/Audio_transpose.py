from pydub import AudioSegment

audio = AudioSegment.from_file("C:/Users/남현승/Desktop/programing/etc/AUDIO/sull.wav")

new_sample_rate = 22000
audio = audio.set_frame_rate(new_sample_rate)

output_path = "C:/Users/남현승/Desktop/programing/etc/AUDIO/sull_22kHz.wav"
audio.export(output_path, format="wav")
