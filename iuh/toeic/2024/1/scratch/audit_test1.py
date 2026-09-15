import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('all_tests_answers.json', encoding='utf-8') as f:
    all_answers = json.load(f)

filename = 'web/data/test1.json'
with open(filename, encoding='utf-8') as f:
    data = json.load(f)

official = all_answers.get('test1', {})
dummy_vocab = 0
lt_2_vocab = 0
lt_2_colloc = 0
zero_grammar = 0
short_exp = 0
mismatches = 0
missing_passage_p7 = 0

for q in data['questions']:
    qid = q['id']
    vocs = q.get('vocabulary') or q.get('vocab') or []
    colls = q.get('collocations') or []
    gram = q.get('grammar') or q.get('grammarPoints') or []
    exp = q.get('explanation') or ''
    ptext = q.get('passageText') or ''

    for v in vocs:
        if v.get('meaning') == 'xác nhận, khẳng định' or v.get('ipa') == '/kənˈfɜːm/' or v.get('word') in ['what', 'there', 'which', 'will', 'have', 'most']:
            dummy_vocab += 1

    if len(vocs) < 2:
        lt_2_vocab += 1

    if len(colls) < 2:
        lt_2_colloc += 1

    if len(gram) < 1:
        zero_grammar += 1

    if len(exp) < 60:
        short_exp += 1

    if q.get('part') == 7 and len(ptext) < 100:
        missing_passage_p7 += 1

    if str(qid) in official:
        if q.get('correctAnswer') != official[str(qid)]:
            mismatches += 1

print("=" * 60)
print("=== FULL AUDIT REPORT: TEST 1 ===")
print("=" * 60)
print(f"File: {filename}")
print(f"Total Questions: {len(data['questions'])} / 200")
print(f"Dummy confirm vocab: {dummy_vocab}")
print(f"Questions with < 2 vocab: {lt_2_vocab}")
print(f"Questions with < 2 collocations: {lt_2_colloc}")
print(f"Questions with 0 grammar points: {zero_grammar}")
print(f"Questions with short explanations (<60 chars): {short_exp}")
print(f"Part 7 missing passageText: {missing_passage_p7}")
print(f"Answer mismatches vs official keys: {mismatches}")
print("=" * 60 + "\n")
