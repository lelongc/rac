import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    qid = q['id']
    if 32 <= qid <= 70 and qid in [38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68]:
        t = q.get('transcript') or q.get('passage') or ''
        print(f"\n==================== Q{qid}-{qid+2} ====================")
        print("Transcript:\n", t[:350])
