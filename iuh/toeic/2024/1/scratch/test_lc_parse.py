import fitz
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
# Test 2 is pages 32 to 60 (0-indexed 31 to 59)
t2_text = "\n".join([doc[i].get_text() for i in range(31, 60)])

print(f"Test 2 script text total characters: {len(t2_text)}")

# Test parsing Part 1: Q1 to Q6
print("\n=== PARSING PART 1 (Q1-Q6) ===")
for q in range(1, 7):
    # Search for question number followed by (A), (B), (C), (D)
    # In script nghe, question number is often like:
    # 1 W-Am \n (A) ... \n (B) ... \n (C) ... \n (D) ...
    # or at top of column
    pattern = rf"(?:^|\n)\s*{q}\s+(?:[MW]-[A-Za-z]+\s*\n)?\s*\(([ABCD])\)\s*([^\n]+)\s*\n\s*\(([ABCD])\)\s*([^\n]+)\s*\n\s*\(([ABCD])\)\s*([^\n]+)\s*\n\s*\(([ABCD])\)\s*([^\n]+)"
    m = re.search(pattern, t2_text)
    if m:
        opts = {m.group(1): m.group(2).strip(), m.group(3): m.group(4).strip(), m.group(5): m.group(6).strip(), m.group(7): m.group(8).strip()}
        print(f"Q{q}: {opts}")
    else:
        # Try finding around "\n{q}\n"
        print(f"Q{q}: Not matched by standard pattern, searching snippet...")
        idx = t2_text.find(f"\n{q}\n")
        if idx != -1:
            print(t2_text[idx:idx+300])

# Test parsing Part 2: Q7 to Q31
print("\n=== PARSING SAMPLE PART 2 (Q7, Q8, Q9, Q10) ===")
for q in [7, 8, 9, 10]:
    # Look for: q \n Speaker prompt \n (A) ... \n (B) ... \n (C) ...
    idx = t2_text.find(f"\n{q}\n")
    if idx != -1:
        snippet = t2_text[idx:idx+400]
        print(f"--- Q{q} SNIPPET ---")
        print(snippet[:250])
