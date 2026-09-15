import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    qid = q['id']
    if 32 <= qid <= 100:
        if (qid - 32) % 3 == 0 or qid in [32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98]:
            t = q.get('transcript') or q.get('passage') or ''
            print(f"\n==================== Q{qid}-{qid+2} ====================")
            print("Transcript/Passage:\n", t[:400])
        print(f"  Q{qid}: stem='{q.get('questionText')}', opts={list(q.get('options', {}).values())[:3]}")
