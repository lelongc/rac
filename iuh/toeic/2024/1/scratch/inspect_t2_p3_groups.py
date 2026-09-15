import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

p3_qs = [q for q in t2['questions'] if q.get('part') == 3]

# Print grouped by 3
for i in range(0, len(p3_qs), 3):
    group = p3_qs[i:i+3]
    first = group[0]
    print(f"=== Questions {group[0]['id']}-{group[-1]['id']} ===")
    print("Passage:", first.get('passage', '')[:200] + "...")
    for q in group:
        print(f"  Q{q['id']}: {q.get('questionText')} | Ans: {q.get('correctAnswer')}: {q.get('options', {}).get(q.get('correctAnswer'))}")
    print()
