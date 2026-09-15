import fitz
from PIL import Image

doc_rc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\ETS 2024 - READING.pdf")
pix = doc_rc[30].get_pixmap(dpi=300) # double DPI to 300 for maximum clarity
im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
# Crop around Q101 options at 300 dpi
# At 300 dpi, dimensions are doubled
q101_c = im.crop((100, 1300, 1200, 1750))
q101_c.save(r"d:\folder\rac\iuh\toeic\2024\1\scratch\q101_300dpi.png")

import subprocess
cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", r"d:\folder\rac\iuh\toeic\2024\1\scratch\q101_300dpi.png"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print("300 DPI OCR:")
print(res.stdout)
