import json, sys
sys.stdout.reconfigure(encoding='utf-8')

for t in [4, 5]:
    print(f"\n==================== TEST {t} Part 3 & 4 Check ====================")
    with open(f'web/data/test{t}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    qs = [q for q in data['questions'] if q['part'] in [3, 4]]
    print(f"Test {t} Part 3 & 4 question count: {len(qs)}")
    
    # Check sample triplet
    for sample_id in [32, 50, 71, 95]:
        q = next((q for q in qs if q['id'] == sample_id), None)
        if q:
            print(f"\n--- Q{q['id']} (Part {q['part']}) ---")
            print(f"  stem: '{q.get('questionText')}'")
            print(f"  opts: {q.get('options')}")
            print(f"  audioClip: {q.get('audioClip')}")
            print(f"  transcript snippet: {(q.get('transcript') or '')[:100]}...")
            print(f"  vocab: {[v.get('word') for v in q.get('vocabulary', [])]}")
