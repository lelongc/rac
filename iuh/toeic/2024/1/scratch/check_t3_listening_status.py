import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

for part_no in [1, 2, 3, 4]:
    qs = [q for q in t3['questions'] if q.get('part') == part_no]
    print(f"=== Part {part_no}: count={len(qs)} ===")
    for q in qs[:2]:
        print(f"Q{q['id']}:")
        print("  transcript preview:", (q.get('transcript') or '')[:80].replace('\n', ' '))
        print("  transcriptVi preview:", (q.get('transcriptVi') or '')[:80].replace('\n', ' '))
        print("  passageVi preview:", (q.get('passageVi') or '')[:80].replace('\n', ' '))
