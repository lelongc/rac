import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

p7_qs = [q for q in t2['questions'] if q.get('part') == 7]

ranges = [
    (147, 148), (149, 150), (151, 152), (153, 154), (155, 157),
    (158, 160), (161, 163), (164, 167), (168, 171), (172, 175),
    (176, 180), (181, 185), (186, 190), (191, 195), (196, 200)
]

for start, end in ranges:
    group = [q for q in p7_qs if start <= q['id'] <= end]
    first = group[0] if group else None
    print(f"=== Range {start}-{end} ({len(group)} Qs) ===")
    if first:
        ptext = first.get('passageText', '')
        print("PassageText length:", len(ptext), "Preview:", ptext[:120].replace('\n', ' '))
        for q in group:
            print(f"  Q{q['id']}: {q.get('questionText')} | Ans: {q.get('correctAnswer')}: {q.get('options', {}).get(q.get('correctAnswer'))}")
    print()
