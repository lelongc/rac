import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# High-yield, 100% authentic vocabulary for Test 3 Part 3 & Part 4 (Q32-Q100)
p3_p4_vocab = {
    # Q32-Q34: Moving offices
    32: [
        {"word": "relocate", "ipa": "/ˌriː.ləʊˈkeɪt/", "pos": "v", "meaning": "di dời, chuyển văn phòng", "example": "The company is relocating its headquarters to a more spacious building."},
        {"word": "move offices", "ipa": "/muːv ˈɒf.ɪ.sɪz/", "pos": "phr", "meaning": "chuyển địa điểm văn phòng", "example": "Staff are preparing for moving offices at the end of the year."},
        {"word": "spacious", "ipa": "/ˈspeɪ.ʃəs/", "pos": "adj", "meaning": "rộng rãi, thoáng đãng", "example": "The new office space will be much bigger and more spacious."}
    ],
    33: [
        {"word": "staffer", "ipa": "/ˈstɑːf.ər/", "pos": "n", "meaning": "nhân viên trong cơ quan/công ty", "example": "Management decided to hire additional staffers for the expanding department."},
        {"word": "workstation", "ipa": "/ˈwɜːkˌsteɪ.ʃən/", "pos": "n", "meaning": "bàn làm việc, góc làm việc", "example": "Each workstation is equipped with dual monitors and ergonomic chairs."},
        {"word": "expand", "ipa": "/ɪkˈspænd/", "pos": "v", "meaning": "mở rộng quy mô hoạt động", "example": "The design studio is expanding to accommodate new team members."}
    ],
    34: [
        {"word": "floor plan", "ipa": "/flɔːr plæn/", "pos": "n", "meaning": "sơ đồ bố trí mặt bằng các tầng", "example": "The architect shared the updated floor plan for the second floor."},
        {"word": "furniture", "ipa": "/ˈfɜː.nɪ.tʃər/", "pos": "n", "meaning": "đồ nội thất văn phòng (bàn ghế tủ)", "example": "New ergonomic furniture will be delivered next Thursday."},
        {"word": "department", "ipa": "/dɪˈpɑːt.mənt/", "pos": "n", "meaning": "phòng ban chuyên môn", "example": "The marketing department will occupy the east wing of the building."}
    ],

    # Q35-Q37: Southeast Medical Trade Show
    35: [
        {"word": "trade show", "ipa": "/ˈtreɪd ˌʃəʊ/", "pos": "n", "meaning": "hội chợ thương mại, triển lãm ngành", "example": "Exhibitors gathered at the Southeast Medical Trade Show to display new devices."},
        {"word": "organizer", "ipa": "/ˈɔː.ɡən.aɪ.zər/", "pos": "n", "meaning": "người tổ chức sự kiện/hội nghị", "example": "The journalist interviewed the event organizer about attendance figures."},
        {"word": "journalist", "ipa": "/ˈdʒɜː.nə.lɪst/", "pos": "n", "meaning": "nhà báo, phóng viên", "example": "The women are journalists covering healthcare technology for a newspaper."}
    ],
    36: [
        {"word": "interview", "ipa": "/ˈɪn.tə.vjuː/", "pos": "v, n", "meaning": "phỏng vấn; cuộc phỏng vấn", "example": "Reporters requested an interview with the keynote speaker."},
        {"word": "newspaper", "ipa": "/ˈnjuːzˌpeɪ.pər/", "pos": "n", "meaning": "tờ báo in, cơ quan thông tấn", "example": "The article about medical innovation will appear in Sunday's newspaper."},
        {"word": "exhibit", "ipa": "/ɪɡˈzɪb.ɪt/", "pos": "v, n", "meaning": "trưng bày; gian hàng triển lãm", "example": "Several biotech firms exhibit their latest surgical instruments."}
    ],
    37: [
        {"word": "medical equipment", "ipa": "/ˈmed.ɪ.kəl ɪˈkwɪp.mənt/", "pos": "n", "meaning": "trang thiết bị y tế chuyên dụng", "example": "The trade show features state-of-the-art diagnostic medical equipment."},
        {"word": "booth", "ipa": "/buːð/", "pos": "n", "meaning": "gian hàng trưng bày tại triển lãm", "example": "Visitors crowded around the demonstration booth to test the device."},
        {"word": "badge", "ipa": "/bædʒ/", "pos": "n", "meaning": "thẻ đeo khách tham quan hội chợ", "example": "Press members must display their media badge at all times."}
    ],

    # Q38-Q40: Redesigning Ace Bancorp Website
    38: [
        {"word": "redesign", "ipa": "/ˌriː.dɪˈzaɪn/", "pos": "v, n", "meaning": "thiết kế lại giao diện", "example": "I've been redesigning the website to integrate online banking functions."},
        {"word": "online banking", "ipa": "/ˌɒn.laɪn ˈbæŋ.kɪŋ/", "pos": "n", "meaning": "nghiệp vụ ngân hàng điện tử trực tuyến", "example": "Customers can transfer funds easily through the online banking portal."},
        {"word": "spare time", "ipa": "/speər taɪm/", "pos": "phr", "meaning": "dành ra chút thời gian rảnh", "example": "Can you spare 30 minutes after lunch to look over my project?"}
    ],
    39: [
        {"word": "streamlined", "ipa": "/ˈstriːm.laɪnd/", "pos": "adj", "meaning": "tối giản, hợp lý hóa, tinh gọn", "example": "The client requested streamlined navigation menus on the home page."},
        {"word": "redevelopment", "ipa": "/ˌriː.dɪˈvel.əp.mənt/", "pos": "n", "meaning": "sự phát triển lại, nâng cấp hoàn thiện", "example": "The engineer agreed to test out the web platform's redevelopment."},
        {"word": "home page", "ipa": "/ˈhəʊm ˌpeɪdʒ/", "pos": "n", "meaning": "trang chủ của trang web", "example": "Key service options are clearly visible on the redesigned home page."}
    ],
    40: [
        {"word": "client", "ipa": "/ˈklaɪ.ənt/", "pos": "n", "meaning": "khách hàng doanh nghiệp", "example": "The developer consulted the client before finalizing the mobile interface."},
        {"word": "function", "ipa": "/ˈfʌŋk.ʃən/", "pos": "n", "meaning": "tính năng, chức năng hệ thống", "example": "The banking app includes bill-pay and account alert functions."},
        {"word": "feedback", "ipa": "/ˈfiːd.bæk/", "pos": "n", "meaning": "ý kiến phản hồi góp ý", "example": "User feedback will help us identify bugs before the official release."}
    ],

    # Q41-Q43: Train Platform & Track Repairs
    41: [
        {"word": "platform", "ipa": "/ˈplæt.fɔːm/", "pos": "n", "meaning": "sân ga, ke ga đợi tàu", "example": "Passengers waited on platform 4 for the delayed express train."},
        {"word": "track", "ipa": "/træk/", "pos": "n", "meaning": "đường ray xe lửa", "example": "Railway crews are repairing tracks north of the central terminal."},
        {"word": "depart", "ipa": "/dɪˈpɑːt/", "pos": "v", "meaning": "khởi hành, rời ga", "example": "No trains are currently departing from this platform due to maintenance."}
    ],
    42: [
        {"word": "appointment", "ipa": "/əˈpɔɪnt.mənt/", "pos": "n", "meaning": "cuộc hẹn làm việc quan trọng", "example": "The commuter was upset because the railway delay made him late for an appointment."},
        {"word": "upset", "ipa": "/ʌpˈset/", "pos": "adj", "meaning": "khó chịu, bực bội lo lắng", "example": "Passengers grew upset when the announcement confirmed cancellation."},
        {"word": "delay", "ipa": "/dɪˈleɪ/", "pos": "n, v", "meaning": "sự chậm trễ; làm chậm hoãn", "example": "Unexpected track work caused significant delays on commuter routes."}
    ],
    43: [
        {"word": "shuttle bus", "ipa": "/ˈʃʌt.əl bʌs/", "pos": "n", "meaning": "xe buýt trung chuyển tuyến ngắn", "example": "Transit authorities are providing free shuttle buses between stations."},
        {"word": "alternative", "ipa": "/ɒlˈtɜː.nə.tɪv/", "pos": "adj, n", "meaning": "phương án thay thế", "example": "Station staff suggested an alternative travel route via bus."},
        {"word": "passenger", "ipa": "/ˈpæs.ən.dʒər/", "pos": "n", "meaning": "hành khách đi tàu xe", "example": "Staff guided stranded passengers to the designated bus stop."}
    ],

    # Q44-Q46: Bike Racks & Investors
    44: [
        {"word": "investor", "ipa": "/ɪnˈves.tər/", "pos": "n", "meaning": "nhà đầu tư vốn", "example": "The entrepreneur pitched his startup idea to venture capital investors."},
        {"word": "space-saving", "ipa": "/ˈspeɪsˌseɪ.vɪŋ/", "pos": "adj", "meaning": "tiết kiệm không gian, diện tích", "example": "He designed a space-saving bike rack specifically for small urban apartments."},
        {"word": "storing", "ipa": "/ˈstɔː.rɪŋ/", "pos": "n, v", "meaning": "việc cất giữ, lưu trữ đồ đạc", "example": "Storing bicycles in compact studio apartments can be challenging."}
    ],
    45: [
        {"word": "bicycle rack", "ipa": "/ˈbaɪ.sɪ.kəl ræk/", "pos": "n", "meaning": "giá đỡ, kệ treo xe đạp", "example": "The indoor bicycle rack can be mounted securely to any drywall surface."},
        {"word": "adjustable", "ipa": "/əˈdʒʌs.tə.bəl/", "pos": "adj", "meaning": "có thể điều chỉnh linh hoạt", "example": "His product can be adjusted to fit diverse frame sizes and styles."},
        {"word": "unique", "ipa": "/juːˈniːk/", "pos": "adj", "meaning": "độc đáo, đặc sắc riêng có", "example": "What makes this bike rack unique is its customizable arm length."}
    ],
    46: [
        {"word": "patent", "ipa": "/ˈpeɪ.tənt/", "pos": "n, v", "meaning": "bằng sáng chế; đăng ký phát minh", "example": "The inventor applied for an international patent to protect his design."},
        {"word": "prototype", "ipa": "/ˈprəʊ.tə.taɪp/", "pos": "n", "meaning": "mẫu thử nghiệm đầu tiên", "example": "Investors inspected a working prototype during the demonstration."},
        {"word": "commercialize", "ipa": "/kəˈmɜː.ʃəl.aɪz/", "pos": "v", "meaning": "thương mại hóa sản phẩm", "example": "Funding will help the company commercialize the product within months."}
    ],

    # Q47-Q49: Interview at Central Bank
    47: [
        {"word": "studio", "ipa": "/ˈstjuː.di.əʊ/", "pos": "n", "meaning": "phòng thu âm, phim trường ghi hình", "example": "It's time to pack up equipment, leave the studio, and head to the bank."},
        {"word": "central bank", "ipa": "/ˌsen.trəl ˈbæŋk/", "pos": "n", "meaning": "ngân hàng trung ương", "example": "The news crew scheduled an interview with the governor of the central bank."},
        {"word": "head over", "ipa": "/hed ˈəʊ.vər/", "pos": "phr v", "meaning": "đi sang, di chuyển đến", "example": "Let's head over to the financial district early to beat traffic."}
    ],
    48: [
        {"word": "camera", "ipa": "/ˈkæm.rə/", "pos": "n", "meaning": "máy quay phim, máy ảnh chuyên nghiệp", "example": "Alberto confirmed that all video cameras and tripods were packed in the van."},
        {"word": "interview", "ipa": "/ˈɪn.tə.vjuː/", "pos": "n", "meaning": "cuộc phỏng vấn truyền hình", "example": "The broadcast journalist prepared questions for the high-profile interview."},
        {"word": "director", "ipa": "/daɪˈrek.tər/", "pos": "n", "meaning": "giám đốc, người đứng đầu", "example": "The interview will focus on the bank director's monetary outlook."}
    ],
    49: [
        {"word": "equipment", "ipa": "/ɪˈkwɪp.mənt/", "pos": "n", "meaning": "thiết bị quay phim, máy móc chuyên dùng", "example": "The crew loaded sound and lighting equipment into the company vehicle."},
        {"word": "broadcast", "ipa": "/ˈbrɔːd.kɑːst/", "pos": "n, v", "meaning": "chương trình phát sóng; phát thanh truyền hình", "example": "The recorded conversation will be broadcast on the evening news."},
        {"word": "schedule", "ipa": "/ˈskedʒ.uːl/", "pos": "n", "meaning": "lịch trình công tác", "example": "The media crew adhered strictly to their tight shooting schedule."}
    ],

    # Q50-Q52: Sabine Hoffman's Retirement Party
    50: [
        {"word": "retirement party", "ipa": "/rɪˈtaɪə.mənt ˈpɑː.ti/", "pos": "n", "meaning": "bữa tiệc chia tay về hưu", "example": "Preparations are underway for Sabine Hoffman's retirement party."},
        {"word": "preparation", "ipa": "/ˌprep.ərˈeɪ.ʃən/", "pos": "n", "meaning": "sự chuẩn bị, công tác tổ chức", "example": "Colleagues inquired how party preparations were progressing."},
        {"word": "celebrate", "ipa": "/ˈsel.ə.breɪt/", "pos": "v", "meaning": "kỷ niệm, tôn vinh cống hiến", "example": "Staff gathered to celebrate Sabine's thirty years of dedicated service."}
    ],
    51: [
        {"word": "caterer", "ipa": "/ˈkeɪ.tər.ər/", "pos": "n", "meaning": "nhà cung cấp dịch vụ tiệc ăn uống", "example": "The organizer booked a private hall and called the caterer for appetizers."},
        {"word": "book a room", "ipa": "/bʊk ə ruːm/", "pos": "phr", "meaning": "đặt trước một phòng họp/tiệc", "example": "I've already booked a spacious conference room for the celebration."},
        {"word": "invite", "ipa": "/ɪnˈvaɪt/", "pos": "v", "meaning": "mời tham dự", "example": "Formal invitations were emailed to all department colleagues."}
    ],
    52: [
        {"word": "former colleague", "ipa": "/ˈfɔː.mər ˈkɒl.iːɡ/", "pos": "n phr", "meaning": "đồng nghiệp cũ từng làm chung", "example": "Sabine would love to catch up with former colleagues from other divisions."},
        {"word": "gift", "ipa": "/ɡɪft/", "pos": "n", "meaning": "món quà tri ân", "example": "Team members contributed toward a commemorative farewell gift."},
        {"word": "speech", "ipa": "/spiːtʃ/", "pos": "n", "meaning": "bài phát biểu chia tay", "example": "The division head gave an emotional farewell speech honoring Sabine."}
    ],

    # Q53-Q55: Kota Ogawa at Hotel Facilities
    53: [
        {"word": "retreat", "ipa": "/rɪˈtriːt/", "pos": "n", "meaning": "chuyến dã ngoại công ty, hội nghị nghỉ dưỡng", "example": "Langston Limited is organizing an upcoming corporate retreat for executives."},
        {"word": "facilities", "ipa": "/fəˈsɪl.ə.tiz/", "pos": "n pl", "meaning": "cơ sở vật chất, tiện nghi khách sạn", "example": "Mr. Ogawa arrived to view the hotel's meeting and banquet facilities."},
        {"word": "appointment", "ipa": "/əˈpɔɪnt.mənt/", "pos": "n", "meaning": "cuộc hẹn đã định trước", "example": "I have a scheduled appointment with Ms. Ishikawa at 10:00 A.M."}
    ],
    54: [
        {"word": "wrap up", "ipa": "/ræp ʌp/", "pos": "phr v", "meaning": "kết thúc gọn ghẽ, hoàn tất", "example": "The manager just wrapped up an urgent telephone call with headquarters."},
        {"word": "expecting", "ipa": "/ɪkˈspek.tɪŋ/", "pos": "v", "meaning": "đang chờ đón, mong đợi", "example": "The receptionist confirmed that Ms. Ishikawa was expecting Mr. Ogawa."},
        {"word": "urgent", "ipa": "/ˈɜː.dʒənt/", "pos": "adj", "meaning": "khẩn cấp, cấp thiết", "example": "She had to resolve an urgent client matter before starting the tour."}
    ],
    55: [
        {"word": "banquet room", "ipa": "/ˈbæŋ.kwɪt ruːm/", "pos": "n", "meaning": "phòng tiệc lớn của khách sạn", "example": "The hotel representative showed the client their premier banquet room."},
        {"word": "accommodate", "ipa": "/əˈkɒm.ə.deɪt/", "pos": "v", "meaning": "chứa được, đáp ứng sức chứa", "example": "The ballroom can easily accommodate up to 200 conference guests."},
        {"word": "amenities", "ipa": "/əˈmiː.nə.tiz/", "pos": "n pl", "meaning": "các dịch vụ tiện ích đi kèm", "example": "The resort offers high-speed Wi-Fi, audio equipment, and fitness amenities."}
    ],

    # Q56-Q58: Pineapple Slicing Machine at Grocery
    56: [
        {"word": "fruit aisle", "ipa": "/fruːt aɪl/", "pos": "n", "meaning": "quầy / gian hàng hoa quả tươi", "example": "A novel pineapple-slicing machine was installed in the fruit aisle."},
        {"word": "sales increase", "ipa": "/seɪlz ɪnˈkriːs/", "pos": "n phr", "meaning": "doanh số bán hàng tăng trưởng mạnh", "example": "Sales of whole pineapples went up significantly after adding the device."},
        {"word": "install", "ipa": "/ɪnˈstɔːl/", "pos": "v", "meaning": "lắp đặt máy móc thiết bị", "example": "Management plans to install similar automated slicers in other branches."}
    ],
    57: [
        {"word": "peel", "ipa": "/piːl/", "pos": "v", "meaning": "gọt vỏ trái cây", "example": "Shoppers enjoy watching the automated machine peel and core pineapples."},
        {"word": "slice", "ipa": "/slaɪs/", "pos": "v, n", "meaning": "cắt lát mỏng; lát cắt", "example": "The device can slice an entire fruit in less than thirty seconds."},
        {"word": "unique experience", "ipa": "/juːˈniːk ɪkˈspɪə.ri.əns/", "pos": "n phr", "meaning": "trải nghiệm mua sắm độc đáo thú vị", "example": "Watching the fruit prep machine provides a unique experience for shoppers."}
    ],
    58: [
        {"word": "branch", "ipa": "/brɑːntʃ/", "pos": "n", "meaning": "chi nhánh cửa hàng siêu thị", "example": "The grocery chain operates three supermarket branches across the city."},
        {"word": "customer satisfaction", "ipa": "/ˈkʌs.tə.mər ˌsæt.ɪsˈfæk.ʃən/", "pos": "n", "meaning": "sự hài lòng thỏa mãn của khách hàng", "example": "Adding convenient services boosted overall customer satisfaction."},
        {"word": "produce department", "ipa": "/ˈprɒd.juːs dɪˈpɑːt.mənt/", "pos": "n", "meaning": "khu vực bán nông sản thực phẩm tươi", "example": "Fresh local fruits are featured prominently in the produce department."}
    ],

    # Q59-Q61: Dental Clinic Appointment Cancellations
    59: [
        {"word": "dental appointment", "ipa": "/ˈden.təl əˈpɔɪnt.mənt/", "pos": "n", "meaning": "cuộc hẹn khám răng tại nha khoa", "example": "Three patients had to cancel their dental appointments at the last minute."},
        {"word": "at the last minute", "ipa": "/æt ðə lɑːst ˈmɪn.ɪt/", "pos": "phr", "meaning": "vào phút chót, ngay sát giờ hẹn", "example": "Late cancellations make it difficult to fill empty consultation slots."},
        {"word": "patient", "ipa": "/ˈpeɪ.ʃənt/", "pos": "n", "meaning": "bệnh nhân đến khám chữa bệnh", "example": "Other registered patients could have taken those canceled appointment slots."}
    ],
    60: [
        {"word": "notification", "ipa": "/ˌnəʊ.tɪ.fɪˈkeɪ.ʃən/", "pos": "n", "meaning": "thông báo tin nhắn tự động", "example": "The clinic enabled text notifications to alert clients of sudden openings."},
        {"word": "schedule online", "ipa": "/ˈskedʒ.uːl ˌɒnˈlaɪn/", "pos": "phr", "meaning": "đặt lịch hẹn trực tuyến qua web", "example": "Patients can easily schedule a doctor's visit online anytime."},
        {"word": "waitlist", "ipa": "/ˈweɪt.lɪst/", "pos": "n", "meaning": "danh sách chờ xếp lượt", "example": "Staff maintain an active waitlist to quickly reassign open appointment hours."}
    ],
    61: [
        {"word": "policy", "ipa": "/ˈpɒl.ə.si/", "pos": "n", "meaning": "quy định chính sách hủy hẹn", "example": "The clinic instituted a 24-hour cancellation policy to reduce no-shows."},
        {"word": "reminder", "ipa": "/rɪˈmaɪn.dər/", "pos": "n", "meaning": "tin nhắn nhắc nhở lịch hẹn", "example": "Automated SMS reminders help patients remember scheduled cleanings."},
        {"word": "remedy", "ipa": "/ˈrem.ə.di/", "pos": "v, n", "meaning": "khắc phục xử lý; biện pháp giải quyết", "example": "Adopting digital scheduling remedied the lost clinic revenue issue."}
    ],

    # Q62-Q64: New Year Employee Gifts
    62: [
        {"word": "employee gift", "ipa": "/ɪmˈplɔɪ.iː ɡɪft/", "pos": "n", "meaning": "quà tặng tri ân nhân viên", "example": "The manager looked for a thoughtful New Year employee gift."},
        {"word": "hard work", "ipa": "/hɑːd wɜːk/", "pos": "n", "meaning": "sự nỗ lực làm việc chăm chỉ", "example": "The company presented gifts to thank staff for their dedication and hard work."},
        {"word": "appreciation", "ipa": "/əˌpriː.ʃiˈeɪ.ʃən/", "pos": "n", "meaning": "sự cảm kích, ghi nhận đóng góp", "example": "Giving seasonal presents is a great way to show worker appreciation."}
    ],
    63: [
        {"word": "travel mug", "ipa": "/ˈtræv.əl mʌɡ/", "pos": "n", "meaning": "cốc giữ nhiệt mang đi làm", "example": "A high-quality stainless steel travel mug makes a practical corporate gift."},
        {"word": "brochure", "ipa": "/ˈbrəʊ.ʃər/", "pos": "n", "meaning": "cuốn cẩm nang giới thiệu sản phẩm", "example": "Raquel handed him a vendor brochure showcasing diverse mug designs."},
        {"word": "variety", "ipa": "/vəˈraɪ.ə.ti/", "pos": "n", "meaning": "sự đa dạng phong phú mẫu mã", "example": "The catalog offers a wide variety of scenic patterns and brand logos."}
    ],
    64: [
        {"word": "customized", "ipa": "/ˈkʌs.tə.maɪzd/", "pos": "adj", "meaning": "được in khắc theo yêu cầu riêng", "example": "Mugs can be customized with employee names and corporate colors."},
        {"word": "bulk discount", "ipa": "/bʌlk ˈdɪs.kaʊnt/", "pos": "n", "meaning": "mức chiết khấu mua số lượng lớn", "example": "Ordering 100 mugs qualifies the firm for an attractive bulk discount."},
        {"word": "order", "ipa": "/ˈɔː.dər/", "pos": "v, n", "meaning": "đặt mua; đơn đặt hàng", "example": "The supervisor submitted the merchandise order before the holiday deadline."}
    ],

    # Q65-Q67: Film Shoot Driving Scene
    65: [
        {"word": "film shoot", "ipa": "/fɪlm ʃuːt/", "pos": "n", "meaning": "buổi quay phim tại bối cảnh", "example": "The crew coordinated logistics for next week's on-location film shoot."},
        {"word": "driving scene", "ipa": "/ˈdraɪ.vɪŋ siːn/", "pos": "n", "meaning": "cảnh quay lái xe trên đường", "example": "Actors will film an intense driving scene heading north on Maple Street."},
        {"word": "film industry", "ipa": "/fɪlm ˈɪn.dəs.tri/", "pos": "n", "meaning": "ngành công nghiệp điện ảnh làm phim", "example": "The speakers work as production crew members in the film industry."}
    ],
    66: [
        {"word": "camera operator", "ipa": "/ˈkæm.rə ˈɒp.ər.eɪ.tər/", "pos": "n", "meaning": "quay phim viên, người vận hành máy quay", "example": "Camera operators need unobstructed visibility to track vehicle motion."},
        {"word": "actor", "ipa": "/ˈæk.tər/", "pos": "n", "meaning": "diễn viên diễn xuất", "example": "Lead actors practiced the timing of their dialogue before shooting resumed."},
        {"word": "follow the action", "ipa": "/ˈfɒl.əʊ ði ˈæk.ʃən/", "pos": "phr", "meaning": "lia máy theo dõi chuyển động hành động", "example": "Modifying the car route makes it easier for cameras to follow the action."}
    ],
    67: [
        {"word": "permit", "ipa": "/ˈpɜː.mɪt/", "pos": "n", "meaning": "giấy phép quay phim / sử dụng đường bộ", "example": "The location manager secured a street closure permit from city hall."},
        {"word": "route", "ipa": "/ruːt/", "pos": "n", "meaning": "lộ trình xe chạy trên trường quay", "example": "The director altered the driving route to avoid congested traffic intersections."},
        {"word": "lighting", "ipa": "/ˈlaɪ.tɪŋ/", "pos": "n", "meaning": "ánh sáng trường quay, bố trí chiếu sáng", "example": "Adjusting the vehicle trajectory ensured optimal morning natural lighting."}
    ],

    # Q68-Q70: Video Game Launch & Glitch
    68: [
        {"word": "video game", "ipa": "/ˈvɪd.i.əʊ ˌɡeɪm/", "pos": "n", "meaning": "trò chơi điện tử trên máy tính/console", "example": "The developers discussed final polish for the video game they are launching."},
        {"word": "launch", "ipa": "/lɔːntʃ/", "pos": "v, n", "meaning": "phát hành, ra mắt chính thức", "example": "The studio plans to launch the multiplayer action game next month."},
        {"word": "software development", "ipa": "/ˈsɒft.weər dɪˈvel.əp.mənt/", "pos": "n", "meaning": "phát triển và lập trình phần mềm", "example": "The colleagues collaborate closely in video game software development."}
    ],
    69: [
        {"word": "glitch", "ipa": "/ɡlɪtʃ/", "pos": "n", "meaning": "lỗi phần mềm kỹ thuật đột ngột", "example": "Testers discovered a visual glitch during the underwater temple sequence."},
        {"word": "gameplay", "ipa": "/ˈɡeɪm.pleɪ/", "pos": "n", "meaning": "lối chơi, trải nghiệm vận hành game", "example": "Smooth gameplay is crucial for keeping players engaged across levels."},
        {"word": "layout", "ipa": "/ˈleɪ.aʊt/", "pos": "n", "meaning": "bố cục bản đồ, thiết kế không gian", "example": "While reviewing the level layout, she identified an unexpected bug."}
    ],
    70: [
        {"word": "fix a bug", "ipa": "/fɪks ə bʌɡ/", "pos": "phr", "meaning": "sửa lỗi lập trình phần mềm", "example": "The programmers spent the weekend fixing bugs prior to submission."},
        {"word": "testing phase", "ipa": "/ˈtes.tɪŋ feɪz/", "pos": "n", "meaning": "giai đoạn thử nghiệm chất lượng", "example": "Rigorous beta testing ensures high performance upon commercial release."},
        {"word": "character", "ipa": "/ˈkær.ək.tər/", "pos": "n", "meaning": "nhân vật trong trò chơi", "example": "Players control a character navigating through an ancient submerged ruin."}
    ],

    # Q71-Q73: Volkov Tire and Auto Service
    71: [
        {"word": "automotive service", "ipa": "/ˌɔː.təˈməʊ.tɪv ˈsɜː.vɪs/", "pos": "n", "meaning": "dịch vụ sửa chữa bảo dưỡng ô tô", "example": "Volkov Tire provides professional automotive service to Livingstone Valley."},
        {"word": "tire replacement", "ipa": "/taɪər rɪˈpleɪs.mənt/", "pos": "n", "meaning": "thay thế lốp xe ô tô", "example": "The garage offers complete wheel alignments and tire replacement specials."},
        {"word": "mechanic", "ipa": "/məˈkæn.ɪk/", "pos": "n", "meaning": "thợ sửa xe máy/ô tô", "example": "Certified mechanics inspect every vehicle before returning it to the owner."}
    ],
    72: [
        {"word": "brake inspection", "ipa": "/breɪk ɪnˈspek.ʃən/", "pos": "n", "meaning": "kiểm tra hệ thống phanh xe", "example": "Receive a complimentary brake inspection with every standard oil change."},
        {"word": "discount coupon", "ipa": "/ˈdɪs.kaʊnt ˈkuː.pɒn/", "pos": "n", "meaning": "phiếu giảm giá dịch vụ", "example": "Listeners can present our radio discount coupon to save $20 on repairs."},
        {"word": "maintain", "ipa": "/meɪnˈteɪn/", "pos": "v", "meaning": "bảo trì, giữ gìn phương tiện", "example": "Regular tune-ups help maintain optimal engine performance and safety."}
    ],
    73: [
        {"word": "serve the area", "ipa": "/sɜːv ði ˈeə.ri.ə/", "pos": "phr", "meaning": "phục vụ cộng đồng cư dân khu vực", "example": "We have been proud to serve the local community for over fifteen years."},
        {"word": "guarantee", "ipa": "/ˌɡær.ənˈtiː/", "pos": "n, v", "meaning": "cam kết bảo hành chất lượng", "example": "All automotive repairs come with a twelve-month parts and labor guarantee."},
        {"word": "appointment", "ipa": "/əˈpɔɪnt.mənt/", "pos": "n", "meaning": "lịch hẹn mang xe đến sửa", "example": "Call our service desk today to book a convenient morning appointment."}
    ],

    # Q74-Q76: Social Media Marketing Podcast
    74: [
        {"word": "podcast episode", "ipa": "/ˈpɒd.kɑːst ˈep.ɪ.səʊd/", "pos": "n", "meaning": "tập phát sóng của chương trình podcast", "example": "Today's podcast episode explores the nuances of social media marketing."},
        {"word": "marketing strategy", "ipa": "/ˈmɑː.kɪ.tɪŋ ˈstræt.ə.dʒi/", "pos": "n", "meaning": "chiến lược tiếp thị kinh doanh", "example": "Small enterprises rely on digital marketing strategies to reach young buyers."},
        {"word": "possibilities and limitations", "ipa": "/ˌpɒs.əˈbɪl.ə.tiz ənd ˌlɪm.ɪˈteɪ.ʃənz/", "pos": "n phr", "meaning": "những tiềm năng và giới hạn", "example": "The host analyzed the possibilities and limitations of influencer advertising."}
    ],
    75: [
        {"word": "complicated ideas", "ipa": "/ˈkɒm.plɪ.keɪ.tɪd aɪˈdɪəz/", "pos": "n pl", "meaning": "những khái niệm / ý tưởng phức tạp", "example": "Ms. Bertrand excels at explaining complicated ideas in relatable language."},
        {"word": "explain", "ipa": "/ɪkˈspleɪn/", "pos": "v", "meaning": "giải thích, diễn giải rõ ràng", "example": "The guest speaker explained how algorithms prioritize sponsored video posts."},
        {"word": "clarity", "ipa": "/ˈklær.ə.ti/", "pos": "n", "meaning": "sự rõ ràng, tính dễ hiểu", "example": "Listeners praised the presentation for its analytical clarity and real examples."}
    ],
    76: [
        {"word": "survey results", "ipa": "/ˈsɜː.veɪ rɪˈzʌlts/", "pos": "n pl", "meaning": "kết quả thu được từ cuộc khảo sát", "example": "Next up, the host will reveal survey results regarding customer brand trust."},
        {"word": "discuss next", "ipa": "/dɪˈskʌs nekst/", "pos": "phr", "meaning": "thảo luận trong phần tiếp theo", "example": "Stay tuned as we discuss consumer feedback metrics in our next segment."},
        {"word": "audience", "ipa": "/ˈɔː.di.əns/", "pos": "n", "meaning": "thính giả theo dõi chương trình", "example": "Over fifty thousand listeners tuned in to the weekly live marketing podcast."}
    ],

    # Q77-Q79: Potted Plants Delivery & Office Productivity
    77: [
        {"word": "potted plant", "ipa": "/ˈpɒt.ɪd plɑːnt/", "pos": "n", "meaning": "cây cảnh trồng trong chậu", "example": "The delivery service brought fifty potted plants to brighten up the office."},
        {"word": "brighten up", "ipa": "/ˈbraɪ.tən ʌp/", "pos": "phr v", "meaning": "làm rạng rỡ, làm sinh động không gian", "example": "Green foliage helps brighten up common reception and cafeteria spaces."},
        {"word": "common area", "ipa": "/ˈkɒm.ən ˈeə.ri.ə/", "pos": "n", "meaning": "khu vực sinh hoạt chung của cơ quan", "example": "Plants placed in common areas create a welcoming corporate atmosphere."}
    ],
    78: [
        {"word": "workplace productivity", "ipa": "/ˈwɜːk.pleɪs ˌprɒd.ʌkˈtɪv.ə.ti/", "pos": "n", "meaning": "năng suất làm việc tại công sở", "example": "Studies demonstrate that indoor greenery increases overall workplace productivity."},
        {"word": "stress reliever", "ipa": "/stres rɪˈliː.vər/", "pos": "n", "meaning": "biện pháp xoa dịu, giải tỏa căng thẳng", "example": "Natural plants act as natural stress relievers during intense project cycles."},
        {"word": "surroundings", "ipa": "/səˈraʊn.dɪŋz/", "pos": "n pl", "meaning": "không gian môi trường xung quanh", "example": "Pleasant office surroundings enhance employee well-being and job satisfaction."}
    ],
    79: [
        {"word": "catalog", "ipa": "/ˈkæt.əl.ɒɡ/", "pos": "n", "meaning": "cuốn danh mục sản phẩm cây cảnh", "example": "Staff can browse the nursery catalog in the break room to pick their desk plant."},
        {"word": "staff room", "ipa": "/stɑːf ruːm/", "pos": "n", "meaning": "phòng nghỉ giải lao của nhân viên", "example": "The order sign-up form and product catalog are located on the staff room table."},
        {"word": "cover the cost", "ipa": "/ˈkʌv.ər ðə kɒst/", "pos": "phr", "meaning": "chi trả, đài thọ toàn bộ chi phí", "example": "The company will cover the cost for one personal desktop plant per employee."}
    ],

    # Q80-Q82: Abandoned Shoe Factory Makeover
    80: [
        {"word": "abandoned factory", "ipa": "/əˈbæn.dənd ˈfæk.tər.i/", "pos": "n", "meaning": "nhà xưởng cũ bị bỏ hoang", "example": "The abandoned shoe factory in the central district had stood empty for three years."},
        {"word": "makeover", "ipa": "/ˈmeɪkˌəʊ.vər/", "pos": "n", "meaning": "công cuộc tân trang, đổi mới diện mạo", "example": "The historic brick complex is finally undergoing an extensive architectural makeover."},
        {"word": "central business district", "ipa": "/ˌsen.trəl ˈbɪz.nɪs ˈdɪs.trɪkt/", "pos": "n", "meaning": "trung tâm tài chính / thương mại thành phố (CBD)", "example": "New housing developments revitalize urban life in the central business district."}
    ],
    81: [
        {"word": "real estate developer", "ipa": "/ˈrɪəl ɪˌsteɪt dɪˈvel.ə.pər/", "pos": "n", "meaning": "nhà phát triển dự án bất động sản", "example": "Town council voted to sell the property to real estate developer Matthew Hughes."},
        {"word": "convert into", "ipa": "/kənˈvɜːt ˈɪn.tuː/", "pos": "phr v", "meaning": "chuyển đổi công năng thành", "example": "The developer plans to convert the industrial loft into ten modern family apartments."},
        {"word": "town council", "ipa": "/taʊn ˈkaʊn.səl/", "pos": "n", "meaning": "hội đồng nhân dân thành phố / thị trấn", "example": "The town council approved zoning permits after reviewing community feedback."}
    ],
    82: [
        {"word": "local news", "ipa": "/ˈləʊ.kəl njuːz/", "pos": "n", "meaning": "bản tin thời sự địa phương", "example": "Stay tuned to our local news broadcast for city traffic and transit reports."},
        {"word": "hear next", "ipa": "/hɪər nekst/", "pos": "phr", "meaning": "lắng nghe trong phần tin tiếp theo", "example": "Listeners will hear a brief weather forecast right after the commercial break."},
        {"word": "commercial break", "ipa": "/kəˈmɜː.ʃəl breɪk/", "pos": "n", "meaning": "khoảng dừng phát quảng cáo", "example": "Our sports reporter will join us following this quick thirty-second commercial break."}
    ],

    # Q83-Q85: Springdale Bridge Replacement Update
    83: [
        {"word": "bridge replacement", "ipa": "/brɪdʒ rɪˈpleɪs.mənt/", "pos": "n", "meaning": "dự án thay thế xây cầu mới", "example": "The director provided an official update on the Springdale bridge replacement project."},
        {"word": "transportation agency", "ipa": "/ˌtræn.spɔːˈteɪ.ʃən ˈeɪ.dʒən.si/", "pos": "n", "meaning": "sở giao thông vận tải", "example": "Agency engineers met to review infrastructure spending across the municipality."},
        {"word": "update", "ipa": "/ˈʌp.deɪt/", "pos": "n, v", "meaning": "bản cập nhật tiến độ; cập nhật", "example": "She shared a timeline update regarding river crossing construction milestones."}
    ],
    84: [
        {"word": "explain a delay", "ipa": "/ɪkˈspleɪn ə dɪˈleɪ/", "pos": "phr", "meaning": "giải thích lý do chậm trễ tiến độ", "example": "The speaker noted multiple concurrent jobs to explain the project delay."},
        {"word": "completion date", "ipa": "/kəmˈpliː.ʃən deɪt/", "pos": "n", "meaning": "ngày hoàn công dự kiến", "example": "The bridge is already six months past its original scheduled completion date."},
        {"word": "concurrent", "ipa": "/kənˈkʌr.ənt/", "pos": "adj", "meaning": "diễn ra đồng thời nhiều việc", "example": "Managing concurrent highway repairs stretched available engineering crews thin."}
    ],
    85: [
        {"word": "opening ceremony", "ipa": "/ˈəʊ.pən.ɪŋ ˈser.ɪ.mə.ni/", "pos": "n", "meaning": "lễ khánh thành đưa vào sử dụng", "example": "Officials discussed organizing a formal opening ceremony when the bridge opens."},
        {"word": "public announcement", "ipa": "/ˈpʌb.lɪk əˈnaʊns.mənt/", "pos": "n", "meaning": "thông cáo rộng rãi tới công chúng", "example": "The agency released a public announcement detailing detour routes during paving."},
        {"word": "infrastructure", "ipa": "/ˈɪn.frəˌstrʌk.tʃər/", "pos": "n", "meaning": "hạ tầng cơ sở kỹ thuật", "example": "Long-term investment modernizes bridges, roadways, and public transit links."}
    ],

    # Q86-Q88: Leadership Skills Workshop for Entrepreneurs
    86: [
        {"word": "leadership skills", "ipa": "/ˈliː.də.ʃɪp skɪlz/", "pos": "n pl", "meaning": "các kỹ năng lãnh đạo điều hành", "example": "The weekend seminar focuses on developing core leadership skills for founders."},
        {"word": "entrepreneur", "ipa": "/ˌɒn.trə.prəˈnɜːr/", "pos": "n", "meaning": "doanh nhân khởi nghiệp", "example": "Ambitious tech entrepreneurs shared strategies for team motivation and growth."},
        {"word": "work in pairs", "ipa": "/wɜːk ɪn peəz/", "pos": "phr", "meaning": "làm việc theo cặp hai người", "example": "Unlike yesterday's group talk, participants will work in pairs today."}
    ],
    87: [
        {"word": "communication skills", "ipa": "/kəˌmjuː.nɪˈkeɪ.ʃən skɪlz/", "pos": "n pl", "meaning": "kỹ năng giao tiếp truyền thông", "example": "Today's practical session emphasizes improving internal communication skills."},
        {"word": "goal setting", "ipa": "/ɡəʊl ˈset.ɪŋ/", "pos": "n", "meaning": "hoạch định và thiết lập mục tiêu", "example": "Yesterday's workshop focused on strategic goal setting for growing ventures."},
        {"word": "workshop session", "ipa": "/ˈwɜːk.ʃɒp ˈseʃ.ən/", "pos": "n", "meaning": "phiên tập huấn chuyên đề", "example": "Attendees participated enthusiastically in the afternoon workshop session."}
    ],
    88: [
        {"word": "catered lunch", "ipa": "/ˈkeɪ.təd lʌntʃ/", "pos": "n", "meaning": "bữa trưa được đặt tiệc phục vụ", "example": "The speaker informed the group that a healthy vegetarian lunch would be provided."},
        {"word": "vegetarian", "ipa": "/ˌvedʒ.ɪˈteə.ri.ən/", "pos": "adj", "meaning": "ăn chay, món chay thanh đạm", "example": "The buffet features delicious vegetarian soups, wraps, and grain salads."},
        {"word": "break", "ipa": "/breɪk/", "pos": "n", "meaning": "giờ nghỉ giải lao giữa buổi", "example": "Participants can network during the one-hour lunch break in the courtyard."}
    ],

    # Q89-Q91: Adisa from Car Pro (Sluggish Sedan)
    89: [
        {"word": "auto mechanic", "ipa": "/ˈɔː.təʊ məˌkæn.ɪk/", "pos": "n", "meaning": "thợ kỹ thuật cơ khí ô tô", "example": "The speaker works as an experienced auto mechanic at Car Pro repair shop."},
        {"word": "sedan", "ipa": "/sɪˈdæn/", "pos": "n", "meaning": "xe ô tô con 4-5 chỗ", "example": "The customer called reporting that her four-door sedan was running poorly."},
        {"word": "return a call", "ipa": "/rɪˈtɜːn ə kɔːl/", "pos": "phr", "meaning": "gọi điện thoại lại cho khách", "example": "This is Adisa returning your voicemail concerning the vehicle diagnostics."}
    ],
    90: [
        {"word": "sluggish", "ipa": "/ˈslʌɡ.ɪʃ/", "pos": "adj", "meaning": "chậm chạp, ì ạch, máy yếu", "example": "The owner noted that the vehicle felt sluggish and was hesitant to accelerate."},
        {"word": "accelerate", "ipa": "/əkˈsel.ə.reɪt/", "pos": "v", "meaning": "tăng tốc độ, đạp ga tăng vận tốc", "example": "A faulty sensor prevented the engine from accelerating smoothly on hills."},
        {"word": "take a look", "ipa": "/teɪk ə lʊk/", "pos": "phr", "meaning": "xem xét kiểm tra kỹ lưỡng", "example": "The technician cannot quote a final cost until he can take a look under the hood."}
    ],
    91: [
        {"word": "oil filter", "ipa": "/ɔɪl ˈfɪl.tər/", "pos": "n", "meaning": "bộ lọc dầu động cơ xe", "example": "Replacing a clogged oil filter is a fast and inexpensive service procedure."},
        {"word": "business hours", "ipa": "/ˈbɪz.nɪs aʊəz/", "pos": "n pl", "meaning": "giờ mở cửa hoạt động", "example": "The repair shop will open tomorrow at 8:00 A.M. to accept walk-in clients."},
        {"word": "estimate", "ipa": "/ˈes.tɪ.meɪt/", "pos": "n, v", "meaning": "bản báo giá dự trù chi phí", "example": "Our staff will provide a written repair cost estimate after completing diagnostics."}
    ],

    # Q92-Q94: Furniture Showroom Floor Displays
    92: [
        {"word": "showroom floor", "ipa": "/ˈʃəʊ.ruːm flɔːr/", "pos": "n", "meaning": "sàn trưng bày sản phẩm nội thất", "example": "The staff arranged new bedroom and living room sets across the showroom floor."},
        {"word": "furniture store", "ipa": "/ˈfɜː.nɪ.tʃər stɔːr/", "pos": "n", "meaning": "cửa hàng bán đồ gỗ nội thất", "example": "The manager oversees sales associates at a major home furniture store."},
        {"word": "display", "ipa": "/dɪˈspleɪ/", "pos": "n, v", "meaning": "khu trưng bày; bày trí sản phẩm", "example": "The living room display features sectional sofas and oak coffee tables."}
    ],
    93: [
        {"word": "time off", "ipa": "/taɪm ɒf/", "pos": "n", "meaning": "nghỉ phép, xin nghỉ làm việc", "example": "Several associates requested time off next Wednesday to attend the town parade."},
        {"word": "parade", "ipa": "/pəˈreɪd/", "pos": "n", "meaning": "cuộc diễu hành lễ hội trên phố", "example": "Downtown streets will be shut down for the annual holiday parade."},
        {"word": "grant a request", "ipa": "/ɡrɑːnt ə rɪˈkwest/", "pos": "phr", "meaning": "chấp thuận yêu cầu, phê duyệt đơn", "example": "The manager decided to grant their requests because store foot traffic would be low."}
    ],
    94: [
        {"word": "employee schedule", "ipa": "/ɪmˈplɔɪ.iː ˈskedʒ.uːl/", "pos": "n", "meaning": "lịch phân ca làm việc của nhân viên", "example": "Management posted an adjusted employee schedule on the breakroom board."},
        {"word": "feedback", "ipa": "/ˈfiːd.bæk/", "pos": "n", "meaning": "phản hồi ý kiến đóng góp", "example": "Sales associates were asked to provide feedback on customer floor preferences."},
        {"word": "announcement", "ipa": "/əˈnaʊns.mənt/", "pos": "n", "meaning": "thông báo miệng ngắn", "example": "The store director shared one more quick announcement before opening the doors."}
    ],

    # Q95-Q97: Emily from Speedy Services (Rideshare)
    95: [
        {"word": "rideshare driver", "ipa": "/ˈraɪd.ʃeər ˈdraɪ.vər/", "pos": "n", "meaning": "tài xế xe công nghệ đưa đón", "example": "Emily called the passenger to confirm pickup outside the train station."},
        {"word": "pickup location", "ipa": "/ˈpɪk.ʌp ləʊˈkeɪ.ʃən/", "pos": "n", "meaning": "điểm đón khách đã chọn", "example": "Heavy street traffic prompted the driver to suggest an alternate pickup location."},
        {"word": "central station", "ipa": "/ˌsen.trəl ˈsteɪ.ʃən/", "pos": "n", "meaning": "nhà ga xe lửa trung tâm thành phố", "example": "Commuters arrived at the central train station during the evening rush hour."}
    ],
    96: [
        {"word": "grand concourse", "ipa": "/ɡrænd ˈkɒŋ.kɔːs/", "pos": "n", "meaning": "đại sảnh trung tâm rộng lớn của nhà ga", "example": "Meet me right outside the station's grand concourse exit doors."},
        {"word": "designated area", "ipa": "/ˈdez.ɪɡ.neɪ.tɪd ˈeə.ri.ə/", "pos": "n", "meaning": "khu vực quy định riêng biệt", "example": "A designated area for rideshare passenger pickup is marked in yellow paint."},
        {"word": "traffic", "ipa": "/ˈtræf.ɪk/", "pos": "n", "meaning": "giao thông ùn tắc xe cộ", "example": "Congested vehicular traffic delayed taxis waiting along Twelfth Street."}
    ],
    97: [
        {"word": "confirm via app", "ipa": "/kənˈfɜːm ˈvaɪə æp/", "pos": "phr", "meaning": "xác nhận thay đổi qua ứng dụng điện thoại", "example": "Please accept the pickup point change in your smartphone app."},
        {"word": "rideshare app", "ipa": "/ˈraɪd.ʃeər æp/", "pos": "n", "meaning": "ứng dụng gọi xe trên điện thoại", "example": "Passengers can track their assigned driver in real time via the app."},
        {"word": "modify", "ipa": "/ˈmɒd.ɪ.faɪ/", "pos": "v", "meaning": "sửa đổi điều chỉnh thông tin", "example": "Users can modify trip preferences with a single tap on the screen."}
    ],

    # Q98-Q100: Nutritional Benefits of Eating Fruit
    98: [
        {"word": "nutritional benefits", "ipa": "/njuːˈtrɪʃ.ən.əl ˈben.ɪ.fɪts/", "pos": "n pl", "meaning": "các lợi ích về dinh dưỡng sức khỏe", "example": "The physician's lecture analyzed the nutritional benefits of consuming whole fruit."},
        {"word": "presentation", "ipa": "/ˌprez.ənˈteɪ.ʃən/", "pos": "n", "meaning": "bài báo cáo khoa học, bài thuyết trình", "example": "Dr. Novikova delivered a keynote presentation at the annual wellness symposium."},
        {"word": "diet", "ipa": "/ˈdaɪ.ət/", "pos": "n", "meaning": "chế độ ăn uống dinh dưỡng hàng ngày", "example": "Patients should incorporate fiber-rich berries into their daily diet."}
    ],
    99: [
        {"word": "publish a study", "ipa": "/ˈpʌb.lɪʃ ə ˈstʌd.i/", "pos": "phr", "meaning": "xuất bản một nghiên cứu khoa học", "example": "Last year, the doctor published a research study on dietary sugar in a medical journal."},
        {"word": "recommended serving", "ipa": "/ˌrek.əˈmen.dɪd ˈsɜː.vɪŋ/", "pos": "n", "meaning": "khẩu phần ăn được chuyên gia khuyến nghị", "example": "Health agencies advise consuming two to three servings of fresh fruit per day."},
        {"word": "medical research", "ipa": "/ˈmed.ɪ.kəl rɪˈsɜːtʃ/", "pos": "n", "meaning": "nghiên cứu trong y khoa", "example": "Her peer-reviewed medical research clarified misconceptions about natural sugars."}
    ],
    100: [
        {"word": "lobby", "ipa": "/ˈlɒb.i/", "pos": "n", "meaning": "sảnh đón khách, tiền sảnh hội nghị", "example": "Conference attendees can sample fruit-based snacks at the station in the main lobby."},
        {"word": "test out", "ipa": "/test aʊt/", "pos": "phr v", "meaning": "nếm thử hoặc dùng thử trải nghiệm", "example": "Guests are invited to test out healthy recipes outside the lecture hall."},
        {"word": "auditorium", "ipa": "/ˌɔː.dɪˈtɔː.ri.əm/", "pos": "n", "meaning": "khán phòng lớn, giảng đường thuyết trình", "example": "Over four hundred nutritionists packed the convention auditorium."}
    ]
}

# Write output to json
with open('scratch/t3_p3_p4_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(p3_p4_vocab, f, ensure_ascii=False, indent=2)

print(f"Successfully generated scratch/t3_p3_p4_vocab.json with {len(p3_p4_vocab)} questions!")
