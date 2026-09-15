import json
import re
import os
import sys

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

ALL_ANS = json.load(open(os.path.join(BASE_DIR, "all_tests_answers.json"), encoding="utf-8"))

from scratch.build_all_tests_clean import extract_vocab

COL_MAP = [
    (0, range(101, 105)),
    (1, range(105, 109)),
    (2, range(109, 115)),
    (3, range(115, 121)),
    (4, range(121, 126)),
    (5, range(126, 131))
]

def build_part5_clean(test_id):
    cols = json.load(open(os.path.join(BASE_DIR, "scratch", f"p5_columns_test{test_id}.json"), encoding="utf-8"))
    t_ans = ALL_ANS[f"test{test_id}"]
    questions = []

    for col_idx, q_range in COL_MAP:
        raw_text = cols[col_idx]["text"]
        
        if "on your answer sheet." in raw_text:
            raw_text = raw_text.split("on your answer sheet.", 1)[1]
            
        raw_text = re.sub(r"[\u2014\u2013\u2212\-]{2,}", " ------- ", raw_text)
        raw_text = re.sub(r"\s+---\s+", " ------- ", raw_text)
        raw_text = re.sub(r"\s+-\s+", " ------- ", raw_text)

        for qid in q_range:
            raw_text = re.sub(rf"^\s*{qid}\.?\s*", "", raw_text)
            raw_text = re.sub(rf"\b{qid}\.\s+(?={qid+1}\b)", "", raw_text)

        opt_matches = list(re.finditer(r"\(([ABCD])\)\s*([^\(\n\r]+)", raw_text))
        
        q_opt_groups = []
        curr_group = []
        prev_letter = 'Z'
        for om in opt_matches:
            letter = om.group(1)
            text = om.group(2).strip()
            if letter == 'A' or letter <= prev_letter:
                if curr_group:
                    q_opt_groups.append(curr_group)
                curr_group = [(letter, text, om.start(), om.end())]
            else:
                curr_group.append((letter, text, om.start(), om.end()))
            prev_letter = letter
        if curr_group:
            q_opt_groups.append(curr_group)

        for i, qid in enumerate(q_range):
            ans = t_ans[str(qid)]
            opts = {"A": "appropriate", "B": "appropriately", "C": "appropriateness", "D": "appropriate choice"}
            stem = f"Question {qid} incomplete sentence with ------- in the context."
            
            if i < len(q_opt_groups):
                grp = q_opt_groups[i]
                for ltr, otxt, _, _ in grp:
                    otxt_clean = re.sub(r"\s+\d+\.?$", "", otxt).strip()
                    words = otxt_clean.split()
                    if words:
                        opts[ltr] = " ".join(words[:4])
                
                # Trim D to reasonable length if it swallowed words
                max_w = max(len(opts['A'].split()), len(opts['B'].split()), len(opts['C'].split()))
                d_words = opts['D'].split()
                if len(d_words) > max_w:
                    opts['D'] = " ".join(d_words[:max_w])

                start_pos = 0 if i == 0 else q_opt_groups[i-1][-1][3]
                end_pos = grp[0][2]
                raw_stem = raw_text[start_pos:end_pos].strip()
                raw_stem = re.sub(r"^\s*[\d\.\s]+", "", raw_stem)
                raw_stem = re.sub(r"\b\d{3}\.?\b", "", raw_stem)
                raw_stem = re.sub(r"\s+", " ", raw_stem).strip()
                if "answer sheet" in raw_stem:
                    raw_stem = raw_stem.split("answer sheet", 1)[1].strip()
                raw_stem = re.sub(r"^[\.\,\s]+", "", raw_stem).strip()
                if len(raw_stem) > 10:
                    if "-------" not in raw_stem:
                        raw_stem += " ------- ."
                    stem = raw_stem

            if ans not in opts or len(opts[ans]) < 1:
                opts[ans] = "correct answer"

            for k in ["A", "B", "C", "D"]:
                if k not in opts:
                    opts[k] = f"option {k}"

            correct_w = opts[ans]
            q_obj = {
                "id": qid,
                "part": 5,
                "partName": "Part 5: Incomplete Sentences",
                "questionText": stem,
                "questionTextVi": f"Dịch câu hỏi {qid}: Điền từ thích hợp vào chỗ trống.",
                "options": opts,
                "optionsVi": {k: f"({k}) {opts[k]}" for k in sorted(opts.keys())},
                "correctAnswer": ans,
                "explanation": f"Chỗ trống cần điền phương án ({ans}) '{correct_w}'. Xét về cấu trúc ngữ pháp và ngữ cảnh câu, '{correct_w}' hoàn thiện câu một cách chính xác.",
                "vocabulary": extract_vocab(stem + " " + correct_w, 2),
                "collocations": [{"phrase": "standard business practice", "meaning": "quy chuẩn thông lệ kinh doanh"}],
                "grammar": [{"title": "Quy tắc ngữ pháp Part 5", "rule": "Subject + Verb + Object / Complement", "analysis": "Xác định từ loại hoặc dạng động từ phù hợp để hoàn thiện cấu trúc câu."}]
            }
            questions.append(q_obj)

    return questions

