import json
import fitz

doc_rc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\ETS 2024 - READING.pdf")

# In Test 1 (pages 0 to 28):
# Page 1 (index 0): Directions / Cover
# Page 2 (index 1): Part 5 (Q101-115)
# Page 3 (index 2): Part 5 (Q116-125)
# Page 4 (index 3): Part 5 (Q126-130)
# Page 5 (index 4): Part 6 (Q131-134)
# Page 6 (index 5): Part 6 (Q135-138)
# Page 7 (index 6): Part 6 (Q139-142)
# Page 8 (index 7): Part 6 (Q143-146)
# Page 9 (index 8): Part 7 (Q147-148)
# Page 10 (index 9): Part 7 (Q149-150)
# Page 11 (index 10): Part 7 (Q151-152)
# Page 12 (index 11): Part 7 (Q153-154)
# Page 13 (index 12): Part 7 (Q155-157)
# Page 14 (index 13): Part 7 (Q158-160)
# Page 15 (index 14): Part 7 (Q161-163)
# Page 16 (index 15): Part 7 (Q164-167)
# Page 17-18 (index 16-17): Part 7 (Q168-171)
# Page 19 (index 18): Part 7 (Q172-175)
# Page 20-21 (index 19-20): Part 7 (Q176-180)
# Page 22-23 (index 21-22): Part 7 (Q181-185)
# Page 24-25 (index 23-24): Part 7 (Q186-190)
# Page 26-27 (index 25-26): Part 7 (Q191-195)
# Page 28-29 (index 27-28): Part 7 (Q196-200)

print("Verifying Test 2 page count:")
print("Test 2 start:", 1 * 29, "Test 2 end:", 2 * 29 - 1)
# Exactly 29 pages per test!
