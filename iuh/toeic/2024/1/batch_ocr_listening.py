# batch_ocr_listening.py: Sequentially OCR Listening Part 3 & 4 pages for Tests 2 to 10
import fitz
import subprocess
import os
import json
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRATCH_DIR = os.path.join(BASE_DIR, "scratch")
os.makedirs(SCRATCH_DIR, exist_ok=True)
doc_lc = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - LISTENING.pdf"))

OCR_SCRIPT = "d:/folder/rac/ocr.ps1"

for t in range(2, 11):
    cache_file = os.path.join(SCRATCH_DIR, f"ocr_lc_test{t}.json")
    if os.path.exists(cache_file):
        print(f"Test {t} LC OCR cache already exists, skipping.")
        continue
        
    t0 = time.time()
    print(f"--- Starting OCR for Test {t} Listening Part 3 & 4 ---")
    lc_start = (t - 1) * 13
    test_pages = {}
    
    # Part 3: pages 7, 8, 9 (indices 6, 7, 8)
    # Part 4: pages 10, 11, 12 (indices 9, 10, 11)
    for p in range(6, 12):
        page_num = p + 1
        pdf_page_idx = lc_start + p
        img_temp = os.path.join(SCRATCH_DIR, f"temp_lc_t{t}_p{page_num}.png")
        
        doc_lc[pdf_page_idx].get_pixmap(dpi=150).save(img_temp)
        
        cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", OCR_SCRIPT, "-ImagePath", img_temp]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        test_pages[str(page_num)] = res.stdout.strip()
        
        try:
            os.remove(img_temp)
        except Exception:
            pass
            
        time.sleep(0.05)
        
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(test_pages, f, ensure_ascii=False, indent=2)
        
    t1 = time.time()
    print(f"Test {t} LC OCR complete in {t1 - t0:.1f}s, saved to {cache_file}")

print("All LC OCR caches generated successfully!")
