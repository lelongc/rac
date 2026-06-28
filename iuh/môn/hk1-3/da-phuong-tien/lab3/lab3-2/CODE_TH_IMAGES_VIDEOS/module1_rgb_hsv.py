# -*- coding: utf-8 -*-
"""
Module 1 — Light & Color Models (RGB, HSV/HSB)
Spyder usage: set IMAGE_PATH below and press F5.
"""
from utils_media import check_cv2, imread_rgb, to_bgr, show
import cv2

# ---------- CONFIG ----------
IMAGE_PATH = "sample.jpg"   # <- change to your image path
# ----------------------------

def main():
    check_cv2()
    img = imread_rgb(IMAGE_PATH)
    show("Original (RGB)", img)

    hsv = cv2.cvtColor(to_bgr(img), cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    show("Hue (H)", h, cmap="gray")
    show("Saturation (S)", s, cmap="gray")
    show("Value (V)", v, cmap="gray")

    recon_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    recon_rgb = cv2.cvtColor(recon_rgb, cv2.COLOR_BGR2RGB)
    show("Reconstructed RGB from HSV", recon_rgb)
    print("[M1] Done.")

if __name__ == "__main__":
    main()
