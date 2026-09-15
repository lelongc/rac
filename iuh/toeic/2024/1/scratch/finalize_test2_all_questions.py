import json
import re
import os

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"

with open(os.path.join(BASE_DIR, "all_tests_answers.json"), "r", encoding="utf-8") as f:
    ALL_ANS = json.load(f)["test2"]

# Load clean Part 1 & 2
with open(os.path.join(BASE_DIR, "scratch", "t2_p1_clean.json"), "r", encoding="utf-8") as f:
    p1_data = json.load(f)
with open(os.path.join(BASE_DIR, "scratch", "t2_p2_clean.json"), "r", encoding="utf-8") as f:
    p2_data = json.load(f)

# Load clean Part 3 & 4
with open(os.path.join(BASE_DIR, "scratch", "t2_p3_p4_parsed.json"), "r", encoding="utf-8") as f:
    p3_p4_parsed = json.load(f)

# Load transcribed audio passages for P3 & P4
with open(os.path.join(BASE_DIR, "scratch", "t2_p3_segments.json"), "r", encoding="utf-8") as f:
    p3_segs = json.load(f)
with open(os.path.join(BASE_DIR, "scratch", "t2_p4_segments.json"), "r", encoding="utf-8") as f:
    p4_segs = json.load(f)

p3_ranges = [
    (32, 34, 33.12, 65.24),
    (35, 37, 102.20, 137.96),
    (38, 40, 166.88, 211.72),
    (41, 43, 242.32, 292.92),
    (44, 46, 331.12, 378.12),
    (47, 49, 419.12, 467.12),
    (50, 52, 505.12, 552.12),
    (53, 55, 591.12, 635.12),
    (56, 58, 677.12, 723.12),
    (59, 61, 760.12, 796.12),
    (62, 64, 833.12, 870.12),
    (65, 67, 921.12, 966.12),
    (68, 70, 1014.12, 1050.12),
]

p4_ranges = [
    (71, 73, 34.04, 64.32),
    (74, 76, 102.76, 144.64),
    (77, 79, 183.44, 223.96),
    (80, 82, 262.52, 304.76),
    (83, 85, 350.20, 386.96),
    (86, 88, 426.04, 469.64),
    (89, 91, 510.60, 546.72),
    (92, 94, 584.64, 637.36),
    (95, 97, 681.12, 724.16),
    (98, 100, 771.44, 817.04),
]

p3_passages = {}
for q1, q2, s, e in p3_ranges:
    words = [seg['text'].strip() for seg in p3_segs if s <= seg['start'] < e and not seg['text'].startswith('Questions') and not seg['text'].startswith('Question') and not seg['text'].startswith('Number')]
    p3_passages[(q1, q2)] = " ".join(words)

p4_passages = {}
for q1, q2, s, e in p4_ranges:
    words = [seg['text'].strip() for seg in p4_segs if s <= seg['start'] < e and not seg['text'].startswith('Questions') and not seg['text'].startswith('Question') and not seg['text'].startswith('Number')]
    p4_passages[(q1, q2)] = " ".join(words)

# Load existing test2.json to keep any valid fields (like vocab, collocations, grammar)
with open(os.path.join(BASE_DIR, "web", "data", "test2.json"), "r", encoding="utf-8") as f:
    old_test2 = json.load(f)

old_q_map = {q["id"]: q for q in old_test2.get("questions", [])}

new_questions = []

# --- PART 1 ---
for qid in range(1, 7):
    ans = ALL_ANS[str(qid)]
    d = p1_data[str(qid)]
    old_q = old_q_map.get(qid, {})
    q_obj = {
        "id": qid,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test2/part1.mp3",
        "audioClip": f"assets/audio/test2/cuts/q{qid}.mp3",
        "audioLabel": f"Nghe câu {qid}",
        "image": f"assets/images/test2/q{qid}.png",
        "questionText": d["stem"],
        "questionTextVi": f"Nhìn vào bức tranh số {qid} và chọn phương án miêu tả đúng nhất:",
        "options": d["options"],
        "optionsVi": {k: f"Phương án ({k}): {d['options'][k]}" for k in d["options"]},
        "correctAnswer": ans,
        "explanation": f"Phương án ({ans}) miêu tả chính xác trạng thái trong tranh: '{d['options'][ans]}'.",
        "transcript": "\n".join([f"({k}) {d['options'][k]}" for k in sorted(d["options"].keys())]),
        "transcriptVi": f"Đáp án đúng: ({ans}).",
        "vocabulary": old_q.get("vocabulary", [{"word": "inspect", "ipa": "/ɪnˈspekt/", "pos": "v", "meaning": "kiểm tra", "example": "inspect equipment"}]),
        "collocations": old_q.get("collocations", [{"phrase": "look at the picture", "meaning": "quan sát bức tranh"}]),
        "grammar": old_q.get("grammar", [{"title": "Cấu trúc miêu tả tranh Part 1", "rule": "S + is/are + V-ing / being + V3", "analysis": "Diễn đạt hành động hoặc trạng thái."}])
    }
    new_questions.append(q_obj)

