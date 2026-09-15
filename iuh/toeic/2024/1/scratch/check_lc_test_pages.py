import fitz, sys
from PIL import Image

doc = fitz.open('ETS 2024 - LISTENING.pdf')

# Let's save snapshots of pages from 35 to 70 to identify exactly where Test 4 and Test 5 begin
# In check_t3, Test 3 was pages 27-40 (p27 was directions, p28 was Q1-Q2, p29 was Q3-Q4, p30 was Q5-Q6)
# Each test is 14 pages in Listening!
# Test 1: p0 (directions), p1 (Q1-Q2), p2 (Q3-Q4), p3 (Q5-Q6)...
# Test 2: p14 (directions), p15 (Q1-Q2), p16 (Q3-Q4), p17 (Q5-Q6)...
# Test 3: p27 (directions), p28 (Q1-Q2), p29 (Q3-Q4), p30 (Q5-Q6)...
# Test 4: p40 or p41?
# Test 5: p54 or p55?

print("=== Checking potential Part 1 pages ===")
for pno in [40, 41, 42, 43, 44, 53, 54, 55, 56, 57]:
    if pno < len(doc):
        pix = doc[pno].get_pixmap(dpi=72)
        pix.save(f'scratch/thumb_p{pno}.png')
        print(f"Saved scratch/thumb_p{pno}.png")
