import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

part = sys.argv[1] if len(sys.argv) > 1 else "1"

if part == "1":
    ranges = [(147, 148), (149, 150), (151, 152), (153, 155), (156, 157), (158, 160)]
elif part == "2":
    ranges = [(161, 163), (164, 167), (168, 171), (172, 175)]
else:
    ranges = [(176, 180), (181, 185), (186, 190), (191, 195), (196, 200)]

for s, e in ranges:
    qs = [q for q in t3['questions'] if s <= q['id'] <= e]
    print(f"\n==================== RANGE {s}-{e} ====================")
    print("PassageText:\n", qs[0].get('passageText'))
    for q in qs:
        print(f"\n--- Q{q['id']} ---")
        print("Question:", q.get('questionText'))
        print("Options:", q.get('options'))
