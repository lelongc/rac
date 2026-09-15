import json
import os

for t in [1, 2, 3]:
    p = f'web/data/test{t}.json'
    sz = os.path.getsize(p)
    with open(p, encoding='utf-8') as f:
        d = json.load(f)
    print(f"Test {t}: {sz:,} bytes | {len(d['questions'])} questions")
