import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    qid = q['id']
    if qid in [33, 91, 164]:
        print(f"\n=== Q{qid} text ===")
        print("questionText:", q.get('questionText'))
        print("options:", q.get('options'))
        print("passageText/passage:", (q.get('passageText') or q.get('passage') or '')[:100])
        print("transcript:", (q.get('transcript') or '')[:100])
