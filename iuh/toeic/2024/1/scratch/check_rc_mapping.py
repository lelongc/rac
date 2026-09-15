import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect the files in web/assets/images/test2/
# In fitz, TEST 2 RC (1).pdf has 29 pages (0 to 28)
doc = fitz.open('TEST 2 RC (1).pdf')
print("Total pages in TEST 2 RC (1).pdf:", len(doc))

# Let's find what is on page 7, 8, 9, 10 of TEST 2 RC (1).pdf using OCR or checking text
# Wait, TEST 2 RC (1).pdf pages are images. But we can check ocr_rc_test2.json
# In ocr_rc_test2.json, keys are '2', '3', ..., '29'
# Let's see which PDF page index corresponds to key '8' and '9' in ocr_rc_test2.json
with open('scratch/check_rc_pages.py', 'r', encoding='utf-8') as f:
    print("--- check_rc_pages.py ---")
    print(f.read()[:500])
