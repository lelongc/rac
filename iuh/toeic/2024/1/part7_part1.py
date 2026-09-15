# part7_part1.py: Part 7 Questions 147 - 175
import json

P7_PART1 = [
    # 147 - 148
    {
        "id": 147,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_1",
        "passageTitle": "Product Information: Indoor Delight",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_9.png"],
        "passageText": "STOP! PLEASE READ FIRST.\nThank you for purchasing this item. As you do the unpacking, please verify that all components are included and place them in a safe area to avoid loss or damage. Assemble the item on a soft surface or on the flattened empty box. Follow the pictures and begin the assembly by placing the main part on its side. Never overtighten any screws or bolts, or you may damage the wood or cushioning. Please visit our Web site to obtain maintenance tips and register your product for warranty coverage: www.indoordelight.com.",
        "passageTextVi": "DỪNG LẠI! VUI LÒNG ĐỌC TRƯỚC TIÊN.\nCảm ơn bạn đã mua sản phẩm này. Trong quá trình mở hộp, vui lòng kiểm tra xem tất cả các bộ phận đã đầy đủ hay chưa và đặt chúng ở nơi an toàn để tránh thất lạc hoặc hư hỏng. Hãy lắp ráp sản phẩm trên một bề mặt mềm hoặc trên vỏ hộp rỗng đã được trải phẳng. Làm theo hình ảnh hướng dẫn và bắt đầu lắp ráp bằng cách đặt bộ phận chính nằm nghiêng. Không bao giờ siết quá chặt ốc vít hoặc bu lông, nếu không bạn có thể làm hỏng gỗ hoặc đệm lót. Vui lòng truy cập trang web của chúng tôi để nhận các mẹo bảo dưỡng và đăng ký bảo hành sản phẩm: www.indoordelight.com.",
        "questionText": "Where is the information most likely found?",
        "questionTextVi": "Thông tin này rất có thể được tìm thấy ở đâu?",
        "options": {
            "A": "On a door",
            "B": "On a receipt",
            "C": "In a box",
            "D": "On a Web site"
        },
        "optionsVi": {
            "A": "Trên một cánh cửa",
            "B": "Trên một biên lai",
            "C": "Bên trong một chiếc hộp đựng đồ",
            "D": "Trên một trang web"
        },
        "correctAnswer": "C",
        "explanation": "Đoạn văn viết: 'As you do the unpacking, please verify that all components are included... Assemble the item on a soft surface or on the flattened empty box' (Khi bạn mở hộp, vui lòng kiểm tra xem tất cả các linh kiện có đầy đủ không... Lắp ráp sản phẩm trên bề mặt mềm hoặc trên chiếc hộp rỗng đã làm phẳng). Điều này chứng minh tờ hướng dẫn này nằm ngay bên trong thùng/hộp sản phẩm khi người mua mở ra. Chọn (C).",
        "vocabulary": [
            { "word": "unpacking", "ipa": "/ʌnˈpæk.ɪŋ/", "pos": "n", "meaning": "việc mở hộp, tháo kiện hàng", "example": "Be careful during the unpacking of delicate glassware." },
            { "word": "component", "ipa": "/kəmˈpəʊ.nənt/", "pos": "n", "meaning": "thành phần, linh kiện", "example": "The kit includes all necessary assembly components." },
            { "word": "assembly", "ipa": "/əˈsem.bli/", "pos": "n", "meaning": "sự lắp ráp", "example": "Assembly instructions are printed on page two." }
        ],
        "collocations": [
            { "phrase": "verify components", "meaning": "kiểm tra đối chiếu các linh kiện" },
            { "phrase": "warranty coverage", "meaning": "phạm vi bảo hành" }
        ],
        "grammarPoints": [
            { "title": "Mệnh lệnh thức (Imperative Form)", "content": "Sử dụng động từ nguyên thể không 'to' đầu câu ('Verify...', 'Assemble...', 'Follow...') để đưa ra chỉ dẫn kỹ thuật." }
        ]
    },
    {
        "id": 148,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_1",
        "passageTitle": "Product Information: Indoor Delight",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_9.png"],
        "passageText": "STOP! PLEASE READ FIRST.\nThank you for purchasing this item. As you do the unpacking, please verify that all components are included and place them in a safe area to avoid loss or damage. Assemble the item on a soft surface or on the flattened empty box. Follow the pictures and begin the assembly by placing the main part on its side. Never overtighten any screws or bolts, or you may damage the wood or cushioning. Please visit our Web site to obtain maintenance tips and register your product for warranty coverage: www.indoordelight.com.",
        "passageTextVi": "DỪNG LẠI! VUI LÒNG ĐỌC TRƯỚC TIÊN... Không bao giờ siết quá chặt ốc vít hoặc bu lông, nếu không bạn có thể làm hỏng gỗ hoặc đệm lót...",
        "questionText": "What kind of item is most likely discussed?",
        "questionTextVi": "Loại mặt hàng nào nhiều khả năng đang được thảo luận nhất?",
        "options": {
            "A": "A desktop computer",
            "B": "A piece of furniture",
            "C": "A household appliance",
            "D": "A power tool"
        },
        "optionsVi": {
            "A": "Một máy tính để bàn",
            "B": "Một món đồ nội thất",
            "C": "Một thiết bị gia dụng",
            "D": "Một dụng cụ điện cầm tay"
        },
        "correctAnswer": "B",
        "explanation": "Chi tiết 'damage the wood or cushioning' (làm hỏng phần gỗ hoặc phần đệm mút) và 'indoordelight' cho thấy đây là một món đồ nội thất (furniture), ví dụ như ghế bọc đệm hoặc sofa gỗ. Chọn (B).",
        "vocabulary": [
            { "word": "cushioning", "ipa": "/ˈkʊʃ.ən.ɪŋ/", "pos": "n", "meaning": "lớp đệm, phần đệm mút", "example": "The chair provides firm lumbar cushioning." },
            { "word": "overtighten", "ipa": "/ˌəʊ.vəˈtaɪ.tən/", "pos": "v", "meaning": "siết quá chặt", "example": "Do not overtighten the bolts to prevent cracking." }
        ],
        "collocations": [
            { "phrase": "piece of furniture", "meaning": "món đồ nội thất" },
            { "phrase": "screws or bolts", "meaning": "ốc vít hoặc bu lông" }
        ],
        "grammarPoints": [
            { "title": "Kỹ năng đọc suy luận chi tiết (Inference Question)", "content": "Tìm kiếm manh mối từ các từ vựng chuyên ngành trong bài: 'wood or cushioning', 'screws or bolts', 'assembly'." }
        ]
    },

    # 149 - 150
    {
        "id": 149,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_2",
        "passageTitle": "Meeting Schedule: Winnipeg and Toulouse Offices",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_10.png"],
        "passageText": "We are asking all Winnipeg staff to keep a copy of this schedule at their desks as a quick reference tool for scheduling interoffice meetings. Whenever possible, please schedule these meetings during one of the underlined hours, that is, after 7:00 A.M. but before 11:00 A.M.\n\nWinnipeg:\n7:00 A.M. | 8:00 A.M. | 9:00 A.M. | 10:00 A.M. | 11:00 A.M. | 12:00 noon\n\nToulouse:\n2:00 P.M. | 3:00 P.M. | 4:00 P.M. | 5:00 P.M. | 6:00 P.M. | 7:00 P.M.",
        "passageTextVi": "Chúng tôi yêu cầu toàn thể nhân viên tại Winnipeg lưu một bản sao của lịch trình này tại bàn làm việc như một công cụ tra cứu nhanh để sắp xếp các cuộc họp liên văn phòng. Bất cứ khi nào có thể, vui lòng lên lịch các cuộc họp này vào một trong các khung giờ được gạch chân, tức là sau 7:00 sáng nhưng trước 11:00 sáng.\n\nGiờ Winnipeg:\n7:00 SA | 8:00 SA | 9:00 SA | 10:00 SA | 11:00 SA | 12:00 trưa\n\nGiờ Toulouse:\n2:00 CH | 3:00 CH | 4:00 CH | 5:00 CH | 6:00 CH | 7:00 CH",
        "questionText": "What is suggested by the schedule?",
        "questionTextVi": "Lịch trình này gợi ý điều gì?",
        "options": {
            "A": "A conference has been scheduled.",
            "B": "A firm has offices in two time zones.",
            "C": "Administrative assistants make travel plans.",
            "D": "Some meeting times have been changed."
        },
        "optionsVi": {
            "A": "Một hội nghị đã được lên lịch.",
            "B": "Một công ty có các văn phòng ở hai múi giờ khác nhau.",
            "C": "Các trợ lý hành chính lập kế hoạch đi công tác.",
            "D": "Một số thời gian họp đã được thay đổi."
        },
        "correctAnswer": "B",
        "explanation": "Lịch trình so sánh giờ làm việc giữa văn phòng Winnipeg (Canada) và văn phòng Toulouse (Pháp) để sắp xếp cuộc họp liên văn phòng ('interoffice meetings'). Điều này chứng tỏ công ty có các văn phòng nằm ở hai múi giờ khác nhau. Chọn (B).",
        "vocabulary": [
            { "word": "interoffice", "ipa": "/ˌɪn.tərˈɒf.ɪs/", "pos": "adj", "meaning": "giữa các văn phòng với nhau", "example": "Send the documents via interoffice mail." },
            { "word": "time zone", "ipa": "/ˈtaɪm ˌzəʊn/", "pos": "n", "meaning": "múi giờ", "example": "We collaborate with teams across multiple time zones." }
        ],
        "collocations": [
            { "phrase": "interoffice meetings", "meaning": "các cuộc họp liên văn phòng" },
            { "phrase": "quick reference tool", "meaning": "công cụ tra cứu nhanh" }
        ],
        "grammarPoints": [
            { "title": "Từ ghép với tiền tố 'inter-'", "content": "Tiền tố 'inter-' nghĩa là 'giữa/liên kết' (interoffice = giữa các văn phòng, international = quốc tế)." }
        ]
    },
    {
        "id": 150,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_2",
        "passageTitle": "Meeting Schedule: Winnipeg and Toulouse Offices",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_10.png"],
        "passageText": "We are asking all Winnipeg staff to keep a copy of this schedule at their desks as a quick reference tool for scheduling interoffice meetings. Whenever possible, please schedule these meetings during one of the underlined hours, that is, after 7:00 A.M. but before 11:00 A.M.\n\nWinnipeg:\n7:00 A.M. | 8:00 A.M. | 9:00 A.M. | 10:00 A.M. | 11:00 A.M. | 12:00 noon\n\nToulouse:\n2:00 P.M. | 3:00 P.M. | 4:00 P.M. | 5:00 P.M. | 6:00 P.M. | 7:00 P.M.",
        "passageTextVi": "...Bất cứ khi nào có thể, vui lòng lên lịch các cuộc họp này vào một trong các khung giờ được gạch chân, tức là sau 7:00 sáng nhưng trước 11:00 sáng...",
        "questionText": "What is indicated about 11:00 A.M. Winnipeg time?",
        "questionTextVi": "Điều gì được chỉ ra về khung giờ 11:00 sáng theo giờ Winnipeg?",
        "options": {
            "A": "It is when the Winnipeg office closes for lunch.",
            "B": "It is when staff in Toulouse begin their workday.",
            "C": "It is not a preferred time to schedule a meeting.",
            "D": "It has just been added to the schedule."
        },
        "optionsVi": {
            "A": "Đó là lúc văn phòng Winnipeg nghỉ ăn trưa.",
            "B": "Đó là lúc nhân viên ở Toulouse bắt đầu ngày làm việc.",
            "C": "Đó không phải là thời điểm được ưu tiên để sắp xếp cuộc họp.",
            "D": "Nó vừa mới được thêm vào lịch trình."
        },
        "correctAnswer": "C",
        "explanation": "Đoạn văn hướng dẫn rõ: 'please schedule these meetings during one of the underlined hours, that is, after 7:00 A.M. but before 11:00 A.M.' (vui lòng lên lịch họp vào các giờ được gạch chân, tức là sau 7:00 sáng nhưng TRƯỚC 11:00 sáng). Vì 11:00 AM không nằm trong khoảng 'trước 11:00 AM' và lúc đó ở Toulouse đã là 6:00 PM (hết giờ làm), nên đây không phải là khung giờ được ưu tiên. Chọn (C).",
        "vocabulary": [
            { "word": "preferred", "ipa": "/prɪˈfɜːd/", "pos": "adj", "meaning": "được ưa chuộng hơn, được ưu tiên", "example": "Morning is our preferred time for interviews." },
            { "word": "underlined", "ipa": "/ˌʌn.dəˈlaɪnd/", "pos": "adj", "meaning": "được gạch chân", "example": "Check the underlined words in the text." }
        ],
        "collocations": [
            { "phrase": "preferred time", "meaning": "thời gian được ưu tiên lựa chọn" },
            { "phrase": "schedule a meeting", "meaning": "lên lịch một cuộc họp" }
        ],
        "grammarPoints": [
            { "title": "Giới từ chỉ thời gian 'before' và 'after'", "content": "'before 11:00 A.M.' có nghĩa là trước 11 giờ, nên chính xác lúc 11:00 A.M. không thuộc khoảng thời gian được khuyến nghị." }
        ]
    },

    # 151 - 152
    {
        "id": 151,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_3",
        "passageTitle": "Brochure: The Bryant Foyer & Andito's",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_11.png"],
        "passageText": "The Bryant Foyer is one of the premier event spaces in our area. Set on a hill, it has expansive windows that provide sweeping views of the adjacent botanical gardens and the river. Built in 1897, it was the home of the Francona Charitable Trust until its renovation just over a year ago. Today, the space can accommodate up to 200 guests and is ideal for wedding receptions, office parties, and panel presentations. With its marble floors, cathedral ceiling, and stunning artwork, the Bryant Foyer is the ideal location for your next gathering. The on-site restaurant, Andito's, caters our events and also operates as its own business. This farm-to-table restaurant, headed by chef Michaela Rymond, meets all dietary needs and has revolutionized the local food scene. Area residents know to plan far in advance to get a seat. To reserve the event space or to make a dinner reservation, give us a call at 216-555-0157.",
        "passageTextVi": "The Bryant Foyer là một trong những không gian tổ chức sự kiện hàng đầu trong khu vực của chúng tôi. Nằm trên một ngọn đồi, nơi đây có những ô cửa sổ lớn mang đến tầm nhìn bao quát ra vườn bách thảo liền kề và dòng sông. Được xây dựng vào năm 1897, nơi đây từng là trụ sở của Quỹ Từ thiện Francona cho đến khi được cải tạo cách đây hơn một năm. Ngày nay, không gian có thể chứa tới 200 khách và là nơi lý tưởng cho các buổi tiệc cưới, tiệc công ty và các buổi thuyết trình hội thảo. Với sàn lát đá cẩm thạch, trần nhà cao kiểu vòm thánh đường và các tác phẩm nghệ thuật tuyệt đẹp, Bryant Foyer là địa điểm lý tưởng cho buổi tụ họp tiếp theo của bạn. Nhà hàng tại chỗ, Andito's, phục vụ ăn uống cho các sự kiện của chúng tôi và cũng hoạt động như một doanh nghiệp độc lập. Nhà hàng từ nông trại đến bàn ăn này do bếp trưởng Michaela Rymond đứng đầu, đáp ứng mọi nhu cầu ăn kiêng và đã tạo nên cuộc cách mạng cho nền ẩm thực địa phương. Cư dân trong khu vực đều biết phải lên kế hoạch từ rất sớm để có được chỗ ngồi. Để đặt không gian sự kiện hoặc đặt bàn ăn tối, vui lòng gọi cho chúng tôi theo số 216-555-0157.",
        "questionText": "What is indicated about the Bryant Foyer?",
        "questionTextVi": "Điều gì được chỉ ra về tòa nhà The Bryant Foyer?",
        "options": {
            "A": "It is located on the shores of a lake.",
            "B": "It has recently been renovated.",
            "C": "It will build a botanical garden for guests.",
            "D": "It is reserved solely for corporate events."
        },
        "optionsVi": {
            "A": "Nó nằm bên bờ của một cái hồ.",
            "B": "Nó gần đây đã được cải tạo, nâng cấp.",
            "C": "Nó sẽ xây dựng một vườn bách thảo cho khách tham quan.",
            "D": "Nó chỉ được dành riêng cho các sự kiện doanh nghiệp."
        },
        "correctAnswer": "B",
        "explanation": "Đoạn 1 nêu rõ: 'until its renovation just over a year ago' (cho đến khi được cải tạo cách đây hơn một năm). Điều này tương ứng với phương án (B) 'It has recently been renovated' (Nó gần đây đã được cải tạo).",
        "vocabulary": [
            { "word": "renovation", "ipa": "/ˌren.əˈveɪ.ʃən/", "pos": "n", "meaning": "sự cải tạo, tu bổ", "example": "The historic building reopened after extensive renovation." },
            { "word": "expansive", "ipa": "/ɪkˈspæn.sɪv/", "pos": "adj", "meaning": "rộng lớn, bao la", "example": "The penthouse features expansive glass windows." },
            { "word": "accommodate", "ipa": "/əˈkɒm.ə.deɪt/", "pos": "v", "meaning": "chứa được, đáp ứng sức chứa", "example": "The auditorium can accommodate 500 people." }
        ],
        "collocations": [
            { "phrase": "sweeping views", "meaning": "tầm nhìn bao quát, trải rộng" },
            { "phrase": "wedding reception", "meaning": "tiệc cưới" }
        ],
        "grammarPoints": [
            { "title": "Rút gọn mệnh đề phân từ (Past Participle Clause)", "content": "'Built in 1897, it was the home of...' là mệnh đề phân từ quá khứ rút gọn mang nghĩa bị động: '(Being) built in 1897'." }
        ]
    },
    {
        "id": 152,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_3",
        "passageTitle": "Brochure: The Bryant Foyer & Andito's",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_11.png"],
        "passageText": "The Bryant Foyer is one of the premier event spaces in our area... The on-site restaurant, Andito's, caters our events and also operates as its own business. This farm-to-table restaurant, headed by chef Michaela Rymond, meets all dietary needs and has revolutionized the local food scene. Area residents know to plan far in advance to get a seat. To reserve the event space or to make a dinner reservation, give us a call at 216-555-0157.",
        "passageTextVi": "...Nhà hàng tại chỗ, Andito's, phục vụ ăn uống cho các sự kiện... Cư dân trong khu vực đều biết phải lên kế hoạch từ rất sớm để có được chỗ ngồi...",
        "questionText": "What is suggested about Andito's?",
        "questionTextVi": "Điều gì được gợi ý về nhà hàng Andito's?",
        "options": {
            "A": "It was started by an international chef.",
            "B": "It offers limited menu options.",
            "C": "It is now funded by a charitable organization.",
            "D": "It is very popular with local residents."
        },
        "optionsVi": {
            "A": "Nó được thành lập bởi một đầu bếp quốc tế.",
            "B": "Nó cung cấp các lựa chọn thực đơn hạn chế.",
            "C": "Hiện nay nó được tài trợ bởi một tổ chức từ thiện.",
            "D": "Nó rất được người dân địa phương ưa chuộng, yêu thích."
        },
        "correctAnswer": "D",
        "explanation": "Đoạn 2 nêu rõ: 'Area residents know to plan far in advance to get a seat' (Cư dân trong vùng đều biết phải lên kế hoạch đặt trước từ rất sớm mới có chỗ ngồi). Điều này chứng tỏ nhà hàng rất đắt khách và được người dân địa phương ưa chuộng (very popular with local residents). Chọn (D).",
        "vocabulary": [
            { "word": "dietary", "ipa": "/ˈdaɪ.ə.tri/", "pos": "adj", "meaning": "thuộc về chế độ ăn uống", "example": "Please inform us of any special dietary requirements." },
            { "word": "revolutionize", "ipa": "/ˌrev.əˈluː.ʃən.aɪz/", "pos": "v", "meaning": "cách mạng hóa", "example": "Smartphones revolutionized communication worldwide." }
        ],
        "collocations": [
            { "phrase": "plan in advance", "meaning": "lên kế hoạch từ trước" },
            { "phrase": "farm-to-table", "meaning": "từ trang trại đến bàn ăn (nguyên liệu tươi sạch)" }
        ],
        "grammarPoints": [
            { "title": "Paraphrase trong bài thi TOEIC", "content": "'plan far in advance to get a seat' được diễn đạt lại (paraphrase) thành 'very popular with local residents'." }
        ]
    },

    # 153 - 154
    {
        "id": 153,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_4",
        "passageTitle": "Text-Message Chain: Joan Chi and Mina Evers",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_12.png"],
        "passageText": "Joan Chi (12:39 P.M.)\nHello Mina. Are you almost finished with the field measurements? I'm getting hungry.\n\nMina Evers (12:40 P.M.)\nSorry, Joan. I'm afraid you and Ms. Lim will have to go to lunch without me today. There's a problem with the site coordinates. This is going to take some time.\n\nJoan Chi (12:51 P.M.)\nOh no. Should we bring something back for you?\n\nMina Evers (12:59 P.M.)\nGet me a chicken sandwich.\n\nJoan Chi (1:00 P.M.)\nSure thing, Mina. See you in a while.",
        "passageTextVi": "Joan Chi (12:39 CH)\nChào Mina. Chị đã đo đạc thực địa sắp xong chưa? Tôi bắt đầu thấy đói rồi.\n\nMina Evers (12:40 CH)\nXin lỗi Joan. Tôi e là bạn và cô Lim sẽ phải đi ăn trưa mà không có tôi hôm nay rồi. Có vấn đề với tọa độ công trường. Việc này sẽ mất một khoảng thời gian.\n\nJoan Chi (12:51 CH)\nÔi không. Chúng tôi có nên mua món gì mang về cho chị không?\n\nMina Evers (12:59 CH)\nMua giúp tôi một cái bánh sandwich gà nhé.\n\nJoan Chi (1:00 CH)\nChắc chắn rồi, Mina. Hẹn gặp lại một lát nữa nhé.",
        "questionText": "At 1:00 P.M., what does Ms. Chi most likely mean when she writes, 'Sure thing, Mina'?",
        "questionTextVi": "Vào lúc 1:00 chiều, cô Chi nhiều khả năng có ý gì nhất khi nhắn: 'Sure thing, Mina'?",
        "options": {
            "A": "She will bring lunch for Ms. Evers.",
            "B": "She can provide a tool that Ms. Evers needs.",
            "C": "Some site coordinates are correct.",
            "D": "Some measurements must be double-checked."
        },
        "optionsVi": {
            "A": "Cô ấy sẽ mua bữa trưa mang về cho cô Evers.",
            "B": "Cô ấy có thể cung cấp công cụ mà cô Evers cần.",
            "C": "Một số tọa độ công trường là chính xác.",
            "D": "Một số số đo phải được kiểm tra lại."
        },
        "correctAnswer": "A",
        "explanation": "Trước đó lúc 12:59 PM, cô Mina Evers nhờ: 'Get me a chicken sandwich' (Mua cho tôi một cái sandwich gà). Câu trả lời lúc 1:00 PM 'Sure thing, Mina' (Chắc chắn rồi, Mina) là lời đồng ý sẽ mua bánh sandwich gà (bữa trưa) mang về cho Mina. Do đó chọn (A).",
        "vocabulary": [
            { "word": "coordinates", "ipa": "/kəʊˈɔː.dɪ.nəts/", "pos": "n", "meaning": "tọa độ", "example": "Enter the GPS coordinates into the navigation device." },
            { "word": "measurements", "ipa": "/ˈmeʒ.ə.mənts/", "pos": "n", "meaning": "các số đo, phép đo lường", "example": "Field measurements must be accurate to the millimeter." }
        ],
        "collocations": [
            { "phrase": "sure thing", "meaning": "chắc chắn rồi, hiển nhiên rồi (khẩu ngữ đồng ý)" },
            { "phrase": "see you in a while", "meaning": "hẹn gặp lại lát nữa" }
        ],
        "grammarPoints": [
            { "title": "Câu hỏi suy luận ý người nói trong đoạn chat (Chat Inference)", "content": "Phân tích ngữ cảnh của lời thoại ngay trước đó: yêu cầu mua đồ ăn -> lời đáp xác nhận thực hiện yêu cầu đó." }
        ]
    },
    {
        "id": 154,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_4",
        "passageTitle": "Text-Message Chain: Joan Chi and Mina Evers",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_12.png"],
        "passageText": "Joan Chi (12:39 P.M.)\nHello Mina. Are you almost finished with the field measurements? I'm getting hungry.\n\nMina Evers (12:40 P.M.)\nSorry, Joan. I'm afraid you and Ms. Lim will have to go to lunch without me today. There's a problem with the site coordinates. This is going to take some time.\n\nJoan Chi (12:51 P.M.)\nOh no. Should we bring something back for you?\n\nMina Evers (12:59 P.M.)\nGet me a chicken sandwich.\n\nJoan Chi (1:00 P.M.)\nSure thing, Mina. See you in a while.",
        "passageTextVi": "...Sorry, Joan. I'm afraid you and Ms. Lim will have to go to lunch without me today... See you in a while.",
        "questionText": "What will happen next?",
        "questionTextVi": "Điều gì sẽ diễn ra tiếp theo?",
        "options": {
            "A": "Ms. Chi will get new site coordinates.",
            "B": "Ms. Chi and Ms. Lim will be out for a while.",
            "C": "Ms. Evers will share a recipe.",
            "D": "Ms. Lim will begin taking measurements."
        },
        "optionsVi": {
            "A": "Cô Chi sẽ lấy các tọa độ công trường mới.",
            "B": "Cô Chi và cô Lim sẽ ra ngoài một lúc để đi ăn trưa.",
            "C": "Cô Evers sẽ chia sẻ một công thức nấu ăn.",
            "D": "Cô Lim sẽ bắt đầu tiến hành đo đạc."
        },
        "correctAnswer": "B",
        "explanation": "Mina bảo Joan và cô Lim hãy đi ăn trưa: 'you and Ms. Lim will have to go to lunch without me today'. Joan nhắn lại: 'See you in a while' (Hẹn gặp lại lát nữa sau khi đi ăn về). Do đó hành động diễn ra tiếp theo là cô Chi và cô Lim sẽ ra ngoài một lúc để đi ăn (will be out for a while). Chọn (B).",
        "vocabulary": [
            { "word": "in a while", "ipa": "/ɪn ə waɪl/", "pos": "idiom", "meaning": "một lát nữa, chẳng bao lâu", "example": "The manager will return in a while." }
        ],
        "collocations": [
            { "phrase": "go to lunch", "meaning": "đi ăn trưa" },
            { "phrase": "take some time", "meaning": "mất chút thời gian" }
        ],
        "grammarPoints": [
            { "title": "Cụm từ 'be out'", "content": "'be out' mang nghĩa là đang ra ngoài (không có mặt tại văn phòng/nơi làm việc)." }
        ]
    }
]

if __name__ == "__main__":
    print(f"P7 Part 1 loaded with {len(P7_PART1)} questions.")
