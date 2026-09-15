import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

for t in range(2, 11):
    p = f"scratch/ocr_rc_test{t}.json"
    if os.path.exists(p):
        d = json.load(open(p, encoding='utf-8'))
        p2 = d.get('2', '')
        print(f"Test {t:2d}: page 2 length = {len(p2):4d} | first 60 chars: {p2[:60]}")
    else:
        print(f"Test {t:2d}: MISSING")
