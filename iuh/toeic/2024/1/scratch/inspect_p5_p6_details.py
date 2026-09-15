import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

for q in t2['questions']:
    if q.get('part') in [5, 6]:
        vocs = q.get('vocabulary') or q.get('vocab') or []
        colls = q.get('collocations') or []
        if len(vocs) < 2 or len(colls) < 2:
            print(f"Q{q['id']} (Part {q['part']}): {q.get('questionText')}")
            print(f"  Ans: {q.get('correctAnswer')} : {q.get('options', {}).get(q.get('correctAnswer'))}")
            print(f"  Vocab ({len(vocs)}): {[v.get('word') for v in vocs]}")
            print(f"  Colloc ({len(colls)}): {[c.get('phrase') for c in colls]}")
            print()
