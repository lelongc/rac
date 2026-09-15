import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

# Check where Test 4 and Test 5 are in ETS 2024 - LISTENING.pdf
doc_lc = fitz.open('ETS 2024 - LISTENING.pdf')
print(f"Total listening pages: {len(doc_lc)}")

# Test 1: pages ~0-14 (book 1..15)
# Test 2: pages ~14-27
# Test 3: pages ~27-41 (p28, p29, p30 were Part 1 of Test 3)
# Where is Test 4 Part 1?
# Let's scan pages 35-70 to find "TEST 4" and "TEST 5"
for pno in range(len(doc_lc)):
    text = doc_lc[pno].get_text()
    if 'TEST 4' in text.upper() or 'TEST 04' in text.upper():
        print(f"LC Page {pno} (1-indexed {pno+1}) mentions TEST 4")
    if 'TEST 5' in text.upper() or 'TEST 05' in text.upper():
        print(f"LC Page {pno} (1-indexed {pno+1}) mentions TEST 5")
