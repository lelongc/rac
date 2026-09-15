# scratch/make_all_p3_p4.py: Comprehensive enrichment for Test 3 LC Part 3 (Q44-Q70) & Part 4 (Q71-Q100)
import json

enrichment = {}

# Group 44 - 46 (Bike rack investment)
enrichment[44] = {
    "exp": "Người phụ nữ mở lời: 'I understand from your e-mail that you're looking for investors in your business' (Tôi hiểu từ email của bạn rằng bạn đang tìm kiếm nhà đầu tư cho doanh nghiệp của mình) -> Người đàn ông gọi điện để thuyết phục người phụ nữ đầu tư vào công việc kinh doanh ('To persuade the woman to invest in his business'). Đáp án đúng là (D).",
    "vocab": [
        {"word": "investor", "ipa": "/ɪnˈves.tər/", "pos": "n", "meaning": "nhà đầu tư", "example": "The startup attracted several prominent foreign investors."},
        {"word": "persuade", "ipa": "/pəˈsweɪd/", "pos": "v", "meaning": "thuyết phục", "example": "He managed to persuade the board to increase the marketing budget."},
        {"word": "venture", "ipa": "/ˈven.tʃər/", "pos": "n", "meaning": "dự án kinh doanh mạo hiểm", "example": "They launched a joint venture in renewable energy."}
    ],
    "collocations": [{"phrase": "look for investors", "meaning": "tìm kiếm nhà đầu tư"}, {"phrase": "persuade someone to do something", "meaning": "thuyết phục ai làm gì"}],
    "grammar": [{"title": "Cấu trúc hiểu ý qua văn bản 'understand from...'", "rule": "understand from + N/email + that + S + V", "content": "Dùng để xác nhận lại thông tin đã đọc được từ nguồn tài liệu hoặc thư từ trước đó."}]
}

enrichment[45] = {
    "exp": "Người phụ nữ hỏi: 'What's different about yours?' (Giá đỡ xe đạp của bạn có gì khác biệt?). Người đàn ông đáp: 'Most indoor racks are one size. But not mine. Its arms can be adjusted to hold any size bicycle frame' (Hầu hết giá đỡ trong nhà chỉ có một kích thước. Nhưng cái của tôi thì khác. Cánh tay đòn có thể điều chỉnh để giữ mọi kích cỡ khung xe đạp) -> Điểm độc đáo là nó có thể điều chỉnh được ('It is adjustable'). Đáp án đúng là (C).",
    "vocab": [
        {"word": "adjustable", "ipa": "/əˈdʒʌs.tə.bəl/", "pos": "adj", "meaning": "có thể điều chỉnh được", "example": "The office chair has an adjustable height and backrest."},
        {"word": "frame", "ipa": "/freɪm/", "pos": "n", "meaning": "khung (xe đạp, tranh ảnh)", "example": "The bicycle is built with a lightweight aluminum frame."},
        {"word": "feature", "ipa": "/ˈfiː.tʃər/", "pos": "n", "meaning": "tính năng, đặc điểm", "example": "Safety is the most attractive feature of the new model."}
    ],
    "collocations": [{"phrase": "adjustable arms", "meaning": "tay đỡ có thể điều chỉnh"}, {"phrase": "bicycle frame", "meaning": "khung xe đạp"}],
    "grammar": [{"title": "Bị động với động từ khiếm khuyết (Modal Verbs)", "rule": "can + be + V3/ed (can be adjusted)", "content": "Diễn tả khả năng của vật thể chịu tác động hành động (có thể được điều chỉnh linh hoạt)."}]
}

enrichment[46] = {
    "exp": "Người phụ nữ yêu cầu: 'Send me your business plan, and I'll review it' (Hãy gửi bản kế hoạch kinh doanh của bạn, tôi sẽ xem xét đánh giá nó) -> Người phụ nữ yêu cầu tài liệu để đánh giá đề xuất ('To evaluate a proposal'). Paraphrasing: business plan -> proposal, review -> evaluate. Đáp án đúng là (D).",
    "vocab": [
        {"word": "evaluate", "ipa": "/ɪˈvæl.ju.eɪt/", "pos": "v", "meaning": "đánh giá, thẩm định", "example": "The committee will evaluate every research proposal."},
        {"word": "proposal", "ipa": "/prəˈpəʊ.zəl/", "pos": "n", "meaning": "bản đề xuất, kế hoạch dự án", "example": "Submit the budget proposal before Friday afternoon."},
        {"word": "business plan", "ipa": "/ˈbɪz.nɪs plæn/", "pos": "n", "meaning": "bản kế hoạch kinh doanh", "example": "A convincing business plan attracts potential partners."}
    ],
    "collocations": [{"phrase": "evaluate a proposal", "meaning": "thẩm định bản đề xuất"}, {"phrase": "review a business plan", "meaning": "xem xét kế hoạch kinh doanh"}],
    "grammar": [{"title": "Paraphrasing động từ chỉ hành động thẩm định", "rule": "review = evaluate = assess", "content": "Trong TOEIC, 'review' (xem lại) thường được diễn đạt tương đương bằng 'evaluate' hoặc 'assess'."}]
}

