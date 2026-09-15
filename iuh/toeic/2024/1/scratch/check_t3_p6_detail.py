import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

p6_qs = [q for q in t3['questions'] if q.get('part') == 6]
print(f"Total Part 6 questions: {len(p6_qs)}")
ranges = ['131_134', '135_138', '139_142', '143_146']

for r in ranges:
    s, e = map(int, r.split('_'))
    q_s = next(q for q in p6_qs if q['id'] == s)
    print(f"\n=== Range {r} ===")
    print("passage preview:", (q_s.get('passage') or '')[:120].replace('\n', ' '))
    print("passageText preview:", (q_s.get('passageText') or '')[:120].replace('\n', ' '))
    print("passageVi preview:", (q_s.get('passageVi') or '')[:120].replace('\n', ' '))
    print("passageTextVi preview:", (q_s.get('passageTextVi') or '')[:120].replace('\n', ' '))
    for q in [q for q in p6_qs if s <= q['id'] <= e]:
        print(f"  Q{q['id']}: opts={q.get('options')} | optsVi={q.get('optionsVi')}")
