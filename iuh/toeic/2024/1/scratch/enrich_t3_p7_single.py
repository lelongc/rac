# scratch/enrich_t3_p7_single.py: In-depth enrichment for Test 3 RC Part 7 Single Passages (Q147 - Q175)
import json

p7_single = {}

# Pass 1: 147 - 148 (Medillo Shoes Celebrates Twenty Years)
p7_single[147] = {
    "exp": "Đoạn quảng cáo viết rõ: 'To thank our loyal customers on May 10, all footwear in the store will be offered at a 30 percent discount' (Để cảm ơn những khách hàng thân thiết vào ngày 10 tháng 5, tất cả giày dép trong cửa hàng sẽ được giảm giá 30%) -> Vào ngày 10 tháng 5, toàn bộ giày dép sẽ được giảm giá ('All shoes will be discounted'). Phương án (A) là đáp án chính xác duy nhất. Các phương án khác: (B) tuyển nhân viên, (C) ngừng một mẫu giày, (D) chuyển sang địa điểm mới đều sai lệch thông tin.",
    "vocab": [
        {"word": "footwear", "ipa": "/ˈfʊt.weər/", "pos": "n", "meaning": "giày dép nói chung (tất cả các loại)", "example": "The athletic store stocks footwear for hiking and running."},
        {"word": "discount", "ipa": "/ˈdɪs.kaʊnt/", "pos": "v, n", "meaning": "giảm giá; khoản tiền giảm", "example": "Selected winter boots are discounted by 20 percent."},
        {"word": "loyal", "ipa": "/ˈlɔɪ.əl/", "pos": "adj", "meaning": "trung thành, gắn bó thân thiết", "example": "Loyal patrons receive exclusive coupons via email."}
    ],
    "collocations": [{"phrase": "loyal customers", "meaning": "khách hàng thân thiết"}, {"phrase": "offered at a discount", "meaning": "được bán giảm giá"}],
    "grammar": [{"title": "Kỹ thuật Paraphrasing danh từ tổng quát", "rule": "footwear = shoes (giày dép)", "content": "Bài đọc dùng từ bao quát 'footwear', câu hỏi dùng danh từ quen thuộc 'shoes'."}]
}

p7_single[148] = {
    "exp": "Đoạn văn viết ở dòng tiêu đề: 'Medillo Shoes Celebrates Twenty Years in Cape Town! 246 Breda Place' và dòng cuối: 'Parking is available behind the store' (Có bãi đỗ xe phía sau cửa hàng) -> Phương án (D) 'It has customer parking' (Cửa hàng có chỗ đỗ xe cho khách) là nhận định chính xác. Các phương án: (A) sai vì đã hoạt động 20 năm chứ không phải 10 năm ('Twenty Years'), (B) sai vì bán giày thông thường chứ không chuyên đồ thể thao, (C) sai vì không nhắc tới vị trí cạnh thư viện.",
    "vocab": [
        {"word": "available", "ipa": "/əˈveɪ.lə.bəl/", "pos": "adj", "meaning": "có sẵn, hiện hữu để sử dụng", "example": "Complimentary parking is available in the garage."},
        {"word": "celebrate", "ipa": "/ˈsel.ə.breɪt/", "pos": "v", "meaning": "kỷ niệm, ăn mừng", "example": "The family restaurant celebrated its diamond jubilee."},
        {"word": "patron", "ipa": "/ˈpeɪ.trən/", "pos": "n", "meaning": "khách hàng quen, người lui tới", "example": "Patrons enjoy free Wi-Fi in the cafe lounge."}
    ],
    "collocations": [{"phrase": "parking is available", "meaning": "có chỗ đỗ xe"}, {"phrase": "celebrate an anniversary", "meaning": "kỷ niệm ngày thành lập"}]
}

# Pass 2: 149 - 150 (Email from Neil Cullen to Sales Team)
p7_single[149] = {
    "exp": "Bức thư mở đầu: 'I am writing to share some exciting news regarding our team structure. Effective next Monday, Elena Soroka will assume the role of Senior Account Lead...' (Tôi viết thư này để chia sẻ tin tức thú vị liên quan đến cơ cấu đội ngũ của chúng ta. Có hiệu lực từ thứ Hai tới, Elena Soroka sẽ đảm nhận vị trí Trưởng nhóm Quản lý Khách hàng Cấp cao...) -> Mục đích của email là thông báo cho đồng nghiệp về sự thăng chức nhân sự ('To inform coworkers of a promotion'). Phương án (D) là đáp án chính xác.",
    "vocab": [
        {"word": "promotion", "ipa": "/prəˈməʊ.ʃən/", "pos": "n", "meaning": "sự thăng chức, đề bạt nhân sự", "example": "Her outstanding performance earned her a swift promotion."},
        {"word": "assume", "ipa": "/əˈsjuːm/", "pos": "v", "meaning": "đảm đương, tiếp quản (vị trí/trách nhiệm)", "example": "He will assume the duties of acting director next month."},
        {"word": "effective", "ipa": "/ɪˈfek.tɪv/", "pos": "adj", "meaning": "có hiệu lực kể từ ngày", "example": "The revised dress code becomes effective on June 1."}
    ],
    "collocations": [{"phrase": "assume the role of", "meaning": "tiếp quản vai trò"}, {"phrase": "effective next Monday", "meaning": "có hiệu lực từ thứ Hai tới"}],
    "grammar": [{"title": "Cụm phân từ 'Effective + thời gian' chỉ mốc bắt đầu áp dụng", "rule": "Effective + Date / Day, S + will + V", "content": "Cụm từ chuẩn mực dùng trong thư thông cáo nội bộ công ty để xác định ngày quyết định có hiệu lực thi hành."}]
}

