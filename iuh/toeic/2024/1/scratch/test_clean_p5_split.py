import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/p_30_left.png", "rb") as f:
    pass # we have t2_p5_ocr from before

# Let's inspect the exact questions on Page 2 Left Column
import subprocess
txt_l = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", r"d:\folder\rac\iuh\toeic\2024\1\scratch\p_30_left.png"], capture_output=True, text=True, encoding="utf-8").stdout

# Clean
txt_l = txt_l.replace("—", "-------").replace("–", "-------")
print("=== RAW LEFT COLUMN ===")
print(txt_l)

# Regex to find: (sentence) (A) ... (B) ... (C) ... (D) ...
items = re.findall(r"([A-Z][^\n\r\(\)]+?)\s*\([A]\)\s*([^\(\n\r]+)\s*\([B]\)\s*([^\(\n\r]+)\s*\([C]\)\s*([^\(\n\r]+)\s*\([D]\)\s*([^\n\r]+)", txt_l)
print(f"\nFound {len(items)} questions:")
for i, item in enumerate(items):
    stem, a, b, c, d = item
    # Clean stem: remove leading numbers like "101." or "50"
    stem = re.sub(r"^[\d\.\s]+", "", stem.strip())
    print(f"Item {i+1}:")
    print(f"  Stem: {stem}")
    print(f"  A: {a.strip()} | B: {b.strip()} | C: {c.strip()} | D: {d.strip()}")