# Group 47 - 49 (Central bank interview & photography)
enrichment[47] = {
    "exp": "Người phụ nữ giục: 'Alberto, it's time to leave the studio and head over to the central bank for our interview with the director' (Alberto, đến lúc rời studio và sang ngân hàng trung ương để phỏng vấn giám đốc rồi) -> Họ đang chuẩn bị cho một buổi phỏng vấn ('An interview'). Đáp án đúng là (C).",
    "vocab": [
        {"word": "interview", "ipa": "/ˈɪn.tə.vjuː/", "pos": "n", "meaning": "cuộc phỏng vấn", "example": "The journalist conducted an exclusive interview with the CEO."},
        {"word": "studio", "ipa": "/ˈstjuː.di.əʊ/", "pos": "n", "meaning": "trường quay, phòng thu", "example": "The broadcasting studio is equipped with top-tier soundproofing."},
        {"word": "head over", "ipa": "/hed ˈəʊ.vər/", "pos": "phr v", "meaning": "đi tới, hướng về phía", "example": "Let's head over to the conference hall immediately."}
    ],
    "collocations": [{"phrase": "head over to", "meaning": "đi sang địa điểm nào"}, {"phrase": "central bank", "meaning": "ngân hàng trung ương"}],
    "grammar": [{"title": "Cấu trúc 'It's time to + V'", "rule": "It is time to + V-inf", "content": "Nhấn mạnh đã đến thời điểm thích hợp hoặc cấp bách để thực hiện một hành động cụ thể."}]
}

enrichment[48] = {
    "exp": "Người phụ nữ lưu ý: 'And make sure you have the special lenses with you. The poor lighting in the conference room might be a problem' (Hãy nhớ mang theo các ống kính đặc biệt. Ánh sáng yếu trong phòng hội thảo có thể là vấn đề) -> Cô ấy lo ngại về vấn đề ánh sáng ('A lighting issue'). Đáp án đúng là (A).",
    "vocab": [
        {"word": "lighting", "ipa": "/ˈlaɪ.tɪŋ/", "pos": "n", "meaning": "ánh sáng, hệ thống chiếu sáng", "example": "The stage lighting creates a warm ambiance."},
        {"word": "lens", "ipa": "/lenz/", "pos": "n", "meaning": "ống kính máy ảnh (số nhiều: lenses)", "example": "He purchased a telephoto lens for portrait shoots."},
        {"word": "poor", "ipa": "/pɔːr/", "pos": "adj", "meaning": "kém chất lượng, thiếu thốn (ánh sáng)", "example": "Poor lighting can cause unnecessary eye strain."}
    ],
    "collocations": [{"phrase": "poor lighting", "meaning": "ánh sáng kém/yếu"}, {"phrase": "lighting issue", "meaning": "vấn đề về ánh sáng"}],
    "grammar": [{"title": "Cấu trúc lưu ý 'Make sure (that)...'", "rule": "Make sure (that) + S + V", "content": "Dùng để nhắc nhở hoặc yêu cầu đối phương bảo đảm chắc chắn thực hiện một việc."}]
}

enrichment[49] = {
    "exp": "Người đàn ông đề xuất: 'And by the way, can I invite Marcel Lambert to come along? He's our new intern...' (Nhân tiện, tôi có thể mời Marcel Lambert đi cùng không? Cậu ấy là thực tập sinh mới của chúng ta...) -> Marcel Lambert là thực tập sinh ('An intern'). Đáp án đúng là (D).",
    "vocab": [
        {"word": "intern", "ipa": "/ˈɪn.tɜːn/", "pos": "n", "meaning": "thực tập sinh", "example": "The marketing intern assisted with the digital ad campaign."},
        {"word": "come along", "ipa": "/kʌm əˈlɒŋ/", "pos": "phr v", "meaning": "đi cùng, tháp tùng", "example": "Feel free to come along if you have free time."},
        {"word": "experience", "ipa": "/ɪkˈspɪə.ri.əns/", "pos": "n", "meaning": "kinh nghiệm làm việc thực tế", "example": "Internships offer students valuable hands-on experience."}
    ],
    "collocations": [{"phrase": "come along", "meaning": "đi cùng"}, {"phrase": "new intern", "meaning": "thực tập sinh mới"}],
    "grammar": [{"title": "Cách giới thiệu vai trò chức danh bằng 'He is...'", "rule": "S + be + Possessive/Article + Title/Role", "content": "Các từ khóa chỉ vai trò như 'intern', 'assistant', 'director' giúp nhận diện chức vụ ngay lập tức."}]
}

# Group 50 - 52 (Retirement party & room booking)
enrichment[50] = {
    "exp": "Người đàn ông nói: 'Oh, yes, those are all ready' (Ồ vâng, những tài liệu đó đã chuẩn bị xong cả rồi). Người phụ nữ đáp: 'Excellent! Thanks.' (Tuyệt quá! Cảm ơn anh.) -> Người phụ nữ cảm ơn vì anh ấy đã chuẩn bị bản in tài liệu ('Preparing some paper copies'). Đáp án đúng là (D).",
    "vocab": [
        {"word": "copies", "ipa": "/ˈkɒp.iz/", "pos": "n pl", "meaning": "bản sao, bản in tài liệu", "example": "Please distribute printed copies of the agenda."},
        {"word": "preparation", "ipa": "/ˌprep.ərˈeɪ.ʃən/", "pos": "n", "meaning": "sự chuẩn bị", "example": "Preparations for the annual gala are nearly complete."},
        {"word": "ready", "ipa": "/ˈred.i/", "pos": "adj", "meaning": "sẵn sàng", "example": "The conference room is ready for the attendees."}
    ],
    "collocations": [{"phrase": "paper copies", "meaning": "bản sao in trên giấy"}, {"phrase": "all ready", "meaning": "đã sẵn sàng tất cả"}],
    "grammar": [{"title": "Lời cảm ơn trực tiếp trong giao tiếp 'Thanks...'", "rule": "Thanks / Thank you + for + V-ing/Noun", "content": "Khi trả lời câu hỏi 'What does the woman thank the man for?', hãy chú ý câu thoại ngay trước và sau từ 'Thanks'."}]
}

