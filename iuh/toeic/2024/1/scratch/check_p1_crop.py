import fitz
from PIL import Image

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\ETS 2024 - LISTENING.pdf")
# Test 2 Page 2 is index 14
pix = doc[14].get_pixmap(dpi=150)
im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

print(f"Test 2 Page 2 size: {im.size}")
# Crop Q1 and Q2 with generous box
q1 = im.crop((115, 140, 1085, 810))
q2 = im.crop((115, 880, 1085, 1550))
q1.save(r"d:\folder\rac\iuh\toeic\2024\1\scratch\check_t2_q1.png")
q2.save(r"d:\folder\rac\iuh\toeic\2024\1\scratch\check_t2_q2.png")
print("Saved scratch/check_t2_q1.png and q2.png")
