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

def extract_part1_for_test(test_id):
    p1, _ = TEST_PAGES[test_id]
    # In script nghe, Part 1 is usually in pages p1 to p1+3
    text = "\n".join([doc[p].get_text() for p in range(p1, p1 + 4)])
    
    # Collect all lines with (A), (B), (C), (D) where text is English
    lines = text.splitlines()
    blocks = []
    curr = {}
    for line in lines:
        line = line.strip()
        m = re.match(r"^\(([ABCD])\)\s*([A-Za-z][^\n\r]+)$", line)
        if m:
            letter = m.group(1)
            t = m.group(2).strip()
            # remove Korean chars
            t = re.split(r"[\uac00-\ud7a3]", t)[0].strip()
            ascii_ratio = sum(1 for c in t if c.isascii()) / len(t) if t else 0
            if ascii_ratio > 0.8 and len(t) > 12:
                curr[letter] = t
                if len(curr) == 4:
                    # Check if this block is unique
                    if not any(curr['A'] == b['A'] for b in blocks):
                        blocks.append(curr)
                    curr = {}
                    if len(blocks) == 6:
                        break
    return blocks

for t in range(2, 11):
    blks = extract_part1_for_test(t)
    print(f"Test {t:2d}: Extracted {len(blks)}/6 Part 1 sets")
    if len(blks) < 6:
        print(f"  Only {len(blks)} found for Test {t}")
