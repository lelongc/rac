import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('all_tests_answers.json', encoding='utf-8') as f:
    all_answers = json.load(f)

print("=" * 80)
print(f"{'TEST':<8} | {'QUESTIONS':<10} | {'DUMMY VOCAB':<12} | {'VOCAB >= 2':<12} | {'COLLOC >= 2':<12} | {'GRAMMAR':<8} | {'MISMATCH':<8}")
print("=" * 80)

for test_num in [1, 2, 3]:
    filename = f'web/data/test{test_num}.json'
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)

    official = all_answers.get(f'test{test_num}', {})
    dummy_vocab = 0
    lt_2_vocab = 0
    lt_2_colloc = 0
    zero_grammar = 0
    mismatches = 0

    for q in data['questions']:
        qid = q['id']
        vocs = q.get('vocabulary') or q.get('vocab') or []
        colls = q.get('collocations') or []
        gram = q.get('grammar') or q.get('grammarPoints') or []

        for v in vocs:
            if v.get('meaning') == 'xác nhận, khẳng định' or v.get('ipa') == '/kənˈfɜːm/' or v.get('word') in ['what', 'there', 'which', 'will', 'have', 'most']:
                dummy_vocab += 1

        if len(vocs) < 2:
            lt_2_vocab += 1

        if len(colls) < 2:
            lt_2_colloc += 1

        if len(gram) < 1:
            zero_grammar += 1

        if str(qid) in official:
            if q.get('correctAnswer') != official[str(qid)]:
                mismatches += 1

    t_str = f"Test {test_num}"
    q_str = f"{len(data['questions'])}/200"
    v_str = f"{dummy_vocab} dummy"
    v2_str = f"{200 - lt_2_vocab}/200"
    c2_str = f"{200 - lt_2_colloc}/200"
    g_str = f"{200 - zero_grammar}/200"
    m_str = f"{mismatches} errors"
    print(f"{t_str:<8} | {q_str:<10} | {v_str:<12} | {v2_str:<12} | {c2_str:<12} | {g_str:<8} | {m_str:<8}")

print("=" * 80)
