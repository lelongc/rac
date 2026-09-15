# scratch/enrich_t3_p6.py: In-depth enrichment for Test 3 RC Part 6 (Q131 - Q146)
import json

p6_enrichment = {}

# Passage 1: 131 - 134 (Florence Shawn's retirement & leadership transition)
p6_enrichment[131] = {
    "exp": "Căn cứ ngữ cảnh bức thư: Bà Florence Shawn chuẩn bị nghỉ hưu và công ty đang sắp xếp nhân sự kế nhiệm. Câu văn viết: 'In preparation for this [131], Ms. Shawn has been working closely with our executive team...' (Để chuẩn bị cho sự thay đổi này, bà Shawn đã làm việc chặt chẽ với ban điều hành...). Danh từ 'change' (sự thay đổi/chuyển giao nhân sự) là từ duy nhất phù hợp để chỉ việc bà Shawn rời nhiệm sở. Phương án (C) 'change' là đáp án đúng. Các phương án: (A) 'difference' (sự khác biệt), (B) 'strategy' (chiến lược), (D) 'practice' (thực hành, thông lệ).",
    "vocab": [
        {"word": "transition", "ipa": "/trænˈzɪʃ.ən/", "pos": "n", "meaning": "sự chuyển tiếp, quá trình chuyển giao", "example": "The executive smooths the management transition."},
        {"word": "change", "ipa": "/tʃeɪndʒ/", "pos": "n", "meaning": "sự thay đổi, biến chuyển", "example": "Embrace technological change to maintain competitiveness."},
        {"word": "executive", "ipa": "/ɪɡˈzek.jə.tɪv/", "pos": "adj, n", "meaning": "thuộc ban điều hành; cán bộ cấp cao", "example": "The executive committee approved the reorganization."}
    ],
    "collocations": [{"phrase": "in preparation for", "meaning": "để chuẩn bị cho"}, {"phrase": "work closely with", "meaning": "làm việc chặt chẽ với"}],
    "grammar": [{"title": "Cụm từ chỉ mục đích 'In preparation for + Noun'", "rule": "In preparation for + Noun Phrase (this change), S + V", "content": "Dùng để diễn giải tiền đề chuẩn bị cho một sự kiện hoặc bước chuyển đổi quan trọng trong doanh nghiệp."}]
}

p6_enrichment[132] = {
    "exp": "Căn cứ ngữ pháp và dấu hiệu thời gian: Trong câu có cụm 'Over the past six months' (Trong suốt sáu tháng qua), đây là dấu hiệu đặc trưng của thì Hiện tại hoàn thành hoặc Hiện tại hoàn thành tiếp diễn: 'Ms. Shawn [132] her successor, David Cho...' (Bà Shawn đã và đang trực tiếp hướng dẫn người kế nhiệm mình, David Cho...). Do hành động hướng dẫn kéo dài liên tục từ quá khứ đến hiện tại và còn tiếp diễn, ta chọn (D) 'has been mentoring'. Các phương án: (A) 'mentors' (hiện tại đơn), (B) 'is mentoring' (hiện tại tiếp diễn), (C) 'will mentor' (tương lai đơn).",
    "vocab": [
        {"word": "mentor", "ipa": "/ˈmen.tɔːr/", "pos": "v, n", "meaning": "hướng dẫn, cố vấn chuyên môn; người cố vấn", "example": "Senior partners mentor junior associates throughout the year."},
        {"word": "successor", "ipa": "/səkˈses.ər/", "pos": "n", "meaning": "người kế nhiệm, người tiếp quản vị trí", "example": "The board unanimously named her as his successor."},
        {"word": "closely", "ipa": "/ˈkləʊs.li/", "pos": "adv", "meaning": "một cách chặt chẽ, sát sao", "example": "The engineers collaborated closely with the quality team."}
    ],
    "collocations": [{"phrase": "mentor a successor", "meaning": "hướng dẫn người kế nhiệm"}, {"phrase": "over the past six months", "meaning": "trong suốt sáu tháng qua"}],
    "grammar": [{"title": "Thì Hiện tại hoàn thành tiếp diễn với 'Over the past...'", "rule": "Over the past + time period + S + have/has been + V-ing", "content": "Nhấn mạnh tính liên tục và không gián đoạn của hành động đào tạo, bàn giao công việc."}]
}

