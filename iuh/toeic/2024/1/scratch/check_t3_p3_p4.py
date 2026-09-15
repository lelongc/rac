import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    t3 = json.load(f)

for pno in [3, 4]:
    print(f"\n=== INSPECTING PART {pno} ===")
    p_qs = [q for q in t3['questions'] if q['part'] == pno]
    for q in p_qs:
        qid = q['id']
        stem = q.get('questionText', '')
        opts = q.get('options', {})
        # check if options have strange text or korean
        has_garbage = False
        for s in [stem] + list(opts.values()):
            if any(ch for ch in s if '\uac00' <= ch <= '\ud7a3' or '\u1100' <= ch <= '\u11ff' or '\u3130' <= ch <= '\u318f' or '®' in s or '§' in s or 'Ml' in s):
                has_garbage = True
                break
        if has_garbage or len(opts) != 4 or 'Question ' in stem:
            print(f"  Q{qid} defect: text={stem[:50]}... | opts={opts}")
