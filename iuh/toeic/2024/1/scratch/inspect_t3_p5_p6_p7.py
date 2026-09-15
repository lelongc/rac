import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total questions: {len(data['questions'])}")
for q in data['questions']:
    qid = q['id']
    if qid in [101, 102, 120, 131, 135, 147, 150, 170, 190]:
        print(f"\n--- Q{qid} ---")
        print("Stem:", q.get('questionText'))
        print("Options:", q.get('options'))
        vocab = q.get('vocabulary', [])
        print(f"Vocab count: {len(vocab)}")
        for v in vocab:
            print(f"  - {v.get('word')}: {v.get('meaning')}")