p6_enrichment[133] = {
    "exp": "Căn cứ ngữ cảnh: Bức thư thông báo ngày làm việc cuối cùng của bà Shawn trước khi về hưu: 'Ms. Shawn's [133] day in the office will be March 31' (Ngày làm việc cuối cùng của bà Shawn tại văn phòng sẽ là ngày 31 tháng 3). Cụm từ chuẩn xác là 'one's last day' (ngày làm việc cuối cùng). Phương án (A) 'last' là đáp án đúng. Các phương án: (B) 'original' (nguyên bản), (C) 'flexible' (linh hoạt), (D) 'alternate' (luân phiên, thay thế).",
    "vocab": [
        {"word": "last day", "ipa": "/lɑːst deɪ/", "pos": "n phr", "meaning": "ngày làm việc cuối cùng trước khi nghỉ", "example": "Colleagues brought cake on her last day at the company."},
        {"word": "retire", "ipa": "/rɪˈtaɪər/", "pos": "v", "meaning": "nghỉ hưu", "example": "After four decades in banking, he decided to retire."},
        {"word": "dedication", "ipa": "/ˌded.ɪˈkeɪ.ʃən/", "pos": "n", "meaning": "sự cống hiến, tận tụy", "example": "We applaud her exceptional dedication to public service."}
    ],
    "collocations": [{"phrase": "last day in the office", "meaning": "ngày làm việc cuối cùng ở cơ quan"}, {"phrase": "congratulate someone on", "meaning": "chúc mừng ai về điều gì"}],
    "grammar": [{"title": "Cụm từ cố định 'last day'", "rule": "Possessive + last day (her last day in the office)", "content": "Cách diễn đạt tiêu chuẩn trong văn bản nội bộ khi thông báo nhân sự rời công ty hoặc về hưu."}]
}

p6_enrichment[134] = {
    "exp": "Căn cứ tính mạch lạc của văn bản: Câu trước đó thông báo: 'A farewell gathering will be held in the main cafeteria on Friday at 3:00 P.M.' (Một buổi gặp mặt chia tay sẽ được tổ chức tại căng tin chính vào thứ Sáu lúc 3 giờ chiều). Câu điền vào chỗ trống [134] phải là lời mời gọi mọi người đến tham dự sự kiện chia tay này. Phương án (B) 'We hope that you can all attend to wish her well.' (Chúng tôi hy vọng tất cả các bạn có thể tham dự để gửi lời chúc tốt đẹp đến bà ấy) kết nối logic hoàn hảo. Các phương án khác lạc đề về tuyển dụng hay dự án mới.",
    "vocab": [
        {"word": "farewell gathering", "ipa": "/ˌfeəˈwel ˈɡæð.ər.ɪŋ/", "pos": "n", "meaning": "buổi họp mặt chia tay", "example": "Staff organized a heartfelt farewell gathering for the director."},
        {"word": "wish well", "ipa": "/wɪʃ wel/", "pos": "v phr", "meaning": "gửi lời chúc may mắn, tốt lành", "example": "Teammates signed a card to wish her well in retirement."},
        {"word": "attend", "ipa": "/əˈtend/", "pos": "v", "meaning": "tham dự, có mặt", "example": "All employees are invited to attend the awards ceremony."}
    ],
    "collocations": [{"phrase": "farewell gathering", "meaning": "buổi gặp mặt chia tay"}, {"phrase": "wish someone well", "meaning": "chúc ai điều tốt lành"}],
    "grammar": [{"title": "Kỹ thuật điền câu (Sentence Insertion) dựa trên quan hệ nối tiếp", "rule": "Thông báo thời gian/địa điểm sự kiện -> Lời mời tham gia (We hope you can all attend)", "content": "Câu điền vào phải liên kết trực tiếp với đại từ và sự kiện được nêu ngay ở câu đứng trước."}]
}

