import fitz
import os

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\ETS 2024 - LISTENING.pdf")
print("Total LC pages:", len(doc))

# For each test, there are 13 pages
# Let's see: in Test 1:
# Page 1 (index 0): Cover
# Page 2 (index 1): Part 1 Q1-2
# Page 3 (index 2): Part 1 Q3-4
# Page 4 (index 3): Part 1 Q5-6
# Page 5 (index 4): Part 2
# Page 6 (index 5): Part 2
# Page 7 (index 6): Part 3
# Page 8 (index 7): Part 3
# Page 9 (index 8): Part 3 (Q62-70 with graphics!)
# Page 10 (index 9): Part 4
# Page 11 (index 10): Part 4
# Page 12 (index 11): Part 4
# Page 13 (index 12): Part 4 (Q95-100 with graphics!)

# Let's verify this layout across all 10 tests:
for t in range(1, 11):
    base = (t - 1) * 13
    print(f"Test {t:2d}: Part 3 graphics is Page {base + 9} (index {base + 8}), Part 4 graphics is Page {base + 13} (index {base + 12})")
