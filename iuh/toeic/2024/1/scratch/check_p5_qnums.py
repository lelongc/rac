import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for t in [2, 3, 4]:
    d = json.load(open(f"scratch/ocr_rc_test{t}.json", encoding='utf-8'))
    # Pages 2, 3, 4 are Part 5
    p5_txt = d.get('2', '') + " " + d.get('3', '') + " " + d.get('4', '')
    print(f"\n=== TEST {t} PART 5 ===")
    found = 0
    for q in range(101, 131):
        if re.search(rf"\b{q}\b", p5_txt):
            found += 1
    print(f"Found question numbers: {found}/30")
