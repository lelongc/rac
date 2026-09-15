import json, sys
sys.stdout.reconfigure(encoding='utf-8')

t4_fixes = {
    # Part 3 & 4
    37: {
        "questionText": "What does the woman offer to do?",
        "questionTextVi": "Người phụ nữ đề nghị làm gì?",
        "options": {
            "A": "Attend an event",
            "B": "Fill out an online form",
            "C": "Place an order",
            "D": "Search for an item"
        },
        "optionsVi": {
            "A": "(A) Tham dự một sự kiện",
            "B": "(B) Điền vào một mẫu đơn trực tuyến",
            "C": "(C) Đặt một đơn hàng",
            "D": "(D) Tìm kiếm một món đồ / mặt hàng"
        },
        "correctAnswer": "D",
        "explanation": "Người phụ nữ nói rằng cô ấy sẽ tìm kiếm sản phẩm cho khách hàng: 'Let me check our inventory and search for that item for you.' Do đó, đáp án đúng là (D)."
    },
    45: {
        "questionText": "What does the woman say recently happened?",
        "questionTextVi": "Người phụ nữ nói điều gì vừa mới xảy ra gần đây?",
        "options": {
            "A": "She earned a degree.",
            "B": "She won an award.",
            "C": "She got a promotion.",
            "D": "She transferred to a new location."
        },
        "optionsVi": {
            "A": "(A) Cô ấy đã nhận được một tấm bằng.",
            "B": "(B) Cô ấy đã giành được một giải thưởng.",
            "C": "(C) Cô ấy vừa được thăng chức.",
            "D": "(D) Cô ấy đã chuyển đến một địa điểm mới."
        },
        "correctAnswer": "C",
        "explanation": "Trong đoạn hội thoại, người phụ nữ nói: 'I did just get promoted at work recently, so I can afford to spend more.' (Gần đây tôi vừa được thăng chức tại chỗ làm, vì vậy tôi có khả năng chi trả nhiều hơn). Đáp án chính xác là (C)."
    },
    46: {
        "questionText": "What will the man do next?",
        "questionTextVi": "Người đàn ông sẽ làm gì tiếp theo?",
        "options": {
            "A": "Make a phone call",
            "B": "Prepare a contract",
            "C": "Drop off a key",
            "D": "Log some work hours"
        },
        "optionsVi": {
            "A": "(A) Thực hiện một cuộc gọi điện thoại",
            "B": "(B) Chuẩn bị một bản hợp đồng",
            "C": "(C) Giao / để lại một chiếc chìa khóa",
            "D": "(D) Ghi nhận giờ làm việc"
        },
        "correctAnswer": "A",
        "explanation": "Người đàn ông kết thúc cuộc trò chuyện bằng câu: 'I'll call the current tenant and we can figure out a time for a viewing.' (Tôi sẽ gọi cho người thuê nhà hiện tại và chúng ta có thể sắp xếp thời gian xem nhà). Hành động tiếp theo là gọi điện thoại (A)."
    },
    56: {
        "questionText": "Why does the man apologize?",
        "questionTextVi": "Tại sao người đàn ông xin lỗi?",
        "options": {
            "A": "He missed a meeting.",
            "B": "He has a poor Internet connection.",
            "C": "He failed to complete an assignment.",
            "D": "He lost his employee badge."
        },
        "optionsVi": {
            "A": "(A) Anh ấy đã bỏ lỡ một cuộc họp.",
            "B": "(B) Anh ấy có kết nối mạng Internet kém.",
            "C": "(C) Anh ấy đã không hoàn thành một nhiệm vụ.",
            "D": "(D) Anh ấy đã làm mất thẻ nhân viên của mình."
        },
        "correctAnswer": "B",
        "explanation": "Người đàn ông xin lỗi vì sự cố đường truyền mạng: 'I apologize, my Internet connection is very unstable today.' Đáp án đúng là (B)."
    },
    60: {
        "questionText": "Why does the woman say, \"They usually market to a younger clientele\"?",
        "questionTextVi": "Tại sao người phụ nữ lại nói: \"Họ thường tiếp thị tới nhóm khách hàng trẻ tuổi hơn\"?",
        "options": {
            "A": "To reject a suggestion",
            "B": "To justify a decision",
            "C": "To express disappointment",
            "D": "To ask for clarification"
        },
        "optionsVi": {
            "A": "(A) Để từ chối một gợi ý",
            "B": "(B) Để biện minh cho một quyết định",
            "C": "(C) Để bày tỏ sự thất vọng",
            "D": "(D) Để yêu cầu làm rõ thêm"
        },
        "correctAnswer": "A",
        "explanation": "Khi người đàn ông đề xuất hợp tác hoặc quảng cáo trên kênh nào đó, người phụ nữ nói 'They usually market to a younger clientele' để từ chối đề xuất này vì không phù hợp với phân khúc khách hàng của họ. Đáp án (A)."
    },
    61: {
        "questionText": "What does the man say he will give the woman?",
        "questionTextVi": "Người đàn ông nói anh ấy sẽ đưa cho người phụ nữ thứ gì?",
        "options": {
            "A": "An area map",
            "B": "A list of businesses",
            "C": "Some photographs",
            "D": "Some measurements"
        },
        "optionsVi": {
            "A": "(A) Một bản đồ khu vực",
            "B": "(B) Một danh sách các doanh nghiệp",
            "C": "(C) Một vài bức ảnh chụp",
            "D": "(D) Một vài số đo kích thước"
        },
        "correctAnswer": "C",
        "explanation": "Người đàn ông hứa sẽ gửi cho người phụ nữ một số bức ảnh: 'I'll provide you with some photographs taken yesterday.' Đáp án đúng là (C)."
    },
    62: {
        "questionText": "Look at the graphic. Who is the woman?",
        "questionTextVi": "Nhìn vào hình ảnh. Người phụ nữ là ai?",
        "options": {
            "A": "Liliana Flores",
            "B": "Svetlana Popova",
            "C": "Lauren Campbell",
            "D": "So-Jin Park"
        },
        "optionsVi": {
            "A": "(A) Liliana Flores",
            "B": "(B) Svetlana Popova",
            "C": "(C) Lauren Campbell",
            "D": "(D) So-Jin Park"
        },
        "correctAnswer": "A",
        "explanation": "Trong hội thoại, người phụ nữ thảo luận về việc thiết kế bối cảnh sân khấu (Set designer). Đối chiếu bảng phân công: Set designer là Liliana Flores. Đáp án (A)."
    },
    64: {
        "questionText": "What will happen next week?",
        "questionTextVi": "Điều gì sẽ diễn ra vào tuần tới?",
        "options": {
            "A": "A playwright will attend a show.",
            "B": "Publicity photos will be taken.",
            "C": "A play will open.",
            "D": "A dress rehearsal will be held."
        },
        "optionsVi": {
            "A": "(A) Một nhà viết kịch sẽ tham dự buổi diễn.",
            "B": "(B) Các bức ảnh quảng bá sẽ được chụp.",
            "C": "(C) Một vở kịch sẽ chính thức công diễn.",
            "D": "(D) Một buổi tổng duyệt trang phục sẽ được tổ chức."
        },
        "correctAnswer": "C",
        "explanation": "Các nhân vật đề cập rằng buổi biểu diễn/vở kịch sẽ chính thức ra mắt vào tuần sau: 'The play opens next week.' Đáp án (C)."
    },
    68: {
        "questionText": "What is the conversation mostly about?",
        "questionTextVi": "Cuộc trò chuyện chủ yếu nói về điều gì?",
        "options": {
            "A": "Organizing an exhibit",
            "B": "Arranging a public tour",
            "C": "Filming a documentary",
            "D": "Requesting financial support"
        },
        "optionsVi": {
            "A": "(A) Tổ chức một buổi triển lãm",
            "B": "(B) Sắp xếp một chuyến tham quan công cộng",
            "C": "(C) Quay một bộ phim tài liệu",
            "D": "(D) Yêu cầu hỗ trợ tài chính"
        },
        "correctAnswer": "C",
        "explanation": "Người phụ nữ giới thiệu: 'Since it's our first day of filming for our TV documentary special, we're mainly going to capture general footage of your team at work.' Cuộc hội thoại nói về việc quay phim tài liệu (C)."
    },
    69: {
        "questionText": "Look at the graphic. Which part of the castle is being excavated today?",
        "questionTextVi": "Nhìn vào hình ảnh. Khu vực nào của lâu đài đang được khai quật hôm nay?",
        "options": {
            "A": "The garden",
            "B": "The kitchen",
            "C": "The tower",
            "D": "The great hall"
        },
        "optionsVi": {
            "A": "(A) Khu vườn (Garden)",
            "B": "(B) Nhà bếp (Kitchen)",
            "C": "(C) Tòa tháp (Tower)",
            "D": "(D) Đại sảnh (Great Hall)"
        },
        "correctAnswer": "B",
        "explanation": "Người đàn ông nói: 'We're working in quadrant two today.' Đối chiếu hình vẽ: Quadrant 2 tương ứng với 'Kitchen'. Đáp án là (B)."
    },
    70: {
        "questionText": "According to the man, why has some work been delayed?",
        "questionTextVi": "Theo người đàn ông, tại sao một phần công việc đã bị trì hoãn?",
        "options": {
            "A": "An archaeological team is very small.",
            "B": "Weather conditions have been poor.",
            "C": "A source of funding was unavailable.",
            "D": "New volunteers required special training."
        },
        "optionsVi": {
            "A": "(A) Đội khảo cổ có quy mô rất nhỏ.",
            "B": "(B) Điều kiện thời tiết xấu / bất lợi.",
            "C": "(C) Nguồn tài trợ không có sẵn.",
            "D": "(D) Các tình nguyện viên mới cần đào tạo đặc biệt."
        },
        "correctAnswer": "B",
        "explanation": "Người đàn ông giải thích: 'There've been lots of thunderstorms lately, which have slowed things down.' (Dạo này có nhiều dông bão khiến tiến độ bị chậm lại). Điều kiện thời tiết xấu (B)."
    },
    82: {
        "questionText": "What additional service is mentioned?",
        "questionTextVi": "Dịch vụ bổ sung nào được đề cập?",
        "options": {
            "A": "A catered meal",
            "B": "A shuttle bus",
            "C": "Technical support",
            "D": "Secure storage"
        },
        "optionsVi": {
            "A": "(A) Bữa ăn phục vụ tận nơi",
            "B": "(B) Xe buýt đưa đón trung chuyển",
            "C": "(C) Hỗ trợ kỹ thuật",
            "D": "(D) Lưu trữ an toàn"
        },
        "correctAnswer": "B",
        "explanation": "Người nói nhắc đến dịch vụ bổ sung là tuyến xe buýt đưa đón: 'We also offer a complimentary shuttle bus service to the venue.' Đáp án (B)."
    },
    86: {
        "questionText": "What industry does the speaker most likely work in?",
        "questionTextVi": "Người nói có nhiều khả năng nhất làm việc trong ngành nào?",
        "options": {
            "A": "Civil service",
            "B": "Hospitality",
            "C": "Media",
            "D": "Architecture"
        },
        "optionsVi": {
            "A": "(A) Công vụ / dịch vụ hành chính công",
            "B": "(B) Khách sạn - nhà hàng",
            "C": "(C) Truyền thông / báo chí",
            "D": "(D) Kiến trúc"
        },
        "correctAnswer": "C",
        "explanation": "Người nói nhắc tới: 'We were able to beat the other networks in getting that interview to the public.' Ngữ cảnh mạng lưới truyền hình / phỏng vấn thuộc ngành truyền thông (Media - C)."
    },
    99: {
        "questionText": "Why is a building special?",
        "questionTextVi": "Tại sao tòa nhà lại đặc biệt?",
        "options": {
            "A": "It was constructed in a short time.",
            "B": "It has a technologically advanced security system.",
            "C": "It has environmentally friendly features.",
            "D": "It was designed by a famous architect."
        },
        "optionsVi": {
            "A": "(A) Nó được xây dựng trong thời gian ngắn.",
            "B": "(B) Nó có hệ thống an ninh công nghệ cao.",
            "C": "(C) Nó có các đặc điểm thân thiện với môi trường.",
            "D": "(D) Nó được thiết kế bởi một kiến trúc sư nổi tiếng."
        },
        "correctAnswer": "C",
        "explanation": "Người nói nhấn mạnh: 'Notice the environmentally friendly elements incorporated into the structure...' (Hãy chú ý các yếu tố thân thiện với môi trường được tích hợp vào công trình). Đáp án (C)."
    },
    # Part 6 & 7
    142: {
        "questionText": "Select the best answer for blank [142]:",
        "questionTextVi": "Chọn đáp án thích hợp nhất cho chỗ trống [142]:",
        "options": {
            "A": "save",
            "B": "work",
            "C": "shop",
            "D": "register"
        },
        "optionsVi": {
            "A": "(A) tiết kiệm / lưu trữ",
            "B": "(B) làm việc",
            "C": "(C) mua sắm",
            "D": "(D) đăng ký"
        },
        "correctAnswer": "B",
        "explanation": "Câu trong bài: 'Approximately 75 percent of all employees live within two miles of the store where they work.' (Khoảng 75% nhân viên sống trong phạm vi 2 dặm tính từ cửa hàng nơi họ làm việc). Chủ ngữ 'they' chỉ 'employees' nên động từ phù hợp là 'work' (B)."
    },
    151: {
        "questionText": "What most likely has Ms. Dibello purchased?",
        "questionTextVi": "Bà Dibello có nhiều khả năng nhất đã mua thứ gì?",
        "options": {
            "A": "Linens",
            "B": "Bookshelves",
            "C": "Gardening tools",
            "D": "Appliances"
        },
        "optionsVi": {
            "A": "(A) Khăn trải giường / khăn vải",
            "B": "(B) Giá sách",
            "C": "(C) Dụng cụ làm vườn",
            "D": "(D) Thiết bị gia dụng (bếp)"
        },
        "correctAnswer": "D",
        "explanation": "Maxine nói: 'She says she needs to set up her kitchen properly so that she can prepare a special meal tonight.' (Bà ấy nói cần lắp đặt nhà bếp cẩn thận để chuẩn bị bữa ăn đặc biệt tối nay). Mặt hàng lắp đặt nhà bếp để nấu ăn là các thiết bị gia dụng (Appliances - D)."
    },
    152: {
        "questionText": "At 11:17 A.M., what does Ms. Larsen most likely mean when she writes, \"What's your estimate\"?",
        "questionTextVi": "Vào lúc 11:17 sáng, bà Larsen có ý gì khi viết: \"What's your estimate\" (Ước tính của anh là thế nào)?",
        "options": {
            "A": "She must verify the distance of a route.",
            "B": "She wants to know how much traffic there is.",
            "C": "She wants to know a delivery time.",
            "D": "She has to calculate a delivery charge."
        },
        "optionsVi": {
            "A": "(A) Cô ấy phải xác minh khoảng cách của lộ trình.",
            "B": "(B) Cô ấy muốn biết mức độ tắc đường là bao nhiêu.",
            "C": "(C) Cô ấy muốn biết thời gian giao hàng ước tính.",
            "D": "(D) Cô ấy phải tính toán phí giao hàng."
        },
        "correctAnswer": "C",
        "explanation": "Sau khi nghe Frank nói về việc tắc đường và đường sửa chữa, Larsen hỏi 'What's your estimate?' và Frank trả lời 'Maybe around 1 P.M.'. Như vậy Larsen đang hỏi ước tính giờ giao hàng đến nơi (C)."
    },
    161: {
        "questionText": "What is indicated about Martino Technical?",
        "questionTextVi": "Điều gì được chỉ ra về Martino Technical?",
        "options": {
            "A": "It acquires most clients through social media.",
            "B": "It was founded over 30 years ago.",
            "C": "It has received many industry awards.",
            "D": "It has offices throughout the world."
        },
        "optionsVi": {
            "A": "(A) Nó tìm kiếm hầu hết khách hàng qua mạng xã hội.",
            "B": "(B) Nó được thành lập hơn 30 năm trước.",
            "C": "(C) Nó đã nhận được nhiều giải thưởng trong ngành.",
            "D": "(D) Nó có các văn phòng trên khắp thế giới."
        },
        "correctAnswer": "B",
        "explanation": "Dòng đầu tiên của bài quảng cáo: 'Martino Technical has been providing live sound-mixing services for more than 30 years.' (Martino Technical đã cung cấp dịch vụ hòa âm trực tiếp hơn 30 năm qua). Tương đương với được thành lập hơn 30 năm trước (B)."
    },
    162: {
        "questionText": "The word \"promote\" in paragraph 2, line 4, is closest in meaning to",
        "questionTextVi": "Từ \"promote\" ở đoạn 2, dòng 4 có nghĩa gần nhất với từ nào?",
        "options": {
            "A": "encourage",
            "B": "schedule",
            "C": "publicize",
            "D": "advance"
        },
        "optionsVi": {
            "A": "(A) khuyến khích, động viên",
            "B": "(B) lên lịch trình",
            "C": "(C) quảng bá, tuyên truyền",
            "D": "(D) nâng cao, tiến bộ"
        },
        "correctAnswer": "C",
        "explanation": "Câu trong bài: '...that they can post on social media to promote their shows.' (mà họ có thể đăng lên mạng xã hội để quảng bá các buổi diễn của mình). 'promote' ở đây có nghĩa là quảng bá, truyền thông, đồng nghĩa với 'publicize' (C)."
    },
    176: {
        "questionText": "What can be inferred about Mr. Torres?",
        "questionTextVi": "Có thể suy ra điều gì về ông Torres?",
        "options": {
            "A": "He is moving to a new home.",
            "B": "He recently bought a car.",
            "C": "He will be retiring soon.",
            "D": "He recently opened a bank account."
        },
        "optionsVi": {
            "A": "(A) Ông ấy đang chuyển đến một ngôi nhà mới.",
            "B": "(B) Ông ấy gần đây vừa mới mua một chiếc ô tô.",
            "C": "(C) Ông ấy sẽ sớm nghỉ hưu.",
            "D": "(D) Ông ấy gần đây vừa mở tài khoản ngân hàng."
        },
        "correctAnswer": "B",
        "explanation": "Bức thư đầu viết: 'We are pleased to provide you with comprehensive automobile insurance for your new vehicle.' (Chúng tôi hân hạnh cung cấp bảo hiểm toàn diện cho chiếc xe mới của bạn). Bức thư hồi đáp cũng ghi: 'the new car is now registered in my name'. Do đó ông Torres vừa mua xe mới (B)."
    },
    177: {
        "questionText": "In the first e-mail, the word \"coverage\" in paragraph 1, line 3, is closest in meaning to",
        "questionTextVi": "Trong email đầu tiên, từ \"coverage\" ở đoạn 1, dòng 3 có nghĩa gần nhất với từ nào?",
        "options": {
            "A": "measurement",
            "B": "information",
            "C": "commentary",
            "D": "protection"
        },
        "optionsVi": {
            "A": "(A) sự đo lường",
            "B": "(B) thông tin",
            "C": "(C) bài bình luận",
            "D": "(D) sự bảo vệ, bảo hiểm"
        },
        "correctAnswer": "D",
        "explanation": "Trong hợp đồng bảo hiểm: 'your coverage is now in effect' (sự bảo vệ / phạm vi bảo hiểm của bạn đã bắt đầu có hiệu lực). 'coverage' đồng nghĩa với 'protection' (sự bảo vệ tài chính khi rủi ro) (D)."
    },
    178: {
        "questionText": "What does Ms. Patel recommend that Mr. Torres do?",
        "questionTextVi": "Bà Patel khuyến nghị ông Torres làm điều gì?",
        "options": {
            "A": "Call an agent if needed",
            "B": "Register at a local office",
            "C": "Place an order promptly",
            "D": "Revise an agreement"
        },
        "optionsVi": {
            "A": "(A) Gọi cho nhân viên đại diện nếu cần thiết",
            "B": "(B) Đăng ký tại văn phòng địa phương",
            "C": "(C) Đặt hàng nhanh chóng",
            "D": "(D) Sửa đổi thỏa thuận"
        },
        "correctAnswer": "A",
        "explanation": "Email của Patel nêu rõ: 'In the event of a vehicle incident, please contact an agent as soon as possible at 020 7946 0520.' Khuyến nghị gọi đại lý khi cần (A)."
    },
    186: {
        "questionText": "What does the report indicate about the Yuma County region?",
        "questionTextVi": "Báo cáo chỉ ra điều gì về khu vực Hạt Yuma?",
        "options": {
            "A": "It does not tax fruit that is sold there.",
            "B": "Several types of fruit are cultivated there.",
            "C": "More workers are needed for agricultural jobs.",
            "D": "New types of fruit are being produced there."
        },
        "optionsVi": {
            "A": "(A) Nơi đây không đánh thuế trái cây bán ra.",
            "B": "(B) Một số loại trái cây khác nhau được canh tác ở đó.",
            "C": "(C) Cần thêm nhiều lao động cho các công việc nông nghiệp.",
            "D": "(D) Các loại trái cây mới đang được sản xuất ở đó."
        },
        "correctAnswer": "B",
        "explanation": "Báo cáo liệt kê nhiều loại quả có múi được trồng: lemons (chanh vàng), oranges (cam), grapefruit (bưởi chùm). Do đó 'Several types of fruit are cultivated there' (B)."
    },
    187: {
        "questionText": "What is one reason Ms. Schreiber writes to Mr. Ramirez?",
        "questionTextVi": "Một lý do khiến bà Schreiber viết thư cho ông Ramirez là gì?",
        "options": {
            "A": "To explain the benefits of doing business together",
            "B": "To clarify information in the report",
            "C": "To remind him to make a loan payment",
            "D": "To offer him advice from university agricultural researchers"
        },
        "optionsVi": {
            "A": "(A) Để giải thích lợi ích của việc hợp tác kinh doanh cùng nhau",
            "B": "(B) Để làm rõ thông tin trong báo cáo",
            "C": "(C) Để nhắc ông ấy thanh toán khoản vay",
            "D": "(D) Để đưa ra lời khuyên từ các nhà nghiên cứu nông nghiệp đại học"
        },
        "correctAnswer": "A",
        "explanation": "Schreiber viết cho Ramirez (Giám đốc Sở Nông nghiệp Arizona): 'City West Bank wants to help... We offer low-interest loans and provide expert advice... Together, we can accomplish great things.' Mục đích là giải thích các lợi ích khi hợp tác với ngân hàng (A)."
    },
    188: {
        "questionText": "According to the letter, why do tourists visit Yuma County?",
        "questionTextVi": "Theo bức thư, tại sao khách du lịch lại đến thăm Hạt Yuma?",
        "options": {
            "A": "To shop at farmers markets",
            "B": "To take pictures",
            "C": "To enjoy theme parks",
            "D": "To observe wildlife"
        },
        "optionsVi": {
            "A": "(A) Để mua sắm tại chợ nông sản",
            "B": "(B) Để chụp ảnh",
            "C": "(C) Để vui chơi ở công viên giải trí",
            "D": "(D) Để quan sát đời sống hoang dã (ngắm chim)"
        },
        "correctAnswer": "D",
        "explanation": "Bức thư đề cập: '...agritourism in southwest Arizona is growing as a result of the popularity of farm tours, bird-watching, and scenic country lodging...'. 'bird-watching' (ngắm chim) chính là quan sát động vật hoang dã (observe wildlife - D)."
    },
    189: {
        "questionText": "What is suggested about Mr. Ramirez?",
        "questionTextVi": "Điều gì được gợi ý về ông Ramirez?",
        "options": {
            "A": "He accepted Ms. Schreiber's proposal.",
            "B": "He used to be employed by City West Bank.",
            "C": "He is a member of the Yuma Chamber of Commerce.",
            "D": "He recently bought a citrus farm."
        },
        "optionsVi": {
            "A": "(A) Ông ấy đã chấp nhận lời đề xuất của bà Schreiber.",
            "B": "(B) Ông ấy từng làm việc cho ngân hàng City West Bank.",
            "C": "(C) Ông ấy là thành viên của Phòng Thương mại Yuma.",
            "D": "(D) Ông ấy gần đây đã mua một trang trại trồng cây ăn quả."
        },
        "correctAnswer": "A",
        "explanation": "Bài báo thứ 3 cho biết: 'Ms. Schreiber's efforts in working with the director of the Arizona Agriculture Division have significantly boosted citrus production.' Điều này chứng minh ông Ramirez (Giám đốc Sở) đã đồng ý hợp tác theo đề xuất của Schreiber (A)."
    },
    190: {
        "questionText": "For what accomplishment does Mr. Dolle praise Ms. Schreiber?",
        "questionTextVi": "Chủ tịch Dolle khen ngợi bà Schreiber vì thành tựu nào?",
        "options": {
            "A": "Arranging the shipping of agricultural products",
            "B": "Opening many City West Bank branch offices",
            "C": "Helping to increase grapefruit production to 15,000 boxes",
            "D": "Promoting Yuma County as a vacation destination"
        },
        "optionsVi": {
            "A": "(A) Thu xếp việc vận chuyển nông sản",
            "B": "(B) Mở nhiều chi nhánh ngân hàng City West Bank",
            "C": "(C) Giúp tăng sản lượng bưởi chùm lên 15.000 thùng",
            "D": "(D) Quảng bá Hạt Yuma như một điểm đến nghỉ dưỡng"
        },
        "correctAnswer": "C",
        "explanation": "Trong bài báo, Dolle nói: 'Yuma County now produces as many grapefruit as it does oranges.' Báo cáo ban đầu cho thấy cam là 15.000 thùng còn bưởi chùm là 9.000 thùng. Khi sản lượng bưởi bằng cam, tức là đã tăng lên 15.000 thùng (C)."
    },
    194: {
        "questionText": "What do Ms. Smith and Mr. Hilliard have in common?",
        "questionTextVi": "Bà Smith và ông Hilliard có điểm chung gì?",
        "options": {
            "A": "They cofounded Clear Path.",
            "B": "They are colleagues at Pryor and Martell.",
            "C": "They were classmates at Turnbull University.",
            "D": "They both conducted research in Nigeria."
        },
        "optionsVi": {
            "A": "(A) Họ cùng đồng sáng lập Clear Path.",
            "B": "(B) Họ là đồng nghiệp tại Pryor and Martell.",
            "C": "(C) Họ là bạn học cùng lớp tại Đại học Turnbull.",
            "D": "(D) Cả hai người đều từng thực hiện nghiên cứu tại Nigeria."
        },
        "correctAnswer": "D",
        "explanation": "Trang web nói Hilliard 'carried out extensive research on emerging markets in West Africa while teaching business management in Lagos, Nigeria'. Trong email, Smith viết: 'My research in Lagos ended last year'. Cả hai đều từng nghiên cứu tại Lagos, Nigeria (D)."
    },
    195: {
        "questionText": "What is one purpose of Ms. Smith's e-mail to Mr. Hilliard?",
        "questionTextVi": "Một mục đích trong email của bà Smith gửi cho ông Hilliard là gì?",
        "options": {
            "A": "To request his professional services",
            "B": "To provide a professional reference",
            "C": "To conduct an informational interview",
            "D": "To apply for a position at Albright School of Business"
        },
        "optionsVi": {
            "A": "(A) Để yêu cầu các dịch vụ chuyên môn của ông ấy",
            "B": "(B) Để cung cấp người tham chiếu chuyên môn",
            "C": "(C) Để thực hiện một buổi phỏng vấn thu thập thông tin",
            "D": "(D) Để nộp đơn ứng tuyển tại Trường Kinh doanh Albright"
        },
        "correctAnswer": "A",
        "explanation": "Smith viết rằng cháu trai cô muốn học đại học tại Mỹ: '...hoping I could put you both in touch so that he can take advantage of your new company's expertise in this area.' (sử dụng dịch vụ tư vấn du học Clear Path của Hilliard). Đáp án là (A)."
    }
}

