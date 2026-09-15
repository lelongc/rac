import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

few_vocab = []
missing_fields = []
mismatched_vocab = []

for q in data['questions']:
    qid = q['id']
    vocab = q.get('vocabulary', [])
    if len(vocab) < 3:
        few_vocab.append((qid, len(vocab)))
    
    # build full text of question context
    ctx = (q.get('questionText') or '') + ' '
    ctx += (q.get('passage') or '') + ' '
    ctx += (q.get('transcript') or '') + ' '
    opts = q.get('options', {})
    if isinstance(opts, dict):
        ctx += ' '.join(opts.values()) + ' '
    elif isinstance(opts, list):
        for o in opts:
            if isinstance(o, dict):
                ctx += o.get('text', '') + ' '
            else:
                ctx += str(o) + ' '
    
    ctx_lower = ctx.lower()
    
    for v in vocab:
        w = v.get('word', '').strip()
        ipa = v.get('ipa', '').strip()
        pos = v.get('pos', '').strip()
        meaning = v.get('meaning', '').strip()
        example = v.get('example', '').strip()
        
        if not (w and ipa and pos and meaning and example):
            missing_fields.append((qid, w))
            
        # check relevance: at least one word from w should match ctx
        # for multi-word phrases (e.g. "customer service"), check if any key word is in ctx
        w_clean = re.sub(r'[^a-zA-Z\s]', '', w).lower()
        w_tokens = [tok for tok in w_clean.split() if len(tok) > 3]
        if w_tokens:
            matched = any(tok in ctx_lower for tok in w_tokens)
            if not matched:
                # also check root/stem
                matched = any(tok[:4] in ctx_lower for tok in w_tokens if len(tok) >= 5)
            if not matched:
                mismatched_vocab.append((qid, w))
        else:
            if w_clean and w_clean not in ctx_lower:
                mismatched_vocab.append((qid, w))

print(f"Total questions: {len(data['questions'])}")
print(f"Questions with < 3 vocab: {len(few_vocab)} -> {few_vocab[:10]}")
print(f"Vocab items with missing fields: {len(missing_fields)} -> {missing_fields[:10]}")
print(f"Mismatched vocab items: {len(mismatched_vocab)} -> {mismatched_vocab[:15]}")
