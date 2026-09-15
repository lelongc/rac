import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)

for part_no in range(1, 8):
    qs = [q for q in t1['questions'] if q.get('part') == part_no]
    sample = qs[0]
    print(f"Part {part_no}: count={len(qs)} | transcript={bool(sample.get('transcript'))} | transcriptVi={bool(sample.get('transcriptVi'))} | passage={bool(sample.get('passage'))} | passageVi={bool(sample.get('passageVi'))}")
