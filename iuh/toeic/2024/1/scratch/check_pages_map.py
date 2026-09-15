import fitz
import json
import os

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
rc_doc = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - READING.pdf"))
lc_doc = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - LISTENING.pdf"))

# Let's inspect Test 1 vs Test 2 page mapping
print("=== RC TEST 1 vs TEST 2 ===")
# Test 1 is pages 0 to 28 (29 pages)
# Test 2 is pages 29 to 57 (29 pages)

# In each test:
# Page 1: Cover/Directions
# Page 2: Part 5 (101-115)
# Page 3: Part 5 (116-125)
# Page 4: Part 5 (126-130)
# Page 5: Part 6 (131-134)
# Page 6: Part 6 (135-138)
# Page 7: Part 6 (139-142)
# Page 8: Part 6 (143-146)
# Page 9: Part 7 (147-148)
# ...
# Let's check if Test 2 follows this EXACT same page count per part!

# Let's check by rendering OCR or checking text
# Also check LC pages:
# In Test 1 LC (pages 0 to 12 = 13 pages)
# In Test 2 LC (pages 13 to 25 = 13 pages)
# Which page has Part 3 graphic (Q62-70)?
# Which page has Part 4 graphic (Q95-100)?

print("Checking LC graphics pages for each test:")
for t in range(1, 11):
    start_p = (t - 1) * 13
    # Look at pages 8, 9, 12, 13
    print(f"Test {t}: LC pages {start_p + 1} to {start_p + 13}")
