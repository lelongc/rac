import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
print("Total pages in script nghe:", len(doc))

# Search for "Questions 77-79" or "Questions 77 through 79" in the first 30 pages
found = []
for p in range(min(50, len(doc))):
    text = doc[p].get_text()
    if "77" in text and "78" in text and "79" in text:
        print(f"Found on page {p+1}:")
        for line in text.splitlines():
            if any(k in line for k in ["77", "78", "79", "80", "Kenneth", "Orchid"]):
                print("  ", line)
        found.append(p)
        if len(found) >= 2:
            break
