import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    qid = q['id']
    if 32 <= qid <= 100 and (qid - 32) % 3 == 0:
        p_prev = (q.get('passage') or q.get('transcript') or '')[:120].replace('\n', ' ')
        print(f"Q{qid}-{qid+2}: {p_prev}...")
