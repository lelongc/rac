import fitz
from PIL import Image
import subprocess

doc_rc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\ETS 2024 - READING.pdf")
pix = doc_rc[30].get_pixmap(dpi=150)
im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
q101_opts = im.crop((50, 650, 600, 850))
q101_opts.save(r"d:\folder\rac\iuh\toeic\2024\1\scratch\q101_opts.png")

cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", r"d:\folder\rac\iuh\toeic\2024\1\scratch\q101_opts.png"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print("Q101 options OCR:")
print(res.stdout)
