
import os


input_file = 'sample.txt'
output_file = 'summary.txt'

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()


num_lines = len(lines)
num_words = sum(len(line.split()) for line in lines)
num_chars = sum(len(line) for line in lines)


print(f"Số dòng: {num_lines}")
print(f"Số từ: {num_words}")
print(f"Số ký tự: {num_chars}")


with open(output_file, 'w', encoding='utf-8') as f:
    f.write("KẾT QUẢ THỐNG KÊ FILE sample.txt\n")
    f.write(f"Số dòng: {num_lines}\n")
    f.write(f"Số từ: {num_words}\n")
    f.write(f"Số ký tự: {num_chars}\n")

print(f"Đã lưu kết quả vào file {output_file}")
