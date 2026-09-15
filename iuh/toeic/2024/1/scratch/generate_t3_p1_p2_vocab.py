# scratch/generate_t3_p1_p2_vocab.py
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

t3_p1_p2_vocab = {
    1: [
        {"word": "put trash in a bag", "ipa": "/pʊt træʃ ɪn ə bæɡ/", "pos": "phr", "meaning": "bỏ rác vào trong túi", "example": "They’re putting trash in a large garbage bag."},
        {"word": "take off", "ipa": "/teɪk ɒf/", "pos": "phr v", "meaning": "cởi ra (áo khoác, giày dép)", "example": "They’re taking off their jackets before entering the building."},
        {"word": "facing", "ipa": "/ˈfeɪ.sɪŋ/", "pos": "prep/v", "meaning": "đối diện, quay mặt về phía", "example": "They’re facing a tall shelving unit in the warehouse."},
        {"word": "shelving unit", "ipa": "/ˈʃel.vɪŋ ˌjuː.nɪt/", "pos": "n", "meaning": "kệ để đồ, giá sách nhiều tầng", "example": "Storage boxes are stacked neatly on the shelving unit."},
        {"word": "paint", "ipa": "/peɪnt/", "pos": "v", "meaning": "sơn, quét sơn phòng", "example": "They’re painting the interior walls of a room."}
    ],
    2: [
        {"word": "oven", "ipa": "/ˈʌv.ən/", "pos": "n", "meaning": "lò nướng thức ăn", "example": "She’s cleaning the grease inside an oven."},
        {"word": "pot", "ipa": "/pɒt/", "pos": "n", "meaning": "cái nồi, xong nấu", "example": "She’s carefully moving a heavy cooking pot."},
        {"word": "cabinet", "ipa": "/ˈkæb.ɪ.nət/", "pos": "n", "meaning": "tủ đựng đồ có cánh đóng", "example": "She’s opening the wooden kitchen cabinet."},
        {"word": "towel", "ipa": "/taʊəl/", "pos": "n", "meaning": "khăn lau, khăn mặt", "example": "She’s holding a dry towel to wipe the dishes."}
    ],
    3: [
        {"word": "ladder", "ipa": "/ˈlæd.ər/", "pos": "n", "meaning": "cái thang đứng", "example": "A tall ladder has been leaned against a tree."},
        {"word": "lean against", "ipa": "/liːn əˈɡenst/", "pos": "phr v", "meaning": "tựa vào, dựa sát vào", "example": "Wooden planks were leaned against the garden wall."},
        {"word": "tree branch", "ipa": "/triː brɑːntʃ/", "pos": "n", "meaning": "cành cây to", "example": "Fallen tree branches were cleared from the public walkway."},
        {"word": "wooden bench", "ipa": "/ˈwʊd.ən bentʃ/", "pos": "n", "meaning": "ghế dài bằng gỗ", "example": "Wooden benches have been arranged in a circle for visitors."}
    ],
    4: [
        {"word": "remove", "ipa": "/rɪˈmuːv/", "pos": "v", "meaning": "cởi ra, tháo bỏ (mũ, áo)", "example": "One of the men is removing his sun hat."},
        {"word": "line of customers", "ipa": "/laɪn əv ˈkʌs.tə.mərz/", "pos": "n", "meaning": "hàng dài khách hàng", "example": "A line of customers extends out the storefront door."},
        {"word": "install a sign", "ipa": "/ɪnˈstɔːl ə saɪn/", "pos": "phr", "meaning": "lắp đặt biển quảng cáo/biển hiệu", "example": "Technicians are installing a bright neon sign."},
        {"word": "musician", "ipa": "/mjuːˈzɪʃ.ən/", "pos": "n", "meaning": "nhạc công, nghệ sĩ biểu diễn", "example": "Musicians have gathered in a circle in the town square."}
    ],
    5: [
        {"word": "railing", "ipa": "/ˈreɪ.lɪŋ/", "pos": "n", "meaning": "lan can, rào chắn an toàn", "example": "A safety railing is being removed along the balcony."},
        {"word": "under construction", "ipa": "/ˈʌn.dər kənˈstrʌk.ʃən/", "pos": "phr", "meaning": "đang trong quá trình thi công xây dựng", "example": "The roof of the commercial complex is under construction."},
        {"word": "sheet of metal", "ipa": "/ʃiːt əv ˈmet.əl/", "pos": "n", "meaning": "tấm tôn/kim loại xây dựng", "example": "Workers are holding durable sheets of metal."},
        {"word": "ladder", "ipa": "/ˈlæd.ər/", "pos": "n", "meaning": "cái thang gấp", "example": "Two workers are carrying an aluminum ladder across the site."}
    ],
    6: [
        {"word": "tool set", "ipa": "/tuːl set/", "pos": "n", "meaning": "bộ đồ nghề, bộ dụng cụ sửa chữa", "example": "Several tool sets have been laid out on the workbench."},
        {"word": "lay out", "ipa": "/leɪ aʊt/", "pos": "phr v", "meaning": "trải ra, bày biện ngăn nắp", "example": "Architectural plans were laid out on the conference table."},
        {"word": "spill", "ipa": "/spɪl/", "pos": "v", "meaning": "làm tràn, đổ nước ra ngoài", "example": "A cup of coffee has spilled on the cafeteria floor."},
        {"word": "table leg", "ipa": "/ˈteɪ.bəl leɡ/", "pos": "n", "meaning": "chân bàn", "example": "A wooden table leg is being repaired by the craftsman."}
    ],
    7: [
        {"word": "flour", "ipa": "/flaʊər/", "pos": "n", "meaning": "bột mì làm bánh", "example": "Why is there no baking flour left on the shelf?"},
        {"word": "out of stock", "ipa": "/aʊt əv stɒk/", "pos": "phr", "meaning": "hết hàng trong kho", "example": "The popular brand of flour is temporarily out of stock."},
        {"word": "shelf", "ipa": "/ʃelf/", "pos": "n", "meaning": "kệ bày hàng, giá sách", "example": "Packaged goods are displayed on the supermarket shelf."},
        {"word": "smell", "ipa": "/smel/", "pos": "v", "meaning": "có mùi hương, tỏa hương thơm", "example": "Those freshly cut roses smell very pleasant."}
    ],
    8: [
        {"word": "catering company", "ipa": "/ˈkeɪ.tər.ɪŋ ˈkʌm.pə.ni/", "pos": "n", "meaning": "công ty cung cấp tiệc lưu động", "example": "When will the catering company arrive at our banquet hall?"},
        {"word": "arrive", "ipa": "/əˈraɪv/", "pos": "v", "meaning": "đến nơi, cập bến", "example": "The delivery van will arrive precisely at four o'clock."},
        {"word": "vegetarian option", "ipa": "/ˌvedʒ.ɪˈteə.ri.ən ˈɒp.ʃən/", "pos": "n", "meaning": "món ăn chay tùy chọn", "example": "The banquet menu features several delicious vegetarian options."},
        {"word": "flavor", "ipa": "/ˈfleɪ.vər/", "pos": "n", "meaning": "hương vị ẩm thực", "example": "The chef experimented with a unique citrus flavor."}
    ],
    9: [
        {"word": "scheduled to start", "ipa": "/ˈʃedʒ.uːld tuː stɑːt/", "pos": "phr", "meaning": "được lên lịch bắt đầu", "example": "When is the project kickoff meeting scheduled to start?"},
        {"word": "networking event", "ipa": "/ˈnet.wɜː.kɪŋ ɪˈvent/", "pos": "n", "meaning": "sự kiện giao lưu kết nối doanh nghiệp", "example": "Professionals exchanged business cards at the networking event."},
        {"word": "right after", "ipa": "/raɪt ˈɑːf.tər/", "pos": "phr", "meaning": "ngay sau khi", "example": "We will resume the presentation right after lunch."}
    ],
    10: [
        {"word": "repair cost", "ipa": "/rɪˈpeər kɒst/", "pos": "n", "meaning": "chi phí sửa chữa hỏng hóc", "example": "How much will the automobile repairs cost?"},
        {"word": "cost", "ipa": "/kɒst/", "pos": "v, n", "meaning": "trị giá, tiêu tốn số tiền", "example": "The maintenance work will cost around 200 dollars."},
        {"word": "downtown", "ipa": "/ˌdaʊnˈtaʊn/", "pos": "adj, adv", "meaning": "khu vực trung tâm thành phố", "example": "The company headquarters is situated downtown."}
    ],
    11: [
        {"word": "dentist", "ipa": "/ˈden.tɪst/", "pos": "n", "meaning": "nha sĩ, phòng khám răng", "example": "You went to the dentist this morning for an exam, didn't you?"},
        {"word": "annual checkup", "ipa": "/ˈæn.ju.əl ˈtʃek.ʌp/", "pos": "n", "meaning": "khám sức khỏe định kỳ hàng năm", "example": "Patients are encouraged to schedule an annual checkup."},
        {"word": "take the bus", "ipa": "/teɪk ðə bʌs/", "pos": "phr", "meaning": "bắt xe buýt đi lại", "example": "Let's take the commuter bus rather than driving."}
    ],
    12: [
        {"word": "printer", "ipa": "/ˈprɪn.tər/", "pos": "n", "meaning": "máy in văn phòng", "example": "Where should we install the newly delivered printer?"},
        {"word": "corner", "ipa": "/ˈkɔː.nər/", "pos": "n", "meaning": "góc phòng, khúc quanh", "example": "Set up the supply table in the corner by the stairs."},
        {"word": "ink cartridge", "ipa": "/ɪŋk ˈkɑː.trɪdʒ/", "pos": "n", "meaning": "hộp mực máy in", "example": "This model uses an economical reusable ink cartridge."}
    ],
    13: [
        {"word": "plant", "ipa": "/plɑːnt/", "pos": "n", "meaning": "cây cảnh văn phòng", "example": "What type of decorative plant do you have in your office?"},
        {"word": "require", "ipa": "/rɪˈkwaɪər/", "pos": "v", "meaning": "yêu cầu, đòi hỏi (nước, chăm sóc)", "example": "Cacti are ideal desk plants because they don't require much water."},
        {"word": "desk", "ipa": "/desk/", "pos": "n", "meaning": "bàn làm việc", "example": "Clear unnecessary paper off your desk every evening."}
    ],
    14: [
        {"word": "furniture store", "ipa": "/ˈfɜː.nɪ.tʃər stɔːr/ ", "pos": "n", "meaning": "cửa hàng bán đồ nội thất", "example": "There was a major clearance sale at the downtown furniture store."},
        {"word": "convention center", "ipa": "/kənˈven.ʃən ˈsen.tər/", "pos": "n", "meaning": "trung tâm hội nghị triển lãm", "example": "The annual home design expo is hosted at the convention center."},
        {"word": "sale", "ipa": "/seɪl/", "pos": "n", "meaning": "đợt giảm giá, bán hàng đại hạ giá", "example": "Did you purchase any desks during the seasonal sale?"}
    ],
    15: [
        {"word": "submit", "ipa": "/səbˈmɪt/", "pos": "v", "meaning": "nộp, gửi đi (hồ sơ, yêu cầu)", "example": "Can you show me how to submit a technical help ticket?"},
        {"word": "help ticket", "ipa": "/help ˈtɪk.ɪt/", "pos": "n", "meaning": "phiếu báo lỗi/yêu cầu trợ giúp IT", "example": "The IT department resolved the help ticket in two hours."},
        {"word": "link", "ipa": "/lɪŋk/", "pos": "n", "meaning": "đường dẫn liên kết trực tuyến", "example": "Let me email you the intranet help desk link."},
        {"word": "broken", "ipa": "/ˈbrəʊ.kən/", "pos": "adj", "meaning": "bị hư hỏng, không chạy được", "example": "The packaging machine is broken and requires immediate repair."}
    ],
    16: [
        {"word": "power button", "ipa": "/ˈpaʊ.ər ˈbʌt.ən/", "pos": "n", "meaning": "nút bật nguồn thiết bị", "example": "Where is the power button located on this tablet?"},
        {"word": "model", "ipa": "/ˈmɒd.əl/", "pos": "n", "meaning": "mẫu mã, phiên bản sản phẩm", "example": "I've never operated that particular model before."},
        {"word": "device", "ipa": "/dɪˈvaɪs/", "pos": "n", "meaning": "thiết bị điện tử máy móc", "example": "Turn off the electronic device before cleaning it."}
    ],
    17: [
        {"word": "take a walk", "ipa": "/teɪk ə wɔːk/", "pos": "phr", "meaning": "đi dạo bộ, tản bộ", "example": "Do you want to take a walk now, or would later be better?"},
        {"word": "free", "ipa": "/friː/", "pos": "adj", "meaning": "rảnh rỗi, có thời gian trống", "example": "I'm free to walk over to the client's office now."},
        {"word": "nearby", "ipa": "/ˌnɪəˈbaɪ/", "pos": "adj, adv", "meaning": "ở gần bên cạnh", "example": "We enjoyed a stroll around the nearby lake."}
    ],
    18: [
        {"word": "equipment", "ipa": "/ɪˈkwɪp.mənt/", "pos": "n", "meaning": "trang thiết bị máy móc", "example": "I ordered high-tech manufacturing equipment for the factory."},
        {"word": "factory", "ipa": "/ˈfæk.tər.i/", "pos": "n", "meaning": "nhà máy, nhà xưởng công nghiệp", "example": "The automotive factory operates on two continuous shifts."},
        {"word": "dealership", "ipa": "/ˈdiː.lə.ʃɪp/", "pos": "n", "meaning": "đại lý kinh doanh ô tô", "example": "He purchased a reliable fleet van from the local car dealership."}
    ],
    19: [
        {"word": "place to rent", "ipa": "/pleɪs tuː rent/", "pos": "n phr", "meaning": "căn hộ/địa điểm cho thuê", "example": "There's an affordable place to rent on Mercer Street."},
        {"word": "rent", "ipa": "/rent/", "pos": "n, v", "meaning": "tiền thuê nhà, thuê mướn", "example": "Monthly rent is due on the first day of each month."},
        {"word": "bedroom", "ipa": "/ˈbed.ruːm/", "pos": "n", "meaning": "phòng ngủ", "example": "How many bedrooms does the rental apartment feature?"}
    ],
    20: [
        {"word": "heating system", "ipa": "/ˈhiː.tɪŋ ˈsɪs.təm/", "pos": "n", "meaning": "hệ thống sưởi ấm tòa nhà", "example": "Is the building's heating system working properly?"},
        {"word": "warm", "ipa": "/wɔːm/", "pos": "adj", "meaning": "ấm áp, đủ nhiệt độ", "example": "The radiators were repaired, so the office is warm."},
        {"word": "work", "ipa": "/wɜːk/", "pos": "v", "meaning": "hoạt động, vận hành", "example": "Ensure all thermostat sensors work correctly."}
    ],
    21: [
        {"word": "roadwork", "ipa": "/ˈrəʊd.wɜːk/", "pos": "n", "meaning": "công trình sửa chữa nâng cấp đường", "example": "Isn't the ongoing roadwork in front of city hall finished yet?"},
        {"word": "traffic", "ipa": "/ˈtræf.ɪk/", "pos": "n", "meaning": "giao thông xe cộ", "example": "Expect heavy traffic along main commuter routes in the evening."},
        {"word": "city hall", "ipa": "/ˌsɪt.i ˈhɔːl/", "pos": "n", "meaning": "tòa thị chính thành phố", "example": "Permit applications must be filed at city hall."}
    ],
    22: [
        {"word": "employee training", "ipa": "/ɪmˈplɔɪ.iː ˈtreɪ.nɪŋ/", "pos": "n", "meaning": "buổi đào tạo nhân viên", "example": "Who will lead the new employee training workshop today?"},
        {"word": "recorded video", "ipa": "/rɪˈkɔː.dɪd ˈvɪd.i.əʊ/", "pos": "n", "meaning": "video ghi hình sẵn bài giảng", "example": "We are using a recorded video for the onboarding orientation."},
        {"word": "lead", "ipa": "/liːd/", "pos": "v", "meaning": "chủ trì, hướng dẫn", "example": "The training director will lead the afternoon seminar."}
    ],
    23: [
        {"word": "safety inspection", "ipa": "/ˈseɪf.ti ɪnˈspek.ʃən/", "pos": "n", "meaning": "cuộc thanh tra an toàn lao động", "example": "Is the quarterly safety inspection scheduled for this month?"},
        {"word": "supervisor", "ipa": "/ˈsuː.pə.vaɪ.zər/", "pos": "n", "meaning": "người quản lý giám sát", "example": "The factory supervisor accompanied the safety auditors."},
        {"word": "scheduled", "ipa": "/ˈʃedʒ.uːld/", "pos": "adj", "meaning": "được lên thời gian biểu", "example": "The audit is scheduled for this coming Wednesday."}
    ],
    24: [
        {"word": "harvest festival", "ipa": "/ˈhɑː.vɪst ˈfes.tɪ.vəl/", "pos": "n", "meaning": "lễ hội mùa màng nông sản", "example": "When is the annual harvest festival taking place?"},
        {"word": "community center", "ipa": "/kəˈmjuː.nə.ti ˈsen.tər/", "pos": "n", "meaning": "trung tâm cộng đồng địa phương", "example": "Festivities are held at the neighborhood community center."},
        {"word": "take place", "ipa": "/teɪk pleɪs/", "pos": "phr", "meaning": "diễn ra, tổ chức", "example": "The agricultural fair will take place sometime in October."}
    ],
    25: [
        {"word": "expensive", "ipa": "/ɪkˈspen.sɪv/", "pos": "adj", "meaning": "đắt đỏ, giá cao", "example": "Was your new business laptop expensive to purchase?"},
        {"word": "discount coupon", "ipa": "/ˈdɪs.kaʊnt ˈkuː.pɒn/", "pos": "n", "meaning": "phiếu/mã giảm giá mua hàng", "example": "I redeemed a 20-percent discount coupon online."},
        {"word": "laptop", "ipa": "/ˈlæp.tɒp/", "pos": "n", "meaning": "máy vi tính xách tay", "example": "The company issued lightweight laptops to all remote staffers."}
    ],
    26: [
        {"word": "camping trip", "ipa": "/ˈkæm.pɪŋ trɪp/", "pos": "n", "meaning": "chuyến cắm trại ngoài trời", "example": "Why don't we go on our camping trip next weekend?"},
        {"word": "work for someone", "ipa": "/wɜːk fɔːr ˈsʌm.wʌn/", "pos": "phr", "meaning": "thuận lợi/phù hợp với ai", "example": "Next Saturday works for me if the weather stays sunny."},
        {"word": "weekend", "ipa": "/ˌwiːkˈend/", "pos": "n", "meaning": "ngày cuối tuần", "example": "We plan weekend outings to recharge after busy workweeks."}
    ],
    27: [
        {"word": "postpone", "ipa": "/pəʊstˈpəʊn/", "pos": "v", "meaning": "trì hoãn, dời lịch lại", "example": "The management workshop for this afternoon was postponed."},
        {"word": "attend", "ipa": "/əˈtend/", "pos": "v", "meaning": "tham dự, có mặt tham gia", "example": "About thirty employees attended the rescheduled training session."},
        {"word": "workshop", "ipa": "/ˈwɜːk.ʃɒp/", "pos": "n", "meaning": "buổi hội thảo chuyên đề", "example": "The productivity workshop will take place next Monday."}
    ],
    28: [
        {"word": "production figures", "ipa": "/prəˈdʌk.ʃən ˈfɪɡ.ərz/", "pos": "n pl", "meaning": "các số liệu sản lượng sản xuất", "example": "How were our manufacturing production figures last month?"},
        {"word": "closed down", "ipa": "/kləʊzd daʊn/", "pos": "phr", "meaning": "tạm ngừng hoạt động, đóng cửa xưởng", "example": "The assembly plant was closed down for a week of retooling."},
        {"word": "electric car", "ipa": "/iˈlek.trɪk kɑːr/", "pos": "n", "meaning": "xe ô tô điện", "example": "The manufacturer produces eco-friendly electric cars."}
    ],
    29: [
        {"word": "speech therapist", "ipa": "/spiːtʃ ˈθer.ə.pɪst/", "pos": "n", "meaning": "chuyên gia trị liệu phát âm/ngôn ngữ", "example": "When can I make an appointment to see the speech therapist?"},
        {"word": "opening", "ipa": "/ˈəʊ.pən.ɪŋ/", "pos": "n", "meaning": "khung giờ trống lịch hẹn", "example": "The specialist has an unexpected opening tomorrow morning."},
        {"word": "speech", "ipa": "/spiːtʃ/", "pos": "n", "meaning": "bài phát biểu diễn văn", "example": "The keynote speaker delivered a compelling twenty-minute speech."}
    ],
    30: [
        {"word": "pick up", "ipa": "/pɪk ʌp/", "pos": "phr v", "meaning": "đón ai đó (bằng ô tô)", "example": "Aren't you picking up the visiting clients from the airport?"},
        {"word": "client", "ipa": "/ˈklaɪ.ənt/", "pos": "n", "meaning": "khách hàng đối tác", "example": "We escorted the prospective clients to the boardroom."},
        {"word": "aisle seat", "ipa": "/aɪl siːt/", "pos": "n", "meaning": "ghế ngồi cạnh lối đi máy bay", "example": "He requested an aisle seat for the cross-country flight."}
    ],
    31: [
        {"word": "contract", "ipa": "/ˈkɒn.trækt/", "pos": "n", "meaning": "hợp đồng ký kết", "example": "The commercial supply contract is now officially signed."},
        {"word": "officially", "ipa": "/əˈfɪʃ.əl.i/", "pos": "adv", "meaning": "một cách chính thức", "example": "The partnership was officially announced in today's press release."},
        {"word": "client meeting", "ipa": "/ˈklaɪ.ənt ˈmiː.tɪŋ/", "pos": "n", "meaning": "cuộc họp với khách hàng", "example": "How was your morning client meeting in conference room two?"}
    ]
}

with open('scratch/t3_p1_p2_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(t3_p1_p2_vocab, f, ensure_ascii=False, indent=2)

print("Generated scratch/t3_p1_p2_vocab.json successfully!")
