import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
print("Total pages:", len(doc))

test_starts = {}
for p_idx in range(len(doc)):
    txt = doc[p_idx].get_text()
    m = re.search(r"TEST\s*([0-9]{1,2})", txt)
    if m:
        t_num = int(m.group(1))
        if t_num not in test_starts:
            test_starts[t_num] = p_idx + 1

for t in sorted(test_starts.keys()):
    print(f"Test {t:2d} starts around page {test_starts[t]}")
