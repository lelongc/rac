import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/t3_p1_p2_vi.json', encoding='utf-8') as f:
    p1_p2 = json.load(f)

for qid in [1, 2, 7, 8]:
    s_id = str(qid)
    print(f"=== Q{qid} in t3_p1_p2 ===")
    item = p1_p2[s_id]
    for k, v in item.items():
        if isinstance(v, str):
            print(f"  {k}: {v[:80]}")
        else:
            print(f"  {k}: {v}")
