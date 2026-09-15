import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test3.json', 'r', encoding='utf-8') as f:
    ocr_rc = json.load(f)

for pno in range(18, 30):
    print(f"================== PAGE {pno} ==================")
    print(ocr_rc[str(pno)])
