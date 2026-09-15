import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

print("=== TEST 3 PART 1 ===")
for q in t3['questions'][:6]:
    print(f"Q{q['id']}: options={q.get('options')}")

print("\n=== TEST 3 PART 2 ===")
for q in t3['questions'][6:31]:
    print(f"Q{q['id']}: text={q.get('questionText')} | options={q.get('options')}")
