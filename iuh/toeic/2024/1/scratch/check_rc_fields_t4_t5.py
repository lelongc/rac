import json, sys
sys.stdout.reconfigure(encoding='utf-8')

for t in [4, 5]:
    print(f"\n==================== TEST {t} Part 6 & 7 Check ====================")
    with open(f'web/data/test{t}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    qs = data['questions']
    
    # Check Q131 (Part 6)
    q131 = next(q for q in qs if q['id'] == 131)
    print(f"Test {t} Q131 keys: {list(q131.keys())}")
    print(f"  passageText: {bool(q131.get('passageText'))}, len={len(q131.get('passageText') or '')}")
    print(f"  passageTextVi: {bool(q131.get('passageTextVi'))}")
    print(f"  questionTextVi: {bool(q131.get('questionTextVi'))}")
    print(f"  optionsVi: {bool(q131.get('optionsVi'))}")
    print(f"  pageImage: {q131.get('pageImage')}")
    print(f"  image: {q131.get('image')}")
    
    # Check Q147 (Part 7)
    q147 = next(q for q in qs if q['id'] == 147)
    print(f"\nTest {t} Q147 keys: {list(q147.keys())}")
    print(f"  passageText: {bool(q147.get('passageText'))}, len={len(q147.get('passageText') or '')}")
    print(f"  passageTextVi: {bool(q147.get('passageTextVi'))}")
    print(f"  questionTextVi: {bool(q147.get('questionTextVi'))}")
    print(f"  optionsVi: {bool(q147.get('optionsVi'))}")
    print(f"  pageImages: {q147.get('pageImages')}")
    print(f"  image: {q147.get('image')}")

    # Check how many questions in RC lack questionTextVi or optionsVi
    no_qvi = sum(1 for q in qs if q['id'] >= 101 and not q.get('questionTextVi'))
    no_optvi = sum(1 for q in qs if q['id'] >= 101 and not q.get('optionsVi'))
    print(f"\nRC questions lacking questionTextVi: {no_qvi}")
    print(f"RC questions lacking optionsVi: {no_optvi}")
