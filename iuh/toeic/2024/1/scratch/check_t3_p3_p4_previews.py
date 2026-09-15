import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

print("=== TEST 3 PART 3 DIALOGUES PREVIEW ===")
for i in range(31, 70, 3):
    q = t3['questions'][i]
    print(f"Q{q['id']}-{q['id']+2}: {str(q.get('passage'))[:120]}...")

print("\n=== TEST 3 PART 4 TALKS PREVIEW ===")
for i in range(70, 100, 3):
    q = t3['questions'][i]
    print(f"Q{q['id']}-{q['id']+2}: {str(q.get('passage'))[:120]}...")
