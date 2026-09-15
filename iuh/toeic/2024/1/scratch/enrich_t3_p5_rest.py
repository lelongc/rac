# scratch/enrich_t3_p5_rest.py: Enrichment for Test 3 RC Part 5 (Q111 - Q130)
import json

p5_rest = {}

p5_rest[111] = {
    "exp": "Cấu trúc: Đứng sau mạo từ 'an' và tính từ 'extended' (được mở rộng, gia hạn) cần một danh từ số ít làm tân ngữ cho động từ 'include'. Cụm danh từ cố định: 'an extended warranty' (chế độ bảo hành mở rộng). Phương án (D) 'warranty' (giấy bảo hành, cam kết bảo hành) là đáp án chính xác. Các phương án: (A) 'warrant' (lệnh, sự chứng thực), (B) 'warranted' (V-ed), (C) 'warranting' (V-ing). Dịch câu: Các dòng xe Maihama bao gồm gói bảo hành mở rộng để chi trả cho các sửa chữa động cơ.",
    "vocab": [
        {"word": "warranty", "ipa": "/ˈwɒr.ən.ti/", "pos": "n", "meaning": "phiếu bảo hành, cam kết bảo hành", "example": "The refrigerator comes with a two-year manufacturer warranty."},
        {"word": "extended", "ipa": "/ɪkˈsten.dɪd/", "pos": "adj", "meaning": "được kéo dài, mở rộng (thời hạn)", "example": "Customers can purchase an extended warranty for laptops."},
        {"word": "repair", "ipa": "/rɪˈpeər/", "pos": "n", "meaning": "việc sửa chữa hư hỏng", "example": "The warranty covers parts and labor for major engine repairs."}
    ],
    "collocations": [{"phrase": "extended warranty", "meaning": "bảo hành mở rộng"}, {"phrase": "engine repairs", "meaning": "sửa chữa động cơ"}],
    "grammar": [{"title": "Cụm danh từ với phân từ quá khứ làm tính từ", "rule": "an + V-ed/adj (extended) + Noun (warranty)", "content": "'Extended' đóng vai trò là tính từ mô tả tính chất gia hạn thêm của danh từ chính 'warranty'."}]
}

p5_rest[112] = {
    "exp": "Cấu trúc: Đứng sau mạo từ 'an' và trước danh từ 'collection' (bộ sưu tập) cần một tính từ bắt đầu bằng nguyên âm để bổ nghĩa. 'An impressive collection' (một bộ sưu tập ấn tượng/đáng ngưỡng mộ) là cách kết hợp tự nhiên trong văn phong quảng bá. Phương án (C) 'impressive' là đáp án đúng. Các phương án: (A) 'impress' (động từ), (B) 'impressing' (V-ing), (D) 'impressively' (trạng từ). Dịch câu: Trang web mới của khách sạn sở hữu một bộ sưu tập ấn tượng gồm các hình ảnh chất lượng cao.",
    "vocab": [
        {"word": "impressive", "ipa": "/ɪmˈpres.ɪv/", "pos": "adj", "meaning": "ấn tượng, đáng nể", "example": "The marketing candidate demonstrated an impressive track record."},
        {"word": "collection", "ipa": "/kəˈlek.ʃən/", "pos": "n", "meaning": "bộ sưu tập, tập hợp ảnh/tài liệu", "example": "The gallery houses an impressive collection of modern sculptures."},
        {"word": "feature", "ipa": "/ˈfiː.tʃər/", "pos": "v", "meaning": "nổi bật với, có tính năng chính là", "example": "The luxury sedan features leather upholstery and GPS."}
    ],
    "collocations": [{"phrase": "impressive collection", "meaning": "bộ sưu tập ấn tượng"}, {"phrase": "high-quality images", "meaning": "hình ảnh chất lượng cao"}],
    "grammar": [{"title": "Vị trí tính từ đứng trước danh từ với mạo từ 'an'", "rule": "an + Adjective (vowel sound: impressive) + Noun (collection)", "content": "Mạo từ 'an' đi kèm tính từ bắt đầu bằng nguyên âm /ɪ/ bổ nghĩa cho danh từ đếm được số ít."}]
}