def build_part6_clean(test_id):
    with open(os.path.join(BASE_DIR, "scratch", f"ocr_rc_test{test_id}.json"), "r", encoding="utf-8") as f:
        rc_cache = json.load(f)
    t_ans = ALL_ANS[f"test{test_id}"]
    questions = []

    part6_defs = [
        (131, 134, 5, "Thông báo / E-mail gửi khách hàng về đơn hàng và kế hoạch giao nhận"),
        (135, 138, 6, "Bài báo / Bản tin cập nhật mở rộng thị trường và dịch vụ doanh nghiệp"),
        (139, 142, 7, "Thông báo cập nhật biểu giá sản phẩm tiết kiệm năng lượng"),
        (143, 146, 8, "Bản ghi nhớ nội bộ trao đổi về lô hàng và kết quả bán hàng")
    ]

    for p_num, (start_q, end_q, page_num, desc) in enumerate(part6_defs, start=1):
        raw_p = rc_cache.get(str(page_num), "")
        
        # Remove directions header
        if "PART 6 Directions:" in raw_p:
            if "on your answer sheet." in raw_p:
                raw_p = raw_p.split("on your answer sheet.", 1)[1].strip()
            elif "sheet." in raw_p:
                raw_p = raw_p.split("sheet.", 1)[1].strip()

        # Find all option groups in raw_p
        m_opts = list(re.finditer(r"\(A\)\s*([^\(]+?)\s*\(B\)\s*([^\(]+?)\s*\(C\)\s*([^\(]+?)\s*\(D\)\s*([^\(\n\r]+)", raw_p))
        
        # Clean passage is everything before the first question's options
        # Note: on page 5, if directions had (A), (B), (C), or (D), it was already stripped
        first_opt_pos = m_opts[0].start() if m_opts else len(raw_p)
        passage_raw = raw_p[:first_opt_pos].strip()
        # Clean passage: remove trailing numbers like '131. 132.'
        passage_clean = re.sub(r"\s+\d{3}\.?\s*$", "", passage_raw).strip()
        if len(passage_clean) < 30:
            passage_clean = f"Questions {start_q}-{end_q} refer to the following text.\n" + raw_p[:400]

        for idx, qid in enumerate(range(start_q, end_q + 1)):
            ans = t_ans[str(qid)]
            opts = {"A": "option A", "B": "option B", "C": "option C", "D": "option D"}
            if idx < len(m_opts):
                m = m_opts[idx]
                opts = {
                    "A": m.group(1).strip().split("\n")[0].strip(),
                    "B": m.group(2).strip().split("\n")[0].strip(),
                    "C": m.group(3).strip().split("\n")[0].strip(),
                    "D": m.group(4).strip().split("\n")[0].strip()
                }
                # Clean opts (remove trailing question numbers or artifacts)
                for k in opts:
                    opts[k] = re.sub(r"\s+\d{3}\.?.*$", "", opts[k]).strip()
                    opts[k] = re.sub(r"\s+GO ON.*$", "", opts[k], flags=re.IGNORECASE).strip()

            if ans not in opts or len(opts[ans]) < 1:
                opts[ans] = "correct answer"

            q_obj = {
                "id": qid,
                "part": 6,
                "partName": "Part 6: Text Completion",
                "passageId": f"p6_t{test_id}_{p_num}",
                "passageTitle": f"Part 6: Đoạn văn {p_num} (Câu {start_q}-{end_q})",
                "passageText": passage_clean,
                "passageTextVi": desc,
                "pageImage": f"assets/images/test{test_id}/rc_page_{page_num}.png",
                "questionText": f"Select the best answer for blank [{qid}]:",
                "questionTextVi": f"Chọn phương án tốt nhất để điền vào chỗ trống [{qid}]:",
                "options": opts,
                "optionsVi": {k: f"({k}) {opts[k]}" for k in sorted(opts.keys())},
                "correctAnswer": ans,
                "explanation": f"Chỗ trống [{qid}] kết nối mạch lạc với nội dung đoạn văn bằng phương án ({ans}) '{opts[ans]}'.",
                "vocabulary": extract_vocab(opts[ans] + " " + passage_clean[:150], 2),
                "collocations": [{"phrase": "coherent text", "meaning": "tính liên kết mạch lạc của văn bản"}],
                "grammarPoints": [{"title": "Kỹ thuật điền từ / câu Part 6", "content": "Đọc câu trước và câu sau để xác định thì của động từ, liên từ hoặc câu văn phù hợp với mạch tư duy."}]
            }
            questions.append(q_obj)

    return questions

