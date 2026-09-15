# scratch/t2_bilingual_part5_6_7.py: Translations for Test 2 Part 6 and Part 7
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Part 6 Passages Vietnamese Translation
p6_passages_vi = {
    (131, 134): (
        "Kính gửi Quý khách hàng,\n"
        "Cảm ơn bạn đã lựa chọn xưởng mộc của chúng tôi. Chúng tôi viết thư này để thông báo rằng đơn đặt hàng [131] đặc biệt của bạn cho bộ bàn ghế ăn bằng gỗ sồi đã hoàn thành và sẵn sàng để giao. "
        "Chúng tôi sẽ điều phối đội ngũ vận chuyển để thực hiện việc giao [132] đồ nội thất tới địa chỉ nhà bạn vào thứ Ba tuần tới. "
        "Nếu bạn có bất kỳ yêu cầu cụ thể nào về thời gian hoặc cách thức lắp đặt, vui lòng [133] yêu cầu nói chuyện trực tiếp với người quản lý giao hàng của chúng tôi. "
        "[134] Anh ấy có thể sắp xếp một khung giờ thuận tiện nhất cho lịch trình của bạn.\n"
        "Trân trọng,\nĐội ngũ dịch vụ khách hàng"
    ),
    (135, 138): (
        "Dịch vụ bảo dưỡng hệ thống điều hòa & sưởi Apex Comfort:\n"
        "Mùa đông đang đến gần, việc đảm bảo hệ thống sưởi ấm của gia đình bạn hoạt động ổn định là điều tối quan trọng đối với sự [135] an toàn và tiện nghi của mọi thành viên. "
        "Các kỹ thuật viên được cấp chứng chỉ của chúng tôi sẽ tiến hành kiểm tra toàn diện 20 hạng mục kỹ thuật để tối ưu hóa hiệu suất thiết bị. "
        "[136] Hơn nữa, việc bảo dưỡng định kỳ giúp tiết kiệm đáng kể chi phí điện năng hàng tháng. "
        "[137] Thêm vào đó, đội ngũ kỹ thuật viên của chúng tôi luôn thân thiện, làm việc sạch sẽ và có kiến thức chuyên môn vững vàng. "
        "Mọi công việc sửa chữa và linh kiện thay thế đều được [138] bảo đảm bằng cam kết bảo hành hoàn tiền trong 12 tháng.\n"
        "Hãy liên hệ đặt lịch hẹn ngay hôm nay!"
    ),
    (139, 142): (
        "Thông báo gửi toàn thể khách hàng thân thiết,\n"
        "Do chi phí nguyên vật liệu đầu vào và giá vận tải quốc tế tăng cao, chúng tôi xin thông báo biểu phí dịch vụ in ấn của chúng tôi sẽ có sự điều chỉnh. "
        "Mức giá mới sẽ [139] thay đổi tùy thuộc vào số lượng trang in và chất liệu giấy mà quý khách lựa chọn. "
        "Xin lưu ý rằng tất cả các đơn hàng [140] được tiếp nhận trước ngày 15 tháng 3 vẫn sẽ được áp dụng theo bảng giá cũ. "
        "[141] Bảng báo giá chi tiết cập nhật sẽ được công bố chính thức trên trang web vào ngày 20 tháng 3. "
        "Chúng tôi cam kết tiếp tục mang lại chất lượng sản phẩm [142] vượt trội và dịch vụ tận tâm nhất tới quý vị."
    ),
    (143, 146): (
        "Kính gửi cô Tanaka,\n"
        "Tôi vô cùng ấn tượng trước sự tinh xảo trong các tác phẩm trang sức gốm thủ công của cô tại triển lãm tuần trước. "
        "Chuỗi cửa hàng lưu niệm cao cấp của chúng tôi đang tìm kiếm các dòng sản phẩm độc đáo nhằm tiếp cận lượng [143] khách hàng sành điệu tại các thành phố lớn. "
        "[144] Mức giá cả hết sức hợp lý cũng khiến các tác phẩm của cô trở thành sự lựa chọn tuyệt vời có giá trị cao. "
        "Nếu cô đồng ý hợp tác, chúng tôi dự định sẽ [145] tăng gấp đôi số lượng đơn hàng nhập vào dịp lễ cuối năm. "
        "Tôi tin tưởng rằng một thỏa thuận phân phối độc quyền sẽ mang lại lợi ích to lớn cho cả hai bên [146] chúng ta.\n"
        "Rất mong sớm nhận được phản hồi từ cô,\nKenneth Okon"
    )
}

