import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    t3 = json.load(f)

with open('scratch/test3_official_answers.json', 'r', encoding='utf-8') as f:
    official_ans = json.load(f)

questions = t3.get('questions', [])
print(f"Total questions in test3.json: {len(questions)}")

# 1. Check answer matches
mismatches = []
for q in questions:
    qid = str(q['id'])
    cur = q.get('correctAnswer')
    exp = official_ans.get(qid)
    if cur != exp:
        mismatches.append((qid, cur, exp))
print(f"Answer key mismatches vs official: {len(mismatches)}")
for m in mismatches[:10]:
    print(f"  Q{m[0]}: current={m[1]}, expected={m[2]}")

# 2. Check Part 1 images
print("\n--- Part 1 Images & Questions ---")
for q in questions[:6]:
    print(f"Q{q['id']}: img={q.get('image')}, ans={q.get('correctAnswer')}, stem={q.get('questionText')[:40]}...")
    opts = q.get('options', {})
    for k in sorted(opts.keys()):
        print(f"   ({k}) {opts[k]}")

# 3. Check Part 5 questions for dummy placeholders
print("\n--- Part 5 Placeholders ---")
p5_placeholders = []
for q in questions:
    if q.get('part') == 5:
        qtext = q.get('questionText', '')
        if 'incomplete sentence' in qtext.lower() or 'question ' in qtext.lower() or not qtext.strip():
            p5_placeholders.append((q['id'], qtext))
print(f"Part 5 placeholder stems: {len(p5_placeholders)}/30")
for p in p5_placeholders[:5]:
    print(f"  Q{p[0]}: {p[1]}")

# 4. Check Part 6 passages
print("\n--- Part 6 Passages ---")
p6_empty = []
for q in questions:
    if q.get('part') == 6:
        ptext = q.get('passageText', '')
        if not ptext.strip():
            p6_empty.append(q['id'])
print(f"Part 6 empty passageText: {len(p6_empty)}/16")

# 5. Check Part 7 images and duplicate options
print("\n--- Part 7 Check ---")
p7_images = {}
prev_opts = None
p7_dup_opts = []
for q in questions:
    if q.get('part') == 7:
        qid = q['id']
        img = q.get('image') or q.get('pageImage')
        p7_images[qid] = img
        opts = tuple(sorted(q.get('options', {}).values()))
        if opts == prev_opts:
            p7_dup_opts.append(qid)
        prev_opts = opts

print(f"Part 7 duplicate options: {p7_dup_opts}")
print("Part 7 sample images:")
for qid in [147, 148, 149, 150, 161, 181, 196, 200]:
    print(f"  Q{qid}: {p7_images.get(qid)}")
