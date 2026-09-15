import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

ans = json.load(open('all_tests_answers.json', encoding='utf-8'))['test1']
with open('web/data/test1.json', 'r', encoding='utf-8') as f:
    t1_data = json.load(f)

print("Test 1 mismatches:")
for q in t1_data['questions']:
    qid = str(q['id'])
    curr = q.get('correctAnswer')
    off = ans.get(qid)
    if curr != off:
        print(f"Q{qid}: current={curr}, official={off}, part={q.get('part')}")