enrichment[51] = {
    "exp": "Người phụ nữ hỏi tiếp: 'By the way, how are the preparations coming along for Sabine Hoffman's retirement party?' (Nhân tiện, khâu chuẩn bị cho bữa tiệc nghỉ hưu của Sabine Hoffman diễn ra đến đâu rồi?) -> Bữa tiệc được tổ chức vì một đồng nghiệp sắp nghỉ hưu ('A colleague will be retiring'). Đáp án đúng là (C).",
    "vocab": [
        {"word": "retire", "ipa": "/rɪˈtaɪər/", "pos": "v", "meaning": "nghỉ hưu", "example": "Senior engineers usually retire after 35 years of service."},
        {"word": "retirement party", "ipa": "/rɪˈtaɪə.mənt ˈpɑː.ti/", "pos": "n", "meaning": "tiệc liên hoan chia tay về hưu", "example": "We held a heartfelt retirement party for the branch manager."},
        {"word": "colleague", "ipa": "/ˈkɒl.iːɡ/", "pos": "n", "meaning": "đồng nghiệp", "example": "He consults his trusted colleagues before making decisions."}
    ],
    "collocations": [{"phrase": "retirement party", "meaning": "tiệc nghỉ hưu"}, {"phrase": "come along", "meaning": "tiến triển, tiến hành"}],
    "grammar": [{"title": "Cụm động từ 'come along' chỉ tiến độ", "rule": "How is/are + N + coming along?", "content": "Mẫu câu hỏi thăm thông dụng về tiến độ công việc hoặc dự án đang diễn ra."}]
}

enrichment[52] = {
    "exp": "Người phụ nữ gợi ý: 'I'm sure she would love to have former staff members come too' (Tôi chắc chắn cô ấy sẽ rất vui nếu có các nhân viên cũ cùng đến). Người đàn ông đáp: 'I booked conference room B, but I'll see if a larger room is free' (Tôi đã đặt phòng họp B, nhưng tôi sẽ xem liệu có phòng lớn hơn còn trống không) -> Câu nói ngụ ý phòng đã đặt quá nhỏ nếu mời thêm người ('A room is too small'). Đáp án đúng là (A).",
    "vocab": [
        {"word": "former", "ipa": "/ˈfɔː.mər/", "pos": "adj", "meaning": "cựu, trước đây", "example": "The reunion was attended by several former executives."},
        {"word": "conference room", "ipa": "/ˈkɒn.fər.əns ruːm/", "pos": "n", "meaning": "phòng hội nghị, phòng họp", "example": "Reserve the main conference room for Friday."},
        {"word": "capacity", "ipa": "/kəˈpæs.ə.ti/", "pos": "n", "meaning": "sức chứa", "example": "The auditorium has a seating capacity of 300."}
    ],
    "collocations": [{"phrase": "former staff members", "meaning": "các cựu nhân viên"}, {"phrase": "book a room", "meaning": "đặt trước phòng"}],
    "grammar": [{"title": "Câu hỏi suy luận hàm ý (Inference Question)", "rule": "Nghe hiểu ngữ cảnh: mời thêm người -> đổi sang phòng lớn -> phòng hiện tại nhỏ", "content": "Dạng câu hỏi 'What does the speaker imply when saying...' đòi hỏi liên kết giữa lời đề nghị trước đó và giải pháp kế tiếp."}]
}

# Group 53 - 55 (Langston Limited retreat at hotel)
enrichment[53] = {
    "exp": "Người đàn ông giới thiệu: 'I'm Kota Ogawa from Langston Limited. I have an appointment with Ms. Ishikawa to view your hotel facilities for my company's upcoming retreat' (Tôi là Kota Ogawa từ Langston Limited. Tôi có hẹn với cô Ishikawa để xem cơ sở vật chất khách sạn cho chuyến nghỉ dưỡng sắp tới của công ty tôi) -> Sự kiện là chuyến nghỉ dưỡng công ty ('A company retreat'). Đáp án đúng là (B).",
    "vocab": [
        {"word": "retreat", "ipa": "/rɪˈtriːt/", "pos": "n", "meaning": "chuyến nghỉ dưỡng tập thể, kỳ dã ngoại công ty", "example": "The annual company retreat fosters team bonding."},
        {"word": "facilities", "ipa": "/fəˈsɪl.ə.tiz/", "pos": "n pl", "meaning": "cơ sở vật chất, tiện nghi", "example": "The resort boasts comprehensive conference facilities."},
        {"word": "upcoming", "ipa": "/ˈʌpˌkʌm.ɪŋ/", "pos": "adj", "meaning": "sắp tới, sắp diễn ra", "example": "Prepare the sales forecast for the upcoming fiscal quarter."}
    ],
    "collocations": [{"phrase": "company retreat", "meaning": "chuyến nghỉ dưỡng/dã ngoại công ty"}, {"phrase": "hotel facilities", "meaning": "cơ sở vật chất của khách sạn"}],
    "grammar": [{"title": "Rút gọn mệnh đề chỉ mục đích với 'to + V'", "rule": "have an appointment + to-V (to view hotel facilities)", "content": "Dùng 'to + động từ nguyên thể' để chỉ mục đích của cuộc hẹn."}]
}

