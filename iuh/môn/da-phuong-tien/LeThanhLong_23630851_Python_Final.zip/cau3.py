
from pydub import AudioSegment


input_audio = 'input.wav'
output_audio = 'output_clip.wav'


sound = AudioSegment.from_file(input_audio)


start_time = 5 * 1000
end_time = 10 * 1000
clip = sound[start_time:end_time]


normalized_clip = clip.apply_gain(-clip.max_dBFS)


normalized_clip.export(output_audio, format='wav')

print(f"Đã cắt và chuẩn hóa âm thanh, lưu tại: {output_audio}")
