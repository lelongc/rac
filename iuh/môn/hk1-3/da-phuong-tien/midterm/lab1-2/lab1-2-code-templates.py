# -*- coding: utf-8 -*-
"""
🎯 PYTHON CHEAT SHEET THI GIỮA KỲ - LAB1 & LAB2 AUDIO
Author: Lê Thành Long
Date: 2025

🔍 TÌM NHANH THEO ĐỀ BÀI - SỬ DỤNG CTRL+F:
==========================================

📝 LAB1 - ENCODING/DECODING:
• "mã hóa utf-8" → search "A) MÃ HÓA UTF-8"
• "giải mã utf-8" → search "A) GIẢI MÃ UTF-8"  
• "bytes sang string" → search "B) XỬ LÝ BYTES"
• "hex sang binary" → search "hex_val = 0x"
• "text encode" → search "text.encode"
• "độ dài bytes" → search "len(encoded)"

📝 LAB2 - AUDIO PROCESSING:
• "đọc file wav" → search "2A) ĐỌC WAV METADATA"
• "thông tin file wav" → search "read_wav_metadata"
• "ghi file wav" → search "2B) GHI FILE WAV"
• "tạo âm thanh" → search "generate_and_save_tone"
• "vẽ waveform" → search "3A) VẼ WAVEFORM"
• "phân tích phổ" → search "3B) PHÂN TÍCH FFT"
• "fft spectrum" → search "np.fft.fft"
• "ghi âm micro" → search "4A) GHI ÂM"
• "phát lại âm thanh" → search "4B) PHÁT LẠI"
• "sounddevice" → search "import sounddevice"
• "lọc tín hiệu" → search "5A) LỌC THÔNG THẤP"
• "low pass filter" → search "lowpass_filter"
• "high pass filter" → search "highpass_filter"
• "gaussian blur" → search "apply_gaussian_blur"
• "trích xuất mfcc" → search "6A) TRÍCH XUẤT MFCC"
• "python_speech_features" → search "from python_speech_features"
• "so sánh chất lượng" → search "calculate_mse"
• "tính psnr" → search "calculate_psnr"

🎯 DẠNG ĐỀ BÀI THƯỜNG GẶP:
===========================

🏷️ LAB1:
┌─ "Mã hóa chuỗi thành bytes UTF-8" → Copy Section 1A
├─ "Giải mã bytes UTF-8 thành string" → Copy Section 1A  
├─ "Chuyển hex sang binary" → Copy Section 1A
├─ "Xử lý list bytes" → Copy Section 1B
└─ "Tính độ dài bytes" → Copy Section 1B

🏷️ LAB2:
┌─ "Đọc file WAV và hiển thị thông tin" → Copy Section 2A
├─ "Tạo âm thanh từ công thức và lưu WAV" → Copy Section 2B
├─ "Vẽ waveform và phổ tần số" → Copy Section 3
├─ "Ghi âm từ micro và phát lại" → Copy Section 4
├─ "Áp dụng bộ lọc low-pass/high-pass" → Copy Section 5
├─ "Trích xuất đặc trưng MFCC" → Copy Section 6
├─ "So sánh chất lượng âm thanh (MSE/PSNR)" → Copy Section 7
└─ "Bài tổng hợp xử lý âm thanh" → Copy Section 8

⚡ IMPORTS THIẾT YẾU CHO THI:
============================
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import sounddevice as sd
from python_speech_features import mfcc
"""

# =============================================================================
# 1A) MÃ HÓA/GIẢI MÃ UTF-8 - DÙNG KHI ĐỀ VỀ ENCODING
# =============================================================================

def demo_encoding_basic():
    """🎯 Copy khi đề yêu cầu: mã hóa UTF-8, giải mã bytes"""
    
    # Mã hóa string → bytes
    text = "ĐẠI HỌC CÔNG NGHIỆP TP HỒ CHÍ MINH"
    encoded = text.encode('utf-8')
    print("📝 Text gốc:", text)
    print("🔢 Encoded bytes:", encoded)
    print("📏 Độ dài bytes:", len(encoded))
    
    # Giải mã bytes → string
    decoded = encoded.decode('utf-8')
    print("✅ Decoded text:", decoded)
    
    # Chuyển hex → binary (thường có trong đề)
    hex_val = 0xc3
    binary = f"{hex_val:08b}"
    print(f"🔄 Hex {hex(hex_val)} = Binary {binary}")
    
    return encoded, decoded

