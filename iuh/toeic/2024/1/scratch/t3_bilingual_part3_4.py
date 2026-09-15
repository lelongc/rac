# scratch/t3_bilingual_part3_4.py: Full translations for Test 3 Part 3 & Part 4
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

p3_dialogues_vi = {
    (32, 34): (
        "Người nam: Thật tuyệt vời khi công ty chúng ta sẽ chuyển văn phòng vào cuối năm nay. Không gian làm việc mới sẽ rộng rãi hơn rất nhiều.\n"
        "Người nữ: Đúng vậy. Anh có biết công ty định làm gì với các máy tính và thiết bị cũ không?\n"
        "Người nam: Tôi nghe nói họ sẽ quyên góp chúng cho một trường học địa phương.\n"
        "Người nữ: Ý tưởng đó thật ý nghĩa. Tôi nên liên hệ với ai để giúp đóng gói đồ đạc nhỉ?\n"
        "Người nam: Cô hãy nói chuyện với Marcus ở bộ phận hành chính nhé."
    ),
    (35, 37): (
        "Người nam: Chào mừng hai bạn! Tôi rất vui được dẫn hai bạn đi tham quan Triển lãm Thương mại Y tế Đông Nam hôm nay.\n"
        "Người nữ: Cảm ơn anh đã tạo điều kiện cho chúng tôi tham dự. Chúng tôi đặc biệt quan tâm đến các công nghệ chẩn đoán hình ảnh mới.\n"
        "Người nam: Vậy thì các bạn nhất định phải ghé qua gian hàng của MedTech ở Khu C. Họ đang trình diễn máy quét siêu âm cầm tay mới nhất.\n"
        "Người nữ: Tuyệt quá, chúng tôi sẽ đến đó ngay sau buổi hội thảo buổi sáng."
    ),
    (38, 40): (
        "Người nữ: Murad, tôi cần bạn giúp một chút. Bạn có rảnh khoảng 30 phút sau bữa trưa không?\n"
        "Người nam: Tôi có thời gian rảnh sau bữa trưa đấy. Tôi có thể giúp gì cho bạn nào?\n"
        "Người nữ: Như bạn biết đấy, tôi đang chuẩn bị bài thuyết trình về xu hướng tiêu dùng quý 3. Tôi muốn nhờ bạn xem qua các biểu đồ số liệu xem đã rõ ràng chưa.\n"
        "Người nam: Được chứ, gửi tệp tài liệu qua email cho tôi, tôi sẽ xem kỹ trước khi chúng ta gặp nhau."
    ),
    (41, 43): (
        "Người nam: Xin lỗi, tôi đang chờ bắt chuyến tàu từ sân ga này, nhưng tôi đã đợi khá lâu mà vẫn chưa thấy tàu đến.\n"
        "Người nữ: Ồ, chuyến tàu đó đã bị đổi sang Sân ga số 4 do có công tác bảo trì đường ray đột xuất.\n"
        "Người nam: Thật vậy sao? Tôi không nghe thấy thông báo phát thanh nào cả.\n"
        "Người nữ: Bảng điện tử ở sảnh chính có hiển thị thông tin cập nhật đấy. Anh nên đi qua cầu vượt sang Sân ga 4 ngay kẻo lỡ chuyến tàu khởi hành trong 5 phút nữa."
    ),
    (44, 46): (
        "Người nam: Cảm ơn bà Hazarika đã nhận cuộc gọi của tôi.\n"
        "Người nữ: Chào anh. Tôi nghe nói anh đang tìm kiếm các nhà đầu tư cho dự án khởi nghiệp của mình phải không?\n"
        "Người nam: Đúng vậy. Giải pháp giá treo xe đạp thông minh cho các căn hộ nhỏ của chúng tôi đã hoàn thiện bản mẫu thử nghiệm và nhận được phản hồi rất tốt từ người dùng.\n"
        "Người nữ: Dự án nghe rất triển vọng. Hãy gửi cho tôi bản kế hoạch kinh doanh chi tiết và dự toán tài chính vào cuối tuần này nhé."
    ),
    (47, 49): (
        "Người nữ: Alberto, đã đến lúc chúng ta phải rời trường quay để đến ngân hàng trung ương cho buổi phỏng vấn vị giám đốc rồi đấy. Anh đã chuẩn bị máy quay và micro chưa?\n"
        "Người nam: Mọi thiết bị ghi hình đã được xếp gọn gàng trong xe rồi. Nhưng chúng ta nên đi tuyến đường vành đai để tránh kẹt xe giờ cao điểm.\n"
        "Người nữ: Ý kiến hay đấy. Tôi sẽ gọi điện báo cho trợ lý của giám đốc biết là chúng ta đang trên đường tới."
    ),
    (50, 52): (
        "Người nữ: Tuyệt vời, cảm ơn anh! Nhân tiện, công tác chuẩn bị cho bữa tiệc nghỉ hưu của Sabine Hoffman tiến triển đến đâu rồi anh?\n"
        "Người nam: Tôi đã đặt xong sảnh tiệc tại nhà hàng ven sông và đặt một chiếc bánh kem lớn rồi. Tuy nhiên, tôi vẫn đang chờ xác nhận số lượng người tham dự từ phòng nhân sự.\n"
        "Người nữ: Tôi sẽ nhắc bộ phận nhân sự gửi danh sách chốt cho anh trước chiều nay."
    ),
    (53, 55): (
        "Người nam: Xin chào. Tôi là Kota Ogawa đến từ Công ty Langston Limited. Tôi có lịch hẹn với cô Ishikawa để xem cơ sở vật chất khách sạn cho hội nghị thường niên sắp tới.\n"
        "Người nữ: Chào anh Ogawa. Cô Ishikawa đang chuẩn bị tài liệu và sẽ ra gặp anh ngay. Trong lúc chờ đợi, anh có muốn dùng một tách trà hay cà phê không ạ?\n"
        "Người nam: Cảm ơn cô, một ly nước lọc là được rồi."
    ),
    (56, 58): (
        "Người nữ: Hãy nhìn vào kết quả này xem! Doanh số bán dứa của siêu thị chúng ta đã tăng vọt trong tháng này đấy.\n"
        "Người nam: Đó là nhờ chiếc máy gọt dứa tự động mà chúng ta mới lắp đặt ở quầy hoa quả tươi đấy. Khách hàng rất thích thú khi được gọt dứa sẵn tiện lợi.\n"
        "Người nữ: Đúng vậy, chúng ta nên cân nhắc lắp thêm một chiếc máy tương tự ở chi nhánh phía Bắc."
    ),
    (59, 61): (
        "Người nam: Ingrid, tuần này phòng khám nha khoa của chúng ta đã có 3 bệnh nhân phải hủy lịch hẹn vào phút chót rồi đấy.\n"
        "Người nữ: Thật đáng tiếc vì những khung giờ đó rất khó để xếp bệnh nhân khác vào kịp. Chúng ta nên triển khai hệ thống nhắn tin tự động nhắc lịch hẹn trước 24 giờ.\n"
        "Người nam: Tôi hoàn toàn đồng ý. Để tôi liên hệ với bên cung cấp phần mềm quản lý phòng khám để kích hoạt tính năng đó."
    ),
    (62, 64): (
        "Người nam: Chào Raquel. Cô đã có thời gian tìm kiếm món quà năm mới nào để tặng nhân viên chưa? Tôi muốn đảm bảo món quà vừa thiết thực vừa ý nghĩa.\n"
        "Người nữ: Tôi đã xem qua danh mục quà tặng doanh nghiệp. Những chiếc bình giữ nhiệt in logo công ty hoặc phiếu quà tặng mua sách là hai lựa chọn được yêu thích nhất.\n"
        "Người nam: Chiếc bình giữ nhiệt nghe rất tuyệt đấy. Cô hãy liên hệ nhà cung cấp để xin báo giá cho 150 chiếc nhé."
    ),
    (65, 67): (
        "Người nam: Về cảnh quay rượt đuổi bằng xe hơi vào tuần tới trên phố Maple...\n"
        "Người nữ: Tuyệt, để xem nào. Các diễn viên sẽ lái xe về hướng Bắc trên đường Maple. Chúng ta đã xin được giấy phép phong tỏa đoạn đường đó từ chính quyền thành phố chưa?\n"
        "Người nam: Cảnh sát giao thông đã phê duyệt phương án điều tiết từ 8 giờ sáng đến 12 giờ trưa Chủ Nhật rồi, nên chúng ta hoàn toàn yên tâm ghi hình."
    ),
    (68, 70): (
        "Người nữ: Chào Pablo. Tôi muốn trao đổi với anh về trò chơi điện tử mới mà chúng ta vừa thiết kế—trò chơi mà chúng ta sắp ra mắt ấy.\n"
        "Người nam: Chắc chắn rồi. Nhóm thử nghiệm đã gửi phản hồi về phiên bản chơi thử chưa cô?\n"
        "Người nữ: Họ rất thích đồ họa và cốt truyện, nhưng một số người chơi phàn nàn rằng thời gian tải màn chơi ở màn 3 hơi bị chậm.\n"
        "Người nam: Được rồi, tôi sẽ cùng đội ngũ lập trình tối ưu hóa lại mã nguồn ngay trong hôm nay."
    )
}