# Part 7 Passages Vietnamese Translation & Titles
p7_passages_vi = {
    (147, 148): {
        "title": "Thư mời hội thảo trực tuyến: Tiếp thị truyền thông xã hội (Savan Business Center)",
        "textVi": (
            "Trung tâm Kinh doanh Savan trân trọng kính mời quý doanh nghiệp tham gia hội thảo trực tuyến: 'Tập trung Tiếp thị Truyền thông Xã hội'.\n"
            "Trong hơn 12 năm qua, Trung tâm Kinh doanh Savan đã đồng hành và hỗ trợ hàng nghìn doanh nhân khởi nghiệp và các chủ doanh nghiệp nhỏ trên khắp khu vực đô thị.\n"
            "Hội thảo trực tuyến tương tác lần này sẽ mang đến những hướng dẫn thực chiến sâu sắc về cách xây dựng các bài viết thu hút, video ngắn quảng bá và nội dung quảng cáo số tiếp cận khách hàng mục tiêu hiệu quả.\n"
            "Thời gian: Thứ Tư, ngày 14 tháng 5, từ 10:00 sáng đến 11:30 sáng.\n"
            "Đăng ký miễn phí tại: https://www.savanbusinesscenter.com/socialmedia"
        )
    },
    (149, 150): {
        "title": "Thông báo: Lễ hội Ẩm thực Dine Out Darville trở lại!",
        "textVi": (
            "Dine Out Darville đã trở lại!\n"
            "Dine Out Darville, ngày hội ẩm thực kéo dài 7 ngày hàng đầu của thành phố chúng ta, sẽ chính thức khởi động từ thứ Hai, ngày 12 tháng 10 đến hết Chủ Nhật, ngày 18 tháng 10.\n"
            "Hơn 40 nhà hàng và quán ăn xuất sắc nhất trên toàn thành phố sẽ tham gia phục vụ thực đơn 3 món đặc biệt với mức giá ưu đãi cố định ($25 cho bữa trưa và $40 cho bữa tối).\n"
            "Mỗi suất ăn bao gồm một món khai vị, một món chính và một món tráng miệng tùy chọn theo sở thích của thực khách.\n"
            "Lưu ý quan trọng: Các loại đồ uống có cồn/giải khát và tiền boa phục vụ không bao gồm trong giá vé và sẽ được tính phí riêng.\n"
            "Xem danh sách đầy đủ các nhà hàng tham gia tại www.darvillechamber.org/dineout."
        )
    },
    (151, 152): {
        "title": "Bài báo: Rainsy LLC mở rộng cơ sở mới tại Dade",
        "textVi": (
            "Rainsy LLC, công ty hàng đầu trong lĩnh vực lưu trữ dữ liệu người tiêu dùng và phân tích hành vi khách hàng, vừa chính thức công bố kế hoạch mở rộng quy mô.\n"
            "Khu phức hợp văn phòng công nghệ mới tại thành phố Dade sẽ trở thành trung tâm vận hành chiến lược thứ hai của tập đoàn.\n"
            "Theo kế hoạch tái bố trí nhân sự, khoảng 50% trong tổng số 400 nhân viên của công ty sẽ chuyển về làm việc tại trụ sở Dade mới bắt đầu từ quý tới.\n"
            "Văn phòng mới tọa lạc tại số 12 Glacier Parkway, được trang bị hạ tầng máy chủ điện toán đám mây tối tân nhất hiện nay."
        )
    },
    (153, 154): {
        "title": "Chuỗi tin nhắn: Michael Liu và Jana Bhat (Mua vật tư in ấn)",
        "textVi": (
            "Michael Liu (9:43 sáng): Chào Jana. Tôi đang ở cửa hàng Biz Plus. Có phải cô cần loại giấy bìa màu xanh da trời nhạt pastel để in tờ rơi quảng cáo không?\n"
            "Jana Bhat (9:45 sáng): Đúng rồi, chính xác là tông màu xanh da trời dịu nhẹ đó nhé. Giá ở đó thế nào?\n"
            "Michael Liu (9:47 sáng): Họ đang bán với giá $28 một ram giấy ở đây, đắt gần gấp đôi so với giá chúng ta thường đặt mua trực tuyến.\n"
            "Jana Bhat (9:49 sáng): Thôi, bỏ qua đi. Để tôi đặt đơn giao gấp trên trang web quen thuộc của chúng ta, vừa rẻ vừa được giao tận văn phòng."
        )
    },
    (155, 157): {
        "title": "Bức thư: Hồi đáp đề xuất tổ chức hội thảo tài chính tại Thư viện Queensland",
        "textVi": (
            "Ngày 20 tháng 5\n"
            "Kính gửi ông Neil Croft, Giám đốc Hệ thống Thư viện Queensland,\n"
            "Cảm ơn bức thư đề ngày 10 tháng 5 của ông đã hỏi thăm về khả năng hợp tác tổ chức các buổi đào tạo kiến thức tài chính cộng đồng.\n"
            "Hiệp hội Cố vấn Quản lý Tài chính chúng tôi rất vinh dự được đồng hành cùng các thư viện công cộng để mang lại giá trị thiết thực cho người dân. [1] "
            "Ông có đề cập đến việc điều chỉnh nội dung bài giảng để tập trung vào quản lý chi tiêu và lập kế hoạch hưu trí cho người cao tuổi. [2] Đây là điều mà tôi rất sẵn lòng thu xếp thực hiện. "
            "Để chuẩn bị chu đáo, ông có thể vui lòng gửi cho tôi danh sách địa chỉ cụ thể và sức chứa chỗ ngồi của các chi nhánh thư viện dự kiến tổ chức không? [3] "
            "Chúng tôi sẽ lên lịch trình giảng viên tương ứng cho từng cơ sở. [4]\n"
            "Trân trọng,\nEleanor Otney, Chủ tịch Hiệp hội Cố vấn Quản lý Tài chính"
        )
    },
    (158, 160): {
        "title": "Quảng cáo: Chương trình khuyến mãi gọng kính mùa xuân tại Claro Vision",
        "textVi": (
            "Claro Vision - Sự khác biệt rõ ràng!\n"
            "Hãy chăm sóc đôi mắt của bạn nhân dịp Chương trình Khuyến mãi Gọng kính Mùa xuân Thường niên của chúng tôi!\n"
            "Giảm giá ngay 30% cho tất cả các mẫu gọng kính thiết kế cao cấp trong suốt sự kiện ưu đãi kéo dài hai tuần kết thúc vào ngày 30 tháng 4.\n"
            "Mỗi đơn mua hàng đều được tặng kèm dịch vụ nắn chỉnh gọng và lắp ráp theo kích cỡ khuôn mặt hoàn toàn miễn phí tại tất cả các cửa hàng.\n"
            "Ngoài ra, các buổi khám và kiểm tra thị lực toàn diện được thực hiện trực tiếp bởi đội ngũ bác sĩ nhãn khoa có chứng chỉ hành nghề của chúng tôi với máy móc chẩn đoán tối tân.\n"
            "Tìm cửa hàng gần bạn nhất tại www.clarovision.ca/locations."
        )
    },
    (161, 163): {
        "title": "Bức thư: Thông báo chi tiết hợp đồng thuê căn hộ tại Tòa nhà Rossery",
        "textVi": (
            "Tập đoàn Xây dựng Rossery - 2710 South Exmouth Drive\n"
            "Kính gửi cô Balakrishnan,\n"
            "Chúng tôi rất vui mừng được cung cấp cho cô các chi tiết và điều khoản trong hợp đồng thuê căn hộ ở Căn hộ số 4B tại Tòa nhà Rossery.\n"
            "Hợp đồng thuê có thời hạn 12 tháng, bắt đầu từ ngày 1 tháng 7.\n"
            "Tiền thuê nhà hàng tháng đã bao gồm chi phí nước sinh hoạt và hệ thống sưởi ấm. Tuy nhiên, đối với những cư dân có nhu cầu sử dụng chỗ đỗ xe ô tô riêng biệt tại tầng hầm, mức phí đỗ xe bổ sung là $75 mỗi tháng sẽ được ghi vào hóa đơn thanh toán hàng tháng.\n"
            "Vui lòng ký vào bản sao hợp đồng đính kèm và gửi lại cho văn phòng quản lý trước ngày 15 tháng 6.\n"
            "Trân trọng,\nAndrea Tan, Quản lý Bất động sản tại chỗ, Tập đoàn Xây dựng Rossery"
        )
    },
    (164, 167): {
        "title": "Email: Đàm phán hợp đồng cung ứng kính ô tô với Qualiview Ltd.",
        "textVi": (
            "Gửi tới: Quản lý Kinh doanh, Qualiview Ltd.\n"
            "Người gửi: Kenneth Hagel, Giám đốc Thu mua, Britel Auto Assembly\n"
            "Ngày: 18 tháng 3 | Tiêu đề: Đàm phán dự thảo hợp đồng nhà cung ứng\n"
            "Kính gửi Quý công ty,\n"
            "Tôi viết email này để thảo luận một số điểm sửa đổi nhỏ đối với các điều khoản nêu trong dự thảo hợp đồng cung ứng linh kiện trước khi bộ phận pháp lý của chúng tôi phê duyệt chính thức.\n"
            "Nhà máy lắp ráp ô tô của chúng tôi đánh giá rất cao chất lượng kính chắn gió chịu lực và kính cửa sổ ô tô mà Qualiview sản xuất. "
            "Tuy nhiên, chúng tôi muốn giải quyết (address) các điểm khác biệt về tiến độ giao hàng và điều kiện bảo hành trong một cuộc gọi trao đổi trực tiếp.\n"
            "Tôi hoàn toàn rảnh vào sáng thứ Tư tuần tới trước 12:00 trưa để họp trực tuyến qua video. Xin vui lòng báo cho tôi khung giờ thuận tiện nhất đối với quý vị.\n"
            "Trân trọng,\nKenneth Hagel"
        )
    },
    (168, 171): {
        "title": "Bài báo: Tình trạng khan hiếm container vận tải biển ảnh hưởng tới các nhà sản xuất",
        "textVi": (
            "Các hãng vận tải hàng hải quốc tế đang đối mặt với tình trạng thiếu hụt trầm trọng thùng công-ten-nơ vận chuyển đường biển, gây ra sự chậm trễ giao hàng trên diện rộng.\n"
            "Chuyên gia phân tích chuỗi cung ứng, ông David Lam, nhấn mạnh rằng giải pháp cấp bách nhất hiện nay là tăng cường giao tiếp và điều phối minh bạch giữa các bên bị ảnh hưởng, bao gồm chính quyền cảng, hãng tàu và các công ty sản xuất.\n"
            "Tình trạng này đã tác động trực tiếp đến các đơn hàng xuất khẩu đi châu Âu của Fezker, một nhà sản xuất hàng đầu về trang phục thể thao và đồ chạy bộ. [1] [2] [3] "
            "Tuy nhiên, doanh số tại các thị trường nội địa lân cận vẫn tăng trưởng rất khả quan. [4] Các thị trường nội địa này được tiếp tế thuận lợi hơn nhờ phương thức vận tải đường sắt và xe tải đường bộ vốn sẵn có hơn nhiều.\n"
            "'Chúng tôi đang tích cực đàm phán để hạn chế tối đa tác động lên lợi nhuận quý này,' CEO Fezker, bà Nuwa Lee chia sẻ."
        )
    },
    (172, 175): {
        "title": "Thảo luận trực tuyến: Cập nhật tiến độ thi công dự án Riverview",
        "textVi": (
            "Gary Wendel (7:40 sáng): Chào buổi sáng Robbie. Cậu có thể cập nhật cho tôi về tiến độ công trường dự án Riverview không?\n"
            "Robbie Zuniga (7:43 sáng): Chào anh Gary. Đội thợ đã hoàn thành việc đổ móng bê tông cho tòa tháp phía Tây vào chiều hôm qua.\n"
            "Gary Wendel (7:46 sáng): Tiến độ tổng thể đang như thế nào so với mốc thời gian bàn giao?\n"
            "Robbie Zuniga (7:50 sáng): Thật không may là do các đợt mưa lớn kéo dài tuần trước và sự cố chậm giao bê tông trước đó, dự án của chúng ta đã bị chậm tiến độ tới lần thứ ba rồi.\n"
            "Gary Wendel (7:54 sáng): Chúng ta cần đẩy nhanh tiến độ hoàn thiện khung thép. Cậu hãy tham dự cuộc họp giao ban lúc 10:00 sáng với tổng thầu và báo cho tôi biết kết quả quyết định của họ về việc tăng cường thêm nhân công nhé.\n"
            "Robbie Zuniga (7:58 sáng): Tôi sẽ làm vậy (Will do)."
        )
    },
    (176, 180): {
        "title": "Email & Phiếu khảo sát: Kiểm nghiệm hương vị kem mới của Karabel Industries",
        "textVi": (
            "[VĂN BẢN 1: Email nội bộ]\n"
            "Từ: Madalyn Kerluke, Trưởng bộ phận R&D | Tới: Nhóm phát triển sản phẩm\n"
            "Ngày: 12 tháng 8 | Tiêu đề: Kết quả thử nghiệm hương vị kem đợt 1\n"
            "Chào cả nhóm, chúng ta đã nhận được bảng tổng hợp đánh giá cảm quan từ phòng thí nghiệm Fatior Labs.\n"
            "Tin tốt là các nhà hóa học thực phẩm của chúng ta đã xác nhận công thức chất tạo màu tự nhiên chiết xuất từ rau củ quả có thể dễ dàng điều chỉnh màu sắc của kem mà không hề làm ảnh hưởng đến hương vị gốc.\n"
            "Tôi muốn triệu tập một cuộc họp toàn thể nhóm vào thứ Sáu tuần này lúc 10:00 sáng để rà soát công thức.\n"
            "Sau khi hoàn thiện tinh chỉnh, chúng ta sẽ thuê Fatior Labs tiến hành thêm một đợt thử vị người tiêu dùng nữa.\n\n"
            "[VĂN BẢN 2: Phiếu khảo sát cảm quan]\n"
            "Mã người tham gia: #54 | Nhóm tuổi: [x] 25–40 tuổi\n"
            "Đánh giá hương vị Peanut Brittle (Đậu phộng giòn): 2/5 sao.\n"
            "Nhận xét của người tham gia: 'Các mẩu đậu phộng bên trong hơi quá cứng và giòn; nếu cho thêm các vệt sốt sô-cô-la fudge hoặc các mẩu bánh brownie mềm thì món kem này chắc chắn sẽ là một cú hích lớn!'"
        )
    },
    (181, 185): {
        "title": "Trang tuyển dụng & Thư xin việc: Vị trí thiết kế đồ họa tại CreateGreat",
        "textVi": (
            "[VĂN BẢN 1: Trang web tuyển dụng CreateGreat]\n"
            "Vị trí tuyển dụng: Chuyên viên Thiết kế Đồ họa Cao cấp (Toàn thời gian).\n"
            "Công việc này cho phép làm việc từ xa hoàn toàn 100% (telecommuting) từ bất kỳ nơi nào tại Canada.\n"
            "Ứng viên cần có kinh nghiệm quản lý quy trình sản xuất ấn phẩm và sở hữu hồ sơ năng lực (portfolio) phù hợp (suits) với thẩm mỹ thương hiệu của chúng tôi.\n"
            "Hạn chót nộp hồ sơ: Ngày 15 tháng 4.\n\n"
            "[VĂN BẢN 2: Thư xin việc của Annie Smith]\n"
            "Ngày 18 tháng 4\n"
            "Kính gửi Ban Tuyển dụng CreateGreat,\n"
            "Tôi xin nộp đơn ứng tuyển vào vị trí Chuyên viên Thiết kế Đồ họa của quý công ty.\n"
            "Trong vai trò hiện tại tại tạp chí MODA, tôi trực tiếp quản lý quy trình sản xuất từ đầu đến cuối cho các ấn phẩm kỹ thuật số và tạp chí thời trang in ấn định kỳ.\n"
            "Ngoài ra, tôi cũng thường xuyên đóng góp thiết kế đồ họa thị giác cho Medesheen, một trang blog thời trang và phong cách sống trực tuyến nổi tiếng.\n"
            "Hồ sơ năng lực và thư giới thiệu đính kèm xin gửi tới quý công ty xem xét.\n"
            "Trân trọng,\nAnnie Smith"
        )
    },
    (186, 190): {
        "title": "Email trao đổi & Biên lai: Đơn hàng văn phòng phẩm tại Fowler Office Supplies",
        "textVi": (
            "[VĂN BẢN 1: Email của Akira Nakashima]\n"
            "Kính gửi Fowler Office Supplies, tôi vừa nhận được email xác nhận đơn hàng số B19849. Tuy nhiên, hóa đơn tự động gửi cho tôi chỉ hiển thị tổng số tiền mà không liệt kê chi tiết giá của từng mặt hàng, điều mà phòng kế toán của chúng tôi bắt buộc phải có để hoàn ứng công tác phí.\n\n"
            "[VĂN BẢN 2: Email hồi đáp của Martin Higgins]\n"
            "Chào ông Nakashima, tôi xin gửi lại bản hóa đơn chi tiết từng khoản mục đính kèm. Để tạ lỗi vì sự bất tiện này, chúng tôi xin gửi tặng ông mã giảm giá 15% cho đơn hàng tiếp theo.\n"
            "Nhận thấy ông thường xuyên mua giấy in photocopy hàng tháng, tôi đề xuất ông nên chọn tính năng 'Đặt hàng định kỳ' (Recurring Order) cho giấy in để luôn có sẵn hàng khi cần.\n"
            "Tôi cũng đã chuyển đề xuất tới đội ngũ kỹ thuật trang web để nghiên cứu thêm tùy chọn gửi hóa đơn tự động tới nhiều địa chỉ email.\n\n"
            "[VĂN BẢN 3: Biên lai mua hàng B19849]\n"
            "Mặt hàng: Giấy in đa năng (Carton 5 ram) - $80.00; Mực in cartridge - $50.00; Kẹp giấy - $15.00.\n"
            "Chính sách: Khách hàng đổi trả hàng tại cửa hàng chỉ cần xuất trình mã số đơn hàng 9 chữ số."
        )
    },
    (191, 195): {
        "title": "Bài báo, Trang web & Biên lai: Khai trương chuỗi bách hóa Crawford and Duval",
        "textVi": (
            "[VĂN BẢN 1: Bản tin kinh tế]\n"
            "Thương hiệu bán lẻ cao cấp Crawford and Duval vừa tưng bừng khai trương hai cửa hàng bách hóa tổng hợp mới tại trung tâm thương mại thành phố, cung cấp các sản phẩm nội thất gia đình, đồ trang trí và thời trang đẳng cấp.\n\n"
            "[VĂN BẢN 2: Trang web dịch vụ khách hàng]\n"
            "Hãy biến đổi không gian sống của bạn! Quý khách có thể đặt lịch hẹn tư vấn phong cách miễn phí trong 60 phút cùng các nhà thiết kế nội thất chuyên nghiệp thuộc biên chế chính thức của chúng tôi.\n\n"
            "[VĂN BẢN 3: Biên lai mua hàng của Mei-Lin Fong]\n"
            "Ngày mua: 23 tháng 2 | Cửa hàng bách hóa Crawford and Duval\n"
            "Các mặt hàng: Đèn bàn bằng tre ($65.00), Đệm gối trang trí ($45.00), Chăn mỏng dệt len cashmere pha (Có thể giặt bằng máy) - $120.00.\n"
            "Khách hàng thân thiết: Mã hội viên Câu lạc bộ Mua sắm Thường xuyên #49281. Điểm tích lũy hôm nay: 120 điểm."
        )
    },
    (196, 200): {
        "title": "Trang web & Đánh giá khách hàng: Dịch vụ Team Building của Osawa",
        "textVi": (
            "[VĂN BẢN 1: Trang giới thiệu gói sự kiện Osawa]\n"
            "Các gói hoạt động xây dựng đội ngũ (Team Building):\n"
            "- Trò chơi vượt chướng ngại vật: Thời lượng 2 tiếng, tối đa 80 người.\n"
            "- Cuộc truy tìm mật thư (Scavenger Hunt): Thời lượng 3 tiếng, mức độ vận động trung bình, tối đa 100 người.\n"
            "- Ngày hội trò chơi tập thể (Game Day): Thời lượng 4 tiếng, sức chứa từ 50 đến 500 người tham gia.\n\n"
            "[VĂN BẢN 2: Chính sách tri ân khách hàng]\n"
            "Khách hàng để lại bài đánh giá chân thực về sự kiện trên cổng thông tin sẽ nhận được mã giảm giá 10% cho lần đặt dịch vụ tiếp theo!\n\n"
            "[VĂN BẢN 3: Bài đánh giá của Karen Peterson (Công ty Whitten Tech)]\n"
            "Whitten Tech ban đầu dự định đặt gói Scavenger Hunt cho ngày thứ Sáu, nhưng vì gói đó đã kín chỗ nên chúng tôi chuyển sang City Quest.\n"
            "Các hướng dẫn viên của Osawa rất nhiệt tình và chu đáo. Tuy nhiên, điều đáng thất vọng duy nhất là sự thiếu hụt hoàn toàn thông tin cảnh báo trước về quãng đường đi bộ quá dài, khiến nhiều đồng nghiệp đi giày công sở bị đau chân."
        )
    }
}

with open('scratch/t2_p6_p7_bilingual.json', 'w', encoding='utf-8') as f:
    json.dump({
        "p6_passages_vi": {f"{s}_{e}": vi for (s, e), vi in p6_passages_vi.items()},
        "p7_passages_vi": {f"{s}_{e}": data for (s, e), data in p7_passages_vi.items()}
    }, f, ensure_ascii=False, indent=2)

print("Saved Test 2 Part 6 & Part 7 bilingual data successfully!")
