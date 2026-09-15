import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Load official answers
with open('scratch/test4_official_answers.json', encoding='utf-8') as f:
    official4 = json.load(f)
with open('scratch/test5_official_answers.json', encoding='utf-8') as f:
    official5 = json.load(f)

# Part 5 for Test 4
t4_p5 = {
    101: {
        "questionText": "Mr. Barrientos has worked at the company ------- six years.",
        "questionTextVi": "Ông Barrientos đã làm việc tại công ty được ------- sáu năm.",
        "options": {"A": "for", "B": "since", "C": "with", "D": "lately"},
        "optionsVi": {"A": "(A) trong khoảng", "B": "(B) kể từ khi", "C": "(C) cùng với", "D": "(D) gần đây"},
        "explanation": "Thì hiện tại hoàn thành (has worked) kết hợp với khoảng thời gian 'six years' đi với giới từ 'for' (chỉ khoảng thời gian). 'since' đi với mốc thời gian."
    },
    102: {
        "questionText": "The staff cafeteria stops ------- lunch at 2:00 P.M.",
        "questionTextVi": "Nhà ăn nhân viên ngừng ------- bữa trưa vào lúc 2:00 chiều.",
        "options": {"A": "taking", "B": "buying", "C": "serving", "D": "working"},
        "optionsVi": {"A": "(A) lấy", "B": "(B) mua", "C": "(C) phục vụ", "D": "(D) làm việc"},
        "explanation": "Căn cứ vào ngữ cảnh nhà ăn (cafeteria) và bữa trưa (lunch), động từ phù hợp nhất là 'serving' (phục vụ bữa trưa). Cấu trúc 'stop doing something' (ngừng hẳn việc gì)."
    },
    103: {
        "questionText": "The annual report will be ready after ------- make the necessary revisions.",
        "questionTextVi": "Báo cáo thường niên sẽ sẵn sàng sau khi ------- thực hiện các chỉnh sửa cần thiết.",
        "options": {"A": "I", "B": "me", "C": "myself", "D": "my"},
        "optionsVi": {"A": "(A) tôi (đại từ chủ ngữ)", "B": "(B) tôi (tân ngữ)", "C": "(C) chính tôi (đại từ phản thân)", "D": "(D) của tôi (tính từ sở hữu)"},
        "explanation": "Sau liên từ 'after' mở đầu một mệnh đề phụ chỉ thời gian có động từ chính 'make', cần một đại từ nhân xưng đóng vai trò chủ ngữ (S). Do đó chọn đại từ chủ ngữ 'I' (A)."
    },
    104: {
        "questionText": "Mr. Louden was offered a full-time position at Fortelio Corporation ------- a division manager.",
        "questionTextVi": "Ông Louden đã được đề bạt một vị trí làm việc toàn thời gian tại Tập đoàn Fortelio ------- vị trí giám đốc bộ phận.",
        "options": {"A": "about", "B": "as", "C": "after", "D": "around"},
        "optionsVi": {"A": "(A) về", "B": "(B) với tư cách là / như là", "C": "(C) sau khi", "D": "(D) xung quanh"},
        "explanation": "Giới từ 'as' mang nghĩa 'với tư cách là / ở vị trí là' thường đi kèm các chức danh công việc: 'as a division manager' (với vai trò giám đốc bộ phận)."
    },
    105: {
        "questionText": "Kennedy Sports will ------- its end-of-season sale through the month of January.",
        "questionTextVi": "Kennedy Sports sẽ ------- chương trình giảm giá cuối mùa trong suốt tháng Giêng.",
        "options": {"A": "continuing", "B": "continued", "C": "continues", "D": "continue"},
        "optionsVi": {"A": "(A) đang tiếp tục", "B": "(B) đã tiếp tục", "C": "(C) tiếp tục (ngôi 3 số ít)", "D": "(D) tiếp tục (nguyên mẫu)"},
        "explanation": "Sau động từ khuyết thiếu 'will', động từ chính phải ở dạng nguyên mẫu không to (V-bare). Do đó chọn 'continue' (D)."
    },
    106: {
        "questionText": "Ms. Najjar is going to give a presentation ------- workplace regulations at noon.",
        "questionTextVi": "Bà Najjar sẽ có một bài thuyết trình ------- các quy định tại nơi làm việc vào buổi trưa.",
        "options": {"A": "near", "B": "to", "C": "past", "D": "on"},
        "optionsVi": {"A": "(A) gần", "B": "(B) tới", "C": "(C) qua", "D": "(D) về (chủ đề)"},
        "explanation": "Cụm danh từ 'a presentation on/about something' mang nghĩa bài thuyết trình về một chủ đề cụ thể. Giới từ phù hợp là 'on' (D)."
    },
    107: {
        "questionText": "Mr. Telguld submitted the ------- surveys before the monthly board meeting.",
        "questionTextVi": "Ông Telguld đã nộp các bản khảo sát đã ------- trước cuộc họp hội đồng quản trị hàng tháng.",
        "options": {"A": "completely", "B": "completed", "C": "completing", "D": "completes"},
        "optionsVi": {"A": "(A) một cách hoàn toàn", "B": "(B) đã hoàn thành (phân từ 2)", "C": "(C) đang hoàn thành", "D": "(D) hoàn thành (chia thì)"},
        "explanation": "Trước danh từ 'surveys' cần một tính từ hoặc quá khứ phân từ mang nghĩa bị động để bổ nghĩa: 'the completed surveys' (các bản khảo sát đã được hoàn thành/điền xong). Chọn (B)."
    },
    108: {
        "questionText": "Travel funds are available to student presenters coming to the conference from a significant -------.",
        "questionTextVi": "Quỹ hỗ trợ chi phí đi lại có sẵn cho các báo cáo viên sinh viên đến hội nghị từ một ------- đáng kể.",
        "options": {"A": "location", "B": "amount", "C": "reason", "D": "distance"},
        "optionsVi": {"A": "(A) địa điểm", "B": "(B) số lượng", "C": "(C) lý do", "D": "(D) khoảng cách (xa)"},
        "explanation": "Cụm 'from a significant distance' (từ một khoảng cách xa đáng kể) phù hợp nhất với ngữ cảnh hỗ trợ quỹ đi lại (travel funds). Đáp án (D)."
    },
    109: {
        "questionText": "Ms. Okada is ------- a new social media campaign at the request of our office manager.",
        "questionTextVi": "Bà Okada đang ------- một chiến dịch truyền thông xã hội mới theo yêu cầu của trưởng phòng.",
        "options": {"A": "organize", "B": "organized", "C": "organizing", "D": "organization"},
        "optionsVi": {"A": "(A) tổ chức (nguyên mẫu)", "B": "(B) đã tổ chức", "C": "(C) đang tổ chức", "D": "(D) tổ chức (danh từ)"},
        "explanation": "Cấu trúc thì hiện tại tiếp diễn: S + is + V-ing ('is organizing a new campaign'). Sau 'is' đi với tân ngữ phía sau thì cần động từ dạng V-ing thể chủ động (C)."
    },
    110: {
        "questionText": "The speaker will offer five tips for making wise purchasing -------.",
        "questionTextVi": "Diễn giả sẽ đưa ra 5 lời khuyên để đưa ra các ------- mua sắm khôn ngoan.",
        "options": {"A": "items", "B": "decisions", "C": "values", "D": "remedies"},
        "optionsVi": {"A": "(A) món đồ", "B": "(B) quyết định", "C": "(C) giá trị", "D": "(D) biện pháp khắc phục"},
        "explanation": "Cụm danh từ cố định: 'make purchasing decisions' (đưa ra các quyết định mua sắm). Do đó danh từ số nhiều phù hợp là 'decisions' (B)."
    },
    111: {
        "questionText": "Please log on to your online checking account ------- the next 30 days in order to keep it active.",
        "questionTextVi": "Vui lòng đăng nhập vào tài khoản vãng lai trực tuyến của bạn ------- 30 ngày tới để duy trì hoạt động.",
        "options": {"A": "within", "B": "how", "C": "whether", "D": "and"},
        "optionsVi": {"A": "(A) trong vòng", "B": "(B) làm thế nào", "C": "(C) liệu rằng", "D": "(D) và"},
        "explanation": "Giới từ 'within' đi với khoảng thời gian mang nghĩa 'trong vòng / trong thời hạn': 'within the next 30 days' (trong vòng 30 ngày tới). Đáp án (A)."
    },
    112: {
        "questionText": "The Bradyville Inn ------- live jazz music in the dining area on Friday evenings.",
        "questionTextVi": "Khách sạn Bradyville Inn ------- nhạc jazz sống tại khu vực phòng ăn vào các tối thứ Sáu.",
        "options": {"A": "features", "B": "marks", "C": "sounds", "D": "collects"},
        "optionsVi": {"A": "(A) có biểu diễn / giới thiệu", "B": "(B) đánh dấu", "C": "(C) vang lên", "D": "(D) thu thập"},
        "explanation": "Động từ 'features' có nghĩa là có màn biểu diễn đặc sắc hoặc có điểm nổi bật là: 'features live jazz music' (có biểu diễn nhạc jazz sống). Đáp án (A)."
    },
    113: {
        "questionText": "Leeann's Organic Fruit Spreads can be purchased ------- from the company's Web site.",
        "questionTextVi": "Các loại mứt trái cây hữu cơ của Leeann có thể được mua ------- từ trang web của công ty.",
        "options": {"A": "direction", "B": "directly", "C": "directness", "D": "directed"},
        "optionsVi": {"A": "(A) phương hướng", "B": "(B) một cách trực tiếp (trạng từ)", "C": "(C) sự thẳng thắn", "D": "(D) được chỉ đạo"},
        "explanation": "Cần một trạng từ (adv) để bổ nghĩa cho động từ dạng bị động 'can be purchased': 'purchased directly from...' (được mua trực tiếp từ...). Chọn (B)."
    },
    114: {
        "questionText": "------- the event organizers' best efforts, they have been unable to attract enough volunteers this spring.",
        "questionTextVi": "------- những nỗ lực hết mình của các nhà tổ chức sự kiện, họ vẫn không thể thu hút đủ tình nguyện viên vào mùa xuân này.",
        "options": {"A": "Behind", "B": "During", "C": "Despite", "D": "Within"},
        "optionsVi": {"A": "(A) Phía sau", "B": "(B) Trong suốt", "C": "(C) Mặc dù / Bất chấp", "D": "(D) Trong vòng"},
        "explanation": "'Despite + Noun Phrase' diễn tả sự tương phản: 'Despite the event organizers' best efforts' (Mặc cho những nỗ lực tốt nhất của ban tổ chức). Đáp án (C)."
    },
    115: {
        "questionText": "Mr. Perez ------- as an industrial engineer at Gaberly Logistics for almost twenty years.",
        "questionTextVi": "Ông Perez ------- làm kỹ sư công nghiệp tại Gaberly Logistics được gần 20 năm.",
        "options": {"A": "employs", "B": "to be employed", "C": "is employing", "D": "has been employed"},
        "optionsVi": {"A": "(A) tuyển dụng", "B": "(B) để được thuê", "C": "(C) đang tuyển dụng", "D": "(D) đã và đang được tuyển dụng / làm việc"},
        "explanation": "Dấu hiệu 'for almost twenty years' chỉ hành động bắt đầu trong quá khứ kéo dài đến hiện tại, kết hợp thể bị động 'has been employed as' (được tuyển dụng làm việc ở vị trí...). Đáp án (D)."
    },
    116: {
        "questionText": "Soon after Ms. Manilla was hired, the sales department's productivity began to increase -------.",
        "questionTextVi": "Ngay sau khi bà Manilla được tuyển dụng, năng suất của phòng kinh doanh đã bắt đầu tăng lên -------.",
        "options": {"A": "mainly", "B": "respectively", "C": "noticeably", "D": "closely"},
        "optionsVi": {"A": "(A) chủ yếu", "B": "(B) lần lượt", "C": "(C) một cách đáng kể / rõ rệt", "D": "(D) chặt chẽ"},
        "explanation": "Cần trạng từ bổ nghĩa cho động từ 'increase' (tăng lên). 'increase noticeably' (tăng lên một cách rõ rệt, đáng chú ý). Đáp án (C)."
    },
    117: {
        "questionText": "Small businesses ------- participate in the Get Ahead program will receive marketing tools to help them attract customers.",
        "questionTextVi": "Các doanh nghiệp nhỏ ------- tham gia vào chương trình Get Ahead sẽ nhận được các công cụ tiếp thị để giúp họ thu hút khách hàng.",
        "options": {"A": "that", "B": "they", "C": "what", "D": "whoever"},
        "optionsVi": {"A": "(A) mà (đại từ quan hệ)", "B": "(B) họ", "C": "(C) cái gì", "D": "(D) bất kỳ ai"},
        "explanation": "Mệnh đề quan hệ xác định thay thế cho danh từ chỉ sự vật 'Small businesses' làm chủ ngữ trước động từ 'participate'. Dùng đại từ quan hệ 'that' (A)."
    },
    118: {
        "questionText": "Our copy editors will review the manuscript ------- will not return it until the end of next week.",
        "questionTextVi": "Các biên tập viên của chúng tôi sẽ xem xét bản thảo ------- sẽ không trả lại nó cho đến cuối tuần sau.",
        "options": {"A": "or", "B": "once", "C": "either", "D": "but"},
        "optionsVi": {"A": "(A) hoặc", "B": "(B) một khi", "C": "(C) hoặc là", "D": "(D) nhưng"},
        "explanation": "Liên từ 'but' nối hai mệnh đề có ý tương phản: sẽ xem xét bản thảo nhưng sẽ không gửi lại cho đến cuối tuần tới. Đáp án (D)."
    },
    119: {
        "questionText": "Mira Kumar was probably the ------- of all the interns at Kolbry Media last summer.",
        "questionTextVi": "Mira Kumar có lẽ là người ------- trong số tất cả các thực tập sinh tại Kolbry Media vào mùa hè năm ngoái.",
        "options": {"A": "ambitious", "B": "most ambitious", "C": "ambitiously", "D": "more ambitiously"},
        "optionsVi": {"A": "(A) tham vọng", "B": "(B) tham vọng nhất (so sánh nhất)", "C": "(C) một cách tham vọng", "D": "(D) tham vọng hơn"},
        "explanation": "Cấu trúc so sánh nhất: 'the + most + adj + of all...' (trong số tất cả...). Dùng 'the most ambitious' (B)."
    },
    120: {
        "questionText": "Orbin's Fish Company expanded to a total of 26 stores ------- its takeover of a rival chain.",
        "questionTextVi": "Công ty Thủy sản Orbin đã mở rộng lên tổng cộng 26 cửa hàng ------- việc tiếp quản một chuỗi đối thủ.",
        "options": {"A": "whenever", "B": "toward", "C": "following", "D": "usually"},
        "optionsVi": {"A": "(A) bất cứ khi nào", "B": "(B) về phía", "C": "(C) sau khi / tiếp sau", "D": "(D) thông thường"},
        "explanation": "Giới từ 'following' mang nghĩa 'sau khi' (= after): 'following its takeover of...' (sau đợt thâu tóm chuỗi cửa hàng đối thủ). Đáp án (C)."
    },
    121: {
        "questionText": "Ms. Cartwright told her team members that she wanted ------- to streamline the company's assembly process.",
        "questionTextVi": "Bà Cartwright nói với các thành viên trong nhóm rằng bà muốn ------- tinh giản quy trình lắp ráp của công ty.",
        "options": {"A": "theirs", "B": "they", "C": "them", "D": "themselves"},
        "optionsVi": {"A": "(A) của họ", "B": "(B) họ (chủ ngữ)", "C": "(C) họ (tân ngữ)", "D": "(D) chính họ"},
        "explanation": "Cấu trúc: 'want somebody to do something' (muốn ai làm gì). Sau động từ 'wanted' cần đại từ ở vị trí tân ngữ (object pronoun): 'them'. Đáp án (C)."
    },
    122: {
        "questionText": "Rupert's Food Service uses ------- technology to track all of its shipments.",
        "questionTextVi": "Dịch vụ Thực phẩm của Rupert sử dụng công nghệ ------- để theo dõi toàn bộ các lô hàng của mình.",
        "options": {"A": "strict", "B": "numerous", "C": "advanced", "D": "crowded"},
        "optionsVi": {"A": "(A) nghiêm ngặt", "B": "(B) nhiều", "C": "(C) tiên tiến / hiện đại", "D": "(D) đông đúc"},
        "explanation": "Cụm danh từ: 'advanced technology' (công nghệ tiên tiến, hiện đại). Phù hợp nhất để theo dõi lô hàng hiệu quả. Đáp án (C)."
    },
    123: {
        "questionText": "Our app includes a ------- so that users can determine whether they are within their budget goals.",
        "questionTextVi": "Ứng dụng của chúng tôi tích hợp một ------- để người dùng có thể xác định xem họ có nằm trong giới hạn ngân sách hay không.",
        "options": {"A": "calculator", "B": "calculated", "C": "calculating", "D": "calculations"},
        "optionsVi": {"A": "(A) máy tính / công cụ tính toán (số ít)", "B": "(B) đã tính toán", "C": "(C) đang tính toán", "D": "(D) các phép tính (số nhiều)"},
        "explanation": "Sau mạo từ 'a' cần một danh từ số ít đếm được. 'calculator' ở đây chỉ công cụ/tính năng tính toán trong ứng dụng. Chọn (A)."
    },
    124: {
        "questionText": "To ------- that its facilities are cleaned every day, the Selboa Company has hired more janitors.",
        "questionTextVi": "Để ------- rằng cơ sở vật chất của mình được dọn dẹp mỗi ngày, Công ty Selboa đã thuê thêm lao công.",
        "options": {"A": "ensure", "B": "affect", "C": "provide", "D": "secure"},
        "optionsVi": {"A": "(A) đảm bảo", "B": "(B) ảnh hưởng", "C": "(C) cung cấp", "D": "(D) bảo vệ an toàn"},
        "explanation": "Động từ 'ensure that...' mang nghĩa 'đảm bảo rằng...'. 'To ensure that its facilities are cleaned...' (Để đảm bảo rằng cơ sở vật chất luôn sạch sẽ...). Đáp án (A)."
    },
    125: {
        "questionText": "During his term as a legislator, Jeremy Moran ------- promoted public awareness of the need for infrastructure improvements.",
        "questionTextVi": "Trong nhiệm kỳ là một nhà lập pháp, Jeremy Moran đã tích cực ------- nâng cao nhận thức cộng đồng về nhu cầu cải thiện cơ sở hạ tầng.",
        "options": {"A": "act", "B": "action", "C": "active", "D": "actively"},
        "optionsVi": {"A": "(A) hành động (V)", "B": "(B) hành động (N)", "C": "(C) tích cực (Adj)", "D": "(D) một cách tích cực (Adv)"},
        "explanation": "Đứng trước động từ quá khứ 'promoted', cần một trạng từ (adv) bổ nghĩa: 'actively promoted' (tích cực thúc đẩy/quảng bá). Đáp án (D)."
    },
    126: {
        "questionText": "Pyxie Print's business is so new that we need to explain the full range of our services to ------- clients.",
        "questionTextVi": "Doanh nghiệp của Pyxie Print còn quá mới nên chúng tôi cần giải thích toàn bộ các dịch vụ của mình cho các khách hàng -------.",
        "options": {"A": "trained", "B": "potential", "C": "elected", "D": "paid"},
        "optionsVi": {"A": "(A) đã qua đào tạo", "B": "(B) tiềm năng", "C": "(C) được bầu cử", "D": "(D) được trả lương"},
        "explanation": "Cụm danh từ: 'potential clients' (các khách hàng tiềm năng). Phù hợp nhất với ngữ cảnh công ty mới thành lập cần giới thiệu dịch vụ. Đáp án (B)."
    },
    127: {
        "questionText": "Phone orders that are ------- to local stores by 11:00 A.M. are eligible for same-day pickup.",
        "questionTextVi": "Các đơn đặt hàng qua điện thoại được ------- tới các cửa hàng địa phương trước 11:00 sáng sẽ đủ điều kiện lấy hàng ngay trong ngày.",
        "options": {"A": "submitted", "B": "submission", "C": "submitting", "D": "submits"},
        "optionsVi": {"A": "(A) được gửi / nộp (P2)", "B": "(B) sự nộp", "C": "(C) đang nộp", "D": "(D) nộp (chia thì)"},
        "explanation": "Cấu trúc bị động trong mệnh đề quan hệ: 'that are submitted to...' (được gửi đến). Sau to-be 'are' cần quá khứ phân từ 'submitted' (A)."
    },
    128: {
        "questionText": "An Oswald Hardware associate will ------- place an order for customers who need larger quantities than what is in stock.",
        "questionTextVi": "Một nhân viên của Oswald Hardware sẽ ------- đặt hàng cho các khách hàng có nhu cầu số lượng lớn hơn số hàng đang có sẵn trong kho.",
        "options": {"A": "slightly", "B": "wholly", "C": "busily", "D": "gladly"},
        "optionsVi": {"A": "(A) một chút", "B": "(B) hoàn toàn", "C": "(C) một cách bận rộn", "D": "(D) vui lòng / sẵn lòng"},
        "explanation": "Trạng từ 'gladly' (vui lòng, sẵn lòng) thể hiện tinh thần phục vụ khách hàng chu đáo: 'will gladly place an order' (sẽ sẵn lòng đặt hàng giúp khách). Đáp án (D)."
    },
    129: {
        "questionText": "Mia Daushvili performed with the Bayhead Orchestra on Monday evening, ------- her virtuosic skills on the piccolo.",
        "questionTextVi": "Mia Daushvili đã biểu diễn cùng Dàn nhạc Giao hưởng Bayhead vào tối thứ Hai, ------- kỹ năng điêu luyện của mình trên cây sáo piccolo.",
        "options": {"A": "displays", "B": "had displayed", "C": "displaying", "D": "was displayed"},
        "optionsVi": {"A": "(A) thể hiện (chia thì)", "B": "(B) đã thể hiện (quá khứ hoàn thành)", "C": "(C) thể hiện (phân từ hiện tại rút gọn)", "D": "(D) đã được thể hiện"},
        "explanation": "Rút gọn mệnh đề đồng chủ ngữ ở thể chủ động diễn tả hành động xảy ra đồng thời, sử dụng dạng V-ing: 'displaying her virtuosic skills...' (phô diễn kỹ năng điêu luyện). Đáp án (C)."
    },
    130: {
        "questionText": "When reviewing applicants for the clerk position, Ms. Ng will consider both education and ------- experience.",
        "questionTextVi": "Khi xem xét các ứng viên cho vị trí nhân viên bán hàng, bà Ng sẽ cân nhắc cả học vấn lẫn kinh nghiệm -------.",
        "options": {"A": "prior", "B": "quick", "C": "lean", "D": "calm"},
        "optionsVi": {"A": "(A) trước đây / đã có từ trước", "B": "(B) nhanh chóng", "C": "(C) tinh gọn", "D": "(D) điềm tĩnh"},
        "explanation": "Cụm danh từ nghề nghiệp phổ biến: 'prior experience' (kinh nghiệm làm việc trước đây). Đáp án (A)."
    }
}

