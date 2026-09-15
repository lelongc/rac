import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions'][:6]:
    print(f"=== Q{q['id']} ===")
    print("image:", q.get('image'))
    print("audioClip:", q.get('audioClip'))
    print("correctAnswer:", q.get('correctAnswer'))
    print("options:", q.get('options'))
    print("transcript:", q.get('transcript'))
    print("explanation:", q.get('explanation'))
