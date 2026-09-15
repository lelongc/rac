import subprocess
import json
import re
import os

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"

def get_page_columns(pno):
    img_path = f"scratch/rc_p{pno}.png"
    if not os.path.exists(img_path):
        return "", ""
    res = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', 'scratch/ocr_boxes.ps1', img_path], capture_output=True, text=True)
    words = []
    for line in res.stdout.splitlines():
        for m in re.finditer(r'([^\s\[]+)\[x=(\d+),y=(\d+)\]', line):
            words.append({'text': m.group(1), 'x': int(m.group(2)), 'y': int(m.group(3))})
    
    left = sorted([w for w in words if w['x'] < 550], key=lambda w: (w['y'], w['x']))
    right = sorted([w for w in words if w['x'] >= 550], key=lambda w: (w['y'], w['x']))
    
    def lines(w_list):
        out = []
        cur = []
        cy = -100
        for w in w_list:
            if abs(w['y'] - cy) > 12:
                if cur:
                    cur.sort(key=lambda x: x['x'])
                    out.append(' '.join([x['text'] for x in cur]))
                cur = [w]
                cy = w['y']
            else:
                cur.append(w)
        if cur:
            cur.sort(key=lambda x: x['x'])
            out.append(' '.join([x['text'] for x in cur]))
        return '\n'.join(out)
        
    return lines(left), lines(right)

parsed_p7 = {}
q_to_page = {}

print("Extracting Part 7 questions from RC pages 8 to 28...")
for pno in range(8, 29):
    l_txt, r_txt = get_page_columns(pno)
    col_texts = [l_txt, r_txt]
    for col in col_texts:
        # split by question numbers like 147., 148. etc
        blocks = re.split(r'\n(?=1\d\d\.\s+)', '\n' + col)
        for b in blocks:
            b = b.strip()
            if not b: continue
            m = re.match(r'^(1\d\d)\.\s+(.*?)(?=\([ABCD]\))', b, re.DOTALL)
            if not m:
                continue
            qid = int(m.group(1))
            stem = " ".join(m.group(2).split())
            opts = {}
            opt_matches = list(re.finditer(r'\(([ABCD])\)\s*([^(\n\r]+(?:\n(?!\([ABCD]\)|1\d\d\.)[^\n\r]+)*)', b))
            for om in opt_matches:
                ltr = om.group(1)
                otxt = " ".join(om.group(2).split())
                # clean trailing page directions
                otxt = re.sub(r'GO ON TO THE NEXT PAGE.*$', '', otxt).strip()
                otxt = re.sub(r'TEST \d.*$', '', otxt).strip()
                opts[ltr] = otxt
            if len(opts) == 4 and 147 <= qid <= 200:
                parsed_p7[qid] = {
                    "stem": stem,
                    "options": opts,
                    "page": pno
                }
                q_to_page[qid] = pno
    print(f"Page {pno} done. Total Qs parsed so far: {len(parsed_p7)}")

print(f"\nCompleted! Total parsed Part 7 questions: {len(parsed_p7)}/54 (target 147-200)")
missing = [q for q in range(147, 201) if q not in parsed_p7]
print(f"Missing Qs: {missing}")

with open("scratch/t2_p7_parsed.json", "w", encoding="utf-8") as f:
    json.dump(parsed_p7, f, ensure_ascii=False, indent=2)
