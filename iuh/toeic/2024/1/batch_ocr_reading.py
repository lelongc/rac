# batch_ocr_reading.py: Sequentially OCR reading pages for Tests 2 to 10
import fitz
import subprocess
import os
import json
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRATCH_DIR = os.path.join(BASE_DIR, "scratch")
os.makedirs(SCRATCH_DIR, exist_ok=True)
doc_rc = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - READING.pdf"))

OCR_SCRIPT = "d:/folder/rac/ocr.ps1"

for t in range(2, 11):
    cache_file = os.path.join(SCRATCH_DIR, f"ocr_rc_test{t}.json")
    if os.path.exists(cache_file):
        print(f"Test {t} RC OCR cache already exists, skipping.")
        continue
        
    t0 = time.time()
    print(f"--- Starting OCR for Test {t} Reading (pages 1 to 29) ---")
    rc_start = (t - 1) * 29
    test_pages = {}
    
    for p in range(1, 29): # Page 0 is cover, pages 1 to 28 are test content
        page_num = p + 1 # 1-indexed (e.g. page 2 to 29)
        pdf_page_idx = rc_start + p
        img_temp = os.path.join(SCRATCH_DIR, f"temp_t{t}_p{page_num}.png")
        
        # Render image
        doc_rc[pdf_page_idx].get_pixmap(dpi=150).save(img_temp)
        
        # Run Windows Media OCR
        cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", OCR_SCRIPT, "-ImagePath", img_temp]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        test_pages[str(page_num)] = res.stdout.strip()
        
        # Remove temp image
        try:
            os.remove(img_temp)
        except Exception:
            pass
            
        time.sleep(0.05) # Tiny rest for i5-7200U
        
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(test_pages, f, ensure_ascii=False, indent=2)
        
    t1 = time.time()
    print(f"Test {t} RC OCR complete in {t1 - t0:.1f}s, saved to {cache_file}")

print("All RC OCR caches generated successfully!")