def demo_encoding_advanced():
    """🎯 Copy khi đề có nhiều chuỗi và yêu cầu so sánh"""
    
    # Ví dụ từ đề thi thường gặp
    s1 = "résumé"
    s2 = "El Niño" 
    
    s1_encoded = s1.encode("utf-8")
    s2_encoded = s2.encode("utf-8")
    
    print("📊 SO SÁNH ENCODING:")
    print(f"S1: '{s1}' → {s1_encoded} (len={len(s1_encoded)})")
    print(f"S2: '{s2}' → {s2_encoded} (len={len(s2_encoded)})")
    
    # Chuyển nhiều hex sang binary cùng lúc
    hex_bytes = [0xc3, 0xb1]
    binary_str = " ".join(f"{i:08b}" for i in hex_bytes)
    print(f"🔢 Hex bytes {hex_bytes} → Binary: {binary_str}")

# =============================================================================
# 1B) XỬ LÝ BYTES LIST - DÙNG KHI ĐỀ CHO SẴN BYTES
# =============================================================================

def process_given_bytes():
    """🎯 Copy khi đề cho sẵn bytes và yêu cầu xử lý"""
    
    # Từ bytes → list số
    data = b'\xf0\x9f\xa4\xa8'
    byte_list = list(data)
    print("📋 Bytes as list:", byte_list)
    print("📏 Số bytes:", len(data))
    
    # Ví dụ bytes phức tạp (từ đề thật)
    s1 = b'Vi\xe1\xbb\x87t Nam m\xe1\xba\xbfn y\xc3\xaau'
    s2 = b'ng\xc6\xb0\xe1\xbb\x9di Vi\xe1\xbb\x87t'
    
    try:
        s1_decoded = s1.decode('utf-8')
        s2_decoded = s2.decode('utf-8')
        
        print("🇻🇳 Vietnamese text decoded:")
        print(f"S1: {s1_decoded}")
        print(f"S2: {s2_decoded}")
        print(f"📏 S1 byte length: {len(s1)}")
        print(f"📏 S2 byte length: {len(s2)}")
        
    except UnicodeDecodeError as e:
        print(f"❌ Decode error: {e}")

# =============================================================================
# 2A) ĐỌC WAV METADATA - DÙNG KHI ĐỀ YÊU CẦU THÔNG TIN FILE
# =============================================================================

def read_wav_metadata(filename):
    """🎯 Copy khi đề yêu cầu: đọc thông tin file WAV chi tiết"""
    import wave
    import contextlib
    
    print(f"🎵 PHÂN TÍCH FILE: {filename}")
    print("=" * 40)
    
    with contextlib.closing(wave.open(filename, 'rb')) as audio:
        channels = audio.getnchannels()
        sample_width = audio.getsampwidth()  
        framerate = audio.getframerate()
        nframes = audio.getnframes()
        duration = nframes / float(framerate)
        
        print(f"📻 Số kênh: {channels} ({'Mono' if channels == 1 else 'Stereo'})")
        print(f"🔢 Độ sâu bit: {sample_width * 8} bits")
        print(f"📊 Tần số lấy mẫu: {framerate} Hz")
        print(f"📏 Số frame: {nframes:,}")
        print(f"⏱️  Thời lượng: {duration:.2f} giây")
        print(f"💾 Kích thước: {nframes * channels * sample_width:,} bytes")
        
        return {
            'channels': channels,
            'sample_width': sample_width, 
            'framerate': framerate,
            'nframes': nframes,
            'duration': duration
        }

def read_wav_scipy(filename):
    """🎯 Copy khi cần đọc nhanh bằng scipy"""
    from scipy.io import wavfile
    
    rate, data = wavfile.read(filename)
    
    print(f"🚀 SCIPY READ: {filename}")
    print(f"📊 Sample rate: {rate} Hz")
    print(f"📐 Data shape: {data.shape}")
    print(f"🔢 Data type: {data.dtype}")
    
    # Auto convert stereo → mono
    if data.ndim == 2:
        data = data[:, 0]
        print("🔄 Converted stereo → mono")
    
    return rate, data

