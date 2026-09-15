# scratch/t2_bilingual_part3_4.py: Full translations for Test 2 Part 3 & Part 4
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

# Dialogue and Talk Vietnamese translations mapping by question ID range
p3_dialogues_vi = {
    (32, 34): (
        "Người nữ: Chào buổi sáng, Thuyền trưởng. Chúng ta sẽ cập cảng ở Kolkata vào tối nay, đúng không ạ?\n"
        "Người nam: Thực ra, chúng ta đã phải đổi hải trình trong đêm để tránh một cơn bão, vì vậy chúng ta đang bị chậm so với lịch trình. Nhưng chúng ta sẽ đến nơi vào sáng sớm mai.\n"
        "Người nữ: Ồ, như vậy cũng không tệ lắm.\n"
        "Người nam: Hector hôm nay được nghỉ phép. Vì vậy tôi cần cô đi tuần tra ca sáng, bắt đầu bằng việc kiểm tra máy móc trong buồng máy nhé.\n"
        "Người nữ: Tất nhiên rồi, tôi sẽ xuống đó ngay bây giờ."
    ),
    (35, 37): (
        "Người nam: Xin chào, tôi đến đây để đăng ký một số buổi tập với huấn luyện viên cá nhân.\n"
        "Người nữ: Được chứ, mục tiêu thể hình của anh là gì vậy?\n"
        "Người nam: Tôi muốn nâng tạ và tăng cường thể lực.\n"
        "Người nữ: Tôi có thể hướng dẫn anh việc đó. Hiện tại anh đã là hội viên ở đây chưa?\n"
        "Người nam: Chưa, nhưng bên bạn có ưu đãi giảm giá cho sinh viên không?\n"
        "Người nữ: Có chứ, sinh viên chính quy được giảm 15%. Để tôi dẫn anh đi tham quan cơ sở vật chất và các máy móc thiết bị trước nhé."
    ),
    (38, 40): (
        "Người nữ: Như anh thấy đấy, bức tranh phong cảnh thời Phục hưng mà chúng ta mới mua về đang trong tình trạng rất tệ. Chúng ta chưa thể trưng bày nó được.\n"
        "Người nam: Ừm, đúng vậy, bức tranh này sẽ cần công việc phục chế đáng kể đấy. Tôi sẽ bắt đầu bằng việc kiểm tra xem liệu lớp véc-ni bị biến màu có thể được loại bỏ an toàn mà không làm hỏng lớp sơn bên dưới hay không.\n"
        "Người nữ: Tuyệt vời. Anh có thể bắt đầu ngay tuần này được không? Sự kiện dạ tiệc kỷ niệm của bảo tàng đang đến gần rồi, và giám đốc muốn bức tranh này được treo ở phòng trưng bày chính."
    ),
    (41, 43): (
        "Người nữ: Chào Ozone. Anh có thời gian xem qua vài trang slide tôi sẽ trình bày trong cuộc họp vào thứ Năm không?\n"
        "Người nam: Ồ, đó có phải cuộc họp với Tập đoàn Smith không?\n"
        "Người nữ: Đúng rồi, tôi sẽ trình bày với họ kế hoạch tiếp thị cập nhật cho chuỗi nhà sách bán lẻ trên toàn quốc của họ.\n"
        "Người nam: Vì chúng ta đã làm việc thân thiết với đội ngũ của họ nhiều năm rồi, tôi nghĩ buổi họp nên giữ không khí thoải mái, thân mật như một cuộc trò chuyện thay vì quá trịnh trọng.\n"
        "Người nữ: Tôi hoàn toàn đồng ý với gợi ý đó."
    ),
    (44, 46): (
        "Người nữ: Tôi nghe nói kết quả thí nghiệm của anh tốt hơn nhiều so với dự kiến. Xin chúc mừng nhé!\n"
        "Người nam: Cảm ơn cô. Tôi từng nghĩ chúng tôi sẽ phải chạy phản ứng đó 10 lần mới có kết quả khả quan, nhưng chúng tôi đã thành công ngay lần thứ hai.\n"
        "Người nữ: Anh nên viết một bản báo cáo tóm tắt cho Esra ngay đi.\n"
        "Người nam: À, tuần tới Esra sẽ rời công ty rồi.\n"
        "Người nữ: Vậy à? Thế kế hoạch sắp tới của anh là gì?\n"
        "Người nam: Tôi hy vọng sẽ được dẫn dắt nhóm nghiên cứu vào quý tới để tích lũy thêm kinh nghiệm quản lý."
    ),
    (47, 49): (
        "Người nữ: Bây giờ chúng ta sẽ chuyển sang một chuyên mục đặc biệt của chương trình thời sự, nơi chúng tôi giới thiệu các doanh nghiệp địa phương mới tới khán giả. Hôm nay tôi đang trò chuyện cùng Drove Bahaj, một huấn luyện viên cá nhân kiêm chủ phòng tập thể hình. Cảm ơn anh đã tham gia chương trình.\n"
        "Người nam: Cảm ơn bạn. Chúng tôi vừa khai trương cơ sở phòng tập thứ hai tại khu trung tâm vào tháng trước.\n"
        "Người nữ: Tuyệt vời. Anh có thể chia sẻ cho khán giả biết về con đường sự nghiệp của anh và cách anh chuyển đổi từ vận động viên sang chủ doanh nghiệp không?"
    ),
    (50, 52): (
        "Người nam: Với tư cách là giám đốc, tôi rất vui mừng được chào đón cô đến với Viện Thủy sinh Redmond. Chúng tôi rất vui vì cô sẽ sản xuất nội dung bài viết cho trang web của chúng tôi.\n"
        "Người nữ: Tôi rất mong chờ được viết bài về các sáng kiến và nỗ lực bảo tồn môi trường thủy sinh của Redmond.\n"
        "Người nam: Sứ mệnh hàng đầu của chúng tôi là bảo vệ hệ sinh thái biển và các loài sinh vật ven bờ.\n"
        "Người nữ: Điều tôi thấy thực sự hào hứng là chúng ta sẽ sử dụng các thiết bị camera lặn ngầm hiện đại để ghi lại những thước phim trực tiếp dưới đáy đại dương."
    ),
    (53, 55): (
        "Người nữ: Matthew, anh không định hủy cuộc họp ngân sách vào thứ Tư chứ?\n"
        "Người nam: Tôi vẫn chưa gửi thông báo hủy, nhưng các đối tác nghiên cứu của chúng ta ở Trung Quốc tuần này được nghỉ lễ quốc gia, nên sẽ không có cập nhật dự án nào từ họ đâu.\n"
        "Người nữ: Nhưng chúng ta vẫn chưa phân bổ kinh phí cho vị trí trưởng dự án mà! Cuộc họp vẫn cần phải diễn ra.\n"
        "Người nam: Vậy còn các khoản chi phí đi lại dự kiến thì sao?\n"
        "Người nữ: Chúng hoàn toàn không cần thiết, vì chúng ta hoàn toàn có thể họp trực tuyến."
    ),
    (56, 58): (
        "Người nam: Xin chào, đây là bộ phận hỗ trợ kỹ thuật.\n"
        "Người nữ: Tôi gọi đến từ Công ty Thiết bị Nhà hàng Ruben. Gần đây tôi có mua phần mềm của bên anh để quản lý hàng tồn kho trong kho của mình, và tôi có câu hỏi về việc cài đặt cảnh báo.\n"
        "Người nam: Vâng, tôi có thể hướng dẫn cô. Cô chỉ cần vào phần Cài đặt, chọn mục Thông báo và chỉnh lại mức giới hạn số lượng theo ý mình là được."
    ),
    (59, 61): (
        "Người nữ: Tôi vừa nói chuyện với giám đốc vườn thực vật. Ông ấy muốn chúng ta lắp đặt hệ thống tưới nước tự động trong vườn hoa hồng, cũng như ở khu vườn mộc lan. Ông ấy muốn đảm bảo hoa nhận đủ nước trong mùa hè nóng nực.\n"
        "Người nam: Được rồi. Chúng ta có thể vẫn còn một số ống nước và vòi phun trong kho chứa đồ phía sau nhà kính. Để tôi đi kiểm tra vật tư ngay bây giờ."
    ),
    (62, 64): (
        "Người nam: Chào buổi sáng, cô Al Jahani. Xin lỗi cô tôi đến hơi muộn. Giao thông sáng nay tắc đường khủng khiếp quá.\n"
        "Người nữ: Không sao, nhưng văn phòng cho thuê xe của chúng ta sáng nay sẽ rất bận đấy. Có một hội nghị giáo dục lớn bắt đầu hôm nay, nên nhiều người tham dự sẽ đến thuê xe.\n"
        "Người nam: Tôi hiểu rồi. Tôi nên bắt đầu từ đâu?\n"
        "Người nữ: Anh hãy ra Khu vực 2 (Area 2) trước để kiểm tra lại dàn xe sedan cỡ nhỏ nhé."
    ),
    (65, 67): (
        "Người nam: Tôi vừa đi nghỉ phép về nên đã lỡ cuộc họp của bộ phận. Cô có thể cập nhật tình hình cho tôi không?\n"
        "Người nữ: Mọi chương trình cộng đồng và sự kiện công cộng của chúng ta đều đúng tiến độ. Tháng sau chúng ta sẽ tổ chức một cuộc thi vẽ áp phích cho học sinh tiểu học.\n"
        "Người nam: Còn dự án công viên thì sao?\n"
        "Người nữ: Chúng ta sẽ phát tặng 200 cây giống cây Eastern redbud (cây cành đỏ miền Đông) có hoa màu hồng tím rất đẹp."
    ),
    (68, 70): (
        "Người nam: Xin chào. Cho tôi một ly cà phê đen lớn và một phần bánh trứng phô mai nhé.\n"
        "Người nữ: Vâng, của anh hết 8 đô la. Anh có phải là khách hàng ưu tiên của tiệm không ạ?\n"
        "Người nam: Không, nhưng tôi có thẻ Easy Cash.\n"
        "Người nữ: Tuyệt, thẻ đó được giảm 2% trên tổng hóa đơn đấy ạ.\n"
        "Người nam: Tốt quá. Chiều nay tôi sẽ gọi điện cho bên ngân hàng phát hành thẻ để hỏi thêm về việc gia hạn."
    )
}

