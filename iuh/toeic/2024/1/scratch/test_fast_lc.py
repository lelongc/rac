import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

TEST_PAGES = {
    1: (1, 31),
    2: (31, 60),
    3: (60, 90),
    4: (90, 119),
    5: (119, 148),
    6: (148, 178),
    7: (178, 208),
    8: (208, 238),
    9: (238, 267),
    10: (267, 296)
}

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")

for t in range(2, 11):
    p1, p2 = TEST_PAGES[t]
    txt = "\n".join([doc[p].get_text() for p in range(p1, p2)])
    # Check questions 1 to 100
    found = 0
    for q in range(1, 101):
        # Look for question number
        if re.search(rf"\b{q}\b", txt):
            found += 1
    print(f"Test {t:2d}: Found {found}/100 questions in text ({len(txt)} chars)")
