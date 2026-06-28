from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt

try:
   
    fs, data = read('sample.wav')

   
    duration = len(data) / fs
    print(f"Tần số lấy mẫu (Sample Rate): {fs} Hz")
    print(f"Thời lượng (Duration): {duration:.2f} giây")

   
    plt.figure(figsize=(12, 4))
    plt.plot(data[:2000])
    plt.title('Biểu đồ sóng âm (2000 mẫu đầu tiên)')
    plt.xlabel('Mẫu (Sample)')
    plt.ylabel('Biên độ (Amplitude)')
    plt.grid(True)
    plt.show()

   
    audio_float = data.astype(np.float32)
    
   
    max_amp = np.max(np.abs(audio_float))
    if max_amp > 0:
        normalized_data = audio_float / max_amp
    else:
        normalized_data = audio_float 

    write('normalized.wav', fs, normalized_data)
    print("Đã chuẩn hóa âm thanh và lưu thành công file 'normalized.wav'")
    
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'sample.wav'. Vui lòng đặt file vào cùng thư mục.")