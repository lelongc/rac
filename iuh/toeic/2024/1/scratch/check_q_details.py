import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Check Q81 in script
doc = fitz.open('giai/script nghe_0001.pdf')
for p in range(50, 62):
    text = doc[p].get_text()
    if '81' in text and ('competitor' in text.lower() or 'different' in text.lower()):
        print(f"=== Script Page {p+1} (Q81) ===")
        for line in text.splitlines():
            if any(k in line.lower() for k in ['81.', '81', 'competitor', 'different']):
                print("  ", line)

# Check Q166 & Q182 in RC PDF
doc_rc = fitz.open('TEST 2 RC (1).pdf')
for pno in range(len(doc_rc)):
    text = doc_rc[pno].get_text()
    if '166' in text or '182' in text:
        print(f"=== RC PDF Page {pno+1} ===")
        for line in text.splitlines():
            if any(k in line.lower() for k in ['166', 'address', '182', 'suit', 'closest']):
                print("  ", line)
