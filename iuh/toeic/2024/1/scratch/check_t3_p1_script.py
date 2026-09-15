import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')
for pno in [59, 60, 61, 62]:
    print(f"=== SCRIPT PAGE {pno+1} ===")
    text = doc[pno].get_text()
    for l in text.splitlines():
        if any(w in l for w in ['(A)', '(B)', '(C)', '(D)', '01', '02', '03', '04', '05', '06', 'TEST 3']):
            print("  ", l)