p4_talks_vi = {
    (71, 73): (
        "Người nói: Chào Amina. Tôi là Sabine gọi đến từ Blue Drop Creations. Tôi vừa mới gửi bưu điện đôi bông tai và các dây chuyền mà bạn đã đặt làm từ tôi. "
        "Bởi vì bạn đã là khách hàng thân thiết gắn bó hơn 10 năm qua, tôi cũng gửi kèm một chiếc hộp đựng trang sức thủ công như một món quà tri ân. "
        "Khi nhận được kiện hàng, xin vui lòng gọi lại cho tôi để chia sẻ cảm nhận và đóng góp ý kiến phản hồi về những mẫu thiết kế này nhé."
    ),
    (74, 76): (
        "Người nói: Chào buổi sáng. Tôi là Brandon từ Công ty Đóng Khung Dakota, xin gọi lại theo yêu cầu của bạn. "
        "Chúng tôi đã nhận được tin nhắn thoại của bạn về việc muốn đóng khung một bức ảnh cưới. "
        "Bạn không cần phải tự in ảnh ra đâu; bạn chỉ cần tải tệp ảnh kỹ thuật số lên trang web của chúng tôi, chọn mẫu khung viền và đặt đơn hàng trực tuyến. "
        "Nếu trả thêm một khoản phụ phí nhỏ, bạn sẽ nhận được gói bảo hành kính chống vỡ mở rộng."
    ),
    (77, 79): (
        "Người nói: Chào mừng tất cả các bạn đến với buổi tập huấn tuần này trong chuỗi chương trình chăm sóc người bệnh của chúng ta. "
        "Trung tâm vật lý trị liệu của chúng ta luôn nổi tiếng với dịch vụ chăm sóc tận tâm dành cho bệnh nhân, và đó là nhờ có đội ngũ nhân viên y tế tuyệt vời như các bạn. "
        "Hôm nay, thay vì chỉ nghe thuyết trình, tôi đã chuẩn bị nhiều hoạt động tương tác đóng vai để chúng ta cùng thực hành. "
        "Tuy nhiên, do tôi phải rời đi lúc giữa trưa để dự họp ban điều hành, một số nội dung hôm nay sẽ được chuyển sang buổi sau."
    ),
    (80, 82): (
        "Người nói: Bạn có phải là một tài xế xe tải thương mại có chứng chỉ? Công ty Vận Tải Quá Khổ Hoffman hiện đang tìm kiếm các tài xế giàu kinh nghiệm gia nhập đội ngũ của chúng tôi. "
        "Chúng tôi chuyên vận chuyển các lô hàng siêu trường siêu trọng trên toàn quốc. "
        "Khác với các đối thủ cạnh tranh áp đặt lịch trình cứng nhắc, công ty chúng tôi mang đến thời gian làm việc linh hoạt, cho phép bạn tự chọn ca làm và tuyến đường. "
        "Hãy truy cập trang web của chúng tôi ngay hôm nay để nhận thêm thông tin chi tiết và nộp hồ sơ."
    ),
    (83, 85): (
        "Người nói: Chào Genew. Tôi có tin rất hào hứng đây. Chương trình truyền hình The Farmer's Table muốn đưa nhà hàng chúng ta lên sóng trong một tập sắp tới! "
        "Họ sẽ đến vào thứ Tư để quay cảnh mọi người làm việc trong gian bếp. "
        "Vì đoàn quay phim đến rất sớm lúc 7 giờ sáng, bạn có thể đi làm sớm hơn một tiếng vào thứ Tư để giúp chuẩn bị nguyên liệu không? "
        "Tuần sau tôi sẽ đi công tác tới một lễ hội ẩm thực ở Chicago, nên mọi việc ở bếp trông cậy vào bạn nhé."
    ),
    (86, 88): (
        "Người nói: Chào buổi tối quý khán giả, cảm ơn quý vị đang theo dõi bản tin Channel 4 News. "
        "Tôi đang có mặt tại Rockville, một vùng ngoại ô của khu vực đô thị. "
        "Rockville vừa được chọn làm địa điểm xây dựng nhà máy sản xuất pin xe điện trị giá nhiều triệu đô la. "
        "Trong buổi điều trần công khai tối qua, không ai đưa ra bình luận phản đối nào, cho thấy dự án nhận được sự đồng thuận cao từ cộng đồng. "
        "Bắt đầu từ ngày mai, người dân có thể đến sảnh tòa nhà thị chính để xem các hình ảnh và bản vẽ phối cảnh của dự án."
    ),
    (89, 91): (
        "Người nói: Bạn có mệt mỏi vì hay thất lạc đồ đạc trên bàn làm việc do quá bừa bộn không? "
        "Nếu có, chiếc khay sắp xếp bàn làm việc Optimum Space Organizer chính là giải pháp dành cho bạn. "
        "Sản phẩm có các ngăn chứa đồ thông minh có thể điều chỉnh kích thước linh hoạt, giúp bạn để vừa cả máy tính bảng, sổ tay và văn phòng phẩm. "
        "Đặc biệt, nếu gọi điện đặt hàng qua số tổng đài miễn cước trong vòng 20 phút tới, bạn sẽ được giảm giá ngay 20% trên tổng hóa đơn!"
    ),
    (92, 94): (
        "Người nói: Cảm ơn các bạn đã lắng nghe tập podcast Fabulous Foods tuần này. "
        "Mỗi tuần, chúng tôi đều giới thiệu một loại rau củ nguyên liệu riêng biệt và các phương pháp nấu nướng để tôn vinh hương vị tối đa. "
        "Trước khi bắt đầu, tôi xin lưu ý rằng dòng sách công thức đặc biệt này sẽ không có sẵn lâu đâu, vì vậy hãy nhanh tay đặt hàng ngay hôm nay nhé. "
        "Khách mời tuần này của chúng ta là đầu bếp tài năng Rebecca Murray, người vừa khai trương một nhà hàng mới ấm cúng tại Seattle."
    ),
    (95, 97): (
        "Người nói: Xin quý hành khách chú ý. Công tác cải tạo và nâng cấp nhà ga xe lửa của chúng ta đang được tiến hành. "
        "Chúng tôi thành thật xin lỗi vì sự bất tiện do tiếng ồn công trường gây ra. "
        "Do thang máy số 2 đang tạm ngưng phục vụ, quý hành khách cần hỗ trợ vận chuyển hành lý nặng xin vui lòng liên hệ nhân viên nhà ga tại Quầy số 4. "
        "Chuyến tàu 133 đi Hartford dự kiến sẽ đến điểm dừng tiếp theo vào lúc 12:05 trưa."
    ),
    (98, 100): (
        "Người nói: Xin chào mọi người. Tôi là Carmen Salazar, giám đốc vận hành sân bay, xin cảm ơn các phóng viên báo chí đã đến tham dự buổi họp báo hôm nay. "
        "Công tác thi công tại Nhà ga C hiện đang bị chậm tiến độ khoảng 4 tuần do thiếu hụt chuỗi cung ứng vật tư, điều này sẽ ảnh hưởng trực tiếp tới hãng hàng không Selca Air. "
        "Trước khi bước vào phần hỏi đáp, tôi trân trọng mời các bạn cùng đến xem mô hình thu nhỏ 3D của nhà ga mới được trưng bày tại góc phòng."
    )
}