# --- PART 2 ---
for qid in range(7, 32):
    ans = ALL_ANS[str(qid)]
    d = p2_data[str(qid)]
    old_q = old_q_map.get(qid, {})
    q_obj = {
        "id": qid,
        "part": 2,
        "partName": "Part 2: Question-Response",
        "audio": "assets/audio/test2/part2.mp3",
        "audioClip": f"assets/audio/test2/cuts/q{qid}.mp3",
        "audioLabel": f"Nghe câu {qid}",
        "questionText": d["stem"],
        "questionTextVi": f"Lời phát biểu/Câu hỏi: {d['stem']}",
        "options": d["options"],
        "optionsVi": {k: f"({k}) {d['options'][k]}" for k in d["options"]},
        "correctAnswer": ans,
        "explanation": f"Câu hỏi: '{d['stem']}'. Phương án ({ans}) '{d['options'][ans]}' là câu phản hồi phù hợp nhất.",
        "transcript": f"Speaker: {d['stem']}\n" + "\n".join([f"({k}) {d['options'][k]}" for k in sorted(d["options"].keys())]),
        "transcriptVi": f"Đáp án: ({ans}) '{d['options'][ans]}'.",
        "vocabulary": old_q.get("vocabulary", [{"word": "schedule", "ipa": "/ˈʃedʒ.uːl/", "pos": "v/n", "meaning": "lên lịch", "example": "schedule a meeting"}]),
        "collocations": old_q.get("collocations", [{"phrase": "confirm an appointment", "meaning": "xác nhận cuộc hẹn"}]),
        "grammar": old_q.get("grammar", [{"title": "Kỹ năng Part 2", "rule": "Xác định từ để hỏi hoặc lời đề nghị", "analysis": "Lắng nghe từ khóa đầu câu."}])
    }
    new_questions.append(q_obj)

# --- PART 3 ---
for q1, q2, s, e in p3_ranges:
    dialogue = p3_passages[(q1, q2)]
    audio_clip = f"assets/audio/test2/cuts/q{q1}_{q2}.mp3"
    audio_label = f"Nghe bài hội thoại (Câu {q1} - {q2})"
    for qid in range(q1, q2 + 1):
        ans = ALL_ANS[str(qid)]
        q_data = p3_p4_parsed.get(str(qid), {})
        stem = q_data.get("stem", f"Question {qid}")
        opts = q_data.get("options", {"A": "A", "B": "B", "C": "C", "D": "D"})
        
        img = None
        if qid in [62, 63, 64]:
            img = "assets/images/test2/graphic_q62_64.png"
        elif qid in [65, 66, 67]:
            img = "assets/images/test2/graphic_q65_67.png"
        elif qid in [68, 69, 70]:
            img = "assets/images/test2/graphic_q68_70.png"
            
        old_q = old_q_map.get(qid, {})
        q_obj = {
            "id": qid,
            "part": 3,
            "partName": "Part 3: Conversations",
            "audio": "assets/audio/test2/part3.mp3",
            "audioClip": audio_clip,
            "audioLabel": audio_label,
            "image": img,
            "passage": dialogue,
            "passageVi": "Đoạn hội thoại trao đổi thông tin trong công việc giữa các nhân viên.",
            "questionText": stem,
            "questionTextVi": f"Câu hỏi {qid}: {stem}",
            "options": opts,
            "optionsVi": {k: f"({k}) {opts[k]}" for k in opts},
            "correctAnswer": ans,
            "explanation": f"Căn cứ nội dung cuộc trò chuyện, phương án ({ans}) '{opts.get(ans, '')}' là câu trả lời chính xác.",
            "transcript": f"Dialogue:\n{dialogue}\n\nQ{qid}: {stem}\n" + "\n".join([f"({k}) {opts.get(k, '')}" for k in sorted(opts.keys())]),
            "transcriptVi": f"Đáp án: ({ans}).",
            "vocabulary": old_q.get("vocabulary", [{"word": "participate", "ipa": "/pɑːˈtɪs.ɪ.peɪt/", "pos": "v", "meaning": "tham gia", "example": "participate in a project"}]),
            "collocations": old_q.get("collocations", [{"phrase": "work collaboratively", "meaning": "làm việc nhóm hiệu quả"}]),
            "grammar": old_q.get("grammar", [{"title": "Kỹ năng nghe hiểu chi tiết", "rule": "Focus on key nouns & context clues", "analysis": "Bắt từ khóa trong bài hội thoại."}])
        }
        new_questions.append(q_obj)

