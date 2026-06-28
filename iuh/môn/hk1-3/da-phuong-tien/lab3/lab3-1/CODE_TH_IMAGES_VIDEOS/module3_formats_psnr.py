# -*- coding: utf-8 -*-
"""
Module 3 — Image Data Formats & PSNR (PNG vs JPEG quality)
Spyder: set IMAGE_PATH, OUT_DIR, and press F5.
"""
from utils_media import check_cv2, imread_rgb, to_bgr, show, ensure_dir, psnr
import cv2, os

# ---------- CONFIG ----------
IMAGE_PATH = "sample.jpg"
OUT_DIR = "outputs_module3"
JPEG_QUALITY = 85  # 1..100
# ----------------------------

def main():
    check_cv2()
    ensure_dir(OUT_DIR)
    img_rgb = imread_rgb(IMAGE_PATH)
    bgr = to_bgr(img_rgb)
    base = os.path.splitext(os.path.basename(IMAGE_PATH))[0]
    out_png = os.path.join(OUT_DIR, f"{base}.png")
    out_jpg_q = os.path.join(OUT_DIR, f"{base}_q{JPEG_QUALITY}.jpg")
    out_jpg_50 = os.path.join(OUT_DIR, f"{base}_q50.jpg")

    cv2.imwrite(out_png, bgr)
    cv2.imwrite(out_jpg_q, bgr, [cv2.IMWRITE_JPEG_QUALITY, int(JPEG_QUALITY)])
    cv2.imwrite(out_jpg_50, bgr, [cv2.IMWRITE_JPEG_QUALITY, 50])

    ref = cv2.cvtColor(cv2.imread(out_png), cv2.COLOR_BGR2RGB)
    test_q = cv2.cvtColor(cv2.imread(out_jpg_q), cv2.COLOR_BGR2RGB)
    test_50 = cv2.cvtColor(cv2.imread(out_jpg_50), cv2.COLOR_BGR2RGB)

    p_q = psnr(ref, test_q); p_50 = psnr(ref, test_50)

    print("[M3] Saved to:", OUT_DIR)
    print(f"  PNG (lossless) path: {out_png}")
    print(f"  JPEG q={JPEG_QUALITY}: PSNR={p_q:.2f} dB, path: {out_jpg_q}")
    print(f"  JPEG q=50:          PSNR={p_50:.2f} dB, path: {out_jpg_50}")

    show("Reference (PNG)", ref)
    show(f"JPEG (q={JPEG_QUALITY})", test_q)
    show("JPEG (q=50)", test_50)

if __name__ == "__main__":
    main()