# Individual Questions & Options Vietnamese translations for Q32 - Q100
p3_p4_questions_vi = {
    32: {
        "qVi": "Cuộc hội thoại rất có thể đang diễn ra ở đâu?",
        "optVi": {"A": "(A) Trên tàu hỏa", "B": "(B) Trên một chiếc thuyền/tàu thủy", "C": "(C) Tại một nhà xưởng", "D": "(D) Tại một sân bay"}
    },
    33: {
        "qVi": "Điều gì đã gây ra sự chậm trễ?",
        "optVi": {"A": "(A) Một bộ phận động cơ bị hỏng", "B": "(B) Quy định đã thay đổi", "C": "(C) Giao thông bị tắc nghẽn", "D": "(D) Thời tiết xấu"}
    },
    34: {
        "qVi": "Người đàn ông sẽ làm gì tiếp theo?",
        "optVi": {"A": "(A) Chuẩn bị bữa ăn", "B": "(B) Sửa chữa điện thoại", "C": "(C) Kiểm tra máy móc thiết bị", "D": "(D) Liên hệ với khách hàng"}
    },
    35: {
        "qVi": "Người phụ nữ rất có thể làm việc ở đâu?",
        "optVi": {"A": "(A) Tại một phòng khám y tế", "B": "(B) Tại một trung tâm thể hình/thể dục", "C": "(C) Tại một cửa hàng bán đồ thể thao", "D": "(D) Tại một trường đại học"}
    },
    36: {
        "qVi": "Người đàn ông hỏi về điều gì?",
        "optVi": {"A": "(A) Một khoản giảm giá", "B": "(B) Một huấn luyện viên khác", "C": "(C) Tủ để đồ cá nhân", "D": "(D) Lớp học bơi lội"}
    },
    37: {
        "qVi": "Người phụ nữ sẽ làm gì tiếp theo?",
        "optVi": {"A": "(A) Đặt lịch hẹn", "B": "(B) Xử lý khoản thanh toán", "C": "(C) Dẫn đi tham quan một vòng", "D": "(D) Giới thiệu một đồng nghiệp"}
    },
    38: {
        "qVi": "Những người nói chuyện rất có thể là ai?",
        "optVi": {"A": "(A) Những người phục chế tác phẩm nghệ thuật", "B": "(B) Những người mua bất động sản", "C": "(C) Các nhà báo", "D": "(D) Các nhà khoa học môi trường"}
    },
    39: {
        "qVi": "Người phụ nữ nói cô ấy sẽ làm gì?",
        "optVi": {"A": "(A) Liên hệ với một đại lý", "B": "(B) Đặt mua một số vật tư", "C": "(C) Tạo một ngân sách", "D": "(D) Điều tra, khảo sát một vấn đề"}
    },
    40: {
        "qVi": "Tại sao người đàn ông lại đề xuất bắt đầu dự án nhanh chóng?",
        "optVi": {"A": "(A) Một ngân sách sắp hết hạn", "B": "(B) Một hợp đồng sắp kết thúc", "C": "(C) Một sự kiện quan trọng đang đến gần", "D": "(D) Một đồng nghiệp sắp nghỉ hưu"}
    },
    41: {
        "qVi": "Người phụ nữ đang chuẩn bị cái gì?",
        "optVi": {"A": "(A) Một bài thuyết trình bằng slide", "B": "(B) Một ngân sách dự án", "C": "(C) Một bản hợp đồng", "D": "(D) Một tài liệu phát tay đào tạo"}
    },
    42: {
        "qVi": "Smith Incorporated là loại hình doanh nghiệp nào?",
        "optVi": {"A": "(A) Một công ty quảng cáo", "B": "(B) Một nhà sản xuất giấy", "C": "(C) Một nhà phân phối phần mềm", "D": "(D) Một chuỗi hiệu sách"}
    },
    43: {
        "qVi": "Hai người đồng ý với nhau về điều gì?",
        "optVi": {"A": "(A) Nên dời lại một cuộc họp", "B": "(B) Một dự án cần thêm kinh phí", "C": "(C) Nên tạo một video", "D": "(D) Một cuộc họp nên diễn ra thân mật, thoải mái"}
    },
    44: {
        "qVi": "Tại sao người phụ nữ lại chúc mừng người đàn ông?",
        "optVi": {"A": "(A) Anh ấy vừa được thăng chức", "B": "(B) Anh ấy đã đạt chỉ tiêu bán hàng", "C": "(C) Thí nghiệm của anh ấy đã thành công", "D": "(D) Bản đề xuất của anh ấy đã được phê duyệt"}
    },
    45: {
        "qVi": "Người đàn ông ngụ ý điều gì khi nói: 'Esra's leaving the company next week'?",
        "optVi": {"A": "(A) Anh ấy sẽ ứng tuyển vào vị trí của Esra", "B": "(B) Anh ấy sẽ không nộp báo cáo cho Esra", "C": "(C) Anh ấy muốn tổ chức tiệc chia tay cho Esra", "D": "(D) Anh ấy sẽ tiếp quản các khách hàng của Esra"}
    },
    46: {
        "qVi": "Người đàn ông hy vọng sẽ làm gì vào quý tới?",
        "optVi": {"A": "(A) Chuyển sang văn phòng khác", "B": "(B) Đi công tác nước ngoài", "C": "(C) Học một kỹ năng kỹ thuật mới", "D": "(D) Tích lũy kinh nghiệm quản lý"}
    },
    47: {
        "qVi": "Những người nói chuyện rất có thể đang ở đâu?",
        "optVi": {"A": "(A) Tại một phòng khám y tế", "B": "(B) Tại một trường quay truyền hình", "C": "(C) Tại một sự kiện thể thao", "D": "(D) Tại một lễ trao giải thưởng"}
    },
    48: {
        "qVi": "Người đàn ông cho biết gần đây anh ấy đã làm gì?",
        "optVi": {"A": "(A) Đã viết một cuốn sách", "B": "(B) Đã giành một giải thưởng", "C": "(C) Đã mở một cơ sở mới", "D": "(D) Đã thuê một giám đốc tiếp thị"}
    },
    49: {
        "qVi": "Người phụ nữ yêu cầu người đàn ông nói về điều gì?",
        "optVi": {"A": "(A) Con đường phát triển sự nghiệp của anh ấy", "B": "(B) Kế hoạch mở rộng kinh doanh", "C": "(C) Một chế độ tập luyện thể dục", "D": "(D) Một chiến dịch quảng bá"}
    },
    50: {
        "qVi": "Người phụ nữ được tuyển dụng để làm công việc gì?",
        "optVi": {"A": "(A) Viết các bài báo/nội dung", "B": "(B) Thiết kế một trang web", "C": "(C) Dẫn các tour du lịch", "D": "(D) Tiến hành các thí nghiệm khoa học"}
    },
    51: {
        "qVi": "Theo vị giám đốc, mục tiêu của tổ chức là gì?",
        "optVi": {"A": "(A) Thu hút thêm du khách", "B": "(B) Xuất bản một tạp chí khoa học", "C": "(C) Quyên góp quỹ tài trợ", "D": "(D) Bảo vệ môi trường thủy sinh"}
    },
    52: {
        "qVi": "Roberto cho biết điều gì là rất hào hứng?",
        "optVi": {"A": "(A) Việc sử dụng một số trang thiết bị", "B": "(B) Sự hợp tác với một trường đại học", "C": "(C) Một địa điểm nghiên cứu mới", "D": "(D) Một buổi thuyết trình sắp diễn ra"}
    },
    53: {
        "qVi": "Người đàn ông nói gì về một số đối tác liên hệ ở Trung Quốc?",
        "optVi": {"A": "(A) Họ đã ký một hợp đồng mới", "B": "(B) Họ sắp đến thăm văn phòng", "C": "(C) Họ đang đón mừng một kỳ nghỉ lễ", "D": "(D) Họ đang gặp trục trặc kỹ thuật"}
    },
    54: {
        "qVi": "Người phụ nữ ngụ ý điều gì khi nói: 'we didn't allocate funds for a project leader'?",
        "optVi": {"A": "(A) Một dự án nên bị hủy bỏ", "B": "(B) Cần thuê thêm nhân viên tư vấn", "C": "(C) Một cuộc họp đã lên lịch vẫn nên diễn ra", "D": "(D) Ngân sách chi tiêu cần được cắt giảm"}
    },
    55: {
        "qVi": "Người phụ nữ nói gì về một số chi phí đi lại?",
        "optVi": {"A": "(A) Chúng là không cần thiết", "B": "(B) Chúng đã được hoàn trả lại", "C": "(C) Chúng vượt quá dự toán", "D": "(D) Chúng cần được phê duyệt"}
    },
    56: {
        "qVi": "Người phụ nữ đang gọi điện đến từ đâu?",
        "optVi": {"A": "(A) Một nhà hàng ẩm thực", "B": "(B) Một công ty phần mềm máy tính", "C": "(C) Một công ty cung cấp thiết bị nhà hàng", "D": "(D) Một kho bãi vận tải"}
    },
    57: {
        "qVi": "Phần mềm đang được sử dụng cho mục đích gì?",
        "optVi": {"A": "(A) Quản lý hàng tồn kho", "B": "(B) Xử lý bảng lương", "C": "(C) Theo dõi các đơn đặt hàng", "D": "(D) Lên lịch làm việc cho nhân viên"}
    },
    58: {
        "qVi": "Người đàn ông giúp người phụ nữ làm điều gì?",
        "optVi": {"A": "(A) Khôi phục mật khẩu", "B": "(B) Tùy chỉnh một mục cài đặt", "C": "(C) Cập nhật một ứng dụng", "D": "(D) Đổi trả một sản phẩm"}
    },
    59: {
        "qVi": "Những người nói chuyện rất có thể đang làm việc ở đâu?",
        "optVi": {"A": "(A) Tại một trang trại nông nghiệp", "B": "(B) Tại một vườn bách thảo/vườn thực vật", "C": "(C) Tại một công ty cảnh quan", "D": "(D) Tại một trung tâm làm vườn"}
    },
    60: {
        "qVi": "Những người nói chuyện đã được yêu cầu làm gì?",
        "optVi": {"A": "(A) Cắt tỉa một số cành cây", "B": "(B) Trồng các khóm hoa mới", "C": "(C) Lắp đặt một hệ thống tưới nước", "D": "(D) Xây dựng một lối đi bộ"}
    },
    61: {
        "qVi": "Người đàn ông đề nghị làm điều gì?",
        "optVi": {"A": "(A) Đi tìm kiếm một số vật liệu/vật tư", "B": "(B) Gọi điện cho một nhà cung cấp", "C": "(C) Kiểm tra dự báo thời tiết", "D": "(D) Nhờ thêm đồng nghiệp giúp đỡ"}
    },
    62: {
        "qVi": "Tại sao người đàn ông lại xin lỗi?",
        "optVi": {"A": "(A) Anh ấy quên một tài liệu", "B": "(B) Anh ấy đã đến muộn", "C": "(C) Anh ấy làm hỏng một thiết bị", "D": "(D) Anh ấy gửi nhầm email"}
    },
    63: {
        "qVi": "Theo người phụ nữ, tại sao hôm nay họ sẽ rất bận rộn?",
        "optVi": {"A": "(A) Có một đợt giảm giá lớn", "B": "(B) Văn phòng bị thiếu nhân sự", "C": "(C) Có một hội nghị đang diễn ra trong thành phố", "D": "(D) Họ đang chuyển văn phòng"}
    },
    64: {
        "qVi": "Nhìn vào hình ảnh. Người đàn ông sẽ đi đến đâu đầu tiên?",
        "optVi": {"A": "(A) Khu vực 1 (Area 1)", "B": "(B) Khu vực 2 (Area 2)", "C": "(C) Khu vực 3 (Area 3)", "D": "(D) Khu vực 4 (Area 4)"}
    },
    65: {
        "qVi": "Những người nói chuyện rất có thể làm việc ở đâu?",
        "optVi": {"A": "(A) Tại một công ty kiến trúc", "B": "(B) Tại một cơ quan chính quyền địa phương", "C": "(C) Tại một công ty tổ chức sự kiện", "D": "(D) Tại một trường tiểu học"}
    },
    66: {
        "qVi": "Người phụ nữ nói điều gì sẽ diễn ra vào tháng tới?",
        "optVi": {"A": "(A) Một lễ khánh thành công viên", "B": "(B) Một hội chợ việc làm", "C": "(C) Một cuộc thi vẽ áp phích", "D": "(D) Một buổi hòa nhạc gây quỹ"}
    },
    67: {
        "qVi": "Nhìn vào hình ảnh. Loại cây giống nào sẽ được phát tặng miễn phí?",
        "optVi": {"A": "(A) Cây Eastern redbud (cành đỏ miền Đông)", "B": "(B) Cây Sugar maple (phong đường)", "C": "(C) Cây White oak (sồi trắng)", "D": "(D) Cây Flowering dogwood (thù du hoa)"}
    },
    68: {
        "qVi": "Cuộc hội thoại rất có thể đang diễn ra ở đâu?",
        "optVi": {"A": "(A) Tại một quán cà phê", "B": "(B) Tại một cửa hàng tạp hóa", "C": "(C) Tại một ngân hàng", "D": "(D) Tại một tiệm bánh mì"}
    },
    69: {
        "qVi": "Nhìn vào hình ảnh. Người đàn ông sẽ tiết kiệm được bao nhiêu phần trăm khi mua hàng?",
        "optVi": {"A": "(A) 5%", "B": "(B) 10%", "C": "(C) 15%", "D": "(D) 2%"}
    },
    70: {
        "qVi": "Người đàn ông nói anh ấy sẽ làm gì vào chiều nay?",
        "optVi": {"A": "(A) Gọi điện cho một doanh nghiệp/ngân hàng", "B": "(B) Đăng ký một chương trình hội viên", "C": "(C) Đến thăm một người bạn", "D": "(D) Nộp lại một biên lai"}
    },

    # Part 4: Q71 - Q100
    71: {
        "qVi": "Người nói rất có thể là ai?",
        "optVi": {"A": "(A) Chủ một phòng triển lãm nghệ thuật", "B": "(B) Một nhà tạo mẫu tóc", "C": "(C) Một nhà thiết kế thời trang", "D": "(D) Một người thợ làm đồ trang sức"}
    },
    72: {
        "qVi": "Tại sao người nói lại gửi kèm một món quà đặc biệt?",
        "optVi": {"A": "(A) Vì người nghe đã giới thiệu khách hàng mới", "B": "(B) Nhân dịp sinh nhật người nghe", "C": "(C) Vì người nghe là khách hàng thân thiết gắn bó", "D": "(D) Để bù đắp cho việc giao hàng chậm"}
    },
    73: {
        "qVi": "Tại sao người nghe lại được yêu cầu gọi lại?",
        "optVi": {"A": "(A) Để đóng góp ý kiến phản hồi", "B": "(B) Để xác nhận địa chỉ giao hàng", "C": "(C) Để thanh toán hóa đơn", "D": "(D) Để đặt thêm đơn hàng khác"}
    },
    74: {
        "qVi": "Người nghe muốn làm điều gì?",
        "optVi": {"A": "(A) Mua một máy in ảnh", "B": "(B) Đặt lịch chụp ảnh cưới", "C": "(C) Tham gia một lớp học nhiếp ảnh", "D": "(D) Đem đóng khung một bức ảnh"}
    },
    75: {
        "qVi": "Người nói muốn người nghe làm gì trên trang web?",
        "optVi": {"A": "(A) Để lại đánh giá nhận xét", "B": "(B) Đặt một đơn hàng", "C": "(C) Đăng ký nhận bản tin", "D": "(D) Tải về một phiếu giảm giá"}
    },
    76: {
        "qVi": "Điều gì được bao gồm nếu trả thêm một khoản phụ phí?",
        "optVi": {"A": "(A) Giao hàng hỏa tốc", "B": "(B) Một album ảnh lưu niệm", "C": "(C) Khung viền tùy chỉnh riêng", "D": "(D) Một gói bảo hành hư hại"}
    },
    77: {
        "qVi": "Người nghe là những ai?",
        "optVi": {"A": "(A) Các bệnh nhân tại trung tâm", "B": "(B) Đội ngũ nhân viên chăm sóc y tế", "C": "(C) Các sinh viên thực tập", "D": "(D) Các tình nguyện viên cộng đồng"}
    },
    78: {
        "qVi": "Người nói đã chuẩn bị cái gì?",
        "optVi": {"A": "(A) Các hoạt động tương tác thực hành", "B": "(B) Một bài kiểm tra viết", "C": "(C) Một chuyến tham quan cơ sở", "D": "(D) Một bữa tiệc trưa chiêu đãi"}
    },
    79: {
        "qVi": "Người nói ngụ ý điều gì khi nói: 'I must leave at noon'?",
        "optVi": {"A": "(A) Buổi tập huấn sẽ bắt đầu muộn hơn", "B": "(B) Người nghe nên tự luyện tập thêm", "C": "(C) Một người thuyết trình khác sẽ tiếp quản", "D": "(D) Một số tài liệu/nội dung sẽ không được đề cập hết hôm nay"}
    },
    80: {
        "qVi": "Mục đích của bài quảng cáo là gì?",
        "optVi": {"A": "(A) Để bán xe tải đã qua sử dụng", "B": "(B) Để quảng bá một tuyến đường vận chuyển mới", "C": "(C) Để thông báo về việc mở chi nhánh mới", "D": "(D) Để tuyển dụng thêm nhân viên"}
    },
    81: {
        "qVi": "Công ty của người nói khác biệt gì so với các đối thủ cạnh tranh?",
        "optVi": {"A": "(A) Mức lương khởi điểm cao hơn", "B": "(B) Xe tải tiết kiệm nhiên liệu hơn", "C": "(C) Cung cấp lịch trình làm việc linh hoạt", "D": "(D) Nhiều ngày nghỉ phép có lương hơn"}
    },
    82: {
        "qVi": "Người nói khuyến khích người nghe làm điều gì?",
        "optVi": {"A": "(A) Đăng ký một lớp học lái xe", "B": "(B) Nộp đơn xin cấp giấy phép", "C": "(C) Gọi điện cho tổng đài chăm sóc", "D": "(D) Nhận thêm thông tin chi tiết qua trang web"}
    },
    83: {
        "qVi": "Tin nhắn chủ yếu nói về nội dung gì?",
        "optVi": {"A": "(A) Một sự thay đổi trong thực đơn nhà hàng", "B": "(B) Việc quay hình cho một chương trình truyền hình", "C": "(C) Một cuộc thanh tra an toàn vệ sinh", "D": "(D) Một sự kiện khai trương chi nhánh"}
    },
    84: {
        "qVi": "Người nói yêu cầu người nghe làm gì vào thứ Tư?",
        "optVi": {"A": "(A) Đến nơi làm việc sớm hơn", "B": "(B) Mặc đồng phục đặc biệt", "C": "(C) Chuẩn bị một món ăn mới", "D": "(D) Đón tiếp các vị khách đặc biệt"}
    },
    85: {
        "qVi": "Người nói sẽ đi đâu vào tuần tới?",
        "optVi": {"A": "(A) Đến một lễ hội ẩm thực", "B": "(B) Đi nghỉ mát cùng gia đình", "C": "(C) Đến một hội nghị nhà hàng", "D": "(D) Đi thăm một nông trại địa phương"}
    },
    86: {
        "qVi": "Người nói chủ yếu đang thảo luận về điều gì?",
        "optVi": {"A": "(A) Một trung tâm mua sắm", "B": "(B) Một nhà máy sản xuất", "C": "(C) Một công viên công cộng", "D": "(D) Một dự án đường cao tốc"}
    },
    87: {
        "qVi": "Người nói ngụ ý điều gì khi nói: 'No one made any comments'?",
        "optVi": {"A": "(A) Cuộc họp kết thúc sớm hơn dự kiến", "B": "(B) Công chúng chưa được thông báo đầy đủ", "C": "(C) Dự án nhận được sự đồng thuận, ủng hộ của cộng đồng", "D": "(D) Cần tổ chức một phiên điều trần khác"}
    },
    88: {
        "qVi": "Công chúng có thể xem cái gì tại tòa nhà thị chính thành phố?",
        "optVi": {"A": "(A) Một bộ phim tài liệu", "B": "(B) Một số hình ảnh/bản vẽ phối cảnh", "C": "(C) Một mẫu sản phẩm thực tế", "D": "(D) Một danh sách việc làm"}
    },
    89: {
        "qVi": "Loại sản phẩm nào đang được quảng cáo?",
        "optVi": {"A": "(A) Một chiếc ghế văn phòng công thái học", "B": "(B) Một phần mềm quản lý công việc", "C": "(C) Một bộ đèn bàn làm việc", "D": "(D) Một khay sắp xếp đồ đạc bàn làm việc"}
    },
    90: {
        "qVi": "Người nói nhấn mạnh tính năng đặc biệt nào của sản phẩm?",
        "optVi": {"A": "(A) Nó được làm từ vật liệu tái chế", "B": "(B) Nó có thể điều chỉnh kích thước linh hoạt", "C": "(C) Nó có nhiều màu sắc khác nhau", "D": "(D) Nó có tính năng khóa an toàn"}
    },
    91: {
        "qVi": "Làm thế nào để người nghe nhận được giảm giá?",
        "optVi": {"A": "(A) Bằng cách gọi điện trong khoảng thời gian quy định", "B": "(B) Bằng cách nhập một mã giảm giá trực tuyến", "C": "(C) Bằng cách mua combo hai sản phẩm", "D": "(D) Bằng cách đăng ký làm thành viên mới"}
    },
    92: {
        "qVi": "Theo người nói, mục đích của podcast này là gì?",
        "optVi": {"A": "(A) Để phỏng vấn các đầu bếp nổi tiếng", "B": "(B) Để đánh giá các nhà hàng địa phương", "C": "(C) Để chia sẻ mẹo làm bánh", "D": "(D) Để giới thiệu từng loại nguyên liệu riêng biệt"}
    },
    93: {
        "qVi": "Tại sao người nói lại nói: 'this product line will not be available for long'?",
        "optVi": {"A": "(A) Để thúc giục người nghe nhanh chóng đặt hàng", "B": "(B) Để giải thích sự chậm trễ trong giao hàng", "C": "(C) Để thông báo về việc ngừng sản xuất", "D": "(D) Để xin lỗi vì hết hàng"}
    },
    94: {
        "qVi": "Theo người nói, Rebecca Murray gần đây đã làm điều gì?",
        "optVi": {"A": "(A) Xuất bản một cuốn sách nấu ăn", "B": "(B) Giành một giải thưởng ẩm thực", "C": "(C) Khai trương một nhà hàng mới", "D": "(D) Xuất hiện trên một chương trình truyền hình"}
    },
    95: {
        "qVi": "Tại sao người nói lại đưa ra lời xin lỗi?",
        "optVi": {"A": "(A) Có tiếng ồn thi công công trường tại nhà ga", "B": "(B) Một chuyến tàu bị hoãn giờ khởi hành", "C": "(C) Giá vé tàu vừa mới tăng", "D": "(D) Một quầy bán vé tạm thời đóng cửa"}
    },
    96: {
        "qVi": "Theo người nói, tại sao một số hành khách có thể cần gặp nhân viên nhà ga?",
        "optVi": {"A": "(A) Để đổi lại vé tàu", "B": "(B) Để yêu cầu dịch vụ hỗ trợ hành lý", "C": "(C) Để hỏi thông tin về lịch trình", "D": "(D) Để tìm lại hành lý thất lạc"}
    },
    97: {
        "qVi": "Nhìn vào hình ảnh. Chuyến tàu 133 dự kiến sẽ đến điểm dừng tiếp theo lúc mấy giờ?",
        "optVi": {"A": "(A) Lúc 11:45 sáng", "B": "(B) Lúc 12:05 trưa", "C": "(C) Lúc 12:20 trưa", "D": "(D) Lúc 12:40 chiều"}
    },
    98: {
        "qVi": "Những người nghe rất có thể là ai?",
        "optVi": {"A": "(A) Các hành khách đi máy bay", "B": "(B) Các nhân viên hàng không", "C": "(C) Các phóng viên báo chí, nhà báo", "D": "(D) Các nhà thầu xây dựng"}
    },
    99: {
        "qVi": "Nhìn vào hình ảnh. Công ty nào sau đây sẽ bị ảnh hưởng bởi việc chậm tiến độ?",
        "optVi": {"A": "(A) Selca Air", "B": "(B) Apex Aviation", "C": "(C) Crestline Airlines", "D": "(D) Horizon Jet"}
    },
    100: {
        "qVi": "Người nói mời những người nghe làm điều gì?",
        "optVi": {"A": "(A) Tham gia một chuyến tham quan thực địa", "B": "(B) Xem một mô hình thu nhỏ 3D", "C": "(C) Dùng đồ ăn nhẹ giải khát", "D": "(D) Đặt các câu hỏi phỏng vấn"}
    }
}

with open('scratch/t2_p3_p4_bilingual.json', 'w', encoding='utf-8') as f:
    json.dump({
        "dialogues_vi": {f"{s}_{e}": vi for (s, e), vi in p3_dialogues_vi.items()},
        "talks_vi": {f"{s}_{e}": vi for (s, e), vi in p4_talks_vi.items()},
        "questions_vi": {str(k): v for k, v in p3_p4_questions_vi.items()}
    }, f, ensure_ascii=False, indent=2)

print("Saved Test 2 Part 3 & Part 4 bilingual data successfully!")
