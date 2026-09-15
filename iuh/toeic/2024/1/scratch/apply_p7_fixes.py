# scratch/apply_p7_fixes.py
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

t4_fixes = {
    147: {
        "questionText": "What was purchased on May 23 ?",
        "questionTextVi": "Mặt hàng nào đã được mua vào ngày 23 tháng 5?",
        "options": {"A": "Fuel", "B": "Snacks", "C": "Auto parts", "D": "Phone accessories"},
        "optionsVi": {"A": "(A) Nhiên liệu / xăng dầu", "B": "(B) Đồ ăn nhẹ / đồ ăn vặt", "C": "(C) Phụ tùng ô tô", "D": "(D) Phụ kiện điện thoại"}
    },
    148: {
        "questionText": "What does the receipt indicate about Zippy Petrol Mart?",
        "questionTextVi": "Hóa đơn cho biết điều gì về trạm Zippy Petrol Mart?",
        "options": {
            "A": "It has multiple locations.",
            "B": "It accepts most major credit cards.",
            "C": "It has a customer rewards program.",
            "D": "It reduced the prices of all its merchandise."
        },
        "optionsVi": {
            "A": "(A) Nó có nhiều địa điểm chi nhánh.",
            "B": "(B) Nó chấp nhận hầu hết các loại thẻ tín dụng lớn.",
            "C": "(C) Nó có chương trình tích điểm thưởng cho khách hàng.",
            "D": "(D) Nó đã giảm giá tất cả các mặt hàng."
        }
    },
    155: {
        "questionText": "What is the purpose of the letter?",
        "questionTextVi": "Mục đích của lá thư là gì?",
        "options": {
            "A": "To announce a special event",
            "B": "To explain changes based on a relocation",
            "C": "To propose a new meeting time",
            "D": "To request updated contact information"
        },
        "optionsVi": {
            "A": "(A) Để công bố một sự kiện đặc biệt",
            "B": "(B) Để giải thích những thay đổi do việc chuyển nơi cư trú",
            "C": "(C) Để đề xuất thời gian họp mới",
            "D": "(D) Để yêu cầu cập nhật thông tin liên lạc"
        }
    },
    156: {
        "questionText": "What is suggested about the city of Canberra?",
        "questionTextVi": "Điều gì được gợi ý về thành phố Canberra?",
        "options": {
            "A": "It is famous for its many gardens.",
            "B": "It houses the headquarters of Ms. Davis' organization.",
            "C": "It is where Ms. Harabi previously lived.",
            "D": "It is home to some of Australia's rarest plants."
        },
        "optionsVi": {
            "A": "(A) Nơi đây nổi tiếng với nhiều khu vườn.",
            "B": "(B) Đây là nơi đặt trụ sở tổ chức của bà Davis.",
            "C": "(C) Đó là nơi bà Harabi từng sinh sống trước đây.",
            "D": "(D) Đây là môi trường sống của một số loài thực vật quý hiếm nhất nước Úc."
        }
    },
    157: {
        "questionText": "What can be concluded about the Native Plant Society?",
        "questionTextVi": "Có thể kết luận điều gì về Hội Thực vật Bản địa?",
        "options": {
            "A": "It is under new leadership.",
            "B": "Its membership is growing.",
            "C": "It is raising membership dues.",
            "D": "Its chapters hold monthly meetings."
        },
        "optionsVi": {
            "A": "(A) Hội đang dưới sự lãnh đạo mới.",
            "B": "(B) Số lượng hội viên đang tăng lên.",
            "C": "(C) Hội đang tăng mức hội phí.",
            "D": "(D) Các chi hội của hội tổ chức các cuộc họp hằng tháng."
        }
    },
    158: {
        "questionText": "According to the Web page, what can visitors to the Web site do?",
        "questionTextVi": "Theo trang web, khách truy cập có thể làm gì trên trang web này?",
        "options": {
            "A": "Discuss how to create a garden",
            "B": "Learn how to maximize vegetable production",
            "C": "Seek advice about landscaping problems",
            "D": "Help contractors calculate costs"
        },
        "optionsVi": {
            "A": "(A) Thảo luận về cách tạo một khu vườn",
            "B": "(B) Học cách tối đa hóa sản lượng rau",
            "C": "(C) Tìm kiếm lời khuyên về các vấn đề cảnh quan",
            "D": "(D) Giúp các nhà thầu tính toán chi phí"
        }
    },
    159: {
        "questionText": "What is NOT mentioned about green roofs?",
        "questionTextVi": "Điều gì KHÔNG được nhắc đến về mái nhà xanh?",
        "options": {
            "A": "They decrease energy bills.",
            "B": "They remove pollution from the air.",
            "C": "They make a structure more beautiful.",
            "D": "They can be installed on commercial and residential buildings."
        },
        "optionsVi": {
            "A": "(A) Chúng làm giảm hóa đơn tiền năng lượng.",
            "B": "(B) Chúng loại bỏ ô nhiễm khỏi không khí.",
            "C": "(C) Chúng làm cho công trình trở nên đẹp hơn.",
            "D": "(D) Chúng có thể được lắp đặt trên cả tòa nhà thương mại và nhà ở."
        }
    },
    160: {
        "questionText": "In paragraph 3, line 1, the word 'handle' is closest in meaning to",
        "questionTextVi": "Trong đoạn 3, dòng 1, từ 'handle' gần nghĩa nhất với từ nào?",
        "options": {"A": "touch", "B": "control", "C": "deliver", "D": "support"},
        "optionsVi": {"A": "(A) chạm vào", "B": "(B) kiểm soát", "C": "(C) giao hàng", "D": "(D) chịu đựng, nâng đỡ (tải trọng)"}
    },
    164: {
        "questionText": "What is the main purpose of the e-mail?",
        "questionTextVi": "Mục đích chính của email là gì?",
        "options": {
            "A": "To ask staff to sign up to give speeches at a celebration",
            "B": "To find people willing to bring various items to a dinner",
            "C": "To invite workers to a surprise party",
            "D": "To look for volunteers to help plan an event"
        },
        "optionsVi": {
            "A": "(A) Yêu cầu nhân viên đăng ký phát biểu tại lễ kỷ niệm",
            "B": "(B) Tìm người sẵn sàng mang các món đồ tới bữa tối",
            "C": "(C) Mời nhân viên tới tham dự một bữa tiệc bất ngờ",
            "D": "(D) Tìm tình nguyện viên giúp lên kế hoạch sự kiện"
        }
    },
    165: {
        "questionText": "According to the e-mail, when are most people expected to arrive?",
        "questionTextVi": "Theo email, hầu hết mọi người dự kiến sẽ đến vào lúc mấy giờ?",
        "options": {"A": "At 5:00 P.M.", "B": "At 6:15 P.M.", "C": "At 6:30 P.M.", "D": "At 8:00 P.M."},
        "optionsVi": {"A": "(A) Lúc 5:00 chiều", "B": "(B) Lúc 6:15 chiều", "C": "(C) Lúc 6:30 chiều", "D": "(D) Lúc 8:00 tối"}
    },
    166: {
        "questionText": "What should people do if they want to sign a card?",
        "questionTextVi": "Mọi người nên làm gì nếu muốn ký vào tấm thiệp mừng?",
        "options": {
            "A": "They should request it from Mr. Bonahoom.",
            "B": "They should e-mail Ms. Noh.",
            "C": "They should wait for it to be passed around the office.",
            "D": "They should go to Ms. Mueller's desk."
        },
        "optionsVi": {
            "A": "(A) Họ nên yêu cầu từ ông Bonahoom.",
            "B": "(B) Họ nên gửi email cho bà Noh.",
            "C": "(C) Họ nên chờ thiệp được chuyển quanh văn phòng.",
            "D": "(D) Họ nên đến bàn làm việc của cô Mueller."
        }
    },
    167: {
        "questionText": "In which of the positions marked [1], [2], [3], and [4] does the following sentence best belong? 'The senior staff will be presenting a commemorative plaque on behalf of the whole office.'",
        "questionTextVi": "Câu sau đây phù hợp nhất ở vị trí nào được đánh dấu [1], [2], [3] và [4]? 'Đội ngũ nhân viên kỳ cựu sẽ thay mặt toàn thể văn phòng trao tặng kỷ niệm chương.'",
        "options": {"A": "[1]", "B": "[2]", "C": "[3]", "D": "[4]"},
        "optionsVi": {"A": "(A) Vị trí [1]", "B": "(B) Vị trí [2]", "C": "(C) Vị trí [3]", "D": "(D) Vị trí [4]"}
    },
    168: {
        "questionText": "What type of company do the writers most likely work for?",
        "questionTextVi": "Những người viết nhiều khả năng làm việc cho loại công ty nào?",
        "options": {"A": "Publishing", "B": "Accounting", "C": "Retail", "D": "Design"},
        "optionsVi": {"A": "(A) Xuất bản", "B": "(B) Kế toán", "C": "(C) Bán lẻ", "D": "(D) Thiết kế"}
    },
    169: {
        "questionText": "What does Mr. Wikander suggest about a question?",
        "questionTextVi": "Ông Wikander gợi ý điều gì về một câu hỏi?",
        "options": {
            "A": "It is mislabeled.",
            "B": "It is difficult to read.",
            "C": "It should be reworded.",
            "D": "It should be made optional."
        },
        "optionsVi": {
            "A": "(A) Nó bị dán nhãn sai.",
            "B": "(B) Nó khó đọc.",
            "C": "(C) Nó nên được diễn đạt lại bằng từ ngữ khác.",
            "D": "(D) Nó nên được chuyển thành câu hỏi tùy chọn."
        }
    },
    170: {
        "questionText": "At 10:25 A.M., what does Mr. Wikander most likely mean when he writes, 'Well, it's four pages already'?",
        "questionTextVi": "Vào lúc 10:25 sáng, ông Wikander có ý gì nhất khi viết 'À, nó đã dài bốn trang rồi đấy'?",
        "options": {
            "A": "He is surprised by the long answers clients gave.",
            "B": "He is impressed with how quickly the questionnaire is coming along.",
            "C": "He thinks information in the first four pages should be cut out.",
            "D": "He thinks the questionnaire should not be any longer."
        },
        "optionsVi": {
            "A": "(A) Ông ngạc nhiên trước câu trả lời dài của khách hàng.",
            "B": "(B) Ông ấn tượng với tiến độ hoàn thành bảng hỏi.",
            "C": "(C) Ông nghĩ nên cắt giảm thông tin trong bốn trang đầu.",
            "D": "(D) Ông nghĩ rằng bảng câu hỏi không nên dài thêm nữa."
        }
    },
    171: {
        "questionText": "Why does Ms. Sakai think that paperless forms will be preferable?",
        "questionTextVi": "Tại sao cô Sakai lại nghĩ biểu mẫu điện tử không dùng giấy sẽ tốt hơn?",
        "options": {
            "A": "They allow for faster data collection.",
            "B": "They reduce the number of errors.",
            "C": "They are good for the environment.",
            "D": "They do not take up space in an office."
        },
        "optionsVi": {
            "A": "(A) Chúng cho phép thu thập dữ liệu nhanh chóng hơn.",
            "B": "(B) Chúng làm giảm số lượng lỗi sai.",
            "C": "(C) Chúng tốt cho môi trường sinh thái.",
            "D": "(D) Chúng không chiếm diện tích trong văn phòng."
        }
    },
    172: {
        "questionText": "Why did Mr. Karikas write the post?",
        "questionTextVi": "Tại sao ông Karikas lại viết bài đăng này?",
        "options": {
            "A": "To promote a job fair",
            "B": "To request referrals to a service provider",
            "C": "To recommend a tourist destination",
            "D": "To invite colleagues to a grand opening"
        },
        "optionsVi": {
            "A": "(A) Để quảng bá một hội chợ việc làm",
            "B": "(B) Để xin giới thiệu về một nhà cung cấp dịch vụ",
            "C": "(C) Để giới thiệu một địa điểm du lịch",
            "D": "(D) Để mời đồng nghiệp tới dự lễ khai trương"
        }
    },
    173: {
        "questionText": "What is suggested about the TRE Hospitality Association?",
        "questionTextVi": "Điều gì được gợi ý về Hiệp hội Khách sạn TRE?",
        "options": {
            "A": "It is based in Egypt.",
            "B": "It was recently expanded to include hotel owners.",
            "C": "It is an international organization.",
            "D": "It offers janitorial services."
        },
        "optionsVi": {
            "A": "(A) Nó có trụ sở tại Ai Cập.",
            "B": "(B) Nó vừa được mở rộng để bao gồm các chủ khách sạn.",
            "C": "(C) Đây là một tổ chức quốc tế.",
            "D": "(D) Nó cung cấp dịch vụ dọn dẹp vệ sinh."
        }
    },
    174: {
        "questionText": "What is indicated about Mr. Karikas?",
        "questionTextVi": "Điều gì được chỉ ra về ông Karikas?",
        "options": {
            "A": "He teaches a hospitality course.",
            "B": "He lives in Rabat.",
            "C": "He is a former restaurant owner.",
            "D": "He attended at least one hospitality conference."
        },
        "optionsVi": {
            "A": "(A) Ông giảng dạy một khóa học về quản trị khách sạn.",
            "B": "(B) Ông sống ở Rabat.",
            "C": "(C) Ông là cựu chủ nhà hàng.",
            "D": "(D) Ông đã tham dự ít nhất một hội nghị ngành khách sạn."
        }
    },
    175: {
        "questionText": "In which of the positions marked [1], [2], [3], and [4] does the following sentence best belong? 'It will also have a large meeting room.'",
        "questionTextVi": "Câu sau đây phù hợp nhất ở vị trí nào được đánh dấu [1], [2], [3] và [4]? 'Khách sạn cũng sẽ có một phòng họp lớn.'",
        "options": {"A": "[1]", "B": "[2]", "C": "[3]", "D": "[4]"},
        "optionsVi": {"A": "(A) Vị trí [1]", "B": "(B) Vị trí [2]", "C": "(C) Vị trí [3]", "D": "(D) Vị trí [4]"}
    },
    179: {
        "questionText": "How does Mr. Torres intend to make future payments?",
        "questionTextVi": "Ông Torres dự định thực hiện các khoản thanh toán trong tương lai bằng cách nào?",
        "options": {"A": "By cash", "B": "By credit card", "C": "By electronic transfer", "D": "By personal check"},
        "optionsVi": {"A": "(A) Bằng tiền mặt", "B": "(B) Bằng thẻ tín dụng", "C": "(C) Bằng chuyển khoản điện tử", "D": "(D) Bằng séc cá nhân"}
    },
    180: {
        "questionText": "What does Mr. Torres state that he looked for?",
        "questionTextVi": "Ông Torres nêu rõ rằng ông đã tìm kiếm thứ gì?",
        "options": {
            "A": "Directions to an office",
            "B": "A document to download",
            "C": "Reviews from customers",
            "D": "Contact information"
        },
        "optionsVi": {
            "A": "(A) Chỉ đường tới văn phòng",
            "B": "(B) Một tài liệu để tải về",
            "C": "(C) Đánh giá từ khách hàng",
            "D": "(D) Thông tin liên hệ"
        }
    },
    181: {
        "questionText": "According to the schedule, what is NOT mentioned as an activity for Mr. Darr?",
        "questionTextVi": "Theo lịch trình, điều gì KHÔNG được đề cập như một hoạt động dành cho ông Darr?",
        "options": {
            "A": "Reading from his book",
            "B": "Answering questions",
            "C": "Signing books for individuals",
            "D": "Taking photos with participants"
        },
        "optionsVi": {
            "A": "(A) Đọc trích đoạn từ cuốn sách của mình",
            "B": "(B) Trả lời các câu hỏi",
            "C": "(C) Ký tặng sách cho từng người",
            "D": "(D) Chụp ảnh lưu niệm với người tham dự"
        }
    },
    182: {
        "questionText": "What city is the book reviewer from?",
        "questionTextVi": "Người đánh giá sách đến từ thành phố nào?",
        "options": {"A": "Toronto", "B": "Ottawa", "C": "Winnipeg", "D": "Regina"},
        "optionsVi": {"A": "(A) Toronto", "B": "(B) Ottawa", "C": "(C) Winnipeg", "D": "(D) Regina"}
    },
    183: {
        "questionText": "What is most likely true about Down the Mountainside ?",
        "questionTextVi": "Điều gì nhiều khả năng là đúng nhất về tác phẩm 'Down the Mountainside'?",
        "options": {
            "A": "It is the author's first book.",
            "B": "It is a collection of short stories.",
            "C": "It is part of a series.",
            "D": "It is being translated into French."
        },
        "optionsVi": {
            "A": "(A) Đây là cuốn sách đầu tay của tác giả.",
            "B": "(B) Đây là một tuyển tập truyện ngắn.",
            "C": "(C) Nó là một phần của một bộ truyện dài kỳ.",
            "D": "(D) Nó đang được dịch sang tiếng Pháp."
        }
    },
    184: {
        "questionText": "Who is Mr. Martin?",
        "questionTextVi": "Ông Martin là ai?",
        "options": {
            "A": "A fan of the author's",
            "B": "A character in the book",
            "C": "The writer of the review",
            "D": "The owner of a bookstore"
        },
        "optionsVi": {
            "A": "(A) Một người hâm mộ của tác giả",
            "B": "(B) Một nhân vật trong cuốn sách",
            "C": "(C) Người viết bài đánh giá sách",
            "D": "(D) Chủ của một hiệu sách"
        }
    },
    185: {
        "questionText": "According to the review, who would most likely read Down the Mountainside ?",
        "questionTextVi": "Theo bài đánh giá, ai sẽ là người thích đọc cuốn 'Down the Mountainside' nhất?",
        "options": {
            "A": "People who like to read mysteries",
            "B": "People who enjoy novels based on true stories",
            "C": "People who travel frequently",
            "D": "People who prefer science fiction"
        },
        "optionsVi": {
            "A": "(A) Những người thích đọc truyện trinh thám ly kỳ",
            "B": "(B) Những người thích tiểu thuyết dựa trên những câu chuyện có thật",
            "C": "(C) Những người thường xuyên đi du lịch",
            "D": "(D) Những người chuộng thể loại khoa học viễn tưởng"
        }
    },
    196: {
        "questionText": "How does Modern Salon Academy teach its students?",
        "questionTextVi": "Học viện Modern Salon đào tạo học viên của mình như thế nào?",
        "options": {
            "A": "Through online courses",
            "B": "Through academic lectures",
            "C": "Through individualized training",
            "D": "Through large-group discussions"
        },
        "optionsVi": {
            "A": "(A) Thông qua các khóa học trực tuyến",
            "B": "(B) Thông qua các bài giảng lý thuyết",
            "C": "(C) Thông qua hình thức kèm cặp/đào tạo từng cá nhân",
            "D": "(D) Thông qua thảo luận nhóm lớn"
        }
    },
    197: {
        "questionText": "According to the article, what has increased at Modern Salon Academy?",
        "questionTextVi": "Theo bài báo, điều gì đã gia tăng tại Học viện Modern Salon?",
        "options": {
            "A": "The cost of tuition",
            "B": "The number of students",
            "C": "The requirements for admission",
            "D": "The hours needed for certification"
        },
        "optionsVi": {
            "A": "(A) Chi phí học phí",
            "B": "(B) Số lượng học viên theo học",
            "C": "(C) Tiêu chuẩn yêu cầu đầu vào",
            "D": "(D) Số giờ cần thiết để được cấp chứng chỉ"
        }
    },
    198: {
        "questionText": "What is most likely true about Shoreline Barbers?",
        "questionTextVi": "Điều gì nhiều khả năng là đúng nhất về tiệm cắt tóc Shoreline Barbers?",
        "options": {
            "A": "It is located in Oshawa.",
            "B": "It is opening a shop in Toronto.",
            "C": "It was sold to Francine Dupuis.",
            "D": "It has very affordable services."
        },
        "optionsVi": {
            "A": "(A) Nó tọa lạc tại thành phố Oshawa.",
            "B": "(B) Nó đang mở một chi nhánh tại Toronto.",
            "C": "(C) Nó đã được bán cho bà Francine Dupuis.",
            "D": "(D) Nó có các dịch vụ với giá cả rất bình dân."
        }
    },
    199: {
        "questionText": "Who would best meet Mr. Persaud's needs?",
        "questionTextVi": "Nhóm học viên nào sẽ đáp ứng tốt nhất nhu cầu của ông Persaud?",
        "options": {
            "A": "Students in Cosmetology I",
            "B": "Students in Cosmetology II",
            "C": "Students in Skin Care",
            "D": "Students in Leadership"
        },
        "optionsVi": {
            "A": "(A) Học viên lớp Thẩm mỹ I (Cosmetology I)",
            "B": "(B) Học viên lớp Thẩm mỹ II (Cosmetology II)",
            "C": "(C) Học viên lớp Chăm sóc da (Skin Care)",
            "D": "(D) Học viên lớp Kỹ năng lãnh đạo (Leadership)"
        }
    },
    200: {
        "questionText": "According to the e-mail, what does Mr. Persaud want to do?",
        "questionTextVi": "Theo email, ông Persaud muốn làm điều gì?",
        "options": {
            "A": "Establish another business",
            "B": "Retrain staff members",
            "C": "Teach some classes",
            "D": "Interview some students"
        },
        "optionsVi": {
            "A": "(A) Thành lập một cơ sở kinh doanh khác",
            "B": "(B) Đào tạo lại các nhân viên",
            "C": "(C) Giảng dạy một số lớp học",
            "D": "(D) Phỏng vấn một số học viên"
        }
    }
}

