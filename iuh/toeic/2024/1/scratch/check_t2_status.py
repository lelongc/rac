import json

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

for part in range(1, 8):
    qs = [q for q in t2['questions'] if q.get('part') == part]
    if not qs:
        continue
    dummy_cnt = sum(1 for q in qs for v in (q.get('vocabulary') or q.get('vocab') or []) if v.get('meaning') == 'xác nhận, khẳng định' or v.get('ipa') == '/kənˈfɜːm/' or v.get('word') in ['what', 'there', 'which'])
    has_grammar = sum(1 for q in qs if q.get('grammar') or q.get('grammarPoints'))
    has_colloc = sum(1 for q in qs if q.get('collocations'))
    first_id = qs[0]['id']
    last_id = qs[-1]['id']
    print(f"Part {part}: {len(qs)} Qs (Q{first_id}-Q{last_id}) | Dummy vocab: {dummy_cnt} | Grammar: {has_grammar}/{len(qs)} | Collocations: {has_colloc}/{len(qs)}")
