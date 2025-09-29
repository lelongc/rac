# Phần A – Lý thuyết (3 điểm)
# Câu 1 (1 điểm)
# a)	Unicode là gì? Unicode giải quyết vấn đề gì so với các bảng mã cũ như ASCII, TCVN3?
# b) Trình bày sự khác nhau giữa UTF-8, UTF-16 và UTF-32.

### a) Unicode là gì? Unicode giải quyết vấn đề gì so với các bảng mã cũ như ASCII, TCVN3?

# - **Unicode** là một tiêu chuẩn mã hóa ký tự toàn cầu, cho phép biểu diễn hầu hết các ký tự của tất cả các ngôn ngữ trên thế giới bằng một hệ thống duy nhất.
# - **Vấn đề của bảng mã cũ**:
#   - **ASCII** chỉ mã hóa được 128 ký tự (chủ yếu là tiếng Anh).
#   - **TCVN3** và các bảng mã khác chỉ hỗ trợ một số ngôn ngữ, không tương thích với nhau, gây lỗi hiển thị khi trao đổi dữ liệu.
# - **Unicode** giải quyết vấn đề này bằng cách:
#   - Cung cấp mã duy nhất cho mỗi ký tự, không phụ thuộc nền tảng, ngôn ngữ hay chương trình.
#   - Hỗ trợ đa ngôn ngữ, giúp trao đổi dữ liệu dễ dàng và nhất quán.

# ---

### b) Sự khác nhau giữa UTF-8, UTF-16 và UTF-32

# - **UTF-8**:
#   - Mã hóa mỗi ký tự bằng 1 đến 4 byte.
#   - Tương thích với ASCII (ký tự tiếng Anh chỉ dùng 1 byte).
#   - Tiết kiệm dung lượng cho văn bản chủ yếu là tiếng Anh.
# - **UTF-16**:
#   - Mã hóa mỗi ký tự bằng 2 hoặc 4 byte.
#   - Phù hợp với các ngôn ngữ có nhiều ký tự đặc biệt (như tiếng Trung, Nhật).
# - **UTF-32**:
#   - Mỗi ký tự luôn dùng 4 byte.
#   - Đơn giản khi xử lý, nhưng tốn bộ nhớ hơn.
# - **Tóm lại**: UTF-8 tiết kiệm dung lượng nhất cho văn bản tiếng Anh, UTF-16 cân bằng giữa dung lượng và hỗ trợ ký tự, UTF-32 đơn giản nhưng tốn nhiều bộ nhớ.

# ________________________________________
# Câu 2 (1 điểm)
# Cho các ký tự sau:
# •	"A"
# •	"Â"
# •	"🙂"
# Hãy viết code point của từng ký tự theo dạng U+xxxx.

# Kết quả:
# "A"   : U+0041
# "Â"   : U+00C2
# "🙂"  : U+1F642

# Câu 3 (1 điểm)
# Tại sao cùng một chữ cái có dấu (ví dụ: "ấ") nhưng trong Python khi so sánh có thể ra False? Hãy giải thích và nêu cách xử lý.

# Giải thích:
# - Một ký tự có dấu như "ấ" có thể được biểu diễn theo nhiều cách trong Unicode:
#   - Dạng tổ hợp: ký tự "a" + dấu mũ (̂) + dấu sắc (́).
#   - Dạng dựng sẵn: một mã Unicode duy nhất cho "ấ".
# - Khi so sánh, Python so sánh từng mã Unicode nên hai cách biểu diễn khác nhau sẽ cho kết quả False.

# Cách xử lý:
# - Chuẩn hóa chuỗi về cùng một dạng (NFC hoặc NFD) trước khi so sánh, dùng unicodedata.normalize.

# import unicodedata

# a1 = "ấ"  # dạng dựng sẵn
# a2 = "a\u0302\u0301"  # dạng tổ hợp: a + ̂ + ́

# print(a1 == a2)  # False

# # Chuẩn hóa về dạng NFC
# print(unicodedata.normalize('NFC', a1) == unicodedata.normalize('NFC', a2))
# Phần B – Lập trình (7 điểm)
# Phần B – Lập trình (7 điểm)
# Câu 4 (3 điểm)
# Viết chương trình Python:
# 1. Nhập vào một chuỗi từ bàn phím (có thể chứa tiếng Việt và emoji).
# 2. In ra số ký tự (len) và số byte khi encode theo UTF-8, UTF-16, UTF-32.
# 3. In ra bảng gồm: ký tự, mã Unicode (U+xxxx), tên ký tự.

# import unicodedata

# s = input("Nhập chuỗi: ")

# print("Số ký tự:", len(s))
# print("Số byte UTF-8 :", len(s.encode('utf-8')))
# print("Số byte UTF-16:", len(s.encode('utf-16')))
# print("Số byte UTF-32:", len(s.encode('utf-32')))

# print("\nBảng ký tự:")
# print("{:<5} {:<10} {}".format("Ký tự", "Mã Unicode", "Tên ký tự"))
# for c in s:
#     code = f"U+{ord(c):04X}"
#     try:
#         name = unicodedata.name(c)
#     except ValueError:
#         name = "Không xác định"
#     print("{:<5} {:<10} {}".format(c, code, name))

# Câu 5 (4 điểm)
# Cho file input.txt có nội dung chứa tiếng Việt và ký tự đặc biệt (ví dụ: "Trường học Việt Nam 🏫🇻🇳").
# Yêu cầu:
# 1. Đọc file theo UTF-8. Nếu lỗi thì thử UTF-16, UTF-32.
# 2. Chuẩn hóa toàn bộ chuỗi sang NFC.
# 3. Đếm số chữ cái tiếng Việt có dấu (à, á, ă, â, ê, ô, ơ, ư,…).
# 4. Ghi kết quả ra file output.txt theo UTF-8.

import unicodedata
import os

viet_dau = "àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ" \
           "ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ"

# Đảm bảo luôn lấy đường dẫn file txt cùng thư mục với file .py
base_dir = os.getcwd()
input_path = os.path.join(base_dir, 'input.txt')
output_path = os.path.join(base_dir, 'output.txt')

def read_file_try_encodings(filename):
    encodings = ['utf-8', 'utf-16', 'utf-32']
    for enc in encodings:
        try:
            with open(filename, encoding=enc) as f:
                return f.read()
        except Exception:
            continue
    raise Exception("Không đọc được file với các encoding thông dụng.")

# 1. Đọc file với các encoding
try:
    text = read_file_try_encodings(input_path)
except Exception as e:
    text = ""
    print(e)

# 2. Chuẩn hóa về NFC
text_nfc = unicodedata.normalize('NFC', text)

# 3. Đếm số chữ cái tiếng Việt có dấu
count = sum(1 for c in text_nfc if c in viet_dau)

# 4. Ghi kết quả ra file output.txt
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("Nội dung sau chuẩn hóa NFC:\n")
    f.write(text_nfc + "\n")
    f.write(f"Số chữ cái tiếng Việt có dấu: {count}\n")