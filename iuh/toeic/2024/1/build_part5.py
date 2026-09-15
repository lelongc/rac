# build_part5.py: Generate Part 5 Questions (101 - 130) with rich grammar & vocabulary
import json

PART5_QUESTIONS = [
    {
        "id": 101,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Former Sendai Company CEO Ken Nakata spoke about ------- career experiences.",
        "questionTextVi": "Cựu Giám đốc điều hành của Công ty Sendai, ông Ken Nakata, đã nói về những trải nghiệm nghề nghiệp của mình.",
        "options": {
            "A": "he",
            "B": "his",
            "C": "him",
            "D": "himself"
        },
        "optionsVi": {
            "A": "anh ấy (đại từ nhân xưng chủ ngữ)",
            "B": "của anh ấy (tính từ sở hữu)",
            "C": "anh ấy (đại từ nhân xưng tân ngữ)",
            "D": "chính bản thân anh ấy (đại từ phản thân)"
        },
        "correctAnswer": "B",
        "explanation": "Chỗ trống đứng trước cụm danh từ 'career experiences' (những trải nghiệm nghề nghiệp) nên cần một tính từ sở hữu (possessive adjective) đứng trước để bổ nghĩa và xác định quyền sở hữu. Do đó, phương án (B) 'his' là đáp án chính xác duy nhất. (A) 'he' là đại từ chủ ngữ; (C) 'him' là đại từ tân ngữ; (D) 'himself' là đại từ phản thân.",
        "vocabulary": [
            { "word": "former", "ipa": "/ˈfɔː.mər/", "pos": "adj", "meaning": "cựu, trước đây", "example": "The former president attended the opening ceremony." },
            { "word": "career", "ipa": "/kəˈrɪər/", "pos": "n", "meaning": "sự nghiệp, nghề nghiệp", "example": "She had a successful career in international finance." },
            { "word": "experience", "ipa": "/ɪkˈspɪə.ri.əns/", "pos": "n", "meaning": "kinh nghiệm, trải nghiệm", "example": "He shared valuable work experiences with the students." }
        ],
        "collocations": [
            { "phrase": "career experiences", "meaning": "trải nghiệm/kinh nghiệm nghề nghiệp" },
            { "phrase": "speak about something", "meaning": "phát biểu, chia sẻ về vấn đề gì" }
        ],
        "grammar": [
            {
                "title": "Tính từ sở hữu đứng trước danh từ (Possessive Adjectives)",
                "rule": "Possessive Adjective (his/her/their/my/our) + Noun",
                "analysis": "Khi khoảng trống nằm ngay trước một cụm danh từ hoặc danh từ chính và không có mạo từ (a/an/the), ta luôn chọn tính từ sở hữu để bổ nghĩa."
            }
        ]
    },
    {
        "id": 102,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Passengers who will be taking a ------- domestic flight should go to Terminal A.",
        "questionTextVi": "Những hành khách sẽ đi chuyến bay nội địa chuyển tiếp nên đi đến Nhà ga A.",
        "options": {
            "A": "connectivity",
            "B": "connects",
            "C": "connect",
            "D": "connecting"
        },
        "optionsVi": {
            "A": "khả năng kết nối (danh từ)",
            "B": "kết nối (động từ chia ngôi thứ 3 số ít)",
            "C": "kết nối (động từ nguyên mẫu)",
            "D": "chuyển tiếp / nối chuyến (phân từ làm tính từ)"
        },
        "correctAnswer": "D",
        "explanation": "Cụm danh từ 'a ------- domestic flight' đã có mạo từ 'a' và danh từ chính 'flight'. Vị trí khoảng trống cần một tính từ đứng trước để bổ nghĩa cho cụm 'domestic flight'. 'Connecting' là phân từ hiện tại đóng vai trò tính từ trong thuật ngữ hàng không quen thuộc 'connecting flight' (chuyến bay chuyển tiếp/nối chuyến).",
        "vocabulary": [
            { "word": "passenger", "ipa": "/ˈpæs.ən.dʒər/", "pos": "n", "meaning": "hành khách đi tàu/xe/máy bay", "example": "All passengers must fasten their seat belts." },
            { "word": "domestic", "ipa": "/dəˈmes.tɪk/", "pos": "adj", "meaning": "nội địa, trong nước", "example": "Domestic flights operate from the north terminal." },
            { "word": "terminal", "ipa": "/ˈtɜː.mɪ.nəl/", "pos": "n", "meaning": "nhà ga sân bay/bến tàu", "example": "Please proceed directly to Terminal 2." }
        ],
        "collocations": [
            { "phrase": "connecting flight", "meaning": "chuyến bay nối chuyến/chuyển tiếp" },
            { "phrase": "domestic flight", "meaning": "chuyến bay nội địa" }
        ],
        "grammar": [
            {
                "title": "Phân từ làm tính từ bổ nghĩa cho danh từ (Participle as Adjective)",
                "rule": "Mạo từ + (V-ing / V-ed) + Noun",
                "analysis": "'Connecting' đóng vai trò tính từ chỉ đặc tính chủ động của chuyến bay (chuyến bay mang tính kết nối hành trình tiếp theo)."
            }
        ]
    },
    {
        "id": 103,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Fresh and ------- apple-cider donuts are available at Oakcrest Orchard's retail shop for £6 per dozen.",
        "questionTextVi": "Những chiếc bánh donut táo tươi ngon có sẵn tại cửa hàng bán lẻ của Oakcrest Orchard với giá 6 bảng một tá.",
        "options": {
            "A": "eaten",
            "B": "open",
            "C": "tasty",
            "D": "free"
        },
        "optionsVi": {
            "A": "đã bị ăn",
            "B": "mở cửa",
            "C": "thơm ngon, đậm đà",
            "D": "miễn phí"
        },
        "correctAnswer": "C",
        "explanation": "Liên từ 'and' nối hai từ có cùng từ loại và tính chất bổ nghĩa cho cụm danh từ 'apple-cider donuts'. Trước 'and' là tính từ 'Fresh' (tươi mới), do đó vị trí sau cần một tính từ miêu tả chất lượng món ăn. 'Tasty' (ngon miệng, thơm ngon) là lựa chọn duy nhất mang nghĩa tự nhiên và hợp lý. (D) 'free' sai vì vế sau nêu rõ giá tiền 'for £6 per dozen'.",
        "vocabulary": [
            { "word": "tasty", "ipa": "/ˈteɪ.sti/", "pos": "adj", "meaning": "thơm ngon, vừa miệng", "example": "They served a selection of tasty desserts." },
            { "word": "orchard", "ipa": "/ˈɔː.tʃəd/", "pos": "n", "meaning": "vườn cây ăn quả", "example": "The family owns an apple orchard." },
            { "word": "retail shop", "ipa": "/ˈriː.teɪl ʃɒp/", "pos": "n", "meaning": "cửa hàng bán lẻ", "example": "The farm operates a retail shop selling fresh produce." },
            { "word": "dozen", "ipa": "/ˈdʌz.ən/", "pos": "n", "meaning": "một tá (12 cái)", "example": "A dozen eggs." }
        ],
        "collocations": [
            { "phrase": "retail shop", "meaning": "cửa hàng bán lẻ" },
            { "phrase": "per dozen", "meaning": "trên mỗi tá (12 sản phẩm)" }
        ],
        "grammar": [
            {
                "title": "Cấu trúc song hành với liên từ 'and' (Parallel Structure)",
                "rule": "Adj + and + Adj + Noun",
                "analysis": "'Fresh' (Adj) and 'tasty' (Adj) cùng bổ nghĩa cho danh từ chỉ thức ăn 'donuts'."
            }
        ]
    },
    {
        "id": 104,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Zahn Flooring has the widest selection of ------- in the United Kingdom.",
        "questionTextVi": "Công ty Lát sàn Zahn có bộ sưu tập gạch ốp lát đa dạng nhất tại Vương quốc Anh.",
        "options": {
            "A": "paints",
            "B": "tiles",
            "C": "furniture",
            "D": "curtains"
        },
        "optionsVi": {
            "A": "sơn",
            "B": "gạch lát / ốp sàn",
            "C": "nội thất đồ gỗ",
            "D": "rèm cửa"
        },
        "correctAnswer": "B",
        "explanation": "Câu hỏi từ vựng dựa vào ngữ cảnh: Tên công ty là 'Zahn Flooring' (kinh doanh giải pháp sàn nhà/lát nền), do đó sản phẩm trọng tâm tương ứng với lĩnh vực lát sàn là 'tiles' (gạch lát sàn/ốp lát). (A) sơn tường, (C) nội thất, (D) rèm cửa không phải sản phẩm cốt lõi của công ty sàn.",
        "vocabulary": [
            { "word": "tile", "ipa": "/taɪl/", "pos": "n", "meaning": "gạch ốp lát, đá lát sàn", "example": "Ceramic tiles are popular for bathroom floors." },
            { "word": "flooring", "ipa": "/ˈflɔː.rɪŋ/", "pos": "n", "meaning": "vật liệu làm sàn, sàn nhà", "example": "Specialists in wooden and vinyl flooring." },
            { "word": "selection", "ipa": "/sɪˈlek.ʃən/", "pos": "n", "meaning": "sự lựa chọn, bộ sưu tập đa dạng", "example": "The store offers a wide selection of books." }
        ],
        "collocations": [
            { "phrase": "wide selection of", "meaning": "nhiều sự lựa chọn đa dạng về..." },
            { "phrase": "ceramic tiles", "meaning": "gạch men lát nền" }
        ],
        "grammar": [
            {
                "title": "Cụm danh từ đo lường định lượng (Collective / Quantifying Noun Phrases)",
                "rule": "the widest selection of + Plural Noun",
                "analysis": "Cụm 'a/the selection of' luôn đi kèm danh từ số nhiều đếm được hoặc danh từ không đếm được để chỉ sự phong phú của mặt hàng."
            }
        ]
    },
    {
        "id": 105,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "One responsibility of the IT department is to ensure that the company is using ------- software.",
        "questionTextVi": "Một trong những trách nhiệm của phòng CNTT là đảm bảo công ty đang sử dụng phần mềm đã được cập nhật.",
        "options": {
            "A": "update",
            "B": "updating",
            "C": "updates",
            "D": "updated"
        },
        "optionsVi": {
            "A": "cập nhật (động từ nguyên mẫu / danh từ số ít)",
            "B": "đang cập nhật (hiện tại phân từ)",
            "C": "các bản cập nhật (danh từ số nhiều / động từ ngôi thứ 3)",
            "D": "đã được cập nhật mới nhất (quá khứ phân từ làm tính từ)"
        },
        "correctAnswer": "D",
        "explanation": "Khoảng trống đứng trước danh từ 'software' nên cần một tính từ mang nghĩa bị động: 'phần mềm đã được cập nhật phiên bản mới'. Dạng quá khứ phân từ 'updated' (past participle) được dùng làm tính từ chỉ trạng thái hoàn tất của phần mềm.",
        "vocabulary": [
            { "word": "updated", "ipa": "/ʌpˈdeɪ.tɪd/", "pos": "adj", "meaning": "được cập nhật mới nhất", "example": "Please install the updated version of the app." },
            { "word": "responsibility", "ipa": "/rɪˌspɒn.sɪˈbɪl.ə.ti/", "pos": "n", "meaning": "trách nhiệm, nhiệm vụ", "example": "It is your responsibility to back up all project files." },
            { "word": "ensure", "ipa": "/ɪnˈʃɔːr/", "pos": "v", "meaning": "đảm bảo, bảo đảm", "example": "Measures were taken to ensure passenger safety." }
        ],
        "collocations": [
            { "phrase": "ensure that", "meaning": "đảm bảo rằng" },
            { "phrase": "updated software", "meaning": "phần mềm đã cập nhật phiên bản mới" }
        ],
        "grammar": [
            {
                "title": "Quá khứ phân từ làm tính từ (Past Participle as Adjective)",
                "rule": "V-ed + Noun (mang nghĩa bị động / trạng thái hoàn tất)",
                "analysis": "'Updated software' mang ý nghĩa phần mềm đã được nâng cấp bởi đội ngũ kỹ thuật viên."
            }
        ]
    },
    {
        "id": 106,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "It is wise to check a company's dress code ------- visiting its head office.",
        "questionTextVi": "Thật khôn ngoan khi kiểm tra quy định về trang phục của một công ty trước khi đến thăm văn phòng trụ sở chính của họ.",
        "options": {
            "A": "so",
            "B": "how",
            "C": "like",
            "D": "before"
        },
        "optionsVi": {
            "A": "vì vậy (liên từ kết quả)",
            "B": "như thế nào (từ nghi vấn / liên từ)",
            "C": "giống như (giới từ so sánh)",
            "D": "trước khi (giới từ / liên từ chỉ thời gian)"
        },
        "correctAnswer": "D",
        "explanation": "Phía sau khoảng trống là danh động từ 'visiting its head office' (việc đến thăm trụ sở). 'Before' là giới từ chỉ thời gian có thể đi trực tiếp với danh động từ (V-ing) mang nghĩa 'trước khi làm việc gì'. Các từ còn lại không phù hợp về mặt ngữ pháp và ngữ nghĩa.",
        "vocabulary": [
            { "word": "dress code", "ipa": "/ˈdres ˌkəʊd/", "pos": "n", "meaning": "quy định về trang phục", "example": "The firm enforces a formal business dress code." },
            { "word": "head office", "ipa": "/ˌhed ˈɒf.ɪs/", "pos": "n", "meaning": "trụ sở chính, tổng hành dinh", "example": "The head office is situated in central London." },
            { "word": "wise", "ipa": "/waɪz/", "pos": "adj", "meaning": "khôn ngoan, sáng suốt", "example": "It is wise to invest in employee training." }
        ],
        "collocations": [
            { "phrase": "dress code", "meaning": "quy tắc ăn mặc nơi công sở" },
            { "phrase": "head office", "meaning": "trụ sở công ty chính" }
        ],
        "grammar": [
            {
                "title": "Giới từ chỉ thời gian đi với V-ing (Preposition of Time + Gerund)",
                "rule": "before / after / since + V-ing",
                "analysis": "Khi hai mệnh đề có cùng chủ ngữ ngầm định, mệnh đề trạng ngữ thời gian có thể rút gọn về dạng Giới từ + V-ing."
            }
        ]
    },
    {
        "id": 107,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Wexler Store's management team expects that employees will support any new hires -------.",
        "questionTextVi": "Ban quản lý Cửa hàng Wexler kỳ vọng rằng nhân viên sẽ nhiệt tình hỗ trợ bất kỳ nhân sự mới tuyển dụng nào.",
        "options": {
            "A": "enthusiastically",
            "B": "enthusiasm",
            "C": "enthusiastic",
            "D": "enthused"
        },
        "optionsVi": {
            "A": "một cách nhiệt tình (trạng từ)",
            "B": "sự nhiệt huyết, hăng hái (danh từ)",
            "C": "nhiệt tình, hăng hái (tính từ)",
            "D": "cảm thấy phấn khích (phân từ tính từ)"
        },
        "correctAnswer": "A",
        "explanation": "Mệnh đề 'employees (S) will support (V) any new hires (O)' đã đầy đủ thành phần chủ vị và tân ngữ. Vị trí cuối câu cần một trạng từ (adverb) để bổ nghĩa cho động từ 'support' (hỗ trợ như thế nào? -> hỗ trợ một cách nhiệt tình). Do đó, chọn trạng từ đuôi -ly (A) 'enthusiastically'.",
        "vocabulary": [
            { "word": "enthusiastically", "ipa": "/ɪnˌθjuː.ziˈæs.tɪ.kəl.i/", "pos": "adv", "meaning": "một cách nhiệt tình, đầy hăng hái", "example": "The audience applauded enthusiastically." },
            { "word": "new hire", "ipa": "/njuː ˈhaɪər/", "pos": "n", "meaning": "nhân viên mới được tuyển", "example": "Orientation is mandatory for all new hires." },
            { "word": "support", "ipa": "/səˈpɔːt/", "pos": "v, n", "meaning": "hỗ trợ, ủng hộ", "example": "Colleagues readily supported the initiative." }
        ],
        "collocations": [
            { "phrase": "support new hires", "meaning": "hướng dẫn, hỗ trợ nhân viên mới tuyển" },
            { "phrase": "management team", "meaning": "đội ngũ/ban quản lý" }
        ],
        "grammar": [
            {
                "title": "Vị trí của trạng từ thể cách (Adverb of Manner)",
                "rule": "S + V + O + Adverb",
                "analysis": "Trạng từ thể cách thường đứng ở cuối câu sau tân ngữ để mô tả cách thức tiến hành của hành động."
            }
        ]
    },
    {
        "id": 108,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Wheel alignments and brake system ------- are part of our vehicle service plan.",
        "questionTextVi": "Cân chỉnh góc đặt bánh xe và việc kiểm tra hệ thống phanh là một phần trong gói dịch vụ bảo dưỡng phương tiện của chúng tôi.",
        "options": {
            "A": "inspects",
            "B": "inspector",
            "C": "inspected",
            "D": "inspections"
        },
        "optionsVi": {
            "A": "kiểm tra (động từ ngôi thứ 3 số ít)",
            "B": "thanh tra viên / người kiểm tra (danh từ chỉ người số ít)",
            "C": "đã kiểm tra (quá khứ đơn / quá khứ phân từ)",
            "D": "những đợt kiểm tra (danh từ chỉ việc số nhiều)"
        },
        "correctAnswer": "D",
        "explanation": "Chủ ngữ là sự kết hợp song hành qua liên từ 'and': 'Wheel alignments' (danh từ số nhiều chỉ dịch vụ cân chỉnh bánh) và 'brake system -------'. Cần một danh từ số nhiều tương ứng để chỉ quy trình kỹ thuật. 'Inspections' (các đợt kiểm tra) hoàn thiện danh từ ghép 'brake system inspections' phù hợp với động từ số nhiều 'are'. (B) 'inspector' là danh từ chỉ người đếm được số ít, không thể đứng trơ trọi không có mạo từ.",
        "vocabulary": [
            { "word": "inspection", "ipa": "/ɪnˈspek.ʃən/", "pos": "n", "meaning": "sự kiểm tra, thanh tra kỹ thuật", "example": "The building passed the annual safety inspection." },
            { "word": "alignment", "ipa": "/əˈlaɪn.mənt/", "pos": "n", "meaning": "sự căn chỉnh, định vị thẳng hàng", "example": "Proper wheel alignment extends tire life." },
            { "word": "vehicle", "ipa": "/ˈvɪə.kəl/", "pos": "n", "meaning": "phương tiện giao thông, xe cộ", "example": "Electric vehicles are gaining popularity." }
        ],
        "collocations": [
            { "phrase": "brake system", "meaning": "hệ thống phanh xe" },
            { "phrase": "service plan", "meaning": "gói/kế hoạch bảo trì dịch vụ" }
        ],
        "grammar": [
            {
                "title": "Danh từ ghép song hành làm chủ ngữ (Compound Noun Subject)",
                "rule": "Noun + Noun -> Compound Noun; N1 (plural) and N2 (plural) + Plural Verb (are)",
                "analysis": "'Brake system inspections' là danh từ ghép chỉ hạng mục công việc trong gói bảo dưỡng xe hơi."
            }
        ]
    },
    {
        "id": 109,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Registration for the Marketing Coalition Conference is now open ------- September 30.",
        "questionTextVi": "Việc đăng ký tham dự Hội nghị Liên minh Tiếp thị hiện mở cho đến ngày 30 tháng 9.",
        "options": {
            "A": "until",
            "B": "into",
            "C": "yet",
            "D": "while"
        },
        "optionsVi": {
            "A": "cho đến khi (giới từ chỉ thời hạn)",
            "B": "vào trong (giới từ chuyển động)",
            "C": "chưa / tuy nhiên (phó từ / liên từ)",
            "D": "trong khi (liên từ chỉ thời gian song hành)"
        },
        "correctAnswer": "A",
        "explanation": "Khoảng trống đứng trước mốc thời gian ngày tháng cụ thể 'September 30'. Cụm 'open until + mốc thời gian' là cách diễn đạt chuẩn chỉ việc cổng đăng ký sẽ duy trì mở liên tục cho tới ngày đó. (B) 'into' chỉ hướng đi vào; (C) 'yet' không làm giới từ thời gian; (D) 'while' là liên từ cần đi kèm một mệnh đề (S + V).",
        "vocabulary": [
            { "word": "registration", "ipa": "/ˌredʒ.ɪˈstreɪ.ʃən/", "pos": "n", "meaning": "sự đăng ký", "example": "Early bird registration ends this Friday." },
            { "word": "coalition", "ipa": "/ˌkəʊ.əˈlɪʃ.ən/", "pos": "n", "meaning": "liên minh, sự hợp tác hiệp hội", "example": "A coalition of environmental groups was formed." }
        ],
        "collocations": [
            { "phrase": "open until", "meaning": "mở cửa / mở nhận hồ sơ cho đến ngày..." },
            { "phrase": "registration for", "meaning": "việc đăng ký tham dự cho sự kiện..." }
        ],
        "grammar": [
            {
                "title": "Giới từ chỉ thời hạn kéo dài 'Until'",
                "rule": "open / valid / last + until + Time Point",
                "analysis": "'Until' nhấn mạnh trạng thái (open) tiếp diễn liên tục không ngắt quãng cho đến thời điểm mốc."
            }
        ]
    },
    {
        "id": 110,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Growth in the home entertainment industry has been ------- this quarter.",
        "questionTextVi": "Sự tăng trưởng trong ngành công nghiệp giải trí tại gia đã bị hạn chế trong quý này.",
        "options": {
            "A": "separate",
            "B": "limited",
            "C": "willing",
            "D": "assorted"
        },
        "optionsVi": {
            "A": "riêng biệt, tách rời",
            "B": "bị hạn chế, có giới hạn",
            "C": "sẵn lòng, tự nguyện",
            "D": "hỗn hợp, gồm nhiều loại"
        },
        "correctAnswer": "B",
        "explanation": "Câu hỏi từ vựng chọn tính từ phù hợp đi sau 'has been' để bổ nghĩa cho chủ ngữ 'Growth' (sự tăng trưởng). 'Limited' (hạn chế, khiêm tốn) là tính từ mô tả mức độ tăng trưởng kinh tế quen thuộc trong báo cáo tài chính TOEIC ('growth has been limited' = tăng trưởng không đáng kể / chậm lại).",
        "vocabulary": [
            { "word": "growth", "ipa": "/ɡrəʊθ/", "pos": "n", "meaning": "sự phát triển, tăng trưởng", "example": "Economic growth rebounded in the second quarter." },
            { "word": "limited", "ipa": "/ˈlɪm.ɪ.tɪd/", "pos": "adj", "meaning": "bị hạn chế, có giới hạn", "example": "Due to limited space, seating is available on a first-come basis." },
            { "word": "entertainment", "ipa": "/ˌen.təˈteɪn.mənt/", "pos": "n", "meaning": "sự giải trí, ngành giải trí", "example": "The city offers diverse options for entertainment." }
        ],
        "collocations": [
            { "phrase": "limited growth", "meaning": "mức tăng trưởng hạn chế, tăng trưởng chậm" },
            { "phrase": "this quarter", "meaning": "trong quý này" }
        ],
        "grammar": [
            {
                "title": "Vị trí của tính từ vị ngữ (Predicative Adjective)",
                "rule": "S (noun) + have/has been + Adjective",
                "analysis": "Tính từ đứng sau động từ to be ở thì hiện tại hoàn thành đóng vai trò vị ngữ miêu tả đặc điểm tình hình của chủ ngữ."
            }
        ]
    }
]