p7_single[150] = {
    "exp": "Đoạn văn viết: 'In her new capacity, Elena will manage our major enterprise accounts, which she previously supported as an associate' (Trên cương vị mới, Elena sẽ quản lý các tài khoản khách hàng doanh nghiệp lớn của chúng ta, nhóm tài khoản mà cô từng hỗ trợ với vai trò cộng sự viên) -> Cô Soroka có kinh nghiệm làm việc với các tài khoản này từ trước ('She has worked with large accounts before'). Phương án (B) là đáp án chính xác.",
    "vocab": [
        {"word": "capacity", "ipa": "/kəˈpæs.ə.ti/", "pos": "n", "meaning": "tư cách, cương vị công tác", "example": "In his capacity as auditor, he scrutinized the expenses."},
        {"word": "enterprise account", "ipa": "/ˈen.tə.praɪz əˌkaʊnt/", "pos": "n phr", "meaning": "tài khoản khách hàng doanh nghiệp lớn", "example": "Enterprise accounts generate steady recurring revenue."},
        {"word": "previously", "ipa": "/ˈpriː.vi.əs.li/", "pos": "adv", "meaning": "trước đây, trước đó", "example": "She previously worked as a corporate paralegal."}
    ],
    "collocations": [{"phrase": "in her new capacity", "meaning": "trên cương vị mới của cô ấy"}, {"phrase": "enterprise accounts", "meaning": "tài khoản doanh nghiệp lớn"}]
}

# Pass 3: 151 - 152 (City of Bryan Building Permit Office notice)
p7_single[151] = {
    "exp": "Bản thông báo nêu rõ: 'Beginning August 1, all applications for residential and commercial building permits must be submitted through our new digital portal instead of in person' (Bắt đầu từ ngày 1 tháng 8, tất cả đơn xin cấp phép xây dựng nhà ở và thương mại phải được nộp qua cổng điện tử mới thay vì nộp trực tiếp) -> Văn phòng cấp phép chuyển sang tiếp nhận hồ sơ trực tuyến ('Requiring online permit submissions'). Phương án (C) là đáp án đúng.",
    "vocab": [
        {"word": "permit", "ipa": "/ˈpɜː.mɪt/", "pos": "n", "meaning": "giấy phép chính thức (xây dựng, đỗ xe)", "example": "Contractors must obtain a building permit before excavating."},
        {"word": "portal", "ipa": "/ˈpɔː.təl/", "pos": "n", "meaning": "cổng thông tin điện tử", "example": "Upload architectural blueprints through the municipal portal."},
        {"word": "in person", "ipa": "/ɪn ˈpɜː.sən/", "pos": "adv phr", "meaning": "trực tiếp bằng xương bằng thịt", "example": "Submit visa renewal applications online or in person."}
    ],
    "collocations": [{"phrase": "building permit", "meaning": "giấy phép xây dựng"}, {"phrase": "submit through a portal", "meaning": "nộp qua cổng thông tin"}]
}

p7_single[152] = {
    "exp": "Đoạn văn nêu lý do: 'This transition will significantly expedite review times and eliminate paperwork backlogs' (Sự chuyển đổi này sẽ đẩy nhanh đáng kể thời gian xét duyệt và loại bỏ tình trạng hồ sơ giấy tờ bị tồn đọng) -> Lý do là để rút ngắn thời gian xử lý hồ sơ ('To speed up processing times'). Paraphrasing: expedite review times -> speed up processing times. Phương án (A) là đáp án đúng.",
    "vocab": [
        {"word": "expedite", "ipa": "/ˈek.spə.daɪt/", "pos": "v", "meaning": "xúc tiến, đẩy nhanh tiến độ", "example": "Pay an additional fee to expedite passport renewal."},
        {"word": "backlog", "ipa": "/ˈbæk.lɒɡ/", "pos": "n", "meaning": "lượng công việc/hồ sơ tồn đọng", "example": "Hiring temp staff helped clear the invoice backlog."},
        {"word": "processing", "ipa": "/ˈprəʊ.ses.ɪŋ/", "pos": "n", "meaning": "sự xử lý, xét duyệt", "example": "Electronic filing minimizes document processing time."}
    ],
    "collocations": [{"phrase": "expedite review times", "meaning": "đẩy nhanh thời gian xét duyệt"}, {"phrase": "clear a backlog", "meaning": "giải quyết lượng việc tồn đọng"}],
    "grammar": [{"title": "Paraphrasing động từ chỉ sự đẩy nhanh tốc độ", "rule": "expedite = speed up = accelerate", "content": "Từ vựng học thuật 'expedite' trong văn bản thường được kiểm tra bằng cụm động từ thông dụng 'speed up'."}]
}

# Pass 4: 153 - 155 (River tour receipt for Mr. Califf)
p7_single[153] = {
    "exp": "Phiếu biên nhận nêu rõ chi tiết hành trình: 'Vessel departs promptly from Pier 4 at 10:00 A.M. Complimentary coffee and snacks are provided onboard' (Tàu khởi hành đúng 10:00 sáng từ Cầu cảng số 4. Cà phê và đồ ăn nhẹ miễn phí được phục vụ trên tàu) -> Chuyến du ngoạn có phục vụ đồ ăn thức uống ('Food and beverages are included'). Phương án (B) là đáp án chính xác.",
    "vocab": [
        {"word": "vessel", "ipa": "/ˈves.əl/", "pos": "n", "meaning": "tàu thủy, thuyền lớn", "example": "The passenger vessel navigated the scenic waterway."},
        {"word": "complimentary", "ipa": "/ˌkɒm.plɪˈmen.tər.i/", "pos": "adj", "meaning": "miễn phí (được phục vụ kèm)", "example": "Guests enjoy a complimentary buffet breakfast."},
        {"word": "onboard", "ipa": "/ˈɒn.bɔːd/", "pos": "adj, adv", "meaning": "ở trên tàu/máy bay", "example": "Wi-Fi connectivity is available onboard the ferry."}
    ],
    "collocations": [{"phrase": "complimentary snacks", "meaning": "đồ ăn nhẹ miễn phí"}, {"phrase": "depart promptly", "meaning": "khởi hành đúng giờ"}]
}

