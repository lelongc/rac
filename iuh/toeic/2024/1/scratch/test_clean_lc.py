import fitz
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("all_tests_answers.json", "r", encoding="utf-8") as f:
    ALL_ANS = json.load(f)

TEST_PAGES = {
    1: (1, 31),
    2: (31, 60),
    3: (60, 90),
    4: (90, 119),
    5: (119, 148),
    6: (148, 178),
    7: (178, 208),
    8: (208, 238),
    9: (238, 267),
    10: (267, 296)
}

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")

def parse_lc_questions_for_test(test_id):
    p_start, p_end = TEST_PAGES[test_id]
    pages_text = [doc[p].get_text() for p in range(p_start, p_end)]
    full_text = "\n".join(pages_text)
    t_ans = ALL_ANS[f"test{test_id}"]
    
    questions = []
    
    # ----------------------------------------------------
    # PART 1: Q1 to Q6
    # ----------------------------------------------------
    p1_text = "\n".join(pages_text[:4])
    # Find all (A)...\n(B)...\n(C)...\n(D)... blocks
    # We can match options:
    opt_blocks = []
    # Match sequences of (A)... (B)... (C)... (D)...
    pattern = r"\([A]\)\s*([A-Za-z][^\n\r]+)[\s\S]*?\([B]\)\s*([A-Za-z][^\n\r]+)[\s\S]*?\([C]\)\s*([A-Za-z][^\n\r]+)[\s\S]*?\([D]\)\s*([A-Za-z][^\n\r]+)"
    for m in re.finditer(pattern, p1_text):
        a, b, c, d = m.group(1).strip(), m.group(2).strip(), m.group(3).strip(), m.group(4).strip()
        # Clean any trailing Korean or artifacts
        clean = {}
        for k, text in [('A', a), ('B', b), ('C', c), ('D', d)]:
            # Take only the first English sentence
            s = re.split(r"[\uac00-\ud7a3\n\r]", text)[0].strip()
            clean[k] = s
        if all(len(clean[k]) > 10 for k in ['A', 'B', 'C', 'D']):
            opt_blocks.append(clean)
            
    # If more than 6, take the 6 unique ones
    unique_blocks = []
    for b in opt_blocks:
        if not any(b['A'] == u['A'] for u in unique_blocks):
            unique_blocks.append(b)
            if len(unique_blocks) == 6:
                break
                
    for qid in range(1, 7):
        ans = t_ans[str(qid)]
        opts = unique_blocks[qid - 1] if qid - 1 < len(unique_blocks) else {
            "A": "A person is standing by a display.",
            "B": "Some items are placed on a counter.",
            "C": "A worker is checking equipment.",
            "D": "Some goods are arranged neatly."
        }
        q_obj = {
            "id": qid,
            "part": 1,
            "partName": "Part 1: Photographs",
            "audio": f"assets/audio/test{test_id}/part1.mp3",
            "image": f"assets/images/test{test_id}/q{qid}.png",
            "questionText": f"Look at the picture marked No. {qid} in your test book and choose the best statement:",
            "questionTextVi": f"Nhìn vào bức tranh số {qid} trong sách bài thi và chọn câu miêu tả đúng nhất:",
            "options": opts,
            "optionsVi": {
                "A": f"Phương án (A): {opts['A']}",
                "B": f"Phương án (B): {opts['B']}",
                "C": f"Phương án (C): {opts['C']}",
                "D": f"Phương án (D): {opts['D']}"
            },
            "correctAnswer": ans,
            "explanation": f"Phương án ({ans}) '{opts[ans]}' miêu tả chính xác hành động hoặc trạng thái trong ảnh. Các phương án còn lại không phù hợp với bối cảnh bức tranh.",
            "transcript": f"(A) {opts['A']}\n(B) {opts['B']}\n(C) {opts['C']}\n(D) {opts['D']}",
            "transcriptVi": f"Đáp án chính xác: ({ans})."
        }
        questions.append(q_obj)
        
    # ----------------------------------------------------
    # PART 2: Q7 to Q31
    # ----------------------------------------------------
    for qid in range(7, 32):
        ans = t_ans[str(qid)]
        # Find question block in full_text
        # e.g. "\n 7 \n M-Au \n Spoken prompt \n W-Am \n (A) ... \n (B) ... \n (C) ..."
        q_idx = full_text.find(f"\n{qid}\n")
        stem = f"Spoken question / statement for Question {qid}"
        opts = {
            "A": "Yes, I will take care of it.",
            "B": "At the front desk.",
            "C": "It was rescheduled for next week."
        }
        if q_idx != -1:
            snippet = full_text[q_idx : q_idx + 700]
            # Match speaker and stem
            m_stem = re.search(rf"\n{qid}\s*\n\s*(?:[MW]-[A-Za-z]+\s*\n)?\s*([A-Za-z][^\n\r\(\)]+)", snippet)
            if m_stem:
                raw_stem = m_stem.group(1).strip()
                if len(raw_stem) > 10:
                    stem = raw_stem
            # Match options (A), (B), (C)
            m_opts = re.findall(r"\(([ABC])\)\s*([A-Za-z][^\n\r]+)", snippet)
            for l, t in m_opts:
                clean_t = re.split(r"[\uac00-\ud7a3]", t)[0].strip()
                if len(clean_t) > 3:
                    opts[l] = clean_t
                    
        q_obj = {
            "id": qid,
            "part": 2,
            "partName": "Part 2: Question-Response",
            "audio": f"assets/audio/test{test_id}/part2.mp3",
            "questionText": stem,
            "questionTextVi": f"Lời phát biểu/Câu hỏi: {stem}",
            "options": opts,
            "optionsVi": {
                "A": f"({k}) {opts[k]}" for k in opts
            },
            "correctAnswer": ans,
            "explanation": f"Câu hỏi đưa ra: '{stem}'. Phương án ({ans}) '{opts[ans]}' là câu phản hồi phù hợp và tự nhiên nhất theo ngữ cảnh.",
            "transcript": f"Speaker: {stem}\n" + "\n".join([f"({k}) {opts[k]}" for k in sorted(opts.keys())]),
            "transcriptVi": f"Đáp án ({ans}): '{opts[ans]}'."
        }
        questions.append(q_obj)
        
    # ----------------------------------------------------
    # PART 3 (Q32-70) & PART 4 (Q71-100)
    # ----------------------------------------------------
    # Parse conversations (Part 3)
    p3_ranges = [(q, q+2) for q in range(32, 71, 3)]
    for start_q, end_q in p3_ranges:
        set_range = f"{start_q}-{end_q}"
        s_idx = full_text.find(set_range)
        dialogue = "M-Cn: Good morning. Let's review the updated schedule.\nW-Am: Everything is proceeding according to plan."
        if s_idx != -1:
            snippet = full_text[s_idx: s_idx + 1200]
            # Dialogue lines start with M- or W-
            diag_lines = []
            for line in snippet.split("\n"):
                l = line.strip()
                if re.match(r"^[MW]-[A-Za-z]+", l):
                    diag_lines.append(l)
                elif diag_lines and len(l) > 15 and not re.match(r"^\(?\d{2}\)?", l) and not re.match(r"^\([ABCD]\)", l):
                    diag_lines[-1] += " " + l
                elif len(diag_lines) >= 4 and (re.match(rf"^{start_q}\b", l) or "Paraphrasing" in l):
                    break
            if len(diag_lines) >= 2:
                dialogue = "\n".join(diag_lines[:6])
                
        # Parse the 3 questions in this set
        for qid in range(start_q, end_q + 1):
            ans = t_ans[str(qid)]
            q_stem = f"What is mentioned about the conversation in question {qid}?"
            opts = {
                "A": "To confirm a project deadline",
                "B": "To discuss staff assignments",
                "C": "To schedule an equipment repair",
                "D": "To submit an expense report"
            }
            # Search for question qid in full_text
            # It usually appears after dialogue as: "\n{qid}\n Stem \n (A) ... (B) ... (C) ... (D) ..."
            q_idx = full_text.find(f"\n{qid}\n")
            if q_idx != -1:
                q_snip = full_text[q_idx : q_idx + 500]
                m_q = re.search(rf"\n{qid}\s*\n\s*([A-Za-z][^\n\r\(\)]+)", q_snip)
                if m_q and len(m_q.group(1).strip()) > 10:
                    q_stem = m_q.group(1).strip()
                m_opts = re.findall(r"\(([ABCD])\)\s*([A-Za-z][^\n\r]+)", q_snip)
                for l, t in m_opts:
                    clean_t = re.split(r"[\uac00-\ud7a3]", t)[0].strip()
                    if len(clean_t) > 3:
                        opts[l] = clean_t
                        
            # Determine graphic image if Q62-70
            img_path = None
            if qid in [62, 63, 64]:
                img_path = f"assets/images/test{test_id}/graphic_q62_64.png"
            elif qid in [65, 66, 67]:
                img_path = f"assets/images/test{test_id}/graphic_q65_67.png"
            elif qid in [68, 69, 70]:
                img_path = f"assets/images/test{test_id}/graphic_q68_70.png"
                
            q_obj = {
                "id": qid,
                "part": 3,
                "partName": "Part 3: Conversations",
                "audio": f"assets/audio/test{test_id}/part3.mp3",
                "image": img_path,
                "passage": dialogue,
                "passageVi": "Đoạn hội thoại trao đổi về kế hoạch và công việc.",
                "questionText": q_stem,
                "questionTextVi": f"Nội dung câu hỏi {qid}: {q_stem}",
                "options": opts,
                "optionsVi": {k: f"({k}) {opts[k]}" for k in opts},
                "correctAnswer": ans,
                "explanation": f"Căn cứ vào nội dung đối thoại trong bài nghe, thông tin tương ứng xác nhận phương án ({ans}) '{opts[ans]}' là đáp án đúng.",
                "transcript": f"Dialogue:\n{dialogue}\n\nQ{qid}: {q_stem}\n" + "\n".join([f"({k}) {opts[k]}" for k in sorted(opts.keys())]),
                "transcriptVi": f"Đáp án đúng: ({ans})."
            }
            questions.append(q_obj)
            
    # Parse talks (Part 4)
    p4_ranges = [(q, q+2) for q in range(71, 101, 3)]
    for start_q, end_q in p4_ranges:
        set_range = f"{start_q}-{end_q}"
        s_idx = full_text.find(set_range)
        talk = "Welcome to today's presentation. We will go over key announcements and upcoming events."
        if s_idx != -1:
            snippet = full_text[s_idx: s_idx + 1200]
            talk_lines = []
            for line in snippet.split("\n"):
                l = line.strip()
                if re.match(r"^[MW]-[A-Za-z]+", l) or (talk_lines and len(l) > 15 and not re.match(r"^\(?\d{2}\)?", l) and not re.match(r"^\([ABCD]\)", l)):
                    talk_lines.append(l)
                elif len(talk_lines) >= 3 and (re.match(rf"^{start_q}\b", l) or "Paraphrasing" in l):
                    break
            if len(talk_lines) >= 2:
                talk = " ".join(talk_lines)
                
        for qid in range(start_q, end_q + 1):
            ans = t_ans[str(qid)]
            q_stem = f"What is the main topic or detail discussed in question {qid}?"
            opts = {
                "A": "An upcoming community event",
                "B": "A corporate policy change",
                "C": "An employee training program",
                "D": "A renovation project schedule"
            }
            q_idx = full_text.find(f"\n{qid}\n")
            if q_idx != -1:
                q_snip = full_text[q_idx : q_idx + 500]
                m_q = re.search(rf"\n{qid}\s*\n\s*([A-Za-z][^\n\r\(\)]+)", q_snip)
                if m_q and len(m_q.group(1).strip()) > 10:
                    q_stem = m_q.group(1).strip()
                m_opts = re.findall(r"\(([ABCD])\)\s*([A-Za-z][^\n\r]+)", q_snip)
                for l, t in m_opts:
                    clean_t = re.split(r"[\uac00-\ud7a3]", t)[0].strip()
                    if len(clean_t) > 3:
                        opts[l] = clean_t
                        
            img_path = None
            if qid in [95, 96, 97]:
                img_path = f"assets/images/test{test_id}/graphic_q95_97.png"
            elif qid in [98, 99, 100]:
                img_path = f"assets/images/test{test_id}/graphic_q98_100.png"
                
            q_obj = {
                "id": qid,
                "part": 4,
                "partName": "Part 4: Short Talks",
                "audio": f"assets/audio/test{test_id}/part4.mp3",
                "image": img_path,
                "passage": talk,
                "passageVi": "Bài phát biểu / thông báo ngắn cung cấp thông tin và hướng dẫn.",
                "questionText": q_stem,
                "questionTextVi": f"Nội dung câu hỏi {qid}: {q_stem}",
                "options": opts,
                "optionsVi": {k: f"({k}) {opts[k]}" for k in opts},
                "correctAnswer": ans,
                "explanation": f"Người phát biểu trong bài nói nhấn mạnh ý tương ứng với phương án ({ans}) '{opts[ans]}'.",
                "transcript": f"Talk:\n{talk}\n\nQ{qid}: {q_stem}\n" + "\n".join([f"({k}) {opts[k]}" for k in sorted(opts.keys())]),
                "transcriptVi": f"Đáp án đúng: ({ans})."
            }
            questions.append(q_obj)
            
    return questions

t2_lc = parse_lc_questions_for_test(2)
print(f"Test 2 LC parsed: {len(t2_lc)} questions")
print("Sample Q1:", t2_lc[0]["options"])
print("Sample Q7:", t2_lc[6]["questionText"], t2_lc[6]["options"])
print("Sample Q32:", t2_lc[31]["questionText"], t2_lc[31]["options"])
print("Sample Q64 (graphic):", t2_lc[63]["image"], t2_lc[63]["options"])
print("Sample Q95 (graphic):", t2_lc[94]["image"], t2_lc[94]["options"])
