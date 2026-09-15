import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

p5_qs = [q for q in t3['questions'] if q.get('part') == 5]
print(f"Total Part 5 questions: {len(p5_qs)}")

missing_qvi = [q['id'] for q in p5_qs if not q.get('questionTextVi') or 'Nội dung câu hỏi' in q.get('questionTextVi', '')]
missing_optvi = [q['id'] for q in p5_qs if not q.get('optionsVi') or any('(A) ' not in str(v) and len(str(v)) < 2 for v in q.get('optionsVi', {}).values())]

print("Missing/placeholder questionTextVi in Part 5:", missing_qvi)
print("Part 5 sample Q101-Q105:")
for q in p5_qs[:5]:
    print(f"Q{q['id']}:")
    print("  EN:", q['questionText'])
    print("  VI:", q.get('questionTextVi'))
    print("  opts:", q.get('options'))
    print("  optsVi:", q.get('optionsVi'))
