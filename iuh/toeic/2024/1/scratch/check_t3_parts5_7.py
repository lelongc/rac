import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

for part_no in [5, 6, 7]:
    qs = [q for q in t3['questions'] if q.get('part') == part_no]
    print(f"=== Part {part_no}: count={len(qs)} ===")
    for q in qs[:2]:
        print(f"Q{q['id']}:")
        print("  questionText:", q.get('questionText'))
        print("  questionTextVi:", q.get('questionTextVi'))
        print("  options:", q.get('options'))
        print("  optionsVi:", q.get('optionsVi'))
        if 'passageText' in q:
            print("  passageText preview:", (q.get('passageText') or '')[:60])
        if 'passageTextVi' in q:
            print("  passageTextVi preview:", (q.get('passageTextVi') or '')[:60])
        if 'passageVi' in q:
            print("  passageVi preview:", (q.get('passageVi') or '')[:60])
        if 'passage' in q:
            print("  passage preview:", (q.get('passage') or '')[:60])
