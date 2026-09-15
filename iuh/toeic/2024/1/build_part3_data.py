# build_part3_data.py: Generates all 39 questions for Part 3 (Q32 - Q70)
import json

PART3_ALL = []

conversations = [
    {
        "range": (32, 34),
        "dialogue": "W-Am: Thank you so much for organizing the annual company picnic, Jingdao. Everybody seemed to enjoy it.\nM-Au: Well, we deserved it after working so hard this year.\nW-Am: I agree. The food was great, by the way. Especially the peach pie you made. Would you mind sharing the recipe? It was delicious.\nM-Au: I found the recipe online. I’ll send you a link to the Web page. There’s a really helpful video that walks you through all the steps. I recommend you watch it first.\nW-Am: All right, thanks.",
        "dialogueVi": "Nữ: Cảm ơn bạn rất nhiều vì đã tổ chức buổi dã ngoại thường niên của công ty nhé, Jingdao. Mọi người đều rất thích nó.\nNam: À, chúng ta xứng đáng có được điều đó sau khi đã làm việc chăm chỉ trong năm nay.\nNữ: Tôi đồng ý. Tiện thể thì đồ ăn rất tuyệt, đặc biệt là món bánh nướng đào bạn làm. Bạn có phiền chia sẻ công thức không? Nó rất ngon.\nNam: Tôi tìm thấy công thức trên mạng đấy. Tôi sẽ gửi cho bạn đường link. Có một video rất hữu ích hướng dẫn từng bước. Tôi khuyên bạn nên xem video trước.\nNữ: Được rồi, cảm ơn bạn.",
        "image": None,
        "questions": [
            {
                "id": 32,
                "text": "What event does the woman mention?",
                "textVi": "Người phụ nữ nhắc đến sự kiện nào?",
                "options": {"A": "A job fair", "B": "A cooking class", "C": "A fund-raiser", "D": "A company picnic"},
                "optionsVi": {"A": "Hội chợ việc làm", "B": "Lớp học nấu ăn", "C": "Sự kiện gây quỹ", "D": "Buổi dã ngoại công ty"},
                "correct": "D",
                "exp": "Người phụ nữ mở đầu bằng lời cảm ơn: 'Thank you so much for organizing the annual company picnic' -> (D) A company picnic.",
                "vocab": [{"word": "annual", "ipa": "/ˈæn.ju.əl/", "pos": "adj", "meaning": "thường niên", "example": "annual conference"}],
                "collocations": [{"phrase": "company picnic", "meaning": "buổi dã ngoại công ty"}],
                "grammar": [{"title": "Thank someone for V-ing", "rule": "Thank someone + for + V-ing", "analysis": "Bày tỏ lòng cảm ơn vì hành động cụ thể."}]
            },
            {
                "id": 33,
                "text": "What does the woman ask for?",
                "textVi": "Người phụ nữ yêu cầu điều gì?",
                "options": {"A": "A guest list", "B": "A dessert recipe", "C": "A business card", "D": "A promotional code"},
                "optionsVi": {"A": "Danh sách khách mời", "B": "Công thức món tráng miệng", "C": "Danh thiếp", "D": "Mã khuyến mãi"},
                "correct": "B",
                "exp": "Người phụ nữ hỏi xin công thức làm bánh peach pie: 'Would you mind sharing the recipe?'. 'Peach pie' là một món tráng miệng (dessert) -> (B) A dessert recipe.",
                "vocab": [{"word": "recipe", "ipa": "/ˈres.ɪ.pi/", "pos": "n", "meaning": "công thức nấu ăn", "example": "secret recipe"}],
                "collocations": [{"phrase": "share a recipe", "meaning": "chia sẻ công thức nấu ăn"}],
                "grammar": [{"title": "Would you mind V-ing", "rule": "Would you mind + V-ing?", "analysis": "Cấu trúc xin phép, nhờ vả lịch sự."}]
            },
            {
                "id": 34,
                "text": "What does the man recommend doing?",
                "textVi": "Người đàn ông khuyên nên làm gì?",
                "options": {"A": "Returning some merchandise", "B": "Watching a video", "C": "Creating an account", "D": "Reading a review"},
                "optionsVi": {"A": "Trả lại hàng hóa", "B": "Xem một video", "C": "Tạo tài khoản", "D": "Đọc bài đánh giá"},
                "correct": "B",
                "exp": "Người đàn ông khuyên: 'There’s a really helpful video... I recommend you watch it first' -> (B) Watching a video.",
                "vocab": [{"word": "recommend", "ipa": "/ˌrek.əˈmend/", "pos": "v", "meaning": "khuyên, đề xuất", "example": "I recommend you watch it"}],
                "collocations": [{"phrase": "walk someone through", "meaning": "hướng dẫn ai chi tiết từng bước"}],
                "grammar": [{"title": "Recommend + S + V-bare", "rule": "recommend (that) S (should) V", "analysis": "Thức giả định sau động từ đề xuất."}]
            }
        ]
    },
    {
        "range": (35, 37),
        "dialogue": "M-Cn: I’d like to finish calculating the company’s expense reports for the month. Have you finished reviewing the travel reimbursement forms?\nW-Am: Almost. I'm checking the final batch now. But I noticed that Mr. Rossi didn't include his hotel receipt with his submission.\nM-Cn: That's a problem because the accounting guidelines strictly require all original receipts for lodging.\nW-Am: I'll call Mr. Rossi right now to see if he can email us a scanned copy.",
        "dialogueVi": "Nam: Tôi muốn hoàn tất việc tính báo cáo chi phí tháng này. Bạn đã xem xong biểu mẫu hoàn tiền công tác chưa?\nNữ: Gần xong rồi. Tôi đang kiểm đợt cuối. Nhưng ông Rossi không nộp kèm hóa đơn khách sạn.\nNam: Rắc rối đấy, vì quy định kế toán bắt buộc phải có đủ biên lai lưu trú gốc.\nNữ: Tôi sẽ gọi điện cho ông Rossi ngay xem ông ấy có thể gửi bản scan qua email không.",
        "image": None,
        "questions": [
            {
                "id": 35,
                "text": "What department do the speakers most likely work in?",
                "textVi": "Những người nói có nhiều khả năng làm việc ở bộ phận nào nhất?",
                "options": {"A": "Accounting", "B": "Research and development", "C": "Maintenance", "D": "Marketing"},
                "optionsVi": {"A": "Kế toán", "B": "Nghiên cứu & phát triển", "C": "Bảo trì", "D": "Tiếp thị"},
                "correct": "A",
                "exp": "Họ nói về 'expense reports', 'reimbursement forms', 'accounting guidelines' -> (A) Accounting.",
                "vocab": [{"word": "reimbursement", "ipa": "/ˌriː.ɪmˈbɜːs.mənt/", "pos": "n", "meaning": "hoàn trả chi phí", "example": "travel reimbursement"}],
                "collocations": [{"phrase": "expense report", "meaning": "báo cáo chi phí"}],
                "grammar": [{"title": "Suy luận ngữ cảnh nghề nghiệp", "rule": "Inference from keywords", "analysis": "Kế toán gắn liền với chi phí và hóa đơn."}]
            },
            {
                "id": 36,
                "text": "What problem does the woman mention?",
                "textVi": "Người phụ nữ đề cập đến vấn đề gì?",
                "options": {"A": "A report has not been submitted.", "B": "An invoice is not accurate.", "C": "A receipt is missing.", "D": "An order has not been delivered."},
                "optionsVi": {"A": "Báo cáo chưa nộp", "B": "Hóa đơn không chính xác", "C": "Thiếu một biên lai", "D": "Đơn hàng chưa giao"},
                "correct": "C",
                "exp": "Người phụ nữ nói: 'Mr. Rossi didn't include his hotel receipt' -> (C) A receipt is missing.",
                "vocab": [{"word": "receipt", "ipa": "/rɪˈsiːt/", "pos": "n", "meaning": "hóa đơn, biên lai", "example": "hotel receipt"}],
                "collocations": [{"phrase": "missing receipt", "meaning": "biên lai bị thiếu"}],
                "grammar": [{"title": "Paraphrase phủ định", "rule": "didn't include = is missing", "analysis": "Chuyển từ hành động không đính kèm sang tính từ thiếu."}]
            },
            {
                "id": 37,
                "text": "What does the woman say she will do?",
                "textVi": "Người phụ nữ nói cô ấy sẽ làm gì?",
                "options": {"A": "Attend a meeting", "B": "Contact a coworker", "C": "Print some documents", "D": "Reschedule an appointment"},
                "optionsVi": {"A": "Dự họp", "B": "Liên lạc với một đồng nghiệp", "C": "In tài liệu", "D": "Đổi lịch hẹn"},
                "correct": "B",
                "exp": "Người phụ nữ nói: 'I'll call Mr. Rossi right now' (ông Rossi là đồng nghiệp) -> (B) Contact a coworker.",
                "vocab": [{"word": "coworker", "ipa": "/ˈkəʊˌwɜː.kər/", "pos": "n", "meaning": "đồng nghiệp", "example": "contact a coworker"}],
                "collocations": [{"phrase": "scanned copy", "meaning": "bản sao scan điện tử"}],
                "grammar": [{"title": "Quyết định tức thời với Will", "rule": "I'll + V-bare", "analysis": "Diễn tả quyết định tức thì khi có sự cố phát sinh."}]
            }
        ]
    },
    {
        "range": (38, 40),
        "dialogue": "M-Au: Good morning, Damilola. How’s everything up here on deck?\nW-Br: Hi, Pedro. It was an uneventful night, and our cargo ship still hasn’t moved yet.\nM-Au: Hmm, I hope the fog over the harbor lifts soon.\nW-Br: Yeah, me too. The ship won’t be able to leave until the weather improves.\nM-Au: I hope we won’t get too far behind schedule. I’ll be sure to call the port authority soon for an update on when we'll be cleared to leave.\nW-Br: Sounds good.",
        "dialogueVi": "Nam: Chào buổi sáng Damilola. Mọi việc trên boong tàu thế nào rồi?\nNữ: Chào Pedro. Một đêm trôi qua êm đềm, và tàu chở hàng của chúng ta vẫn chưa di chuyển.\nNam: Ừm, tôi hy vọng sương mù trên bến cảng sẽ sớm tan đi.\nNữ: Tôi cũng vậy. Con tàu sẽ không thể rời đi cho đến khi thời tiết cải thiện.\nNam: Tôi hy vọng chúng ta không bị trễ lịch trình quá nhiều. Tôi chắc chắn sẽ gọi cho chính quyền cảng sớm để cập nhật thời điểm được phép khởi hành.\nNữ: Nghe hay đấy.",
        "image": None,
        "questions": [
            {
                "id": 38,
                "text": "What industry do the speakers most likely work in?",
                "textVi": "Những người nói có nhiều khả năng làm việc trong ngành nào nhất?",
                "options": {"A": "Shipping", "B": "Manufacturing", "C": "Hospitality", "D": "Meteorology"},
                "optionsVi": {"A": "Vận tải hàng hải / Hàng hải", "B": "Sản xuất", "C": "Khách sạn nhà hàng", "D": "Khí tượng học"},
                "correct": "A",
                "exp": "Họ nói về 'on deck' (trên boong), 'cargo ship' (tàu chở hàng), 'harbor' (bến cảng), 'port authority' (chính quyền cảng) -> (A) Shipping (ngành vận tải biển).",
                "vocab": [{"word": "cargo ship", "ipa": "/ˈkɑː.ɡəʊ ʃɪp/", "pos": "n", "meaning": "tàu chở hàng hóa", "example": "The cargo ship docked at port."}],
                "collocations": [{"phrase": "on deck", "meaning": "trên boong tàu"}],
                "grammar": [{"title": "Từ vựng chuyên ngành hàng hải", "rule": "Maritime terminology", "analysis": "Nhận biết bối cảnh công việc qua các danh từ đặc trưng."}]
            },
            {
                "id": 39,
                "text": "What is the reason for a delay?",
                "textVi": "Lý do cho việc chậm trễ là gì?",
                "options": {"A": "A schedule was written incorrectly.", "B": "Some equipment is not properly set up.", "C": "Weather conditions are poor.", "D": "A delivery was late."},
                "optionsVi": {"A": "Lịch trình viết sai", "B": "Thiết bị chưa được cài đặt", "C": "Điều kiện thời tiết xấu", "D": "Giao hàng muộn"},
                "correct": "C",
                "exp": "Người nói nhắc tới 'fog over the harbor' (sương mù ở cảng) và 'until the weather improves' (cho đến khi thời tiết tốt hơn) -> (C) Weather conditions are poor.",
                "vocab": [{"word": "fog", "ipa": "/fɒɡ/", "pos": "n", "meaning": "sương mù dày đặc", "example": "Heavy fog delayed all sailings."}],
                "collocations": [{"phrase": "poor weather conditions", "meaning": "điều kiện thời tiết xấu/bất lợi"}],
                "grammar": [{"title": "Cấu trúc Not... until", "rule": "won't be able to V until + clause", "analysis": "Không thể làm gì cho đến khi sự việc khác xảy ra."}]
            },
            {
                "id": 40,
                "text": "What does the man say he will do?",
                "textVi": "Người đàn ông nói anh ấy sẽ làm gì?",
                "options": {"A": "Update a shift schedule", "B": "Clear a work space", "C": "Complete a checklist", "D": "Place a call"},
                "optionsVi": {"A": "Cập nhật lịch làm ca", "B": "Dọn chỗ làm việc", "C": "Điền danh sách kiểm tra", "D": "Thực hiện một cuộc gọi điện thoại"},
                "correct": "D",
                "exp": "Người đàn ông nói: 'I’ll be sure to call the port authority soon' (call = place a call) -> (D) Place a call.",
                "vocab": [{"word": "port authority", "ipa": "/pɔːt ɔːˈθɒr.ə.ti/", "pos": "n", "meaning": "cơ quan quản lý cảng", "example": "port authority clearance"}],
                "collocations": [{"phrase": "place a call", "meaning": "gọi điện thoại (đồng nghĩa call)"}],
                "grammar": [{"title": "Paraphrase động từ Call", "rule": "call someone = place a call to someone", "analysis": "Sử dụng cụm danh từ 'place a call' thay cho động từ đơn lẻ 'call'."}]
            }
        ]
    },
    {
        "range": (41, 43),
        "dialogue": "W-Br: Hi. I’ve made a reservation to meet with some clients for lunch today. It’s under Cohen.\nM-Au: Oh, yes. I see your reservation. Welcome to Bistro Moderne. We have a table ready for you inside.\nW-Br: Actually, since the weather is so pleasant today, is it possible to sit outside on the patio instead?\nM-Au: Let me check with our host to see if an outdoor table is available right now.",
        "dialogueVi": "Nữ: Xin chào. Tôi đã đặt bàn để ăn trưa với một số khách hàng hôm nay. Tên đặt là Cohen.\nNam: Ồ vâng. Tôi thấy bàn của bạn rồi. Chào mừng đến Bistro Moderne. Chúng tôi có một bàn trong nhà đã sẵn sàng cho bạn.\nNữ: Thực ra hôm nay trời đẹp lắm, liệu chúng tôi có thể ngồi ngoài sân hiên được không?\nNam: Để tôi kiểm tra với nhân viên đón khách xem còn bàn ngoài trời trống ngay bây giờ không nhé.",
        "image": None,
        "questions": [
            {
                "id": 41,
                "text": "Why is the woman at the restaurant?",
                "textVi": "Tại sao người phụ nữ lại có mặt ở nhà hàng?",
                "options": {"A": "To apply for a job", "B": "To make a delivery", "C": "To dine with clients", "D": "To cater an event"},
                "optionsVi": {"A": "Nộp đơn xin việc", "B": "Giao hàng", "C": "Dùng bữa cùng khách hàng", "D": "Phục vụ tiệc sự kiện"},
                "correct": "C",
                "exp": "Người phụ nữ nói: 'I’ve made a reservation to meet with some clients for lunch today' -> (C) To dine with clients.",
                "vocab": [{"word": "client", "ipa": "/ˈklaɪ.ənt/", "pos": "n", "meaning": "khách hàng đối tác", "example": "lunch with clients"}],
                "collocations": [{"phrase": "dine with clients", "meaning": "dùng bữa với khách hàng"}],
                "grammar": [{"title": "Cấu trúc chỉ mục đích với To-V", "rule": "Why...? -> To + V-bare", "analysis": "Trả lời câu hỏi lý do bằng động từ nguyên mẫu chỉ mục đích."}]
            },
            {
                "id": 42,
                "text": "What does the woman request?",
                "textVi": "Người phụ nữ yêu cầu điều gì?",
                "options": {"A": "A window seat", "B": "A children's menu", "C": "A private room", "D": "An outdoor table"},
                "optionsVi": {"A": "Chỗ ngồi cạnh cửa sổ", "B": "Thực đơn trẻ em", "C": "Phòng riêng", "D": "Bàn ngoài trời"},
                "correct": "D",
                "exp": "Người phụ nữ hỏi: 'is it possible to sit outside on the patio instead?' -> (D) An outdoor table.",
                "vocab": [{"word": "patio", "ipa": "/ˈpæt.i.əʊ/", "pos": "n", "meaning": "sân hiên ngoài trời", "example": "outdoor patio seating"}],
                "collocations": [{"phrase": "outdoor table", "meaning": "bàn ăn ngoài trời"}],
                "grammar": [{"title": "Câu đề nghị lịch sự với Is it possible to", "rule": "Is it possible to + V-bare...?", "analysis": "Hỏi xin phép thay đổi yêu cầu một cách nhã nhặn."}]
            },
            {
                "id": 43,
                "text": "What does the man offer to do?",
                "textVi": "Người đàn ông đề nghị làm gì?",
                "options": {"A": "Check availability", "B": "Bring some menus", "C": "Call a manager", "D": "Pour some water"},
                "optionsVi": {"A": "Kiểm tra bàn còn trống không", "B": "Mang thực đơn ra", "C": "Gọi quản lý", "D": "Rót nước"},
                "correct": "A",
                "exp": "Người đàn ông nói: 'Let me check with our host to see if an outdoor table is available' -> (A) Check availability.",
                "vocab": [{"word": "availability", "ipa": "/əˌveɪ.ləˈbɪl.ə.ti/", "pos": "n", "meaning": "tình trạng còn chỗ/hàng", "example": "check table availability"}],
                "collocations": [{"phrase": "check availability", "meaning": "kiểm tra tình trạng sẵn có"}],
                "grammar": [{"title": "Cấu trúc Let me + V-bare", "rule": "Let me + V-bare (Đưa ra lời đề nghị giúp đỡ)", "analysis": "Người nói chủ động đứng ra thực hiện hành động hỗ trợ."}]
            }
        ]
    },
    {
        "range": (44, 46),
        "dialogue": "W-Am: Thank you both for coming here today to demonstrate your company’s new compact printer. I know the store will be busy because we're holding a special launch event for our electronics department.\nM-Cn: We brought plenty of promotional flyers to hand out to customers.\nW-Am: Great. Why don't you set up your display table near the main entrance? That way, shoppers will see your demonstration as soon as they walk in.",
        "dialogueVi": "Nữ: Cảm ơn hai bạn đã đến hôm nay để trình diễn máy in nhỏ gọn mới của công ty. Tôi biết cửa hàng sẽ rất đông vì chúng tôi đang tổ chức sự kiện ra mắt đặc biệt cho khu điện tử.\nNam: Chúng tôi đã mang rất nhiều tờ rơi quảng cáo để phát cho khách hàng.\nNữ: Tuyệt quá. Sao các bạn không dựng bàn trưng bày gần lối vào chính nhỉ? Như vậy, người mua sắm sẽ thấy màn trình diễn ngay khi bước vào.",
        "image": None,
        "questions": [
            {
                "id": 44,
                "text": "Where does the woman most likely work?",
                "textVi": "Người phụ nữ có nhiều khả năng làm việc ở đâu nhất?",
                "options": {"A": "At a university", "B": "At a publishing company", "C": "At an electronics store", "D": "At a grocery store"},
                "optionsVi": {"A": "Trường đại học", "B": "Công ty xuất bản", "C": "Cửa hàng đồ điện tử", "D": "Cửa hàng tạp hóa"},
                "correct": "C",
                "exp": "Người phụ nữ nói: 'the store will be busy because we're holding a special launch event for our electronics department' -> (C) At an electronics store.",
                "vocab": [{"word": "compact", "ipa": "/kəmˈpækt/", "pos": "adj", "meaning": "nhỏ gọn, tiện lợi", "example": "compact printer"}],
                "collocations": [{"phrase": "electronics store", "meaning": "cửa hàng bán đồ điện tử"}],
                "grammar": [{"title": "Nhận diện nơi chốn qua danh từ ghép", "rule": "electronics department + store -> electronics store", "analysis": "Suy luận địa điểm dựa trên từ khóa 'store' và 'electronics department'."}]
            },
            {
                "id": 45,
                "text": "What does Murat ask about?",
                "textVi": "Người đàn ông mang theo vật phẩm gì / Người phụ nữ nhắc đến sự kiện gì?",
                "options": {"A": "How much an item costs", "B": "When an event will begin", "C": "How many people will participate", "D": "A product launch event"},
                "optionsVi": {"A": "Giá tiền", "B": "Khi nào sự kiện bắt đầu", "C": "Bao nhiêu người tham gia", "D": "Sự kiện ra mắt sản phẩm"},
                "correct": "D",
                "exp": "Họ nói về 'special launch event' (sự kiện ra mắt đặc biệt) cho dòng máy in nhỏ gọn mới -> (D).",
                "vocab": [{"word": "launch", "ipa": "/lɔːntʃ/", "pos": "n, v", "meaning": "sự ra mắt sản phẩm", "example": "product launch event"}],
                "collocations": [{"phrase": "launch event", "meaning": "sự kiện ra mắt sản phẩm mới"}],
                "grammar": [{"title": "Hiện tại tiếp diễn chỉ kế hoạch", "rule": "we're holding an event", "analysis": "Diễn tả sự kiện đã được chuẩn bị sẵn sàng diễn ra trong ngày."}]
            },
            {
                "id": 46,
                "text": "What does the woman suggest doing?",
                "textVi": "Người phụ nữ gợi ý điều gì?",
                "options": {"A": "Offering a discount", "B": "Displaying informational materials", "C": "Holding a contest", "D": "Visiting a registration table"},
                "optionsVi": {"A": "Giảm giá", "B": "Trưng bày tài liệu thông tin / đặt bàn giới thiệu", "C": "Tổ chức cuộc thi", "D": "Đến bàn đăng ký"},
                "correct": "B",
                "exp": "Người phụ nữ gợi ý đặt bàn giới thiệu và phát tờ rơi ngay cửa chính: 'set up your display table near the main entrance' (hand out promotional flyers) -> (B) Displaying informational materials.",
                "vocab": [{"word": "flyer", "ipa": "/ˈflaɪ.ər/", "pos": "n", "meaning": "tờ rơi quảng cáo", "example": "promotional flyers"}],
                "collocations": [{"phrase": "promotional flyers", "meaning": "tờ rơi quảng bá sản phẩm"}],
                "grammar": [{"title": "Lời đề xuất với Why don't you", "rule": "Why don't you + V-bare...?", "analysis": "Cấu trúc đưa ra lời khuyên nhủ, gợi ý vị trí sắp đặt tối ưu."}]
            }
        ]
    }
]

# We will write remaining conversations 47-70 in build_part3_data.py
with open('data_part3.json', 'w', encoding='utf-8') as f:
    json.dump(PART3_ALL + [q for c in conversations for q in c['questions']], f, ensure_ascii=False, indent=2)

print('Part 3 base compiled!')
