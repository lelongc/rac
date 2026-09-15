import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)
with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)
with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

for name, t in [('Test 1', t1), ('Test 2', t2), ('Test 3', t3)]:
    print(f"\n=== {name} ===")
    total_words = 0
    min_words = 999
    max_words = 0
    zero_count = 0
    for q in t['questions']:
        vocab = q.get('vocabulary') or q.get('vocab') or []
        count = len(vocab)
        total_words += count
        if count == 0:
            zero_count += 1
        if count < min_words:
            min_words = count
        if count > max_words:
            max_words = count
    print(f"Total vocab across 200 questions: {total_words} (avg {total_words/200:.1f}/q)")
    print(f"Min: {min_words}, Max: {max_words}, Questions with 0 vocab: {zero_count}")

    # Inspect sample questions
    for qid in [1, 7, 32, 71, 101, 131, 147]:
        q = next((x for x in t['questions'] if x['id'] == qid), None)
        if q:
            vocab = q.get('vocabulary') or q.get('vocab') or []
            print(f"  Q{qid} (Part {q.get('part')}): {len(vocab)} words -> {[w.get('word') for w in vocab[:4]]}")
