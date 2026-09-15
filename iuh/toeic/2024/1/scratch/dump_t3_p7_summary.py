import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Group questions by passageId
p_groups = {}
for q in data['questions']:
    if q['id'] >= 147:
        pid = q.get('passageId', 'unknown')
        if pid not in p_groups:
            p_groups[pid] = []
        p_groups[pid].append(q)

print(f"Total Part 7 groups: {len(p_groups)}")
for pid, qlist in p_groups.items():
    qids = [q['id'] for q in qlist]
    q1 = qlist[0]
    ptext = (q1.get('passageText') or '')[:150].replace('\n', ' ')
    print(f"\nGroup {pid} (Q{qids[0]}-Q{qids[-1]}): title='{q1.get('passageTitle')}'")
    print(f"  Snippet: {ptext}...")
    for q in qlist:
        print(f"    Q{q['id']}: stem='{q.get('questionText')}', options={list(q.get('options', {}).values())}")
        print(f"           curr_vocab={[v.get('word') for v in q.get('vocabulary', [])]}")
