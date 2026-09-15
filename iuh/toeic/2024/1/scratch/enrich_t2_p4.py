# scratch/enrich_t2_p4.py: Part 4 Enrichment for Test 2 (Q71-Q100)
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

p4_enrichment = {
    # Q71-Q73: Blue Drop Creations, jewelry, loyal customer, feedback
    "71": {
        "exp": "Người nói giới thiệu trong tin nhắn thoại: 'This is Sabine calling from Blue Drop Creations. I just put the earrings and necklaces that you ordered from me in the mail...' (Đây là Sabine gọi từ Blue Drop Creations. Tôi vừa mới gửi bưu điện đôi bông tai và các dây chuyền mà bạn đã đặt làm từ tôi...). Các mặt hàng 'earrings' (bông tai) và 'necklaces' (dây chuyền trang sức) chứng minh người nói là một người thợ chế tác trang sức -> Chọn (D) A jewelry maker.",
        "vocab": [
            {"word": "jewelry", "ipa": "/ˈdʒuː.əl.ri/", "pos": "n", "meaning": "đồ kim hoàn, trang sức quý", "example": "The boutique specializes in handcrafted artisan jewelry."},
            {"word": "necklace", "ipa": "/ˈnek.ləs/", "pos": "n", "meaning": "dây chuyền, vòng đeo cổ", "example": "She wore a delicate silver necklace adorned with pearls."},
            {"word": "earrings", "ipa": "/ˈɪə.rɪŋz/", "pos": "n", "meaning": "đôi hoa tai, khuyên tai", "example": "The set comes with matching gold earrings and a bracelet."}
        ],
        "collocations": [
            {"phrase": "jewelry maker", "meaning": "thợ làm/chế tác đồ trang sức"},
            {"phrase": "put in the mail", "meaning": "gửi qua đường bưu điện"}
        ],
        "grammar": [
            {"title": "Kỹ năng nhận biết nghề nghiệp người nói trong Part 4", "rule": "Listen to opening company name and product nouns", "analysis": "Thông tin nghề nghiệp thường xuất hiện trong 1-2 câu đầu tiên của bài nói qua tên thương hiệu và danh từ chỉ sản phẩm."}
        ]
    },
    "72": {
        "exp": "Người nói giải thích lý do tặng quà: '...and because you've been a customer for over 10 years, I've also included a handcrafted jewelry box as a token of my appreciation' (...và bởi vì bạn đã là khách hàng thân thiết trong hơn 10 năm qua, tôi cũng đã gửi kèm một hộp đựng trang sức thủ công như một món quà tri ân). Khách hàng đã ủng hộ hơn 10 năm là một khách hàng trung thành -> Chọn (C) Because the listener is a loyal customer.",
        "vocab": [
            {"word": "loyal", "ipa": "/ˈlɔɪ.əl/", "pos": "adj", "meaning": "trung thành, gắn bó lâu năm", "example": "Retailers offer special reward tiers to reward loyal shoppers."},
            {"word": "appreciation", "ipa": "/əˌpriː.ʃiˈeɪ.ʃən/", "pos": "n", "meaning": "sự tri ân, lòng biết ơn", "example": "Employees received bonuses in appreciation of their dedication."}
        ],
        "collocations": [
            {"phrase": "loyal customer", "meaning": "khách hàng trung thành, thân thiết"},
            {"phrase": "token of appreciation", "meaning": "món quà thay lời tri ân"}
        ],
        "grammar": [
            {"title": "Mệnh đề chỉ nguyên nhân với 'because'", "rule": "Because + clause (cause), main clause (effect)", "analysis": "'because you've been a customer for over 10 years' là mệnh đề trạng ngữ chỉ lý do cho hành động tặng quà."}
        ]
    },
    "73": {
        "exp": "Người nói yêu cầu khách hàng gọi lại: 'Once you receive the package, please give me a call to let me know how you like the custom designs and if you have any feedback' (Khi bạn nhận được kiện hàng, xin hãy gọi lại cho tôi để cho tôi biết bạn thấy những mẫu thiết kế riêng đó thế nào và bạn có góp ý gì không). Mục đích gọi lại là để đóng góp ý kiến nhận xét -> Chọn (A) To give feedback.",
        "vocab": [
            {"word": "feedback", "ipa": "/ˈfiːd.bæk/", "pos": "n", "meaning": "ý kiến phản hồi, nhận xét đánh giá", "example": "Constructive client feedback helps us refine our services."},
            {"word": "custom", "ipa": "/ˈkʌs.təm/", "pos": "adj", "meaning": "được thiết kế riêng theo đơn đặt hàng", "example": "The tailor manufactures custom suits to individual measurements."}
        ],
        "collocations": [
            {"phrase": "give feedback", "meaning": "đưa ra ý kiến nhận xét, phản hồi"},
            {"phrase": "custom design", "meaning": "thiết kế riêng, mẫu mã đặt trước"}
        ],
        "grammar": [
            {"title": "Mệnh đề thời gian với liên từ 'Once'", "rule": "Once + S + V (present), imperative / future", "analysis": "'Once you receive the package, please give me a call...' - 'Once' có nghĩa là 'một khi/ngay khi'."}
        ]
    },

    # Q74-Q76: Dakota Framing, wedding picture, place order, warranty
    "74": {
        "exp": "Người nói mở đầu tin nhắn: 'Good morning. This is Brandon from Dakota Framing Company, returning your call. We received your voice mail about wanting to frame a wedding picture' (Chào buổi sáng. Tôi là Brandon từ Công ty Đóng Khung Dakota, xin gọi lại cho bạn. Chúng tôi đã nhận được hộp thư thoại của bạn về việc muốn đóng khung một bức ảnh cưới). Khách hàng muốn đóng khung một bức ảnh -> Chọn (D) Have a photograph framed.",
        "vocab": [
            {"word": "frame", "ipa": "/freɪm/", "pos": "v, n", "meaning": "đóng khung ảnh; khung tranh ảnh", "example": "She chose an antique wooden border to frame the family portrait."},
            {"word": "photograph", "ipa": "/ˈfəʊ.tə.ɡrɑːf/", "pos": "n", "meaning": "bức ảnh chụp", "example": "The exhibition showcases black-and-white historic photographs."}
        ],
        "collocations": [
            {"phrase": "have a photograph framed", "meaning": "đem đóng khung một bức ảnh"},
            {"phrase": "return a call", "meaning": "gọi điện thoại lại"}
        ],
        "grammar": [
            {"title": "Thể truyền khiến bị động (Causative Passive: have + O + V3/ed)", "rule": "have/get + object + past participle", "analysis": "'have a photograph framed' nghĩa là thuê/nhờ người khác đóng khung bức ảnh cho mình."}
        ]
    },
    "75": {
        "exp": "Người nói hướng dẫn: 'There is no need to print the photo yourself... simply upload the digital file to our website, select your favorite frame moulding, and place your order directly online' (Bạn không cần tự in ảnh... chỉ cần tải tệp ảnh kỹ thuật số lên trang web của chúng tôi, chọn viền khung yêu thích và đặt hàng trực tiếp qua mạng). Hành động trên trang web là đặt đơn hàng -> Chọn (B) Place an order.",
        "vocab": [
            {"word": "upload", "ipa": "/ʌpˈləʊd/", "pos": "v", "meaning": "tải dữ liệu/ảnh lên mạng", "example": "Applicants must upload scanned identification documents."},
            {"word": "moulding", "ipa": "/ˈməʊl.dɪŋ/", "pos": "n", "meaning": "đường gờ, viền khung tranh gỗ", "example": "The studio offers ornate gilded mouldings for vintage canvases."}
        ],
        "collocations": [
            {"phrase": "place an order", "meaning": "đặt một đơn hàng"},
            {"phrase": "upload a digital file", "meaning": "tải tệp kỹ thuật số lên"}
        ],
        "grammar": [
            {"title": "Cấu trúc 'There is no need to + V-inf'", "rule": "There is no need to V-bare", "analysis": "Dùng để diễn tả sự không cần thiết phải làm một việc gì đó: 'There is no need to print the photo yourself'."}
        ]
    },
    "76": {
        "exp": "Người nói thông báo thêm: 'All our frames come with standard glass, but for an extra twenty dollars, you can add an extended five-year damage warranty that covers accidental glass breakage' (Tất cả khung ảnh của chúng tôi đều đi kèm kính tiêu chuẩn, nhưng chỉ với thêm 20 đô la, bạn có thể bổ sung gói bảo hành hư hại mở rộng 5 năm chi trả cho trường hợp vô tình làm vỡ kính). Khoản phụ phí đi kèm là gói bảo hành -> Chọn (D) A warranty.",
        "vocab": [
            {"word": "warranty", "ipa": "/ˈwɒr.ən.ti/", "pos": "n", "meaning": "phiếu bảo hành, cam kết bảo hành", "example": "The television comes with a two-year manufacturer warranty."},
            {"word": "extended", "ipa": "/ɪkˈsten.dɪd/", "pos": "adj", "meaning": "mở rộng, kéo dài thời hạn", "example": "Customers can purchase an extended warranty for extra protection."}
        ],
        "collocations": [
            {"phrase": "damage warranty", "meaning": "bảo hành hư hại/hỏng hóc"},
            {"phrase": "for an extra fee", "meaning": "với một khoản phụ phí"}
        ],
        "grammar": [
            {"title": "Giới từ chỉ sự bổ sung 'for an extra + [fee/cost]'", "rule": "for an extra + amount", "analysis": "Diễn đạt việc trả thêm tiền để có thêm quyền lợi: 'for an extra twenty dollars, you can add...'."}
        ]
    },

    # Q77-Q79: Physical therapy training, activities, I must leave at noon
    "77": {
        "exp": "Người nói mở đầu buổi tập huấn: 'Welcome all to this week's training in our series of patient care programs. Our physical therapy center is known for the excellent care we provide to our patients. And that's because of you, our staff...' (Chào mừng tất cả các bạn đến với buổi tập huấn tuần này trong chuỗi chương trình chăm sóc người bệnh. Trung tâm vật lý trị liệu của chúng ta nổi tiếng vì sự chăm sóc tuyệt vời dành cho bệnh nhân. Và điều đó là nhờ có các bạn, đội ngũ nhân viên...). Người nghe là nhân viên chăm sóc y tế -> Chọn (B) Health-care staff.",
        "vocab": [
            {"word": "therapy", "ipa": "/ˈθer.ə.pi/", "pos": "n", "meaning": "liệu pháp điều trị, trị liệu phục hồi", "example": "Physical therapy assists patients in recovering joint mobility."},
            {"word": "patient", "ipa": "/ˈpeɪ.ʃənt/", "pos": "n", "meaning": "bệnh nhân, người bệnh", "example": "Nurses monitor outpatient vital signs every morning."}
        ],
        "collocations": [
            {"phrase": "health-care staff", "meaning": "đội ngũ nhân viên chăm sóc sức khỏe/y tế"},
            {"phrase": "physical therapy", "meaning": "vật lý trị liệu"}
        ],
        "grammar": [
            {"title": "Cấu trúc lời chào mở đầu cuộc họp/tập huấn", "rule": "Welcome (all) to + event/location", "analysis": "Thường chứa trực tiếp đối tượng tham gia và chủ đề sự kiện: 'Welcome all to this week's training in...'."}
        ]
    },
    "78": {
        "exp": "Người nói nêu nội dung chương trình: 'Instead of just listening to a lecture today, I've prepared several interactive role-playing activities so we can practice handling difficult patient situations' (Thay vì chỉ ngồi nghe giảng hôm nay, tôi đã chuẩn bị vài hoạt động tương tác đóng vai để chúng ta có thể thực hành xử lý các tình huống người bệnh khó tính). Người nói đã chuẩn bị các hoạt động thực hành -> Chọn (A) Activities.",
        "vocab": [
            {"word": "interactive", "ipa": "/ˌɪn.təˈræk.tɪv/", "pos": "adj", "meaning": "có tính tương tác qua lại", "example": "The workshop utilized interactive simulations to engage participants."},
            {"word": "role-playing", "ipa": "/ˈrəʊlˌpleɪ.ɪŋ/", "pos": "n", "meaning": "hoạt cảnh đóng vai thực hành", "example": "Customer service trainees practice role-playing challenging phone calls."}
        ],
        "collocations": [
            {"phrase": "interactive activities", "meaning": "các hoạt động có tính tương tác"},
            {"phrase": "prepare activities", "meaning": "chuẩn bị các hoạt động"}
        ],
        "grammar": [
            {"title": "Cụm từ chỉ sự thay thế 'Instead of + V-ing'", "rule": "Instead of + V-ing, S + V", "analysis": "'Instead of just listening to a lecture...' mang nghĩa 'thay vì chỉ lắng nghe bài giảng'."}
        ]
    },
    "79": {
        "exp": "Người nói thông báo: 'However, looking at the clock, I must leave at noon to attend an executive board meeting at regional headquarters' (Tuy nhiên, nhìn đồng hồ thì tôi bắt buộc phải rời đi lúc giữa trưa để tham dự cuộc họp hội đồng quản trị ở trụ sở vùng). Câu nói này ngụ ý vì phải về sớm nên một số nội dung tập huấn hôm nay sẽ không thể bao quát hết được -> Chọn (D) Some material will not be covered today.",
        "vocab": [
            {"word": "cover", "ipa": "/ˈkʌv.ər/", "pos": "v", "meaning": "bao quát, trình bày hết các chủ đề", "example": "The training seminar did not cover advanced financial forecasting."},
            {"word": "material", "ipa": "/məˈtɪə.ri.əl/", "pos": "n", "meaning": "tài liệu, nội dung học tập", "example": "Review all training materials prior to taking the certification exam."}
        ],
        "collocations": [
            {"phrase": "cover material", "meaning": "giảng dạy/bao quát hết tài liệu nội dung"},
            {"phrase": "executive board meeting", "meaning": "cuộc họp hội đồng điều hành/quản trị"}
        ],
        "grammar": [
            {"title": "Động từ khuyết thiếu chỉ sự bắt buộc 'must'", "rule": "S + must + V-bare", "analysis": "'I must leave at noon' nhấn mạnh tính chất bắt buộc của việc phải rời đi, dẫn tới hạn chế thời gian tập huấn."}
        ]
    },

    # Q80-Q82: Hoffman Oversized Haulers, truck drivers, flexible schedules, info
    "80": {
        "exp": "Mở đầu mẩu quảng cáo: 'Are you a certified commercial truck driver? Hoffman Oversized Haulers is currently looking for experienced truck drivers to join our team' (Bạn có phải là tài xế xe tải thương mại có chứng chỉ? Công ty Hoffman Oversized Haulers hiện đang tìm kiếm các tài xế xe tải giàu kinh nghiệm gia nhập đội ngũ của chúng tôi). Mục đích của mẩu quảng cáo là tuyển dụng nhân viên -> Chọn (D) To recruit employees.",
        "vocab": [
            {"word": "recruit", "ipa": "/rɪˈkruːt/", "pos": "v", "meaning": "tuyển dụng, chiêu mộ nhân sự", "example": "The tech firm plans to recruit fifty software engineers this quarter."},
            {"word": "commercial", "ipa": "/kəˈmɜː.ʃəl/", "pos": "adj", "meaning": "thương mại, chuyên chở hàng hóa", "example": "Drivers must possess a valid commercial operating license."}
        ],
        "collocations": [
            {"phrase": "recruit employees", "meaning": "tuyển dụng nhân viên"},
            {"phrase": "join our team", "meaning": "gia nhập đội ngũ của chúng tôi"}
        ],
        "grammar": [
            {"title": "Cấu trúc quảng cáo tuyển dụng với 'look for'", "rule": "be looking for + job titles + to join our team", "analysis": "Mẫu câu kinh điển trong các bài quảng cáo tuyển dụng nhằm thu hút ứng viên nộp hồ sơ."}
        ]
    },
    "81": {
        "exp": "Người nói chỉ ra lợi thế khác biệt của công ty: 'Unlike other shipping firms that mandate rigid 60-hour workweeks, we offer flexible schedules and let drivers choose their routes and shift preferences' (Không giống các hãng vận tải khác ép buộc tuần làm việc 60 tiếng cứng nhắc, chúng tôi cung cấp lịch trình linh hoạt và cho phép tài xế tự chọn lộ trình và ca làm mong muốn) -> Chọn (C) It offers flexible schedules.",
        "vocab": [
            {"word": "flexible", "ipa": "/ˈflek.sə.bəl/", "pos": "adj", "meaning": "linh hoạt, có thể tự do điều chỉnh", "example": "Remote work arrangements allow for flexible working hours."},
            {"word": "rigid", "ipa": "/ˈrɪdʒ.ɪd/", "pos": "adj", "meaning": "cứng nhắc, bất di bất dịch", "example": "The company dropped its rigid dress code in favor of casual wear."}
        ],
        "collocations": [
            {"phrase": "flexible schedule", "meaning": "lịch trình làm việc linh hoạt"},
            {"phrase": "shift preference", "meaning": "nguyện vọng đăng ký ca làm"}
        ],
        "grammar": [
            {"title": "Giới từ chỉ sự đối lập 'Unlike + Noun'", "rule": "Unlike A, B + verb...", "analysis": "'Unlike other shipping firms...' dùng để làm nổi bật sự vượt trội hoặc khác biệt của công ty so với đối thủ cạnh tranh."}
        ]
    },
    "82": {
        "exp": "Kết thúc bài quảng cáo, người nói kêu gọi: 'To learn more about competitive benefits and wage rates, visit our career portal at www.hoffmanhaulers.com/apply today' (Để tìm hiểu thêm về các chế độ đãi ngộ cạnh tranh và mức lương, hãy truy cập cổng thông tin nghề nghiệp của chúng tôi ngay hôm nay). Lời kêu gọi là tìm kiếm thêm thông tin -> Chọn (D) Get more information.",
        "vocab": [
            {"word": "competitive", "ipa": "/kəmˈpet.ɪ.tɪv/", "pos": "adj", "meaning": "có tính cạnh tranh, hấp dẫn trên thị trường", "example": "We offer competitive salaries and comprehensive health insurance."},
            {"word": "portal", "ipa": "/ˈpɔː.təl/", "pos": "n", "meaning": "cổng thông tin điện tử", "example": "Employees submit leave requests through the internal corporate portal."}
        ],
        "collocations": [
            {"phrase": "get more information", "meaning": "nhận thêm thông tin, tìm hiểu thêm"},
            {"phrase": "competitive benefits", "meaning": "chế độ đãi ngộ cạnh tranh"}
        ],
        "grammar": [
            {"title": "Cụm từ chỉ mục đích 'To learn more about...'", "rule": "To learn more about X, visit/call...", "analysis": "Mẫu câu Call-to-Action (kêu gọi hành động) ở phần kết bài quảng cáo để điều hướng người nghe tìm hiểu thông tin chi tiết."}
        ]
    },

    # Q83-Q85: Farmer's Table TV show, come early Wednesday, food festival
    "83": {
        "exp": "Người nói hào hứng thông báo: 'Hi, Genew. I have some exciting news. The Farmer's Table television program wants to feature our restaurant in an upcoming episode. They'll be coming on Wednesday to film everyone at work in the kitchen...' (Chào Genew. Tôi có vài tin vui đây. Chương trình truyền hình The Farmer's Table muốn đưa nhà hàng chúng ta lên sóng trong một tập sắp tới. Họ sẽ đến vào thứ Tư để quay cảnh mọi người làm việc trong bếp...). Tin nhắn nói về việc quay hình cho một chương trình truyền hình -> Chọn (B) Filming for a television show.",
        "vocab": [
            {"word": "feature", "ipa": "/ˈfiː.tʃər/", "pos": "v", "meaning": "đưa lên sóng, làm nổi bật, có sự tham gia của", "example": "The travel documentary will feature local street food artisans."},
            {"word": "episode", "ipa": "/ˈep.ɪ.səʊd/", "pos": "n", "meaning": "tập phim, số phát sóng của chương trình", "example": "The final episode attracted an audience of ten million viewers."}
        ],
        "collocations": [
            {"phrase": "film for a show", "meaning": "quay hình cho một chương trình"},
            {"phrase": "upcoming episode", "meaning": "tập phát sóng sắp tới"}
        ],
        "grammar": [
            {"title": "Động từ 'feature' chỉ việc giới thiệu, quảng bá", "rule": "S + feature + Object", "analysis": "'wants to feature our restaurant' mang nghĩa muốn chọn nhà hàng làm nhân vật/chủ đề chính trong chương trình."}
        ]
    },
    "84": {
        "exp": "Người nói yêu cầu người nghe vào thứ Tư: 'Since the camera crew arrives at 7 A.M., could you please come in an hour earlier than your normal shift to help prepare the prep stations?' (Vì đoàn quay phim sẽ tới lúc 7 giờ sáng, bạn có thể vui lòng đến sớm hơn ca làm bình thường một tiếng để giúp chuẩn bị các khu sơ chế không?). Yêu cầu là đến làm sớm -> Chọn (A) Come to work early.",
        "vocab": [
            {"word": "shift", "ipa": "/ʃɪft/", "pos": "n", "meaning": "ca làm việc", "example": "Factory workers rotate between morning and night shifts."},
            {"word": "crew", "ipa": "/kruː/", "pos": "n", "meaning": "đoàn làm phim, tổ công tác", "example": "The filming crew set up lighting and sound gear on location."}
        ],
        "collocations": [
            {"phrase": "come to work early", "meaning": "đến nơi làm việc sớm"},
            {"phrase": "camera crew", "meaning": "đoàn quay phim, tổ ghi hình"}
        ],
        "grammar": [
            {"title": "Yêu cầu lịch sự 'Could you please + V-bare?'", "rule": "Could you please + V-inf?", "analysis": "Cấu trúc câu nhờ vả, giao việc lịch sự trong môi trường làm việc: 'could you please come in an hour earlier...'."}
        ]
    },
    "85": {
        "exp": "Người nói chia sẻ lịch trình tuần sau: 'I won't be in the kitchen next week because I'll be traveling to Chicago to present our organic pastries at the National Food Festival' (Tuần tới tôi sẽ không có mặt ở bếp vì tôi sẽ đi Chicago để giới thiệu các món bánh nướng hữu cơ của chúng ta tại Lễ hội Ẩm thực Quốc gia). Địa điểm người nói sẽ tới là một lễ hội ẩm thực -> Chọn (A) To a food festival.",
        "vocab": [
            {"word": "festival", "ipa": "/ˈfes.tɪ.vəl/", "pos": "n", "meaning": "lễ hội, ngày hội văn hóa ẩm thực", "example": "The annual film festival attracts international directors and critics."},
            {"word": "pastry", "ipa": "/ˈpeɪ.stri/", "pos": "n", "meaning": "bánh ngọt, đồ nướng điểm tâm", "example": "The French bakery sells delicate fruit pastries and tarts."}
        ],
        "collocations": [
            {"phrase": "food festival", "meaning": "lễ hội ẩm thực"},
            {"phrase": "travel to a city", "meaning": "đi công tác/du lịch đến một thành phố"}
        ],
        "grammar": [
            {"title": "Thì tương lai tiếp diễn diễn tả lịch trình đã định (will be + V-ing)", "rule": "S + will be + V-ing", "analysis": "'I'll be traveling to Chicago' diễn đạt hành động sẽ đang diễn ra theo kế hoạch định sẵn trong tuần tới."}
        ]
    },

    # Q86-Q88: Channel 4 News, EV battery factory, community support, city hall images
    "86": {
        "exp": "Phóng viên truyền hình đưa tin: 'Rockville was recently chosen as the site of a multi-million dollar electric vehicle battery manufacturing plant...' (Rockville gần đây đã được chọn làm địa điểm xây dựng nhà máy sản xuất pin xe điện trị giá hàng triệu đô la...). 'manufacturing plant' chính là một nhà máy sản xuất -> Chọn (B) A factory.",
        "vocab": [
            {"word": "manufacturing", "ipa": "/ˌmæn.jʊˈfæk.tʃə.rɪŋ/", "pos": "n", "meaning": "ngành sản xuất chế tạo", "example": "Automation plays a critical role in modern automotive manufacturing."},
            {"word": "suburb", "ipa": "/ˈsʌb.ɜːb/", "pos": "n", "meaning": "khu vực ngoại ô, vùng ven đô", "example": "Many families prefer living in quiet residential suburbs."}
        ],
        "collocations": [
            {"phrase": "manufacturing plant", "meaning": "nhà máy chế tạo sản xuất"},
            {"phrase": "electric vehicle", "meaning": "xe điện, phương tiện chạy điện"}
        ],
        "grammar": [
            {"title": "Từ đồng nghĩa plant = factory", "rule": "Lexical equivalence", "analysis": "'manufacturing plant' trong bài nói được thay thế bằng danh từ tương đương 'factory' trong câu hỏi trắc nghiệm."}
        ]
    },
    "87": {
        "exp": "Phóng viên nhắc đến phiên điều trần công khai: 'During last night's city council public hearing, no one made any comments against the zoning approval' (Trong phiên điều trần công khai của hội đồng thành phố tối qua, không ai đưa ra bình luận phản đối nào đối với việc phê duyệt quy hoạch). Việc không ai phản đối chứng minh dự án nhận được sự đồng thuận, ủng hộ của cộng đồng -> Chọn (C) A project has community support.",
        "vocab": [
            {"word": "hearing", "ipa": "/ˈhɪə.rɪŋ/", "pos": "n", "meaning": "phiên điều trần công khai", "example": "Citizens expressed water quality concerns at the public hearing."},
            {"word": "approval", "ipa": "/əˈpruː.vəl/", "pos": "n", "meaning": "sự tán thành, phê chuẩn chính thức", "example": "The construction permit received final regulatory approval."}
        ],
        "collocations": [
            {"phrase": "community support", "meaning": "sự ủng hộ của cộng đồng dân cư"},
            {"phrase": "public hearing", "meaning": "phiên điều trần công khai"}
        ],
        "grammar": [
            {"title": "Suy luận logic từ phát ngôn phủ định", "rule": "Inference from double negative / lack of objection", "analysis": "'no one made any comments [against]' -> không ai phản đối đồng nghĩa với việc mọi người đồng thuận ủng hộ dự án."}
        ]
    },
    "88": {
        "exp": "Phóng viên hướng dẫn người dân: 'Starting tomorrow, residents can view architectural renderings and aerial site plans on display in the lobby of the city hall building' (Bắt đầu từ ngày mai, người dân có thể xem các bản vẽ phối cảnh kiến trúc và sơ đồ mặt bằng trên cao được trưng bày tại sảnh tòa nhà thị chính). 'renderings and aerial plans' là các bản vẽ phối cảnh, hình ảnh công trình -> Chọn (B) Some images.",
        "vocab": [
            {"word": "rendering", "ipa": "/ˈren.dər.ɪŋ/", "pos": "n", "meaning": "bản vẽ phối cảnh kiến trúc 3D", "example": "The architect revealed digital 3D renderings of the proposed airport."},
            {"word": "resident", "ipa": "/ˈrez.ɪ.dənt/", "pos": "n", "meaning": "cư dân, người dân sinh sống trong vùng", "example": "Local residents attended the town hall to discuss park upgrades."}
        ],
        "collocations": [
            {"phrase": "architectural rendering", "meaning": "bản vẽ phối cảnh kiến trúc"},
            {"phrase": "on display", "meaning": "được trưng bày công khai"}
        ],
        "grammar": [
            {"title": "Khái quát hóa từ vựng (renderings/plans -> images)", "rule": "Superordinate category noun", "analysis": "Danh từ bao quát 'images' (hình ảnh) được dùng để đại diện cho 'renderings and plans' (bản vẽ/hình ảnh thiết kế)."}
        ]
    },

    # Q89-Q91: Optimum Space Organizer, desk organizer, adjustable, call time limit
    "89": {
        "exp": "Mở đầu quảng cáo: 'Tired of losing things on your desk because it's too cluttered? If so, the Optimum Space Organizer is the perfect product for you...' (Bạn mệt mỏi vì thất lạc đồ đạc trên bàn làm việc do quá bừa bộn? Nếu vậy, Thiết bị sắp xếp Optimum Space chính là sản phẩm hoàn hảo cho bạn...). Sản phẩm được quảng cáo là đồ sắp xếp đồ đạc trên bàn làm việc -> Chọn (D) A desk organizer.",
        "vocab": [
            {"word": "organizer", "ipa": "/ˈɔː.ɡən.aɪ.zər/", "pos": "n", "meaning": "đồ sắp xếp dụng cụ, hộp đựng ngăn nắp", "example": "She purchased a mesh desk organizer for pens and memo pads."},
            {"word": "cluttered", "ipa": "/ˈklʌt.əd/", "pos": "adj", "meaning": "bừa bộn, lộn xộn ngổn ngang đồ đạc", "example": "A cluttered workspace often impairs mental concentration."}
        ],
        "collocations": [
            {"phrase": "desk organizer", "meaning": "khay/hộp sắp xếp đồ dùng trên bàn"},
            {"phrase": "cluttered desk", "meaning": "bàn làm việc bừa bộn"}
        ],
        "grammar": [
            {"title": "Cấu trúc mở đầu quảng cáo gợi vấn đề 'Tired of + V-ing?'", "rule": "Tired of + Noun / V-ing?", "analysis": "Mẫu câu hỏi tu từ đánh trúng tâm lý khó chịu của khách hàng trước khi đưa ra giải pháp sản phẩm."}
        ]
    },
    "90": {
        "exp": "Người nói nêu bật tính năng đặc biệt: 'What sets our organizer apart is its modular sliding compartments. You can effortlessly adjust the width and height of each section to accommodate tablets, notebooks, or office supplies' (Điểm khác biệt của sản phẩm chúng tôi là các ngăn trượt dạng mô-đun. Bạn có thể dễ dàng điều chỉnh chiều rộng và chiều cao từng ngăn để vừa máy tính bảng, sổ tay hoặc văn phòng phẩm). Tính năng nổi trội là có thể tùy chỉnh kích thước -> Chọn (B) It is adjustable.",
        "vocab": [
            {"word": "adjustable", "ipa": "/əˈdʒʌs.tə.bəl/", "pos": "adj", "meaning": "có thể điều chỉnh kích thước/độ cao", "example": "Ergonomic chairs feature fully adjustable armrests and lumbar support."},
            {"word": "compartment", "ipa": "/kəmˈpɑːt.mənt/", "pos": "n", "meaning": "ngăn chứa đồ, khoang để đồ", "example": "The briefcase has a padded compartment for laptops."}
        ],
        "collocations": [
            {"phrase": "easily adjustable", "meaning": "dễ dàng điều chỉnh được"},
            {"phrase": "sliding compartment", "meaning": "ngăn trượt linh hoạt"}
        ],
        "grammar": [
            {"title": "Mệnh đề nhấn mạnh đặc điểm: 'What sets X apart is...'", "rule": "What sets [noun] apart is + noun/clause", "analysis": "Cấu trúc dùng để khẳng định điểm độc đáo, nổi trội khác biệt nhất của một sản phẩm."}
        ]
    },
    "91": {
        "exp": "Người nói đưa ra ưu đãi có giới hạn thời gian: 'Call the toll-free number on your screen within the next 20 minutes, and we will cut twenty percent off your total purchase price' (Hãy gọi tới số miễn cước trên màn hình trong vòng 20 phút tới, và chúng tôi sẽ giảm ngay 20% trên tổng giá trị đơn hàng của bạn). Điều kiện để được giảm giá là gọi điện trong thời hạn quy định -> Chọn (A) By calling within a time limit.",
        "vocab": [
            {"word": "toll-free", "ipa": "/ˌtəʊlˈfriː/", "pos": "adj", "meaning": "miễn cước cuộc gọi", "example": "Customers can dial our toll-free support line anytime."},
            {"word": "purchase", "ipa": "/ˈpɜː.tʃəs/", "pos": "n", "meaning": "khoản mua sắm, giá trị đơn hàng", "example": "A valid receipt is required for all returns on recent purchases."}
        ],
        "collocations": [
            {"phrase": "within a time limit", "meaning": "trong giới hạn thời gian quy định"},
            {"phrase": "toll-free number", "meaning": "số điện thoại miễn cước"}
        ],
        "grammar": [
            {"title": "Cấu trúc câu điều kiện mệnh lệnh kết hợp 'and'", "rule": "Imperative + and + S + will + V-bare", "analysis": "'Call the toll-free number... and we will cut twenty percent off...' mang ý nghĩa điều kiện: 'Nếu bạn gọi... thì chúng tôi sẽ giảm...'."}
        ]
    },

    # Q92-Q94: Fabulous Foods podcast, showcase ingredients, order book, Rebecca Murray restaurant
    "92": {
        "exp": "Người dẫn chương trình podcast chia sẻ: 'Every week we discuss a different vegetable and ways to cook with it to maximize flavor' (Mỗi tuần chúng tôi thảo luận về một loại rau củ khác nhau và các phương pháp nấu nướng để tối đa hóa hương vị). Mục đích của podcast là giới thiệu từng loại nguyên liệu riêng lẻ -> Chọn (D) To showcase individual ingredients.",
        "vocab": [
            {"word": "ingredient", "ipa": "/ɪnˈɡriː.di.ənt/", "pos": "n", "meaning": "nguyên liệu nấu ăn, thành phần", "example": "Fresh culinary herbs are essential ingredients in Mediterranean cuisine."},
            {"word": "showcase", "ipa": "/ˈʃəʊ.keɪs/", "pos": "v, n", "meaning": "trưng bày, giới thiệu nổi bật", "example": "The food channel showcases regional delicacies from around the world."}
        ],
        "collocations": [
            {"phrase": "individual ingredients", "meaning": "từng nguyên liệu ẩm thực riêng lẻ"},
            {"phrase": "maximize flavor", "meaning": "tối đa hóa hương vị món ăn"}
        ],
        "grammar": [
            {"title": "Cấu trúc chỉ mục đích với 'ways to + V-inf'", "rule": "ways to + V-bare", "analysis": "'ways to cook with it to maximize flavor' - 'ways to V' diễn tả các cách thức, giải pháp thực hiện."}
        ]
    },
    "93": {
        "exp": "Người nói nhắc nhở về tập sách công thức nấu ăn đặc biệt: '...this product line will not be available for long, as only 500 copies were printed' (...dòng sản phẩm này sẽ không có sẵn lâu đâu, vì chỉ có 500 bản được in mà thôi). Người nói đưa ra câu này nhằm tạo sự cấp bách để khuyến khích khán thính giả nhanh chóng đặt mua sản phẩm -> Chọn (A) To encourage the listeners to place an order.",
        "vocab": [
            {"word": "encourage", "ipa": "/ɪnˈkʌr.ɪdʒ/", "pos": "v", "meaning": "khuyến khích, thúc giục hành động", "example": "Special promotional discounts encourage shoppers to place larger orders."},
            {"word": "available", "ipa": "/əˈveɪ.lə.bəl/", "pos": "adj", "meaning": "có sẵn, còn hàng để bán", "example": "Limited-edition prints are only available while supplies last."}
        ],
        "collocations": [
            {"phrase": "place an order", "meaning": "đặt mua hàng, gửi đơn đặt"},
            {"phrase": "available for long", "meaning": "có sẵn trong thời gian dài"}
        ],
        "grammar": [
            {"title": "Kỹ thuật tạo sự khan hiếm trong bán hàng (Scarcity Tactic)", "rule": "Create urgency to drive action", "analysis": "Câu nói 'will not be available for long' thúc giục người nghe phải đặt mua ngay lập tức kẻo hết hàng."}
        ]
    },
    "94": {
        "exp": "Người dẫn giới thiệu khách mời: 'Our guest chef today is Rebecca Murray, who recently celebrated the grand opening of her farm-to-table bistro in Seattle' (Đầu bếp khách mời của chúng ta hôm nay là Rebecca Murray, người vừa mới kỷ niệm ngày khai trương quán ăn ấm cúng phong cách từ nông trại tới bàn ăn tại Seattle). Rebecca Murray vừa mở một nhà hàng -> Chọn (C) She opened a restaurant.",
        "vocab": [
            {"word": "bistro", "ipa": "/ˈbiː.strəʊ/", "pos": "n", "meaning": "quán ăn nhỏ ấm cúng, nhà hàng mini", "example": "The downtown French bistro serves authentic regional onion soup."},
            {"word": "celebrate", "ipa": "/ˈsel.ə.breɪt/", "pos": "v", "meaning": "kỷ niệm, ăn mừng một sự kiện", "example": "The corporation celebrated twenty successful years in international trade."}
        ],
        "collocations": [
            {"phrase": "grand opening", "meaning": "lễ khai trương trọng thể"},
            {"phrase": "farm-to-table", "meaning": "từ nông trại đến bàn ăn (nguyên liệu tươi sạch)"}
        ],
        "grammar": [
            {"title": "Mệnh đề quan hệ không giới hạn với 'who'", "rule": "Name, who + verb...", "analysis": "Bổ sung thông tin về nghề nghiệp và thành tựu gần đây của một người cụ thể: 'Rebecca Murray, who recently celebrated...'."}
        ]
    },

    # Q95-Q97: Train station, construction noise, baggage service, Train 133 at 12:05 P.M.
    "95": {
        "exp": "Phát thanh viên tại nhà ga thông báo: 'Attention passengers. Renovation work to upgrade and modernize our train station is underway. We apologize for the inconvenience the construction noise may cause' (Xin quý hành khách chú ý. Công tác tu sửa nâng cấp và hiện đại hóa nhà ga của chúng ta đang được tiến hành. Chúng tôi thành thật xin lỗi vì sự bất tiện mà tiếng ồn công trường có thể gây ra). Người nói xin lỗi vì tiếng ồn thi công tại nhà ga -> Chọn (A) There is construction noise at the station.",
        "vocab": [
            {"word": "renovation", "ipa": "/ˌren.əˈveɪ.ʃən/", "pos": "n", "meaning": "sự tu sửa, cải tạo công trình", "example": "The terminal renovation will add six new passenger boarding gates."},
            {"word": "inconvenience", "ipa": "/ˌɪn.kənˈviː.ni.əns/", "pos": "n", "meaning": "sự bất tiện, phiền toái", "example": "We sincerely apologize for any travel inconvenience caused by delays."}
        ],
        "collocations": [
            {"phrase": "construction noise", "meaning": "tiếng ồn thi công công trường"},
            {"phrase": "apologize for the inconvenience", "meaning": "xin lỗi vì sự bất tiện"}
        ],
        "grammar": [
            {"title": "Mẫu câu xin lỗi trang trọng trong thông báo công cộng", "rule": "We apologize for + Noun phrase", "analysis": "Mẫu câu quy chuẩn tại các sân bay, nhà ga khi công trình gây phiền hà cho hành khách: 'We apologize for the inconvenience...'."}
        ]
    },
    "96": {
        "exp": "Người nói lưu ý hành khách: 'Because elevator number 2 near the boarding platform is temporarily out of service, passengers requiring assistance carrying heavy luggage or oversized bags should see a station agent at Counter 4' (Do thang máy số 2 gần sân ga tạm thời ngừng hoạt động, hành khách cần trợ giúp mang vác hành lý nặng hoặc túi quá khổ xin hãy gặp nhân viên nhà ga tại Quầy 4). Mục đích gặp nhân viên là yêu cầu hỗ trợ hành lý -> Chọn (B) To request baggage service.",
        "vocab": [
            {"word": "luggage", "ipa": "/ˈlʌɡ.ɪdʒ/", "pos": "n", "meaning": "hành lý xách tay, vali", "example": "Airline passengers may check two pieces of heavy luggage for free."},
            {"word": "assistance", "ipa": "/əˈsɪs.təns/", "pos": "n", "meaning": "sự trợ giúp, hỗ trợ kỹ thuật hoặc sức người", "example": "Senior travelers can request boarding assistance upon check-in."}
        ],
        "collocations": [
            {"phrase": "baggage service", "meaning": "dịch vụ hỗ trợ hành lý"},
            {"phrase": "out of service", "meaning": "ngừng hoạt động, đang hỏng"}
        ],
        "grammar": [
            {"title": "Rút gọn mệnh đề quan hệ chủ động với hiện tại phân từ (V-ing)", "rule": "passengers requiring assistance = passengers who require assistance", "analysis": "'passengers requiring assistance' rút gọn mệnh đề quan hệ xác định."}
        ]
    },
    "97": {
        "exp": "Người phát thanh nói: 'Train 133 bound for Hartford is departing on schedule from Track 3' (Chuyến tàu 133 đi Hartford đang khởi hành đúng giờ từ Đường ray số 3). Nhìn vào bảng điện tử hành trình trên hình ảnh đồ họa: Dòng thông tin 'Train 133 - Next Stop: Meriden' ghi rõ giờ đến dự kiến là 12:05 P.M. -> Chọn (B) At 12:05 P.M.",
        "vocab": [
            {"word": "scheduled", "ipa": "/ˈʃedʒ.uːld/", "pos": "adj", "meaning": "được lên lịch, theo thời gian biểu", "example": "The aircraft is scheduled to land at Frankfurt airport at dawn."},
            {"word": "bound", "ipa": "/baʊnd/", "pos": "adj", "meaning": "hướng về, đi về phía", "example": "All passengers on trains bound for Chicago must board at Gate B."}
        ],
        "collocations": [
            {"phrase": "on schedule", "meaning": "đúng lịch trình, đúng giờ"},
            {"phrase": "next stop", "meaning": "trạm dừng/ga dừng kế tiếp"}
        ],
        "grammar": [
            {"title": "Đối chiếu thông tin bài nghe với bảng giờ tàu (Timetable Graphic)", "rule": "Listen for train number and match arrival time", "analysis": "Bắt số hiệu chuyến tàu 'Train 133' trong audio và đọc cột thời gian đến 'Arrival Time' tương ứng."}
        ]
    },

    # Q98-Q100: Carmen Salazar airport press conference, reporters, Selca Air delay, look at model
    "98": {
        "exp": "Người nói mở đầu cuộc họp báo: 'Hello everyone. I'm Carmen Salazar, the airport operations director, and I wanted to thank you for attending this press conference' (Xin chào mọi người. Tôi là Carmen Salazar, giám đốc vận hành sân bay, và tôi muốn cảm ơn các bạn đã tham dự buổi họp báo này). Người tham dự một buổi họp báo (press conference) chính là các phóng viên báo đài -> Chọn (C) News reporters.",
        "vocab": [
            {"word": "conference", "ipa": "/ˈkɒn.fər.əns/", "pos": "n", "meaning": "hội nghị, buổi họp báo", "example": "Journalists gathered at the city center for the official press conference."},
            {"word": "operations", "ipa": "/ˌɒp.ərˈeɪ.ʃənz/", "pos": "n", "meaning": "hoạt động vận hành, điều hành", "example": "The director oversees day-to-day flight operations at the hub."}
        ],
        "collocations": [
            {"phrase": "press conference", "meaning": "cuộc họp báo"},
            {"phrase": "news reporters", "meaning": "các phóng viên báo chí, nhà báo"}
        ],
        "grammar": [
            {"title": "Suy luận đối tượng thính giả qua thể loại sự kiện", "rule": "Event genre indicates audience identity", "analysis": "'press conference' (buổi họp báo) quy định người nghe là phóng viên, ký giả thông tấn (news reporters)."}
        ]
    },
    "99": {
        "exp": "Người nói cập nhật: 'Work on Concourse C is running approximately four weeks behind schedule due to supply chain shortages, affecting its primary airline tenant' (Công trình tại Nhà ga C đang bị chậm tiến độ khoảng 4 tuần do đứt gãy chuỗi cung ứng vật tư, ảnh hưởng trực tiếp tới hãng hàng không thuê chính tại đây). Nhìn vào sơ đồ bố trí nhà ga trong hình ảnh đồ họa: Hãng hàng không đặt tại Concourse C là Selca Air -> Chọn (A) Selca Air.",
        "vocab": [
            {"word": "concourse", "ipa": "/ˈkɒŋ.kɔːs/", "pos": "n", "meaning": "nhà ga nối tiếp, sảnh chờ sân bay", "example": "Passengers proceeded through security to boarding Concourse B."},
            {"word": "tenant", "ipa": "/ˈten.ənt/", "pos": "n", "meaning": "bên thuê địa điểm kinh doanh, người thuê", "example": "The shopping mall houses eighty retail and culinary tenants."}
        ],
        "collocations": [
            {"phrase": "behind schedule", "meaning": "chậm hơn so với kế hoạch"},
            {"phrase": "primary tenant", "meaning": "bên thuê chính, khách thuê chủ chốt"}
        ],
        "grammar": [
            {"title": "Đối chiếu tên khu vực với nhà mạng thuê", "rule": "Cross-reference location code (Concourse C) to brand logo/name", "analysis": "Nghe tên khu vực bị trễ hạn 'Concourse C' và dò tìm trên sơ đồ để thấy hãng bay đại diện là Selca Air."}
        ]
    },
    "100": {
        "exp": "Kết thúc bài phát biểu, giám đốc mời: 'Before we take questions, I invite all of you to gather around the table in the corner to look at the three-dimensional scale model of the completed international terminal' (Trước khi chúng ta bước vào phần trả lời câu hỏi, tôi mời tất cả các bạn tập trung quanh chiếc bàn ở góc phòng để chiêm ngưỡng mô hình thu nhỏ 3D của nhà ga quốc tế khi hoàn thành). Lời mời là xem mô hình thu nhỏ công trình -> Chọn (B) Look at a model.",
        "vocab": [
            {"word": "model", "ipa": "/ˈmɒd.əl/", "pos": "n", "meaning": "mô hình thu nhỏ của công trình kiến trúc", "example": "Architects presented a detailed acrylic scale model of the museum."},
            {"word": "scale", "ipa": "/skeɪl/", "pos": "n", "meaning": "tỷ lệ xích, quy mô thu nhỏ", "example": "The scaled replica represents one percent of the actual stadium size."}
        ],
        "collocations": [
            {"phrase": "look at a model", "meaning": "ngắm nhìn/xem một mô hình kiến trúc"},
            {"phrase": "scale model", "meaning": "mô hình thu nhỏ theo tỷ lệ"}
        ],
        "grammar": [
            {"title": "Cấu trúc mời mọc trang trọng 'invite someone to do something'", "rule": "S + invite + Object + to V-inf", "analysis": "Mẫu câu lịch sự: 'I invite all of you to gather around the table... to look at...'."}
        ]
    }
}

with open('scratch/t2_p4_enrichment.json', 'w', encoding='utf-8') as f:
    json.dump(p4_enrichment, f, ensure_ascii=False, indent=2)

print(f"Enriched {len(p4_enrichment)} questions for Test 2 Part 4 successfully!")
