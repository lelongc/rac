import fitz
from PIL import Image

doc_lc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\ETS 2024 - LISTENING.pdf")

# In Test 2, start page is (2-1)*13 = 13
# Page 9 of Test 2 is index 13 + 8 = 21 (page 22)
# Page 13 of Test 2 is index 13 + 12 = 25 (page 26)

pix_p9 = doc_lc[21].get_pixmap(dpi=150)
im_p9 = Image.frombytes("RGB", [pix_p9.width, pix_p9.height], pix_p9.samples)
im_p9.save(r"d:\folder\rac\iuh\toeic\2024\1\scratch\t2_lc_p9.png")
print(f"Test 2 LC Page 9 saved: size={im_p9.size}")

pix_p13 = doc_lc[25].get_pixmap(dpi=150)
im_p13 = Image.frombytes("RGB", [pix_p13.width, pix_p13.height], pix_p13.samples)
im_p13.save(r"d:\folder\rac\iuh\toeic\2024\1\scratch\t2_lc_p13.png")
print(f"Test 2 LC Page 13 saved: size={im_p13.size}")
