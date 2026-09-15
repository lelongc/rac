import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_lc_test3.json', 'r', encoding='utf-8') as f:
    ocr_lc = json.load(f)
print("ocr_lc_test3 keys:", list(ocr_lc.keys())[:10])
for k in list(ocr_lc.keys())[:3]:
    print(f"=== LC Page {k} ===")
    print(ocr_lc[k][:250])

with open('scratch/p5_columns_test3.json', 'r', encoding='utf-8') as f:
    p5_col = json.load(f)
print(f"\np5_columns_test3 has {len(p5_col)} items")
for item in p5_col[:3]:
    print(f"Page {item.get('page')}, Col {item.get('col')}: {item.get('text')[:150]}...")
