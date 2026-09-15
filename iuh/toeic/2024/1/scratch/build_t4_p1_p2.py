# scratch/build_t4_p1_p2.py
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

t4_p1_p2 = [
    # Q1
    {
        "id": 1,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test4/part1.mp3",
        "image": "assets/images/test4/q1.png",
        "questionText": "Look at the picture marked No. 1 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 1 trong sách bài thi và chọn câu miêu tả đúng nhất:",
        "options": {
            "A": "He’s cleaning the floor.",
            "B": "He’s setting a plant on a shelf.",
            "C": "He’s pouring some liquid into a cup.",
            "D": "He’s ironing a shirt."
        },
        "optionsVi": {
            "A": "(A) Anh ấy đang lau sàn nhà.",
            "B": "(B) Anh ấy đang đặt chậu cây lên kệ.",
            "C": "(C) Anh ấy đang rót chất lỏng vào một chiếc cốc.",
            "D": "(D) Anh ấy đang ủi một chiếc áo sơ mi."
        },
        "correctAnswer": "C",
        "explanation": "Phương án (C) miêu tả chính xác hành động trong bức ảnh: Người đàn ông tại tiệm giặt đang cầm chai nước giặt và rót dung dịch vào nắp/cốc đo lường ('pouring some liquid into a cup'). Các phương án còn lại miêu tả hành động không xuất hiện trong ảnh.",
        "transcript": "(A) He’s cleaning the floor.\n(B) He’s setting a plant on a shelf.\n(C) He’s pouring some liquid into a cup.\n(D) He’s ironing a shirt.",
        "transcriptVi": "Người nói:\n(A) Anh ấy đang lau sàn nhà.\n(B) Anh ấy đang đặt chậu cây lên kệ.\n(C) Anh ấy đang rót chất lỏng vào một chiếc cốc.\n(D) Anh ấy đang ủi một chiếc áo sơ mi.",
        "vocabulary": [
            {"word": "pour", "ipa": "/pɔːr/", "pos": "v", "meaning": "rót, đổ chất lỏng", "example": "He’s pouring detergent liquid into a measuring cup."},
            {"word": "liquid", "ipa": "/ˈlɪk.wɪd/", "pos": "n", "meaning": "chất lỏng, dung dịch", "example": "Store the cleaning liquid in a cool place."},
            {"word": "clean the floor", "ipa": "/kliːn ðə flɔːr/", "pos": "phr", "meaning": "lau dọn sàn nhà", "example": "The staff members clean the floor every evening."},
            {"word": "iron a shirt", "ipa": "/ˈaɪən ə ʃɜːt/", "pos": "phr", "meaning": "ủi áo sơ mi", "example": "He quickly ironed his shirt before the interview."}
        ],
        "collocations": [
            {"phrase": "pour liquid into", "meaning": "rót chất lỏng vào"},
            {"phrase": "set on a shelf", "meaning": "đặt lên trên kệ"}
        ],
        "grammar": [
            {"title": "Thì hiện tại tiếp diễn miêu tả hành động người", "rule": "S + is/are + V-ing", "analysis": "Diễn tả hành động đang diễn ra tại thời điểm chụp bức ảnh."}
        ],
        "audioClip": "assets/audio/test4/cuts/q1.mp3",
        "audioLabel": "Nghe câu 1"
    },
    # Q2
    {
        "id": 2,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test4/part1.mp3",
        "image": "assets/images/test4/q2.png",
        "questionText": "Look at the picture marked No. 2 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 2 trong sách bài thi và chọn câu miêu tả đúng nhất:",
        "options": {
            "A": "They’re glancing at a monitor.",
            "B": "They’re putting pens in a jar.",
            "C": "They’re wiping off a desk.",
            "D": "They’re examining a document."
        },
        "optionsVi": {
            "A": "(A) Họ đang liếc nhìn vào màn hình máy tính.",
            "B": "(B) Họ đang cắm bút vào ống đựng bút.",
            "C": "(C) Họ đang lau chùi bàn làm việc.",
            "D": "(D) Họ đang xem xét một tập tài liệu."
        },
        "correctAnswer": "D",
        "explanation": "Phương án (D) miêu tả chính xác hành động của hai người phụ nữ: Cả hai đang cùng tập trung nhìn và kiểm tra các thông tin trên tập tài liệu gắn trên bảng kẹp ('They’re examining a document').",
        "transcript": "(A) They’re glancing at a monitor.\n(B) They’re putting pens in a jar.\n(C) They’re wiping off a desk.\n(D) They’re examining a document.",
        "transcriptVi": "Người nói:\n(A) Họ đang liếc nhìn vào màn hình máy tính.\n(B) Họ đang cắm bút vào ống đựng bút.\n(C) Họ đang lau chùi bàn làm việc.\n(D) Họ đang xem xét một tập tài liệu.",
        "vocabulary": [
            {"word": "examine", "ipa": "/ɪɡˈzæm.ɪn/", "pos": "v", "meaning": "xem xét, kiểm tra kỹ lưỡng", "example": "The supervisors are examining a project document together."},
            {"word": "document", "ipa": "/ˈdɒk.jə.mənt/", "pos": "n", "meaning": "tài liệu, văn kiện", "example": "Please sign the document before leaving the office."},
            {"word": "glance at", "ipa": "/ɡlɑːns æt/", "pos": "phr v", "meaning": "liếc nhìn thoáng qua", "example": "She glanced at her computer monitor to check the time."},
            {"word": "wipe off", "ipa": "/waɪp ɒf/", "pos": "phr v", "meaning": "lau sạch bụi bẩn trên bề mặt", "example": "He used a damp cloth to wipe off the wooden desk."}
        ],
        "collocations": [
            {"phrase": "examine a document", "meaning": "kiểm tra tài liệu"},
            {"phrase": "glance at a monitor", "meaning": "liếc nhìn màn hình"}
        ],
        "grammar": [
            {"title": "Động từ chỉ hoạt động thị giác và tư thế", "rule": "examine / glance at + Noun", "analysis": "'examine' chỉ hành động quan sát, nghiên cứu kỹ lưỡng chi tiết."}
        ],
        "audioClip": "assets/audio/test4/cuts/q2.mp3",
        "audioLabel": "Nghe câu 2"
    },
    # Q3
    {
        "id": 3,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test4/part1.mp3",
        "image": "assets/images/test4/q3.png",
        "questionText": "Look at the picture marked No. 3 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 3 trong sách bài thi và chọn câu miêu tả đúng nhất:",
        "options": {
            "A": "Some people are taking a ride on a boat.",
            "B": "A boat is floating under a bridge.",
            "C": "A boat is being loaded with cargo.",
            "D": "Some people are rowing a boat past a lighthouse."
        },
        "optionsVi": {
            "A": "(A) Một số người đang đi dạo/du ngoạn trên một chiếc thuyền.",
            "B": "(B) Một chiếc thuyền đang trôi dưới chân cầu.",
            "C": "(C) Một chiếc thuyền đang được chất hàng hóa lên.",
            "D": "(D) Một số người đang chèo thuyền ngang qua một ngọn hải đăng."
        },
        "correctAnswer": "A",
        "explanation": "Phương án (A) miêu tả đúng bức ảnh: Các hành khách đang ngồi tham quan, du ngoạn trên chiếc thuyền trên mặt nước ('taking a ride on a boat'). Bức ảnh không có cây cầu (bridge), không có việc bốc dỡ hàng hóa (cargo), và không có ngọn hải đăng (lighthouse).",
        "transcript": "(A) Some people are taking a ride on a boat.\n(B) A boat is floating under a bridge.\n(C) A boat is being loaded with cargo.\n(D) Some people are rowing a boat past a lighthouse.",
        "transcriptVi": "Người nói:\n(A) Một số người đang đi du ngoạn trên thuyền.\n(B) Một chiếc thuyền đang trôi dưới chân cầu.\n(C) Một chiếc thuyền đang được chất hàng hóa lên.\n(D) Một số người đang chèo thuyền ngang qua ngọn hải đăng.",
        "vocabulary": [
            {"word": "take a ride", "ipa": "/teɪk ə raɪd/", "pos": "phr", "meaning": "đi dạo, đi du ngoạn (bằng xe, thuyền)", "example": "Tourists enjoy taking a scenic ride on the river boat."},
            {"word": "float", "ipa": "/fləʊt/", "pos": "v", "meaning": "nổi bồng bềnh, trôi trên mặt nước", "example": "Several wooden rafts were floating near the pier."},
            {"word": "cargo", "ipa": "/ˈkɑː.ɡəʊ/", "pos": "n", "meaning": "hàng hóa chuyên chở (tàu biển, máy bay)", "example": "The container ship was loaded with heavy cargo."},
            {"word": "lighthouse", "ipa": "/ˈlaɪt.haʊs/", "pos": "n", "meaning": "ngọn hải đăng", "example": "The historic lighthouse guides ships safely into port."}
        ],
        "collocations": [
            {"phrase": "take a ride on a boat", "meaning": "du ngoạn trên thuyền"},
            {"phrase": "loaded with cargo", "meaning": "được bốc đầy hàng hóa"}
        ],
        "grammar": [
            {"title": "Cấu trúc bị động tiếp diễn", "rule": "S + is/are + being + V3", "analysis": "'is being loaded' miêu tả hành động bốc dỡ hàng đang trực tiếp xảy ra."}
        ],
        "audioClip": "assets/audio/test4/cuts/q3.mp3",
        "audioLabel": "Nghe câu 3"
    },
    # Q4
    {
        "id": 4,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test4/part1.mp3",
        "image": "assets/images/test4/q4.png",
        "questionText": "Look at the picture marked No. 4 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 4 trong sách bài thi và chọn câu miêu tả đúng nhất:",
        "options": {
            "A": "There’s a fire burning in a fireplace.",
            "B": "There’s a guitar beside a fireplace.",
            "C": "Some cables have been left on the ground in a pile.",
            "D": "A television is being packed into a box."
        },
        "optionsVi": {
            "A": "(A) Có ngọn lửa đang cháy trong lò sưởi.",
            "B": "(B) Có một cây đàn ghi-ta đặt cạnh lò sưởi.",
            "C": "(C) Một số dây cáp bị vứt thành đống trên mặt đất.",
            "D": "(D) Một chiếc ti vi đang được đóng gói vào thùng các-tông."
        },
        "correctAnswer": "B",
        "explanation": "Phương án (B) miêu tả chính xác cảnh tĩnh trong căn phòng: Chiếc đàn ghi-ta đặt tựa ở góc bên cạnh lò sưởi ('There’s a guitar beside a fireplace'). Trong lò sưởi không hề có lửa đang cháy (loại A), không có dây cáp (loại C), và không có người đang đóng gói TV (loại D).",
        "transcript": "(A) There’s a fire burning in a fireplace.\n(B) There’s a guitar beside a fireplace.\n(C) Some cables have been left on the ground in a pile.\n(D) A television is being packed into a box.",
        "transcriptVi": "Người nói:\n(A) Có ngọn lửa đang cháy trong lò sưởi.\n(B) Có một cây đàn ghi-ta đặt cạnh lò sưởi.\n(C) Một số dây cáp bị vứt thành đống trên sàn.\n(D) Một chiếc ti vi đang được đóng gói vào thùng các-tông.",
        "vocabulary": [
            {"word": "fireplace", "ipa": "/ˈfaɪə.pleɪs/", "pos": "n", "meaning": "lò sưởi trong nhà", "example": "An acoustic guitar was resting beside the brick fireplace."},
            {"word": "beside", "ipa": "/bɪˈsaɪd/", "pos": "prep", "meaning": "bên cạnh, sát gần", "example": "He placed the floor lamp beside the comfortable armchair."},
            {"word": "in a pile", "ipa": "/ɪn ə paɪl/", "pos": "phr", "meaning": "chất thành đống, xếp chồng lên nhau", "example": "Magazines were stacked neatly in a pile on the coffee table."},
            {"word": "pack", "ipa": "/pæk/", "pos": "v", "meaning": "đóng gói, xếp đồ vào thùng", "example": "Workers packed delicate glassware into protective boxes."}
        ],
        "collocations": [
            {"phrase": "beside a fireplace", "meaning": "bên cạnh lò sưởi"},
            {"phrase": "left on the ground", "meaning": "bị để lại trên sàn"}
        ],
        "grammar": [
            {"title": "Cấu trúc tồn tại với 'There is / There are'", "rule": "There + be + Noun + Prepositional Phrase", "analysis": "Dùng để miêu tả vị trí và sự hiện diện của đồ vật trong không gian."}
        ],
        "audioClip": "assets/audio/test4/cuts/q4.mp3",
        "audioLabel": "Nghe câu 4"
    },
    # Q5
    {
        "id": 5,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test4/part1.mp3",
        "image": "assets/images/test4/q5.png",
        "questionText": "Look at the picture marked No. 5 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 5 trong sách bài thi và chọn câu miêu tả đúng nhất:",
        "options": {
            "A": "Some people are riding bicycles through a field.",
            "B": "Some people are moving a picnic table.",
            "C": "There are some mountains in the distance.",
            "D": "A bicycle has fallen over on the ground."
        },
        "optionsVi": {
            "A": "(A) Một số người đang đạp xe đạp băng qua cánh đồng.",
            "B": "(B) Một số người đang khiêng bàn dã ngoại.",
            "C": "(C) Có những dãy núi ở phía xa xa.",
            "D": "(D) Một chiếc xe đạp bị đổ ngã trên mặt đất."
        },
        "correctAnswer": "C",
        "explanation": "Phương án (C) miêu tả chính xác bối cảnh hậu cảnh của bức ảnh phong cảnh: Phía đằng xa có những dãy núi nhấp nhô ('There are some mountains in the distance'). Không có ai đang đạp xe, không có ai khiêng bàn dã ngoại, và xe đạp không bị đổ ngã.",
        "transcript": "(A) Some people are riding bicycles through a field.\n(B) Some people are moving a picnic table.\n(C) There are some mountains in the distance.\n(D) A bicycle has fallen over on the ground.",
        "transcriptVi": "Người nói:\n(A) Một số người đang đạp xe qua cánh đồng.\n(B) Một số người đang khiêng bàn dã ngoại.\n(C) Có những dãy núi ở phía xa xa.\n(D) Một chiếc xe đạp bị ngã đổ trên mặt đất.",
        "vocabulary": [
            {"word": "in the distance", "ipa": "/ɪn ðə ˈdɪs.təns/", "pos": "phr", "meaning": "ở đằng xa, phía chân trời xa", "example": "Snow-capped mountain peaks could be seen in the distance."},
            {"word": "picnic table", "ipa": "/ˈpɪk.nɪk ˈteɪ.bəl/", "pos": "n", "meaning": "bàn ghế ăn dã ngoại ngoài trời", "example": "Visitors rested at a wooden picnic table under the trees."},
            {"word": "fall over", "ipa": "/fɔːl ˈəʊ.vər/", "pos": "phr v", "meaning": "ngã đổ, sụp xuống", "example": "The strong wind caused the parked bicycle to fall over."},
            {"word": "field", "ipa": "/fiːld/", "pos": "n", "meaning": "cánh đồng cỏ, thảo nguyên", "example": "Wildflowers bloomed across the green grassy field."}
        ],
        "collocations": [
            {"phrase": "in the distance", "meaning": "ở đằng xa"},
            {"phrase": "ride bicycles through", "meaning": "đạp xe xuyên qua"}
        ],
        "grammar": [
            {"title": "Cụm giới từ chỉ phương hướng và khoảng cách", "rule": "in the distance / on the horizon", "analysis": "Dùng để miêu tả các chi tiết phong cảnh nằm ở hậu cảnh (background) của bức ảnh."}
        ],
        "audioClip": "assets/audio/test4/cuts/q5.mp3",
        "audioLabel": "Nghe câu 5"
    },
    # Q6
    {
        "id": 6,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test4/part1.mp3",
        "image": "assets/images/test4/q6.png",
        "questionText": "Look at the picture marked No. 6 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 6 trong sách bài thi và chọn câu miêu tả đúng nhất:",
        "options": {
            "A": "Some couches have been pushed against a wall.",
            "B": "Some lights have been hung from the ceiling.",
            "C": "Some cushions have been stacked on the floor.",
            "D": "Some flowers have been arranged in a vase."
        },
        "optionsVi": {
            "A": "(A) Một số ghế sofa đã được kê sát vào tường.",
            "B": "(B) Một số bóng đèn đã được treo từ trần nhà xuống.",
            "C": "(C) Một số chiếc đệm gối đã được xếp chồng lên sàn.",
            "D": "(D) Một số bông hoa đã được cắm/sắp đặt trong bình hoa."
        },
        "correctAnswer": "D",
        "explanation": "Phương án (D) miêu tả đúng vật thể nổi bật trên bàn: Một bình hoa cắm hoa tươi được bài trí trang nhã ('Some flowers have been arranged in a vase'). Ghế sofa không kê sát tường, gối không xếp chồng trên sàn nhà.",
        "transcript": "(A) Some couches have been pushed against a wall.\n(B) Some lights have been hung from the ceiling.\n(C) Some cushions have been stacked on the floor.\n(D) Some flowers have been arranged in a vase.",
        "transcriptVi": "Người nói:\n(A) Một số ghế sofa đã được kê sát vào tường.\n(B) Một số bóng đèn đã được treo từ trần nhà xuống.\n(C) Một số chiếc đệm gối đã được xếp chồng trên sàn nhà.\n(D) Một số bông hoa đã được cắm trang nhã trong bình hoa.",
        "vocabulary": [
            {"word": "arrange flowers", "ipa": "/əˈreɪndʒ ˈflaʊ.ərz/", "pos": "phr", "meaning": "cắm hoa, sắp xếp hoa vào bình", "example": "Fresh lilies have been beautifully arranged in a glass vase."},
            {"word": "vase", "ipa": "/vɑːz/", "pos": "n", "meaning": "bình hoa, lọ hoa", "example": "A ceramic vase stands on the reception side table."},
            {"word": "cushion", "ipa": "/ˈkʊʃ.ən/", "pos": "n", "meaning": "gối tựa lưng, đệm ngồi sofa", "example": "Decorative soft cushions were placed on the modern couch."},
            {"word": "hang from the ceiling", "ipa": "/hæŋ frəm ðə ˈsiː.lɪŋ/", "pos": "phr", "meaning": "treo lơ lửng từ trần nhà", "example": "Pendant lights hang gracefully from the wooden ceiling."}
        ],
        "collocations": [
            {"phrase": "arranged in a vase", "meaning": "được cắm trong bình hoa"},
            {"phrase": "pushed against a wall", "meaning": "kê sát vào tường"}
        ],
        "grammar": [
            {"title": "Thể bị động hiện tại hoàn thành diễn tả trạng thái", "rule": "have/has been + V3", "analysis": "'have been arranged' diễn tả kết quả của hành động đã hoàn tất và lưu lại trạng thái tĩnh ở hiện tại."}
        ],
        "audioClip": "assets/audio/test4/cuts/q6.mp3",
        "audioLabel": "Nghe câu 6"
    }
]

print("Built Test 4 Part 1 questions 1 to 6!")