# Passage 2: 135 - 138 (Lovitt Real Estate advertisement)
p6_enrichment[135] = {
    "exp": "Căn cứ cấu trúc câu: 'Whether you are a first-time home [135] or looking to relocate...' (Dù bạn là người sở hữu nhà lần đầu hay đang tìm cách chuyển chỗ ở...). Trước chỗ trống là cụm 'first-time home' (nhà ở lần đầu), ta cần danh từ chỉ người 'homeowner / home owner' (chủ sở hữu nhà). Phương án (C) 'owner' là đáp án đúng. Các phương án: (A) 'own' (động từ), (B) 'owned' (V-ed), (D) 'owning' (V-ing).",
    "vocab": [
        {"word": "homeowner", "ipa": "/ˈhəʊmˌəʊ.nər/", "pos": "n", "meaning": "chủ nhà, người sở hữu nhà ở", "example": "First-time homeowners qualify for property tax incentives."},
        {"word": "real estate", "ipa": "/ˈrɪəl ɪˌsteɪt/", "pos": "n", "meaning": "bất động sản, địa ốc", "example": "Investing in commercial real estate yields reliable returns."},
        {"word": "relocate", "ipa": "/ˌriː.ləʊˈkeɪt/", "pos": "v", "meaning": "chuyển chỗ ở, di dời", "example": "Families relocate to suburban districts for better schools."}
    ],
    "collocations": [{"phrase": "first-time home owner", "meaning": "người mua nhà lần đầu"}, {"phrase": "real estate agent", "meaning": "môi giới bất động sản"}],
    "grammar": [{"title": "Cấu trúc tương phản lựa chọn 'Whether... or...'", "rule": "Whether S + be + Noun, or + V-ing...", "content": "Bao quát toàn bộ các nhóm đối tượng khách hàng tiềm năng mà đại lý bất động sản hướng đến."}]
}

p6_enrichment[136] = {
    "exp": "Căn cứ cấu trúc giới từ: Động từ đi kèm giới từ 'in': 'specialize in something' (chuyên về lĩnh vực gì). Câu văn viết: 'Our dedicated agents [136] in residential properties across the province' (Các đại lý tận tâm của chúng tôi chuyên về bất động sản nhà ở trên toàn tỉnh). Phương án (B) 'specialize' là đáp án chính xác. Các phương án: (A) 'practice' (không đi với in để chỉ chuyên môn kinh doanh), (C) 'report' (báo cáo, đi với on/to), (D) 'purchase' (mua hàng, là ngoại động từ có tân ngữ trực tiếp).",
    "vocab": [
        {"word": "specialize", "ipa": "/ˈspeʃ.əl.aɪz/", "pos": "v", "meaning": "chuyên về, hoạt động chuyên môn hóa trong", "example": "The law firm specializes in intellectual property disputes."},
        {"word": "residential", "ipa": "/ˌrez.ɪˈden.ʃəl/", "pos": "adj", "meaning": "thuộc về nhà ở, khu dân cư", "example": "The zoning ordinance protects quiet residential neighborhoods."},
        {"word": "dedicated", "ipa": "/ˈded.ɪ.keɪ.tɪd/", "pos": "adj", "meaning": "tận tụy, chuyên tâm", "example": "Our dedicated support staff assists patrons around the clock."}
    ],
    "collocations": [{"phrase": "specialize in", "meaning": "chuyên về lĩnh vực"}, {"phrase": "residential property", "meaning": "bất động sản nhà ở"}],
    "grammar": [{"title": "Cụm động từ đi với giới từ 'specialize in'", "rule": "specialize + in + Field / Noun Phrase", "content": "Đặc biệt phổ biến trong TOEIC Reading Part 6 khi giới thiệu thế mạnh chuyên môn của doanh nghiệp."}]
}