# =============================================================================
# 2B) GHI FILE WAV - DÙNG KHI ĐỀ YÊU CẦU TẠO ÂM THANH
# =============================================================================

def generate_and_save_tone():
    """🎯 Copy khi đề yêu cầu: tạo âm từ công thức toán học"""
    import numpy as np
    from scipy.io.wavfile import write
    
    print("🎼 TẠO ÂM THANH TỪ CÔNG THỨC")
    
    # Tham số âm thanh
    fs = 44100        # Hz - Tần số lấy mẫu
    duration = 2.0    # giây
    frequency = 440   # Hz - Tần số âm (A4)
    amplitude = 0.3   # Biên độ
    
    # Tạo trục thời gian
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    
    # CÔNG THỨC TẠO ÂM (thay đổi theo đề)
    # Sóng sin chuẩn
    tone = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Các công thức khác thường gặp:
    # tone = amplitude * np.cos(2 * np.pi * frequency * t)  # Cosine
    # tone = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))  # Square wave
    # tone = amplitude * (2 * (t * frequency - np.floor(t * frequency + 0.5)))  # Sawtooth
    
    # Chuyển sang int16 để lưu WAV
    tone_int16 = (tone * 32767).astype(np.int16)
    
    # Lưu file
    output_file = "generated_tone.wav"
    write(output_file, fs, tone_int16)
    
    print(f"✅ Đã tạo: {output_file}")
    print(f"🎵 Tần số: {frequency} Hz")
    print(f"⏱️  Thời lượng: {duration} giây")
    
    return tone, output_file

# =============================================================================
# 3A) VẼ WAVEFORM - DÙNG KHI ĐỀ YÊU CẦU VẼ DẠNG SÓNG
# =============================================================================

def plot_waveform_detailed(filename):
    """🎯 Copy khi đề yêu cầu: vẽ waveform đẹp có chú thích"""
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.io import wavfile
    
    # Đọc file
    rate, data = wavfile.read(filename)
    
    # Xử lý stereo
    if data.ndim == 2:
        data = data[:, 0]
        print("🔄 Chuyển từ stereo sang mono")
    
    # Giới hạn số mẫu hiển thị (để đồ thị rõ ràng)
    N_show = min(len(data), 3000)
    
    # Tạo trục thời gian (giây)
    time_axis = np.arange(N_show) / rate
    
    # VẼ ĐỒ THỊ
    plt.figure(figsize=(12, 6))
    plt.plot(time_axis, data[:N_show], 'b-', linewidth=0.8)
    plt.title(f"📈 Waveform - {N_show} mẫu đầu ({N_show/rate:.2f}s)")
    plt.xlabel("⏰ Thời gian (giây)")
    plt.ylabel("📊 Biên độ")
    plt.grid(True, alpha=0.3)
    
    # Thống kê
    plt.figtext(0.02, 0.02, f"📋 File: {filename} | 📊 Rate: {rate}Hz | 📏 Samples: {len(data):,}", 
                fontsize=9, ha='left')
    
    plt.tight_layout()
    plt.show()
    
    # In thống kê
    print(f"📊 THỐNG KÊ WAVEFORM:")
    print(f"Max: {np.max(data)}")
    print(f"Min: {np.min(data)}")
    print(f"Mean: {np.mean(data):.2f}")
    print(f"RMS: {np.sqrt(np.mean(data**2)):.2f}")
    
    return rate, data

# =============================================================================
# 3B) PHÂN TÍCH FFT - DÙNG KHI ĐỀ YÊU CẦU PHỔ TẦN SỐ
# =============================================================================

