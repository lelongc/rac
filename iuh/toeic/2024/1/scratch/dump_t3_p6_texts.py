import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

print("=== PART 6 ENGLISH TEXTS ===")
for r in ['131_134', '135_138', '139_142', '143_146']:
    s, e = map(int, r.split('_'))
    qs = [q for q in t3['questions'] if s <= q['id'] <= e]
    print(f"\n--- Range {r} ---")
    print("PassageText:\n", qs[0].get('passageText'))
    for q in qs:
        print(f"  Q{q['id']}: {q.get('questionText')} | Options: {q.get('options')}")