p5_rest[113] = {
    "exp": "Cấu trúc: Chỗ trống đứng giữa chủ ngữ 'we' và động từ chính 'thank you' (cảm ơn quý vị), do đó cần một trạng từ chỉ cách thức (adverb of manner) để bổ nghĩa cho động từ 'thank'. Phương án (C) 'sincerely' (một cách chân thành) là đáp án đúng. Cụm 'sincerely thank someone' thường xuyên xuất hiện trong các thư tín cảm ơn đối tác. Các phương án: (A) 'sincere' (tính từ), (B) 'sincerity' (danh từ), (D) 'most sincere' (dạng so sánh nhất của tính từ). Dịch câu: Thay mặt mọi người tại Ngân hàng Uniontown, chúng tôi chân thành cảm ơn quý khách vì đã tiếp tục ủng hộ dịch vụ của chúng tôi.",
    "vocab": [
        {"word": "sincerely", "ipa": "/sɪnˈsɪə.li/", "pos": "adv", "meaning": "một cách chân thành, thật lòng", "example": "We sincerely appreciate your patience during the system upgrade."},
        {"word": "patronage", "ipa": "/ˈpæt.rə.nɪdʒ/", "pos": "n", "meaning": "sự lui tới mua sắm, sự ủng hộ của khách hàng thân thiết", "example": "Thank you for your valued patronage over the past decade."},
        {"word": "on behalf of", "ipa": "/ɒn bɪˈhɑːf əv/", "pos": "prep phr", "meaning": "thay mặt cho, đại diện cho", "example": "On behalf of the board, I welcome you to the firm."}
    ],
    "collocations": [{"phrase": "sincerely thank", "meaning": "chân thành cảm ơn"}, {"phrase": "continued patronage", "meaning": "sự ủng hộ liên tục của khách hàng"}],
    "grammar": [{"title": "Vị trí trạng từ đứng giữa Chủ ngữ và Động từ chính", "rule": "Subject + Adverb of manner (sincerely) + Main Verb (thank)", "content": "Trạng từ có thể đặt ngay trước động từ thường để nhấn mạnh mức độ và thái độ của người nói."}]
}

p5_rest[114] = {
    "exp": "Cấu trúc: Cấu trúc thể bị động 'is + Adverb + damaged' (bị hư hại do vô tình). Đứng giữa trợ động từ 'is' và quá khứ phân từ 'damaged' cần một trạng từ bổ nghĩa. Phương án (D) 'accidentally' (một cách tình cờ/vô ý) phù hợp hoàn hảo về ngữ pháp và ngữ nghĩa. Các phương án: (A) 'accidental' (tính từ), (B) 'accident' (danh từ), (C) 'accidents' (danh từ số nhiều). Dịch câu: Thiết bị dễ vỡ phải được cất giữ ở một vị trí an toàn để không có vật gì bị hư hại do vô ý.",
    "vocab": [
        {"word": "fragile", "ipa": "/ˈfrædʒ.aɪl/", "pos": "adj", "meaning": "dễ vỡ, mỏng manh", "example": "Mark the packaging clearly with 'Fragile - Handle with Care'."},
        {"word": "accidentally", "ipa": "/ˌæk.sɪˈden.təl.i/", "pos": "adv", "meaning": "vô tình, ngoài ý muốn", "example": "Important financial records were accidentally deleted from the server."},
        {"word": "secure", "ipa": "/sɪˈkjʊər/", "pos": "adj", "meaning": "an toàn, kiên cố", "example": "Store sensitive files in a secure filing cabinet."}
    ],
    "collocations": [{"phrase": "fragile equipment", "meaning": "thiết bị dễ vỡ"}, {"phrase": "accidentally damaged", "meaning": "bị hư hại do vô tình"}],
    "grammar": [{"title": "Trạng từ đứng giữa trợ động từ 'be' và phân từ hai 'V3/ed'", "rule": "be + Adverb (accidentally) + V3/ed (damaged)", "content": "Vị trí xen giữa của trạng từ giúp làm rõ phương thức hoặc hoàn cảnh diễn ra của hành động bị động."}]
}

p5_rest[115] = {
    "exp": "Cấu trúc: Cụm từ phủ định 'will not arrive... until after' (sẽ không đến cho tới sau khi...). Cấu trúc 'not... until...' (không làm gì cho đến tận khi...) là mẫu câu kinh điển trong TOEIC. Phương án (A) 'until' là đáp án đúng. Các phương án: (B) 'sooner' (so sánh hơn, đi với than), (C) 'meanwhile' (trạng từ liên kết, không nối cụm), (D) 'except' (ngoại trừ, không hợp nghĩa). Dịch câu: Cô Sampson sẽ không đến hội nghị cho tới tận sau khi bài thuyết trình của nhóm chúng ta kết thúc.",
    "vocab": [
        {"word": "until", "ipa": "/ənˈtɪl/", "pos": "prep, conj", "meaning": "cho đến tận khi", "example": "The store will not open until 9:00 A.M."},
        {"word": "convention", "ipa": "/kənˈven.ʃən/", "pos": "n", "meaning": "hội nghị lớn, đại hội", "example": "Over 2,000 delegates attended the annual medical convention."},
        {"word": "presentation", "ipa": "/ˌprez.ənˈteɪ.ʃən/", "pos": "n", "meaning": "bài thuyết trình, phần trình bày", "example": "Her slide presentation captivated the prospective investors."}
    ],
    "collocations": [{"phrase": "not... until after", "meaning": "không... cho tới tận sau khi"}, {"phrase": "team's presentation", "meaning": "bài thuyết trình của nhóm"}],
    "grammar": [{"title": "Cấu trúc phủ định đi với 'until' (Not... until)", "rule": "S + will not + V + until + Time Expression", "content": "Dùng để nhấn mạnh một sự việc chỉ thực sự bắt đầu hoặc xảy ra sau một mốc thời gian hay sự kiện nhất định."}]
}

