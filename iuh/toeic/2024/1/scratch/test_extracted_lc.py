import re, sys
sys.stdout.reconfigure(encoding='utf-8')

for t_num, fn, check_ids in [
    (4, 'scratch/t4_giai_lc.txt', [68, 69, 70, 82, 83, 85, 86]),
    (5, 'scratch/t5_giai_lc.txt', [40, 41, 43, 44, 68, 69, 70, 82, 83, 96, 97])
]:
    with open(fn, encoding='utf-8') as f:
        content = f.read()
    print(f'=== TEST {t_num} Extracted ===')
    for qid in check_ids:
        m = re.search(r'\n(' + str(qid) + r')\s*\n\s*([^\n]+(?:\n[^\n]+)*?\?)\s*\n\s*\(A\)\s*([^\n]+)\s*\n\s*\(B\)\s*([^\n]+)\s*\n\s*\(C\)\s*([^\n]+)\s*\n\s*\(D\)\s*([^\n]+)', content)
        if m:
            clean_stem = " ".join(m.group(2).strip().split())
            print(f'Q{qid}: {clean_stem}')
            print(f'   (A) {m.group(3).strip()}')
            print(f'   (B) {m.group(4).strip()}')
            print(f'   (C) {m.group(5).strip()}')
            print(f'   (D) {m.group(6).strip()}')