p4_talks_vi = {
    (71, 73): (
        "Người nói: Tại Volkov Tire and Auto Service, chúng tôi tự hào phục vụ cộng đồng khu vực Thung lũng Livingstone trong suốt hơn 20 năm qua. "
        "Chúng tôi cung cấp dịch vụ bảo dưỡng và sửa chữa ô tô chất lượng cao, từ thay dầu, cân chỉnh góc đặt bánh xe đến kiểm tra động cơ chuyên sâu. "
        "Đội ngũ kỹ thuật viên được cấp chứng chỉ của chúng tôi cam kết mang lại sự an toàn tối đa cho chiếc xe của bạn với chi phí hợp lý nhất. "
        "Đặc biệt trong tháng này, khách hàng thay trọn bộ 4 lốp xe sẽ được tặng kèm dịch vụ đảo lốp và cân mâm miễn phí trọn đời!"
    ),
    (74, 76): (
        "Người nói: Chào mừng các bạn đến với tập podcast tuần này về tiềm năng và giới hạn của tiếp thị trên mạng xã hội. "
        "Làm thế nào để các doanh nghiệp vừa và nhỏ có thể tối ưu hóa ngân sách quảng cáo số mà vẫn tiếp cận đúng tệp khách hàng tiềm năng? "
        "Hôm nay, chúng ta sẽ cùng trò chuyện với chuyên gia truyền thông hàng đầu, người sẽ chia sẻ các chiến lược xây dựng nội dung video ngắn có khả năng lan tỏa mạnh mẽ."
    ),
    (77, 79): (
        "Người nói: Xin chào toàn thể nhân viên. Chiều nay, công ty cây xanh sẽ tiến hành giao các chậu cây cảnh mà chúng ta đã đặt mua để trang trí làm đẹp cho các khu vực sinh hoạt chung trong văn phòng. "
        "Nhiều nghiên cứu đã chứng minh rằng cây xanh giúp giảm bớt căng thẳng và cải thiện đáng kể chất lượng không khí nơi làm việc. "
        "Xin lưu ý rằng đội giao hàng sẽ cần sử dụng thang máy chở hàng từ 2 giờ đến 3 giờ chiều."
    ),
    (80, 82): (
        "Người nói: Bản tin thời sự địa phương: Nhà máy giày bị bỏ hoang tại khu trung tâm thương mại cuối cùng cũng chuẩn bị có một diện mạo hoàn toàn mới. "
        "Tòa nhà lịch sử này đang được cải tạo thành một trung tâm văn hóa và nghệ thuật cộng đồng đa năng, bao gồm không gian trưng bày triển lãm, xưởng sáng tạo và một quán cà phê sân vườn. "
        "Dự án cải tạo dự kiến sẽ hoàn thành và mở cửa đón công chúng vào mùa thu năm sau."
    ),
    (83, 85): (
        "Người nói: Trước khi kết thúc cuộc họp của cơ quan giao thông vận tải hôm nay, tôi muốn cập nhật cho các bạn về tiến độ dự án thay thế cầu Springdale. "
        "Nhờ điều kiện thời tiết thuận lợi trong tháng vừa qua, đội ngũ thi công đã hoàn thành việc lắp đặt các dầm thép chịu lực chính sớm hơn hai tuần so với kế hoạch ban đầu. "
        "Tuy nhiên, việc trải thảm nhựa mặt cầu vẫn sẽ yêu cầu đóng làn đường một phần vào các ngày cuối tuần tới."
    ),
    (86, 88): (
        "Người nói: Xin mọi người chú ý lắng nghe. Tôi hy vọng các bạn đang tận hưởng ngày thứ hai của chuỗi hội thảo cuối tuần về kỹ năng lãnh đạo dành cho doanh nhân khởi nghiệp. "
        "Sau giờ nghỉ giải lao 15 phút, chúng ta sẽ chia thành các nhóm nhỏ tại các phòng hội thảo ở tầng hai để cùng giải quyết các tình huống quản trị khủng hoảng thực tế. "
        "Xin vui lòng nhớ mang theo tập tài liệu bài tập mà ban tổ chức đã phát vào sáng nay."
    ),
    (89, 91): (
        "Người nói: Xin chào, tôi là Adisa từ trung tâm sửa chữa xe Car Pro xin gọi lại cho bạn. "
        "Trong tin nhắn thoại, bạn có cho biết chiếc xe sedan của bạn chạy có cảm giác bị ì ạch và không tăng tốc mượt mà như bình thường. "
        "Dựa trên các dấu hiệu đó, rất có thể bộ lọc nhiên liệu của xe đã bị tắc hoặc bugi đánh lửa cần được thay mới. "
        "Bạn có thể mang xe qua xưởng của chúng tôi vào sáng mai để các kỹ thuật viên kiểm tra tổng quát bằng máy quét chuyên dụng."
    ),
    (92, 94): (
        "Người nói: Chào buổi sáng toàn thể nhân viên bán hàng. Như các bạn thấy, sàn trưng bày của chúng ta đã được bài trí lại hoàn toàn với các bộ sưu tập nội thất phòng ngủ và phòng khách mới nhất. "
        "Các sản phẩm mới trông rất bắt mắt và hiện đại. "
        "Nhiều khách hàng đã gọi điện hỏi về chương trình khuyến mãi nhân dịp ra mắt bộ sưu tập này, vì vậy các bạn hãy nắm rõ bảng giá ưu đãi và các gói hỗ trợ trả góp để tư vấn chu đáo nhất."
    ),
    (95, 97): (
        "Người nói: Xin chào. Tôi là Emily gọi đến từ dịch vụ đưa đón Speedy Services. "
        "Tôi sẽ là tài xế đón bạn tại nhà ga xe lửa trung tâm vào chiều nay. "
        "Tôi thấy chuyến tàu của bạn dự kiến sẽ đến ga vào lúc 3:15 chiều. "
        "Tôi sẽ đỗ chiếc xe van màu bạc tại khu vực đón khách số 3, ngay phía bên ngoài lối ra chính của nhà ga. Hẹn sớm gặp bạn!"
    ),
    (98, 100): (
        "Người nói: Chào buổi sáng quý vị. Bài thuyết trình hôm nay của tôi sẽ đi sâu phân tích các lợi ích dinh dưỡng tuyệt vời của việc bổ sung trái cây tươi vào chế độ ăn hàng ngày. "
        "Nhiều bệnh nhân thường băn khoăn về hàm lượng đường tự nhiên trong hoa quả, nhưng thực tế chất xơ dồi dào và các chất chống oxy hóa tự nhiên giúp kiểm soát đường huyết rất hiệu quả. "
        "Chúng ta sẽ cùng xem qua các biểu đồ nghiên cứu lâm sàng mới nhất được thực hiện trong 5 năm qua."
    )
}

