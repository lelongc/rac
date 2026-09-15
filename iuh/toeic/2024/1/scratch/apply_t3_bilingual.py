# scratch/apply_t3_bilingual.py: Master application of bilingual data for Test 3
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', encoding='utf-8') as f:
    t3 = json.load(f)

with open('scratch/t3_p1_p2_vi.json', encoding='utf-8') as f:
    t3_p1_p2 = json.load(f)

with open('scratch/t3_p3_p4_bilingual.json', encoding='utf-8') as f:
    t3_p3_p4 = json.load(f)

with open('scratch/t3_p6_bilingual.json', encoding='utf-8') as f:
    t3_p6 = json.load(f)

with open('scratch/t3_p7_bilingual.json', encoding='utf-8') as f:
    t3_p7 = json.load(f)

q149_150_passage = (
    "Questions 149-150 refer to the following e-mail.\n\n"
    "To: Sales Team\n"
    "From: Neil Cullen\n"
    "Date: 10 April\n"
    "Subject: My schedule next week\n\n"
    "Dear Team,\n"
    "I will be out of the office next week, from 15 to 19 April, attending the conference of the National Technology Alliance in Glasgow. "
    "While away, I will check e-mail and voice mail infrequently. For any urgent matters, please contact my assistant, Christina Choo. "
    "If you have a specific question about the Ezenx Industries account, please e-mail Mya Soroka. "
    "I will be back in the office on 22 April and will see all of you then.\n\n"
    "Best,\n"
    "Neil Cullen, Director of Sales and Marketing\n"
    "Shallok Technology"
)

for q in t3['questions']:
    qid = q['id']
    s_id = str(qid)
    part = q.get('part', 1)

    # Part 1 & Part 2
    if s_id in t3_p1_p2:
        item = t3_p1_p2[s_id]
        q['questionTextVi'] = item['questionTextVi']
        q['optionsVi'] = item['optionsVi']
        q['transcript'] = item['transcript']
        q['transcriptVi'] = item['transcriptVi']

    # Part 3
    elif part == 3:
        # Dialogue translation
        for range_key, pass_vi in t3_p3_p4['dialogues_vi'].items():
            s, e = map(int, range_key.split('_'))
            if s <= qid <= e:
                q['passageVi'] = pass_vi
                break

        # Question and options translation
        if s_id in t3_p3_p4['questions_vi']:
            q_info = t3_p3_p4['questions_vi'][s_id]
            q['questionTextVi'] = q_info['qVi']
            q['optionsVi'] = q_info['optVi']

        # Format full rich transcript and transcriptVi
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

    # Part 4
    elif part == 4:
        # Talk translation
        for range_key, talk_vi in t3_p3_p4['talks_vi'].items():
            s, e = map(int, range_key.split('_'))
            if s <= qid <= e:
                q['passageVi'] = talk_vi
                break

        # Question and options translation
        if s_id in t3_p3_p4['questions_vi']:
            q_info = t3_p3_p4['questions_vi'][s_id]
            q['questionTextVi'] = q_info['qVi']
            q['optionsVi'] = q_info['optVi']

        # Format full rich transcript and transcriptVi
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

    # Part 6
    elif part == 6:
        for range_key, pass_vi in t3_p6['p6_passages_vi'].items():
            s, e = map(int, range_key.split('_'))
            if s <= qid <= e:
                q['passageVi'] = pass_vi
                q['passageTextVi'] = pass_vi
                break

        if s_id in t3_p6['p6_questions_vi']:
            q_info = t3_p6['p6_questions_vi'][s_id]
            q['questionTextVi'] = q_info['qVi']
            q['optionsVi'] = q_info['optVi']

    # Part 7
    elif part == 7:
        if qid in [149, 150]:
            q['passageText'] = q149_150_passage

        for range_key, p_info in t3_p7['p7_passages_vi'].items():
            s, e = map(int, range_key.split('_'))
            if s <= qid <= e:
                q['passageTitle'] = p_info['title']
                q['passageTextVi'] = p_info['textVi']
                q['passageVi'] = p_info['textVi']
                break

        if s_id in t3_p7['p7_questions_vi']:
            q_info = t3_p7['p7_questions_vi'][s_id]
            q['questionTextVi'] = q_info['qVi']
            q['optionsVi'] = q_info['optVi']

with open('web/data/test3.json', 'w', encoding='utf-8') as f:
    json.dump(t3, f, ensure_ascii=False, indent=2)

print("Applied full bilingual translations to web/data/test3.json successfully!")
