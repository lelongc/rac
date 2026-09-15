import fitz
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')

# Part 2 is on pages 62 to 69
full_p2_text = ""
for pno in range(61, 70):
    full_p2_text += doc[pno].get_text() + "\n"

# Let's search for questions 7 to 31
for qid in range(7, 32):
    # Pattern to find question number
    m = re.search(rf'\b{qid}\b', full_p2_text)
    if m:
        sub = full_p2_text[m.start():m.start()+350]
        lines = [l.strip() for l in sub.splitlines() if l.strip()]
        print(f"--- Q{qid} ---")
        for l in lines[:6]:
            print("  ", l)
