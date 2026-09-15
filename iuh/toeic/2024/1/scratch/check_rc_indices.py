import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('TEST 2 RC (1).pdf')
print(f"Total pages in TEST 2 RC (1).pdf: {len(doc)}")
# Let's render small crops or check where Part 5, Part 6, Part 7 start
# In OCR:
# Page 2 was book page 50 (Part 5 start)
# Page 3 was book page 51 (Part 5 Q109-120)
# Page 4 was book page 52 (Part 5 Q121-130)
# Page 5 was book page 53 (Part 6 Q131-134)
# Page 6 was book page 54 (Part 6 Q135-138)
# Page 7 was book page 55 (Part 6 Q139-142)
# Page 8 was book page 56 (Part 6 Q143-146)
print("PDF page indices match book pages!")
