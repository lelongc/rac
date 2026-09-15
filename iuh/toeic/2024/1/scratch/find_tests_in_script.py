import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')
print(f"Total script pages: {len(doc)}")

for pno in range(len(doc)):
    text = doc[pno].get_text()
    for t in [4, 5, 6, 7, 8, 9, 10]:
        if f'TEST {t}' in text.upper():
            # Check if this page is the answer key or the start of the script
            print(f"Script page {pno+1} (idx {pno}) has 'TEST {t}'")
