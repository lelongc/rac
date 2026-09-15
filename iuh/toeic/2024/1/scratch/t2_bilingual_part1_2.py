# scratch/t2_bilingual_part1_2.py: Full translations for Test 2 Part 1 & Part 2
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

t2_p1_p2_vi = {
    # Part 1: Q1 - Q6
    1: {
        "questionTextVi": "Nhìn vào bức tranh số 1 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Cô ấy đang cắm một sợi dây nguồn vào ổ cắm trên tường.",
            "B": "(B) Cô ấy đang nhấn một nút bấm trên máy móc.",
            "C": "(C) Cô ấy đang cầm tay nắm của một ngăn kéo.",
            "D": "(D) Cô ấy đang gắn một thông báo lên tường."
        },
        "transcript": "(A) She's inserting a cord into an outlet.\n(B) She's pressing a button on a machine.\n(C) She's gripping the handle of a drawer.\n(D) She's tacking a notice onto the wall.",
        "transcriptVi": "Người nói:\n(A) Cô ấy đang cắm một sợi dây nguồn vào ổ cắm trên tường.\n(B) Cô ấy đang nhấn một nút bấm trên máy móc.\n(C) Cô ấy đang cầm tay nắm của một ngăn kéo.\n(D) Cô ấy đang gắn một thông báo lên tường."
    },
    2: {
        "questionTextVi": "Nhìn vào bức tranh số 2 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Một số cửa chớp cửa sổ đang được thay thế.",
            "B": "(B) Một chiếc gối đang được sắp xếp đặt lên ghế ngồi.",
            "C": "(C) Một chiếc bàn ngoài trời đang được dọn sạch đồ.",
            "D": "(D) Một số tấm ván gỗ đang được sơn màu."
        },
        "transcript": "(A) Some window shutters are being replaced.\n(B) A pillow is being arranged on a seat.\n(C) An outdoor table is being cleared off.\n(D) Some wooden boards are being painted.",
        "transcriptVi": "Người nói:\n(A) Một số cửa chớp cửa sổ đang được thay thế.\n(B) Một chiếc gối đang được sắp xếp đặt lên ghế ngồi.\n(C) Một chiếc bàn ngoài trời đang được dọn sạch đồ.\n(D) Một số tấm ván gỗ đang được sơn màu."
    },
    3: {
        "questionTextVi": "Nhìn vào bức tranh số 3 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Một số dụng cụ đã bị vứt vào thùng rác.",
            "B": "(B) Một số chai lọ đang được đổ hết vào bồn rửa.",
            "C": "(C) Một chiếc ghế xoay có bánh xe đã được đặt cạnh quầy bàn.",
            "D": "(D) Một số ngăn kéo đang bị để mở."
        },
        "transcript": "(A) Some utensils have been discarded in a bin.\n(B) Some bottles are being emptied into a sink.\n(C) A rolling chair has been placed next to a counter.\n(D) Some drawers have been left open.",
        "transcriptVi": "Người nói:\n(A) Một số dụng cụ đã bị vứt vào thùng rác.\n(B) Một số chai lọ đang được đổ hết vào bồn rửa.\n(C) Một chiếc ghế xoay có bánh xe đã được đặt cạnh quầy bàn.\n(D) Một số ngăn kéo đang bị để mở."
    },
    4: {
        "questionTextVi": "Nhìn vào bức tranh số 4 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Một người đàn ông đang chặt gỗ thành từng mảnh nhỏ.",
            "B": "(B) Lá cây đang rải rác khắp bãi cỏ.",
            "C": "(C) Một người đàn ông đang đóng cửa sổ.",
            "D": "(D) Củi gỗ được chất đống gần một hàng rào."
        },
        "transcript": "(A) A man is chopping some wood into pieces.\n(B) Leaves are scattered across the grass.\n(C) A man is closing a window.\n(D) Wood is piled near a fence.",
        "transcriptVi": "Người nói:\n(A) Một người đàn ông đang chặt gỗ thành từng mảnh nhỏ.\n(B) Lá cây đang rải rác khắp bãi cỏ.\n(C) Một người đàn ông đang đóng cửa sổ.\n(D) Củi gỗ được chất đống gần một hàng rào."
    },
    5: {
        "questionTextVi": "Nhìn vào bức tranh số 5 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Mọi người đang xếp hàng trong một tiền sảnh.",
            "B": "(B) Hàng hóa đang được xếp vào các túi mua hàng.",
            "C": "(C) Những chiếc lều bạt đã được dựng lên tại khu vực đỗ xe.",
            "D": "(D) Một công nhân đang dựng một mái che bạt."
        },
        "transcript": "(A) People are standing in line in a lobby.\n(B) Items are being loaded into shopping bags.\n(C) Tents have been set up in a parking area.\n(D) A worker is putting up a canopy.",
        "transcriptVi": "Người nói:\n(A) Mọi người đang xếp hàng trong một tiền sảnh.\n(B) Hàng hóa đang được xếp vào các túi mua hàng.\n(C) Những chiếc lều bạt đã được dựng lên tại khu vực đỗ xe.\n(D) Một công nhân đang dựng một mái che bạt."
    },
    6: {
        "questionTextVi": "Nhìn vào bức tranh số 6 và chọn phương án miêu tả đúng nhất:",
        "optionsVi": {
            "A": "(A) Một số hành lý được xếp cạnh thang cuốn.",
            "B": "(B) Một chiếc vali đang được nhấc lên xe buýt đưa đón.",
            "C": "(C) Một số vali được trưng bày trong cửa sổ tiệm bán hàng.",
            "D": "(D) Một giá để hành lý có hai tầng."
        },
        "transcript": "(A) Some luggage is stacked next to an escalator.\n(B) A suitcase is being lifted onto a shuttle bus.\n(C) Some suitcases are displayed in a shop window.\n(D) A luggage rack has two levels.",
        "transcriptVi": "Người nói:\n(A) Một số hành lý được xếp cạnh thang cuốn.\n(B) Một chiếc vali đang được nhấc lên xe buýt đưa đón.\n(C) Một số vali được trưng bày trong cửa sổ tiệm bán hàng.\n(D) Một giá để hành lý có hai tầng."
    },

    # Part 2: Q7 - Q31
    7: {
        "questionTextVi": "Các máy móc trên sàn nhà xưởng đã được dọn sạch chưa?",
        "optionsVi": {
            "A": "(A) Chưa, vẫn chưa được dọn.",
            "B": "(B) Nó ở trong thùng công-ten-nơ vận chuyển.",
            "C": "(C) Tôi vừa mới vứt nó vào thùng rác."
        },
        "transcript": "Speaker: Have the machines on the factory floor been cleaned?\n(A) No, not yet.\n(B) It's in the shipping container.\n(C) I just put it in the trash bin.",
        "transcriptVi": "Người hỏi: Các máy móc trên sàn nhà xưởng đã được dọn sạch chưa?\n(A) Chưa, vẫn chưa được dọn.\n(B) Nó ở trong thùng công-ten-nơ vận chuyển.\n(C) Tôi vừa mới vứt nó vào thùng rác."
    },
    8: {
        "questionTextVi": "Ngân sách năm tới sẽ tăng thêm bao nhiêu?",
        "optionsVi": {
            "A": "(A) Khoảng 10 phần trăm.",
            "B": "(B) Tôi nghĩ là khoảng ba tiếng.",
            "C": "(C) Tại chi nhánh chính của ngân hàng."
        },
        "transcript": "Speaker: How much will the budget increase next year?\n(A) About 10 percent.\n(B) Three hours, I think.\n(C) At the bank's main branch.",
        "transcriptVi": "Người hỏi: Ngân sách năm tới sẽ tăng thêm bao nhiêu?\n(A) Khoảng 10 phần trăm.\n(B) Tôi nghĩ là khoảng ba tiếng.\n(C) Tại chi nhánh chính của ngân hàng."
    },
    9: {
        "questionTextVi": "Bạn sẽ tưới cây trước khi ra về, đúng không?",
        "optionsVi": {
            "A": "(A) Tôi đã đi bộ suốt cả quãng đường.",
            "B": "(B) Vâng, ngay sau bữa trưa.",
            "C": "(C) Ở trong phòng nghỉ giải lao."
        },
        "transcript": "Speaker: You're going to water the plants before you leave, aren't you?\n(A) I walked the whole way.\n(B) Yes, right after lunch.\n(C) In the break room.",
        "transcriptVi": "Người hỏi: Bạn sẽ tưới cây trước khi ra về, đúng không?\n(A) Tôi đã đi bộ suốt cả quãng đường.\n(B) Vâng, ngay sau bữa trưa.\n(C) Ở trong phòng nghỉ giải lao."
    },
    10: {
        "questionTextVi": "Bạn không định hẹn lịch khám bác sĩ mắt à?",
        "optionsVi": {
            "A": "(A) Chiếc kính đó trông rất hợp với bạn.",
            "B": "(B) Tôi đã hẹn lịch rồi.",
            "C": "(C) Hội thảo kéo dài ba ngày."
        },
        "transcript": "Speaker: Aren't you going to schedule an eye doctor appointment?\n(A) Those glasses look nice on you.\n(B) I already scheduled one.\n(C) The seminar is three days long.",
        "transcriptVi": "Người hỏi: Bạn không định hẹn lịch khám bác sĩ mắt à?\n(A) Chiếc kính đó trông rất hợp với bạn.\n(B) Tôi đã hẹn lịch rồi.\n(C) Hội thảo kéo dài ba ngày."
    },
    11: {
        "questionTextVi": "Tôi sẽ thử sửa chiếc máy in này.",
        "optionsVi": {
            "A": "(A) Nó không vừa vặn.",
            "B": "(B) Bản sao chụp hai mặt.",
            "C": "(C) Bạn có chắc là nó sửa được không?"
        },
        "transcript": "Speaker: I'm going to try to fix this printer.\n(A) It doesn't fit.\n(B) Double-sided copies.\n(C) Are you sure it can be repaired?",
        "transcriptVi": "Người nói: Tôi sẽ thử sửa chiếc máy in này.\n(A) Nó không vừa vặn.\n(B) Bản sao chụp hai mặt.\n(C) Bạn có chắc là nó sửa được không?"
    },
    12: {
        "questionTextVi": "Chúng ta nên làm gì với những tập tài liệu quảng cáo này?",
        "optionsVi": {
            "A": "(A) Một chuyến đi đến bờ biển.",
            "B": "(B) Vâng, tôi đã tìm thấy nó rồi.",
            "C": "(C) Tôi sẽ để chúng ở bàn tiếp tân."
        },
        "transcript": "Speaker: What should we do with these brochures?\n(A) A trip to the seashore.\n(B) Yes, I found it already.\n(C) I'll leave them at the front desk.",
        "transcriptVi": "Người hỏi: Chúng ta nên làm gì với những tập tài liệu quảng cáo này?\n(A) Một chuyến đi đến bờ biển.\n(B) Vâng, tôi đã tìm thấy nó rồi.\n(C) Tôi sẽ để chúng ở bàn tiếp tân."
    },
    13: {
        "questionTextVi": "Cuộc họp về chính sách đã được đổi lịch chưa?",
        "optionsVi": {
            "A": "(A) Chúng tôi có rất nhiều mẫu thiết kế lịch để bàn.",
            "B": "(B) Có, nó sẽ diễn ra vào ngày mai thay vào đó.",
            "C": "(C) Món súp này rất ngon."
        },
        "transcript": "Speaker: Has the policy meeting been rescheduled?\n(A) We have lots of desk calendar designs.\n(B) Yes, it's happening tomorrow instead.\n(C) This soup is delicious.",
        "transcriptVi": "Người hỏi: Cuộc họp về chính sách đã được đổi lịch chưa?\n(A) Chúng tôi có rất nhiều mẫu thiết kế lịch để bàn.\n(B) Có, nó sẽ diễn ra vào ngày mai thay vào đó.\n(C) Món súp này rất ngon."
    },
    14: {
        "questionTextVi": "Sao chúng ta không ghé căng-tin công ty trên đường tới buổi hội thảo nhỉ?",
        "optionsVi": {
            "A": "(A) Được chứ, chúng ta có đủ thời gian mà.",
            "B": "(B) Một bữa tiệc tự chọn phục vụ đầy đủ.",
            "C": "(C) Chủ đề là kết nối mạng lưới quan hệ chuyên nghiệp."
        },
        "transcript": "Speaker: Why don't we stop by the office cafeteria on our way to the workshop?\n(A) Sure, we have time for that.\n(B) A full service buffet.\n(C) The topic is professional networking.",
        "transcriptVi": "Người nói: Sao chúng ta không ghé căng-tin công ty trên đường tới buổi hội thảo nhỉ?\n(A) Được chứ, chúng ta có đủ thời gian mà.\n(B) Một bữa tiệc tự chọn phục vụ đầy đủ.\n(C) Chủ đề là kết nối mạng lưới quan hệ chuyên nghiệp."
    },
    15: {
        "questionTextVi": "Bạn đã thử món mì ống nổi tiếng của chúng tôi chưa?",
        "optionsVi": {
            "A": "(A) Chúng tôi cần một bàn cho năm người.",
            "B": "(B) Vâng, món đó rất ngon.",
            "C": "(C) Tôi sẽ cố gắng đến đúng giờ."
        },
        "transcript": "Speaker: Have you tried our famous pasta dish?\n(A) We need a table for five.\n(B) Yes, it was delicious.\n(C) I'll try to make it on time.",
        "transcriptVi": "Người hỏi: Bạn đã thử món mì ống nổi tiếng của chúng tôi chưa?\n(A) Chúng tôi cần một bàn cho năm người.\n(B) Vâng, món đó rất ngon.\n(C) Tôi sẽ cố gắng đến đúng giờ."
    },
    16: {
        "questionTextVi": "Ai là người biểu diễn mở màn trong buổi hòa nhạc tối nay?",
        "optionsVi": {
            "A": "(A) Bạn có thể tăng âm lượng lên được không?",
            "B": "(B) Một ca sĩ nhạc jazz đến từ nước Pháp.",
            "C": "(C) Vị trí công việc đó đã được tuyển đủ."
        },
        "transcript": "Speaker: Who's the opening act at tonight's concert?\n(A) Could you turn up the volume?\n(B) A jazz singer from France.\n(C) The position has been filled.",
        "transcriptVi": "Người hỏi: Ai là người biểu diễn mở màn trong buổi hòa nhạc tối nay?\n(A) Bạn có thể tăng âm lượng lên được không?\n(B) Một ca sĩ nhạc jazz đến từ nước Pháp.\n(C) Vị trí công việc đó đã được tuyển đủ."
    },
    17: {
        "questionTextVi": "Khi nào thì phần thuyết trình giới thiệu sản phẩm bắt đầu?",
        "optionsVi": {
            "A": "(A) Lịch trình đã được gửi qua email vào thứ Sáu tuần trước.",
            "B": "(B) Một vài tính năng rất sáng tạo đột phá.",
            "C": "(C) Tôi nghĩ là ở phòng 202."
        },
        "transcript": "Speaker: When do the product demonstrations start?\n(A) The schedule was emailed last Friday.\n(B) Some innovative features.\n(C) In room 202, I think.",
        "transcriptVi": "Người hỏi: Khi nào thì phần thuyết trình giới thiệu sản phẩm bắt đầu?\n(A) Lịch trình đã được gửi qua email vào thứ Sáu tuần trước.\n(B) Một vài tính năng rất sáng tạo đột phá.\n(C) Tôi nghĩ là ở phòng 202."
    },
    18: {
        "questionTextVi": "Tôi đã cố cập nhật trang web, nhưng không thành công.",
        "optionsVi": {
            "A": "(A) Ngày đó thuận tiện cho tôi.",
            "B": "(B) Thường là các bài đánh giá trực tuyến của chúng tôi.",
            "C": "(C) Cứ gửi cho tôi những nội dung thay đổi mà bạn muốn."
        },
        "transcript": "Speaker: I tried updating the website, but it didn't work.\n(A) That date works for me.\n(B) Usually our online reviews.\n(C) Just send me the changes you want.",
        "transcriptVi": "Người nói: Tôi đã cố cập nhật trang web, nhưng không thành công.\n(A) Ngày đó thuận tiện cho tôi.\n(B) Thường là các bài đánh giá trực tuyến của chúng tôi.\n(C) Cứ gửi cho tôi những nội dung thay đổi mà bạn muốn."
    },
    19: {
        "questionTextVi": "Bạn đã tuyển một chuyên gia thợ hàn mới rồi à?",
        "optionsVi": {
            "A": "(A) Bộ phận linh kiện này đang hết hàng tạm thời.",
            "B": "(B) Vâng, anh ấy bắt đầu đi làm từ ngày mai.",
            "C": "(C) Không, nó nên ở mức cao hơn."
        },
        "transcript": "Speaker: Did you hire a new welding specialist?\n(A) The part is back-ordered.\n(B) Yes, he starts tomorrow.\n(C) No, it should be higher.",
        "transcriptVi": "Người hỏi: Bạn đã tuyển một chuyên gia thợ hàn mới rồi à?\n(A) Bộ phận linh kiện này đang hết hàng tạm thời.\n(B) Vâng, anh ấy bắt đầu đi làm từ ngày mai.\n(C) Không, nó nên ở mức cao hơn."
    },
    20: {
        "questionTextVi": "Bảng phối màu cho sảnh tòa nhà đã được chọn như thế nào vậy?",
        "optionsVi": {
            "A": "(A) Màu xanh lam và màu cam.",
            "B": "(B) Mọi chuyện đều ổn, cảm ơn bạn.",
            "C": "(C) Tôi không tham gia vào việc đó."
        },
        "transcript": "Speaker: How was the color palette for the lobby chosen?\n(A) Blue and orange.\n(B) It was fine, thanks.\n(C) I wasn't involved.",
        "transcriptVi": "Người hỏi: Bảng phối màu cho sảnh tòa nhà đã được chọn như thế nào vậy?\n(A) Màu xanh lam và màu cam.\n(B) Mọi chuyện đều ổn, cảm ơn bạn.\n(C) Tôi không tham gia vào việc đó."
    },
    21: {
        "questionTextVi": "Khi nào chúng ta sẽ đặt thêm đồ dùng văn phòng phẩm cho văn phòng?",
        "optionsVi": {
            "A": "(A) Trong tủ để đồ dự trữ.",
            "B": "(B) Vào thứ Hai tuần tới.",
            "C": "(C) Chiếc bàn làm việc mới trông rất đẹp."
        },
        "transcript": "Speaker: When are we ordering more supplies for the office?\n(A) In the storage closet.\n(B) Next week on Monday.\n(C) The new desk looks great.",
        "transcriptVi": "Người hỏi: Khi nào chúng ta sẽ đặt thêm đồ dùng văn phòng phẩm cho văn phòng?\n(A) Trong tủ để đồ dự trữ.\n(B) Vào thứ Hai tuần tới.\n(C) Chiếc bàn làm việc mới trông rất đẹp."
    },
    22: {
        "questionTextVi": "Pin cho máy bơm nước sẽ dùng năng lượng mặt trời, đúng không?",
        "optionsVi": {
            "A": "(A) Chúng tôi vẫn đang trong các giai đoạn lập kế hoạch.",
            "B": "(B) 140 đô la mỗi năm.",
            "C": "(C) Vâng, tôi rất muốn một cốc nước."
        },
        "transcript": "Speaker: The battery for the water pump is going to be solar powered, right?\n(A) We're still in the planning stages.\n(B) 140 dollars per year.\n(C) Yes, I'd love a glass of water.",
        "transcriptVi": "Người hỏi: Pin cho máy bơm nước sẽ dùng năng lượng mặt trời, đúng không?\n(A) Chúng tôi vẫn đang trong các giai đoạn lập kế hoạch.\n(B) 140 đô la mỗi năm.\n(C) Vâng, tôi rất muốn một cốc nước."
    },
    23: {
        "questionTextVi": "Tôi có thể mua cục sạc cho chiếc máy tính xách tay này ở đâu?",
        "optionsVi": {
            "A": "(A) Vào khoảng ba giờ đúng.",
            "B": "(B) Tôi có thể đặt mua một chiếc giúp bạn.",
            "C": "(C) Chính sách đổi trả hàng có giới hạn."
        },
        "transcript": "Speaker: Where can I buy a charger for this laptop?\n(A) Around three o'clock.\n(B) I can order one for you.\n(C) A limited return policy.",
        "transcriptVi": "Người hỏi: Tôi có thể mua cục sạc cho chiếc máy tính xách tay này ở đâu?\n(A) Vào khoảng ba giờ đúng.\n(B) Tôi có thể đặt mua một chiếc giúp bạn.\n(C) Chính sách đổi trả hàng có giới hạn."
    },
    24: {
        "questionTextVi": "Tôi có cần phải đặt trước phòng họp không?",
        "optionsVi": {
            "A": "(A) Có chứ, để tôi chỉ cho bạn cách đặt nhé.",
            "B": "(B) Dịch vụ ở đó rất tốt.",
            "C": "(C) Bài thuyết trình slide của tôi."
        },
        "transcript": "Speaker: Do I need to reserve a meeting room?\n(A) Yes, let me show you how.\n(B) The service is good.\n(C) My slide presentation.",
        "transcriptVi": "Người hỏi: Tôi có cần phải đặt trước phòng họp không?\n(A) Có chứ, để tôi chỉ cho bạn cách đặt nhé.\n(B) Dịch vụ ở đó rất tốt.\n(C) Bài thuyết trình slide của tôi."
    },
    25: {
        "questionTextVi": "Khi nào thì giám đốc bộ phận mới dự kiến sẽ bắt đầu làm việc?",
        "optionsVi": {
            "A": "(A) Nó kéo dài khoảng một tiếng đồng hồ.",
            "B": "(B) Bà Pavlova vài tuần nữa mới nghỉ hưu cơ.",
            "C": "(C) Không, bộ phận đó ở tầng trên."
        },
        "transcript": "Speaker: When's the new department director supposed to start?\n(A) It's an hour long.\n(B) Ms. Pavlova isn't retiring for several weeks.\n(C) No, that department's upstairs.",
        "transcriptVi": "Người hỏi: Khi nào thì giám đốc bộ phận mới dự kiến sẽ bắt đầu làm việc?\n(A) Nó kéo dài khoảng một tiếng đồng hồ.\n(B) Bà Pavlova vài tuần nữa mới nghỉ hưu cơ.\n(C) Không, bộ phận đó ở tầng trên."
    },
    26: {
        "questionTextVi": "Tôi nên đi giao những chiếc bánh pizza này, hay là bạn sẽ đi?",
        "optionsVi": {
            "A": "(A) Thôi cảm ơn, tôi không thấy đói.",
            "B": "(B) Mười đô la cho hai chiếc.",
            "C": "(C) Khách hàng đang đến lấy trực tiếp rồi."
        },
        "transcript": "Speaker: Should I deliver these pizzas, or will you?\n(A) No thanks, I'm not hungry.\n(B) Ten dollars for two.\n(C) They're being picked up.",
        "transcriptVi": "Người hỏi: Tôi nên đi giao những chiếc bánh pizza này, hay là bạn sẽ đi?\n(A) Thôi cảm ơn, tôi không thấy đói.\n(B) Mười đô la cho hai chiếc.\n(C) Khách hàng đang đến lấy trực tiếp rồi."
    },
    27: {
        "questionTextVi": "Lịch trình giao hàng tháng này đã được sửa đổi lại.",
        "optionsVi": {
            "A": "(A) Tôi cũng không tìm thấy chúng.",
            "B": "(B) Những ngày nào đã bị thay đổi vậy?",
            "C": "(C) Hai đô la một pound."
        },
        "transcript": "Speaker: This month's shipment schedule has been revised.\n(A) I couldn't find them either.\n(B) Which dates have been changed?\n(C) Two dollars per pound.",
        "transcriptVi": "Người nói: Lịch trình giao hàng tháng này đã được sửa đổi lại.\n(A) Tôi cũng không tìm thấy chúng.\n(B) Những ngày nào đã bị thay đổi vậy?\n(C) Hai đô la một pound."
    },
    28: {
        "questionTextVi": "Chi phí sửa chữa sẽ hết bao nhiêu tiền?",
        "optionsVi": {
            "A": "(A) Chi phí sửa chữa được gói bảo hành chi trả toàn bộ.",
            "B": "(B) Vâng, nó cũng có màu đỏ nữa.",
            "C": "(C) Trong khoảng hai tuần."
        },
        "transcript": "Speaker: How much will the repairs cost?\n(A) The work is covered under the warranty plan.\n(B) Yes, it's also available in red.\n(C) In about two weeks.",
        "transcriptVi": "Người hỏi: Chi phí sửa chữa sẽ hết bao nhiêu tiền?\n(A) Chi phí sửa chữa được gói bảo hành chi trả toàn bộ.\n(B) Vâng, nó cũng có màu đỏ nữa.\n(C) Trong khoảng hai tuần."
    },
    29: {
        "questionTextVi": "Sao chúng ta không cung cấp thêm các mẫu hoa văn giấy dán tường nhỉ?",
        "optionsVi": {
            "A": "(A) Báo được phát hàng ngày.",
            "B": "(B) Một khóa học thiết kế nội thất.",
            "C": "(C) Có rất nhiều mẫu trong các tập bìa hồ sơ rồi mà."
        },
        "transcript": "Speaker: Why don't we provide more samples of the wallpaper patterns?\n(A) The newspaper is delivered daily.\n(B) An interior design course.\n(C) There are plenty in the binders.",
        "transcriptVi": "Người nói: Sao chúng ta không cung cấp thêm các mẫu hoa văn giấy dán tường nhỉ?\n(A) Báo được phát hàng ngày.\n(B) Một khóa học thiết kế nội thất.\n(C) Có rất nhiều mẫu trong các tập bìa hồ sơ rồi mà."
    },
    30: {
        "questionTextVi": "Bạn có thể dẫn tôi đi tham quan bất động sản này vào chiều nay được không?",
        "optionsVi": {
            "A": "(A) Xin lỗi, đến tận ngày mai tôi mới có thời gian rảnh.",
            "B": "(B) Nó có một thiết kế rất hiện đại.",
            "C": "(C) Một ngôi nhà trên đường Maple."
        },
        "transcript": "Speaker: Can you give me a tour of the property this afternoon?\n(A) Sorry, I won't have time until tomorrow.\n(B) It has a very modern design.\n(C) A house on Maple Street.",
        "transcriptVi": "Người hỏi: Bạn có thể dẫn tôi đi tham quan bất động sản này vào chiều nay được không?\n(A) Xin lỗi, đến tận ngày mai tôi mới có thời gian rảnh.\n(B) Nó có một thiết kế rất hiện đại.\n(C) Một ngôi nhà trên đường Maple."
    },
    31: {
        "questionTextVi": "Ai được xếp lịch kiểm thử sản phẩm vào hôm nay?",
        "optionsVi": {
            "A": "(A) Chúng tôi vẫn đang chờ xác nhận.",
            "B": "(B) Đó là một album tuyệt vời, phải không?",
            "C": "(C) Khoảng sáu tuần trước."
        },
        "transcript": "Speaker: Who's scheduled to test the product today?\n(A) We're waiting for confirmation.\n(B) It's a great album, right?\n(C) About six weeks ago.",
        "transcriptVi": "Người hỏi: Ai được xếp lịch kiểm thử sản phẩm vào hôm nay?\n(A) Chúng tôi vẫn đang chờ xác nhận.\n(B) Đó là một album tuyệt vời, phải không?\n(C) Khoảng sáu tuần trước."
    }
}

with open('scratch/t2_p1_p2_vi.json', 'w', encoding='utf-8') as f:
    json.dump(t2_p1_p2_vi, f, ensure_ascii=False, indent=2)

print("Saved Test 2 Part 1 & Part 2 bilingual translations successfully!")