# We will append Q111 - Q130 programmatically or with clean list
MORE_P5 = [
    {
        "id": 111,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Hawson Furniture will be making ------- on the east side of town on Thursday.",
        "questionTextVi": "Công ty Nội thất Hawson sẽ thực hiện các đợt giao hàng ở khu vực phía đông thị trấn vào thứ Năm.",
        "options": {
            "A": "deliveries",
            "B": "delivered",
            "C": "deliver",
            "D": "deliverable"
        },
        "optionsVi": {
            "A": "các chuyến giao hàng (danh từ số nhiều)",
            "B": "đã giao (quá khứ đơn / phân từ)",
            "C": "giao hàng (động từ nguyên mẫu)",
            "D": "có thể giao được (tính từ)"
        },
        "correctAnswer": "A",
        "explanation": "Cụm động từ 'make + noun': đi với 'deliveries' tạo thành collocation 'make deliveries' (thực hiện việc giao hàng). Vị trí sau 'making' cần một danh từ làm tân ngữ trực tiếp cho ngoại động từ này.",
        "vocabulary": [
            { "word": "delivery", "ipa": "/dɪˈlɪv.ər.i/", "pos": "n", "meaning": "sự giao hàng, chuyến hàng giao", "example": "We guarantee free delivery on orders over $50." },
            { "word": "furniture", "ipa": "/ˈfɜː.nɪ.tʃər/", "pos": "n", "meaning": "đồ nội thất (danh từ không đếm được)", "example": "The showroom displays handcrafted wooden furniture." }
        ],
        "collocations": [
            { "phrase": "make deliveries", "meaning": "thực hiện giao hàng đến địa chỉ người mua" },
            { "phrase": "east side of town", "meaning": "khu vực phía đông thị trấn" }
        ],
        "grammar": [
            {
                "title": "Collocation của động từ Make với Danh từ hành động",
                "rule": "make + deliveries / reservations / decisions / investments",
                "analysis": "Động từ 'make' kết hợp với danh từ để diễn đạt hành động cụ thể."
            }
        ]
    },
    {
        "id": 112,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "The Marlton City Council does not have the authority to ------- parking on city streets.",
        "questionTextVi": "Hội đồng Thành phố Marlton không có thẩm quyền cấm đỗ xe trên các tuyến phố trong thành phố.",
        "options": {
            "A": "drive",
            "B": "prohibit",
            "C": "bother",
            "D": "travel"
        },
        "optionsVi": {
            "A": "lái xe",
            "B": "cấm, ngăn cấm",
            "C": "làm phiền",
            "D": "đi lại, du lịch"
        },
        "correctAnswer": "B",
        "explanation": "Dựa vào nghĩa của ngữ cảnh: Cụm 'authority to + V' (thẩm quyền làm gì). Một cơ quan quản lý như 'City Council' chỉ có thể cân nhắc thẩm quyền ban hành lệnh cấm ('prohibit parking' = cấm đỗ xe) trên đường phố. Các từ 'drive', 'bother', 'travel' không mang nghĩa phù hợp với quyền hạn cơ quan chức năng.",
        "vocabulary": [
            { "word": "authority", "ipa": "/ɔːˈθɒr.ə.ti/", "pos": "n", "meaning": "thẩm quyền, quyền lực, cơ quan chức năng", "example": "Only the manager has the authority to sign contracts." },
            { "word": "prohibit", "ipa": "/prəˈhɪb.ɪt/", "pos": "v", "meaning": "cấm, nghiêm cấm bằng luật pháp", "example": "Smoking is strictly prohibited inside the facility." },
            { "word": "council", "ipa": "/ˈkaʊn.səl/", "pos": "n", "meaning": "hội đồng (thành phố, cơ quan)", "example": "The town council approved the new roadway plan." }
        ],
        "collocations": [
            { "phrase": "have the authority to do something", "meaning": "có thẩm quyền làm việc gì" },
            { "phrase": "prohibit parking", "meaning": "nghiêm cấm việc đỗ xe" }
        ],
        "grammar": [
            {
                "title": "Cấu trúc Danh từ + to-infinitive",
                "rule": "Noun (authority / ability / permission / right) + to V-bare",
                "analysis": "Động từ nguyên mẫu có 'to' đóng vai trò bổ ngữ làm rõ nội dung quyền hạn của danh từ đứng trước."
            }
        ]
    },
    {
        "id": 113,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Project Earth Group is ------- for ways to reduce transport-related greenhouse gas emissions.",
        "questionTextVi": "Tập đoàn Dự án Trái Đất đang tìm kiếm các cách thức nhằm cắt giảm lượng khí thải nhà kính liên quan đến giao thông.",
        "options": {
            "A": "looking",
            "B": "seeing",
            "C": "driving",
            "D": "leaning"
        },
        "optionsVi": {
            "A": "tìm kiếm (look for)",
            "B": "nhìn thấy",
            "C": "lái xe",
            "D": "dựa vào, nghiêng"
        },
        "correctAnswer": "A",
        "explanation": "Cụm động từ cố định 'look for' mang nghĩa 'tìm kiếm (giải pháp, cơ hội, đồ vật)'. Sau chỗ trống có giới từ 'for' ('is looking for ways to reduce...'). Các động từ khác không kết hợp với 'for' để mang nghĩa tìm kiếm.",
        "vocabulary": [
            { "word": "greenhouse gas", "ipa": "/ˈɡriːn.haʊs ˌɡæs/", "pos": "n", "meaning": "khí nhà kính gây biến đổi khí hậu", "example": "Initiatives to reduce greenhouse gas emissions." },
            { "word": "emission", "ipa": "/iˈmɪʃ.ən/", "pos": "n", "meaning": "sự phát thải, lượng khí thải", "example": "Automakers must meet stringent carbon emission caps." },
            { "word": "transport-related", "ipa": "/ˈtræn.spɔːt rɪˈleɪ.tɪd/", "pos": "adj", "meaning": "liên quan đến lĩnh vực vận tải", "example": "Transport-related pollution has dropped." }
        ],
        "collocations": [
            { "phrase": "look for ways to do something", "meaning": "tìm kiếm các giải pháp để thực hiện điều gì" },
            { "phrase": "greenhouse gas emissions", "meaning": "khí thải nhà kính" }
        ],
        "grammar": [
            {
                "title": "Cụm động từ (Phrasal Verb) với Look",
                "rule": "look for + Noun (tìm kiếm) vs look at (nhìn vào) vs look after (chăm sóc)",
                "analysis": "Đi kèm giới từ 'for' sau 'is looking' tạo thành thì hiện tại tiếp diễn diễn tả nỗ lực nghiên cứu tìm kiếm giải pháp hiện tại."
            }
        ]
    },
    {
        "id": 114,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Our skilled tailors are happy to design a custom-made suit that fits your style and budget -------.",
        "questionTextVi": "Những thợ may lành nghề của chúng tôi rất sẵn lòng thiết kế một bộ âu phục may đo vừa vặn hoàn hảo với phong cách và ngân sách của bạn.",
        "options": {
            "A": "perfect",
            "B": "perfects",
            "C": "perfectly",
            "D": "perfection"
        },
        "optionsVi": {
            "A": "hoàn hảo (tính từ)",
            "B": "hoàn thiện (động từ ngôi 3 số ít)",
            "C": "một cách hoàn hảo (trạng từ)",
            "D": "sự hoàn hảo (danh từ)"
        },
        "correctAnswer": "C",
        "explanation": "Mệnh đề quan hệ 'that fits your style and budget' đã có chủ ngữ 'that', động từ 'fits' và tân ngữ kép 'your style and budget'. Vị trí cuối mệnh đề cần một trạng từ (adverb) đuôi -ly để bổ nghĩa cho động từ 'fits' (vừa vặn như thế nào? -> vừa vặn một cách hoàn hảo). Chọn (C) 'perfectly'.",
        "vocabulary": [
            { "word": "tailor", "ipa": "/ˈteɪ.lər/", "pos": "n", "meaning": "thợ may trang phục", "example": "The tailor took his measurements for a bespoke tuxedo." },
            { "word": "custom-made", "ipa": "/ˌkʌs.təmˈmeɪd/", "pos": "adj", "meaning": "may đo theo yêu cầu, đặt làm riêng", "example": "She wore a custom-made evening gown." },
            { "word": "budget", "ipa": "/ˈbʌdʒ.ɪt/", "pos": "n", "meaning": "ngân sách chi tiêu", "example": "We completed the renovation strictly within budget." }
        ],
        "collocations": [
            { "phrase": "custom-made suit", "meaning": "bộ âu phục may đo riêng" },
            { "phrase": "fit perfectly", "meaning": "vừa vặn một cách hoàn hảo" }
        ],
        "grammar": [
            {
                "title": "Trạng từ bổ nghĩa cho động từ thường (Adverb modifying Verb)",
                "rule": "Verb + Object + Adverb of Manner (-ly)",
                "analysis": "'Perfect' là tính từ bổ nghĩa danh từ; khi bổ nghĩa cho động từ 'fits' bắt buộc phải chuyển sang dạng trạng từ 'perfectly'."
            }
        ]
    },
    {
        "id": 115,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Project manager Hannah Chung has proved to be very ------- with completing company projects.",
        "questionTextVi": "Giám đốc dự án Hannah Chung đã chứng tỏ mình rất hữu ích và đắc lực trong việc hoàn thành các dự án của công ty.",
        "options": {
            "A": "helpfulness",
            "B": "help",
            "C": "helpfully",
            "D": "helpful"
        },
        "optionsVi": {
            "A": "sự hữu ích (danh từ)",
            "B": "sự giúp đỡ / giúp đỡ (danh từ / động từ)",
            "C": "một cách hữu ích (trạng từ)",
            "D": "hữu ích, nhiệt tình giúp đỡ (tính từ)"
        },
        "correctAnswer": "D",
        "explanation": "Cấu trúc 'prove to be + Adj' (chứng tỏ là như thế nào). Sau trạng từ chỉ mức độ 'very' và động từ nối 'to be' ta cần một tính từ. Do đó, phương án (D) 'helpful' là đáp án chuẩn xác. (A) là danh từ; (C) là trạng từ.",
        "vocabulary": [
            { "word": "helpful", "ipa": "/ˈhelp.fəl/", "pos": "adj", "meaning": "hữu ích, đắc lực, hay giúp đỡ", "example": "The customer support staff were polite and very helpful." },
            { "word": "prove", "ipa": "/pruːv/", "pos": "v", "meaning": "chứng minh, chứng tỏ là", "example": "The new strategy proved to be highly effective." }
        ],
        "collocations": [
            { "phrase": "prove to be", "meaning": "chứng tỏ / tỏ ra là..." },
            { "phrase": "complete a project", "meaning": "hoàn thành một dự án" }
        ],
        "grammar": [
            {
                "title": "Cấu trúc với động từ nối Prove to be",
                "rule": "S + prove to be + (adv) + Adjective",
                "analysis": "Động từ 'prove to be' đóng vai trò linking verb, thành phần vị ngữ theo sau bắt buộc là tính từ (helpful)."
            }
        ]
    },
    {
        "id": 116,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Lehua Vacation Club members will receive double points ------- the month of August at participating hotels.",
        "questionTextVi": "Các hội viên Câu lạc bộ Nghỉ dưỡng Lehua sẽ nhận được điểm tích lũy nhân đôi trong suốt tháng 8 tại các khách sạn tham gia chương trình.",
        "options": {
            "A": "onto",
            "B": "above",
            "C": "during",
            "D": "between"
        },
        "optionsVi": {
            "A": "lên trên bề mặt",
            "B": "ở phía trên cao",
            "C": "trong suốt, trong khoảng thời gian",
            "D": "giữa (hai đối tượng)"
        },
        "correctAnswer": "C",
        "explanation": "Cụm 'the month of August' là một khoảng thời gian (khoảng một tháng). Giới từ 'during' đi kèm danh từ chỉ thời gian mang nghĩa 'trong suốt khoảng thời gian đó'. (A) 'onto' chỉ chuyển động lên trên; (B) 'above' chỉ vị trí phía trên; (D) 'between' đòi hỏi cấu trúc 'between A and B'.",
        "vocabulary": [
            { "word": "during", "ipa": "/ˈdʒʊə.rɪŋ/", "pos": "prep", "meaning": "trong suốt khoảng thời gian", "example": "Guests are invited to cocktails during the intermission." },
            { "word": "participating", "ipa": "/pɑːˈtɪs.ɪ.peɪ.tɪŋ/", "pos": "adj", "meaning": "tham gia, có tham dự", "example": "Discount coupons are valid at participating stores only." }
        ],
        "collocations": [
            { "phrase": "during the month of", "meaning": "trong suốt tháng..." },
            { "phrase": "participating hotels", "meaning": "các khách sạn tham gia chương trình ưu đãi" }
        ],
        "grammar": [
            {
                "title": "Giới từ chỉ thời gian 'During'",
                "rule": "during + Time Period (the summer / the month / the presentation)",
                "analysis": "Khác với 'for' đi với con số (for 3 weeks), 'during' đi với danh từ chỉ một thời kỳ hoặc sự kiện xác định."
            }
        ]
    },
    {
        "id": 117,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "The costumes were not received ------- enough to be used in the first dress rehearsal.",
        "questionTextVi": "Trang phục biểu diễn đã không được nhận đủ sớm để kịp dùng trong buổi tổng duyệt sân khấu đầu tiên.",
        "options": {
            "A": "far",
            "B": "very",
            "C": "almost",
            "D": "soon"
        },
        "optionsVi": {
            "A": "xa",
            "B": "rất",
            "C": "hầu như, gần như",
            "D": "sớm (trạng từ)"
        },
        "correctAnswer": "D",
        "explanation": "Cấu trúc với 'enough': '[Adj / Adv] + enough + to-V' (đủ... để làm gì). Động từ ở thể bị động 'were received' cần một trạng từ đứng trước 'enough' để chỉ thời điểm nhận được. 'Soon enough' nghĩa là 'đủ sớm để làm gì'. Các từ 'far', 'very', 'almost' không đứng trước 'enough' trong cấu trúc này.",
        "vocabulary": [
            { "word": "costume", "ipa": "/ˈkɒs.tʃuːm/", "pos": "n", "meaning": "trang phục hóa trang, biểu diễn", "example": "The actors wore elaborate period costumes." },
            { "word": "dress rehearsal", "ipa": "/ˌdres rɪˈhɜː.səl/", "pos": "n", "meaning": "buổi tổng duyệt trang phục trên sân khấu", "example": "The final dress rehearsal went without a hitch." },
            { "word": "soon", "ipa": "/suːn/", "pos": "adv", "meaning": "sớm, mau chóng", "example": "She realized her mistake soon enough to correct it." }
        ],
        "collocations": [
            { "phrase": "dress rehearsal", "meaning": "buổi tổng duyệt trang phục trước giờ diễn" },
            { "phrase": "soon enough to do something", "meaning": "đủ sớm để kịp làm điều gì" }
        ],
        "grammar": [
            {
                "title": "Cấu trúc Enough với Tính từ và Trạng từ",
                "rule": "Adjective / Adverb + enough + to-infinitive",
                "analysis": "Tính từ hoặc trạng từ luôn đứng TRƯỚC 'enough', trái ngược với danh từ đứng SAU 'enough' (enough money/time)."
            }
        ]
    },
    {
        "id": 118,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "As a former publicist for several renowned orchestras, Mr. Wu would excel in the role of event -------.",
        "questionTextVi": "Từng là chuyên viên truyền thông cho một số dàn nhạc nổi tiếng, ông Wu sẽ thể hiện xuất sắc trong vai trò người tổ chức sự kiện.",
        "options": {
            "A": "organized",
            "B": "organizer",
            "C": "organizes",
            "D": "organizational"
        },
        "optionsVi": {
            "A": "đã tổ chức (động từ)",
            "B": "người tổ chức (danh từ chỉ người)",
            "C": "tổ chức (động từ ngôi thứ 3)",
            "D": "thuộc về tổ chức (tính từ)"
        },
        "correctAnswer": "B",
        "explanation": "Cụm 'the role of event -------' (vai trò của...). Sau cụm 'the role of' nói về vị trí công việc của ông Wu, ta cần một danh từ chỉ người đảm nhận chức danh đó. Danh từ ghép 'event organizer' (người điều phối/tổ chức sự kiện) là cấu trúc chuẩn xác duy nhất.",
        "vocabulary": [
            { "word": "publicist", "ipa": "/ˈpʌb.lɪ.sɪst/", "pos": "n", "meaning": "chuyên viên quan hệ công chúng, nhà báo chí", "example": "The celebrity hired an experienced publicist." },
            { "word": "renowned", "ipa": "/rɪˈnaʊnd/", "pos": "adj", "meaning": "nổi tiếng, trứ danh", "example": "A renowned scientist was awarded the prize." },
            { "word": "excel", "ipa": "/ɪkˈsel/", "pos": "v", "meaning": "xuất sắc, vượt trội trong lĩnh vực nào", "example": "She excels in project planning and negotiation." },
            { "word": "organizer", "ipa": "/ˈɔː.ɡən.aɪ.zər/", "pos": "n", "meaning": "người tổ chức sự kiện", "example": "Event organizers coordinated the security protocol." }
        ],
        "collocations": [
            { "phrase": "in the role of", "meaning": "ở cương vị / trong vai trò là..." },
            { "phrase": "event organizer", "meaning": "nhà tổ chức sự kiện" }
        ],
        "grammar": [
            {
                "title": "Danh từ ghép chỉ nghề nghiệp / chức vụ (Compound Noun for Job Title)",
                "rule": "Noun (event) + Noun (organizer) = Job Title",
                "analysis": "Cấu trúc danh từ ghép kết hợp danh từ chỉ lĩnh vực (event) và danh từ chỉ người thực hiện (organizer)."
            }
        ]
    },
    {
        "id": 119,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "The northbound lane on Davis Street will be ------- closed because of the city's bridge reinforcement project.",
        "questionTextVi": "Làn đường đi về hướng bắc trên phố Davis sẽ tạm thời bị đóng do dự án gia cố cầu của thành phố.",
        "options": {
            "A": "temporarily",
            "B": "competitively",
            "C": "recently",
            "D": "collectively"
        },
        "optionsVi": {
            "A": "tạm thời, trong một thời gian ngắn",
            "B": "một cách có tính cạnh tranh",
            "C": "gần đây (thường dùng thì hoàn thành / quá khứ)",
            "D": "một cách tập thể, cùng nhau"
        },
        "correctAnswer": "A",
        "explanation": "Dựa vào ngữ cảnh thông báo giao thông: Làn đường đóng lại để thi công dự án sửa cầu nên việc đóng cửa chỉ mang tính chất ngắn hạn/tạm thời trong thời gian công trình diễn ra ('temporarily closed'). Cụm 'temporarily closed' là collocation cực kỳ thông dụng trong bài thi TOEIC.",
        "vocabulary": [
            { "word": "temporarily", "ipa": "/ˈtem.pər.ər.əl.i/", "pos": "adv", "meaning": "tạm thời, nhất thời", "example": "The website is temporarily unavailable due to scheduled maintenance." },
            { "word": "reinforcement", "ipa": "/ˌriː.ɪnˈfɔːs.mənt/", "pos": "n", "meaning": "sự gia cố, củng cố kết cấu", "example": "Bridge reinforcement work began early this month." },
            { "word": "lane", "ipa": "/leɪn/", "pos": "n", "meaning": "làn đường xe chạy", "example": "The right lane is reserved for public transit buses." }
        ],
        "collocations": [
            { "phrase": "temporarily closed", "meaning": "tạm thời đóng cửa / tạm thời cấm đường" },
            { "phrase": "bridge reinforcement", "meaning": "việc gia cố độ an toàn của cây cầu" }
        ],
        "grammar": [
            {
                "title": "Vị trí của trạng từ trong cấu trúc Bị động tương lai",
                "rule": "will be + Adverb + V3/ed",
                "analysis": "Trạng từ đứng giữa trợ động từ 'be' và quá khứ phân từ 'closed' để bổ nghĩa trực tiếp cho hành động bị động."
            }
        ]
    },
    {
        "id": 120,
        "part": 5,
        "partName": "Part 5: Incomplete Sentences",
        "questionText": "Airline representatives must handle a wide range of passenger issues, ------- missed connections to lost luggage.",
        "questionTextVi": "Các đại diện hãng hàng không phải xử lý rất nhiều vấn đề của hành khách, từ việc lỡ chuyến bay nối chuyến cho đến thất lạc hành lý.",
        "options": {
            "A": "from",
            "B": "under",
            "C": "on",
            "D": "against"
        },
        "optionsVi": {
            "A": "từ... (cấu trúc from... to...)",
            "B": "dưới",
            "C": "trên",
            "D": "chống lại"
        },
        "correctAnswer": "A",
        "explanation": "Cặp liên từ/giới từ chỉ phạm vi 'from X to Y' (từ cái này cho đến cái kia): 'from missed connections to lost luggage'. Phía sau đã có giới từ 'to', do đó vị trí đầu tiên bắt buộc phải là giới từ 'from'.",
        "vocabulary": [
            { "word": "representative", "ipa": "/ˌrep.rɪˈzen.tə.tɪv/", "pos": "n", "meaning": "đại diện, nhân viên phụ trách", "example": "A customer service representative will assist you." },
            { "word": "connection", "ipa": "/kəˈnek.ʃən/", "pos": "n", "meaning": "chuyến bay nối chuyến, sự liên kết", "example": "Flight delays caused passengers to miss their onward connection." },
            { "word": "luggage", "ipa": "/ˈlʌɡ.ɪdʒ/", "pos": "n", "meaning": "hành lý (danh từ không đếm được)", "example": "Report any lost luggage to the baggage claim counter." }
        ],
        "collocations": [
            { "phrase": "from X to Y", "meaning": "trải dài từ phạm trù X đến phạm trù Y" },
            { "phrase": "wide range of", "meaning": "rất nhiều, đa dạng các loại..." },
            { "phrase": "missed connection", "meaning": "lỡ chuyến bay chuyển tiếp" }
        ],
        "grammar": [
            {
                "title": "Cấu trúc giới từ tương quan chỉ phạm vi (Correlative Prepositional Phrase)",
                "rule": "from + N1 + to + N2",
                "analysis": "Dùng để liệt kê biên độ phong phú của các sự vụ từ trường hợp thông thường đến trường hợp phức tạp."
            }
        ]
    }
]

# Write Part 5 questions 101 to 120 and continue 121 to 130
with open('data_part5.json', 'w', encoding='utf-8') as f:
    json.dump(PART5_QUESTIONS + MORE_P5, f, ensure_ascii=False, indent=2)
print(f'Wrote data_part5.json with {len(PART5_QUESTIONS) + len(MORE_P5)} questions so far')