t5_fixes = {
    # Part 3 & 4
    32: {
        "questionText": "What problem does the woman describe?",
        "questionTextVi": "Người phụ nữ mô tả vấn đề gì?",
        "options": {
            "A": "A room is not available.",
            "B": "A window will not open.",
            "C": "A projector is not working.",
            "D": "The weather has changed suddenly."
        },
        "optionsVi": {
            "A": "(A) Một phòng họp không có sẵn.",
            "B": "(B) Một chiếc cửa sổ không thể mở được.",
            "C": "(C) Một chiếc máy chiếu không hoạt động.",
            "D": "(D) Thời tiết thay đổi đột ngột."
        },
        "correctAnswer": "C",
        "explanation": "Người phụ nữ gặp sự cố với máy chiếu trong phòng họp: 'The projector in the conference room isn't turning on.' Đáp án là (C)."
    },
    34: {
        "questionText": "What does the man hand to the woman?",
        "questionTextVi": "Người đàn ông đưa cho người phụ nữ thứ gì?",
        "options": {
            "A": "An umbrella",
            "B": "Some keys",
            "C": "A cable",
            "D": "Some printouts"
        },
        "optionsVi": {
            "A": "(A) Một chiếc ô",
            "B": "(B) Một vài chiếc chìa khóa",
            "C": "(C) Một sợi dây cáp",
            "D": "(D) Một số tài liệu in"
        },
        "correctAnswer": "C",
        "explanation": "Người đàn ông nói: 'By the way, you'll need a special cable to connect your laptop. Here, take this one.' Anh ấy đưa cho cô một sợi cáp (C)."
    },
    37: {
        "questionText": "What does the man tell the woman to do?",
        "questionTextVi": "Người đàn ông bảo người phụ nữ làm gì?",
        "options": {
            "A": "Arrive early",
            "B": "Pay a fee",
            "C": "Wear a name badge",
            "D": "Choose a menu option"
        },
        "optionsVi": {
            "A": "(A) Đến sớm",
            "B": "(B) Nộp lệ phí",
            "C": "(C) Đeo thẻ tên",
            "D": "(D) Chọn một món trong thực đơn"
        },
        "correctAnswer": "C",
        "explanation": "Người đàn ông nhắc nhở: 'Make sure you wear your name badge at all times during the conference.' Yêu cầu đeo thẻ tên (C)."
    },
    39: {
        "questionText": "What does the man offer to do?",
        "questionTextVi": "Người đàn ông đề nghị làm gì?",
        "options": {
            "A": "Authorize free shipping",
            "B": "Apply a discount",
            "C": "Provide a sample",
            "D": "Make a recommendation"
        },
        "optionsVi": {
            "A": "(A) Cho phép miễn phí vận chuyển",
            "B": "(B) Áp dụng mức giảm giá",
            "C": "(C) Cung cấp sản phẩm mẫu",
            "D": "(D) Đưa ra lời giới thiệu / khuyến nghị"
        },
        "correctAnswer": "B",
        "explanation": "Người đàn ông đề xuất giảm giá cho khách hàng: 'Since you're buying in bulk, I can apply a ten percent discount to your order.' Đáp án (B)."
    },
    40: {
        "questionText": "What does the woman ask about?",
        "questionTextVi": "Người phụ nữ hỏi về điều gì?",
        "options": {
            "A": "An expiration date",
            "B": "A manufacturer's guarantee",
            "C": "The origin of a product",
            "D": "The cost of a product"
        },
        "optionsVi": {
            "A": "(A) Ngày hết hạn / hạn sử dụng",
            "B": "(B) Bảo hành của nhà sản xuất",
            "C": "(C) Nguồn gốc xuất xứ sản phẩm",
            "D": "(D) Giá thành sản phẩm"
        },
        "correctAnswer": "A",
        "explanation": "Người phụ nữ hỏi: 'How long can these items be stored before they expire?' (Hỏi về hạn sử dụng - expiration date). Đáp án (A)."
    },
    41: {
        "questionText": "Why is the woman visiting?",
        "questionTextVi": "Tại sao người phụ nữ lại đến thăm?",
        "options": {
            "A": "To promote a product",
            "B": "To sign a contract",
            "C": "To tour a facility",
            "D": "To inspect some equipment"
        },
        "optionsVi": {
            "A": "(A) Để quảng bá một sản phẩm",
            "B": "(B) Để ký kết một hợp đồng",
            "C": "(C) Để tham quan cơ sở vật chất",
            "D": "(D) Để kiểm tra một số thiết bị"
        },
        "correctAnswer": "A",
        "explanation": "Người phụ nữ đến để giới thiệu và quảng bá giải pháp / sản phẩm công nghệ mới của công ty cô: 'I'm here today to introduce our new machine-monitoring software.' Đáp án (A)."
    },
    43: {
        "questionText": "What does the woman say her company can provide?",
        "questionTextVi": "Người phụ nữ nói công ty của cô ấy có thể cung cấp điều gì?",
        "options": {
            "A": "A new client discount",
            "B": "A training video",
            "C": "An extended warranty",
            "D": "Customer testimonials"
        },
        "optionsVi": {
            "A": "(A) Giảm giá cho khách hàng mới",
            "B": "(B) Video hướng dẫn đào tạo",
            "C": "(C) Bảo hành mở rộng",
            "D": "(D) Đánh giá chứng thực của khách hàng"
        },
        "correctAnswer": "B",
        "explanation": "Người phụ nữ nói rằng công ty cô có thể cung cấp video đào tạo để nhân viên dễ dàng làm quen với hệ thống: 'We can also provide comprehensive training videos for your team.' Đáp án (B)."
    },
    44: {
        "questionText": "Who most likely is the man?",
        "questionTextVi": "Người đàn ông có nhiều khả năng nhất là ai?",
        "options": {
            "A": "A theater employee",
            "B": "A taxi driver",
            "C": "A train conductor",
            "D": "A construction worker"
        },
        "optionsVi": {
            "A": "(A) Nhân viên rạp hát",
            "B": "(B) Tài xế taxi",
            "C": "(C) Người soát vé tàu",
            "D": "(D) Công nhân xây dựng"
        },
        "correctAnswer": "B",
        "explanation": "Người đàn ông đang lái xe chở khách và trao đổi về lộ trình đường sá: 'Where can I take you today?' Anh ấy là tài xế taxi (B)."
    },
    46: {
        "questionText": "What does the man say he will do?",
        "questionTextVi": "Người đàn ông nói anh ấy sẽ làm gì?",
        "options": {
            "A": "Ask for a refund",
            "B": "Take a different route",
            "C": "Postpone a trip",
            "D": "File a complaint"
        },
        "optionsVi": {
            "A": "(A) Yêu cầu hoàn tiền",
            "B": "(B) Đi theo một lộ trình khác",
            "C": "(C) Hoãn một chuyến đi",
            "D": "(D) Nộp đơn khiếu nại"
        },
        "correctAnswer": "B",
        "explanation": "Khi thấy đường phía trước đang đóng/tắc, người đàn ông nói: 'The main road is closed, so I will take a different route through the side streets.' (B)."
    },
    64: {
        "questionText": "Look at the graphic. Where will the man travel to next?",
        "questionTextVi": "Nhìn vào hình ảnh. Người đàn ông sẽ di chuyển đến đâu tiếp theo?",
        "options": {
            "A": "Shady Grove",
            "B": "Braddock Bay",
            "C": "Largo",
            "D": "Ashburn"
        },
        "optionsVi": {
            "A": "(A) Shady Grove",
            "B": "(B) Braddock Bay",
            "C": "(C) Largo",
            "D": "(D) Ashburn"
        },
        "correctAnswer": "D",
        "explanation": "Người đàn ông nói anh ấy sẽ bắt chuyến tàu Silver Line tiếp theo. Đối chiếu bảng thông tin: Tuyến Silver Line có điểm đến là 'Ashburn'. Đáp án (D)."
    },
    67: {
        "questionText": "What will the woman most likely do next?",
        "questionTextVi": "Người phụ nữ có nhiều khả năng nhất sẽ làm gì tiếp theo?",
        "options": {
            "A": "Move her car",
            "B": "Go to a patio",
            "C": "Make a reservation",
            "D": "Meet some friends"
        },
        "optionsVi": {
            "A": "(A) Di chuyển xe của cô ấy",
            "B": "(B) Đi ra khu vực sân hiên ngoài trời",
            "C": "(C) Đặt bàn trước",
            "D": "(D) Gặp gỡ vài người bạn"
        },
        "correctAnswer": "B",
        "explanation": "Sau khi chọn món xong, người phục vụ bảo bàn ngoài sân hiên đã sẵn sàng, người phụ nữ nói: 'Great, I'll head out to the patio right now.' Đáp án (B)."
    },
    69: {
        "questionText": "Look at the graphic. How far will the speakers hike?",
        "questionTextVi": "Nhìn vào hình ảnh. Những người nói sẽ đi bộ đường dài bao xa?",
        "options": {
            "A": "7 kilometers",
            "B": "5 kilometers",
            "C": "2 kilometers",
            "D": "1 kilometer"
        },
        "optionsVi": {
            "A": "(A) 7 km",
            "B": "(B) 5 km",
            "C": "(C) 2 km",
            "D": "(D) 1 km"
        },
        "correctAnswer": "B",
        "explanation": "Hai người thống nhất sẽ đi trên tuyến đường có thác nước (Waterfall Trail). Đối chiếu bản đồ: Tuyến đường Waterfall Trail dài 5 km. Đáp án (B)."
    },
    70: {
        "questionText": "What can the speakers do while waiting for the shuttle?",
        "questionTextVi": "Những người nói có thể làm gì trong khi chờ xe đưa đón?",
        "options": {
            "A": "Buy some snacks",
            "B": "Watch a video",
            "C": "Visit a gift shop",
            "D": "Rent some equipment"
        },
        "optionsVi": {
            "A": "(A) Mua một số đồ ăn nhẹ",
            "B": "(B) Xem một đoạn video",
            "C": "(C) Ghé thăm cửa hàng quà lưu niệm",
            "D": "(D) Thuê một số thiết bị"
        },
        "correctAnswer": "B",
        "explanation": "Người nói gợi ý: 'While we wait for the shuttle at the visitor center, we can watch a short informational video about the park.' Đáp án (B)."
    },
    83: {
        "questionText": "What is the speech mainly about?",
        "questionTextVi": "Bài phát biểu chủ yếu nói về điều gì?",
        "options": {
            "A": "A financial report",
            "B": "A round of promotions",
            "C": "A product prototype",
            "D": "A construction project"
        },
        "optionsVi": {
            "A": "(A) Một báo cáo tài chính",
            "B": "(B) Một đợt thăng chức",
            "C": "(C) Một sản phẩm mẫu thử nghiệm",
            "D": "(D) Một dự án xây dựng"
        },
        "correctAnswer": "D",
        "explanation": "Người nói mở đầu cuộc họp báo: '...the Grand Falls Bridge improvement work has been underway for almost a year.' Dự án cải tạo cầu là một dự án xây dựng (Construction project - D)."
    },
    85: {
        "questionText": "What will the next speaker discuss?",
        "questionTextVi": "Người nói tiếp theo sẽ thảo luận về điều gì?",
        "options": {
            "A": "A job fair",
            "B": "A school opening",
            "C": "A ceremony",
            "D": "A sporting event"
        },
        "optionsVi": {
            "A": "(A) Hội chợ việc làm",
            "B": "(B) Lễ khai giảng trường học",
            "C": "(C) Một buổi lễ (khánh thành)",
            "D": "(D) Một sự kiện thể thao"
        },
        "correctAnswer": "C",
        "explanation": "Người nói thông báo: 'After that, our special-events coordinator will discuss the bridge-opening ceremony that's being planned.' (buổi lễ khánh thành cầu - A ceremony - C)."
    },
    90: {
        "questionText": "Who will participate in a project?",
        "questionTextVi": "Ai sẽ tham gia vào dự án?",
        "options": {
            "A": "Biologists",
            "B": "Farmers",
            "C": "Airline pilots",
            "D": "Real estate agents"
        },
        "optionsVi": {
            "A": "(A) Các nhà sinh vật học",
            "B": "(B) Các nông dân",
            "C": "(C) Các phi công hàng không",
            "D": "(D) Các môi giới bất động sản"
        },
        "correctAnswer": "B",
        "explanation": "Dự án hợp tác nông nghiệp thu hút sự tham gia của các chủ trang trại địa phương (Farmers - B)."
    },
    91: {
        "questionText": "What will the participants receive?",
        "questionTextVi": "Những người tham gia sẽ nhận được gì?",
        "options": {
            "A": "Tickets to an industry event",
            "B": "Technical assistance",
            "C": "Financial compensation",
            "D": "Advertising advice"
        },
        "optionsVi": {
            "A": "(A) Vé tham dự một sự kiện ngành",
            "B": "(B) Hỗ trợ kỹ thuật",
            "C": "(C) Khoản bồi thường / tiền thù lao tài chính",
            "D": "(D) Lời khuyên về quảng cáo"
        },
        "correctAnswer": "B",
        "explanation": "Những người tham gia chương trình sẽ được cung cấp hỗ trợ kỹ thuật từ các chuyên gia (Technical assistance - B)."
    },
    93: {
        "questionText": "Why is the speaker calling?",
        "questionTextVi": "Tại sao người nói lại gọi điện?",
        "options": {
            "A": "To apologize for a cancellation",
            "B": "To confirm a delivery",
            "C": "To share a price quote",
            "D": "To update some contact information"
        },
        "optionsVi": {
            "A": "(A) Để xin lỗi vì một sự hủy bỏ",
            "B": "(B) Để xác nhận một đợt giao hàng",
            "C": "(C) Để chia sẻ bảng báo giá",
            "D": "(D) Để cập nhật thông tin liên hệ"
        },
        "correctAnswer": "B",
        "explanation": "Người nói gọi đến để xác nhận đơn hàng và thời gian giao hàng dự kiến tới địa chỉ của khách hàng (Confirm a delivery - B)."
    },
    95: {
        "questionText": "What is the purpose of the talk?",
        "questionTextVi": "Mục đích của bài nói là gì?",
        "options": {
            "A": "To discuss a schedule",
            "B": "To consider changing suppliers",
            "C": "To train employees",
            "D": "To develop an inventory system"
        },
        "optionsVi": {
            "A": "(A) Để thảo luận về một lịch trình",
            "B": "(B) Để xem xét thay đổi nhà cung cấp",
            "C": "(C) Để đào tạo nhân viên",
            "D": "(D) Để phát triển một hệ thống kiểm kê"
        },
        "correctAnswer": "C",
        "explanation": "Người nói bắt đầu: 'As part of your training, you'll be expected to learn which cleaning solutions are used on different surfaces...' Mục đích là đào tạo nhân viên mới (Train employees - C)."
    },
    96: {
        "questionText": "Look at the graphic. Which product does the speaker say is new?",
        "questionTextVi": "Nhìn vào hình ảnh. Người nói cho biết sản phẩm nào là sản phẩm mới?",
        "options": {
            "A": "Klennlee",
            "B": "Baxlon",
            "C": "Z-Factor",
            "D": "Clean Sure"
        },
        "optionsVi": {
            "A": "(A) Klennlee",
            "B": "(B) Baxlon",
            "C": "(C) Z-Factor",
            "D": "(D) Clean Sure"
        },
        "correctAnswer": "B",
        "explanation": "Người nói giới thiệu bình xịt tẩy rửa mới bổ sung vào tủ dụng cụ: 'The spray bottle on the top shelf is our newest addition.' Đối chiếu hình vẽ: Chai dạng xịt ở tầng trên là 'Baxlon'. Đáp án (B)."
    },
    # Part 5, 6, 7
    110: {
        "questionText": "Starting on October 8, ------- board of education meetings will be streamed live on the school district's Web site.",
        "questionTextVi": "Bắt đầu từ ngày 8 tháng 10, ------- các cuộc họp của hội đồng giáo dục sẽ được phát trực tiếp trên trang web của học khu.",
        "options": {
            "A": "all",
            "B": "so",
            "C": "that",
            "D": "to"
        },
        "optionsVi": {
            "A": "(A) tất cả",
            "B": "(B) vì vậy",
            "C": "(C) rằng, điều đó",
            "D": "(D) tới, để"
        },
        "correctAnswer": "A",
        "explanation": "Cần một từ hạn định bổ nghĩa cho danh từ số nhiều đếm được 'board of education meetings' (các cuộc họp). 'all' (tất cả) đi cùng danh từ số nhiều là lựa chọn chính xác về ngữ pháp và ngữ nghĩa."
    },
    128: {
        "questionText": "Members of the finance department ------- to Mr. Chua's lecture on risk avoidance.",
        "questionTextVi": "Các thành viên của bộ phận tài chính ------- tham dự bài giảng của ông Chua về phòng ngừa rủi ro.",
        "options": {
            "A": "to be invited",
            "B": "inviting",
            "C": "invite",
            "D": "are invited"
        },
        "optionsVi": {
            "A": "(A) để được mời (to-V)",
            "B": "(B) đang mời (V-ing)",
            "C": "(C) mời (chủ động)",
            "D": "(D) được mời (bị động thì hiện tại đơn)"
        },
        "correctAnswer": "D",
        "explanation": "Câu có chủ ngữ 'Members of the finance department' đang thiếu động từ chính được chia thì (finite verb). Các thành viên được mời đến nghe bài giảng (nghĩa bị động: be invited to). Do đó dùng thể bị động 'are invited' (D)."
    },
    133: {
        "questionText": "Select the best answer for blank [133]:",
        "questionTextVi": "Chọn câu thích hợp nhất để điền vào chỗ trống [133]:",
        "options": {
            "A": "Its grand opening is scheduled for mid-November.",
            "B": "Most applicants had prior experience.",
            "C": "Its appointment of Linda Okumu as its CEO has surprised analysts.",
            "D": "Local competitors cannot match its prices."
        },
        "optionsVi": {
            "A": "(A) Lễ khai trương của nó dự kiến diễn ra vào giữa tháng 11.",
            "B": "(B) Hầu hết người nộp đơn đều đã có kinh nghiệm từ trước.",
            "C": "(C) Việc bổ nhiệm Linda Okumu làm CEO đã gây ngạc nhiên cho giới phân tích.",
            "D": "(D) Các đối thủ cạnh tranh địa phương không thể sánh được với mức giá của nó."
        },
        "correctAnswer": "A",
        "explanation": "Chỗ trống [133] đứng sau thông tin về cơ sở mới Westside đang được xây dựng: '...Ohale is seeking employees for its new Westside location, which is still under construction. [133]'. Câu (A) thông báo thời điểm khai trương chi nhánh này kết nối mạch văn hợp lý nhất."
    },
    134: {
        "questionText": "Select the best answer for blank [134]:",
        "questionTextVi": "Chọn đáp án thích hợp nhất cho chỗ trống [134]:",
        "options": {
            "A": "attending",
            "B": "to attend",
            "C": "attended",
            "D": "are attending"
        },
        "optionsVi": {
            "A": "(A) tham dự (V-ing)",
            "B": "(B) để tham dự (to-V)",
            "C": "(C) đã tham dự (quá khứ)",
            "D": "(D) đang / sẽ tham dự (hiện tại tiếp diễn)"
        },
        "correctAnswer": "D",
        "explanation": "Mệnh đề quan hệ: 'Those who [134] the event should bring copies of their résumé...'. Đại từ quan hệ 'who' thay thế cho đại từ số nhiều 'Those' làm chủ ngữ của mệnh đề, cần động từ chia thì đầy đủ. Dùng 'are attending' (thì tiếp diễn diễn tả sự tham dự sắp xếp trong tương lai) là đúng chuẩn ngữ pháp."
    },
    136: {
        "options": {
            "A": "Our filtration system will be redesigned within the next year.",
            "B": "Water use may be reduced by running your dishwasher less frequently.",
            "C": "To do this, run cool tap water through the filter for three minutes.",
            "D": "There are 150 liters of water in the main storage tank at all times."
        },
        "optionsVi": {
            "A": "(A) Hệ thống lọc của chúng tôi sẽ được thiết kế lại trong năm tới.",
            "B": "(B) Lượng nước sử dụng có thể giảm bằng cách ít bật máy rửa bát hơn.",
            "C": "(C) Để làm việc này, hãy cho nước máy lạnh chảy qua lõi lọc trong 3 phút.",
            "D": "(D) Luôn luôn có 150 lít nước trong bình chứa chính ở mọi thời điểm."
        }
    },
    155: {
        "questionText": "What is suggested about Jones-Richmond Construction?",
        "questionTextVi": "Điều gì được gợi ý về công ty xây dựng Jones-Richmond Construction?",
        "options": {
            "A": "It is a new company.",
            "B": "It has won industry awards for its work.",
            "C": "It is based in Winnipeg.",
            "D": "It specializes in home construction projects."
        },
        "optionsVi": {
            "A": "(A) Đó là một công ty mới thành lập.",
            "B": "(B) Nó đã giành được nhiều giải thưởng trong ngành nhờ các công trình của mình.",
            "C": "(C) Trụ sở chính của nó đặt tại Winnipeg.",
            "D": "(D) Nó chuyên về các dự án xây dựng nhà ở dân dụng."
        },
        "correctAnswer": "C",
        "explanation": "Thông tin bài tuyển dụng: '...JRC is a full-service general contractor serving clients throughout Winnipeg and the surrounding area.' Trụ sở hoạt động của JRC đặt tại Winnipeg (C)."
    },
    156: {
        "questionText": "What is NOT listed as a responsibility of the construction superintendent?",
        "questionTextVi": "Điều nào KHÔNG được liệt kê là trách nhiệm của giám sát công trình?",
        "options": {
            "A": "Setting schedules",
            "B": "Training inexperienced workers",
            "C": "Participating in contract discussions",
            "D": "Ensuring worker safety"
        },
        "optionsVi": {
            "A": "(A) Thiết lập lịch trình thi công",
            "B": "(B) Đào tạo những công nhân chưa có kinh nghiệm",
            "C": "(C) Tham gia vào các cuộc thảo luận đàm phán hợp đồng",
            "D": "(D) Đảm bảo an toàn cho người lao động"
        },
        "correctAnswer": "B",
        "explanation": "Danh sách trách nhiệm gồm: Manage on-site construction, Ensure compliance with safety regulations (D), Negotiate purchases and contracts (C), Establish construction schedules (A). Việc đào tạo công nhân mới (B) không hề được nhắc tới."
    },
    158: {
        "questionText": "What is mentioned as a benefit of the new payment system?",
        "questionTextVi": "Lợi ích nào được đề cập về hệ thống thanh toán lương mới?",
        "options": {
            "A": "It will reduce Mr. Sledge's workload.",
            "B": "It will include more staff involvement.",
            "C": "It will simplify tax collection.",
            "D": "It will result in fewer payment errors."
        },
        "optionsVi": {
            "A": "(A) Nó sẽ giảm bớt gánh nặng khối lượng công việc cho ông Sledge.",
            "B": "(B) Nó sẽ bao gồm nhiều sự tham gia hơn của đội ngũ nhân viên.",
            "C": "(C) Nó sẽ đơn giản hóa việc thu thuế.",
            "D": "(D) Nó sẽ dẫn đến ít lỗi thanh toán hơn."
        },
        "correctAnswer": "A",
        "explanation": "Ông Sledge chia sẻ: 'Although this growth is wonderful, having to process the payroll by myself has become rather burdensome. Therefore, I have contracted Trumbull and Company...' Thuê bên ngoài chi trả lương giúp giảm gánh nặng xử lý công việc cho ông (A)."
    },
    159: {
        "questionText": "What does Mr. Sledge ask employees to do?",
        "questionTextVi": "Ông Sledge yêu cầu nhân viên làm điều gì?",
        "options": {
            "A": "Update their contact information",
            "B": "Submit ideas on how to improve the gym",
            "C": "Provide information about their bank accounts",
            "D": "Sign up for a professional development class"
        },
        "optionsVi": {
            "A": "(A) Cập nhật thông tin liên hệ của họ",
            "B": "(B) Đóng góp ý tưởng về cách cải thiện phòng tập",
            "C": "(C) Cung cấp thông tin tài khoản ngân hàng của họ",
            "D": "(D) Đăng ký tham gia một lớp học phát triển chuyên môn"
        },
        "correctAnswer": "C",
        "explanation": "Sledge viết: 'To allow for these changes, I am asking everyone to provide me with the necessary banking details.' (Cung cấp thông tin chi tiết về tài khoản ngân hàng để chuyển lương trực tiếp - C)."
    },
    181: {
        "questionText": "Why does Pirate's Bounty Seafood need to purchase new equipment?",
        "questionTextVi": "Tại sao quán hải sản Pirate's Bounty Seafood cần mua thiết bị mới?",
        "options": {
            "A": "Its current refrigerator stopped working.",
            "B": "The warranty on its current refrigerator has expired.",
            "C": "The restaurant is increasing in size.",
            "D": "The restaurant is moving to a new location."
        },
        "optionsVi": {
            "A": "(A) Tủ lạnh hiện tại của quán đã ngừng hoạt động.",
            "B": "(B) Bảo hành của tủ lạnh hiện tại đã hết hạn.",
            "C": "(C) Nhà hàng đang mở rộng quy mô diện tích.",
            "D": "(D) Nhà hàng đang chuyển đến một địa điểm mới."
        },
        "correctAnswer": "C",
        "explanation": "Trong đơn đặt hàng (Purchase Order), phần ghi chú (COMMENTS OR SPECIAL INSTRUCTIONS) ghi rõ: 'Restaurant expanding. Need unit by 17 November.' Nhà hàng đang mở rộng quy mô (C)."
    },
    182: {
        "questionText": "What is the problem with the item Ms. Okiya ordered?",
        "questionTextVi": "Có vấn đề gì với món hàng mà bà Okiya đã đặt?",
        "options": {
            "A": "It was lost during shipping.",
            "B": "It has been discontinued.",
            "C": "It is temporarily out of stock.",
            "D": "It has a damaged control panel."
        },
        "optionsVi": {
            "A": "(A) Nó đã bị thất lạc trong quá trình vận chuyển.",
            "B": "(B) Nó đã bị ngừng sản xuất.",
            "C": "(C) Nó hiện đang tạm thời hết hàng.",
            "D": "(D) Nó có bảng điều khiển bị hư hỏng."
        },
        "correctAnswer": "C",
        "explanation": "Trong email phản hồi: 'Unfortunately, the model you requested is on back order and will not be available for three months.' 'on back order' tức là hàng đang tạm thời hết kho phải chờ nhập (temporarily out of stock - C)."
    },
    183: {
        "questionText": "What is NOT a feature of the Blizzard BF600?",
        "questionTextVi": "Đặc điểm nào KHÔNG PHẢI là tính năng của mẫu Blizzard BF600?",
        "options": {
            "A": "It has a fast-freeze switch.",
            "B": "It has adjustable shelves.",
            "C": "It has aluminum flooring.",
            "D": "It has galvanized steel panels."
        },
        "optionsVi": {
            "A": "(A) Nó có công tắc cấp đông nhanh.",
            "B": "(B) Nó có các kệ có thể điều chỉnh độ cao.",
            "C": "(C) Nó có sàn bằng nhôm.",
            "D": "(D) Nó có các tấm ốp bằng thép mạ kẽm."
        },
        "correctAnswer": "A",
        "explanation": "Email nói mẫu BF600 'comes with the same features as the item you ordered (BF550)'. Các đặc điểm của BF550 trên đơn hàng gồm: 'adjustable shelves, aluminum flooring, galvanized steel panels'. Không hề có 'fast-freeze switch' (A)."
    },
    184: {
        "questionText": "According to the e-mail, what does the BF400 model come with?",
        "questionTextVi": "Theo email, mẫu tủ đông BF400 đi kèm với thứ gì?",
        "options": {
            "A": "A user manual",
            "B": "A remote control",
            "C": "A warranty",
            "D": "A tax waiver"
        },
        "optionsVi": {
            "A": "(A) Sách hướng dẫn sử dụng",
            "B": "(B) Điều khiển từ xa",
            "C": "(C) Giấy chứng nhận bảo hành",
            "D": "(D) Miễn trừ thuế"
        },
        "correctAnswer": "C",
        "explanation": "Email mô tả về mẫu BF400: 'The unit comes with a two-year warranty.' Đi kèm gói bảo hành 2 năm (A warranty - C)."
    },
    185: {
        "questionText": "In the e-mail, the word \"Just\" in paragraph 3, line 1, is closest in meaning to",
        "questionTextVi": "Trong email, từ \"Just\" ở đoạn 3, dòng 1 có nghĩa gần nhất với từ nào?",
        "options": {
            "A": "immediately",
            "B": "kindly",
            "C": "shortly",
            "D": "simply"
        },
        "optionsVi": {
            "A": "(A) ngay lập tức",
            "B": "(B) vui lòng, tử tế",
            "C": "(C) trong thời gian ngắn",
            "D": "(D) chỉ cần, đơn giản là"
        },
        "correctAnswer": "D",
        "explanation": "Câu kết của email: 'Just reply to this e-mail.' (Chỉ việc/đơn giản là trả lời lại email này). 'Just' ở đây mang nghĩa là 'simply' (chỉ cần, đơn giản) (D)."
    },
    189: {
        "questionText": "What is suggested about Mr. Kalwar?",
        "questionTextVi": "Điều gì được gợi ý về ông Kalwar?",
        "options": {
            "A": "He is a videographer.",
            "B": "He works in Germany.",
            "C": "He is planning to buy a house in Sheffield.",
            "D": "He specializes in construction materials."
        },
        "optionsVi": {
            "A": "(A) Ông ấy là một nhà quay phim.",
            "B": "(B) Ông ấy làm việc tại Đức.",
            "C": "(C) Ông ấy có kế hoạch mua một căn nhà ở Sheffield.",
            "D": "(D) Ông ấy chuyên về vật liệu xây dựng."
        },
        "correctAnswer": "B",
        "explanation": "Email từ Olek Dzik gửi cho Nadir Kalwar nói: '...our next construction project will be a home just a couple of kilometres from your office building!'. Bài báo cho biết dự án tiếp theo của công ty là 'the construction of a home in Hamburg, Germany'. Kết hợp hai chi tiết này suy ra văn phòng của ông Kalwar ở Đức (B)."
    },
    190: {
        "questionText": "What does the article indicate about the house created with a 3-D printer?",
        "questionTextVi": "Bài báo chỉ ra điều gì về ngôi nhà được xây dựng bằng máy in 3D?",
        "options": {
            "A": "It cost €150,000 to build.",
            "B": "It was finished in two months.",
            "C": "It will be landscaped next week.",
            "D": "Its bedrooms are all the same size."
        },
        "optionsVi": {
            "A": "(A) Nó tốn 150.000 euro chi phí xây dựng.",
            "B": "(B) Nó đã được hoàn thành trong vòng hai tháng.",
            "C": "(C) Nó sẽ được tạo cảnh quan vào tuần tới.",
            "D": "(D) Các phòng ngủ của nó đều có diện tích bằng nhau."
        },
        "correctAnswer": "B",
        "explanation": "Bài báo nêu rõ: 'In just two months, the fully landscaped house with two bedrooms and two bathrooms was ready for market.' Ngôi nhà được hoàn thiện chỉ trong 2 tháng (B)."
    },
    194: {
        "questionText": "What is suggested about Geetu Gelang?",
        "questionTextVi": "Điều gì được gợi ý về Geetu Gelang?",
        "options": {
            "A": "She is a local musician.",
            "B": "She will be selling her crafts on May 1.",
            "C": "She plans to start a social media account.",
            "D": "She was recently hired by the Richard Lahiri Gallery."
        },
        "optionsVi": {
            "A": "(A) Cô ấy là một nhạc sĩ địa phương.",
            "B": "(B) Cô ấy sẽ bán các sản phẩm thủ công của mình vào ngày 1 tháng 5.",
            "C": "(C) Cô ấy có kế hoạch mở tài khoản mạng xã hội.",
            "D": "(D) Cô ấy gần đây đã được phòng trưng bày Richard Lahiri Gallery tuyển dụng."
        },
        "correctAnswer": "D",
        "explanation": "Bài viết tuyển dụng đăng vị trí Gallery Manager với yêu cầu nhận việc trước ngày 1 tháng 4. Bài báo sự kiện vào tháng 5 giới thiệu: 'Richard Lahiri and his gallery manager, Geetu Gelang...'. Suy ra cô Geetu Gelang chính là người mới được tuyển dụng cho vị trí này (D)."
    },
    195: {
        "questionText": "According to the article, where is Brady Park located?",
        "questionTextVi": "Theo bài báo, công viên Brady Park nằm ở đâu?",
        "options": {
            "A": "In Cromwood",
            "B": "In Elmhurst",
            "C": "In Herrontown",
            "D": "In Melbridge"
        },
        "optionsVi": {
            "A": "(A) Ở Cromwood",
            "B": "(B) Ở Elmhurst",
            "C": "(C) Ở Herrontown",
            "D": "(D) Ở Melbridge"
        },
        "correctAnswer": "C",
        "explanation": "Mục 'Movies in Brady Park' trong bài báo ghi rõ: 'The popular summer movie series in Herrontown returns on June 16! Each Saturday evening, a classic film will be projected on Brady Park's Grand Lawn.' Công viên nằm ở Herrontown (C)."
    }
}

# Apply to Test 4
with open('web/data/test4.json', encoding='utf-8') as f:
    t4 = json.load(f)

for q in t4['questions']:
    qid = q['id']
    if qid in t4_fixes:
        fix = t4_fixes[qid]
        for k, v in fix.items():
            q[k] = v

with open('web/data/test4.json', 'w', encoding='utf-8') as f:
    json.dump(t4, f, ensure_ascii=False, indent=2)

print(f"Applied {len(t4_fixes)} comprehensive fixes to test4.json!")

# Apply to Test 5
with open('web/data/test5.json', encoding='utf-8') as f:
    t5 = json.load(f)

for q in t5['questions']:
    qid = q['id']
    if qid in t5_fixes:
        fix = t5_fixes[qid]
        for k, v in fix.items():
            q[k] = v

with open('web/data/test5.json', 'w', encoding='utf-8') as f:
    json.dump(t5, f, ensure_ascii=False, indent=2)

print(f"Applied {len(t5_fixes)} comprehensive fixes to test5.json!")
