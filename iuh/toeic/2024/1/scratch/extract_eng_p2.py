import fitz
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')

# Let's inspect pages 62 to 69 and print only English lines
print("=== EXTRACTING ENGLISH LINES FROM SCRIPT PAGES 62-69 ===")
for pno in range(61, 70):
    text = doc[pno].get_text()
    lines = text.splitlines()
    eng_lines = []
    for l in lines:
        l_clean = l.strip()
        # check if contains English words and no/few hangul
        if re.search(r'[a-zA-Z]{3,}', l_clean):
            # check proportion of ascii
            ascii_count = sum(1 for c in l_clean if ord(c) < 128)
            if ascii_count / max(1, len(l_clean)) > 0.6:
                eng_lines.append(l_clean)
    print(f"--- Page {pno+1} ({len(eng_lines)} lines) ---")
    for el in eng_lines[:25]:
        print("  ", el)
