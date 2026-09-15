import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test2.json', 'r', encoding='utf-8') as f:
    ocr = json.load(f)

for p in ['22', '23', '24', '25']:
    if p in ocr:
        print(f"=== Page {p} ===")
        print(ocr[p])
