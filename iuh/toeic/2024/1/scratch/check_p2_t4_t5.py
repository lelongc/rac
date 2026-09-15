import json, sys
sys.stdout.reconfigure(encoding='utf-8')

for t in [4, 5]:
    print(f"\n==================== TEST {t} Part 2 Check ====================")
    with open(f'web/data/test{t}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    qs = [q for q in data['questions'] if q['part'] == 2]
    print(f"Test {t} Part 2 question count: {len(qs)} (Q{qs[0]['id']} - Q{qs[-1]['id']})")
    for q in qs[:4]:
        print(f"  Q{q['id']}: stem='{q.get('questionText')}'")
        print(f"      opts={q.get('options')}")
        print(f"      ans={q.get('correctAnswer')}, audio={q.get('audioClip')}")
        print(f"      transcript snippet: {(q.get('transcript') or '')[:70]}")
        print(f"      vocab: {[v.get('word') for v in q.get('vocabulary', [])]}")
