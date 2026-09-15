import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test2.json', encoding='utf-8') as f:
    ocr2 = json.load(f)

print("Pages in ocr_rc_test2.json:", sorted(list(ocr2.keys()), key=lambda x: int(x) if x.isdigit() else 999))

for page_num in range(8, 29):
    k = str(page_num)
    if k in ocr2:
        text = ocr2[k]
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        first_lines = " | ".join(lines[:3])
        print(f"Page {k} ({len(text)} chars): {first_lines[:100]}")
