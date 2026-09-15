import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. ETS 2024 - LISTENING.pdf
doc_lc = fitz.open('ETS 2024 - LISTENING.pdf')
print(f"ETS LISTENING total pages: {len(doc_lc)}")
# Let's search for "TEST 03" or "TEST 3" or book page numbers
# Test 1 is ~pages 0-14, Test 2 is ~pages 15-28, Test 3 is ~pages 29-...
for i in range(len(doc_lc)):
    text = doc_lc[i].get_text()
    if 'TEST 3' in text.upper() or 'TEST 03' in text.upper():
        print(f"LC Page {i+1} has TEST 3 text")

# 2. ETS 2024 - READING.pdf
doc_rc = fitz.open('ETS 2024 - READING.pdf')
print(f"ETS READING total pages: {len(doc_rc)}")
# In check_rc_pages.py, each test is 29 pages:
# Test 1: 0..28
# Test 2: 29..57
# Test 3: 58..86!
print(f"Test 3 in Reading PDF should be pages 58 to 86 (index 58 to 86)")
