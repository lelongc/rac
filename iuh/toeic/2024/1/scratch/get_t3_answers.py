import fitz
import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

def parse_test3_answers():
    # LC TEST 3 is on Page 2, x between 50 and 260, y between 440 and 740
    doc_lc = fitz.open('giai/ĐÁP ÁN ETS 2024 LC.pdf')
    p_lc = doc_lc[1]
    blocks_lc = p_lc.get_text("blocks")
    lc_answers = {}
    for b in blocks_lc:
        x0, y0, x1, y1, text = b[:5]
        if 40 <= x0 <= 270 and 440 <= y0 <= 740:
            matches = re.findall(r'(\d+)\s*\(([A-D])\)', text)
            for q_num, ans in matches:
                lc_answers[int(q_num)] = ans

    # RC TEST 3 is on Page 2, x between 50 and 270, y between 440 and 740
    doc_rc = fitz.open('giai/ĐÁP ÁN ETS 2024 RC.pdf')
    p_rc = doc_rc[1]
    blocks_rc = p_rc.get_text("blocks")
    rc_answers = {}
    for b in blocks_rc:
        x0, y0, x1, y1, text = b[:5]
        if 40 <= x0 <= 270 and 440 <= y0 <= 740:
            matches = re.findall(r'(\d+)\s*\(([A-D])\)', text)
            for q_num, ans in matches:
                rc_answers[int(q_num)] = ans

    return lc_answers, rc_answers

lc_ans, rc_ans = parse_test3_answers()
print(f"Parsed LC answers for Test 3: {len(lc_ans)}/100")
print(f"Parsed RC answers for Test 3: {len(rc_ans)}/100")

# Print first 10 and last 10 of each
print("LC 1-10:", [lc_ans.get(i) for i in range(1, 11)])
print("LC 91-100:", [lc_ans.get(i) for i in range(91, 101)])
print("RC 101-110:", [rc_ans.get(i) for i in range(101, 111)])
print("RC 191-200:", [rc_ans.get(i) for i in range(191, 201)])

# Save to scratch/test3_official_answers.json
t3_ans = {}
for k, v in lc_ans.items():
    t3_ans[str(k)] = v
for k, v in rc_ans.items():
    t3_ans[str(k)] = v

with open('scratch/test3_official_answers.json', 'w', encoding='utf-8') as f:
    json.dump(t3_ans, f, indent=2)
print("Saved scratch/test3_official_answers.json successfully!")
