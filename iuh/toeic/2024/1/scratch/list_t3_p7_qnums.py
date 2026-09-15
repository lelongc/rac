import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test3.json', 'r', encoding='utf-8') as f:
    ocr_rc = json.load(f)

# Let's inspect the questions on each page from 9 to 29
for pno in range(9, 30):
    text = ocr_rc[str(pno)]
    # find question numbers like 147., 148., etc.
    q_matches = re.findall(r'(\b1[4-9]\d\b|\b200\b)\.', text)
    print(f"Page {pno}: Questions found -> {q_matches}")
