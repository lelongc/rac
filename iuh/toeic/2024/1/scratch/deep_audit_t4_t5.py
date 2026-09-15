import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

for t in [4, 5]:
    print(f"\n========================================================")
    print(f"               DEEP AUDIT FOR TEST {t}                 ")
    print(f"========================================================")
    with open(f'web/data/test{t}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    qs = data.get('questions', [])
    
    corrupted_korean_qs = []
    missing_transcript_qs = []
    missing_explanation_qs = []
    missing_options_qs = []
    few_vocab_qs = []
    
    for q in qs:
        qid = q['id']
        part = q.get('part')
        
        # Check vocab
        v = q.get('vocabulary', [])
        if len(v) < 3:
            few_vocab_qs.append(qid)
            
        # Check options
        opts = q.get('options', {})
        if isinstance(opts, dict):
            for k, val in opts.items():
                if any('\uac00' <= ch <= '\ud7a3' for ch in str(val)) or '\\' in str(val):
                    corrupted_korean_qs.append((qid, f"opt_{k}: {val[:30]}"))
        elif not opts:
            missing_options_qs.append(qid)
            
        # Check stem
        stem = q.get('questionText', '')
        if any('\uac00' <= ch <= '\ud7a3' for ch in stem):
            corrupted_korean_qs.append((qid, f"stem: {stem[:30]}"))
            
        # Check transcript in listening
        if part <= 4:
            tr = q.get('transcript') or ''
            if not tr or len(tr.strip()) < 10:
                missing_transcript_qs.append(qid)
            elif any('\uac00' <= ch <= '\ud7a3' for ch in tr) and part <= 2:
                corrupted_korean_qs.append((qid, f"transcript: {tr[:30]}"))
                
        # Check explanation
        exp = q.get('explanation') or ''
        if not exp or len(exp.strip()) < 15:
            missing_explanation_qs.append(qid)
            
    print(f"Total questions: {len(qs)}")
    print(f"Questions with < 3 vocab: {len(few_vocab_qs)}")
    print(f"Questions with corrupted Korean / broken text: {len(corrupted_korean_qs)}")
    for item in corrupted_korean_qs[:15]:
        print(f"  Q{item[0]}: {item[1]}")
    print(f"Questions with missing/empty transcript (P1-P4): {len(missing_transcript_qs)} -> {missing_transcript_qs[:10]}")
    print(f"Questions with missing explanation: {len(missing_explanation_qs)} -> {missing_explanation_qs[:10]}")
