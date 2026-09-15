import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

for qid in [116, 138, 140, 141, 145, 146]:
    q = next(item for item in t2['questions'] if item['id'] == qid)
    print(f"Q{qid}: Vocab: {[v.get('word') for v in q.get('vocabulary', [])]}")
    print(f"      Colloc: {[c.get('phrase') for c in q.get('collocations', [])]}")
