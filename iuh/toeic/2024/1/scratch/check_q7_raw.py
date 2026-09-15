import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
# Test 2 is pages 32 to 60
t2_text = "\n".join([doc[p].get_text() for p in range(31, 60)])
idx = t2_text.find("\n7\n")
print(t2_text[idx:idx+400])