p7_single[154] = {
    "exp": "Đối chiếu bảng chi tiết đơn hàng trên biên nhận: 'Adult Admission: 2 x $35.00 = $70.00; Youth Admission: 1 x $20.00 = $20.00. Total Tickets: 3' (Vé người lớn: 2 vé; Vé trẻ em: 1 vé. Tổng cộng: 3 vé) -> Ông Califf đã mua 3 vé ('3'). Phương án (C) là đáp án chính xác.",
    "vocab": [
        {"word": "admission", "ipa": "/ədˈmɪʃ.ən/", "pos": "n", "meaning": "vé vào cổng, quyền vào cửa", "example": "General admission tickets cost twenty dollars each."},
        {"word": "receipt", "ipa": "/rɪˈsiːt/", "pos": "n", "meaning": "hóa đơn, biên lai thu tiền", "example": "Present the digital receipt at the boarding gate."},
        {"word": "quantity", "ipa": "/ˈkwɒn.tə.ti/", "pos": "n", "meaning": "số lượng", "example": "Specify the desired quantity of tickets during checkout."}
    ],
    "collocations": [{"phrase": "admission ticket", "meaning": "vé vào cửa"}, {"phrase": "total amount", "meaning": "tổng số tiền"}]
}

p7_single[155] = {
    "exp": "Dòng ghi chú dưới cùng của biên lai viết: 'Present this receipt within 14 days to receive 15% off any Historic Walking Tour booked in person at our visitor center' (Xuất trình biên lai này trong vòng 14 ngày để được giảm giá 15% cho bất kỳ Tour đi bộ lịch sử nào được đặt trực tiếp tại trung tâm du khách) -> Khách hàng được giảm giá bằng cách xuất trình phiếu thu ('By showing a receipt'). Phương án (D) là đáp án chính xác.",
    "vocab": [
        {"word": "present", "ipa": "/prɪˈzent/", "pos": "v", "meaning": "xuất trình, đưa ra (giấy tờ/biên lai)", "example": "Present a valid photo ID upon boarding the aircraft."},
        {"word": "discount", "ipa": "/ˈdɪs.kaʊnt/", "pos": "n", "meaning": "mức giảm giá", "example": "Show your student card for a ten percent discount."},
        {"word": "walking tour", "ipa": "/ˈwɔː.kɪŋ tʊər/", "pos": "n", "meaning": "tour du lịch đi bộ khám phá", "example": "The walking tour explores colonial architectural heritage."}
    ],
    "collocations": [{"phrase": "present a receipt", "meaning": "xuất trình hóa đơn"}, {"phrase": "receive a discount", "meaning": "nhận được ưu đãi giảm giá"}]
}

# Pass 5: 156 - 157 (Text-message chain: Mr. Kwon & Ms. Saunders)
p7_single[156] = {
    "exp": "Lúc 8:10 A.M., cô Saunders nhắn: 'The client wants the proposal revised by noon today, which seems impossible given our current staffing' (Khách hàng muốn bản đề xuất được sửa xong trước buổi trưa nay, điều này có vẻ bất khả thi với quân số hiện tại của chúng ta). Lúc 8:12 A.M., ông Kwon đáp: 'I have some bandwidth' (Tôi có chút thời gian/năng lực rảnh rỗi) -> Ông Kwon ngụ ý rằng ông ấy có thể hỗ trợ cô Saunders xử lý công việc ('He is available to help'). Phương án (B) là đáp án đúng.",
    "vocab": [
        {"word": "bandwidth", "ipa": "/ˈbænd.wɪtʃ/", "pos": "n (idiom)", "meaning": "thời gian/năng lực xử lý công việc", "example": "I don't have the bandwidth to take on an extra client right now."},
        {"word": "proposal", "ipa": "/prəˈpəʊ.zəl/", "pos": "n", "meaning": "bản đề xuất dự án", "example": "The marketing proposal outlines three launch strategies."},
        {"word": "revise", "ipa": "/rɪˈvaɪz/", "pos": "v", "meaning": "sửa đổi, hiệu đính tài liệu", "example": "Revise the executive summary before printing."}
    ],
    "collocations": [{"phrase": "have bandwidth", "meaning": "có thời gian/khả năng đảm đương việc"}, {"phrase": "revise a proposal", "meaning": "chỉnh sửa bản đề xuất"}],
    "grammar": [{"title": "Thuật ngữ văn phòng mang nghĩa bóng (Corporate Jargon)", "rule": "bandwidth = time / capacity to take on tasks", "content": "Trong tiếng Anh công sở hiện đại, 'bandwidth' thường được dùng để chỉ quỹ thời gian hoặc năng lực xử lý việc của một cá nhân."}]
}

p7_single[157] = {
    "exp": "Sau khi ông Kwon ngỏ ý giúp, cô Saunders nhắn: 'That would be a lifesaver! Let me email you the financial section right away so you can review the budget projections' (Thế thì cứu tinh rồi! Để tôi email cho anh phần tài chính ngay bây giờ để anh xem xét các dự toán ngân sách) -> Hành động tiếp theo của cô Saunders là gửi tài liệu cho ông Kwon ('Send a document to Mr. Kwon'). Phương án (C) là đáp án đúng.",
    "vocab": [
        {"word": "lifesaver", "ipa": "/ˈlaɪfˌseɪ.vər/", "pos": "n", "meaning": "vị cứu tinh, sự cứu nguy kịp thời", "example": "Your quick assistance was an absolute lifesaver."},
        {"word": "projections", "ipa": "/prəˈdʒek.ʃənz/", "pos": "n pl", "meaning": "dự toán, số liệu dự báo", "example": "Financial projections show robust revenue growth next fiscal year."},
        {"word": "budget", "ipa": "/ˈbʌdʒ.ɪt/", "pos": "n", "meaning": "ngân sách chi tiêu", "example": "Stay strictly within the allocated department budget."}
    ],
    "collocations": [{"phrase": "send a document", "meaning": "gửi tài liệu"}, {"phrase": "budget projections", "meaning": "các dự toán ngân sách"}]
}

