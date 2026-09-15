import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/p5_columns_test3.json', 'r', encoding='utf-8') as f:
    p5_col = json.load(f)

for i, item in enumerate(p5_col):
    print(f"=== Item {i} (Page {item['page']} {item['col']}) ===")
    print(item['text'])
