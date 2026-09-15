import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')
print(f"Total script pages: {len(doc)}")

for pno in range(len(doc)):
    text = doc[pno].get_text()
    if 'TEST 03' in text.upper() or 'TEST 3' in text.upper():
        print(f"Page {pno+1} has TEST 3")
        # print first 5 lines
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        print("  Lines:", lines[:3])
        if len(lines) > 5:
            # check if Part 1
            if any('PART 1' in l.upper() for l in lines[:10]):
                print(f"  FOUND PART 1 START AT PAGE {pno+1}!")
