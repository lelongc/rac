import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

for q in t2['questions'][:6]:
    qid = q['id']
    print(f"=== Q{qid} ===")
    print('Exp:', q.get('explanation'))
    print('Vocab:', [v.get('word') for v in (q.get('vocabulary') or q.get('vocab') or [])])
    print('Colloc:', q.get('collocations'))
    print('Grammar:', q.get('grammar') or q.get('grammarPoints'))
    print()