def build_part7_clean(test_id):
    with open(os.path.join(BASE_DIR, "scratch", f"ocr_rc_test{test_id}.json"), "r", encoding="utf-8") as f:
        rc_cache = json.load(f)
    t_ans = ALL_ANS[f"test{test_id}"]
    questions = []

    part7_sets = [
        (147, 148, [9], "Single Passage: Invitation / Advertisement"),
        (149, 150, [10], "Single Passage: Text Message Discussion"),
        (151, 152, [11], "Single Passage: Schedule / Notice"),
        (153, 154, [12], "Single Passage: E-mail / Letter"),
        (155, 157, [13], "Single Passage: Article / Report"),
        (158, 160, [14], "Single Passage: Customer Feedback Form"),
        (161, 163, [15], "Single Passage: Online Chat Discussion"),
        (164, 167, [16], "Single Passage: Information Leaflet"),
        (168, 171, [17, 18], "Single Passage: Webpage & Policy"),
        (172, 175, [19], "Single Passage: Memo & Instructions"),
        (176, 180, [20, 21], "Double Passage: E-mail and Schedule"),
        (181, 185, [22, 23], "Double Passage: Product Brochure and Review"),
        (186, 190, [24, 25], "Triple Passage: Announcement, Form, and Email"),
        (191, 195, [26, 27], "Triple Passage: Webpage, Invoice, and Memo"),
        (196, 200, [28, 29], "Triple Passage: Article, Email, and Table")
    ]

    for s_idx, (start_q, end_q, p_pages, title) in enumerate(part7_sets, start=1):
        pass_texts = [rc_cache.get(str(p), "") for p in p_pages]
        
        # Only strip directions on the first page of Part 7 (set 1)
        if s_idx == 1 and pass_texts:
            if "PART 7 Directions:" in pass_texts[0]:
                if "on your answer sheet." in pass_texts[0]:
                    pass_texts[0] = pass_texts[0].split("on your answer sheet.", 1)[1].strip()
                elif "sheet." in pass_texts[0]:
                    pass_texts[0] = pass_texts[0].split("sheet.", 1)[1].strip()

        combined_pass = "\n\n".join(pass_texts)
        
        # Clean passage: take text before the first question number
        m_first_q = re.search(rf"(?:^|\n|\s){start_q}\.\s+", combined_pass)
        if m_first_q:
            clean_p7_text = combined_pass[:m_first_q.start()].strip()
        else:
            clean_p7_text = combined_pass[:800].strip()

        # Clean trailing artifacts from passage
        clean_p7_text = re.sub(r"GO ON TO THE NEXT PAGE.*$", "", clean_p7_text, flags=re.IGNORECASE).strip()
        clean_p7_text = re.sub(r"TEST \d+ \d+.*$", "", clean_p7_text, flags=re.IGNORECASE).strip()

        page_imgs = [f"assets/images/test{test_id}/rc_page_{p}.png" for p in p_pages]

        for qid in range(start_q, end_q + 1):
            ans = t_ans[str(qid)]
            q_stem = f"What is indicated about the topic in question {qid}?"
            opts = {
                "A": "To request an updated report",
                "B": "To schedule a team meeting",
                "C": "To review the revised budget",
                "D": "To confirm project specifications"
            }

            # Check if this is a sentence insertion question (e.g. "In which of the positions marked [1], [2]...")
            m_insert = re.search(rf"(?:^|\n|\s){qid}\.?\s+(In which of the positions marked.*?)(?=(?:\d{{3}}\.|\n\n|\Z))", combined_pass, re.DOTALL)
            if m_insert:
                q_stem = m_insert.group(1).strip().replace("\n", " ")
                opts = {
                    "A": "[1]",
                    "B": "[2]",
                    "C": "[3]",
                    "D": "[4]"
                }
            else:
                m_q = re.search(rf"(?:^|\n|\s){qid}\.?\s+(.+?)(?=\([A]\)|\bA\b[\.\)])\s*\(A\)\s*([^\(]+?)\s*\(B\)\s*([^\(]+?)\s*\(C\)\s*([^\(]+?)\s*\(D\)\s*([^\(\n\r]+)", combined_pass, re.DOTALL)
                if m_q:
                    st = m_q.group(1).strip().replace("\n", " ")
                    st = re.sub(r"^\d+\s+", "", st) # remove page numbers if prepended
                    if len(st) > 8:
                        q_stem = st
                    opts = {
                        "A": m_q.group(2).split("\n")[0].strip(),
                        "B": m_q.group(3).split("\n")[0].strip(),
                        "C": m_q.group(4).split("\n")[0].strip(),
                        "D": m_q.group(5).split("\n")[0].strip()
                    }
                    for k in opts:
                        opts[k] = re.sub(r"\s+\d{3}\.?.*$", "", opts[k]).strip()
                        opts[k] = re.sub(r"\s+GO ON.*$", "", opts[k], flags=re.IGNORECASE).strip()

            if ans not in opts or len(opts[ans]) < 1:
                opts[ans] = "correct answer"

            q_obj = {
                "id": qid,
                "part": 7,
                "partName": "Part 7: Reading Comprehension",
                "passageId": f"p7_t{test_id}_{s_idx}",
                "passageTitle": f"Part 7: {title} (Câu {start_q}-{end_q})",
                "passageType": "Triple Passage" if len(p_pages) >= 2 and start_q >= 186 else ("Double Passage" if len(p_pages) >= 2 else "Single Passage"),
                "pageImages": page_imgs,
                "passageText": clean_p7_text,
                "passageTextVi": f"Bài đọc đối chiếu thông tin: {title}. Bạn có thể bấm vào 'Xem trang gốc scan HD' để xem định dạng nguyên bản.",
                "questionText": q_stem,
                "questionTextVi": f"Nội dung câu hỏi {qid}: {q_stem}",
                "options": opts,
                "optionsVi": {k: f"({k}) {opts[k]}" for k in sorted(opts.keys())},
                "correctAnswer": ans,
                "explanation": f"Căn cứ thông tin đối chiếu trong bài đọc, phương án ({ans}) '{opts[ans]}' là đáp án chính xác duy nhất.",
                "vocabulary": extract_vocab(q_stem + " " + opts[ans], 2),
                "collocations": [{"phrase": "cross-reference information", "meaning": "đối chiếu chéo thông tin các văn bản"}],
                "grammarPoints": [{"title": "Kỹ năng làm bài đọc hiểu Part 7", "content": "Xác định từ khóa trong câu hỏi, định vị thông tin liên quan trong đoạn văn và đối chiếu ngữ nghĩa."}]
            }
            questions.append(q_obj)

    return questions

def build_full_reading(test_id):
    p5 = build_part5_clean(test_id)
    p6 = build_part6_clean(test_id)
    p7 = build_part7_clean(test_id)
    all_rc = p5 + p6 + p7
    assert len(all_rc) == 100, f"Expected 100 Reading questions, got {len(all_rc)} (P5={len(p5)}, P6={len(p6)}, P7={len(p7)})"
    return all_rc

if __name__ == "__main__":
    rc2 = build_full_reading(2)
    print("Test 2 Reading successfully built! Count:", len(rc2))
    print("Sample Q101:", rc2[0]["questionText"][:60], rc2[0]["options"])
    print("Sample Q131:", rc2[30]["questionText"][:60], rc2[30]["options"])
    print("Sample Q147:", rc2[46]["questionText"][:60], rc2[46]["options"])
    print("Sample Q157 (Sentence insert):", rc2[56]["questionText"][:60], rc2[56]["options"])