p5_rest[116] = {
    "exp": "Cấu trúc: Giới từ chỉ nơi chốn 'held in the park' (được tổ chức tại công viên). Đối với địa điểm có ranh giới không gian cụ thể như công viên (the park), ta dùng giới từ (A) 'in'. Các phương án: (B) 'by' (bởi/cạnh), (C) 'as' (như là), (D) 'down' (xuống dưới). Dịch câu: Buổi dã ngoại cộng đồng sẽ được tổ chức tại công viên phía sau Thư viện Công cộng Seltzer.",
    "vocab": [
        {"word": "community", "ipa": "/kəˈmjuː.nə.ti/", "pos": "n", "meaning": "cộng đồng dân cư", "example": "The festival brings together the whole local community."},
        {"word": "picnic", "ipa": "/ˈpɪk.nɪk/", "pos": "n", "meaning": "buổi dã ngoại ngoài trời", "example": "Staff enjoyed a relaxing picnic by the lakeside."},
        {"word": "hold", "ipa": "/həʊld/", "pos": "v", "meaning": "tổ chức (sự kiện, cuộc họp)", "example": "The annual shareholders meeting will be held in London."}
    ],
    "collocations": [{"phrase": "community picnic", "meaning": "buổi dã ngoại cộng đồng"}, {"phrase": "be held in the park", "meaning": "được tổ chức tại công viên"}],
    "grammar": [{"title": "Giới từ chỉ địa điểm không gian mở 'in'", "rule": "be held + in + the park / city / room", "content": "Dùng 'in' trước các địa danh có khuôn viên xác định (công viên, sân vận động, khu vực quảng trường)."}]
}

p5_rest[117] = {
    "exp": "Cấu trúc: Câu có chủ ngữ 'The new hires' (những nhân viên mới được tuyển dụng), trạng từ chỉ thời gian tương lai 'on May 10 at 9:00 A.M.'. Câu đang thiếu vị ngữ chính. Ta cần một động từ chia thì tương lai hoặc mang tính chỉ dẫn bổn phận. Phương án (B) 'should report' (cần phải trình diện/có mặt) phù hợp hoàn hảo về mặt ngữ pháp. Các phương án: (A) 'reporting' (dạng V-ing thiếu trợ động từ), (C) 'reportedly' (trạng từ), (D) 'reports' (danh từ số nhiều/động từ số ít). Dịch câu: Các nhân sự mới tuyển dụng cần có mặt tại buổi định hướng vào ngày 10 tháng 5 lúc 9 giờ sáng.",
    "vocab": [
        {"word": "new hire", "ipa": "/njuː ˈhaɪər/", "pos": "n", "meaning": "nhân viên mới được tuyển dụng", "example": "New hires undergo a rigorous two-week orientation."},
        {"word": "orientation", "ipa": "/ˌɔː.ri.enˈteɪ.ʃən/", "pos": "n", "meaning": "buổi định hướng, làm quen công việc", "example": "The orientation program covers company policies and benefits."},
        {"word": "report", "ipa": "/rɪˈpɔːt/", "pos": "v", "meaning": "trình diện, có mặt báo cáo nhiệm vụ", "example": "Technicians must report to site headquarters by 8:00 A.M."}
    ],
    "collocations": [{"phrase": "new hires", "meaning": "nhân sự mới tuyển"}, {"phrase": "report for an orientation", "meaning": "trình diện tại buổi định hướng"}],
    "grammar": [{"title": "Động từ khiếm khuyết 'should' chỉ bổn phận hướng dẫn", "rule": "Subject + should + V-bare (should report)", "content": "Được sử dụng trong các thông báo hành chính để đưa ra yêu cầu hoặc chỉ dẫn lịch sự cho nhân viên."}]
}

