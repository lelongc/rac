import fitz
import sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open("giai/script nghe_0001.pdf")
print("Total pages in script nghe_0001.pdf:", len(doc))

# Check first few pages
for i in range(min(5, len(doc))):
    text = doc[i].get_text()
    print(f"Page {i+1} ({len(text)} chars): {text[:150].replace(chr(10), ' ')}")
