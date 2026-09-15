import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    qid = q['id']
    if qid in [176, 181, 186, 191, 196]:
        print(f"\n==================== Q{qid} ====================")
        print("PassageTitle:", q.get('passageTitle'))
        print("PassageText:\n", (q.get('passageText') or '')[:500])