def analyze_spectrum_complete(filename):
    """🎯 Copy khi đề yêu cầu: phân tích phổ tần số chi tiết"""
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.io import wavfile
    
    # Đọc và xử lý
    rate, data = wavfile.read(filename)
    if data.ndim == 2:
        data = data[:, 0]
    
    # TÍNH FFT
    N = len(data)
    yf = np.fft.fft(data)
    xf = np.fft.fftfreq(N, 1.0 / rate)
    
    # Chỉ lấy nửa dương (do tính đối xứng)
    half = N // 2
    magnitude = np.abs(yf[:half])
    freqs = xf[:half]
    
    # VẼ 2 SUBPLOT: Waveform + Spectrum
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Subplot 1: Waveform
    N_show = min(N, 2000)
    time_show = np.arange(N_show) / rate
    ax1.plot(time_show, data[:N_show])
    ax1.set_title("🌊 Waveform")
    ax1.set_xlabel("Thời gian (s)")
    ax1.set_ylabel("Biên độ")
    ax1.grid(True)
    
    # Subplot 2: Spectrum  
    ax2.plot(freqs, magnitude)
    ax2.set_title("🔍 Phổ biên độ (Magnitude Spectrum)")
    ax2.set_xlabel("Tần số (Hz)")
    ax2.set_ylabel("Biên độ")
    ax2.grid(True)
    
    # Tìm peak frequency
    peak_idx = np.argmax(magnitude)
    peak_freq = freqs[peak_idx]
    ax2.axvline(peak_freq, color='red', linestyle='--', alpha=0.7)
    ax2.text(peak_freq, magnitude[peak_idx], f'Peak: {peak_freq:.1f}Hz', 
             rotation=90, ha='right', va='bottom')
    
    plt.tight_layout()
    plt.show()
    
    print(f"🎯 Tần số chính: {peak_freq:.2f} Hz")
    print(f"🔊 Biên độ cực đại: {np.max(magnitude):.0f}")
    
    return freqs, magnitude, peak_freq

# =============================================================================
# 4A) GHI ÂM - DÙNG KHI ĐỀ YÊU CẦU GHI TỪ MICRO
# =============================================================================

def record_from_microphone():
    """🎯 Copy khi đề yêu cầu: ghi âm từ micro"""
    import sounddevice as sd
    import numpy as np
    from scipy.io.wavfile import write
    
    # Cấu hình ghi âm
    fs = 44100        # Tần số lấy mẫu
    duration = 3      # Thời lượng (giây)
    channels = 1      # Mono
    
    print("🎤 CHUẨN BỊ GHI ÂM...")
    print(f"⚙️  Cấu hình: {fs}Hz, {duration}s, {channels} kênh")
    print("🔴 Bắt đầu ghi âm trong 2 giây...")
    
    import time
    time.sleep(2)  # Đếm ngược
    
    # GHI ÂM
    print("⏺️  ĐANG GHI...")
    audio_data = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=channels,
        dtype='int16'
    )
    
    sd.wait()  # Chờ hoàn tất
    print("✅ Hoàn tất ghi âm!")
    
    # Lưu file
    output_file = "recorded_audio.wav"
    write(output_file, fs, audio_data)
    print(f"💾 Đã lưu: {output_file}")
    
    # Thống kê
    print(f"📊 Thống kê:")
    print(f"   - Kích thước: {audio_data.shape}")
    print(f"   - Max: {np.max(audio_data)}")
    print(f"   - RMS: {np.sqrt(np.mean(audio_data**2)):.0f}")
    
    return audio_data, output_file

# =============================================================================
# 4B) PHÁT LẠI - DÙNG KHI ĐỀ YÊU CẦU PLAY AUDIO
# =============================================================================

def playback_audio(filename):
    """🎯 Copy khi đề yêu cầu: phát lại file âm thanh"""
    import sounddevice as sd
    from scipy.io.wavfile import read
    
    try:
        print(f"🔊 PHÁT LẠI: {filename}")
        rate, data = read(filename)
        
        print(f"📊 Thông tin: {rate}Hz, shape={data.shape}")
        print("▶️  Đang phát...")
        
        sd.play(data, rate)
        sd.wait()  # Chờ phát xong
        
        print("✅ Phát lại hoàn tất!")
        
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file: {filename}")
    except Exception as e:
        print(f"❌ Lỗi phát lại: {e}")

# =============================================================================
# 5A) LỌC THÔNG THẤP - DÙNG KHI ĐỀ VỀ LOW-PASS FILTER
# =============================================================================

