import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

rc_data = json.load(open('scratch/ocr_rc_test2.json', encoding='utf-8'))
# Pages 2, 3, 4 are Part 5 (Q101 - Q130)
p5_text = rc_data.get('2', '') + "\n" + rc_data.get('3', '') + "\n" + rc_data.get('4', '')
print("Part 5 raw OCR length:", len(p5_text))
print("First 1000 chars:\n", p5_text[:1000])
