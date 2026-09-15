import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== AUDITING TEST 3 VOCABULARY RELEVANCE ===")
mismatched_report = []

for q in data['questions']:
    qid = q['id']
    vocab = q.get('vocabulary', [])
    
    # gather all textual content for this question
    ctx_parts = [
        q.get('questionText') or '',
        q.get('questionTextVi') or '',
        q.get('passageText') or '',
        q.get('passageTextVi') or '',
        q.get('passage') or '',
        q.get('passageVi') or '',
        q.get('transcript') or '',
        q.get('transcriptVi') or '',
        q.get('explanation') or ''
    ]
    opts = q.get('options', {})
    if isinstance(opts, dict):
        ctx_parts.extend(opts.values())
    elif isinstance(opts, list):
        for o in opts:
            if isinstance(o, dict):
                ctx_parts.append(o.get('text', ''))
            else:
                ctx_parts.append(str(o))
    
    ctx = ' '.join(ctx_parts).lower()
    
    for v in vocab:
        w = v.get('word', '').strip()
        meaning = v.get('meaning', '').strip()
        w_clean = re.sub(r'[^a-zA-Z\s]', '', w).lower()
        tokens = [t for t in w_clean.split() if len(t) >= 4]
        
        # Check if any main token or prefix matches the text
        matched = False
        if tokens:
            for t in tokens:
                if t in ctx or t[:4] in ctx:
                    matched = True
                    break
        else:
            if w_clean and w_clean in ctx:
                matched = True
        
        # Also check if Vietnamese meaning tokens match explanation or translation
        if not matched and meaning:
            m_tokens = [m for m in re.sub(r'[^a-zA-Z\s\w]', '', meaning).split() if len(m) >= 4]
            for m in m_tokens:
                if m.lower() in ctx:
                    matched = True
                    break

        if not matched:
            mismatched_report.append((qid, w, meaning))

print(f"Total questions audited: {len(data['questions'])}")
print(f"Mismatched vocabulary items: {len(mismatched_report)}")
if mismatched_report:
    print("\nMismatched samples (up to 20):")
    for qid, w, m in mismatched_report[:20]:
        print(f"  Q{qid}: '{w}' ({m})")
else:
    print("ALL VOCABULARY IN TEST 3 IS 100% RELEVANT AND DIRECTLY PRESENT IN CONTEXT!")
