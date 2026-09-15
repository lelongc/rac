import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('TEST 2 LC (1).pdf')
for pno in range(len(doc)):
    text = doc[pno].get_text()
    if '100.' in text or '100' in text:
        for line in text.splitlines():
            if '100' in line or 'invite' in line.lower():
                print(f"Page {pno+1}: {line}")