p5_rest[118] = {
    "exp": "Cấu trúc: Đứng giữa chủ ngữ 'the receptionist' và động từ quá khứ đơn 'offered' cần một trạng từ chỉ cách thức bổ nghĩa: 'promptly offered him a seat' (nhanh chóng/ngay lập tức mời ông ấy ngồi). Phương án (A) 'promptly' (ngay lập tức, kịp thời) là đáp án đúng. Các phương án: (B) 'prompt' (tính từ/động từ), (C) 'promptness' (danh từ), (D) 'prompts' (danh từ số nhiều). Dịch câu: Khi ông Young bước đến quầy lễ tân, nhân viên tiếp tân đã nhanh chóng mời ông một chỗ ngồi trong phòng chờ.",
    "vocab": [
        {"word": "receptionist", "ipa": "/rɪˈsep.ʃən.ɪst/", "pos": "n", "meaning": "nhân viên tiếp tân", "example": "The receptionist greeted visitors with a courteous smile."},
        {"word": "promptly", "ipa": "/ˈprɒmpt.li/", "pos": "adv", "meaning": "ngay lập tức, nhanh chóng không chậm trễ", "example": "Customer service agents respond promptly to client queries."},
        {"word": "waiting room", "ipa": "/ˈweɪ.tɪŋ ruːm/", "pos": "n", "meaning": "phòng chờ", "example": "Magazines and complimentary water are provided in the waiting room."}
    ],
    "collocations": [{"phrase": "promptly offer", "meaning": "nhanh chóng đưa ra/mời"}, {"phrase": "in the waiting room", "meaning": "trong phòng chờ"}],
    "grammar": [{"title": "Trạng từ đứng trước động từ quá khứ đơn để nhấn mạnh tính phản xạ", "rule": "Subject + Adverb (promptly) + Verb (offered) + Object", "content": "Bổ sung ý nghĩa về sự chuyên nghiệp và tốc độ phản ứng nhanh nhẹn của nhân viên phục vụ."}]
}

p5_rest[119] = {
    "exp": "Cấu trúc: Mệnh đề danh ngữ sau liên từ 'that' đang thiếu chủ ngữ đứng trước vị ngữ 'was the best design...'. Chủ ngữ này cần thay thế cho 'thiết kế của họ' (their design). Đại từ sở hữu (possessive pronoun) thay thế cho 'tính từ sở hữu + danh từ' chính là (C) 'theirs' (= their design). Các phương án: (A) 'they' (đại từ nhân xưng chủ ngữ, chỉ người, không hòa hợp với 'was the best design'), (B) 'them' (đại từ tân ngữ), (D) 'their' (tính từ sở hữu, bắt buộc phải có danh từ đi sau). Dịch câu: Các thành viên của nhóm tiếp thị Marvale khẳng định rằng mẫu thiết kế của họ là mẫu đẹp nhất cho logo mới của công ty.",
    "vocab": [
        {"word": "corporate logo", "ipa": "/ˈkɔː.pər.ət ˈləʊ.ɡəʊ/", "pos": "n", "meaning": "logo thương hiệu công ty", "example": "The designer revamped the corporate logo with vibrant gradients."},
        {"word": "claim", "ipa": "/kleɪm/", "pos": "v", "meaning": "khẳng định, tuyên bố quả quyết", "example": "Researchers claim that the new battery extends vehicle range."},
        {"word": "theirs", "ipa": "/ðeəz/", "pos": "pron", "meaning": "cái của họ (đại từ sở hữu)", "example": "Our proposal was rejected, but theirs was approved."}
    ],
    "collocations": [{"phrase": "corporate logo", "meaning": "biểu trưng công ty"}, {"phrase": "marketing team", "meaning": "nhóm tiếp thị"}],
    "grammar": [{"title": "Đại từ sở hữu làm chủ ngữ (Possessive Pronouns)", "rule": "Possessive Pronoun (theirs = their design) + Verb", "content": "Dùng đại từ sở hữu (theirs, ours, mine, yours, his, hers) để tránh lặp lại danh từ đã được nhắc tới trước đó."}]
}

p5_rest[120] = {
    "exp": "Cấu trúc: Cụm từ rút gọn chỉ ngoại trừ hoặc không bao gồm chi phí 'not including tax' (chưa bao gồm thuế). 'Including' là một giới từ/phân từ mang nghĩa 'bao gồm'. Cụm 'not including + Noun' thường dùng trên bảng giá niêm yết thương mại. Phương án (D) 'including' là đáp án chính xác. Các phương án: (A) 'includes' (động từ chia số ít), (B) 'included' (V-ed), (C) 'inclusion' (danh từ). Dịch câu: Máy quay video Kitsuna mới hiện đang được giảm giá với giá 375 USD, chưa bao gồm thuế.",
    "vocab": [
        {"word": "on sale", "ipa": "/ɒn seɪl/", "pos": "idiom", "meaning": "đang được giảm giá", "example": "Winter coats are currently on sale at 40% off."},
        {"word": "including", "ipa": "/ɪnˈkluː.dɪŋ/", "pos": "prep", "meaning": "bao gồm cả", "example": "The ticket price is $50, not including processing fees."},
        {"word": "tax", "ipa": "/tæks/", "pos": "n", "meaning": "thuế giá trị gia tăng, thuế bán hàng", "example": "Sales tax is calculated at checkout based on local regulations."}
    ],
    "collocations": [{"phrase": "not including tax", "meaning": "chưa tính thuế"}, {"phrase": "on sale for", "meaning": "đang giảm giá với mức..."}],
    "grammar": [{"title": "Cụm phân từ rút gọn mang chức năng giới từ 'including'", "rule": "Amount + (not) including + Noun (tax/shipping)", "content": "Dùng 'including' hoặc 'not including' để chỉ rõ các khoản phụ phí có hay không nằm trong giá niêm yết."}]
}