def lowpass_filter_demo(filename):
    """🎯 Copy khi đề yêu cầu: bộ lọc thông thấp"""
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.io import wavfile
    from numpy.fft import rfft, rfftfreq, irfft
    
    # Đọc file
    rate, data = wavfile.read(filename)
    if data.ndim == 2:
        data = data[:, 0]
    data = data.astype(np.float32)
    
    # HÀM LỌC THÔNG THẤP
    def lowpass_filter(signal, fs, cutoff_hz):
        """Lọc thông thấp: giữ tần số <= cutoff, loại bỏ tần số > cutoff"""
        N = len(signal)
        X = rfft(signal)                    # FFT
        freqs = rfftfreq(N, 1.0/fs)        # Trục tần số
        
        # Tạo mask: True cho tần số <= cutoff
        mask = freqs <= cutoff_hz
        X_filtered = X * mask               # Áp dụng mask
        
        return irfft(X_filtered, n=N)       # IFFT về miền thời gian
    
    # Áp dụng lọc
    cutoff = 2000  # Hz - Thay đổi theo đề
    filtered_signal = lowpass_filter(data, rate, cutoff)
    
    # VẼ SO SÁNH
    N_show = min(len(data), 2000)
    
    plt.figure(figsize=(12, 8))
    
    # Waveform comparison
    plt.subplot(2, 1, 1)
    plt.plot(data[:N_show], label="🔵 Gốc", alpha=0.8)
    plt.plot(filtered_signal[:N_show], label=f"🔴 Low-pass (<{cutoff}Hz)", alpha=0.8)
    plt.title("Waveform Comparison")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    
    # Spectrum comparison
    plt.subplot(2, 1, 2)
    N = len(data)
    freqs = rfftfreq(N, 1.0/rate)
    
    original_fft = np.abs(rfft(data))
    filtered_fft = np.abs(rfft(filtered_signal))
    
    plt.plot(freqs, original_fft, label="🔵 Gốc", alpha=0.7)
    plt.plot(freqs, filtered_fft, label=f"🔴 Filtered", alpha=0.7)
    plt.axvline(cutoff, color='red', linestyle='--', label=f'Cutoff: {cutoff}Hz')
    plt.title("Spectrum Comparison")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude") 
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    # Lưu kết quả
    filtered_int16 = (filtered_signal / np.max(np.abs(filtered_signal)) * 32767).astype(np.int16)
    output_file = "lowpass_filtered.wav"
    wavfile.write(output_file, rate, filtered_int16)
    print(f"💾 Đã lưu: {output_file}")
    
    return filtered_signal

# =============================================================================
# 5B) LỌC THÔNG CAO - DÙNG KHI ĐỀ VỀ HIGH-PASS FILTER
# =============================================================================

def highpass_filter_demo(filename):
    """🎯 Copy khi đề yêu cầu: bộ lọc thông cao"""
    import numpy as np
    from scipy.io import wavfile
    from numpy.fft import rfft, rfftfreq, irfft
    
    # Đọc file
    rate, data = wavfile.read(filename)
    if data.ndim == 2:
        data = data[:, 0]
    data = data.astype(np.float32)
    
    # HÀM LỌC THÔNG CAO
    def highpass_filter(signal, fs, cutoff_hz):
        """Lọc thông cao: giữ tần số >= cutoff, loại bỏ tần số < cutoff"""
        N = len(signal)
        X = rfft(signal)
        freqs = rfftfreq(N, 1.0/fs)
        
        # Mask: True cho tần số >= cutoff
        mask = freqs >= cutoff_hz  
        X_filtered = X * mask
        
        return irfft(X_filtered, n=N)
    
    cutoff = 200  # Hz
    filtered_signal = highpass_filter(data, rate, cutoff)
    
    print(f"🔍 High-pass filter applied: cutoff = {cutoff}Hz")
    print(f"📊 Original RMS: {np.sqrt(np.mean(data**2)):.2f}")
    print(f"📊 Filtered RMS: {np.sqrt(np.mean(filtered_signal**2)):.2f}")
    
    return filtered_signal

# =============================================================================
# 6A) TRÍCH XUẤT MFCC - DÙNG KHI ĐỀ VỀ FEATURE EXTRACTION
# =============================================================================

