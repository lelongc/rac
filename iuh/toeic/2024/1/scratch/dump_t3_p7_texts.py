import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

ranges = [
    (147, 148), (149, 150), (151, 152), (153, 155), (156, 157),
    (158, 160), (161, 163), (164, 167), (168, 171), (172, 175),
    (176, 180), (181, 185), (186, 190), (191, 195), (196, 200)
]

print("=== PART 7 ENGLISH PASSAGES & QUESTIONS ===")
for s, e in ranges:
    qs = [q for q in t3['questions'] if s <= q['id'] <= e]
    print(f"\n==================== RANGE {s}-{e} ====================")
    print("PassageText:\n", qs[0].get('passageText'))
    for q in qs:
        print(f"\n--- Q{q['id']} ---")
        print("Question:", q.get('questionText'))
        print("Options:", q.get('options'))
