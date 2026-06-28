# -*- coding: utf-8 -*-
"""
Module 4A — Video Camera Capture & Display (Webcam).
Spyder: set CAMERA_INDEX, MAX_FRAMES, press F5.
"""
from utils_media import check_cv2
import cv2

# ---------- CONFIG ----------
CAMERA_INDEX = 0
MAX_FRAMES = 300
# ----------------------------

def main():
    check_cv2()
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print("[M4A] Cannot open camera. Try a different index.")
        return
    print("[M4A] Press 'q' in the window to quit.")
    count = 0
    while True:
        ok, frame = cap.read()
        if not ok: break
        cv2.imshow("Camera", frame)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'): break
        if count >= MAX_FRAMES: break
    cap.release()
    cv2.destroyAllWindows()
    print("[M4A] Finished.")

if __name__ == "__main__":
    main()
