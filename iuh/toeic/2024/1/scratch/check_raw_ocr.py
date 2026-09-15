import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open('scratch/ocr_rc_test2.json', encoding='utf-8'))
print("Sample page 2 raw OCR:")
print(d['2'][:500])
