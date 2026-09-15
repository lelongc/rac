import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test2.json', 'r', encoding='utf-8') as f:
    ocr = json.load(f)

with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    t2 = json.load(f)

t2_qmap = {q['id']: q for q in t2['questions']}

print("=== CHECKING ALL PART 7 QUESTIONS (147-200) OPTIONS ===")
for qid in range(147, 201):
    q = t2_qmap.get(qid)
    opts = q.get('options', {}) if q else {}
    print(f"Q{qid}: {q.get('questionText')}")
    for k in ['A', 'B', 'C', 'D']:
        print(f"  ({k}) {opts.get(k)}")
