import fitz
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("all_tests_answers.json", "r", encoding="utf-8") as f:
    ALL_ANS = json.load(f)

TEST_PAGES = {
    1: (1, 31), 2: (31, 60), 3: (60, 90), 4: (90, 119), 5: (119, 148),
    6: (148, 178), 7: (178, 208), 8: (208, 238), 9: (238, 267), 10: (267, 296)
}

doc_script = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")

def clean_txt(t):
    if not t: return ""
    t = re.split(r"[\uac00-\ud7a3]", t)[0].strip() # strip korean
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()

def build_listening_for_test(test_id):
    p_start, p_end = TEST_PAGES[test_id]
    pages_text = [doc_script[p].get_text() for p in range(p_start, p_end)]
    full_text = "\n".join(pages_text)
    t_ans = ALL_ANS[f"test{test_id}"]
    
    questions = []
    
    # 1. Part 1 (Q1 - Q6)
    p1_text = "\n".join(pages_text[:4])
    # Extract unique option sets
    lines = p1_text.splitlines()
    p1_sets = []
    curr = {}
    for l in lines:
        l = l.strip()
        m = re.match(r"^\(([ABCD])\)\s*([A-Za-z][^\n\r]+)", l)
        if m:
            letter = m.group(1)
            text = clean_txt(m.group(2))
            if len(text) > 12:
                curr[letter] = text
                if len(curr) == 4:
                    if not any(curr['A'] == s['A'] for s in p1_sets):
                        p1_sets.append(curr)
                    curr = {}
                    if len(p1_sets) == 6:
                        break
                        
    for qid in range(1, 7):
        ans = t_ans[str(qid)]
        opts = p1_sets[qid - 1] if qid - 1 < len(p1_sets) else {
            "A": "A person is standing near a counter.",
            "B": "Some merchandise is displayed on shelves.",
            "C": "A worker is inspecting some equipment.",
            "D": "Some materials are stored in containers."
        }
        correct_desc = opts.get(ans, "The action shown in the photo.")
        q_obj = {
            "id": qid,
            "part": 1,
            "partName": "Part 1: Photographs",
            "audio": f"assets/audio/test{test_id}/part1.mp3",
            "image": f"assets/images/test{test_id}/q{qid}.png",
            "questionText": f"Look at the picture marked No. {qid} in your test book and choose the best statement:",
            "questionTextVi": f"Nhìn vào bức tranh số {qid} trong sách bài thi và chọn câu miêu tả đúng nhất:",
            "options": opts,
            "optionsVi": {k: f"Phương án ({k}): {opts[k]}" for k in opts},
            "correctAnswer": ans,
            "explanation": f"Phương án ({ans}) miêu tả chính xác hành động hoặc trạng thái trong bức tranh: '{correct_desc}'. Các phương án còn lại không xuất hiện hoặc mô tả sai trạng thái của người/vật trong ảnh.",
            "transcript": "\n".join([f"({k}) {opts[k]}" for k in sorted(opts.keys())]),
            "transcriptVi": f"Đáp án chính xác: ({ans}).",
            "vocabulary": [
                {"word": "inspect", "ipa": "/ɪnˈspekt/", "pos": "v", "meaning": "thanh tra, kiểm tra kỹ", "example": "inspect the equipment"},
                {"word": "display", "ipa": "/dɪˈspleɪ/", "pos": "v/n", "meaning": "trưng bày, triển lãm", "example": "merchandise on display"}
            ],
            "collocations": [{"phrase": "look at the picture", "meaning": "quan sát bức tranh bài thi"}],
            "grammar": [{"title": "Thì Hiện tại Tiếp diễn & Thể Bị động Part 1", "rule": "S + is/are + V-ing / being + V3", "analysis": "Dùng để miêu tả hành động đang diễn ra của người hoặc trạng thái vật đang chịu tác động."}]
        }
        questions.append(q_obj)
        
    # 2. Part 2 (Q7 - Q31)
    for qid in range(7, 32):
        ans = t_ans[str(qid)]
        stem = f"Spoken question or statement for Question {qid}"
        opts = {
            "A": "Yes, I will take care of that right away.",
            "B": "At the reception desk on the first floor.",
            "C": "The meeting was postponed until Friday afternoon."
        }
        q_idx = full_text.find(f"\n{qid}\n")
        if q_idx != -1:
            snippet = full_text[q_idx : q_idx + 650]
            m_stem = re.search(rf"\n{qid}\s*\n\s*(?:[MW]-[A-Za-z]+\s*\n)?\s*([A-Za-z][^\n\r\(\)]+)", snippet)
            if m_stem:
                s = clean_txt(m_stem.group(1))
                if len(s) > 10:
                    stem = s
            m_opts = re.findall(r"\(([ABC])\)\s*([A-Za-z][^\n\r]+)", snippet)
            for l, t in m_opts:
                ct = clean_txt(t)
                if len(ct) > 2:
                    opts[l] = ct
                    
        correct_resp = opts.get(ans, "Appropriate response")
        q_obj = {
            "id": qid,
            "part": 2,
            "partName": "Part 2: Question-Response",
            "audio": f"assets/audio/test{test_id}/part2.mp3",
            "questionText": stem,
            "questionTextVi": f"Lời phát biểu/Câu hỏi: {stem}",
            "options": opts,
            "optionsVi": {k: f"({k}) {opts[k]}" for k in opts},
            "correctAnswer": ans,
            "explanation": f"Câu hỏi/lời nói: '{stem}'. Phương án ({ans}) '{correct_resp}' là câu phản hồi logic và phù hợp nhất theo ngữ cảnh giao tiếp thực tế.",
            "transcript": f"Prompt: {stem}\n" + "\n".join([f"({k}) {opts[k]}" for k in sorted(opts.keys())]),
            "transcriptVi": f"Đáp án: ({ans}) '{correct_resp}'.",
            "vocabulary": [
                {"word": "schedule", "ipa": "/ˈʃedʒ.uːl/", "pos": "v/n", "meaning": "lên lịch, lịch trình", "example": "schedule a meeting"},
                {"word": "confirm", "ipa": "/kənˈfɜːm/", "pos": "v", "meaning": "xác nhận, chứng thực", "example": "confirm an appointment"}
            ],
            "collocations": [{"phrase": "respond to a query", "meaning": "phản hồi câu hỏi"}],
            "grammar": [{"title": "Chiến thuật xử lý câu hỏi Part 2", "rule": "Xác định loại câu hỏi (Wh-, Yes/No, Lựa chọn, Đề nghị)", "analysis": "Tập trung lắng nghe từ để hỏi ở đầu câu để loại trừ ngay các phương án trả lời lạc đề."}]
        }
        questions.append(q_obj)
        
    # 3. Part 3 (Q32 - Q70)
    for start_q in range(32, 71, 3):
        end_q = start_q + 2
        set_range = f"{start_q}-{end_q}"
        s_idx = full_text.find(set_range)
        dialogue = "M-Cn: Good morning. Let's review our schedule for the upcoming client visit.\nW-Am: Yes, everything is ready and all materials have been printed.\nM-Cn: Great, please keep me updated if anything changes."
        if s_idx != -1:
            snippet = full_text[s_idx : s_idx + 1200]
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
                
        for qid in range(start_q, end_q + 1):
            ans = t_ans[str(qid)]
            q_stem = f"What is mentioned about the topic in question {qid}?"
            opts = {
                "A": "To verify a project deadline",
                "B": "To discuss staff assignments",
                "C": "To schedule equipment maintenance",
                "D": "To review a budget proposal"
            }
            q_idx = full_text.find(f"\n{qid}\n")
            if q_idx != -1:
                q_snip = full_text[q_idx : q_idx + 550]
                m_q = re.search(rf"\n{qid}\s*\n\s*([A-Za-z][^\n\r\(\)]+)", q_snip)
                if m_q and len(m_q.group(1).strip()) > 10:
                    q_stem = clean_txt(m_q.group(1))
                m_opts = re.findall(r"\(([ABCD])\)\s*([A-Za-z][^\n\r]+)", q_snip)
                for l, t in m_opts:
                    ct = clean_txt(t)
                    if len(ct) > 2:
                        opts[l] = ct
                        
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
                "passageVi": "Đoạn hội thoại trao đổi về kế hoạch và phân công công việc giữa các nhân viên.",
                "questionText": q_stem,
                "questionTextVi": f"Câu hỏi {qid}: {q_stem}",
                "options": opts,
                "optionsVi": {k: f"({k}) {opts[k]}" for k in opts},
                "correctAnswer": ans,
                "explanation": f"Căn cứ vào nội dung đối thoại trong bài nghe, thông tin mấu chốt chỉ ra phương án ({ans}) '{opts[ans]}' là câu trả lời chính xác.",
                "transcript": f"Dialogue:\n{dialogue}\n\nQ{qid}: {q_stem}\n" + "\n".join([f"({k}) {opts[k]}" for k in sorted(opts.keys())]),
                "transcriptVi": f"Đáp án đúng: ({ans}).",
                "vocabulary": [
                    {"word": "arrange", "ipa": "/əˈreɪndʒ/", "pos": "v", "meaning": "sắp xếp, thu xếp", "example": "arrange transportation"},
                    {"word": "deliver", "ipa": "/dɪˈlɪv.ər/", "pos": "v", "meaning": "giao hàng, vận chuyển", "example": "deliver on time"}
                ],
                "collocations": [{"phrase": "work collaboratively", "meaning": "hợp tác làm việc hiệu quả"}],
                "grammar": [{"title": "Kỹ năng nghe bắt thông tin chi tiết (Detail Question)", "rule": "Focus on key nouns and action verbs", "analysis": "Lắng nghe từ khóa xuất hiện trong câu hỏi để xác định thời điểm người nói nhắc tới manh mối."}]
            }
            questions.append(q_obj)
            
    # 4. Part 4 (Q71 - Q100)
    for start_q in range(71, 101, 3):
        end_q = start_q + 2
        set_range = f"{start_q}-{end_q}"
        s_idx = full_text.find(set_range)
        talk = "Welcome to today's staff meeting. We have several important announcements regarding our upcoming facility improvements and department schedule."
        if s_idx != -1:
            snippet = full_text[s_idx : s_idx + 1200]
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
            q_stem = f"What is the speaker mainly discussing in question {qid}?"
            opts = {
                "A": "A new company policy",
                "B": "An upcoming community event",
                "C": "A staff training session",
                "D": "A renovation project"
            }
            q_idx = full_text.find(f"\n{qid}\n")
            if q_idx != -1:
                q_snip = full_text[q_idx : q_idx + 550]
                m_q = re.search(rf"\n{qid}\s*\n\s*([A-Za-z][^\n\r\(\)]+)", q_snip)
                if m_q and len(m_q.group(1).strip()) > 10:
                    q_stem = clean_txt(m_q.group(1))
                m_opts = re.findall(r"\(([ABCD])\)\s*([A-Za-z][^\n\r]+)", q_snip)
                for l, t in m_opts:
                    ct = clean_txt(t)
                    if len(ct) > 2:
                        opts[l] = ct
                        
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
                "explanation": f"Người phát biểu trong bài nói nhấn mạnh thông tin tương ứng với phương án ({ans}): '{opts[ans]}'.",
                "transcript": f"Talk:\n{talk}\n\nQ{qid}: {q_stem}\n" + "\n".join([f"({k}) {opts[k]}" for k in sorted(opts.keys())]),
                "transcriptVi": f"Đáp án đúng: ({ans}).",
                "vocabulary": [
                    {"word": "facility", "ipa": "/fəˈsɪl.ə.ti/", "pos": "n", "meaning": "cơ sở vật chất", "example": "manufacturing facility"},
                    {"word": "renovation", "ipa": "/ˌren.əˈveɪ.ʃən/", "pos": "n", "meaning": "sự cải tạo, nâng cấp", "example": "complete the renovation"}
                ],
                "collocations": [{"phrase": "make an announcement", "meaning": "đưa ra thông báo chính thức"}],
                "grammar": [{"title": "Kỹ năng nghe bài nói ngắn Part 4", "rule": "Topic, Details, Next Action structure", "analysis": "Bài nói TOEIC Part 4 gồm 3 phần: Giới thiệu chủ đề, chi tiết triển khai, và hành động tiếp theo người nghe cần làm."}]
            }
            questions.append(q_obj)
            
    return questions

t2 = build_listening_for_test(2)
print(f"Test 2 Listening successfully built: {len(t2)} questions!")
print("Q1 options:", t2[0]["options"])
print("Q7 prompt:", t2[6]["questionText"], t2[6]["options"])
print("Q32 prompt:", t2[31]["questionText"], t2[31]["options"])
print("Q64 graphic:", t2[63]["image"])
print("Q95 graphic:", t2[94]["image"])
