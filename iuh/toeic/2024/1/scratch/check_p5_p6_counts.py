import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

for part in [5, 6]:
    qs = [q for q in t2['questions'] if q.get('part') == part]
    for q in qs:
        vocs = q.get('vocabulary') or q.get('vocab') or []
        colls = q.get('collocations') or []
        if len(vocs) < 2 or len(colls) < 2:
            print(f"Q{q['id']} (Part {part}): Vocab count={len(vocs)}, Colloc count={len(colls)}")
