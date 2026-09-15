import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
t2_text = "\n".join([doc[p].get_text() for p in range(31, 60)])

# Split sections
p2_split = t2_text.split("PART 2")
p1_sec = p2_split[0]
rest1 = p2_split[1]

p3_split = rest1.split("PART 3")
p2_sec = p3_split[0]
rest2 = p3_split[1]

p4_split = rest2.split("PART 4")
p3_sec = p4_split[0]
p4_sec = p4_split[1]

print(f"P1 len: {len(p1_sec)}, P2 len: {len(p2_sec)}, P3 len: {len(p3_sec)}, P4 len: {len(p4_sec)}")

# In p3_sec, search for 32:
idx32 = p3_sec.find("\n32\n")
if idx32 != -1:
    print("\n--- P3 Q32 Found ---")
    print(p3_sec[idx32:idx32+250])
else:
    # search regex
    m = re.search(r"\n\s*32\s*\n\s*([A-Za-z][^\n]+)", p3_sec)
    if m:
        print("\n--- P3 Q32 Regex Match ---")
        print(m.group(0))

# In p4_sec, search for 71:
m71 = re.search(r"\n\s*71\s*\n\s*([A-Za-z][^\n]+)", p4_sec)
if m71:
    print("\n--- P4 Q71 Regex Match ---")
    print(m71.group(0))
