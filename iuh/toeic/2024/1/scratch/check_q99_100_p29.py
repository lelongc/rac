import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
print("=== PAGE 29 OF SCRIPT NGHE ===")
for line in doc[28].get_text().splitlines():
    if any(k in line for k in ["98", "99", "100", "Look at", "graphic", "depth", "newsletter", "inches", "(A)", "(B)", "(C)", "(D)"]):
        print("  ", line)
