# scratch/generate_t2_p5_p6_vocab.py: Contextual vocabulary for Test 2 Part 5 & 6 (Q101 - Q146)
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

t2_p5_p6_vocab = {
    101: [
        {"word": "handheld", "ipa": "/ˈhænd.held/", "pos": "adj", "meaning": "cầm tay, di động", "example": "Before operating your handheld device, please read the manual."},
        {"word": "enclosed", "ipa": "/ɪnˈkləʊzd/", "pos": "adj", "meaning": "được đính kèm, gửi kèm bên trong", "example": "Use the enclosed charging cable to power the battery."},
        {"word": "charge", "ipa": "/tʃɑːdʒ/", "pos": "v", "meaning": "sạc điện, nạp pin", "example": "Charge the wireless mouse fully before first use."}
    ],
    102: [
        {"word": "original", "ipa": "/əˈrɪdʒ.ən.əl/", "pos": "adj", "meaning": "nguyên bản, ban đầu", "example": "Customers must retain the original purchase receipt."},
        {"word": "purchase receipt", "ipa": "/ˈpɜː.tʃəs rɪˈsiːt/", "pos": "n", "meaning": "biên lai hóa đơn mua hàng", "example": "Present your purchase receipt to request a cash refund."},
        {"word": "return", "ipa": "/rɪˈtɜːn/", "pos": "v, n", "meaning": "trả hàng, đổi trả", "example": "Items must be returned in their original packaging."}
    ],
    103: [
        {"word": "travel to", "ipa": "/ˈtræv.əl tuː/", "pos": "phr v", "meaning": "đi công tác tới, di chuyển đến", "example": "Mr. Peterson will travel to the Tokyo office for the annual summit."},
        {"word": "annual meeting", "ipa": "/ˈæn.ju.əl ˈmiː.tɪŋ/", "pos": "n", "meaning": "cuộc họp thường niên hàng năm", "example": "Shareholders gathered in Chicago for the annual meeting."},
        {"word": "overseas", "ipa": "/ˌəʊ.vəˈsiːz/", "pos": "adj, adv", "meaning": "ở nước ngoài, hải ngoại", "example": "The company expanded its overseas client network."}
    ],
    104: [
        {"word": "back order", "ipa": "/bæk ˈɔː.dər/", "pos": "n", "meaning": "đơn đặt hàng tạm chờ nhập thêm hàng", "example": "Items on back order will ship once new inventory arrives."},
        {"word": "charge", "ipa": "/tʃɑːdʒ/", "pos": "v", "meaning": "tính phí, đòi tiền", "example": "We will not charge your credit card until items leave our warehouse."},
        {"word": "warehouse", "ipa": "/ˈweə.haʊs/", "pos": "n", "meaning": "kho hàng trung chuyển", "example": "Goods are dispatched directly from the regional warehouse."}
    ],
    105: [
        {"word": "premium", "ipa": "/ˈpriː.mi.əm/", "pos": "adj", "meaning": "cao cấp, thượng hạng", "example": "Our premium day tour takes visitors to historic architectural sites."},
        {"word": "historic site", "ipa": "/hɪˈstɒr.ɪk saɪt/", "pos": "n", "meaning": "di tích lịch sử", "example": "Tour guides explain the cultural significance of historic sites."},
        {"word": "along", "ipa": "/əˈlɒŋ/", "pos": "prep", "meaning": "dọc theo (con sông, con đường)", "example": "Take a scenic walk along the Aprico River."}
    ],
    106: [
        {"word": "survey", "ipa": "/ˈsɜː.veɪ/", "pos": "v, n", "meaning": "khảo sát, cuộc điều tra ý kiến", "example": "Eighty percent of drivers surveyed showed interest in clean energy."},
        {"word": "electricity", "ipa": "/ɪˌlekˈtrɪs.ə.ti/", "pos": "n", "meaning": "điện lực, năng lượng điện", "example": "More commuters consider buying vehicles that run on electricity."},
        {"word": "consider", "ipa": "/kənˈsɪd.ər/", "pos": "v", "meaning": "cân nhắc, xem xét", "example": "Management will consider upgrading the corporate fleet."}
    ],
    107: [
        {"word": "operations", "ipa": "/ˌɒp.ərˈeɪ.ʃənz/", "pos": "n pl", "meaning": "hoạt động vận hành sản xuất", "example": "He was appointed vice president of global operations."},
        {"word": "join", "ipa": "/dʒɔɪn/", "pos": "v", "meaning": "gia nhập, tham gia vào công ty", "example": "She joined the architectural engineering firm last month."},
        {"word": "vice president", "ipa": "/vaɪs ˈprez.ɪ.dənt/", "pos": "n", "meaning": "phó chủ tịch, phó giám đốc", "example": "The vice president delivered the keynote address."}
    ],
    108: [
        {"word": "author's hour", "ipa": "/ˈɔː.θərz aʊər/", "pos": "n", "meaning": "buổi giao lưu cùng tác giả", "example": "The bookstore will be holding its third author's hour in Cleveland."},
        {"word": "its", "ipa": "/ɪts/", "pos": "det", "meaning": "của nó (tính từ sở hữu)", "example": "The publishing company celebrated its twentieth anniversary."},
        {"word": "hold an event", "ipa": "/həʊld ən ɪˈvent/", "pos": "phr", "meaning": "tổ chức một sự kiện", "example": "They decided to hold an outdoor book fair this weekend."}
    ],
    109: [
        {"word": "recently", "ipa": "/ˈriː.sənt.li/", "pos": "adv", "meaning": "gần đây, mới đây", "example": "Chester's Tiles recently expanded to a second retail location."},
        {"word": "expand", "ipa": "/ɪkˈspænd/", "pos": "v", "meaning": "mở rộng quy mô, phát triển thêm", "example": "The chain plans to expand throughout neighboring cities."},
        {"word": "location", "ipa": "/ləʊˈkeɪ.ʃən/", "pos": "n", "meaning": "địa điểm, chi nhánh cửa hàng", "example": "The new storefront location attracts abundant foot traffic."}
    ],
    110: [
        {"word": "significantly", "ipa": "/sɪɡˈnɪf.ɪ.kənt.li/", "pos": "adv", "meaning": "một cách đáng kể", "example": "The snack company significantly increased the proportion of almonds."},
        {"word": "increase", "ipa": "/ɪnˈkriːs/", "pos": "v, n", "meaning": "làm tăng lên, nâng cao", "example": "Targeted advertising helped increase online sales."},
        {"word": "snack pack", "ipa": "/snæk pæk/", "pos": "n", "meaning": "gói đồ ăn nhẹ", "example": "The Nut Medley snack pack is convenient for travelers."}
    ],
    111: [
        {"word": "wherever", "ipa": "/weərˈev.ər/", "pos": "conj", "meaning": "bất cứ nơi đâu, bất kể nơi nào", "example": "Wherever she travels, the designer collects local fabric swatches."},
        {"word": "fabric", "ipa": "/ˈfæb.rɪk/", "pos": "n", "meaning": "vải vóc, chất liệu may mặc", "example": "Cotton and linen are breathable summer fabrics."},
        {"word": "pattern", "ipa": "/ˈpæt.ən/", "pos": "n", "meaning": "hoa văn, họa tiết trang trí", "example": "Artisans dye intricate geometric patterns onto silk scarves."}
    ],
    112: [
        {"word": "picture frame", "ipa": "/ˈpɪk.tʃər freɪm/", "pos": "n", "meaning": "khung ảnh, khung tranh", "example": "Most picture frames at Glowing Photo Lab go on sale today."},
        {"word": "go on sale", "ipa": "/ɡəʊ ɒn seɪl/", "pos": "phr", "meaning": "được bán giảm giá", "example": "Electronics go on sale during the holiday shopping season."},
        {"word": "photo lab", "ipa": "/ˈfəʊ.təʊ læb/", "pos": "n", "meaning": "hiệu ảnh, xưởng rửa ảnh", "example": "The professional photo lab offers custom framing services."}
    ],
    113: [
        {"word": "advanced degree", "ipa": "/ədˈvɑːnst dɪˈɡriː/", "pos": "n", "meaning": "bằng cấp cao (thạc sĩ, tiến sĩ)", "example": "All students in the business management class hold advanced college degrees."},
        {"word": "business management", "ipa": "/ˈbɪz.nɪs ˈmæn.ɪdʒ.mənt/", "pos": "n", "meaning": "quản trị kinh doanh", "example": "She enrolled in a master's program in business management."},
        {"word": "hold", "ipa": "/həʊld/", "pos": "v", "meaning": "nắm giữ, sở hữu (chứng chỉ, bằng)", "example": "Candidates must hold an accredited accounting certification."}
    ],
    114: [
        {"word": "evaluate", "ipa": "/ɪˈvæl.ju.eɪt/", "pos": "v", "meaning": "thẩm định, đánh giá giá trị", "example": "We hired an auditor to evaluate our company's financial assets."},
        {"word": "financial assets", "ipa": "/faɪˈnæn.ʃəl ˈæs.ets/", "pos": "n pl", "meaning": "tài sản tài chính", "example": "Firms must accurately declare all tangible and financial assets."},
        {"word": "hire", "ipa": "/haɪər/", "pos": "v", "meaning": "thuê mướn chuyên gia", "example": "The director decided to hire an outside consulting agency."}
    ],
    115: [
        {"word": "take on", "ipa": "/teɪk ɒn/", "pos": "phr v", "meaning": "đảm nhận (trách nhiệm, công việc mới)", "example": "Ms. Charisse is taking on a new corporate account next week."},
        {"word": "account", "ipa": "/əˈkaʊnt/", "pos": "n", "meaning": "khách hàng, tài khoản thương mại", "example": "Winning the automotive account boosted our agency's revenue."},
        {"word": "finish", "ipa": "/ˈfɪn.ɪʃ/", "pos": "v", "meaning": "hoàn thành, dứt điểm", "example": "She will take on new duties after she finishes the current project."}
    ],
    116: [
        {"word": "profit", "ipa": "/ˈprɒf.ɪt/", "pos": "n", "meaning": "lợi nhuận doanh thu", "example": "Cormet Motors' quarterly profits are significantly higher this year."},
        {"word": "higher than", "ipa": "/ˈhaɪ.ər ðæn/", "pos": "phr", "meaning": "cao hơn so với", "example": "Customer satisfaction ratings are higher than last year."},
        {"word": "motor", "ipa": "/ˈməʊ.tər/", "pos": "n", "meaning": "động cơ, ô tô cơ giới", "example": "The motor company unveiled its newest hybrid crossover model."}
    ],
    117: [
        {"word": "advertising campaign", "ipa": "/ˈæd.və.taɪ.zɪŋ kæmˈpeɪn/", "pos": "n", "meaning": "chiến dịch quảng cáo", "example": "In its current advertising campaign, the brand highlights reliability."},
        {"word": "current", "ipa": "/ˈkʌr.ənt/", "pos": "adj", "meaning": "hiện tại, đương thời", "example": "Our current promotional discounts expire at the end of the month."},
        {"word": "reliable", "ipa": "/rɪˈlaɪ.ə.bəl/", "pos": "adj", "meaning": "đáng tin cậy, bền vững", "example": "Jaymor Tools manufactures sturdy and reliable power drills."}
    ],
    118: [
        {"word": "reimbursement", "ipa": "/ˌriː.ɪmˈbɜːs.mənt/", "pos": "n", "meaning": "khoản thanh toán bồi hoàn chi phí", "example": "Submit itemized receipts for travel expense reimbursement."},
        {"word": "receipt", "ipa": "/rɪˈsiːt/", "pos": "n", "meaning": "hóa đơn, biên lai thu tiền", "example": "Keep every meal receipt when traveling on official business."},
        {"word": "business trip", "ipa": "/ˈbɪz.nɪs trɪp/", "pos": "n", "meaning": "chuyến đi công tác", "example": "File expense reports promptly when returning from a business trip."}
    ],
    119: [
        {"word": "patron", "ipa": "/ˈpeɪ.trən/", "pos": "n", "meaning": "bạn đọc thư viện, khách quen", "example": "Library patrons will be able to borrow newly acquired titles."},
        {"word": "newly acquired", "ipa": "/ˈnjuː.li əˈkwaɪəd/", "pos": "adj phr", "meaning": "mới được sưu tầm, mới tiếp nhận", "example": "The gallery showcases a newly acquired collection of oil paintings."},
        {"word": "collection", "ipa": "/kəˈlek.ʃən/", "pos": "n", "meaning": "bộ sưu tập tài liệu/sách", "example": "The reference collection includes rare regional historical maps."}
    ],
    120: [
        {"word": "direct to", "ipa": "/daɪˈrekt tuː/", "pos": "v", "meaning": "chuyển hướng, gửi câu hỏi tới", "example": "Please direct any questions about time sheets to the payroll officer."},
        {"word": "time sheet", "ipa": "/taɪm ʃiːt/", "pos": "n", "meaning": "bảng theo dõi giờ làm/chấm công", "example": "Submit your biweekly time sheet by 5:00 P.M. on Friday."},
        {"word": "payroll department", "ipa": "/ˈpeɪ.rəʊl dɪˈpɑːt.mənt/", "pos": "n", "meaning": "phòng kế toán chi trả lương", "example": "The payroll department handles direct salary deposits."}
    ],
    121: [
        {"word": "delivery receipt", "ipa": "/dɪˈlɪv.ər.i rɪˈsiːt/", "pos": "n", "meaning": "biên bản nhận hàng giao", "example": "Before signing the delivery receipt, inspect all freight packages."},
        {"word": "double-check", "ipa": "/ˌdʌb.əlˈtʃek/", "pos": "v", "meaning": "kiểm tra lại lần hai cho chắc chắn", "example": "Double-check that all invoiced serial numbers match the physical stock."},
        {"word": "shipment", "ipa": "/ˈʃɪp.mənt/", "pos": "n", "meaning": "lô hàng vận chuyển", "example": "The entire shipment arrived without any transit damage."}
    ],
    122: [
        {"word": "funds", "ipa": "/fʌndz/", "pos": "n pl", "meaning": "nguồn tiền vốn, ngân quỹ", "example": "Additional funds have been allocated to the capital development budget."},
        {"word": "associated with", "ipa": "/əˈsəʊ.si.eɪ.tɪd wɪð/", "pos": "adj phr", "meaning": "gắn liền với, liên quan tới", "example": "Expenses associated with facility construction were carefully reviewed."},
        {"word": "budget", "ipa": "/ˈbʌdʒ.ɪt/", "pos": "n", "meaning": "ngân sách chi tiêu", "example": "Stay within the approved annual operating budget."}
    ],
    123: [
        {"word": "notice", "ipa": "/ˈnəʊ.tɪs/", "pos": "v", "meaning": "nhận thấy, phát hiện ra", "example": "Ms. Bernard noticed that a project deadline was approaching quickly."},
        {"word": "approaching", "ipa": "/əˈprəʊ.tʃɪŋ/", "pos": "adj", "meaning": "đang đến gần (thời gian)", "example": "Staff worked overtime to meet the rapidly approaching delivery date."},
        {"word": "request assistance", "ipa": "/rɪˈkwest əˈsɪs.təns/", "pos": "phr", "meaning": "yêu cầu sự hỗ trợ giúp đỡ", "example": "She requested technical assistance from the IT help desk."}
    ],
    124: [
        {"word": "hopeful", "ipa": "/ˈhəʊp.fəl/", "pos": "adj", "meaning": "đầy hy vọng, tràn trề niềm tin", "example": "The committee is hopeful that the renowned author will attend."},
        {"word": "keynote speech", "ipa": "/ˈkiː.nəʊt spiːtʃ/", "pos": "n", "meaning": "bài diễn văn bế mạc/chủ đạo", "example": "Dr. Tanaka agreed to present the opening keynote speech at the conference."},
        {"word": "agree to", "ipa": "/əˈɡriː tuː/", "pos": "v", "meaning": "đồng ý, chấp thuận làm gì", "example": "The board agreed to sponsor the educational symposium."}
    ],
    125: [
        {"word": "smartphone", "ipa": "/ˈsmɑːt.fəʊn/", "pos": "n", "meaning": "điện thoại thông minh", "example": "Tech manufacturers compete aggressively to release cutting-edge smartphones."},
        {"word": "unclear", "ipa": "/ʌnˈklɪər/", "pos": "adj", "meaning": "chưa rõ ràng, chưa xác định", "example": "It is currently unclear which device model will hit store shelves first."},
        {"word": "become available", "ipa": "/bɪˈkʌm əˈveɪ.lə.bəl/", "pos": "phr", "meaning": "chính thức mở bán/sẵn có", "example": "The new tablet will become available to consumers next Tuesday."}
    ],
    126: [
        {"word": "weights", "ipa": "/weɪts/", "pos": "n pl", "meaning": "tạ tập thể hình, quả tạ", "example": "The gym trainer offers members instructions in how to lift weights properly."},
        {"word": "properly", "ipa": "/ˈprɒp.əl.i/", "pos": "adv", "meaning": "đúng kỹ thuật, chuẩn xác", "example": "Learn how to operate cardiovascular machinery properly to prevent injury."},
        {"word": "gym member", "ipa": "/dʒɪm ˈmem.bər/", "pos": "n", "meaning": "hội viên câu lạc bộ thể hình", "example": "Gym members receive complimentary access to sauna facilities."}
    ],
    127: [
        {"word": "according to", "ipa": "/əˈkɔː.dɪŋ tuː/", "pos": "prep", "meaning": "theo như (quy định, thỏa thuận)", "example": "According to facility rules, overnight parking is strictly prohibited."},
        {"word": "permitted", "ipa": "/pəˈmɪt.ɪd/", "pos": "adj", "meaning": "được cho phép, hợp lệ", "example": "Smoking is not permitted anywhere inside the office building."},
        {"word": "clubhouse", "ipa": "/ˈklʌb.haʊs/", "pos": "n", "meaning": "nhà sinh hoạt câu lạc bộ", "example": "The community clubhouse features a lounge and swimming pool."}
    ],
    128: [
        {"word": "once", "ipa": "/wʌns/", "pos": "conj", "meaning": "ngay khi, một khi", "example": "Once all branch managers have arrived, we can begin the video conference."},
        {"word": "conference call", "ipa": "/ˈkɒn.fər.əns kɔːl/", "pos": "n", "meaning": "cuộc gọi họp hội nghị trực tuyến", "example": "Dial the access code to join the international conference call."},
        {"word": "arrive", "ipa": "/əˈraɪv/", "pos": "v", "meaning": "có mặt, đến nơi họp", "example": "Ensure all participants arrive ten minutes prior to the briefing."}
    ],
    129: [
        {"word": "accomplishment", "ipa": "/əˈkʌm.plɪʃ.mənt/", "pos": "n", "meaning": "thành tựu, thành quả đạt được", "example": "The annual video highlights the notable accomplishments of our sales teams."},
        {"word": "motivational", "ipa": "/ˌməʊ.tɪˈveɪ.ʃən.əl/", "pos": "adj", "meaning": "mang tính khích lệ, truyền cảm hứng", "example": "The CEO gave a highly motivational speech to inaugurate the fiscal year."},
        {"word": "highlight", "ipa": "/ˈhaɪ.laɪt/", "pos": "v", "meaning": "nhấn mạnh, làm nổi bật lên", "example": "The report highlights major revenue growth in Asian export markets."}
    ],
    130: [
        {"word": "retirement dinner", "ipa": "/rɪˈtaɪə.mənt ˈdɪn.ər/", "pos": "n", "meaning": "bữa tiệc tối chia tay nghỉ hưu", "example": "Employees organized a banquet retirement dinner for the veteran engineer."},
        {"word": "honor", "ipa": "/ˈɒn.ər/", "pos": "v", "meaning": "tôn vinh, vinh danh cống hiến", "example": "Colleagues gathered to honor her thirty dedicated years of public service."},
        {"word": "years of service", "ipa": "/jɪərz əv ˈsɜː.vɪs/", "pos": "n phr", "meaning": "thâm niên công tác cống hiến", "example": "He received a gold watch in recognition of 25 years of service."}
    ],

    # Part 6 (Q131-Q146)
    131: [
        {"word": "special order", "ipa": "/ˈspeʃ.əl ˈɔː.dər/", "pos": "n", "meaning": "đơn đặt hàng thiết kế riêng", "example": "The carpentry shop completed your special order for custom cabinetry."},
        {"word": "custom-built", "ipa": "/ˈkʌs.təm bɪlt/", "pos": "adj", "meaning": "đóng theo kích thước yêu cầu", "example": "Handcrafted oak dining tables are custom-built to client specifications."},
        {"word": "craft", "ipa": "/krɑːft/", "pos": "v, n", "meaning": "chế tác tinh xảo, nghề thủ công", "example": "Skilled carpenters craft exquisite solid wood furniture."}
    ],
    132: [
        {"word": "furniture", "ipa": "/ˈfɜː.nɪ.tʃər/", "pos": "n", "meaning": "đồ nội thất bàn ghế", "example": "Delivery crews will transport the new dining room furniture next Tuesday."},
        {"word": "transport", "ipa": "/trænˈspɔːt/", "pos": "v", "meaning": "vận chuyển, chuyên chở", "example": "Freight carriers transport delicate wood furnishings with great care."},
        {"word": "deliver", "ipa": "/dɪˈlɪv.ər/", "pos": "v", "meaning": "giao tận nơi", "example": "Couriers will deliver your dining set directly to your home address."}
    ],
    133: [
        {"word": "speak to", "ipa": "/spiːk tuː/", "pos": "phr v", "meaning": "nói chuyện trực tiếp với ai", "example": "Please ask to speak to our shipping supervisor if you have special requests."},
        {"word": "delivery manager", "ipa": "/dɪˈlɪv.ər.i ˈmæn.ɪ.dʒər/", "pos": "n", "meaning": "người quản lý khâu giao hàng", "example": "Contact the delivery manager to verify your scheduled drop-off window."},
        {"word": "specific request", "ipa": "/spəˈsɪf.ɪk rɪˈkwest/", "pos": "n", "meaning": "yêu cầu cụ thể chi tiết", "example": "Note any specific requests regarding installation on your order form."}
    ],
    134: [
        {"word": "convenient time", "ipa": "/kənˈviː.ni.ənt taɪm/", "pos": "n", "meaning": "thời gian thuận tiện nhất", "example": "Our logistics coordinator can arrange a convenient time for delivery."},
        {"word": "schedule", "ipa": "/ˈʃedʒ.uːl/", "pos": "v", "meaning": "sắp xếp lịch hẹn", "example": "We will schedule the furniture assembly for Wednesday afternoon."},
        {"word": "coordinate", "ipa": "/kəʊˈɔː.dɪ.neɪt/", "pos": "v", "meaning": "điều phối nhịp nhàng", "example": "Customer support coordinates dispatch times with local homeowners."}
    ],
    135: [
        {"word": "heating system", "ipa": "/ˈhiː.tɪŋ ˈsɪs.təm/", "pos": "n", "meaning": "hệ thống sưởi ấm gia đình", "example": "Ensuring your heating system runs efficiently is vital for home safety."},
        {"word": "safety", "ipa": "/ˈseɪf.ti/", "pos": "n", "meaning": "sự an toàn, an ninh", "example": "Annual equipment maintenance guarantees overall operational safety."},
        {"word": "comfort", "ipa": "/ˈkʌm.fət/", "pos": "n", "meaning": "sự tiện nghi, dễ chịu", "example": "Apex Comfort delivers reliable indoor climate solutions for families."}
    ],
    136: [
        {"word": "furthermore", "ipa": "/ˌfɜː.ðəˈmɔːr/", "pos": "adv", "meaning": "hơn nữa, thêm vào đó", "example": "Furthermore, seasonal tune-ups reduce monthly electricity bills considerably."},
        {"word": "routine inspection", "ipa": "/ruːˈtiːn ɪnˈspek.ʃən/", "pos": "n", "meaning": "kiểm tra kỹ thuật định kỳ", "example": "Technicians conduct a comprehensive 20-point routine inspection."},
        {"word": "optimize", "ipa": "/ˈɒp.tɪ.maɪz/", "pos": "v", "meaning": "tối ưu hóa hiệu năng", "example": "Regular maintenance helps optimize heating furnace performance."}
    ],
    137: [
        {"word": "knowledgeable", "ipa": "/ˈnɒl.ɪ.dʒə.bəl/", "pos": "adj", "meaning": "am hiểu chuyên sâu, có kiến thức", "example": "Our certified technicians are courteous, tidy, and highly knowledgeable."},
        {"word": "friendly", "ipa": "/ˈfrend.li/", "pos": "adj", "meaning": "thân thiện, niềm nở", "example": "Homeowners appreciate our friendly customer service approach."},
        {"word": "technician", "ipa": "/tekˈnɪʃ.ən/", "pos": "n", "meaning": "kỹ thuật viên lành nghề", "example": "Experienced HVAC technicians resolve air conditioning faults quickly."}
    ],
    138: [
        {"word": "backed by", "ipa": "/bækt baɪ/", "pos": "adj phr", "meaning": "được bảo đảm bởi, cam kết bởi", "example": "All repair work and replacement parts are backed by a full 12-month warranty."},
        {"word": "money-back guarantee", "ipa": "/ˈmʌn.i bæk ˌɡær.ənˈtiː/", "pos": "n", "meaning": "cam kết hoàn tiền nếu không hài lòng", "example": "Our furnace installation services feature a complete money-back guarantee."},
        {"word": "warranty", "ipa": "/ˈwɒr.ən.ti/", "pos": "n", "meaning": "chế độ bảo hành", "example": "Keep your service invoice as proof of active warranty coverage."}
    ],
    139: [
        {"word": "vary", "ipa": "/ˈveə.ri/", "pos": "v", "meaning": "thay đổi, dao động tùy theo", "example": "Printing service rates will vary depending on page count and paper stock."},
        {"word": "raw materials", "ipa": "/rɔː məˈtɪə.ri.əlz/", "pos": "n pl", "meaning": "nguyên vật liệu đầu vào", "example": "Rising prices of raw materials prompted a general price adjustment."},
        {"word": "shipping cost", "ipa": "/ˈʃɪp.ɪŋ kɒst/", "pos": "n", "meaning": "chi phí vận tải cước hàng", "example": "International shipping costs have escalated significantly this quarter."}
    ],
    140: [
        {"word": "received", "ipa": "/rɪˈsiːvd/", "pos": "v-ed", "meaning": "được tiếp nhận, được gửi đến", "example": "All purchase orders received before March 15 will be honored at old rates."},
        {"word": "prior to", "ipa": "/ˈpraɪ.ər tuː/", "pos": "prep", "meaning": "trước ngày, trước thời điểm", "example": "Confirm your conference travel reservations prior to departure."},
        {"word": "apply", "ipa": "/əˈplaɪ/", "pos": "v", "meaning": "áp dụng bảng giá/quy định", "example": "Special bulk discounts apply to wholesale corporate purchases."}
    ],
    141: [
        {"word": "price list", "ipa": "/praɪs lɪst/", "pos": "n", "meaning": "bảng báo giá chi tiết", "example": "The updated service price list will be published on our corporate website."},
        {"word": "effective date", "ipa": "/ɪˈfek.tɪv deɪt/", "pos": "n", "meaning": "ngày có hiệu lực chính thức", "example": "The new tariff takes effect beginning March 20."},
        {"word": "notice", "ipa": "/ˈnəʊ.tɪs/", "pos": "n", "meaning": "thông báo gửi khách hàng", "example": "Post a notice explaining the revised fee schedule at checkout."}
    ],
    142: [
        {"word": "exceptional", "ipa": "/ɪkˈsep.ʃən.əl/", "pos": "adj", "meaning": "vượt trội, xuất sắc phi thường", "example": "We remain firmly committed to delivering exceptional print quality and service."},
        {"word": "dedication", "ipa": "/ˌded.ɪˈkeɪ.ʃən/", "pos": "n", "meaning": "sự cống hiến, tận tâm", "example": "Our team works with dedication to meet strict publishing standards."},
        {"word": "superior", "ipa": "/suːˈpɪə.ri.ər/", "pos": "adj", "meaning": "cao cấp hơn, chất lượng vượt bậc", "example": "Our presses yield superior color reproduction on glossy paper."}
    ],
    143: [
        {"word": "clientele", "ipa": "/ˌkliː.ɒnˈtel/", "pos": "n", "meaning": "tệp khách hàng, tập khách quen", "example": "Our gift shops attract an upscale, discerning clientele across urban hubs."},
        {"word": "exhibition", "ipa": "/ˌek.sɪˈbɪʃ.ən/", "pos": "n", "meaning": "buổi triển lãm trưng bày tác phẩm", "example": "I admired your handcrafted ceramic jewelry at last weekend's crafts exhibition."},
        {"word": "handcrafted", "ipa": "/ˌhændˈkrɑːf.tɪd/", "pos": "adj", "meaning": "chế tác thủ công tinh xảo", "example": "Shoppers seek out unique handcrafted artisanal home accessories."}
    ],
    144: [
        {"word": "reasonable price", "ipa": "/ˈriː.zən.ə.bəl praɪs/", "pos": "n", "meaning": "mức giá cả phải chăng, hợp lý", "example": "The reasonable prices make your handmade pieces an outstanding value."},
        {"word": "value", "ipa": "/ˈvæl.juː/", "pos": "n", "meaning": "giá trị thực tế mang lại", "example": "Customers look for high artistic value at fair market retail rates."},
        {"word": "originality", "ipa": "/əˌrɪdʒ.ənˈæl.ə.ti/", "pos": "n", "meaning": "tính độc đáo, tính nguyên bản", "example": "Buyers praised the originality and subtle color palette of her brooches."}
    ],
    145: [
        {"word": "double", "ipa": "/ˈdʌb.əl/", "pos": "v", "meaning": "nhân đôi, tăng gấp đôi số lượng", "example": "We plan to double our wholesale inventory orders for the holiday season."},
        {"word": "holiday season", "ipa": "/ˈhɒl.ə.deɪ ˌsiː.zən/", "pos": "n", "meaning": "mùa mua sắm lễ tết cuối năm", "example": "Retail turnover spikes substantially throughout the busy holiday season."},
        {"word": "wholesale order", "ipa": "/ˈhəʊl.seɪl ˈɔː.dər/", "pos": "n", "meaning": "đơn đặt hàng mua buôn/sỉ", "example": "Submit wholesale orders early to ensure guaranteed warehouse delivery."}
    ],
    146: [
        {"word": "partnership", "ipa": "/ˈpɑːt.nə.ʃɪp/", "pos": "n", "meaning": "mối quan hệ đối tác kinh doanh", "example": "An exclusive distribution partnership will bring mutual benefits to both of us."},
        {"word": "mutual benefit", "ipa": "/ˈmjuː.tʃu.əl ˈben.ɪ.fɪt/", "pos": "n", "meaning": "lợi ích đôi bên cùng có lợi", "example": "The joint venture creates mutual benefits for designers and retailers."},
        {"word": "exclusive agreement", "ipa": "/ɪkˈskluː.sɪv əˈɡriː.mənt/", "pos": "n", "meaning": "thỏa thuận độc quyền phân phối", "example": "They signed an exclusive agreement to market the brand nationwide."}
    ]
}

with open('scratch/t2_p5_p6_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(t2_p5_p6_vocab, f, ensure_ascii=False, indent=2)

print("Generated scratch/t2_p5_p6_vocab.json successfully!")