# Pass 6: 158 - 160 (Letter from Kipbank Business to Ms. Omar)
p7_single[158] = {
    "exp": "Bức thư viết: 'Dear Ms. Omar, Thank you for choosing Kipbank for your company's banking needs. As the authorized administrator for Omar Logistics, you can now manage employee spending limits...' (Kính gửi cô Omar, Cảm ơn cô đã chọn Kipbank... Với tư cách là người quản trị được ủy quyền của công ty Omar Logistics, giờ đây cô có thể quản lý hạn mức chi tiêu của nhân viên...) -> Cô Omar là người điều hành một doanh nghiệp ('She runs a business'). Phương án (C) là đáp án chính xác.",
    "vocab": [
        {"word": "administrator", "ipa": "/ədˈmɪn.ɪ.streɪ.tər/", "pos": "n", "meaning": "người quản trị, điều hành", "example": "System administrators manage network security protocols."},
        {"word": "authorized", "ipa": "/ˈɔː.θər.aɪzd/", "pos": "adj", "meaning": "được ủy quyền chính thức", "example": "Only authorized personnel may enter the server room."},
        {"word": "logistics", "ipa": "/ləˈdʒɪs.tɪks/", "pos": "n pl", "meaning": "ngành hậu cần, vận tải hàng hóa", "example": "Third-party logistics firms handle international warehousing."}
    ],
    "collocations": [{"phrase": "authorized administrator", "meaning": "người quản trị được ủy quyền"}, {"phrase": "spending limits", "meaning": "hạn mức chi tiêu"}]
}

p7_single[159] = {
    "exp": "Đoạn văn viết: 'The five corporate credit cards you requested for your sales drivers are enclosed. Please note that each card is currently inactive until activated through our corporate portal' (Năm chiếc thẻ tín dụng doanh nghiệp cô yêu cầu cho các tài xế bán hàng đã được đính kèm. Xin lưu ý rằng mỗi thẻ hiện đang chưa kích hoạt cho đến khi được kích hoạt qua cổng thông tin doanh nghiệp) -> Những chiếc thẻ tín dụng cần phải được kích hoạt trước khi dùng ('They must be activated before use'). Phương án (C) là đáp án đúng.",
    "vocab": [
        {"word": "activate", "ipa": "/ˈæk.tɪ.veɪt/", "pos": "v", "meaning": "kích hoạt (thẻ, tài khoản)", "example": "Activate your new debit card at any local ATM."},
        {"word": "enclosed", "ipa": "/ɪnˈkləʊzd/", "pos": "adj", "meaning": "được đính kèm theo thư", "example": "Please find enclosed the signed licensing agreement."},
        {"word": "corporate card", "ipa": "/ˈkɔː.pər.ət kɑːd/", "pos": "n", "meaning": "thẻ tín dụng doanh nghiệp", "example": "Charge travel expenses directly to the corporate card."}
    ],
    "collocations": [{"phrase": "corporate credit cards", "meaning": "thẻ tín dụng doanh nghiệp"}, {"phrase": "activate a card", "meaning": "kích hoạt thẻ"}]
}

p7_single[160] = {
    "exp": "Câu cần điền: 'This security feature ensures that unauthorized persons cannot use them if intercepted in the mail.' (Tính năng bảo mật này đảm bảo rằng người không có thẩm quyền không thể sử dụng chúng nếu thư bị chặn trên đường bưu điện). Vị trí [1] đứng ngay sau câu thông báo rằng các thẻ hiện đang ở trạng thái chưa kích hoạt ('each card is currently inactive until activated'). Đại từ 'This security feature' liên kết chặt chẽ với quy định chưa kích hoạt để bảo mật. Phương án (A) '[1]' là vị trí chính xác nhất.",
    "vocab": [
        {"word": "intercept", "ipa": "/ˌɪn.təˈsept/", "pos": "v", "meaning": "chặn bắt, thu giữ trên đường vận chuyển", "example": "Customs agents intercepted the counterfeit cargo."},
        {"word": "security feature", "ipa": "/sɪˈkjʊə.rə.ti ˈfiː.tʃər/", "pos": "n", "meaning": "tính năng bảo mật", "example": "The passport includes holographic security features."},
        {"word": "unauthorized", "ipa": "/ʌnˈɔː.θər.aɪzd/", "pos": "adj", "meaning": "trái phép, không được phép", "example": "Unauthorized access to internal files is strictly prohibited."}
    ],
    "collocations": [{"phrase": "security feature", "meaning": "tính năng bảo mật"}, {"phrase": "unauthorized persons", "meaning": "những người không có thẩm quyền"}],
    "grammar": [{"title": "Kỹ thuật điền câu có đại từ chỉ định 'This + Noun'", "rule": "Sentence with feature (inactive cards) -> This security feature ensures...", "content": "Cụm 'This security feature' bắt buộc phải quy chiếu trực tiếp về biện pháp kỹ thuật vừa được nhắc tới ngay câu trước."}]
}

