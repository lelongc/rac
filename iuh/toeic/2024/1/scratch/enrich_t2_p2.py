# scratch/enrich_t2_p2.py: Comprehensive enrichment for Test 2 Part 2 (Q7 - Q31)
import json

t2_p2 = {
    7: {
        "exp": "Phương án (A) là câu trả lời chính xác: Câu hỏi 'Have the machines on the factory floor been cleaned?' (Các máy móc trên sàn nhà máy đã được vệ sinh chưa?) là câu hỏi Yes/No ở thì hiện tại hoàn thành. Phương án (A) 'No, not yet' (Chưa, vẫn chưa xong) trả lời trực tiếp và tự nhiên nhất. Bẫy: (B) bẫy từ 'shipping container' trả lời cho Where; (C) trả lời cho câu hỏi người.",
        "vocab": [
            {"word": "factory floor", "ipa": "/ˈfæk.tər.i flɔːr/", "pos": "n", "meaning": "khu vực xưởng sản xuất, sàn nhà máy", "example": "Safety goggles are mandatory on the factory floor."},
            {"word": "clean", "ipa": "/kliːn/", "pos": "v", "meaning": "lau chùi, vệ sinh máy móc", "example": "Technicians clean the conveyor belts daily."},
            {"word": "not yet", "ipa": "/nɒt jet/", "pos": "adv phr", "meaning": "vẫn chưa (hoàn thành)", "example": "The quarterly financial statements are not yet finalized."}
        ],
        "collocations": [{"phrase": "factory floor", "meaning": "sàn xưởng nhà máy"}, {"phrase": "not yet", "meaning": "vẫn chưa xong"}],
        "grammar": [{"title": "Câu hỏi Yes/No ở thì Hiện tại hoàn thành bị động", "rule": "Have/Has + S + been + V3/ed? -> Yes/No (+ not yet)", "content": "Câu hỏi kiểm tra tiến độ thường có câu trả lời phủ định tự nhiên là 'No, not yet'."}]
    },
    8: {
        "exp": "Phương án (A) là câu trả lời chính xác: Câu hỏi 'How much will the budget increase next year?' (Ngân sách sẽ tăng bao nhiêu vào năm tới?) hỏi về lượng tăng ngân sách. Phương án (A) 'About 10 percent' (Khoảng 10 phần trăm) đưa ra tỷ lệ phần trăm trực tiếp. Bẫy: (B) trả lời cho How long (khoảng thời gian 3 tiếng); (C) trả lời cho Where (tại chi nhánh ngân hàng).",
        "vocab": [
            {"word": "budget", "ipa": "/ˈbʌdʒ.ɪt/", "pos": "n", "meaning": "ngân sách chi tiêu", "example": "The board approved a revised annual marketing budget."},
            {"word": "increase", "ipa": "/ɪnˈkriːs/", "pos": "v, n", "meaning": "gia tăng; mức tăng", "example": "Sales revenues increased by five percent this quarter."},
            {"word": "percent", "ipa": "/pəˈsent/", "pos": "n", "meaning": "phần trăm", "example": "Over seventy percent of shareholders approved the proposal."}
        ],
        "collocations": [{"phrase": "budget increase", "meaning": "sự tăng ngân sách"}, {"phrase": "next year", "meaning": "vào năm tới"}],
        "grammar": [{"title": "Câu hỏi số lượng/mức độ 'How much'", "rule": "How much + will + S + increase? -> Tỷ lệ phần trăm / Khoản tiền", "content": "Khi hỏi về mức tăng ngân sách, phản hồi trực tiếp thường nêu số tiền hoặc tỷ lệ phần trăm cụ thể."}]
    },
    9: {
        "exp": "Phương án (B) là câu trả lời chính xác: Câu hỏi đuôi 'You're going to water the plants before you leave, aren't you?' (Bạn sẽ tưới cây trước khi rời đi đúng không?) xác nhận kế hoạch. Phương án (B) 'Yes, right after I finish this email' (Vâng, ngay sau khi tôi hoàn thành xong email này) xác nhận và nêu thời điểm thực hiện cụ thể. Bẫy: (A) bẫy thì quá khứ không liên quan; (C) trả lời lạc đề về văn phòng.",
        "vocab": [
            {"word": "water", "ipa": "/ˈwɔː.tər/", "pos": "v", "meaning": "tưới nước (cây cảnh)", "example": "Remember to water the indoor ferns twice a week."},
            {"word": "right after", "ipa": "/raɪt ˈɑːf.tər/", "pos": "prep phr", "meaning": "ngay sau khi", "example": "We will resume deliberations right after lunch."},
            {"word": "leave", "ipa": "/liːv/", "pos": "v", "meaning": "rời đi, tan sở", "example": "Staff usually leave the office by six o'clock."}
        ],
        "collocations": [{"phrase": "water the plants", "meaning": "tưới cây"}, {"phrase": "right after", "meaning": "ngay sau khi"}],
        "grammar": [{"title": "Câu hỏi đuôi (Tag Question) xác nhận dự định", "rule": "You're going to + V..., aren't you? -> Yes/No + Mốc thời gian", "content": "Xác nhận hành động sắp tới với cấu trúc tương lai gần 'be going to'."}]
    },
    10: {
        "exp": "Phương án (B) là câu trả lời chính xác: Câu hỏi phủ định 'Aren't you going to schedule an eye doctor appointment?' (Bạn không định đặt lịch khám bác sĩ mắt à?). Phương án (B) 'I already scheduled it for next week' (Tôi đã đặt lịch xong cho tuần tới rồi) trả lời gián tiếp xác nhận việc đã hoàn tất. Bẫy: (A) 'glasses' là bẫy từ vựng liên tưởng đến mắt; (C) lạc đề.",
        "vocab": [
            {"word": "schedule", "ipa": "/ˈʃedʒ.uːl/", "pos": "v", "meaning": "lên lịch, đặt hẹn", "example": "Schedule a routine eye examination annually."},
            {"word": "appointment", "ipa": "/əˈpɔɪnt.mənt/", "pos": "n", "meaning": "cuộc hẹn khám", "example": "Confirm your doctor's appointment 24 hours in advance."},
            {"word": "already", "ipa": "/ɔːlˈred.i/", "pos": "adv", "meaning": "đã... rồi (hoàn thành trước đó)", "example": "The shipment has already departed from the warehouse."}
        ],
        "collocations": [{"phrase": "doctor appointment", "meaning": "cuộc hẹn với bác sĩ"}, {"phrase": "schedule an appointment", "meaning": "đặt một cuộc hẹn"}],
        "grammar": [{"title": "Câu hỏi nghi vấn phủ định (Negative Question)", "rule": "Aren't you + going to-V? -> Phản hồi về tình trạng thực tế", "content": "Người hỏi dùng câu hỏi phủ định để nhắc nhở hoặc bày tỏ sự ngạc nhiên. Phản hồi 'already' giải tỏa thắc mắc ngay lập tức."}]
    },
    11: {
        "exp": "Phương án (C) là câu trả lời chính xác: Lời phát biểu 'I'm going to try to fix this printer' (Tôi sẽ thử sửa chiếc máy in này). Phương án (C) 'Are you sure it can be repaired?' (Bạn có chắc là nó sửa được không?) thể hiện sự nghi ngờ hợp lý và cảnh báo đồng nghiệp. Bẫy: (A) bẫy từ đồng âm 'fit' với 'fix'; (B) 'copies' là bẫy liên tưởng của máy in.",
        "vocab": [
            {"word": "repair", "ipa": "/rɪˈpeər/", "pos": "v", "meaning": "sửa chữa", "example": "Certified technicians repair multifunction network copiers."},
            {"word": "printer", "ipa": "/ˈprɪn.tər/", "pos": "n", "meaning": "máy in", "example": "The wireless printer is out of cyan toner."},
            {"word": "sure", "ipa": "/ʃɔːr/", "pos": "adj", "meaning": "chắc chắn", "example": "Are you sure the warranty coverage is still valid?"}
        ],
        "collocations": [{"phrase": "fix a printer", "meaning": "sửa máy in"}, {"phrase": "can be repaired", "meaning": "có thể sửa được"}],
        "grammar": [{"title": "Phản hồi một lời tuyên bố (Statement Response)", "rule": "Statement (dự định sửa) -> Question expressing doubt (Are you sure...?)", "content": "Trong Part 2, câu trần thuật thường được phản hồi bằng một câu hỏi ngược lại nhằm kiểm tra tính khả thi."}]
    },
    12: {
        "exp": "Phương án (C) là câu trả lời chính xác: Câu hỏi 'What should we do with these brochures?' (Chúng ta nên làm gì với những tập tài liệu quảng cáo này?) hỏi phương hướng xử lý. Phương án (C) 'I'll leave them on the reception desk' (Tôi sẽ để chúng trên bàn lễ tân) đưa ra giải pháp cụ thể. Bẫy: (A) 'seashore' lạc đề; (B) 'Yes' không dùng trả lời câu hỏi Wh-.",
        "vocab": [
            {"word": "brochure", "ipa": "/ˈbrəʊ.ʃər/", "pos": "n", "meaning": "cuốn cẩm nang, tờ rơi giới thiệu sản phẩm", "example": "Distribute promotional brochures to trade show visitors."},
            {"word": "reception desk", "ipa": "/rɪˈsep.ʃən desk/", "pos": "n", "meaning": "bàn tiếp tân", "example": "Inquire at the reception desk for hotel facility maps."},
            {"word": "leave", "ipa": "/liːv/", "pos": "v", "meaning": "để lại, đặt ở vị trí nào", "example": "Leave completed feedback forms in the drop box."}
        ],
        "collocations": [{"phrase": "reception desk", "meaning": "bàn lễ tân"}, {"phrase": "promotional brochure", "meaning": "tập sách nhỏ quảng cáo"}],
        "grammar": [{"title": "Câu hỏi xin chỉ thị với 'should'", "rule": "What should we do with + Noun? -> I will + V (đưa ra giải pháp)", "content": "Người nói nhận trách nhiệm xử lý công việc bằng cách dùng thì tương lai đơn 'I'll leave...'."}]
    },
    13: {
        "exp": "Phương án (B) là câu trả lời chính xác: Câu hỏi 'Has the policy meeting been rescheduled?' (Cuộc họp chính sách đã được dời lịch chưa?). Phương án (B) 'Yes, it's happening tomorrow afternoon' (Có, nó sẽ diễn ra vào chiều mai) xác nhận và cung cấp mốc giờ mới. Bẫy: (A) 'desk calendar' bẫy liên tưởng lịch trình.",
        "vocab": [
            {"word": "reschedule", "ipa": "/ˌriːˈʃedʒ.uːl/", "pos": "v", "meaning": "dời lịch, sắp xếp lại thời gian", "example": "Heavy weather forced managers to reschedule the outdoor summit."},
            {"word": "policy", "ipa": "/ˈpɒl.ə.si/", "pos": "n", "meaning": "chính sách, quy định", "example": "Review the updated corporate travel reimbursement policy."},
            {"word": "happen", "ipa": "/ˈhæp.ən/", "pos": "v", "meaning": "diễn ra, xảy ra", "example": "The annual symposium is happening this Friday."}
        ],
        "collocations": [{"phrase": "policy meeting", "meaning": "cuộc họp về chính sách"}, {"phrase": "tomorrow afternoon", "meaning": "chiều mai"}],
        "grammar": [{"title": "Thì Hiện tại tiếp diễn mang ý nghĩa tương lai 'is happening'", "rule": "be + happening + Future Time Expression", "content": "Diễn tả sự kiện đã được tái ấn định chắc chắn trong lịch làm việc."}]
    },
    14: {
        "exp": "Phương án (A) là câu trả lời chính xác: Lời rủ 'Why don't we stop by the office cafeteria on our way to the workshop?' (Tại sao chúng ta không ghé qua căng tin văn phòng trên đường đến buổi hội thảo?). Phương án (A) 'Sure, we have time for that' (Chắc chắn rồi, chúng ta có đủ thời gian cho việc đó) đồng ý với đề xuất. Bẫy: (B) bẫy liên tưởng 'workshop'.",
        "vocab": [
            {"word": "stop by", "ipa": "/stɒp baɪ/", "pos": "phr v", "meaning": "ghé tạt qua một địa điểm", "example": "Stop by my office before leaving for the day."},
            {"word": "cafeteria", "ipa": "/ˌkæf.əˈtɪə.ri.ə/", "pos": "n", "meaning": "quán ăn tự phục vụ, căng tin", "example": "Staff gather in the cafeteria for catered company lunches."},
            {"word": "on the way to", "ipa": "/ɒn ðə weɪ tuː/", "pos": "prep phr", "meaning": "trên đường đi tới đâu", "example": "Pick up supplies on the way to the construction site."}
        ],
        "collocations": [{"phrase": "stop by the cafeteria", "meaning": "ghé qua căng tin"}, {"phrase": "have time for", "meaning": "có thời gian dành cho"}],
        "grammar": [{"title": "Cấu trúc rủ rê/đề xuất 'Why don't we + V'", "rule": "Why don't we + V-inf? -> Sure / Sounds good", "content": "Mẫu câu đề xuất quen thuộc trong giao tiếp công sở, thường được tán đồng bằng 'Sure, we have time'."}]
    },
    15: {
        "exp": "Phương án (B) là câu trả lời chính xác: Câu hỏi 'Have you tried our famous pasta dish?' (Bạn đã thử món mì Ý nổi tiếng của chúng tôi chưa?). Phương án (B) 'Yes, it was delicious' (Vâng, nó rất ngon) xác nhận và khen ngợi món ăn. Bẫy: (A) 'table for five' là bẫy ngữ cảnh nhà hàng; (C) 'I'll try' bẫy lặp từ.",
        "vocab": [
            {"word": "delicious", "ipa": "/dɪˈlɪʃ.əs/", "pos": "adj", "meaning": "thơm ngon, tuyệt vời", "example": "The banquet chef prepared a delicious seafood paella."},
            {"word": "pasta", "ipa": "/ˈpæs.tə/", "pos": "n", "meaning": "món mì Ý", "example": "Fresh handmade pasta is the house specialty."},
            {"word": "famous", "ipa": "/ˈfeɪ.məs/", "pos": "adj", "meaning": "nổi tiếng", "example": "The bistro is famous for its artisanal sourdough loaves."}
        ],
        "collocations": [{"phrase": "famous dish", "meaning": "món ăn nổi tiếng"}, {"phrase": "taste delicious", "meaning": "có vị rất ngon"}],
        "grammar": [{"title": "Câu hỏi Hiện tại hoàn thành trải nghiệm 'Have you tried...?'", "rule": "Have you + V3/ed...? -> Yes, it was + Adj", "content": "Hỏi về trải nghiệm cá nhân đối với sản phẩm/món ăn, phản hồi bằng cảm nhận thực tế trong quá khứ."}]
    },
    16: {
        "exp": "Phương án (B) là câu trả lời chính xác: Câu hỏi 'Who's the opening act at tonight's concert?' (Ai là người biểu diễn mở màn trong buổi hòa nhạc tối nay?) hỏi người biểu diễn. Phương án (B) 'A jazz singer from France' (Một ca sĩ nhạc jazz đến từ Pháp) trả lời trực tiếp danh tính nghệ sĩ. Bẫy: (A) bẫy từ 'volume' liên tưởng âm nhạc.",
        "vocab": [
            {"word": "opening act", "ipa": "/ˈəʊ.pən.ɪŋ ækt/", "pos": "n phr", "meaning": "tiết mục biểu diễn mở màn", "example": "The indie rock band served as the opening act."},
            {"word": "concert", "ipa": "/ˈkɒn.sət/", "pos": "n", "meaning": "buổi hòa nhạc", "example": "Buy concert tickets before they sell out."},
            {"word": "jazz singer", "ipa": "/dʒæz ˈsɪŋ.ər/", "pos": "n", "meaning": "ca sĩ nhạc jazz", "example": "The acclaimed jazz singer performed at the civic hall."}
        ],
        "collocations": [{"phrase": "opening act", "meaning": "tiết mục mở màn"}, {"phrase": "tonight's concert", "meaning": "buổi hòa nhạc tối nay"}],
        "grammar": [{"title": "Câu hỏi Wh- với từ để hỏi 'Who'", "rule": "Who + be + Noun? -> Danh từ chỉ người / Chức danh", "content": "Lắng nghe từ để hỏi 'Who' đầu câu để nhận diện ngay phản hồi chỉ nhân vật hoặc nghệ sĩ biểu diễn."}]
    },
    17: {
        "exp": "Phương án (A) là câu trả lời chính xác: Câu hỏi 'When do the product demonstrations start?' (Khi nào thì các buổi trình diễn sản phẩm bắt đầu?) hỏi thời gian. Phương án (A) 'The schedule was emailed last Friday' (Lịch trình đã được gửi qua email vào thứ Sáu tuần trước) cung cấp nguồn tra cứu thời gian gián tiếp. Bẫy: (B) bẫy từ 'features' liên tưởng sản phẩm.",
        "vocab": [
            {"word": "demonstration", "ipa": "/ˌdem.ənˈstreɪ.ʃən/", "pos": "n", "meaning": "buổi biểu diễn thử nghiệm sản phẩm", "example": "Attend a live demonstration of the floor-buffing machine."},
            {"word": "schedule", "ipa": "/ˈʃedʒ.uːl/", "pos": "n", "meaning": "lịch trình, thời gian biểu", "example": "Check the seminar schedule for speaker room assignments."},
            {"word": "email", "ipa": "/ˈiː.meɪl/", "pos": "v", "meaning": "gửi thư điện tử", "example": "The coordinator will email the revised itinerary shortly."}
        ],
        "collocations": [{"phrase": "product demonstration", "meaning": "buổi trình diễn sản phẩm"}, {"phrase": "email a schedule", "meaning": "gửi email lịch trình"}],
        "grammar": [{"title": "Câu trả lời gián tiếp cho câu hỏi thời gian 'When'", "rule": "When...? -> Refer to document / email (The schedule was emailed...)", "content": "Thay vì đưa ra mốc giờ cụ thể, câu trả lời hướng người hỏi đến tài liệu chứa thông tin."}]
    },
    18: {
        "exp": "Phương án (C) là câu trả lời chính xác: Lời phàn nàn 'I tried updating the website, but it didn't work' (Tôi đã thử cập nhật trang web nhưng không được). Phương án (C) 'Let me contact our web developer' (Để tôi liên hệ với lập trình viên web của chúng ta) đưa ra phương án xử lý trợ giúp ngay lập tức. Bẫy: (A) bẫy lặp từ 'works'; (B) 'online reviews' lạc đề.",
        "vocab": [
            {"word": "developer", "ipa": "/dɪˈvel.ə.pər/", "pos": "n", "meaning": "nhà phát triển phần mềm/trang web", "example": "Our web developer resolved the shopping cart bug."},
            {"word": "update", "ipa": "/ʌpˈdeɪt/", "pos": "v", "meaning": "cập nhật thông tin mới", "example": "Update your profile information in the portal."},
            {"word": "contact", "ipa": "/ˈkɒn.tækt/", "pos": "v", "meaning": "liên hệ, liên lạc", "example": "Contact technical assistance for hardware failures."}
        ],
        "collocations": [{"phrase": "update a website", "meaning": "cập nhật trang web"}, {"phrase": "web developer", "meaning": "lập trình viên trang web"}],
        "grammar": [{"title": "Cấu trúc đề nghị giúp đỡ 'Let me + V'", "rule": "Let me + V-inf (Let me contact...)", "content": "Thể hiện sự chủ động hỗ trợ đồng nghiệp khi xảy ra sự cố kỹ thuật."}]
    },
    19: {
        "exp": "Phương án (B) là câu trả lời chính xác: Câu hỏi 'Did you hire a new welding specialist?' (Bạn đã thuê chuyên gia hàn mới chưa?). Phương án (B) 'Yes, he starts tomorrow' (Có, anh ấy sẽ bắt đầu làm việc vào ngày mai) xác nhận và cung cấp thêm ngày bắt đầu làm việc. Bẫy: (A) 'back-ordered' là bẫy từ vựng cơ khí.",
        "vocab": [
            {"word": "welding", "ipa": "/ˈwel.dɪŋ/", "pos": "n", "meaning": "nghề hàn kim loại, kỹ thuật hàn", "example": "Protective face shields are essential during arc welding."},
            {"word": "specialist", "ipa": "/ˈspeʃ.əl.ɪst/", "pos": "n", "meaning": "chuyên gia, chuyên viên", "example": "Consult an ergonomic specialist to assess workstation posture."},
            {"word": "hire", "ipa": "/haɪər/", "pos": "v", "meaning": "tuyển dụng, thuê nhân sự", "example": "The contractor plans to hire ten licensed electricians."}
        ],
        "collocations": [{"phrase": "welding specialist", "meaning": "chuyên gia kỹ thuật hàn"}, {"phrase": "start tomorrow", "meaning": "bắt đầu công việc ngày mai"}],
        "grammar": [{"title": "Thì Hiện tại đơn diễn tả lịch trình cố định 'he starts tomorrow'", "rule": "Subject + V-s/es + Future Time", "content": "Dùng thì hiện tại đơn để diễn tả lịch bắt đầu làm việc đã được thỏa thuận trong hợp đồng."}]
    },
    20: {
        "exp": "Phương án (C) là câu trả lời chính xác: Câu hỏi 'How was the color palette for the lobby chosen?' (Bảng phối màu cho sảnh chờ đã được lựa chọn như thế nào?). Phương án (C) 'I wasn't involved in that decision' (Tôi không tham gia vào quyết định đó) là cách trả lời gián tiếp rất phổ biến trong TOEIC khi người nói không phụ trách mảng đó. Bẫy: (A) liệt kê màu sắc; (B) phản hồi cho How was your day.",
        "vocab": [
            {"word": "color palette", "ipa": "/ˈkʌl.ər ˌpæl.ət/", "pos": "n", "meaning": "bảng phối màu sắc trong thiết kế", "example": "The interior architect selected an earthy color palette."},
            {"word": "involved in", "ipa": "/ɪnˈvɒlvd ɪn/", "pos": "adj phr", "meaning": "tham gia vào, dính líu đến", "example": "Senior partners were not involved in daily bookkeeping."},
            {"word": "lobby", "ipa": "/ˈlɒb.i/", "pos": "n", "meaning": "tiền sảnh tòa nhà", "example": "Guests congregated near the fountain in the hotel lobby."}
        ],
        "collocations": [{"phrase": "color palette", "meaning": "bảng màu thiết kế"}, {"phrase": "involved in a decision", "meaning": "tham gia vào một quyết định"}],
        "grammar": [{"title": "Phản hồi né tránh trách nhiệm/thông tin (Indirect Response)", "rule": "I wasn't involved in... / I have no idea / Check with...", "content": "Phương án đúng thường thừa nhận người nói không nắm rõ quyết định do phân công công việc."}]
    },
    21: {
        "exp": "Phương án (B) là câu trả lời chính xác: Câu hỏi 'When are we ordering more supplies for the office?' (Khi nào chúng ta sẽ đặt thêm đồ dùng cho văn phòng?) hỏi mốc thời gian. Phương án (B) 'Next week on Monday' (Vào thứ Hai tuần tới) nêu rõ thời điểm cụ thể. Bẫy: (A) 'storage closet' trả lời cho Where; (C) trả lời cho câu hỏi khác.",
        "vocab": [
            {"word": "supplies", "ipa": "/səˈplaɪz/", "pos": "n pl", "meaning": "vật tư, đồ dùng văn phòng", "example": "Reorder printer paper and pens from office supplies."},
            {"word": "order", "ipa": "/ˈɔː.dər/", "pos": "v", "meaning": "đặt mua hàng hóa", "example": "Order replacement parts before inventories run dry."},
            {"word": "closet", "ipa": "/ˈklɒz.ɪt/", "pos": "n", "meaning": "tủ để đồ nhỏ", "example": "Cleaning chemicals are locked inside the supply closet."}
        ],
        "collocations": [{"phrase": "office supplies", "meaning": "văn phòng phẩm"}, {"phrase": "next week on Monday", "meaning": "thứ Hai tuần tới"}],
        "grammar": [{"title": "Cụm chỉ thời gian tương lai 'Next week on Monday'", "rule": "Next week + on + Day of the week", "content": "Xác định rõ ràng ngày trong tuần diễn ra hoạt động mua sắm tiếp liệu."}]
    },
    22: {
        "exp": "Phương án (A) là câu trả lời chính xác: Câu hỏi 'The battery for the water pump is going to be solar powered, right?' (Pin cho máy bơm nước sẽ chạy bằng năng lượng mặt trời đúng không?). Phương án (A) 'We're still in the planning stages' (Chúng tôi vẫn đang trong giai đoạn lên kế hoạch) chỉ rõ thiết kế vẫn chưa được chốt cố định. Bẫy: (B) bẫy liên tưởng 'water'.",
        "vocab": [
            {"word": "solar powered", "ipa": "/ˈsəʊ.lə ˌpaʊəd/", "pos": "adj", "meaning": "chạy bằng năng lượng mặt trời", "example": "Install solar powered pathway lighting across the campus."},
            {"word": "planning stage", "ipa": "/ˈplæn.ɪŋ steɪdʒ/", "pos": "n", "meaning": "giai đoạn lên kế hoạch dự án", "example": "Budget estimates are refined during the initial planning stage."},
            {"word": "pump", "ipa": "/pʌmp/", "pos": "n", "meaning": "máy bơm nước/dầu", "example": "Electric water pumps maintain reservoir pressure."}
        ],
        "collocations": [{"phrase": "solar powered", "meaning": "chạy bằng năng lượng mặt trời"}, {"phrase": "in the planning stages", "meaning": "trong giai đoạn lên kế hoạch"}],
        "grammar": [{"title": "Cụm giới từ chỉ trạng thái 'in the ... stage'", "rule": "be + in the planning / early / final stage", "content": "Diễn tả dự án đang ở một bước cụ thể trong quy trình phát triển."}]
    },
    23: {
        "exp": "Phương án (B) là câu trả lời chính xác: Câu hỏi 'Where can I buy a charger for this laptop?' (Tôi có thể mua củ sạc cho chiếc laptop này ở đâu?). Phương án (B) 'I can order one for you' (Tôi có thể đặt mua một cái giúp bạn) là giải pháp hỗ trợ thiết thực nhất. Bẫy: (A) trả lời cho When; (C) trả lời lạc đề về bảo hành.",
        "vocab": [
            {"word": "charger", "ipa": "/ˈtʃɑː.dʒər/", "pos": "n", "meaning": "dây sạc, củ sạc pin", "example": "Universal USB-C chargers power most modern laptops."},
            {"word": "laptop", "ipa": "/ˈlæp.tɒp/", "pos": "n", "meaning": "máy tính xách tay", "example": "Staff are issued corporate laptops for remote work."},
            {"word": "order", "ipa": "/ˈɔː.dər/", "pos": "v", "meaning": "đặt hàng giúp ai", "example": "Let me order extra memory cards from the supplier."}
        ],
        "collocations": [{"phrase": "laptop charger", "meaning": "cục sạc máy tính xách tay"}, {"phrase": "order one for you", "meaning": "đặt mua một cái cho bạn"}],
        "grammar": [{"title": "Lời đề nghị giúp đỡ với động từ khiếm khuyết 'can'", "rule": "I can + V-inf + for you", "content": "Thay vì chỉ ra cửa hàng, người nói đưa ra hành động trợ giúp trực tiếp mua hộ sản phẩm."}]
    },
    24: {
        "exp": "Phương án (A) là câu trả lời chính xác: Câu hỏi 'Do I need to reserve a meeting room?' (Tôi có cần đặt trước phòng họp không?). Phương án (A) 'Yes, let me show you how' (Có chứ, để tôi chỉ cho bạn cách làm) xác nhận sự cần thiết và đề nghị hướng dẫn thao tác đặt phòng. Bẫy: (B) khen ngợi dịch vụ lạc đề; (C) nhắc đến bài thuyết trình.",
        "vocab": [
            {"word": "reserve", "ipa": "/rɪˈzɜːv/", "pos": "v", "meaning": "đặt chỗ trước", "example": "Reserve the auditorium two weeks prior to the seminar."},
            {"word": "meeting room", "ipa": "/ˈmiː.tɪŋ ruːm/", "pos": "n", "meaning": "phòng họp", "example": "The executive meeting room includes teleconferencing equipment."},
            {"word": "show how", "ipa": "/ʃəʊ haʊ/", "pos": "phr v", "meaning": "hướng dẫn cách làm", "example": "Senior accountants show recruits how to log billable hours."}
        ],
        "collocations": [{"phrase": "reserve a meeting room", "meaning": "đặt phòng họp"}, {"phrase": "show someone how", "meaning": "hướng dẫn ai cách làm"}],
        "grammar": [{"title": "Cấu trúc hỏi về sự cần thiết 'Do I need to...?'", "rule": "Do I need to + V-inf? -> Yes/No + Hướng dẫn thêm", "content": "Sau khi trả lời khẳng định 'Yes', người nói cung cấp thêm giải pháp hướng dẫn thao tác."}]
    },
    25: {
        "exp": "Phương án (B) là câu trả lời chính xác: Câu hỏi 'When's the new department director supposed to start?' (Khi nào giám đốc bộ phận mới dự kiến sẽ bắt đầu làm việc?). Phương án (B) 'Ms. Pavlova isn't retiring for another month' (Bà Pavlova còn một tháng nữa mới về hưu) ngụ ý rằng vị trí đó chưa thể có người mới bắt đầu ngay lúc này. Bẫy: (A) trả lời cho How long (kéo dài 1 tiếng).",
        "vocab": [
            {"word": "retire", "ipa": "/rɪˈtaɪər/", "pos": "v", "meaning": "nghỉ hưu", "example": "The chief legal counsel will retire at the end of the year."},
            {"word": "director", "ipa": "/daɪˈrek.tər/", "pos": "n", "meaning": "giám đốc bộ phận", "example": "The creative director reviewed candidate graphic portfolios."},
            {"word": "supposed to", "ipa": "/səˈpəʊzd tuː/", "pos": "adj phr", "meaning": "được cho là / dự định làm gì", "example": "The courier is supposed to arrive by mid-afternoon."}
        ],
        "collocations": [{"phrase": "department director", "meaning": "giám đốc bộ phận"}, {"phrase": "be supposed to start", "meaning": "được dự kiến bắt đầu"}],
        "grammar": [{"title": "Cụm giới từ chỉ khoảng thời gian còn lại 'for another + time'", "rule": "not ... for another + month / week", "content": "Diễn tả sự việc cũ vẫn còn tiếp diễn thêm một khoảng thời gian nữa trước khi sự kiện mới diễn ra."}]
    },
    26: {
        "exp": "Phương án (C) là câu trả lời chính xác: Câu hỏi lựa chọn 'Should I deliver these pizzas, or will you?' (Tôi nên đi giao những chiếc bánh pizza này hay bạn sẽ đi?). Phương án (C) 'They're already on the delivery truck' (Chúng đã ở trên xe tải giao hàng rồi) phủ định cả 2 phương án và cho biết việc đã được tài xế khác đảm nhận. Bẫy: (A) trả lời mời ăn bánh; (B) trả lời giá tiền.",
        "vocab": [
            {"word": "deliver", "ipa": "/dɪˈlɪv.ər/", "pos": "v", "meaning": "giao hàng, vận chuyển đến nơi", "example": "Drivers deliver hot meals within a thirty-minute window."},
            {"word": "delivery truck", "ipa": "/dɪˈlɪv.ər.i trʌk/", "pos": "n", "meaning": "xe tải giao hàng", "example": "Load frozen items into the refrigerated delivery truck."},
            {"word": "already", "ipa": "/ɔːlˈred.i/", "pos": "adv", "meaning": "đã... xong rồi", "example": "The warehouse has already dispatched your parcel."}
        ],
        "collocations": [{"phrase": "deliver pizza", "meaning": "giao bánh pizza"}, {"phrase": "delivery truck", "meaning": "xe tải giao hàng"}],
        "grammar": [{"title": "Phản hồi câu hỏi lựa chọn 'A or B' bằng phương án thứ ba", "rule": "A or B? -> Neither (đã được giải quyết bằng cách khác)", "content": "Dạng bẫy câu hỏi lựa chọn không nhất thiết phải chọn A hoặc B mà có thể chỉ ra việc đã được xử lý xong."}]
    },
    27: {
        "exp": "Phương án (B) là câu trả lời chính xác: Lời thông báo 'This month's shipment schedule has been revised' (Lịch trình giao hàng tháng này đã được sửa đổi). Phương án (B) 'Which dates have been changed?' (Những ngày nào đã bị thay đổi vậy?) hỏi thêm chi tiết làm rõ một cách tự nhiên nhất. Bẫy: (A) lạc đề không liên quan.",
        "vocab": [
            {"word": "revise", "ipa": "/rɪˈvaɪz/", "pos": "v", "meaning": "sửa đổi, hiệu chỉnh", "example": "Revise the shipping manifest before customs inspection."},
            {"word": "shipment", "ipa": "/ˈʃɪp.mənt/", "pos": "n", "meaning": "lô hàng vận chuyển", "example": "Track the overseas container shipment online."},
            {"word": "schedule", "ipa": "/ˈʃedʒ.uːl/", "pos": "n", "meaning": "lịch trình", "example": "Supply chain disruptions impacted the delivery schedule."}
        ],
        "collocations": [{"phrase": "shipment schedule", "meaning": "lịch trình giao hàng"}, {"phrase": "dates have been changed", "meaning": "các ngày đã bị thay đổi"}],
        "grammar": [{"title": "Thì Hiện tại hoàn thành bị động 'has been revised'", "rule": "S + have/has + been + V3/ed", "content": "Diễn tả văn bản hoặc lịch trình đã được điều chỉnh xong và kết quả đang có hiệu lực thi hành."}]
    },
    28: {
        "exp": "Phương án (A) là câu trả lời chính xác: Câu hỏi 'How much will the repairs cost?' (Việc sửa chữa sẽ tốn bao nhiêu chi phí?). Phương án (A) 'The work is covered under the warranty plan' (Công việc sửa chữa được chi trả theo gói bảo hành) trả lời gián tiếp rằng khách hàng không phải tốn tiền vì có bảo hành. Bẫy: (B) bẫy từ 'available' lạc đề.",
        "vocab": [
            {"word": "covered", "ipa": "/ˈkʌv.əd/", "pos": "adj", "meaning": "được bảo hiểm/bảo hành chi trả", "example": "Dental checkups are fully covered under our health plan."},
            {"word": "warranty plan", "ipa": "/ˈwɒr.ən.ti plæn/", "pos": "n phr", "meaning": "gói/chế độ bảo hành", "example": "Purchase an extended warranty plan for home appliances."},
            {"word": "repair cost", "ipa": "/rɪˈpeə kɒst/", "pos": "n phr", "meaning": "chi phí sửa chữa", "example": "Diagnostic tests help estimate total repair costs."}
        ],
        "collocations": [{"phrase": "covered under warranty", "meaning": "được bảo hành chi trả"}, {"phrase": "repairs cost", "meaning": "chi phí sửa chữa"}],
        "grammar": [{"title": "Cụm từ bị động 'be covered under...'", "rule": "S + be + covered under + policy/warranty", "content": "Cụm từ quen thuộc trong dịch vụ khách hàng chỉ quyền lợi được miễn phí theo chế độ bảo hành."}]
    },
    29: {
        "exp": "Phương án (C) là câu trả lời chính xác: Lời đề xuất 'Why don't we provide more samples of the wallpaper patterns?' (Tại sao chúng ta không cung cấp thêm các mẫu hoa văn giấy dán tường?). Phương án (C) 'We ran out of pattern books' (Chúng ta đã hết sạch sách mẫu hoa văn rồi) giải thích lý do không thể thực hiện được đề xuất. Bẫy: (A) giao báo hàng ngày lạc đề.",
        "vocab": [
            {"word": "pattern", "ipa": "/ˈpæt.ən/", "pos": "n", "meaning": "hoa văn, họa tiết", "example": "Select decorative geometric patterns for accent walls."},
            {"word": "sample", "ipa": "/ˈsɑːm.pəl/", "pos": "n", "meaning": "mẫu thử, mẫu vật liệu", "example": "Clients request fabric samples before selecting upholstery."},
            {"word": "run out of", "ipa": "/rʌn aʊt əv/", "pos": "phr v", "meaning": "hết sạch, cạn kiệt", "example": "The print shop ran out of heavy cardstock."}
        ],
        "collocations": [{"phrase": "run out of", "meaning": "hết sạch thứ gì"}, {"phrase": "wallpaper patterns", "meaning": "hoa văn giấy dán tường"}],
        "grammar": [{"title": "Cụm động từ 'run out of' (hết sạch)", "rule": "Subject + run out of + Noun", "content": "Diễn tả tình trạng kho hàng hoặc nguồn dự trữ đã cạn kiệt không còn vật phẩm để cung cấp."}]
    },
    30: {
        "exp": "Phương án (A) là câu trả lời chính xác: Lời nhờ vả 'Can you give me a tour of the property this afternoon?' (Bạn có thể dẫn tôi đi xem khu bất động sản vào chiều nay được không?). Phương án (A) 'Sorry, I won't have time until tomorrow' (Xin lỗi, tôi sẽ không rảnh cho tới ngày mai) từ chối lịch sự kèm lý do bận việc. Bẫy: (B) miêu tả căn nhà lạc đề.",
        "vocab": [
            {"word": "property", "ipa": "/ˈprɒp.ə.ti/", "pos": "n", "meaning": "bất động sản, khu đất/tòa nhà", "example": "Real estate brokers conduct weekend property viewings."},
            {"word": "tour", "ipa": "/tʊər/", "pos": "n", "meaning": "chuyến tham quan khảo sát", "example": "Prospective tenants took a guided tour of the complex."},
            {"word": "until tomorrow", "ipa": "/ənˈtɪl təˈmɒr.əʊ/", "pos": "prep phr", "meaning": "cho tới tận ngày mai", "example": "The inspection report will not be finalized until tomorrow."}
        ],
        "collocations": [{"phrase": "give a tour of", "meaning": "dẫn đi tham quan"}, {"phrase": "have time until", "meaning": "có thời gian cho tới khi"}],
        "grammar": [{"title": "Lời từ chối lịch sự 'Sorry, I won't have time...'", "rule": "Sorry, + S + won't + have time until + Time", "content": "Mẫu câu nhã nhặn vừa từ chối yêu cầu vừa gợi ý thời điểm có thể thực hiện thay thế."}]
    },
    31: {
        "exp": "Phương án (A) là câu trả lời chính xác: Câu hỏi 'Who's scheduled to test the product today?' (Ai được xếp lịch kiểm thử sản phẩm ngày hôm nay?). Phương án (A) 'We're waiting for confirmation' (Chúng tôi đang chờ xác nhận) trả lời gián tiếp rằng danh tính người kiểm thử vẫn chưa được chốt. Bẫy: (B) nhắc đến album nhạc; (C) trả lời lạc đề về phòng thí nghiệm.",
        "vocab": [
            {"word": "confirmation", "ipa": "/ˌkɒn.fəˈmeɪ.ʃən/", "pos": "n", "meaning": "sự xác nhận, thông báo khẳng định", "example": "Wait for written confirmation before booking hotel rooms."},
            {"word": "test", "ipa": "/test/", "pos": "v", "meaning": "kiểm tra, thử nghiệm", "example": "Quality assurance teams test the prototype under stress."},
            {"word": "scheduled", "ipa": "/ˈʃedʒ.uːld/", "pos": "adj", "meaning": "được lên lịch trình", "example": "Who is scheduled to chair the morning session?"}
        ],
        "collocations": [{"phrase": "wait for confirmation", "meaning": "chờ đợi sự xác nhận"}, {"phrase": "test the product", "meaning": "thử nghiệm sản phẩm"}],
        "grammar": [{"title": "Cấu trúc 'wait for + Noun'", "rule": "S + be + waiting for + Noun (confirmation)", "content": "Diễn đạt việc đang chờ thông tin phản hồi từ một bên thứ ba trước khi có câu trả lời dứt khoát."}]
    }
}

with open('scratch/t2_p2_enrichment.json', 'w', encoding='utf-8') as f:
    json.dump(t2_p2, f, ensure_ascii=False, indent=2)
print("Saved Test 2 Part 2 enrichment successfully!")
