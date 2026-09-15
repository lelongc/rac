# extract_all_images.py: Extract images and scan pages for Tests 3-10
import fitz
import os
import time
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_LC_PATH = os.path.join(BASE_DIR, "ETS 2024 - LISTENING.pdf")
DOC_RC_PATH = os.path.join(BASE_DIR, "ETS 2024 - READING.pdf")

doc_lc = fitz.open(DOC_LC_PATH)
doc_rc = fitz.open(DOC_RC_PATH)

for t in range(3, 11):
    t0 = time.time()
    dest_dir = os.path.join(BASE_DIR, "web", "assets", "images", f"test{t}")
    os.makedirs(dest_dir, exist_ok=True)
    
    # 1. Part 1 photos (6 questions)
    lc_start = (t - 1) * 13
    
    # Page 2: Q1, Q2
    pix2 = doc_lc[lc_start + 1].get_pixmap(dpi=150)
    im2 = Image.frombytes("RGB", [pix2.width, pix2.height], pix2.samples)
    im2.crop((115, 140, 1085, 810)).save(os.path.join(dest_dir, "q1.png"))
    im2.crop((115, 880, 1085, 1550)).save(os.path.join(dest_dir, "q2.png"))
    
    # Page 3: Q3, Q4
    pix3 = doc_lc[lc_start + 2].get_pixmap(dpi=150)
    im3 = Image.frombytes("RGB", [pix3.width, pix3.height], pix3.samples)
    im3.crop((115, 140, 1085, 810)).save(os.path.join(dest_dir, "q3.png"))
    im3.crop((115, 880, 1085, 1550)).save(os.path.join(dest_dir, "q4.png"))
    
    # Page 4: Q5, Q6
    pix4 = doc_lc[lc_start + 3].get_pixmap(dpi=150)
    im4 = Image.frombytes("RGB", [pix4.width, pix4.height], pix4.samples)
    im4.crop((115, 140, 1085, 810)).save(os.path.join(dest_dir, "q5.png"))
    im4.crop((115, 880, 1085, 1550)).save(os.path.join(dest_dir, "q6.png"))
    
    # 2. Part 3 & Part 4 graphics pages
    doc_lc[lc_start + 7].get_pixmap(dpi=150).save(os.path.join(dest_dir, "lc_page_8.png"))
    doc_lc[lc_start + 11].get_pixmap(dpi=150).save(os.path.join(dest_dir, "lc_page_12.png"))
    
    # 3. Reading booklet scan pages (29 pages)
    rc_start = (t - 1) * 29
    for p in range(29):
        doc_rc[rc_start + p].get_pixmap(dpi=150).save(os.path.join(dest_dir, f"rc_page_{p+1}.png"))
        
    t1 = time.time()
    print(f"Test {t}: Extracted 6 photos, 2 LC graphic pages, and 29 RC booklet pages in {t1 - t0:.1f}s")

print("All images extracted successfully!")
