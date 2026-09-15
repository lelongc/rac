import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

for q in t3['questions']:
    colls = q.get('collocations') or []
    if len(colls) < 2:
        qid = q['id']
        part = q.get('part')
        print(f"T3 Q{qid} (Part {part}): {[c.get('phrase') for c in colls]}")