t5_fixes = {
    71: {
        "questionText": "What did the listener do yesterday?",
        "questionTextVi": "Người nghe đã làm gì vào ngày hôm qua?",
        "options": {
            "A": "She placed an order.",
            "B": "She scheduled an event.",
            "C": "She called a manager.",
            "D": "She painted some rooms."
        },
        "optionsVi": {
            "A": "(A) Cô ấy đã đặt một đơn hàng.",
            "B": "(B) Cô ấy đã lên lịch cho một sự kiện.",
            "C": "(C) Cô ấy đã gọi cho một người quản lý.",
            "D": "(D) Cô ấy đã sơn một số căn phòng."
        },
        "correctAnswer": "A"
    },
    161: {
        "questionText": "The word 'top' in paragraph 1, line 3, is closest in meaning to",
        "questionTextVi": "Trong đoạn 1, dòng 3, từ 'top' gần nghĩa nhất với từ nào?",
        "options": {"A": "only", "B": "leading", "C": "highest", "D": "modern"},
        "optionsVi": {"A": "(A) duy nhất", "B": "(B) hàng đầu, dẫn đầu", "C": "(C) cao nhất về độ cao", "D": "(D) hiện đại"}
    },
    162: {
        "questionText": "Who will NOT be conducting informational presentations at the fair?",
        "questionTextVi": "Ai sẽ KHÔNG thực hiện các bài thuyết trình cung cấp thông tin tại hội chợ?",
        "options": {
            "A": "Chefs",
            "B": "Coffee growers",
            "C": "Equipment makers",
            "D": "Coffeehouse owners"
        },
        "optionsVi": {
            "A": "(A) Các đầu bếp",
            "B": "(B) Người trồng cà phê",
            "C": "(C) Nhà sản xuất trang thiết bị",
            "D": "(D) Chủ các quán cà phê"
        }
    },
    164: {
        "questionText": "What is the purpose of the e-mail?",
        "questionTextVi": "Mục đích của email là gì?",
        "options": {
            "A": "To advertise some new pastries",
            "B": "To present options for an event",
            "C": "To recommend serving a larger cake",
            "D": "To request payment on an order"
        },
        "optionsVi": {
            "A": "(A) Để quảng cáo một số loại bánh ngọt mới",
            "B": "(B) Để giới thiệu các lựa chọn cho một sự kiện",
            "C": "(C) Để khuyên nên phục vụ một chiếc bánh lớn hơn",
            "D": "(D) Để yêu cầu thanh toán cho một đơn hàng"
        }
    },
    165: {
        "questionText": "What does Ms. Luhya indicate about the mini cheesecakes?",
        "questionTextVi": "Bà Luhya chỉ ra điều gì về những chiếc bánh phô mai mini?",
        "options": {
            "A": "They are the most expensive dessert.",
            "B": "They are available in several flavors.",
            "C": "They should not be unrefrigerated for a long time.",
            "D": "They cannot be ordered in larger sizes."
        },
        "optionsVi": {
            "A": "(A) Chúng là món tráng miệng đắt nhất.",
            "B": "(B) Chúng có sẵn nhiều hương vị khác nhau.",
            "C": "(C) Chúng không nên để ngoài mà không được làm lạnh quá lâu.",
            "D": "(D) Chúng không thể đặt theo kích cỡ lớn hơn."
        }
    },
    166: {
        "questionText": "The word 'disturbing' in paragraph 2, line 6, is closest in meaning to",
        "questionTextVi": "Trong đoạn 2, dòng 6, từ 'disturbing' gần nghĩa nhất với từ nào?",
        "options": {"A": "interrupting", "B": "frightening", "C": "rearranging", "D": "moving"},
        "optionsVi": {"A": "(A) làm gián đoạn, làm phiền", "B": "(B) gây hoảng sợ", "C": "(C) sắp xếp lại", "D": "(D) di chuyển"}
    },
    167: {
        "questionText": "What information does Ms. Luhya request from Ms. Otero?",
        "questionTextVi": "Bà Luhya yêu cầu thông tin gì từ bà Otero?",
        "options": {
            "A": "A street address",
            "B": "An approximate budget",
            "C": "The name of a caterer",
            "D": "The number of guests"
        },
        "optionsVi": {
            "A": "(A) Địa chỉ đường phố",
            "B": "(B) Ngân sách ước tính",
            "C": "(C) Tên đơn vị phục vụ tiệc",
            "D": "(D) Số lượng khách tham dự"
        }
    },
    168: {
        "questionText": "What is indicated about Candella Interior Design?",
        "questionTextVi": "Điều gì được chỉ ra về công ty Thiết kế Nội thất Candella?",
        "options": {
            "A": "Its main office is located in a major city.",
            "B": "Its staff members visit clients' houses.",
            "C": "It has been in business longer than its competitors have been.",
            "D": "It is a family-run business."
        },
        "optionsVi": {
            "A": "(A) Văn phòng chính của nó tọa lạc tại một thành phố lớn.",
            "B": "(B) Nhân viên của nó đến tận nhà khách hàng.",
            "C": "(C) Nó đã kinh doanh lâu hơn các đối thủ cạnh tranh.",
            "D": "(D) Đây là một doanh nghiệp gia đình."
        }
    },
    169: {
        "questionText": "Why does Ms. Futrel want to redecorate her apartment?",
        "questionTextVi": "Tại sao bà Futrel lại muốn trang trí lại căn hộ của mình?",
        "options": {
            "A": "To prepare for a visit from relatives",
            "B": "To make it attractive to potential buyers",
            "C": "To replace furniture that she dislikes",
            "D": "To use it as an example for her clients"
        },
        "optionsVi": {
            "A": "(A) Để chuẩn bị đón người thân đến chơi",
            "B": "(B) Để làm cho nó hấp dẫn người mua tiềm năng",
            "C": "(C) Để thay thế đồ nội thất mà bà không thích",
            "D": "(D) Để dùng làm ví dụ mẫu cho khách hàng"
        }
    },
    172: {
        "questionText": "What is the purpose of Mr. Wilkins' first text message?",
        "questionTextVi": "Mục đích của tin nhắn đầu tiên của ông Wilkins là gì?",
        "options": {
            "A": "To confirm a race schedule",
            "B": "To give an estimate of repair costs",
            "C": "To ask for additional time to service a bicycle",
            "D": "To request permission to do some work"
        },
        "optionsVi": {
            "A": "(A) Để xác nhận lịch thi đấu",
            "B": "(B) Để đưa ra ước tính chi phí sửa chữa",
            "C": "(C) Để xin thêm thời gian bảo dưỡng xe đạp",
            "D": "(D) Để xin phép được thực hiện một số hạng mục công việc"
        }
    },
    173: {
        "questionText": "What most likely cost about $30 ?",
        "questionTextVi": "Khoản nào nhiều khả năng có giá khoảng $30?",
        "options": {
            "A": "A regular maintenance service",
            "B": "A drivetrain cleaning",
            "C": "New brake pads",
            "D": "Labor charges"
        },
        "optionsVi": {
            "A": "(A) Dịch vụ bảo dưỡng thông thường",
            "B": "(B) Vệ sinh bộ truyền động",
            "C": "(C) Má phanh mới",
            "D": "(D) Tiền công lao động"
        }
    },
    174: {
        "questionText": "At 11:24 A.M., what does Ms. Clarke most likely mean when she writes, 'I guess we have to do it'?",
        "questionTextVi": "Vào lúc 11:24 sáng, cô Clarke có ý gì nhất khi viết 'Tôi đoán chúng ta phải làm thôi'?",
        "options": {
            "A": "She will participate in an upcoming event.",
            "B": "She will authorize the recommended repairs.",
            "C": "She will cancel a scheduled appointment.",
            "D": "She will purchase a new bicycle."
        },
        "optionsVi": {
            "A": "(A) Cô ấy sẽ tham gia một sự kiện sắp tới.",
            "B": "(B) Cô ấy sẽ cho phép thực hiện việc sửa chữa được khuyến nghị.",
            "C": "(C) Cô ấy sẽ hủy một cuộc hẹn đã lên lịch.",
            "D": "(D) Cô ấy sẽ mua một chiếc xe đạp mới."
        }
    },
    176: {
        "questionText": "Who most likely is Ms. Raferty?",
        "questionTextVi": "Cô Raferty nhiều khả năng nhất là ai?",
        "options": {
            "A": "A plumbing contractor",
            "B": "An office assistant",
            "C": "A medical clinic administrator",
            "D": "A Web-site designer"
        },
        "optionsVi": {
            "A": "(A) Một nhà thầu sửa ống nước",
            "B": "(B) Một trợ lý văn phòng",
            "C": "(C) Quản trị viên phòng khám y tế",
            "D": "(D) Một nhà thiết kế trang web"
        }
    },
    177: {
        "questionText": "What is indicated about Mr. Zimri?",
        "questionTextVi": "Điều gì được chỉ ra về ông Zimri?",
        "options": {
            "A": "He is seeking to hire technicians.",
            "B": "He was recommended by Dr. O'Leary.",
            "C": "He has designed websites for several clinics.",
            "D": "He will attend a grand opening party."
        },
        "optionsVi": {
            "A": "(A) Ông ấy đang tìm kiếm để tuyển dụng kỹ thuật viên.",
            "B": "(B) Ông ấy được bác sĩ O'Leary giới thiệu.",
            "C": "(C) Ông ấy đã thiết kế trang web cho nhiều phòng khám.",
            "D": "(D) Ông ấy sẽ tham dự một bữa tiệc khai trương."
        }
    },
    178: {
        "questionText": "Where will a grand opening party be held?",
        "questionTextVi": "Bữa tiệc khai trương sẽ được tổ chức ở đâu?",
        "options": {
            "A": "At Zimri Mechanical's main office",
            "B": "At 47 High Street",
            "C": "At the Brandmore shoe factory",
            "D": "At Clary Medical Centre's main campus"
        },
        "optionsVi": {
            "A": "(A) Tại văn phòng chính của Zimri Mechanical",
            "B": "(B) Tại số 47 phố High Street",
            "C": "(C) Tại nhà máy giày Brandmore",
            "D": "(D) Tại cơ sở chính của Trung tâm Y tế Clary"
        }
    },
    179: {
        "questionText": "The word 'maintain' in paragraph 2, line 4, of the Web page is closest in meaning to",
        "questionTextVi": "Từ 'maintain' trong đoạn 2, dòng 4 của trang web gần nghĩa nhất với từ nào?",
        "options": {"A": "support", "B": "operate", "C": "preserve", "D": "claim"},
        "optionsVi": {"A": "(A) hỗ trợ", "B": "(B) vận hành", "C": "(C) giữ gìn, bảo tồn", "D": "(D) khẳng định"}
    },
    180: {
        "questionText": "According to the Web page, what is NOT part of the Clary Clinic?",
        "questionTextVi": "Theo trang web, điều gì KHÔNG thuộc về Phòng khám Clary?",
        "options": {
            "A": "Examination rooms",
            "B": "An x-ray facility",
            "C": "A pharmacy",
            "D": "A laboratory"
        },
        "optionsVi": {
            "A": "(A) Các phòng khám bệnh",
            "B": "(B) Cơ sở chụp X-quang",
            "C": "(C) Một hiệu thuốc",
            "D": "(D) Một phòng xét nghiệm"
        }
    },
    191: {
        "questionText": "What is stated in the job posting about the managerial position?",
        "questionTextVi": "Điều gì được nêu trong thông báo tuyển dụng về vị trí quản lý?",
        "options": {
            "A": "It is located in Melbridge.",
            "B": "It requires experience with graphic design software.",
            "C": "It includes health insurance benefits.",
            "D": "It will be part-time until April 1."
        },
        "optionsVi": {
            "A": "(A) Nó nằm ở Melbridge.",
            "B": "(B) Nó yêu cầu kinh nghiệm với phần mềm thiết kế đồ họa.",
            "C": "(C) Nó bao gồm các quyền lợi bảo hiểm y tế.",
            "D": "(D) Nó sẽ là công việc bán thời gian cho đến ngày 1 tháng 4."
        }
    },
    192: {
        "questionText": "According to the flyer, what will happen on May 1 ?",
        "questionTextVi": "Theo tờ rơi, điều gì sẽ diễn ra vào ngày 1 tháng 5?",
        "options": {
            "A": "A gallery will open on the boardwalk.",
            "B": "A film will be screened in Brady Park.",
            "C": "The Summer Scene Arts Program will begin.",
            "D": "Craft vendors will sell food and drinks."
        },
        "optionsVi": {
            "A": "(A) Một phòng trưng bày sẽ mở cửa trên lối đi lát ván.",
            "B": "(B) Một bộ phim sẽ được chiếu ở công viên Brady.",
            "C": "(C) Chương trình Nghệ thuật Summer Scene sẽ bắt đầu.",
            "D": "(D) Các gian hàng thủ công sẽ bán đồ ăn và thức uống."
        }
    },
    193: {
        "questionText": "Who is Geetu Gelang?",
        "questionTextVi": "Geetu Gelang là ai?",
        "options": {
            "A": "An artist demonstrating virtual art",
            "B": "The hiring manager for Middleton County",
            "C": "A gallery manager in Cromwood",
            "D": "The director of Brady Park activities"
        },
        "optionsVi": {
            "A": "(A) Một nghệ sĩ trình diễn nghệ thuật ảo",
            "B": "(B) Giám đốc tuyển dụng của Hạt Middleton",
            "C": "(C) Một người quản lý phòng tranh tại Cromwood",
            "D": "(D) Giám đốc hoạt động của Công viên Brady"
        }
    },
    196: {
        "questionText": "What does Gendalla mainly produce?",
        "questionTextVi": "Thương hiệu Gendalla chủ yếu sản xuất mặt hàng gì?",
        "options": {"A": "Watches", "B": "Luggage", "C": "Clothing", "D": "Fragrances"},
        "optionsVi": {"A": "(A) Đồng hồ", "B": "(B) Hành lý, vali", "C": "(C) Quần áo thời trang", "D": "(D) Nước hoa"}
    },
    197: {
        "questionText": "According to the article, why is Senano Designs acquiring Gendalla?",
        "questionTextVi": "Theo bài báo, tại sao Senano Designs lại thâu tóm Gendalla?",
        "options": {
            "A": "To sell products at a lower price",
            "B": "To expand its social media presence",
            "C": "To offer a more diverse range of products",
            "D": "To address declining sales in some cities"
        },
        "optionsVi": {
            "A": "(A) Để bán sản phẩm với mức giá thấp hơn",
            "B": "(B) Để mở rộng sự hiện diện trên mạng xã hội",
            "C": "(C) Để cung cấp danh mục sản phẩm đa dạng hơn",
            "D": "(D) Để giải quyết tình trạng sụt giảm doanh số ở một số thành phố"
        }
    },
    198: {
        "questionText": "What are Gendalla's employees invited to do on March 28 ?",
        "questionTextVi": "Nhân viên của Gendalla được mời làm gì vào ngày 28 tháng 3?",
        "options": {
            "A": "Suggest changes to a travel policy",
            "B": "Attend a meeting in the afternoon",
            "C": "Tour Senano's corporate headquarters",
            "D": "Make an appointment with an accountant"
        },
        "optionsVi": {
            "A": "(A) Đề xuất các thay đổi đối với chính sách đi lại",
            "B": "(B) Tham dự một cuộc họp vào buổi chiều",
            "C": "(C) Tham quan trụ sở chính của Senano",
            "D": "(D) Đặt lịch hẹn với một kế toán viên"
        }
    },
    199: {
        "questionText": "Where is Ms. Dawson's office?",
        "questionTextVi": "Văn phòng của bà Dawson ở đâu?",
        "options": {"A": "In New York", "B": "In Chicago", "C": "In Philadelphia", "D": "In Los Angeles"},
        "optionsVi": {"A": "(A) Tại New York", "B": "(B) Tại Chicago", "C": "(C) Tại Philadelphia", "D": "(D) Tại Los Angeles"}
    },
    200: {
        "questionText": "How is Gendalla's current travel expense policy likely different from Senano's?",
        "questionTextVi": "Chính sách công tác phí hiện tại của Gendalla nhiều khả năng khác với của Senano như thế nào?",
        "options": {
            "A": "A receipt must be submitted for every expense.",
            "B": "Preapproval must be obtained for expenses over $50.",
            "C": "The expense report must be signed by a manager.",
            "D": "Employees can submit their expense reports jointly."
        },
        "optionsVi": {
            "A": "(A) Phải nộp hóa đơn cho từng khoản chi tiêu bất kể lớn nhỏ.",
            "B": "(B) Phải có phê duyệt trước đối với các khoản chi trên $50.",
            "C": "(C) Báo cáo chi phí phải được người quản lý ký duyệt.",
            "D": "(D) Nhân viên có thể nộp chung báo cáo chi phí của họ."
        }
    }
}

# Apply to test4.json
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

print(f"Applied {len(t4_fixes)} Part 7 question fixes to test4.json!")

# Apply to test5.json
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

print(f"Applied {len(t5_fixes)} Part 7 & Part 4 fixes to test5.json!")
