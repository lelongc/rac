import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

print("=== APPLYING COMPLETE TEST 3 VOCABULARY ===")

# 1. Load the four generated vocabulary files
with open('scratch/t3_p1_p2_vocab.json', 'r', encoding='utf-8') as f:
    p1_p2 = json.load(f)
with open('scratch/t3_p3_p4_vocab.json', 'r', encoding='utf-8') as f:
    p3_p4 = json.load(f)
with open('scratch/t3_p5_p6_vocab.json', 'r', encoding='utf-8') as f:
    p5_p6 = json.load(f)
with open('scratch/t3_p7_vocab.json', 'r', encoding='utf-8') as f:
    p7 = json.load(f)

all_vocab = {}
for source in [p1_p2, p3_p4, p5_p6, p7]:
    for k, v in source.items():
        all_vocab[int(k)] = v

print(f"Total curated questions: {len(all_vocab)} (Range: {min(all_vocab.keys())} - {max(all_vocab.keys())})")
assert len(all_vocab) == 200, f"Expected 200 questions, got {len(all_vocab)}"

# 2. Update web/data/test3.json
with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    test3 = json.load(f)

updated_count = 0
for q in test3['questions']:
    qid = q['id']
    if qid in all_vocab:
        curated = all_vocab[qid]
        q['vocabulary'] = curated
        q['vocab'] = curated
        updated_count += 1

print(f"Updated {updated_count} questions in test3.json")

with open('web/data/test3.json', 'w', encoding='utf-8') as f:
    json.dump(test3, f, ensure_ascii=False, indent=2)

# 3. Update web/data/vocab_bank.json
with open('web/data/vocab_bank.json', 'r', encoding='utf-8') as f:
    vocab_bank = json.load(f)

existing_words = {entry.get('word', '').lower(): entry for entry in vocab_bank}
added_count = 0

for qid in sorted(all_vocab.keys()):
    for item in all_vocab[qid]:
        w_lower = item['word'].strip().lower()
        if w_lower not in existing_words:
            entry = {
                "word": item['word'],
                "ipa": item.get('ipa', ''),
                "pos": item.get('pos', ''),
                "meaning": item.get('meaning', ''),
                "example": item.get('example', ''),
                "testId": 3,
                "questionId": qid
            }
            vocab_bank.append(entry)
            existing_words[w_lower] = entry
            added_count += 1

with open('web/data/vocab_bank.json', 'w', encoding='utf-8') as f:
    json.dump(vocab_bank, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} new unique vocabulary words to vocab_bank.json (Total now: {len(vocab_bank)})")

# 4. Immediate verification on test3.json
v_counts = [len(q.get('vocabulary', [])) for q in test3['questions']]
print(f"\nTest 3 Vocab Stats:")
print(f"  Min words per question: {min(v_counts)}")
print(f"  Max words per question: {max(v_counts)}")
print(f"  Average words per question: {sum(v_counts)/len(v_counts):.2f}")
print(f"  Questions with < 3 words: {sum(1 for c in v_counts if c < 3)}")

missing_fields = 0
for q in test3['questions']:
    for v in q.get('vocabulary', []):
        if not (v.get('word') and v.get('ipa') and v.get('pos') and v.get('meaning') and v.get('example')):
            missing_fields += 1

print(f"  Vocabulary entries with missing fields: {missing_fields}")
print("\n=== TEST 3 VOCABULARY APPLICATION COMPLETED SUCCESSFULLY ===")
