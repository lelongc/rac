import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    qid = q['id']
    if qid in [131, 135, 139, 143]:
        print(f"=== Q{qid} (Passage group) ===")
        print(f"Passage:\n{q.get('passage')}\n")
        print(f"Q{qid} stem: {q.get('questionText')}, options: {q.get('options')}")
