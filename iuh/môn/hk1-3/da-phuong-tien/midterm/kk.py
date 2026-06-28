BÀI ÔN TẬP GIỮA KỲ – CÔNG NGHỆ ĐA PHƯƠNG TIỆN
Learning Outcome 1: Giải thích được các công nghệ cơ bản liên quan đến thiết kế hệ đa phương tiện (hình ảnh, âm thanh, text).
Mục tiêu: Hiểu – Giải thích – Thực hành với các thành phần đa phương tiện cơ bản.
I. PHẦN LÝ THUYẾT
1. Khái niệm hệ đa phương tiện
Đa phương tiện (Multimedia) là sự kết hợp của văn bản (text), hình ảnh (image), âm thanh (audio), video, và đồ họa động (animation) trong một hệ thống số hóa. Ứng dụng: quảng cáo, e-learning, game, website tương tác, hệ thống y tế,…
2. Công nghệ xử lý văn bản (Text)
Mã hóa ký tự: ASCII (7-bit, chỉ tiếng Anh), Unicode (đa ngôn ngữ), UTF-8 (phổ biến nhất, biến độ dài 1–4 byte). Chuẩn hóa Unicode: NFC (composed) và NFD (decomposed).
Ví dụ Python:
import unicodedata
text = 'Trường Đại học'
for ch in text:
    print(ch, '→', unicodedata.name(ch, '?'))
3. Công nghệ xử lý hình ảnh (Image)
Ảnh số là ma trận pixel. Mô hình màu: RGB (Red–Green–Blue), HSV (Hue–Saturation–Value), Grayscale. Định dạng ảnh: JPG (lossy), PNG (lossless), BMP, TIFF.
Ví dụ Python:
from PIL import Image
import numpy as np
img = Image.open('flower.jpg')
gray = img.convert('L')
print('Mức xám trung bình:', np.array(gray).mean())
gray.save('gray_flower.png')
4. Công nghệ xử lý âm thanh (Audio)
Âm thanh số là chuỗi mẫu biên độ lấy mẫu theo thời gian. Thông số: Sample rate (Hz), Bit depth, Channels. Ví dụ Python:
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np

fs, data = read('sample.wav')
print('Sample rate:', fs)
print('Duration:', len(data)/fs, 's')
plt.plot(data[:2000]); plt.title('Waveform'); plt.show()
5. Tổng kết lý thuyết
Text – xử lý ký tự Unicode.
Image – xử lý pixel và mô hình màu.
Audio – xử lý tín hiệu số, biểu đồ sóng âm.
II. PHẦN THỰC HÀNH ÔN TẬP
Bài 1 – Text (Unicode)
Nhập chuỗi tiếng Việt → in mã Unicode → chuẩn hóa NFC/NFD → so sánh độ dài chuỗi trước & sau chuẩn hóa.
Bài 2 – Image (RGB → Grayscale)
Đọc ảnh input.jpg → in kích thước, số kênh, mức xám trung bình → chuyển grayscale → lưu output_gray.png → giải thích RGB vs HSV.
Bài 3 – Audio (Đọc và chuẩn hóa WAV)
Đọc sample.wav → in tần số lấy mẫu, thời lượng → vẽ waveform → chuẩn hóa biên độ về [-1,1] → lưu normalized.wav.
Bài 4 – Tích hợp
Viết chương trình đa phương tiện tổng hợp:
1. Nhập văn bản
2. Ghi text lên ảnh bằng PIL.ImageDraw
3. Phát âm thanh bằng playsound khi hiển thị ảnh.
III. CÂU HỎI ÔN TẬP
●	1. Sự khác nhau giữa RGB và HSV trong biểu diễn màu?
●	2. Phân biệt lossless và lossy compression?
●	3. Tần số lấy mẫu và bit depth ảnh hưởng thế nào đến chất lượng âm thanh?
●	4. Mục đích của việc chuẩn hóa Unicode là gì?
●	5. Khi nào nên chuyển ảnh sang grayscale trước khi xử lý?
●	6. Nếu muốn tách vùng màu đỏ trong ảnh, nên dùng mô hình màu nào?
●	7. Vì sao cần chuẩn hóa biên độ âm thanh về [-1,1]?



__________
Trả lời 

Chào bạn, đây là câu trả lời chi tiết cho từng phần trong đề cương ôn tập giữa kỳ môn Công nghệ Đa phương tiện của bạn. Các câu trả lời được giải thích rõ ràng và kèm theo mã nguồn đầy đủ cho phần thực hành.
BÀI ÔN TẬP GIỮA KỲ – CÔNG NGHỆ ĐA PHƯƠNG TIỆN
Nội dung ôn tập được chia thành ba phần rõ ràng: Lý thuyết, Thực hành và Câu hỏi ôn tập. Dưới đây là lời giải chi tiết cho các phần bạn cần hoàn thành.
I. PHẦN LÝ THUYẾT
Phần này bạn đã tóm tắt rất tốt các khái niệm cốt lõi:
 * Đa phương tiện (Multimedia): Là sự tích hợp của nhiều loại phương tiện (text, image, audio, video, animation) trên một nền tảng số.
 * Văn bản (Text): Tập trung vào công nghệ mã hóa ký tự, đặc biệt là Unicode và chuẩn hóa (NFC, NFD) để xử lý đa ngôn ngữ.
 * Hình ảnh (Image): Bản chất là ma trận pixel, được biểu diễn qua các mô hình màu (RGB, HSV) và lưu trữ dưới các định dạng (JPG, PNG).
 * Âm thanh (Audio): Là tín hiệu tương tự được số hóa thông qua quá trình lấy mẫu, đặc trưng bởi các thông số như tần số lấy mẫu (Sample Rate) và độ sâu bit (Bit depth).
Các ví dụ Python bạn đưa ra là minh họa chính xác cho từng phần. Chúng ta sẽ sử dụng nền tảng lý thuyết này để giải quyết các bài tập bên dưới.
II. PHẦN THỰC HÀNH ÔN TẬP
Dưới đây là lời giải chi tiết kèm mã nguồn và giải thích cho từng bài.
(Lưu ý: Để chạy các đoạn mã sau, bạn cần cài đặt các thư viện cần thiết: pip install numpy Pillow scipy matplotlib playsound)
Bài 1 – Text (Unicode)
Yêu cầu: Nhập chuỗi tiếng Việt → in mã Unicode → chuẩn hóa NFC/NFD → so sánh độ dài chuỗi trước & sau chuẩn hóa.
Mã nguồn (Python):
import unicodedata

# 1. Nhập chuỗi tiếng Việt từ người dùng
input_text = input("Nhập một chuỗi tiếng Việt: ")
print(f"\nChuỗi gốc: '{input_text}'")
print(f"Độ dài chuỗi gốc: {len(input_text)}")

# 2. In mã Unicode của từng ký tự
print("\nMã Unicode (Code Point) của từng ký tự:")
for char in input_text:
    # ord() trả về mã code point của ký tự
    print(f"'{char}' → U+{ord(char):04X}")

# 3. Chuẩn hóa sang NFC (composed) và NFD (decomposed)
text_nfc = unicodedata.normalize('NFC', input_text)
text_nfd = unicodedata.normalize('NFD', input_text)

print("\n--- Chuẩn hóa Unicode ---")
print(f"Chuẩn hóa NFC: '{text_nfc}'")
print(f"Độ dài sau khi chuẩn hóa NFC: {len(text_nfc)}")

print(f"Chuẩn hóa NFD: '{text_nfd}'")
print(f"Độ dài sau khi chuẩn hóa NFD: {len(text_nfd)}")

# 4. So sánh và giải thích
print("\n--- So sánh độ dài ---")
if len(input_text) == len(text_nfc):
    print("Độ dài chuỗi gốc và chuỗi NFC thường bằng nhau vì hầu hết hệ thống đã dùng NFC.")
else:
    print("Độ dài chuỗi gốc và chuỗi NFC khác nhau.")

if len(text_nfd) > len(text_nfc):
    print("Độ dài chuỗi NFD lớn hơn NFC vì NFD tách ký tự thành ký tự cơ sở và dấu thanh.")
    print("Ví dụ: 'ệ' (1 ký tự NFC) → 'e' + '̣' + '̂' (3 ký tự NFD)")

Giải thích:
 * ord(char): Hàm này lấy mã số (code point) của một ký tự trong bảng mã Unicode.
 * unicodedata.normalize('NFC', text): Chuẩn hóa Composition Form. Nó sẽ tổ hợp một ký tự cơ sở và các dấu của nó thành một ký tự duy nhất đã được định nghĩa sẵn (ví dụ: e + ^ → ê).
 * unicodedata.normalize('NFD', text): Chuẩn hóa Decomposition Form. Nó sẽ phân rã một ký tự thành ký tự cơ sở và các dấu riêng biệt (ví dụ: ệ → e + ̣ + ̂). Vì vậy, độ dài chuỗi sau khi chuẩn hóa NFD thường lớn hơn.
Bài 2 – Image (RGB → Grayscale)
Yêu cầu: Đọc ảnh input.jpg → in kích thước, số kênh, mức xám trung bình → chuyển grayscale → lưu output_gray.png → giải thích RGB vs HSV.
Mã nguồn (Python):
from PIL import Image
import numpy as np

try:
    # 1. Đọc ảnh và in thông tin
    img = Image.open('input.jpg')
    print(f"Đã mở ảnh 'input.jpg'")
    print(f"Kích thước (rộng x cao): {img.size}")
    print(f"Số kênh màu (Mode): {img.mode}") # 'RGB' là 3 kênh, 'L' là 1 kênh

    # 2. Chuyển sang ảnh xám (grayscale)
    gray_img = img.convert('L')
    print("\nĐã chuyển ảnh sang Grayscale.")

    # 3. Tính mức xám trung bình
    # Chuyển ảnh PIL thành mảng numpy để tính toán
    gray_array = np.array(gray_img)
    average_gray = gray_array.mean()
    print(f"Mức xám trung bình của ảnh: {average_gray:.2f}")

    # 4. Lưu ảnh kết quả
    gray_img.save('output_gray.png')
    print("Đã lưu ảnh xám thành 'output_gray.png'")
    
    # Hiển thị ảnh (tùy chọn)
    # gray_img.show()

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'input.jpg'. Hãy chắc chắn bạn có file này trong cùng thư mục.")


