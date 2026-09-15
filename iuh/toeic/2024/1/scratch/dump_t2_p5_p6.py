import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

print("=== TEST 2 PART 5 & 6 SAMPLES ===")
for qid in range(101, 147):
    q = next(x for x in t2['questions'] if x['id'] == qid)
    print(f"Q{qid} (Part {q['part']}): {q.get('questionText')} | Ans: {q.get('correctAnswer')} | Opts: {q.get('options')}")