enrichment[54] = {
    "exp": "Người phụ nữ tiếp tân giải thích: 'I know that she's been expecting you, but she had to take an urgent call from head office. She should be finished in a couple of minutes' (Tôi biết cô ấy đang chờ anh, nhưng cô ấy phải nghe một cuộc gọi khẩn cấp từ trụ sở chính) -> Cô Ishikawa bị chậm trễ vì bận điện thoại ('She was on the phone'). Đáp án đúng là (D).",
    "vocab": [
        {"word": "urgent", "ipa": "/ˈɜː.dʒənt/", "pos": "adj", "meaning": "khẩn cấp, cấp bách", "example": "The manager responded to an urgent request from the client."},
        {"word": "head office", "ipa": "/ˌhed ˈɒf.ɪs/", "pos": "n", "meaning": "trụ sở chính, tổng công ty", "example": "Direct all policy questions to the head office."},
        {"word": "expecting", "ipa": "/ɪkˈspek.tɪŋ/", "pos": "v-ing", "meaning": "chờ đợi, đón tiếp ai", "example": "The reception desk is expecting visitors from Tokyo."}
    ],
    "collocations": [{"phrase": "take an urgent call", "meaning": "nghe một cuộc điện thoại khẩn"}, {"phrase": "on the phone", "meaning": "đang nghe điện thoại"}],
    "grammar": [{"title": "Paraphrasing tình huống giao tiếp", "rule": "take a call = be on the phone", "content": "Cụm 'take a call from head office' trong audio được chuyển tải thành 'She was on the phone' trong phương án chọn."}]
}

enrichment[55] = {
    "exp": "Người phụ nữ hướng dẫn người đàn ông: 'While you wait, another staff member can show you the meeting rooms. That way you can check their capability for video presentations' (Trong lúc chờ, một nhân viên khác có thể dẫn anh đi xem các phòng họp để kiểm tra khả năng trình chiếu video) -> Người đàn ông muốn xem trang thiết bị công nghệ ('Technology equipment'). Đáp án đúng là (D).",
    "vocab": [
        {"word": "capability", "ipa": "/ˌkeɪ.pəˈbɪl.ə.ti/", "pos": "n", "meaning": "năng lực, khả năng đáp ứng", "example": "The new server has enhanced data processing capability."},
        {"word": "presentation", "ipa": "/ˌprez.ənˈteɪ.ʃən/", "pos": "n", "meaning": "buổi thuyết trình, trình chiếu", "example": "He delivered an impressive presentation to the board."},
        {"word": "equipment", "ipa": "/ɪˈkwɪp.mənt/", "pos": "n", "meaning": "trang thiết bị (danh từ không đếm được)", "example": "Audio-visual equipment is included in the rental."}
    ],
    "collocations": [{"phrase": "video presentation", "meaning": "bài trình chiếu video"}, {"phrase": "meeting room", "meaning": "phòng họp"}],
    "grammar": [{"title": "Cụm trạng từ liên kết 'That way'", "rule": "That way + S + can + V", "content": "Dùng để diễn tả 'Bằng cách đó, nhờ thế mà...', chỉ phương thức giải quyết công việc thuận tiện."}]
}

# Group 56 - 58 (Pineapple sales & peeling machine)
enrichment[56] = {
    "exp": "Người phụ nữ mở đầu: 'Look at these results! Sales of pineapples have gone up a lot this month' (Hãy nhìn vào kết quả này xem! Doanh số dứa đã tăng vọt trong tháng này) và hai người đang thảo luận về quầy bán hàng thực phẩm -> Cuộc trò chuyện diễn ra tại siêu thị ('At a supermarket'). Đáp án đúng là (D).",
    "vocab": [
        {"word": "supermarket", "ipa": "/ˈsuː.pəˌmɑː.kɪt/", "pos": "n", "meaning": "siêu thị thực phẩm", "example": "Fresh local produce is delivered to the supermarket daily."},
        {"word": "pineapple", "ipa": "/ˈpaɪnˌæp.əl/", "pos": "n", "meaning": "quả dứa, trái thơm", "example": "Pineapples are displayed in the fruit section."},
        {"word": "produce", "ipa": "/ˈprɒd.juːs/", "pos": "n", "meaning": "nông sản, hoa quả rau củ tươi", "example": "The grocery sells locally grown farm produce."}
    ],
    "collocations": [{"phrase": "sales have gone up", "meaning": "doanh số tăng trưởng"}, {"phrase": "supermarket aisle", "meaning": "lối đi trong siêu thị"}],
    "grammar": [{"title": "Thì Hiện tại hoàn thành chỉ kết quả kinh doanh", "rule": "S + have/has + V3/ed (sales have gone up)", "content": "Diễn tả xu hướng tăng trưởng doanh số bắt đầu trong tháng và kết quả vẫn đang được thể hiện rõ rệt."}]
}

