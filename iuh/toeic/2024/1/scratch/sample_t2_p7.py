import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

p7_qs = [q for q in t2['questions'] if q.get('part') == 7]
print(f"Total Test 2 Part 7 questions: {len(p7_qs)}")
for q in p7_qs[::4]: # every 4th question
    print(f"Q{q['id']}: {q.get('questionText')} | Opts: {q.get('options')}")
