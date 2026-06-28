# -*- coding: utf-8 -*-
"""
utils_media.py — Common helpers for Image & Video Fundamentals labs (Spyder-friendly).
Place this file in the same folder as the module scripts.
"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def check_cv2():
    try:
        _ = cv2.__version__
    except Exception as e:
        raise RuntimeError(f"OpenCV import failed: {e}")

def ensure_file(path: str):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def imread_rgb(path: str) -> np.ndarray:
    ensure_file(path)
    bgr = cv2.imread(path, cv2.IMREAD_COLOR)
    if bgr is None:
        raise ValueError(f"Failed to read: {path}")
    return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

def to_bgr(img_rgb: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

def show(title: str, img: np.ndarray, cmap: str = None):
    plt.figure()
    if img.ndim == 2:
        plt.imshow(img, cmap=cmap or "gray")
    else:
        plt.imshow(img)
    plt.title(title)
    plt.axis("off")
    plt.show()

def mse(a: np.ndarray, b: np.ndarray) -> float:
    a = a.astype(np.float64); b = b.astype(np.float64)
    return np.mean((a - b) ** 2)

def psnr(a: np.ndarray, b: np.ndarray, max_val: float = 255.0) -> float:
    m = mse(a, b)
    if m == 0: return float("inf")
    import math
    return 20.0 * math.log10(max_val) - 10.0 * math.log10(m)
