import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
# Page range for test 2: 31 to 60 (0-indexed 30 to 59)
print("=== SCRIPT NGHE TEST 2 FIRST 3 PAGES ===")
for p in range(30, 34):
    print(f"\n--- PAGE {p+1} ---")
    print(doc[p].get_text()[:1500])