p5_rest[121] = {
    "exp": "Cấu trúc: Cấu trúc thể bị động 'be required to do something' (được yêu cầu/bắt buộc phải làm gì). Sau động từ 'are', ta cần quá khứ phân từ (D) 'required' để tạo thành cấu trúc quy định bổn phận. Các phương án: (A) 'require' (động từ nguyên mẫu), (B) 'requiring' (V-ing), (C) 'requirement' (danh từ). Dịch câu: Tất cả các cộng sự viên được yêu cầu phải tuân thủ các quy trình vận hành tiêu chuẩn được nêu trong sổ tay nhân viên.",
    "vocab": [
        {"word": "require", "ipa": "/rɪˈkwaɪər/", "pos": "v", "meaning": "đòi hỏi, yêu cầu bắt buộc", "example": "Safety regulations require all workers to wear protective goggles."},
        {"word": "standard operating procedure", "ipa": "/ˈstæn.dəd ˌɒp.ər.eɪ.tɪŋ prəˈsiː.dʒər/", "pos": "n", "meaning": "quy trình vận hành tiêu chuẩn (SOP)", "example": "Document standard operating procedures in the factory handbook."},
        {"word": "handbook", "ipa": "/ˈhænd.bʊk/", "pos": "n", "meaning": "sổ tay hướng dẫn nội bộ", "example": "Review the employee handbook for leave entitlement guidelines."}
    ],
    "collocations": [{"phrase": "be required to + V", "meaning": "bị bắt buộc/được yêu cầu làm gì"}, {"phrase": "standard operating procedure", "meaning": "quy trình thao tác chuẩn"}],
    "grammar": [{"title": "Cấu trúc bị động thể hiện nghĩa vụ 'be required to V'", "rule": "S + be + required / requested / expected + to-V", "content": "Cấu trúc chuẩn mực diễn tả quy chế bắt buộc trong các văn bản và thông báo nội quy doanh nghiệp."}]
}

p5_rest[122] = {
    "exp": "Cấu trúc: Cụm so sánh nhất với mạo từ/tính từ sở hữu 'its largest expansion so far' (đợt mở rộng lớn nhất của hãng cho đến nay). Cụm từ 'so far' (cho tới nay) là dấu hiệu điển hình của cấp so sánh nhất. Sau tính từ sở hữu 'its' và trước danh từ 'expansion', ta cần dạng so sánh nhất (D) 'largest'. Các phương án: (A) 'largely' (trạng từ), (B) 'large' (tính từ nguyên cấp), (C) 'larger' (so sánh hơn). Dịch câu: Tháng này, Nhà xuất bản Framley đang bắt tay vào đợt mở rộng quy mô lớn nhất của mình cho đến nay.",
    "vocab": [
        {"word": "expansion", "ipa": "/ɪkˈspæn.ʃən/", "pos": "n", "meaning": "sự mở rộng quy mô kinh doanh", "example": "The company financed a nationwide retail expansion."},
        {"word": "embark on", "ipa": "/ɪmˈbɑːk ɒn/", "pos": "phr v", "meaning": "bắt tay vào, khởi xướng (kế hoạch/hành trình mới)", "example": "The firm will embark on a multi-million dollar modernization project."},
        {"word": "publishing house", "ipa": "/ˈpʌb.lɪ.ʃɪŋ haʊs/", "pos": "n", "meaning": "nhà xuất bản", "example": "The publishing house distributes academic textbooks globally."}
    ],
    "collocations": [{"phrase": "embark on an expansion", "meaning": "bắt tay vào đợt mở rộng"}, {"phrase": "so far", "meaning": "cho đến thời điểm này"}],
    "grammar": [{"title": "Cấu trúc so sánh nhất đi với 'so far'", "rule": "Possessive (its) + Adj-est (largest) + Noun + so far", "content": "'So far' nhấn mạnh mức độ cao nhất đạt được tính đến thời điểm hiện tại."}]
}

p5_rest[123] = {
    "exp": "Cấu trúc: Đứng giữa cụm chủ ngữ 'Matricks Technology's software developers' và động từ chia thì quá khứ đơn 'released' cần một trạng từ chỉ thời gian/kết quả (adverb of time/completion) để bổ nghĩa: 'finally released a top-quality product' (cuối cùng đã phát hành sản phẩm đỉnh cao). Phương án (C) 'finally' là đáp án đúng. Các phương án: (A) 'final' (tính từ), (B) 'finalize' (động từ), (D) 'finality' (danh từ). Dịch câu: Sau nhiều tháng hợp tác, các nhà phát triển phần mềm của Matricks Technology cuối cùng đã cho ra mắt một sản phẩm chất lượng hàng đầu.",
    "vocab": [
        {"word": "finally", "ipa": "/ˈfaɪ.nəl.i/", "pos": "adv", "meaning": "cuối cùng thì, rốt cuộc", "example": "After lengthy negotiations, the parties finally inked the contract."},
        {"word": "collaboration", "ipa": "/kəˌlæb.əˈreɪ.ʃən/", "pos": "n", "meaning": "sự cộng tác, hợp tác làm việc", "example": "Cross-departmental collaboration accelerated prototype testing."},
        {"word": "release", "ipa": "/rɪˈliːs/", "pos": "v", "meaning": "phát hành, tung ra thị trường", "example": "The software studio released the patch to resolve server lag."}
    ],
    "collocations": [{"phrase": "finally release", "meaning": "cuối cùng đã phát hành"}, {"phrase": "top-quality product", "meaning": "sản phẩm chất lượng hàng đầu"}],
    "grammar": [{"title": "Vị trí trạng từ chỉ kết quả 'finally' trước động từ chính", "rule": "Subject + finally + Main Verb (released)", "content": "Diễn đạt một kết quả mong đợi đạt được sau một quãng thời gian dài nỗ lực làm việc."}]
}

