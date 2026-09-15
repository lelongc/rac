import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', 'r', encoding='utf-8') as f:
    t1 = json.load(f)

p6 = [q for q in t1['questions'] if q['part'] == 6]
print("Test 1 Part 6 sample Q131:")
print(json.dumps(p6[0], indent=2, ensure_ascii=False))
