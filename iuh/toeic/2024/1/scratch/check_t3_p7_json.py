import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    t3 = json.load(f)

p7 = [q for q in t3['questions'] if q['part'] == 7]
print(f"Total Part 7 questions: {len(p7)}")

for q in p7[:10]:
    print(f"Q{q['id']} [ans={q.get('correctAnswer')}]: {q.get('questionText')}")
    print(f"   Opts: {q.get('options')}")
    print(f"   Image: {q.get('image')} | pageImage: {q.get('pageImage')} | pageImages: {q.get('pageImages')}")
