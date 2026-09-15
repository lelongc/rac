import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

ranges = [
    (32, 34), (35, 37), (38, 40), (41, 43), (44, 46), (47, 49),
    (50, 52), (53, 55), (56, 58), (59, 61), (62, 64), (65, 67), (68, 70),
    (71, 73), (74, 76), (77, 79), (80, 82), (83, 85), (86, 88),
    (89, 91), (92, 94), (95, 97), (98, 100)
]

for s, e in ranges:
    q = next(x for x in t2['questions'] if x['id'] == s)
    print(f"\n==================== Q{s}-Q{e} ====================")
    print("Passage:\n", q.get('passage'))
    for qid in range(s, e + 1):
        cur = next(x for x in t2['questions'] if x['id'] == qid)
        print(f"  Q{qid}: {cur.get('questionText')} | Opts: {cur.get('options')}")
