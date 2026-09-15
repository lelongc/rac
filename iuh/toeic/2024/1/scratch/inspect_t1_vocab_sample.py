import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Test 1 question count: {len(data['questions'])}")
v_counts = [len(q.get('vocabulary', [])) for q in data['questions']]
print(f"Test 1 vocab count stats: min={min(v_counts)}, max={max(v_counts)}, avg={sum(v_counts)/len(v_counts):.2f}")

for sample_id in [1, 7, 32, 71, 101, 131, 147]:
    for q in data['questions']:
        if q['id'] == sample_id:
            print(f"\n--- Test 1 Q{sample_id} ---")
            print("Question stem:", q.get('questionText'))
            print("Vocab count:", len(q.get('vocabulary', [])))
            for v in q.get('vocabulary', [])[:4]:
                print(f"  * {v.get('word')} ({v.get('pos')}, {v.get('ipa')}): {v.get('meaning')}")