Giải thích RGB vs HSV:
 * RGB (Red, Green, Blue):
   * Cơ chế: Là mô hình màu cộng, mô phỏng cách màn hình (TV, máy tính) phát ra ánh sáng. Mỗi màu được tạo ra bằng cách kết hợp ba màu gốc Đỏ, Xanh lá, Xanh dương với cường độ khác nhau (thường từ 0-255).
   * Ưu điểm: Phù hợp với phần cứng hiển thị.
   * Nhược điểm: Không trực quan với con người. Rất khó để xác định một màu cụ thể (ví dụ: "màu đỏ") vì nó phụ thuộc vào cả 3 giá trị R, G, B.
 * HSV (Hue, Saturation, Value):
   * Cơ chế: Mô phỏng cách con người cảm nhận màu sắc.
     * Hue (Tông màu): Loại màu sắc (đỏ, vàng, lục, lam,...), biểu diễn bằng một góc từ 0-360 độ.
     * Saturation (Độ bão hòa): Độ "tinh khiết" của màu. 100% là màu rực rỡ nhất, 0% là màu xám.
     * Value (Giá trị): Độ sáng tối của màu. 100% là sáng nhất, 0% là màu đen.
   * Ưu điểm: Rất trực quan. Nếu muốn tìm tất cả các đối tượng "màu đỏ" trong ảnh, ta chỉ cần lọc theo một khoảng giá trị của Hue, bất kể độ sáng hay độ bão hòa.
Bài 3 – Audio (Đọc và chuẩn hóa WAV)
Yêu cầu: Đọc sample.wav → in tần số lấy mẫu, thời lượng → vẽ waveform → chuẩn hóa biên độ về [-1,1] → lưu normalized.wav.
Mã nguồn (Python):
from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt

try:
    # 1. Đọc file WAV
    fs, data = read('sample.wav')

    # 2. In thông số
    duration = len(data) / fs
    print(f"Tần số lấy mẫu (Sample Rate): {fs} Hz")
    print(f"Thời lượng (Duration): {duration:.2f} giây")
    print(f"Kiểu dữ liệu của mẫu: {data.dtype}")

    # 3. Vẽ biểu đồ sóng (waveform) - vẽ 2 giây đầu tiên cho dễ nhìn
    time_axis = np.linspace(0., duration, len(data))
    plt.figure(figsize=(12, 4))
    plt.plot(time_axis, data)
    plt.title('Biểu đồ sóng âm (Waveform) - Gốc')
    plt.xlabel('Thời gian (s)')
    plt.ylabel('Biên độ')
    plt.grid(True)
    plt.show()

    # 4. Chuẩn hóa biên độ về [-1, 1]
    # Chuyển dữ liệu sang kiểu float để thực hiện phép chia
    audio_float = data.astype(np.float32)
    # Tìm giá trị biên độ lớn nhất
    max_amp = np.max(np.abs(audio_float))
    if max_amp > 0:
        normalized_data = audio_float / max_amp
    else:
        normalized_data = audio_float # Tránh chia cho 0 nếu file âm thanh im lặng

    print(f"\nĐã chuẩn hóa biên độ về khoảng [-1, 1].")
    print(f"Biên độ lớn nhất trước khi chuẩn hóa: {max_amp}")
    print(f"Biên độ lớn nhất sau khi chuẩn hóa: {np.max(np.abs(normalized_data))}")

    # 5. Lưu file đã chuẩn hóa
    # scipy.io.wavfile.write yêu cầu kiểu dữ liệu phù hợp
    # Ở đây ta lưu dưới dạng float32
    write('normalized.wav', fs, normalized_data)
    print("Đã lưu file âm thanh đã chuẩn hóa thành 'normalized.wav'")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'sample.wav'.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

Bài 4 – Tích hợp
Yêu cầu: Viết chương trình nhập văn bản, ghi text lên ảnh, và phát âm thanh khi hiển thị ảnh.
Mã nguồn (Python):
from PIL import Image, ImageDraw, ImageFont
from playsound import playsound
import threading

def play_audio_async(sound_file):
    """Hàm để phát âm thanh trong một luồng riêng biệt."""
    try:
        playsound(sound_file)
    except Exception as e:
        print(f"Không thể phát âm thanh '{sound_file}': {e}")

# --- Cấu hình ---
IMAGE_PATH = 'input.jpg'
SOUND_PATH = 'sample.wav'
# Bạn có thể cần thay đổi đường dẫn đến file font của bạn
# Trên Windows: "arial.ttf". Trên Linux/macOS có thể khác.
FONT_PATH = "arial.ttf" 
FONT_SIZE = 50

try:
    # 1. Nhập văn bản từ người dùng
    text_to_write = input("Nhập văn bản bạn muốn ghi lên ảnh: ")

    # 2. Mở ảnh và chuẩn bị để vẽ
    with Image.open(IMAGE_PATH) as img:
        draw = ImageDraw.Draw(img)
        
        # Tải font chữ
        try:
            font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        except IOError:
            print(f"Không tìm thấy font tại '{FONT_PATH}'. Sử dụng font mặc định.")
            font = ImageFont.load_default()

        # Xác định vị trí ghi text (ví dụ: góc trên bên trái)
        position = (20, 20)
        text_color = (255, 0, 0) # Màu đỏ (R, G, B)

        # Ghi text lên ảnh
        draw.text(position, text_to_write, font=font, fill=text_color)
        print("Đã ghi văn bản lên ảnh.")

        # 3. Phát âm thanh và hiển thị ảnh đồng thời
        print("Đang hiển thị ảnh và phát âm thanh...")
        
        # Tạo và bắt đầu một luồng mới để phát âm thanh
        # Điều này cho phép ảnh hiển thị ngay lập tức mà không cần chờ âm thanh phát xong
        audio_thread = threading.Thread(target=play_audio_async, args=(SOUND_PATH,))
        audio_thread.start()
        
        # Hiển thị ảnh
        img.show()

        # Chờ luồng âm thanh kết thúc (nếu bạn muốn chương trình chính đợi)
        audio_thread.join()
        print("Hoàn thành.")

