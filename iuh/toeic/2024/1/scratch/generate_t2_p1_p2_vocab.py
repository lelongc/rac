# scratch/generate_t2_p1_p2_vocab.py
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

t2_p1_p2_vocab = {
    1: [
        {"word": "insert", "ipa": "/ɪnˈsɜːt/", "pos": "v", "meaning": "cắm vào, chèn vào", "example": "She inserted the plug into the wall socket."},
        {"word": "cord", "ipa": "/kɔːd/", "pos": "n", "meaning": "dây điện, dây cáp mềm", "example": "An electrical cord runs behind the desk."},
        {"word": "outlet", "ipa": "/ˈaʊt.let/", "pos": "n", "meaning": "ổ cắm điện trên tường", "example": "Plug the device into the nearest electrical outlet."},
        {"word": "tack", "ipa": "/tæk/", "pos": "v", "meaning": "đóng đinh ghim, gắn bằng đinh ghim", "example": "She tacked a notice onto the bulletin board."}
    ],
    2: [
        {"word": "shutter", "ipa": "/ˈʃʌt.ər/", "pos": "n", "meaning": "cửa chớp, cánh cửa sổ", "example": "Window shutters help block intense sunlight."},
        {"word": "arrange", "ipa": "/əˈreɪndʒ/", "pos": "v", "meaning": "sắp xếp, bài trí", "example": "Pillows are neatly arranged on the outdoor seat."},
        {"word": "clear off", "ipa": "/klɪər ɒf/", "pos": "phr v", "meaning": "dọn dẹp sạch bề mặt", "example": "Waiters are clearing off the dining tables."},
        {"word": "wooden board", "ipa": "/ˈwʊd.ən bɔːd/", "pos": "n", "meaning": "tấm ván gỗ", "example": "Construction workers replaced damaged wooden boards."}
    ],
    3: [
        {"word": "utensil", "ipa": "/juːˈten.sɪl/", "pos": "n", "meaning": "dụng cụ nhà bếp/đồ dùng", "example": "Kitchen utensils are stored in the top drawer."},
        {"word": "discard", "ipa": "/dɪˈskɑːd/", "pos": "v", "meaning": "vứt bỏ, thải loại", "example": "Discard all expired food items in the bin."},
        {"word": "sink", "ipa": "/sɪŋk/", "pos": "n", "meaning": "bồn rửa bát/rửa chén", "example": "Bottles are being rinsed in the kitchen sink."},
        {"word": "rolling chair", "ipa": "/ˈrəʊ.lɪŋ tʃeər/", "pos": "n", "meaning": "ghế có bánh xe xoay", "example": "Ergonomic rolling chairs were placed near the counter."}
    ],
    4: [
        {"word": "chop", "ipa": "/tʃɒp/", "pos": "v", "meaning": "chặt, chẻ (củi, gỗ)", "example": "A man is chopping some wood into pieces."},
        {"word": "scatter", "ipa": "/ˈskæt.ər/", "pos": "v", "meaning": "rải rác, phân tán", "example": "Autumn leaves are scattered across the grass."},
        {"word": "pile", "ipa": "/paɪl/", "pos": "v, n", "meaning": "chất đống, đống", "example": "Wood is piled neatly near a wooden fence."}
    ],
    5: [
        {"word": "stand in line", "ipa": "/stænd ɪn laɪn/", "pos": "phr", "meaning": "xếp hàng chờ đợi", "example": "People are standing in line in the hotel lobby."},
        {"word": "load", "ipa": "/ləʊd/", "pos": "v", "meaning": "chất hàng lên, xếp đồ vào", "example": "Items are being loaded into shopping bags."},
        {"word": "canopy", "ipa": "/ˈkæn.ə.pi/", "pos": "n", "meaning": "mái che, bạt che nắng ngoài trời", "example": "A worker is putting up a protective canopy."},
        {"word": "parking area", "ipa": "/ˈpɑː.kɪŋ ˈeə.ri.ə/", "pos": "n", "meaning": "khu vực đỗ xe", "example": "Tents have been set up in the parking area."}
    ],
    6: [
        {"word": "luggage", "ipa": "/ˈlʌɡ.ɪdʒ/", "pos": "n", "meaning": "hành lý, kiện hàng", "example": "Some luggage is stacked next to an escalator."},
        {"word": "escalator", "ipa": "/ˈes.kə.leɪ.tər/", "pos": "n", "meaning": "thang cuốn tự động", "example": "Take the escalator up to the departures terminal."},
        {"word": "shuttle bus", "ipa": "/ˈʃʌt.əl bʌs/", "pos": "n", "meaning": "xe buýt đưa đón cự ly ngắn", "example": "A suitcase is being lifted onto a shuttle bus."},
        {"word": "luggage rack", "ipa": "/ˈlʌɡ.ɪdʒ ræk/", "pos": "n", "meaning": "giá để hành lý", "example": "The luggage rack has two spacious levels."}
    ],
    7: [
        {"word": "factory floor", "ipa": "/ˈfæk.tər.i flɔːr/", "pos": "n", "meaning": "sàn nhà xưởng, khu sản xuất", "example": "Have the machines on the factory floor been cleaned?"},
        {"word": "shipping container", "ipa": "/ˈʃɪp.ɪŋ kənˈteɪ.nər/", "pos": "n", "meaning": "thùng công-ten-nơ vận chuyển", "example": "The parts are stored in the shipping container."},
        {"word": "trash bin", "ipa": "/træʃ bɪn/", "pos": "n", "meaning": "thùng rác", "example": "I just put the waste into the trash bin."}
    ],
    8: [
        {"word": "budget", "ipa": "/ˈbʌdʒ.ɪt/", "pos": "n", "meaning": "ngân sách chi tiêu", "example": "How much will the department budget increase next year?"},
        {"word": "increase", "ipa": "/ɪnˈkriːs/", "pos": "v, n", "meaning": "tăng lên, sự gia tăng", "example": "Profits are projected to increase by about 10 percent."},
        {"word": "main branch", "ipa": "/meɪn brɑːntʃ/", "pos": "n", "meaning": "chi nhánh chính, trụ sở chính", "example": "Submit loan applications at the bank's main branch."}
    ],
    9: [
        {"word": "water", "ipa": "/ˈwɔː.tər/", "pos": "v", "meaning": "tưới nước (cho cây cối)", "example": "You're going to water the plants before you leave, aren't you?"},
        {"word": "break room", "ipa": "/ˈbreɪk ruːm/", "pos": "n", "meaning": "phòng nghỉ ngơi cho nhân viên", "example": "Employees relax and drink tea in the break room."},
        {"word": "after lunch", "ipa": "/ˈɑːf.tər lʌntʃ/", "pos": "phr", "meaning": "ngay sau bữa trưa", "example": "The meeting will resume right after lunch."}
    ],
    10: [
        {"word": "appointment", "ipa": "/əˈpɔɪnt.mənt/", "pos": "n", "meaning": "cuộc hẹn khám/gặp gỡ", "example": "Aren't you going to schedule an eye doctor appointment?"},
        {"word": "schedule", "ipa": "/ˈʃedʒ.uːl/", "pos": "v, n", "meaning": "lên lịch, sắp xếp thời gian", "example": "I already scheduled an appointment for Thursday."},
        {"word": "seminar", "ipa": "/ˈsem.ɪ.nɑːr/", "pos": "n", "meaning": "hội thảo chuyên đề", "example": "The marketing seminar is three days long."}
    ],
    11: [
        {"word": "printer", "ipa": "/ˈprɪn.tər/", "pos": "n", "meaning": "máy in văn phòng", "example": "I'm going to try to fix this office printer."},
        {"word": "repair", "ipa": "/rɪˈpeər/", "pos": "v, n", "meaning": "sửa chữa, bảo dưỡng", "example": "Are you sure the equipment can be repaired?"},
        {"word": "double-sided", "ipa": "/ˌdʌb.əlˈsaɪ.dɪd/", "pos": "adj", "meaning": "hai mặt (in hai mặt)", "example": "The copy machine is set for double-sided copies."}
    ],
    12: [
        {"word": "brochure", "ipa": "/ˈbrəʊ.ʃər/", "pos": "n", "meaning": "tờ gấp quảng cáo, sách cẩm nang", "example": "What should we do with these marketing brochures?"},
        {"word": "front desk", "ipa": "/frʌnt desk/", "pos": "n", "meaning": "quầy lễ tân", "example": "I will leave the informational packets at the front desk."},
        {"word": "seashore", "ipa": "/ˈsiː.ʃɔːr/", "pos": "n", "meaning": "bờ biển, ven biển", "example": "They took a weekend trip to the seashore."}
    ],
    13: [
        {"word": "policy", "ipa": "/ˈpɒl.ə.si/", "pos": "n", "meaning": "chính sách, quy định", "example": "Has the company policy meeting been rescheduled?"},
        {"word": "reschedule", "ipa": "/ˌriːˈʃedʒ.uːl/", "pos": "v", "meaning": "đổi lịch trình, dời ngày", "example": "The conference has been rescheduled for tomorrow instead."},
        {"word": "desk calendar", "ipa": "/desk ˈkæl.ɪn.dər/", "pos": "n", "meaning": "lịch để bàn làm việc", "example": "We have lots of custom desk calendar designs."}
    ],
    14: [
        {"word": "stop by", "ipa": "/stɒp baɪ/", "pos": "phr v", "meaning": "ghé qua, tạt qua", "example": "Why don't we stop by the office cafeteria on our way?"},
        {"word": "cafeteria", "ipa": "/ˌkæf.əˈtɪə.ri.ə/", "pos": "n", "meaning": "quán ăn tự phục vụ văn phòng", "example": "Lunch is served daily in the company cafeteria."},
        {"word": "buffet", "ipa": "/ˈbʊf.eɪ/", "pos": "n", "meaning": "tiệc đứng buffet", "example": "The banquet offered a full service buffet."},
        {"word": "networking", "ipa": "/ˈnet.wɜː.kɪŋ/", "pos": "n", "meaning": "kết nối quan hệ nghề nghiệp", "example": "The workshop topic is professional networking."}
    ],
    15: [
        {"word": "famous", "ipa": "/ˈfeɪ.məs/", "pos": "adj", "meaning": "nổi tiếng, trứ danh", "example": "Have you tried our famous homemade pasta dish?"},
        {"word": "pasta dish", "ipa": "/ˈpæs.tə dɪʃ/", "pos": "n", "meaning": "món mì Ý", "example": "The chef recommended their signature pasta dish."},
        {"word": "on time", "ipa": "/ɒn taɪm/", "pos": "phr", "meaning": "đúng giờ", "example": "I'll try to make it on time despite the traffic."}
    ],
    16: [
        {"word": "opening act", "ipa": "/ˈəʊ.pən.ɪŋ ækt/", "pos": "n", "meaning": "tiết mục mở màn buổi diễn", "example": "Who is the opening act at tonight's music concert?"},
        {"word": "concert", "ipa": "/ˈkɒn.sət/", "pos": "n", "meaning": "buổi hòa nhạc", "example": "A jazz singer from France will perform at the concert."},
        {"word": "turn up", "ipa": "/tɜːn ʌp/", "pos": "phr v", "meaning": "vặn to lên (âm thanh)", "example": "Could you please turn up the sound volume?"}
    ],
    17: [
        {"word": "product demonstration", "ipa": "/ˈprɒd.ʌkt ˌdem.ənˈstreɪ.ʃən/", "pos": "n", "meaning": "buổi giới thiệu/demo sản phẩm", "example": "When do the product demonstrations start?"},
        {"word": "innovative", "ipa": "/ˈɪn.ə.və.tɪv/", "pos": "adj", "meaning": "mang tính sáng tạo, đổi mới", "example": "The new smartphone boasts several innovative features."},
        {"word": "feature", "ipa": "/ˈfiː.tʃər/", "pos": "n", "meaning": "tính năng, đặc điểm", "example": "The system includes advanced security features."}
    ],
    18: [
        {"word": "update", "ipa": "/ʌpˈdeɪt/", "pos": "v", "meaning": "cập nhật, sửa đổi mới", "example": "I tried updating the company website, but it didn't work."},
        {"word": "online review", "ipa": "/ˈɒn.laɪn rɪˈvjuː/", "pos": "n", "meaning": "nhận xét, đánh giá trực tuyến", "example": "Customers often consult our online reviews."},
        {"word": "work", "ipa": "/wɜːk/", "pos": "v", "meaning": "hoạt động tốt, phát huy tác dụng", "example": "The revised script works well for our team."}
    ],
    19: [
        {"word": "welding specialist", "ipa": "/ˈwel.dɪŋ ˈspeʃ.əl.ɪst/", "pos": "n", "meaning": "chuyên gia/thợ hàn kỹ thuật", "example": "Did you hire a new certified welding specialist?"},
        {"word": "hire", "ipa": "/haɪər/", "pos": "v", "meaning": "tuyển dụng, thuê nhân viên", "example": "The company decided to hire two technicians."},
        {"word": "back-ordered", "ipa": "/bæk ˈɔː.dəd/", "pos": "adj", "meaning": "tạm hết hàng, đặt hàng trước", "example": "The mechanical part is currently back-ordered."}
    ],
    20: [
        {"word": "color palette", "ipa": "/ˈkʌl.ə ˈpæl.ət/", "pos": "n", "meaning": "bảng phối màu sắc", "example": "How was the color palette for the lobby chosen?"},
        {"word": "lobby", "ipa": "/ˈlɒb.i/", "pos": "n", "meaning": "tiền sảnh tòa nhà", "example": "Blue and orange accents were added to the lobby."},
        {"word": "involved", "ipa": "/ɪnˈvɒlvd/", "pos": "adj", "meaning": "tham gia vào, dính líu đến", "example": "I wasn't involved in the interior design selection."}
    ],
    21: [
        {"word": "supplies", "ipa": "/səˈplaɪz/", "pos": "n pl", "meaning": "vật tư, văn phòng phẩm", "example": "When are we ordering more supplies for the office?"},
        {"word": "storage closet", "ipa": "/ˈstɔː.rɪdʒ ˈklɒz.ɪt/", "pos": "n", "meaning": "tủ/kho chứa đồ đạc", "example": "Extra notebooks are stored in the storage closet."},
        {"word": "order", "ipa": "/ˈɔː.dər/", "pos": "v", "meaning": "đặt hàng, đặt mua", "example": "We will order new computer accessories on Monday."}
    ],
    22: [
        {"word": "water pump", "ipa": "/ˈwɔː.tər pʌmp/", "pos": "n", "meaning": "máy bơm nước", "example": "The battery for the water pump will be solar powered."},
        {"word": "solar powered", "ipa": "/ˈsəʊ.lər ˈpaʊ.əd/", "pos": "adj", "meaning": "chạy bằng năng lượng mặt trời", "example": "Solar powered devices reduce electricity costs."},
        {"word": "planning stage", "ipa": "/ˈplæn.ɪŋ steɪdʒ/", "pos": "n", "meaning": "giai đoạn lập kế hoạch", "example": "The construction project is still in the planning stages."}
    ],
    23: [
        {"word": "charger", "ipa": "/ˈtʃɑː.dʒər/", "pos": "n", "meaning": "bộ sạc pin, dây sạc", "example": "Where can I buy a compatible charger for this laptop?"},
        {"word": "return policy", "ipa": "/rɪˈtɜːn ˈpɒl.ə.si/", "pos": "n", "meaning": "chính sách đổi trả hàng", "example": "The electronics retailer has a limited return policy."},
        {"word": "order", "ipa": "/ˈɔː.dər/", "pos": "v", "meaning": "đặt mua hàng trực tuyến", "example": "I can order an original replacement charger for you."}
    ],
    24: [
        {"word": "reserve", "ipa": "/rɪˈzɜːv/", "pos": "v", "meaning": "đặt trước, giữ chỗ phòng", "example": "Do I need to reserve a meeting room in advance?"},
        {"word": "meeting room", "ipa": "/ˈmiː.tɪŋ ruːm/", "pos": "n", "meaning": "phòng họp cơ quan", "example": "Reserve meeting room B for the client briefing."},
        {"word": "slide presentation", "ipa": "/slaɪd ˌprez.ənˈteɪ.ʃən/", "pos": "n", "meaning": "bài thuyết trình trang chiếu", "example": "Let me test my slide presentation on the projector."}
    ],
    25: [
        {"word": "department director", "ipa": "/dɪˈpɑːt.mənt daɪˈrek.tər/", "pos": "n", "meaning": "giám đốc bộ phận", "example": "When is the new department director supposed to start?"},
        {"word": "retire", "ipa": "/rɪˈtaɪər/", "pos": "v", "meaning": "nghỉ hưu", "example": "Ms. Pavlova isn't retiring for several weeks."},
        {"word": "supposed to", "ipa": "/səˈpəʊzd tuː/", "pos": "phr", "meaning": "dự kiến sẽ, theo lịch", "example": "The train is supposed to arrive in ten minutes."}
    ],
    26: [
        {"word": "deliver", "ipa": "/dɪˈlɪv.ər/", "pos": "v", "meaning": "giao hàng, chuyển phát", "example": "Should I deliver these pizzas, or will you?"},
        {"word": "pick up", "ipa": "/pɪk ʌp/", "pos": "phr v", "meaning": "đến lấy hàng, nhận hàng", "example": "The food orders are being picked up by the customer."},
        {"word": "hungry", "ipa": "/ˈhʌŋ.ɡri/", "pos": "adj", "meaning": "đói bụng", "example": "No thanks, I'm not hungry right now."}
    ],
    27: [
        {"word": "shipment schedule", "ipa": "/ˈʃɪp.mənt ˈʃedʒ.uːl/", "pos": "n", "meaning": "lịch trình vận chuyển hàng", "example": "This month's shipment schedule has been revised."},
        {"word": "revise", "ipa": "/rɪˈvaɪz/", "pos": "v", "meaning": "sửa đổi, hiệu chỉnh", "example": "Which delivery dates have been changed or revised?"},
        {"word": "per pound", "ipa": "/pɜːr paʊnd/", "pos": "phr", "meaning": "trên mỗi pao cân nặng", "example": "The shipping rate is two dollars per pound."}
    ],
    28: [
        {"word": "repair cost", "ipa": "/rɪˈpeər kɒst/", "pos": "n", "meaning": "chi phí sửa chữa", "example": "How much will the mechanical repairs cost?"},
        {"word": "warranty plan", "ipa": "/ˈwɒr.ən.ti plæn/", "pos": "n", "meaning": "chế độ/gói bảo hành", "example": "The work is fully covered under the warranty plan."},
        {"word": "covered", "ipa": "/ˈkʌv.əd/", "pos": "adj", "meaning": "được chi trả, được bảo hiểm", "example": "All maintenance fees are covered by the contract."}
    ],
    29: [
        {"word": "sample", "ipa": "/ˈsɑːm.pəl/", "pos": "n", "meaning": "mẫu thử, mẫu vật liệu", "example": "Why don't we provide more samples of wallpaper patterns?"},
        {"word": "wallpaper pattern", "ipa": "/ˈwɔːlˌpeɪ.pər ˈpæt.ən/", "pos": "n", "meaning": "mẫu hoa văn giấy dán tường", "example": "Customers can choose from various wallpaper patterns."},
        {"word": "binder", "ipa": "/ˈbaɪn.dər/", "pos": "n", "meaning": "tập hồ sơ lưu trữ bìa cứng", "example": "There are plenty of sample swatches in the binders."}
    ],
    30: [
        {"word": "tour", "ipa": "/tʊər/", "pos": "n, v", "meaning": "chuyến tham quan, khảo sát", "example": "Can you give me a tour of the property this afternoon?"},
        {"word": "property", "ipa": "/ˈprɒp.ə.ti/", "pos": "n", "meaning": "bất động sản, khu nhà đất", "example": "The real estate agent manages several rental properties."},
        {"word": "modern design", "ipa": "/ˈmɒd.ən dɪˈzaɪn/", "pos": "n", "meaning": "thiết kế hiện đại", "example": "The newly built house features a very modern design."}
    ],
    31: [
        {"word": "confirmation", "ipa": "/ˌkɒn.fəˈmeɪ.ʃən/", "pos": "n", "meaning": "sự xác nhận, thông báo chuẩn y", "example": "We're still waiting for official confirmation."},
        {"word": "test", "ipa": "/test/", "pos": "v", "meaning": "kiểm tra, thử nghiệm sản phẩm", "example": "Who's scheduled to test the new product today?"},
        {"word": "scheduled", "ipa": "/ˈʃedʒ.uːld/", "pos": "adj", "meaning": "được lên lịch trình", "example": "The product testing is scheduled for this morning."}
    ]
}

with open('scratch/t2_p1_p2_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(t2_p1_p2_vocab, f, ensure_ascii=False, indent=2)

print("Generated scratch/t2_p1_p2_vocab.json successfully!")