p5_rest[124] = {
    "exp": "Cấu trúc: Đứng sau giới từ 'for' trong cụm 'allow for...' cần một danh từ hoặc danh động từ: 'allow for reentry into the venue' (cho phép việc vào lại địa điểm). Phương án (B) 'reentry' (sự quay trở lại, sự vào lại) là danh từ đúng. Các phương án: (A) 'reentering' (danh động từ, nhưng tiếng Anh thương mại dùng danh từ chuyên biệt 'reentry'), (C) 'reentered' (V-ed), (D) 'reenter' (động từ nguyên mẫu). Dịch câu: Vé chỉ có giá trị cho một lần vào cửa và không cho phép quay trở lại địa điểm sau khi đã rời đi.",
    "vocab": [
        {"word": "reentry", "ipa": "/riːˈen.tri/", "pos": "n", "meaning": "sự vào lại, quyền quay trở lại", "example": "Concert wristbands permit unlimited reentry until midnight."},
        {"word": "venue", "ipa": "/ˈven.juː/", "pos": "n", "meaning": "địa điểm tổ chức sự kiện/hội nghị", "example": "The exhibition center was chosen as the premier tournament venue."},
        {"word": "valid", "ipa": "/ˈvæl.ɪd/", "pos": "adj", "meaning": "có giá trị, có hiệu lực", "example": "The promotional voucher remains valid for thirty days."}
    ],
    "collocations": [{"phrase": "one-time access", "meaning": "lối vào một lần duy nhất"}, {"phrase": "allow for reentry", "meaning": "cho phép vào lại"}],
    "grammar": [{"title": "Cụm động từ 'allow for' đi với Danh từ", "rule": "allow for + Noun (reentry)", "content": "'Allow for' mang nghĩa 'tính đến, cho phép sự xuất hiện của cái gì', theo sau là một danh từ."}]
}

p5_rest[125] = {
    "exp": "Cấu trúc: Hai mệnh đề có mối quan hệ tương phản nhượng bộ: 'We hired Okafor Construction... although it was not the lowest bidder...' (Chúng tôi thuê công ty mặc dù họ không phải đơn vị bỏ thầu thấp nhất). Phương án (D) 'although' (mặc dù) là liên từ nối mệnh đề chỉ sự tương phản. Các phương án: (A) 'beside' (giới từ: bên cạnh), (B) 'furthermore' (trạng từ liên kết), (C) 'even' (trạng từ nhấn mạnh, cần 'though' để nối mệnh đề). Dịch câu: Chúng tôi đã thuê Okafor Construction để thực hiện việc cải tạo mặc dù họ không phải là nhà thầu có mức giá chào thầu thấp nhất trong dự án.",
    "vocab": [
        {"word": "bidder", "ipa": "/ˈbɪd.ər/", "pos": "n", "meaning": "nhà thầu tham gia đấu giá/chào thầu", "example": "The municipal contract was awarded to the lowest qualified bidder."},
        {"word": "renovation", "ipa": "/ˌren.əˈveɪ.ʃən/", "pos": "n", "meaning": "sự cải tạo, tu sửa công trình", "example": "The historic hotel underwent a extensive interior renovation."},
        {"word": "although", "ipa": "/ɔːlˈðəʊ/", "pos": "conj", "meaning": "mặc dù, dẫu cho", "example": "Sales improved although consumer spending decreased overall."}
    ],
    "collocations": [{"phrase": "lowest bidder", "meaning": "nhà thầu bỏ giá thấp nhất"}, {"phrase": "hire someone to do renovation", "meaning": "thuê ai làm việc tu sửa"}],
    "grammar": [{"title": "Liên từ phụ thuộc chỉ sự nhượng bộ (Concession Clauses)", "rule": "Main Clause + although / even though + Subordinate Clause", "content": "Theo sau 'although' phải là một mệnh đề hoàn chỉnh (chủ ngữ + động từ chia) diễn tả sự tương phản logic."}]
}

