
"""
Module 4B — Play a Video File frame-by-frame.
Spyder: set VIDEO_PATH, MAX_FRAMES, press F5.
"""
from utils_media import check_cv2, ensure_file
import cv2

# ---------- CONFIG ----------
VIDEO_PATH = "sample.mp4"
MAX_FRAMES = 600
# ----------------------------

def main():
    check_cv2()
    ensure_file(VIDEO_PATH)
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print(f"[M4B] Failed to open: {VIDEO_PATH}")
        return
    print("[M4B] Playing. Press 'q' to quit.")
    count = 0
    while True:
        ok, frame = cap.read()
        if not ok: break
        cv2.imshow("Video", frame)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'): break
        if count >= MAX_FRAMES: break
    cap.release()
    cv2.destroyAllWindows()
    print("[M4B] Finished.")

if __name__ == "__main__":
    main()
