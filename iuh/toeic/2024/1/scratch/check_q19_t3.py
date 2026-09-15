import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

for qid in [19, 20, 21, 22]:
    q = next(x for x in t3['questions'] if x['id'] == qid)
    print(f"\n--- Q{qid} ---")
    print("Transcript:\n", q.get('transcript'))
    print("Vocab:", [w.get('word') for w in (q.get('vocabulary') or q.get('vocab') or [])])
