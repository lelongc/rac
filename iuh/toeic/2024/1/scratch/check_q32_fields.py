import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

q32 = next(q for q in t2['questions'] if q['id'] == 32)
print("Keys of Q32:", q32.keys())
print("passage:", q32.get('passage'))
print("transcript preview:", (q32.get('transcript') or '')[:100])
