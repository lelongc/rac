import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)
with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)
with open('web/data/vocab_bank.json', encoding='utf-8') as f:
    vb = json.load(f)

vb_map = {item['word'].lower(): item for item in vb}

def analyze_test(t, name):
    print(f"\n=== Analyzing {name} ===")
    p3_p4_qs = [q for q in t['questions'] if q.get('part') in [3, 4]]
    print(f"Total P3/P4 questions: {len(p3_p4_qs)}")
    for q in p3_p4_qs[:5]:
        qid = q['id']
        passage = q.get('passage', '')
        q_text = q.get('questionText', '')
        opts = ' '.join(q.get('options', {}).values())
        combined = f"{passage} {q_text} {opts}".lower()
        words = set(re.findall(r'[a-z]{4,}', combined))
        matched = [w for w in words if w in vb_map]
        print(f"Q{qid}: {len(words)} unique words -> {len(matched)} matched in vocab_bank: {matched[:6]}")

analyze_test(t2, "Test 2")
analyze_test(t3, "Test 3")