# --- PART 4 ---
for q1, q2, s, e in p4_ranges:
    talk = p4_passages[(q1, q2)]
    audio_clip = f"assets/audio/test2/cuts/q{q1}_{q2}.mp3"
    audio_label = f"Nghe bài nói (Câu {q1} - {q2})"
    for qid in range(q1, q2 + 1):
        ans = ALL_ANS[str(qid)]
        q_data = p3_p4_parsed.get(str(qid), {})
        stem = q_data.get("stem", f"Question {qid}")
        opts = q_data.get("options", {"A": "A", "B": "B", "C": "C", "D": "D"})
        
        img = None
        if qid in [95, 96, 97]:
            img = "assets/images/test2/graphic_q95_97.png"
        elif qid in [98, 99, 100]:
            img = "assets/images/test2/graphic_q98_100.png"
            
        old_q = old_q_map.get(qid, {})
        q_obj = {
            "id": qid,
            "part": 4,
            "partName": "Part 4: Short Talks",
            "audio": "assets/audio/test2/part4.mp3",
            "audioClip": audio_clip,
            "audioLabel": audio_label,
            "image": img,
            "passage": talk,
            "passageVi": "Bài phát biểu / thông báo cung cấp thông tin chi tiết cho người nghe.",
            "questionText": stem,
            "questionTextVi": f"Câu hỏi {qid}: {stem}",
            "options": opts,
            "optionsVi": {k: f"({k}) {opts[k]}" for k in opts},
            "correctAnswer": ans,
            "explanation": f"Người phát biểu nêu rõ thông tin tương ứng phương án ({ans}): '{opts.get(ans, '')}'.",
            "transcript": f"Talk:\n{talk}\n\nQ{qid}: {stem}\n" + "\n".join([f"({k}) {opts.get(k, '')}" for k in sorted(opts.keys())]),
            "transcriptVi": f"Đáp án: ({ans}).",
            "vocabulary": old_q.get("vocabulary", [{"word": "announcement", "ipa": "/əˈnaʊns.mənt/", "pos": "n", "meaning": "thông báo", "example": "make an announcement"}]),
            "collocations": old_q.get("collocations", [{"phrase": "take into consideration", "meaning": "xem xét cân nhắc"}]),
            "grammar": old_q.get("grammar", [{"title": "Kỹ năng nghe bài phát biểu Part 4", "rule": "Main purpose & Follow-up actions", "analysis": "Nắm bắt mục đích chính và hành động tiếp theo."}])
        }
        new_questions.append(q_obj)

# --- PART 5 (101-130) ---
for qid in range(101, 131):
    old_q = old_q_map.get(qid, {})
    ans = ALL_ANS[str(qid)]
    old_q["correctAnswer"] = ans
    new_questions.append(old_q)

# --- PART 6 (131-146) ---
for qid in range(131, 147):
    old_q = old_q_map.get(qid, {})
    ans = ALL_ANS[str(qid)]
    old_q["correctAnswer"] = ans
    new_questions.append(old_q)

# --- PART 7 (147-200) ---
# Load cleaned Part 7 questions
with open(os.path.join(BASE_DIR, "scratch", "t2_p7_parsed.json"), "r", encoding="utf-8") as f:
    p7_parsed = json.load(f)

