# build_part3.py: Generate complete Part 3 questions (32 to 70)
import json

PART3_QUESTIONS = [
    # Conversation 1: 32 - 34
    {
        "id": 32,
        "part": 3,
        "partName": "Part 3: Conversations",
        "audio": "assets/audio/part3.mp3",
        "passage": "W-Am: Thank you so much for organizing the annual company picnic, Jingdao. Everybody seemed to enjoy it.\nM-Au: Well, we deserved it after working so hard this year.\nW-Am: I agree. The food was great, by the way. Especially the peach pie you made. Would you mind sharing the recipe? It was delicious.\nM-Au: I found the recipe online. I'll send you a link to the Web page. There's a really helpful video that walks you through all the steps. I recommend you watch it first.\nW-Am: All right, thanks.",
        "passageVi": "Nữ: Cảm ơn bạn rất nhiều vì đã tổ chức buổi dã ngoại thường niên của công ty nhé, Jingdao. Mọi người dường như đều rất thích nó.\nNam: À, chúng ta xứng đáng có được điều đó sau khi đã làm việc chăm chỉ trong năm nay mà.\nNữ: Tôi đồng ý. Tiện thể thì đồ ăn hôm đó rất tuyệt vời, đặc biệt là món bánh nướng đào bạn làm. Bạn có phiền chia sẻ công thức không? Nó thực sự rất ngon.\nNam: Tôi tìm thấy công thức trên mạng đấy. Tôi sẽ gửi cho bạn đường dẫn tới trang web. Có một video rất hữu ích hướng dẫn chi tiết từng bước. Tôi khuyên bạn nên xem video đó trước.\nNữ: Được rồi, cảm ơn bạn.",
        "questionText": "What event does the woman mention?",
        "questionTextVi": "Người phụ nữ nhắc đến sự kiện nào?",
        "options": {
            "A": "A job fair",
            "B": "A cooking class",
            "C": "A fund-raiser",
            "D": "A company picnic"
        },
        "optionsVi": {
            "A": "Một hội chợ việc làm",
            "B": "Một lớp học nấu ăn",
            "C": "Một buổi gây quỹ từ thiện",
            "D": "Một buổi dã ngoại công ty"
        },
        "correctAnswer": "D",
        "explanation": "Ngay đầu đoạn hội thoại, người phụ nữ nói: 'Thank you so much for organizing the annual company picnic, Jingdao' (Cảm ơn bạn rất nhiều vì đã tổ chức buổi dã ngoại thường niên của công ty). Do đó, sự kiện được nhắc tới là (D) A company picnic. Các phương án khác không được đề cập.",
        "vocabulary": [
            { "word": "organize", "ipa": "/ˈɔː.ɡən.aɪz/", "pos": "v", "meaning": "tổ chức, sắp xếp", "example": "She helped organize the annual conference." },
            { "word": "annual", "ipa": "/ˈæn.ju.əl/", "pos": "adj", "meaning": "hàng năm, thường niên", "example": "The company holds an annual picnic in July." },
            { "word": "deserve", "ipa": "/dɪˈzɜːv/", "pos": "v", "meaning": "xứng đáng", "example": "After months of hard work, they deserved a break." }
        ],
        "collocations": [
            { "phrase": "annual company picnic", "meaning": "buổi dã ngoại thường niên của công ty" },
            { "phrase": "work so hard", "meaning": "làm việc rất chăm chỉ" }
        ],
        "grammar": [
            {
                "title": "Cấu trúc cảm ơn vì việc gì (Thank someone for V-ing)",
                "rule": "Thank someone + for + V-ing / Noun Phrase",
                "analysis": "'Thank you so much for organizing...' dùng để bày tỏ sự tri ân đối với nỗ lực của Jingdao."
            }
        ]
    },
    {
        "id": 33,
        "part": 3,
        "partName": "Part 3: Conversations",
        "audio": "assets/audio/part3.mp3",
        "passage": "W-Am: Thank you so much for organizing the annual company picnic, Jingdao. Everybody seemed to enjoy it.\nM-Au: Well, we deserved it after working so hard this year.\nW-Am: I agree. The food was great, by the way. Especially the peach pie you made. Would you mind sharing the recipe? It was delicious.\nM-Au: I found the recipe online. I'll send you a link to the Web page. There's a really helpful video that walks you through all the steps. I recommend you watch it first.\nW-Am: All right, thanks.",
        "passageVi": "Nữ: Cảm ơn bạn rất nhiều vì đã tổ chức buổi dã ngoại thường niên của công ty nhé, Jingdao. Mọi người dường như đều rất thích nó.\nNam: À, chúng ta xứng đáng có được điều đó sau khi đã làm việc chăm chỉ trong năm nay mà.\nNữ: Tôi đồng ý. Tiện thể thì đồ ăn hôm đó rất tuyệt vời, đặc biệt là món bánh nướng đào bạn làm. Bạn có phiền chia sẻ công thức không? Nó thực sự rất ngon.\nNam: Tôi tìm thấy công thức trên mạng đấy. Tôi sẽ gửi cho bạn đường dẫn tới trang web. Có một video rất hữu ích hướng dẫn chi tiết từng bước. Tôi khuyên bạn nên xem video đó trước.\nNữ: Được rồi, cảm ơn bạn.",
        "questionText": "What does the woman ask for?",
        "questionTextVi": "Người phụ nữ yêu cầu điều gì?",
        "options": {
            "A": "A guest list",
            "B": "A dessert recipe",
            "C": "A business card",
            "D": "A promotional code"
        },
        "optionsVi": {
            "A": "Một danh sách khách mời",
            "B": "Công thức làm món tráng miệng",
            "C": "Một danh thiếp kinh doanh",
            "D": "Một mã khuyến mãi giảm giá"
        },
        "correctAnswer": "B",
        "explanation": "Người phụ nữ khen món bánh đào nướng (peach pie) và hỏi xin công thức: 'Especially the peach pie you made. Would you mind sharing the recipe?'. Món 'peach pie' được paraphrase thành 'dessert' (món tráng miệng). Do đó đáp án là (B) A dessert recipe.",
        "vocabulary": [
            { "word": "recipe", "ipa": "/ˈres.ɪ.pi/", "pos": "n", "meaning": "công thức nấu ăn", "example": "Follow the recipe step by step." },
            { "word": "dessert", "ipa": "/dɪˈzɜːt/", "pos": "n", "meaning": "món tráng miệng", "example": "We ordered chocolate cake for dessert." },
            { "word": "delicious", "ipa": "/dɪˈlɪʃ.əs/", "pos": "adj", "meaning": "ngon miệng, tuyệt hảo", "example": "The homemade soup was absolutely delicious." }
        ],
        "collocations": [
            { "phrase": "share a recipe", "meaning": "chia sẻ công thức nấu ăn / làm bánh" },
            { "phrase": "peach pie", "meaning": "bánh nướng nhân đào" }
        ],
        "grammar": [
            {
                "title": "Cấu trúc đề nghị lịch sự với Would you mind",
                "rule": "Would you mind + V-ing...?",
                "analysis": "'Would you mind sharing the recipe?' là cấu trúc nhờ vả trang trọng trong giao tiếp tiếng Anh."
            }
        ]
    },
    {
        "id": 34,
        "part": 3,
        "partName": "Part 3: Conversations",
        "audio": "assets/audio/part3.mp3",
        "passage": "W-Am: Thank you so much for organizing the annual company picnic, Jingdao. Everybody seemed to enjoy it.\nM-Au: Well, we deserved it after working so hard this year.\nW-Am: I agree. The food was great, by the way. Especially the peach pie you made. Would you mind sharing the recipe? It was delicious.\nM-Au: I found the recipe online. I'll send you a link to the Web page. There's a really helpful video that walks you through all the steps. I recommend you watch it first.\nW-Am: All right, thanks.",
        "passageVi": "Nữ: Cảm ơn bạn rất nhiều vì đã tổ chức buổi dã ngoại thường niên của công ty nhé, Jingdao. Mọi người dường như đều rất thích nó.\nNam: À, chúng ta xứng đáng có được điều đó sau khi đã làm việc chăm chỉ trong năm nay mà.\nNữ: Tôi đồng ý. Tiện thể thì đồ ăn hôm đó rất tuyệt vời, đặc biệt là món bánh nướng đào bạn làm. Bạn có phiền chia sẻ công thức không? Nó thực sự rất ngon.\nNam: Tôi tìm thấy công thức trên mạng đấy. Tôi sẽ gửi cho bạn đường dẫn tới trang web. Có một video rất hữu ích hướng dẫn chi tiết từng bước. Tôi khuyên bạn nên xem video đó trước.\nNữ: Được rồi, cảm ơn bạn.",
        "questionText": "What does the man recommend doing?",
        "questionTextVi": "Người đàn ông khuyên nên làm gì?",
        "options": {
            "A": "Returning some merchandise",
            "B": "Watching a video",
            "C": "Creating an account",
            "D": "Reading a review"
        },
        "optionsVi": {
            "A": "Trả lại một số hàng hóa",
            "B": "Xem một video hướng dẫn",
            "C": "Tạo một tài khoản mới",
            "D": "Đọc một bài đánh giá"
        },
        "correctAnswer": "B",
        "explanation": "Người đàn ông nói: 'There’s a really helpful video that walks you through all the steps. I recommend you watch it first' (Có một video rất hữu ích hướng dẫn từng bước. Tôi khuyên bạn nên xem nó trước). Do đó chọn (B) Watching a video.",
        "vocabulary": [
            { "word": "recommend", "ipa": "/ˌrek.əˈmend/", "pos": "v", "meaning": "khuyên, giới thiệu, đề xuất", "example": "I recommend booking your flights well in advance." },
            { "word": "walk through", "ipa": "/wɔːk θruː/", "pos": "phr v", "meaning": "hướng dẫn chi tiết từng bước một", "example": "The technician walked us through the setup procedure." }
        ],
        "collocations": [
            { "phrase": "walk someone through all the steps", "meaning": "hướng dẫn ai tường tận từng công đoạn" },
            { "phrase": "watch a video", "meaning": "xem video" }
        ],
        "grammar": [
            {
                "title": "Cấu trúc đưa ra lời khuyên với Recommend",
                "rule": "recommend (that) someone (should) V-bare / recommend + V-ing",
                "analysis": "'I recommend you watch it first' sử dụng cấu trúc giả định thức (subjunctive mood) lược bỏ 'should'."
            }
        ]
    },

    # Conversation 2: 35 - 37
    {
        "id": 35,
        "part": 3,
        "partName": "Part 3: Conversations",
        "audio": "assets/audio/part3.mp3",
        "passage": "M-Cn: I’d like to finish calculating the company’s expense reports for the month. Have you finished reviewing the travel reimbursement forms?\nW-Am: Almost. I'm checking the final batch now. But I noticed that Mr. Rossi didn't include his hotel receipt with his submission.\nM-Cn: That's a problem because the accounting guidelines strictly require all original receipts for lodging.\nW-Am: I'll call Mr. Rossi right now to see if he can email us a scanned copy.",
        "passageVi": "Nam: Tôi muốn hoàn tất việc tính toán báo cáo chi phí của công ty trong tháng này. Bạn đã xem xong các biểu mẫu hoàn trả chi phí đi lại chưa?\nNữ: Gần xong rồi. Tôi đang kiểm tra đợt cuối cùng. Nhưng tôi nhận thấy ông Rossi không gửi kèm biên lai khách sạn trong hồ sơ của mình.\nNam: Đó là một vấn đề đấy, vì các quy định kế toán bắt buộc nghiêm ngặt phải có đầy đủ hóa đơn gốc đối với chi phí lưu trú.\nNữ: Tôi sẽ gọi điện cho ông Rossi ngay bây giờ để xem ông ấy có thể gửi cho chúng ta bản scan qua email được không.",
        "questionText": "What department do the speakers most likely work in?",
        "questionTextVi": "Những người nói có nhiều khả năng làm việc ở bộ phận nào nhất?",
        "options": {
            "A": "Accounting",
            "B": "Research and development",
            "C": "Maintenance",
            "D": "Marketing"
        },
        "optionsVi": {
            "A": "Phòng Kế toán",
            "B": "Phòng Nghiên cứu và Phát triển",
            "C": "Bộ phận Bảo trì",
            "D": "Phòng Tiếp thị"
        },
        "correctAnswer": "A",
        "explanation": "Người đàn ông nói về việc tính toán báo cáo chi phí ('calculating the company’s expense reports'), xem xét biểu mẫu hoàn trả chi phí công tác ('travel reimbursement forms') và nhắc tới quy định kế toán ('accounting guidelines strictly require...'). Tất cả các manh mối này chỉ ra họ làm việc ở (A) Accounting.",
        "vocabulary": [
            { "word": "reimbursement", "ipa": "/ˌriː.ɪmˈbɜːs.mənt/", "pos": "n", "meaning": "sự hoàn tiền, thanh toán lại chi phí", "example": "Submit receipts to claim reimbursement for meals." },
            { "word": "expense report", "ipa": "/ɪkˈspens rɪˌpɔːt/", "pos": "n", "meaning": "báo cáo chi tiêu công tác", "example": "Employees must submit an expense report after each business trip." }
        ],
        "collocations": [
            { "phrase": "expense report", "meaning": "báo cáo chi tiêu chi phí" },
            { "phrase": "travel reimbursement", "meaning": "hoàn trả chi phí đi lại công tác" }
        ],
        "grammar": [
            {
                "title": "Suy luận ngữ cảnh nghề nghiệp (Context Inference)",
                "rule": "expense reports + reimbursement + accounting guidelines -> Accounting Department",
                "analysis": "Dạng câu hỏi 'Where do the speakers work?' dựa vào hệ thống từ vựng chuyên ngành trong bài hội thoại."
            }
        ]
    },
    {
        "id": 36,
        "part": 3,
        "partName": "Part 3: Conversations",
        "audio": "assets/audio/part3.mp3",
        "passage": "M-Cn: I’d like to finish calculating the company’s expense reports for the month. Have you finished reviewing the travel reimbursement forms?\nW-Am: Almost. I'm checking the final batch now. But I noticed that Mr. Rossi didn't include his hotel receipt with his submission.\nM-Cn: That's a problem because the accounting guidelines strictly require all original receipts for lodging.\nW-Am: I'll call Mr. Rossi right now to see if he can email us a scanned copy.",
        "passageVi": "Nam: Tôi muốn hoàn tất việc tính toán báo cáo chi phí của công ty trong tháng này. Bạn đã xem xong các biểu mẫu hoàn trả chi phí đi lại chưa?\nNữ: Gần xong rồi. Tôi đang kiểm tra đợt cuối cùng. Nhưng tôi nhận thấy ông Rossi không gửi kèm biên lai khách sạn trong hồ sơ của mình.\nNam: Đó là một vấn đề đấy, vì các quy định kế toán bắt buộc nghiêm ngặt phải có đầy đủ hóa đơn gốc đối với chi phí lưu trú.\nNữ: Tôi sẽ gọi điện cho ông Rossi ngay bây giờ để xem ông ấy có thể gửi cho chúng ta bản scan qua email được không.",
        "questionText": "What problem does the woman mention?",
        "questionTextVi": "Người phụ nữ đề cập đến vấn đề gì?",
        "options": {
            "A": "A report has not been submitted.",
            "B": "An invoice is not accurate.",
            "C": "A receipt is missing.",
            "D": "An order has not been delivered."
        },
        "optionsVi": {
            "A": "Một bản báo cáo chưa được nộp.",
            "B": "Một hóa đơn không chính xác.",
            "C": "Một biên lai bị thiếu.",
            "D": "Một đơn hàng chưa được giao."
        },
        "correctAnswer": "C",
        "explanation": "Người phụ nữ nói rõ: 'Mr. Rossi didn't include his hotel receipt with his submission' (Ông Rossi không gửi kèm hóa đơn khách sạn trong hồ sơ). Nghĩa là biên lai đang bị thiếu -> (C) A receipt is missing.",
        "vocabulary": [
            { "word": "lodging", "ipa": "/ˈlɒdʒ.ɪŋ/", "pos": "n", "meaning": "nơi ăn chốn ở, chi phí lưu trú", "example": "The company pays for travel, meals, and lodging." },
            { "word": "receipt", "ipa": "/rɪˈsiːt/", "pos": "n", "meaning": "biên lai, hóa đơn thu tiền", "example": "Keep your receipt in case you need to return the item." }
        ],
        "collocations": [
            { "phrase": "hotel receipt", "meaning": "hóa đơn tiền phòng khách sạn" },
            { "phrase": "strictly require", "meaning": "yêu cầu một cách nghiêm ngặt" }
        ],
        "grammar": [
            {
                "title": "Kỹ thuật Paraphrase danh từ phủ định",
                "rule": "didn't include receipt = a receipt is missing",
                "analysis": "Hành động phủ định 'không đính kèm' được diễn đạt lại bằng tính từ trạng thái 'bị thất lạc/thiếu'."
            }
        ]
    },
    {
        "id": 37,
        "part": 3,
        "partName": "Part 3: Conversations",
        "audio": "assets/audio/part3.mp3",
        "passage": "M-Cn: I’d like to finish calculating the company’s expense reports for the month. Have you finished reviewing the travel reimbursement forms?\nW-Am: Almost. I'm checking the final batch now. But I noticed that Mr. Rossi didn't include his hotel receipt with his submission.\nM-Cn: That's a problem because the accounting guidelines strictly require all original receipts for lodging.\nW-Am: I'll call Mr. Rossi right now to see if he can email us a scanned copy.",
        "passageVi": "Nam: Tôi muốn hoàn tất việc tính toán báo cáo chi phí của công ty trong tháng này. Bạn đã xem xong các biểu mẫu hoàn trả chi phí đi lại chưa?\nNữ: Gần xong rồi. Tôi đang kiểm tra đợt cuối cùng. Nhưng tôi nhận thấy ông Rossi không gửi kèm biên lai khách sạn trong hồ sơ của mình.\nNam: Đó là một vấn đề đấy, vì các quy định kế toán bắt buộc nghiêm ngặt phải có đầy đủ hóa đơn gốc đối với chi phí lưu trú.\nNữ: Tôi sẽ gọi điện cho ông Rossi ngay bây giờ để xem ông ấy có thể gửi cho chúng ta bản scan qua email được không.",
        "questionText": "What does the woman say she will do?",
        "questionTextVi": "Người phụ nữ nói cô ấy sẽ làm gì?",
        "options": {
            "A": "Attend a meeting",
            "B": "Contact a coworker",
            "C": "Print some documents",
            "D": "Reschedule an appointment"
        },
        "optionsVi": {
            "A": "Tham dự một cuộc họp",
            "B": "Liên hệ với một đồng nghiệp",
            "C": "In một số tài liệu",
            "D": "Đổi lại lịch hẹn"
        },
        "correctAnswer": "B",
        "explanation": "Cuối hội thoại, người phụ nữ quyết định: 'I'll call Mr. Rossi right now to see if he can email us a scanned copy'. Hành động gọi điện cho ông Rossi (một nhân viên trong công ty) tương đương với (B) Contact a coworker.",
        "vocabulary": [
            { "word": "coworker", "ipa": "/ˈkəʊˌwɜː.kər/", "pos": "n", "meaning": "đồng nghiệp cùng công ty", "example": "She gets along very well with her coworkers." },
            { "word": "scanned copy", "ipa": "/skænd ˈkɒp.i/", "pos": "n", "meaning": "bản quét scan tài liệu", "example": "Please email a scanned copy of your passport." }
        ],
        "collocations": [
            { "phrase": "contact a coworker", "meaning": "liên lạc với đồng nghiệp" },
            { "phrase": "scanned copy", "meaning": "bản sao quét điện tử" }
        ],
        "grammar": [
            {
                "title": "Thì Tương lai đơn đưa ra quyết định tức thì (Instant Decision with Will)",
                "rule": "S + will + V-bare (I'll call Mr. Rossi right now)",
                "analysis": "Dùng 'will' để diễn tả quyết định hành động nảy sinh ngay tại thời điểm nói để giải quyết sự cố phát sinh."
            }
        ]
    }
]

with open('data_part3.json', 'w', encoding='utf-8') as f:
    json.dump(PART3_QUESTIONS, f, ensure_ascii=False, indent=2)
print(f'Wrote data_part3.json with {len(PART3_QUESTIONS)} questions so far')
