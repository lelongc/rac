import json, sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['scratch/t3_p1_p2_vocab.json', 'scratch/t3_p3_p4_vocab.json']:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            d = json.load(f)
        print(f"{fname}: {len(d)} questions covered (keys: {min(map(int, d.keys()))} to {max(map(int, d.keys()))})")
        # print sample
        k = list(d.keys())[0]
        print(f"  Sample Q{k}: {[v['word'] for v in d[k]]}")
    except Exception as e:
        print(f"{fname}: Error {e}")
