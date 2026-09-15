import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Check what each page of TEST 2 RC (1).pdf contains
# TEST 2 RC (1).pdf has 29 pages (index 0 to 28)
# Let's see: what was exported to web/assets/images/test2/rc_page_X.png?
# Let's check the size or render of each page
doc = fitz.open('TEST 2 RC (1).pdf')
print(f"TEST 2 RC (1).pdf has {len(doc)} pages.")

# In scratch/ocr_rc_test2.json, keys were '2', '3', ..., '29'
# Let's check how ocr_rc_test2.json was created!
with open('scratch/ocr_rc_test2.json', 'r', encoding='utf-8') as f:
    import json
    ocr = json.load(f)

for k in ['2', '5', '8', '9', '10', '28', '29']:
    if k in ocr:
        print(f"Key {k} (first 60 chars): {ocr[k][:60]}")
