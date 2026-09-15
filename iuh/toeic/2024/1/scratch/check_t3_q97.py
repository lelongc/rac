import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')
for pno in range(86, 91):
    text = doc[pno].get_text()
    if '97' in text and 'TEST 3' in text:
        print(f"=== SCRIPT PAGE {pno+1} ===")
        for l in text.splitlines():
            if any(k in l for k in ['95', '96', '97', '98', '99', '100', 'Look at the graphic', '?']):
                print("  ", l)
