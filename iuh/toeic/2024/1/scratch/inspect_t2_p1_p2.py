import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

print("=== TEST 2 PART 1 ===")
for q in t2['questions'][:6]:
    print(f"Q{q['id']}: options={q.get('options')}")

print("\n=== TEST 2 PART 2 ===")
for q in t2['questions'][6:31]:
    print(f"Q{q['id']}: text={q.get('questionText')} | options={q.get('options')}")