# Part 5 for Test 5
t5_p5 = {
    101: {
        "questionText": "After upgrading to Pro Data Whiz, our clients began ------- problems with spreadsheets.",
        "questionTextVi": "Sau khi nâng cấp lên Pro Data Whiz, khách hàng của chúng tôi bắt đầu ------- các sự cố với bảng tính.",
        "options": {"A": "has", "B": "had", "C": "have", "D": "having"},
        "optionsVi": {"A": "(A) có (ngôi 3 số ít)", "B": "(B) đã có", "C": "(C) có (nguyên thể)", "D": "(D) gặp phải (V-ing)"},
        "explanation": "Sau động từ 'begin/began' có thể đi với to-V hoặc V-ing ('began having problems' - bắt đầu gặp phải các sự cố). Do đó chọn 'having' (D)."
    },
    102: {
        "questionText": "Requests for additional days off are ------- by Ms. Chung in Human Resources.",
        "questionTextVi": "Các yêu cầu xin nghỉ thêm ngày được ------- bởi bà Chung ở phòng Nhân sự.",
        "options": {"A": "approved", "B": "dropped", "C": "reached", "D": "reminded"},
        "optionsVi": {"A": "(A) phê duyệt", "B": "(B) làm rơi / hủy", "C": "(C) tiếp cận", "D": "(D) nhắc nhở"},
        "explanation": "Dạng bị động 'are approved by...' (được phê duyệt bởi...). Yêu cầu xin nghỉ phép (requests for days off) phải được phòng Nhân sự duyệt. Đáp án (A)."
    },
    103: {
        "questionText": "The programmers have a list of changes ------- the next software update.",
        "questionTextVi": "Các lập trình viên có một danh sách các thay đổi ------- bản cập nhật phần mềm tiếp theo.",
        "options": {"A": "between", "B": "of", "C": "for", "D": "above"},
        "optionsVi": {"A": "(A) ở giữa", "B": "(B) của", "C": "(C) dành cho", "D": "(D) ở trên"},
        "explanation": "Giới từ 'for' chỉ mục đích hoặc đối tượng hướng tới: 'changes for the next software update' (các thay đổi dành cho bản cập nhật tiếp theo). Đáp án (C)."
    },
    104: {
        "questionText": "Let Farida Banquet Service ------- professional catering for your important corporate events.",
        "questionTextVi": "Hãy để Dịch vụ Tiệc Farida ------- dịch vụ ăn uống chuyên nghiệp cho các sự kiện công ty quan trọng của bạn.",
        "options": {"A": "providing", "B": "provide", "C": "provides", "D": "to provide"},
        "optionsVi": {"A": "(A) đang cung cấp", "B": "(B) cung cấp (nguyên thể)", "C": "(C) cung cấp (ngôi 3 số ít)", "D": "(D) để cung cấp"},
        "explanation": "Cấu trúc cầu khiến: 'let + somebody + V-bare' (để ai đó làm gì mà không dùng to). 'Let Farida Banquet Service provide...' Chọn (B)."
    },
    105: {
        "questionText": "Using various innovative techniques, Boyd Industries has improved the ------- of its tiles.",
        "questionTextVi": "Bằng cách sử dụng nhiều kỹ thuật đổi mới khác nhau, Boyd Industries đã cải thiện ------- của gạch lát.",
        "options": {"A": "closure", "B": "product", "C": "quality", "D": "method"},
        "optionsVi": {"A": "(A) sự đóng cửa", "B": "(B) sản phẩm", "C": "(C) chất lượng", "D": "(D) phương pháp"},
        "explanation": "Căn cứ vào động từ 'improved' (cải thiện) và đối tượng 'tiles' (gạch ốp lát), danh từ phù hợp nhất là 'quality' (cải thiện chất lượng gạch). Đáp án (C)."
    },
    106: {
        "questionText": "------- of all cosmetics are final, and refunds will not be given under any circumstances.",
        "questionTextVi": "------- của tất cả mỹ phẩm là cố định và việc hoàn tiền sẽ không được thực hiện trong bất kỳ trường hợp nào.",
        "options": {"A": "Sale", "B": "Sales", "C": "sells", "D": "Selling"},
        "optionsVi": {"A": "(A) đợt giảm giá (số ít)", "B": "(B) doanh số / việc bán hàng (số nhiều)", "C": "(C) bán (động từ)", "D": "(D) việc bán"},
        "explanation": "Cần một danh từ số nhiều làm chủ ngữ cho động từ to-be 'are' trong câu: 'Sales of all cosmetics are final' (Tất cả các giao dịch bán mỹ phẩm đều là quyết định cuối cùng, không hoàn trả). Chọn (B)."
    },
    107: {
        "questionText": "If you have already submitted your response, no ------- action is required.",
        "questionTextVi": "Nếu bạn đã gửi câu trả lời của mình, không cần thực hiện thêm hành động ------- nào nữa.",
        "options": {"A": "bright", "B": "further", "C": "previous", "D": "average"},
        "optionsVi": {"A": "(A) sáng sủa", "B": "(B) thêm / sâu hơn nữa", "C": "(C) trước đó", "D": "(D) trung bình"},
        "explanation": "Cụm từ thông dụng: 'no further action is required' (không cần thực hiện thêm hành động nào nữa). 'further' đóng vai trò tính từ mang nghĩa 'hơn nữa, thêm vào'. Đáp án (B)."
    },
    108: {
        "questionText": "Ms. Sieglak stated that the app design was based on ------- own research.",
        "questionTextVi": "Bà Sieglak tuyên bố rằng thiết kế ứng dụng được dựa trên nghiên cứu của chính -------.",
        "options": {"A": "she", "B": "hers", "C": "her", "D": "herself"},
        "optionsVi": {"A": "(A) cô ấy (chủ ngữ)", "B": "(B) của cô ấy (đại từ sở hữu)", "C": "(C) của cô ấy (tính từ sở hữu)", "D": "(D) chính cô ấy"},
        "explanation": "Cấu trúc sở hữu kết hợp với 'own': 'possessive adjective + own + noun'. Với chủ ngữ là nữ (Ms. Sieglak), dùng tính từ sở hữu 'her own research' (nghiên cứu của chính cô ấy). Đáp án (C)."
    },
    109: {
        "questionText": "------- the organization has doubled its outreach efforts, it has yet to see an increase in new clients.",
        "questionTextVi": "------- tổ chức đã nhân đôi nỗ lực tiếp cận cộng đồng, họ vẫn chưa thấy lượng khách hàng mới tăng lên.",
        "options": {"A": "Until", "B": "Because", "C": "Although", "D": "Therefore"},
        "optionsVi": {"A": "(A) Cho đến khi", "B": "(B) Bởi vì", "C": "(C) Mặc dù", "D": "(D) Do đó"},
        "explanation": "Hai mệnh đề thể hiện sự tương phản đối lập: đã tăng gấp đôi nỗ lực tiếp cận nhưng vẫn chưa thấy tăng khách hàng. Dùng liên từ chỉ sự nhượng bộ 'Although' (Mặc dù). Đáp án (C)."
    },
    110: {
        "questionText": "Starting on October 8, ------- board of education meetings will be streamed live on the school district's Web site.",
        "questionTextVi": "Bắt đầu từ ngày 8 tháng 10, ------- các cuộc họp của hội đồng giáo dục sẽ được phát trực tiếp trên trang web của học khu.",
        "options": {"A": "all", "B": "so", "C": "that", "D": "to"},
        "optionsVi": {"A": "(A) tất cả", "B": "(B) vì vậy", "C": "(C) rằng / đó", "D": "(D) để / tới"},
        "explanation": "Cần từ hạn định đi với danh từ đếm được số nhiều 'meetings'. 'all' (tất cả các cuộc họp) là đáp án đúng (A)."
    },
    111: {
        "questionText": "The hairstylists at Urbanite Salon have ------- experience working with a variety of hair products.",
        "questionTextVi": "Các nhà tạo mẫu tóc tại Urbanite Salon có kinh nghiệm ------- khi làm việc với nhiều loại sản phẩm chăm sóc tóc.",
        "options": {"A": "considers", "B": "considerable", "C": "considerate", "D": "considering"},
        "optionsVi": {"A": "(A) cân nhắc (động từ)", "B": "(B) đáng kể / dày dặn (tính từ)", "C": "(C) chu đáo / ân cần", "D": "(D) xét đến"},
        "explanation": "Cần một tính từ bổ nghĩa cho danh từ không đếm được 'experience'. 'considerable experience' mang nghĩa kinh nghiệm dày dặn, đáng kể. 'considerate' nghĩa là chu đáo, ân cần (chỉ tính cách con người). Đáp án (B)."
    },
    112: {
        "questionText": "Both candidates are ------- suitable for the assistant manager position.",
        "questionTextVi": "Cả hai ứng viên đều phù hợp ------- cho vị trí trợ lý giám đốc.",
        "options": {"A": "permanently", "B": "promptly", "C": "equally", "D": "gradually"},
        "optionsVi": {"A": "(A) vĩnh viễn", "B": "(B) ngay lập tức", "C": "(C) như nhau / ngang nhau", "D": "(D) dần dần"},
        "explanation": "Chủ ngữ là 'Both candidates' (cả hai ứng viên). Trạng từ 'equally' (ngang nhau, như nhau) bổ nghĩa cho tính từ 'suitable': 'equally suitable' (phù hợp ngang nhau). Đáp án (C)."
    },
    113: {
        "questionText": "With the acquisition of Bloom Circuit, Wellstrom Hardware has ------- expanded its offerings and services.",
        "questionTextVi": "Với việc mua lại Bloom Circuit, Wellstrom Hardware đã mở rộng ------- các sản phẩm và dịch vụ của mình.",
        "options": {"A": "greater", "B": "greatness", "C": "great", "D": "greatly"},
        "optionsVi": {"A": "(A) lớn hơn", "B": "(B) sự vĩ đại", "C": "(C) to lớn (tính từ)", "D": "(D) rất nhiều / đáng kể (trạng từ)"},
        "explanation": "Vị trí giữa trợ động từ 'has' và quá khứ phân từ 'expanded' cần một trạng từ (adv) để bổ nghĩa: 'has greatly expanded' (đã mở rộng rất nhiều). Đáp án (D)."
    },
    114: {
        "questionText": "Please note that file names should not ------- capital letters or spaces.",
        "questionTextVi": "Xin lưu ý rằng tên tệp không nên ------- các chữ cái in hoa hoặc khoảng trắng.",
        "options": {"A": "differ", "B": "contain", "C": "match", "D": "pick"},
        "optionsVi": {"A": "(A) khác biệt", "B": "(B) chứa / bao gồm", "C": "(C) khớp", "D": "(D) chọn"},
        "explanation": "Sau 'should not' cần động từ nguyên thể chỉ nội dung của tên tệp: 'contain capital letters or spaces' (chứa chữ in hoa hoặc dấu cách). Đáp án (B)."
    },
    115: {
        "questionText": "The Sun-Tech ceiling fan has received more than 15,000 five-star reviews from ------- customers.",
        "questionTextVi": "Quạt trần Sun-Tech đã nhận được hơn 15.000 đánh giá năm sao từ các khách hàng -------.",
        "options": {"A": "satisfied", "B": "checked", "C": "adjusted", "D": "allowed"},
        "optionsVi": {"A": "(A) hài lòng (tính từ)", "B": "(B) đã kiểm tra", "C": "(C) đã điều chỉnh", "D": "(D) được cho phép"},
        "explanation": "Cụm danh từ quen thuộc trong thương mại: 'satisfied customers' (những khách hàng hài lòng). Nhận được đánh giá 5 sao từ khách hàng hài lòng. Đáp án (A)."
    },
    116: {
        "questionText": "Please ------- the Returns section of our Web site if you are unhappy with any part of your order.",
        "questionTextVi": "Vui lòng ------- mục Đổi trả trên trang web của chúng tôi nếu bạn không hài lòng với bất kỳ phần nào của đơn hàng.",
        "options": {"A": "visit", "B": "visits", "C": "visited", "D": "visiting"},
        "optionsVi": {"A": "(A) ghé thăm (nguyên mẫu)", "B": "(B) ghé thăm (ngôi 3 số ít)", "C": "(C) đã ghé thăm", "D": "(D) đang ghé thăm"},
        "explanation": "Câu mệnh lệnh bắt đầu bằng 'Please' yêu cầu động từ ở dạng nguyên thể không to (V-bare): 'Please visit the Returns section...'. Đáp án (A)."
    },
    117: {
        "questionText": "Ito Auto Group is offering excellent ------- on pre-owned vehicles this month.",
        "questionTextVi": "Tập đoàn Ô tô Ito đang đưa ra các mức giá / ưu đãi ------- tuyệt vời cho các phương tiện đã qua sử dụng trong tháng này.",
        "options": {"A": "trips", "B": "reasons", "C": "customs", "D": "deals"},
        "optionsVi": {"A": "(A) chuyến đi", "B": "(B) lý do", "C": "(C) phong tục / hải quan", "D": "(D) ưu đãi / món hời giá tốt"},
        "explanation": "Cụm từ 'offer excellent deals on vehicles' mang nghĩa cung cấp các mức giá ưu đãi/khuyến mãi hấp dẫn khi mua xe. Đáp án (D)."
    },
    118: {
        "questionText": "Product prices are influenced ------- such factors as consumer demand and retail competition.",
        "questionTextVi": "Giá sản phẩm bị ảnh hưởng ------- các yếu tố như nhu cầu của người tiêu dùng và sự cạnh tranh bán lẻ.",
        "options": {"A": "by", "B": "under", "C": "those", "D": "nearly"},
        "optionsVi": {"A": "(A) bởi", "B": "(B) dưới", "C": "(C) những cái đó", "D": "(D) gần như"},
        "explanation": "Cấu trúc câu bị động: 'be influenced by something' (bị ảnh hưởng bởi cái gì). Đáp án (A)."
    },
    119: {
        "questionText": "Monmouth Enterprises will be ------- prefabricated houses online starting on April 1.",
        "questionTextVi": "Doanh nghiệp Monmouth sẽ ------- nhà lắp ghép trực tuyến bắt đầu từ ngày 1 tháng 4.",
        "options": {"A": "predicting", "B": "passing", "C": "retaining", "D": "marketing"},
        "optionsVi": {"A": "(A) dự đoán", "B": "(B) vượt qua", "C": "(C) giữ lại", "D": "(D) tiếp thị / quảng bá bán hàng"},
        "explanation": "Cấu trúc tương lai tiếp diễn: 'will be marketing prefabricated houses online' (sẽ tiếp thị, chào bán nhà lắp ghép trên mạng). Đáp án (D)."
    },
    120: {
        "questionText": "All employees should familiarize ------- with the company's policies and procedures.",
        "questionTextVi": "Tất cả nhân viên nên tự làm quen ------- với các chính sách và quy trình của công ty.",
        "options": {"A": "their", "B": "them", "C": "theirs", "D": "themselves"},
        "optionsVi": {"A": "(A) của họ", "B": "(B) họ", "C": "(C) cái của họ", "D": "(D) chính bản thân họ"},
        "explanation": "Cụm động từ phản thân: 'familiarize oneself with something' (tự làm quen, tìm hiểu kỹ về cái gì). Với chủ ngữ số nhiều 'All employees', đại từ phản thân tương ứng là 'themselves' (D)."
    },
    121: {
        "questionText": "Custom furniture orders require a 50 percent deposit ------- the time of the order.",
        "questionTextVi": "Các đơn đặt hàng đồ nội thất theo yêu cầu đòi hỏi phải đặt cọc 50% ------- thời điểm đặt hàng.",
        "options": {"A": "as", "B": "off", "C": "into", "D": "at"},
        "optionsVi": {"A": "(A) như là", "B": "(B) tắt / khỏi", "C": "(C) vào trong", "D": "(D) vào lúc / tại"},
        "explanation": "Cụm giới từ chỉ thời điểm: 'at the time of the order' (vào thời điểm đặt hàng). Đáp án (D)."
    },
    122: {
        "questionText": "We are planning a ------- for the Klemner Corporation's twentieth anniversary.",
        "questionTextVi": "Chúng tôi đang lên kế hoạch cho một ------- nhân dịp kỷ niệm 20 năm thành lập Tập đoàn Klemner.",
        "options": {"A": "celebration", "B": "celebrated", "C": "celebrity", "D": "celebrate"},
        "optionsVi": {"A": "(A) lễ kỷ niệm / buổi tiệc mừng", "B": "(B) nổi tiếng (tính từ)", "C": "(C) người nổi tiếng", "D": "(D) kỷ niệm (động từ)"},
        "explanation": "Sau mạo từ 'a' cần một danh từ số ít chỉ sự kiện: 'a celebration' (một buổi lễ kỷ niệm). Đáp án (A)."
    },
    123: {
        "questionText": "Though she lacks political experience, Ms. Diaz has been ------- impressive in her first term as mayor.",
        "questionTextVi": "Mặc dù thiếu kinh nghiệm chính trị, bà Diaz đã gây ấn tượng ------- trong nhiệm kỳ đầu tiên trên cương vị thị trưởng.",
        "options": {"A": "quite", "B": "soon", "C": "ever", "D": "next"},
        "optionsVi": {"A": "(A) khá là / rất", "B": "(B) sớm", "C": "(C) từng", "D": "(D) tiếp theo"},
        "explanation": "Phó từ 'quite' bổ nghĩa cho tính từ 'impressive': 'quite impressive' (khá là ấn tượng). Đáp án (A)."
    },
    124: {
        "questionText": "The university library usually acquires ------- copies of best-selling books to meet students' demand.",
        "questionTextVi": "Thư viện trường đại học thường mua ------- bản sao các cuốn sách bán chạy nhất để đáp ứng nhu cầu của sinh viên.",
        "options": {"A": "multiply", "B": "multiple", "C": "multiples", "D": "multiplicity"},
        "optionsVi": {"A": "(A) nhân lên (động từ)", "B": "(B) nhiều (tính từ)", "C": "(C) bội số", "D": "(D) sự đa dạng"},
        "explanation": "Trước danh từ số nhiều 'copies' cần một tính từ bổ nghĩa: 'multiple copies' (nhiều bản sao / nhiều cuốn sách). Đáp án (B)."
    },
    125: {
        "questionText": "This year's conference tote bags were ------- donated by Etani Designs.",
        "questionTextVi": "Những chiếc túi tote tại hội nghị năm nay đã được Etani Designs quyên tặng một cách -------.",
        "options": {"A": "generous", "B": "generosity", "C": "generously", "D": "generosities"},
        "optionsVi": {"A": "(A) hào phóng (tính từ)", "B": "(B) sự hào phóng", "C": "(C) một cách hào phóng (trạng từ)", "D": "(D) các sự hào phóng"},
        "explanation": "Vị trí giữa to-be 'were' và quá khứ phân từ 'donated' cần một trạng từ (adv) bổ nghĩa: 'generously donated' (được quyên tặng một cách hào phóng). Đáp án (C)."
    },
    126: {
        "questionText": "We will be holding a ------- on Friday to honor the 30-year engineering career of Mr. Kuan.",
        "questionTextVi": "Chúng tôi sẽ tổ chức một ------- vào thứ Sáu để vinh danh sự nghiệp kỹ thuật 30 năm của ông Kuan.",
        "options": {"A": "record", "B": "share", "C": "reception", "D": "place"},
        "optionsVi": {"A": "(A) hồ sơ / kỷ lục", "B": "(B) cổ phần", "C": "(C) buổi chiêu đãi / tiệc đón tiếp", "D": "(D) địa điểm"},
        "explanation": "Cụm 'hold a reception' (tổ chức một buổi tiệc chiêu đãi để vinh danh ai đó). Đáp án (C)."
    },
    127: {
        "questionText": "Groove Background creates soothing playlists of instrumental music, ------- classical and jazz.",
        "questionTextVi": "Groove Background tạo ra các danh sách phát nhạc không lời êm dịu, ------- cả nhạc cổ điển và nhạc jazz.",
        "options": {"A": "instead", "B": "including", "C": "in addition", "D": "indeed"},
        "optionsVi": {"A": "(A) thay vì", "B": "(B) bao gồm", "C": "(C) ngoài ra (cần 'to')", "D": "(D) thực sự"},
        "explanation": "Giới từ 'including' dùng để đưa ra các ví dụ cụ thể cho danh từ đứng trước: 'instrumental music, including classical and jazz'. Đáp án (B)."
    },
    128: {
        "questionText": "Members of the finance department ------- to Mr. Chua's lecture on risk avoidance.",
        "questionTextVi": "Các thành viên của phòng tài chính ------- tham dự bài giảng của ông Chua về phòng tránh rủi ro.",
        "options": {"A": "to be invited", "B": "inviting", "C": "invite", "D": "are invited"},
        "optionsVi": {"A": "(A) để được mời", "B": "(B) đang mời", "C": "(C) mời (chủ động)", "D": "(D) được mời (bị động)"},
        "explanation": "Câu thiếu vị ngữ chia thì đầy đủ mang nghĩa bị động: 'are invited to' (được mời tham dự). Đáp án (D)."
    },
    129: {
        "questionText": "The board of trustees debated for hours ------- the revised hiring policies.",
        "questionTextVi": "Hội đồng quản trị đã tranh luận suốt nhiều giờ ------- các chính sách tuyển dụng sửa đổi.",
        "options": {"A": "during", "B": "above", "C": "over", "D": "across"},
        "optionsVi": {"A": "(A) trong suốt", "B": "(B) phía trên", "C": "(C) về / xoay quanh (vấn đề)", "D": "(D) băng qua"},
        "explanation": "Cụm động từ: 'debate over something' (tranh luận, thảo luận sôi nổi về một chủ đề/chính sách nào đó). Đáp án (C)."
    },
    130: {
        "questionText": "The participants closely ------- the fitness instructor's movements tend to learn the proper technique more quickly.",
        "questionTextVi": "Những người tham gia quan sát và bắt chước chặt chẽ ------- các động tác của huấn luyện viên thể hình có xu hướng học kỹ thuật đúng nhanh hơn.",
        "options": {"A": "imitate", "B": "imitations", "C": "imitative", "D": "imitating"},
        "optionsVi": {"A": "(A) bắt chước (chia thì)", "B": "(B) các sự bắt chước", "C": "(C) có tính bắt chước", "D": "(D) bắt chước (phân từ hiện tại rút gọn)"},
        "explanation": "Câu đã có động từ chính là 'tend to learn'. Thành phần đứng sau 'The participants' là mệnh đề quan hệ rút gọn ở thể chủ động: 'who closely imitate...' rút gọn thành 'closely imitating...'. Đáp án (D)."
    }
}

