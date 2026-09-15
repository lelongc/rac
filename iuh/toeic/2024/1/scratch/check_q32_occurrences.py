import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
t2_text = "\n".join([doc[p].get_text() for p in range(31, 60)])

for m in re.finditer(r"(?:^|\n)\s*32\s*(?:\n|\b)", t2_text):
    start = max(0, m.start() - 20)
    end = min(len(t2_text), m.end() + 250)
    print("--- Occurrence at", m.start(), "---")
    print(t2_text[start:end])