def extract_mfcc_features(filename):
    """🎯 Copy khi đề yêu cầu: trích xuất MFCC cho ML"""
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.io import wavfile
    from python_speech_features import mfcc, logfbank
    
    # Đọc file
    rate, data = wavfile.read(filename)
    if data.ndim == 2:
        data = data[:, 0]
    
    # Chuyển về float32 nếu cần
    if data.dtype.kind in ('i', 'u'):
        data = data.astype(np.float32) / 32768.0
    
    print(f"🎵 Trích xuất MFCC từ: {filename}")
    
    # TRÍCH XUẤT MFCC
    mfcc_features = mfcc(
        signal=data,
        samplerate=rate,
        numcep=13,        # 13 hệ số MFCC
        nfft=2048,        # Kích thước FFT
        winstep=0.01      # Bước cửa sổ 10ms
    )
    
    # Log Mel Filterbank  
    fbank_features = logfbank(
        signal=data,
        samplerate=rate,
        nfft=2048
    )
    
    # Thông tin
    print(f"📊 MFCC shape: {mfcc_features.shape}")
    print(f"📊 Filterbank shape: {fbank_features.shape}")
    print(f"🕰️  Số frame: {mfcc_features.shape[0]}")
    print(f"🔢 Số đặc trưng MFCC: {mfcc_features.shape[1]}")
    
    # VẼ VISUALIZATION
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # MFCC heatmap
    im1 = ax1.imshow(mfcc_features.T, aspect='auto', origin='lower', cmap='viridis')
    ax1.set_title("🔍 MFCC Features")
    ax1.set_xlabel("Frame")
    ax1.set_ylabel("MFCC Coefficient")
    plt.colorbar(im1, ax=ax1)
    
    # Filterbank heatmap
    im2 = ax2.imshow(fbank_features.T, aspect='auto', origin='lower', cmap='viridis')
    ax2.set_title("🔍 Log Mel Filterbank Features")
    ax2.set_xlabel("Frame") 
    ax2.set_ylabel("Filter Bank")
    plt.colorbar(im2, ax=ax2)
    
    plt.tight_layout()
    plt.show()
    
    # Thống kê MFCC
    print(f"📈 MFCC Statistics:")
    for i in range(min(5, mfcc_features.shape[1])):
        coef = mfcc_features[:, i]
        print(f"   MFCC[{i}]: mean={np.mean(coef):.3f}, std={np.std(coef):.3f}")
    
    return mfcc_features, fbank_features

# =============================================================================
# 7A) SO SÁNH CHẤT LƯỢNG - DÙNG KHI ĐỀ VỀ MSE/PSNR
# =============================================================================

def calculate_audio_quality_metrics(original_file, processed_file):
    """🎯 Copy khi đề yêu cầu: tính MSE, PSNR để so sánh chất lượng"""
    import numpy as np
    from scipy.io import wavfile
    
    # Đọc 2 file
    rate1, data1 = wavfile.read(original_file)
    rate2, data2 = wavfile.read(processed_file)
    
    # Kiểm tra tương thích
    if rate1 != rate2:
        print(f"⚠️  Warning: Different sample rates ({rate1} vs {rate2})")
    
    # Đảm bảo cùng kích thước
    min_len = min(len(data1), len(data2))
    data1 = data1[:min_len].astype(np.float64)
    data2 = data2[:min_len].astype(np.float64)
    
    # TÍNH MSE (Mean Squared Error)
    mse = np.mean((data1 - data2) ** 2)
    
    # TÍNH PSNR (Peak Signal-to-Noise Ratio)
    if mse == 0:
        psnr = float('inf')
    else:
        max_pixel = np.max([np.max(np.abs(data1)), np.max(np.abs(data2))])
        psnr = 20 * np.log10(max_pixel) - 10 * np.log10(mse)
    
    # Tính SNR
    signal_power = np.mean(data1 ** 2)
    noise_power = np.mean((data1 - data2) ** 2)
    if noise_power == 0:
        snr = float('inf')
    else:
        snr = 10 * np.log10(signal_power / noise_power)
    
    # KẾT QUẢ
    print("📊 CHẤT LƯỢNG AUDIO COMPARISON")
    print("=" * 40)
    print(f"📁 Original: {original_file}")
    print(f"📁 Processed: {processed_file}")
    print(f"📏 Sample length: {min_len:,}")
    print(f"🔢 MSE: {mse:.6f}")
    print(f"📶 PSNR: {psnr:.2f} dB")
    print(f"📻 SNR: {snr:.2f} dB")
    
    # Đánh giá chất lượng
    if psnr >= 40:
        quality = "Excellent (≥40dB)"
    elif psnr >= 30:
        quality = "Good (30-40dB)"  
    elif psnr >= 20:
        quality = "Fair (20-30dB)"
    else:
        quality = "Poor (<20dB)"
    
    print(f"⭐ Quality rating: {quality}")
    
    return {
        'mse': mse,
        'psnr': psnr,
        'snr': snr,
        'quality': quality
    }

