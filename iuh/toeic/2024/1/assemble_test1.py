# assemble_test1.py: Merge all 7 parts into web/data/test1.json and build vocab bank
import json
import os

parts = [
    ("Part 1", "data_part1.json"),
    ("Part 2", "data_part2.json"),
    ("Part 3", "data_part3.json"),
    ("Part 4", "data_part4.json"),
    ("Part 5", "data_part5.json"),
    ("Part 6", "data_part6.json"),
    ("Part 7", "data_part7.json"),
]

all_questions = []
vocab_bank = []
grammar_bank = []

for name, filename in parts:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        print(f"Loaded {name}: {len(data)} questions")
        all_questions.extend(data)

print(f"Total compiled questions: {len(all_questions)}")
assert len(all_questions) == 200, f"Expected 200 questions, got {len(all_questions)}"

# Verify IDs from 1 to 200
ids = [q["id"] for q in all_questions]
assert ids == list(range(1, 201)), "Questions IDs are not strictly 1 to 200!"

# Build Vocabulary Bank with question references
vocab_seen = set()
for q in all_questions:
    q_id = q["id"]
    part_num = q.get("part", 1)
    for v in q.get("vocabulary", []):
        word_key = v.get("word", "").strip().lower()
        if word_key and word_key not in vocab_seen:
            vocab_seen.add(word_key)
            vocab_bank.append({
                "word": v.get("word"),
                "ipa": v.get("ipa", ""),
                "pos": v.get("pos", ""),
                "meaning": v.get("meaning", ""),
                "example": v.get("example", ""),
                "part": part_num,
                "questionId": q_id
            })

print(f"Extracted {len(vocab_bank)} unique high-frequency vocabulary entries!")

# Build Grammar Bank
for q in all_questions:
    q_id = q["id"]
    part_num = q.get("part", 1)
    for g in q.get("grammarPoints", []):
        grammar_bank.append({
            "title": g.get("title"),
            "content": g.get("content"),
            "part": part_num,
            "questionId": q_id
        })

print(f"Extracted {len(grammar_bank)} grammar points!")

os.makedirs("web/data", exist_ok=True)

with open("web/data/test1.json", "w", encoding="utf-8") as f:
    json.dump({
        "testTitle": "ETS TOEIC 2024 - Full Actual Test 1",
        "totalQuestions": 200,
        "questions": all_questions
    }, f, ensure_ascii=False, indent=2)

with open("web/data/vocab_bank.json", "w", encoding="utf-8") as f:
    json.dump(vocab_bank, f, ensure_ascii=False, indent=2)

with open("web/data/grammar_bank.json", "w", encoding="utf-8") as f:
    json.dump(grammar_bank, f, ensure_ascii=False, indent=2)

print("Saved web/data/test1.json, vocab_bank.json, and grammar_bank.json successfully!")