enrichment[57] = {
    "exp": "Người đàn ông nhận xét: 'It must be the pineapple-peeling machine we installed. Customers love watching it peel and core the pineapple for them' (Chắc chắn là nhờ chiếc máy gọt dứa mà chúng ta mới lắp đặt. Khách hàng rất thích ngắm nó tự động gọt vỏ và bỏ cùi) -> Người đàn ông cho biết chiếc máy tự phục vụ đang rất được ưa chuộng ('A self-service machine'). Đáp án đúng là (B).",
    "vocab": [
        {"word": "self-service", "ipa": "/ˌselfˈsɜː.vɪs/", "pos": "adj", "meaning": "tự phục vụ", "example": "Self-service checkout kiosks reduce cashier queues."},
        {"word": "peel", "ipa": "/piːl/", "pos": "v", "meaning": "gọt vỏ, lột vỏ hoa quả", "example": "Peel the potatoes before boiling them."},
        {"word": "install", "ipa": "/ɪnˈstɔːl/", "pos": "v", "meaning": "lắp đặt (máy móc, phần mềm)", "example": "Technicians will install the automated packaging unit."}
    ],
    "collocations": [{"phrase": "self-service machine", "meaning": "máy tự phục vụ"}, {"phrase": "peeling machine", "meaning": "máy gọt vỏ"}]
}

enrichment[58] = {
    "exp": "Người đàn ông đề xuất: 'I'm not sure about that. I think the novelty will wear off in a few weeks. Let's wait to see if sales numbers stay high before we order another one' (Tôi không chắc lắm. Cảm giác mới lạ sẽ phai nhạt sau vài tuần. Hãy chờ xem liệu doanh số có duy trì ở mức cao hay không trước khi đặt mua thêm cái nữa) -> Người đàn ông khuyên nên đợi trước khi đưa ra quyết định ('Waiting before making a decision'). Đáp án đúng là (B).",
    "vocab": [
        {"word": "novelty", "ipa": "/ˈnɒv.əl.ti/", "pos": "n", "meaning": "sự mới lạ, tính chất độc đáo ban đầu", "example": "The novelty of the gadget wore off after several months."},
        {"word": "wear off", "ipa": "/weər ɒf/", "pos": "phr v", "meaning": "mất dần tác dụng, nguội đi", "example": "The pain medication will wear off in a couple of hours."},
        {"word": "decision", "ipa": "/dɪˈsɪʒ.ən/", "pos": "n", "meaning": "quyết định", "example": "Delay the purchasing decision until market reports arrive."}
    ],
    "collocations": [{"phrase": "wear off", "meaning": "nhạt phai, biến mất dần"}, {"phrase": "make a decision", "meaning": "đưa ra quyết định"}],
    "grammar": [{"title": "Cấu trúc đề xuất trì hoãn 'Let's wait to see...'", "rule": "Let's wait to see if + Clause", "content": "Mẫu câu đưa ra khuyến nghị mang tính thận trọng trong quản lý kinh doanh."}]
}

# Group 59 - 61 (Dental clinic cancellations & software)
enrichment[59] = {
    "exp": "Người đàn ông trao đổi: 'Ingrid, we've had three patients this week who had to cancel their dental appointments because they forgot about them' (Ingrid, tuần này chúng ta có 3 bệnh nhân phải hủy hẹn nha khoa vì họ quên mất lịch) -> Họ đang thảo luận về việc bệnh nhân hủy lịch khám ('Patient cancellations'). Đáp án đúng là (C).",
    "vocab": [
        {"word": "patient", "ipa": "/ˈpeɪ.ʃənt/", "pos": "n", "meaning": "bệnh nhân", "example": "The clinic treats hundreds of dental patients each month."},
        {"word": "cancellation", "ipa": "/ˌkæn.səlˈeɪ.ʃən/", "pos": "n", "meaning": "sự hủy bỏ, hủy lịch", "example": "Last-minute cancellations disrupt the doctor's schedule."},
        {"word": "appointment", "ipa": "/əˈpɔɪnt.mənt/", "pos": "n", "meaning": "cuộc hẹn khám bệnh", "example": "Always send a reminder one day before the dental appointment."}
    ],
    "collocations": [{"phrase": "cancel an appointment", "meaning": "hủy một cuộc hẹn"}, {"phrase": "dental appointment", "meaning": "cuộc hẹn khám nha khoa"}],
    "grammar": [{"title": "Mệnh đề quan hệ xác định với 'who'", "rule": "patients (người) + who + had to cancel...", "content": "Dùng 'who' làm đại từ quan hệ thay thế cho danh từ chỉ người 'patients'."}]
}

enrichment[60] = {
    "exp": "Người đàn ông chia sẻ giải pháp: 'I recently read an article about an automated software that sends text reminders to clients' (Gần đây tôi có đọc một bài báo về một phần mềm tự động gửi tin nhắn văn bản nhắc nhở khách hàng) -> Người đàn ông đề xuất sử dụng phần mềm ('Use a software program'). Đáp án đúng là (B).",
    "vocab": [
        {"word": "automated", "ipa": "/ˈɔː.tə.meɪ.tɪd/", "pos": "adj", "meaning": "tự động hóa", "example": "An automated notification system alerts staff of incoming orders."},
        {"word": "software", "ipa": "/ˈsɒft.weər/", "pos": "n", "meaning": "phần mềm ứng dụng (không đếm được)", "example": "Upgrade to the latest medical billing software."},
        {"word": "reminder", "ipa": "/rɪˈmaɪn.dər/", "pos": "n", "meaning": "lời nhắc nhở, thông báo nhắc hẹn", "example": "The automated SMS serves as a timely appointment reminder."}
    ],
    "collocations": [{"phrase": "automated software", "meaning": "phần mềm tự động"}, {"phrase": "text reminder", "meaning": "tin nhắn nhắc nhở"}]
}

