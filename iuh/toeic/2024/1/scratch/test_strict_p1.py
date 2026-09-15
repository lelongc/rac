import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")

for t in range(2, 6):
    p_start = (t - 1) * 30 + 1
    t_text = "\n".join([doc[p].get_text() for p in range(p_start, p_start + 4)])
    
    # Pattern to find blocks of (A), (B), (C), (D) where text is English
    pattern = r"\n\s*\(A\)\s*([A-Za-z][^\n\r]+)\n\s*\(B\)\s*([A-Za-z][^\n\r]+)\n\s*\(C\)\s*([A-Za-z][^\n\r]+)\n\s*\(D\)\s*([A-Za-z][^\n\r]+)"
    matches = re.findall(pattern, t_text)
    
    clean_blocks = []
    for a, b, c, d in matches:
        if all(sum(1 for char in opt if char.isascii()) / len(opt) > 0.8 for opt in [a, b, c, d]):
            clean_blocks.append({"A": a.strip(), "B": b.strip(), "C": c.strip(), "D": d.strip()})
            
    print(f"Test {t}: Found {len(clean_blocks)} clean Part 1 4-option blocks")
    for i, blk in enumerate(clean_blocks):
        print(f"  Q{i+1}: {blk['A'][:40]} | {blk['B'][:40]} | {blk['C'][:40]} | {blk['D'][:40]}")
