import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

t3_extra_colls = {
    1: {"phrase": "holding a roller", "meaning": "cầm cây lăn sơn"},
    2: {"phrase": "reaching into a cabinet", "meaning": "với tay vào trong tủ"},
    4: {"phrase": "wait in line", "meaning": "xếp hàng chờ đợi"},
    5: {"phrase": "safety helmet", "meaning": "mũ bảo hộ lao động"},
    6: {"phrase": "outdoor patio", "meaning": "khoảng sân hiên ngoài trời"}
}

for q in t3['questions']:
    qid = q['id']
    if qid in t3_extra_colls:
        colls = q.get('collocations', [])
        if not any(c['phrase'] == t3_extra_colls[qid]['phrase'] for c in colls):
            colls.append(t3_extra_colls[qid])
        q['collocations'] = colls

with open('web/data/test3.json', 'w', encoding='utf-8') as f:
    json.dump(t3, f, ensure_ascii=False, indent=2)

print("Updated Test 3 Part 1 extra collocations successfully!")
