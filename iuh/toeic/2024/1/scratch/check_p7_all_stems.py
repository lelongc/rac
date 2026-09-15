import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    t3 = json.load(f)

for q in t3['questions']:
    if q.get('part') == 7:
        qid = q['id']
        stem = q.get('questionText', '')
        # Check if stem looks unclean
        print(f"Q{qid}: {stem}")