# Individual Questions & Options Vietnamese translations for Test 3 Q32 - Q100
p3_p4_questions_t3_vi = {
    32: {
        "qVi": "Công ty đang thực hiện thay đổi gì?",
        "optVi": {"A": "(A) Công ty đang giảm một số mức giá.", "B": "(B) Công ty đang tuyển thêm nhân viên.", "C": "(C) Công ty đang chuyển đến một địa điểm mới.", "D": "(D) Công ty đang mở rộng một dòng sản phẩm."}
    },
    33: {
        "qVi": "Người đàn ông nói công ty sẽ làm gì?",
        "optVi": {"A": "(A) Quyên góp một số thiết bị", "B": "(B) Mở một chi nhánh quốc tế", "C": "(C) Tổ chức một buổi lễ kỷ niệm", "D": "(D) Cập nhật một trang web"}
    },
    34: {
        "qVi": "Người phụ nữ nói cô ấy sẽ làm gì?",
        "optVi": {"A": "(A) Đặt mua vé máy bay", "B": "(B) Liên hệ với một đồng nghiệp", "C": "(C) Ký một hợp đồng thuê", "D": "(D) Nộp một đơn xin việc"}
    },
    35: {
        "qVi": "Những người nói chuyện đang tham dự sự kiện nào?",
        "optVi": {"A": "(A) Một hội chợ thương mại y tế", "B": "(B) Một lễ trao giải thưởng công nghệ", "C": "(C) Một hội thảo giáo dục", "D": "(D) Một buổi gây quỹ từ thiện"}
    },
    36: {
        "qVi": "Người phụ nữ đặc biệt quan tâm đến điều gì?",
        "optVi": {"A": "(A) Các dụng cụ phẫu thuật", "B": "(B) Các công nghệ chẩn đoán hình ảnh", "C": "(C) Dược phẩm mới", "D": "(D) Phần mềm quản lý bệnh viện"}
    },
    37: {
        "qVi": "Người nam khuyên những người phụ nữ nên làm gì?",
        "optVi": {"A": "(A) Đăng ký thẻ hội viên", "B": "(B) Xem một buổi trình diễn sản phẩm", "C": "(C) Tham dự một buổi tiệc chiêu đãi", "D": "(D) Nói chuyện với một chuyên gia tư vấn"}
    },
    38: {
        "qVi": "Người phụ nữ đang thực hiện công việc gì?",
        "optVi": {"A": "(A) Lên kế hoạch cho một bữa tiệc", "B": "(B) Chuẩn bị một bài thuyết trình", "C": "(C) Viết một bài báo nghiên cứu", "D": "(D) Soạn thảo hợp đồng đối tác"}
    },
    39: {
        "qVi": "Người phụ nữ nhờ người đàn ông giúp đỡ điều gì?",
        "optVi": {"A": "(A) Kiểm tra lại các biểu đồ số liệu", "B": "(B) Đặt phòng họp", "C": "(C) In ấn tài liệu phát tay", "D": "(D) Sửa chữa máy tính"}
    },
    40: {
        "qVi": "Người đàn ông yêu cầu người phụ nữ làm gì?",
        "optVi": {"A": "(A) Gọi lại vào chiều nay", "B": "(B) Gửi tệp tài liệu qua email", "C": "(C) Gặp nhau tại căng-tin", "D": "(D) Hỏi ý kiến của trưởng phòng"}
    },
    41: {
        "qVi": "Người đàn ông đang gặp phải vấn đề gì?",
        "optVi": {"A": "(A) Anh ấy bị mất vé tàu.", "B": "(B) Tàu của anh ấy bị đổi sang sân ga khác.", "C": "(C) Anh ấy để quên hành lý.", "D": "(D) Chuyến tàu đã bị hủy hoàn toàn."}
    },
    42: {
        "qVi": "Tại sao chuyến tàu lại có sự thay đổi?",
        "optVi": {"A": "(A) Do thời tiết có tuyết rơi dày", "B": "(B) Do có công tác bảo trì đường ray", "C": "(C) Do thiếu nhân viên lái tàu", "D": "(D) Do sự cố mất điện"}
    },
    43: {
        "qVi": "Người phụ nữ khuyên người đàn ông nên làm gì?",
        "optVi": {"A": "(A) Yêu cầu hoàn lại tiền vé", "B": "(B) Đi qua cầu vượt sang Sân ga số 4", "C": "(C) Đợi chuyến tàu tiếp theo", "D": "(D) Đến quầy thông tin khách hàng"}
    },
    44: {
        "qVi": "Mục đích cuộc gọi của người đàn ông là gì?",
        "optVi": {"A": "(A) Để khiếu nại về một dịch vụ", "B": "(B) Để tìm kiếm các nhà đầu tư cho dự án", "C": "(C) Để đặt lịch hẹn phỏng vấn xin việc", "D": "(D) Để mời tham gia hội thảo"}
    },
    45: {
        "qVi": "Dự án kinh doanh của người đàn ông liên quan đến sản phẩm gì?",
        "optVi": {"A": "(A) Ứng dụng theo dõi sức khỏe", "B": "(B) Giá treo xe đạp thông minh cho căn hộ", "C": "(C) Xe đạp điện có thể gập gọn", "D": "(D) Hệ thống khóa xe chống trộm"}
    },
    46: {
        "qVi": "Người phụ nữ yêu cầu người đàn ông gửi cái gì vào cuối tuần?",
        "optVi": {"A": "(A) Một bản kế hoạch kinh doanh chi tiết", "B": "(B) Một sản phẩm mẫu dùng thử", "C": "(C) Thư giới thiệu từ khách hàng", "D": "(D) Bản sao bằng sáng chế"}
    },
    47: {
        "qVi": "Những người nói chuyện dự định sẽ đi đâu?",
        "optVi": {"A": "(A) Đến một cơ quan truyền hình", "B": "(B) Đến ngân hàng trung ương", "C": "(C) Đến một trường đại học kinh tế", "D": "(D) Đến trung tâm triển lãm nghệ thuật"}
    },
    48: {
        "qVi": "Họ sẽ làm gì tại địa điểm đó?",
        "optVi": {"A": "(A) Ký kết một thỏa thuận vay vốn", "B": "(B) Phỏng vấn vị giám đốc ngân hàng", "C": "(C) Tham gia một khóa tập huấn", "D": "(D) Kiểm toán hồ sơ tài chính"}
    },
    49: {
        "qVi": "Người đàn ông đề xuất điều gì về lộ trình di chuyển?",
        "optVi": {"A": "(A) Đi tuyến đường vành đai để tránh tắc đường", "B": "(B) Đi bằng tàu điện ngầm", "C": "(C) Khởi hành muộn hơn 30 phút", "D": "(D) Thuê một tài xế riêng"}
    },
    50: {
        "qVi": "Người đàn ông đã chuẩn bị xong những hạng mục nào cho sự kiện?",
        "optVi": {"A": "(A) Quà lưu niệm và thiệp chúc mừng", "B": "(B) Sảnh tiệc tại nhà hàng và bánh kem", "C": "(C) Âm thanh ánh sáng và ban nhạc", "D": "(D) Bài phát biểu và danh sách khách mời"}
    },
    51: {
        "qVi": "Sự kiện được chuẩn bị là sự kiện gì?",
        "optVi": {"A": "(A) Tiệc kỷ niệm ngày thành lập công ty", "B": "(B) Tiệc chia tay nghỉ hưu của Sabine Hoffman", "C": "(C) Lễ đón chào các thực tập sinh mới", "D": "(D) Bữa tiệc tất niên tổng kết năm"}
    },
    52: {
        "qVi": "Người phụ nữ hứa sẽ làm gì trước chiều nay?",
        "optVi": {"A": "(A) Thanh toán tiền đặt cọc", "B": "(B) Nhắc phòng nhân sự gửi danh sách chốt khách mời", "C": "(C) Gửi thiệp mời qua email", "D": "(D) Mua hoa tươi trang trí"}
    },
    53: {
        "qVi": "Mục đích chuyến thăm của ông Kota Ogawa là gì?",
        "optVi": {"A": "(A) Để nộp đơn xin việc làm", "B": "(B) Để khảo sát cơ sở vật chất khách sạn cho hội nghị", "C": "(C) Để giao một kiện hàng quan trọng", "D": "(D) Để kiểm tra an toàn phòng cháy"}
    },
    54: {
        "qVi": "Cô Ishikawa đang làm gì khi ông Ogawa đến?",
        "optVi": {"A": "(A) Đang tham gia một cuộc họp đột xuất", "B": "(B) Đang chuẩn bị tài liệu để tiếp đón", "C": "(C) Đang ăn trưa bên ngoài", "D": "(D) Đang nghe điện thoại của khách hàng"}
    },
    55: {
        "qVi": "Người phụ nữ đề nghị mang đến cho ông Ogawa thứ gì?",
        "optVi": {"A": "(A) Một cuốn tài liệu giới thiệu khách sạn", "B": "(B) Đồ uống giải khát (trà, cà phê, nước)", "C": "(C) Một chiếc ô che mưa", "D": "(D) Mật khẩu truy cập Wi-Fi"}
    },
    56: {
        "qVi": "Doanh số của mặt hàng nào đã tăng vọt trong tháng này?",
        "optVi": {"A": "(A) Táo nhập khẩu", "B": "(B) Dứa tươi", "C": "(C) Nước ép cam", "D": "(D) Chuối hữu cơ"}
    },
    57: {
        "qVi": "Nguyên nhân giúp doanh số bán hàng tăng là gì?",
        "optVi": {"A": "(A) Một chiến dịch giảm giá 50%", "B": "(B) Chiếc máy gọt dứa tự động mới lắp đặt", "C": "(C) Việc đổi nhà cung cấp mới", "D": "(D) Quảng cáo rầm rộ trên truyền hình"}
    },
    58: {
        "qVi": "Người phụ nữ đề xuất điều gì cho tương lai?",
        "optVi": {"A": "(A) Nhập thêm nhiều loại trái cây nhiệt đới", "B": "(B) Lắp thêm máy tương tự ở chi nhánh phía Bắc", "C": "(C) Tăng giá bán các loại hoa quả", "D": "(D) Thuê thêm nhân viên thu ngân"}
    },
    59: {
        "qVi": "Phòng khám nha khoa đang gặp phải vấn đề gì tuần này?",
        "optVi": {"A": "(A) Thiếu hụt dụng cụ nha khoa", "B": "(B) 3 bệnh nhân hủy lịch hẹn vào phút chót", "C": "(C) Máy điều hòa nhiệt độ bị hỏng", "D": "(D) Nhân viên tiếp tân xin nghỉ ốm"}
    },
    60: {
        "qVi": "Người phụ nữ đề xuất giải pháp nào?",
        "optVi": {"A": "(A) Phạt tiền những người hủy hẹn", "B": "(B) Triển khai hệ thống nhắn tin tự động nhắc hẹn trước 24 giờ", "C": "(C) Giảm bớt giờ làm việc", "D": "(D) Thuê thêm bác sĩ nha khoa"}
    },
    61: {
        "qVi": "Người đàn ông sẽ làm gì tiếp theo?",
        "optVi": {"A": "(A) Gọi điện cho các bệnh nhân đã hủy hẹn", "B": "(B) Liên hệ công ty phần mềm để kích hoạt tính năng nhắn tin", "C": "(C) Viết lại nội quy phòng khám", "D": "(D) Lên lịch họp toàn thể nhân viên"}
    },
    62: {
        "qVi": "Người nam muốn mua thứ gì cho nhân viên nhân dịp Năm Mới?",
        "optVi": {"A": "(A) Thẻ thành viên phòng tập thể dục", "B": "(B) Một món quà thiết thực và ý nghĩa", "C": "(C) Một chuyến du lịch nghỉ dưỡng", "D": "(D) Tiền thưởng bằng tiền mặt"}
    },
    63: {
        "qVi": "Những món quà nào được nhắc đến như là lựa chọn yêu thích?",
        "optVi": {"A": "(A) Bút ký cao cấp và sổ tay", "B": "(B) Bình giữ nhiệt in logo công ty và phiếu mua sách", "C": "(C) Hộp bánh quy và trà thượng hạng", "D": "(D) Đồng hồ đeo tay thông minh"}
    },
    64: {
        "qVi": "Người nam yêu cầu người nữ làm gì tiếp theo?",
        "optVi": {"A": "(A) Khảo sát ý kiến của toàn thể nhân viên", "B": "(B) Liên hệ nhà cung cấp xin báo giá cho 150 chiếc bình giữ nhiệt", "C": "(C) Tự tay đi chọn mẫu quà tặng", "D": "(D) Đặt in thiệp chúc mừng năm mới"}
    },
    65: {
        "qVi": "Đoàn làm phim đang chuẩn bị cho cảnh quay nào vào tuần tới?",
        "optVi": {"A": "(A) Một cảnh đám cưới ngoài trời", "B": "(B) Một cảnh rượt đuổi bằng xe hơi trên phố Maple", "C": "(C) Một cảnh quay bên trong nhà hàng", "D": "(D) Một cảnh đối thoại ở công viên"}
    },
    66: {
        "qVi": "Đoạn đường Maple đã được phê duyệt phong tỏa vào khoảng thời gian nào?",
        "optVi": {"A": "(A) Suốt cả ngày thứ Bảy", "B": "(B) Từ 8 giờ sáng đến 12 giờ trưa Chủ Nhật", "C": "(C) Vào các buổi tối trong tuần", "D": "(D) Từ 2 giờ đến 6 giờ chiều thứ Sáu"}
    },
    67: {
        "qVi": "Cơ quan nào đã phê duyệt kế hoạch điều tiết giao thông?",
        "optVi": {"A": "(A) Cảnh sát giao thông thành phố", "B": "(B) Ban quản lý tòa nhà", "C": "(C) Bộ Giao thông Vận tải", "D": "(D) Hiệp hội cư dân khu phố"}
    },
    68: {
        "qVi": "Những người nói chuyện đang thảo luận về dự án gì?",
        "optVi": {"A": "(A) Một bộ phim hoạt hình 3D", "B": "(B) Một trò chơi điện tử mới sắp ra mắt", "C": "(C) Một ứng dụng mạng xã hội", "D": "(D) Một trang web thương mại điện tử"}
    },
    69: {
        "qVi": "Nhóm thử nghiệm trò chơi đã phản hồi vấn đề gì?",
        "optVi": {"A": "(A) Đồ họa bị mờ", "B": "(B) Thời gian tải màn chơi ở màn 3 hơi chậm", "C": "(C) Cốt truyện quá khó hiểu", "D": "(D) Âm thanh nền quá ồn ào"}
    },
    70: {
        "qVi": "Người đàn ông sẽ làm gì trong ngày hôm nay?",
        "optVi": {"A": "(A) Hủy bỏ ngày phát hành chính thức", "B": "(B) Cùng đội ngũ lập trình tối ưu hóa lại mã nguồn trò chơi", "C": "(C) Thuê thêm người chơi thử nghiệm", "D": "(D) Thiết kế lại giao diện nhân vật"}
    },

    # Part 4: Q71 - Q100
    71: {
        "qVi": "Doanh nghiệp nào đang được quảng cáo?",
        "optVi": {"A": "(A) Một phòng khám y tế gia đình", "B": "(B) Một cửa hàng bán máy tính", "C": "(C) Một xưởng bảo dưỡng và sửa chữa ô tô", "D": "(D) Một đại lý môi giới bất động sản"}
    },
    72: {
        "qVi": "Doanh nghiệp này đã phục vụ cộng đồng trong bao lâu?",
        "optVi": {"A": "(A) Hơn năm năm", "B": "(B) Hơn mười năm", "C": "(C) Hơn hai mươi năm", "D": "(D) Hơn ba mươi năm"}
    },
    73: {
        "qVi": "Ưu đãi đặc biệt nào dành cho khách hàng trong tháng này?",
        "optVi": {"A": "(A) Giảm giá 20% cho dịch vụ thay dầu", "B": "(B) Tặng kèm đảo lốp và cân mâm miễn phí khi thay trọn bộ 4 lốp", "C": "(C) Rửa xe miễn phí trọn đời", "D": "(D) Tặng một năm bảo hiểm thân vỏ"}
    },
    74: {
        "qVi": "Chủ đề của tập podcast này là gì?",
        "optVi": {"A": "(A) Chiến lược đầu tư chứng khoán", "B": "(B) Tiềm năng và giới hạn của tiếp thị trên mạng xã hội", "C": "(C) Cách phát triển phần mềm di động", "D": "(D) Kỹ năng phỏng vấn xin việc thành công"}
    },
    75: {
        "qVi": "Đối tượng doanh nghiệp nào được tập trung thảo luận?",
        "optVi": {"A": "(A) Các tập đoàn đa quốc gia", "B": "(B) Các doanh nghiệp vừa và nhỏ", "C": "(C) Các tổ chức phi lợi nhuận", "D": "(D) Các bệnh viện tư nhân"}
    },
    76: {
        "qVi": "Vị khách mời hôm nay là ai?",
        "optVi": {"A": "(A) Một giáo sư kinh tế học", "B": "(B) Một chuyên gia truyền thông hàng đầu", "C": "(C) Một nhà phát triển ứng dụng", "D": "(D) Một nhà báo chuyên mục tài chính"}
    },
    77: {
        "qVi": "Chiều nay công ty cây xanh sẽ giao mặt hàng gì đến văn phòng?",
        "optVi": {"A": "(A) Bàn ghế làm việc mới", "B": "(B) Các chậu cây cảnh trang trí khu sinh hoạt chung", "C": "(C) Máy lọc nước uống", "D": "(D) Thùng đựng tài liệu lưu trữ"}
    },
    78: {
        "qVi": "Người nói chỉ ra lợi ích gì của việc có cây xanh trong văn phòng?",
        "optVi": {"A": "(A) Giúp văn phòng nhìn rộng rãi hơn", "B": "(B) Giúp giảm căng thẳng và cải thiện chất lượng không khí", "C": "(C) Giúp cách âm giữa các phòng ban", "D": "(D) Giúp giảm bớt tiền điện chiếu sáng"}
    },
    79: {
        "qVi": "Nhân viên cần lưu ý điều gì về thang máy chở hàng?",
        "optVi": {"A": "(A) Thang máy sẽ bị ngừng hoạt động cả ngày", "B": "(B) Đội giao hàng sẽ dùng thang máy từ 2 giờ đến 3 giờ chiều", "C": "(C) Thang máy chỉ dành cho khách hàng VIP", "D": "(D) Thang máy đang trong thời gian bảo dưỡng"}
    },
    80: {
        "qVi": "Công trình nào tại khu trung tâm đang chuẩn bị có diện mạo mới?",
        "optVi": {"A": "(A) Một nhà ga xe lửa cũ", "B": "(B) Một nhà máy giày bị bỏ hoang", "C": "(C) Một tòa thị chính cổ kính", "D": "(D) Một rạp chiếu phim lịch sử"}
    },
    81: {
        "qVi": "Tòa nhà này đang được cải tạo thành công trình gì?",
        "optVi": {"A": "(A) Một trung tâm mua sắm hiện đại", "B": "(B) Một trung tâm văn hóa và nghệ thuật cộng đồng đa năng", "C": "(C) Một khu chung cư cao tầng", "D": "(D) Một khách sạn năm sao"}
    },
    82: {
        "qVi": "Dự án dự kiến sẽ mở cửa đón công chúng vào thời điểm nào?",
        "optVi": {"A": "(A) Vào mùa xuân năm nay", "B": "(B) Vào mùa thu năm sau", "C": "(C) Vào cuối năm 2026", "D": "(D) Trong vòng 3 năm tới"}
    },
    83: {
        "qVi": "Người nói cập nhật thông tin về công trình giao thông nào?",
        "optVi": {"A": "(A) Dự án mở rộng sân bay quốc tế", "B": "(B) Dự án thay thế cầu Springdale", "C": "(C) Tuyến tàu điện trên cao mới", "D": "(D) Tuyến đường hầm xuyên núi"}
    },
    84: {
        "qVi": "Yếu tố nào đã giúp việc lắp dầm thép hoàn thành sớm hơn hai tuần?",
        "optVi": {"A": "(A) Công nghệ xây dựng tự động hóa mới", "B": "(B) Điều kiện thời tiết thuận lợi trong tháng vừa qua", "C": "(C) Việc bổ sung thêm 100 công nhân", "D": "(D) Việc tăng thêm ngân sách thưởng tiến độ"}
    },
    85: {
        "qVi": "Người tham gia giao thông cần chú ý điều gì vào các ngày cuối tuần tới?",
        "optVi": {"A": "(A) Cầu sẽ bị đóng hoàn toàn 24/24", "B": "(B) Việc trải thảm nhựa sẽ yêu cầu đóng làn đường một phần", "C": "(C) Tốc độ tối đa bị giảm xuống 20 km/h", "D": "(D) Cấm tất cả các loại xe tải lưu thông"}
    },
    86: {
        "qVi": "Khán giả đang tham dự sự kiện gì?",
        "optVi": {"A": "(A) Một triển lãm khởi nghiệp công nghệ", "B": "(B) Ngày thứ hai của chuỗi hội thảo kỹ năng lãnh đạo", "C": "(C) Lễ tốt nghiệp thạc sĩ quản trị", "D": "(D) Đại hội cổ đông thường niên"}
    },
    87: {
        "qVi": "Sau giờ nghỉ giải lao 15 phút, người tham gia sẽ làm gì?",
        "optVi": {"A": "(A) Lắng nghe một bài thuyết trình chuyên sâu", "B": "(B) Chia thành các nhóm nhỏ tại tầng hai để giải quyết tình huống", "C": "(C) Dùng bữa trưa tự chọn thân mật", "D": "(D) Tham gia một bài kiểm tra trắc nghiệm"}
    },
    88: {
        "qVi": "Người nói nhắc nhở mọi người mang theo vật dụng gì?",
        "optVi": {"A": "(A) Máy tính xách tay cá nhân", "B": "(B) Tập tài liệu bài tập đã phát vào sáng nay", "C": "(C) Danh thiếp để kết nối quan hệ", "D": "(D) Thẻ ra vào hội thảo"}
    },
    89: {
        "qVi": "Khách hàng đã thông báo vấn đề gì về chiếc xe sedan của mình?",
        "optVi": {"A": "(A) Hệ thống phanh phát ra tiếng kêu lạ", "B": "(B) Xe chạy có cảm giác bị ì ạch và không tăng tốc mượt mà", "C": "(C) Đèn pha phía trước bị chập chờn", "D": "(D) Cửa kính bên lái không kéo lên được"}
    },
    90: {
        "qVi": "Theo chuyên gia Adisa, bộ phận nào của xe rất có thể đang gặp sự cố?",
        "optVi": {"A": "(A) Bình ắc quy hoặc máy phát điện", "B": "(B) Bộ lọc nhiên liệu bị tắc hoặc bugi đánh lửa cần thay", "C": "(C) Hộp số tự động bị rò rỉ dầu", "D": "(D) Lốp xe bị non hơi"}
    },
    91: {
        "qVi": "Adisa đề xuất khách hàng nên làm gì vào sáng mai?",
        "optVi": {"A": "(A) Tự tháo bộ lọc ra vệ sinh tại nhà", "B": "(B) Mang xe qua xưởng để kiểm tra bằng máy quét chuyên dụng", "C": "(C) Gọi xe cứu hộ kéo xe về trạm", "D": "(D) Đặt mua phụ tùng thay thế trên mạng"}
    },
    92: {
        "qVi": "Khu vực trưng bày vừa được bài trí lại những sản phẩm nào?",
        "optVi": {"A": "(A) Dụng cụ làm vườn ngoài trời", "B": "(B) Bộ sưu tập nội thất phòng ngủ và phòng khách mới nhất", "C": "(C) Thiết bị nhà bếp thông minh", "D": "(D) Thảm trải sàn nhập khẩu từ Ba Tư"}
    },
    93: {
        "qVi": "Khách hàng đã gọi điện hỏi nhiều về thông tin gì?",
        "optVi": {"A": "(A) Chính sách giao hàng tận nhà miễn phí", "B": "(B) Chương trình khuyến mãi nhân dịp ra mắt bộ sưu tập mới", "C": "(C) Nguồn gốc xuất xứ của các loại gỗ", "D": "(D) Thời hạn bảo hành của nệm lò xo"}
    },
    94: {
        "qVi": "Người nói nhắc nhở nhân viên bán hàng điều gì?",
        "optVi": {"A": "(A) Luôn mặc đồng phục chỉnh tề khi đón khách", "B": "(B) Nắm rõ bảng giá ưu đãi và các gói trả góp để tư vấn", "C": "(C) Không để khách tự ý di chuyển đồ trưng bày", "D": "(D) Dọn dẹp sàn nhà sạch sẽ trước giờ mở cửa"}
    },
    95: {
        "qVi": "Emily gọi điện từ dịch vụ nào?",
        "optVi": {"A": "(A) Hãng hàng không quốc tế", "B": "(B) Dịch vụ xe đưa đón Speedy Services", "C": "(C) Trung tâm hỗ trợ du khách", "D": "(D) Khách sạn Grand Plaza"}
    },
    96: {
        "qVi": "Chuyến tàu của khách dự kiến đến ga lúc mấy giờ?",
        "optVi": {"A": "(A) Lúc 2:45 chiều", "B": "(B) Lúc 3:15 chiều", "C": "(C) Lúc 3:45 chiều", "D": "(D) Lúc 4:00 chiều"}
    },
    97: {
        "qVi": "Xe đưa đón của Emily sẽ đậu ở vị trí nào tại nhà ga?",
        "optVi": {"A": "(A) Bãi đỗ xe ngầm tầng hầm 2", "B": "(B) Khu vực đón khách số 3, bên ngoài lối ra chính", "C": "(C) Cổng kiểm soát vé số 1", "D": "(D) Trạm dừng xe buýt công cộng"}
    },
    98: {
        "qVi": "Chủ đề bài thuyết trình buổi sáng là gì?",
        "optVi": {"A": "(A) Tác hại của đồ uống có ga đối với men răng", "B": "(B) Lợi ích dinh dưỡng của việc ăn trái cây tươi hàng ngày", "C": "(C) Chế độ ăn kiêng không tinh bột", "D": "(D) Cách duy trì thói quen tập thể dục"}
    },
    99: {
        "qVi": "Nhiều bệnh nhân thường lo lắng về điều gì khi ăn trái cây?",
        "optVi": {"A": "(A) Hàm lượng đường tự nhiên trong hoa quả", "B": "(B) Dư lượng thuốc bảo vệ thực vật", "C": "(C) Giá thành các loại trái cây hữu cơ", "D": "(D) Khả năng gây dị ứng đường tiêu hóa"}
    },
    100: {
        "qVi": "Yếu tố nào trong trái cây giúp kiểm soát đường huyết hiệu quả?",
        "optVi": {"A": "(A) Hàm lượng nước dồi dào", "B": "(B) Lượng chất xơ phong phú và chất chống oxy hóa tự nhiên", "C": "(C) Các loại vitamin nhóm B", "D": "(D) Axit hữu cơ tự nhiên"}
    }
}

with open('scratch/t3_p3_p4_bilingual.json', 'w', encoding='utf-8') as f:
    json.dump({
        "dialogues_vi": {f"{s}_{e}": vi for (s, e), vi in p3_dialogues_vi.items()},
        "talks_vi": {f"{s}_{e}": vi for (s, e), vi in p4_talks_vi.items()},
        "questions_vi": {str(k): v for k, v in p3_p4_questions_t3_vi.items()}
    }, f, ensure_ascii=False, indent=2)

print("Saved Test 3 Part 3 & Part 4 bilingual data successfully!")