# Pass 7: 161 - 163 (Article on Carila Corporation)
p7_single[161] = {
    "exp": "Bài báo đưa tin: 'Carila Corporation announced on Tuesday that it has finalized the purchase of Nexor Systems, an Ottawa-based artificial intelligence startup...' (Tập đoàn Carila thông báo vào hôm thứ Ba rằng họ đã hoàn tất việc mua lại Nexor Systems, một công ty khởi nghiệp trí tuệ nhân tạo có trụ sở tại Ottawa...) -> Mục đích bài báo là tường thuật về một thương vụ thâu tóm công ty ('To report on a business acquisition'). Phương án (C) là đáp án chính xác.",
    "vocab": [
        {"word": "acquisition", "ipa": "/ˌæk.wɪˈzɪʃ.ən/", "pos": "n", "meaning": "sự mua lại, thâu tóm doanh nghiệp", "example": "The merger and acquisition reshaped the telecom market."},
        {"word": "finalize", "ipa": "/ˈfaɪ.nəl.aɪz/", "pos": "v", "meaning": "hoàn tất, chốt lại (thỏa thuận)", "example": "Attorneys worked through the night to finalize the contract."},
        {"word": "startup", "ipa": "/ˈstɑːt.ʌp/", "pos": "n", "meaning": "công ty khởi nghiệp", "example": "Venture capital firms invest heavily in promising tech startups."}
    ],
    "collocations": [{"phrase": "business acquisition", "meaning": "thương vụ mua lại doanh nghiệp"}, {"phrase": "finalize a purchase", "meaning": "hoàn tất việc mua lại"}]
}

p7_single[162] = {
    "exp": "Đoạn 2 của bài báo nêu: 'Industry analysts note that Carila has struggled in recent quarters to integrate cloud services into its hardware line, lagging behind rival manufacturers' (Các nhà phân tích trong ngành lưu ý rằng Carila đã gặp nhiều khó khăn trong những quý gần đây để tích hợp dịch vụ đám mây vào dòng phần cứng, tụt hậu so với các nhà sản xuất đối thủ) -> Carila đang gặp khó khăn trong việc phát triển công nghệ của riêng mình ('It has had difficulty developing its own technology'). Phương án (B) là đáp án đúng.",
    "vocab": [
        {"word": "lag behind", "ipa": "/læɡ bɪˈhaɪnd/", "pos": "phr v", "meaning": "tụt hậu lại phía sau", "example": "Companies that resist automation lag behind industry peers."},
        {"word": "struggle", "ipa": "/ˈstrʌɡ.əl/", "pos": "v", "meaning": "vật lộn, gặp nhiều trở ngại khó khăn", "example": "Small retailers struggle against giant e-commerce platforms."},
        {"word": "integrate", "ipa": "/ˈɪn.tɪ.ɡreɪt/", "pos": "v", "meaning": "tích hợp, kết hợp nhuần nhuyễn", "example": "Integrate customer relationship management with accounting tools."}
    ],
    "collocations": [{"phrase": "lag behind rivals", "meaning": "tụt hậu so với các đối thủ"}, {"phrase": "integrate services", "meaning": "tích hợp các dịch vụ"}]
}

p7_single[163] = {
    "exp": "Căn cứ ngữ cảnh đoạn 3, dòng 6: 'Nexor's proprietary algorithm provides an elegant solution to data bottlenecking across distributed networks' (Thuật toán độc quyền của Nexor cung cấp một giải pháp / phương án giải quyết vấn đề tinh gọn đối với sự nghẽn cổ chai dữ liệu trên các mạng phân tán). Từ 'solution' trong ngữ cảnh này đồng nghĩa với 'fix / answer / remedy' (cách giải quyết vấn đề). Phương án (D) 'answer' là từ có nghĩa tương đương nhất. Các phương án khác: (A) hỗn hợp hóa học (liquid mixture), (B) lời giải thích (explanation), (C) đề xuất hợp tác.",
    "vocab": [
        {"word": "solution", "ipa": "/səˈluː.ʃən/", "pos": "n", "meaning": "giải pháp, cách tháo gỡ khó khăn", "example": "Engineers developed an energy-efficient cooling solution."},
        {"word": "answer", "ipa": "/ˈɑːn.sər/", "pos": "n", "meaning": "giải pháp hữu hiệu, câu trả lời cho vấn đề", "example": "Renewable energy is the answer to fossil fuel depletion."},
        {"word": "proprietary", "ipa": "/prəˈpraɪə.tər.i/", "pos": "adj", "meaning": "độc quyền, thuộc quyền sở hữu riêng", "example": "The firm protects its proprietary software algorithms fiercely."}
    ],
    "collocations": [{"phrase": "elegant solution", "meaning": "giải pháp tinh gọn/thanh lịch"}, {"phrase": "provide a solution", "meaning": "đưa ra giải pháp"}]
}

# Pass 8: 164 - 167 (Commbolt internet advertisement & referral rewards)
p7_single[164] = {
    "exp": "Đoạn quảng cáo nêu ưu điểm của dịch vụ Commbolt: 'With Commbolt Fiber, you enjoy guaranteed 99.9% uptime and round-the-clock technical support with no long-term contracts required' (Với Commbolt Fiber, bạn tận hưởng thời gian hoạt động đảm bảo 99.9% và hỗ trợ kỹ thuật 24/7 mà không yêu cầu hợp đồng dài hạn) -> Lợi ích được nhắc đến là không có hợp đồng dài hạn ràng buộc ('No long-term contracts'). Phương án (B) là đáp án chính xác.",
    "vocab": [
        {"word": "contract", "ipa": "/ˈkɒn.trækt/", "pos": "n", "meaning": "hợp đồng cam kết", "example": "Sign a one-year service contract to lock in monthly rates."},
        {"word": "uptime", "ipa": "/ˈʌp.taɪm/", "pos": "n", "meaning": "thời gian hệ thống vận hành liên tục không lỗi", "example": "Enterprise cloud providers guarantee 99.99% server uptime."},
        {"word": "round-the-clock", "ipa": "/ˌraʊnd.ðəˈklɒk/", "pos": "adj", "meaning": "suốt ngày đêm, 24/7", "example": "The call center provides round-the-clock technical support."}
    ],
    "collocations": [{"phrase": "long-term contracts", "meaning": "hợp đồng dài hạn"}, {"phrase": "round-the-clock support", "meaning": "hỗ trợ kỹ thuật suốt ngày đêm"}]
}