p5_rest[126] = {
    "exp": "Cấu trúc: Đứng sau tính từ số thứ tự 'The first' và trước cụm giới từ 'of the training' cần một danh từ số ít chỉ một phần/buổi của khóa học: 'The first session of the training' (Buổi đầu tiên của khóa tập huấn). Phương án (A) 'session' (buổi làm việc/học tập) là đáp án đúng. Các phương án khác không hợp nghĩa: (B) 'result' (kết quả), (C) 'advance' (sự tiến bộ), (D) 'manner' (cách thức). Dịch câu: Buổi đào tạo đầu tiên sẽ giới thiệu cho nhân viên một số trách nhiệm cụ thể tại nơi làm việc.",
    "vocab": [
        {"word": "session", "ipa": "/ˈseʃ.ən/", "pos": "n", "meaning": "buổi tập huấn, phiên họp", "example": "The morning breakout session focused on conflict resolution."},
        {"word": "responsibility", "ipa": "/rɪˌspɒn.sɪˈbɪl.ə.ti/", "pos": "n", "meaning": "trách nhiệm, nhiệm vụ được giao", "example": "Key responsibilities include client onboarding and database upkeep."},
        {"word": "training", "ipa": "/ˈtreɪ.nɪŋ/", "pos": "n", "meaning": "khóa đào tạo, huấn luyện kỹ năng", "example": "Attend mandatory compliance training before operating machinery."}
    ],
    "collocations": [{"phrase": "training session", "meaning": "buổi tập huấn"}, {"phrase": "workplace responsibilities", "meaning": "trách nhiệm tại nơi làm việc"}],
    "grammar": [{"title": "Cụm danh từ ghép 'The first session of...'", "rule": "Ordinal Number + Head Noun (session) + of + Noun", "content": "'Session' là danh từ đếm được chỉ một đợt sinh hoạt, học tập hoặc phiên làm việc diễn ra trong khung giờ xác định."}]
}

p5_rest[127] = {
    "exp": "Cấu trúc: Đứng sau danh từ 'industry' cần một danh từ chỉ người làm việc phân tích chuyên môn để làm chủ ngữ cho hành động nhận định/phán đoán: 'According to industry analysts,...' (Theo các nhà phân tích trong ngành,...). Phương án (D) 'analysts' (các nhà phân tích) hoàn toàn chính xác. Các phương án: (A) 'analyses' (danh từ số nhiều chỉ các bản phân tích), (B) 'analyze' (động từ), (C) 'analytical' (tính từ). Dịch câu: Theo các nhà phân tích trong ngành, Công ty Ghira có kế hoạch di dời trụ sở chính sang Úc.",
    "vocab": [
        {"word": "analyst", "ipa": "/ˈæn.ə.lɪst/", "pos": "n", "meaning": "nhà phân tích chuyên môn", "example": "Financial analysts forecast a rebound in commodity prices."},
        {"word": "relocate", "ipa": "/ˌriː.ləʊˈkeɪt/", "pos": "v", "meaning": "di dời cơ sở/trụ sở", "example": "The tech firm decided to relocate to Austin, Texas."},
        {"word": "headquarters", "ipa": "/ˌhedˈkwɔː.təz/", "pos": "n", "meaning": "trụ sở chính (dạng số ít và số nhiều giống nhau)", "example": "The multinational maintains corporate headquarters in Geneva."}
    ],
    "collocations": [{"phrase": "industry analysts", "meaning": "các nhà phân tích trong ngành"}, {"phrase": "relocate headquarters", "meaning": "di dời trụ sở chính"}],
    "grammar": [{"title": "Danh từ ghép (Compound Nouns) chỉ chức danh nghề nghiệp", "rule": "industry (Noun) + analysts (Noun)", "content": "Danh từ đứng trước đóng vai trò như thuộc tính bổ nghĩa cho danh từ chỉ người phía sau."}]
}

p5_rest[128] = {
    "exp": "Cấu trúc: Đứng trước danh từ ghép 'furniture and clothing' (đồ nội thất và trang phục) cần một tính từ bổ nghĩa cho thời kỳ lịch sử: 'historic furniture' (đồ nội thất có tính lịch sử/cổ kính). Phương án (A) 'historic' (có ý nghĩa lịch sử) là tính từ đúng. Các phương án: (B) 'historian' (nhà sử học), (C) 'historically' (trạng từ), (D) 'history' (danh từ). Dịch câu: Tháng tới, Nhà lưu niệm Kneath House sẽ tổ chức một cuộc triển lãm đồ nội thất và trang phục mang tính lịch sử từ thế kỷ thứ mười tám.",
    "vocab": [
        {"word": "historic", "ipa": "/hɪˈstɒr.ɪk/", "pos": "adj", "meaning": "mang tính lịch sử, cổ kính có giá trị", "example": "Preserve historic landmarks within the downtown quarter."},
        {"word": "exhibition", "ipa": "/ˌek.sɪˈbɪʃ.ən/", "pos": "n", "meaning": "cuộc triển lãm, trưng bày hiện vật", "example": "The museum launched an exhibition of Renaissance oil paintings."},
        {"word": "furniture", "ipa": "/ˈfɜː.nɪ.tʃər/", "pos": "n", "meaning": "đồ nội thất (danh từ không đếm được)", "example": "Handcrafted antique furniture commands premium prices."}
    ],
    "collocations": [{"phrase": "host an exhibition", "meaning": "tổ chức một cuộc triển lãm"}, {"phrase": "eighteenth century", "meaning": "thế kỷ thứ 18"}],
    "grammar": [{"title": "Phân biệt tính từ 'historic' và 'historical'", "rule": "historic (quan trọng/mang giá trị lịch sử) vs. historical (thuộc về quá khứ/lịch sử học)", "content": "'Historic' miêu tả những hiện vật, đồ dùng cổ có giá trị to lớn còn lưu lại."}]
}

