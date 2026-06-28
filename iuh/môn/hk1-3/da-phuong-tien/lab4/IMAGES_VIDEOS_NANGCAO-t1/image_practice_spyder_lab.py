# -*- coding: utf-8 -*-
"""
BÀI THỰC HÀNH XỬ LÝ ẢNH (Spyder / Python)
========================================

Mục tiêu
--------
1) Tạo ảnh xám 128×128, thao tác các mức cường độ (0..255) và hiển thị kết quả.
2) Thực hiện các biến đổi hình học cơ bản: lật, xoay, tịnh tiến, phóng/thu, nghiêng (shear).
3) Tách ảnh RGB thành 3 kênh R, G, B và hiển thị riêng.
(Phần mở rộng – tùy chọn): Nâng cấp bằng equalize histogram, CLAHE, hoặc chuỗi biến đổi.

Gợi ý chạy trên Spyder
----------------------
- Mở file này trong Spyder, nhấn Run (F5). Mỗi phần có thể chạy độc lập.
- Kết quả sẽ hiện ở "Plots" hoặc cửa sổ đồ thị. Ảnh xuất ra thư mục ./outputs_lab.
- Bạn có thể thay ảnh RGB mẫu bằng ảnh của bạn (chỉnh biến `RGB_INPUT` trong phần cấu hình).

Thư viện dùng
-------------
- NumPy, PIL (Pillow), Matplotlib.
"""

import os, math
from pathlib import Path
import numpy as np
from PIL import Image, ImageOps, ImageEnhance
import matplotlib.pyplot as plt

OUT_DIR = Path("./outputs_lab")
OUT_DIR.mkdir(exist_ok=True)

RGB_INPUT = None  # ví dụ: r"D:/my_photos/cat.png" (để None sẽ dùng ảnh tổng hợp)

def show_img(title, img):
    plt.figure(figsize=(4,4))
    if isinstance(img, Image.Image):
        if img.mode == 'L':
            plt.imshow(img, cmap='gray')
        else:
            plt.imshow(img)
    else:
        if img.ndim == 2:
            plt.imshow(img, cmap='gray')
        else:
            plt.imshow(img)
    plt.title(title); plt.axis('off'); plt.tight_layout(); plt.show()

def save_img(path, img):
    if isinstance(img, Image.Image):
        img.save(path)
    else:
        arr = np.asarray(img)
        if arr.dtype != np.uint8:
            arr = np.clip(arr, 0, 255)
            if arr.max() <= 1.0:
                arr = (arr * 255.0).round()
            arr = arr.astype(np.uint8)
        Image.fromarray(arr).save(path)

