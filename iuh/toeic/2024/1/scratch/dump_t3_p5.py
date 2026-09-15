import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    qid = q['id']
    if 101 <= qid <= 130:
        print(f"Q{qid}: stem='{q.get('questionText')}', options={q.get('options')}, curr_vocab={[v['word'] for v in q.get('vocabulary', [])]}")
