import fitz
from PIL import Image
import subprocess
import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
doc_rc = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - READING.pdf"))

# For Test 2:
# Page 2: index 30 (Q101-115)
# Page 3: index 31 (Q116-125)
# Page 4: index 32 (Q126-130)

def ocr_split_page(page_idx):
    pix = doc_rc[page_idx].get_pixmap(dpi=200)
    im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    w, h = im.size
    
    left = im.crop((50, 100, int(w * 0.52), h - 80))
    right = im.crop((int(w * 0.48), 100, w - 50, h - 80))
    
    p_left = os.path.join(BASE_DIR, "scratch", f"p_{page_idx}_left.png")
    p_right = os.path.join(BASE_DIR, "scratch", f"p_{page_idx}_right.png")
    left.save(p_left)
    right.save(p_right)
    
    cmd_l = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", p_left]
    cmd_r = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", p_right]
    
    txt_l = subprocess.run(cmd_l, capture_output=True, text=True, encoding="utf-8").stdout
    txt_r = subprocess.run(cmd_r, capture_output=True, text=True, encoding="utf-8").stdout
    
    return txt_l + "\n" + txt_r

print("Running column-aware OCR for Test 2 Part 5 (Pages 2, 3, 4)...")
t2_p5_ocr = ocr_split_page(30) + "\n" + ocr_split_page(31) + "\n" + ocr_split_page(32)

print("Total OCR length:", len(t2_p5_ocr))

# Parse questions 101 to 130
parsed_p5 = {}
# Clean text: replace — or with -------
cleaned_text = t2_p5_ocr.replace("—", "-------").replace("–", "-------").replace("------", "-------")

for q in range(101, 131):
    # Pattern to find Question q
    # e.g. "101. Before operating ... (A) ... (B) ... (C) ... (D) ..."
    # or "Before operating ... 101. ... (A) ... (B) ... (C) ... (D) ..."
    pattern = rf"(?:^|\n)(?:[^\n\d]*?)\b{q}\b[\.\s]+(.*?)(?=\([A]\)|\bA\b[\.\)])\s*[\(\[]?A[\)\]]?\s*([^\(\n\r]+)\s*[\(\[]?B[\)\]]?\s*([^\(\n\r]+)\s*[\(\[]?C[\)\]]?\s*([^\(\n\r]+)\s*[\(\[]?D[\)\]]?\s*([^\n\r]+)"
    m = re.search(pattern, cleaned_text, re.DOTALL)
    if m:
        stem = m.group(1).strip()
        a = m.group(2).strip()
        b = m.group(3).strip()
        c = m.group(4).strip()
        d = m.group(5).strip()
        parsed_p5[q] = {"stem": stem, "A": a, "B": b, "C": c, "D": d}
    else:
        # simpler search
        m2 = re.search(rf"\b{q}\b[\.\s]+([^\n\r]+)", cleaned_text)
        if m2:
            parsed_p5[q] = {"stem": m2.group(1).strip()}

print(f"Parsed {len(parsed_p5)}/30 questions in Part 5")
for q in [101, 102, 103, 104, 105, 115, 120, 130]:
    if q in parsed_p5:
        print(f"Q{q}: {parsed_p5[q]}")
