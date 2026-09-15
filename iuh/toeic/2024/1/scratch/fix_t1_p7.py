import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)

q191 = next(q for q in t1['questions'] if q['id'] == 191)
full_passage_vi = q191.get('passageTextVi')

for q in t1['questions']:
    if 191 <= q['id'] <= 195:
        q['passageTextVi'] = full_passage_vi
        q['passageVi'] = full_passage_vi

with open('web/data/test1.json', 'w', encoding='utf-8') as f:
    json.dump(t1, f, ensure_ascii=False, indent=2)

print("Fixed Test 1 Q191-195 passageTextVi to have the full triple passage translation!")