p6_enrichment[137] = {
    "exp": "Căn cứ tính mạch lạc: Câu đứng trước khẳng định: 'Our agents have an unmatched knowledge of local neighborhoods and school districts.' (Các đại lý của chúng tôi có hiểu biết vô song về các khu dân cư và học khu địa phương). Câu điền vào vị trí [137] cần giải thích nguyên nhân tại sao họ lại am hiểu tường tận như vậy: 'That is because they live in the communities they serve.' (Đó là bởi vì họ sinh sống ngay trong chính các cộng đồng mà họ phục vụ). Phương án (B) là đáp án đúng. Các phương án khác về đưa đón học sinh hay ngân hàng đều hoàn toàn lạc đề.",
    "vocab": [
        {"word": "unmatched", "ipa": "/ʌnˈmætʃt/", "pos": "adj", "meaning": "vô song, không đối thủ nào sánh kịp", "example": "The consultancy possesses unmatched expertise in trade law."},
        {"word": "neighborhood", "ipa": "/ˈneɪ.bə.hʊd/", "pos": "n", "meaning": "khu phố lân cận, xóm giềng", "example": "The suburban neighborhood features wide tree-lined sidewalks."},
        {"word": "community", "ipa": "/kəˈmjuː.nə.ti/", "pos": "n", "meaning": "cộng đồng dân cư", "example": "Agents take pride in supporting their local communities."}
    ],
    "collocations": [{"phrase": "unmatched knowledge", "meaning": "sự hiểu biết không ai sánh bằng"}, {"phrase": "communities they serve", "meaning": "cộng đồng mà họ phục vụ"}],
    "grammar": [{"title": "Mệnh đề nguyên nhân giải thích 'That is because + Clause'", "rule": "Assertion (sự khẳng định) -> That is because + Reason Clause", "content": "'That is because' dùng để liên kết và giải thích lý do sâu xa cho nhận định vừa được đưa ra trước đó."}]
}

p6_enrichment[138] = {
    "exp": "Căn cứ cụm giới từ: 'working [138] your goals' (hướng về phía / nỗ lực đạt được mục tiêu của bạn). Giới từ 'toward' đi với danh từ 'goals' tạo thành cụm từ mang ý nghĩa 'hướng tới các mục tiêu'. Câu văn viết: 'Let us guide you toward finding your dream home' (Hãy để chúng tôi dẫn lối cho bạn hướng tới việc tìm thấy ngôi nhà mơ ước). Phương án (A) 'toward' là đáp án đúng. Các phương án: (B) 'fixing' (dạng V-ing), (C) 'because' (liên từ nối mệnh đề), (D) 'along' (dọc theo).",
    "vocab": [
        {"word": "toward", "ipa": "/təˈwɔːd/", "pos": "prep", "meaning": "hướng về, hướng tới (mục tiêu)", "example": "Every donation moves us closer toward our funding goal."},
        {"word": "dream home", "ipa": "/driːm həʊm/", "pos": "n", "meaning": "ngôi nhà mơ ước", "example": "Couples work diligently to finance their dream home."},
        {"word": "guide", "ipa": "/ɡaɪd/", "pos": "v", "meaning": "chỉ dẫn, dẫn đường", "example": "Experienced brokers guide clients through complex escrow contracts."}
    ],
    "collocations": [{"phrase": "guide someone toward", "meaning": "dẫn lối ai hướng tới điều gì"}, {"phrase": "dream home", "meaning": "ngôi nhà trong mơ"}],
    "grammar": [{"title": "Giới từ chỉ phương hướng và mục tiêu 'toward'", "rule": "guide / work / strive + toward + Noun Phrase", "content": "Diễn tả xu hướng tiến đến một đích đến lý tưởng hoặc mục đích trong tương lai."}]
}

