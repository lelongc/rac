# -*- coding: utf-8 -*-
"""
Module 8 — Luma Sampling & Chroma Sub-Sampling (4:4:4, 4:2:2, 4:2:0)
Spyder: set IMAGE_PATH and MODE in {"444","422","420"}, press F5.
"""
from utils_media import check_cv2, imread_rgb, to_bgr, show
import cv2

# ---------- CONFIG ----------
IMAGE_PATH = "sample.jpg"
MODE = "420"   # choose: "444", "422", "420"
# ----------------------------

def yuv444_from_rgb(img_rgb):
    bgr = to_bgr(img_rgb)
    yuv = cv2.cvtColor(bgr, cv2.COLOR_BGR2YUV)
    return cv2.split(yuv)

def chroma_subsample(U, V, mode: str):
    h, w = U.shape[:2]
    if mode == "444":
        return U.copy(), V.copy()
    elif mode == "422":
        U_ds = cv2.resize(U, (w//2, h), interpolation=cv2.INTER_AREA)
        V_ds = cv2.resize(V, (w//2, h), interpolation=cv2.INTER_AREA)
        U_up = cv2.resize(U_ds, (w, h), interpolation=cv2.INTER_LINEAR)
        V_up = cv2.resize(V_ds, (w, h), interpolation=cv2.INTER_LINEAR)
        return U_up, V_up
    elif mode == "420":
        U_ds = cv2.resize(U, (w//2, h//2), interpolation=cv2.INTER_AREA)
        V_ds = cv2.resize(V, (w//2, h//2), interpolation=cv2.INTER_AREA)
        U_up = cv2.resize(U_ds, (w, h), interpolation=cv2.INTER_LINEAR)
        V_up = cv2.resize(V_ds, (w, h), interpolation=cv2.INTER_LINEAR)
        return U_up, V_up
    else:
        raise ValueError("MODE must be one of '444','422','420'")

def yuv_to_rgb(Y, U, V):
    yuv = cv2.merge([Y, U, V])
    bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    return rgb

def main():
    check_cv2()
    img = imread_rgb(IMAGE_PATH)
    Y, U, V = yuv444_from_rgb(img)
    U_up, V_up = chroma_subsample(U, V, MODE)
    recon = yuv_to_rgb(Y, U_up, V_up)
    show("Original RGB", img)
    show(f"Reconstructed RGB (Chroma {MODE})", recon)
    print(f"[M8] Chroma subsampling {MODE} done.")

if __name__ == "__main__":
    main()
