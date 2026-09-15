import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)

for qid in [164, 165, 166, 167, 176, 177, 183, 184]:
    q = next(item for item in t1['questions'] if item['id'] == qid)
    print(f"Q{qid}: passageText len={len(q.get('passageText') or '')}")
