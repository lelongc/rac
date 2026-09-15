import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    test3 = json.load(f)

with open('web/data/vocab_bank.json', 'r', encoding='utf-8') as f:
    bank = json.load(f)

existing = {b['word'].strip().lower(): b for b in bank}
added = 0

for q in test3['questions'][:6]:
    for v in q.get('vocabulary', []):
        w_lower = v['word'].strip().lower()
        if w_lower not in existing:
            entry = {
                "word": v['word'],
                "ipa": v.get('ipa', ''),
                "pos": v.get('pos', ''),
                "meaning": v.get('meaning', ''),
                "example": v.get('example', ''),
                "testId": 3,
                "questionId": q['id']
            }
            bank.append(entry)
            existing[w_lower] = entry
            added += 1

with open('web/data/vocab_bank.json', 'w', encoding='utf-8') as f:
    json.dump(bank, f, ensure_ascii=False, indent=2)

print(f"Updated vocab bank. Added {added} new words. Total: {len(bank)}")