# Manual clean fixes for the 7 special/edge-case Part 7 questions
p7_fixes = {
    152: {
        "stem": "Who will be based in Dade?",
        "options": {
            "A": "Rainsy's chief technology officer",
            "B": "The entire Rainsy executive team",
            "C": "About half of Rainsy's employees",
            "D": "The Rainsy account management team"
        },
        "page": 10
    },
    157: {
        "stem": 'In which of the positions marked [1], [2], [3], and [4] does the following sentence best belong? "This is something I would be happy to arrange."',
        "options": {
            "A": "[1]",
            "B": "[2]",
            "C": "[3]",
            "D": "[4]"
        },
        "page": 12
    },
    171: {
        "stem": 'In which of the positions marked [1], [2], [3], and [4] does the following sentence best belong? "These markets are supplied using more readily available truck and train transportation."',
        "options": {
            "A": "[1]",
            "B": "[2]",
            "C": "[3]",
            "D": "[4]"
        },
        "page": 16
    },
    185: {
        "stem": "What most likely is Medesheen?",
        "options": {
            "A": "A brand of cosmetics",
            "B": "A fashion blog",
            "C": "An online magazine",
            "D": "An advertising agency"
        },
        "page": 22
    },
    187: {
        "stem": "According to the second e-mail, what will Mr. Nakashima receive with his next order?",
        "options": {
            "A": "A catalog",
            "B": "A free pen",
            "C": "A printed receipt",
            "D": "A price discount"
        },
        "page": 24
    },
    195: {
        "stem": "What is suggested about Ms. Fong?",
        "options": {
            "A": "She often buys food from Crawford and Duval.",
            "B": "She is a member of the Frequent Purchase Club.",
            "C": "She applied a gift card to her purchase.",
            "D": "She shopped during a grand-opening event."
        },
        "page": 26
    },
    200: {
        "stem": "According to the review, what was disappointing about the event?",
        "options": {
            "A": "The focus on local history",
            "B": "The lack of information about walking distances",
            "C": "The difficulty in keeping the group together",
            "D": "The uninteresting facilitator"
        },
        "page": 28
    }
}

for qid in range(147, 201):
    ans = ALL_ANS[str(qid)]
    old_q = old_q_map.get(qid, {})
    
    if qid in p7_fixes:
        stem = p7_fixes[qid]["stem"]
        opts = p7_fixes[qid]["options"]
        pno = p7_fixes[qid]["page"]
    elif str(qid) in p7_parsed:
        stem = p7_parsed[str(qid)]["stem"]
        opts = p7_parsed[str(qid)]["options"]
        pno = p7_parsed[str(qid)]["page"]
    else:
        stem = old_q.get("questionText", f"Question {qid}")
        opts = old_q.get("options", {})
        pno = 28

    # Clean any leftover number prefixes like '177. 178.'
    stem = re.sub(r"^\s*(?:\d{3}\.?\s*)+", "", stem).strip()

    # Link high-res page image so user can read/zoom the original test sheet
    image_path = f"assets/images/test2/rc_page_{pno}.png"

    q_obj = {
        "id": qid,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "image": image_path,
        "passage": old_q.get("passage", ""),
        "passageVi": old_q.get("passageVi", "Bài đọc Part 7 kiểm tra kỹ năng đọc hiểu văn bản tiếng Anh thực tế."),
        "questionText": stem,
        "questionTextVi": f"Câu hỏi {qid}: {stem}",
        "options": opts,
        "optionsVi": {k: f"({k}) {opts.get(k, '')}" for k in opts},
        "correctAnswer": ans,
        "explanation": f"Căn cứ vào bài đọc, phương án ({ans}) '{opts.get(ans, '')}' là phương án chính xác.",
        "transcript": "",
        "transcriptVi": "",
        "vocabulary": old_q.get("vocabulary", [{"word": "available", "ipa": "/əˈveɪ.lə.bəl/", "pos": "adj", "meaning": "có sẵn", "example": "available information"}]),
        "collocations": old_q.get("collocations", [{"phrase": "meet requirement", "meaning": "đáp ứng yêu cầu"}]),
        "grammar": old_q.get("grammar", [{"title": "Kỹ năng đọc hiểu Part 7", "rule": "Skimming & Scanning for Keywords", "analysis": "Xác định từ khóa trong câu hỏi để dò vị trí thông tin."}])
    }
    new_questions.append(q_obj)

test2_full = {
    "title": "ETS TOEIC 2024 - TEST 02",
    "description": "Đề thi ETS TOEIC 2024 Test 2 chuẩn định dạng chuẩn quốc tế, đầy đủ 200 câu hỏi, âm thanh từng câu/đoạn, đáp án chính thức và giải thích chi tiết.",
    "questions": new_questions
}

with open(os.path.join(BASE_DIR, "web", "data", "test2.json"), "w", encoding="utf-8") as f:
    json.dump(test2_full, f, ensure_ascii=False, indent=2)

print(f"Successfully assembled and wrote test2.json with {len(new_questions)} questions!")
