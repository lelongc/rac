import json
import sys

# Set stdout to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== PART 1 AUDIT (Q1-Q6) ===")
for q in data['questions'][:6]:
    print(f"\n--- Question {q['id']} ---")
    print(f"Image: {q.get('image')}")
    print(f"AudioClip: {q.get('audioClip')}")
    print(f"Correct: {q.get('correctAnswer')}")
    print(f"QuestionText: {q.get('questionText')}")
    print("Options:")
    for k, v in q.get('options', {}).items():
        print(f"  {k}: {v}")
    print("Transcript:")
    for t in q.get('transcript', []):
        print(f"  {t}")
    print(f"Explanation: {q.get('explanation', '')[:100]}...")
