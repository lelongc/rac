import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)

for part in [1, 2, 3, 4, 5, 6, 7]:
    q = next(item for item in t1['questions'] if item.get('part') == part)
    qid = q['id']
    print(f"=== T1 Part {part} (Q{qid}) ===")
    for k in ['passage', 'passageVi', 'questionText', 'questionTextVi', 'options', 'optionsVi', 'transcript', 'transcriptVi']:
        val = str(q.get(k, ''))
        print(f"  {k}: {val[:80]}...")
