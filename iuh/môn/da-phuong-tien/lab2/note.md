# ===== 1. Nhập các thư viện cần thiết =====

import numpy as np
# numpy: Thư viện toán học nổi tiếng trong Python, giúp xử lý mảng số, tính toán nhanh, tạo sóng sin, và thực hiện các phép biến đổi Fourier (FFT).

import matplotlib.pyplot as plt
# matplotlib.pyplot: Thư viện vẽ đồ thị phổ biến nhất Python. Dùng để vẽ dạng sóng (waveform) và phổ tần số (spectrum).

from scipy.io import wavfile
# scipy.io.wavfile: Hỗ trợ đọc/ghi file âm thanh dạng WAV, rất tiện cho xử lý tín hiệu số.


# ===== 2. Đọc dữ liệu từ file WAV =====

filename = "example.wav"  # Đổi thành đường dẫn file WAV của bạn
rate, data = wavfile.read(filename)
# wavfile.read() trả về 2 giá trị:
#   - rate: tần số lấy mẫu của file (số mẫu/giây, đơn vị Hz)
#   - data: mảng numpy chứa dữ liệu sóng âm thanh (có thể là int16, int32, float32...)

# Kiểm tra dữ liệu là mono hay stereo (1 kênh hay 2 kênh)
if data.ndim == 2:        # Nếu là stereo (dạng (N, 2))
    data = data[:, 0]     # Chỉ lấy kênh đầu tiên để đơn giản hóa xử lý

# In thông tin cơ bản về file âm thanh
print("Tần số lấy mẫu (Hz):", rate)
print("Số mẫu âm thanh:", len(data))
print("Kiểu dữ liệu:", data.dtype)


# ===== 3. Vẽ dạng sóng (waveform) =====

# Để dễ quan sát, chỉ vẽ 2000 mẫu đầu tiên (nếu file quá dài)
N_show = min(len(data), 2000)

plt.figure()  # Tạo cửa sổ đồ thị mới
plt.plot(np.arange(N_show), data[:N_show])
# np.arange(N_show): tạo mảng số thứ tự 0, 1, 2, ..., N_show-1 (tức là trục X)
# data[:N_show]: lấy 2000 mẫu đầu tiên (tức là trục Y - biên độ âm thanh)

plt.title("Waveform ({} samples)".format(N_show))  # Tiêu đề
plt.xlabel("Sample")       # Nhãn trục X
plt.ylabel("Amplitude")    # Nhãn trục Y
plt.show()
# Kết quả: Bạn sẽ thấy hình dạng "làn sóng" của âm thanh - gọi là waveform.


# ===== 4. Phân tích phổ tần số bằng FFT =====

# FFT (Fast Fourier Transform) là thuật toán giúp phân tích xem âm thanh chứa những tần số nào.
N = len(data)  # Tổng số mẫu dữ liệu

yf = np.fft.fft(data)  # Tính FFT, trả về một mảng số phức (complex)
# Kết quả yf chứa cả biên độ và pha của từng tần số, nhưng thường ta chỉ quan tâm biên độ (magnitude).

xf = np.fft.fftfreq(N, 1.0 / rate)
# Tạo trục tần số (Hz) tương ứng với từng giá trị trong yf
# N là số mẫu, rate là số mẫu/giây → 1.0/rate là độ rộng giữa 2 mẫu về thời gian.

# Chỉ lấy nửa phổ dương (do FFT đối xứng)
half = N // 2

plt.figure()
plt.plot(xf[:half], np.abs(yf[:half]))
# xf[:half]: trục tần số từ 0 đến gần Nyquist (rate/2)
# np.abs(yf[:half]): lấy trị tuyệt đối phần biên độ (bỏ qua pha)

plt.title("Phổ biên độ (Magnitude Spectrum)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()
# Kết quả: Đồ thị hiển thị các tần số xuất hiện trong âm thanh, tần số nào mạnh sẽ có cột cao.