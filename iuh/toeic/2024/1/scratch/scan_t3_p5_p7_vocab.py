import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    qid = q['id']
    if qid >= 101:
        ctx = (q.get('questionText') or '') + ' ' + (q.get('passage') or '') + ' '
        opts = q.get('options', {})
        if isinstance(opts, dict):
            ctx += ' '.join(opts.values())
        ctx_lower = ctx.lower()
        
        vocab = q.get('vocabulary', [])
        mismatched = []
        for v in vocab:
            w = v.get('word', '').strip()
            w_clean = re.sub(r'[^a-zA-Z\s]', '', w).lower()
            tokens = [t for t in w_clean.split() if len(t) > 3]
            if tokens:
                matched = any(t in ctx_lower or t[:4] in ctx_lower for t in tokens)
                if not matched:
                    mismatched.append(w)
            elif w_clean and w_clean not in ctx_lower:
                mismatched.append(w)
        if mismatched or len(vocab) < 3:
            print(f"Q{qid}: count={len(vocab)}, mismatched={mismatched}")
