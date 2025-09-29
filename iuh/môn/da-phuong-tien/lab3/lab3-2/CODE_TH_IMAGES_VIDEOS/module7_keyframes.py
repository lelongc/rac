# -*- coding: utf-8 -*-
"""
Module 7 — Digital Video: Keyframe extraction (histogram difference).
Spyder: set VIDEO_PATH, OUT_DIR and press F5.
"""
from utils_media import check_cv2, ensure_file, ensure_dir
import cv2, os
import numpy as np

# ---------- CONFIG ----------
VIDEO_PATH = "sample.mp4"
OUT_DIR = "outputs_keyframes"
THRESHOLD = 0.7   # Bhattacharyya distance; higher -> fewer keyframes
EVERY_N = 1       # process every Nth frame
# ----------------------------

def frame_histogram(frame_bgr, bins=32):
    parts = []
    for ch in range(3):
        h = cv2.calcHist([frame_bgr], [ch], None, [bins], [0,256])
        h = cv2.normalize(h, None).flatten()
        parts.append(h)
    return np.concatenate(parts)

def main():
    check_cv2()
    ensure_file(VIDEO_PATH); ensure_dir(OUT_DIR)
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print(f"[M7] Failed to open: {VIDEO_PATH}"); return
    ok, prev = cap.read()
    if not ok: print("[M7] Empty video."); return
    prev_hist = frame_histogram(prev)
    idx = 0; saved = 0
    while True:
        ok, frame = cap.read()
        if not ok: break
        if idx % EVERY_N == 0:
            hist = frame_histogram(frame)
            diff = cv2.compareHist(prev_hist.astype(np.float32), hist.astype(np.float32), cv2.HISTCMP_BHATTACHARYYA)
            if diff > THRESHOLD:
                out = os.path.join(OUT_DIR, f"keyframe_{idx:06d}.png")
                cv2.imwrite(out, frame); saved += 1; prev_hist = hist
        idx += 1
    cap.release()
    print(f"[M7] Saved {saved} keyframes to: {OUT_DIR}")

if __name__ == "__main__":
    main()
