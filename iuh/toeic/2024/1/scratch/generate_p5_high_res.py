import fitz
from PIL import Image
import subprocess
import os
import json
import time
import re

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
SCRATCH_DIR = os.path.join(BASE_DIR, "scratch")
doc_rc = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - READING.pdf"))

def ocr_image(img_path):
    cmd = ["powershell", "-NoLogo", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", img_path]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return res.stdout.strip()

def process_test_p5(t):
    out_file = os.path.join(SCRATCH_DIR, f"p5_columns_test{t}.json")
    if os.path.exists(out_file):
        print(f"Test {t} P5 columns already cached.")
        with open(out_file, "r", encoding="utf-8") as f:
            return json.load(f)

    print(f"--- Rendering & OCRing Part 5 for Test {t} (300 DPI) ---")
    rc_start = (t - 1) * 29
    # Part 5 is on pages 2, 3, 4 -> global indices rc_start + 1, rc_start + 2, rc_start + 3
    columns = []

    for p_offset in [1, 2, 3]:
        page_idx = rc_start + p_offset
        pix = doc_rc[page_idx].get_pixmap(dpi=300)
        im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        w, h = im.size

        # On page 2 (p_offset == 1), skip directions at the top
        y_top_left = 500 if p_offset == 1 else 150
        y_top_right = 350 if p_offset == 1 else 150

        left_crop = im.crop((80, y_top_left, w // 2 + 60, h - 140))
        right_crop = im.crop((w // 2 - 60, y_top_right, w - 80, h - 140))

        tmp_l = os.path.join(SCRATCH_DIR, f"tmp_t{t}_p{p_offset}_l.png")
        tmp_r = os.path.join(SCRATCH_DIR, f"tmp_t{t}_p{p_offset}_r.png")

        left_crop.save(tmp_l)
        right_crop.save(tmp_r)

        txt_l = ocr_image(tmp_l)
        time.sleep(0.05)
        txt_r = ocr_image(tmp_r)
        time.sleep(0.05)

        for tmp in [tmp_l, tmp_r]:
            if os.path.exists(tmp):
                try: os.remove(tmp)
                except: pass

        columns.append({"page": p_offset + 1, "col": "left", "text": txt_l})
        columns.append({"page": p_offset + 1, "col": "right", "text": txt_r})

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(columns, f, ensure_ascii=False, indent=2)

    print(f"Test {t} Part 5 OCR cached to {out_file}")
    return columns

if __name__ == "__main__":
    for t in range(2, 11):
        cols = process_test_p5(t)
        print(f"Test {t} columns count: {len(cols)}")
        time.sleep(0.5) # Gentle cooldown for i5-7200U
    print("ALL TESTS PART 5 HIGH-RES OCR FINISHED!")
