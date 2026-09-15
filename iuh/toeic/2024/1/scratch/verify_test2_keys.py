import fitz
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def parse_test2_answers():
    # LC TEST 2 is on Page 2, x between 300 and 550, y between 90 and 380
    doc_lc = fitz.open('giai/ĐÁP ÁN ETS 2024 LC.pdf')
    p_lc = doc_lc[1]
    blocks_lc = p_lc.get_text("blocks")
    lc_answers = {}
    for b in blocks_lc:
        x0, y0, x1, y1, text = b[:5]
        if 300 <= x0 <= 550 and 90 <= y0 <= 380:
            # find all (Q, Ans)
            matches = re.findall(r'(\d+)\s*\(([A-D])\)', text)
            for q_num, ans in matches:
                lc_answers[int(q_num)] = ans

    # RC TEST 2 is on Page 2, x between 300 and 550, y between 90 and 380
    doc_rc = fitz.open('giai/ĐÁP ÁN ETS 2024 RC.pdf')
    p_rc = doc_rc[1]
    blocks_rc = p_rc.get_text("blocks")
    rc_answers = {}
    for b in blocks_rc:
        x0, y0, x1, y1, text = b[:5]
        if 300 <= x0 <= 550 and 90 <= y0 <= 380:
            matches = re.findall(r'(\d+)\s*\(([A-D])\)', text)
            for q_num, ans in matches:
                rc_answers[int(q_num)] = ans

    return lc_answers, rc_answers

lc_ans, rc_ans = parse_test2_answers()
print(f"Parsed LC answers for Test 2: {len(lc_ans)}/100")
print(f"Parsed RC answers for Test 2: {len(rc_ans)}/100")

# Compare with test2.json
import json
with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    t2_data = json.load(f)

mismatches = []
for q in t2_data['questions']:
    qid = q['id']
    actual = q.get('correctAnswer')
    expected = None
    if qid <= 100:
        expected = lc_ans.get(qid)
    else:
        expected = rc_ans.get(qid)
    
    if expected is not None and actual != expected:
        mismatches.append((qid, actual, expected))

print(f"\nMismatches with official answer keys: {len(mismatches)}")
for m in mismatches:
    print(f"  Q{m[0]}: current={m[1]}, official={m[2]}")