enrichment[61] = {
    "exp": "Người phụ nữ hưởng ứng: 'That would be helpful. I have some time this afternoon—why don't I research a few different programs and see what features they have?' (Thế thì hữu ích quá. Chiều nay tôi có chút thời gian rảnh—để tôi tìm hiểu một vài chương trình khác nhau xem chúng có những tính năng gì nhé?) -> Người phụ nữ sẽ tìm kiếm thông tin về các chương trình ('Search for some information'). Paraphrasing: research a few programs -> search for information. Đáp án đúng là (A).",
    "vocab": [
        {"word": "research", "ipa": "/rɪˈsɜːtʃ/", "pos": "v", "meaning": "tìm hiểu kỹ, nghiên cứu", "example": "Research competitor pricing strategies before launching the product."},
        {"word": "helpful", "ipa": "/ˈhelp.fəl/", "pos": "adj", "meaning": "hữu ích, có ích", "example": "The tutorial provided extremely helpful guidance."},
        {"word": "feature", "ipa": "/ˈfiː.tʃər/", "pos": "n", "meaning": "tính năng, đặc trưng", "example": "Compare key features across the candidate software platforms."}
    ],
    "collocations": [{"phrase": "search for information", "meaning": "tìm kiếm thông tin"}, {"phrase": "research programs", "meaning": "nghiên cứu khảo sát các phần mềm"}],
    "grammar": [{"title": "Cấu trúc đề xuất tự mình đảm nhận 'Why don't I...?'", "rule": "Why don't I + V-inf?", "content": "Người nói chủ động xung phong thực hiện một phần việc trong nhóm cộng tác."}]
}

# Group 62 - 64 (Employee gifts & travel mugs)
enrichment[62] = {
    "exp": "Người đàn ông hỏi: 'Have you had a chance to look for something I could buy the employees for the company anniversary?' (Bạn đã có cơ hội tìm kiếm món quà nào để tôi có thể mua cho các nhân viên nhân dịp kỷ niệm ngày thành lập công ty chưa?) -> Người đàn ông muốn tặng quà cho các nhân viên ('Employees'). Đáp án đúng là (B).",
    "vocab": [
        {"word": "anniversary", "ipa": "/ˌæn.ɪˈvɜː.sər.i/", "pos": "n", "meaning": "ngày kỷ niệm, lễ kỷ niệm", "example": "The firm celebrated its 20th anniversary with a banquet."},
        {"word": "employee", "ipa": "/ɪmˈplɔɪ.iː/", "pos": "n", "meaning": "nhân viên, người lao động", "example": "Gifts were handed out to all full-time employees."},
        {"word": "token", "ipa": "/ˈtəʊ.kən/", "pos": "n", "meaning": "vật kỷ niệm, biểu hiện tri ân", "example": "Please accept this personalized pen as a token of appreciation."}
    ],
    "collocations": [{"phrase": "company anniversary", "meaning": "ngày kỷ niệm thành lập công ty"}, {"phrase": "buy gifts for employees", "meaning": "mua quà tặng nhân viên"}],
    "grammar": [{"title": "Cấu trúc hỏi thăm việc đã làm 'Have you had a chance to...?'", "rule": "Have you had a chance to + V-inf?", "content": "Mẫu câu hỏi lịch sự trong công sở để kiểm tra xem đồng nghiệp đã kịp xử lý công việc chưa."}]
}

enrichment[63] = {
    "exp": "Người phụ nữ gợi ý: 'Well, a good quality travel mug would be practical, especially since so many people commute by train or bus' (Một chiếc cốc giữ nhiệt du lịch chất lượng tốt sẽ rất thiết thực, đặc biệt vì rất nhiều người đi làm bằng tàu hỏa hoặc xe buýt) -> Người phụ nữ gợi ý tặng cốc giữ nhiệt ('A travel mug'). Đáp án đúng là (A).",
    "vocab": [
        {"word": "travel mug", "ipa": "/ˈtræv.əl mʌɡ/", "pos": "n", "meaning": "cốc/bình giữ nhiệt mang đi", "example": "Stainless steel travel mugs keep coffee hot during commutes."},
        {"word": "practical", "ipa": "/ˈpræk.tɪ.kəl/", "pos": "adj", "meaning": "thiết thực, thực tế", "example": "Giving insulated tumblers is a very practical corporate gift."},
        {"word": "commute", "ipa": "/kəˈmjuːt/", "pos": "v", "meaning": "đi làm đều đặn hàng ngày", "example": "Thousands of workers commute into the financial center."}
    ],
    "collocations": [{"phrase": "travel mug", "meaning": "cốc giữ nhiệt di động"}, {"phrase": "commute by train", "meaning": "đi làm bằng tàu điện"}]
}

