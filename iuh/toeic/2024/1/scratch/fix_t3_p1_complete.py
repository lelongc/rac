import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test3.json', 'r', encoding='utf-8') as f:
    test3 = json.load(f)

# Definitions for Questions 1 to 6 in Test 3
p1_updates = {
    1: {
        "id": 1,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test3/part1.mp3",
        "audioClip": "assets/audio/test3/cuts/q1.mp3",
        "audioLabel": "Nghe câu 1",
        "image": "assets/images/test3/q1.png",
        "questionText": "Look at the picture marked No. 1 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 1 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "She’s cleaning an oven.",
            "B": "She’s moving a pot.",
            "C": "She’s opening a cabinet.",
            "D": "She’s holding a towel."
        },
        "optionsVi": {
            "A": "(A) Cô ấy đang lau chùi lò nướng.",
            "B": "(B) Cô ấy đang di chuyển một chiếc nồi.",
            "C": "(C) Cô ấy đang mở ngăn tủ.",
            "D": "(D) Cô ấy đang cầm một chiếc khăn."
        },
        "correctAnswer": "D",
        "explanation": "Phương án (D) miêu tả chính xác hành động trong bức ảnh: Người phụ nữ trong bếp đang hai tay cầm một chiếc khăn vải ('She's holding a towel').",
        "transcript": "(A) She’s cleaning an oven.\n(B) She’s moving a pot.\n(C) She’s opening a cabinet.\n(D) She’s holding a towel.",
        "transcriptVi": "Người nói:\n(A) Cô ấy đang lau chùi lò nướng.\n(B) Cô ấy đang di chuyển một chiếc nồi.\n(C) Cô ấy đang mở ngăn tủ.\n(D) Cô ấy đang cầm một chiếc khăn.",
        "vocabulary": [
            {"word": "holding a towel", "ipa": "/ˈhəʊl.dɪŋ ə ˈtaʊ.əl/", "pos": "phr", "meaning": "cầm, giữ một chiếc khăn vải trên tay", "example": "The woman is holding a clean towel while standing in the kitchen."},
            {"word": "clean an oven", "ipa": "/kliːn ən ˈʌv.ən/", "pos": "phr", "meaning": "lau chùi, vệ sinh lò nướng", "example": "He used a sponge to clean an oven after preparing dinner."},
            {"word": "move a pot", "ipa": "/muːv ə pɒt/", "pos": "phr", "meaning": "di chuyển chiếc xoong/nồi nấu", "example": "Be careful when you move a hot pot from the stove."},
            {"word": "cabinet", "ipa": "/ˈkæb.ɪ.nət/", "pos": "n", "meaning": "ngăn tủ bếp, tủ kệ có cánh", "example": "Plates and cups are neatly stored inside the kitchen cabinet."}
        ],
        "collocations": [
            {"phrase": "hold a towel", "meaning": "cầm khăn trên tay"},
            {"phrase": "clean an oven", "meaning": "vệ sinh lò nướng"}
        ],
        "grammar": [
            {"title": "Thì hiện tại tiếp diễn chủ động", "rule": "S + is + V-ing", "content": "'She is holding a towel' diễn tả hành động đang diễn ra tại thời điểm chụp ảnh."}
        ]
    },
    2: {
        "id": 2,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test3/part1.mp3",
        "audioClip": "assets/audio/test3/cuts/q2.mp3",
        "audioLabel": "Nghe câu 2",
        "image": "assets/images/test3/q2.png",
        "questionText": "Look at the picture marked No. 2 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 2 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "They’re putting trash in a bag.",
            "B": "They’re taking off their jackets.",
            "C": "They’re facing a shelving unit.",
            "D": "They’re painting a room."
        },
        "optionsVi": {
            "A": "(A) Họ đang bỏ rác vào trong một chiếc túi.",
            "B": "(B) Họ đang cởi áo khoác.",
            "C": "(C) Họ đang đứng đối diện với một giá kệ.",
            "D": "(D) Họ đang sơn một căn phòng."
        },
        "correctAnswer": "C",
        "explanation": "Phương án (C) miêu tả chính xác hành động trong bức ảnh: Hai người đàn ông đang đứng quay mặt nhìn về phía chiếc kệ nhiều tầng trên tường ('They're facing a shelving unit').",
        "transcript": "(A) They’re putting trash in a bag.\n(B) They’re taking off their jackets.\n(C) They’re facing a shelving unit.\n(D) They’re painting a room.",
        "transcriptVi": "Người nói:\n(A) Họ đang bỏ rác vào trong một chiếc túi.\n(B) Họ đang cởi áo khoác.\n(C) Họ đang đứng đối diện với một giá kệ.\n(D) Họ đang sơn một căn phòng.",
        "vocabulary": [
            {"word": "facing a shelving unit", "ipa": "/ˈfeɪ.sɪŋ ə ˈʃel.vɪŋ ˈjuː.nɪt/", "pos": "phr", "meaning": "đứng đối diện, quay mặt về phía giá kệ để đồ", "example": "The workers are facing a shelving unit while inspecting stock."},
            {"word": "put trash in a bag", "ipa": "/pʊt træʃ ɪn ə bæɡ/", "pos": "phr", "meaning": "cho rác vào trong túi", "example": "Volunteers put plastic bottles and trash in a large trash bag."},
            {"word": "take off jackets", "ipa": "/teɪk ɒf ˈdʒæk.ɪts/", "pos": "phr", "meaning": "cởi áo khoác ngoài", "example": "Both men chose to take off their heavy jackets indoors."},
            {"word": "paint a room", "ipa": "/peɪnt ə ruːm/", "pos": "phr", "meaning": "sơn tường căn phòng", "example": "The tenants decided to paint a room before moving their furniture in."}
        ],
        "collocations": [
            {"phrase": "face a shelving unit", "meaning": "quay mặt về phía kệ sách/đồ"},
            {"phrase": "put trash in a bag", "meaning": "bỏ rác vào bao/túi"}
        ],
        "grammar": [
            {"title": "Động từ trạng thái / phương hướng 'face'", "rule": "S + are facing + Object", "content": "'facing' dùng để chỉ hướng nhìn hoặc hướng quay mặt của chủ thể về phía vật thể."}
        ]
    },
    3: {
        "id": 3,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test3/part1.mp3",
        "audioClip": "assets/audio/test3/cuts/q3.mp3",
        "audioLabel": "Nghe câu 3",
        "image": "assets/images/test3/q3.png",
        "questionText": "Look at the picture marked No. 3 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 3 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "One of the men is removing his hat.",
            "B": "A line of customers extends out a door.",
            "C": "Some workers are installing a sign.",
            "D": "Musicians have gathered in a circle."
        },
        "optionsVi": {
            "A": "(A) Một trong những người đàn ông đang cởi mũ của mình.",
            "B": "(B) Một hàng dài khách hàng kéo dài ra ngoài cửa.",
            "C": "(C) Một số công nhân đang lắp đặt một biển hiệu.",
            "D": "(D) Các nhạc sĩ đã tụ tập lại thành một vòng tròn."
        },
        "correctAnswer": "D",
        "explanation": "Phương án (D) miêu tả chính xác bức ảnh: Nhóm nhạc sĩ đang ngồi quây quần thành vòng tròn chơi đàn và ca hát ('Musicians have gathered in a circle').",
        "transcript": "(A) One of the men is removing his hat.\n(B) A line of customers extends out a door.\n(C) Some workers are installing a sign.\n(D) Musicians have gathered in a circle.",
        "transcriptVi": "Người nói:\n(A) Một trong những người đàn ông đang cởi mũ của mình.\n(B) Một hàng dài khách hàng kéo dài ra ngoài cửa.\n(C) Một số công nhân đang lắp đặt một biển hiệu.\n(D) Các nhạc sĩ đã tụ tập lại thành một vòng tròn.",
        "vocabulary": [
            {"word": "gather in a circle", "ipa": "/ˈɡæð.ər ɪn ə ˈsɜː.kəl/", "pos": "phr", "meaning": "tụ họp, quây quần thành một vòng tròn", "example": "Musicians have gathered in a circle to play traditional island melodies."},
            {"word": "musician", "ipa": "/mjuːˈzɪʃ.ən/", "pos": "n", "meaning": "nhạc sĩ, nghệ sĩ biểu diễn nhạc cụ", "example": "Local musicians performed outside the open-air pavilion."},
            {"word": "remove a hat", "ipa": "/rɪˈmuːv ə hæt/", "pos": "phr", "meaning": "tháo mũ, cởi mũ ra khỏi đầu", "example": "Gentlemen are requested to remove their hats inside the hall."},
            {"word": "install a sign", "ipa": "/ɪnˈstɔːl ə saɪn/", "pos": "phr", "meaning": "lắp đặt một tấm biển hiệu", "example": "Workers used power tools to install a sign above the entrance."}
        ],
        "collocations": [
            {"phrase": "gather in a circle", "meaning": "quây quần thành vòng tròn"},
            {"phrase": "line of customers", "meaning": "hàng dài khách hàng"}
        ],
        "grammar": [
            {"title": "Thì hiện tại hoàn thành miêu tả trạng thái tĩnh", "rule": "S + have/has + V3/ed", "content": "'Musicians have gathered in a circle' miêu tả kết quả của hành động đã hoàn tất và kết quả hiện hữu trong ảnh."}
        ]
    },
    4: {
        "id": 4,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test3/part1.mp3",
        "audioClip": "assets/audio/test3/cuts/q4.mp3",
        "audioLabel": "Nghe câu 4",
        "image": "assets/images/test3/q4.png",
        "questionText": "Look at the picture marked No. 4 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 4 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "Some tools have been left on a chair.",
            "B": "Some tool sets have been laid out.",
            "C": "A cup of coffee has spilled.",
            "D": "A table leg is being repaired."
        },
        "optionsVi": {
            "A": "(A) Một số dụng cụ được để lại trên ghế.",
            "B": "(B) Một số bộ dụng cụ đã được bày ra trên bàn.",
            "C": "(C) Một tách cà phê đã bị đổ tràn ra.",
            "D": "(D) Chân bàn đang được sửa chữa."
        },
        "correctAnswer": "B",
        "explanation": "Phương án (B) miêu tả chính xác trạng thái của các vật trên bàn: Các bộ đồ nghề sửa chữa đã được trải ra ngay ngắn trên mặt bàn gỗ ('Some tool sets have been laid out').",
        "transcript": "(A) Some tools have been left on a chair.\n(B) Some tool sets have been laid out.\n(C) A cup of coffee has spilled.\n(D) A table leg is being repaired.",
        "transcriptVi": "Người nói:\n(A) Một số dụng cụ được để lại trên ghế.\n(B) Một số bộ dụng cụ đã được bày ra trên bàn.\n(C) Một tách cà phê đã bị đổ tràn ra.\n(D) Chân bàn đang được sửa chữa.",
        "vocabulary": [
            {"word": "laid out", "ipa": "/leɪd aʊt/", "pos": "adj, phr v", "meaning": "được bày biện, trải ra ngăn nắp trên mặt bàn", "example": "Precision screwdrivers and tool sets have been laid out on the wooden desk."},
            {"word": "tool set", "ipa": "/tuːl set/", "pos": "n", "meaning": "bộ dụng cụ đồ nghề sửa chữa", "example": "The technician opened his portable tool set to service the laptop."},
            {"word": "cup of coffee", "ipa": "/kʌp əv ˈkɒf.i/", "pos": "n phr", "meaning": "ly cà phê, tách cà phê", "example": "A paper cup of coffee rests next to the electronic device."},
            {"word": "spilled", "ipa": "/spɪld/", "pos": "adj, v", "meaning": "bị đổ tràn ra ngoài", "example": "Fortunately, none of the hot liquid had spilled onto the keyboard."}
        ],
        "collocations": [
            {"phrase": "lay out tools", "meaning": "bày biện dụng cụ ra"},
            {"phrase": "spill coffee", "meaning": "làm đổ cà phê"}
        ],
        "grammar": [
            {"title": "Thể bị động hiện tại hoàn thành", "rule": "S + have/has been + V3/ed", "content": "'Some tool sets have been laid out' diễn tả trạng thái của đồ vật sau khi đã được ai đó sắp đặt."}
        ]
    },
    5: {
        "id": 5,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test3/part1.mp3",
        "audioClip": "assets/audio/test3/cuts/q5.mp3",
        "audioLabel": "Nghe câu 5",
        "image": "assets/images/test3/q5.png",
        "questionText": "Look at the picture marked No. 5 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 5 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "A railing is being removed.",
            "B": "A roof is under construction.",
            "C": "Some workers are carrying a ladder.",
            "D": "Some workers are holding sheets of metal."
        },
        "optionsVi": {
            "A": "(A) Một lan can đang bị tháo dỡ.",
            "B": "(B) Một mái nhà đang được thi công xây dựng.",
            "C": "(C) Một số công nhân đang khiêng một chiếc thang.",
            "D": "(D) Một số công nhân đang cầm các tấm kim loại."
        },
        "correctAnswer": "B",
        "explanation": "Phương án (B) miêu tả chính xác hoạt động xây dựng: Phần mái nhà của căn nhà gỗ đang trong quá trình được thi công lắp đặt ('A roof is under construction').",
        "transcript": "(A) A railing is being removed.\n(B) A roof is under construction.\n(C) Some workers are carrying a ladder.\n(D) Some workers are holding sheets of metal.",
        "transcriptVi": "Người nói:\n(A) Một lan can đang bị tháo dỡ.\n(B) Một mái nhà đang được thi công xây dựng.\n(C) Một số công nhân đang khiêng một chiếc thang.\n(D) Một số công nhân đang cầm các tấm kim loại.",
        "vocabulary": [
            {"word": "under construction", "ipa": "/ˈʌn.dər kənˈstrʌk.ʃən/", "pos": "phr", "meaning": "đang trong quá trình thi công xây dựng", "example": "The front roof of the log cabin is under construction this summer."},
            {"word": "railing", "ipa": "/ˈreɪ.lɪŋ/", "pos": "n", "meaning": "lan can rào chắn quanh hiên nhà", "example": "A wooden railing surrounds the outdoor balcony terrace."},
            {"word": "ladder", "ipa": "/ˈlæd.ər/", "pos": "n", "meaning": "chiếc thang chữ A gấp gọn", "example": "A metal stepladder is positioned beneath the roof beams."},
            {"word": "sheet of metal", "ipa": "/ʃiːt əv ˈmet.əl/", "pos": "n phr", "meaning": "tấm kim loại dùng lợp mái", "example": "Roofers installed corrugated sheets of metal to prevent leaks."}
        ],
        "collocations": [
            {"phrase": "under construction", "meaning": "đang thi công"},
            {"phrase": "carry a ladder", "meaning": "khiêng chiếc thang"}
        ],
        "grammar": [
            {"title": "Cụm giới từ chỉ trạng thái 'under + Noun'", "rule": "under construction / under repair", "content": "'under construction' đóng vai trò vị ngữ chỉ tình trạng đang được xây dựng."}
        ]
    },
    6: {
        "id": 6,
        "part": 1,
        "partName": "Part 1: Photographs",
        "audio": "assets/audio/test3/part1.mp3",
        "audioClip": "assets/audio/test3/cuts/q6.mp3",
        "audioLabel": "Nghe câu 6",
        "image": "assets/images/test3/q6.png",
        "questionText": "Look at the picture marked No. 6 in your test book and choose the best statement:",
        "questionTextVi": "Nhìn vào bức tranh số 6 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "A ladder has been leaned against a tree.",
            "B": "There are piles of tree branches discarded in a field.",
            "C": "Wooden benches have been arranged in a circle.",
            "D": "A wooden structure has been built near some trees."
        },
        "optionsVi": {
            "A": "(A) Một chiếc thang đã được dựng dựa vào thân cây.",
            "B": "(B) Có những đống cành cây bị vứt bỏ trên cánh đồng.",
            "C": "(C) Những chiếc ghế dài bằng gỗ đã được xếp thành vòng tròn.",
            "D": "(D) Một công trình bằng gỗ đã được dựng lên gần một số hàng cây."
        },
        "correctAnswer": "D",
        "explanation": "Phương án (D) miêu tả chính xác khung cảnh: Một cấu trúc chòi gỗ (khung nhà gỗ) được xây dựng ở khu vực gần các cây rừng ('A wooden structure has been built near some trees').",
        "transcript": "(A) A ladder has been leaned against a tree.\n(B) There are piles of tree branches discarded in a field.\n(C) Wooden benches have been arranged in a circle.\n(D) A wooden structure has been built near some trees.",
        "transcriptVi": "Người nói:\n(A) Một chiếc thang đã được dựng dựa vào thân cây.\n(B) Có những đống cành cây bị vứt bỏ trên cánh đồng.\n(C) Những chiếc ghế dài bằng gỗ đã được xếp thành vòng tròn.\n(D) Một công trình bằng gỗ đã được dựng lên gần một số hàng cây.",
        "vocabulary": [
            {"word": "wooden structure", "ipa": "/ˈwʊd.ən ˈstrʌk.tʃər/", "pos": "n phr", "meaning": "công trình, kết cấu dựng bằng gỗ", "example": "A rustic wooden structure has been built near some mature trees."},
            {"word": "leaned against", "ipa": "/liːnd əˈɡenst/", "pos": "phr v", "meaning": "được tựa vào, dựng dựa vào", "example": "A wooden beam was leaned against the frame during assembly."},
            {"word": "tree branches", "ipa": "/triː ˈbrɑːn.tʃɪz/", "pos": "n pl", "meaning": "các cành cây", "example": "Workers cleared fallen tree branches from the clearing."},
            {"word": "arranged in a circle", "ipa": "/əˈreɪndʒd ɪn ə ˈsɜː.kəl/", "pos": "phr", "meaning": "được sắp xếp thành hình tròn", "example": "Picnic benches were arranged in a circle around the campfire."}
        ],
        "collocations": [
            {"phrase": "wooden structure", "meaning": "công trình bằng gỗ"},
            {"phrase": "lean against a tree", "meaning": "dựa vào thân cây"}
        ],
        "grammar": [
            {"title": "Thể bị động thì Hiện tại hoàn thành với trạng từ nơi chốn", "rule": "S + has been built + near + Noun", "content": "Nhấn mạnh kết quả công trình kiến trúc đã được hoàn thành tại vị trí cố định."}
        ]
    }
}

# Apply to test3
for q in test3['questions']:
    qid = q['id']
    if qid in p1_updates:
        u = p1_updates[qid]
        for k, v in u.items():
            q[k] = v
        q['vocab'] = u['vocabulary']
        print(f"Updated Q{qid}: options A='{u['options']['A']}' correct='{u['correctAnswer']}'")

with open('web/data/test3.json', 'w', encoding='utf-8') as f:
    json.dump(test3, f, ensure_ascii=False, indent=2)

print("Saved updated web/data/test3.json successfully!")
