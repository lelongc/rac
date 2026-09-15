import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)
with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)
with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

print("=== TEST 1 Q1 VOCAB ===")
q1_t1 = next(q for q in t1['questions'] if q['id'] == 1)
print(json.dumps(q1_t1.get('vocabulary') or q1_t1.get('vocab'), ensure_ascii=False, indent=2))

print("\n=== TEST 2 Q1 VOCAB ===")
q1_t2 = next(q for q in t2['questions'] if q['id'] == 1)
print(json.dumps(q1_t2.get('vocabulary') or q1_t2.get('vocab'), ensure_ascii=False, indent=2))

print("\n=== TEST 3 Q1 VOCAB ===")
q1_t3 = next(q for q in t3['questions'] if q['id'] == 1)
print(json.dumps(q1_t3.get('vocabulary') or q1_t3.get('vocab'), ensure_ascii=False, indent=2))

print("\n=== TEST 1 Q101 VOCAB ===")
q101_t1 = next(q for q in t1['questions'] if q['id'] == 101)
print(json.dumps(q101_t1.get('vocabulary') or q101_t1.get('vocab'), ensure_ascii=False, indent=2))

print("\n=== TEST 2 Q101 VOCAB ===")
q101_t2 = next(q for q in t2['questions'] if q['id'] == 101)
print(json.dumps(q101_t2.get('vocabulary') or q101_t2.get('vocab'), ensure_ascii=False, indent=2))

print("\n=== TEST 3 Q101 VOCAB ===")
q101_t3 = next(q for q in t3['questions'] if q['id'] == 101)
print(json.dumps(q101_t3.get('vocabulary') or q101_t3.get('vocab'), ensure_ascii=False, indent=2))