# =============================================================================
# 8A) BÀI TẬP TỔNG HỢP - DÙNG CHO ĐỀ THI HOÀN CHỈNH
# =============================================================================

def complete_audio_analysis_exam():
    """🎯 Template hoàn chỉnh cho bài thi tổng hợp LAB1+LAB2
    📝 Copy toàn bộ và thay đổi theo yêu cầu đề bài
    """
    
    print("🎯 BÀI THI TỔNG HỢP - AUDIO PROCESSING")
    print("=" * 50)
    
    # PHẦN 1: ENCODING (nếu đề có)
    print("\n📝 PHẦN 1: TEXT ENCODING")
    text_samples = [
        "ĐẠI HỌC CÔNG NGHIỆP TP HỒ CHÍ MINH",
        "Khoa Công nghệ thông tin",
        "Xử lý đa phương tiện"
    ]
    
    for i, text in enumerate(text_samples, 1):
        encoded = text.encode('utf-8')
        print(f"{i}. '{text}'")
        print(f"   → UTF-8: {encoded}")
        print(f"   → Length: {len(encoded)} bytes")
    
    # PHẦN 2: AUDIO ANALYSIS
    print(f"\n🎵 PHẦN 2: AUDIO ANALYSIS")
    
    # Thay đổi filename theo đề bài
    filename = "sample-6s.wav"  # <<<< THAY ĐỔI ĐÂY
    
    try:
        # 2.1 Đọc metadata
        print(f"\n2.1 Metadata Analysis:")
        metadata = read_wav_metadata(filename)
        
        # 2.2 Waveform & Spectrum  
        print(f"\n2.2 Signal Analysis:")
        freqs, magnitude, peak_freq = analyze_spectrum_complete(filename)
        
        # 2.3 Filtering (nếu đề yêu cầu)
        print(f"\n2.3 Signal Filtering:")
        filtered_lp = lowpass_filter_demo(filename)
        filtered_hp = highpass_filter_demo(filename)
        
        # 2.4 Feature Extraction (nếu đề yêu cầu)
        print(f"\n2.4 Feature Extraction:")
        mfcc_feat, fbank_feat = extract_mfcc_features(filename)
        
        # PHẦN 3: KẾT QUẢ TỔNG HỢP
        print(f"\n📋 PHẦN 3: SUMMARY REPORT")
        print(f"✅ File processed: {filename}")
        print(f"📊 Duration: {metadata['duration']:.2f}s")
        print(f"🎯 Peak frequency: {peak_freq:.1f} Hz")
        print(f"🔢 MFCC features: {mfcc_feat.shape}")
        print(f"💾 Output files created:")
        print(f"   - lowpass_filtered.wav")
        print(f"   - highpass_filtered.wav")
        
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found!")
        print("💡 Hướng dẫn: Thay đổi 'filename' trong code theo đề bài")
    
    except Exception as e:
        print(f"❌ Error: {e}")

# =============================================================================
# 9A) QUICK REFERENCE - COPY NHANH THEO YÊU CẦU
# =============================================================================

