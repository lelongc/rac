import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    qid = q['id']
    if 131 <= qid <= 146:
        print(f"=== Q{qid} ===")
        print(f"passageId: {q.get('passageId')}")
        print(f"stem: {q.get('questionText')}")
        print(f"options: {q.get('options')}")
        print(f"curr_vocab: {[v['word'] for v in q.get('vocabulary', [])]}")
        if qid in [131, 135, 139, 143]:
            print(f"passageText:\n{q.get('passageText')}\n")
