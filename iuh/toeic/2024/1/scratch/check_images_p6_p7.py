import json, sys
sys.stdout.reconfigure(encoding='utf-8')

for t in [1, 2, 3, 4, 5]:
    with open(f'web/data/test{t}.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"\n==================== TEST {t} ====================")
    p6_q = next((q for q in d['questions'] if q['part'] == 6), None)
    if p6_q:
        print(f"Part 6 sample Q{p6_q['id']}: image={p6_q.get('image')}, pageImage={p6_q.get('pageImage')}, pageImages={p6_q.get('pageImages')}")
    p7_q = next((q for q in d['questions'] if q['part'] == 7), None)
    if p7_q:
        print(f"Part 7 sample Q{p7_q['id']}: image={p7_q.get('image')}, pageImage={p7_q.get('pageImage')}, pageImages={p7_q.get('pageImages')}")
    
    # Also check what images exist in Part 1
    p1_imgs = [q.get('image') for q in d['questions'] if q['part'] == 1]
    print(f"Part 1 images: {p1_imgs}")
    
    # Check if Part 3 or Part 4 has graphic images
    p3_imgs = [(q['id'], q.get('image')) for q in d['questions'] if q['part'] == 3 and q.get('image') and q.get('image') != 'None']
    p4_imgs = [(q['id'], q.get('image')) for q in d['questions'] if q['part'] == 4 and q.get('image') and q.get('image') != 'None']
    print(f"Part 3 graphic images count: {len(p3_imgs)}: {p3_imgs}")
    print(f"Part 4 graphic images count: {len(p4_imgs)}: {p4_imgs}")