def quick_templates():
    """🚀 Templates nhanh cho từng dạng câu hỏi"""
    
    # Template 1: Đọc file và hiển thị thông tin
    template_read = '''
# 🎯 ĐỌC FILE VÀ HIỂN THỊ THÔNG TIN
from scipy.io import wavfile
filename = "your_file.wav"  # THAY ĐỔI
rate, data = wavfile.read(filename)
print(f"Sample rate: {rate} Hz")
print(f"Shape: {data.shape}")
print(f"Duration: {len(data)/rate:.2f}s")
    '''
    
    # Template 2: Vẽ waveform và FFT
    template_plot = '''
# 🎯 VẼ WAVEFORM VÀ FFT
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate, data = wavfile.read("file.wav")  # THAY ĐỔI
if data.ndim == 2: data = data[:,0]

# Waveform
plt.subplot(2,1,1)
plt.plot(data[:2000])
plt.title("Waveform")

# FFT
N = len(data)
yf = np.fft.fft(data)
xf = np.fft.fftfreq(N, 1.0/rate)
plt.subplot(2,1,2)
plt.plot(xf[:N//2], np.abs(yf[:N//2]))
plt.title("Spectrum")
plt.show()
    '''
    
    # Template 3: MFCC
    template_mfcc = '''
# 🎯 TRÍCH XUẤT MFCC
from python_speech_features import mfcc
from scipy.io import wavfile
import matplotlib.pyplot as plt

rate, data = wavfile.read("file.wav")  # THAY ĐỔI
if data.ndim == 2: data = data[:,0]
if data.dtype.kind in ('i','u'): 
    data = data.astype(float) / 32768.0

mfcc_feat = mfcc(data, rate, numcep=13)
plt.imshow(mfcc_feat.T, aspect='auto', origin='lower')
plt.colorbar()
plt.show()
    '''
    
    print("🚀 QUICK TEMPLATES:")
    print("1️⃣  Đọc file:", template_read)
    print("2️⃣  Plot:", template_plot) 
    print("3️⃣  MFCC:", template_mfcc)

# =============================================================================
# MAIN - DEMO VÀ TESTING
# =============================================================================

if __name__ == "__main__":
    """
    🎯 SỬ DỤNG TRONG THI:
    
    1️⃣ Tìm nhanh: Ctrl+F với từ khóa từ đầu file
    2️⃣ Copy function phù hợp với đề bài  
    3️⃣ Thay đổi filename theo đề
    4️⃣ Run và check kết quả
    
    📚 VÍ DỤ:
    - Đề: "Đọc file WAV hiển thị thông tin" → search "2A) ĐỌC WAV"
    - Đề: "Vẽ waveform và phổ tần số" → search "3A) VẼ WAVEFORM"  
    - Đề: "Mã hóa UTF-8" → search "1A) MÃ HÓA"
    - Đề: "Lọc thông thấp" → search "5A) LỌC THÔNG THẤP"
    """
    
    print("🎯 CHEAT SHEET THI GIỮA KỲ - READY!")
    print("🔍 Dùng Ctrl+F để tìm nhanh theo đề bài")
    print("📋 Xem hướng dẫn tìm kiếm ở đầu file")
    
    # Test với file mẫu  
    test_file = "D:/mon/da-phuong-tien/lab2/sample-6s.wav"  
    
    print(f"\n🧪 Testing với file: {test_file}")
    if os.path.exists(test_file):
        print("✅ File tồn tại - có thể test functions")
        # Uncomment để test:
        # read_wav_metadata(test_file)
        # plot_waveform_detailed(test_file)
    else:
        print("⚠️  File test không tồn tại, thay đổi đường dẫn để test")
    
    print(f"\n📖 Quick reference:")
    quick_templates()

"""
🔥 MEMORY AID - GHI NHỚ NHANH:

🎯 LAB1 - ENCODING:
text.encode('utf-8') → bytes
bytes.decode('utf-8') → string
f"{hex_val:08b}" → binary
list(bytes) → decimal list

🎯 LAB2 - AUDIO:  
wavfile.read(file) → rate, data
plt.plot(data) → waveform
np.fft.fft(data) → spectrum
sd.rec() → ghi âm
mfcc(data, rate) → MFCC
rfft + mask + irfft → filtering

⚡ MUST REMEMBER:
- Stereo → mono: data = data[:,0]
- Int → float: data.astype(float)/32768.0  
- Save WAV: data.astype(int16)
- FFT: chỉ lấy nửa dương [:N//2]
"""