p7_single[165] = {
    "exp": "Đoạn văn quy định chương trình giới thiệu: 'Receive a $50 billing credit for each friend who signs up for Commbolt Fiber. If your referred friend also adds home phone service, you earn an additional $25 bonus credit, up to a maximum total of $75 per referral' (Nhận 50 USD giảm trừ hóa đơn cho mỗi người bạn đăng ký... Nếu người bạn đó đăng ký thêm dịch vụ điện thoại bàn, bạn nhận thêm 25 USD, tối đa lên tới 75 USD cho mỗi lượt giới thiệu) -> Số tiền tối đa nhận được cho một người bạn giới thiệu là 75 USD ('$75'). Phương án (B) là đáp án đúng.",
    "vocab": [
        {"word": "credit", "ipa": "/ˈkred.ɪt/", "pos": "n", "meaning": "khoản tiền giảm trừ trên hóa đơn", "example": "A $20 promotional credit was applied to your monthly bill."},
        {"word": "referral", "ipa": "/rɪˈfɜː.rəl/", "pos": "n", "meaning": "sự giới thiệu khách hàng mới", "example": "Earn bonuses through our customer referral rewards program."},
        {"word": "maximum", "ipa": "/ˈmæk.sɪ.məm/", "pos": "n, adj", "meaning": "mức tối đa", "example": "The grant covers up to a maximum of $5,000 in tuition."}
    ],
    "collocations": [{"phrase": "billing credit", "meaning": "tiền giảm trừ hóa đơn"}, {"phrase": "per referral", "meaning": "cho mỗi lượt giới thiệu"}]
}

p7_single[166] = {
    "exp": "Đoạn văn ghi chú điều kiện chương trình: 'Referral credits are applied directly to your future monthly statements and cannot be redeemed for cash' (Các khoản tín dụng giới thiệu được áp dụng trực tiếp vào các kỳ sao kê hóa đơn hàng tháng tương lai của bạn và không thể quy đổi ra tiền mặt) -> Khoản ưu đãi được trừ vào các hóa đơn tương lai ('It is applied to future bills'). Phương án (D) là đáp án chính xác.",
    "vocab": [
        {"word": "statement", "ipa": "/ˈsteɪt.mənt/", "pos": "n", "meaning": "bản sao kê hóa đơn tài khoản", "example": "Check your monthly credit card statement for discrepancies."},
        {"word": "redeem", "ipa": "/rɪˈdiːm/", "pos": "v", "meaning": "quy đổi thành tiền hoặc nhận quà", "example": "Reward points cannot be redeemed for cash disbursements."},
        {"word": "apply", "ipa": "/əˈplaɪ/", "pos": "v", "meaning": "áp dụng, khấu trừ vào", "example": "The promotional discount applies automatically at checkout."}
    ],
    "collocations": [{"phrase": "apply to bills", "meaning": "khấu trừ vào các hóa đơn"}, {"phrase": "redeemed for cash", "meaning": "quy đổi ra tiền mặt"}]
}

p7_single[167] = {
    "exp": "Câu cần điền: 'Existing customers can generate this unique link by logging into their Commbolt portal account.' (Khách hàng hiện tại có thể tạo liên kết độc nhất này bằng cách đăng nhập vào tài khoản cổng thông tin Commbolt của họ). Đại từ 'this unique link' (liên kết độc nhất này) bắt buộc phải đứng ngay sau câu nhắc đến đường dẫn giới thiệu bạn bè ('Share your personalized referral link via email or social media...'). Vị trí [3] là vị trí chuẩn xác nhất. Phương án (C) là đáp án đúng.",
    "vocab": [
        {"word": "unique link", "ipa": "/juːˈniːk lɪŋk/", "pos": "n phr", "meaning": "đường dẫn liên kết độc nhất vô nhị", "example": "Share your unique link with friends to earn referral bonuses."},
        {"word": "generate", "ipa": "/ˈdʒen.ə.reɪt/", "pos": "v", "meaning": "tạo ra, sinh ra (mã/đường link)", "example": "The software generates a secure one-time passcode."},
        {"word": "log into", "ipa": "/lɒɡ ˈɪn.tuː/", "pos": "phr v", "meaning": "đăng nhập vào hệ thống", "example": "Log into your employee profile to submit expense claims."}
    ],
    "collocations": [{"phrase": "generate a link", "meaning": "tạo một đường dẫn liên kết"}, {"phrase": "log into an account", "meaning": "đăng nhập vào tài khoản"}],
    "grammar": [{"title": "Quy tắc móc xích thông tin (Cohesive Ties)", "rule": "Mention a link -> Existing customers can generate this unique link...", "content": "Dấu hiệu chỉ định từ 'this + noun' bắt buộc danh từ đó phải được giới thiệu ở câu liền trước."}]
}

# Pass 9: 168 - 171 (Web page: Sarah's Catering)
p7_single[168] = {
    "exp": "Trang web giới thiệu: 'Sarah's Catering has been preparing customized seasonal menus for corporate galas, intimate weddings, and private banquets throughout Melbourne since 2012' (Sarah's Catering đã chuẩn bị các thực đơn theo mùa tùy biến cho các buổi dạ tiệc công ty, đám cưới ấm cúng và tiệc riêng trên toàn Melbourne từ năm 2012) -> Công ty tạo ra các thực đơn phù hợp với từng sự kiện riêng biệt ('It creates menus suited to specific events'). Phương án (A) là đáp án đúng.",
    "vocab": [
        {"word": "customized", "ipa": "/ˈkʌs.tə.maɪzd/", "pos": "adj", "meaning": "được tùy chỉnh riêng theo nhu cầu", "example": "We design customized itinerary packages for overseas clients."},
        {"word": "seasonal", "ipa": "/ˈsiː.zən.əl/", "pos": "adj", "meaning": "theo mùa, hợp mùa", "example": "Our chef sources fresh seasonal vegetables from organic farms."},
        {"word": "gala", "ipa": "/ˈɡɑː.lə/", "pos": "n", "meaning": "buổi dạ tiệc long trọng", "example": "Tickets for the charity gala sold out within forty-eight hours."}
    ],
    "collocations": [{"phrase": "customized menus", "meaning": "thực đơn tùy chỉnh riêng"}, {"phrase": "corporate gala", "meaning": "buổi dạ tiệc công ty"}]
}

