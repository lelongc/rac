import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    qid = q['id']
    if 147 <= qid <= 175 and qid in [147, 149, 151, 153, 156, 158, 161, 165, 168, 172]:
        print(f"\n==================== Q{qid} ====================")
        print("PassageTitle:", q.get('passageTitle'))
        print("PassageText:\n", (q.get('passageText') or '')[:500])
