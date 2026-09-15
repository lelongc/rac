import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    t2 = json.load(f)

print("=== CHECKING QUESTION TEXT ENDINGS ===")
for q in t2['questions']:
    qtext = q.get('questionText', '').strip()
    # Check if ends with standard punctuation
    if not (qtext.endswith('?') or qtext.endswith('.') or qtext.endswith(':') or qtext.endswith('_') or qtext.endswith('---') or qtext.endswith('."') or qtext.endswith('?"') or qtext.endswith(')')):
        print(f"Q{q['id']} (Part {q['part']}): {repr(qtext)}")