# Passage 3: 139 - 142 (Distributing Your Savings seminar intro)
p6_enrichment[139] = {
    "exp": "Căn cứ cấu trúc ngữ pháp: 'This slide [139] is the third installment in our series...' (Buổi thuyết trình bằng slide này là phần thứ ba trong chuỗi hội thảo của chúng tôi...). Đứng sau chỉ từ 'This' và danh từ phụ 'slide' làm thuộc từ, ta cần danh từ chính làm chủ ngữ cho động từ 'is'. Phương án (C) 'presentation' (bài thuyết trình, phần trình bày) là danh từ chính xác. Cụm 'slide presentation' là cụm danh từ ghép chuẩn. Các phương án: (A) 'presenting' (V-ing), (B) 'presents' (động từ ngôi 3 số ít), (D) 'presented' (V-ed).",
    "vocab": [
        {"word": "presentation", "ipa": "/ˌprez.ənˈteɪ.ʃən/", "pos": "n", "meaning": "bài thuyết trình, buổi trình chiếu", "example": "The keynote presentation captivated the entire audience."},
        {"word": "installment", "ipa": "/ɪnˈstɔːl.mənt/", "pos": "n", "meaning": "phần/kỳ trong một chuỗi, kỳ trả góp", "example": "The final installment of the documentary airs tonight."},
        {"word": "savings", "ipa": "/ˈseɪ.vɪŋz/", "pos": "n pl", "meaning": "tiền tiết kiệm", "example": "Deposit a portion of monthly earnings into personal savings."}
    ],
    "collocations": [{"phrase": "slide presentation", "meaning": "bài trình chiếu bằng slide"}, {"phrase": "installment in our series", "meaning": "phần trong chuỗi chương trình"}],
    "grammar": [{"title": "Danh từ ghép (Compound Noun) 'slide presentation'", "rule": "Noun (slide) + Head Noun (presentation) + Verb (is)", "content": "Danh từ 'slide' bổ nghĩa cho 'presentation' tạo nên cụm từ chỉ buổi thuyết trình sử dụng slide chiếu."}]
}

p6_enrichment[140] = {
    "exp": "Căn cứ tính mạch lạc: Phần giới thiệu hội thảo vừa nêu đây là buổi thứ ba trong chuỗi chuyên đề tài chính. Câu điền vào vị trí [140] cần tóm lược mục đích thiết kế của cả chuỗi hội thảo: 'The series is designed to help you make informed financial decisions.' (Chuỗi bài giảng này được thiết kế để giúp quý vị đưa ra các quyết định tài chính sáng suốt). Phương án (B) hoàn toàn ăn khớp và liền mạch. Các phương án khác về điền mẫu đơn hay khám phá văn phòng đều lạc đề ở phần mở đầu slide.",
    "vocab": [
        {"word": "informed decision", "ipa": "/ɪnˈfɔːmd dɪˈsɪʒ.ən/", "pos": "n phr", "meaning": "quyết định sáng suốt, dựa trên thông tin đầy đủ", "example": "Review analysts' reports to make informed investment decisions."},
        {"word": "financial", "ipa": "/faɪˈnæn.ʃəl/", "pos": "adj", "meaning": "thuộc về tài chính, tiền tệ", "example": "Seek professional financial advice prior to early retirement."},
        {"word": "designed to", "ipa": "/dɪˈzaɪnd tuː/", "pos": "adj phr", "meaning": "được thiết kế nhằm mục đích", "example": "The software is designed to streamline inventory tracking."}
    ],
    "collocations": [{"phrase": "make an informed decision", "meaning": "đưa ra quyết định sáng suốt"}, {"phrase": "be designed to", "meaning": "được thiết kế để"}]
}