def make_sample_rgb(w=256, h=256):
    x = np.linspace(0, 1, w, dtype=np.float32)
    y = np.linspace(0, 1, h, dtype=np.float32)
    X, Y = np.meshgrid(x, y)
    R = (X*255).astype(np.uint8)
    G = (Y*255).astype(np.uint8)
    B = ((1 - 0.5*X - 0.5*Y)*255).clip(0,255).astype(np.uint8)
    rgb = np.stack([R,G,B], axis=-1)
    img = Image.fromarray(rgb, mode="RGB")
    from PIL import ImageDraw
    dr = ImageDraw.Draw(img)
    dr.rectangle([20,20,120,90], outline="white", width=3)
    dr.ellipse([150,50,230,130], outline="yellow", width=3)
    dr.line([0,h//2,w,h//2], fill="black", width=2)
    return img

def task1_gray_and_intensity():
    print("\n[Task 1] Ảnh xám 128×128 & biến đổi cường độ")
    h = w = 128
    x = np.linspace(0, 255, w, dtype=np.float32)
    grad = np.tile(x, (h,1))
    img_gray = Image.fromarray(grad.astype(np.uint8), mode='L')
    save_img(OUT_DIR/'t1_gray.png', img_gray); show_img("T1 - Gray 128×128", img_gray)

    neg = ImageOps.invert(img_gray)
    save_img(OUT_DIR/'t1_negative.png', neg); show_img("T1 - Negative", neg)

    T = 128
    thr = (np.array(img_gray) > T).astype(np.uint8) * 255
    thr = Image.fromarray(thr, mode='L')
    save_img(OUT_DIR/'t1_threshold_T128.png', thr); show_img("T1 - Threshold (T=128)", thr)

    lo, hi = 50.0, 200.0
    arr = np.array(img_gray, dtype=np.float32)
    stretched = ((arr - lo) / (hi - lo) * 255.0)
    stretched = np.clip(stretched, 0, 255).astype(np.uint8)
    stretched = Image.fromarray(stretched, mode='L')
    save_img(OUT_DIR/'t1_contrast_stretch.png', stretched)
    show_img("T1 - Contrast Stretch [50..200]→[0..255]", stretched)

    def gamma_corr(imgL: Image.Image, gamma: float):
        a = np.array(imgL, dtype=np.float32)/255.0
        b = np.power(a, gamma) * 255.0
        return Image.fromarray(b.clip(0,255).astype(np.uint8), mode='L')
    gamma06 = gamma_corr(img_gray, 0.6)
    gamma16 = gamma_corr(img_gray, 1.6)
    save_img(OUT_DIR/'t1_gamma_0p6.png', gamma06); show_img("T1 - Gamma 0.6", gamma06)
    save_img(OUT_DIR/'t1_gamma_1p6.png', gamma16); show_img("T1 - Gamma 1.6", gamma16)

def affine_translate(img: Image.Image, tx=20, ty=10):
    return img.transform(img.size, Image.AFFINE, (1,0,tx, 0,1,ty), resample=Image.BICUBIC, fillcolor=(0,0,0))

def affine_scale_keep_canvas(img: Image.Image, sx=1.2, sy=1.2):
    inv = (1/sx, 0, 0, 0, 1/sy, 0)
    return img.transform(img.size, Image.AFFINE, inv, resample=Image.BICUBIC)

def affine_shear(img: Image.Image, shear_x=0.3, shear_y=0.0):
    return img.transform(img.size, Image.AFFINE, (1.0, shear_x, 0.0, shear_y, 1.0, 0.0), resample=Image.BICUBIC)

def task2_geom_transforms():
    print("\n[Task 2] Biến đổi hình học")
    if RGB_INPUT and Path(RGB_INPUT).exists():
        img = Image.open(RGB_INPUT).convert('RGB')
    else:
        img = make_sample_rgb(256, 256)
    save_img(OUT_DIR/'t2_input.png', img); show_img("T2 - Ảnh gốc (RGB)", img)

    hflip = ImageOps.mirror(img); save_img(OUT_DIR/'t2_hflip.png', hflip); show_img("T2 - Lật ngang", hflip)
    vflip = ImageOps.flip(img);   save_img(OUT_DIR/'t2_vflip.png', vflip); show_img("T2 - Lật dọc", vflip)

    rot90 = img.rotate(90, expand=True); save_img(OUT_DIR/'t2_rot90.png', rot90); show_img("T2 - Xoay 90°", rot90)
    rot30 = img.rotate(30, resample=Image.BICUBIC, expand=True); save_img(OUT_DIR/'t2_rot30.png', rot30); show_img("T2 - Xoay 30°", rot30)

    trans = affine_translate(img, tx=30, ty=15); save_img(OUT_DIR/'t2_translate_tx30_ty15.png', trans); show_img("T2 - Tịnh tiến (30,15)", trans)

    scaled = affine_scale_keep_canvas(img, sx=1.2, sy=1.2); save_img(OUT_DIR/'t2_scale_1p2.png', scaled); show_img("T2 - Phóng 1.2×", scaled)

    sheared = affine_shear(img, shear_x=0.3, shear_y=0.0); save_img(OUT_DIR/'t2_shear_x0p3.png', sheared); show_img("T2 - Shear x=0.3", sheared)

def task3_split_rgb():
    print("\n[Task 3] Tách ảnh RGB")
    if RGB_INPUT and Path(RGB_INPUT).exists():
        img = Image.open(RGB_INPUT).convert('RGB')
    else:
        img = make_sample_rgb(256, 256)
    save_img(OUT_DIR/'t3_input.png', img); show_img("T3 - Ảnh gốc (RGB)", img)
    r, g, b = img.split()
    save_img(OUT_DIR/'t3_R_gray.png', r); show_img("T3 - Kênh R (xám)", r)
    save_img(OUT_DIR/'t3_G_gray.png', g); show_img("T3 - Kênh G (xám)", g)
    save_img(OUT_DIR/'t3_B_gray.png', b); show_img("T3 - Kênh B (xám)", b)
    zr = Image.merge('RGB', (r, Image.new('L', r.size), Image.new('L', r.size)))
    zg = Image.merge('RGB', (Image.new('L', g.size), g, Image.new('L', g.size)))
    zb = Image.merge('RGB', (Image.new('L', b.size), Image.new('L', b.size), b))
    save_img(OUT_DIR/'t3_R_only.png', zr); show_img("T3 - Hiển thị kênh R", zr)
    save_img(OUT_DIR/'t3_G_only.png', zg); show_img("T3 - Hiển thị kênh G", zg)
    save_img(OUT_DIR/'t3_B_only.png', zb); show_img("T3 - Hiển thị kênh B", zb)

def main():
    run_task1 = True; run_task2 = True; run_task3 = True
    if run_task1: task1_gray_and_intensity()
    if run_task2: task2_geom_transforms()
    if run_task3: task3_split_rgb()
    print(f"\nHoàn tất. Ảnh đã lưu vào: {OUT_DIR.resolve()}")

if __name__ == "__main__":
    main()