# LC specific question updates for Test 4
t4_lc_addons = {
    56: {"correctAnswer": "A"},
    61: {"correctAnswer": "B"},
    62: {"correctAnswer": "B"},
    83: {
        "questionText": "According to the speaker, why are some changes needed?",
        "questionTextVi": "Theo người nói, tại sao một số thay đổi lại cần thiết?",
        "options": {
            "A": "To retain employees",
            "B": "To attract investors",
            "C": "To satisfy customers",
            "D": "To increase productivity"
        },
        "optionsVi": {
            "A": "(A) Để giữ chân nhân viên",
            "B": "(B) Để thu hút các nhà đầu tư",
            "C": "(C) Để làm hài lòng khách hàng",
            "D": "(D) Để tăng năng suất lao động"
        },
        "correctAnswer": "C",
        "explanation": "Người nói chỉ ra rằng các thay đổi này được đưa ra nhằm đáp ứng kỳ vọng và làm hài lòng khách hàng (C)."
    },
    85: {
        "questionText": "According to the speaker, what will begin next month?",
        "questionTextVi": "Theo người nói, điều gì sẽ bắt đầu vào tháng tới?",
        "options": {
            "A": "A workshop series",
            "B": "A new corporate policy",
            "C": "A land development project",
            "D": "A business collaboration"
        },
        "optionsVi": {
            "A": "(A) Một chuỗi các buổi hội thảo",
            "B": "(B) Một chính sách mới của công ty",
            "C": "(C) Một dự án phát triển đất đai",
            "D": "(D) Một sự hợp tác kinh doanh"
        },
        "correctAnswer": "D",
        "explanation": "Người nói đề cập rằng sự hợp tác kinh doanh mới sẽ chính thức bắt đầu vào tháng sau (D)."
    }
}