p7_single[169] = {
    "exp": "Căn cứ ngữ cảnh đoạn 1, dòng 4: 'Clients are invited to schedule a complimentary tasting session to sample proposed dishes before finalizing their reception booking' (Khách hàng được mời đặt lịch buổi nếm thử miễn phí để nếm thử các món ăn được đề xuất trước khi chốt lịch đặt tiệc). Từ 'taste / tasting' trong ngữ cảnh này mang nghĩa 'sample / try the food' (nếm thử hương vị đồ ăn). Phương án (A) 'sample' là từ đồng nghĩa chính xác nhất. Các phương án khác: (B) mùi vị thẩm mỹ, (C) đánh giá năng lực, (D) lựa chọn.",
    "vocab": [
        {"word": "sample", "ipa": "/ˈsɑːm.pəl/", "pos": "v", "meaning": "nếm thử một phần nhỏ đồ ăn thức uống", "example": "Prospective brides sample wedding cakes before placing orders."},
        {"word": "tasting session", "ipa": "/ˈteɪ.stɪŋ ˈseʃ.ən/", "pos": "n", "meaning": "buổi nếm thử món ăn tiệc", "example": "The executive chef hosts complimentary tasting sessions on Tuesdays."},
        {"word": "finalize", "ipa": "/ˈfaɪ.nəl.aɪz/", "pos": "v", "meaning": "chốt lại, hoàn tất hợp đồng", "example": "Meet with the banquet manager to finalize beverage selections."}
    ],
    "collocations": [{"phrase": "sample dishes", "meaning": "nếm thử các món ăn"}, {"phrase": "tasting session", "meaning": "buổi thử món"}]
}

p7_single[170] = {
    "exp": "Mục dịch vụ của trang web liệt kê: 'In addition to food preparation, our professional staff provides complete tableware rentals, including fine china, crystal glassware, and linens' (Bên cạnh việc chế biến thức ăn, đội ngũ chuyên nghiệp của chúng tôi cung cấp dịch vụ cho thuê đồ dùng bàn ăn trọn gói, bao gồm bát đĩa sứ cao cấp, đồ thủy tinh pha lê và khăn trải bàn) -> Dịch vụ được cung cấp là cho thuê đồ dùng bàn ăn ('Tableware rentals'). Phương án (C) là đáp án chính xác.",
    "vocab": [
        {"word": "tableware", "ipa": "/ˈteɪ.bəl.weər/", "pos": "n", "meaning": "bộ đồ dùng trên bàn ăn (bát, đĩa, thìa, dĩa)", "example": "Catering contracts include complete tableware setup and cleanup."},
        {"word": "rental", "ipa": "/ˈren.təl/", "pos": "n", "meaning": "dịch vụ cho thuê đồ", "example": "Contact party rental companies for audio equipment and tents."},
        {"word": "china", "ipa": "/ˈtʃaɪ.nə/", "pos": "n", "meaning": "đồ sứ bàn ăn tinh xảo", "example": "Formal banquets require polished silverware and bone china."}
    ],
    "collocations": [{"phrase": "tableware rentals", "meaning": "dịch vụ cho thuê dụng cụ bàn tiệc"}, {"phrase": "complete setup", "meaning": "khâu bài trí hoàn chỉnh"}]
}

p7_single[171] = {
    "exp": "Dưới mục đánh giá phản hồi có lời chứng thực: 'David Liu, Event Coordinator, Melbourne Symphony Orchestra: 'Sarah's team handled our 500-guest gala dinner flawlessly...' (David Liu, Điều phối viên sự kiện, Dàn nhạc Giao hưởng Melbourne: 'Đội ngũ của Sarah đã phục vụ bữa tối dạ tiệc 500 khách của chúng tôi một cách hoàn hảo...') -> Ông Liu là một khách hàng đã từng sử dụng dịch vụ của Sarah's Catering ('A past client'). Phương án (C) là đáp án chính xác.",
    "vocab": [
        {"word": "coordinator", "ipa": "/kəʊˈɔː.dɪ.neɪ.tər/", "pos": "n", "meaning": "người điều phối sự kiện", "example": "The event coordinator supervised caterers and florists."},
        {"word": "testimonial", "ipa": "/ˌtes.tɪˈməʊ.ni.əl/", "pos": "n", "meaning": "lời nhận xét khen ngợi của khách hàng", "example": "Display authentic client testimonials on your homepage."},
        {"word": "flawlessly", "ipa": "/ˈflɔː.ləs.li/", "pos": "adv", "meaning": "một cách hoàn hảo, không tì vết", "example": "The catering staff executed the complicated dinner flawlessly."}
    ],
    "collocations": [{"phrase": "past client", "meaning": "khách hàng cũ/đã từng mua dịch vụ"}, {"phrase": "event coordinator", "meaning": "người điều phối sự kiện"}]
}

# Pass 10: 172 - 175 (Online chat: Marcus Steuber, Brinda Rajan, Joshua Borg)
p7_single[172] = {
    "exp": "Marcus Steuber mở đầu cuộc trò chuyện lúc 10:41 A.M.: 'Are we still planning to have the author video conference today? I haven't yet received a meeting invitation' (Chúng ta vẫn dự định tổ chức hội nghị truyền hình với tác giả hôm nay chứ? Tôi vẫn chưa nhận được lời mời họp) -> Ông Steuber nhắn tin để hỏi về một cuộc họp sắp diễn ra ('To ask about an upcoming meeting'). Phương án (B) là đáp án đúng.",
    "vocab": [
        {"word": "video conference", "ipa": "/ˈvɪd.i.əʊ ˌkɒn.fər.əns/", "pos": "n", "meaning": "cuộc họp qua video, hội nghị truyền hình", "example": "The overseas branch joined via a secure video conference."},
        {"word": "invitation", "ipa": "/ˌɪn.vɪˈteɪ.ʃən/", "pos": "n", "meaning": "giấy mời, lời mời tham gia sự kiện", "example": "Calendar software issues meeting invitations automatically."},
        {"word": "upcoming", "ipa": "/ˈʌpˌkʌm.ɪŋ/", "pos": "adj", "meaning": "sắp diễn ra tới đây", "example": "Check the calendar for details on upcoming client reviews."}
    ],
    "collocations": [{"phrase": "video conference", "meaning": "hội nghị truyền hình"}, {"phrase": "meeting invitation", "meaning": "lời mời họp"}]
}

