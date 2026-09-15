import fitz
from PIL import Image
import os

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
doc_lc = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - LISTENING.pdf"))

print("Cropping Part 3 & 4 graphics for Tests 2 to 10...")

for t in range(2, 11):
    base_p = (t - 1) * 13
    dest_dir = os.path.join(BASE_DIR, "web", "assets", "images", f"test{t}")
    os.makedirs(dest_dir, exist_ok=True)
    
    # Page 9 (index base_p + 8): Q62-64
    pix9 = doc_lc[base_p + 8].get_pixmap(dpi=150)
    im9 = Image.frombytes("RGB", [pix9.width, pix9.height], pix9.samples)
    g62 = im9.crop((580, 120, 1120, 420))
    g62.save(os.path.join(dest_dir, "graphic_q62_64.png"))
    
    # Page 10 (index base_p + 9): Q65-67 and Q68-70
    pix10 = doc_lc[base_p + 9].get_pixmap(dpi=150)
    im10 = Image.frombytes("RGB", [pix10.width, pix10.height], pix10.samples)
    g65 = im10.crop((100, 120, 600, 500))
    g65.save(os.path.join(dest_dir, "graphic_q65_67.png"))
    g68 = im10.crop((580, 120, 1120, 500))
    g68.save(os.path.join(dest_dir, "graphic_q68_70.png"))
    
    # Page 13 (index base_p + 12): Q95-97 and Q98-100
    pix13 = doc_lc[base_p + 12].get_pixmap(dpi=150)
    im13 = Image.frombytes("RGB", [pix13.width, pix13.height], pix13.samples)
    g95 = im13.crop((100, 120, 600, 500))
    g95.save(os.path.join(dest_dir, "graphic_q95_97.png"))
    g98 = im13.crop((580, 120, 1120, 500))
    g98.save(os.path.join(dest_dir, "graphic_q98_100.png"))
    
    print(f"Test {t:2d}: Successfully cropped all 5 graphics!")

print("All graphics cropped perfectly for all tests!")
