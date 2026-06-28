# 🎧 ĐỀ THI THƯỜNG KỲ – AUDIO XỬ LÝ TÍN HIỆU
# 📌 Công cụ: Python (numpy, scipy, matplotlib, sounddevice, python_speech_features)
# ________________________________________
# PHẦN I – LÝ THUYẾT (5 điểm)
# Câu 1 (1đ):
# Âm thanh số (digital audio) được biểu diễn bởi hai tham số cơ bản:
# 1. **Tần số lấy mẫu (sampling rate)**: Số mẫu tín hiệu được lấy trong một giây (đơn vị: Hz).
# 2. **Độ phân giải bit (bit depth)**: Số bit dùng để biểu diễn giá trị của mỗi mẫu (quyết định độ chi tiết).
# Câu 2 (1đ):
# Định lý Nyquist phát biểu rằng: Để tránh hiện tượng aliasing khi lấy mẫu tín hiệu, tần số lấy mẫu phải lớn hơn hoặc bằng hai lần tần số cao nhất có trong tín hiệu (f_s ≥ 2 * f_max).

# Câu 3 (1đ):
# Trong chuẩn PCM, "quantization" (lượng tử hóa) là quá trình chuyển đổi giá trị biên độ liên tục của tín hiệu analog thành các mức rời rạc (số hữu hạn giá trị) để biểu diễn bằng số trong máy tính.
# Câu 4 (1đ):
# Biến đổi Fourier (FFT) giúp ta phân tích tín hiệu âm thanh theo miền gì?
# - Biến đổi Fourier (FFT) giúp ta phân tích tín hiệu âm thanh theo miền tần số (frequency domain).
# Câu 5 (1đ):
# So sánh giữa waveform (dạng sóng trong miền thời gian) và spectrum (phổ biên độ trong miền tần số). Cho ví dụ ứng dụng thực tế của mỗi loại.
# - **Waveform (dạng sóng miền thời gian):**
#   - Biểu diễn sự thay đổi biên độ của tín hiệu theo thời gian.
#   - Dùng để quan sát hình dạng tín hiệu, phát hiện nhiễu, cắt/gán đoạn âm thanh.
#   - Ứng dụng: chỉnh sửa âm thanh, phát hiện điểm bắt đầu/kết thúc lời nói.
# - **Spectrum (phổ tần số miền tần số):**
#   - Biểu diễn mức năng lượng của các thành phần tần số trong tín hiệu.
#   - Dùng để phân tích đặc tính tần số, nhận diện âm sắc, lọc nhiễu.
#   - Ứng dụng: nhận diện giọng nói, phân tích nhạc, nhận diện nhạc cụ, lọc tạp âm.

# PHẦN II – THỰC HÀNH PYTHON (5 điểm)
# Câu 6 (2đ):
# Viết chương trình đọc file example.wav, in ra: số kênh, tần số lấy mẫu, số frame, thời lượng.
import wave

filename = 'sample-6s.wav'

# with wave.open(filename, 'rb') as wf:
#     n_channels = wf.getnchannels()
#     framerate = wf.getframerate()
#     n_frames = wf.getnframes()
#     duration = n_frames / framerate

# print(f"Số kênh        : {n_channels}")
# print(f"Tần số lấy mẫu : {framerate} Hz")
# print(f"Số frame       : {n_frames}")
# print(f"Thời lượng      : {duration:.2f} giây")

# Câu 7 (1.5đ):
# Dùng numpy.fft để tính và vẽ phổ tần số của file âm thanh trên.
# import numpy as np
# import matplotlib.pyplot as plt
# import wave

# filename = 'sample-6s.wav'

# # Đọc dữ liệu sóng
# with wave.open(filename, 'rb') as wf:
#     framerate = wf.getframerate()
#     n_frames = wf.getnframes()
#     n_channels = wf.getnchannels()
#     audio_bytes = wf.readframes(n_frames)

# # Chuyển dữ liệu sang numpy array
# audio_np = np.frombuffer(audio_bytes, dtype=np.int16)
# if n_channels == 2:
#     audio_np = audio_np[::2]  # Lấy 1 kênh nếu là stereo

# # Tính FFT
# N = len(audio_np)
# yf = np.fft.fft(audio_np)
# xf = np.fft.fftfreq(N, 1/framerate)

# # Vẽ phổ tần số (chỉ lấy nửa đầu phổ)
# plt.figure(figsize=(10,4))
# plt.plot(xf[:N//2], np.abs(yf[:N//2]))
# plt.title('Phổ tần số của file âm thanh')
# plt.xlabel('Tần số (Hz)')
# plt.ylabel('Biên độ')
# plt.grid()
# plt.tight_layout()
# plt.show()

# Câu 8 (1.5đ):
# Ghi âm 3 giây từ micro và lưu ra file my_record.wav.
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

fs = 44100  # Tần số lấy mẫu (Hz)
duration = 3  # Thời gian ghi (giây)

print("Bắt đầu ghi âm...")
audio = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype='int16')
sd.wait()
print("Ghi âm xong, lưu file my_record.wav")

wav.write('my_record.wav', fs, audio)
