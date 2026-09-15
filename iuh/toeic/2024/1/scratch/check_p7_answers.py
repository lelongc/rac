import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

for q in t3['questions']:
    if q.get('part') == 7:
        print(f"Q{q['id']}: {q.get('correctAnswer')}", end=' ')
print()
