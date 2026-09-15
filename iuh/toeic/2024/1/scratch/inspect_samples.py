import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

for qid in [32, 45, 71, 85, 147, 176]:
    q = next(item for item in t2['questions'] if item['id'] == qid)
    print(f"=== Q{qid} (Part {q.get('part')}) ===")
    print('Exp:', q.get('explanation', '')[:120])
    print('Grammar:', q.get('grammar', []) or q.get('grammarPoints', []))
    print('Colloc:', q.get('collocations', []))
    print('Vocab:', [v.get('word') for v in (q.get('vocabulary') or q.get('vocab') or [])])
    print()
