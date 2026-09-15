import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

for t in [4, 5]:
    print(f"\n==================== TEST {t} AUDIT ====================")
    with open(f'web/data/test{t}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    qs = data.get('questions', [])
    
    # Check images across parts
    parts_with_images = {}
    for q in qs:
        part = q.get('part')
        img = q.get('image') or q.get('pageImage')
        if img and img != 'None':
            parts_with_images[part] = parts_with_images.get(part, 0) + 1
    print(f"Questions with images per Part in Test {t}: {parts_with_images}")
    
    # Check Part 1 questions
    for q in qs[:6]:
        print(f"  Q{q['id']}: image={q.get('image')}, audio={q.get('audioClip')}, opts={list(q.get('options', {}).values())[:2]}")
    
    # Check Part 2 questions (Q7-Q31)
    p2_imgs = [q['id'] for q in qs if q.get('part') == 2 and q.get('image') and q.get('image') != 'None']
    if p2_imgs:
        print(f"  WARNING: Part 2 has images in questions: {p2_imgs[:10]}")
    
    # Check options formatting in Part 2, 3, 4, 5, 6, 7
    opt_types = set()
    for q in qs:
        opts = q.get('options')
        opt_types.add(type(opts).__name__)
        if isinstance(opts, dict):
            if set(opts.keys()) not in [{'A', 'B', 'C'}, {'A', 'B', 'C', 'D'}]:
                print(f"  Non-standard option keys in Q{q['id']}: {list(opts.keys())}")
        elif isinstance(opts, list):
            print(f"  List options in Q{q['id']}: {len(opts)}")
    print(f"Option types across Test {t}: {opt_types}")
