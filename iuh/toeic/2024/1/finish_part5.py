# Append Q121 to Q130 to build_part5.py and save full 30 questions
import json

with open('data_part5.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

Q121_130 = [
    {
        "id": 121,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "The meeting notes were ------- deleted, but Mr. Hahm was able to recreate them from memory.",
        "questionTextVi": "Các ghi chú cuộc họp đã vô tình bị xóa, nhưng ông Hahm đã có thể khôi phục lại chúng từ trí nhớ của mình.",
        "options": {
            "A": "accident",
            "B": "accidental",
            "C": "accidents",
            "D": "accidentally"
        },
        "optionsVi": {
            "A": "tai nạn, sự cố (danh từ số ít)",
            "B": "tình cờ, vô ý (tính từ)",
            "C": "các tai nạn (danh từ số nhiều)",
            "D": "một cách vô tình, do sơ suất (trạng từ)"
        },
        "correctAnswer": "D",
        "explanation": "Khoảng trống đứng giữa trợ động từ 'were' và quá khứ phân từ 'deleted' trong cấu trúc bị động 'were ------- deleted'. Vị trí này bắt buộc phải là một trạng từ (adverb) đuôi -ly để bổ nghĩa cho động từ bị xóa (bị xóa như thế nào? -> bị xóa một cách vô tình). Chọn (D) 'accidentally'.",
        "vocabulary": [
            { "word": "accidentally", "ipa": "/ˌæk.sɪˈden.təl.i/", "pos": "adv", "meaning": "vô tình, không cố ý, do sơ suất", "example": "I accidentally dropped my glass on the floor." },
            { "word": "recreate", "ipa": "/ˌriː.kriˈeɪt/", "pos": "v", "meaning": "tái tạo lại, khôi phục lại", "example": "The artist tried to recreate the historic scene." },
            { "word": "from memory", "ipa": "/frɒm ˈmem.ər.i/", "pos": "phr", "meaning": "từ trí nhớ, thuộc lòng", "example": "He recited the entire poem from memory." }
        ],
        "collocations": [
            { "phrase": "accidentally deleted", "meaning": "vô tình bị xóa mất dữ liệu" },
            { "phrase": "recreate from memory", "meaning": "khôi phục/vẽ lại từ trí nhớ" }
        ],
        "grammar": [
            {
                "title": "Trạng từ đứng giữa Be và Động từ phân từ (Adverb in Passive Voice)",
                "rule": "be + Adverb + V3/ed",
                "analysis": "Cấu trúc kinh điển trong Part 5: trạng từ xen giữa động từ to be và phân từ để chỉ mức độ hoặc tính chất của hành động bị động."
            }
        ]
    },
    {
        "id": 122,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "The current issue of Farming Scene magazine predicts that the price of corn will rise 5 percent over the ------- year.",
        "questionTextVi": "Số phát hành hiện tại của tạp chí Farming Scene dự đoán rằng giá ngô sẽ tăng 5% trong vòng một năm tới.",
        "options": {
            "A": "next",
            "B": "with",
            "C": "which",
            "D": "now"
        },
        "optionsVi": {
            "A": "tiếp theo, tới đây (tính từ thời gian)",
            "B": "với (giới từ)",
            "C": "cái mà (đại từ quan hệ)",
            "D": "bây giờ (trạng từ)"
        },
        "correctAnswer": "A",
        "explanation": "Cụm từ chỉ thời gian trong tương lai 'over the next year' (trong vòng một năm tới / năm tiếp theo). Động từ trong mệnh đề chia thì tương lai đơn 'will rise', do đó tính từ 'next' hoàn toàn hòa hợp về ngữ nghĩa và ngữ pháp với mạo từ 'the' và danh từ 'year'.",
        "vocabulary": [
            { "word": "predict", "ipa": "/prɪˈdɪkt/", "pos": "v", "meaning": "dự đoán, dự báo", "example": "Economists predict a modest increase in consumer spending." },
            { "word": "issue", "ipa": "/ˈɪʃ.uː/", "pos": "n", "meaning": "số báo/tạp chí phát hành, vấn đề", "example": "The special anniversary issue includes exclusive interviews." }
        ],
        "collocations": [
            { "phrase": "over the next year", "meaning": "trong vòng một năm tới" },
            { "phrase": "current issue", "meaning": "kỳ/số phát hành hiện tại của tạp chí" }
        ],
        "grammar": [
            {
                "title": "Cụm thời gian chỉ tương lai với 'Next'",
                "rule": "over / during the next + Period of Time (year / decade / few months)",
                "analysis": "'The next year' chỉ khoảng thời gian kéo dài 12 tháng kể từ thời điểm hiện tại trở đi."
            }
        ]
    },
    {
        "id": 123,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Anyone who still ------- to take the fire safety training should do so before the end of the month.",
        "questionTextVi": "Bất kỳ ai vẫn còn cần tham gia khóa đào tạo an toàn phòng cháy chữa cháy nên làm điều đó trước cuối tháng.",
        "options": {
            "A": "needing",
            "B": "needs",
            "C": "has needed",
            "D": "were needing"
        },
        "optionsVi": {
            "A": "cần (hiện tại phân từ)",
            "B": "cần (động từ số ít thì hiện tại đơn)",
            "C": "đã từng cần (hiện tại hoàn thành)",
            "D": "đã đang cần (quá khứ tiếp diễn số nhiều)"
        },
        "correctAnswer": "B",
        "explanation": "Đại từ bất định 'Anyone' (bất kỳ ai) luôn được quy ước là chủ ngữ số ít. Mệnh đề quan hệ 'who still ------- to take...' bổ nghĩa cho 'Anyone' thì động từ trong mệnh đề quan hệ phải hòa hợp với 'Anyone' ở dạng số ít. Trong thì hiện tại với trạng từ 'still' (vẫn còn), động từ chia ở dạng số ít thêm -s: 'needs'.",
        "vocabulary": [
            { "word": "safety training", "ipa": "/ˈseɪf.ti ˈtreɪ.nɪŋ/", "pos": "n", "meaning": "khóa huấn luyện an toàn lao động", "example": "Attending safety training is mandatory for laboratory workers." },
            { "word": "fire safety", "ipa": "/faɪər ˈseɪf.ti/", "pos": "n", "meaning": "an toàn phòng cháy chữa cháy", "example": "Compliance with fire safety regulations is strictly enforced." }
        ],
        "collocations": [
            { "phrase": "anyone who", "meaning": "bất kỳ người nào mà..." },
            { "phrase": "take training", "meaning": "tham gia khóa tập huấn / đào tạo" },
            { "phrase": "before the end of the month", "meaning": "trước khi tháng kết thúc" }
        ],
        "grammar": [
            {
                "title": "Sự hòa hợp giữa Đại từ bất định và Động từ mệnh đề quan hệ (Subject-Verb Agreement)",
                "rule": "Anyone / Everyone / Someone + who + Singular Verb (V-s/es)",
                "analysis": "'Anyone' là đại từ số ít không xác định, đòi hỏi động từ trong mệnh đề quan hệ 'who' phải chia theo ngôi thứ ba số ít (needs)."
            }
        ]
    },
    {
        "id": 124,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Emerging technologies have ------- begun to transform the shipping industry in ways that were once unimaginable.",
        "questionTextVi": "Các công nghệ mới nổi đã bắt đầu làm biến đổi ngành vận tải biển theo những cách mà trước đây từng là không thể tưởng tượng nổi.",
        "options": {
            "A": "already",
            "B": "exactly",
            "C": "hardly",
            "D": "closely"
        },
        "optionsVi": {
            "A": "đã, đã bắt đầu rồi (trạng từ nhấn mạnh)",
            "B": "chính xác",
            "C": "hầu như không (phủ định)",
            "D": "một cách chặt chẽ, sát sao"
        },
        "correctAnswer": "A",
        "explanation": "Khoảng trống đứng giữa 'have' và quá khứ phân từ 'begun' trong thì Hiện tại hoàn thành. Trạng từ 'already' (đã... rồi) thường đứng giữa trợ động từ have/has và V3/ed để nhấn mạnh rằng hành động biến đổi đó trên thực tế đã sớm bắt đầu diễn ra. Các từ khác không phù hợp ngữ cảnh.",
        "vocabulary": [
            { "word": "emerging", "ipa": "/ɪˈmɜː.dʒɪŋ/", "pos": "adj", "meaning": "mới nổi, đang phát triển nhanh", "example": "Investment in emerging markets carries both opportunity and risk." },
            { "word": "transform", "ipa": "/trænsˈfɔːm/", "pos": "v", "meaning": "biến đổi hoàn toàn, cách mạng hóa", "example": "Artificial intelligence will transform healthcare delivery." },
            { "word": "unimaginable", "ipa": "/ˌʌn.ɪˈmædʒ.ɪ.nə.bəl/", "pos": "adj", "meaning": "không thể tưởng tượng được, ngoài sức tưởng tượng", "example": "The disaster caused unimaginable disruption." }
        ],
        "collocations": [
            { "phrase": "emerging technologies", "meaning": "các công nghệ mới nổi / đột phá" },
            { "phrase": "shipping industry", "meaning": "ngành công nghiệp vận tải hàng hải" }
        ],
        "grammar": [
            {
                "title": "Vị trí của trạng từ Already trong thì Hiện tại hoàn thành",
                "rule": "have/has + already + V3/ed",
                "analysis": "'Already' dùng trong câu khẳng định đặt giữa trợ động từ 'have' và động từ chính 'begun' để nhấn mạnh tính hiện thực của sự việc."
            }
        ]
    },
    {
        "id": 125,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "The company handbook outlines the high ------- that employees are expected to meet every day.",
        "questionTextVi": "Cuốn sổ tay công ty vạch ra những tiêu chuẩn cao mà nhân viên được kỳ vọng sẽ đáp ứng mỗi ngày.",
        "options": {
            "A": "experts",
            "B": "accounts",
            "C": "recommendations",
            "D": "standards"
        },
        "optionsVi": {
            "A": "những chuyên gia",
            "B": "các tài khoản / khách hàng",
            "C": "các khuyến nghị",
            "D": "các tiêu chuẩn, chuẩn mực"
        },
        "correctAnswer": "D",
        "explanation": "Cụm động từ - danh từ cố định: 'meet standards' (đáp ứng tiêu chuẩn). Sổ tay nhân viên (handbook) là nơi quy định các chuẩn mực làm việc (standards) mà nhân sự cần tuân thủ và đáp ứng hàng ngày.",
        "vocabulary": [
            { "word": "handbook", "ipa": "/ˈhænd.bʊk/", "pos": "n", "meaning": "sổ tay hướng dẫn, cẩm nang", "example": "Consult the staff handbook for company leave policies." },
            { "word": "standard", "ipa": "/ˈstæn.dəd/", "pos": "n", "meaning": "tiêu chuẩn, thước đo chuẩn mực", "example": "The restaurant maintains rigorous standards of cleanliness." },
            { "word": "outline", "ipa": "/ˈaʊt.laɪn/", "pos": "v", "meaning": "vạch ra, phác thảo các điểm chính", "example": "The CEO outlined the five-year strategic roadmap." }
        ],
        "collocations": [
            { "phrase": "meet standards", "meaning": "đáp ứng / thỏa mãn các tiêu chuẩn đề ra" },
            { "phrase": "company handbook", "meaning": "sổ tay nội quy công ty" }
        ],
        "grammar": [
            {
                "title": "Collocation động từ Meet đi với Danh từ mục tiêu/tiêu chuẩn",
                "rule": "meet + standards / requirements / deadlines / expectations / demand",
                "analysis": "Động từ 'meet' khi đi với các danh từ mang tính chuẩn mực mang nghĩa đáp ứng, hoàn thành đúng quy định."
            }
        ]
    },
    {
        "id": 126,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Because ------- of the board members have scheduling conflicts, the board meeting will be moved to a date when all can attend.",
        "questionTextVi": "Bởi vì một số thành viên hội đồng quản trị bị trùng lịch trình, cuộc họp hội đồng sẽ được chuyển sang một ngày mà tất cả mọi người đều có thể tham dự.",
        "options": {
            "A": "any",
            "B": "everybody",
            "C": "those",
            "D": "some"
        },
        "optionsVi": {
            "A": "bất kỳ (thường dùng trong câu phủ định / nghi vấn)",
            "B": "mọi người (không dùng cấu trúc 'everybody of the...')",
            "C": "những người/vật đó",
            "D": "một số, một vài (đại từ định lượng đi với of the...)"
        },
        "correctAnswer": "D",
        "explanation": "Cấu trúc lượng từ 'some of the + danh từ số nhiều' (một vài trong số những...). Câu này nêu nguyên nhân một nhóm nhỏ thành viên bị bận ('have scheduling conflicts') nên cuộc họp hoãn để chuyển tới ngày tất cả ('all') có thể dự. 'Everybody' không đi với 'of the'; 'any' không dùng trong ngữ cảnh khẳng định chỉ một số người cụ thể.",
        "vocabulary": [
            { "word": "scheduling conflict", "ipa": "/ˈʃedʒ.uːl.ɪŋ ˈkɒn.flɪkt/", "pos": "n", "meaning": "sự trùng lịch trình, xung đột lịch hẹn", "example": "Due to a scheduling conflict, the director had to decline the invitation." },
            { "word": "board member", "ipa": "/bɔːd ˈmem.bər/", "pos": "n", "meaning": "thành viên hội đồng quản trị", "example": "Board members voted unanimously in favor of the merger." }
        ],
        "collocations": [
            { "phrase": "scheduling conflict", "meaning": "trùng lịch làm việc" },
            { "phrase": "some of the board members", "meaning": "một vài thành viên trong ban quản trị" }
        ],
        "grammar": [
            {
                "title": "Đại từ chỉ số lượng đi với 'of the' (Partitive Quantifiers)",
                "rule": "Some / Many / Most / All + of the + Plural Noun + Plural Verb",
                "analysis": "'Some of the board members' làm chủ ngữ số nhiều đi với động từ số nhiều 'have'."
            }
        ]
    },
    {
        "id": 127,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "The project ------- the collaboration of several teams across the company.",
        "questionTextVi": "Dự án đòi hỏi sự hợp tác của một vài đội nhóm trong toàn công ty.",
        "options": {
            "A": "passed",
            "B": "decided",
            "C": "required",
            "D": "performed"
        },
        "optionsVi": {
            "A": "đã vượt qua / thông qua",
            "B": "đã quyết định",
            "C": "đã đòi hỏi, yêu cầu (ngoại động từ)",
            "D": "đã thực hiện, biểu diễn"
        },
        "correctAnswer": "C",
        "explanation": "Câu hỏi từ vựng chọn động từ chính: 'The project (S) ------- the collaboration (O)'. Một dự án có quy mô lớn thì 'đòi hỏi / cần có' ('required') sự chung tay cộng tác của nhiều phòng ban. (A), (B), (D) không kết hợp phù hợp với tân ngữ 'the collaboration'.",
        "vocabulary": [
            { "word": "collaboration", "ipa": "/kəˌlæb.əˈreɪ.ʃən/", "pos": "n", "meaning": "sự cộng tác, hợp tác làm việc", "example": "The successful campaign was the result of cross-team collaboration." },
            { "word": "require", "ipa": "/rɪˈkwaɪər/", "pos": "v", "meaning": "đòi hỏi, yêu cầu bắt buộc", "example": "The position requires a bachelor's degree in engineering." }
        ],
        "collocations": [
            { "phrase": "require collaboration", "meaning": "đòi hỏi / yêu cầu sự hợp tác" },
            { "phrase": "across the company", "meaning": "trên toàn bộ công ty" }
        ],
        "grammar": [
            {
                "title": "Ngoại động từ với Tân ngữ danh từ trừu tượng",
                "rule": "Subject + require + Abstract Noun (collaboration / effort / attention)",
                "analysis": "'Require' là ngoại động từ chỉ nhu cầu thiết yếu của một dự án để có thể đi đến thành công."
            }
        ]
    },
    {
        "id": 128,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "We cannot send the store's coupon booklet to the printers until it ------- by Ms. Jeon.",
        "questionTextVi": "Chúng tôi không thể gửi tập sách phiếu giảm giá của cửa hàng đến nhà in cho đến khi nó được bà Jeon phê duyệt.",
        "options": {
            "A": "is approving",
            "B": "approves",
            "C": "has been approved",
            "D": "will be approved"
        },
        "optionsVi": {
            "A": "đang phê duyệt (chủ động)",
            "B": "phê duyệt (chủ động ngôi thứ 3)",
            "C": "đã được phê duyệt (bị động hiện tại hoàn thành)",
            "D": "sẽ được phê duyệt (tương lai đơn bị động)"
        },
        "correctAnswer": "C",
        "explanation": "Quy tắc hòa hợp thì trong mệnh đề trạng ngữ chỉ thời gian với 'until':\n1. Không được dùng thì tương lai (will) trong mệnh đề thời gian (loại D).\n2. Chủ ngữ 'it' (thay thế cho 'the store's coupon booklet') là vật nên phải chịu tác động ở thể bị động 'by Ms. Jeon' (loại A, B).\n3. Dạng bị động duy nhất là (C) 'has been approved' (hiện tại hoàn thành bị động diễn tả hành động hoàn tất trước khi có thể gửi đi in).",
        "vocabulary": [
            { "word": "booklet", "ipa": "/ˈbʊk.lət/", "pos": "n", "meaning": "tập sách nhỏ, cuốn cẩm nang mỏng", "example": "The tourist information booklet lists local attractions." },
            { "word": "printer", "ipa": "/ˈprɪn.tər/", "pos": "n", "meaning": "nhà in, xưởng in ấn", "example": "The catalog proofs were dispatched to the commercial printers." },
            { "word": "approve", "ipa": "/əˈpruːv/", "pos": "v", "meaning": "phê duyệt, chấp thuận", "example": "The budget proposal was officially approved by the board." }
        ],
        "collocations": [
            { "phrase": "coupon booklet", "meaning": "tập phiếu giảm giá" },
            { "phrase": "send to the printers", "meaning": "gửi bản thiết kế đến xưởng in" }
        ],
        "grammar": [
            {
                "title": "Mệnh đề trạng ngữ chỉ thời gian và thể Bị động",
                "rule": "Until + S + has been V3/ed (diễn tả hành động hoàn thành làm điều kiện tiên quyết)",
                "analysis": "Không bao giờ dùng 'will' sau các liên từ chỉ thời gian (when, until, as soon as, before, after)."
            }
        ]
    },
    {
        "id": 129,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "------- the closure of Verdigold Transport Services, we are looking for a new shipping company.",
        "questionTextVi": "Xét đến việc đóng cửa của Dịch vụ Vận tải Verdigold, chúng tôi đang tìm kiếm một công ty giao hàng mới.",
        "options": {
            "A": "In spite of",
            "B": "Just as",
            "C": "In light of",
            "D": "According to"
        },
        "optionsVi": {
            "A": "mặc dù (chỉ sự nhượng bộ / tương phản)",
            "B": "ngay khi, giống như là (liên từ nối mệnh đề)",
            "C": "xét đến, vì lý do (giới từ chỉ nguyên nhân)",
            "D": "theo như (nguồn thông tin)"
        },
        "correctAnswer": "C",
        "explanation": "Cụm giới từ 'In light of + Noun' mang nghĩa 'xét đến / căn cứ theo / bởi vì điều gì': 'In light of the closure...' (Xét đến việc công ty đóng cửa, chúng tôi phải tìm đối tác mới). Mối quan hệ giữa hai vế là nguyên nhân - kết quả. (A) 'In spite of' dùng cho mối quan hệ tương phản đối lập; (B) 'Just as' cần một mệnh đề; (D) 'According to' chỉ nguồn trích dẫn thông tin.",
        "vocabulary": [
            { "word": "closure", "ipa": "/ˈkləʊ.ʒər/", "pos": "n", "meaning": "sự đóng cửa vĩnh viễn / tạm thời", "example": "The factory closure led to significant regional job losses." },
            { "word": "in light of", "ipa": "/ɪn laɪt əv/", "pos": "prep phr", "meaning": "xét đến, vì xem xét lý do gì", "example": "In light of recent developments, we have updated our policy." }
        ],
        "collocations": [
            { "phrase": "in light of", "meaning": "xét về mặt / căn cứ vào tình hình..." },
            { "phrase": "shipping company", "meaning": "công ty vận chuyển giao nhận" }
        ],
        "grammar": [
            {
                "title": "Cụm giới từ chỉ nguyên nhân 'In light of'",
                "rule": "In light of + Noun Phrase, Clause",
                "analysis": "Đóng vai trò trạng ngữ nguyên nhân tương đương với 'Because of / Considering'."
            }
        ]
    },
    {
        "id": 130,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "The ------- information provided by Uniss Bank's brochure helps applicants understand the terms of their loans.",
        "questionTextVi": "Thông tin bổ sung được cung cấp bởi tờ rơi quảng cáo của Ngân hàng Uniss giúp người nộp đơn hiểu được các điều khoản trong khoản vay của họ.",
        "options": {
            "A": "arbitrary",
            "B": "supplemental",
            "C": "superfluous",
            "D": "potential"
        },
        "optionsVi": {
            "A": "tùy tiện, độc đoán",
            "B": "bổ sung, phụ trợ (tính từ)",
            "C": "thừa thãi, không cần thiết",
            "D": "tiềm năng, tiềm tàng"
        },
        "correctAnswer": "B",
        "explanation": "Câu hỏi từ vựng nâng cao: Vị trí đứng trước danh từ 'information' (thông tin). 'Supplemental information' (thông tin bổ sung / tài liệu phụ lục giải thích thêm) là thuật ngữ chính xác mô tả các thông tin chi tiết được đính kèm trong tờ gấp để giúp khách hàng hiểu rõ các điều khoản vay. (A) độc đoán; (C) thừa thãi vô ích; (D) tiềm năng không hợp nghĩa.",
        "vocabulary": [
            { "word": "supplemental", "ipa": "/ˌsʌp.lɪˈmen.təl/", "pos": "adj", "meaning": "bổ sung, kèm thêm", "example": "Students received supplemental reading materials." },
            { "word": "brochure", "ipa": "/ˈbrəʊ.ʃər/", "pos": "n", "meaning": "tờ rơi giới thiệu, sách quảng cáo nhỏ", "example": "Pick up a complimentary travel brochure at the desk." },
            { "word": "applicant", "ipa": "/ˈæp.lɪ.kənt/", "pos": "n", "meaning": "người nộp đơn (vay vốn, xin việc)", "example": "Loan applicants must submit proof of steady income." },
            { "word": "terms", "ipa": "/tɜːmz/", "pos": "n", "meaning": "các điều khoản, điều kiện hợp đồng", "example": "Please read the terms and conditions carefully." }
        ],
        "collocations": [
            { "phrase": "supplemental information", "meaning": "thông tin tài liệu bổ sung" },
            { "phrase": "terms of a loan", "meaning": "các điều khoản của khoản vay ngân hàng" }
        ],
        "grammar": [
            {
                "title": "Tính từ bổ nghĩa cho danh từ không đếm được",
                "rule": "Adjective + Uncountable Noun (information)",
                "analysis": "'Information' là danh từ không đếm được, kết hợp với tính từ 'supplemental' để tạo thành cụm danh từ chuyên ngành tài chính/ngân hàng."
            }
        ]
    }
]

questions.extend(Q121_130)
with open('data_part5.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f'Full Part 5 completed with {len(questions)} questions in data_part5.json!')