except FileNotFoundError:
    print(f"Lỗi: Hãy chắc chắn file '{IMAGE_PATH}' và '{SOUND_PATH}' tồn tại.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

III. CÂU HỎI ÔN TẬP
1. Sự khác nhau giữa RGB và HSV trong biểu diễn màu?
 * RGB (Red-Green-Blue): Hướng phần cứng, biểu diễn màu bằng cách pha trộn 3 kênh màu gốc (Đỏ, Lục, Lam). Mô hình này không trực quan với cách con người cảm nhận màu sắc.
 * HSV (Hue-Saturation-Value): Hướng con người, biểu diễn màu sắc theo 3 thuộc tính mà con người dễ nhận biết: Tông màu (Hue), Độ bão hòa (Saturation), và Độ sáng (Value). Mô hình này rất hữu ích trong xử lý ảnh khi cần chọn hoặc thay đổi một màu cụ thể.
2. Phân biệt lossless và lossy compression?
 * Lossless Compression (Nén không mất dữ liệu):
   * Mục đích: Giảm kích thước file mà không làm mất bất kỳ thông tin nào.
   * Cách hoạt động: Tìm và loại bỏ các dữ liệu dư thừa. Dữ liệu gốc có thể được khôi phục lại 100% từ file đã nén.
   * Ví dụ: PNG (ảnh), ZIP, FLAC (âm thanh).
 * Lossy Compression (Nén mất dữ liệu):
   * Mục đích: Đạt được tỉ lệ nén cao hơn nhiều bằng cách loại bỏ những thông tin được cho là "không quan trọng" hoặc khó nhận biết bởi tai/mắt người.
   * Cách hoạt động: Dữ liệu gốc không thể khôi phục hoàn toàn. Mỗi lần lưu lại file, chất lượng có thể giảm thêm.
   * Ví dụ: JPEG (ảnh), MP3 (âm thanh), MPEG (video).
3. Tần số lấy mẫu và bit depth ảnh hưởng thế nào đến chất lượng âm thanh?
 * Tần số lấy mẫu (Sample Rate - Hz): Là số lần tín hiệu âm thanh tương tự được "đo" hoặc "chụp lại" trong một giây để chuyển thành tín hiệu số.
   * Ảnh hưởng: Tần số càng cao, khả năng tái tạo các tần số âm thanh cao (âm treble, tiếng leng keng) càng chính xác. Tần số thấp sẽ làm mất các âm thanh tần số cao. Chuẩn CD là 44100 Hz, có thể tái tạo âm thanh lên tới 22050 Hz, vượt ngưỡng nghe của người.
 * Độ sâu bit (Bit Depth): Là số bit thông tin được dùng để biểu diễn mỗi mẫu âm thanh.
   * Ảnh hưởng: Bit depth càng cao, dải động (dynamic range - sự khác biệt giữa âm thanh nhỏ nhất và lớn nhất) càng rộng và chi tiết. Bit depth thấp gây ra "nhiễu lượng tử hóa" (quantization noise), làm âm thanh nghe "rè" hoặc thiếu chi tiết, đặc biệt ở những đoạn yên tĩnh. Chuẩn CD là 16-bit.
4. Mục đích của việc chuẩn hóa Unicode là gì?
Mục đích chính là để đảm bảo tính nhất quán và so sánh chính xác. Trong Unicode, một ký tự có dấu (ví dụ: ệ) có thể được biểu diễn theo hai cách:
 * Dưới dạng một ký tự duy nhất đã được tổ hợp sẵn (pre-composed).
 * Dưới dạng một chuỗi gồm ký tự cơ sở (e) và các dấu (^, .).
Việc chuẩn hóa (sang NFC hoặc NFD) sẽ đưa tất cả các chuỗi về một dạng duy nhất, giúp cho các tác vụ như tìm kiếm, so sánh chuỗi, và sắp xếp hoạt động đáng tin cậy. Nếu không chuẩn hóa, hai chuỗi trông giống hệt nhau có thể bị coi là khác nhau.
5. Khi nào nên chuyển ảnh sang grayscale trước khi xử lý?
Nên chuyển ảnh sang grayscale khi thông tin màu sắc không quan trọng hoặc gây nhiễu cho tác vụ xử lý. Cụ thể:
 * Phân tích hình dạng và kết cấu: Ví dụ như nhận dạng vật thể, phát hiện cạnh (edge detection).
 * Nhận dạng ký tự quang học (OCR): Máy chỉ cần quan tâm đến hình dạng của ký tự, không cần màu sắc.
 * Nhận dạng khuôn mặt: Nhiều thuật toán ban đầu hoạt động trên ảnh xám để tập trung vào các đặc điểm như mắt, mũi, miệng.
 * Giảm độ phức tạp tính toán: Xử lý trên 1 kênh (ảnh xám) nhanh hơn nhiều so với 3 kênh (ảnh RGB).
6. Nếu muốn tách vùng màu đỏ trong ảnh, nên dùng mô hình màu nào?
Nên dùng mô hình màu HSV. Lý do là trong mô hình HSV, màu đỏ tương ứng với một khoảng giá trị rất hẹp của kênh Hue (Tông màu). Ta có thể dễ dàng lọc tất cả các pixel có giá trị Hue nằm trong khoảng đó, bất kể chúng sáng hay tối, đậm hay nhạt. Việc này rất khó thực hiện trong mô hình RGB vì một pixel màu đỏ có thể có vô số sự kết hợp của các giá trị R, G, B.
7. Vì sao cần chuẩn hóa biên độ âm thanh về [-1,1]?
Chuẩn hóa biên độ âm thanh về khoảng [-1, 1] (hoặc [0, 1]) là một quy ước tiêu chuẩn trong xử lý tín hiệu số (DSP) và học máy vì các lý do sau:
 * Ngăn ngừa Clipping (vỡ tiếng): Đảm bảo tín hiệu không vượt quá giá trị tối đa mà định dạng số có thể biểu diễn, tránh gây ra méo tiếng.
 * Tạo sự nhất quán: Đưa tất cả các file âm thanh (dù được thu ở âm lượng to hay nhỏ) về một thang đo chung, giúp các thuật toán xử lý (như bộ lọc, hiệu ứng) hoạt động đồng đều.
 * Yêu cầu của thuật toán: Nhiều thuật toán xử lý âm thanh và mô hình học máy được thiết kế để làm việc với dữ liệu đầu vào trong một khoảng giá trị cố định.
 * Độc lập với Bit Depth: Biên độ [-1, 1] là một biểu diễn tương đối, không phụ thuộc vào bit depth (16-bit, 24-bit, 32-bit float) của file gốc.




—-------------------------------------------------------------------------------------------------------------------
BÀI ÔN TẬP GIỮA KỲ – CÔNG NGHỆ ĐA PHƯƠNG TIỆN
Learning Outcome 2: Giải thích được các công nghệ (hệ điều hành, mạng) hỗ trợ hệ thống đa phương tiện.
Mục tiêu: Hiểu rõ vai trò của hệ điều hành và mạng trong việc xây dựng, truyền tải và xử lý các nội dung đa phương tiện (âm thanh, hình ảnh, video, text).
I. PHẦN LÝ THUYẾT
1. Vai trò của Hệ điều hành trong hệ thống đa phương tiện
Hệ điều hành (Operating System – OS) là nền tảng điều phối tài nguyên (CPU, bộ nhớ, thiết bị ngoại vi) để các ứng dụng đa phương tiện có thể hoạt động trơn tru.
• OS quản lý thời gian thực (real-time scheduling) giúp âm thanh và video phát mượt.
• Cung cấp API và driver cho card đồ họa, card âm thanh, thiết bị nhập/xuất.
• Quản lý file và hệ thống lưu trữ (filesystem) để truy xuất nhanh các dữ liệu lớn như video 4K.
• Hỗ trợ đa nhiệm (multitasking), xử lý song song (multithreading).
2. Các công nghệ hệ điều hành hỗ trợ đa phương tiện
• **Windows Media Foundation** – Framework xử lý audio/video của Windows.
• **Core Audio / Core Image** – API của macOS.
• **ALSA / PulseAudio / GStreamer** – Hệ thống âm thanh và stream trong Linux.
• **DirectX / OpenGL / Vulkan** – Giao diện lập trình đồ họa, hỗ trợ tăng tốc GPU.
• **Real-Time OS (RTOS)** – Hệ điều hành thời gian thực cho các ứng dụng streaming, truyền hình, IoT.
3. Vai trò của mạng trong hệ thống đa phương tiện
Mạng máy tính giúp **truyền tải nội dung đa phương tiện** giữa các thiết bị: truyền hình trực tuyến, hội nghị video, âm thanh, hoặc phát trực tiếp (livestream).
• Cần đảm bảo **băng thông (bandwidth)** đủ lớn để truyền video HD/4K.
• **Độ trễ (latency)** thấp để âm thanh và hình ảnh đồng bộ.
• **QoS (Quality of Service)** giúp ưu tiên luồng đa phương tiện.
• **Streaming protocols:** RTP, RTSP, HTTP Live Streaming (HLS), DASH.
• **Nén và truyền tải:** Sử dụng codec (H.264, AAC) để giảm dung lượng.
4. Công nghệ mạng hỗ trợ đa phương tiện
• **CDN (Content Delivery Network):** Phân phối nội dung qua nhiều máy chủ giúp giảm tải và tăng tốc độ truy cập.
• **Cloud Streaming (YouTube, Netflix):** Dịch vụ đám mây lưu trữ và truyền phát video.
• **WebRTC:** Giao thức giao tiếp thời gian thực giữa các trình duyệt (dùng trong Zoom, Google Meet).
• **Multicast / Unicast / Broadcast:** Các phương thức truyền dữ liệu trong mạng.
5. Tổng kết phần lý thuyết
Hệ điều hành cung cấp nền tảng và API cho xử lý, hiển thị đa phương tiện; mạng đảm bảo truyền tải nhanh, ổn định và đồng bộ nội dung. Sự kết hợp giữa OS + Network giúp hệ thống đa phương tiện hoạt động trơn tru, liên tục và theo thời gian thực.
II. PHẦN THỰC HÀNH ÔN TẬP
Bài 1 – Kiểm tra thông tin hệ điều hành
Viết chương trình Python in ra tên hệ điều hành, phiên bản, số lõi CPU và dung lượng RAM khả dụng.
Ví dụ:
import platform, psutil
print('OS:', platform.system(), platform.release())
print('CPU cores:', psutil.cpu_count(logical=True))
print('RAM (GB):', round(psutil.virtual_memory().total/1e9,2))
Bài 2 – Kiểm tra băng thông và độ trễ mạng
Sử dụng Python kiểm tra tốc độ tải xuống, tải lên và độ trễ trung bình.
Ví dụ (yêu cầu thư viện speedtest-cli):
import speedtest
st = speedtest.Speedtest()
st.download(); st.upload()
print('Ping (ms):', st.results.ping)
print('Download (Mbps):', st.download()/1e6)
print('Upload (Mbps):', st.upload()/1e6)
Bài 3 – Mô phỏng streaming video đơn giản
Tạo socket server và client để gửi và nhận khung hình từ webcam (OpenCV). Mục tiêu: hiểu cơ chế truyền dữ liệu đa phương tiện qua mạng LAN.
Bài 4 – Quản lý tiến trình xử lý âm thanh/video
Dùng mô-đun multiprocessing của Python để phát âm thanh và hiển thị ảnh cùng lúc, mô phỏng cơ chế đa nhiệm của hệ điều hành trong ứng dụng đa phương tiện.
III. CÂU HỎI ÔN TẬP
●	1. Hệ điều hành ảnh hưởng thế nào đến hiệu suất xử lý đa phương tiện?
●	2. Phân biệt DirectX, OpenGL, và Vulkan.
●	3. Tại sao video streaming yêu cầu QoS và băng thông cao?
●	4. Nêu sự khác nhau giữa Unicast, Multicast và Broadcast.
●	5. CDN hoạt động như thế nào để tăng tốc độ truyền nội dung?
●	6. So sánh ưu nhược điểm của RTSP và HLS.
●	7. Mạng 5G hỗ trợ truyền tải đa phương tiện tốt hơn 4G ở điểm nào?
●	8. Vì sao WebRTC được dùng nhiều trong họp trực tuyến?


—-------
Chào bạn, tiếp nối phần ôn tập trước, đây là câu trả lời chi tiết cho các nội dung liên quan đến vai trò của Hệ điều hành và Mạng trong hệ thống đa phương tiện.
BÀI ÔN TẬP GIỮA KỲ – CÔNG NGHỆ ĐA PHƯƠNG TIỆN (Phần 2)
Nội dung ôn tập này tập trung vào các công nghệ nền tảng (hệ điều hành, mạng) hỗ trợ cho hệ thống đa phương tiện. Dưới đây là giải đáp chi tiết cho phần thực hành và các câu hỏi lý thuyết.
I. PHẦN LÝ THUYẾT
Bạn đã tóm tắt rất chính xác và đầy đủ vai trò của Hệ điều hành và Mạng:
 * Hệ điều hành (OS): Đóng vai trò là "nhạc trưởng", điều phối tài nguyên phần cứng (CPU, RAM, GPU), cung cấp các API chuyên dụng (DirectX, Core Audio), và quản lý đa nhiệm để các ứng dụng media chạy mượt mà, ổn định.
 * Mạng máy tính (Network): Đóng vai trò là "hệ thống giao thông", chịu trách nhiệm truyền tải nội dung đa phương tiện đi xa. Các yếu tố quan trọng là băng thông (tốc độ), độ trễ (thời gian chờ), và các giao thức streaming (HLS, DASH) để đảm bảo nội dung được phát liên tục và đồng bộ.
Đây là nền tảng vững chắc để chúng ta giải quyết các bài tập thực hành.
II. PHẦN THỰC HÀNH ÔN TẬP
Dưới đây là lời giải chi tiết kèm mã nguồn và giải thích cho từng bài.
(Lưu ý: Để chạy các đoạn mã, bạn cần cài đặt các thư viện cần thiết bằng lệnh: pip install psutil speedtest-cli opencv-python numpy)
Bài 1 – Kiểm tra thông tin hệ điều hành
Yêu cầu: Viết chương trình Python in ra tên hệ điều hành, phiên bản, số lõi CPU và dung lượng RAM.
Mã nguồn (Python):
import platform
import psutil
import os

print("--- THÔNG TIN HỆ ĐIỀU HÀNH VÀ PHẦN CỨNG ---")

# Lấy thông tin hệ điều hành
print(f"Hệ điều hành (OS): {platform.system()}")
print(f"Phiên bản OS: {platform.release()}")
print(f"Kiến trúc: {platform.machine()}")

# Lấy thông tin CPU
# logical=True: đếm cả lõi logic (luồng xử lý). logical=False: chỉ đếm lõi vật lý.
print(f"Số lõi CPU (vật lý): {psutil.cpu_count(logical=False)}")
print(f"Số luồng CPU (logic): {psutil.cpu_count(logical=True)}")

# Lấy thông tin bộ nhớ RAM
mem = psutil.virtual_memory()
total_ram_gb = mem.total / (1024 ** 3) # Chuyển đổi từ byte sang GB
available_ram_gb = mem.available / (1024 ** 3)

print(f"Tổng dung lượng RAM: {total_ram_gb:.2f} GB")
print(f"Dung lượng RAM khả dụng: {available_ram_gb:.2f} GB")

Giải thích:
 * platform: Thư viện này cung cấp thông tin về nền tảng đang chạy chương trình, như tên OS, phiên bản, kiến trúc.
 * psutil (process and system utilities): Là thư viện mạnh mẽ để truy xuất thông tin về các tiến trình đang chạy và tài nguyên hệ thống như CPU, bộ nhớ, ổ đĩa, mạng.
Bài 2 – Kiểm tra băng thông và độ trễ mạng
Yêu cầu: Sử dụng Python kiểm tra tốc độ tải xuống, tải lên và độ trễ mạng.
Mã nguồn (Python):
import speedtest

print("--- KIỂM TRA TỐC ĐỘ MẠNG ---")
print("Đang tìm máy chủ tốt nhất, vui lòng chờ...")

try:
    st = speedtest.Speedtest()
    st.get_best_server() # Tìm server có ping thấp nhất để kiểm tra

    print("Đang kiểm tra tốc độ tải xuống (Download)...")
    download_speed = st.download() / 1_000_000 # Chuyển từ bit/s sang Mbit/s

    print("Đang kiểm tra tốc độ tải lên (Upload)...")
    upload_speed = st.upload() / 1_000_000 # Chuyển từ bit/s sang Mbit/s
    
    ping_result = st.results.ping

    print("\n--- KẾT QUẢ ---")
    print(f"Độ trễ (Ping): {ping_result:.2f} ms")
    print(f"Tốc độ tải xuống: {download_speed:.2f} Mbps")
    print(f"Tốc độ tải lên: {upload_speed:.2f} Mbps")

except speedtest.SpeedtestException as e:
    print(f"Lỗi: Không thể thực hiện kiểm tra. Vui lòng kiểm tra kết nối mạng. ({e})")

Giải thích:
 * Thư viện speedtest-cli tự động hóa việc kết nối đến các máy chủ của Speedtest.net để đo lường các thông số mạng quan trọng.
 * Ping (ms): Độ trễ, là thời gian để một gói tin đi từ máy bạn đến máy chủ và quay về. Ping càng thấp, kết nối càng có độ phản hồi tốt, quan trọng cho game và họp trực tuyến.
 * Download/Upload (Mbps): Băng thông, là lượng dữ liệu tối đa có thể truyền/nhận trong một giây. Băng thông càng cao, khả năng xem video chất lượng cao và tải file lớn càng tốt.
Bài 3 – Mô phỏng streaming video đơn giản
Yêu cầu: Tạo socket server và client để truyền và nhận khung hình từ webcam qua mạng LAN.
Giải thích cơ chế:
 * Server: Mở webcam, liên tục chụp từng khung hình (frame).
 * Serialize: Chuyển đổi khung hình (một mảng NumPy) thành một chuỗi byte bằng pickle.
 * Gửi dữ liệu: Gửi kích thước của chuỗi byte trước, sau đó gửi chính chuỗi byte đó qua socket. Việc gửi kích thước trước rất quan trọng để client biết cần nhận bao nhiêu byte.
 * Client: Nhận kích thước, sau đó nhận đủ số byte của khung hình.
 * Deserialize: Chuyển chuỗi byte nhận được trở lại thành khung hình.
 * Hiển thị: Hiển thị khung hình lên màn hình.
Mã nguồn Server (server.py):
import socket, cv2, pickle, struct

# Tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1' # Chạy trên máy local, hoặc dùng IP LAN của bạn
port = 9999
socket_address = (host_ip, port)

# Bind socket và lắng nghe
server_socket.bind(socket_address)
server_socket.listen(5)
print("SERVER ĐANG LẮNG NGHE TẠI:", socket_address)

# Chấp nhận kết nối từ client
while True:
    client_socket, addr = server_socket.accept()
    print('KẾT NỐI TỪ:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0) # Mở webcam
        while vid.isOpened():
            ret, frame = vid.read()
            if not ret:
                break
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            try:
                client_socket.sendall(message)
            except:
                print(f"Client {addr} đã ngắt kết nối.")
                break
            # cv2.imshow('TRANSMITTING VIDEO', frame) # Bỏ comment nếu muốn xem server đang gửi gì
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
        client_socket.close()

Mã nguồn Client (client.py):
import socket, cv2, pickle, struct

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1' # Địa chỉ IP của Server
port = 9999
client_socket.connect((host_ip, port))

data = b""
payload_size = struct.calcsize("Q")
print("ĐÃ KẾT NỐI TỚI SERVER.")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024)
        if not packet: break
        data += packet
    if not data: break
    
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]
    
    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    
    frame_data = data[:msg_size]
    data = data[msg_size:]
    
    frame = pickle.loads(frame_data)
    cv2.imshow("RECEIVING VIDEO", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
client_socket.close()
cv2.destroyAllWindows()

Cách chạy: Mở terminal, chạy python server.py. Sau đó mở terminal khác, chạy python client.py.
Bài 4 – Quản lý tiến trình xử lý âm thanh/video
Yêu cầu: Dùng multiprocessing để phát âm thanh và hiển thị ảnh cùng lúc.
Mã nguồn (Python):
import multiprocessing
from playsound import playsound
from PIL import Image
import time

# --- Các file media cần có sẵn ---
SOUND_FILE = 'sample.wav' 
IMAGE_FILE = 'input.jpg'

def play_audio(file_path):
    """Hàm này sẽ chạy trong một tiến trình riêng để phát âm thanh."""
    print(f"[Tiến trình Audio] Bắt đầu phát file: {file_path}")
    try:
        playsound(file_path)
        print("[Tiến trình Audio] Đã phát xong.")
    except Exception as e:
        print(f"[Tiến trình Audio] Lỗi: {e}")

def display_image(file_path):
    """Hàm này chạy trong một tiến trình riêng để hiển thị ảnh."""
    print(f"[Tiến trình Image] Bắt đầu hiển thị file: {file_path}")
    try:
        img = Image.open(file_path)
        img.show()
        # Giữ tiến trình sống một lúc để người dùng xem ảnh
        time.sleep(5) 
        print("[Tiến trình Image] Đã đóng.")
    except Exception as e:
        print(f"[Tiến trình Image] Lỗi: {e}")

if __name__ == "__main__":
    print("--- MÔ PHỎNG ĐA NHIỆM CỦA HỆ ĐIỀU HÀNH ---")
    
    # Tạo hai tiến trình riêng biệt
    audio_process = multiprocessing.Process(target=play_audio, args=(SOUND_FILE,))
    image_process = multiprocessing.Process(target=display_image, args=(IMAGE_FILE,))

    # Bắt đầu chạy cả hai tiến trình gần như đồng thời
    audio_process.start()
    image_process.start()

    print("[Tiến trình chính] Đã khởi chạy 2 tiến trình con.")
    
    # Chờ cho cả hai tiến trình kết thúc
    audio_process.join()
    image_process.join()
    
    print("[Tiến trình chính] Tất cả các tiến trình đã hoàn thành.")


Giải thích:
 * Hệ điều hành có khả năng chạy nhiều chương trình cùng lúc (đa nhiệm). Thư viện multiprocessing mô phỏng điều này bằng cách tạo ra các tiến trình (process) riêng biệt.
 * Mỗi tiến trình có không gian bộ nhớ độc lập và được OS lên lịch thực thi song song trên các lõi CPU khác nhau (nếu có thể).
 * Kết quả là âm thanh có thể phát và hình ảnh có thể hiển thị mà không cái nào phải chờ cái nào, giống như khi bạn vừa nghe nhạc vừa xem ảnh trên máy tính.




Chắc chắn rồi, đây là phần tóm tắt các câu hỏi và trả lời ôn tập dưới dạng văn bản (text) thuần túy, ngắn gọn và dễ hiểu.
TÓM TẮT ÔN TẬP – HỆ ĐIỀU HÀNH & MẠNG CHO ĐA PHƯƠNG TIỆN
PHẦN CÂU HỎI ÔN TẬP (Dạng text)
1. Hệ điều hành ảnh hưởng thế nào đến hiệu suất xử lý đa phương tiện?
HĐH ảnh hưởng qua 3 cơ chế chính:
 * Lập lịch (Scheduling): Ưu tiên tài nguyên CPU cho các ứng dụng media để chạy mượt mà, không bị giật.
 * Quản lý Driver: Cung cấp driver để phần mềm khai thác sức mạnh của card đồ họa/âm thanh, giúp tăng tốc phần cứng.
 * Quản lý Bộ nhớ: Tối ưu hóa việc đọc/ghi các file media dung lượng lớn thông qua bộ nhớ đệm (cache).
2. Phân biệt DirectX, OpenGL, và Vulkan.
Đây là các API đồ họa (cầu nối giữa phần mềm và GPU):
 * DirectX: Của Microsoft, chỉ dùng cho Windows và Xbox, cấp cao, dễ dùng.
 * OpenGL: Đa nền tảng, là tiêu chuẩn công nghiệp trong nhiều năm, cấp cao.
 * Vulkan: Thế hệ mới của OpenGL, đa nền tảng, cấp thấp, cho phép kiểm soát phần cứng tối đa để đạt hiệu năng cao nhất nhưng phức tạp hơn khi lập trình.
3. Tại sao video streaming yêu cầu QoS và băng thông cao?
 * Băng thông cao: Giống như "đường ống" mạng phải đủ lớn để lượng dữ liệu video khổng lồ có thể truyền qua liên tục mà không bị tắc nghẽn (gây buffering).
 * QoS (Quality of Service): Giống như "làn đường ưu tiên" trên xa lộ mạng. Nó đảm bảo các gói tin video nhạy cảm với thời gian được đi trước, tránh bị các dữ liệu khác làm trễ, giúp video không bị giật lag.
4. Nêu sự khác nhau giữa Unicast, Multicast và Broadcast.
 * Unicast (1-tới-1): Một người gửi, một người nhận. (Ví dụ: Duyệt một trang web).
 * Broadcast (1-tới-tất cả): Một người gửi, tất cả mọi người trong cùng mạng LAN đều nhận. (Ví dụ: Thông báo chung trong mạng nội bộ).
 * Multicast (1-tới-nhiều): Một người gửi, chỉ những ai đã đăng ký nhận mới nhận được. (Ví dụ: Truyền hình IPTV).
5. CDN hoạt động như thế nào để tăng tốc độ truyền nội dung?
CDN (Mạng phân phối nội dung) đặt các máy chủ chứa bản sao của nội dung (video, ảnh) ở nhiều vị trí địa lý. Khi bạn yêu cầu nội dung, thay vì kết nối tới máy chủ gốc ở xa, CDN sẽ điều hướng bạn đến máy chủ gần bạn nhất. Việc này giúp giảm đáng kể độ trễ và tăng tốc độ tải.
6. So sánh ưu nhược điểm của RTSP và HLS.
 * RTSP (Real-Time Streaming Protocol): Ưu điểm là độ trễ rất thấp, phù hợp cho camera an ninh, giám sát. Nhược điểm là dùng cổng riêng nên khó vượt tường lửa và kém tương thích với trình duyệt.
 * HLS (HTTP Live Streaming): Ưu điểm là chạy trên cổng web chuẩn (80/443) nên tương thích mọi nơi, dễ dàng vượt tường lửa và hỗ trợ tốt việc tự đổi chất lượng video theo mạng. Nhược điểm là độ trễ cao hơn RTSP.
7. Mạng 5G hỗ trợ truyền tải đa phương tiện tốt hơn 4G ở điểm nào?
5G vượt trội 4G ở 3 điểm chính:
 * Băng thông cao hơn: Cho phép stream video 4K/8K, VR/AR mượt mà.
 * Độ trễ cực thấp: Phản hồi gần như tức thì, lý tưởng cho game streaming và các ứng dụng tương tác thời gian thực.
 * Mật độ kết nối lớn: Hỗ trợ nhiều thiết bị kết nối cùng lúc mà không làm giảm chất lượng mạng.
8. Vì sao WebRTC được dùng nhiều trong họp trực tuyến?
WebRTC (Giao tiếp thời gian thực trên web) phổ biến cho họp trực tuyến vì:
 * Độ trễ thấp và được thiết kế cho giao tiếp thời gian thực.
 * Hỗ trợ kết nối ngang hàng (P2P) trực tiếp giữa người dùng, giảm tải cho máy chủ.
 * Tích hợp sẵn trong trình duyệt, không cần cài đặt phần mềm.
 * Bảo mật vì mọi luồng dữ liệu đều được mã hóa bắt buộc.



PHẦN A – LÝ THUYẾT (4 điểm) – 60 phút
Câu 1 (1.5 điểm)
a. Trình bày mô hình màu RGB và HSV, nêu sự khác nhau giữa chúng.
b. Trong xử lý ảnh, tại sao nhiều ứng dụng lại chuyển ảnh từ RGB sang HSV trước khi tách màu?
Câu 2 (1 điểm)
a. Giải thích khái niệm Unicode và chuẩn hóa ký tự (Normalization).
b. Phân biệt ASCII và UTF-8 bằng ví dụ.
Câu 3 (1 điểm)
a. Mô tả nguyên lý lấy mẫu và lượng tử hóa trong âm thanh số.
b. Giải thích mối quan hệ giữa Sample Rate, Bit Depth và chất lượng âm thanh.
Câu 4 (0.5 điểm)
a. Trình bày vai trò của hệ điều hành trong xử lý đa phương tiện.
b. Nêu 2 công nghệ hoặc API tiêu biểu hỗ trợ âm thanh/đồ họa trên Windows, Linux hoặc macOS.
PHẦN B – THỰC HÀNH PYTHON (6 điểm) – 120 phút
Câu 5 (1.5 điểm) – Xử lý văn bản Unicode
1. Nhập vào một chuỗi có dấu tiếng Việt.
2. In ra mã Unicode của từng ký tự.
3. Thực hiện chuẩn hóa chuỗi theo NFC và NFD, so sánh độ dài.
4. Ghi kết quả vào file unicode_report.txt.
Gợi ý thư viện: unicodedata, open().
Câu 6 (1.5 điểm) – Xử lý ảnh
1. Đọc tệp ảnh flower.jpg.
2. In kích thước (width × height), số kênh màu, giá trị trung bình độ sáng.
3. Chuyển sang grayscale và lưu thành flower_gray.png.
4. Hiển thị song song ảnh gốc và ảnh grayscale bằng matplotlib.
Gợi ý: Pillow, numpy, matplotlib.pyplot.
Câu 7 (1.5 điểm) – Xử lý âm thanh
1. Đọc file sample.wav.
2. In ra tần số lấy mẫu và thời lượng.
3. Vẽ biểu đồ sóng âm cho 3000 mẫu đầu tiên.
4. Chuẩn hóa âm thanh về [-1,1] và lưu thành sample_norm.wav.
Gợi ý: scipy.io.wavfile, matplotlib, numpy.
Câu 8 (1.5 điểm) – Hệ điều hành và mạng
1. In ra tên hệ điều hành, phiên bản, số lõi CPU và dung lượng RAM (GB).
2. Kiểm tra kết nối mạng đến www.google.com bằng ping, in kết quả.
3. Nếu ping thành công, ghi dòng “Kết nối mạng OK” vào file system_report.txt.
Gợi ý: platform, psutil, subprocess, os.




Bai-lam



Chắc chắn rồi, dưới đây là đáp án chi tiết và giải thích đầy đủ cho đề thi giữa kỳ môn Công nghệ Đa phương tiện.
ĐÁP ÁN ĐỀ THI GIỮA KỲ – CÔNG NGHỆ ĐA PHƯƠG TIỆN
PHẦN A – LÝ THUYẾT (4 điểm)
Câu 1 (1.5 điểm)
a. Trình bày mô hình màu RGB và HSV, nêu sự khác nhau giữa chúng.
 * Mô hình màu RGB (Red, Green, Blue):
   * Nguyên lý: Là mô hình màu cộng, hoạt động dựa trên nguyên tắc pha trộn ba màu gốc là Đỏ (Red), Lục (Green), và Lam (Blue) để tạo ra các màu khác.
   * Biểu diễn: Mỗi màu được biểu diễn bằng một bộ 3 giá trị (R, G, B), mỗi giá trị thường nằm trong khoảng từ 0 đến 255. Ví dụ: (255, 0, 0) là màu đỏ, (0, 0, 0) là màu đen, (255, 255, 255) là màu trắng.
   * Ứng dụng: Được sử dụng chủ yếu trong các thiết bị phát sáng như màn hình máy tính, TV, máy ảnh số.
 * Mô hình màu HSV (Hue, Saturation, Value):
   * Nguyên lý: Là mô hình màu mô phỏng cách con người cảm nhận màu sắc.
     * Hue (Tông màu): Loại màu sắc, biểu diễn bằng một góc từ 0-360 độ trên vòng tròn màu (ví dụ: 0° là đỏ, 120° là lục, 240° là lam).
     * Saturation (Độ bão hòa): Độ "tinh khiết" hay "đậm" của màu. Giá trị 0 là màu xám, giá trị tối đa là màu thuần khiết nhất.
     * Value (Độ sáng): Độ sáng tối của màu. Giá trị 0 là màu đen.
   * Ứng dụng: Thường được dùng trong các phần mềm đồ họa, xử lý ảnh để chọn và điều chỉnh màu một cách trực quan:
So sánh sự khác nhau giữa RGB và HSV
 * Về bản chất:
   * RGB: Hướng tới phần cứng (mô hình màu cộng).
   * HSV: Hướng tới cảm nhận của con người.
 * Về tính trực quan:
   * RGB: Khó điều chỉnh độ sáng hay độ đậm nhạt.
   * HSV: Rất trực quan, dễ dàng thay đổi riêng lẻ tông màu, độ bão hòa, và độ sáng.
 * Về sự phụ thuộc giữa các thành phần:
   * RGB: Các thành phần R, G, B liên quan chặt chẽ với nhau.
   * HSV: Các thành phần H, S, V tương đối độc lập với nhau.

 b. Trong xử lý ảnh, tại sao nhiều ứng dụng lại chuyển ảnh từ RGB sang HSV trước khi tách màu?
Nhiều ứng dụng chuyển ảnh từ RGB sang HSV trước khi tách màu vì mô hình HSV tách biệt rõ ràng thông tin về màu sắc (Hue) khỏi thông tin về cường độ sáng (Value) và độ bão hòa (Saturation).
Điều này cực kỳ hữu ích, ví dụ khi muốn tách tất cả các đối tượng màu đỏ trong ảnh. Trong không gian màu HSV, ta chỉ cần lọc tất cả các pixel có giá trị Hue nằm trong một khoảng hẹp của màu đỏ. Điều này sẽ lấy được cả màu đỏ đậm, đỏ nhạt, đỏ tươi. Ngược lại, trong không gian RGB, việc này rất phức tạp vì màu đỏ nhạt và đỏ đậm có các bộ giá trị (R, G, B) hoàn toàn khác nhau.
Câu 2 (1 điểm)
a. Giải thích khái niệm Unicode và chuẩn hóa ký tự (Normalization).
 * Unicode: Là một tiêu chuẩn mã hóa ký tự quốc tế, với mục tiêu cung cấp một mã số duy nhất (gọi là code point) cho mọi ký tự trong mọi ngôn ngữ trên thế giới, bao gồm cả các ký tự đặc biệt, biểu tượng. Điều này giải quyết vấn đề xung đột giữa các bảng mã khác nhau (như TCVN3, VNI) và cho phép xử lý văn bản đa ngôn ngữ một cách nhất quán.
 * Chuẩn hóa ký tự (Normalization): Là quá trình chuyển đổi một chuỗi ký tự về một dạng biểu diễn chuẩn tắc. Trong Unicode, một ký tự có dấu (ví dụ ệ) có thể được biểu diễn bằng 2 cách: dạng tổ hợp (một code point duy nhất) hoặc dạng phân rã (ký tự e + dấu ^ + dấu .). Chuẩn hóa đảm bảo rằng hai chuỗi trông giống hệt nhau sẽ thực sự bằng nhau khi so sánh, giúp cho việc tìm kiếm, sắp xếp hoạt động chính xác.
b. Phân biệt ASCII và UTF-8 bằng ví dụ.
 * ASCII (American Standard Code for Information Interchange):
   * Dùng 7 bit, chỉ biểu diễn được 128 ký tự.
   * Chỉ bao gồm các chữ cái Latin không dấu, chữ số, và các ký tự điều khiển cơ bản. Không thể biểu diễn tiếng Việt có dấu.
   * Mỗi ký tự chiếm đúng 1 byte.
 * UTF-8 (Unicode Transformation Format - 8-bit):
   * Là một cách mã hóa cho bộ ký tự Unicode, có thể biểu diễn mọi ký tự trên thế giới.
   * Sử dụng bộ mã hóa có độ dài thay đổi: từ 1 đến 4 byte cho mỗi ký tự.
   * Tương thích ngược hoàn toàn với ASCII (128 ký tự đầu tiên của ASCII và UTF-8 có cùng mã).
 * Ví dụ:
   * Ký tự A:
     * Trong ASCII: 01000001 (1 byte)
     * Trong UTF-8: 01000001 (1 byte) -> Giống hệt ASCII.
   * Ký tự â:
     * Trong ASCII: Không tồn tại.
     * Trong UTF-8: 11000011 10100011 (2 byte).
Câu 3 (1 điểm)
a. Mô tả nguyên lý lấy mẫu và lượng tử hóa trong âm thanh số.
 * Lấy mẫu (Sampling): Là quá trình chuyển đổi tín hiệu âm thanh tương tự (liên tục theo thời gian) thành một chuỗi các giá trị rời rạc. Quá trình này thực hiện bằng cách "đo" giá trị biên độ của sóng âm tại những khoảng thời gian đều đặn. Tần suất của các lần đo này được gọi là tần số lấy mẫu (Sample Rate).
 * Lượng tử hóa (Quantization): Sau khi lấy mẫu, mỗi giá trị biên độ đo được (vẫn là giá trị tương tự) sẽ được làm tròn và gán cho một giá trị số nguyên gần nhất trong một thang đo có hữu hạn mức. Số lượng mức trong thang đo này được quyết định bởi độ sâu bit (Bit Depth).
b. Giải thích mối quan hệ giữa Sample Rate, Bit Depth và chất lượng âm thanh.
Sample Rate và Bit Depth là hai thông số quyết định trực tiếp đến chất lượng âm thanh số và dung lượng file:
 * Sample Rate (Tần số lấy mẫu): Quyết định dải tần số của âm thanh. Sample rate càng cao, khả năng tái tạo các âm thanh có tần số cao (âm treble, tiếng leng keng) càng chính xác. Nếu sample rate quá thấp, các âm thanh tần số cao sẽ bị mất.
 * Bit Depth (Độ sâu bit): Quyết định dải động (sự khác biệt giữa âm thanh to nhất và nhỏ nhất) và độ chi tiết của âm thanh. Bit depth càng cao, số mức lượng tử hóa càng nhiều, âm thanh được ghi lại càng chính xác, mượt mà và ít nhiễu hơn.
Kết luận: Âm thanh có Sample Rate cao hơn và Bit Depth lớn hơn sẽ có chất lượng cao hơn, trung thực hơn nhưng cũng chiếm dung lượng lưu trữ lớn hơn.
Câu 4 (0.5 điểm)
a. Trình bày vai trò của hệ điều hành trong xử lý đa phương tiện.
Hệ điều hành (OS) đóng vai trò nền tảng, điều phối và hỗ trợ các ứng dụng đa phương tiện thông qua các chức năng chính:
 * Quản lý tài nguyên: Phân bổ và quản lý CPU, RAM, GPU để các tác vụ xử lý video, audio được thực thi hiệu quả.
 * Lập lịch thời gian thực (Real-time Scheduling): Ưu tiên các tiến trình xử lý media để đảm bảo âm thanh, video phát liên tục, không bị giật, lag.
 * Cung cấp Driver: Cung cấp trình điều khiển để ứng dụng có thể giao tiếp và khai thác sức mạnh của phần cứng chuyên dụng như card đồ họa, card âm thanh.
 * Cung cấp API: Cung cấp các bộ thư viện (API) giúp lập trình viên dễ dàng xây dựng các ứng dụng đa phương tiện mà không cần làm việc trực tiếp với phần cứng.
b. Nêu 2 công nghệ hoặc API tiêu biểu hỗ trợ âm thanh/đồ họa trên Windows, Linux hoặc macOS.
 * Windows: DirectX (API đồ họa, âm thanh, game), Media Foundation (framework xử lý media).
 * macOS: Metal (API đồ họa), Core Audio (API âm thanh).
 * Linux: OpenGL/Vulkan (API đồ họa), ALSA/PulseAudio (hệ thống âm thanh), GStreamer (framework media).
PHẦN B – THỰC HÀNH PYTHON (6 điểm)
Lưu ý: Để chạy các đoạn mã, cần cài đặt các thư viện:
pip install numpy Pillow matplotlib scipy psutil
Câu 5 (1.5 điểm) – Xử lý văn bản Unicode
import unicodedata

# 1. Nhập vào một chuỗi có dấu tiếng Việt
input_string = "Trường Đại học Công nghệ Thông tin"
print(f"Chuỗi gốc: {input_string}")

# Mở file để ghi kết quả
with open("unicode_report.txt", "w", encoding="utf-8") as f:
    f.write(f"Phân tích chuỗi: '{input_string}'\n")
    f.write("="*30 + "\n\n")

    # 2. In ra mã Unicode của từng ký tự
    f.write("1. Mã Unicode (Code Point) của từng ký tự:\n")
    print("\n1. Mã Unicode (Code Point) của từng ký tự:")
    for char in input_string:
        unicode_code = f"U+{ord(char):04X}"
        print(f"'{char}' -> {unicode_code}")
        f.write(f"'{char}' -> {unicode_code}\n")

    # 3. Thực hiện chuẩn hóa chuỗi theo NFC và NFD, so sánh độ dài
    print("\n2. Chuẩn hóa và so sánh độ dài:")
    f.write("\n2. Chuẩn hóa và so sánh độ dài:\n")

    # NFC
    nfc_string = unicodedata.normalize('NFC', input_string)
    print(f"Dạng NFC: '{nfc_string}' - Độ dài: {len(nfc_string)}")
    f.write(f"Dạng NFC: '{nfc_string}' - Độ dài: {len(nfc_string)}\n")

    # NFD
    nfd_string = unicodedata.normalize('NFD', input_string)
    print(f"Dạng NFD: '{nfd_string}' - Độ dài: {len(nfd_string)}")
    f.write(f"Dạng NFD: '{nfd_string}' - Độ dài: {len(nfd_string)}\n")

    # So sánh
    if len(nfd_string) > len(nfc_string):
        comparison = "Độ dài chuỗi NFD lớn hơn NFC vì NFD tách ký tự thành ký tự cơ sở và dấu."
        print(comparison)
        f.write(comparison + "\n")

print("\nĐã ghi kết quả vào file 'unicode_report.txt'")

Câu 6 (1.5 điểm) – Xử lý ảnh
(Yêu cầu có file flower.jpg trong cùng thư mục)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

try:
    # 1. Đọc tệp ảnh flower.jpg
    img = Image.open('flower.jpg')

    # 2. In kích thước, số kênh màu, giá trị trung bình độ sáng
    width, height = img.size
    img_array = np.array(img)
    num_channels = img_array.shape[2] if len(img_array.shape) == 3 else 1
    
    # Tính độ sáng trung bình (average of pixel values)
    # Chuyển sang ảnh xám trước để tính độ sáng cho ảnh màu
    mean_brightness = np.array(img.convert('L')).mean()

    print(f"Kích thước ảnh: {width} × {height} pixels")
    print(f"Số kênh màu: {num_channels}")
    print(f"Giá trị độ sáng trung bình: {mean_brightness:.2f}")

    # 3. Chuyển sang grayscale và lưu thành flower_gray.png
    gray_img = img.convert('L')
    gray_img.save('flower_gray.png')
    print("Đã chuyển ảnh sang grayscale và lưu thành 'flower_gray.png'")

    # 4. Hiển thị song song ảnh gốc và ảnh grayscale
    plt.figure(figsize=(10, 5))

    # Ảnh gốc
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Ảnh gốc (Original)')
    plt.axis('off')

    # Ảnh grayscale
    plt.subplot(1, 2, 2)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Ảnh Grayscale')
    plt.axis('off')

    plt.suptitle('So sánh ảnh gốc và ảnh Grayscale')
    plt.show()

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'flower.jpg'. Vui lòng đặt file vào cùng thư mục.")

Câu 7 (1.5 điểm) – Xử lý âm thanh
(Yêu cầu có file sample.wav trong cùng thư mục)
from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt

try:
    # 1. Đọc file sample.wav
    fs, data = read('sample.wav')

    # 2. In ra tần số lấy mẫu và thời lượng
    duration = len(data) / fs
    print(f"Tần số lấy mẫu (Sample Rate): {fs} Hz")
    print(f"Thời lượng (Duration): {duration:.2f} giây")

    # 3. Vẽ biểu đồ sóng âm cho 3000 mẫu đầu tiên
    plt.figure(figsize=(12, 4))
    plt.plot(data[:3000])
    plt.title('Biểu đồ sóng âm (3000 mẫu đầu tiên)')
    plt.xlabel('Mẫu (Sample)')
    plt.ylabel('Biên độ (Amplitude)')
    plt.grid(True)
    plt.show()

    # 4. Chuẩn hóa âm thanh về [-1,1] và lưu thành sample_norm.wav
    # Chuyển dữ liệu sang kiểu float để tính toán
    audio_float = data.astype(np.float32)
    
    # Tìm giá trị biên độ lớn nhất
    max_amp = np.max(np.abs(audio_float))
    if max_amp > 0:
        normalized_data = audio_float / max_amp
    else:
        normalized_data = audio_float # Tránh chia cho 0

    write('sample_norm.wav', fs, normalized_data)
    print("Đã chuẩn hóa âm thanh và lưu thành công file 'sample_norm.wav'")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'sample.wav'. Vui lòng đặt file vào cùng thư mục.")

Câu 8 (1.5 điểm) – Hệ điều hành và mạng
import platform
import psutil
import subprocess
import os

# Mở file để ghi báo cáo
with open("system_report.txt", "w", encoding="utf-8") as f:
    f.write("Báo cáo hệ thống và mạng\n")
    f.write("="*30 + "\n\n")

    # 1. In ra thông tin hệ điều hành và phần cứng
    print("--- Thông tin hệ thống ---")
    f.write("--- Thông tin hệ thống ---\n")

    os_name = f"Hệ điều hành: {platform.system()} {platform.release()}"
    cpu_cores = f"Số lõi CPU: {psutil.cpu_count(logical=True)}"
    total_ram = f"Dung lượng RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB"

    print(os_name)
    print(cpu_cores)
    print(total_ram)
    
    f.write(os_name + "\n")
    f.write(cpu_cores + "\n")
    f.write(total_ram + "\n\n")

    # 2. Kiểm tra kết nối mạng đến www.google.com bằng ping
    print("\n--- Kiểm tra kết nối mạng ---")
    f.write("--- Kiểm tra kết nối mạng ---\n")
    hostname = "www.google.com"
    
    # Lệnh ping khác nhau tùy hệ điều hành
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', hostname]
    
    print(f"Đang ping đến {hostname}...")
    
    try:
        # Chạy lệnh và ẩn output trên console
        result = subprocess.run(command, capture_output=True, text=True, timeout=5)
        
        # 3. Nếu ping thành công, ghi kết quả
        if result.returncode == 0:
            message = "Kết nối mạng OK"
            print(message)
            f.write(message + "\n")
            # In ra output của lệnh ping để xem
            print(result.stdout)
        else:
            message = f"Kết nối mạng thất bại. Lỗi: {result.stderr}"
            print(message)
            f.write(message + "\n")
            
    except subprocess.TimeoutExpired:
        message = "Ping timed out. Không thể kết nối."
        print(message)
        f.write(message + "\n")
    except FileNotFoundError:
        message = "Lỗi: Lệnh 'ping' không tồn tại trên hệ thống này."
        print(message)
        f.write(message + "\n")

print("\nĐã ghi báo cáo vào file 'system_report.txt'")


—------------------------------------------------------------------------------------------------


PHẦN A – LÝ THUYẾT (4 điểm) – 60 phút
Câu 1 (1.5 điểm)
a. Trình bày mô hình màu RGB và HSV, nêu sự khác nhau giữa chúng.
b. Trong xử lý ảnh, tại sao nhiều ứng dụng lại chuyển ảnh từ RGB sang HSV trước khi tách màu?
Câu 2 (1 điểm)
a. Giải thích khái niệm Unicode và chuẩn hóa ký tự (Normalization).
b. Phân biệt ASCII và UTF-8 bằng ví dụ.
Câu 3 (1 điểm)
a. Mô tả nguyên lý lấy mẫu và lượng tử hóa trong âm thanh số.
b. Giải thích mối quan hệ giữa Sample Rate, Bit Depth và chất lượng âm thanh.
Câu 4 (0.5 điểm)
a. Trình bày vai trò của hệ điều hành trong xử lý đa phương tiện.
b. Nêu 2 công nghệ hoặc API tiêu biểu hỗ trợ âm thanh/đồ họa trên Windows, Linux hoặc macOS.
PHẦN B – THỰC HÀNH PYTHON (6 điểm) – 120 phút
Câu 5 (1.5 điểm) – Xử lý văn bản Unicode
1. Nhập vào một chuỗi có dấu tiếng Việt.
2. In ra mã Unicode của từng ký tự.
3. Thực hiện chuẩn hóa chuỗi theo NFC và NFD, so sánh độ dài.
4. Ghi kết quả vào file unicode_report.txt.
Gợi ý thư viện: unicodedata, open().
Câu 6 (1.5 điểm) – Xử lý ảnh
1. Đọc tệp ảnh flower.jpg.
2. In kích thước (width × height), số kênh màu, giá trị trung bình độ sáng.
3. Chuyển sang grayscale và lưu thành flower_gray.png.
4. Hiển thị song song ảnh gốc và ảnh grayscale bằng matplotlib.
Gợi ý: Pillow, numpy, matplotlib.pyplot.
Câu 7 (1.5 điểm) – Xử lý âm thanh
1. Đọc file sample.wav.
2. In ra tần số lấy mẫu và thời lượng.
3. Vẽ biểu đồ sóng âm cho 3000 mẫu đầu tiên.
4. Chuẩn hóa âm thanh về [-1,1] và lưu thành sample_norm.wav.
Gợi ý: scipy.io.wavfile, matplotlib, numpy.
Câu 8 (1.5 điểm) – Hệ điều hành và mạng
1. In ra tên hệ điều hành, phiên bản, số lõi CPU và dung lượng RAM (GB).
2. Kiểm tra kết nối mạng đến www.google.com bằng ping, in kết quả.
3. Nếu ping thành công, ghi dòng “Kết nối mạng OK” vào file system_report.txt.
Gợi ý: platform, psutil, subprocess, os.




Bai-lam



Chắc chắn rồi, dưới đây là đáp án chi tiết và giải thích đầy đủ cho đề thi giữa kỳ môn Công nghệ Đa phương tiện.
ĐÁP ÁN ĐỀ THI GIỮA KỲ – CÔNG NGHỆ ĐA PHƯƠG TIỆN
PHẦN A – LÝ THUYẾT (4 điểm)
Câu 1 (1.5 điểm)
a. Trình bày mô hình màu RGB và HSV, nêu sự khác nhau giữa chúng.
 * Mô hình màu RGB (Red, Green, Blue):
   * Nguyên lý: Là mô hình màu cộng, hoạt động dựa trên nguyên tắc pha trộn ba màu gốc là Đỏ (Red), Lục (Green), và Lam (Blue) để tạo ra các màu khác.
   * Biểu diễn: Mỗi màu được biểu diễn bằng một bộ 3 giá trị (R, G, B), mỗi giá trị thường nằm trong khoảng từ 0 đến 255. Ví dụ: (255, 0, 0) là màu đỏ, (0, 0, 0) là màu đen, (255, 255, 255) là màu trắng.
   * Ứng dụng: Được sử dụng chủ yếu trong các thiết bị phát sáng như màn hình máy tính, TV, máy ảnh số.
 * Mô hình màu HSV (Hue, Saturation, Value):
   * Nguyên lý: Là mô hình màu mô phỏng cách con người cảm nhận màu sắc.
     * Hue (Tông màu): Loại màu sắc, biểu diễn bằng một góc từ 0-360 độ trên vòng tròn màu (ví dụ: 0° là đỏ, 120° là lục, 240° là lam).
     * Saturation (Độ bão hòa): Độ "tinh khiết" hay "đậm" của màu. Giá trị 0 là màu xám, giá trị tối đa là màu thuần khiết nhất.
     * Value (Độ sáng): Độ sáng tối của màu. Giá trị 0 là màu đen.
   * Ứng dụng: Thường được dùng trong các phần mềm đồ họa, xử lý ảnh để chọn và điều chỉnh màu một cách trực quan:
So sánh sự khác nhau giữa RGB và HSV
 * Về bản chất:
   * RGB: Hướng tới phần cứng (mô hình màu cộng).
   * HSV: Hướng tới cảm nhận của con người.
 * Về tính trực quan:
   * RGB: Khó điều chỉnh độ sáng hay độ đậm nhạt.
   * HSV: Rất trực quan, dễ dàng thay đổi riêng lẻ tông màu, độ bão hòa, và độ sáng.
 * Về sự phụ thuộc giữa các thành phần:
   * RGB: Các thành phần R, G, B liên quan chặt chẽ với nhau.
   * HSV: Các thành phần H, S, V tương đối độc lập với nhau.

 b. Trong xử lý ảnh, tại sao nhiều ứng dụng lại chuyển ảnh từ RGB sang HSV trước khi tách màu?
Nhiều ứng dụng chuyển ảnh từ RGB sang HSV trước khi tách màu vì mô hình HSV tách biệt rõ ràng thông tin về màu sắc (Hue) khỏi thông tin về cường độ sáng (Value) và độ bão hòa (Saturation).
Điều này cực kỳ hữu ích, ví dụ khi muốn tách tất cả các đối tượng màu đỏ trong ảnh. Trong không gian màu HSV, ta chỉ cần lọc tất cả các pixel có giá trị Hue nằm trong một khoảng hẹp của màu đỏ. Điều này sẽ lấy được cả màu đỏ đậm, đỏ nhạt, đỏ tươi. Ngược lại, trong không gian RGB, việc này rất phức tạp vì màu đỏ nhạt và đỏ đậm có các bộ giá trị (R, G, B) hoàn toàn khác nhau.
Câu 2 (1 điểm)
a. Giải thích khái niệm Unicode và chuẩn hóa ký tự (Normalization).
 * Unicode: Là một tiêu chuẩn mã hóa ký tự quốc tế, với mục tiêu cung cấp một mã số duy nhất (gọi là code point) cho mọi ký tự trong mọi ngôn ngữ trên thế giới, bao gồm cả các ký tự đặc biệt, biểu tượng. Điều này giải quyết vấn đề xung đột giữa các bảng mã khác nhau (như TCVN3, VNI) và cho phép xử lý văn bản đa ngôn ngữ một cách nhất quán.
 * Chuẩn hóa ký tự (Normalization): Là quá trình chuyển đổi một chuỗi ký tự về một dạng biểu diễn chuẩn tắc. Trong Unicode, một ký tự có dấu (ví dụ ệ) có thể được biểu diễn bằng 2 cách: dạng tổ hợp (một code point duy nhất) hoặc dạng phân rã (ký tự e + dấu ^ + dấu .). Chuẩn hóa đảm bảo rằng hai chuỗi trông giống hệt nhau sẽ thực sự bằng nhau khi so sánh, giúp cho việc tìm kiếm, sắp xếp hoạt động chính xác.
b. Phân biệt ASCII và UTF-8 bằng ví dụ.
 * ASCII (American Standard Code for Information Interchange):
   * Dùng 7 bit, chỉ biểu diễn được 128 ký tự.
   * Chỉ bao gồm các chữ cái Latin không dấu, chữ số, và các ký tự điều khiển cơ bản. Không thể biểu diễn tiếng Việt có dấu.
   * Mỗi ký tự chiếm đúng 1 byte.
 * UTF-8 (Unicode Transformation Format - 8-bit):
   * Là một cách mã hóa cho bộ ký tự Unicode, có thể biểu diễn mọi ký tự trên thế giới.
   * Sử dụng bộ mã hóa có độ dài thay đổi: từ 1 đến 4 byte cho mỗi ký tự.
   * Tương thích ngược hoàn toàn với ASCII (128 ký tự đầu tiên của ASCII và UTF-8 có cùng mã).
 * Ví dụ:
   * Ký tự A:
     * Trong ASCII: 01000001 (1 byte)
     * Trong UTF-8: 01000001 (1 byte) -> Giống hệt ASCII.
   * Ký tự â:
     * Trong ASCII: Không tồn tại.
     * Trong UTF-8: 11000011 10100011 (2 byte).
Câu 3 (1 điểm)
a. Mô tả nguyên lý lấy mẫu và lượng tử hóa trong âm thanh số.
 * Lấy mẫu (Sampling): Là quá trình chuyển đổi tín hiệu âm thanh tương tự (liên tục theo thời gian) thành một chuỗi các giá trị rời rạc. Quá trình này thực hiện bằng cách "đo" giá trị biên độ của sóng âm tại những khoảng thời gian đều đặn. Tần suất của các lần đo này được gọi là tần số lấy mẫu (Sample Rate).
 * Lượng tử hóa (Quantization): Sau khi lấy mẫu, mỗi giá trị biên độ đo được (vẫn là giá trị tương tự) sẽ được làm tròn và gán cho một giá trị số nguyên gần nhất trong một thang đo có hữu hạn mức. Số lượng mức trong thang đo này được quyết định bởi độ sâu bit (Bit Depth).
b. Giải thích mối quan hệ giữa Sample Rate, Bit Depth và chất lượng âm thanh.
Sample Rate và Bit Depth là hai thông số quyết định trực tiếp đến chất lượng âm thanh số và dung lượng file:
 * Sample Rate (Tần số lấy mẫu): Quyết định dải tần số của âm thanh. Sample rate càng cao, khả năng tái tạo các âm thanh có tần số cao (âm treble, tiếng leng keng) càng chính xác. Nếu sample rate quá thấp, các âm thanh tần số cao sẽ bị mất.
 * Bit Depth (Độ sâu bit): Quyết định dải động (sự khác biệt giữa âm thanh to nhất và nhỏ nhất) và độ chi tiết của âm thanh. Bit depth càng cao, số mức lượng tử hóa càng nhiều, âm thanh được ghi lại càng chính xác, mượt mà và ít nhiễu hơn.
Kết luận: Âm thanh có Sample Rate cao hơn và Bit Depth lớn hơn sẽ có chất lượng cao hơn, trung thực hơn nhưng cũng chiếm dung lượng lưu trữ lớn hơn.
Câu 4 (0.5 điểm)
a. Trình bày vai trò của hệ điều hành trong xử lý đa phương tiện.
Hệ điều hành (OS) đóng vai trò nền tảng, điều phối và hỗ trợ các ứng dụng đa phương tiện thông qua các chức năng chính:
 * Quản lý tài nguyên: Phân bổ và quản lý CPU, RAM, GPU để các tác vụ xử lý video, audio được thực thi hiệu quả.
 * Lập lịch thời gian thực (Real-time Scheduling): Ưu tiên các tiến trình xử lý media để đảm bảo âm thanh, video phát liên tục, không bị giật, lag.
 * Cung cấp Driver: Cung cấp trình điều khiển để ứng dụng có thể giao tiếp và khai thác sức mạnh của phần cứng chuyên dụng như card đồ họa, card âm thanh.
 * Cung cấp API: Cung cấp các bộ thư viện (API) giúp lập trình viên dễ dàng xây dựng các ứng dụng đa phương tiện mà không cần làm việc trực tiếp với phần cứng.
b. Nêu 2 công nghệ hoặc API tiêu biểu hỗ trợ âm thanh/đồ họa trên Windows, Linux hoặc macOS.
 * Windows: DirectX (API đồ họa, âm thanh, game), Media Foundation (framework xử lý media).
 * macOS: Metal (API đồ họa), Core Audio (API âm thanh).
 * Linux: OpenGL/Vulkan (API đồ họa), ALSA/PulseAudio (hệ thống âm thanh), GStreamer (framework media).
PHẦN B – THỰC HÀNH PYTHON (6 điểm)
Lưu ý: Để chạy các đoạn mã, cần cài đặt các thư viện:
pip install numpy Pillow matplotlib scipy psutil
Câu 5 (1.5 điểm) – Xử lý văn bản Unicode
import unicodedata

# 1. Nhập vào một chuỗi có dấu tiếng Việt
input_string = "Trường Đại học Công nghệ Thông tin"
print(f"Chuỗi gốc: {input_string}")

# Mở file để ghi kết quả
with open("unicode_report.txt", "w", encoding="utf-8") as f:
    f.write(f"Phân tích chuỗi: '{input_string}'\n")
    f.write("="*30 + "\n\n")

    # 2. In ra mã Unicode của từng ký tự
    f.write("1. Mã Unicode (Code Point) của từng ký tự:\n")
    print("\n1. Mã Unicode (Code Point) của từng ký tự:")
    for char in input_string:
        unicode_code = f"U+{ord(char):04X}"
        print(f"'{char}' -> {unicode_code}")
        f.write(f"'{char}' -> {unicode_code}\n")

    # 3. Thực hiện chuẩn hóa chuỗi theo NFC và NFD, so sánh độ dài
    print("\n2. Chuẩn hóa và so sánh độ dài:")
    f.write("\n2. Chuẩn hóa và so sánh độ dài:\n")

    # NFC
    nfc_string = unicodedata.normalize('NFC', input_string)
    print(f"Dạng NFC: '{nfc_string}' - Độ dài: {len(nfc_string)}")
    f.write(f"Dạng NFC: '{nfc_string}' - Độ dài: {len(nfc_string)}\n")

    # NFD
    nfd_string = unicodedata.normalize('NFD', input_string)
    print(f"Dạng NFD: '{nfd_string}' - Độ dài: {len(nfd_string)}")
    f.write(f"Dạng NFD: '{nfd_string}' - Độ dài: {len(nfd_string)}\n")

    # So sánh
    if len(nfd_string) > len(nfc_string):
        comparison = "Độ dài chuỗi NFD lớn hơn NFC vì NFD tách ký tự thành ký tự cơ sở và dấu."
        print(comparison)
        f.write(comparison + "\n")

print("\nĐã ghi kết quả vào file 'unicode_report.txt'")

Câu 6 (1.5 điểm) – Xử lý ảnh
(Yêu cầu có file flower.jpg trong cùng thư mục)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

try:
    # 1. Đọc tệp ảnh flower.jpg
    img = Image.open('flower.jpg')

    # 2. In kích thước, số kênh màu, giá trị trung bình độ sáng
    width, height = img.size
    img_array = np.array(img)
    num_channels = img_array.shape[2] if len(img_array.shape) == 3 else 1
    
    # Tính độ sáng trung bình (average of pixel values)
    # Chuyển sang ảnh xám trước để tính độ sáng cho ảnh màu
    mean_brightness = np.array(img.convert('L')).mean()

    print(f"Kích thước ảnh: {width} × {height} pixels")
    print(f"Số kênh màu: {num_channels}")
    print(f"Giá trị độ sáng trung bình: {mean_brightness:.2f}")

    # 3. Chuyển sang grayscale và lưu thành flower_gray.png
    gray_img = img.convert('L')
    gray_img.save('flower_gray.png')
    print("Đã chuyển ảnh sang grayscale và lưu thành 'flower_gray.png'")

    # 4. Hiển thị song song ảnh gốc và ảnh grayscale
    plt.figure(figsize=(10, 5))

    # Ảnh gốc
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Ảnh gốc (Original)')
    plt.axis('off')

    # Ảnh grayscale
    plt.subplot(1, 2, 2)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Ảnh Grayscale')
    plt.axis('off')

    plt.suptitle('So sánh ảnh gốc và ảnh Grayscale')
    plt.show()

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'flower.jpg'. Vui lòng đặt file vào cùng thư mục.")

Câu 7 (1.5 điểm) – Xử lý âm thanh
(Yêu cầu có file sample.wav trong cùng thư mục)
from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt

try:
    # 1. Đọc file sample.wav
    fs, data = read('sample.wav')

    # 2. In ra tần số lấy mẫu và thời lượng
    duration = len(data) / fs
    print(f"Tần số lấy mẫu (Sample Rate): {fs} Hz")
    print(f"Thời lượng (Duration): {duration:.2f} giây")

    # 3. Vẽ biểu đồ sóng âm cho 3000 mẫu đầu tiên
    plt.figure(figsize=(12, 4))
    plt.plot(data[:3000])
    plt.title('Biểu đồ sóng âm (3000 mẫu đầu tiên)')
    plt.xlabel('Mẫu (Sample)')
    plt.ylabel('Biên độ (Amplitude)')
    plt.grid(True)
    plt.show()

    # 4. Chuẩn hóa âm thanh về [-1,1] và lưu thành sample_norm.wav
    # Chuyển dữ liệu sang kiểu float để tính toán
    audio_float = data.astype(np.float32)
    
    # Tìm giá trị biên độ lớn nhất
    max_amp = np.max(np.abs(audio_float))
    if max_amp > 0:
        normalized_data = audio_float / max_amp
    else:
        normalized_data = audio_float # Tránh chia cho 0

    write('sample_norm.wav', fs, normalized_data)
    print("Đã chuẩn hóa âm thanh và lưu thành công file 'sample_norm.wav'")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'sample.wav'. Vui lòng đặt file vào cùng thư mục.")

Câu 8 (1.5 điểm) – Hệ điều hành và mạng
import platform
import psutil
import subprocess
import os

# Mở file để ghi báo cáo
with open("system_report.txt", "w", encoding="utf-8") as f:
    f.write("Báo cáo hệ thống và mạng\n")
    f.write("="*30 + "\n\n")

    # 1. In ra thông tin hệ điều hành và phần cứng
    print("--- Thông tin hệ thống ---")
    f.write("--- Thông tin hệ thống ---\n")

    os_name = f"Hệ điều hành: {platform.system()} {platform.release()}"
    cpu_cores = f"Số lõi CPU: {psutil.cpu_count(logical=True)}"
    total_ram = f"Dung lượng RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB"

    print(os_name)
    print(cpu_cores)
    print(total_ram)
    
    f.write(os_name + "\n")
    f.write(cpu_cores + "\n")
    f.write(total_ram + "\n\n")

    # 2. Kiểm tra kết nối mạng đến www.google.com bằng ping
    print("\n--- Kiểm tra kết nối mạng ---")
    f.write("--- Kiểm tra kết nối mạng ---\n")
    hostname = "www.google.com"
    
    # Lệnh ping khác nhau tùy hệ điều hành
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', hostname]
    
    print(f"Đang ping đến {hostname}...")
    
    try:
        # Chạy lệnh và ẩn output trên console
        result = subprocess.run(command, capture_output=True, text=True, timeout=5)
        
        # 3. Nếu ping thành công, ghi kết quả
        if result.returncode == 0:
            message = "Kết nối mạng OK"
            print(message)
            f.write(message + "\n")
            # In ra output của lệnh ping để xem
            print(result.stdout)
        else:
            message = f"Kết nối mạng thất bại. Lỗi: {result.stderr}"
            print(message)
            f.write(message + "\n")
            
    except subprocess.TimeoutExpired:
        message = "Ping timed out. Không thể kết nối."
        print(message)
        f.write(message + "\n")
    except FileNotFoundError:
        message = "Lỗi: Lệnh 'ping' không tồn tại trên hệ thống này."
        print(message)
        f.write(message + "\n")

print("\nĐã ghi báo cáo vào file 'system_report.txt'")




# -*- coding: utf-8 -*-

