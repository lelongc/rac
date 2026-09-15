import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)
with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

for name, t in [("Test 2", t2), ("Test 3", t3)]:
    print(f"\n=== {name} Samples ===")
    for qid in [1, 2, 7, 8, 15, 32, 50, 71, 101, 105, 115, 131, 147, 160]:
        q = next(x for x in t['questions'] if x['id'] == qid)
        vocab = q.get('vocabulary') or q.get('vocab') or []
        stem = q.get('questionText') or ''
        opts = list(q.get('options', {}).values())
        passage = (q.get('passage') or q.get('passageText') or '')[:100]
        words = [w.get('word') for w in vocab]
        print(f"Q{qid} (Part {q['part']}): {words}")
        print(f"   Stem: {stem[:60]} | Opts: {opts[:2]}")
