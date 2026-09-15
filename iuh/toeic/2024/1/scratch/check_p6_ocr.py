import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test2.json', 'r', encoding='utf-8') as f:
    ocr = json.load(f)

print("=== PART 6 PAGES (5, 6, 7) ===")
for p in ['5', '6', '7']:
    if p in ocr:
        print(f"--- PAGE {p} ---")
        print(ocr[p])
