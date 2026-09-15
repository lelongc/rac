import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test3.json', 'r', encoding='utf-8') as f:
    ocr_rc = json.load(f)

for pno in range(9, 30):
    p_str = str(pno)
    if p_str in ocr_rc:
        print(f"=== Page {p_str} ===")
        text = ocr_rc[p_str]
        print(text[:300])
        print("...")
