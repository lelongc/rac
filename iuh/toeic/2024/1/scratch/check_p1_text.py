import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
# Test 2 Part 1 is in pages 32 and 33
for p in [31, 32]:
    print(f"=== PAGE {p+1} ===")
    lines = doc[p].get_text().split("\n")
    for l in lines:
        if any(l.strip().startswith(f"({k})") for k in ["A", "B", "C", "D"]):
            print("  ", l.strip())
        elif any(f" {k} " in f" {l.strip()} " for k in ["1", "2", "3", "4", "5", "6"]) and len(l.strip()) < 10:
            print("LINE:", l.strip())
