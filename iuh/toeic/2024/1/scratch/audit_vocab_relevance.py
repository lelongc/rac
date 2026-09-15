import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)
with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

for name, t in [("Test 2", t2), ("Test 3", t3)]:
    mismatched = []
    sparse = []
    for q in t['questions']:
        qid = q['id']
        vocab = q.get('vocabulary') or q.get('vocab') or []
        if len(vocab) < 3:
            sparse.append(qid)

        # Build combined text of the question
        stem = q.get('questionText') or ''
        opts = ' '.join(q.get('options', {}).values())
        passage = q.get('passage') or q.get('passageText') or ''
        combined = (stem + ' ' + opts + ' ' + passage).lower()

        for v in vocab:
            w = v.get('word', '').lower()
            # Check if main words of w appear in combined
            w_parts = [p for p in w.split() if len(p) > 2]
            if w_parts and not any(p in combined for p in w_parts):
                mismatched.append((qid, v.get('word')))

    print(f"\n=== {name} ===")
    print(f"Questions with < 3 vocab words: {len(sparse)}/200: {sparse[:10]}...")
    print(f"Vocab words not found in question/options/passage: {len(mismatched)}: {mismatched[:10]}...")
