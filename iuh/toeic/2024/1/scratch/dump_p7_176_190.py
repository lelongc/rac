import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

for s, e in [(176, 180), (181, 185), (186, 190)]:
    qs = [q for q in t3['questions'] if s <= q['id'] <= e]
    print(f"\n==================== RANGE {s}-{e} ====================")
    print("PassageText:\n", qs[0].get('passageText'))
    for q in qs:
        print(f"\n--- Q{q['id']} ---")
        print("Question:", q.get('questionText'))
        print("Options:", q.get('options'))
