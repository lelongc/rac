# -*- coding: utf-8 -*-
"""
Module 5 — Scanning & Interlaced (simulation).
Spyder: set IMAGE_PATH and press F5.
"""
from utils_media import check_cv2, imread_rgb, show
import numpy as np

# ---------- CONFIG ----------
IMAGE_PATH = "sample.jpg"
# ----------------------------

def interlace_sim(img: np.ndarray):
    h = img.shape[0]
    mask_even = np.zeros((h,), dtype=np.uint8); mask_even[0::2] = 1
    mask_odd = 1 - mask_even
    if img.ndim == 3:
        mask_even = mask_even[:, None, None]; mask_odd = mask_odd[:, None, None]
    field_even = img * mask_even
    field_odd = img * mask_odd
    return field_even, field_odd

def deinterlace_simple(field_even: np.ndarray, field_odd: np.ndarray) -> np.ndarray:
    recon = np.where(field_even != 0, field_even, field_odd)
    return recon.astype(np.uint8)

def main():
    check_cv2()
    img = imread_rgb(IMAGE_PATH)
    fe, fo = interlace_sim(img)
    show("Field (even rows)", fe.astype(np.uint8))
    show("Field (odd rows)", fo.astype(np.uint8))
    recon = deinterlace_simple(fe, fo)
    show("Deinterlaced (simple)", recon)
    print("[M5] Done.")

if __name__ == "__main__":
    main()
