import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['scratch/build_t2_rc_clean.py', 'scratch/finalize_test2_all_questions.py']:
    print(f"=== {fname} ===")
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for l in lines[:40]:
        print(l, end='')
    print("\n" + "="*40)
