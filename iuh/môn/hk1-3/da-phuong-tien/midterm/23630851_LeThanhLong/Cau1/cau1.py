import unicodedata
input_string = "Trường Đại học iuh"
print(f"Chuỗi gốc: {input_string}")


with open("unicode_info.txt", "w", encoding="utf-8") as f:
    f.write(f"Phân tích chuỗi: '{input_string}'\n")
    f.write("="*30 + "\n\n")

    
    f.write("1. Mã Unicode (Code Point) của từng ký tự:\n")
    print("\n1. Mã Unicode (Code Point) của từng ký tự:")
    for char in input_string:
        unicode_code = f"U+{ord(char):04X}"
        print(f"'{char}' -> {unicode_code}")
        f.write(f"'{char}' -> {unicode_code}\n")


    print("\n2. Chuẩn hóa và so sánh độ dài:")
    f.write("\n2. Chuẩn hóa và so sánh độ dài:\n")

 
    nfc_string = unicodedata.normalize('NFC', input_string)
    print(f"Dạng NFC: '{nfc_string}' - Độ dài: {len(nfc_string)}")
    f.write(f"Dạng NFC: '{nfc_string}' - Độ dài: {len(nfc_string)}\n")

   
    nfd_string = unicodedata.normalize('NFD', input_string)
    print(f"Dạng NFD: '{nfd_string}' - Độ dài: {len(nfd_string)}")
    f.write(f"Dạng NFD: '{nfd_string}' - Độ dài: {len(nfd_string)}\n")

    
    if len(nfd_string) > len(nfc_string):
        comparison = "Độ dài chuỗi NFD lớn hơn NFC vì NFD tách ký tự thành ký tự cơ sở và dấu."
        print(comparison)
        f.write(comparison + "\n")

print("\nĐã ghi kết quả vào file 'unicode_info.txt'")