import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test2.json', 'r', encoding='utf-8') as f:
    ocr = json.load(f)

print("OCR keys/pages:", list(ocr.keys()))
for p, content in list(ocr.items())[:4]:
    print(f"=== Page {p} ===")
    lines = content.splitlines() if isinstance(content, str) else []
    for l in lines[:20]:
        print("  ", l)
