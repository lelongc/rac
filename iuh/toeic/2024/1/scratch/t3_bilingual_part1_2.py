# scratch/t3_bilingual_part1_2.py: Full translations for Test 3 Part 1 & Part 2
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

t3_p1_p2_vi = {
    # Part 1: Q1 - Q6
    1: {
        "questionTextVi": "Nhìn vào bức tranh số 1 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Họ đang bỏ rác vào trong một chiếc túi.",
            "B": "(B) Họ đang cởi áo khoác ngoài của mình ra.",
            "C": "(C) Họ đang đứng đối diện một chiếc kệ để đồ.",
            "D": "(D) Họ đang sơn một căn phòng."
        },
        "transcript": "(A) They’re putting trash in a bag.\n(B) They’re taking off their jackets.\n(C) They’re facing a shelving unit.\n(D) They’re painting a room.",
        "transcriptVi": "Người nói:\n(A) Họ đang bỏ rác vào trong một chiếc túi.\n(B) Họ đang cởi áo khoác ngoài của mình ra.\n(C) Họ đang đứng đối diện một chiếc kệ để đồ.\n(D) Họ đang sơn một căn phòng."
    },
    2: {
        "questionTextVi": "Nhìn vào bức tranh số 2 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Cô ấy đang lau chùi một chiếc lò nướng.",
            "B": "(B) Cô ấy đang di chuyển một chiếc nồi.",
            "C": "(C) Cô ấy đang mở một cánh cửa tủ.",
            "D": "(D) Cô ấy đang cầm một chiếc khăn lau."
        },
        "transcript": "(A) She’s cleaning an oven.\n(B) She’s moving a pot.\n(C) She’s opening a cabinet.\n(D) She’s holding a towel.",
        "transcriptVi": "Người nói:\n(A) Cô ấy đang lau chùi một chiếc lò nướng.\n(B) Cô ấy đang di chuyển một chiếc nồi.\n(C) Cô ấy đang mở một cánh cửa tủ.\n(D) Cô ấy đang cầm một chiếc khăn lau."
    },
    3: {
        "questionTextVi": "Nhìn vào bức tranh số 3 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Một chiếc thang đã được dựng dựa vào một cái cây.",
            "B": "(B) Có những đống cành cây bị vứt bỏ trong công viên.",
            "C": "(C) Những chiếc ghế băng bằng gỗ đã được sắp xếp thành một vòng tròn.",
            "D": "(D) Một cấu trúc bằng gỗ đã được xây dựng gần một số cây."
        },
        "transcript": "(A) A ladder has been leaned against a tree.\n(B) There are piles of tree branches discarded in a park.\n(C) Wooden benches have been arranged in a circle.\n(D) A wooden structure has been built near some trees.",
        "transcriptVi": "Người nói:\n(A) Một chiếc thang đã được dựng dựa vào một cái cây.\n(B) Có những đống cành cây bị vứt bỏ trong công viên.\n(C) Những chiếc ghế băng bằng gỗ đã được sắp xếp thành một vòng tròn.\n(D) Một cấu trúc bằng gỗ đã được xây dựng gần một số cây."
    },
    4: {
        "questionTextVi": "Nhìn vào bức tranh số 4 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Một trong những người đàn ông đang cởi mũ của mình ra.",
            "B": "(B) Một hàng dài khách hàng kéo dài ra tận bên ngoài cửa.",
            "C": "(C) Một số công nhân đang lắp đặt một tấm biển báo.",
            "D": "(D) Các nhạc công đã tụ tập lại thành một vòng tròn."
        },
        "transcript": "(A) One of the men is removing his hat.\n(B) A line of customers extends out a door.\n(C) Some workers are installing a sign.\n(D) Musicians have gathered in a circle.",
        "transcriptVi": "Người nói:\n(A) Một trong những người đàn ông đang cởi mũ của mình ra.\n(B) Một hàng dài khách hàng kéo dài ra tận bên ngoài cửa.\n(C) Một số công nhân đang lắp đặt một tấm biển báo.\n(D) Các nhạc công đã tụ tập lại thành một vòng tròn."
    },
    5: {
        "questionTextVi": "Nhìn vào bức tranh số 5 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Một lan can đang được tháo dỡ.",
            "B": "(B) Một mái nhà đang trong quá trình thi công xây dựng.",
            "C": "(C) Một số công nhân đang khiêng một chiếc thang.",
            "D": "(D) Một số công nhân đang cầm các tấm kim loại."
        },
        "transcript": "(A) A railing is being removed.\n(B) A roof is under construction.\n(C) Some workers are carrying a ladder.\n(D) Some workers are holding sheets of metal.",
        "transcriptVi": "Người nói:\n(A) Một lan can đang được tháo dỡ.\n(B) Một mái nhà đang trong quá trình thi công xây dựng.\n(C) Một số công nhân đang khiêng một chiếc thang.\n(D) Một số công nhân đang cầm các tấm kim loại."
    },
    6: {
        "questionTextVi": "Nhìn vào bức tranh số 6 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Một số dụng cụ đã bị để lại trên một chiếc ghế.",
            "B": "(B) Một số bộ dụng cụ đã được bày biện ra sẵn.",
            "C": "(C) Một tách cà phê đã bị đổ ra ngoài.",
            "D": "(D) Một chiếc chân bàn đang được sửa chữa."
        },
        "transcript": "(A) Some tools have been left on a chair.\n(B) Some tool sets have been laid out.\n(C) A cup of coffee has spilled.\n(D) A table leg is being repaired.",
        "transcriptVi": "Người nói:\n(A) Một số dụng cụ đã bị để lại trên một chiếc ghế.\n(B) Một số bộ dụng cụ đã được bày biện ra sẵn.\n(C) Một tách cà phê đã bị đổ ra ngoài.\n(D) Một chiếc chân bàn đang được sửa chữa."
    },

    # Part 2: Q7 - Q31
    7: {
        "questionTextVi": "Tại sao không có bột mì trên kệ hàng vậy?",
        "optionsVi": {
            "A": "(A) Bởi vì mặt hàng đó đã hết hàng rồi.",
            "B": "(B) Những bông hoa hồng đó có mùi thơm rất dễ chịu.",
            "C": "(C) Không, chiếc bánh kem kia cơ."
        },
        "transcript": "Speaker: Why is there no flour on the shelf?\n(A) Because it's out of stock.\n(B) Those roses smell nice.\n(C) No, the other cake.",
        "transcriptVi": "Người hỏi: Tại sao không có bột mì trên kệ hàng vậy?\n(A) Bởi vì mặt hàng đó đã hết hàng rồi.\n(B) Những bông hoa hồng đó có mùi thơm rất dễ chịu.\n(C) Không, chiếc bánh kem kia cơ."
    },
    8: {
        "questionTextVi": "Khi nào thì công ty cung cấp tiệc sẽ đến?",
        "optionsVi": {
            "A": "(A) Lúc bốn giờ đúng.",
            "B": "(B) Đó là một hương vị rất ngon.",
            "C": "(C) Nhiều món ăn chay phong phú."
        },
        "transcript": "Speaker: When will the catering company arrive?\n(A) At four o'clock.\n(B) That's a delicious flavor.\n(C) Many vegetarian options.",
        "transcriptVi": "Người hỏi: Khi nào thì công ty cung cấp tiệc sẽ đến?\n(A) Lúc bốn giờ đúng.\n(B) Đó là một hương vị rất ngon.\n(C) Nhiều món ăn chay phong phú."
    },
    9: {
        "questionTextVi": "Khi nào thì cuộc họp dự kiến bắt đầu?",
        "optionsVi": {
            "A": "(A) Tại một sự kiện giao lưu kết nối.",
            "B": "(B) Tôi bắt đầu làm công việc này sáu năm trước.",
            "C": "(C) Ngay sau bữa trưa."
        },
        "transcript": "Speaker: When's the meeting scheduled to start?\n(A) At a networking event.\n(B) I started this job six years ago.\n(C) Right after lunch.",
        "transcriptVi": "Người hỏi: Khi nào thì cuộc họp dự kiến bắt đầu?\n(A) Tại một sự kiện giao lưu kết nối.\n(B) Tôi bắt đầu làm công việc này sáu năm trước.\n(C) Ngay sau bữa trưa."
    },
    10: {
        "questionTextVi": "Chi phí sửa chữa sẽ hết bao nhiêu tiền?",
        "optionsVi": {
            "A": "(A) Tôi có hai đôi giày.",
            "B": "(B) Khoảng 200 đô la.",
            "C": "(C) Nhà hàng ở khu trung tâm thành phố."
        },
        "transcript": "Speaker: How much will the repairs cost?\n(A) I have two pairs of shoes.\n(B) Around 200 dollars.\n(C) The restaurant downtown.",
        "transcriptVi": "Người hỏi: Chi phí sửa chữa sẽ hết bao nhiêu tiền?\n(A) Tôi có hai đôi giày.\n(B) Khoảng 200 đô la.\n(C) Nhà hàng ở khu trung tâm thành phố."
    },
    11: {
        "questionTextVi": "Sáng nay bạn đã đi khám nha sĩ, đúng không?",
        "optionsVi": {
            "A": "(A) Ồ, tôi đã ăn sáng rồi.",
            "B": "(B) Đúng vậy, đi khám răng định kỳ hàng năm.",
            "C": "(C) Chúng ta hãy đi xe buýt nhé."
        },
        "transcript": "Speaker: You went to the dentist this morning, didn't you?\n(A) Oh, I've already had breakfast.\n(B) Yes, for an annual checkup.\n(C) Let's take the bus.",
        "transcriptVi": "Người hỏi: Sáng nay bạn đã đi khám nha sĩ, đúng không?\n(A) Ồ, tôi đã ăn sáng rồi.\n(B) Đúng vậy, đi khám răng định kỳ hàng năm.\n(C) Chúng ta hãy đi xe buýt nhé."
    },
    12: {
        "questionTextVi": "Chúng ta nên đặt chiếc máy in mới ở đâu nhỉ?",
        "optionsVi": {
            "A": "(A) Ở góc phòng cạnh cầu thang.",
            "B": "(B) Trang thứ ba của tập tài liệu.",
            "C": "(C) Một hộp mực in có thể tái sử dụng."
        },
        "transcript": "Speaker: Where should we put the new printer?\n(A) In the corner by the stairs.\n(B) The third page of the document.\n(C) A reusable ink cartridge.",
        "transcriptVi": "Người hỏi: Chúng ta nên đặt chiếc máy in mới ở đâu nhỉ?\n(A) Ở góc phòng cạnh cầu thang.\n(B) Trang thứ ba của tập tài liệu.\n(C) Hộp mực in có thể tái sử dụng."
    },
    13: {
        "questionTextVi": "Bạn trồng loại cây gì trong văn phòng làm việc vậy?",
        "optionsVi": {
            "A": "(A) Bất cứ khi nào tôi ngồi tại bàn làm việc.",
            "B": "(B) Cảm ơn bạn—tôi vừa mới mua nó đấy.",
            "C": "(C) Một loại cây không đòi hỏi phải tưới nhiều nước."
        },
        "transcript": "Speaker: What type of plant do you have in your office?\n(A) Whenever I sit at my desk.\n(B) Thanks—I just bought it.\n(C) One that doesn't require much water.",
        "transcriptVi": "Người hỏi: Bạn trồng loại cây gì trong văn phòng làm việc vậy?\n(A) Bất cứ khi nào tôi ngồi tại bàn làm việc.\n(B) Cảm ơn bạn—tôi vừa mới mua nó đấy.\n(C) Một loại cây không đòi hỏi phải tưới nhiều nước."
    },
    14: {
        "questionTextVi": "Vừa có một đợt giảm giá lớn tại cửa hàng đồ nội thất đấy.",
        "optionsVi": {
            "A": "(A) Đến trung tâm hội nghị triển lãm.",
            "B": "(B) Bạn có mua được món đồ gì không?",
            "C": "(C) Một nhân viên mới."
        },
        "transcript": "Speaker: There was a sale at the furniture store.\n(A) To the convention center.\n(B) Did you buy anything?\n(C) A new employee.",
        "transcriptVi": "Người nói: Vừa có một đợt giảm giá lớn tại cửa hàng đồ nội thất đấy.\n(A) Đến trung tâm hội nghị triển lãm.\n(B) Bạn có mua được món đồ gì không?\n(C) Một nhân viên mới."
    },
    15: {
        "questionTextVi": "Bạn có thể chỉ cho tôi cách gửi phiếu yêu cầu hỗ trợ kỹ thuật không?",
        "optionsVi": {
            "A": "(A) Để tôi gửi đường link trang web cho bạn nhé.",
            "B": "(B) Chiếc máy đang bị hỏng.",
            "C": "(C) Một chiếc vé trị giá hai mươi đô la."
        },
        "transcript": "Speaker: Can you show me how to submit a tech help ticket?\n(A) Let me send you the link.\n(B) The machine is broken.\n(C) A twenty-dollar ticket.",
        "transcriptVi": "Người hỏi: Bạn có thể chỉ cho tôi cách gửi phiếu yêu cầu hỗ trợ kỹ thuật không?\n(A) Để tôi gửi đường link trang web cho bạn nhé.\n(B) Chiếc máy đang bị hỏng.\n(C) Một chiếc vé trị giá hai mươi đô la."
    },
    16: {
        "questionTextVi": "Nút bật nguồn trên thiết bị này nằm ở đâu vậy?",
        "optionsVi": {
            "A": "(A) Tôi chưa từng sử dụng mẫu máy đó trước đây.",
            "B": "(B) Mười euro mỗi giờ.",
            "C": "(C) Đúng vậy, xoay nó sang bên phải."
        },
        "transcript": "Speaker: Where is the power button on this device?\n(A) I've never used that model before.\n(B) Ten euros per hour.\n(C) Yes, turn it to the right.",
        "transcriptVi": "Người hỏi: Nút bật nguồn trên thiết bị này nằm ở đâu vậy?\n(A) Tôi chưa từng sử dụng mẫu máy đó trước đây.\n(B) Mười euro mỗi giờ.\n(C) Đúng vậy, xoay nó sang bên phải."
    },
    17: {
        "questionTextVi": "Bạn muốn đi dạo ngay bây giờ luôn, hay để lát nữa thì tốt hơn?",
        "optionsVi": {
            "A": "(A) Một hồ nước ở gần đây.",
            "B": "(B) Bây giờ tôi đang rảnh để đi dạo đây.",
            "C": "(C) Cô ấy đã đi bộ tới đó vào hôm qua."
        },
        "transcript": "Speaker: Do you want to take a walk now, or would later be better?\n(A) A nearby lake.\n(B) I'm free to walk now.\n(C) She walked there yesterday.",
        "transcriptVi": "Người hỏi: Bạn muốn đi dạo ngay bây giờ luôn, hay để lát nữa thì tốt hơn?\n(A) Một hồ nước ở gần đây.\n(B) Bây giờ tôi đang rảnh để đi dạo đây.\n(C) Cô ấy đã đi bộ tới đó vào hôm qua."
    },
    18: {
        "questionTextVi": "Tôi vừa đặt mua một số thiết bị mới cho nhà xưởng.",
        "optionsVi": {
            "A": "(A) Chương trình thời sự trên Kênh Mười.",
            "B": "(B) Tuyệt quá—tôi rất nóng lòng muốn được sử dụng chúng.",
            "C": "(C) Đại lý bán xe hơi."
        },
        "transcript": "Speaker: I ordered some new equipment for the factory.\n(A) The news program on Channel Ten.\n(B) Great—I can't wait to use it.\n(C) The car dealership.",
        "transcriptVi": "Người nói: Tôi vừa đặt mua một số thiết bị mới cho nhà xưởng.\n(A) Chương trình thời sự trên Kênh Mười.\n(B) Tuyệt quá—tôi rất nóng lòng muốn được sử dụng chúng.\n(C) Đại lý bán xe hơi."
    },
    19: {
        "questionTextVi": "Có một căn nhà cho thuê rất đẹp trên đường Mercer.",
        "optionsVi": {
            "A": "(A) Nó có bao nhiêu phòng ngủ vậy?",
            "B": "(B) Tiền thuê nhà phải thanh toán vào ngày mùng 1.",
            "C": "(C) Vâng, anh ấy rất tốt tính."
        },
        "transcript": "Speaker: There's a nice place to rent on Mercer Street.\n(A) How many bedrooms does it have?\n(B) The rent is due on the first.\n(C) Yes, he's very nice.",
        "transcriptVi": "Người nói: Có một căn nhà cho thuê rất đẹp trên đường Mercer.\n(A) Nó có bao nhiêu phòng ngủ vậy?\n(B) Tiền thuê nhà phải thanh toán vào ngày mùng 1.\n(C) Vâng, anh ấy rất tốt tính."
    },
    20: {
        "questionTextVi": "Hệ thống sưởi ấm có đang hoạt động tốt không?",
        "optionsVi": {
            "A": "(A) Vâng, đó là trang web của tôi.",
            "B": "(B) Một cuộc chạy bộ năm ki-lô-mét.",
            "C": "(C) Có, văn phòng hiện đang rất ấm áp."
        },
        "transcript": "Speaker: Is the heating system working?\n(A) Yes, that's my Web site.\n(B) A five-kilometer run.\n(C) Yes, the office is warm.",
        "transcriptVi": "Người hỏi: Hệ thống sưởi ấm có đang hoạt động tốt không?\n(A) Vâng, đó là trang web của tôi.\n(B) Một cuộc chạy bộ năm ki-lô-mét.\n(C) Có, văn phòng hiện đang rất ấm áp."
    },
    21: {
        "questionTextVi": "Công trình sửa đường trước tòa thị chính vẫn chưa xong à?",
        "optionsVi": {
            "A": "(A) Tôi vừa hoàn thành bài thuyết trình tại hội nghị.",
            "B": "(B) Rất nhiều xe cộ đi lại vào buổi tối.",
            "C": "(C) Chưa, họ vẫn còn một tháng nữa mới hoàn thành."
        },
        "transcript": "Speaker: Isn't the roadwork in front of city hall finished yet?\n(A) I just finished my conference presentation.\n(B) A lot of traffic in the evening.\n(C) No, they still have another month to go.",
        "transcriptVi": "Người hỏi: Công trình sửa đường trước tòa thị chính vẫn chưa xong à?\n(A) Tôi vừa hoàn thành bài thuyết trình tại hội nghị.\n(B) Rất nhiều xe cộ đi lại vào buổi tối.\n(C) Chưa, họ vẫn còn một tháng nữa mới hoàn thành."
    },
    22: {
        "questionTextVi": "Ai sẽ phụ trách buổi đào tạo nhân viên mới hôm nay?",
        "optionsVi": {
            "A": "(A) Chúng ta sẽ sử dụng một video đã được ghi hình sẵn.",
            "B": "(B) Vâng, ngay sau bữa ăn trưa.",
            "C": "(C) Phòng học số 124."
        },
        "transcript": "Speaker: Who will lead the new employee training today?\n(A) We're using a recorded video.\n(B) Yes, right after lunch.\n(C) Classroom 124.",
        "transcriptVi": "Người hỏi: Ai sẽ phụ trách buổi đào tạo nhân viên mới hôm nay?\n(A) Chúng ta sẽ sử dụng một video đã được ghi hình sẵn.\n(B) Vâng, ngay sau bữa ăn trưa.\n(C) Phòng học số 124."
    },
    23: {
        "questionTextVi": "Cuộc thanh tra an toàn được lên lịch vào tháng này hay tháng sau?",
        "optionsVi": {
            "A": "(A) Tôi tưởng là mình đã lưu tệp tài liệu rồi.",
            "B": "(B) Người giám sát nhà xưởng.",
            "C": "(C) Nó diễn ra vào thứ Tư tuần này."
        },
        "transcript": "Speaker: Is the safety inspection scheduled for this month or next month?\n(A) I thought I saved the file.\n(B) The factory supervisor.\n(C) It's this Wednesday.",
        "transcriptVi": "Người hỏi: Cuộc thanh tra an toàn được lên lịch vào tháng này hay tháng sau?\n(A) Tôi tưởng là mình đã lưu tệp tài liệu rồi.\n(B) Người giám sát nhà xưởng.\n(C) Nó diễn ra vào thứ Tư tuần này."
    },
    24: {
        "questionTextVi": "Khi nào thì lễ hội thu hoạch mùa màng sẽ diễn ra?",
        "optionsVi": {
            "A": "(A) Vào một thời điểm nào đó trong tháng Mười.",
            "B": "(B) Tại trung tâm sinh hoạt cộng đồng.",
            "C": "(C) Trái cây và rau củ quả tươi sạch."
        },
        "transcript": "Speaker: When is the harvest festival taking place?\n(A) Sometime in October.\n(B) At the community center.\n(C) Fresh fruits and vegetables.",
        "transcriptVi": "Người hỏi: Khi nào thì lễ hội thu hoạch mùa màng sẽ diễn ra?\n(A) Vào một thời điểm nào đó trong tháng Mười.\n(B) Tại trung tâm sinh hoạt cộng đồng.\n(C) Trái cây và rau củ quả tươi sạch."
    },
    25: {
        "questionTextVi": "Chiếc máy tính xách tay mới của bạn có đắt tiền không?",
        "optionsVi": {
            "A": "(A) Bạn có mật khẩu mới chưa?",
            "B": "(B) Tôi đã có một phiếu giảm giá.",
            "C": "(C) Vâng, nó chạy rất nhanh."
        },
        "transcript": "Speaker: Was your new laptop expensive?\n(A) Do you have a new password?\n(B) I had a discount coupon.\n(C) Yes, it's very fast.",
        "transcriptVi": "Người hỏi: Chiếc máy tính xách tay mới của bạn có đắt tiền không?\n(A) Bạn có mật khẩu mới chưa?\n(B) Tôi đã có một phiếu giảm giá.\n(C) Vâng, nó chạy rất nhanh."
    },
    26: {
        "questionTextVi": "Sao chúng ta không đi cắm trại vào cuối tuần tới nhỉ?",
        "optionsVi": {
            "A": "(A) Vâng, chiếc đèn bàn đó khá là đẹp.",
            "B": "(B) Chúng ta nên đi sang bên trái hay bên phải?",
            "C": "(C) Thời gian đó rất phù hợp với tôi."
        },
        "transcript": "Speaker: Why don't we go on our camping trip next weekend?\n(A) Yes, that table lamp is quite nice.\n(B) Should we go left or right?\n(C) That works for me.",
        "transcriptVi": "Người nói: Sao chúng ta không đi cắm trại vào cuối tuần tới nhỉ?\n(A) Vâng, chiếc đèn bàn đó khá là đẹp.\n(B) Chúng ta nên đi sang bên trái hay bên phải?\n(C) Thời gian đó rất phù hợp với tôi."
    },
    27: {
        "questionTextVi": "Buổi hội thảo chuyên đề chiều nay đã bị dời lại, phải không?",
        "optionsVi": {
            "A": "(A) Tại bưu điện thành phố.",
            "B": "(B) Đúng vậy, hoãn lại cho đến thứ Hai tuần tới.",
            "C": "(C) Khoảng ba mươi người đã tham dự."
        },
        "transcript": "Speaker: The workshop for this afternoon was postponed, wasn't it?\n(A) At the post office.\n(B) Yes, until next Monday.\n(C) About thirty people attended.",
        "transcriptVi": "Người hỏi: Buổi hội thảo chuyên đề chiều nay đã bị dời lại, phải không?\n(A) Tại bưu điện thành phố.\n(B) Đúng vậy, hoãn lại cho đến thứ Hai tuần tới.\n(C) Khoảng ba mươi người đã tham dự."
    },
    28: {
        "questionTextVi": "Số liệu sản lượng sản xuất tháng trước của chúng ta thế nào rồi?",
        "optionsVi": {
            "A": "(A) Họ sản xuất xe ô tô chạy điện.",
            "B": "(B) Chín giờ sáng.",
            "C": "(C) Chúng ta đã phải đóng cửa ngừng hoạt động mất một tuần."
        },
        "transcript": "Speaker: How were our production figures last month?\n(A) They produce electric cars.\n(B) Nine o'clock in the morning.\n(C) We were closed down for a week.",
        "transcriptVi": "Người hỏi: Số liệu sản lượng sản xuất tháng trước của chúng ta thế nào rồi?\n(A) Họ sản xuất xe ô tô chạy điện.\n(B) Chín giờ sáng.\n(C) Chúng ta đã phải đóng cửa ngừng hoạt động mất một tuần."
    },
    29: {
        "questionTextVi": "Khi nào thì tôi có thể gặp bác sĩ trị liệu ngôn ngữ?",
        "optionsVi": {
            "A": "(A) Vâng, tôi đã lắng nghe bài phát biểu.",
            "B": "(B) Ở trên tầng ba.",
            "C": "(C) Cô ấy có một khung giờ hẹn trống vào sáng mai."
        },
        "transcript": "Speaker: When can I see the speech therapist?\n(A) Yes, I heard the speech.\n(B) On the third floor.\n(C) She has an opening tomorrow morning.",
        "transcriptVi": "Người hỏi: Khi nào thì tôi có thể gặp bác sĩ trị liệu ngôn ngữ?\n(A) Vâng, tôi đã lắng nghe bài phát biểu.\n(B) Ở trên tầng ba.\n(C) Cô ấy có một khung giờ hẹn trống vào sáng mai."
    },
    30: {
        "questionTextVi": "Bạn không đi đón các khách hàng từ sân bay à?",
        "optionsVi": {
            "A": "(A) Một buổi trình diễn giới thiệu sản phẩm.",
            "B": "(B) Không, tôi tin là Tomoko đang đi làm việc đó rồi.",
            "C": "(C) Anh ấy thích ngồi ở ghế cạnh lối đi hơn."
        },
        "transcript": "Speaker: Aren't you picking up the clients from the airport?\n(A) A product demonstration.\n(B) No, I believe Tomoko is doing that.\n(C) He prefers an aisle seat.",
        "transcriptVi": "Người hỏi: Bạn không đi đón các khách hàng từ sân bay à?\n(A) Một buổi trình diễn giới thiệu sản phẩm.\n(B) Không, tôi tin là Tomoko đang đi làm việc đó rồi.\n(C) Anh ấy thích ngồi ở ghế cạnh lối đi hơn."
    },
    31: {
        "questionTextVi": "Cuộc gặp khách hàng sáng nay của bạn diễn ra thế nào rồi?",
        "optionsVi": {
            "A": "(A) Rất vui được gặp bạn.",
            "B": "(B) Không, ở phòng hội nghị số hai cơ.",
            "C": "(C) Hợp đồng hiện đã được ký kết chính thức rồi."
        },
        "transcript": "Speaker: How was your morning client meeting?\n(A) It's great to meet you.\n(B) No, over in conference room two.\n(C) The contract is now officially signed.",
        "transcriptVi": "Người hỏi: Cuộc gặp khách hàng sáng nay của bạn diễn ra thế nào rồi?\n(A) Rất vui được gặp bạn.\n(B) Không, ở phòng hội nghị số hai cơ.\n(C) Hợp đồng hiện đã được ký kết chính thức rồi."
    }
}

with open('scratch/t3_p1_p2_vi.json', 'w', encoding='utf-8') as f:
    json.dump(t3_p1_p2_vi, f, ensure_ascii=False, indent=2)

print("Saved Test 3 Part 1 & Part 2 bilingual translations successfully!")
