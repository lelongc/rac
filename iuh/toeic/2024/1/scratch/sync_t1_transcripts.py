import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)

updated_count = 0
for q in t1['questions']:
    part = q.get('part')
    qid = q['id']

    if part == 3:
        passage_en = q.get('passage', '')
        q_en = q.get('questionText', '')
        opts_en = q.get('options', {})
        q['transcript'] = (
            f"Dialogue:\n{passage_en}\n\n"
            f"Q{qid}: {q_en}\n"
            f"(A) {opts_en.get('A', '')}\n"
            f"(B) {opts_en.get('B', '')}\n"
            f"(C) {opts_en.get('C', '')}\n"
            f"(D) {opts_en.get('D', '')}"
        )

        passage_vi = q.get('passageVi', '')
        q_vi = q.get('questionTextVi', '')
        opts_vi = q.get('optionsVi', {})
        q['transcriptVi'] = (
            f"Đoạn hội thoại:\n{passage_vi}\n\n"
            f"Câu hỏi {qid}: {q_vi}\n"
            f"{opts_vi.get('A', '')}\n"
            f"{opts_vi.get('B', '')}\n"
            f"{opts_vi.get('C', '')}\n"
            f"{opts_vi.get('D', '')}"
        )
        updated_count += 1

    elif part == 4:
        passage_en = q.get('passage', '')
        q_en = q.get('questionText', '')
        opts_en = q.get('options', {})
        q['transcript'] = (
            f"Talk:\n{passage_en}\n\n"
            f"Q{qid}: {q_en}\n"
            f"(A) {opts_en.get('A', '')}\n"
            f"(B) {opts_en.get('B', '')}\n"
            f"(C) {opts_en.get('C', '')}\n"
            f"(D) {opts_en.get('D', '')}"
        )

        passage_vi = q.get('passageVi', '')
        q_vi = q.get('questionTextVi', '')
        opts_vi = q.get('optionsVi', {})
        q['transcriptVi'] = (
            f"Bài nói / Thông báo:\n{passage_vi}\n\n"
            f"Câu hỏi {qid}: {q_vi}\n"
            f"{opts_vi.get('A', '')}\n"
            f"{opts_vi.get('B', '')}\n"
            f"{opts_vi.get('C', '')}\n"
            f"{opts_vi.get('D', '')}"
        )
        updated_count += 1

with open('web/data/test1.json', 'w', encoding='utf-8') as f:
    json.dump(t1, f, ensure_ascii=False, indent=2)

print(f"Updated {updated_count} questions in Test 1 with rich transcript and transcriptVi!")
