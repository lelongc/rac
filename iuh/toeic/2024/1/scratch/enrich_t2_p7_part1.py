# scratch/enrich_t2_p7_part1.py: Part 7 Single Passages Enrichment (Q147-Q175)
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

p7_p1_enrichment = {
    # Q147-Q148: Savan Business Center Webinar
    "147": {
        "exp": "Trong đoạn đầu của thư mời, tổ chức nêu rõ: 'For over twelve years, the Savan Business Center has supported emerging entrepreneurs and small business owners throughout the metro region' (Trong hơn 12 năm qua, Trung tâm Kinh doanh Savan đã hỗ trợ các doanh nhân mới khởi nghiệp và các chủ doanh nghiệp nhỏ trên toàn khu vực đô thị). Chi tiết này chứng minh trung tâm hợp tác và hỗ trợ các doanh nghiệp nhỏ -> Chọn (A) It works with small businesses. Các phương án (B) cung cấp tài trợ vốn, (C) tổ chức hội chợ việc làm, (D) chuyển trụ sở chính đều không được đề cập.",
        "vocab": [
            {"word": "entrepreneur", "ipa": "/ˌɒn.trə.prəˈnɜːr/", "pos": "n", "meaning": "doanh nhân, người khởi nghiệp kinh doanh", "example": "Young entrepreneurs pitched creative tech solutions to venture capitalists."},
            {"word": "emerging", "ipa": "/ɪˈmɜː.dʒɪŋ/", "pos": "adj", "meaning": "mới nổi, đang trên đà phát triển", "example": "Government grants assist emerging small businesses with research costs."}
        ],
        "collocations": [
            {"phrase": "small business owner", "meaning": "chủ doanh nghiệp nhỏ"},
            {"phrase": "business center", "meaning": "trung tâm hỗ trợ kinh doanh"}
        ],
        "grammar": [
            {"title": "Kỹ năng tìm kiếm chi tiết trực tiếp (Scanning for Factual Details)", "rule": "Identify key entity and scan for verbs of action", "analysis": "Tìm từ khóa 'Savan Business Center' ở phần giới thiệu đầu văn bản để xác định sứ mệnh và đối tượng phục vụ của tổ chức."}
        ]
    },
    "148": {
        "exp": "Về nội dung hội thảo trực tuyến, thư mời viết: 'This interactive webinar, titled Focus Your Social Media Marketing, delivers actionable guidance on crafting engaging promotional videos, reels, and digital advertising copy' (Hội thảo trực tuyến tương tác này với tựa đề Tập trung Tiếp thị Mạng xã hội, cung cấp các hướng dẫn thiết thực về cách sáng tạo video quảng bá lôi cuốn, video ngắn và bài viết quảng cáo kỹ thuật số). Điều này đồng nghĩa với việc hội thảo đưa ra lời khuyên về cách tạo nội dung quảng bá -> Chọn (B) It features advice on creating promotional content.",
        "vocab": [
            {"word": "promotional", "ipa": "/prəˈməʊ.ʃən.əl/", "pos": "adj", "meaning": "thuộc về quảng bá, khuyến mãi", "example": "Marketing teams distributed promotional brochures at the annual trade fair."},
            {"word": "webinar", "ipa": "/ˈweb.ɪ.nɑːr/", "pos": "n", "meaning": "hội thảo trực tuyến qua internet", "example": "Over five hundred participants registered for the leadership webinar."}
        ],
        "collocations": [
            {"phrase": "promotional content", "meaning": "nội dung quảng bá, bài viết tiếp thị"},
            {"phrase": "actionable guidance", "meaning": "hướng dẫn có tính thực tiễn cao, có thể áp dụng ngay"}
        ],
        "grammar": [
            {"title": "Cấu trúc danh từ ghép trong quảng cáo", "rule": "Noun adjunct + Head noun", "analysis": "'social media marketing' và 'promotional content' là các cụm danh từ kinh tế rất phổ biến trong TOEIC."}
        ]
    },

    # Q149-Q150: Dine Out Darville
    "149": {
        "exp": "Trong thông báo có viết: 'Dine Out Darville, our city's premier seven-day culinary celebration, returns next week from Monday, October 12 through Sunday, October 18' (Dine Out Darville, ngày hội ẩm thực kéo dài 7 ngày hàng đầu của thành phố chúng ta, sẽ trở lại vào tuần tới từ thứ Hai ngày 12/10 đến hết Chủ Nhật ngày 18/10). Cụm 'seven-day culinary celebration' cho thấy sự kiện kéo dài trong đúng một tuần -> Chọn (A) It lasts for one week. Các phương án (B) yêu cầu đặt bàn trước, (C) chỉ dành cho hội viên, (D) tổ chức tại công viên đều sai.",
        "vocab": [
            {"word": "culinary", "ipa": "/ˈkʌl.ɪ.nər.i/", "pos": "adj", "meaning": "thuộc về ẩm thực, nghề bếp núc", "example": "The metropolitan magazine featured an insightful guide to the city's culinary scene."},
            {"word": "celebration", "ipa": "/ˌsel.əˈbreɪ.ʃən/", "pos": "n", "meaning": "ngày hội, lễ kỷ niệm tôn vinh", "example": "The civic parade was part of the town's founding celebration."}
        ],
        "collocations": [
            {"phrase": "culinary celebration", "meaning": "ngày hội ẩm thực, lễ hội ẩm thực"},
            {"phrase": "participating restaurant", "meaning": "nhà hàng tham gia sự kiện"}
        ],
        "grammar": [
            {"title": "Tính từ ghép chỉ thời lượng: Số đếm - danh từ số ít (seven-day)", "rule": "Number - singular noun hyphenated", "analysis": "'seven-day celebration' tương đương với 'lasts for one week' (kéo dài một tuần)."}
        ]
    },
    "150": {
        "exp": "Bài viết liệt kê chi tiết các món trong thực đơn giảm giá: 'Participating bistros offer fixed-price three-course meals that include your choice of appetizer, entrée, and dessert. Please note that beverages and gratuity are charged separately' (Các quán ăn tham gia phục vụ thực đơn 3 món giá cố định bao gồm món khai vị, món chính và món tráng miệng tùy chọn. Xin lưu ý rằng đồ uống và tiền boa phục vụ được tính tiền riêng). Do đó, đồ uống (a beverage) KHÔNG nằm trong suất ăn giảm giá -> Chọn (D) A beverage.",
        "vocab": [
            {"word": "beverage", "ipa": "/ˈbev.ər.ɪdʒ/", "pos": "n", "meaning": "đồ uống, thức uống các loại", "example": "Cold beverages and bottled mineral water were served during the afternoon break."},
            {"word": "gratuity", "ipa": "/ɡrəˈtʃuː.ə.ti/", "pos": "n", "meaning": "tiền boa, tiền thưởng cho phục vụ", "example": "An eighteen percent service gratuity is added for parties of six or more."},
            {"word": "entrée", "ipa": "/ˈɒn.treɪ/", "pos": "n", "meaning": "món ăn chính trong bữa ăn", "example": "Guests selected grilled salmon as their preferred dinner entrée."}
        ],
        "collocations": [
            {"phrase": "three-course meal", "meaning": "bữa ăn gồm ba món (khai vị, món chính, tráng miệng)"},
            {"phrase": "charge separately", "meaning": "tính tiền riêng, không gộp chung"}
        ],
        "grammar": [
            {"title": "Dạng câu hỏi phủ định chi tiết (Negative Fact: NOT question)", "rule": "Eliminate 3 stated items to find the unincluded one", "analysis": "Loại trừ 3 thành phần được bao gồm trong set ăn (appetizer, entrée, dessert), còn lại 'beverage' là món bị tính tiền riêng."}
        ]
    },

    # Q151-Q152: Rainsy LLC article
    "151": {
        "exp": "Đoạn mở đầu bài báo giới thiệu: 'Rainsy LLC, a premier consumer data storage and behavioral analytics firm, announced the expansion of its corporate footprint...' (Rainsy LLC, một công ty hàng đầu về lưu trữ dữ liệu người tiêu dùng và phân tích hành vi, đã công bố việc mở rộng quy mô doanh nghiệp...). Công ty này thực hiện việc lưu trữ và phân tích thông tin người tiêu dùng -> Chọn (A) It stores and analyzes consumer information.",
        "vocab": [
            {"word": "analytics", "ipa": "/ˌæn.əˈlɪt.ɪks/", "pos": "n", "meaning": "ngành phân tích dữ liệu chuyên sâu", "example": "Predictive customer analytics empower companies to forecast quarterly consumer spending."},
            {"word": "footprint", "ipa": "/ˈfʊt.prɪnt/", "pos": "n", "meaning": "dấu ấn, quy mô hiện diện thương mại", "example": "The supermarket giant enlarged its retail footprint by acquiring ten stores."}
        ],
        "collocations": [
            {"phrase": "consumer information", "meaning": "thông tin người tiêu dùng"},
            {"phrase": "data storage", "meaning": "lưu trữ dữ liệu"}
        ],
        "grammar": [
            {"title": "Đồng vị ngữ (Appositive) giải thích tính chất doanh nghiệp", "rule": "Company Name, a [Noun Phrase], announced...", "analysis": "Cụm danh từ đứng giữa hai dấu phẩy 'a premier consumer data storage and behavioral analytics firm' đóng vai trò định nghĩa lĩnh vực hoạt động của công ty."}
        ]
    },
    "152": {
        "exp": "Bài báo đề cập đến nhân sự tại cơ sở Dade: 'Under the relocation plan, approximately 50 percent of the company's 400-member workforce will transfer to the new Dade regional facility' (Theo kế hoạch tái bố trí, khoảng 50% trong tổng số 400 nhân viên của công ty sẽ chuyển về làm việc tại cơ sở khu vực Dade mới). 50% lực lượng lao động tương đương với khoảng một nửa số nhân viên -> Chọn (C) About half of Rainsy's employees.",
        "vocab": [
            {"word": "workforce", "ipa": "/ˈwɜːk.fɔːs/", "pos": "n", "meaning": "lực lượng lao động, toàn bộ nhân viên", "example": "The manufacturing plant employs a skilled industrial workforce of five hundred."},
            {"word": "relocate", "ipa": "/ˌriː.ləʊˈkeɪt/", "pos": "v", "meaning": "chuyển địa điểm làm việc/sinh sống", "example": "The corporate headquarters will relocate to Dallas by early next year."}
        ],
        "collocations": [
            {"phrase": "about half of", "meaning": "khoảng một nửa số lượng"},
            {"phrase": "relocation plan", "meaning": "kế hoạch chuyển địa điểm công tác"}
        ],
        "grammar": [
            {"title": "Quy đổi tỷ lệ phần trăm sang phân số", "rule": "50 percent = half", "analysis": "Trong bài thi TOEIC, '50 percent' thường được paraphrase thành 'half' (một nửa)."}
        ]
    },

    # Q153-Q154: Michael Liu & Jana Bhat text chain
    "153": {
        "exp": "Trong chuỗi tin nhắn, Michael nhắn: 'I'm at Biz Plus right now. Did you need the pastel sky-blue cardstock for the promotional flyers?' và Jana xác nhận: 'Yes, exactly that soft blue shade' (Đúng vậy, chính xác là tông màu xanh da trời nhạt đó). Như vậy loại giấy mà anh Liu đang tìm mua có màu xanh da trời nhạt -> Chọn (A) It is light blue.",
        "vocab": [
            {"word": "cardstock", "ipa": "/ˈkɑːd.stɒk/", "pos": "n", "meaning": "giấy bìa cứng, giấy in thiệp", "example": "Invitations were professionally printed on heavy textured cardstock."},
            {"word": "pastel", "ipa": "/ˈpæs.təl/", "pos": "adj, n", "meaning": "màu phấn nhạt, dịu nhẹ", "example": "The spring catalogue features garments in soothing pastel tones."}
        ],
        "collocations": [
            {"phrase": "light blue", "meaning": "màu xanh da trời nhạt, xanh lơ"},
            {"phrase": "promotional flyer", "meaning": "tờ rơi quảng cáo"}
        ],
        "grammar": [
            {"title": "Từ đồng nghĩa miêu tả màu sắc (pastel sky-blue = light blue)", "rule": "Descriptive color equivalence", "analysis": "'pastel sky-blue' (xanh da trời nhạt) được diễn đạt ngắn gọn bằng 'light blue'."}
        ]
    },
    "154": {
        "exp": "Michael nhắn báo giá: 'Biz Plus wants $28 per ream here, which is nearly double what we normally pay online' (Biz Plus ở đây đòi 28 đô một ram giấy, gần gấp đôi giá chúng ta thường mua trên mạng). Jana trả lời ngay lúc 9:49 A.M.: 'OK, forget it. I'll just place a rush order on our usual website' (Thôi, bỏ qua đi. Tôi sẽ đặt đơn giao gấp trên trang web quen thuộc của chúng ta). Câu nói này có nghĩa là cô Bhat khuyên anh Liu không nên mua giấy ở cửa hàng Biz Plus nữa -> Chọn (B) She thinks Mr. Liu should not purchase paper at Biz Plus.",
        "vocab": [
            {"word": "ream", "ipa": "/riːm/", "pos": "n", "meaning": "ram giấy (đơn vị 500 tờ giấy)", "example": "The office manager ordered twenty reams of standard white photocopy paper."},
            {"word": "supplier", "ipa": "/səˈplaɪ.ər/", "pos": "n", "meaning": "nhà cung ứng, đơn vị cung cấp hàng", "example": "We negotiated lower rates with our domestic paper suppliers."}
        ],
        "collocations": [
            {"phrase": "place an order online", "meaning": "đặt hàng trực tuyến qua mạng"},
            {"phrase": "forget it", "meaning": "thôi bỏ đi, không cần làm nữa"}
        ],
        "grammar": [
            {"title": "Cụm thành ngữ khẩu ngữ trong tin nhắn (Idiomatic Chat Language)", "rule": "'forget it' expresses cancellation of intent", "analysis": "Khi nghe mức giá quá đắt, thành ngữ 'forget it' được dùng để hủy bỏ ý định mua hàng tại chỗ."}
        ]
    },

    # Q155-Q157: Neil Croft letter to Queensland Libraries
    "155": {
        "exp": "Trong đoạn mở đầu bức thư, bà Otney viết: 'Thank you for your letter dated 10 May regarding the possibility of hosting community financial literacy sessions at Queensland Libraries...' (Cảm ơn bức thư đề ngày 10/5 của ông liên quan đến khả năng tổ chức các buổi đào tạo kiến thức tài chính cộng đồng tại các Thư viện Queensland...). Bức thư được viết nhằm hồi đáp câu hỏi thăm dò từ ông Croft -> Chọn (D) To reply to a question from Mr. Croft.",
        "vocab": [
            {"word": "literacy", "ipa": "/ˈlɪt.ər.ə.si/", "pos": "n", "meaning": "kiến thức hiểu biết, năng lực chuyên môn", "example": "The foundation promotes basic digital and financial literacy among youth."},
            {"word": "inquire", "ipa": "/ɪnˈkwaɪər/", "pos": "v", "meaning": "thắc mắc, hỏi thăm thông tin", "example": "Prospective partners inquired about the conference registration schedule."}
        ],
        "collocations": [
            {"phrase": "reply to a question", "meaning": "trả lời/phản hồi một câu hỏi"},
            {"phrase": "financial literacy", "meaning": "kiến thức tài chính cơ bản"}
        ],
        "grammar": [
            {"title": "Công thức mở đầu thư thương mại hồi đáp", "rule": "Thank you for your letter regarding...", "analysis": "Mẫu câu quy chuẩn báo hiệu mục đích viết thư là phản hồi thông tin mà đối tác đã hỏi trước đó."}
        ]
    },
    "156": {
        "exp": "Bà Otney đưa ra yêu cầu cụ thể: 'Could you please provide the specific addresses and seating capacities of the branch library locations where you envision these workshops being held?' (Ông có thể vui lòng cung cấp địa chỉ cụ thể và sức chứa chỗ ngồi của các địa điểm thư viện chi nhánh nơi ông dự kiến các hội thảo này sẽ diễn ra không?). Yêu cầu là địa chỉ vị trí của các thư viện -> Chọn (C) The locations of some libraries.",
        "vocab": [
            {"word": "capacity", "ipa": "/kəˈpæs.ə.ti/", "pos": "n", "meaning": "sức chứa phòng, công suất", "example": "The auditorium has a maximum seating capacity of three hundred guests."},
            {"word": "envision", "ipa": "/ɪnˈvɪʒ.ən/", "pos": "v", "meaning": "hình dung, dự kiến trong tương lai", "example": "Planners envision transforming the former warehouse into an art gallery."}
        ],
        "collocations": [
            {"phrase": "branch library", "meaning": "thư viện chi nhánh"},
            {"phrase": "provide locations", "meaning": "cung cấp các địa điểm"}
        ],
        "grammar": [
            {"title": "Từ đồng nghĩa address = location", "rule": "Lexical substitution in comprehension", "analysis": "Yêu cầu 'specific addresses of the branch libraries' tương đương với 'the locations of some libraries'."}
        ]
    },
    "157": {
        "exp": "Xét vị trí chèn câu 'This is something I would be happy to arrange' (Đây là điều tôi rất sẵn lòng sắp xếp): Trước vị trí [2], bà Otney vừa nhắc đến đề xuất từ ông Croft về việc điều chỉnh chủ đề hội thảo cho phù hợp với người cao tuổi ('You mentioned adjusting curriculum content to suit senior citizens'). Đại từ 'This' liên kết trực tiếp với việc điều chỉnh nội dung đó -> Chọn (B) [2].",
        "vocab": [
            {"word": "arrange", "ipa": "/əˈreɪndʒ/", "pos": "v", "meaning": "thu xếp, sắp đặt công việc", "example": "The administrative assistant arranged flight accommodations for the delegates."},
            {"word": "curriculum", "ipa": "/kəˈrɪk.jə.ləm/", "pos": "n", "meaning": "giáo trình, chương trình giảng dạy", "example": "The business institute revised its accounting curriculum to include modern software."}
        ],
        "collocations": [
            {"phrase": "happy to arrange", "meaning": "rất vui lòng được sắp xếp, thu xếp"},
            {"phrase": "senior citizen", "meaning": "người cao tuổi, người hưu trí"}
        ],
        "grammar": [
            {"title": "Kỹ thuật giải câu hỏi chèn câu (Sentence Insertion)", "rule": "Identify reference pronouns (This, That, Such)", "analysis": "Đại từ chỉ định 'This' bắt buộc phải quy chiếu về một hành động hoặc đề xuất cụ thể vừa xuất hiện ở câu liền kề phía trước."}
        ]
    },

    # Q158-Q160: Claro Vision advertisement
    "158": {
        "exp": "Tiêu đề và nội dung quảng cáo nêu rõ: 'Claro Vision Spring Frame Sale: Enjoy 30% off all designer eyeglass frames during our two-week promotional event ending April 30' (Khuyến mãi gọng kính mùa xuân của Claro Vision: Giảm ngay 30% cho tất cả gọng kính thiết kế trong sự kiện khuyến mãi 2 tuần kết thúc vào 30/4). Mẩu quảng cáo được tạo ra nhằm quảng bá một đợt giảm giá có thời hạn -> Chọn (D) To promote a temporary price discount.",
        "vocab": [
            {"word": "temporary", "ipa": "/ˈtem.pər.ər.i/", "pos": "adj", "meaning": "tạm thời, có thời hạn ngắn", "example": "The firm hired temporary clerical staff during the audit period."},
            {"word": "designer", "ipa": "/dɪˈzaɪ.nər/", "pos": "adj", "meaning": "hàng thiết kế cao cấp, có thương hiệu", "example": "The optical boutique displays designer sunglasses from Italy."}
        ],
        "collocations": [
            {"phrase": "price discount", "meaning": "chiết khấu giảm giá"},
            {"phrase": "promotional event", "meaning": "sự kiện khuyến mãi quảng bá"}
        ],
        "grammar": [
            {"title": "Paraphrase thời gian có hạn (two-week event ending April 30 = temporary)", "rule": "Specific time constraint signifies temporary status", "analysis": "Đợt khuyến mãi 2 tuần kết thúc vào ngày cụ thể là đợt giảm giá tạm thời (temporary price discount)."}
        ]
    },
    "159": {
        "exp": "Quảng cáo khẳng định dịch vụ tại cửa hàng: 'Every purchase includes complimentary custom fitting and adjustment services performed in-store' (Mỗi lần mua hàng đều bao gồm dịch vụ nắn chỉnh và lắp kính theo yêu cầu miễn phí tại cửa hàng). Từ 'complimentary' đồng nghĩa với 'at no cost' (miễn phí) -> Chọn (D) They provide eyeglass fittings at no cost.",
        "vocab": [
            {"word": "complimentary", "ipa": "/ˌkɒm.plɪˈmen.tər.i/", "pos": "adj", "meaning": "miễn phí, tặng kèm dịch vụ", "example": "Hotel guests receive complimentary continental breakfast and high-speed Wi-Fi."},
            {"word": "fitting", "ipa": "/ˈfɪt.ɪŋ/", "pos": "n", "meaning": "việc nắn chỉnh cho vừa vặn, thử đồ", "example": "The tailor offers a final fitting before delivering the formal evening gown."}
        ],
        "collocations": [
            {"phrase": "at no cost", "meaning": "miễn phí, không tốn tiền"},
            {"phrase": "custom fitting", "meaning": "nắn chỉnh vừa vặn theo kích thước cá nhân"}
        ],
        "grammar": [
            {"title": "Cặp từ đồng nghĩa kinh điển trong TOEIC: complimentary = at no cost", "rule": "Synonym match for free services", "analysis": "'complimentary' xuất hiện trong văn bản đọc luôn được diễn giải thành 'at no cost' hoặc 'free of charge' trong đáp án."}
        ]
    },
    "160": {
        "exp": "Về dịch vụ đo mắt, mẩu quảng cáo cam kết: 'Comprehensive vision examinations are conducted by our licensed optometrists using state-of-the-art diagnostic imaging' (Các cuộc kiểm tra thị lực toàn diện được thực hiện bởi các bác sĩ chuyên khoa mắt có chứng chỉ hành nghề của chúng tôi bằng máy móc chẩn đoán tối tân). 'licensed optometrists' chính là các chuyên gia có chứng chỉ chuyên môn -> Chọn (B) They are performed by a certified professional.",
        "vocab": [
            {"word": "optometrist", "ipa": "/ɒpˈtɒm.ə.trɪst/", "pos": "n", "meaning": "bác sĩ đo thị lực, chuyên gia nhãn khoa", "example": "Schedule regular annual examinations with your optometrist to monitor ocular health."},
            {"word": "licensed", "ipa": "/ˈlaɪ.sənst/", "pos": "adj", "meaning": "có giấy phép hành nghề, được cấp phép", "example": "The clinic only hires fully licensed medical practitioners."}
        ],
        "collocations": [
            {"phrase": "certified professional", "meaning": "chuyên gia có chứng chỉ/chứng nhận hành nghề"},
            {"phrase": "vision checkup", "meaning": "kiểm tra thị lực, khám mắt"}
        ],
        "grammar": [
            {"title": "Paraphrase chức danh nghề nghiệp (licensed optometrist = certified professional)", "rule": "General professional category replaces specific job title", "analysis": "'licensed optometrist' được quy về danh từ chung 'certified professional'."}
        ]
    },

    # Q161-Q163: Rossery Building lease letter
    "161": {
        "exp": "Bà Tan mở đầu thư gửi khách thuê: 'Dear Ms. Balakrishnan, We are pleased to provide you with the formal lease agreement details and terms for Suite 4B at Rossery Towers...' (Kính gửi cô Balakrishnan, Chúng tôi rất vui mừng cung cấp cho cô các điều khoản và chi tiết hợp đồng thuê nhà chính thức cho Căn hộ 4B tại Tòa nhà Rossery...). Mục đích bức thư là cung cấp thông tin về hợp đồng thuê nhà -> Chọn (C) To provide information about a lease agreement.",
        "vocab": [
            {"word": "lease", "ipa": "/liːs/", "pos": "n, v", "meaning": "hợp đồng thuê nhà/đất; cho thuê dài hạn", "example": "Tenants signed a twelve-month residential lease for the downtown loft."},
            {"word": "tenant", "ipa": "/ˈten.ənt/", "pos": "n", "meaning": "khách thuê nhà, người thuê phòng", "example": "Prospective tenants submitted credit verification forms."}
        ],
        "collocations": [
            {"phrase": "lease agreement", "meaning": "hợp đồng thuê nhà, thỏa thuận cho thuê"},
            {"phrase": "residential lease", "meaning": "hợp đồng thuê nhà ở"}
        ],
        "grammar": [
            {"title": "Cấu trúc cung cấp thông tin 'provide someone with something'", "rule": "provide + person + with + information/documents", "analysis": "'provide you with the formal lease agreement details' nêu rõ hành động và mục đích của thư."}
        ]
    },
    "162": {
        "exp": "Thư quy định các khoản phí hàng tháng: 'While monthly rent encompasses water and heating utilities, residents requiring a designated vehicle stall must pay a monthly parking space charge of $80' (Trong khi tiền thuê hàng tháng đã bao gồm tiền nước và hệ thống sưởi, những cư dân có nhu cầu về chỗ để xe riêng phải trả một khoản phí đỗ xe hàng tháng là 80 đô la). Khoản phí phải trả hàng tháng là chỗ đỗ xe -> Chọn (D) A parking space.",
        "vocab": [
            {"word": "designated", "ipa": "/ˈdez.ɪɡ.neɪ.tɪd/", "pos": "adj", "meaning": "được chỉ định, dành riêng", "example": "Vehicles parked outside designated visitor stalls will be towed."},
            {"word": "utilities", "ipa": "/juːˈtɪl.ə.tiz/", "pos": "n", "meaning": "các dịch vụ tiện ích (điện, nước, sưởi)", "example": "Monthly rental rates include all municipal utilities except electricity."}
        ],
        "collocations": [
            {"phrase": "parking space", "meaning": "chỗ đỗ xe, vị trí đậu xe"},
            {"phrase": "monthly charge", "meaning": "khoản phí thu hàng tháng"}
        ],
        "grammar": [
            {"title": "Liên từ chỉ sự tương phản 'While'", "rule": "While clause (included items), main clause (separate charges)", "analysis": "Phân biệt những mục đã được miễn phí/gộp sẵn với mục phải đóng tiền riêng hàng tháng."}
        ]
    },
    "163": {
        "exp": "Cuối thư, người ký tên ghi rõ chức danh: 'Sincerely, Andrea Tan, On-Site Property Manager, Rossery Building Corporation' (Trân trọng, Andrea Tan, Quản lý Bất động sản tại chỗ, Tập đoàn Xây dựng Rossery). Chức danh 'Property Manager' xác nhận bà Tan là người quản lý bất động sản/quản lý tòa nhà -> Chọn (B) A property manager.",
        "vocab": [
            {"word": "property", "ipa": "/ˈprɒp.ə.ti/", "pos": "n", "meaning": "bất động sản, tài sản nhà đất", "example": "Real estate companies manage multiple commercial properties downtown."},
            {"word": "manager", "ipa": "/ˈmæn.ɪ.dʒər/", "pos": "n", "meaning": "người quản lý, giám đốc quản trị", "example": "The facilities manager oversaw regular structural maintenance."}
        ],
        "collocations": [
            {"phrase": "property manager", "meaning": "quản lý bất động sản/quản lý tòa nhà"},
            {"phrase": "on-site staff", "meaning": "nhân sự làm việc trực tiếp tại chỗ"}
        ],
        "grammar": [
            {"title": "Đọc phần ký tên cuối thư để xác định nghề nghiệp", "rule": "Sign-off block reveals speaker/author role", "analysis": "Khối chữ ký (signature block) ở chân thư luôn chứa thông tin chính xác về chức vụ và đơn vị công tác của tác giả."}
        ]
    },

    # Q164-Q167: Kenneth Hagel to Qualiview Ltd.
    "164": {
        "exp": "Ông Hagel mở đầu email: 'I am writing to discuss a few modifications to the terms outlined in your proposed supplier contract draft before our legal counsel reviews it' (Tôi viết email này để thảo luận một số điều chỉnh đối với các điều khoản nêu trong bản dự thảo hợp đồng nhà cung ứng của quý công ty trước khi cố vấn pháp lý của chúng tôi xem xét). Mục đích viết email là đàm phán hợp đồng -> Chọn (D) To negotiate a contract.",
        "vocab": [
            {"word": "negotiate", "ipa": "/nəˈɡəʊ.ʃi.eɪt/", "pos": "v", "meaning": "đàm phán, thương lượng các điều khoản", "example": "Procurement specialists negotiate bulk purchasing discounts with vendors."},
            {"word": "modification", "ipa": "/ˌmɒd.ɪ.fɪˈkeɪ.ʃən/", "pos": "n", "meaning": "sự sửa đổi, điều chỉnh điều khoản", "example": "Contractors submitted modifications to the architectural blue prints."}
        ],
        "collocations": [
            {"phrase": "negotiate a contract", "meaning": "thương lượng/đàm phán một hợp đồng"},
            {"phrase": "contract draft", "meaning": "bản dự thảo hợp đồng"}
        ],
        "grammar": [
            {"title": "Cấu trúc chỉ mục đích trong câu mở đầu email thương mại", "rule": "I am writing to + V-bare", "analysis": "'I am writing to discuss a few modifications...' là cấu trúc trực tiếp nêu lý do gửi thư."}
        ]
    },
    "165": {
        "exp": "Trong đoạn 2, ông Hagel nhắc đến sản phẩm của Qualiview: 'Our automobile assembly plant relies heavily on your shatterproof automotive windshields and side windows...' (Nhà máy lắp ráp ô tô của chúng tôi phụ thuộc rất nhiều vào các kính chắn gió ô tô chống vỡ và kính cửa sổ hông của quý công ty...). Qualiview sản xuất kính dành cho xe hơi -> Chọn (B) It makes windows for cars.",
        "vocab": [
            {"word": "windshield", "ipa": "/ˈwɪnd.ʃiːld/", "pos": "n", "meaning": "kính chắn gió xe hơi", "example": "The damaged front windshield was replaced with reinforced glass."},
            {"word": "automotive", "ipa": "/ˌɔː.təˈməʊ.tɪv/", "pos": "adj", "meaning": "thuộc về ngành công nghiệp ô tô", "example": "The factory manufactures automotive replacement parts for European sedans."}
        ],
        "collocations": [
            {"phrase": "automotive windshield", "meaning": "kính chắn gió ô tô"},
            {"phrase": "assembly plant", "meaning": "nhà máy lắp ráp xe hơi"}
        ],
        "grammar": [
            {"title": "Từ đồng nghĩa ngữ cảnh (automotive windshields & windows = windows for cars)", "rule": "Noun phrase substitution", "analysis": "'automotive windshields and side windows' chính là 'windows for cars'."}
        ]
    },
    "166": {
        "exp": "Xét câu chứa từ 'address': 'We hope to address these scheduling and warranty discrepancies during an upcoming conference call' (Chúng tôi hy vọng có thể giải quyết/thảo luận phản hồi về những điểm chưa khớp về lịch trình và bảo hành này trong cuộc gọi họp sắp tới). Từ 'address' trong ngữ cảnh xử lý các điểm vướng mắc đồng nghĩa với 'respond to' (giải quyết, phản hồi, thảo luận) -> Chọn (A) respond to.",
        "vocab": [
            {"word": "address", "ipa": "/əˈdres/", "pos": "v", "meaning": "giải quyết, chú trọng xử lý một vấn đề", "example": "The board convened to address severe workplace safety concerns."},
            {"word": "discrepancy", "ipa": "/dɪˈskrep.ən.si/", "pos": "n", "meaning": "sự sai lệch, điểm bất đồng chưa khớp", "example": "Auditors noticed a minor discrepancy between invoices and ledgers."}
        ],
        "collocations": [
            {"phrase": "address an issue", "meaning": "giải quyết/xử lý một vấn đề"},
            {"phrase": "respond to concerns", "meaning": "phản hồi các mối quan tâm/băn khoăn"}
        ],
        "grammar": [
            {"title": "Đa nghĩa của động từ 'address' trong TOEIC", "rule": "address = deal with / respond to / speak to", "analysis": "Khi 'address' đi với các danh từ như concerns, problems, discrepancies, nó mang nghĩa 'giải quyết, phản hồi, xử lý'."}
        ]
    },
    "167": {
        "exp": "Ở phần cuối thư, ông Hagel đề xuất thời gian họp: 'I am available anytime on Wednesday morning prior to 12:00 P.M. for a video conference' (Tôi rảnh bất cứ lúc nào vào sáng thứ Tư trước 12 giờ trưa để gọi họp video). Như vậy thời điểm ông Hagel rảnh vào tuần sau là sáng thứ Tư -> Chọn (C) On Wednesday morning.",
        "vocab": [
            {"word": "prior", "ipa": "/praɪər/", "pos": "adj", "meaning": "trước khi, ưu tiên trước", "example": "All participants must register forty-eight hours prior to the symposium."},
            {"word": "available", "ipa": "/əˈveɪ.lə.bəl/", "pos": "adj", "meaning": "rảnh rỗi, có thời gian trống", "example": "The managing director is available for consultations on Friday mornings."}
        ],
        "collocations": [
            {"phrase": "Wednesday morning", "meaning": "buổi sáng thứ Tư"},
            {"phrase": "prior to", "meaning": "trước một mốc thời gian cụ thể"}
        ],
        "grammar": [
            {"title": "Cấu trúc diễn đạt sự rảnh rỗi 'be available for/on'", "rule": "S + be available + on [day] / at [time]", "analysis": "'I am available anytime on Wednesday morning prior to 12:00 P.M.' chỉ rõ khoảng thời gian rảnh."}
        ]
    },

    # Q168-Q171: Fezker and global shipping container shortage
    "168": {
        "exp": "Bài báo thông tin về tình hình vận tải: 'Ocean freight operators face a severe global shortage of maritime shipping containers, causing extensive transit delays at international ports' (Các hãng vận tải đường biển đang đối mặt với tình trạng thiếu hụt trầm trọng thùng công-ten-nơ chở hàng trên quy mô toàn cầu, gây ra sự chậm trễ vận chuyển kéo dài tại các cảng quốc tế). Cụm 'severe shortage' có nghĩa là hàng hóa/vật dụng này đang bị khan hiếm -> Chọn (B) They are in short supply.",
        "vocab": [
            {"word": "shortage", "ipa": "/ˈʃɔː.tɪdʒ/", "pos": "n", "meaning": "sự thiếu hụt, tình trạng khan hiếm", "example": "A regional microchip shortage stalled automobile assembly lines worldwide."},
            {"word": "maritime", "ipa": "/ˈmær.ɪ.taɪm/", "pos": "adj", "meaning": "thuộc về hàng hải, đường biển", "example": "Maritime logistics regulations govern container vessel inspections."}
        ],
        "collocations": [
            {"phrase": "in short supply", "meaning": "trong tình trạng khan hiếm, thiếu hụt"},
            {"phrase": "shipping container", "meaning": "thùng công-ten-nơ chở hàng"}
        ],
        "grammar": [
            {"title": "Cụm thành ngữ 'in short supply' = shortage", "rule": "Idiomatic predicate adjective", "analysis": "'in short supply' là cách diễn đạt phổ biến mô tả việc hàng hóa, vật tư bị thiếu hụt trên thị trường."}
        ]
    },
    "169": {
        "exp": "Ông Lam - chuyên gia tư vấn logistics nhận định: 'What is urgently needed to mitigate this crisis is proactive communication and transparent data sharing between ocean carriers, exporters, and port administrators' (Điều cần thiết khẩn cấp để giảm thiểu khủng hoảng này là sự giao tiếp chủ động và chia sẻ dữ liệu minh bạch giữa các hãng tàu biển, các nhà xuất khẩu và cơ quan quản lý cảng biển). Điều cần thiết là sự giao tiếp giữa các bên bị ảnh hưởng -> Chọn (D) Communication between affected groups.",
        "vocab": [
            {"word": "mitigate", "ipa": "/ˈmɪt.ɪ.ɡeɪt/", "pos": "v", "meaning": "giảm nhẹ, xoa dịu mức độ nghiêm trọng", "example": "Diversifying suppliers helps mitigate raw material supply disruptions."},
            {"word": "transparent", "ipa": "/trænˈspær.ənt/", "pos": "adj", "meaning": "minh bạch, rõ ràng không giấu giếm", "example": "Public corporations maintain transparent financial accounting standards."}
        ],
        "collocations": [
            {"phrase": "proactive communication", "meaning": "giao tiếp chủ động, trao đổi tích cực"},
            {"phrase": "affected groups", "meaning": "các nhóm/bên bị ảnh hưởng"}
        ],
        "grammar": [
            {"title": "Mệnh đề danh từ làm chủ ngữ với 'What'", "rule": "What is needed to [verb] is [Noun phrase]", "analysis": "Nhấn mạnh giải pháp cốt lõi cho một vấn đề lớn: 'What is urgently needed... is proactive communication'."}
        ]
    },
    "170": {
        "exp": "Bài báo giới thiệu về Fezker: 'Nuwa Lee, CEO of Fezker, a prominent manufacturer of athletic apparel, sportswear, and running gear, noted that European shipments were delayed' (Nuwa Lee, Giám đốc điều hành của Fezker, một nhà sản xuất nổi tiếng về trang phục điền kinh, đồ thể thao và đồ chạy bộ, lưu ý rằng các lô hàng sang châu Âu đã bị trễ). Fezker sản xuất trang phục thể thao -> Chọn (B) Sportswear.",
        "vocab": [
            {"word": "apparel", "ipa": "/əˈpær.əl/", "pos": "n", "meaning": "quần áo, trang phục thời trang", "example": "The brand launched an eco-friendly line of athletic workout apparel."},
            {"word": "prominent", "ipa": "/ˈprɒm.ɪ.nənt/", "pos": "adj", "meaning": "nổi tiếng, xuất chúng, có tên tuổi", "example": "The forum featured prominent economists from leading international banks."}
        ],
        "collocations": [
            {"phrase": "athletic apparel", "meaning": "quần áo thể thao/trang phục vận động"},
            {"phrase": "sportswear manufacturer", "meaning": "nhà sản xuất đồ thể thao"}
        ],
        "grammar": [
            {"title": "Liệt kê danh từ đồng nghĩa bổ trợ nghĩa", "rule": "athletic apparel, sportswear, and running gear", "analysis": "Các danh từ này đều thuộc phân khúc trang phục thể thao (sportswear)."}
        ]
    },
    "171": {
        "exp": "Xét vị trí chèn câu 'These markets are supplied using more readily available truck and train transportation' (Các thị trường này được tiếp tế bằng phương thức vận tải đường bộ xe tải và tàu hỏa vốn sẵn có hơn nhiều): Câu liền trước vị trí [4] nhắc đến doanh số bán hàng trong nước không bị ảnh hưởng do nằm ở các thị trường nội địa lân cận ('Fortunately, our regional domestic sales remain robust'). Cụm từ 'These markets' liên kết hoàn hảo với 'regional domestic sales' -> Chọn (D) [4].",
        "vocab": [
            {"word": "readily", "ipa": "/ˈred.əl.i/", "pos": "adv", "meaning": "sẵn sàng, dễ dàng tiếp cận", "example": "Technical support guides are readily accessible on the corporate intranet."},
            {"word": "transportation", "ipa": "/ˌtræn.spɔːˈteɪ.ʃən/", "pos": "n", "meaning": "ngành giao thông vận tải", "example": "Intermodal rail transportation reduces freight carbon emissions significantly."}
        ],
        "collocations": [
            {"phrase": "readily available", "meaning": "sẵn có, dễ dàng có được"},
            {"phrase": "truck and train transportation", "meaning": "vận tải bằng đường bộ xe tải và tàu hỏa"}
        ],
        "grammar": [
            {"title": "Mối quan hệ liên kết đại từ chỉ định (These + Plural Noun)", "rule": "These markets refers back to regional domestic sales/markets", "analysis": "'These markets' là manh mối ngữ pháp then chốt để xác định vị trí đặt câu nối tiếp sau câu nói về thị trường nội địa."}
        ]
    },

    # Q172-Q175: Construction online chat (Riverview project)
    "172": {
        "exp": "Trong đoạn chat trực tuyến, Gary Wendel và Robbie Zuniga bàn luận về việc: 'pouring concrete foundations', 'structural steel framework', 'plumbing contractor', 'job site safety' (đổ móng bê tông, khung thép kết cấu, nhà thầu ống nước, an toàn công trường). Các thuật ngữ chuyên môn này chỉ rõ họ làm việc trong ngành xây dựng -> Chọn (A) Construction.",
        "vocab": [
            {"word": "foundation", "ipa": "/faʊnˈdeɪ.ʃən/", "pos": "n", "meaning": "nền móng công trình xây dựng", "example": "Crews excavated deep trenches before pouring concrete for the foundation."},
            {"word": "structural", "ipa": "/ˈstrʌk.tʃər.əl/", "pos": "adj", "meaning": "thuộc về kết cấu chịu lực", "example": "Engineers conducted structural stress tests on the new suspension bridge."}
        ],
        "collocations": [
            {"phrase": "construction industry", "meaning": "ngành công nghiệp xây dựng"},
            {"phrase": "job site", "meaning": "công trường xây dựng, nơi thi công"}
        ],
        "grammar": [
            {"title": "Suy đoán ngành nghề từ biệt ngữ chuyên môn (Jargon-based Inference)", "rule": "Identify technical terms related to industry", "analysis": "'concrete', 'steel framework', 'foundation', 'job site' là các từ vựng chỉ ngành xây dựng (Construction)."}
        ]
    },
    "173": {
        "exp": "Gary Wendel mở đầu đoạn thảo luận lúc 7:40 A.M.: 'Good morning, Robbie. Could you give me an update on the Riverview job site progress?' (Chào buổi sáng, Robbie. Cậu có thể cho tôi một cập nhật về tiến độ thi công tại công trường Riverview được không?). Ông Wendel bắt đầu cuộc trao đổi nhằm lấy thông tin cập nhật về tiến độ công việc -> Chọn (C) To obtain an update on some work.",
        "vocab": [
            {"word": "progress", "ipa": "/ˈprəʊ.ɡres/", "pos": "n", "meaning": "sự tiến triển, tiến độ công việc", "example": "The site manager delivers weekly progress briefings to corporate stakeholders."},
            {"word": "obtain", "ipa": "/əbˈteɪn/", "pos": "v", "meaning": "thu thập, có được thông tin", "example": "Researchers must obtain municipal permits before initiating archeological digs."}
        ],
        "collocations": [
            {"phrase": "obtain an update", "meaning": "nhận thông tin cập nhật"},
            {"phrase": "job site progress", "meaning": "tiến độ thi công tại công trường"}
        ],
        "grammar": [
            {"title": "Câu hỏi yêu cầu thông tin lịch sự 'Could you give me...?'", "rule": "Could you give me + noun phrase?", "analysis": "Cấu trúc đề nghị cung cấp thông tin phổ biến trong tin nhắn công việc: 'Could you give me an update on...?'."}
        ]
    },
    "174": {
        "exp": "Robbie báo cáo về dự án Riverview: 'Unfortunately, persistent rainfall last week and concrete delivery delays have pushed back our project schedule for the third time' (Không may là mưa lớn kéo dài tuần trước và sự chậm trễ giao bê tông đã đẩy lùi tiến độ dự án của chúng ta lần thứ ba). Việc lùi tiến độ tới 3 lần chứng minh dự án đã gặp phải nhiều đợt chậm trễ -> Chọn (A) It has had several delays.",
        "vocab": [
            {"word": "persistent", "ipa": "/pəˈsɪs.tənt/", "pos": "adj", "meaning": "kéo dài dai dẳng, liên tục", "example": "Persistent software glitches delayed the anticipated mobile application launch."},
            {"word": "schedule", "ipa": "/ˈʃedʒ.uːl/", "pos": "n, v", "meaning": "tiến độ, thời hạn biểu", "example": "The construction timeline was revised to reflect delivery schedule changes."}
        ],
        "collocations": [
            {"phrase": "push back a schedule", "meaning": "lùi/hoãn thời hạn biểu, làm chậm tiến độ"},
            {"phrase": "several delays", "meaning": "nhiều lần chậm trễ, dời lịch"}
        ],
        "grammar": [
            {"title": "Cụm động từ 'push back' = postpone / delay", "rule": "push back [time/deadline] = delay", "analysis": "'pushed back our schedule for the third time' tương đương với việc đã bị trễ hẹn nhiều lần ('has had several delays')."}
        ]
    },
    "175": {
        "exp": "Gary dặn dò: 'Please attend the 10 A.M. briefing with the general contractor and let me know their decision on additional labor' (Hãy tham dự cuộc họp ngắn lúc 10 giờ sáng với tổng thầu và báo cho tôi biết quyết định của họ về việc bổ sung nhân công). Robbie nhắn đáp lại lúc 7:58 A.M.: 'Will do' (Tôi sẽ làm vậy). Câu này có nghĩa Robbie sẽ chia sẻ kết quả cuộc họp cho Gary -> Chọn (D) He will share the outcome of a meeting.",
        "vocab": [
            {"word": "contractor", "ipa": "/kənˈtræk.tər/", "pos": "n", "meaning": "nhà thầu thi công xây dựng", "example": "The general contractor selected licensed electrical subcontractors for the tower."},
            {"word": "briefing", "ipa": "/ˈbriː.fɪŋ/", "pos": "n", "meaning": "cuộc họp giao ban ngắn, chỉ đạo nhanh", "example": "Team leaders held a fifteen-minute safety briefing prior to operating equipment."}
        ],
        "collocations": [
            {"phrase": "share the outcome", "meaning": "chia sẻ kết quả/quyết định đạt được"},
            {"phrase": "general contractor", "meaning": "tổng thầu xây dựng"}
        ],
        "grammar": [
            {"title": "Thành ngữ đồng ý thực hiện giao việc: 'Will do'", "rule": "Elliptical expression for 'I will do so'", "analysis": "'Will do' là câu trả lời rút gọn thể hiện sự đồng thuận thực hiện yêu cầu của cấp trên trong trao đổi tin nhắn."}
        ]
    }
}

with open('scratch/t2_p7_p1_enrichment.json', 'w', encoding='utf-8') as f:
    json.dump(p7_p1_enrichment, f, ensure_ascii=False, indent=2)

print(f"Enriched {len(p7_p1_enrichment)} questions for Test 2 Part 7 (Part 1: Q147-Q175) successfully!")
