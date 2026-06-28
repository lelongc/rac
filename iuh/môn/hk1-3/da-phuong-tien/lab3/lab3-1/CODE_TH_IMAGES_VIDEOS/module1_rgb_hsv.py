# -*- coding: utf-8 -*-
"""
Module 1 — Light & Color Models (RGB, HSV/HSB)
Spyder usage: set IMAGE_PATH below and press F5.
"""
# -*- coding: utf-8 -*-
"""
Module 1 — Light & Color Models (RGB, HSV/HSB)
Spyder usage: set IMAGE_PATH below and press F5.
"""

# HSV thuận tiện hơn RGB khi phân đoạn ảnh theo màu sắc vì:

# - Kênh Hue (H) biểu diễn màu sắc: Trong HSV, thông tin về màu sắc được tách riêng ở kênh H, giúp dễ dàng chọn hoặc phân đoạn các vùng có màu giống nhau mà ít bị ảnh hưởng bởi độ sáng (Value) hoặc độ bão hòa (Saturation).
# - Giảm ảnh hưởng của ánh sáng: RGB bị ảnh hưởng mạnh bởi thay đổi ánh sáng, còn HSV cho phép chỉ tập trung vào màu (H), bỏ qua các thay đổi về sáng/tối (V).
# - Dễ xác định ngưỡng màu: Việc đặt ngưỡng để chọn màu trong HSV trực quan và hiệu quả hơn, ví dụ chỉ cần xét giá trị H nằm trong khoảng mong muốn.

# Tóm lại: HSV giúp phân đoạn màu sắc chính xác, ổn định hơn so với RGB.

from utils_media import check_cv2, imread_rgb, to_bgr, show
import cv2

# ---------- CONFIG ----------
IMAGE_PATH = "sample.jpg"   # <- Đường dẫn đến ảnh cần xử lý
# ----------------------------

def main():
    check_cv2()  # Kiểm tra xem thư viện OpenCV đã cài đặt chưa

    # Đọc ảnh màu theo định dạng RGB
    img = imread_rgb(IMAGE_PATH)
    show("Original (RGB)", img)  # Hiển thị ảnh gốc (RGB)

    # Chuyển ảnh RGB sang BGR (do OpenCV dùng BGR), sau đó chuyển sang không gian màu HSV
    hsv = cv2.cvtColor(to_bgr(img), cv2.COLOR_BGR2HSV)

    # Tách các kênh H (Hue), S (Saturation), V (Value) từ ảnh HSV
    h, s, v = cv2.split(hsv)
    show("Hue (H)", h, cmap="gray")           # Hiển thị kênh Hue (màu sắc)
    show("Saturation (S)", s, cmap="gray")    # Hiển thị kênh Saturation (độ bão hòa)
    show("Value (V)", v, cmap="gray")         # Hiển thị kênh Value (độ sáng)

    # Chuyển ảnh HSV về lại BGR, sau đó về lại RGB để hiển thị
    recon_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    recon_rgb = cv2.cvtColor(recon_rgb, cv2.COLOR_BGR2RGB)
    show("Reconstructed RGB from HSV", recon_rgb)  # Hiển thị ảnh RGB tái tạo từ HSV

    print("[M1] Done.")  # Thông báo hoàn thành

if __name__ == "__main__":
    main()



