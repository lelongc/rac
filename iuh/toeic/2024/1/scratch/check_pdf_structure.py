import os
import fitz

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
DOC_LC = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - LISTENING.pdf"))
DOC_RC = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - READING.pdf"))

print(f"LC PDF pages: {len(DOC_LC)}")
print(f"RC PDF pages: {len(DOC_RC)}")

# Each test in LC is 13 pages (10 tests = 130 pages)
# Let's see what is on each page of Test 2 in LC (pages 13 to 25, 0-indexed)
print("\n=== LC TEST 2 (pages 13-25) ===")
for i in range(13, 26):
    txt = DOC_LC[i].get_text()
    first_line = [l.strip() for l in txt.split('\n') if l.strip()][:2]
    print(f"Page {i+1} (Test 2 relative {i-12}): {first_line}")

# Each test in RC is 29 pages (10 tests = 290 pages)
print("\n=== RC TEST 2 (pages 29-57) ===")
for i in range(29, 58):
    txt = DOC_RC[i].get_text()
    first_line = [l.strip() for l in txt.split('\n') if l.strip()][:2]
    if any(k in txt for k in ["PART 5", "PART 6", "PART 7", "131.", "147.", "176.", "186.", "196."]):
        print(f"Page {i+1} (Test 2 relative {i-28}): {first_line}")
