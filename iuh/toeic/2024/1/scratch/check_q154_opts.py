import fitz
from PIL import Image

doc = fitz.open('ETS 2024 - READING.pdf')

# Test 3 starts at page 58 (0-indexed).
# Page 12 of Test 3 is index 58 + 11 = 69
p69 = doc[69].get_pixmap(dpi=150)
p69.save('scratch/rc_t3_p12_full.png')
im = Image.open('scratch/rc_t3_p12_full.png')

# Let's crop the bottom half of the page where questions 153, 154, 155 are
w, h = im.size
q_crop = im.crop((0, int(h * 0.6), w, h))
q_crop.save('scratch/rc_t3_p12_q_area.png')

# Let's OCR q_crop using tesseract or powershell Windows.Media.Ocr
import subprocess
res = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', 'scratch/ocr_boxes.ps1', 'scratch/rc_t3_p12_q_area.png'], capture_output=True, text=True)
print("=== OCR OF Q153-155 AREA ===")
for l in res.stdout.splitlines():
    print(l)
