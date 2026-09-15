import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    t2 = json.load(f)

questions = t2['questions']

print("=== PART 5 INSPECTION (Q101-Q130) ===")
p5 = [q for q in questions if q['part'] == 5]
print(f"Total Part 5 questions: {len(p5)}")
for q in p5:
    opts = q.get('options', {})
    qtext = q.get('questionText', '')
    if len(opts) != 4 or not qtext:
        print(f"  Issue Q{q['id']}: opts={len(opts)}, qtext={qtext[:30]}")
    # print first 2 and last 2 samples
    if q['id'] in [101, 102, 129, 130]:
        print(f"  Q{q['id']}: {qtext}")
        print(f"    Options: {opts}")
        print(f"    Correct: {q.get('correctAnswer')}")

print("\n=== PART 6 INSPECTION (Q131-Q146) ===")
p6 = [q for q in questions if q['part'] == 6]
print(f"Total Part 6 questions: {len(p6)}")
for q in p6:
    opts = q.get('options', {})
    qtext = q.get('questionText', '')
    if len(opts) != 4 or not qtext:
        print(f"  Issue Q{q['id']}: opts={len(opts)}, qtext={qtext[:30]}")
    if q['id'] in [131, 132, 145, 146]:
        print(f"  Q{q['id']}: {qtext}")
        print(f"    Options: {opts}")
        print(f"    Correct: {q.get('correctAnswer')}")
        print(f"    Passage: {repr(q.get('passage', ''))[:80]}...")

print("\n=== PART 7 INSPECTION (Q147-Q200) ===")
p7 = [q for q in questions if q['part'] == 7]
print(f"Total Part 7 questions: {len(p7)}")
for q in p7:
    opts = q.get('options', {})
    qtext = q.get('questionText', '')
    img = q.get('image')
    img_exists = os.path.exists(os.path.join('web', img)) if img else False
    if len(opts) != 4 or not qtext or not img_exists:
        print(f"  Issue Q{q['id']}: opts={len(opts)}, qtext={qtext[:30]}, img_exists={img_exists}")
    if q['id'] in [147, 148, 199, 200]:
        print(f"  Q{q['id']}: {qtext}")
        print(f"    Options: {opts}")
        print(f"    Image: {img}")
        print(f"    Correct: {q.get('correctAnswer')}")