enrichment[64] = {
    "exp": "Người phụ nữ giới thiệu tập tài liệu quảng cáo: 'This company can print custom logos on the side' (Công ty này có thể in logo tùy chỉnh lên thân cốc). Người đàn ông khen: 'That is nice. I like that we can put our logo on it' (Tuyệt đấy. Tôi thích việc chúng ta có thể đặt logo của mình lên đó) -> Một tùy chọn bổ sung là in logo tùy chỉnh ('A custom logo'). Đáp án đúng là (C).",
    "vocab": [
        {"word": "custom", "ipa": "/ˈkʌs.təm/", "pos": "adj", "meaning": "được thiết kế theo yêu cầu riêng", "example": "We ordered custom branded polo shirts for the volunteers."},
        {"word": "logo", "ipa": "/ˈləʊ.ɡəʊ/", "pos": "n", "meaning": "biểu trưng, lô-gô công ty", "example": "The corporate logo was redesigned with modern typography."},
        {"word": "brochure", "ipa": "/ˈbrəʊ.ʃər/", "pos": "n", "meaning": "tập sách giới thiệu sản phẩm", "example": "Browse the promotional brochure for merchandise ideas."}
    ],
    "collocations": [{"phrase": "custom logo", "meaning": "logo in theo yêu cầu"}, {"phrase": "print on the side", "meaning": "in lên mặt bên/thân sản phẩm"}],
    "grammar": [{"title": "Mệnh đề danh ngữ sau động từ 'like'", "rule": "like that + S + can + V", "content": "Diễn tả sự hài lòng hoặc tán đồng một tính năng, dịch vụ cụ thể."}]
}

# Group 65 - 67 (Film shoot driving scene & street closure)
enrichment[65] = {
    "exp": "Người đàn ông mở đầu: 'Alberto, let's go over the locations for next week's shoot, for the driving scene' (Alberto, hãy xem lại các địa điểm ghi hình tuần tới cho cảnh lái xe) và nhắc đến diễn viên ('The actors will be driving...') -> Hai người làm việc trong ngành điện ảnh/làm phim ('Film'). Đáp án đúng là (B).",
    "vocab": [
        {"word": "shoot", "ipa": "/ʃuːt/", "pos": "n", "meaning": "buổi quay phim, buổi ghi hình", "example": "The commercial shoot was delayed due to heavy downpours."},
        {"word": "actor", "ipa": "/ˈæk.tər/", "pos": "n", "meaning": "diễn viên", "example": "The lead actors rehearsed their lines before shooting."},
        {"word": "scene", "ipa": "/siːn/", "pos": "n", "meaning": "cảnh quay trong phim", "example": "The dramatic driving scene was shot in the historic district."}
    ],
    "collocations": [{"phrase": "driving scene", "meaning": "cảnh quay lái xe ô tô"}, {"phrase": "film shoot", "meaning": "buổi quay phim"}],
    "grammar": [{"title": "Nhận diện ngành nghề qua từ vựng chuyên môn", "rule": "shoot + driving scene + actors -> Film industry", "content": "Tập hợp các từ vựng thuộc trường nghĩa nghệ thuật điện ảnh xác định trực tiếp lĩnh vực công tác."}]
}

enrichment[66] = {
    "exp": "Người phụ nữ giải thích: 'I'd rather use a wider street. Turning a camera rig around a tight corner takes too long. A wider road will make the process much easier' (Tôi muốn dùng đường rộng hơn. Việc quay một giá đỡ máy quay quanh góc hẹp tốn quá nhiều thời gian. Một con đường rộng hơn sẽ giúp quy trình dễ dàng hơn nhiều) -> Cô ấy muốn đổi vì quy trình sẽ thuận lợi hơn ('A process will be easier'). Đáp án đúng là (C).",
    "vocab": [
        {"word": "process", "ipa": "/ˈprəʊ.ses/", "pos": "n", "meaning": "quy trình, tiến trình công việc", "example": "Automating data entry made the billing process much easier."},
        {"word": "camera rig", "ipa": "/ˈkæm.rə rɪɡ/", "pos": "n", "meaning": "giá đỡ/khung giàn máy quay", "example": "Crews secured the heavy camera rig onto the camera car."},
        {"word": "tight corner", "ipa": "/taɪt ˈkɔː.nər/", "pos": "n", "meaning": "khúc cua hẹp, góc ngoặt gắt", "example": "Navigating the delivery van around tight corners is difficult."}
    ],
    "collocations": [{"phrase": "make a process easier", "meaning": "khiến một quy trình trở nên dễ dàng hơn"}, {"phrase": "wide street", "meaning": "con đường rộng rãi"}],
    "grammar": [{"title": "Cấu trúc diễn đạt sở thích 'would rather + V'", "rule": "S + would rather + V-inf (I'd rather use a wider street)", "content": "Diễn đạt ý muốn lựa chọn phương án này hơn phương án khác một cách lịch sự."}]
}

enrichment[67] = {
    "exp": "Nhìn vào sơ đồ bản đồ đường phố: Người phụ nữ đề xuất đổi sang đường Bangalore Avenue vì nó rộng rãi hơn. Người đàn ông đồng ý: 'OK. I'll arrange for that road to be closed to traffic during our shoot' -> Con đường cần đóng là đại lộ Bangalore ('Bangalore Avenue'). Đáp án đúng là (A).",
    "vocab": [
        {"word": "closed to traffic", "ipa": "/kləʊzd tuː ˈtræf.ɪk/", "pos": "adj phr", "meaning": "cấm đường, đóng cửa đối với phương tiện giao thông", "example": "Downtown avenues were closed to traffic during the marathon."},
        {"word": "avenue", "ipa": "/ˈæv.ə.njuː/", "pos": "n", "meaning": "đại lộ", "example": "The boutique is situated on a bustling commercial avenue."},
        {"word": "arrange for", "ipa": "/əˈreɪndʒ fɔːr/", "pos": "v phr", "meaning": "sắp xếp, thu xếp việc gì", "example": "Arrange for police permits before blocking public roads."}
    ],
    "collocations": [{"phrase": "closed to traffic", "meaning": "bị cấm lưu thông xe cộ"}, {"phrase": "arrange for something to be done", "meaning": "thu xếp cho việc gì được thực hiện"}],
    "grammar": [{"title": "Kỹ năng kết hợp hình ảnh bản đồ với lời thoại", "rule": "Đối chiếu tên đường được thống nhất trong audio với nhãn trên bản đồ", "content": "Xác định từ khóa tên đường 'Bangalore Avenue' từ lời đề nghị của người phụ nữ và sự chấp thuận của người đàn ông."}]
}

