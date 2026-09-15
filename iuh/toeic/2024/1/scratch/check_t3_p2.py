import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    t3 = json.load(f)

print("=== INSPECTING TEST 3 PART 2 (Q7-Q31) ===")
p2 = [q for q in t3['questions'] if q['part'] == 2]
print(f"Total Part 2 questions: {len(p2)}")

for q in p2:
    qid = q['id']
    stem = q.get('questionText', '')
    opts = q.get('options', {})
    audio = q.get('audioClip', '')
    ans = q.get('correctAnswer', '')
    trans = q.get('transcript', '')
    
    korean = False
    for s in [stem, trans] + list(opts.values()):
        for ch in s:
            if '\uac00' <= ch <= '\ud7a3' or '\u1100' <= ch <= '\u11ff' or '\u3130' <= ch <= '\u318f':
                korean = True
                break
    
    print(f"Q{qid} [{ans}] audio={audio.split('/')[-1]} | opts_cnt={len(opts)} | korean={korean} | text={stem[:40]}...")
