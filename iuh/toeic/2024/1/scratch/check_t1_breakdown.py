import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)

for part in range(1, 8):
    qs = [q for q in t1['questions'] if q.get('part') == part]
    lt_v = sum(1 for q in qs if len(q.get('vocabulary') or q.get('vocab') or []) < 2)
    lt_c = sum(1 for q in qs if len(q.get('collocations') or []) < 2)
    p7_miss = sum(1 for q in qs if part == 7 and len(q.get('passageText') or '') < 100)
    print(f"Test 1 Part {part} ({len(qs)} Qs): <2 vocab={lt_v}, <2 colloc={lt_c}, p7_miss={p7_miss}")
