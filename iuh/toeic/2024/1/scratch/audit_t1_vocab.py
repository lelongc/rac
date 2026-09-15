import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)

mismatched = []
for q in t1['questions']:
    qid = q['id']
    vocab = q.get('vocabulary') or q.get('vocab') or []
    stem = q.get('questionText') or ''
    opts = ' '.join(q.get('options', {}).values())
    passage = q.get('passage') or q.get('passageText') or ''
    transcript = q.get('transcript') or ''
    combined = (stem + ' ' + opts + ' ' + passage + ' ' + transcript).lower()

    for v in vocab:
        w = v.get('word', '').lower()
        w_parts = [p for p in w.split() if len(p) > 2]
        if w_parts and not any(p in combined for p in w_parts):
            mismatched.append((qid, v.get('word')))

print(f"Test 1 vocab mismatches: {len(mismatched)}: {mismatched[:15]}")
