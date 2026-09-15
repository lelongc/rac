import json, sys
sys.stdout.reconfigure(encoding='utf-8')

for t in [4, 5]:
    with open(f'scratch/test{t}_official_answers.json', 'r', encoding='utf-8') as f:
        official = json.load(f)
    with open(f'web/data/test{t}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    mismatches = []
    for q in data['questions']:
        qid = str(q['id'])
        if qid in official:
            curr_ans = q.get('correctAnswer')
            off_ans = official[qid]
            if curr_ans != off_ans:
                mismatches.append((int(qid), curr_ans, off_ans))
                
    print(f"\n=== TEST {t} ANSWER MISMATCHES ({len(mismatches)} / {len(official)}) ===")
    if mismatches:
        # Group by contiguous blocks to see where shifts occurred
        for qid, c, o in mismatches[:30]:
            print(f"  Q{qid}: current='{c}' != official='{o}'")
    else:
        print("  ALL MATCH OFFICIAL ANSWERS!")
