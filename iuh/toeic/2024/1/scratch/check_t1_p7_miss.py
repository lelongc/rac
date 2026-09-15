import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)

for q in t1['questions']:
    if q.get('part') == 7 and len(q.get('passageText') or '') < 100:
        print(f"Q{q['id']}: passageText len={len(q.get('passageText') or '')}")
