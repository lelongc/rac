# part7_part2.py: Part 7 Questions 155 - 175
import json

P7_PART2 = [
    # 155 - 157
    {
        "id": 155,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_5",
        "passageTitle": "Notice: Vosey Farm and Garden",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_13.png"],
        "passageText": "This season's excellent weather has yielded a substantial harvest of fruits and vegetables, in many cases more than growers may find buyers for. Those of you wishing to donate surplus produce to community organizations can do so by visiting Vosey Farm and Garden's Web site (www.vfgrdn.org), where you will find our list of drop-off locations. If you need us to come to you instead, please contact us. We will reach out to one of the many independent truck drivers who have kindly volunteered to transport and quickly distribute your food donations to vetted groups that need it. Check our Web site for more information about this service as well as for insights into topics related to farming and gardening in the Northern Great Plains region.",
        "passageTextVi": "Thời tiết tuyệt vời của mùa này đã mang lại một vụ thu hoạch rau củ quả bội thu, trong nhiều trường hợp vượt quá số lượng mà người trồng trọt có thể tìm được người mua. Những ai trong số quý vị muốn quyên góp nông sản dư thừa cho các tổ chức cộng đồng có thể thực hiện bằng cách truy cập trang web của Vosey Farm and Garden (www.vfgrdn.org), nơi quý vị sẽ tìm thấy danh sách các điểm tiếp nhận của chúng tôi. Nếu quý vị cần chúng tôi đến tận nơi thu gom, vui lòng liên hệ với chúng tôi. Chúng tôi sẽ liên lạc với một trong nhiều tài xế xe tải độc lập đã nhiệt tình tình nguyện vận chuyển và nhanh chóng phân phối các khoản quyên góp thực phẩm của quý vị tới các nhóm được kiểm định đang cần. Hãy kiểm tra trang web của chúng tôi để biết thêm thông tin về dịch vụ này cũng như để tìm hiểu sâu hơn về các chủ đề liên quan đến trồng trọt và làm vườn ở khu vực Northern Great Plains.",
        "questionText": "For whom is the notice most likely intended?",
        "questionTextVi": "Thông báo này rất có thể dành cho đối tượng nào?",
        "options": {
            "A": "Farmers",
            "B": "Professional chefs",
            "C": "Truck drivers",
            "D": "Supermarket managers"
        },
        "optionsVi": {
            "A": "Những người nông dân, người trồng trọt",
            "B": "Các đầu bếp chuyên nghiệp",
            "C": "Các tài xế xe tải",
            "D": "Các quản lý siêu thị"
        },
        "correctAnswer": "A",
        "explanation": "Thông báo viết: 'in many cases more than growers may find buyers for. Those of you wishing to donate surplus produce...' (vượt quá lượng mà người trồng có thể tìm người mua. Những quý vị nào muốn quyên góp nông sản dư thừa...). 'Growers' đồng nghĩa với 'Farmers' (những người nông dân). Chọn (A).",
        "vocabulary": [
            { "word": "yield", "ipa": "/jiːld/", "pos": "v", "meaning": "mang lại, sinh ra (sản lượng)", "example": "The fertile soil yields a high volume of wheat." },
            { "word": "surplus", "ipa": "/ˈsɜː.pləs/", "pos": "n", "meaning": "thặng dư, dư thừa", "example": "Farmers sold their surplus grain to other regions." },
            { "word": "produce", "ipa": "/ˈprɒd.juːs/", "pos": "n", "meaning": "nông sản (rau củ quả)", "example": "The supermarket sells organic local produce." }
        ],
        "collocations": [
            { "phrase": "substantial harvest", "meaning": "vụ mùa bội thu, sản lượng đáng kể" },
            { "phrase": "surplus produce", "meaning": "nông sản dư thừa" }
        ],
        "grammarPoints": [
            { "title": "Phân biệt Danh từ 'produce' và Động từ 'produce'", "content": "Khi là danh từ, 'produce' trọng âm rơi vào âm tiết thứ nhất /ˈprɒd.juːs/, mang nghĩa 'nông sản'." }
        ]
    },
    {
        "id": 156,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_5",
        "passageTitle": "Notice: Vosey Farm and Garden",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_13.png"],
        "passageText": "This season's excellent weather has yielded a substantial harvest of fruits and vegetables, in many cases more than growers may find buyers for. Those of you wishing to donate surplus produce to community organizations can do so by visiting Vosey Farm and Garden's Web site (www.vfgrdn.org), where you will find our list of drop-off locations...",
        "passageTextVi": "Thời tiết tuyệt vời của mùa này đã mang lại một vụ thu hoạch rau củ quả bội thu...",
        "questionText": "What does the notice indicate about the weather?",
        "questionTextVi": "Thông báo cho biết điều gì về thời tiết?",
        "options": {
            "A": "It caused transportation delays.",
            "B": "It included heavier rain than usual.",
            "C": "It was frequently a topic in the local news.",
            "D": "It was beneficial for crops."
        },
        "optionsVi": {
            "A": "Nó gây ra sự chậm trễ trong việc vận chuyển.",
            "B": "Nó bao gồm lượng mưa lớn hơn bình thường.",
            "C": "Nó thường xuyên là một chủ đề trên tin tức địa phương.",
            "D": "Nó có lợi cho mùa màng/cây trồng."
        },
        "correctAnswer": "D",
        "explanation": "Câu đầu tiên nêu rõ: 'This season's excellent weather has yielded a substantial harvest of fruits and vegetables' (Thời tiết tuyệt vời của mùa này đã đem lại vụ mùa bội thu rau củ quả). Thời tiết tuyệt vời đem lại vụ mùa bội thu nghĩa là thời tiết rất có lợi cho cây trồng (beneficial for crops). Do đó chọn (D).",
        "vocabulary": [
            { "word": "substantial", "ipa": "/səbˈstæn.ʃəl/", "pos": "adj", "meaning": "đáng kể, to lớn", "example": "The project received substantial financial support." },
            { "word": "crop", "ipa": "/krɒp/", "pos": "n", "meaning": "cây trồng, vụ mùa", "example": "Apples are the main cash crop in this valley." }
        ],
        "collocations": [
            { "phrase": "beneficial for crops", "meaning": "có lợi cho cây trồng" },
            { "phrase": "excellent weather", "meaning": "thời tiết tuyệt vời, thuận lợi" }
        ],
        "grammarPoints": [
            { "title": "Hiện tại hoàn thành diễn tả kết quả hiện tại", "content": "'has yielded a substantial harvest': diễn tả hành động đã diễn ra và để lại kết quả cụ thể ở hiện tại." }
        ]
    },
    {
        "id": 157,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_5",
        "passageTitle": "Notice: Vosey Farm and Garden",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_13.png"],
        "passageText": "Those of you wishing to donate surplus produce to community organizations can do so by visiting Vosey Farm and Garden's Web site (www.vfgrdn.org), where you will find our list of drop-off locations. If you need us to come to you instead, please contact us. We will reach out to one of the many independent truck drivers who have kindly volunteered to transport and quickly distribute your food donations to vetted groups that need it.",
        "passageTextVi": "...Các tài xế xe tải tình nguyện vận chuyển và nhanh chóng phân phối các khoản quyên góp thực phẩm của quý vị tới các nhóm được kiểm định đang cần...",
        "questionText": "What service does the notice mention?",
        "questionTextVi": "Dịch vụ nào được đề cập trong thông báo?",
        "options": {
            "A": "Staffing for local businesses",
            "B": "Food collection and distribution",
            "C": "Farm machinery repair",
            "D": "Gardening workshops"
        },
        "optionsVi": {
            "A": "Cung cấp nhân sự cho các doanh nghiệp địa phương",
            "B": "Thu gom và phân phối thực phẩm",
            "C": "Sửa chữa máy móc nông nghiệp",
            "D": "Các buổi hội thảo làm vườn"
        },
        "correctAnswer": "B",
        "explanation": "Tổ chức tiếp nhận thực phẩm quyên góp tại các điểm drop-off hoặc điều tài xế tới tận nơi lấy thực phẩm đem phân phát cho người cần: 'transport and quickly distribute your food donations'. Đây chính là dịch vụ thu gom và phân phối thực phẩm (Food collection and distribution). Chọn (B).",
        "vocabulary": [
            { "word": "distribute", "ipa": "/dɪˈstrɪb.juːt/", "pos": "v", "meaning": "phân phát, phân phối", "example": "Volunteers distributed relief packages to families." },
            { "word": "vetted", "ipa": "/ˈvet.ɪd/", "pos": "adj", "meaning": "đã qua thẩm tra, kiểm định", "example": "Only vetted charities receive direct grants." }
        ],
        "collocations": [
            { "phrase": "food donation", "meaning": "sự quyên góp thực phẩm" },
            { "phrase": "drop-off location", "meaning": "điểm tập kết, điểm tiếp nhận" }
        ],
        "grammarPoints": [
            { "title": "Từ loại kép: Collection and Distribution", "content": "'collection' (thu gom) và 'distribution' (phân phối) tạo thành quy trình hoàn chỉnh trong chuỗi cung ứng từ thiện." }
        ]
    },

    # 158 - 160
    {
        "id": 158,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_6",
        "passageTitle": "Notice: Event Guidelines for Attendees",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_14.png"],
        "passageText": "We are delighted that you are joining us for today's event. [1] We ask that you adhere to the following guidelines to ensure that all attendees have an enjoyable experience.\nUpon entering the venue, please put any and all electronic devices in silent mode. Ringtones and lit screens are very distracting to both the performers and your fellow audience members. [2] Moreover, audience members are not allowed to make an audio or visual recording of the performance.\nBags and other items in the aisles pose a safety concern. [3] If your bag is too big to fit properly under a seat, consider storing it in a locker for just $2. [4] One of our attendants will gladly assist you with that. Thank you for your cooperation.",
        "passageTextVi": "Chúng tôi rất vui mừng vì bạn đã cùng tham dự sự kiện hôm nay với chúng tôi. [1] Chúng tôi yêu cầu bạn tuân thủ các nguyên tắc sau để đảm bảo tất cả người tham dự đều có một trải nghiệm thú vị.\nKhi bước vào khán phòng, vui lòng để tất cả các thiết bị điện tử ở chế độ im lặng. Chuông điện thoại và màn hình sáng đèn gây mất tập trung cho cả người biểu diễn và các khán giả đồng hành. [2] Hơn nữa, khán giả không được phép ghi âm hoặc ghi hình buổi biểu diễn.\nTúi xách và các vật dụng khác để ở lối đi sẽ gây lo ngại về an toàn. [3] Nếu túi xách của bạn quá lớn không để vừa dưới ghế ngồi, hãy cân nhắc cất nó trong tủ có khóa chỉ với giá $2. [4] Một trong những nhân viên hỗ trợ của chúng tôi sẽ rất sẵn lòng hỗ trợ bạn việc đó. Cảm ơn sự hợp tác của bạn.",
        "questionText": "Where most likely is the notice posted?",
        "questionTextVi": "Thông báo này rất có thể được dán ở đâu?",
        "options": {
            "A": "In an airplane",
            "B": "In a concert hall",
            "C": "At a restaurant",
            "D": "At a post office"
        },
        "optionsVi": {
            "A": "Trên một chiếc máy bay",
            "B": "Trong một phòng hòa nhạc / khán phòng biểu diễn",
            "C": "Tại một nhà hàng",
            "D": "Tại một bưu điện"
        },
        "correctAnswer": "B",
        "explanation": "Nội dung bài viết nhắc đến: 'performers and your fellow audience members' (người biểu diễn và các khán giả xung quanh), 'recording of the performance' (ghi hình buổi biểu diễn), 'aisles', 'fit under a seat'. Đây là các đặc trưng của một phòng hòa nhạc/khán phòng nhà hát (concert hall / auditorium). Chọn (B).",
        "vocabulary": [
            { "word": "performer", "ipa": "/pəˈfɔː.mər/", "pos": "n", "meaning": "người biểu diễn, nghệ sĩ", "example": "The performers received a standing ovation." },
            { "word": "aisle", "ipa": "/aɪl/", "pos": "n", "meaning": "lối đi giữa các hàng ghế", "example": "Please keep the center aisle clear during emergencies." },
            { "word": "adhere", "ipa": "/ədˈhɪər/", "pos": "v", "meaning": "tuân thủ, gắn bó", "example": "All staff must adhere to safety regulations." }
        ],
        "collocations": [
            { "phrase": "adhere to guidelines", "meaning": "tuân thủ các nguyên tắc hướng dẫn" },
            { "phrase": "silent mode", "meaning": "chế độ im lặng" }
        ],
        "grammarPoints": [
            { "title": "Cấu trúc 'ask that someone + V(bare)'", "content": "Thức giả định (subjunctive mood): 'We ask that you adhere...' động từ 'adhere' ở dạng nguyên thể." }
        ]
    },
    {
        "id": 159,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_6",
        "passageTitle": "Notice: Event Guidelines for Attendees",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_14.png"],
        "passageText": "Bags and other items in the aisles pose a safety concern. [3] If your bag is too big to fit properly under a seat, consider storing it in a locker for just $2. [4] One of our attendants will gladly assist you with that. Thank you for your cooperation.",
        "passageTextVi": "...Nếu túi xách của bạn quá lớn không để vừa dưới ghế ngồi, hãy cân nhắc cất nó trong tủ có khóa chỉ với giá $2...",
        "questionText": "What is stated about large bags?",
        "questionTextVi": "Điều gì được nêu về các loại túi xách cỡ lớn?",
        "options": {
            "A": "They can be put in a locked box for a fee.",
            "B": "They must be left outside the building.",
            "C": "They will be inspected by an attendant.",
            "D": "They must be stored under a seat."
        },
        "optionsVi": {
            "A": "Chúng có thể được cất vào một tủ có khóa với một khoản phí.",
            "B": "Chúng phải được để bên ngoài tòa nhà.",
            "C": "Chúng sẽ được kiểm tra bởi một nhân viên phục vụ.",
            "D": "Chúng bắt buộc phải được để dưới ghế ngồi."
        },
        "correctAnswer": "A",
        "explanation": "Bài viết nêu: 'If your bag is too big to fit properly under a seat, consider storing it in a locker for just $2' (Nếu túi của bạn quá lớn không để vừa gầm ghế, hãy cân nhắc gửi trong tủ khóa chỉ với $2). 'in a locker for just $2' tương đương 'in a locked box for a fee'. Chọn (A).",
        "vocabulary": [
            { "word": "locker", "ipa": "/ˈlɒk.ər/", "pos": "n", "meaning": "tủ đựng đồ có khóa", "example": "Store your backpack in the locker provided." },
            { "word": "attendant", "ipa": "/əˈten.dənt/", "pos": "n", "meaning": "nhân viên phục vụ, tiếp tân", "example": "The flight attendant helped passengers stow their baggage." }
        ],
        "collocations": [
            { "phrase": "for a fee", "meaning": "có tính phí, phải trả phí" },
            { "phrase": "pose a safety concern", "meaning": "gây ra mối lo ngại về an toàn" }
        ],
        "grammarPoints": [
            { "title": "Paraphrase từ vựng", "content": "'storing it in a locker for just $2' -> 'put in a locked box for a fee'." }
        ]
    },
    {
        "id": 160,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_6",
        "passageTitle": "Notice: Event Guidelines for Attendees",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_14.png"],
        "passageText": "We are delighted that you are joining us for today's event. [1] We ask that you adhere to the following guidelines to ensure that all attendees have an enjoyable experience.\nUpon entering the venue, please put any and all electronic devices in silent mode. Ringtones and lit screens are very distracting to both the performers and your fellow audience members. [2] Moreover, audience members are not allowed to make an audio or visual recording of the performance.\nBags and other items in the aisles pose a safety concern. [3] If your bag is too big to fit properly under a seat, consider storing it in a locker for just $2. [4] One of our attendants will gladly assist you with that. Thank you for your cooperation.",
        "passageTextVi": "...Khi bước vào khán phòng, vui lòng để tất cả các thiết bị điện tử ở chế độ im lặng. Chuông điện thoại và màn hình sáng đèn gây mất tập trung cho cả người biểu diễn và các khán giả đồng hành. [2] Hơn nữa, khán giả không được phép ghi âm hoặc ghi hình buổi biểu diễn...",
        "questionText": "In which of the positions marked [1], [2], [3], and [4] does the following sentence best belong?\n\"Please refrain from making phone calls or texting at all times.\"",
        "questionTextVi": "Câu sau đây phù hợp nhất ở vị trí nào trong các vị trí [1], [2], [3] và [4]?\n\"Vui lòng kiềm chế không gọi điện thoại hoặc nhắn tin vào mọi lúc.\"",
        "options": {
            "A": "[1]",
            "B": "[2]",
            "C": "[3]",
            "D": "[4]"
        },
        "optionsVi": {
            "A": "Vị trí [1]",
            "B": "Vị trí [2]",
            "C": "Vị trí [3]",
            "D": "Vị trí [4]"
        },
        "correctAnswer": "B",
        "explanation": "Câu cần điền yêu cầu không gọi điện và nhắn tin ('refrain from making phone calls or texting'). Đoạn ngay trước vị trí [2] nói về việc tắt chuông điện thoại và màn hình sáng ('Ringtones and lit screens are very distracting...'). Do đó câu này kết nối trực tiếp với các hành động sử dụng điện thoại tại vị trí [2]. Tiếp ngay sau đó, từ 'Moreover' bổ sung thêm lệnh cấm quay phim chụp ảnh. Chọn (B).",
        "vocabulary": [
            { "word": "refrain", "ipa": "/rɪˈfreɪn/", "pos": "v", "meaning": "kiềm chế, tránh không làm", "example": "Please refrain from smoking in the building." },
            { "word": "distracting", "ipa": "/dɪˈstræk.tɪŋ/", "pos": "adj", "meaning": "gây xao nhãng, làm mất tập trung", "example": "Loud conversations are distracting to colleagues." }
        ],
        "collocations": [
            { "phrase": "refrain from V-ing", "meaning": "kiềm chế / tránh làm việc gì" },
            { "phrase": "at all times", "meaning": "luôn luôn, mọi lúc" }
        ],
        "grammarPoints": [
            { "title": "Cấu trúc 'refrain from + V-ing'", "content": "Sau cụm 'refrain from' luôn đi cùng Danh động từ (V-ing)." }
        ]
    },

    # 161 - 164
    {
        "id": 161,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_7",
        "passageTitle": "E-mail: Sweeter Specialties Order",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_15.png"],
        "passageText": "To: Camille Ayala <ayala@esplinelectronics.com>\nFrom: Masae Adachi <madachi@sweeterspecialties.com>\nDate: February 12\nSubject: Event order\nAttachment: Sweeter Specialties Request Form\n\nDear Ms. Ayala,\nThank you for selecting our business to provide baked goods for the Esplin Electronics conference event in March. We are honored that you chose us for a fourth year in a row!\nOn March 29, we will provide a large vanilla cake for each of the ten venues you indicated, and we will deliver a custom-baked multilayer cake on the following day. You will be billed on March 28. Please review the attached order form and return it to me within seven days.\nRegarding the cake you ordered for March 30, our head pastry chef will produce it according to your specifications. In fact, he created a sample of the complete recipe earlier today—almond creme cake with fresh raspberry filling. We have judged it to be a delectable treat, and we are sure that you will be pleased. If you have any concerns, just send me an e-mail. As always, we value your business.\n\nSincerely,\nMasae Adachi, Owner\nSweeter Specialties",
        "passageTextVi": "Đến: Camille Ayala <ayala@esplinelectronics.com>\nTừ: Masae Adachi <madachi@sweeterspecialties.com>\nNgày: 12 tháng 2\nTiêu đề: Đơn đặt hàng sự kiện\nĐính kèm: Mẫu yêu cầu Sweeter Specialties\n\nKính gửi bà Ayala,\nCảm ơn bà đã chọn doanh nghiệp của chúng tôi cung cấp bánh nướng cho sự kiện hội nghị của Esplin Electronics vào tháng Ba. Chúng tôi rất vinh dự khi bà đã chọn chúng tôi trong 4 năm liên tiếp!\nVào ngày 29 tháng 3, chúng tôi sẽ cung cấp một chiếc bánh vani lớn cho mỗi địa điểm trong số mười địa điểm mà bà đã chỉ định, và chúng tôi sẽ giao một chiếc bánh nhiều tầng nướng theo yêu cầu vào ngày hôm sau. Bà sẽ nhận được hóa đơn vào ngày 28 tháng 3. Vui lòng xem lại mẫu đơn đặt hàng đính kèm và gửi lại cho tôi trong vòng bảy ngày.\nVề chiếc bánh bà đặt cho ngày 30 tháng 3, bếp trưởng bánh ngọt của chúng tôi sẽ làm theo đúng thông số kỹ thuật của bà. Trên thực tế, anh ấy đã tạo ra một mẫu công thức hoàn chỉnh vào đầu ngày hôm nay—bánh kem hạnh nhân với nhân quả mâm xôi tươi. Chúng tôi đánh giá đây là một món ngon hảo hạng và chúng tôi chắc chắn rằng bà sẽ hài lòng. Nếu bà có bất kỳ lo ngại nào, chỉ cần gửi email cho tôi. Như mọi khi, chúng tôi rất coi trọng sự hợp tác của bà.\n\nTrân trọng,\nMasae Adachi, Chủ sở hữu\nSweeter Specialties",
        "questionText": "What is the main purpose of the e-mail?",
        "questionTextVi": "Mục đích chính của email là gì?",
        "options": {
            "A": "To request confirmation of an order",
            "B": "To adjust some delivery dates",
            "C": "To announce the expansion of a business",
            "D": "To promote new dessert products"
        },
        "optionsVi": {
            "A": "Yêu cầu xác nhận lại một đơn đặt hàng",
            "B": "Điều chỉnh một số ngày giao hàng",
            "C": "Thông báo mở rộng hoạt động kinh doanh",
            "D": "Quảng bá các sản phẩm tráng miệng mới"
        },
        "correctAnswer": "A",
        "explanation": "Email gửi kèm mẫu đơn đặt hàng và yêu cầu: 'Please review the attached order form and return it to me within seven days' (Vui lòng kiểm tra lại đơn đặt hàng đính kèm và gửi lại cho tôi trong vòng 7 ngày). Đây là hành động yêu cầu xác nhận đơn hàng (request confirmation of an order). Do đó chọn (A).",
        "vocabulary": [
            { "word": "confirmation", "ipa": "/ˌkɒn.fəˈmeɪ.ʃən/", "pos": "n", "meaning": "sự xác nhận", "example": "We sent an email confirmation of your booking." },
            { "word": "specification", "ipa": "/ˌspes.ɪ.fɪˈkeɪ.ʃən/", "pos": "n", "meaning": "quy cách, đặc điểm kỹ thuật đặt may/làm", "example": "The machine was customized according to client specifications." }
        ],
        "collocations": [
            { "phrase": "request confirmation", "meaning": "yêu cầu xác nhận" },
            { "phrase": "in a row", "meaning": "liên tiếp" }
        ],
        "grammarPoints": [
            { "title": "Nhận diện mục đích thư tín qua câu yêu cầu", "content": "Câu mang câu mệnh lệnh lịch sự ('Please review and return...') thường chứa mục đích chính (main purpose) của bức thư/email." }
        ]
    },
    {
        "id": 162,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_7",
        "passageTitle": "E-mail: Sweeter Specialties Order",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_15.png"],
        "passageText": "Dear Ms. Ayala,\nThank you for selecting our business to provide baked goods for the Esplin Electronics conference event in March. We are honored that you chose us for a fourth year in a row!...",
        "passageTextVi": "...Cảm ơn bà đã chọn doanh nghiệp chúng tôi... Chúng tôi rất vinh dự khi bà chọn chúng tôi 4 năm liên tiếp!...",
        "questionText": "What is suggested about Ms. Ayala?",
        "questionTextVi": "Điều gì được gợi ý về bà Ayala?",
        "options": {
            "A": "She is receiving a professional award.",
            "B": "She has worked as a pastry chef.",
            "C": "She has been a Sweeter Specialties client in the past.",
            "D": "She received a positive recommendation about a chef."
        },
        "optionsVi": {
            "A": "Bà ấy sắp nhận một giải thưởng chuyên môn.",
            "B": "Bà ấy từng làm đầu bếp bánh ngọt.",
            "C": "Bà ấy đã từng là khách hàng của Sweeter Specialties trong quá khứ.",
            "D": "Bà ấy đã nhận được lời giới thiệu tích cực về một đầu bếp."
        },
        "correctAnswer": "C",
        "explanation": "Tác giả viết: 'We are honored that you chose us for a fourth year in a row!' (Chúng tôi rất vinh dự khi bà đã chọn chúng tôi trong 4 năm liên tiếp!). Điều này chứng tỏ bà Ayala đã là khách hàng của Sweeter Specialties trong quá khứ (client in the past). Chọn (C).",
        "vocabulary": [
            { "word": "honored", "ipa": "/ˈɒn.əd/", "pos": "adj", "meaning": "vinh dự, hân hạnh", "example": "We are honored to host tonight's distinguished speakers." }
        ],
        "collocations": [
            { "phrase": "for a fourth year in a row", "meaning": "năm thứ 4 liên tiếp" },
            { "phrase": "value someone's business", "meaning": "trân trọng sự hợp tác kinh doanh của ai" }
        ],
        "grammarPoints": [
            { "title": "Thì Hiện tại Hoàn thành suy luận thói quen", "content": "'chose us for a fourth year' -> khẳng định mối quan hệ khách hàng lâu năm." }
        ]
    },
    {
        "id": 163,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_7",
        "passageTitle": "E-mail: Sweeter Specialties Order",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_15.png"],
        "passageText": "Regarding the cake you ordered for March 30, our head pastry chef will produce it according to your specifications. In fact, he created a sample of the complete recipe earlier today—almond creme cake with fresh raspberry filling. We have judged it to be a delectable treat, and we are sure that you will be pleased.",
        "passageTextVi": "...Về chiếc bánh nhiều tầng bà đặt cho ngày 30 tháng 3, bếp trưởng bánh ngọt sẽ làm theo đúng yêu cầu riêng của bà. Trên thực tế, hôm nay anh ấy đã thử làm một mẫu hoàn chỉnh theo công thức—bánh kem hạnh nhân nhân quả mâm xôi tươi...",
        "questionText": "What is indicated about the multilayer cake?",
        "questionTextVi": "Điều gì được chỉ ra về chiếc bánh nhiều tầng?",
        "options": {
            "A": "It has been a best-selling product with clients.",
            "B": "It is the most expensive cake at Sweeter Specialties.",
            "C": "It is baked for Esplin Electronics annually.",
            "D": "It is a new flavor combination for Sweeter Specialties."
        },
        "optionsVi": {
            "A": "Nó là sản phẩm bán chạy nhất đối với khách hàng.",
            "B": "Nó là chiếc bánh đắt nhất tại Sweeter Specialties.",
            "C": "Nó được nướng hàng năm cho Esplin Electronics.",
            "D": "Nó là một sự kết hợp hương vị mới đối với Sweeter Specialties."
        },
        "correctAnswer": "D",
        "explanation": "Bếp trưởng làm chiếc bánh này theo yêu cầu riêng của khách ('according to your specifications') và 'he created a sample of the complete recipe earlier today' (anh ấy đã làm thử một mẫu công thức hoàn chỉnh vào đầu ngày hôm nay để nếm thử). Việc đầu bếp phải làm mẫu thử nghiệm trước cho thấy đây là một công thức phối vị mới (new flavor combination) được thiết kế riêng. Chọn (D).",
        "vocabulary": [
            { "word": "multilayer", "ipa": "/ˌmʌl.tiˈleɪ.ər/", "pos": "adj", "meaning": "nhiều tầng, nhiều lớp", "example": "A multilayer wedding cake was displayed on the table." },
            { "word": "recipe", "ipa": "/ˈres.ɪ.pi/", "pos": "n", "meaning": "công thức nấu ăn", "example": "He followed the traditional Italian recipe." }
        ],
        "collocations": [
            { "phrase": "flavor combination", "meaning": "sự kết hợp hương vị" },
            { "phrase": "according to specifications", "meaning": "theo đúng thông số / yêu cầu đặt ra" }
        ],
        "grammarPoints": [
            { "title": "Kỹ năng suy luận từ 'sample of the recipe'", "content": "Tạo mẫu (sample) để kiểm tra một công thức phối vị riêng -> New flavor combination." }
        ]
    },
    {
        "id": 164,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_7",
        "passageTitle": "E-mail: Sweeter Specialties Order",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_15.png"],
        "passageText": "We have judged it to be a delectable treat, and we are sure that you will be pleased.",
        "passageTextVi": "Chúng tôi đã đánh giá/nhận định rằng đây là một món ngon tuyệt vời...",
        "questionText": "The word 'judged' in paragraph 2, line 3, is closest in meaning to",
        "questionTextVi": "Từ 'judged' ở đoạn 2, dòng 3 gần nghĩa nhất với",
        "options": {
            "A": "criticized",
            "B": "settled",
            "C": "determined",
            "D": "described"
        },
        "optionsVi": {
            "A": "chỉ trích, phê bình",
            "B": "giải quyết, dàn xếp",
            "C": "nhận định, xác định, phán đoán",
            "D": "miêu tả"
        },
        "correctAnswer": "C",
        "explanation": "Trong câu 'We have judged it to be a delectable treat' (Chúng tôi nhận định/đánh giá rằng đây là một món bánh ngon hảo hạng), từ 'judged' mang nghĩa đánh giá, xác định sau khi xem xét/nếm thử. Do đó nó đồng nghĩa với (C) 'determined' (xác định/nhận định).",
        "vocabulary": [
            { "word": "judge", "ipa": "/dʒʌdʒ/", "pos": "v", "meaning": "đánh giá, nhận định", "example": "The jury judged her performance as flawless." },
            { "word": "delectable", "ipa": "/dɪˈlek.tə.bəl/", "pos": "adj", "meaning": "ngon lành, hảo hạng", "example": "The buffet offered a delectable selection of desserts." }
        ],
        "collocations": [
            { "phrase": "judge something to be", "meaning": "đánh giá cái gì là..." },
            { "phrase": "delectable treat", "meaning": "món ăn ngon hảo hạng" }
        ],
        "grammarPoints": [
            { "title": "Câu hỏi từ vựng đồng nghĩa trong ngữ cảnh (Vocabulary in Context)", "content": "'judge' ở đây mang nghĩa phán đoán, đánh giá sau khi kiểm chứng ('determined')." }
        ]
    },

    # 165 - 167
    {
        "id": 165,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_8",
        "passageTitle": "Product Review: Dish Magic 300 Dishwasher",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_16.png"],
        "passageText": "Great Dishwasher!\nI never had a dishwasher before. After remodeling my kitchen, I finally had room for a compact dishwasher. I did a lot of research, and the Dish Magic 300 seemed to be the best choice. It was pricier than other models, but all of the reviews were excellent. So, I decided to spend the extra money.\nI have had the dishwasher for one month now, and I could not be happier with my decision. Most importantly, the dishes come out sparkling clean, no matter how dirty they were going in. Also, the machine is so quiet, you do not even know it is running. Lastly, it is designed to use water efficiently, which is very important to me. Overall, I am very pleased with this dishwasher.\n— Anna Yakovleva",
        "passageTextVi": "Máy rửa bát tuyệt vời!\nTrước đây tôi chưa từng có một chiếc máy rửa bát nào. Sau khi cải tạo nhà bếp, cuối cùng tôi đã có chỗ cho một chiếc máy rửa bát nhỏ gọn. Tôi đã nghiên cứu rất nhiều và Dish Magic 300 dường như là sự lựa chọn tốt nhất. Nó đắt hơn các mẫu khác, nhưng tất cả các bài đánh giá đều xuất sắc. Vì vậy, tôi quyết định chi thêm tiền.\nTôi đã dùng chiếc máy rửa bát này được một tháng rồi và tôi vô cùng hài lòng với quyết định của mình. Quan trọng nhất là bát đĩa rửa xong sạch bóng loáng, bất kể lúc cho vào bẩn đến mức nào. Ngoài ra, máy chạy rất êm, bạn thậm chí không biết là nó đang hoạt động. Cuối cùng, máy được thiết kế để tiết kiệm nước hiệu quả, điều này rất quan trọng đối với tôi. Nhìn chung, tôi rất hài lòng với chiếc máy rửa bát này.\n— Anna Yakovleva",
        "questionText": "Why did Ms. Yakovleva choose the Dish Magic 300 dishwasher?",
        "questionTextVi": "Tại sao cô Yakovleva lại chọn máy rửa bát Dish Magic 300?",
        "options": {
            "A": "It was less expensive than most models.",
            "B": "It was the largest model available.",
            "C": "It was rated very highly.",
            "D": "It was the same brand as her other appliances."
        },
        "optionsVi": {
            "A": "Nó rẻ hơn hầu hết các mẫu máy khác.",
            "B": "Nó là mẫu máy lớn nhất có sẵn.",
            "C": "Nó được đánh giá rất cao.",
            "D": "Nó cùng thương hiệu với các thiết bị khác của cô ấy."
        },
        "correctAnswer": "C",
        "explanation": "Đoạn 1 nêu rõ lý do cô chọn mua dù giá cao hơn: 'It was pricier than other models, but all of the reviews were excellent' (Nó đắt hơn các dòng máy khác, nhưng tất cả các bài đánh giá đều xuất sắc). 'all reviews were excellent' tương đương với 'It was rated very highly' (Nó được đánh giá rất cao). Chọn (C).",
        "vocabulary": [
            { "word": "pricier", "ipa": "/ˈpraɪ.si.ər/", "pos": "adj", "meaning": "đắt hơn", "example": "Organic groceries are often pricier than conventional ones." },
            { "word": "remodel", "ipa": "/ˌriːˈmɒd.əl/", "pos": "v", "meaning": "cải tạo, tu sửa lại", "example": "They remodeled their kitchen with modern fixtures." }
        ],
        "collocations": [
            { "phrase": "rated highly", "meaning": "được xếp hạng / đánh giá cao" },
            { "phrase": "sparkling clean", "meaning": "sạch bóng loáng" }
        ],
        "grammarPoints": [
            { "title": "Paraphrase cụm từ đánh giá", "content": "'all of the reviews were excellent' -> 'rated very highly'." }
        ]
    },
    {
        "id": 166,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_8",
        "passageTitle": "Product Review: Dish Magic 300 Dishwasher",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_16.png"],
        "passageText": "Also, the machine is so quiet, you do not even know it is running.",
        "passageTextVi": "Ngoài ra, máy chạy rất êm, bạn thậm chí không nhận biết được rằng nó đang chạy/hoạt động.",
        "questionText": "The word 'running' in paragraph 2, line 3, is closest in meaning to",
        "questionTextVi": "Từ 'running' ở đoạn 2, dòng 3 gần nghĩa nhất với",
        "options": {
            "A": "adjusting",
            "B": "controlling",
            "C": "moving",
            "D": "operating"
        },
        "optionsVi": {
            "A": "điều chỉnh",
            "B": "kiểm soát",
            "C": "di chuyển",
            "D": "vận hành, hoạt động"
        },
        "correctAnswer": "D",
        "explanation": "Khi nói về máy móc thiết bị (the machine is running), từ 'running' có nghĩa là đang hoạt động, đang vận hành. Từ đồng nghĩa chính xác nhất là (D) 'operating'.",
        "vocabulary": [
            { "word": "operating", "ipa": "/ˈɒp.ər.eɪ.tɪŋ/", "pos": "v", "meaning": "vận hành, hoạt động", "example": "The motor is operating at maximum efficiency." }
        ],
        "collocations": [
            { "phrase": "run smoothly", "meaning": "vận hành trơn tru" }
        ],
        "grammarPoints": [
            { "title": "Nghĩa của động từ 'run' với máy móc", "content": "Động từ 'run' khi đi với chủ ngữ máy móc thiết bị mang nghĩa 'vận hành' (= operate)." }
        ]
    },
    {
        "id": 167,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_8",
        "passageTitle": "Product Review: Dish Magic 300 Dishwasher",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_16.png"],
        "passageText": "Lastly, it is designed to use water efficiently, which is very important to me. Overall, I am very pleased with this dishwasher.",
        "passageTextVi": "Cuối cùng, máy được thiết kế để sử dụng nước hiệu quả, điều này rất quan trọng đối với tôi...",
        "questionText": "What is indicated about Ms. Yakovleva?",
        "questionTextVi": "Điều gì được chỉ ra về cô Yakovleva?",
        "options": {
            "A": "She cares about saving water.",
            "B": "She recently moved to a new home.",
            "C": "She bought the dishwasher a year ago.",
            "D": "She remodels kitchens professionally."
        },
        "optionsVi": {
            "A": "Cô ấy quan tâm đến việc tiết kiệm nước.",
            "B": "Gần đây cô ấy đã chuyển đến một ngôi nhà mới.",
            "C": "Cô ấy đã mua máy rửa bát cách đây một năm.",
            "D": "Cô ấy cải tạo nhà bếp chuyên nghiệp."
        },
        "correctAnswer": "A",
        "explanation": "Cô viết: 'it is designed to use water efficiently, which is very important to me' (máy được thiết kế sử dụng nước hiệu quả/tiết kiệm, điều này rất quan trọng đối với tôi). Điều này chứng minh cô rất quan tâm đến việc tiết kiệm nước (cares about saving water). Chọn (A).",
        "vocabulary": [
            { "word": "efficiently", "ipa": "/ɪˈfɪʃ.ənt.li/", "pos": "adv", "meaning": "một cách hiệu quả, tiết kiệm năng lượng", "example": "Modern appliances utilize electricity more efficiently." }
        ],
        "collocations": [
            { "phrase": "save water", "meaning": "tiết kiệm nước" },
            { "phrase": "use water efficiently", "meaning": "sử dụng nước hiệu quả" }
        ],
        "grammarPoints": [
            { "title": "Mệnh đề quan hệ không xác định với 'which'", "content": "', which is very important to me' dùng đại từ quan hệ 'which' thay thế cho toàn bộ mệnh đề đứng trước." }
        ]
    },

    # 168 - 171
    {
        "id": 168,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_9",
        "passageTitle": "Company Information: Skyler Airlines Careers",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_17.png"],
        "passageText": "Skyler Airlines employs more than 20,000 people from all over the world. We're growing fast and have many positions available. [1] So regardless of your background, there's probably a place for you on our team. Skyler employees enjoy many perks. [2] For example, our discount program enables them to fly to any of our destinations for a fraction of the average ticket price. [3] We offer upward and global mobility, tuition reimbursement, a mentorship program, and a generous compensation package. [4] Annual paid vacations enable a comfortable work-life balance. It's no wonder that Skyler Airlines was named \"Best Airline to Work For\" by Travel Vista Journal three years in a row.",
        "passageTextVi": "Skyler Airlines sử dụng hơn 20.000 nhân viên từ khắp nơi trên thế giới. Chúng tôi đang phát triển nhanh chóng và có nhiều vị trí tuyển dụng có sẵn. [1] Vì vậy, bất kể nền tảng kinh nghiệm của bạn là gì, rất có thể luôn có một vị trí dành cho bạn trong đội ngũ của chúng tôi. Các nhân viên Skyler được hưởng rất nhiều đặc quyền. [2] Ví dụ, chương trình giảm giá của chúng tôi cho phép họ bay đến bất kỳ điểm đến nào của chúng tôi chỉ với một phần nhỏ giá vé thông thường. [3] Chúng tôi mang lại cơ hội thăng tiến và luân chuyển công tác toàn cầu, hỗ trợ học phí, chương trình cố vấn và gói đãi ngộ hào phóng. [4] Kỳ nghỉ phép có lương hàng năm mang lại sự cân bằng thoải mái giữa công việc và cuộc sống. Không có gì ngạc nhiên khi Skyler Airlines được Tạp chí Travel Vista vinh danh là \"Hãng hàng không tốt nhất để làm việc\" trong ba năm liên tiếp.",
        "questionText": "For whom is the information intended?",
        "questionTextVi": "Thông tin này dành cho đối tượng nào?",
        "options": {
            "A": "Skyler Airlines employees",
            "B": "Skyler Airlines customers",
            "C": "Potential journal subscribers",
            "D": "Current job seekers"
        },
        "optionsVi": {
            "A": "Các nhân viên hiện tại của Skyler Airlines",
            "B": "Các khách hàng của Skyler Airlines",
            "C": "Những người tiềm năng đăng ký tạp chí dài hạn",
            "D": "Những người đang tìm kiếm việc làm hiện nay"
        },
        "correctAnswer": "D",
        "explanation": "Bài viết nhằm thu hút ứng viên tuyển dụng: 'have many positions available... regardless of your background, there's probably a place for you on our team' (có nhiều vị trí đang tuyển... có một vị trí cho bạn trong đội ngũ chúng tôi). Do đó bài viết hướng đến những người đang tìm việc (Current job seekers). Chọn (D).",
        "vocabulary": [
            { "word": "perk", "ipa": "/pɜːk/", "pos": "n", "meaning": "đặc quyền, quyền lợi bổng lộc đi kèm", "example": "Company cars and gym memberships are common corporate perks." },
            { "word": "reimbursement", "ipa": "/ˌriː.ɪmˈbɜːs.mənt/", "pos": "n", "meaning": "sự hoàn trả chi phí", "example": "Submit receipts for tuition reimbursement." }
        ],
        "collocations": [
            { "phrase": "positions available", "meaning": "các vị trí tuyển dụng đang có sẵn" },
            { "phrase": "compensation package", "meaning": "gói lương thưởng và chế độ đãi ngộ" }
        ],
        "grammarPoints": [
            { "title": "Cụm giới từ 'regardless of'", "content": "'regardless of + Noun/Noun clause' mang nghĩa 'bất kể, không màng tới'." }
        ]
    },
    {
        "id": 169,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_9",
        "passageTitle": "Company Information: Skyler Airlines Careers",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_17.png"],
        "passageText": "Skyler employees enjoy many perks. For example, our discount program enables them to fly to any of our destinations for a fraction of the average ticket price. We offer upward and global mobility, tuition reimbursement, a mentorship program, and a generous compensation package. Annual paid vacations enable a comfortable work-life balance.",
        "passageTextVi": "...Các nhân viên Skyler được hưởng rất nhiều đặc quyền... chương trình giảm giá cho phép họ bay... với một phần nhỏ giá vé... hỗ trợ học phí, chương trình cố vấn... kỳ nghỉ phép có lương...",
        "questionText": "In the information, what is NOT mentioned as being offered to employees?",
        "questionTextVi": "Trong thông tin, điều gì KHÔNG được đề cập là được cung cấp cho nhân viên?",
        "options": {
            "A": "Payment for educational expenses",
            "B": "Free airline tickets",
            "C": "Opportunities for mentoring",
            "D": "Paid days off"
        },
        "optionsVi": {
            "A": "Chi trả các chi phí học tập",
            "B": "Vé máy bay miễn phí hoàn toàn",
            "C": "Cơ hội nhận sự cố vấn",
            "D": "Những ngày nghỉ phép hưởng nguyên lương"
        },
        "correctAnswer": "B",
        "explanation": "Hãy đối chiếu từng phương án:\n- (A) tương ứng với 'tuition reimbursement' (hoàn trả học phí).\n- (C) tương ứng với 'a mentorship program' (chương trình cố vấn).\n- (D) tương ứng với 'annual paid vacations' (kỳ nghỉ có lương hàng năm).\nBài chỉ nói nhân viên được giảm giá vé ('fly for a fraction of the average ticket price') chứ KHÔNG nói là vé miễn phí hoàn toàn ('free airline tickets'). Do đó chọn (B).",
        "vocabulary": [
            { "word": "fraction", "ipa": "/ˈfræk.ʃən/", "pos": "n", "meaning": "phân số, một phần nhỏ", "example": "He bought the item for a fraction of its original price." },
            { "word": "mentorship", "ipa": "/ˈmen.tɔː.ʃɪp/", "pos": "n", "meaning": "sự cố vấn hướng dẫn", "example": "The company provides strong mentorship for junior engineers." }
        ],
        "collocations": [
            { "phrase": "tuition reimbursement", "meaning": "chế độ hoàn trả học phí" },
            { "phrase": "paid days off", "meaning": "ngày nghỉ có lương" }
        ],
        "grammarPoints": [
            { "title": "Dạng câu hỏi NOT/TRUE", "content": "Phương pháp loại trừ: tìm thấy 3 chi tiết xuất hiện trong bài, phương án còn lại là đáp án cần chọn." }
        ]
    },
    {
        "id": 170,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_9",
        "passageTitle": "Company Information: Skyler Airlines Careers",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_17.png"],
        "passageText": "It's no wonder that Skyler Airlines was named \"Best Airline to Work For\" by Travel Vista Journal three years in a row.",
        "passageTextVi": "Không có gì ngạc nhiên khi Skyler Airlines được Tạp chí Travel Vista vinh danh là 'Hãng hàng không tốt nhất để làm việc' trong ba năm liên tiếp.",
        "questionText": "What is mentioned about Skyler Airlines?",
        "questionTextVi": "Điều gì được đề cập về Skyler Airlines?",
        "options": {
            "A": "It flies to the most destinations around the world.",
            "B": "It is planning to merge with another airline.",
            "C": "It has been praised by a trade publication.",
            "D": "It has replaced its seats with more comfortable ones."
        },
        "optionsVi": {
            "A": "Hãng bay đến nhiều điểm đến nhất trên khắp thế giới.",
            "B": "Hãng đang lên kế hoạch sáp nhập với một hãng hàng không khác.",
            "C": "Hãng đã được ca ngợi bởi một ấn phẩm chuyên ngành.",
            "D": "Hãng đã thay thế các ghế ngồi bằng loại thoải mái hơn."
        },
        "correctAnswer": "C",
        "explanation": "Câu cuối cho biết: 'named \"Best Airline to Work For\" by Travel Vista Journal' (được tạp chí du lịch Travel Vista bầu chọn là Hãng hàng không tốt nhất để làm việc). Travel Vista Journal là một ấn phẩm chuyên ngành ('trade publication') và việc được bầu chọn là minh chứng cho việc được ca ngợi khen thưởng ('praised'). Chọn (C).",
        "vocabulary": [
            { "word": "praise", "ipa": "/preɪz/", "pos": "v", "meaning": "khen ngợi, biểu dương", "example": "The CEO praised the team's exceptional performance." },
            { "word": "publication", "ipa": "/ˌpʌb.lɪˈkeɪ.ʃən/", "pos": "n", "meaning": "ấn phẩm, xuất bản phẩm", "example": "Trade publications cover specific industrial developments." }
        ],
        "collocations": [
            { "phrase": "three years in a row", "meaning": "ba năm liên tiếp" },
            { "phrase": "trade publication", "meaning": "ấn phẩm ngành nghề, tạp chí chuyên ngành" }
        ],
        "grammarPoints": [
            { "title": "Paraphrase tạp chí chuyên ngành", "content": "'Travel Vista Journal' được quy về khái niệm danh từ chung: 'trade publication'." }
        ]
    },
    {
        "id": 171,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_9",
        "passageTitle": "Company Information: Skyler Airlines Careers",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_17.png"],
        "passageText": "Skyler Airlines employs more than 20,000 people from all over the world. We're growing fast and have many positions available. [1] So regardless of your background, there's probably a place for you on our team. Skyler employees enjoy many perks. [2] For example, our discount program enables them to fly to any of our destinations for a fraction of the average ticket price. [3] We offer upward and global mobility, tuition reimbursement, a mentorship program, and a generous compensation package. [4] Annual paid vacations enable a comfortable work-life balance. It's no wonder that Skyler Airlines was named \"Best Airline to Work For\" by Travel Vista Journal three years in a row.",
        "passageTextVi": "...Chúng tôi đang phát triển nhanh và có nhiều vị trí tuyển dụng có sẵn. [1] Vì vậy, bất kể nền tảng kinh nghiệm của bạn là gì, rất có thể luôn có một vị trí cho bạn trong đội ngũ của chúng tôi...",
        "questionText": "In which of the positions marked [1], [2], [3], and [4] does the following sentence best belong?\n\"Our openings cover a broad range of skill sets.\"",
        "questionTextVi": "Câu sau đây phù hợp nhất ở vị trí nào trong các vị trí [1], [2], [3] và [4]?\n\"Các vị trí tuyển dụng của chúng tôi bao gồm nhiều bộ kỹ năng đa dạng.\"",
        "options": {
            "A": "[1]",
            "B": "[2]",
            "C": "[3]",
            "D": "[4]"
        },
        "optionsVi": {
            "A": "Vị trí [1]",
            "B": "Vị trí [2]",
            "C": "Vị trí [3]",
            "D": "Vị trí [4]"
        },
        "correctAnswer": "A",
        "explanation": "Câu cần điền: 'Our openings cover a broad range of skill sets' (Các vị trí tuyển dụng của chúng tôi trải rộng trên nhiều bộ kỹ năng đa dạng). Câu này liên kết hoàn hảo giữa 'have many positions available' (có nhiều vị trí tuyển dụng) ở trước vị trí [1] và kết luận 'So regardless of your background, there's probably a place for you...' (Vì thế dù bạn có nền tảng nào thì cũng có chỗ cho bạn) ngay sau vị trí [1]. Do đó chọn (A).",
        "vocabulary": [
            { "word": "openings", "ipa": "/ˈəʊ.pən.ɪŋz/", "pos": "n", "meaning": "các vị trí tuyển dụng còn trống", "example": "There are several job openings in the sales department." },
            { "word": "broad", "ipa": "/brɔːd/", "pos": "adj", "meaning": "rộng lớn, đa dạng", "example": "He has a broad knowledge of network architectures." }
        ],
        "collocations": [
            { "phrase": "job openings", "meaning": "các vị trí công việc còn trống" },
            { "phrase": "a broad range of", "meaning": "một loạt các, đa dạng các..." }
        ],
        "grammarPoints": [
            { "title": "Mối liên kết từ vựng (Lexical Cohesion)", "content": "'positions available' -> 'Our openings cover a broad range...' -> 'regardless of your background'." }
        ]
    },

    # 172 - 175
    {
        "id": 172,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_10",
        "passageTitle": "Online Chat: Presentation Slides Preparation",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_18.png", "assets/images/rc_page_19.png"],
        "passageText": "Susan Gowan 9:16 A.M.\nGood morning. The presentation slides about the new line of headphones are almost ready for distribution to our many partner stores. We are on track to send them out next Monday.\n\nMaggie Lorenz 9:17 A.M.\nHow do they look?\n\nSusan Gowan 9:20 A.M.\nThere are still some missing elements.\n\nAlan Woodson 9:21 A.M.\nWe mainly need the information from the user studies that reviewed the headphones for sport use. We should have that report from the research and development office by Wednesday.\n\nMaggie Lorenz 9:22 A.M.\nYes, let's not overlook that. And if you're concerned about the report not arriving by Wednesday, please contact Matt Harven and remind him to expedite a summary to us.\n\nSusan Gowan 9:23 A.M.\nAssuming we receive that summary soon enough to incorporate its findings into the slides, should the three of us schedule a trial run through the presentation on Thursday or Friday?\n\nMaggie Lorenz 9:24 A.M.\nLet's try for Thursday afternoon. Then we will still have Friday to make any necessary changes.\n\nAlan Woodson 9:25 A.M.\nFine by me. I'm free after 2 P.M.",
        "passageTextVi": "Susan Gowan 9:16 SA\nChào buổi sáng. Các slide thuyết trình về dòng tai nghe mới gần như đã sẵn sàng để phân phối tới nhiều cửa hàng đối tác của chúng ta. Chúng ta đang đúng tiến độ để gửi chúng đi vào thứ Hai tới.\n\nMaggie Lorenz 9:17 SA\nTrông chúng thế nào rồi?\n\nSusan Gowan 9:20 SA\nVẫn còn thiếu một vài yếu tố.\n\nAlan Woodson 9:21 SA\nChúng ta chủ yếu cần thông tin từ các nghiên cứu người dùng đánh giá tai nghe dùng cho thể thao. Chúng ta sẽ nhận được báo cáo đó từ phòng nghiên cứu và phát triển vào thứ Tư.\n\nMaggie Lorenz 9:22 SA\nĐúng vậy, chúng ta đừng bỏ qua điều đó. Và nếu bạn lo ngại về việc báo cáo không đến vào thứ Tư, vui lòng liên hệ với Matt Harven và nhắc anh ấy đẩy nhanh gửi bản tóm tắt cho chúng ta.\n\nSusan Gowan 9:23 SA\nGiả sử chúng ta nhận được bản tóm tắt đó đủ sớm để đưa kết quả vào các slide, ba chúng ta có nên lên lịch chạy thử bài thuyết trình vào thứ Năm hoặc thứ Sáu không?\n\nMaggie Lorenz 9:24 SA\nHãy sắp xếp vào chiều thứ Năm. Khi đó chúng ta vẫn còn ngày thứ Sáu để thực hiện bất kỳ thay đổi cần thiết nào.\n\nAlan Woodson 9:25 SA\nTôi đồng ý. Tôi rảnh sau 2 giờ chiều.",
        "questionText": "What is indicated about a presentation?",
        "questionTextVi": "Điều gì được chỉ ra về bài thuyết trình?",
        "options": {
            "A": "It will be expensive to produce.",
            "B": "It will highlight some best-selling products.",
            "C": "It will be Ms. Gowan's first project.",
            "D": "It will be sent to multiple locations."
        },
        "optionsVi": {
            "A": "Nó sẽ tốn kém chi phí để sản xuất.",
            "B": "Nó sẽ làm nổi bật một số sản phẩm bán chạy nhất.",
            "C": "Nó sẽ là dự án đầu tiên của cô Gowan.",
            "D": "Nó sẽ được gửi tới nhiều địa điểm khác nhau."
        },
        "correctAnswer": "D",
        "explanation": "Cô Gowan nhắn ngay đầu đoạn chat: 'The presentation slides about the new line of headphones are almost ready for distribution to our many partner stores' (Các slide thuyết trình... gần như đã sẵn sàng để gửi tới nhiều cửa hàng đối tác của chúng ta). 'distribution to our many partner stores' chứng minh tài liệu sẽ được gửi tới nhiều địa điểm (sent to multiple locations). Chọn (D).",
        "vocabulary": [
            { "word": "distribution", "ipa": "/ˌdɪs.trɪˈbjuː.ʃən/", "pos": "n", "meaning": "sự phân phối, gửi đi", "example": "The magazine has a wide international distribution." },
            { "word": "on track", "ipa": "/ɒn træk/", "pos": "idiom", "meaning": "đúng tiến độ, đúng hướng", "example": "The construction project remains on track for completion." }
        ],
        "collocations": [
            { "phrase": "on track to", "meaning": "đúng tiến độ để làm gì" },
            { "phrase": "partner stores", "meaning": "các cửa hàng đối tác" }
        ],
        "grammarPoints": [
            { "title": "Paraphrase đối tượng nhận tài liệu", "content": "'distribution to our many partner stores' -> 'sent to multiple locations'." }
        ]
    },
    {
        "id": 173,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_10",
        "passageTitle": "Online Chat: Presentation Slides Preparation",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_18.png", "assets/images/rc_page_19.png"],
        "passageText": "Alan Woodson 9:21 A.M.\nWe mainly need the information from the user studies that reviewed the headphones for sport use. We should have that report from the research and development office by Wednesday.\n\nMaggie Lorenz 9:22 A.M.\nYes, let's not overlook that. And if you're concerned about the report not arriving by Wednesday, please contact Matt Harven and remind him to expedite a summary to us.",
        "passageTextVi": "...Alan: Chúng ta chủ yếu cần thông tin từ nghiên cứu người dùng đánh giá tai nghe dùng cho thể thao... Maggie: Đúng vậy, chúng ta đừng bỏ qua điều đó...",
        "questionText": "At 9:22 A.M., what does Ms. Lorenz imply when she writes, 'let's not overlook that'?",
        "questionTextVi": "Vào lúc 9:22 sáng, cô Lorenz ngụ ý điều gì khi viết: 'let's not overlook that'?",
        "options": {
            "A": "More staff should attend a meeting.",
            "B": "Information from the user studies is important.",
            "C": "The presentation must run smoothly.",
            "D": "Partner stores must be notified about an upcoming report."
        },
        "optionsVi": {
            "A": "Nên có thêm nhân viên tham dự một cuộc họp.",
            "B": "Thông tin từ các nghiên cứu người dùng là rất quan trọng.",
            "C": "Bài thuyết trình phải diễn ra suôn sẻ.",
            "D": "Các cửa hàng đối tác phải được thông báo về một báo cáo sắp tới."
        },
        "correctAnswer": "B",
        "explanation": "Từ 'that' quy chiếu về 'the information from the user studies' mà Alan vừa đề cập ở tin nhắn trước. 'Let's not overlook that' nghĩa là 'Chúng ta đừng xem nhẹ/bỏ qua điều đó', ngụ ý thông tin từ nghiên cứu người dùng này là vô cùng quan trọng (Information from the user studies is important). Chọn (B).",
        "vocabulary": [
            { "word": "overlook", "ipa": "/ˌəʊ.vəˈlʊk/", "pos": "v", "meaning": "bỏ qua, xem nhẹ, không chú ý", "example": "Do not overlook the small details in the contract." },
            { "word": "expedite", "ipa": "/ˈek.spə.daɪt/", "pos": "v", "meaning": "đẩy nhanh tiến độ", "example": "We paid an extra fee to expedite the delivery." }
        ],
        "collocations": [
            { "phrase": "user studies", "meaning": "các cuộc nghiên cứu người dùng" },
            { "phrase": "expedite a summary", "meaning": "đẩy nhanh gửi một bản tóm tắt" }
        ],
        "grammarPoints": [
            { "title": "Đại từ quy chiếu trong hội thoại chat", "content": "'that' quy chiếu ngược lại cụm danh từ 'information from the user studies' ở câu trước." }
        ]
    },
    {
        "id": 174,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_10",
        "passageTitle": "Online Chat: Presentation Slides Preparation",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_18.png", "assets/images/rc_page_19.png"],
        "passageText": "Alan Woodson 9:21 A.M.\nWe mainly need the information from the user studies that reviewed the headphones for sport use. We should have that report from the research and development office by Wednesday.\n\nMaggie Lorenz 9:22 A.M.\nYes, let's not overlook that. And if you're concerned about the report not arriving by Wednesday, please contact Matt Harven and remind him to expedite a summary to us.",
        "passageTextVi": "...Alan: Chúng ta sẽ có báo cáo đó từ phòng nghiên cứu và phát triển (R&D) vào thứ Tư. Maggie: ...vui lòng liên hệ với Matt Harven và nhắc anh ấy đẩy nhanh gửi bản tóm tắt cho chúng ta.",
        "questionText": "Who most likely is Mr. Harven?",
        "questionTextVi": "Ông Harven nhiều khả năng nhất là ai?",
        "options": {
            "A": "A store manager",
            "B": "An amateur athlete",
            "C": "A product researcher",
            "D": "An advertising executive"
        },
        "optionsVi": {
            "A": "Một quản lý cửa hàng",
            "B": "Một vận động viên nghiệp dư",
            "C": "Một nhà nghiên cứu sản phẩm",
            "D": "Một giám đốc điều hành quảng cáo"
        },
        "correctAnswer": "C",
        "explanation": "Báo cáo người dùng về tai nghe đến từ phòng Nghiên cứu & Phát triển (research and development office). Khi lo ngại báo cáo đến muộn, họ liên hệ với Matt Harven để giục gửi bản tóm tắt kết quả nghiên cứu. Điều này cho thấy Matt Harven làm việc tại phòng R&D và là một nhà nghiên cứu sản phẩm (product researcher). Chọn (C).",
        "vocabulary": [
            { "word": "research and development", "ipa": "/rɪˈsɜːtʃ ənd dɪˈvel.əp.mənt/", "pos": "n", "meaning": "nghiên cứu và phát triển (R&D)", "example": "The company invests 10% of revenue into research and development." }
        ],
        "collocations": [
            { "phrase": "product researcher", "meaning": "chuyên viên nghiên cứu sản phẩm" },
            { "phrase": "research and development office", "meaning": "văn phòng / phòng nghiên cứu và phát triển" }
        ],
        "grammarPoints": [
            { "title": "Kỹ năng suy luận chức danh nghề nghiệp", "content": "Người phụ trách gửi báo cáo kết quả thử nghiệm của phòng R&D -> Chuyên viên nghiên cứu sản phẩm (Product Researcher)." }
        ]
    },
    {
        "id": 175,
        "part": 7,
        "partName": "Part 7: Reading Comprehension",
        "passageId": "p7_10",
        "passageTitle": "Online Chat: Presentation Slides Preparation",
        "passageType": "Single Passage",
        "pageImages": ["assets/images/rc_page_18.png", "assets/images/rc_page_19.png"],
        "passageText": "Susan Gowan 9:23 A.M.\nAssuming we receive that summary soon enough to incorporate its findings into the slides, should the three of us schedule a trial run through the presentation on Thursday or Friday?\n\nMaggie Lorenz 9:24 A.M.\nLet's try for Thursday afternoon. Then we will still have Friday to make any necessary changes.\n\nAlan Woodson 9:25 A.M.\nFine by me. I'm free after 2 P.M.",
        "passageTextVi": "...Susan: ...chúng ta có nên lên lịch chạy thử bài thuyết trình vào thứ Năm hoặc thứ Sáu không? Maggie: Hãy chọn chiều thứ Năm nhé... Alan: Tôi đồng ý. Tôi rảnh sau 2 giờ chiều.",
        "questionText": "When do the writers plan to meet to review a slide presentation?",
        "questionTextVi": "Khi nào những người viết dự định gặp nhau để xem lại bài thuyết trình slide?",
        "options": {
            "A": "On Monday",
            "B": "On Wednesday",
            "C": "On Thursday",
            "D": "On Friday"
        },
        "optionsVi": {
            "A": "Vào thứ Hai",
            "B": "Vào thứ Tư",
            "C": "Vào thứ Năm",
            "D": "Vào thứ Sáu"
        },
        "correctAnswer": "C",
        "explanation": "Maggie đề xuất: 'Let's try for Thursday afternoon' (Hãy chọn chiều thứ Năm nhé). Alan đồng ý: 'Fine by me. I'm free after 2 P.M.' (Tôi nhất trí. Tôi rảnh sau 2 giờ chiều). Cả nhóm đã thống nhất buổi chạy thử (trial run) vào chiều thứ Năm. Do đó chọn (C) 'On Thursday'.",
        "vocabulary": [
            { "word": "trial run", "ipa": "/ˈtraɪəl rʌn/", "pos": "n", "meaning": "buổi tập dượt, chạy thử nghiệm", "example": "We conducted a trial run before the actual software launch." },
            { "word": "incorporate", "ipa": "/ɪnˈkɔː.pər.eɪt/", "pos": "v", "meaning": "kết hợp, đưa vào", "example": "The new design incorporates feedback from customers." }
        ],
        "collocations": [
            { "phrase": "trial run", "meaning": "buổi diễn tập, buổi chạy thử" },
            { "phrase": "fine by me", "meaning": "tôi đồng ý, với tôi thế là ổn" }
        ],
        "grammarPoints": [
            { "title": "Giới từ chỉ ngày trong tuần", "content": "Sử dụng 'on' trước các thứ trong tuần: 'on Thursday', 'on Friday'." }
        ]
    }
]

if __name__ == "__main__":
    print(f"P7 Part 2 loaded with {len(P7_PART2)} questions.")
