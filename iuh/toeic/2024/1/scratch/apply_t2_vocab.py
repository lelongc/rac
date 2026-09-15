# scratch/apply_t2_vocab.py: Apply contextual vocabulary to web/data/test2.json and update vocab_bank.json
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

with open('scratch/t2_p1_p2_vocab.json', encoding='utf-8') as f:
    v_p1_p2 = json.load(f)

with open('scratch/t2_p3_p4_vocab.json', encoding='utf-8') as f:
    v_p3_p4 = json.load(f)

with open('scratch/t2_p5_p6_vocab.json', encoding='utf-8') as f:
    v_p5_p6 = json.load(f)

with open('scratch/t2_p7_vocab.json', encoding='utf-8') as f:
    v_p7 = json.load(f)

# Combine all dictionaries
all_t2_vocab = {}
all_t2_vocab.update(v_p1_p2)
all_t2_vocab.update(v_p3_p4)
all_t2_vocab.update(v_p5_p6)
all_t2_vocab.update(v_p7)

# Update Test 2 questions
updated_count = 0
for q in t2['questions']:
    qid = str(q['id'])
    if qid in all_t2_vocab:
        new_vocab = all_t2_vocab[qid]
        q['vocabulary'] = new_vocab
        q['vocab'] = new_vocab
        updated_count += 1

with open('web/data/test2.json', 'w', encoding='utf-8') as f:
    json.dump(t2, f, ensure_ascii=False, indent=2)

print(f"Applied new vocabulary to {updated_count}/200 questions in web/data/test2.json!")

# Update vocab_bank.json
with open('web/data/vocab_bank.json', encoding='utf-8') as f:
    vb_list = json.load(f)

existing_words = {v['word'].lower() for v in vb_list}
added_words = 0
for qid, v_list in all_t2_vocab.items():
    for item in v_list:
        w_low = item['word'].lower()
        if w_low not in existing_words:
            vb_list.append(item)
            existing_words.add(w_low)
            added_words += 1

with open('web/data/vocab_bank.json', 'w', encoding='utf-8') as f:
    json.dump(vb_list, f, ensure_ascii=False, indent=2)

print(f"Added {added_words} new words to web/data/vocab_bank.json! Total now: {len(vb_list)}")
