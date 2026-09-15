import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

for q in t3['questions'][:31]:
    qid = q['id']
    print(f"\n--- Q{qid} (Part {q['part']}) ---")
    if q.get('transcript'):
        print("Transcript:", q['transcript'].replace('\n', ' | '))
    else:
        print("Question:", q.get('questionText'))
        print("Options:", q.get('options'))
