# part4_builder.py: Builds all 30 questions of Part 4 (Q71 - Q100)
import json

def get_part4_questions():
    talks = [
        {
            "range": "71-73",
            "audio": "assets/audio/part4.mp3",
            "image": None,
            "talk": "M-Au: You have reached the information line for the Cranbury Apartments management office. On Monday, April twelfth, maintenance workers will begin resurfacing the resident parking areas. All tenants must move their vehicles to the street or temporary overflow spaces before seven A.M. on that day. Any cars left in the lot will be towed at the owner's expense. Please refer to the detailed parking zone map that was mailed to your apartment last week. Thank you for your cooperation as we improve our property.",
            "talkVi": "Nam: Bạn đã gọi đến đường dây thông tin của văn phòng quản lý Chung cư Cranbury. Vào thứ Hai ngày 12 tháng 4, nhân viên bảo trì sẽ bắt đầu trải lại bề mặt các khu vực đỗ xe của cư dân. Tất cả người thuê phải di chuyển phương tiện ra ngoài đường hoặc các chỗ đỗ tạm thời trước 7 giờ sáng hôm đó. Bất kỳ xe nào còn để trong bãi sẽ bị kéo đi với chi phí do chủ xe chịu. Vui lòng tham khảo bản đồ phân vùng đỗ xe chi tiết đã được gửi qua đường bưu điện đến căn hộ của bạn tuần trước. Cảm ơn sự hợp tác của các bạn khi chúng tôi nâng cấp cơ sở vật chất.",
            "qs": [
                {
                    "id": 71, "text": "Who has recorded the message?", "textVi": "Ai là người đã ghi âm tin nhắn này?",
                    "options": {"A": "A city mayor's office", "B": "A maintenance department", "C": "An automobile dealership", "D": "A building management office"},
                    "optionsVi": {"A": "Văn phòng thị trưởng thành phố", "B": "Bộ phận bảo trì", "C": "Đại lý bán xe hơi", "D": "Văn phòng ban quản lý tòa nhà"},
                    "correct": "D",
                    "exp": "Người nói giới thiệu ngay câu đầu: 'You have reached the information line for the Cranbury Apartments management office' -> (D) A building management office.",
                    "vocab": [{"word": "resurface", "ipa": "/ˌriːˈsɜː.fɪs/", "pos": "v", "meaning": "trải lại mặt đường, làm mới bề mặt", "example": "resurface the parking lot"}],
                    "collocations": [{"phrase": "management office", "meaning": "văn phòng ban quản lý chung cư"}],
                    "grammar": [{"title": "Cấu trúc lời chào tổng đài", "rule": "You have reached + Organization", "analysis": "Mẫu câu chuẩn khi gọi điện đến tổng đài tự động."}]
                },
                {
                    "id": 72, "text": "What are the listeners asked to do?", "textVi": "Người nghe được yêu cầu làm gì?",
                    "options": {"A": "Move their vehicles", "B": "Pay their parking fines", "C": "Use an alternate entrance", "D": "Participate in a meeting"},
                    "optionsVi": {"A": "Di chuyển phương tiện của họ", "B": "Nộp tiền phạt đỗ xe", "C": "Dùng lối vào thay thế", "D": "Tham dự cuộc họp"},
                    "correct": "A",
                    "exp": "Thông báo nêu rõ: 'All tenants must move their vehicles to the street' -> (A) Move their vehicles.",
                    "vocab": [{"word": "tow", "ipa": "/təʊ/", "pos": "v", "meaning": "kéo xe, cẩu xe vi phạm", "example": "cars will be towed"}],
                    "collocations": [{"phrase": "move vehicles", "meaning": "di dời xe cộ"}],
                    "grammar": [{"title": "Động từ khuyết thiếu Must chỉ sự bắt buộc", "rule": "must + V-bare", "analysis": "Quy định bắt buộc đối với tất cả cư dân."}]
                },
                {
                    "id": 73, "text": "What does the speaker say was mailed last week?", "textVi": "Người nói cho biết thứ gì đã được gửi thư vào tuần trước?",
                    "options": {"A": "An election ballot", "B": "A maintenance plan", "C": "A map", "D": "A coupon"},
                    "optionsVi": {"A": "Lá phiếu bầu cử", "B": "Kế hoạch bảo trì", "C": "Một tấm bản đồ", "D": "Một phiếu giảm giá"},
                    "correct": "C",
                    "exp": "Người nói nhắc: 'Please refer to the detailed parking zone map that was mailed to your apartment last week' -> (C) A map.",
                    "vocab": [{"word": "mail", "ipa": "/meɪl/", "pos": "v", "meaning": "gửi qua đường bưu điện", "example": "mailed last week"}],
                    "collocations": [{"phrase": "detailed map", "meaning": "bản đồ chỉ dẫn chi tiết"}],
                    "grammar": [{"title": "Mệnh đề quan hệ rút gọn bị động", "rule": "map (that was) mailed last week", "analysis": "Bổ nghĩa cho bản đồ chỉ dẫn đỗ xe."}]
                }
            ]
        },
        {
            "range": "74-76",
            "audio": "assets/audio/part4.mp3",
            "image": None,
            "talk": "W-Am: Welcome to Your House Works. In today’s episode, we will be discussing practical techniques to maintain and make minor repairs to the roof of your home. Before climbing any ladder, it is critical to invest in high-quality safety gear, especially slip-resistant footwear and a sturdy harness. Never compromise on equipment quality when working at heights. Finally, I strongly recommend conducting a thorough roof inspection every autumn before winter storms arrive.",
            "talkVi": "Nữ: Chào mừng các bạn đến với chương trình Your House Works. Trong tập hôm nay, chúng ta sẽ thảo luận về các kỹ thuật thực tế để bảo dưỡng và tự sửa chữa các hư hỏng nhỏ trên mái nhà. Trước khi trèo lên thang, điều tối quan trọng là phải đầu tư vào đồ bảo hộ chất lượng cao, đặc biệt là giày chống trượt và dây an toàn chắc chắn. Đừng bao giờ thỏa hiệp về chất lượng thiết bị khi làm việc trên cao. Cuối cùng, tôi thực sự khuyên bạn nên kiểm tra kỹ lưỡng mái nhà vào mỗi mùa thu trước khi bão mùa đông đến.",
            "qs": [
                {
                    "id": 74, "text": "What is the topic of the episode?", "textVi": "Chủ đề của tập phát sóng hôm nay là gì?",
                    "options": {"A": "Garden landscaping", "B": "Window installation", "C": "Roof maintenance", "D": "Kitchen renovations"},
                    "optionsVi": {"A": "Cảnh quan sân vườn", "B": "Lắp đặt cửa sổ", "C": "Bảo dưỡng mái nhà", "D": "Cải tạo nhà bếp"},
                    "correct": "C",
                    "exp": "Người nói giới thiệu: 'maintain and make minor repairs to the roof of your home' -> (C) Roof maintenance.",
                    "vocab": [{"word": "maintenance", "ipa": "/ˈmeɪn.tən.əns/", "pos": "n", "meaning": "sự bảo dưỡng", "example": "roof maintenance"}],
                    "collocations": [{"phrase": "roof maintenance", "meaning": "bảo trì mái nhà"}],
                    "grammar": [{"title": "Paraphrase Maintain = Maintenance", "rule": "maintain (v) -> maintenance (n)", "analysis": "Chuyển đổi từ loại khi diễn đạt chủ đề bài nói."}]
                },
                {
                    "id": 75, "text": "What does the speaker emphasize about some tools?", "textVi": "Người nói nhấn mạnh điều gì về các dụng cụ/thiết bị?",
                    "options": {"A": "They should be cleaned regularly.", "B": "They should be of high quality.", "C": "They were recently invented.", "D": "They can be easily stored."},
                    "optionsVi": {"A": "Cần lau chùi thường xuyên", "B": "Phải có chất lượng cao", "C": "Mới được phát minh gần đây", "D": "Dễ cất giữ"},
                    "correct": "B",
                    "exp": "Người nói nhấn mạnh: 'invest in high-quality safety gear... Never compromise on equipment quality' -> (B) They should be of high quality.",
                    "vocab": [{"word": "gear", "ipa": "/ɡɪər/", "pos": "n", "meaning": "đồ dùng, thiết bị bảo hộ", "example": "safety gear"}],
                    "collocations": [{"phrase": "high-quality", "meaning": "chất lượng cao"}],
                    "grammar": [{"title": "Cụm tính từ ghép High-quality", "rule": "high + quality", "analysis": "Đóng vai trò tính từ bổ nghĩa cho danh từ gear."}]
                },
                {
                    "id": 76, "text": "What does the speaker recommend doing every year?", "textVi": "Người nói khuyên nên làm việc gì hàng năm?",
                    "options": {"A": "Treating some wood", "B": "Consulting an electrician", "C": "Conducting a roof inspection", "D": "Draining some water"},
                    "optionsVi": {"A": "Xử lý gỗ", "B": "Hỏi ý kiến thợ điện", "C": "Tiến hành kiểm tra mái nhà", "D": "Thoát nước"},
                    "correct": "C",
                    "exp": "Người nói khuyên: 'I strongly recommend conducting a thorough roof inspection every autumn' (every autumn = every year) -> (C) Conducting a roof inspection.",
                    "vocab": [{"word": "inspection", "ipa": "/ɪnˈspek.ʃən/", "pos": "n", "meaning": "sự kiểm tra", "example": "roof inspection"}],
                    "collocations": [{"phrase": "conduct an inspection", "meaning": "tiến hành kiểm tra"}],
                    "grammar": [{"title": "Collocation với Conduct", "rule": "conduct an inspection / survey", "analysis": "Thực hiện việc thanh tra, kiểm tra thực tế."}]
                }
            ]
        },
        {
            "range": "77-79",
            "audio": "assets/audio/part4.mp3",
            "image": None,
            "talk": "W-Am: Welcome to the conservatory! I’m Elena, your tour guide today. We’ll spend forty-five minutes viewing tropical plants and rare orchids. At two o’clock, guest botanist Dr. Kenneth Vance will deliver a special lecture in the auditorium on orchid conservation. Also, his newly published book, 'Orchid Caretakers', will be available for purchase and signing in the gift shop following the talk.",
            "talkVi": "Nữ: Chào mừng các bạn đến với nhà kính trồng cây! Tôi là Elena, hướng dẫn viên của các bạn hôm nay. Chúng ta sẽ dành 45 phút chiêm ngưỡng các loài thực vật nhiệt đới và hoa lan quý hiếm. Vào lúc 2 giờ, nhà thực vật học khách mời - Tiến sĩ Kenneth Vance sẽ có bài giảng đặc biệt tại hội trường về bảo tồn hoa lan. Ngoài ra, cuốn sách mới xuất bản của ông, 'Orchid Caretakers', sẽ được bán và ký tặng tại cửa hàng lưu niệm sau buổi nói chuyện.",
            "qs": [
                {
                    "id": 77, "text": "Who most likely is the speaker?", "textVi": "Người nói có nhiều khả năng là ai nhất?",
                    "options": {"A": "A radio show host", "B": "A tour guide", "C": "A sales associate", "D": "A professor"},
                    "optionsVi": {"A": "Người dẫn chương trình phát thanh", "B": "Một hướng dẫn viên du lịch", "C": "Nhân viên bán hàng", "D": "Một giáo sư"},
                    "correct": "B",
                    "exp": "Người nói tự giới thiệu: 'I’m Elena, your tour guide today' -> (B) A tour guide.",
                    "vocab": [{"word": "conservatory", "ipa": "/kənˈsɜː.və.tər.i/", "pos": "n", "meaning": "nhà kính trồng cây nghệ thuật", "example": "botanical conservatory"}],
                    "collocations": [{"phrase": "tour guide", "meaning": "hướng dẫn viên du lịch/tham quan"}],
                    "grammar": [{"title": "Tự giới thiệu chức danh", "rule": "I'm X, your + Role", "analysis": "Xác định danh tính người nói ngay đầu câu."}]
                },
                {
                    "id": 78, "text": "What will happen at two o’clock?", "textVi": "Điều gì sẽ diễn ra vào lúc 2 giờ?",
                    "options": {"A": "A park will close.", "B": "A demonstration will be given.", "C": "An interview will be conducted.", "D": "A lecture will begin."},
                    "optionsVi": {"A": "Công viên đóng cửa", "B": "Buổi biểu diễn diễn ra", "C": "Buổi phỏng vấn được thực hiện", "D": "Một bài giảng thuyết trình sẽ bắt đầu"},
                    "correct": "D",
                    "exp": "Người nói nêu: 'At two o’clock, guest botanist Dr. Kenneth Vance will deliver a special lecture' -> (D) A lecture will begin.",
                    "vocab": [{"word": "lecture", "ipa": "/ˈlek.tʃər/", "pos": "n", "meaning": "bài thuyết trình, bài giảng", "example": "deliver a lecture"}],
                    "collocations": [{"phrase": "deliver a lecture", "meaning": "thuyết trình, giảng bài"}],
                    "grammar": [{"title": "Paraphrase Deliver a lecture", "rule": "deliver a lecture = a lecture will begin", "analysis": "Diễn đạt lại hành động thuyết giảng."}]
                },
                {
                    "id": 79, "text": "What is Orchid Caretakers?", "textVi": "Orchid Caretakers là gì?",
                    "options": {"A": "A book", "B": "An album", "C": "A film", "D": "A magazine"},
                    "optionsVi": {"A": "Một cuốn sách", "B": "Một album nhạc", "C": "Một bộ phim", "D": "Một tờ tạp chí"},
                    "correct": "A",
                    "exp": "Người nói nói: 'his newly published book, 'Orchid Caretakers'' -> (A) A book.",
                    "vocab": [{"word": "caretaker", "ipa": "/ˈkeəˌteɪ.kər/", "pos": "n", "meaning": "người chăm sóc, người coi sóc", "example": "orchid caretakers"}],
                    "collocations": [{"phrase": "newly published book", "meaning": "cuốn sách mới xuất bản"}],
                    "grammar": [{"title": "Đồng vị ngữ danh từ (Appositive Noun Phrase)", "rule": "book, 'Title', ...", "analysis": "Tên sách đặt trong ngoặc đơn đóng vai trò đồng vị ngữ."}]
                }
            ]
        },
        {
            "range": "80-82",
            "audio": "assets/audio/part4.mp3",
            "image": None,
            "talk": "M-Au: Before the benefit concert begins, I want to thank all of you for supporting the Hillcaster Community Center. As you know, our facilities have been strained by the growing number of community programs we host. Tonight’s proceeds will directly fund our planned building expansion, adding two classrooms and a dance studio. Please be sure to visit the concession stand in the lobby during intermission to purchase refreshments, as all sales benefit the project.",
            "talkVi": "Nam: Trước khi buổi hòa nhạc từ thiện bắt đầu, tôi muốn cảm ơn tất cả các bạn đã ủng hộ Trung tâm Cộng đồng Hillcaster. Như các bạn đã biết, cơ sở vật chất của chúng tôi đã quá tải do số lượng các chương trình cộng đồng ngày càng tăng. Toàn bộ tiền thu được tối nay sẽ trực tiếp tài trợ cho dự án mở rộng tòa nhà, bổ sung 2 phòng học và 1 phòng tập nhảy. Hãy ghé quầy đồ ăn uống ở sảnh trong giờ giải lao để mua đồ giải khát, vì toàn bộ doanh thu sẽ đóng góp cho dự án.",
            "qs": [
                {
                    "id": 80, "text": "What event is taking place?", "textVi": "Sự kiện gì đang diễn ra?",
                    "options": {"A": "A sports competition", "B": "A fund-raising concert", "C": "A play rehearsal", "D": "An awards ceremony"},
                    "optionsVi": {"A": "Thi đấu thể thao", "B": "Buổi hòa nhạc gây quỹ", "C": "Buổi tập kịch", "D": "Lễ trao giải"},
                    "correct": "B",
                    "exp": "Người nói mở đầu: 'Before the benefit concert begins... Tonight’s proceeds will directly fund...' (benefit concert = fund-raising concert) -> (B).",
                    "vocab": [{"word": "benefit concert", "ipa": "/ˈben.ɪ.fɪt ˈkɒn.sət/", "pos": "n", "meaning": "buổi hòa nhạc từ thiện gây quỹ", "example": "charity benefit concert"}],
                    "collocations": [{"phrase": "benefit concert", "meaning": "hòa nhạc quyên góp quỹ"}],
                    "grammar": [{"title": "Paraphrase Benefit = Fund-raising", "rule": "benefit concert = fund-raising concert", "analysis": "Cụm từ tương đương trong chủ đề hoạt động cộng đồng."}]
                },
                {
                    "id": 81, "text": "What does the organization plan to do?", "textVi": "Tổ chức này có kế hoạch làm gì?",
                    "options": {"A": "Change a policy", "B": "Expand a facility / building", "C": "Select a winner", "D": "Sponsor a team"},
                    "optionsVi": {"A": "Đổi chính sách", "B": "Mở rộng cơ sở vật chất / tòa nhà", "C": "Chọn người chiến thắng", "D": "Tài trợ một đội nhóm"},
                    "correct": "B",
                    "exp": "Người nói giải thích: 'fund our planned building expansion, adding two classrooms...' -> (B) Expand a facility / building.",
                    "vocab": [{"word": "expansion", "ipa": "/ɪkˈspæn.ʃən/", "pos": "n", "meaning": "sự mở rộng", "example": "building expansion"}],
                    "collocations": [{"phrase": "building expansion", "meaning": "mở rộng công trình xây dựng"}],
                    "grammar": [{"title": "Danh từ hóa hành động (Nominalization)", "rule": "expand (v) -> expansion (n)", "analysis": "Dùng danh từ expansion để chỉ dự án xây dựng mở rộng."}]
                },
                {
                    "id": 82, "text": "What does the speaker encourage the listeners to do?", "textVi": "Người nói khuyến khích người nghe làm gì?",
                    "options": {"A": "Order tickets early", "B": "Visit a community center", "C": "Purchase refreshments", "D": "Donate clothing"},
                    "optionsVi": {"A": "Đặt vé sớm", "B": "Đến thăm trung tâm", "C": "Mua đồ giải khát / thức ăn nhẹ", "D": "Quyên góp quần áo"},
                    "correct": "C",
                    "exp": "Người nói kêu gọi: 'visit the concession stand in the lobby... to purchase refreshments' -> (C) Purchase refreshments.",
                    "vocab": [{"word": "refreshments", "ipa": "/rɪˈfreʃ.mənts/", "pos": "n", "meaning": "đồ ăn nhẹ và nước giải khát", "example": "purchase refreshments"}],
                    "collocations": [{"phrase": "purchase refreshments", "meaning": "mua đồ ăn nhẹ giải khát"}],
                    "grammar": [{"title": "Động từ khuyến khích kết hợp to-V", "rule": "encourage + someone + to V", "analysis": "Khuyến khích người nghe chi tiêu tại quầy giải khát."}]
                }
            ]
        },
        {
            "range": "83-85",
            "audio": "assets/audio/part4.mp3",
            "image": None,
            "talk": "M-Cn: Thank you all for attending today’s workshop. Erina Kimura and I will be conducting sessions focused on improving team productivity and time management in hybrid work environments. If you didn't receive the printed packet containing the case studies, Erina’s at the back of the room and can hand you a copy. Before we jump into our presentation, we’ll do a five-minute icebreaker activity where you introduce yourself to the colleague sitting next to you.",
            "talkVi": "Nam: Cảm ơn các bạn đã tham dự buổi hội thảo hôm nay. Erina Kimura và tôi sẽ chủ trì các phiên tập trung vào việc cải thiện năng suất đội nhóm và quản lý thời gian trong môi trường làm việc kết hợp. Nếu bạn chưa nhận được tập tài liệu in chứa các bài nghiên cứu tình huống, Erina đang ở phía cuối phòng và có thể phát cho bạn một bản. Trước khi bắt đầu bài thuyết trình, chúng ta sẽ thực hiện hoạt động khởi động 5 phút để bạn tự giới thiệu bản thân với đồng nghiệp ngồi bên cạnh.",
            "qs": [
                {
                    "id": 83, "text": "What is the topic of the workshop?", "textVi": "Chủ đề của buổi hội thảo là gì?",
                    "options": {"A": "Financial accounting", "B": "Public speaking", "C": "Time management and productivity", "D": "Software development"},
                    "optionsVi": {"A": "Kế toán tài chính", "B": "Nói trước công chúng", "C": "Quản lý thời gian và năng suất", "D": "Phát triển phần mềm"},
                    "correct": "C",
                    "exp": "Người nói nêu: 'focused on improving team productivity and time management' -> (C) Time management and productivity.",
                    "vocab": [{"word": "productivity", "ipa": "/ˌprɒd.ʌkˈtɪv.ə.ti/", "pos": "n", "meaning": "năng suất làm việc", "example": "workplace productivity"}],
                    "collocations": [{"phrase": "time management", "meaning": "quản lý thời gian hiệu quả"}],
                    "grammar": [{"title": "Rút gọn mệnh đề phân từ", "rule": "sessions focused on...", "analysis": "Phân từ quá khứ focused bổ nghĩa cho sessions."}]
                },
                {
                    "id": 84, "text": "What does the speaker imply when he says, \"Erina’s at the back of the room\"?", "textVi": "Người nói ngụ ý gì khi nói \"Erina đang ở phía cuối phòng\"?",
                    "options": {"A": "A guest speaker has just arrived.", "B": "Assistance / materials are available.", "C": "Attendees should speak loudly.", "D": "An extra chair should be provided."},
                    "optionsVi": {"A": "Diễn giả khách mời vừa đến", "B": "Có sự hỗ trợ / tài liệu được cung cấp ở đó", "C": "Người nghe nên nói to", "D": "Cần thêm ghế"},
                    "correct": "B",
                    "exp": "Người nói trước đó bảo: 'If you didn't receive the printed packet... Erina’s at the back of the room and can hand you a copy' -> (B) Assistance / materials are available.",
                    "vocab": [{"word": "packet", "ipa": "/ˈpæk.ɪt/", "pos": "n", "meaning": "tập tài liệu in", "example": "information packet"}],
                    "collocations": [{"phrase": "hand someone a copy", "meaning": "trao tận tay cho ai một bản sao"}],
                    "grammar": [{"title": "Câu hỏi hàm ngôn tình huống", "rule": "If you lack materials -> Erina is at the back", "analysis": "Chỉ dẫn hành động giải quyết sự thiếu tài liệu."}]
                },
                {
                    "id": 85, "text": "What will the listeners do next?", "textVi": "Người nghe sẽ làm gì tiếp theo?",
                    "options": {"A": "Participate in an introductory activity", "B": "Take a short break", "C": "Sign their names on a list", "D": "Fill out an evaluation form"},
                    "optionsVi": {"A": "Tham gia vào một hoạt động khởi động / giới thiệu", "B": "Nghỉ giải lao ngắn", "C": "Ký tên vào danh sách", "D": "Điền biểu mẫu đánh giá"},
                    "correct": "A",
                    "exp": "Người nói bảo: 'we’ll do a five-minute icebreaker activity where you introduce yourself...' (icebreaker = introductory activity) -> (A).",
                    "vocab": [{"word": "icebreaker", "ipa": "/ˈaɪsˌbreɪ.kər/", "pos": "n", "meaning": "hoạt động khởi động giao lưu phá băng", "example": "icebreaker game"}],
                    "collocations": [{"phrase": "icebreaker activity", "meaning": "hoạt động khởi động làm quen"}],
                    "grammar": [{"title": "Paraphrase Icebreaker = Introductory activity", "rule": "icebreaker = introductory activity", "analysis": "Thuật ngữ tương đương chỉ hoạt động làm quen mở đầu khóa học."}]
                }
            ]
        },
        {
            "range": "86-88",
            "audio": "assets/audio/part4.mp3",
            "image": None,
            "talk": "W-Br: At this site, archaeologists have uncovered the remains of a fifth-century marketplace with colorful mosaic tiles on the walls. You’ll be able to admire these intricate artworks from our newly constructed elevated viewing platform. However, I must apologize because the underground catacombs are temporarily closed today for restoration work. As we walk along the perimeter, please stay behind the safety ropes and use the handrails when going down the stone steps.",
            "talkVi": "Nữ: Tại địa điểm này, các nhà khảo cổ học đã phát hiện tàn tích của một khu chợ thế kỷ thứ 5 với những bức tranh khảm gạch đầy màu sắc trên tường. Các bạn sẽ có thể chiêm ngưỡng những tác phẩm nghệ thuật tinh xảo này từ bục quan sát trên cao mới được xây dựng. Tuy nhiên, tôi phải xin lỗi vì các hầm mộ dưới lòng đất hôm nay tạm thời đóng cửa để trùng tu. Khi chúng ta đi dọc theo chu vi, vui lòng đứng sau dây an toàn và vịn vào tay vịn khi bước xuống các bậc đá.",
            "qs": [
                {
                    "id": 86, "text": "What is the historical site famous for?", "textVi": "Khu di tích lịch sử này nổi tiếng vì điều gì?",
                    "options": {"A": "Its defensive walls", "B": "Its royal inhabitants", "C": "An event that happened there", "D": "Some artwork / mosaic tiles"},
                    "optionsVi": {"A": "Những bức tường phòng thủ", "B": "Các cư dân hoàng gia", "C": "Một sự kiện đã diễn ra ở đó", "D": "Tác phẩm nghệ thuật / gạch khảm mosaic"},
                    "correct": "D",
                    "exp": "Người nói nhắc tới: 'colorful mosaic tiles... intricate artworks' -> (D) Some artwork / mosaic tiles.",
                    "vocab": [{"word": "mosaic", "ipa": "/məʊˈzeɪ.ɪk/", "pos": "n, adj", "meaning": "nghệ thuật khảm tranh bằng gạch đá", "example": "mosaic tiles"}],
                    "collocations": [{"phrase": "mosaic tiles", "meaning": "gạch khảm nghệ thuật"}],
                    "grammar": [{"title": "Từ vựng mỹ thuật lịch sử", "rule": "mosaic tiles = artwork", "analysis": "Nhận diện thể loại tác phẩm nghệ thuật đặc thù."}]
                },
                {
                    "id": 87, "text": "Why does the speaker apologize?", "textVi": "Tại sao người nói lại xin lỗi?",
                    "options": {"A": "An area is closed to visitors", "B": "The listeners cannot take pictures", "C": "There is no gift shop", "D": "A tour started late"},
                    "optionsVi": {"A": "Một khu vực bị đóng cửa đối với khách tham quan", "B": "Khách không được chụp ảnh", "C": "Không có cửa hàng lưu niệm", "D": "Chuyến tham quan bắt đầu muộn"},
                    "correct": "A",
                    "exp": "Người nói nói: 'I must apologize because the underground catacombs are temporarily closed today' -> (A) An area is closed to visitors.",
                    "vocab": [{"word": "catacombs", "ipa": "/ˈkæt.ə.kuːmz/", "pos": "n", "meaning": "hầm mộ ngầm dưới lòng đất", "example": "ancient catacombs"}],
                    "collocations": [{"phrase": "temporarily closed", "meaning": "tạm thời đóng cửa"}],
                    "grammar": [{"title": "Lời xin lỗi lịch sự trong ngành dịch vụ", "rule": "apologize because + clause", "analysis": "Nêu nguyên nhân của sự bất tiện cho khách tham quan."}]
                },
                {
                    "id": 88, "text": "What does the speaker ask the listeners to do?", "textVi": "Người nói yêu cầu người nghe làm gì?",
                    "options": {"A": "Show their tickets", "B": "Put on protective clothing", "C": "Use some handrails", "D": "Speak quietly"},
                    "optionsVi": {"A": "Xuất trình vé", "B": "Mặc quần áo bảo hộ", "C": "Sử dụng tay vịn lan can", "D": "Nói chuyện nhỏ nhẹ"},
                    "correct": "C",
                    "exp": "Người nói dặn: 'use the handrails when going down the stone steps' -> (C) Use some handrails.",
                    "vocab": [{"word": "handrail", "ipa": "/ˈhænd.reɪl/", "pos": "n", "meaning": "tay vịn cầu thang/lan can", "example": "hold the handrails"}],
                    "collocations": [{"phrase": "use handrails", "meaning": "vịn tay vào lan can an toàn"}],
                    "grammar": [{"title": "Câu mệnh lệnh chỉ dẫn an toàn", "rule": "Please + V-bare (use handrails)", "analysis": "Yêu cầu hành khách bảo đảm an toàn khi di chuyển."}]
                }
            ]
        },
        {
            "range": "89-91",
            "audio": "assets/audio/part4.mp3",
            "image": None,
            "talk": "M-Cn: As you all know, our agency’s just won an important advertising contract with Parker Auto Parts Company. We’ll be developing two thirty-second television commercials for their new nationwide brand campaign. Now, the client wants to debut the ads during the championship playoffs next month, which means this is a top priority. In just a moment, I'll project our preliminary storyboard sketches on the screen so we can brainstorm catchy slogans.",
            "talkVi": "Nam: Như các bạn đều biết, công ty quảng cáo của chúng ta vừa giành được hợp đồng quan trọng với Công ty Phụ tùng Ô tô Parker. Chúng ta sẽ phát triển hai đoạn phim quảng cáo truyền hình dài 30 giây cho chiến dịch thương hiệu toàn quốc mới của họ. Khách hàng muốn phát sóng các quảng cáo này trong các trận đấu giải vô địch vào tháng tới, đồng nghĩa với việc đây là ưu tiên hàng đầu. Lát nữa, tôi sẽ chiếu các bản phác thảo kịch bản phân cảnh sơ bộ lên màn hình để chúng ta cùng lên ý tưởng slogan ấn tượng.",
            "qs": [
                {
                    "id": 89, "text": "What is the speaker mainly discussing?", "textVi": "Người nói chủ yếu thảo luận về vấn đề gì?",
                    "options": {"A": "An office relocation", "B": "A budget audit", "C": "An advertising campaign / commercial", "D": "A staff restructuring"},
                    "optionsVi": {"A": "Chuyển văn phòng", "B": "Kiểm toán ngân sách", "C": "Chiến dịch quảng cáo truyền hình", "D": "Tái cơ cấu nhân sự"},
                    "correct": "C",
                    "exp": "Người nói thông báo giành được hợp đồng: 'advertising contract... developing two thirty-second television commercials' -> (C) An advertising campaign / commercial.",
                    "vocab": [{"word": "commercial", "ipa": "/kəˈmɜː.ʃəl/", "pos": "n", "meaning": "đoạn phim quảng cáo truyền hình", "example": "television commercials"}],
                    "collocations": [{"phrase": "advertising campaign", "meaning": "chiến dịch quảng bá thương hiệu"}],
                    "grammar": [{"title": "Cụm danh từ ngành quảng cáo", "rule": "commercials + advertising contract -> advertising campaign", "analysis": "Xác định trọng tâm nội dung kinh doanh."}]
                },
                {
                    "id": 90, "text": "What does the speaker imply when he says, \"this is a priority\"?", "textVi": "Người nói ngụ ý gì khi nói \"đây là một ưu tiên hàng đầu\"?",
                    "options": {"A": "Overtime pay has been approved.", "B": "A deadline is tight / must be met.", "C": "A client expressed concern.", "D": "Staff will be evaluated closely."},
                    "optionsVi": {"A": "Lương làm thêm giờ đã được duyệt", "B": "Thời hạn rất gấp và phải hoàn thành đúng hạn", "C": "Khách hàng bày tỏ lo ngại", "D": "Nhân viên sẽ bị đánh giá kỹ"},
                    "correct": "B",
                    "exp": "Người nói giải thích: khách hàng muốn phát quảng cáo vào tháng tới trong mùa giải ('during the championship playoffs next month, which means this is a top priority') ngụ ý thời hạn gấp -> (B) A deadline is tight / must be met.",
                    "vocab": [{"word": "priority", "ipa": "/praɪˈɒr.ə.ti/", "pos": "n", "meaning": "sự ưu tiên", "example": "top priority"}],
                    "collocations": [{"phrase": "top priority", "meaning": "ưu tiên số một"}],
                    "grammar": [{"title": "Câu hỏi hàm ngôn về áp lực công việc", "rule": "which means this is a priority -> tight deadline", "analysis": "Suy luận về áp lực tiến độ hoàn thành trước giải đấu."}]
                },
                {
                    "id": 91, "text": "What will the listeners do next?", "textVi": "Người nghe sẽ làm gì tiếp theo?",
                    "options": {"A": "Review a budget sheet", "B": "Vote on a director", "C": "View a presentation / storyboard sketches", "D": "Interview some customers"},
                    "optionsVi": {"A": "Xem bảng ngân sách", "B": "Bỏ phiếu chọn đạo diễn", "C": "Xem bản phác thảo kịch bản phân cảnh trên màn hình", "D": "Phỏng vấn khách hàng"},
                    "correct": "C",
                    "exp": "Người nói nói: 'I'll project our preliminary storyboard sketches on the screen' -> (C) View a presentation / storyboard sketches.",
                    "vocab": [{"word": "storyboard", "ipa": "/ˈstɔː.ri.bɔːd/", "pos": "n", "meaning": "kịch bản phân cảnh bằng hình vẽ", "example": "storyboard sketches"}],
                    "collocations": [{"phrase": "brainstorm slogans", "meaning": "động não nghĩ khẩu hiệu quảng cáo"}],
                    "grammar": [{"title": "Cụm từ thời gian In just a moment", "rule": "In just a moment, I'll + V", "analysis": "Diễn tả hành động chuẩn bị thực hiện ngay tức khắc."}]
                }
            ]
        },
        {
            "range": "92-94",
            "audio": "assets/audio/part4.mp3",
            "image": None,
            "talk": "W-Am: Excuse me, nurses. Your attention please. I’ve been receiving complaints about the free snacks in the hospital break rooms. Several staff members on the night shift reported that the fruit and yogurt are often depleted by 10 P.M. We want to make sure everyone working long hours has access to refreshments. Some have asked if we can increase the weekly restocking budget. That will require management approval, but in the meantime, I’ll ask our supplier to deliver twice as many nonperishable energy bars.",
            "talkVi": "Nữ: Xin lỗi các điều dưỡng viên, xin hãy chú ý. Tôi đã nhận được những phàn nàn về đồ ăn nhẹ miễn phí trong phòng nghỉ của bệnh viện. Một số nhân viên ca đêm báo rằng trái cây và sữa chua thường hết sạch trước 10 giờ tối. Chúng tôi muốn đảm bảo mọi người làm ca dài đều có đồ ăn nhẹ. Có người hỏi liệu chúng ta có thể tăng ngân sách tiếp tế hàng tuần không. Việc đó sẽ cần ban quản lý phê duyệt, nhưng trong lúc chờ đợi, tôi sẽ yêu cầu nhà cung cấp giao thêm gấp đôi thanh năng lượng lâu hỏng.",
            "qs": [
                {
                    "id": 92, "text": "Where do the listeners most likely work?", "textVi": "Người nghe có nhiều khả năng làm việc ở đâu nhất?",
                    "options": {"A": "At a restaurant", "B": "At a hospital", "C": "At a grocery store", "D": "At a fitness center"},
                    "optionsVi": {"A": "Nhà hàng", "B": "Bệnh viện", "C": "Cửa hàng tạp hóa", "D": "Trung tâm thể hình"},
                    "correct": "B",
                    "exp": "Người nói gọi: 'Excuse me, nurses... in the hospital break rooms' -> (B) At a hospital.",
                    "vocab": [{"word": "nurse", "ipa": "/nɜːs/", "pos": "n", "meaning": "y tá, điều dưỡng viên", "example": "registered nurses"}],
                    "collocations": [{"phrase": "hospital break room", "meaning": "phòng nghỉ của nhân viên bệnh viện"}],
                    "grammar": [{"title": "Xác định đối tượng lắng nghe", "rule": "nurses + hospital -> hospital", "analysis": "Lời mở đầu trực tiếp chỉ rõ đối tượng và địa điểm."}]
                },
                {
                    "id": 93, "text": "What is the main purpose of the talk?", "textVi": "Mục đích chính của bài nói là gì?",
                    "options": {"A": "To request an evaluation", "B": "To address staff complaints about break room snacks", "C": "To introduce a new shift schedule", "D": "To explain medical protocols"},
                    "optionsVi": {"A": "Yêu cầu đánh giá", "B": "Giải quyết phàn nàn của nhân viên về đồ ăn nhẹ", "C": "Giới thiệu lịch ca làm mới", "D": "Giải thích quy trình y tế"},
                    "correct": "B",
                    "exp": "Người nói mở đầu: 'I’ve been receiving complaints about the free snacks in the hospital break rooms' -> (B) To address staff complaints about break room snacks.",
                    "vocab": [{"word": "complaint", "ipa": "/kəmˈpleɪnt/", "pos": "n", "meaning": "lời phàn nàn, khiếu nại", "example": "receive complaints"}],
                    "collocations": [{"phrase": "address complaints", "meaning": "giải quyết khiếu nại, phản ánh"}],
                    "grammar": [{"title": "Thì Hiện tại hoàn thành tiếp diễn", "rule": "have been receiving + Noun", "analysis": "Diễn tả hành động tiếp nhận phản ánh liên tục diễn ra từ gần đây."}]
                },
                {
                    "id": 94, "text": "What does the speaker imply when she says, \"That will require management approval\"?", "textVi": "Người nói ngụ ý gì khi nói \"Điều đó sẽ cần có sự phê duyệt của ban quản lý\"?",
                    "options": {"A": "A process was violated.", "B": "Overtime hours must be logged.", "C": "A budget increase cannot happen immediately.", "D": "Staff should contact the director."},
                    "optionsVi": {"A": "Vi phạm quy trình", "B": "Cần ghi chép giờ làm thêm", "C": "Tăng ngân sách không thể thực hiện ngay lập tức", "D": "Nhân viên nên liên hệ giám đốc"},
                    "correct": "C",
                    "exp": "Người nói giải thích về việc tăng ngân sách ('increase weekly budget') phải cần cấp trên duyệt, nên chưa thể làm ngay mà phải dùng giải pháp tạm thời ('in the meantime') -> (C) A budget increase cannot happen immediately.",
                    "vocab": [{"word": "nonperishable", "ipa": "/ˌnɒnˈper.ɪ.ʃə.bəl/", "pos": "adj", "meaning": "không dễ hư hỏng, để được lâu", "example": "nonperishable snacks"}],
                    "collocations": [{"phrase": "management approval", "meaning": "sự phê chuẩn của cấp quản lý"}],
                    "grammar": [{"title": "Cụm liên từ In the meantime", "rule": "in the meantime = meanwhile", "analysis": "Nêu giải pháp tạm thời trong khi chờ đợi phê duyệt."}]
                }
            ]
        },
        {
            "range": "95-97",
            "audio": "assets/audio/part4.mp3",
            "image": "assets/images/graphic_q95_97.png",
            "talk": "M-Cn: As mayor of Lakeville, I’m pleased to welcome you to the celebration for our town’s newly renovated Lakeville Nature Park! The three-month upgrade project repaired all the timber bridges and repaved the main walking loop. We’ll begin our ceremonial walk here at the entrance. We'll end our walk on the hill on the north side of the park, where we’ll be serving free snacks and ice cream. For those taking photos today, don't forget to complete our online visitor survey by scanning the QR code at the exits.",
            "talkVi": "Nam: Với tư cách là thị trưởng Lakeville, tôi rất vui mừng chào đón các bạn đến với buổi lễ khánh thành Công viên Thiên nhiên Lakeville vừa được cải tạo lại! Dự án nâng cấp kéo dài 3 tháng đã sửa chữa toàn bộ cầu gỗ và trải lại mặt đường cho đường đi bộ chính. Chúng ta sẽ bắt đầu cuộc đi bộ khánh thành tại lối vào. Chúng ta sẽ kết thúc cuộc đi bộ trên ngọn đồi ở phía bắc công viên, nơi chúng tôi sẽ phục vụ đồ ăn nhẹ và kem miễn phí. Đối với những ai chụp ảnh hôm nay, đừng quên hoàn thành khảo sát trực tuyến bằng cách quét mã QR tại các lối ra.",
            "qs": [
                {
                    "id": 95, "text": "According to the speaker, what was recently completed?", "textVi": "Theo người nói, công trình gì vừa được hoàn thành gần đây?",
                    "options": {"A": "A municipal library", "B": "A commercial plaza", "C": "A park renovation", "D": "A sports stadium"},
                    "optionsVi": {"A": "Thư viện thành phố", "B": "Khu thương mại", "C": "Dự án cải tạo công viên", "D": "Sân vận động thể thao"},
                    "correct": "C",
                    "exp": "Thị trưởng nói: 'celebration for our town’s newly renovated Lakeville Nature Park' -> (C) A park renovation.",
                    "vocab": [{"word": "renovate", "ipa": "/ˈren.ə.veɪt/", "pos": "v", "meaning": "cải tạo, nâng cấp", "example": "newly renovated park"}],
                    "collocations": [{"phrase": "park renovation", "meaning": "cải tạo công viên"}],
                    "grammar": [{"title": "Quá khứ phân từ làm tính từ", "rule": "newly renovated + Noun", "analysis": "Bổ nghĩa cho công viên mới được trùng tu xong."}]
                },
                {
                    "id": 96, "text": "Look at the graphic. Where does the speaker say refreshments will be served?", "textVi": "Nhìn vào biểu đồ. Người nói cho biết đồ ăn nhẹ giải khát sẽ được phục vụ ở đâu?",
                    "options": {"A": "Location 1", "B": "Location 2", "C": "Location 3", "D": "Location 4"},
                    "optionsVi": {"A": "Vị trí 1", "B": "Vị trí 2", "C": "Vị trí 3", "D": "Vị trí 4"},
                    "correct": "A",
                    "exp": "Người nói nói: 'We'll end our walk on the hill on the north side of the park, where we’ll be serving free snacks and ice cream'. Nhìn bản đồ, '1. Hill' nằm ở phía bắc -> (A) Location 1.",
                    "vocab": [{"word": "hill", "ipa": "/hɪl/", "pos": "n", "meaning": "ngọn đồi", "example": "hill on the north side"}],
                    "collocations": [{"phrase": "serving free snacks", "meaning": "phục vụ đồ ăn nhẹ miễn phí"}],
                    "grammar": [{"title": "Kỹ năng giải câu hỏi bản đồ", "rule": "the hill on the north side = Location 1 (Hill)", "analysis": "Khớp phương hướng 'north' và địa danh 'hill' trên sơ đồ."}]
                },
                {
                    "id": 97, "text": "What are the listeners reminded to do?", "textVi": "Người nghe được nhắc nhở làm điều gì?",
                    "options": {"A": "Donate money", "B": "Join a committee", "C": "Clean up litter", "D": "Complete an online survey"},
                    "optionsVi": {"A": "Quyên góp tiền", "B": "Tham gia ủy ban", "C": "Dọn rác", "D": "Hoàn thành một bài khảo sát trực tuyến"},
                    "correct": "D",
                    "exp": "Thị trưởng nhắc: 'don't forget to complete our online visitor survey by scanning the QR code' -> (D) Complete an online survey.",
                    "vocab": [{"word": "survey", "ipa": "/ˈsɜː.veɪ/", "pos": "n", "meaning": "bài khảo sát ý kiến", "example": "visitor survey"}],
                    "collocations": [{"phrase": "complete an online survey", "meaning": "điền khảo sát trực tuyến"}],
                    "grammar": [{"title": "Cấu trúc Don't forget to V", "rule": "Don't forget to + V-bare", "analysis": "Lời nhắc nhở nhẹ nhàng nhưng dứt khoát."}]
                }
            ]
        },
        {
            "range": "98-100",
            "audio": "assets/audio/part4.mp3",
            "image": "assets/images/graphic_q98_100.png",
            "talk": "W-Br: Thanks, everyone, for attending today’s free public lecture, sponsored by the Springfield Farmers’ Association. Today, we’re going to discuss the importance of soil testing for maintaining crop health and maximizing yield. Since this is September, all soil samples should be extracted from a depth of twelve inches. That ensures we test the root zone before cold weather sets in. Before you leave, please consider signing up for our monthly newsletter at the table in the back.",
            "talkVi": "Nữ: Cảm ơn mọi người đã tham dự buổi diễn thuyết công cộng miễn phí hôm nay do Hiệp hội Nông dân Springfield tài trợ. Hôm nay, chúng ta sẽ thảo luận về tầm quan trọng của việc kiểm tra đất để duy trì sức khỏe cây trồng và tối đa hóa năng suất. Vì hiện tại là tháng Chín, tất cả các mẫu đất cần được lấy từ độ sâu 12 inch. Điều đó đảm bảo chúng ta kiểm tra đúng tầng rễ trước khi thời tiết lạnh ập đến. Trước khi ra về, xin vui lòng cân nhắc đăng ký nhận bản tin hàng tháng của chúng tôi tại chiếc bàn phía sau.",
            "qs": [
                {
                    "id": 98, "text": "What is the topic of today’s lecture?", "textVi": "Chủ đề của bài diễn thuyết hôm nay là gì?",
                    "options": {"A": "When to harvest crops", "B": "Where to plant trees", "C": "Soil testing for crop health", "D": "Which flowers need more sun"},
                    "optionsVi": {"A": "Khi nào thu hoạch mùa màng", "B": "Trồng cây ở đâu", "C": "Kiểm tra đất để bảo vệ mùa màng", "D": "Loài hoa nào cần nhiều nắng"},
                    "correct": "C",
                    "exp": "Người nói thông báo: 'discuss the importance of soil testing for maintaining crop health' -> (C) Soil testing for crop health.",
                    "vocab": [{"word": "soil testing", "ipa": "/sɔɪl ˈtes.tɪŋ/", "pos": "n", "meaning": "việc kiểm nghiệm chất lượng đất", "example": "agricultural soil testing"}],
                    "collocations": [{"phrase": "maximize yield", "meaning": "tối đa hóa sản lượng mùa vụ"}],
                    "grammar": [{"title": "Danh động từ làm tân ngữ sau giới từ", "rule": "importance of + V-ing", "analysis": "Nhấn mạnh ý nghĩa của việc xét nghiệm đất."}]
                },
                {
                    "id": 99, "text": "Look at the graphic. At what depth should samples be collected this month?", "textVi": "Nhìn vào biểu đồ. Trong tháng này, các mẫu đất nên được thu thập ở độ sâu bao nhiêu?",
                    "options": {"A": "4 inches", "B": "6 inches", "C": "12 inches", "D": "8 inches"},
                    "optionsVi": {"A": "4 inch", "B": "6 inch", "C": "12 inch", "D": "8 inch"},
                    "correct": "C",
                    "exp": "Người nói nói: 'Since this is September... extracted from a depth of twelve inches'. Nhìn vào bảng 'Soil Sampling Timeline', hàng 'September-October' ghi Depth là '12 inches' -> (C) 12 inches.",
                    "vocab": [{"word": "depth", "ipa": "/depθ/", "pos": "n", "meaning": "độ sâu", "example": "depth of 12 inches"}],
                    "collocations": [{"phrase": "extract samples", "meaning": "lấy mẫu xét nghiệm"}],
                    "grammar": [{"title": "Đối chiếu bảng thời gian biểu", "rule": "September -> Row: September-October -> Depth: 12 inches", "analysis": "Đối chiếu mốc tháng hiện tại với bảng dữ liệu để tìm thông số."}]
                },
                {
                    "id": 100, "text": "What does the speaker encourage the listeners to do?", "textVi": "Người nói khuyến khích người nghe làm gì?",
                    "options": {"A": "Turn off mobile phones", "B": "Have some refreshments", "C": "Sign up for a monthly newsletter / mailing list", "D": "Purchase some seeds"},
                    "optionsVi": {"A": "Tắt điện thoại", "B": "Ăn nhẹ", "C": "Đăng ký nhận bản tin / danh sách gửi thư hàng tháng", "D": "Mua hạt giống"},
                    "correct": "C",
                    "exp": "Người nói khuyên: 'please consider signing up for our monthly newsletter at the table in the back' -> (C) Sign up for a monthly newsletter / mailing list.",
                    "vocab": [{"word": "newsletter", "ipa": "/ˈnjuːzˌlet.ər/", "pos": "n", "meaning": "bản tin định kỳ", "example": "monthly newsletter"}],
                    "collocations": [{"phrase": "sign up for a newsletter", "meaning": "đăng ký nhận bản tin qua email/thư"}],
                    "grammar": [{"title": "Cấu trúc Consider V-ing", "rule": "consider + V-ing", "analysis": "Cân nhắc việc thực hiện một hành động có lợi."}]
                }
            ]
        }
    ]

    all_qs = []
    for t in talks:
        for q in t['qs']:
            all_qs.append({
                "id": q['id'],
                "part": 4,
                "partName": "Part 4: Short Talks",
                "audio": t['audio'],
                "image": t['image'],
                "passage": t['talk'],
                "passageVi": t['talkVi'],
                "questionText": q['text'],
                "questionTextVi": q['textVi'],
                "options": q['options'],
                "optionsVi": q['optionsVi'],
                "correctAnswer": q['correct'],
                "explanation": q['exp'],
                "vocabulary": q['vocab'],
                "collocations": q['collocations'],
                "grammar": q['grammar']
            })
    return all_qs

if __name__ == '__main__':
    qs = get_part4_questions()
    with open('data_part4.json', 'w', encoding='utf-8') as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print(f'Wrote all {len(qs)} questions of Part 4 to data_part4.json!')
