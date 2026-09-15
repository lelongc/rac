# part7_part3.py: Part 7 Questions 176 - 200 (Double & Triple Passages)
import json

P7_PART3 = [
    # 176 - 180 (Double Passage: Kitchen Swifts & Darius Cordero)
    {
        "id": 176,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_11",
        "passageTitle": "Press Release & Review: Kitchen Swifts and Chef Darius Cordero",
        "passageType": "Double Passage",
        "pageImages": ["assets/images/rc_page_20.png", "assets/images/rc_page_21.png"],
        "passageText": "Aparna Kothari, Media Contact\nKitchen Swifts\nakothari@kitchenswifts.com.au\n\nFOR IMMEDIATE RELEASE\nSYDNEY (4 June)—Kitchen Swifts and Chef Darius Cordero are joining together to give home cooks a new culinary experience. The award-winning chef is the owner of restaurants in both the Philippines and Australia, including the recently opened Enriqua's. He says his cooking reflects his Filipino heritage, which is a blend of many cultures. \"I've designed these simplified recipes for Kitchen Swifts so that cooks at home can enjoy new and exciting flavours with ease,\" he said. \"While preparing and eating these meals, you can feel like you are travelling the world with me.\"\nZahra Chambers, vice president of Kitchen Swifts, says she is pleased to work with Chef Cordero and to offer delicious new recipes to their customers. Kitchen Swifts supplies menus, recipes, and ingredients for two people, four people, or six people, including a range of vegetarian selections. Customers choose the most appropriate meal options, and then a box is delivered weekly. Current customers will see no price increase with the partnership. To find out more, visit the Kitchen Swifts Web site at www.kitchenswifts.com.au.\n\n---\nhttps://www.sydneyrestaurants.com.au\nA colleague arranged for us to eat at Enriqua's while I was at a conference in Sydney. It is usually fully booked for dinner; you may need to call months in advance for a table. We had a wonderful lunch there instead. Everything was delicious, and the bread and desserts are baked on-site! It was a worthwhile treat before I flew back to Hong Kong. — Meili Guan",
        "passageTextVi": "Aparna Kothari, Liên hệ Truyền thông\nKitchen Swifts\nakothari@kitchenswifts.com.au\n\nTHÔNG CÁO BÁO CHÍ ĐỂ PHÁT HÀNH NGAY\nSYDNEY (4 tháng 6)—Kitchen Swifts và Bếp trưởng Darius Cordero đang cùng bắt tay hợp tác để mang đến cho những người nấu ăn tại gia một trải nghiệm ẩm thực hoàn toàn mới. Vị bếp trưởng từng đoạt giải thưởng này là chủ sở hữu của các nhà hàng ở cả Philippines và Úc, bao gồm nhà hàng Enriqua's mới khai trương gần đây. Ông cho biết phong cách nấu ăn của mình phản ánh di sản văn hóa Philippines, vốn là sự hòa quyện của nhiều nền văn hóa. \"Tôi đã thiết kế các công thức đơn giản hóa này cho Kitchen Swifts để những người nấu ăn tại nhà có thể thưởng thức các hương vị mới lạ, thú vị một cách dễ dàng,\" ông chia sẻ. \"Trong khi chuẩn bị và thưởng thức những bữa ăn này, bạn có thể cảm thấy như đang cùng tôi du lịch khắp thế giới.\"\nZahra Chambers, phó chủ tịch của Kitchen Swifts, cho biết bà rất vui mừng được làm việc với Bếp trưởng Cordero và mang đến những công thức nấu ăn mới ngon miệng cho khách hàng của họ. Kitchen Swifts cung cấp thực đơn, công thức nấu ăn và nguyên liệu dành cho hai người, bốn người hoặc sáu người, bao gồm cả một loạt các lựa chọn món chay. Khách hàng lựa chọn các phương án bữa ăn phù hợp nhất, sau đó một hộp nguyên liệu sẽ được giao hàng tuần. Khách hàng hiện tại sẽ không thấy giá tăng với sự hợp tác này. Để tìm hiểu thêm, vui lòng truy cập trang web của Kitchen Swifts tại www.kitchenswifts.com.au.\n\n---\nhttps://www.sydneyrestaurants.com.au\nMột đồng nghiệp đã sắp xếp cho chúng tôi ăn tại Enriqua's trong khi tôi tham dự một hội nghị ở Sydney. Nơi này thường kín chỗ hoàn toàn cho bữa tối; bạn có thể phải gọi điện trước nhiều tháng để đặt bàn. Thay vào đó, chúng tôi đã có một bữa trưa tuyệt vời tại đây. Mọi thứ đều ngon miệng, bánh mì và món tráng miệng đều được nướng tại chỗ! Đó là một bữa thưởng thức hoàn toàn xứng đáng trước khi tôi bay trở về Hồng Kông. — Meili Guan",
        "questionText": "What is the purpose of the press release?",
        "questionTextVi": "Mục đích của bản thông cáo báo chí là gì?",
        "options": {
            "A": "To promote the opening of a restaurant",
            "B": "To announce a business partnership",
            "C": "To introduce a travel program",
            "D": "To congratulate an award recipient"
        },
        "optionsVi": {
            "A": "Quảng bá cho việc khai trương một nhà hàng",
            "B": "Thông báo về một mối quan hệ hợp tác kinh doanh",
            "C": "Giới thiệu một chương trình du lịch",
            "D": "Chúc mừng một người nhận giải thưởng"
        },
        "correctAnswer": "B",
        "explanation": "Ngay đầu thông cáo báo chí nêu: 'Kitchen Swifts and Chef Darius Cordero are joining together to give home cooks a new culinary experience' và nhắc đến 'the partnership'. Mục đích chính là thông báo về sự hợp tác kinh doanh giữa Kitchen Swifts và Bếp trưởng Darius Cordero (To announce a business partnership). Chọn (B).",
        "vocabulary": [
            { "word": "culinary", "ipa": "/ˈkʌl.ɪ.nər.i/", "pos": "adj", "meaning": "thuộc về ẩm thực, nấu nướng", "example": "The city is famous for its diverse culinary delights." },
            { "word": "partnership", "ipa": "/ˈpɑːt.nə.ʃɪp/", "pos": "n", "meaning": "sự hợp tác, quan hệ đối tác", "example": "The two firms entered into a strategic partnership." }
        ],
        "collocations": [
            { "phrase": "culinary experience", "meaning": "trải nghiệm ẩm thực" },
            { "phrase": "announce a partnership", "meaning": "công bố sự hợp tác đối tác" }
        ],
        "grammarPoints": [
            { "title": "Cấu trúc 'join together to + V'", "content": "'join together to do something': cùng nhau liên kết để thực hiện mục tiêu kinh doanh chung." }
        ]
    },
    {
        "id": 177,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_11",
        "passageTitle": "Press Release & Review: Kitchen Swifts and Chef Darius Cordero",
        "passageType": "Double Passage",
        "pageImages": ["assets/images/rc_page_20.png", "assets/images/rc_page_21.png"],
        "passageText": "He says his cooking reflects his Filipino heritage, which is a blend of many cultures.",
        "passageTextVi": "Ông cho biết phong cách nấu ăn của mình phản ánh di sản văn hóa Philippines, vốn là sự hòa quyện của nhiều nền văn hóa.",
        "questionText": "In the press release, the word 'reflects' in paragraph 1, line 4, is closest in meaning to",
        "questionTextVi": "Trong bản thông cáo báo chí, từ 'reflects' ở đoạn 1, dòng 4 gần nghĩa nhất với",
        "options": {
            "A": "results in",
            "B": "changes",
            "C": "shows",
            "D": "thinks about"
        },
        "optionsVi": {
            "A": "dẫn đến kết quả là",
            "B": "thay đổi",
            "C": "thể hiện, cho thấy, phản ánh",
            "D": "suy nghĩ về"
        },
        "correctAnswer": "C",
        "explanation": "Trong ngữ cảnh 'cooking reflects his Filipino heritage' (ẩm thực của ông phản ánh di sản Philippines), từ 'reflects' mang nghĩa biểu hiện, thể hiện rõ nét văn hóa. Từ đồng nghĩa chính xác nhất là (C) 'shows' (cho thấy, thể hiện).",
        "vocabulary": [
            { "word": "reflect", "ipa": "/rɪˈflekt/", "pos": "v", "meaning": "phản ánh, thể hiện", "example": "Her poetry reflects her deep connection to nature." },
            { "word": "heritage", "ipa": "/ˈher.ɪ.tɪdʒ/", "pos": "n", "meaning": "di sản văn hóa", "example": "The historic quarter protects the national architectural heritage." }
        ],
        "collocations": [
            { "phrase": "reflect cultural heritage", "meaning": "phản ánh di sản văn hóa" }
        ],
        "grammarPoints": [
            { "title": "Đa nghĩa của động từ 'reflect'", "content": "'reflect' có thể là phản xạ ánh sáng hoặc suy ngẫm ('reflect on'), nhưng khi đi với tân ngữ trừu tượng thì mang nghĩa 'phản ánh/thể hiện' (= show)." }
        ]
    },
    {
        "id": 178,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_11",
        "passageTitle": "Press Release & Review: Kitchen Swifts and Chef Darius Cordero",
        "passageType": "Double Passage",
        "pageImages": ["assets/images/rc_page_20.png", "assets/images/rc_page_21.png"],
        "passageText": "Kitchen Swifts supplies menus, recipes, and ingredients for two people, four people, or six people, including a range of vegetarian selections. Customers choose the most appropriate meal options, and then a box is delivered weekly.",
        "passageTextVi": "Kitchen Swifts cung cấp thực đơn, công thức nấu ăn và nguyên liệu cho 2 người, 4 người hoặc 6 người, bao gồm cả các lựa chọn ăn chay. Khách hàng lựa chọn các phương án bữa ăn phù hợp nhất...",
        "questionText": "What is indicated about Kitchen Swifts?",
        "questionTextVi": "Điều gì được chỉ ra về dịch vụ Kitchen Swifts?",
        "options": {
            "A": "It raised its prices for all customers.",
            "B": "It revised its delivery schedule.",
            "C": "It offers several meal options.",
            "D": "It has a new vice president."
        },
        "optionsVi": {
            "A": "Họ đã tăng giá cho tất cả khách hàng.",
            "B": "Họ đã điều chỉnh lịch trình giao hàng.",
            "C": "Họ cung cấp một vài phương án bữa ăn đa dạng.",
            "D": "Họ có một phó chủ tịch mới."
        },
        "correctAnswer": "C",
        "explanation": "Đoạn văn nêu: 'supplies menus, recipes, and ingredients for two people, four people, or six people, including a range of vegetarian selections. Customers choose the most appropriate meal options...'. Như vậy công ty đem lại nhiều lựa chọn bữa ăn cho khách hàng (offers several meal options). Chọn (C).",
        "vocabulary": [
            { "word": "appropriate", "ipa": "/əˈprəʊ.pri.ət/", "pos": "adj", "meaning": "thích hợp, phù hợp", "example": "Please wear attire appropriate for a formal dinner." }
        ],
        "collocations": [
            { "phrase": "meal options", "meaning": "các lựa chọn bữa ăn" },
            { "phrase": "vegetarian selections", "meaning": "các lựa chọn món ăn chay" }
        ],
        "grammarPoints": [
            { "title": "Cách dùng từ 'several'", "content": "'several meal options' bao gồm các gói khẩu phần (2, 4, 6 người) và món chay (vegetarian)." }
        ]
    },
    {
        "id": 179,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_11",
        "passageTitle": "Press Release & Review: Kitchen Swifts and Chef Darius Cordero",
        "passageType": "Double Passage",
        "pageImages": ["assets/images/rc_page_20.png", "assets/images/rc_page_21.png"],
        "passageText": "The award-winning chef is the owner of restaurants in both the Philippines and Australia, including the recently opened Enriqua's.\n...\nhttps://www.sydneyrestaurants.com.au\nA colleague arranged for us to eat at Enriqua's while I was at a conference in Sydney... We had a wonderful lunch there instead. Everything was delicious... — Meili Guan",
        "passageTextVi": "Bếp trưởng từng đoạt giải là chủ sở hữu các nhà hàng... bao gồm Enriqua's mới khai trương.\nĐánh giá của Meili Guan: Một đồng nghiệp đã sắp xếp cho chúng tôi ăn tại Enriqua's...",
        "questionText": "What is most likely true about Ms. Guan?",
        "questionTextVi": "Điều gì nhiều khả năng là đúng nhất về cô Guan?",
        "options": {
            "A": "She went to Mr. Cordero's restaurant.",
            "B": "She recently went to Sydney for a vacation.",
            "C": "She is a colleague of Ms. Chambers.",
            "D": "She regularly orders from Kitchen Swifts."
        },
        "optionsVi": {
            "A": "Cô ấy đã đến dùng bữa tại nhà hàng của ông Cordero.",
            "B": "Gần đây cô ấy đã đến Sydney để đi nghỉ mát.",
            "C": "Cô ấy là đồng nghiệp của bà Chambers.",
            "D": "Cô ấy thường xuyên đặt hàng từ Kitchen Swifts."
        },
        "correctAnswer": "A",
        "explanation": "Đoạn 1 của bài thông cáo báo chí cho biết Chef Darius Cordero là chủ nhân nhà hàng Enriqua's mới mở tại Sydney ('owner of restaurants... including the recently opened Enriqua's'). Trong bài đánh giá, cô Meili Guan chia sẻ: 'A colleague arranged for us to eat at Enriqua's... We had a wonderful lunch there'. Như vậy cô Guan đã đến ăn tại nhà hàng của ông Cordero (went to Mr. Cordero's restaurant). Chọn (A).",
        "vocabulary": [
            { "word": "on-site", "ipa": "/ˌɒnˈsaɪt/", "pos": "adv, adj", "meaning": "tại chỗ, ngay tại địa điểm", "example": "Bread is baked fresh on-site every morning." }
        ],
        "collocations": [
            { "phrase": "arrange for someone to", "meaning": "sắp xếp cho ai làm gì" },
            { "phrase": "worthwhile treat", "meaning": "món quà / bữa thưởng thức đáng giá" }
        ],
        "grammarPoints": [
            { "title": "Câu hỏi liên kết thông tin 2 đoạn (Cross-text Reference)", "content": "Liên kết chi tiết chủ sở hữu Enriqua's ở Đoạn 1 với bài review trải nghiệm ăn tại Enriqua's ở Đoạn 2." }
        ]
    },
    {
        "id": 180,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_11",
        "passageTitle": "Press Release & Review: Kitchen Swifts and Chef Darius Cordero",
        "passageType": "Double Passage",
        "pageImages": ["assets/images/rc_page_20.png", "assets/images/rc_page_21.png"],
        "passageText": "It is usually fully booked for dinner; you may need to call months in advance for a table. We had a wonderful lunch there instead.",
        "passageTextVi": "Nơi này thường kín chỗ hoàn toàn cho bữa tối; bạn có thể phải gọi điện trước nhiều tháng để đặt bàn...",
        "questionText": "What did Ms. Guan suggest about Enriqua's in the review?",
        "questionTextVi": "Cô Guan gợi ý điều gì về nhà hàng Enriqua's trong bài đánh giá?",
        "options": {
            "A": "It has a limited lunch menu.",
            "B": "It takes dinner reservations.",
            "C": "It serves bread from a local bakery.",
            "D": "It has a location in Hong Kong."
        },
        "optionsVi": {
            "A": "Nó có thực đơn bữa trưa hạn chế.",
            "B": "Nó nhận đặt bàn trước cho bữa tối.",
            "C": "Nó phục vụ bánh mì từ một tiệm bánh địa phương.",
            "D": "Nó có một chi nhánh ở Hồng Kông."
        },
        "correctAnswer": "B",
        "explanation": "Cô Guan viết: 'It is usually fully booked for dinner; you may need to call months in advance for a table' (Nó thường kín chỗ cho bữa tối; bạn có thể phải gọi trước nhiều tháng để có bàn). Chi tiết 'call months in advance for a table' chứng minh nhà hàng có nhận đặt bàn trước cho bữa tối (It takes dinner reservations). Chọn (B).",
        "vocabulary": [
            { "word": "reservation", "ipa": "/ˌrez.əˈveɪ.ʃən/", "pos": "n", "meaning": "sự đặt chỗ trước", "example": "I'd like to make a table reservation for four at 7 PM." },
            { "word": "fully booked", "ipa": "/ˌfʊl.i ˈbʊkt/", "pos": "adj", "meaning": "kín chỗ, hết chỗ", "example": "The hotel is fully booked for the holiday weekend." }
        ],
        "collocations": [
            { "phrase": "dinner reservation", "meaning": "sự đặt chỗ ăn tối" },
            { "phrase": "fully booked", "meaning": "hết chỗ ngồi / phòng" }
        ],
        "grammarPoints": [
            { "title": "Paraphrase cụm 'call in advance for a table'", "content": "'call in advance for a table' được diễn đạt bằng danh từ 'take reservations'." }
        ]
    },

    # 181 - 185 (Double Passage: Laura Savard & Conor Boyle)
    {
        "id": 181,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_12",
        "passageTitle": "E-mail & Ferry Ticket: Conor Boyle and Laura Savard",
        "passageType": "Double Passage",
        "pageImages": ["assets/images/rc_page_22.png", "assets/images/rc_page_23.png"],
        "passageText": "To: laura.savard@orbitmail.scot\nFrom: cboyle@ceoleire.co.uk\nDate: 25 May\nSubject: RE: Some suggestions\n\nDear Ms. Savard,\nThank you for your kind offer to either pick up your online order from my shop or to pay extra for air or train transport. Neither arrangement is necessary, as I am happy to deliver your items to you in Stranraer myself. It so happens that my sister and her children live nearby in Kirkcolm. Before seeing them, I will drive my rental car to your house and hand deliver the items to you.\nAs you know, my merchandise is 100 percent handcrafted. If any damage occurs in transit, the repair turns into an expensive, time-consuming ordeal. Over the years, I've seen too much damage done by inattentive baggage handlers. My policy is to deliver items personally whenever feasible or hire a ground- or sea-based courier service I trust.\nI look forward to meeting you on 5 June. I expect to arrive at your house no later than 5 P.M.\n\nSincerely,\nConor Boyle\nCeoleire Classics\n\n---\nNorthern Ireland Ferry Service\nDate of Issuance: 26 May\nPassenger Name: Conor Boyle\nDeparting Belfast: Friday, 5 June, 1:05 PM\nDocking at Cairnryan: Friday, 5 June, 3:20 PM\nBaggage: 1 suitcase (small), 2 instrument cases (1 mandolin, 1 guitar)\nVehicle transport: No\nAdult Standard Class: £55.00\nPlease arrive 30 minutes prior to departure.",
        "passageTextVi": "Đến: laura.savard@orbitmail.scot\nTừ: cboyle@ceoleire.co.uk\nNgày: 25 tháng 5\nTiêu đề: RE: Một vài đề xuất\n\nKính gửi cô Savard,\nCảm ơn lời đề nghị tốt bụng của cô về việc đến cửa hàng của tôi để lấy đơn hàng trực tuyến hoặc trả thêm tiền để vận chuyển bằng máy bay hoặc tàu hỏa. Cả hai cách thu xếp đó đều không cần thiết, vì tôi rất sẵn lòng đích thân tự mình giao hàng tới Stranraer cho cô. Thật trùng hợp là em gái tôi và các con của cô ấy đang sống gần đó ở Kirkcolm. Trước khi đến thăm họ, tôi sẽ lái chiếc xe thuê đến nhà cô và tận tay trao các món đồ cho cô.\nNhư cô đã biết, hàng hóa của tôi được làm thủ công 100%. Nếu có bất kỳ hư hỏng nào xảy ra trong quá trình vận chuyển, việc sửa chữa sẽ trở thành một trải nghiệm vô cùng tốn kém và mất thời gian. Trong nhiều năm qua, tôi đã chứng kiến quá nhiều hư hỏng do nhân viên bốc dỡ hành lý bất cẩn gây ra. Chính sách của tôi là tự mình giao các món đồ bất cứ khi nào khả thi, hoặc thuê một dịch vụ chuyển phát đường bộ hoặc đường biển mà tôi tin tưởng.\nTôi rất mong được gặp cô vào ngày 5 tháng 6. Tôi dự kiến sẽ đến nhà cô muộn nhất là 5 giờ chiều.\n\nTrân trọng,\nConor Boyle\nCeoleire Classics\n\n---\nDịch vụ Phà Bắc Ireland\nNgày phát hành: 26 tháng 5\nTên hành khách: Conor Boyle\nKhởi hành từ Belfast: Thứ Sáu, ngày 5 tháng 6, lúc 1:05 chiều\nCập bến tại Cairnryan: Thứ Sáu, ngày 5 tháng 6, lúc 3:20 chiều\nHành lý: 1 vali (nhỏ), 2 hộp đàn nhạc cụ (1 đàn mandolin, 1 đàn guitar)\nVận chuyển phương tiện xe: Không\nVé tiêu chuẩn người lớn: £55.00\nVui lòng có mặt 30 phút trước giờ khởi hành.",
        "questionText": "What is the purpose of the e-mail?",
        "questionTextVi": "Mục đích của bức email là gì?",
        "options": {
            "A": "To finalize a plan",
            "B": "To accept an invitation",
            "C": "To promote a new service",
            "D": "To request feedback on a policy"
        },
        "optionsVi": {
            "A": "Để chốt / hoàn tất một kế hoạch giao hàng",
            "B": "Để chấp nhận một lời mời",
            "C": "Để quảng bá một dịch vụ mới",
            "D": "Để xin ý kiến phản hồi về một chính sách"
        },
        "correctAnswer": "A",
        "explanation": "Khách hàng Laura Savard đề xuất cách lấy hàng/chuyển hàng, và ông Boyle phản hồi để chốt lại kế hoạch cụ thể: ông sẽ tự tay đem giao lúc nào, ngày nào ('I look forward to meeting you on 5 June. I expect to arrive at your house no later than 5 P.M.'). Do đó mục đích là chốt kế hoạch (To finalize a plan). Chọn (A).",
        "vocabulary": [
            { "word": "handcrafted", "ipa": "/ˌhændˈkrɑːf.tɪd/", "pos": "adj", "meaning": "làm thủ công bằng tay", "example": "She sells handcrafted wooden toys." },
            { "word": "ordeal", "ipa": "/ɔːˈdiːl/", "pos": "n", "meaning": "thử thách khó khăn, trải nghiệm gian nan", "example": "Traveling during the snowstorm was quite an ordeal." }
        ],
        "collocations": [
            { "phrase": "finalize a plan", "meaning": "chốt lại / hoàn tất kế hoạch" },
            { "phrase": "hand deliver", "meaning": "giao tận tay" }
        ],
        "grammarPoints": [
            { "title": "Cấu trúc 'neither... nor...' hoặc 'neither arrangement'", "content": "'Neither arrangement is necessary' dùng 'Neither' cho hai sự lựa chọn phủ định cả hai." }
        ]
    },
    {
        "id": 182,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_12",
        "passageTitle": "E-mail & Ferry Ticket: Conor Boyle and Laura Savard",
        "passageType": "Double Passage",
        "pageImages": ["assets/images/rc_page_22.png", "assets/images/rc_page_23.png"],
        "passageText": "It so happens that my sister and her children live nearby in Kirkcolm. Before seeing them, I will drive my rental car to your house and hand deliver the items to you.",
        "passageTextVi": "Thật trùng hợp là em gái tôi và các con của cô ấy sống gần đó ở Kirkcolm. Trước khi đến thăm họ, tôi sẽ lái xe thuê đến nhà cô...",
        "questionText": "Why will Mr. Boyle travel from Stranraer to Kirkcolm?",
        "questionTextVi": "Tại sao ông Boyle lại đi từ Stranraer đến Kirkcolm?",
        "options": {
            "A": "To make a delivery",
            "B": "To attend a meeting",
            "C": "To drop off a rental car",
            "D": "To visit with family members"
        },
        "optionsVi": {
            "A": "Để giao một chuyến hàng",
            "B": "Để tham dự một cuộc họp",
            "C": "Để trả lại một chiếc xe thuê",
            "D": "Để đến thăm các thành viên trong gia đình"
        },
        "correctAnswer": "D",
        "explanation": "Ông Boyle viết: 'my sister and her children live nearby in Kirkcolm' (em gái tôi và các cháu sống gần đó ở Kirkcolm). Sau khi giao hàng ở Stranraer, ông đến Kirkcolm để gặp họ. Em gái và các cháu là các thành viên gia đình (family members). Do đó chọn (D) 'To visit with family members'.",
        "vocabulary": [
            { "word": "nearby", "ipa": "/ˌnɪəˈbaɪ/", "pos": "adv, adj", "meaning": "ở gần, gần đó", "example": "We stopped at a nearby gas station." }
        ],
        "collocations": [
            { "phrase": "visit with family members", "meaning": "đến thăm các thành viên gia đình" },
            { "phrase": "rental car", "meaning": "xe ô tô thuê" }
        ],
        "grammarPoints": [
            { "title": "Paraphrase quan hệ gia đình", "content": "'sister and her children' -> 'family members'." }
        ]
    },
    {
        "id": 183,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_12",
        "passageTitle": "E-mail & Ferry Ticket: Conor Boyle and Laura Savard",
        "passageType": "Double Passage",
        "pageImages": ["assets/images/rc_page_22.png", "assets/images/rc_page_23.png"],
        "passageText": "Over the years, I've seen too much damage done by inattentive baggage handlers. My policy is to deliver items personally whenever feasible or hire a ground- or sea-based courier service I trust.",
        "passageTextVi": "Trong nhiều năm qua, tôi đã chứng kiến quá nhiều hư hại do nhân viên bốc xếp hành lý bất cẩn gây ra. Chính sách của tôi là tự mình giao... hoặc thuê dịch vụ vận chuyển đường bộ hoặc đường biển...",
        "questionText": "What is indicated in the e-mail?",
        "questionTextVi": "Điều gì được chỉ ra trong email?",
        "options": {
            "A": "Mr. Boyle's sister is a cofounder of Ceoleire Classics.",
            "B": "Mr. Boyle has been disappointed by air- and train-freight companies.",
            "C": "Ms. Savard has purchased items from Mr. Boyle in the past.",
            "D": "Ms. Savard prefers a specific brand of luggage."
        },
        "optionsVi": {
            "A": "Em gái của ông Boyle là người đồng sáng lập Ceoleire Classics.",
            "B": "Ông Boyle từng thất vọng với các công ty vận tải hàng không và đường sắt.",
            "C": "Cô Savard từng mua hàng của ông Boyle trong quá khứ.",
            "D": "Cô Savard ưa chuộng một thương hiệu hành lý cụ thể."
        },
        "correctAnswer": "B",
        "explanation": "Khách đề nghị trả thêm tiền gửi máy bay hoặc tàu hỏa ('pay extra for air or train transport'), nhưng ông Boyle từ chối vì: 'Over the years, I've seen too much damage done by inattentive baggage handlers' (Nhiều năm qua tôi đã thấy quá nhiều hư hỏng do nhân viên bốc dỡ gây ra) nên ông tránh gửi đường hàng không hay tàu hỏa. Điều này chứng tỏ ông đã từng rất thất vọng với dịch vụ vận tải hàng không và đường sắt (has been disappointed by air- and train-freight companies). Chọn (B).",
        "vocabulary": [
            { "word": "inattentive", "ipa": "/ˌɪn.əˈten.tɪv/", "pos": "adj", "meaning": "thiếu chú ý, bất cẩn", "example": "Inattentive driving leads to accidents." },
            { "word": "freight", "ipa": "/freɪt/", "pos": "n", "meaning": "hàng hóa chuyên chở, cước vận chuyển", "example": "The goods were sent by air freight." }
        ],
        "collocations": [
            { "phrase": "baggage handlers", "meaning": "nhân viên bốc dỡ hành lý" },
            { "phrase": "in transit", "meaning": "trong quá trình vận chuyển" }
        ],
        "grammarPoints": [
            { "title": "Bị động với 'damage done by'", "content": "Rút gọn mệnh đề quan hệ dạng bị động: 'damage (which was) done by inattentive baggage handlers'." }
        ]
    },
    {
        "id": 184,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_12",
        "passageTitle": "E-mail & Ferry Ticket: Conor Boyle and Laura Savard",
        "passageType": "Double Passage",
        "pageImages": ["assets/images/rc_page_22.png", "assets/images/rc_page_23.png"],
        "passageText": "Baggage: 1 suitcase (small), 2 instrument cases (1 mandolin, 1 guitar)",
        "passageTextVi": "Hành lý mang theo: 1 vali (nhỏ), 2 hộp đàn nhạc cụ (1 mandolin, 1 guitar)",
        "questionText": "What is most likely true about Ms. Savard?",
        "questionTextVi": "Điều gì nhiều khả năng là đúng nhất về cô Savard?",
        "options": {
            "A": "She often travels for her job.",
            "B": "She paid extra to have items hand delivered.",
            "C": "She recently purchased musical instruments.",
            "D": "She will meet Mr. Boyle at the rental car office."
        },
        "optionsVi": {
            "A": "Cô ấy thường xuyên đi lại vì công việc.",
            "B": "Cô ấy đã trả thêm tiền để được giao hàng tận tay.",
            "C": "Gần đây cô ấy đã mua các loại nhạc cụ.",
            "D": "Cô ấy sẽ gặp ông Boyle tại văn phòng cho thuê xe."
        },
        "correctAnswer": "C",
        "explanation": "Email nêu ông Boyle đang tự tay mang đơn hàng của cô Savard đi giao ('deliver your items to you'). Vé phà của ông Boyle ghi rõ hành lý ông mang theo gồm: '2 instrument cases (1 mandolin, 1 guitar)'. Như vậy các món đồ cô Savard đặt mua chính là nhạc cụ (musical instruments). Chọn (C).",
        "vocabulary": [
            { "word": "instrument", "ipa": "/ˈɪn.strə.mənt/", "pos": "n", "meaning": "nhạc cụ (hoặc dụng cụ)", "example": "She plays several traditional musical instruments." },
            { "word": "mandolin", "ipa": "/ˌmæn.dəˈlɪn/", "pos": "n", "meaning": "đàn măng-đô-lin", "example": "He played a cheerful melody on the mandolin." }
        ],
        "collocations": [
            { "phrase": "musical instruments", "meaning": "các loại nhạc cụ" },
            { "phrase": "instrument cases", "meaning": "hộp đựng nhạc cụ" }
        ],
        "grammarPoints": [
            { "title": "Câu hỏi nối thông tin 2 văn bản (Double Passage Cross-check)", "content": "Đối chiếu: 'deliver your items' (Email) + '2 instrument cases: 1 mandolin, 1 guitar' (Ticket) -> Món hàng mua là nhạc cụ." }
        ]
    },
    {
        "id": 185,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_12",
        "passageTitle": "E-mail & Ferry Ticket: Conor Boyle and Laura Savard",
        "passageType": "Double Passage",
        "pageImages": ["assets/images/rc_page_22.png", "assets/images/rc_page_23.png"],
        "passageText": "Northern Ireland Ferry Service\nDate of Issuance: 26 May\nPassenger Name: Conor Boyle\nDeparting Belfast: Friday, 5 June, 1:05 PM\nDocking at Cairnryan: Friday, 5 June, 3:20 PM",
        "passageTextVi": "Dịch vụ Phà Bắc Ireland\nKhởi hành từ Belfast: Thứ Sáu, ngày 5 tháng 6 lúc 1:05 chiều\nCập bến tại Cairnryan: Thứ Sáu, ngày 5 tháng 6 lúc 3:20 chiều",
        "questionText": "How is Mr. Boyle traveling to Cairnryan on June 5?",
        "questionTextVi": "Ông Boyle di chuyển đến Cairnryan vào ngày 5 tháng 6 bằng phương tiện gì?",
        "options": {
            "A": "By car",
            "B": "By train",
            "C": "By boat",
            "D": "By plane"
        },
        "optionsVi": {
            "A": "Bằng xe ô tô",
            "B": "Bằng tàu hỏa",
            "C": "Bằng thuyền / phà",
            "D": "Bằng máy bay"
        },
        "correctAnswer": "C",
        "explanation": "Vé của ông ghi rõ dịch vụ là 'Northern Ireland Ferry Service' (Dịch vụ Phà Bắc Ireland) và hành trình 'Departing Belfast... Docking at Cairnryan' (khởi hành từ Belfast, cập cảng tại Cairnryan). Phà (ferry) là một loại tàu thuyền (boat). Do đó chọn (C) 'By boat'.",
        "vocabulary": [
            { "word": "ferry", "ipa": "/ˈfer.i/", "pos": "n", "meaning": "phà, tàu thủy chở khách", "example": "We took the overnight ferry across the channel." },
            { "word": "dock", "ipa": "/dɒk/", "pos": "v", "meaning": "cập bến, cập cảng", "example": "The cruise ship docked in Singapore at dawn." }
        ],
        "collocations": [
            { "phrase": "ferry service", "meaning": "dịch vụ phà chuyên chở" },
            { "phrase": "dock at a port", "meaning": "cập cảng" }
        ],
        "grammarPoints": [
            { "title": "Giới từ chỉ phương tiện 'by + vehicle'", "content": "Sử dụng 'by boat / by car / by plane' để nói về phương thức di chuyển." }
        ]
    },

    # 186 - 190 (Triple Passage: TTA Advertisement, Forum Post, Bakery Outline)
    {
        "id": 186,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_13",
        "passageTitle": "Ad, Forum & Outline: Train to Achieve (TTA)",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_24.png", "assets/images/rc_page_25.png"],
        "passageText": "Train to Achieve (TTA)—Our classes prepare you to succeed!\nProfiled in the latest Business Directions Nigeria newsletter, Train to Achieve (TTA) is one of the most innovative training providers in West Africa. By offering our classes entirely in online format, we bring the classroom to your home. All classes include individualized instruction and are taught by recognized professionals in their respective fields. Upon successful completion of a class, you will receive an official Certificate of Training, a valuable addition to any résumé. For a complete list of class fees and schedules, visit our Web site at www.traintoachieve.org.ng.\nThe following are some of our most popular classes:\n- Introduction to Social Media Marketing (TTA1504): Taught by marketing consultant Marcus Akpan, the class equips you with the know-how to promote your business online.\n- Become a Successful Freelance Writer (TTA3283): Business writer Brenda Akande gives you expert guidance on how to hone your writing skills and sell your writing services.\n- Starting an Internet Radio Station (TTA7629): Online radio host Natalie Kabiru shows you how to appeal to your target market and gives practical tips for setting up your broadcast service.\n- Basics of Graphic Design (TTA7633): Veteran graphic designer Doug Umaru helps you acquire the basic skills needed to start a graphic design business.\n\n---\nDiscussion forum for students enrolled in Train to Achieve Class TTA1504\nPosted on: 21 May, 9:41 A.M.\nPosted by: Joseph Egbe\nSubject: Presentations\nViewing the list of students enrolled in this class, I remembered chatting with some of you on the forum for January's poster design class. I look forward to sharing our learning experiences again for this class.\nYesterday I was the second student to meet with Mr. Akpan for an individual videoconference about my business. I own a food truck from which I sell baked goods, and when I shared with Mr. Akpan the outline for my Web site, he suggested that I add a section with vivid images of all my baked goods. It was helpful advice.\n\n---\nEgbe's Bakery—Unique baked-in flavours in every bite!\nSection 1: Explore our menu and price list\nSection 2: Browse photos of our delicious treats\nSection 3: Learn about our catering services\nSection 4: View lists of ingredients",
        "passageTextVi": "Train to Achieve (TTA)—Các lớp học của chúng tôi chuẩn bị cho bạn thành công!\nĐược giới thiệu trong bản tin Business Directions Nigeria mới nhất, Train to Achieve (TTA) là một trong những nhà cung cấp dịch vụ đào tạo sáng tạo nhất ở Tây Phi. Bằng cách cung cấp các lớp học hoàn toàn dưới hình thức trực tuyến, chúng tôi mang lớp học đến tận nhà bạn. Tất cả các lớp học đều bao gồm hướng dẫn cá nhân hóa và được giảng dạy bởi các chuyên gia được công nhận trong các lĩnh vực tương ứng. Sau khi hoàn thành xuất sắc một lớp học, bạn sẽ nhận được Chứng chỉ Đào tạo chính thức, một điểm cộng quý giá cho bất kỳ hồ sơ xin việc nào. Để biết danh sách đầy đủ về học phí và lịch học, hãy truy cập trang web của chúng tôi tại www.traintoachieve.org.ng.\nDưới đây là một số lớp học phổ biến nhất của chúng tôi:\n- Nhập môn Tiếp thị Truyền thông Xã hội (TTA1504): Do chuyên gia tư vấn tiếp thị Marcus Akpan giảng dạy, lớp học trang bị cho bạn bí quyết quảng bá doanh nghiệp trực tuyến.\n- Trở thành Người viết tự do Thành công (TTA3283): Nhà văn kinh doanh Brenda Akande cung cấp cho bạn hướng dẫn chuyên môn về cách mài giũa kỹ năng viết và bán dịch vụ viết của mình.\n- Bắt đầu một Đài Phát thanh Internet (TTA7629): Người dẫn chương trình phát thanh trực tuyến Natalie Kabiru chỉ cho bạn cách thu hút thị trường mục tiêu và đưa ra các mẹo thực tế để thiết lập dịch vụ phát sóng của bạn.\n- Cơ bản về Thiết kế Đồ họa (TTA7633): Nhà thiết kế đồ họa kỳ cựu Doug Umaru giúp bạn có được những kỹ năng cơ bản cần thiết để bắt đầu kinh doanh thiết kế đồ họa.\n\n---\nDiễn đàn thảo luận dành cho học viên lớp TTA1504 của Train to Achieve\nĐăng ngày: 21 tháng 5, 9:41 sáng\nNgười đăng: Joseph Egbe\nChủ đề: Bài thuyết trình\nKhi xem danh sách học viên đăng ký lớp học này, tôi nhớ lại từng trò chuyện với một số bạn trên diễn đàn của lớp thiết kế áp phích vào tháng Giêng. Tôi rất mong được chia sẻ lại những trải nghiệm học tập của chúng ta trong lớp học này.\nHôm qua tôi là học viên thứ hai gặp thầy Akpan để họp trực tuyến riêng về doanh nghiệp của mình. Tôi sở hữu một chiếc xe tải bán đồ ăn nướng bánh ngọt, và khi tôi chia sẻ với thầy Akpan dàn ý cho trang web của mình, thầy đã đề xuất tôi nên thêm một phần với những hình ảnh sống động về tất cả các món bánh nướng của tôi. Đó là một lời khuyên vô cùng hữu ích.\n\n---\nEgbe's Bakery—Hương vị nướng độc đáo trong từng miếng bánh!\nPhần 1: Khám phá thực đơn và bảng giá của chúng tôi\nPhần 2: Xem ảnh các món bánh thơm ngon của chúng tôi\nPhần 3: Tìm hiểu về dịch vụ tiệc lưu động của chúng tôi\nPhần 4: Xem danh sách thành phần nguyên liệu",
        "questionText": "What is indicated about TTA?",
        "questionTextVi": "Điều gì được chỉ ra về tổ chức TTA?",
        "options": {
            "A": "It was founded by a graphic designer.",
            "B": "It publishes its own online newsletter.",
            "C": "It offers classes led by industry professionals.",
            "D": "It has classroom facilities in cities across West Africa."
        },
        "optionsVi": {
            "A": "Nó được thành lập bởi một nhà thiết kế đồ họa.",
            "B": "Nó xuất bản bản tin trực tuyến của riêng mình.",
            "C": "Nó cung cấp các lớp học do các chuyên gia trong ngành dẫn dắt.",
            "D": "Nó có các phòng học cơ sở vật chất ở các thành phố khắp Tây Phi."
        },
        "correctAnswer": "C",
        "explanation": "Đoạn 1 nêu rõ: 'All classes include individualized instruction and are taught by recognized professionals in their respective fields' (Tất cả các lớp học... được giảng dạy bởi các chuyên gia được công nhận trong các lĩnh vực tương ứng). 'taught by recognized professionals' tương đương với 'offers classes led by industry professionals'. Do đó chọn (C).",
        "vocabulary": [
            { "word": "individualized", "ipa": "/ˌɪn.dɪˈvɪdʒ.u.ə.laɪzd/", "pos": "adj", "meaning": "cá nhân hóa, riêng biệt cho từng người", "example": "Students benefit from individualized learning plans." },
            { "word": "respective", "ipa": "/rɪˈspek.tɪv/", "pos": "adj", "meaning": "tương ứng, riêng từng người", "example": "They returned to their respective desks." }
        ],
        "collocations": [
            { "phrase": "industry professionals", "meaning": "các chuyên gia trong ngành" },
            { "phrase": "individualized instruction", "meaning": "sự hướng dẫn theo sát từng cá nhân" }
        ],
        "grammarPoints": [
            { "title": "Cấu trúc bị động chỉ người giảng dạy", "content": "'are taught by recognized professionals' -> 'led by industry professionals'." }
        ]
    },
    {
        "id": 187,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_13",
        "passageTitle": "Ad, Forum & Outline: Train to Achieve (TTA)",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_24.png", "assets/images/rc_page_25.png"],
        "passageText": "Upon successful completion of a class, you will receive an official Certificate of Training, a valuable addition to any résumé.",
        "passageTextVi": "Sau khi hoàn thành xuất sắc một lớp học, bạn sẽ nhận được Chứng chỉ Đào tạo chính thức, một sự bổ sung giá trị cho bất kỳ bản sơ yếu lý lịch nào.",
        "questionText": "According to the advertisement, what does TTA provide to students who finish a class?",
        "questionTextVi": "Theo bài quảng cáo, TTA cung cấp điều gì cho các học viên hoàn thành một khóa học?",
        "options": {
            "A": "A résumé-writing workshop",
            "B": "A discount on a follow-up class",
            "C": "A list of current job postings",
            "D": "A certification document"
        },
        "optionsVi": {
            "A": "Một buổi hội thảo hướng dẫn viết sơ yếu lý lịch",
            "B": "Một khoản giảm giá cho khóa học tiếp theo",
            "C": "Danh sách các tin tuyển dụng việc làm hiện tại",
            "D": "Một tài liệu / văn bằng chứng nhận"
        },
        "correctAnswer": "D",
        "explanation": "Quảng cáo ghi rõ: 'Upon successful completion of a class, you will receive an official Certificate of Training' (Sau khi hoàn thành xuất sắc, bạn sẽ nhận được một Chứng chỉ Đào tạo chính thức). 'Certificate of Training' chính là một tài liệu chứng nhận (A certification document). Chọn (D).",
        "vocabulary": [
            { "word": "certificate", "ipa": "/səˈtɪf.ɪ.kət/", "pos": "n", "meaning": "chứng chỉ, giấy chứng nhận", "example": "He received a certificate in digital marketing." },
            { "word": "completion", "ipa": "/kəmˈpliː.ʃən/", "pos": "n", "meaning": "sự hoàn thành", "example": "Bonus payments are awarded upon project completion." }
        ],
        "collocations": [
            { "phrase": "certificate of training", "meaning": "chứng chỉ đào tạo" },
            { "phrase": "upon successful completion", "meaning": "khi hoàn thành thành công" }
        ],
        "grammarPoints": [
            { "title": "Cụm giới từ 'Upon + Noun'", "content": "'Upon + Noun/V-ing' có nghĩa là 'ngay sau khi / vào lúc'." }
        ]
    },
    {
        "id": 188,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_13",
        "passageTitle": "Ad, Forum & Outline: Train to Achieve (TTA)",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_24.png", "assets/images/rc_page_25.png"],
        "passageText": "Discussion forum for students enrolled in Train to Achieve Class TTA1504\nPosted on: 21 May, 9:41 A.M.\nPosted by: Joseph Egbe\nSubject: Presentations\nViewing the list of students enrolled in this class, I remembered chatting with some of you on the forum for January's poster design class. I look forward to sharing our learning experiences again for this class.",
        "passageTextVi": "...Tôi nhớ lại từng trò chuyện với một số bạn trên diễn đàn của lớp học thiết kế áp phích vào tháng Giêng. Tôi rất mong được tiếp tục chia sẻ kinh nghiệm học tập của chúng ta trong lớp này.",
        "questionText": "What is most likely true about Mr. Egbe?",
        "questionTextVi": "Điều gì nhiều khả năng là đúng nhất về ông Egbe?",
        "options": {
            "A": "He helped design a discussion forum.",
            "B": "He has previously taken a TTA class.",
            "C": "He develops videoconferencing software.",
            "D": "He recently sold a bakery food truck."
        },
        "optionsVi": {
            "A": "Ông ấy đã giúp thiết kế một diễn đàn thảo luận.",
            "B": "Trước đây ông ấy đã từng tham gia một lớp học của TTA.",
            "C": "Ông ấy phát triển phần mềm hội nghị truyền hình.",
            "D": "Gần đây ông ấy đã bán một chiếc xe tải bán bánh mì."
        },
        "correctAnswer": "B",
        "explanation": "Ông Egbe viết: 'I remembered chatting with some of you on the forum for January's poster design class' (Tôi nhớ lại việc từng trò chuyện với một số bạn trên diễn đàn lớp thiết kế áp phích hồi tháng Giêng). Điều này chứng minh trước đây ông đã từng theo học một lớp của TTA (has previously taken a TTA class). Do đó chọn (B).",
        "vocabulary": [
            { "word": "previously", "ipa": "/ˈpriː.vi.əs.li/", "pos": "adv", "meaning": "trước đây", "example": "She was previously employed as a graphic designer." }
        ],
        "collocations": [
            { "phrase": "enrolled in a class", "meaning": "đăng ký theo học một lớp" },
            { "phrase": "learning experiences", "meaning": "những trải nghiệm học tập" }
        ],
        "grammarPoints": [
            { "title": "Thì Hiện tại Hoàn thành suy luận kinh nghiệm", "content": "'has previously taken' thể hiện trải nghiệm đã từng diễn ra trong quá khứ." }
        ]
    },
    {
        "id": 189,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_13",
        "passageTitle": "Ad, Forum & Outline: Train to Achieve (TTA)",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_24.png", "assets/images/rc_page_25.png"],
        "passageText": "Ad: Introduction to Social Media Marketing (TTA1504): Taught by marketing consultant Marcus Akpan, the class equips you with the know-how to promote your business online.\n---\nForum: Discussion forum for students enrolled in Train to Achieve Class TTA1504\nPosted by: Joseph Egbe",
        "passageTextVi": "Quảng cáo: Nhập môn Tiếp thị Truyền thông Xã hội (mã lớp: TTA1504) giảng dạy bởi Marcus Akpan...\nDiễn đàn: Diễn đàn thảo luận cho học viên lớp TTA1504. Người đăng: Joseph Egbe",
        "questionText": "What TTA class is Mr. Egbe enrolled in?",
        "questionTextVi": "Ông Egbe đang đăng ký theo học lớp nào của TTA?",
        "options": {
            "A": "Introduction to Social Media Marketing",
            "B": "Become a Successful Freelance Writer",
            "C": "Starting an Internet Radio Station",
            "D": "Basics of Graphic Design"
        },
        "optionsVi": {
            "A": "Nhập môn Tiếp thị Truyền thông Xã hội",
            "B": "Trở thành Người viết tự do Thành công",
            "C": "Bắt đầu một Đài Phát thanh Internet",
            "D": "Cơ bản về Thiết kế Đồ họa"
        },
        "correctAnswer": "A",
        "explanation": "Đoạn 2 là bài đăng của Joseph Egbe trên diễn đàn: 'Discussion forum for students enrolled in Train to Achieve Class TTA1504'. Đối chiếu với Đoạn 1, lớp 'TTA1504' chính là 'Introduction to Social Media Marketing'. Chọn (A).",
        "vocabulary": [
            { "word": "enroll", "ipa": "/ɪnˈrəʊl/", "pos": "v", "meaning": "ghi danh, đăng ký học", "example": "More than 200 students enrolled in the online course." },
            { "word": "consultant", "ipa": "/kənˈsʌl.tənt/", "pos": "n", "meaning": "chuyên gia tư vấn", "example": "He works as an independent marketing consultant." }
        ],
        "collocations": [
            { "phrase": "social media marketing", "meaning": "tiếp thị truyền thông xã hội" },
            { "phrase": "enrolled in", "meaning": "đăng ký vào lớp..." }
        ],
        "grammarPoints": [
            { "title": "Nối mã số khóa học (Cross-referencing Course Codes)", "content": "Khớp mã định danh 'TTA1504' giữa bài quảng cáo và tiêu đề diễn đàn học viên." }
        ]
    },
    {
        "id": 190,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_13",
        "passageTitle": "Ad, Forum & Outline: Train to Achieve (TTA)",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_24.png", "assets/images/rc_page_25.png"],
        "passageText": "Forum: ...when I shared with Mr. Akpan the outline for my Web site, he suggested that I add a section with vivid images of all my baked goods. It was helpful advice.\n---\nOutline:\nEgbe's Bakery—Unique baked-in flavours in every bite!\nSection 1: Explore our menu and price list\nSection 2: Browse photos of our delicious treats\nSection 3: Learn about our catering services\nSection 4: View lists of ingredients",
        "passageTextVi": "Diễn đàn: ...khi tôi chia sẻ với thầy Akpan dàn ý trang web của mình, thầy gợi ý tôi nên thêm một phần có những hình ảnh sống động về tất cả các món bánh nướng của tôi.\nDàn ý:\nPhần 1: Khám phá thực đơn và bảng giá\nPhần 2: Xem ảnh các món bánh thơm ngon\nPhần 3: Tìm hiểu dịch vụ tiệc lưu động\nPhần 4: Xem danh sách thành phần",
        "questionText": "What section did Mr. Egbe most likely add to the outline after speaking with Mr. Akpan?",
        "questionTextVi": "Ông Egbe nhiều khả năng đã thêm phần nào vào dàn ý sau khi trao đổi với ông Akpan?",
        "options": {
            "A": "Section 1",
            "B": "Section 2",
            "C": "Section 3",
            "D": "Section 4"
        },
        "optionsVi": {
            "A": "Phần 1",
            "B": "Phần 2",
            "C": "Phần 3",
            "D": "Phần 4"
        },
        "correctAnswer": "B",
        "explanation": "Trong bài viết diễn đàn, ông Egbe cho biết thầy Akpan khuyên ông nên thêm một mục chứa 'vivid images of all my baked goods' (những bức ảnh sống động về các món bánh). Khi xem dàn ý trang web ở Văn bản 3, mục 'Section 2: Browse photos of our delicious treats' (Xem các bức ảnh về món ngon) hoàn toàn khớp với lời khuyên này. Do đó phần được thêm vào là Section 2. Chọn (B).",
        "vocabulary": [
            { "word": "vivid", "ipa": "/ˈvɪv.ɪd/", "pos": "adj", "meaning": "sống động, rực rỡ sắc nét", "example": "The brochure features vivid photographs of the resort." },
            { "word": "treat", "ipa": "/triːt/", "pos": "n", "meaning": "món ăn ngon đặc biệt, đồ ngọt", "example": "The bakery serves sweet treats like cookies and tarts." }
        ],
        "collocations": [
            { "phrase": "browse photos", "meaning": "lướt xem ảnh" },
            { "phrase": "vivid images", "meaning": "hình ảnh sống động" }
        ],
        "grammarPoints": [
            { "title": "Paraphrase từ vựng Triple Passage", "content": "'vivid images of baked goods' (Forum) -> 'Browse photos of our delicious treats' (Section 2)." }
        ]
    },

    # 191 - 195 (Triple Passage: Orange Bay Kitchen)
    {
        "id": 191,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_14",
        "passageTitle": "Article, Review & E-mail: Orange Bay Kitchen",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_26.png", "assets/images/rc_page_27.png"],
        "passageText": "Caribbean Flavours Abound\nBy Rebecca Roats\nNOTTINGHAM (15 August)—Orange Bay Kitchen has been serving up an infusion of Jamaican flavours in a laid-back Caribbean atmosphere for six months now. Managed by Keron Deslandes, the 150-seat restaurant is an aromatic jewel amid the bustling shops and eateries in Wester Square. The servers are always happy to help diners select from the variety of delights on the extensive menu, which includes curried goat, oxtail soup, and red snapper. The restaurant is most famous for its jerk chicken. Marinated for 24 hours prior to grilling and served with sides of stewed cabbage and coconut rice, the dish is a good deal at £12. If you stop in on any Friday night between 7 and 11 P.M., you will enjoy live reggae music.\n\n---\nhttps://www.dinerreviews.co.uk/orangebaykitchen\nPosted on 22 August by Tamika Peterkin, tpeterkin@sunmail.co.uk\nOrange Bay Kitchen: 2/5 Stars\nAfter reading a glowing article about Orange Bay Kitchen by Rebecca Roats, I was eager to give this place a try. My husband and I arrived there at 7 P.M. yesterday, keen to enjoy live music with our dinner. Unfortunately, the band's performance that night had been cancelled. Undeterred, we stayed and both ordered the jerk chicken. While the chicken's smoky flavour was outstanding, the stewed cabbage was lacking in flavour. Also, the portion size was smaller than we had anticipated, so we ordered another appetiser to avoid going home hungry. The head chef came out to apologise and was extremely nice, but we will probably not go back anytime soon.\n\n---\nFrom: vsmith@orangebaykitchen.co.uk\nTo: tpeterkin@sunmail.co.uk\nDate: 24 August\nSubject: Your review\nAttachment: Gift Certificate 0258\n\nDear Ms. Peterkin,\nThank you for visiting Orange Bay Kitchen and leaving a review. Our manager, Keron Deslandes, told me more about your visit and our failure to live up to your expectations that evening. Please accept the attached £20 gift certificate; I do hope that you will give us another try.\nDuring your visit, our band had an equipment malfunction, which is what led to the last-minute cancellation. However, the band will be back performing weekly beginning in September. Also, I want you to know that Head Chef Adio Brown has changed the spices he uses in the stewed cabbage. I am sure you will find them delightful.\n\nSincerely,\nVea Smith, Owner\nOrange Bay Kitchen",
        "passageTextVi": "Hương vị Caribe Ngập tràn\nBởi Rebecca Roats\nNOTTINGHAM (15 tháng 8)—Orange Bay Kitchen đã phục vụ sự hòa quyện của các hương vị Jamaica trong một không gian Caribe thư thái được sáu tháng nay. Do Keron Deslandes quản lý, nhà hàng 150 chỗ ngồi này là một viên ngọc thơm ngát giữa các cửa hàng và quán ăn nhộn nhịp ở Quảng trường Wester. Các nhân viên phục vụ luôn sẵn lòng giúp thực khách lựa chọn từ vô số món ngon trong thực đơn phong phú, bao gồm dê cà ri, súp đuôi bò và cá hồng. Nhà hàng nổi tiếng nhất với món gà nướng jerk. Được ướp trong 24 giờ trước khi nướng và phục vụ kèm với bắp cải hầm cùng cơm dừa, món ăn này là một món hời với giá £12. Nếu bạn ghé qua vào bất kỳ tối thứ Sáu nào từ 7 đến 11 giờ đêm, bạn sẽ được thưởng thức nhạc reggae sống.\n\n---\nhttps://www.dinerreviews.co.uk/orangebaykitchen\nĐăng ngày 22 tháng 8 bởi Tamika Peterkin, tpeterkin@sunmail.co.uk\nOrange Bay Kitchen: 2/5 Sao\nSau khi đọc một bài báo ca ngợi về Orange Bay Kitchen của tác giả Rebecca Roats, tôi đã rất háo hức muốn thử nơi này. Chồng tôi và tôi đã đến đó vào lúc 7 giờ tối hôm qua, mong muốn được thưởng thức nhạc sống cùng với bữa tối. Thật không may, buổi biểu diễn của ban nhạc tối hôm đó đã bị hủy. Không nản lòng, chúng tôi vẫn ở lại và cả hai đều gọi món gà nướng jerk. Trong khi hương vị hun khói của gà thật tuyệt hảo, thì món bắp cải hầm lại thiếu hương vị đậm đà. Ngoài ra, khẩu phần ăn nhỏ hơn chúng tôi dự tính, vì vậy chúng tôi đã gọi thêm một món khai vị nữa để tránh về nhà với bụng đói. Bếp trưởng đã ra xin lỗi và cực kỳ tử tế, nhưng có lẽ chúng tôi sẽ không sớm quay lại.\n\n---\nTừ: vsmith@orangebaykitchen.co.uk\nĐến: tpeterkin@sunmail.co.uk\nNgày: 24 tháng 8\nTiêu đề: Đánh giá của bạn\nĐính kèm: Phiếu quà tặng 0258\n\nKính gửi bà Peterkin,\nCảm ơn bà đã ghé thăm Orange Bay Kitchen và để lại đánh giá. Người quản lý của chúng tôi, Keron Deslandes, đã kể cho tôi nghe nhiều hơn về chuyến ghé thăm của bà và việc chúng tôi không đáp ứng được kỳ vọng của bà vào tối hôm đó. Xin vui lòng nhận phiếu quà tặng trị giá £20 đính kèm; tôi thực sự hy vọng rằng bà sẽ cho chúng tôi thêm một cơ hội thử lại.\nTrong chuyến ghé thăm của bà, ban nhạc của chúng tôi gặp sự cố kỹ thuật về thiết bị, đó là nguyên nhân dẫn đến việc hủy biểu diễn vào phút chót. Tuy nhiên, ban nhạc sẽ quay trở lại biểu diễn hàng tuần bắt đầu từ tháng Chín. Ngoài ra, tôi muốn bà biết rằng Bếp trưởng Adio Brown đã thay đổi các loại gia vị ông sử dụng cho món bắp cải hầm. Tôi chắc chắn rằng bà sẽ thấy chúng ngon miệng.\n\nTrân trọng,\nVea Smith, Chủ sở hữu\nOrange Bay Kitchen",
        "questionText": "What does the article mention about Orange Bay Kitchen?",
        "questionTextVi": "Bài báo đề cập điều gì về nhà hàng Orange Bay Kitchen?",
        "options": {
            "A": "It is currently hiring servers.",
            "B": "It is located on a quiet street.",
            "C": "It has another location in Jamaica.",
            "D": "It opened six months ago."
        },
        "optionsVi": {
            "A": "Nhà hàng hiện đang tuyển dụng nhân viên phục vụ.",
            "B": "Nhà hàng tọa lạc trên một con phố yên tĩnh.",
            "C": "Nhà hàng có một chi nhánh khác ở Jamaica.",
            "D": "Nhà hàng đã mở cửa được sáu tháng."
        },
        "correctAnswer": "D",
        "explanation": "Câu đầu tiên của bài báo viết: 'Orange Bay Kitchen has been serving up an infusion of Jamaican flavours in a laid-back Caribbean atmosphere for six months now' (Orange Bay Kitchen đã phục vụ... được 6 tháng nay rồi). Điều này tương đương phương án (D) 'It opened six months ago' (Nó đã mở cửa cách đây 6 tháng).",
        "vocabulary": [
            { "word": "infusion", "ipa": "/ɪnˈfjuː.ʒən/", "pos": "n", "meaning": "sự pha trộn, truyền vào", "example": "The chef blends an infusion of spices into the sauce." },
            { "word": "laid-back", "ipa": "/ˌleɪdˈbæk/", "pos": "adj", "meaning": "thư thái, ung dung thoải mái", "example": "The coastal town has a laid-back lifestyle." }
        ],
        "collocations": [
            { "phrase": "opened six months ago", "meaning": "đã mở cửa cách đây 6 tháng" },
            { "phrase": "extensive menu", "meaning": "thực đơn phong phú đa dạng" }
        ],
        "grammarPoints": [
            { "title": "Hiện tại hoàn thành tiếp diễn với khoảng thời gian", "content": "'has been serving... for six months now' = mở cửa hoạt động được 6 tháng." }
        ]
    },
    {
        "id": 192,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_14",
        "passageTitle": "Article, Review & E-mail: Orange Bay Kitchen",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_26.png", "assets/images/rc_page_27.png"],
        "passageText": "The restaurant is most famous for its jerk chicken. Marinated for 24 hours prior to grilling and served with sides of stewed cabbage and coconut rice, the dish is a good deal at £12.",
        "passageTextVi": "Nhà hàng nổi tiếng nhất với món gà nướng jerk...",
        "questionText": "According to the article, what is the most popular menu item at Orange Bay Kitchen?",
        "questionTextVi": "Theo bài báo, món ăn phổ biến/nổi tiếng nhất trong thực đơn tại Orange Bay Kitchen là món gì?",
        "options": {
            "A": "Red snapper",
            "B": "Oxtail soup",
            "C": "Jerk chicken",
            "D": "Curried goat"
        },
        "optionsVi": {
            "A": "Cá hồng",
            "B": "Súp đuôi bò",
            "C": "Gà nướng jerk",
            "D": "Dê nấu cà ri"
        },
        "correctAnswer": "C",
        "explanation": "Bài báo nêu rõ: 'The restaurant is most famous for its jerk chicken' (Nhà hàng nổi tiếng nhất với món gà nướng jerk). 'most famous' tương đương 'most popular menu item'. Chọn (C).",
        "vocabulary": [
            { "word": "marinate", "ipa": "/ˈmær.ɪ.neɪt/", "pos": "v", "meaning": "tẩm ướp gia vị", "example": "Marinate the chicken in herbs before grilling." }
        ],
        "collocations": [
            { "phrase": "most famous for", "meaning": "nổi tiếng nhất về..." },
            { "phrase": "jerk chicken", "meaning": "món gà nướng kiểu Jamaica" }
        ],
        "grammarPoints": [
            { "title": "So sánh nhất 'most famous'", "content": "'most famous' được dùng để nhấn mạnh nét đặc trưng nổi tiếng nhất." }
        ]
    },
    {
        "id": 193,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_14",
        "passageTitle": "Article, Review & E-mail: Orange Bay Kitchen",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_26.png", "assets/images/rc_page_27.png"],
        "passageText": "Article: If you stop in on any Friday night between 7 and 11 P.M., you will enjoy live reggae music.\n---\nReview: My husband and I arrived there at 7 P.M. yesterday, keen to enjoy live music with our dinner. Unfortunately, the band's performance that night had been cancelled.",
        "passageTextVi": "Bài báo: Nếu ghé vào bất kỳ tối thứ Sáu nào từ 7 đến 11 giờ đêm, bạn sẽ thưởng thức nhạc sống reggae.\nĐánh giá: Chồng tôi và tôi đến lúc 7 giờ tối hôm qua, háo hức muốn thưởng thức nhạc sống cùng bữa tối...",
        "questionText": "What is suggested about Ms. Peterkin's visit to Orange Bay Kitchen?",
        "questionTextVi": "Điều gì được gợi ý về chuyến ghé thăm của bà Peterkin đến Orange Bay Kitchen?",
        "options": {
            "A": "She was there on a Friday.",
            "B": "She dined alone.",
            "C": "She requested extra rice.",
            "D": "She ordered dessert."
        },
        "optionsVi": {
            "A": "Bà ấy đã đến quán vào một ngày thứ Sáu.",
            "B": "Bà ấy dùng bữa một mình.",
            "C": "Bà ấy đã yêu cầu thêm cơm.",
            "D": "Bà ấy đã gọi món tráng miệng."
        },
        "correctAnswer": "A",
        "explanation": "Bài báo ở Văn bản 1 nói rõ rằng nhạc sống chỉ được biểu diễn vào các tối thứ Sáu ('on any Friday night between 7 and 11 P.M., you will enjoy live reggae music'). Trong bài review ở Văn bản 2, cô Peterkin viết cô và chồng đến lúc 7 PM vì 'keen to enjoy live music with our dinner'. Việc họ đến vào khung giờ có nhạc sống chứng minh họ đã đến vào một ngày thứ Sáu (She was there on a Friday). Chọn (A).",
        "vocabulary": [
            { "word": "keen", "ipa": "/kiːn/", "pos": "adj", "meaning": "háo hức, nhiệt tình", "example": "She was keen to begin her new internship." },
            { "word": "undeterred", "ipa": "/ˌʌn.dɪˈtɜːd/", "pos": "adj", "meaning": "không nản lòng, không lùi bước", "example": "Undeterred by rain, the runners finished the marathon." }
        ],
        "collocations": [
            { "phrase": "keen to enjoy", "meaning": "háo hức thưởng thức" },
            { "phrase": "live music", "meaning": "nhạc sống biểu diễn trực tiếp" }
        ],
        "grammarPoints": [
            { "title": "Kỹ thuật liên kết thông tin suy luận logic (Cross-text Logic)", "content": "Khớp thời gian tổ chức sự kiện nhạc sống ('Friday night') với mục đích của khách ('keen to enjoy live music') -> Ngày khách đến là thứ Sáu." }
        ]
    },
    {
        "id": 194,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_14",
        "passageTitle": "Article, Review & E-mail: Orange Bay Kitchen",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_26.png", "assets/images/rc_page_27.png"],
        "passageText": "From: vsmith@orangebaykitchen.co.uk\nTo: tpeterkin@sunmail.co.uk\nDate: 24 August\nSubject: Your review\n\nDear Ms. Peterkin,\nThank you for visiting Orange Bay Kitchen and leaving a review. Our manager, Keron Deslandes, told me more about your visit and our failure to live up to your expectations that evening. Please accept the attached £20 gift certificate; I do hope that you will give us another try.\nDuring your visit, our band had an equipment malfunction, which is what led to the last-minute cancellation...",
        "passageTextVi": "Kính gửi bà Peterkin... Người quản lý đã kể về việc chúng tôi không đáp ứng được kỳ vọng của bà vào tối hôm đó. Xin vui lòng nhận phiếu quà tặng £20 đính kèm; tôi thực sự hy vọng bà sẽ cho chúng tôi thêm một cơ hội...",
        "questionText": "What is a purpose of the e-mail?",
        "questionTextVi": "Mục đích của bức email là gì?",
        "options": {
            "A": "To answer a question",
            "B": "To offer an apology",
            "C": "To ask for feedback",
            "D": "To confirm a reservation"
        },
        "optionsVi": {
            "A": "Để trả lời một câu hỏi",
            "B": "Để gửi lời xin lỗi và tạ lỗi",
            "C": "Để xin ý kiến phản hồi",
            "D": "Để xác nhận đặt bàn"
        },
        "correctAnswer": "B",
        "explanation": "Chủ nhà hàng gửi email vì biết buổi tối của khách không như ý ('our failure to live up to your expectations'), giải thích lý do ban nhạc hủy diễn và gửi tặng voucher £20 để mong khách quay lại. Đây là một bức thư gửi lời xin lỗi (To offer an apology). Chọn (B).",
        "vocabulary": [
            { "word": "malfunction", "ipa": "/ˌmælˈfʌŋk.ʃən/", "pos": "n", "meaning": "sự cố kỹ thuật, trục trặc", "example": "The sound system suffered a sudden malfunction." },
            { "word": "apology", "ipa": "/əˈpɒl.ə.dʒi/", "pos": "n", "meaning": "lời xin lỗi", "example": "We received an official letter of apology from the airline." }
        ],
        "collocations": [
            { "phrase": "offer an apology", "meaning": "đưa ra lời xin lỗi" },
            { "phrase": "live up to expectations", "meaning": "đáp ứng được kỳ vọng" }
        ],
        "grammarPoints": [
            { "title": "Cụm 'live up to expectations'", "content": "'fail to live up to expectations': không đáp ứng được sự mong đợi của ai." }
        ]
    },
    {
        "id": 195,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_14",
        "passageTitle": "Article, Review & E-mail: Orange Bay Kitchen",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_26.png", "assets/images/rc_page_27.png"],
        "passageText": "Review: The head chef came out to apologise and was extremely nice, but we will probably not go back anytime soon.\n---\nE-mail: Also, I want you to know that Head Chef Adio Brown has changed the spices he uses in the stewed cabbage.",
        "passageTextVi": "Đánh giá: Bếp trưởng đã ra xin lỗi và cực kỳ dễ mến...\nEmail: Tôi muốn bà biết rằng Bếp trưởng Adio Brown đã thay đổi gia vị mà ông dùng trong món bắp cải hầm.",
        "questionText": "Whom did Ms. Peterkin meet at Orange Bay Kitchen?",
        "questionTextVi": "Bà Peterkin đã gặp ai tại quán Orange Bay Kitchen?",
        "options": {
            "A": "Ms. Roats",
            "B": "Mr. Deslandes",
            "C": "Mr. Brown",
            "D": "Ms. Smith"
        },
        "optionsVi": {
            "A": "Cô Roats",
            "B": "Ông Deslandes",
            "C": "Ông Brown",
            "D": "Bà Smith"
        },
        "correctAnswer": "C",
        "explanation": "Trong bài review, cô Peterkin viết: 'The head chef came out to apologise and was extremely nice' (Vị bếp trưởng đã bước ra bàn để xin lỗi và rất tử tế). Trong email ở Văn bản 3, chủ nhà hàng nhắc đến tên của vị bếp trưởng: 'Head Chef Adio Brown'. Vì thế người mà cô Peterkin đã trực tiếp gặp là ông Adio Brown (Mr. Brown). Chọn (C).",
        "vocabulary": [
            { "word": "apologise", "ipa": "/əˈpɒl.ə.dʒaɪz/", "pos": "v", "meaning": "xin lỗi", "example": "The manager personally apologised for the delay." }
        ],
        "collocations": [
            { "phrase": "head chef", "meaning": "bếp trưởng" }
        ],
        "grammarPoints": [
            { "title": "Khớp chức danh và họ tên (Title and Name Matching)", "content": "'The head chef' (Review) + 'Head Chef Adio Brown' (Email) -> Mr. Brown." }
        ]
    },

    # 196 - 200 (Triple Passage: Orbys Distributors)
    {
        "id": 196,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_15",
        "passageTitle": "Invoice, Notice & E-mail: Orbys Distributors",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_28.png", "assets/images/rc_page_29.png"],
        "passageText": "Orbys Distributors\nClient: Green Canyon\nDate: June 10\nAccount: 4352-0\n\nItem | Price\nGarden soil, 33 cubic meters | $1,170.00\nCrushed gravel, 30 metric tons | 1,710.00\nDecorative stone, 20 metric tons | 1,140.00\n70 paving stones, .6 x .6 meters | 630.00\nSubtotal: $4,650.00\nDiscount (10%): -465.00\nDelivery charge: 350.00\nGrand Total: $4,535.00\n\nPlease see the enclosed notice outlining important changes to your billing.\n\n---\nOrbys Distributors\nTo our valued customers:\nOur current invoicing system has been in use since Orbys Distributors was founded over twenty years ago. As a much-needed upgrade, we are switching to electronic invoicing. Starting August 1, invoices will be generated automatically each month and will be sent to the e-mail address associated with your company's account.\nRest assured that our long-standing incentives remain in place:\n• A 10% discount for orders of more than $4,000\n• A 20% discount for charitable organizations\n• Free deliveries to locations within 5 miles of one of our supply centers\n• Free samples for members of our Frequent Buyer Club\nMore information about our transition to electronic invoicing is available on our Web site. Thank you for your support. Orbys Distributors appreciates your business.\n\n---\nTo: Mary Peterson, Billing Department\nFrom: Tanvir Singh, Account Manager\nDate: September 12\nSubject: Account 1012-4\n\nHello Mary,\nI received a query today from William Tesoriero at Tesoriero Remodeling. His monthly invoice for August never arrived. As you know, Mr. Tesoriero was one of our very first customers. Since we first opened for business, he has made purchases from us on a regular basis. He is also a member of the Frequent Buyer Club. This is a customer we absolutely do not want to lose. I explained to him that the rollout of our electronic invoicing system did not go as smoothly as we had hoped and promised that this would not happen again. I would appreciate it if you could please investigate the problem without delay and send the invoice for August to Mr. Tesoriero.\n\nTanvir",
        "passageTextVi": "Nhà phân phối Orbys\nKhách hàng: Green Canyon\nNgày: 10 tháng 6\nTài khoản: 4352-0\n\nMặt hàng | Giá\nĐất làm vườn, 33 mét khối | $1,170.00\nSỏi nghiền, 30 tấn | 1,710.00\nĐá trang trí, 20 tấn | 1,140.00\n70 viên đá lát nền, 0,6 x 0,6 mét | 630.00\nTổng phụ: $4,650.00\nChiết khấu (10%): -465.00\nPhí giao hàng: 350.00\nTổng cộng: $4,535.00\n\nVui lòng xem thông báo đính kèm nêu rõ những thay đổi quan trọng đối với việc lập hóa đơn của bạn.\n\n---\nNhà phân phối Orbys\nGửi quý khách hàng thân mến:\nHệ thống hóa đơn hiện tại của chúng tôi đã được sử dụng kể từ khi Orbys Distributors được thành lập hơn hai mươi năm trước. Như một sự nâng cấp vô cùng cần thiết, chúng tôi đang chuyển sang xuất hóa đơn điện tử. Bắt đầu từ ngày 1 tháng 8, hóa đơn sẽ được tạo tự động mỗi tháng và sẽ được gửi đến địa chỉ email liên kết với tài khoản công ty của bạn.\nHãy yên tâm rằng các chính sách ưu đãi lâu năm của chúng tôi vẫn được duy trì:\n• Giảm giá 10% cho các đơn hàng trên $4,000\n• Giảm giá 20% cho các tổ chức từ thiện\n• Giao hàng miễn phí tới các địa điểm trong phạm vi 5 dặm tính từ một trong các trung tâm cung ứng của chúng tôi\n• Hàng mẫu miễn phí cho các thành viên Câu lạc bộ Người mua thường xuyên\nThông tin thêm về quá trình chuyển đổi sang hóa đơn điện tử có trên trang web của chúng tôi. Cảm ơn sự hỗ trợ của bạn. Orbys Distributors trân trọng sự hợp tác của bạn.\n\n---\nĐến: Mary Peterson, Phòng Thanh toán\nTừ: Tanvir Singh, Quản lý Khách hàng\nNgày: 12 tháng 9\nTiêu đề: Tài khoản 1012-4\n\nChào Mary,\nHôm nay tôi nhận được một thắc mắc từ William Tesoriero tại Tesoriero Remodeling. Hóa đơn hàng tháng của ông ấy cho tháng Tám không bao giờ đến. Như cô đã biết, ông Tesoriero là một trong những khách hàng đầu tiên của chúng tôi. Kể từ khi chúng tôi lần đầu tiên mở cửa kinh doanh, ông ấy đã mua hàng từ chúng tôi một cách đều đặn. Ông ấy cũng là thành viên của Câu lạc bộ Người mua thường xuyên. Đây là khách hàng mà chúng tôi tuyệt đối không muốn đánh mất. Tôi đã giải thích với ông ấy rằng việc triển khai hệ thống hóa đơn điện tử của chúng tôi không diễn ra suôn sẻ như mong đợi và hứa rằng điều này sẽ không xảy ra nữa. Tôi sẽ rất cảm kích nếu cô có thể điều tra vấn đề mà không chậm trễ và gửi hóa đơn tháng Tám cho ông Tesoriero.\n\nTanvir",
        "questionText": "What does the invoice suggest about Green Canyon?",
        "questionTextVi": "Hóa đơn gợi ý điều gì về công ty Green Canyon?",
        "options": {
            "A": "It does landscaping projects.",
            "B": "It designs highways.",
            "C": "It repairs old houses.",
            "D": "It operates a farm."
        },
        "optionsVi": {
            "A": "Công ty này thực hiện các dự án cảnh quan.",
            "B": "Công ty thiết kế đường cao tốc.",
            "C": "Công ty sửa chữa nhà cũ.",
            "D": "Công ty điều hành một trang trại."
        },
        "correctAnswer": "A",
        "explanation": "Đơn hàng của Green Canyon bao gồm: 'Garden soil' (đất vườn), 'Crushed gravel' (sỏi nghiền), 'Decorative stone' (đá trang trí), 'paving stones' (đá lát lối đi). Các vật liệu này đặc trưng cho việc thi công cảnh quan sân vườn (landscaping projects). Do đó chọn (A).",
        "vocabulary": [
            { "word": "gravel", "ipa": "/ˈɡræv.əl/", "pos": "n", "meaning": "sỏi, đá dăm", "example": "The driveway was paved with crushed gravel." },
            { "word": "paving", "ipa": "/ˈpeɪ.vɪŋ/", "pos": "n", "meaning": "việc lát đá, vật liệu lát nền", "example": "Workers laid the stone paving along the garden path." },
            { "word": "landscaping", "ipa": "/ˈlænd.skeɪ.pɪŋ/", "pos": "n", "meaning": "làm cảnh quan, kiến trúc cảnh quan", "example": "The hotel spent thousands on professional landscaping." }
        ],
        "collocations": [
            { "phrase": "landscaping projects", "meaning": "các dự án thiết kế và thi công cảnh quan" },
            { "phrase": "paving stones", "meaning": "đá lát nền / lối đi" }
        ],
        "grammarPoints": [
            { "title": "Kỹ năng suy luận từ danh sách vật tư", "content": "Tập hợp các danh từ: soil, gravel, decorative stone, paving stone -> Landscaping (cảnh quan)." }
        ]
    },
    {
        "id": 197,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_15",
        "passageTitle": "Invoice, Notice & E-mail: Orbys Distributors",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_28.png", "assets/images/rc_page_29.png"],
        "passageText": "Invoice: Subtotal: $4,650.00 | Discount (10%): -$465.00\nNotice: Rest assured that our long-standing incentives remain in place:\n• A 10% discount for orders of more than $4,000",
        "passageTextVi": "Hóa đơn: Tổng phụ: $4,650.00 | Giảm giá (10%): -$465.00\nThông báo: Chính sách ưu đãi lâu đời:\n• Giảm giá 10% cho các đơn hàng trên $4,000",
        "questionText": "Why most likely did Green Canyon receive a discount on its order dated June 10?",
        "questionTextVi": "Tại sao Green Canyon nhiều khả năng nhất đã nhận được chiết khấu trong đơn hàng ngày 10 tháng 6?",
        "options": {
            "A": "It is a charitable organization.",
            "B": "It belongs to the Frequent Buyer Club.",
            "C": "It spent more than $4,000 on merchandise.",
            "D": "It is located near an Orbys Distributors supply center."
        },
        "optionsVi": {
            "A": "Nó là một tổ chức từ thiện.",
            "B": "Nó thuộc Câu lạc bộ Người mua thường xuyên.",
            "C": "Nó đã chi tiêu hơn $4,000 cho tiền hàng hóa.",
            "D": "Nó nằm gần một trung tâm cung ứng của Orbys Distributors."
        },
        "correctAnswer": "C",
        "explanation": "Trên hóa đơn, Green Canyon được giảm 10% (tiết kiệm $465.00 trên tổng tiền hàng $4,650.00). Đối chiếu với thông báo ưu đãi ở Văn bản 2: 'A 10% discount for orders of more than $4,000' (Chiết khấu 10% cho đơn hàng trên $4,000). Vì tổng đơn hàng là $4,650 (> $4,000) nên họ được áp dụng mức giảm 10% này. Do đó chọn (C).",
        "vocabulary": [
            { "word": "subtotal", "ipa": "/ˈsʌbˌtəʊ.təl/", "pos": "n", "meaning": "tổng phụ (chưa tính thuế/phí)", "example": "The subtotal before discount was $500." },
            { "word": "incentive", "ipa": "/ɪnˈsen.tɪv/", "pos": "n", "meaning": "chính sách khuyến khích, ưu đãi", "example": "The company offers financial incentives for high performers." }
        ],
        "collocations": [
            { "phrase": "receive a discount", "meaning": "nhận được chiết khấu / giảm giá" },
            { "phrase": "orders of more than", "meaning": "các đơn hàng có giá trị trên..." }
        ],
        "grammarPoints": [
            { "title": "So khớp số liệu đa văn bản (Cross-document Numerical Matching)", "content": "So sánh con số: $4,650 > $4,000 -> hưởng ưu đãi 10% discount." }
        ]
    },
    {
        "id": 198,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_15",
        "passageTitle": "Invoice, Notice & E-mail: Orbys Distributors",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_28.png", "assets/images/rc_page_29.png"],
        "passageText": "Our current invoicing system has been in use since Orbys Distributors was founded over twenty years ago. As a much-needed upgrade, we are switching to electronic invoicing. Starting August 1, invoices will be generated automatically each month and will be sent to the e-mail address associated with your company's account.",
        "passageTextVi": "Hệ thống lập hóa đơn hiện tại... đã dùng hơn 20 năm... chúng tôi đang chuyển đổi sang lập hóa đơn điện tử...",
        "questionText": "According to the notice, what is changing at Orbys Distributors?",
        "questionTextVi": "Theo thông báo, điều gì đang thay đổi tại Orbys Distributors?",
        "options": {
            "A": "Its e-mail address",
            "B": "Its list of incentives",
            "C": "Its invoicing system",
            "D": "Its delivery schedule"
        },
        "optionsVi": {
            "A": "Địa chỉ email của công ty",
            "B": "Danh sách các ưu đãi",
            "C": "Hệ thống xuất / lập hóa đơn",
            "D": "Lịch trình giao hàng"
        },
        "correctAnswer": "C",
        "explanation": "Thông báo viết rõ: 'we are switching to electronic invoicing' (chúng tôi đang chuyển sang hệ thống hóa đơn điện tử) thay thế cho 'Our current invoicing system has been in use...'. Điều thay đổi chính là hệ thống hóa đơn (Its invoicing system). Chọn (C).",
        "vocabulary": [
            { "word": "invoicing", "ipa": "/ˈɪn.vɔɪ.sɪŋ/", "pos": "n", "meaning": "việc xuất / lập hóa đơn", "example": "Electronic invoicing speeds up payment cycles." },
            { "word": "upgrade", "ipa": "/ˈʌp.ɡreɪd/", "pos": "n, v", "meaning": "sự nâng cấp", "example": "The IT system is scheduled for an upgrade." }
        ],
        "collocations": [
            { "phrase": "electronic invoicing", "meaning": "hóa đơn điện tử" },
            { "phrase": "switch to", "meaning": "chuyển sang sử dụng" }
        ],
        "grammarPoints": [
            { "title": "Cấu trúc 'switch to + Noun'", "content": "'switch to something': chuyển hẳn sang một phương thức hoặc hệ thống mới." }
        ]
    },
    {
        "id": 199,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_15",
        "passageTitle": "Invoice, Notice & E-mail: Orbys Distributors",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_28.png", "assets/images/rc_page_29.png"],
        "passageText": "Notice: Our current invoicing system has been in use since Orbys Distributors was founded over twenty years ago.\n---\nE-mail: As you know, Mr. Tesoriero was one of our very first customers. Since we first opened for business, he has made purchases from us on a regular basis.",
        "passageTextVi": "Thông báo: ...kể từ khi Orbys Distributors được thành lập hơn hai mươi năm trước.\nEmail: ...ông Tesoriero là một trong những khách hàng đầu tiên của chúng ta. Kể từ khi chúng ta lần đầu mở cửa kinh doanh, ông ấy đã mua hàng đều đặn...",
        "questionText": "What is suggested about Mr. Tesoriero?",
        "questionTextVi": "Điều gì được gợi ý về ông Tesoriero?",
        "options": {
            "A": "He asked to meet with Mr. Singh.",
            "B": "He is interested in employment at Orbys Distributors.",
            "C": "He recently placed an order for some construction machinery.",
            "D": "He has been a customer of Orbys Distributors for about twenty years."
        },
        "optionsVi": {
            "A": "Ông ấy đã yêu cầu gặp ông Singh.",
            "B": "Ông ấy quan tâm đến việc làm tại Orbys Distributors.",
            "C": "Gần đây ông ấy đã đặt mua một số máy móc xây dựng.",
            "D": "Ông ấy đã là khách hàng của Orbys Distributors trong khoảng hai mươi năm."
        },
        "correctAnswer": "D",
        "explanation": "Thông báo cho biết Orbys Distributors được thành lập hơn 20 năm trước ('founded over twenty years ago'). Email cho biết ông Tesoriero là một trong những khách hàng đầu tiên kể từ khi công ty mở cửa ('one of our very first customers. Since we first opened for business...'). Hai dữ liệu này kết hợp lại cho thấy ông Tesoriero đã là khách hàng suốt khoảng 20 năm qua (has been a customer for about twenty years). Chọn (D).",
        "vocabulary": [
            { "word": "rollout", "ipa": "/ˈrəʊl.aʊt/", "pos": "n", "meaning": "sự triển khai sản phẩm / hệ thống mới", "example": "The national rollout of 5G began last month." }
        ],
        "collocations": [
            { "phrase": "on a regular basis", "meaning": "một cách đều đặn, thường xuyên" },
            { "phrase": "customer for twenty years", "meaning": "khách hàng trong suốt 20 năm" }
        ],
        "grammarPoints": [
            { "title": "Nối mốc thời gian suy luận thời lượng", "content": "'founded over twenty years ago' + 'one of our very first customers' -> là khách hàng khoảng 20 năm." }
        ]
    },
    {
        "id": 200,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_15",
        "passageTitle": "Invoice, Notice & E-mail: Orbys Distributors",
        "passageType": "Triple Passage",
        "pageImages": ["assets/images/rc_page_28.png", "assets/images/rc_page_29.png"],
        "passageText": "I explained to him that the rollout of our electronic invoicing system did not go as smoothly as we had hoped and promised that this would not happen again. I would appreciate it if you could please investigate the problem without delay and send the invoice for August to Mr. Tesoriero.",
        "passageTextVi": "Tôi đã giải thích với ông ấy rằng việc triển khai hệ thống hóa đơn điện tử không diễn ra suôn sẻ... Tôi sẽ rất cảm kích nếu cô có thể điều tra vấn đề mà không chậm trễ và gửi hóa đơn tháng Tám cho ông Tesoriero.",
        "questionText": "What does Mr. Singh ask Ms. Peterson to do?",
        "questionTextVi": "Ông Singh yêu cầu cô Peterson làm điều gì?",
        "options": {
            "A": "Make a bill payment",
            "B": "Solve a problem",
            "C": "Confirm an order",
            "D": "Update an account number"
        },
        "optionsVi": {
            "A": "Thực hiện thanh toán hóa đơn",
            "B": "Giải quyết một vấn đề (hóa đơn bị thất lạc/chưa gửi)",
            "C": "Xác nhận một đơn đặt hàng",
            "D": "Cập nhật một số tài khoản"
        },
        "correctAnswer": "B",
        "explanation": "Câu cuối của email ghi rõ: 'I would appreciate it if you could please investigate the problem without delay and send the invoice for August to Mr. Tesoriero' (Tôi rất cảm kích nếu cô có thể điều tra vấn đề mà không chậm trễ và gửi hóa đơn cho khách). Điều này đồng nghĩa với việc giải quyết một trục trặc/vấn đề trong hệ thống gửi hóa đơn (Solve a problem). Chọn (B).",
        "vocabulary": [
            { "word": "investigate", "ipa": "/ɪnˈves.tɪ.ɡeɪt/", "pos": "v", "meaning": "điều tra, tìm hiểu nguyên nhân", "example": "Technicians are investigating the network outage." },
            { "word": "without delay", "ipa": "/wɪˈðaʊt dɪˈleɪ/", "pos": "idiom", "meaning": "ngay lập tức, không chậm trễ", "example": "Please process this request without delay." }
        ],
        "collocations": [
            { "phrase": "investigate the problem", "meaning": "tìm hiểu / giải quyết vấn đề" },
            { "phrase": "without delay", "meaning": "ngay lập tức, không trì hoãn" }
        ],
        "grammarPoints": [
            { "title": "Cấu trúc nhờ cậy lịch sự", "content": "'I would appreciate it if you could please + V': Mẫu câu trang trọng yêu cầu đồng nghiệp hỗ trợ xử lý công việc." }
        ]
    }
]

if __name__ == "__main__":
    print(f"P7 Part 3 loaded with {len(P7_PART3)} questions.")
