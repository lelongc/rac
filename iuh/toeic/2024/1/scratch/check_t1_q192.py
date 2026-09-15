import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)

for q in t1['questions']:
    if q['id'] in [191, 192, 193, 194, 195]:
        print(f"Q{q['id']}: passageTextVi={q.get('passageTextVi')}")
