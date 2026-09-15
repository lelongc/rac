import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    t3 = json.load(f)

p6 = [q for q in t3['questions'] if q['part'] == 6]
print(f"Total Part 6 questions: {len(p6)}")
for q in p6:
    print(f"Q{q['id']} ans={q.get('correctAnswer')}: text={q.get('questionText')}")
    print(f"   Passage len={len(q.get('passageText', ''))}, Title={q.get('passageTitle')}")
    print(f"   Options: {q.get('options')}")
