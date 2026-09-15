import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')
for p in [53, 58, 59, 60]:
    if p < len(doc):
        text = doc[p].get_text()
        print(f"=== SCRIPT PAGE {p+1} ===")
        for line in text.splitlines():
            if any(k in line.lower() for k in ['100.', '100', 'invite', 'test 2', 'test 02']):
                print("  ", line)
