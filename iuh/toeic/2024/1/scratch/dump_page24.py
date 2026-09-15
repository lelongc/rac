import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
print("=== PAGE 24 OF SCRIPT NGHE ===")
print(doc[23].get_text())
