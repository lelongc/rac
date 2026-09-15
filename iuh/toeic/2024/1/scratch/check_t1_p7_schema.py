import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', 'r', encoding='utf-8') as f:
    t1 = json.load(f)

p7 = [q for q in t1['questions'] if q['part'] == 7]
print("Sample Q147:")
print(json.dumps(p7[0], indent=2, ensure_ascii=False)[:600])

print("\nSample Q196 (multi-page):")
print(json.dumps(p7[-5], indent=2, ensure_ascii=False)[:600])
