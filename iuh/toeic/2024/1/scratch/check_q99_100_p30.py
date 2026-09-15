import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
print("=== PAGE 30 OF SCRIPT NGHE ===")
for line in doc[29].get_text().splitlines():
    print("  ", line)
