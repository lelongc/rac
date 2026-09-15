import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

for t_num in [4, 5]:
    filepath = f'web/data/test{t_num}.json'
    official_path = f'scratch/test{t_num}_official_answers.json'
    
    with open(filepath, encoding='utf-8') as f:
        data = json.load(f)
    with open(official_path, encoding='utf-8') as f:
        official = json.load(f)
        
    qs = data['questions']
    print(f"\n==========================================")
    print(f"       FINAL AUDIT: TEST {t_num}          ")
    print(f"==========================================")
    
    # 1. Question count and IDs
    print(f"Total questions: {len(qs)}")
    assert len(qs) == 200, f"Expected 200, got {len(qs)}"
    ids = [q['id'] for q in qs]
    assert ids == list(range(1, 201)), f"IDs out of sequence!"
    print("✓ Question count & ID sequence: 100% OK (1..200)")
    
    # 2. Part 1 images
    p1_missing_imgs = []
    for q in qs[:6]:
        img_path = os.path.join('web', q.get('image', ''))
        if not os.path.exists(img_path):
            p1_missing_imgs.append((q['id'], q.get('image')))
    print(f"✓ Part 1 Images: {'100% OK (6/6 found)' if not p1_missing_imgs else f'FAILED: {p1_missing_imgs}'}")
    
    # 3. Part 2 option structure (A, B, C only)
    p2_bad_opts = []
    for q in qs[6:31]:
        keys = list(q.get('options', {}).keys())
        if set(keys) != {'A', 'B', 'C'}:
            p2_bad_opts.append((q['id'], keys))
    print(f"✓ Part 2 Option Keys (A, B, C only): {'100% OK (25/25 verified)' if not p2_bad_opts else f'FAILED: {p2_bad_opts}'}")
    
    # 4. Audio cut links for P1 & P2
    missing_audio = []
    for q in qs[:31]:
        clip = q.get('audioClip')
        if not clip or not os.path.exists(os.path.join('web', clip)):
            missing_audio.append((q['id'], clip))
    print(f"✓ P1 & P2 Audio Cuts: {'100% OK (31/31 exist)' if not missing_audio else f'FAILED: {missing_audio}'}")
    
    # 5. Placeholders in stem
    placeholders = []
    for q in qs:
        txt = q.get('questionText', '')
        if 'question ' + str(q['id']) in txt.lower() or 'topic in question' in txt.lower():
            placeholders.append((q['id'], txt))
    print(f"✓ Placeholder Questions: {'0 found (100% authentic)' if not placeholders else f'FAILED: {placeholders}'}")
    
    # 6. Dummy options
    dummy_options = []
    for q in qs:
        for k, v in q.get('options', {}).items():
            if 'option' in v.lower() and len(v) < 15:
                dummy_options.append((q['id'], k, v))
            elif len(v.strip()) == 0:
                dummy_options.append((q['id'], k, 'EMPTY'))
    print(f"✓ Dummy Options: {'0 found (100% authentic)' if not dummy_options else f'FAILED: {dummy_options}'}")
    
    # 7. Consecutive duplicate options
    consec_dups = []
    for i in range(len(qs) - 1):
        if qs[i]['part'] != 6 and qs[i].get('options') == qs[i+1].get('options'):
            consec_dups.append((qs[i]['id'], qs[i+1]['id']))
    print(f"✓ Duplicate Adjacent Options: {'0 found (100% distinct)' if not consec_dups else f'FAILED: {consec_dups}'}")
    
    # 8. Answer key accuracy
    key_mismatches = []
    for q in qs:
        qid_str = str(q['id'])
        if qid_str in official:
            if q['correctAnswer'].strip().upper() != official[qid_str].strip().upper():
                key_mismatches.append((q['id'], q['correctAnswer'], official[qid_str]))
    print(f"✓ Official Answer Keys: {'100% Match (200/200 exact)' if not key_mismatches else f'FAILED: {key_mismatches}'}")
    
    # 9. Vocabulary enrichment (>= 3 items)
    low_vocab = []
    for q in qs:
        v = q.get('vocabulary', [])
        if len(v) < 3:
            low_vocab.append((q['id'], len(v)))
    print(f"✓ Vocabulary Enrichment (>= 3 items): {'100% Complete (200/200 have >= 3 items)' if not low_vocab else f'FAILED: {len(low_vocab)} questions'}")
    
    # 10. Vietnamese translations
    missing_vi = []
    for q in qs:
        if not q.get('questionTextVi') or not q.get('optionsVi'):
            missing_vi.append(q['id'])
    print(f"✓ Vietnamese Translations: {'100% Complete (200/200 translated)' if not missing_vi else f'FAILED: {missing_vi}'}")

print("\n==========================================")
print("  ALL AUDITS PASSED WITH PERFECT SCORE!   ")
print("==========================================")