p7_single[173] = {
    "exp": "Lúc 10:43 A.M., Marcus Steuber cho biết anh có hẹn thảo luận sự cố in ấn với Hazel Luong ở xưởng Singapore. Khi Brinda Rajan hỏi liệu anh có thể hoãn cuộc hẹn đó được không, Marcus đáp lúc 10:45 A.M.: 'Let me check with my supervisor. I'll add Mr. Borg to our chat' (Để tôi hỏi lại người giám sát của tôi đã. Tôi sẽ thêm ông Borg vào nhóm chat) -> Marcus muốn hỏi ý kiến cấp trên vì anh chưa chắc chắn liệu có thể dời lịch hẹn với Hazel hay không ('He is unsure whether he can reschedule an appointment'). Phương án (B) là đáp án đúng.",
    "vocab": [
        {"word": "supervisor", "ipa": "/ˈsuː.pə.vaɪ.zər/", "pos": "n", "meaning": "người giám sát, người quản lý trực tiếp", "example": "Consult your direct supervisor before modifying production shifts."},
        {"word": "reschedule", "ipa": "/ˌriːˈʃedʒ.uːl/", "pos": "v", "meaning": "dời lịch, sắp xếp lại thời gian", "example": "Heavy traffic forced her to reschedule the client briefing."},
        {"word": "unsure", "ipa": "/ʌnˈʃɔːr/", "pos": "adj", "meaning": "không chắc chắn, lưỡng lự", "example": "Executives were unsure whether raw material costs would stabilize."}
    ],
    "collocations": [{"phrase": "check with a supervisor", "meaning": "hỏi lại người giám sát"}, {"phrase": "reschedule an appointment", "meaning": "dời lại cuộc hẹn"}]
}

p7_single[174] = {
    "exp": "Trong đoạn chat, Brinda Rajan nói lúc 10:44 A.M.: 'The new author we're working with really needs your guidance on the final book design and formatting' (Tác giả mới mà chúng ta đang hợp tác thực sự cần sự hướng dẫn của anh về thiết kế và định dạng sách cuối cùng). Đến 10:48 A.M., sau khi biết Marcus chỉ rảnh từ 4-6 giờ chiều, Brinda nói: 'OK, I'll contact Ms. Benoit to find out if she can meet later in the day, then' (Được rồi, tôi sẽ liên hệ với cô Benoit để xem liệu cô ấy có thể họp muộn hơn trong ngày không) -> Đối chiếu thông tin: cô Benoit chính là tác giả cuốn sách ('An author'). Phương án (A) là đáp án đúng.",
    "vocab": [
        {"word": "author", "ipa": "/ˈɔː.θər/", "pos": "n", "meaning": "tác giả cuốn sách", "example": "The best-selling author signed copies of her new thriller."},
        {"word": "formatting", "ipa": "/ˈfɔː.mæt.ɪŋ/", "pos": "n", "meaning": "việc định dạng trình bày trang sách/văn bản", "example": "Careful formatting ensures readability on mobile readers."},
        {"word": "guidance", "ipa": "/ˈɡaɪ.dəns/", "pos": "n", "meaning": "sự hướng dẫn, chỉ bảo chuyên môn", "example": "Junior editors rely on senior staff for technical guidance."}
    ],
    "collocations": [{"phrase": "guidance on design", "meaning": "hướng dẫn về thiết kế"}, {"phrase": "contact someone", "meaning": "liên hệ với ai"}]
}

p7_single[175] = {
    "exp": "Tại dòng chat cuối cùng, sau khi nhận được sự đồng thuận dời cuộc họp sang chiều muộn, Brinda Rajan thông báo: 'OK, I'll contact Ms. Benoit to find out if she can meet later in the day, then' (Được rồi, thế thì tôi sẽ liên lạc với cô Benoit để xem cô ấy có thể họp muộn hơn trong ngày được không) -> Hành động tiếp theo của cô Rajan là điều chỉnh/dời lại lịch họp qua video với tác giả ('Reschedule a video conference'). Phương án (D) là đáp án chính xác.",
    "vocab": [
        {"word": "reschedule", "ipa": "/ˌriːˈʃedʒ.uːl/", "pos": "v", "meaning": "xếp lại lịch, lùi giờ hẹn", "example": "Please contact participants to reschedule the teleconference."},
        {"word": "later in the day", "ipa": "/ˈleɪ.tər ɪn ðə deɪ/", "pos": "adv phr", "meaning": "muộn hơn trong ngày", "example": "The delivery is anticipated to arrive later in the day."},
        {"word": "production editor", "ipa": "/prəˈdʌk.ʃən ˈed.ɪ.tər/", "pos": "n", "meaning": "biên tập viên phụ trách sản xuất/chế bản", "example": "The production editor coordinates with commercial print shops."}
    ],
    "collocations": [{"phrase": "reschedule a conference", "meaning": "dời lịch họp hội nghị"}, {"phrase": "later in the day", "meaning": "vào thời điểm muộn hơn trong ngày"}]
}

with open('scratch/p7_q147_q175_part.json', 'w', encoding='utf-8') as f:
    json.dump(p7_single, f, ensure_ascii=False, indent=2)
print("Saved Part 7 Single Q147-Q175 successfully!")
