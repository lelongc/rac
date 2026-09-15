import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    t2 = json.load(f)

print("=== PART 2 INSPECTION (Q7-Q31) ===")
for q in t2['questions'][6:31]:
    qid = q['id']
    opts = q.get('options', {})
    qtext = q.get('questionText', '')
    audio = q.get('audioClip', '')
    ans = q.get('correctAnswer', '')
    trans = q.get('transcript', '')
    vocab = q.get('vocabulary', [])
    colloc = q.get('collocations', [])
    gram = q.get('grammar', [])
    
    issues = []
    if len(opts) != 3:
        issues.append(f"opts count={len(opts)}")
    if not audio:
        issues.append("missing audio")
    if not trans:
        issues.append("missing transcript")
    if not vocab:
        issues.append("empty vocab")
    if not qtext:
        issues.append("empty questionText")
        
    print(f"Q{qid} [{ans}] audio: {audio.split('/')[-1]} | text: {qtext[:40]}... | issues: {issues}")
    if qid in [7, 8, 31]:
        print(f"   Sample Q{qid} text: {qtext}")
        print(f"   Options: {opts}")
        print(f"   Transcript: {trans[:100]}...")
