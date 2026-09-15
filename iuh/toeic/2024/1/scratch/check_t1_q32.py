import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)

q32 = next(q for q in t1['questions'] if q['id'] == 32)
print("Keys of Q32 in Test 1:", q32.keys())
print("passage:\n", q32.get('passage'))
print("passageVi:\n", q32.get('passageVi'))
print("transcript:\n", q32.get('transcript'))
print("transcriptVi:\n", q32.get('transcriptVi'))
