import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

fix_map = {
    78: {
        "options": {
            "A": "A lecture will begin.",
            "B": "A demonstration will be given.",
            "C": "An interview will be conducted.",
            "D": "A park will close."
        },
        "optionsVi": {
            "A": "Một bài giảng sẽ bắt đầu.",
            "B": "Một buổi thuyết minh/thực hành sẽ được diễn ra.",
            "C": "Một cuộc phỏng vấn sẽ được tiến hành.",
            "D": "Công viên sẽ đóng cửa."
        },
        "correctAnswer": "A",
        "explanation": "Người nói thông báo: 'world-renowned botanist Samantha Hughes will be giving a lecture on the care of flowering orchid plants at two o’clock...' -> (A) A lecture will begin."
    },
    79: {
        "options": {
            "A": "A book",
            "B": "An album",
            "C": "A film",
            "D": "A magazine"
        },
        "optionsVi": {
            "A": "Một cuốn sách",
            "B": "Một album",
            "C": "Một bộ phim",
            "D": "Một tạp chí"
        },
        "correctAnswer": "C",
        "explanation": "Người nói chia sẻ: 'Samantha’s work has also been featured in a documentary film called Orchid Caretakers...' -> (C) A film."
    },
    80: {
        "options": {
            "A": "A fund-raising concert",
            "B": "A sports competition",
            "C": "A play rehearsal",
            "D": "An awards ceremony"
        },
        "optionsVi": {
            "A": "Một buổi hòa nhạc gây quỹ",
            "B": "Một cuộc thi thể thao",
            "C": "Một buổi diễn tập kịch",
            "D": "Một lễ trao giải"
        },
        "correctAnswer": "A",
        "explanation": "Mở đầu thông báo: 'Before the benefit concert begins... Tonight’s proceeds will directly fund...' (benefit concert = fund-raising concert) -> (A)."
    },
    83: {
        "questionText": "What is the topic of the workshop?",
        "questionTextVi": "Chủ đề của buổi hội thảo là gì?",
        "options": {
            "A": "Time management",
            "B": "Public speaking",
            "C": "Leadership skills",
            "D": "Professional networking"
        },
        "optionsVi": {
            "A": "Quản lý thời gian",
            "B": "Thuyết trình trước công chúng",
            "C": "Kỹ năng lãnh đạo",
            "D": "Xây dựng mối quan hệ chuyên môn"
        },
        "correctAnswer": "A",
        "explanation": "Người nói nêu: 'focused on improving team productivity and time management' -> (A) Time management."
    },
    85: {
        "questionText": "What will the listeners do next?",
        "questionTextVi": "Người nghe sẽ làm gì tiếp theo?",
        "options": {
            "A": "Sign their names on a list",
            "B": "Take a break",
            "C": "Participate in an introductory activity",
            "D": "Fill out a questionnaire"
        },
        "optionsVi": {
            "A": "Ký tên vào danh sách",
            "B": "Nghỉ giải lao",
            "C": "Tham gia vào hoạt động làm quen / mở đầu",
            "D": "Điền vào bảng khảo sát câu hỏi"
        },
        "correctAnswer": "C",
        "explanation": "Người nói hướng dẫn: 'start off, we’ll do an exercise to get to know one another better' (exercise to get to know = introductory activity) -> (C)."
    },
    89: {
        "questionText": "What is the speaker mainly discussing?",
        "questionTextVi": "Người nói chủ yếu thảo luận về điều gì?",
        "options": {
            "A": "An advertising campaign",
            "B": "A market expansion",
            "C": "Some contract negotiations",
            "D": "Some audit procedures"
        },
        "optionsVi": {
            "A": "Một chiến dịch quảng cáo",
            "B": "Mở rộng thị trường",
            "C": "Đàm phán hợp đồng",
            "D": "Quy trình kiểm toán"
        },
        "correctAnswer": "A",
        "explanation": "Người nói thông báo giành được hợp đồng quảng cáo: 'advertising contract... developing two thirty-second television commercials' -> (A) An advertising campaign."
    },
    92: {
        "questionText": "Where do the listeners most likely work?",
        "questionTextVi": "Những người nghe nhiều khả năng làm việc ở đâu nhất?",
        "options": {
            "A": "At a hospital",
            "B": "At a restaurant",
            "C": "At a grocery store",
            "D": "At an electronics store"
        },
        "optionsVi": {
            "A": "Tại một bệnh viện",
            "B": "Tại một nhà hàng",
            "C": "Tại một cửa hàng tạp hóa",
            "D": "Tại một cửa hàng điện tử"
        },
        "correctAnswer": "A",
        "explanation": "Người nói gọi trực tiếp: 'Excuse me, nurses... in the hospital break rooms' -> (A) At a hospital."
    },
    94: {
        "questionText": "What does the speaker imply when she says, “That will require management approval”?",
        "questionTextVi": "Người nói ngụ ý gì khi nói “Điều đó sẽ cần có sự phê duyệt của cấp quản lý”?",
        "options": {
            "A": "A process has not been followed.",
            "B": "The listeners may be asked to work extra shifts.",
            "C": "The listeners should contact a manager.",
            "D": "A change will not be immediate."
        },
        "optionsVi": {
            "A": "Một quy trình đã không được tuân thủ.",
            "B": "Người nghe có thể bị yêu cầu làm thêm ca.",
            "C": "Người nghe nên liên hệ với quản lý.",
            "D": "Sự thay đổi sẽ không thể diễn ra ngay lập tức."
        },
        "correctAnswer": "D",
        "explanation": "Người nói giải thích về yêu cầu tăng ngân sách phải cần ban giám đốc duyệt ('require management approval'), do đó thay đổi không thể diễn ra ngay lập tức mà cần giải pháp tạm thời -> (D) A change will not be immediate."
    },
    95: {
        "questionText": "According to the speaker, what was recently completed?",
        "questionTextVi": "Theo người nói, công trình/dự án nào vừa được hoàn thành gần đây?",
        "options": {
            "A": "A company reorganization",
            "B": "A park renovation",
            "C": "A volunteer training",
            "D": "A conservation project"
        },
        "optionsVi": {
            "A": "Tái cơ cấu công ty",
            "B": "Cải tạo công viên",
            "C": "Đào tạo tình nguyện viên",
            "D": "Dự án bảo tồn"
        },
        "correctAnswer": "B",
        "explanation": "Người phát biểu chào mừng: 'celebration for our town’s newly renovated Lakeville Park' -> (B) A park renovation."
    },
    99: {
        "questionText": "Look at the graphic. At what depth should samples be collected this month?",
        "questionTextVi": "Nhìn vào biểu đồ/bảng. Mẫu đất nên được thu thập ở độ sâu nào trong tháng này?",
        "options": {
            "A": "12 inches",
            "B": "4 inches",
            "C": "6 inches",
            "D": "8 inches"
        },
        "optionsVi": {
            "A": "12 inch",
            "B": "4 inch",
            "C": "6 inch",
            "D": "8 inch"
        },
        "correctAnswer": "A",
        "explanation": "Người nói lưu ý: 'Since this is September, all soil samples in the next six weeks should be taken from the same depth, as seen on this chart.' Tra bảng 'Soil Sampling Timeline', hàng September-October có Depth là '12 inches' -> (A) 12 inches."
    },
    100: {
        "questionText": "What does the speaker encourage the listeners to do?",
        "questionTextVi": "Người nói khuyến khích người nghe làm điều gì?",
        "options": {
            "A": "Turn off mobile phones",
            "B": "Have some refreshments",
            "C": "Purchase some seeds",
            "D": "Sign up for a mailing list"
        },
        "optionsVi": {
            "A": "Tắt điện thoại di động",
            "B": "Dùng đồ ăn nhẹ",
            "C": "Mua một ít hạt giống",
            "D": "Đăng ký nhận thư điện tử / danh sách gửi thư"
        },
        "correctAnswer": "D",
        "explanation": "Người nói kêu gọi trước khi ra về: 'please sign up for our mailing list to stay informed of future lectures' -> (D) Sign up for a mailing list."
    }
}

path = "web/data/test1.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    qid = q["id"]
    if qid in fix_map:
        for k, v in fix_map[qid].items():
            q[k] = v

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Test 1 Part 4 discrepancies successfully aligned to official ETS standards!")
