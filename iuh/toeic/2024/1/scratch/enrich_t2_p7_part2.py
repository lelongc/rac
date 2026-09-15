# scratch/enrich_t2_p7_part2.py: Part 7 Multi Passages Enrichment (Q176-Q200)
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

p7_p2_enrichment = {
    # Q176-Q180: Karabel Industries ice cream (Email & Survey)
    "176": {
        "exp": "Trong email gửi đội ngũ, bà Madalyn Kerluke viết: 'Fortunately, our food chemists confirmed that the natural vegetable-based dye formulation can be easily adjusted to alter the coloring of our ice cream without compromising taste' (May mắn thay, các nhà hóa học thực phẩm của chúng ta đã xác nhận rằng công thức chất tạo màu tự nhiên từ rau củ có thể dễ dàng điều chỉnh để thay đổi màu sắc của kem mà không ảnh hưởng tới hương vị). Màu sắc của kem có thể thay đổi dễ dàng -> Chọn (B) Its coloring can be changed easily.",
        "vocab": [
            {"word": "coloring", "ipa": "/ˈkʌl.ər.ɪŋ/", "pos": "n", "meaning": "chất tạo màu thực phẩm", "example": "The confectionery uses organic fruit extracts rather than synthetic food coloring."},
            {"word": "compromise", "ipa": "/ˈkɒm.prə.maɪz/", "pos": "v", "meaning": "làm tổn hại, làm suy giảm chất lượng", "example": "Cost-cutting measures must never compromise consumer product safety."}
        ],
        "collocations": [
            {"phrase": "food coloring", "meaning": "chất tạo màu thực phẩm"},
            {"phrase": "easily adjusted", "meaning": "dễ dàng điều chỉnh được"}
        ],
        "grammar": [
            {"title": "Cấu trúc bị động với trạng từ 'easily adjusted'", "rule": "be + easily + past participle", "analysis": "Diễn tả tính khả thi và thuận tiện trong việc can thiệp kỹ thuật hoặc điều chỉnh công thức."}
        ]
    },
    "177": {
        "exp": "Bà Kerluke nêu rõ dự định trong email: 'I want to convene an all-hands meeting with our product development and culinary testing team this Friday at 10 A.M.' (Tôi muốn triệu tập một cuộc họp toàn thể với đội ngũ phát triển sản phẩm và thử nghiệm ẩm thực của chúng ta vào thứ Sáu tuần này lúc 10 giờ sáng). 'convene an all-hands meeting' tương đương với việc tổ chức cuộc họp nhóm -> Chọn (B) Hold a team meeting.",
        "vocab": [
            {"word": "convene", "ipa": "/kənˈviːn/", "pos": "v", "meaning": "triệu tập, tổ chức một cuộc họp", "example": "The committee chairman will convene a special hearing next Tuesday."},
            {"word": "culinary", "ipa": "/ˈkʌl.ɪ.nər.i/", "pos": "adj", "meaning": "thuộc về nghệ thuật ẩm thực, làm bếp", "example": "Students enrolled in prestigious culinary arts academies."}
        ],
        "collocations": [
            {"phrase": "hold a meeting", "meaning": "tổ chức một cuộc họp"},
            {"phrase": "convene a meeting", "meaning": "triệu tập một cuộc họp chính thức"}
        ],
        "grammar": [
            {"title": "Từ đồng nghĩa convene = hold", "rule": "Lexical substitution for meetings", "analysis": "Hai động từ 'convene a meeting' và 'hold a meeting' hoàn toàn tương đương nhau trong văn phong hành chính."}
        ]
    },
    "178": {
        "exp": "Trong đoạn cuối của email, bà Kerluke chỉ đạo: 'Once we finalize these recipe refinements, we will engage Fatior Labs to administer another round of consumer taste tests' (Một khi chúng ta hoàn tất những tinh chỉnh công thức này, chúng ta sẽ thuê Fatior Labs tiến hành thêm một đợt thử vị người tiêu dùng nữa). Fatior Labs sẽ thực hiện một đợt kiểm nghiệm vị giác khác -> Chọn (C) It will perform another taste test for Karabel Industries.",
        "vocab": [
            {"word": "refinement", "ipa": "/rɪˈfaɪn.mənt/", "pos": "n", "meaning": "sự tinh chỉnh, hoàn thiện chi tiết", "example": "Engineers introduced aerodynamic refinements to improve fuel efficiency."},
            {"word": "administer", "ipa": "/ədˈmɪn.ɪ.stər/", "pos": "v", "meaning": "thực hiện, quản lý, tiến hành cuộc kiểm tra", "example": "Clinicians administer diagnostic health surveys to trial participants."}
        ],
        "collocations": [
            {"phrase": "taste test", "meaning": "cuộc thử vị giác, kiểm nghiệm hương vị"},
            {"phrase": "consumer panel", "meaning": "hội đồng người tiêu dùng đánh giá mẫu"}
        ],
        "grammar": [
            {"title": "Mệnh đề thời gian với 'Once' và tương lai", "rule": "Once + S + V (present), S + will + V-bare", "analysis": "'Once we finalize these recipe refinements, we will engage Fatior Labs...' diễn tả trình tự hành động kế tiếp trong tương lai."}
        ]
    },
    "179": {
        "exp": "Đối chiếu bảng khảo sát người tiêu dùng: Vị 'Peanut Brittle' nhận được điểm đánh giá thấp nhất (chỉ đạt 2/5 điểm về độ cân bằng hương vị và kết cấu), kèm nhận xét của người dùng: 'The peanut pieces are too hard and crunchy; adding fudge swirls or brownie bits would make it much better' (Các mẩu đậu phộng quá cứng; thêm các vệt sốt sô-cô-la hoặc mẩu bánh brownie sẽ ngon hơn nhiều). Vì vậy, công ty sẽ điều chỉnh vị Peanut Brittle -> Chọn (D) Peanut Brittle.",
        "vocab": [
            {"word": "brittle", "ipa": "/ˈbrɪt.əl/", "pos": "adj, n", "meaning": "giòn dễ vỡ; kẹo đậu phộng giòn", "example": "The holiday gift basket included gourmet chocolate and almond brittle."},
            {"word": "texture", "ipa": "/ˈteks.tʃər/", "pos": "n", "meaning": "kết cấu, độ mịn/giòn của thức ăn", "example": "The artisanal gelato had a luxuriously velvety smooth texture."}
        ],
        "collocations": [
            {"phrase": "make adjustments to", "meaning": "tiến hành điều chỉnh, sửa đổi"},
            {"phrase": "survey form", "meaning": "mẫu phiếu khảo sát"}
        ],
        "grammar": [
            {"title": "Kỹ năng kết nối thông tin giữa 2 văn bản (Cross-text Synthesis)", "rule": "Connect email concern with lowest survey score", "analysis": "Email nói về việc sửa các món chưa đạt yêu cầu, đối chiếu phiếu khảo sát để tìm món bị đánh giá thấp nhất là Peanut Brittle."}
        ]
    },
    "180": {
        "exp": "Ở phần thông tin nhân khẩu học (Demographics) trên phiếu khảo sát của Người tham gia số 54: Mục 'Age Group' (Độ tuổi) có đánh dấu tích vào ô '25-40'. Điều này chứng minh người tham gia số 54 ở trong độ tuổi từ 25 đến 40 -> Chọn (B) The participant is between the ages of 25 and 40.",
        "vocab": [
            {"word": "participant", "ipa": "/pɑːˈtɪs.ɪ.pənt/", "pos": "n", "meaning": "người tham gia, đối tượng khảo sát", "example": "Survey participants received a ten-dollar gift voucher for completing the questionnaire."},
            {"word": "demographic", "ipa": "/ˌdem.əˈɡræf.ɪk/", "pos": "adj, n", "meaning": "nhân khẩu học, nhóm đối tượng tuổi/giới tính", "example": "Marketers analyzed regional demographic data to identify potential customers."}
        ],
        "collocations": [
            {"phrase": "between the ages of", "meaning": "trong độ tuổi từ... đến..."},
            {"phrase": "demographic information", "meaning": "thông tin nhân khẩu học"}
        ],
        "grammar": [
            {"title": "Đọc dữ liệu bảng biểu và phiếu khảo sát", "rule": "Verify checked checkbox in demographic fields", "analysis": "Tìm mã số người tham gia (Participant #54), dò đến mục tuổi (Age bracket) để xác nhận ô được đánh dấu chọn."}
        ]
    },

    # Q181-Q185: CreateGreat Web page & Annie Smith Application Letter
    "181": {
        "exp": "Trên trang web tuyển dụng của CreateGreat, mục chế độ làm việc nêu rõ: 'This position offers 100% remote telecommuting flexibility, permitting the successful candidate to work from any location in Canada' (Vị trí này mang lại sự linh hoạt làm việc từ xa 100%, cho phép ứng viên trúng tuyển làm việc từ bất kỳ địa điểm nào tại Canada). Người nhận công việc sẽ được làm việc từ xa -> Chọn (A) Work remotely.",
        "vocab": [
            {"word": "telecommuting", "ipa": "/ˌtel.ɪ.kəˈmjuː.tɪŋ/", "pos": "n", "meaning": "làm việc từ xa qua máy tính", "example": "Corporate telecommuting policies lowered office overhead costs substantially."},
            {"word": "remotely", "ipa": "/rɪˈməʊt.li/", "pos": "adv", "meaning": "từ xa, không cần đến trực tiếp văn phòng", "example": "Software developers often collaborate remotely across multiple time zones."}
        ],
        "collocations": [
            {"phrase": "work remotely", "meaning": "làm việc từ xa"},
            {"phrase": "successful candidate", "meaning": "ứng viên trúng tuyển"}
        ],
        "grammar": [
            {"title": "Cặp từ đồng nghĩa telecommuting = work remotely", "rule": "Lexical equivalence in modern workplace English", "analysis": "'telecommuting flexibility' trong mô tả tuyển dụng đồng nghĩa hoàn toàn với 'work remotely'."}
        ]
    },
    "182": {
        "exp": "Xét câu trên trang web: 'Applicants must possess a creative portfolio that suits our corporate brand aesthetic and commercial needs' (Các ứng viên phải sở hữu một hồ sơ năng lực sáng tạo đáp ứng/phù hợp với thẩm mỹ thương hiệu và nhu cầu thương mại của chúng tôi). Từ 'suits' ở đây đồng nghĩa với 'satisfies' (làm thỏa mãn, đáp ứng đúng yêu cầu) -> Chọn (D) satisfy.",
        "vocab": [
            {"word": "suit", "ipa": "/suːt/", "pos": "v", "meaning": "phù hợp, đáp ứng đúng tiêu chuẩn", "example": "Choose a venue layout that suits the specific needs of your conference delegates."},
            {"word": "satisfy", "ipa": "/ˈsæt.ɪs.faɪ/", "pos": "v", "meaning": "làm thỏa mãn, đáp ứng yêu cầu kỹ thuật", "example": "The manufactured materials satisfy all international safety regulations."}
        ],
        "collocations": [
            {"phrase": "suit the needs", "meaning": "phù hợp với nhu cầu"},
            {"phrase": "brand aesthetic", "meaning": "thẩm mỹ thương hiệu"}
        ],
        "grammar": [
            {"title": "Động từ 'suit' mang nghĩa đáp ứng tiêu chuẩn", "rule": "suit = satisfy / meet requirements", "analysis": "Khi 'suit' có tân ngữ là 'needs, criteria, requirements', nó mang nghĩa 'thỏa mãn, đáp ứng được'."}
        ]
    },
    "183": {
        "exp": "Trên trang web tuyển dụng, hạn chót ghi rõ: 'All application packets must be submitted by April 15'. Tuy nhiên, bức thư xin việc của Annie Smith đề ngày: '18 April' (ngày 18/4). Như vậy cô Smith đã nộp hồ sơ sau hạn chót, tức là đã lỡ hạn nộp hồ sơ -> Chọn (C) She missed an application deadline.",
        "vocab": [
            {"word": "deadline", "ipa": "/ˈded.laɪn/", "pos": "n", "meaning": "hạn chót, thời hạn cuối cùng", "example": "The project manager extended the proposal deadline by two business days."},
            {"word": "packet", "ipa": "/ˈpæk.ɪt/", "pos": "n", "meaning": "bộ hồ sơ, tập tài liệu", "example": "Submit the completed application packet along with three professional references."}
        ],
        "collocations": [
            {"phrase": "miss a deadline", "meaning": "lỡ hạn chót, nộp muộn"},
            {"phrase": "application deadline", "meaning": "hạn chót nộp hồ sơ ứng tuyển"}
        ],
        "grammar": [
            {"title": "Suy luận logic so sánh hai mốc ngày tháng", "rule": "Compare submission date with stated deadline", "analysis": "Ngày trên thư xin việc (18/4) muộn hơn hạn chót ghi trên thông báo (15/4) -> 'She missed an application deadline'."}
        ]
    },
    "184": {
        "exp": "Trong thư xin việc, cô Smith mô tả công việc tại MODA: 'In my current role at MODA, I manage the end-to-end production process for our digital and print promotional magazines, coordinating with photographers and prepress teams' (Ở vai trò hiện tại tại MODA, tôi quản lý toàn bộ quy trình sản xuất từ đầu đến cuối cho các tạp chí quảng bá in ấn và kỹ thuật số, phối hợp với các nhiếp ảnh gia và tổ chế bản). Cô Smith chịu trách nhiệm quản lý quy trình sản xuất -> Chọn (C) Managing a production process.",
        "vocab": [
            {"word": "production", "ipa": "/prəˈdʌk.ʃən/", "pos": "n", "meaning": "sự sản xuất, quy trình xuất bản", "example": "The director streamlined publication production to cut printing expenses."},
            {"word": "coordinate", "ipa": "/kəʊˈɔː.dɪ.neɪt/", "pos": "v", "meaning": "phối hợp, điều phối các bộ phận", "example": "Logistics coordinators coordinate transport schedules with maritime carriers."}
        ],
        "collocations": [
            {"phrase": "production process", "meaning": "quy trình sản xuất/chế bản"},
            {"phrase": "end-to-end", "meaning": "từ đầu đến cuối, trọn gói"}
        ],
        "grammar": [
            {"title": "Cụm danh từ chỉ trách nhiệm quản lý: Managing + Noun", "rule": "Gerund phrase as role description", "analysis": "'manage the production process' được diễn giải thành 'Managing a production process'."}
        ]
    },
    "185": {
        "exp": "Cô Smith nhắc đến Medesheen trong thư: 'Additionally, I contributed creative visual designs for Medesheen, an acclaimed online fashion and lifestyle blog featuring weekly editorial posts' (Ngoài ra, tôi còn đóng góp các thiết kế trực quan sáng tạo cho Medesheen, một trang blog thời trang và phong cách sống trực tuyến nổi tiếng với các bài xã luận hàng tuần). Medesheen là một trang blog về thời trang -> Chọn (B) A fashion blog.",
        "vocab": [
            {"word": "acclaimed", "ipa": "/əˈkleɪmd/", "pos": "adj", "meaning": "được đánh giá cao, được khen ngợi rộng rãi", "example": "The internationally acclaimed author delivered a keynote lecture."},
            {"word": "editorial", "ipa": "/ˌed.ɪˈtɔː.ri.əl/", "pos": "adj, n", "meaning": "thuộc về biên tập; bài viết chuyên đề", "example": "The magazine's editorial board approved twenty featured articles."}
        ],
        "collocations": [
            {"phrase": "fashion blog", "meaning": "trang blog về thời trang"},
            {"phrase": "editorial post", "meaning": "bài viết biên tập/xã luận"}
        ],
        "grammar": [
            {"title": "Mệnh đề đồng vị ngữ giải thích bản chất thực thể", "rule": "Entity, an [Adjective] [Noun Phrase]...", "analysis": "'Medesheen, an acclaimed online fashion and lifestyle blog' dùng đồng vị ngữ để định nghĩa trực tiếp Medesheen là một blog thời trang."}
        ]
    },

    # Q186-Q190: Akira Nakashima emails & Fowler Office Supplies receipt
    "186": {
        "exp": "Ông Nakashima mở đầu email đầu tiên gửi Fowler Office Supplies: 'I am writing because the order receipt emailed to me does not contain an itemized cost breakdown for each individual item purchased, which our finance department strictly requires for expense reimbursement' (Tôi viết thư này vì hóa đơn đặt hàng được gửi email cho tôi không có bảng phân tích chi phí chi tiết cho từng mặt hàng đã mua, điều mà phòng tài chính của chúng tôi bắt buộc phải có để hoàn trả chi phí). Lý do gửi thư là vì hóa đơn nhận được chưa đủ chi tiết -> Chọn (C) He received a receipt that was not detailed enough.",
        "vocab": [
            {"word": "itemized", "ipa": "/ˈaɪ.tə.maɪzd/", "pos": "adj", "meaning": "được liệt kê chi tiết từng khoản/món", "example": "Request an itemized hotel bill showing room service and phone fees."},
            {"word": "reimbursement", "ipa": "/ˌriː.ɪmˈbɜːs.mənt/", "pos": "n", "meaning": "sự hoàn tiền, thanh toán lại công tác phí", "example": "Employees submit travel receipts to obtain expense reimbursement."}
        ],
        "collocations": [
            {"phrase": "itemized receipt", "meaning": "hóa đơn chi tiết từng món hàng"},
            {"phrase": "detailed breakdown", "meaning": "bảng phân tích chi tiết"}
        ],
        "grammar": [
            {"title": "Paraphrase mức độ chi tiết: not detailed enough = lacks itemized breakdown", "rule": "Synonym relationship in comprehension", "analysis": "'does not contain an itemized cost breakdown' đồng nghĩa với 'was not detailed enough'."}
        ]
    },
    "187": {
        "exp": "Trong email hồi đáp, nhân viên Higgins viết: 'To apologize for this inconvenience, we have attached a special voucher granting a 15% discount on your next online order' (Để xin lỗi vì sự bất tiện này, chúng tôi đã đính kèm một phiếu giảm giá đặc biệt giảm 15% cho đơn hàng trực tuyến tiếp theo của quý khách). Khách hàng sẽ nhận được mức giảm giá cho đơn tiếp theo -> Chọn (D) A price discount.",
        "vocab": [
            {"word": "voucher", "ipa": "/ˈvaʊ.tʃər/", "pos": "n", "meaning": "phiếu mua hàng, phiếu giảm giá quà tặng", "example": "Guests received a twenty-dollar dining voucher upon check-in."},
            {"word": "discount", "ipa": "/ˈdɪs.kaʊnt/", "pos": "n", "meaning": "mức chiết khấu, giảm giá", "example": "The retailer offered a promotional discount on clearance items."}
        ],
        "collocations": [
            {"phrase": "price discount", "meaning": "chiết khấu giảm giá tiền hàng"},
            {"phrase": "next order", "meaning": "đơn hàng kế tiếp"}
        ],
        "grammar": [
            {"title": "Cấu trúc đền bù khách hàng bằng ưu đãi", "rule": "To apologize for X, we offer [benefit]", "analysis": "Mẫu câu quy chuẩn trong dịch vụ khách hàng: tặng voucher giảm giá để tạ lỗi vì sự cố hóa đơn."}
        ]
    },
    "188": {
        "exp": "Ông Higgins gợi ý cho ông Nakashima: 'Notice that you regularly buy several cartons of multipurpose copy paper each month. I suggest selecting our Recurring Order feature for printer paper so you never run out' (Để ý thấy quý khách thường xuyên mua nhiều thùng giấy photo đa năng mỗi tháng. Tôi đề xuất chọn tính năng Đặt hàng định kỳ cho giấy in để quý khách không bao giờ bị hết hàng). Mặt hàng được gợi ý chọn Recurring Order là giấy in -> Chọn (A) Printer paper.",
        "vocab": [
            {"word": "recurring", "ipa": "/rɪˈkɜː.rɪŋ/", "pos": "adj", "meaning": "định kỳ lặp lại, thường xuyên diễn ra", "example": "Subscribers set up recurring monthly credit card billing."},
            {"word": "carton", "ipa": "/ˈkɑː.tən/", "pos": "n", "meaning": "thùng bìa các-tông đựng hàng", "example": "The supply room stores ten cartons of thermal receipt paper."}
        ],
        "collocations": [
            {"phrase": "printer paper", "meaning": "giấy in văn phòng"},
            {"phrase": "recurring order", "meaning": "đơn đặt hàng định kỳ tự động"}
        ],
        "grammar": [
            {"title": "Cặp từ đồng nghĩa copy paper = printer paper", "rule": "Everyday office vocabulary equivalence", "analysis": "'multipurpose copy paper' trong văn bản là tên gọi khác của 'printer paper'."}
        ]
    },
    "189": {
        "exp": "Về giải pháp kỹ thuật, ông Higgins cho biết: 'I have passed your suggestion to our web development team to explore adding an optional secondary billing email field during checkout, so receipts can automatically be sent to accounting departments directly' (Tôi đã chuyển đề xuất của quý khách tới đội ngũ phát triển trang web để nghiên cứu thêm ô nhập email thanh toán phụ khi thanh toán, để hóa đơn có thể được tự động gửi trực tiếp đến các phòng kế toán). Higgins sẽ đề nghị đội ngũ kỹ thuật nghiên cứu việc gửi hóa đơn đến nhiều địa chỉ email -> Chọn (B) Providing an option to send receipts to multiple e-mail addresses.",
        "vocab": [
            {"word": "billing", "ipa": "/ˈbɪl.ɪŋ/", "pos": "n", "meaning": "thanh toán, lập hóa đơn kế toán", "example": "Please update your billing contact information before the new billing cycle."},
            {"word": "checkout", "ipa": "/ˈtʃek.aʊt/", "pos": "n", "meaning": "bước thanh toán đơn hàng trực tuyến", "example": "Customers enter discount codes during the online checkout process."}
        ],
        "collocations": [
            {"phrase": "multiple e-mail addresses", "meaning": "nhiều địa chỉ email khác nhau"},
            {"phrase": "billing email", "meaning": "email nhận hóa đơn kế toán"}
        ],
        "grammar": [
            {"title": "Cụm động từ 'look into' = explore / investigate", "rule": "look into + noun phrase", "analysis": "'look into' nghĩa là xem xét, khảo sát tính khả thi của một giải pháp kỹ thuật."}
        ]
    },
    "190": {
        "exp": "Trên hóa đơn thứ hai gửi kèm có ghi chú chính sách đổi trả: 'Returns and exchanges may be processed at any Fowler Office Supplies retail store within 30 days. Customers must present the 9-digit order number printed above' (Việc hoàn trả và đổi hàng có thể được xử lý tại bất kỳ cửa hàng bán lẻ Fowler Office Supplies nào trong vòng 30 ngày. Khách hàng bắt buộc phải xuất trình mã số đơn hàng 9 chữ số in ở phía trên). Điều kiện để đổi trả hàng tại cửa hàng là mã số đơn hàng -> Chọn (D) The order number.",
        "vocab": [
            {"word": "exchange", "ipa": "/ɪksˈtʃeɪndʒ/", "pos": "n, v", "meaning": "việc đổi sản phẩm khác; đổi hàng", "example": "Defective merchandise may be presented for exchange within fourteen days."},
            {"word": "present", "ipa": "/prɪˈzent/", "pos": "v", "meaning": "xuất trình giấy tờ/mã số", "example": "Cardholders must present a photo ID when making large cash withdrawals."}
        ],
        "collocations": [
            {"phrase": "order number", "meaning": "mã số đơn đặt hàng"},
            {"phrase": "process a return", "meaning": "xử lý việc trả lại hàng"}
        ],
        "grammar": [
            {"title": "Động từ khuyết thiếu bắt buộc 'must present'", "rule": "must + V-bare for mandatory requirements", "analysis": "'Customers must present the order number' khẳng định điều kiện tiên quyết duy nhất để được hoàn trả."}
        ]
    },

    # Q191-Q195: Crawford and Duval article, Web site, receipt for Mei-Lin Fong
    "191": {
        "exp": "Bài báo mở đầu: 'Crawford and Duval, the renowned luxury retailer, announced the grand opening of two new department store locations in the metropolitan area this weekend...' (Crawford and Duval, nhà bán lẻ xa xỉ nổi tiếng, đã công bố lễ khai trương hai địa điểm cửa hàng bách hóa mới tại khu vực đô thị vào cuối tuần này...). Mục đích của bài báo là thông báo về việc khai trương các cửa hàng mới -> Chọn (B) To announce store openings.",
        "vocab": [
            {"word": "opening", "ipa": "/ˈəʊ.pən.ɪŋ/", "pos": "n", "meaning": "lễ khai trương, việc mở cửa hàng mới", "example": "The grand opening of the suburban shopping mall attracted huge crowds."},
            {"word": "renowned", "ipa": "/rɪˈnaʊnd/", "pos": "adj", "meaning": "nổi tiếng, có danh tiếng lẫy lừng", "example": "The gallery features sculptures created by internationally renowned artists."}
        ],
        "collocations": [
            {"phrase": "grand opening", "meaning": "lễ khai trương trọng thể"},
            {"phrase": "store openings", "meaning": "việc mở các chi nhánh cửa hàng"}
        ],
        "grammar": [
            {"title": "Công thức xác định mục đích bài báo thương mại", "rule": "Opening paragraph states the main news announcement", "analysis": "Đoạn đầu bài báo thông báo sự kiện khai trương hai chi nhánh mới của tập đoàn bán lẻ."}
        ]
    },
    "192": {
        "exp": "Trên trang web của Crawford and Duval có giới thiệu dịch vụ: 'Transform your home with the help of our talented on-staff interior designers. Schedule a complimentary 60-minute styling consultation today' (Biến đổi ngôi nhà của bạn với sự trợ giúp từ các nhà thiết kế nội thất tài năng trực thuộc đội ngũ của chúng tôi. Hãy đặt lịch tư vấn phong cách 60 phút miễn phí ngay hôm nay). Công ty có tuyển dụng các nhà thiết kế nội thất -> Chọn (C) It employs interior designers.",
        "vocab": [
            {"word": "interior", "ipa": "/ɪnˈtɪə.ri.ər/", "pos": "adj, n", "meaning": "nội thất, bên trong nhà", "example": "The historic residence underwent extensive interior renovations."},
            {"word": "consultation", "ipa": "/ˌkɒn.sʌlˈteɪ.ʃən/", "pos": "n", "meaning": "buổi tư vấn chuyên môn", "example": "Clients booked private legal consultations with senior partners."}
        ],
        "collocations": [
            {"phrase": "interior designer", "meaning": "nhà thiết kế nội thất"},
            {"phrase": "on-staff", "meaning": "thuộc biên chế, làm việc chính thức cho công ty"}
        ],
        "grammar": [
            {"title": "Cụm tính từ 'on-staff' đồng nghĩa với 'employs'", "rule": "on-staff [professions] = the company employs [professions]", "analysis": "'on-staff interior designers' chứng minh các chuyên gia này là nhân viên do công ty trực tiếp tuyển dụng."}
        ]
    },
    "193": {
        "exp": "Trên hóa đơn mua hàng của cô Mei-Lin Fong, dòng mặt hàng chăn ghi rõ: 'Cashmere-blend throw blanket (Machine Washable) - $120.00' (Chăn len cashmere pha mỏng (Có thể giặt bằng máy) - 120,00 đô la). Chi tiết 'Machine Washable' cho thấy chiếc chăn có thể giặt bằng máy giặt -> Chọn (A) It can be washed by machine.",
        "vocab": [
            {"word": "washable", "ipa": "/ˈwɒʃ.ə.bəl/", "pos": "adj", "meaning": "có thể giặt được mà không bị hỏng vải", "example": "All children's plush toys must be made from non-toxic, washable fabrics."},
            {"word": "blanket", "ipa": "/ˈblæŋ.kɪt/", "pos": "n", "meaning": "chiếc chăn đắp, mền", "example": "Hotel rooms are stocked with extra wool blankets in the closet."}
        ],
        "collocations": [
            {"phrase": "machine washable", "meaning": "có thể giặt bằng máy"},
            {"phrase": "throw blanket", "meaning": "chăn mỏng đắp sofa/giường"}
        ],
        "grammar": [
            {"title": "Tính từ có hậu tố '-able' chỉ khả năng", "rule": "wash + able = able to be washed", "analysis": "'Machine washable' tương đương với câu bị động 'can be washed by machine'."}
        ]
    },
    "194": {
        "exp": "Kết hợp bài báo và hóa đơn: Hóa đơn mang tiêu đề 'Crawford and Duval - Receipt', và bài báo đã định nghĩa Crawford and Duval là 'a prominent department store chain selling furniture, home decor, and apparel' (chuỗi cửa hàng bách hóa tổng hợp nổi tiếng bán nội thất, đồ trang trí nhà và quần áo). Do đó, cô Fong mua hàng tại một cửa hàng bách hóa tổng hợp -> Chọn (D) In a department store.",
        "vocab": [
            {"word": "department", "ipa": "/dɪˈpɑːt.mənt/", "pos": "n", "meaning": "gian hàng, gian bách hóa", "example": "The shoe department is located on the second floor of the mall."},
            {"word": "furnishings", "ipa": "/ˈfɜː.nɪ.ʃɪŋz/", "pos": "n", "meaning": "đồ đạc nội thất, đồ trang hoàng trong nhà", "example": "The retailer specializes in modern Scandinavian home furnishings."}
        ],
        "collocations": [
            {"phrase": "department store", "meaning": "cửa hàng bách hóa tổng hợp"},
            {"phrase": "make a purchase", "meaning": "thực hiện mua sắm hàng hóa"}
        ],
        "grammar": [
            {"title": "Suy luận liên văn bản về loại hình cửa hàng", "rule": "Synthesize company classification across documents", "analysis": "Hóa đơn ghi tên Crawford and Duval, bài báo giải thích đây là 'department store chain'."}
        ]
    },
    "195": {
        "exp": "Ở chân hóa đơn mua hàng của cô Mei-Lin Fong có ghi: 'Loyalty Rewards: Frequent Purchase Club Member ID #49281 - Points earned today: 120' (Phần thưởng thân thiết: Mã hội viên Câu lạc bộ Mua sắm Thường xuyên #49281 - Điểm tích lũy hôm nay: 120). Chi tiết này chứng minh cô Fong là hội viên của Frequent Purchase Club -> Chọn (B) She is a member of the Frequent Purchase Club.",
        "vocab": [
            {"word": "frequent", "ipa": "/ˈfriː.kwənt/", "pos": "adj", "meaning": "thường xuyên, quen thuộc", "example": "Frequent flyers accumulate airline miles for complimentary upgrades."},
            {"word": "loyalty", "ipa": "/ˈlɔɪ.əl.ti/", "pos": "n", "meaning": "sự trung thành, gắn bó của khách hàng", "example": "Customer loyalty programs reward repeat shoppers with exclusive coupons."}
        ],
        "collocations": [
            {"phrase": "frequent purchase club", "meaning": "câu lạc bộ khách hàng mua sắm thường xuyên"},
            {"phrase": "loyalty points", "meaning": "điểm thưởng tích lũy thân thiết"}
        ],
        "grammar": [
            {"title": "Đọc thông tin chân trang biên lai (Receipt Footer Data)", "rule": "Scan footer for loyalty accounts and membership details", "analysis": "Các dòng ghi chú ở đáy hóa đơn thường chứa thông tin hội viên (Member ID, Loyalty points)."}
        ]
    },

    # Q196-Q200: Osawa Corporate Team Building Web pages & review by Karen Peterson
    "196": {
        "exp": "Trên trang web đầu tiên của Osawa Team Building, phần mô tả gói 'Scavenger Hunt' ghi rõ thông số thời gian: 'Duration: 3 Hours | Activity Level: Moderate' (Thời lượng: 3 tiếng | Mức độ vận động: Trung bình). Gói Scavenger Hunt mất 3 tiếng để hoàn thành -> Chọn (D) It takes three hours to complete.",
        "vocab": [
            {"word": "duration", "ipa": "/djʊˈreɪ.ʃən/", "pos": "n", "meaning": "khoảng thời gian kéo dài, thời lượng", "example": "The training seminar had a scheduled duration of two full days."},
            {"word": "scavenger", "ipa": "/ˈskæv.ɪn.dʒər/", "pos": "n", "meaning": "người lùng tìm đồ vật trong trò chơi", "example": "Teams completed outdoor clues during the exciting corporate scavenger hunt."}
        ],
        "collocations": [
            {"phrase": "take three hours", "meaning": "mất/kéo dài ba tiếng đồng hồ"},
            {"phrase": "scavenger hunt", "meaning": "trò chơi truy tìm đồ vật/mật thư"}
        ],
        "grammar": [
            {"title": "Từ đồng nghĩa duration = takes [time] to complete", "rule": "Duration: 3 Hours = It takes three hours to complete", "analysis": "Thông số 'Duration' trong bảng biểu luôn tương ứng với cấu trúc 'It takes + time + to complete'."}
        ]
    },
    "197": {
        "exp": "Bảng tổng hợp các gói sự kiện trên trang web liệt kê sức chứa số người: Gói 'Obstacle Course' tối đa 80 người; 'City Quest' tối đa 150 người; 'Escape Room' tối đa 60 người; riêng gói 'Game Day' ghi rõ: 'Group Size: 50–500 participants' (Quy mô nhóm: 50 đến 500 người tham gia). Do đó, sự kiện phù hợp nhất cho nhóm trên 200 người là Game Day -> Chọn (A) Game Day.",
        "vocab": [
            {"word": "accommodate", "ipa": "/əˈkɒm.ə.deɪt/", "pos": "v", "meaning": "đáp ứng sức chứa, chứa đủ số lượng", "example": "The grand conference ballroom can accommodate upwards of eight hundred guests."},
            {"word": "participant", "ipa": "/pɑːˈtɪs.ɪ.pənt/", "pos": "n", "meaning": "người tham gia hoạt động", "example": "Over two hundred corporate participants registered for the athletic tournament."}
        ],
        "collocations": [
            {"phrase": "group size", "meaning": "quy mô nhóm, số lượng người tham gia"},
            {"phrase": "game day", "meaning": "ngày hội trò chơi tập thể"}
        ],
        "grammar": [
            {"title": "Kỹ năng tra cứu bảng so sánh số liệu (Comparative Range Analysis)", "rule": "Compare numerical range against threshold (>200)", "analysis": "Chỉ có gói Game Day (50-500) có giới hạn trên vượt qua mức 200 người."}
        ]
    },
    "198": {
        "exp": "Trên trang web thứ hai có ghi chính sách ưu đãi cho khách hàng: 'Share your feedback! Clients who submit an authentic event review on our customer portal will receive a 10% promotional discount voucher code applied to their subsequent booking' (Chia sẻ ý kiến của bạn! Các khách hàng gửi bài đánh giá sự kiện xác thực trên cổng thông tin khách hàng của chúng tôi sẽ nhận được mã phiếu giảm giá 10% áp dụng cho lần đặt sự kiện tiếp theo). Vì bà Peterson đã viết bài đánh giá nên bà sẽ nhận được giảm giá -> Chọn (B) She will receive a discount on an event.",
        "vocab": [
            {"word": "subsequent", "ipa": "/ˈsʌb.sɪ.kwənt/", "pos": "adj", "meaning": "tiếp theo sau, xảy ra sau đó", "example": "The initial launch was successful, and subsequent software updates added features."},
            {"word": "portal", "ipa": "/ˈpɔː.təl/", "pos": "n", "meaning": "cổng thông tin đánh giá điện tử", "example": "Clients submitted feedback ratings through the digital service portal."}
        ],
        "collocations": [
            {"phrase": "receive a discount", "meaning": "nhận được mức giảm giá"},
            {"phrase": "subsequent booking", "meaning": "lần đặt chỗ/đặt dịch vụ tiếp theo"}
        ],
        "grammar": [
            {"title": "Cấu trúc điều kiện liên văn bản", "rule": "Condition stated on web page satisfied by review submission", "analysis": "Trang web đặt điều kiện 'viết review để nhận voucher giảm giá 10%', và bà Peterson đã viết review -> bà ấy sẽ nhận được voucher giảm giá."}
        ]
    },
    "199": {
        "exp": "Trong bài đánh giá của mình, bà Karen Peterson chia sẻ: 'Our company, Whitten Tech, initially requested the Scavenger Hunt, but because it was already fully booked on our selected date, we ended up choosing City Quest instead' (Công ty của chúng tôi, Whitten Tech, ban đầu đã yêu cầu gói Scavenger Hunt, nhưng vì gói đó đã kín lịch vào ngày chúng tôi chọn, cuối cùng chúng tôi đành phải chọn City Quest để thay thế). Điều này có nghĩa Whitten Tech không thể đăng ký được hoạt động lựa chọn số 1 của mình -> Chọn (C) It was unable to schedule its first-choice activity.",
        "vocab": [
            {"word": "fully booked", "ipa": "/ˈfʊl.i bʊkt/", "pos": "adj", "meaning": "đã kín chỗ, hết chỗ trống", "example": "The beach resort was fully booked for the holiday weekend."},
            {"word": "initially", "ipa": "/ɪˈnɪʃ.əl.i/", "pos": "adv", "meaning": "ban đầu, lúc đầu dự tính", "example": "We initially planned an outdoor picnic before rain forced us indoors."}
        ],
        "collocations": [
            {"phrase": "first-choice activity", "meaning": "hoạt động được lựa chọn đầu tiên/ưu tiên số 1"},
            {"phrase": "fully booked", "meaning": "đã được đặt kín lịch, hết chỗ"}
        ],
        "grammar": [
            {"title": "Cụm động từ 'end up + V-ing'", "rule": "end up + V-ing = eventually do something unpredicted", "analysis": "'we ended up choosing City Quest instead' diễn tả kết quả cuối cùng phải chọn phương án dự phòng vì phương án đầu tiên bị hết chỗ."}
        ]
    },
    "200": {
        "exp": "Trong phần góp ý cuối bài đánh giá, bà Peterson nêu rõ điểm đáng thất vọng: 'My only major complaint was the total absence of advance notice regarding the extensive walking distances required. Several colleagues wore formal office shoes and suffered painful blisters' (Lời phàn nàn lớn duy nhất của tôi là việc hoàn toàn không có thông báo trước về quãng đường đi bộ rất dài phải thực hiện. Một số đồng nghiệp đã đi giày công sở và bị phồng rộp chân đau đớn). Điểm thất vọng là sự thiếu thông tin về quãng đường đi bộ -> Chọn (B) The lack of information about walking distances.",
        "vocab": [
            {"word": "absence", "ipa": "/ˈæb.səns/", "pos": "n", "meaning": "sự vắng mặt, thiếu sót hoàn toàn", "example": "The absence of clear directional signage confused conference attendees."},
            {"word": "extensive", "ipa": "/ɪkˈsten.sɪv/", "pos": "adj", "meaning": "rộng lớn, dài, quy mô lớn", "example": "Crews undertook extensive repairs after the seismic tremor."}
        ],
        "collocations": [
            {"phrase": "lack of information", "meaning": "sự thiếu hụt thông tin"},
            {"phrase": "walking distance", "meaning": "quãng đường đi bộ"}
        ],
        "grammar": [
            {"title": "Cặp từ đồng nghĩa absence of notice = lack of information", "rule": "Lexical substitution for negative conditions", "analysis": "'total absence of advance notice regarding walking distances' tương đương với 'The lack of information about walking distances'."}
        ]
    }
}

with open('scratch/t2_p7_p2_enrichment.json', 'w', encoding='utf-8') as f:
    json.dump(p7_p2_enrichment, f, ensure_ascii=False, indent=2)

print(f"Enriched {len(p7_p2_enrichment)} questions for Test 2 Part 7 (Part 2: Q176-Q200) successfully!")
