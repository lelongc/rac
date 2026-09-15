import json
import os
import sys

# Ensure stdout handles UTF-8 on Windows
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
WEB_DIR = os.path.join(BASE_DIR, "web")
DATA_DIR = os.path.join(WEB_DIR, "data")
AUDIO_DIR = os.path.join(WEB_DIR, "assets", "audio")
IMAGES_DIR = os.path.join(WEB_DIR, "assets", "images")

# Load official answer keys
ans_file = os.path.join(BASE_DIR, "all_tests_answers.json")
with open(ans_file, "r", encoding="utf-8") as f:
    official_answers = json.load(f)

print("=== VERIFYING ALL 10 TESTS ===")
total_errors = 0

for t in range(1, 11):
    test_key = f"test{t}"
    json_path = os.path.join(DATA_DIR, f"{test_key}.json")
    
    if not os.path.exists(json_path):
        print(f"ERROR: {json_path} does not exist!")
        total_errors += 1
        continue
        
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to parse {json_path}: {e}")
        total_errors += 1
        continue
        
    questions = data.get("questions", [])
    if len(questions) != 200:
        print(f"ERROR: Test {t} has {len(questions)} questions, expected 200!")
        total_errors += 1
        
    mismatches = 0
    missing_fields = 0
    for q in questions:
        qid = q.get("id")
        q_ans = q.get("correctAnswer", "").strip().upper()
        official_ans = official_answers.get(test_key, {}).get(str(qid), "").strip().upper()
        
        if q_ans != official_ans:
            mismatches += 1
            if mismatches <= 3:
                print(f"  Mismatch in Test {t} Q{qid}: dataset has '{q_ans}', official has '{official_ans}'")
                
        # Check required schema fields
        for field in ["id", "part", "options", "correctAnswer", "explanation"]:
            if field not in q or q[field] is None:
                missing_fields += 1
                
    if mismatches > 0:
        print(f"ERROR: Test {t} has {mismatches} answer mismatches!")
        total_errors += mismatches
    if missing_fields > 0:
        print(f"ERROR: Test {t} has {missing_fields} missing fields!")
        total_errors += missing_fields
        
    # Check audio files
    audio_missing = 0
    for p in range(1, 5):
        aud_path = os.path.join(AUDIO_DIR, f"test{t}", f"part{p}.mp3")
        if not os.path.exists(aud_path):
            audio_missing += 1
            print(f"  Missing audio: {aud_path}")
    if audio_missing > 0:
        total_errors += audio_missing
        
    # Check Part 1 photos (q1-q6)
    p1_img_missing = 0
    for q_idx in range(1, 7):
        img_path = os.path.join(IMAGES_DIR, f"test{t}", f"q{q_idx}.png")
        if not os.path.exists(img_path):
            p1_img_missing += 1
            print(f"  Missing P1 image: {img_path}")
    if p1_img_missing > 0:
        total_errors += p1_img_missing

    print(f"Test {t:2d}: 200 Qs | Official Answer Match: {200 - mismatches}/200 | Audio (4/4): {'OK' if audio_missing == 0 else 'FAIL'} | P1 Images (6/6): {'OK' if p1_img_missing == 0 else 'FAIL'}")

# Check bank files
vocab_bank = os.path.join(DATA_DIR, "vocab_bank.json")
grammar_bank = os.path.join(DATA_DIR, "grammar_bank.json")

print("\n=== VERIFYING VOCAB & GRAMMAR BANKS ===")
if os.path.exists(vocab_bank):
    with open(vocab_bank, "r", encoding="utf-8") as f:
        vb = json.load(f)
    print(f"Vocab Bank: {len(vb)} entries")
else:
    print("ERROR: vocab_bank.json missing!")
    total_errors += 1

if os.path.exists(grammar_bank):
    with open(grammar_bank, "r", encoding="utf-8") as f:
        gb = json.load(f)
    print(f"Grammar Bank: {len(gb)} entries")
else:
    print("ERROR: grammar_bank.json missing!")
    total_errors += 1

print(f"\n==========================================")
print(f"Total Errors: {total_errors}")
if total_errors == 0:
    print("SUCCESS: ALL 10 TESTS VERIFIED 100% PERFECT!")
print(f"==========================================")
