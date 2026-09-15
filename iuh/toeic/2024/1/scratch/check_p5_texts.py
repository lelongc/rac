import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    t2 = json.load(f)

print("=== PART 5 DETAILED INSPECTION ===")
for q in t2['questions']:
    if q['part'] == 5:
        print(f"Q{q['id']}: {q.get('questionText')}")
