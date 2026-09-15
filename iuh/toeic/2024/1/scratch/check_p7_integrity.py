import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    t2 = json.load(f)

p7 = [q for q in t2['questions'] if q['part'] == 7]
print(f"Total Part 7: {len(p7)}")

prev_opts = None
for q in p7:
    qid = q['id']
    opts = q.get('options', {})
    opts_tuple = tuple(sorted(opts.values()))
    if opts_tuple == prev_opts:
        print(f"DUPLICATE OPTIONS DETECTED at Q{qid} (same as previous Q):")
        print(f"  Q{qid} opts: {opts}")
    prev_opts = opts_tuple
    
    # Check if any option is empty or very strange
    for k, v in opts.items():
        if not v or len(v.strip()) == 0:
            print(f"EMPTY OPTION at Q{qid} ({k})")
        if 'finish before time is called' in v.lower():
            print(f"FOOTER IN OPTION at Q{qid} ({k}): {v}")

print("Part 7 option integrity check done.")
