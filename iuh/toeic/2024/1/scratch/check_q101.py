import fitz
from PIL import Image

doc_rc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\ETS 2024 - READING.pdf")
# Crop just question 101 on page 31 (index 30)
pix = doc_rc[30].get_pixmap(dpi=150)
im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
# Q101 is near top of left column
q101_crop = im.crop((50, 400, 600, 700))
q101_crop.save(r"d:\folder\rac\iuh\toeic\2024\1\scratch\q101_crop.png")

import subprocess
cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", r"d:\folder\rac\iuh\toeic\2024\1\scratch\q101_crop.png"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print("Q101 crop OCR:")
print(res.stdout)
