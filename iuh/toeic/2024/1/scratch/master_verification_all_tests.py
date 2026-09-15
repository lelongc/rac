import json, sys
sys.stdout.reconfigure(encoding='utf-8')

print("================================================================")
print("             TOEIC MASTER VERIFICATION AUDIT                   ")
print("================================================================")

all_passed = True

for test_num in [1, 2, 3]:
    fpath = f'web/data/test{test_num}.json'
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = data.get('questions', [])
    q_count = len(questions)
    
    v_counts = [len(q.get('vocabulary', [])) for q in questions]
    min_v = min(v_counts) if v_counts else 0
    max_v = max(v_counts) if v_counts else 0
    avg_v = sum(v_counts) / q_count if q_count else 0
    less_than_3 = sum(1 for c in v_counts if c < 3)
    
    # In Test 1, let's see how many have < 3 (Test 1 is original baseline)
    missing_fields_count = 0
    vocab_vocab_synced = True
    
    for q in questions:
        v1 = q.get('vocabulary', [])
        v2 = q.get('vocab', [])
        if len(v1) != len(v2):
            vocab_vocab_synced = False
        for v in v1:
            if not (v.get('word') and v.get('ipa') and v.get('pos') and v.get('meaning') and v.get('example')):
                missing_fields_count += 1

    print(f"\n--- TEST {test_num} ({fpath}) ---")
    print(f"  Total Questions: {q_count} / 200")
    print(f"  Vocab count range: {min_v} to {max_v} (Average: {avg_v:.2f} words/question)")
    print(f"  Questions with < 3 vocab words: {less_than_3}")
    print(f"  Vocabulary entries with missing fields: {missing_fields_count}")
    print(f"  'vocabulary' and 'vocab' fields in sync: {vocab_vocab_synced}")
    
    if test_num in [2, 3] and (less_than_3 > 0 or missing_fields_count > 0 or not vocab_vocab_synced):
        all_passed = False

# Check vocab_bank.json
with open('web/data/vocab_bank.json', 'r', encoding='utf-8') as f:
    bank = json.load(f)

print(f"\n--- VOCABULARY BANK (web/data/vocab_bank.json) ---")
print(f"  Total Unique Vocabulary Entries: {len(bank)}")
bank_missing = sum(1 for item in bank if not (item.get('word') and item.get('meaning') and item.get('ipa')))
print(f"  Bank items missing required fields: {bank_missing}")

print("\n================================================================")
if all_passed and bank_missing == 0:
    print("  RESULT: ALL VERIFICATIONS PASSED WITH 100% PERFECTION!")
else:
    print("  RESULT: VERIFICATION FOUND ISSUES!")
print("================================================================")