p6_enrichment[141] = {
    "exp": "Căn cứ ngữ nghĩa và danh từ theo sau: 'generating [141] income during retirement' (tạo ra thu nhập bổ sung trong thời kỳ nghỉ hưu). Sau khi về hưu, nguồn thu nhập chính từ lương bị ngừng, người về hưu cần nguồn thu nhập thêm/phụ trợ. Tính từ (C) 'supplemental' (bổ sung, phụ trợ) là từ chuẩn xác nhất: 'supplemental income' (thu nhập bổ sung). Các phương án: (A) 'regional' (khu vực), (B) 'expensive' (đắt đỏ), (D) 'playful' (vui đùa, nghịch ngợm).",
    "vocab": [
        {"word": "supplemental", "ipa": "/ˌsʌp.lɪˈmen.təl/", "pos": "adj", "meaning": "bổ sung, phụ thêm", "example": "Part-time consulting provides supplemental income for retirees."},
        {"word": "retirement", "ipa": "/rɪˈtaɪə.mənt/", "pos": "n", "meaning": "sự nghỉ hưu", "example": "Diversified investments ensure financial security in retirement."},
        {"word": "generate", "ipa": "/ˈdʒen.ə.reɪt/", "pos": "v", "meaning": "tạo ra, sinh ra (doanh thu/thu nhập)", "example": "Rental properties generate steady passive income."}
    ],
    "collocations": [{"phrase": "supplemental income", "meaning": "thu nhập bổ sung"}, {"phrase": "generate income", "meaning": "tạo ra nguồn thu nhập"}],
    "grammar": [{"title": "Cụm từ cố định trong kinh tế 'supplemental income'", "rule": "Adjective (supplemental) + Noun (income)", "content": "Chỉ các dòng tiền kiếm thêm ngoài tiền lương hưu cơ bản hoặc trợ cấp nhà nước."}]
}

p6_enrichment[142] = {
    "exp": "Căn cứ ngữ nghĩa câu kết của bài giảng: 'We strongly recommend [142] a certified financial planner before making irreversible portfolio changes' (Chúng tôi đặc biệt khuyến nghị việc tham khảo ý kiến chuyên gia hoạch định tài chính có chứng chỉ trước khi thực hiện các thay đổi không thể đảo ngược). Động từ 'recommend + V-ing / Noun' mang nghĩa khuyến nghị làm việc gì; 'consult a professional' (tham vấn chuyên gia). Phương án (A) 'consulting' là đáp án đúng. Các phương án: (B) 'prescribing' (kê đơn thuốc), (C) 'listing' (liệt kê), (D) 'following' (theo sau).",
    "vocab": [
        {"word": "consult", "ipa": "/kənˈsʌlt/", "pos": "v", "meaning": "tham khảo ý kiến, hội ý chuyên gia", "example": "Consult an accountant regarding business tax exemptions."},
        {"word": "certified", "ipa": "/ˈsɜː.tɪ.faɪd/", "pos": "adj", "meaning": "được cấp chứng chỉ hành nghề chính thức", "example": "Hire a certified public accountant to audit the ledger."},
        {"word": "portfolio", "ipa": "/pɔːtˈfəʊ.li.əʊ/", "pos": "n", "meaning": "danh mục đầu tư tài chính", "example": "Diversify your investment portfolio across stocks and bonds."}
    ],
    "collocations": [{"phrase": "consult a financial planner", "meaning": "tham khảo ý kiến chuyên gia tài chính"}, {"phrase": "certified planner", "meaning": "chuyên viên có chứng chỉ"}],
    "grammar": [{"title": "Động từ 'recommend' đi kèm danh động từ V-ing", "rule": "recommend + V-ing (recommend consulting)", "content": "Khi không có tân ngữ chỉ người đi kèm, 'recommend' trực tiếp kết hợp với danh động từ V-ing."}]
}

