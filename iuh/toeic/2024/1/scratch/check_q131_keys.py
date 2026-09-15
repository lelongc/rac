import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    if q['id'] in [131, 147]:
        print(f"=== Q{q['id']} keys ===")
        for k, v in q.items():
            if k in ['vocabulary', 'vocab']:
                print(f"  {k}: {len(v)} items")
            elif isinstance(v, str) and len(v) > 100:
                print(f"  {k}: {v[:100]}... (len={len(v)})")
            else:
                print(f"  {k}: {v}")
