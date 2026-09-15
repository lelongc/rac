import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test3.json', 'r', encoding='utf-8') as f:
    ocr = json.load(f)

print(ocr['10'])
