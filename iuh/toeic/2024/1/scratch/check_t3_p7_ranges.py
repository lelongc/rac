import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

p7_qs = [q for q in t3['questions'] if q.get('part') == 7]
print(f"Total Part 7 questions: {len(p7_qs)}")

# Group by passageText or range
ranges = [
    (147, 148), (149, 150), (151, 152), (153, 155), (156, 157),
    (158, 160), (161, 163), (164, 167), (168, 171), (172, 175),
    (176, 180), (181, 185), (186, 190), (191, 195), (196, 200)
]

for s, e in ranges:
    qs = [q for q in p7_qs if s <= q['id'] <= e]
    q_s = qs[0]
    print(f"\n=== Range {s}-{e} ({len(qs)} questions) ===")
    print("passageTitle:", q_s.get('passageTitle'))
    print("passageText preview:", (q_s.get('passageText') or '')[:100].replace('\n', ' '))
    print("passageTextVi preview:", (q_s.get('passageTextVi') or '')[:100].replace('\n', ' '))
    print(f"Q{s} questionText:", q_s.get('questionText'))
    print(f"Q{s} questionTextVi:", q_s.get('questionTextVi'))
    print(f"Q{s} optsVi:", q_s.get('optionsVi'))