# Passage 4: 143 - 146 (Silas Laveau's email regarding workshops)
p6_enrichment[143] = {
    "exp": "Căn cứ mạch lạc đoạn mở đầu bức thư: Người viết mở đầu: 'Thank you for the update on the upcoming professional development workshops.' (Cảm ơn bạn đã cập nhật về các buổi hội thảo phát triển chuyên môn sắp tới). Vị trí [143] nằm ở câu kế tiếp, nêu lý do người viết gửi email này: 'I would like to make a suggestion on this topic.' (Tôi muốn đưa ra một đề xuất về chủ đề này). Phương án (C) tạo sự kết nối tự nhiên và dẫn dắt người đọc vào nội dung đề xuất chi tiết ở các câu sau. Các phương án khác mang tính phàn nàn thời gian hay tự đề cử là không phù hợp.",
    "vocab": [
        {"word": "suggestion", "ipa": "/səˈdʒes.tʃən/", "pos": "n", "meaning": "lời đề xuất, ý kiến gợi ý", "example": "The manager welcomed practical suggestions for saving energy."},
        {"word": "professional development", "ipa": "/prəˌfeʃ.ən.əl dɪˈvel.əp.mənt/", "pos": "n phr", "meaning": "phát triển chuyên môn, bồi dưỡng nghiệp vụ", "example": "The company allocates funds for employee professional development."},
        {"word": "topic", "ipa": "/ˈtɒp.ɪk/", "pos": "n", "meaning": "chủ đề thảo luận", "example": "Brainstorming sessions cover innovative marketing topics."}
    ],
    "collocations": [{"phrase": "make a suggestion", "meaning": "đưa ra lời đề xuất"}, {"phrase": "professional development", "meaning": "phát triển năng lực nghề nghiệp"}],
    "grammar": [{"title": "Cấu trúc đề xuất lịch thiệp 'would like to make a suggestion'", "rule": "S + would like to + V-inf", "content": "Cách diễn đạt trang trọng và chuẩn mực khi cấp dưới đóng góp ý kiến mang tính xây dựng cho cấp trên."}]
}

p6_enrichment[144] = {
    "exp": "Căn cứ sắc thái bổn phận và khuyến nghị: Người viết đưa ra lập luận rằng công ty nên tổ chức thêm lớp về phân tích dữ liệu: 'Given the rapid digitalization of our workflow, our department [144] hands-on workshops in data analytics' (Trước tình hình số hóa nhanh chóng quy trình làm việc của chúng ta, phòng ban của chúng ta nên cung cấp các buổi thực hành thực tế về phân tích dữ liệu). Cấu trúc 'should be offering' diễn tả một việc lẽ ra nên được tiến hành ngay từ thời điểm này. Phương án (D) 'should be offering' là đáp án đúng. Các phương án: (A) 'will offer' (tương lai đơn, thiếu sắc thái đề xuất), (B) 'have offered' (hiện tại hoàn thành), (C) 'were offering' (quá khứ tiếp diễn).",
    "vocab": [
        {"word": "hands-on", "ipa": "/ˌhændzˈɒn/", "pos": "adj", "meaning": "thực hành thực tế, trực quan", "example": "The IT seminar emphasizes hands-on software configuration."},
        {"word": "data analytics", "ipa": "/ˈdeɪ.tə æn.əˈlɪt.ɪks/", "pos": "n pl", "meaning": "phân tích dữ liệu", "example": "Proficiency in data analytics accelerates business reporting."},
        {"word": "workflow", "ipa": "/ˈwɜːk.fləʊ/", "pos": "n", "meaning": "quy trình luồng công việc", "example": "Automated tools optimize editorial review workflows."}
    ],
    "collocations": [{"phrase": "hands-on workshops", "meaning": "buổi hội thảo thực hành thực tế"}, {"phrase": "data analytics", "meaning": "phân tích dữ liệu"}],
    "grammar": [{"title": "Động từ khiếm khuyết 'should' kết hợp tiếp diễn 'be V-ing'", "rule": "S + should + be + V-ing", "content": "Nhấn mạnh tính cấp thiết và phù hợp của một hoạt động lẽ ra cần đang được triển khai."}]
}

