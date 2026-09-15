# scratch/apply_t2_bilingual.py: Master application of bilingual data for Test 2
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

with open('scratch/t2_p1_p2_vi.json', encoding='utf-8') as f:
    t2_p1_p2 = json.load(f)

with open('scratch/t2_p3_p4_bilingual.json', encoding='utf-8') as f:
    t2_p3_p4 = json.load(f)

with open('scratch/t2_p6_p7_bilingual.json', encoding='utf-8') as f:
    t2_p6_p7 = json.load(f)

with open('scratch/t2_p7_questions_vi.json', encoding='utf-8') as f:
    t2_p7_q = json.load(f)

for q in t2['questions']:
    qid = q['id']
    s_id = str(qid)
    part = q.get('part', 1)

    # Part 1 & Part 2
    if s_id in t2_p1_p2:
        item = t2_p1_p2[s_id]
        q['questionTextVi'] = item['questionTextVi']
        q['optionsVi'] = item['optionsVi']
        q['transcript'] = item['transcript']
        q['transcriptVi'] = item['transcriptVi']

    # Part 3
    elif part == 3:
        # Find dialogue translation
        for range_key, pass_vi in t2_p3_p4['dialogues_vi'].items():
            s, e = map(int, range_key.split('_'))
            if s <= qid <= e:
                q['passageVi'] = pass_vi
                break

        # Find question translation
        if s_id in t2_p3_p4['questions_vi']:
            q_info = t2_p3_p4['questions_vi'][s_id]
            q['questionTextVi'] = q_info['qVi']
            q['optionsVi'] = q_info['optVi']

        # Format complete transcript and transcriptVi
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
        # Find talk translation
        for range_key, talk_vi in t2_p3_p4['talks_vi'].items():
            s, e = map(int, range_key.split('_'))
            if s <= qid <= e:
                q['passageVi'] = talk_vi
                break

        # Find question translation
        if s_id in t2_p3_p4['questions_vi']:
            q_info = t2_p3_p4['questions_vi'][s_id]
            q['questionTextVi'] = q_info['qVi']
            q['optionsVi'] = q_info['optVi']

        # Format complete transcript and transcriptVi
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
        for range_key, pass_vi in t2_p6_p7['p6_passages_vi'].items():
            s, e = map(int, range_key.split('_'))
            if s <= qid <= e:
                q['passageVi'] = pass_vi
                break
        q['questionTextVi'] = f"Chọn phương án thích hợp nhất cho chỗ trống [{qid}]:"

    # Part 7
    elif part == 7:
        for range_key, p_info in t2_p6_p7['p7_passages_vi'].items():
            s, e = map(int, range_key.split('_'))
            if s <= qid <= e:
                q['passageTitle'] = p_info['title']
                q['passageTextVi'] = p_info['textVi']
                break

        if s_id in t2_p7_q:
            q_info = t2_p7_q[s_id]
            q['questionTextVi'] = q_info['qVi']
            q['optionsVi'] = q_info['optVi']

with open('web/data/test2.json', 'w', encoding='utf-8') as f:
    json.dump(t2, f, ensure_ascii=False, indent=2)

print("Applied full bilingual translations to web/data/test2.json successfully!")