# Group 68 - 70 (Video game launch & weekend work)
enrichment[68] = {
    "exp": "Người phụ nữ mở lời: 'Hi, Pablo. I wanted to talk to you about the video game we designed—the one we're launching next month' (Chào Pablo. Tôi muốn nói chuyện với anh về trò chơi điện tử chúng ta đã thiết kế—trò chơi mà chúng ta sẽ ra mắt vào tháng tới) -> Họ đang chuẩn bị cho lễ ra mắt sản phẩm ('A product launch'). Đáp án đúng là (C).",
    "vocab": [
        {"word": "launch", "ipa": "/lɔːntʃ/", "pos": "n, v", "meaning": "sự ra mắt sản phẩm mới; tung ra thị trường", "example": "The marketing department orchestrated a nationwide product launch."},
        {"word": "video game", "ipa": "/ˈvɪd.i.əʊ ɡeɪm/", "pos": "n", "meaning": "trò chơi điện tử", "example": "The studio specializes in developing educational video games."},
        {"word": "design", "ipa": "/dɪˈzaɪn/", "pos": "v", "meaning": "thiết kế, lập trình sáng tạo", "example": "Engineers designed the user interface for optimal responsiveness."}
    ],
    "collocations": [{"phrase": "product launch", "meaning": "lễ ra mắt sản phẩm mới"}, {"phrase": "launch a game", "meaning": "tung trò chơi ra thị trường"}],
    "grammar": [{"title": "Thì Hiện tại tiếp diễn mang ý nghĩa tương lai gần", "rule": "be + V-ing (we're launching next month)", "content": "Diễn tả một sự kiện đã được lên lịch trình chắc chắn sẽ xảy ra trong tương lai gần."}]
}

enrichment[69] = {
    "exp": "Nhìn vào đồ họa các màn chơi (Levels): Người phụ nữ nói: 'Our beta testers found a software glitch when the character passes through the castle gates in Level 2' (Nhóm thử nghiệm beta phát hiện lỗi phần mềm khi nhân vật đi qua cổng lâu đài ở Cấp độ 2) -> Cấp độ xảy ra sự cố được thảo luận là Cấp độ 2 ('Level 2'). Đáp án đúng là (B).",
    "vocab": [
        {"word": "glitch", "ipa": "/ɡlɪtʃ/", "pos": "n", "meaning": "sự cố kỹ thuật nhỏ, lỗi phần mềm", "example": "A minor software glitch caused transaction confirmation delays."},
        {"word": "beta tester", "ipa": "/ˈbeɪ.tə ˈtes.tər/", "pos": "n", "meaning": "người thử nghiệm phiên bản tiền phát hành", "example": "Beta testers provided feedback on gameplay balance."},
        {"word": "castle gate", "ipa": "/ˈkɑː.səl ɡeɪt/", "pos": "n", "meaning": "cổng lâu đài (trong trò chơi)", "example": "The character unlocks the castle gate after finding the key."}
    ],
    "collocations": [{"phrase": "software glitch", "meaning": "lỗi phần mềm kỹ thuật"}, {"phrase": "beta tester", "meaning": "người dùng thử nghiệm beta"}],
    "grammar": [{"title": "Kỹ năng nghe bắt tên đối tượng kết hợp Graphic", "rule": "Key noun (Level 2) + issue (glitch)", "content": "Lắng nghe cụm từ 'in Level 2' đi kèm danh từ miêu tả lỗi 'glitch' để chọn ngay hàng tương ứng trên đồ họa."}]
}

enrichment[70] = {
    "exp": "Người phụ nữ đề xuất: 'We still have time before the release date, but we might have to come in on Saturday and Sunday to patch the code' (Chúng ta vẫn còn thời gian trước ngày phát hành, nhưng có thể chúng ta sẽ phải đến công ty vào thứ Bảy và Chủ nhật để vá mã nguồn) -> Người phụ nữ gợi ý làm việc vào cuối tuần ('Working over the weekend'). Paraphrasing: come in on Saturday and Sunday -> work over the weekend. Đáp án đúng là (C).",
    "vocab": [
        {"word": "weekend", "ipa": "/ˌwiːkˈend/", "pos": "n", "meaning": "dịp cuối tuần", "example": "The development team agreed to work over the weekend to meet the deadline."},
        {"word": "patch", "ipa": "/pætʃ/", "pos": "v", "meaning": "vá lỗi (phần mềm)", "example": "Developers released an emergency patch to fix the bug."},
        {"word": "release date", "ipa": "/rɪˈliːs deɪt/", "pos": "n", "meaning": "ngày phát hành chính thức", "example": "The album release date was announced yesterday."}
    ],
    "collocations": [{"phrase": "work over the weekend", "meaning": "làm thêm vào cuối tuần"}, {"phrase": "release date", "meaning": "ngày phát hành"}]
}

with open('scratch/p3_q44_q70_part.json', 'w', encoding='utf-8') as f:
    json.dump(enrichment, f, ensure_ascii=False, indent=2)
print("Saved Q44-Q70 successfully!")