p6_enrichment[145] = {
    "exp": "Căn cứ từ nối liên kết logic: Câu văn viết: '[145], almost every team member now works with spreadsheet automation on a daily basis' (Rốt cuộc thì / Xét cho cùng thì hầu như mọi thành viên trong nhóm hiện nay đều làm việc với tính năng tự động hóa bảng tính hàng ngày). Cụm từ 'After all' (Rốt cuộc, xét cho cùng) được dùng để đưa ra một sự thật hiển nhiên củng cố cho đề xuất trước đó. Phương án (A) 'After all' là đáp án chính xác. Các phương án: (B) 'By the way' (nhân tiện, chuyển đề tài), (C) 'In the meantime' (trong lúc đó), (D) 'On the other hand' (mặt khác, chỉ sự đối lập).",
    "vocab": [
        {"word": "after all", "ipa": "/ˈɑːf.tər ɔːl/", "pos": "adv phr", "meaning": "rốt cuộc, xét cho cùng thì", "example": "We should approve the budget; after all, sales grew steadily."},
        {"word": "spreadsheet", "ipa": "/ˈspred.ʃiːt/", "pos": "n", "meaning": "bảng tính điện tử (Excel/Sheets)", "example": "Consolidate sales figures into a unified spreadsheet."},
        {"word": "automation", "ipa": "/ˌɔː.təˈmeɪ.ʃən/", "pos": "n", "meaning": "sự tự động hóa", "example": "Office automation eliminates tedious manual data transcription."}
    ],
    "collocations": [{"phrase": "after all", "meaning": "xét cho cùng"}, {"phrase": "on a daily basis", "meaning": "trên cơ sở hàng ngày"}],
    "grammar": [{"title": "Liên từ giải thích bổ trợ 'After all'", "rule": "After all, + Clause (đưa ra luận cứ không thể chối cãi)", "content": "'After all' dùng ở đầu câu để nhắc nhở người đọc về một thực tế khách quan ủng hộ cho ý kiến của tác giả."}]
}

p6_enrichment[146] = {
    "exp": "Căn cứ tính từ đi với danh từ 'training': 'I believe such a workshop would be immensely [146] to both new and veteran employees' (Tôi tin rằng một buổi tập huấn như vậy sẽ vô cùng hữu ích cho cả nhân viên mới lẫn nhân viên kỳ cựu). Phương án (A) 'useful' (hữu ích, bổ ích) phù hợp nhất với mục đích cải thiện kỹ năng. Các phương án khác: (B) 'eventful' (có nhiều sự kiện ly kỳ), (C) 'profitable' (sinh lời tài chính), (D) 'comfortable' (thoải mái, tiện nghi).",
    "vocab": [
        {"word": "immensely", "ipa": "/ɪˈmens.li/", "pos": "adv", "meaning": "vô cùng, hết sức", "example": "The mentorship program proved immensely beneficial to recruits."},
        {"word": "useful", "ipa": "/ˈjuːs.fəl/", "pos": "adj", "meaning": "hữu ích, thiết thực", "example": "The keyboard shortcuts guide is very useful for beginners."},
        {"word": "veteran", "ipa": "/ˈvet.ər.ən/", "pos": "adj, n", "meaning": "kỳ cựu, giàu kinh nghiệm", "example": "Veteran sales representatives mentor newer team associates."}
    ],
    "collocations": [{"phrase": "immensely useful", "meaning": "vô cùng hữu ích"}, {"phrase": "veteran employees", "meaning": "những nhân viên kỳ cựu"}],
    "grammar": [{"title": "Cấu trúc tính từ bổ nghĩa sau động từ 'would be'", "rule": "would be + Adverb (immensely) + Adjective (useful)", "content": "Trạng từ mức độ đứng trước tính từ để gia tăng sức thuyết phục cho đề xuất cá nhân."}]
}

with open('scratch/p6_q131_q146_part.json', 'w', encoding='utf-8') as f:
    json.dump(p6_enrichment, f, ensure_ascii=False, indent=2)
print("Saved Part 6 Q131-Q146 successfully!")
