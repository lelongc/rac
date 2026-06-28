from PIL import Image
import numpy as np

try:
  
    img = Image.open('input.jpg')
    print(f"Đã mở ảnh 'input.jpg'")
    print(f"Kích thước (rộng x cao): {img.size}")
   

   
    gray_img = img.convert('L')
    print("\nĐã chuyển ảnh sang Grayscale.")

   
    gray_array = np.array(gray_img)
    average_gray = gray_array.mean()
    print(f"Mức xám trung bình của ảnh: {average_gray:.2f}")

    
    gray_img.save('output_gray.png')
    print("Đã lưu ảnh xám thành 'output_gray.png'")
    
   

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'input.jpg'. Hãy chắc chắn bạn có file này trong cùng thư mục.")

