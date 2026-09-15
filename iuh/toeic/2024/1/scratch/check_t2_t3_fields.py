import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

for t_num in [2, 3]:
    with open(f'web/data/test{t_num}.json', encoding='utf-8') as f:
        t = json.load(f)
    print(f"\n==================== TEST {t_num} ====================")
    for qid in [1, 7, 32, 71, 101, 131, 147]:
        q = next(item for item in t['questions'] if item['id'] == qid)
        print(f"--- Q{qid} (Part {q['part']}) ---")
        print(f"  questionText: {q.get('questionText')}")
        print(f"  questionTextVi: {q.get('questionTextVi')}")
        print(f"  options: {q.get('options')}")
        print(f"  optionsVi: {q.get('optionsVi')}")
        print(f"  passage: {str(q.get('passage'))[:60]}...")
        print(f"  passageVi: {str(q.get('passageVi'))[:60]}...")
        print(f"  transcript: {str(q.get('transcript'))[:60]}...")
        print(f"  transcriptVi: {str(q.get('transcriptVi'))[:60]}...")
        if q['part'] == 7:
            print(f"  passageTitle: {q.get('passageTitle')}")
            print(f"  passageText: {str(q.get('passageText'))[:60]}...")
            print(f"  passageTextVi: {str(q.get('passageTextVi'))[:60]}...")
