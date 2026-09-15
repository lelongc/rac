import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    if q['id'] in [1, 19, 32, 35]:
        print(f"\n=== Q{q['id']} keys and sample values ===")
        for k, v in q.items():
            if k in ['vocabulary', 'vocab']:
                print(f"  {k}: {[x['word'] for x in v]}")
            elif isinstance(v, str) and len(v) > 80:
                print(f"  {k}: {v[:80]}... (len={len(v)})")
            elif isinstance(v, (dict, list)):
                print(f"  {k}: {str(v)[:80]}")
            else:
                print(f"  {k}: {v}")
