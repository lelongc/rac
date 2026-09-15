import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    t2 = json.load(f)

print("=== PART 6 DETAILED ===")
for q in t2['questions']:
    if q['part'] == 6:
        print(f"Q{q['id']}: text={q.get('questionText')} | opts={q.get('options')}")

print("\n=== PART 7 DETAILED ===")
for q in t2['questions']:
    if q['part'] == 7:
        opts = q.get('options', {})
        print(f"Q{q['id']}: text={q.get('questionText')} | image={q.get('image')} | opts_keys={list(opts.keys())}")
        if any('Question ' in str(v) or 'incomplete' in str(v) for v in opts.values()):
            print(f"   WARNING: Q{q['id']} has incomplete in options!")
        if 'Question ' in q.get('questionText', ''):
            print(f"   WARNING: Q{q['id']} has dummy question text!")
