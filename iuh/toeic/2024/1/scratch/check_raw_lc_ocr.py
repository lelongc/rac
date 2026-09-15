import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open('scratch/ocr_lc_test2.json', encoding='utf-8'))
print("Keys:", list(d.keys()))
for k in list(d.keys())[:3]:
    print(f"--- Page {k} ---")
    print(d[k][:300])
