# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 06:41:07 2025

@author: Le Thanh Long 
"""

import wave
import contextlib

filename = "D:/mon/da-phuong-tien/lab2/sample-6s.wav"  # Thay bằng đường dẫn file của bạn

# # Mở file WAV để lấy thông tin
# with contextlib.closing(wave.open(filename, 'rb')) as audio:
#     channels = audio.getnchannels()          # Số kênh (mono/stereo)
#     sample_width = audio.getsampwidth()      # Độ sâu bit mỗi mẫu (bytes)
#     framerate = audio.getframerate()         # Tần số lấy mẫu (Hz)
#     nframes = audio.getnframes()             # Tổng số frame
#     duration = nframes / float(framerate)    # Thời lượng (giây)

#     print("Số kênh:", channels)
#     print("Độ sâu bit (bytes):", sample_width)
#     print("Tần số lấy mẫu (Hz):", framerate)
#     print("Số frame:", nframes)
#     print("Thời lượng (giây):", duration)


from scipy.io import wavfile

# # rate, data = wavfile.read(filename)
# # print("Tần số lấy mẫu (rate):", rate)
# # print("Shape của data:", data.shape)  # (số mẫu, số kênh)
# # print("Kiểu dữ liệu:", data.dtype)

# import numpy as np
# from scipy.io.wavfile import write

# fs = 16000  # Tần số lấy mẫu (Hz)
# t = np.linspace(0, 1.0, int(fs), endpoint=False)  # Mảng thời gian từ 0 đến 1 giây

# # Tạo sóng sin tần số 440Hz (A4)
# tone = 0.2 * np.sin(2 * np.pi * 440 * t)  # Biên độ 0.2 để không bị méo

# # Chuẩn hóa về int16 để ghi WAV 16-bit
# tone_int16 = (tone * 32767).astype(np.int16)

# # Ghi ra file WAV
# write("D:/mon/da-phuong-tien/lab2/output/tone_440Hz.wav", fs, tone_int16)
# print("Đã ghi file tone_440Hz.wav")



import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Đọc file WAV

rate, data = wavfile.read(filename)

# Nếu là stereo thì lấy 1 kênh
if data.ndim == 2:
    data = data[:, 0]

# Vẽ waveform (lấy 2000 mẫu đầu cho dễ nhìn)
N_show = min(len(data), 2000)
plt.figure()
plt.plot(np.arange(N_show), data[:N_show])
plt.title("Waveform ({} samples)".format(N_show))
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.show()

# Phân tích phổ tần số bằng FFT
N = len(data)
yf = np.fft.fft(data)               # FFT ra tín hiệu phức
xf = np.fft.fftfreq(N, 1.0 / rate)  # Trục tần số tương ứng (Hz)

# Chỉ lấy nửa dương (tần số dương)
half = N // 2
plt.figure()
plt.plot(xf[:half], np.abs(yf[:half]))
plt.title("Phổ biên độ (Magnitude Spectrum)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()
