import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
p1_text = "\n".join([doc[p].get_text() for p in range(31, 35)])

sets = []
curr = {}
for line in p1_text.splitlines():
    line = line.strip()
    m = re.match(r"^\(([ABCD])\)\s*([A-Za-z][^\n\r]+)$", line)
    if m:
        letter = m.group(1)
        text = m.group(2).strip()
        # remove Korean text
        text = re.split(r"[\uac00-\ud7a3]", text)[0].strip()
        if len(text) > 15:
            curr[letter] = text
            if len(curr) == 4:
                sets.append(curr)
                curr = {}

print(f"Extracted {len(sets)} Part 1 sets:")
for i, s in enumerate(sets):
    print(f"Q{i+1}:")
    for k in sorted(s.keys()):
        print(f"  ({k}) {s[k]}")
