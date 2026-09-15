import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = data['questions']
print(f"Total questions in test2.json: {len(questions)}")

# Check answer keys from official PDFs if available, or print distribution
parts = {}
missing_audio = []
missing_image = []
korean_chars = []
empty_fields = []

for q in questions:
    qid = q['id']
    part = q['part']
    if part not in parts:
        parts[part] = []
    parts[part].append(q)
    
    # Check image
    img = q.get('image')
    if img:
        if not os.path.exists(os.path.join('web', img)):
            missing_image.append((qid, img))
            
    # Check audio
    audio = q.get('audioClip')
    if audio:
        if not os.path.exists(os.path.join('web', audio)):
            missing_audio.append((qid, audio))
            
    # Check for korean or gibberish
    for key, val in q.items():
        if isinstance(val, str):
            for ch in val:
                if '\uac00' <= ch <= '\ud7a3' or '\u1100' <= ch <= '\u11ff' or '\u3130' <= ch <= '\u318f':
                    korean_chars.append((qid, key, val[:40]))
                    break
        elif isinstance(val, dict):
            for k2, v2 in val.items():
                if isinstance(v2, str):
                    for ch in v2:
                        if '\uac00' <= ch <= '\ud7a3' or '\u1100' <= ch <= '\u11ff' or '\u3130' <= ch <= '\u318f':
                            korean_chars.append((qid, f"{key}.{k2}", v2[:40]))
                            break

print(f"Missing images: {len(missing_image)}")
for item in missing_image[:10]:
    print("  ", item)

print(f"Missing audio: {len(missing_audio)}")
for item in missing_audio[:10]:
    print("  ", item)

print(f"Korean/hangul chars: {len(korean_chars)}")
for item in korean_chars[:10]:
    print("  ", item)

print("\n--- Part Summary ---")
for p, q_list in sorted(parts.items()):
    print(f"Part {p}: {len(q_list)} questions (Q{q_list[0]['id']} to Q{q_list[-1]['id']})")
    ans_counts = {}
    for q in q_list:
        ans = q.get('correctAnswer', '?')
        ans_counts[ans] = ans_counts.get(ans, 0) + 1
    print(f"  Answers: {ans_counts}")
