# -*- coding: utf-8 -*-
"""
Module 2 — Luminance & Chrominance (YUV, YCrCb). YIQ discussed in comments.
Spyder usage: set IMAGE_PATH and press F5.
"""
from utils_media import check_cv2, imread_rgb, to_bgr, show
import cv2

# ---------- CONFIG ----------
IMAGE_PATH = "sample.jpg"
# ----------------------------

def main():
    check_cv2()
    img = imread_rgb(IMAGE_PATH)
    bgr = to_bgr(img)

    yuv = cv2.cvtColor(bgr, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(yuv)
    show("Y (Luminance, YUV)", y, cmap="gray")
    show("U (Chrominance)", u, cmap="gray")
    show("V (Chrominance)", v, cmap="gray")

    ycrcb = cv2.cvtColor(bgr, cv2.COLOR_BGR2YCrCb)
    Y, Cr, Cb = cv2.split(ycrcb)
    show("Y (Luminance, YCrCb)", Y, cmap="gray")
    show("Cr (Chrominance)", Cr, cmap="gray")
    show("Cb (Chrominance)", Cb, cmap="gray")

    # Note: YIQ is historical (NTSC). OpenCV focuses on YUV/YCrCb.
    print("[M2] Done.")

if __name__ == "__main__":
    main()
