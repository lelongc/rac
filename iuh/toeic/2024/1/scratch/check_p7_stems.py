import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test2.json', 'r', encoding='utf-8') as f:
    ocr = json.load(f)

with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    t2 = json.load(f)

t2_qmap = {q['id']: q for q in t2['questions']}

# Find all question numbers in OCR text
for pno, text in sorted(ocr.items(), key=lambda x: int(x[0])):
    if int(pno) < 9: # Part 7 starts around page 9/10
        continue
    # look for questions like 147., 148., etc.
    q_matches = list(re.finditer(r'(\b1[4-9]\d\b|\b200\b)\.?\s+([A-Z][^\n\(\)]+)', text))
    for m in q_matches:
        qid = int(m.group(1))
        qstem_ocr = m.group(2).strip()
        cur_q = t2_qmap.get(qid)
        cur_stem = cur_q.get('questionText', '') if cur_q else ''
        print(f"P{pno} Q{qid}:")
        print(f"   OCR:  {qstem_ocr[:70]}")
        print(f"   JSON: {cur_stem[:70]}")
        if len(qstem_ocr) > len(cur_stem) + 5 or len(cur_stem) > len(qstem_ocr) + 5:
            print(f"   >>> DIFFERENCE IN STEM LENGTH <<<")