p5_rest[129] = {
    "exp": "Cấu trúc: Cụm giới từ cố định chỉ sự chỉ đạo/quản lý: 'under the direction of someone' (dưới sự chỉ đạo/dẫn dắt của ai). Phương án (B) 'under' là giới từ chính xác duy nhất đi với 'the direction of'. Các phương án: (A) 'into' (vào trong), (C) 'upon' (ngay khi), (D) 'past' (vượt qua). Dịch câu: Các giám đốc khu vực của PKTM làm việc dưới sự chỉ đạo của phó chủ tịch.",
    "vocab": [
        {"word": "direction", "ipa": "/daɪˈrek.ʃən/", "pos": "n", "meaning": "sự chỉ đạo, điều hành, dẫn dắt", "example": "Under the new CEO's direction, profits increased by 25%."},
        {"word": "regional manager", "ipa": "/ˈriː.dʒən.əl ˈmæn.ɪ.dʒər/", "pos": "n", "meaning": "giám đốc khu vực", "example": "Regional managers coordinate sales across four provinces."},
        {"word": "vice president", "ipa": "/ˌvaɪs ˈprez.ɪ.dənt/", "pos": "n", "meaning": "phó chủ tịch, phó tổng giám đốc", "example": "Report major quarterly variances directly to the vice president."}
    ],
    "collocations": [{"phrase": "under the direction of", "meaning": "dưới sự chỉ đạo của"}, {"phrase": "regional manager", "meaning": "giám đốc khu vực"}],
    "grammar": [{"title": "Cụm giới từ cố định 'under the direction/supervision of'", "rule": "serve / work + under the direction of + Person/Role", "content": "Diễn đạt mối quan hệ quản lý báo cáo trong sơ đồ tổ chức công ty."}]
}

p5_rest[130] = {
    "exp": "Cấu trúc: Cụm giới từ chỉ phản ứng/hành động đáp lại một xu hướng 'In response to + Noun Phrase' (Để đáp lại / Trước sự gia tăng gần đây...). Sau chỗ trống là cụm danh từ 'a recent surge in demand' (sự gia tăng đột biến về nhu cầu gần đây). Phương án (D) 'In response to' là đáp án đúng. Các phương án: (A) 'In case of' (phòng khi - dùng cho tình huống khẩn cấp như hỏa hoạn), (B) 'Due' (thiếu 'to'), (C) 'According' (thiếu 'to'). Dịch câu: Để đáp ứng sự gia tăng đột biến về nhu cầu gần đây, Công ty Phục vụ tiệc Vanita's đang tuyển thêm bốn nhân viên phục vụ.",
    "vocab": [
        {"word": "surge", "ipa": "/sɜːdʒ/", "pos": "n", "meaning": "sự gia tăng đột biến, nhảy vọt", "example": "A sudden surge in consumer demand caused retail shortages."},
        {"word": "in response to", "ipa": "/ɪn rɪˈspɒns tuː/", "pos": "prep phr", "meaning": "nhằm đáp lại, để phản hồi với", "example": "In response to complaints, we upgraded the ticketing portal."},
        {"word": "server", "ipa": "/ˈsɜː.vər/", "pos": "n", "meaning": "nhân viên phục vụ bàn", "example": "Experienced servers received generous gratuities."}
    ],
    "collocations": [{"phrase": "in response to", "meaning": "nhằm đáp ứng/phản hồi"}, {"phrase": "surge in demand", "meaning": "sự bùng nổ về nhu cầu"}],
    "grammar": [{"title": "Cụm giới từ nguyên nhân - phản ứng 'In response to'", "rule": "In response to + Noun Phrase, S + V", "content": "Được dùng ở đầu câu để giải thích động cơ doanh nghiệp triển khai một biện pháp (tuyển thêm người, mở rộng sản xuất)."}]
}

with open('scratch/p5_q111_q130_part.json', 'w', encoding='utf-8') as f:
    json.dump(p5_rest, f, ensure_ascii=False, indent=2)
print("Saved P5 Q111-Q130 successfully!")
