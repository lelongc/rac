import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    t2 = json.load(f)

print("=== PART 4 INSPECTION (Q71-Q100) ===")
p4_questions = [q for q in t2['questions'] if q['part'] == 4]
print(f"Total Part 4 questions: {len(p4_questions)}")

groups = {}
for q in p4_questions:
    clip = q.get('audioClip', '')
    if clip not in groups:
        groups[clip] = []
    groups[clip].append(q)

print(f"Total audio groups: {len(groups)}")
for clip, qlist in sorted(groups.items()):
    q_ids = [q['id'] for q in qlist]
    has_img = [q.get('image') for q in qlist if q.get('image')]
    print(f"Clip: {clip.split('/')[-1]} -> Questions: {q_ids} | Images: {has_img}")
    for q in qlist:
        opts = q.get('options', {})
        if len(opts) != 4:
            print(f"  ERROR: Q{q['id']} has {len(opts)} options!")
        if not q.get('questionText'):
            print(f"  ERROR: Q{q['id']} empty questionText!")
        if not q.get('transcript'):
            print(f"  ERROR: Q{q['id']} empty transcript!")

# Check graphics in Part 4
print("\n--- Graphic questions in Part 4 ---")
for q in p4_questions:
    if q.get('image'):
        img_path = os.path.join('web', q['image'])
        print(f"Q{q['id']} image: {q['image']} (exists: {os.path.exists(img_path)}, size: {os.path.getsize(img_path) if os.path.exists(img_path) else 0})")
        print(f"   Question text: {q['questionText']}")
