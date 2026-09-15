import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test3.json', 'r', encoding='utf-8') as f:
    ocr_rc = json.load(f)

print("ocr_rc_test3 keys:", list(ocr_rc.keys()))
for p in ['5', '6', '7', '8']:
    if p in ocr_rc:
        print(f"=== Page {p} ===")
        print(ocr_rc[p][:400])
