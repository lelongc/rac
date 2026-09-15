import fitz
from PIL import Image
import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
doc_rc = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - READING.pdf"))

# Test 2 Page 2 is global page index 30 (0-indexed 30, which is page 31 in 1-indexed, or page 2 of Test 2)
# Test 2 is pages 29 to 57.
# Test 2 Page 1 is index 29 (Cover).
# Test 2 Page 2 is index 30 (Part 5 Q101-115).
pix = doc_rc[30].get_pixmap(dpi=150)
im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

w, h = im.size
print(f"Page 2 size: {w}x{h}")

# Column 1: left half (with margin)
# Column 2: right half (with margin)
left_col = im.crop((50, 100, int(w * 0.52), h - 80))
right_col = im.crop((int(w * 0.48), 100, w - 50, h - 80))

left_path = os.path.join(BASE_DIR, "scratch", "t2_p2_left.png")
right_path = os.path.join(BASE_DIR, "scratch", "t2_p2_right.png")

left_col.save(left_path)
right_col.save(right_path)

# Run ocr.ps1 on left and right
def run_ocr(img_path):
    cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", img_path]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return res.stdout

txt_left = run_ocr(left_path)
txt_right = run_ocr(right_path)

print("=== LEFT COLUMN OCR ===")
print(txt_left[:1200])

print("\n=== RIGHT COLUMN OCR ===")
print(txt_right[:1200])