# LC specific question updates for Test 5
t5_lc_addons = {
    37: {"correctAnswer": "A"},
    39: {"correctAnswer": "D"},
    82: {
        "questionText": "According to the speaker, what can the listeners do on a Web site?",
        "questionTextVi": "Theo người nói, người nghe có thể làm gì trên trang web?",
        "options": {
            "A": "Enter a contest",
            "B": "Subscribe to a video channel",
            "C": "Submit some photographs",
            "D": "Download some instructions"
        },
        "optionsVi": {
            "A": "(A) Tham gia một cuộc thi",
            "B": "(B) Đăng ký theo dõi kênh video",
            "C": "(C) Gửi một số bức ảnh chụp",
            "D": "(D) Tải xuống một số tài liệu hướng dẫn"
        },
        "correctAnswer": "D",
        "explanation": "Người nói cho biết tài liệu hướng dẫn chi tiết có sẵn trên trang web để thính giả tải về: 'You can download the full instructions from our website.' Đáp án (D)."
    },
    91: {"correctAnswer": "C"},
    96: {"correctAnswer": "D"}
}

# Apply to test4.json
with open('web/data/test4.json', encoding='utf-8') as f:
    t4_data = json.load(f)

for q in t4_data['questions']:
    qid = q['id']
    if qid in t4_p5:
        for k, v in t4_p5[qid].items():
            q[k] = v
    if qid in t4_lc_addons:
        for k, v in t4_lc_addons[qid].items():
            q[k] = v
    # Always enforce official key
    qid_str = str(qid)
    if qid_str in official4:
        q['correctAnswer'] = official4[qid_str]

with open('web/data/test4.json', 'w', encoding='utf-8') as f:
    json.dump(t4_data, f, ensure_ascii=False, indent=2)

print('Updated Part 5 and LC for Test 4!')

# Apply to test5.json
with open('web/data/test5.json', encoding='utf-8') as f:
    t5_data = json.load(f)

for q in t5_data['questions']:
    qid = q['id']
    if qid in t5_p5:
        for k, v in t5_p5[qid].items():
            q[k] = v
    if qid in t5_lc_addons:
        for k, v in t5_lc_addons[qid].items():
            q[k] = v
    # Always enforce official key
    qid_str = str(qid)
    if qid_str in official5:
        q['correctAnswer'] = official5[qid_str]

with open('web/data/test5.json', 'w', encoding='utf-8') as f:
    json.dump(t5_data, f, ensure_ascii=False, indent=2)

print('Updated Part 5 and LC for Test 5!')
