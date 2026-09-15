import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"

with open(os.path.join(BASE_DIR, "web", "data", "test3.json"), "r", encoding="utf-8") as f:
    t3_data = json.load(f)

questions = t3_data["questions"]
q_map = {q["id"]: q for q in questions}

# ==========================================
# 1. PART 1 (Q1 - Q6)
# ==========================================
p1_info = {
    1: {
        "stem": "Look at the picture marked No. 1 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 1 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "They’re putting trash in a bag.",
            "B": "They’re taking off their jackets.",
            "C": "They’re facing a shelving unit.",
            "D": "They’re painting a room."
        },
        "optionsVi": {
            "A": "Họ đang bỏ rác vào trong túi.",
            "B": "Họ đang cởi áo khoác ngoài.",
            "C": "Họ đang đối diện với một chiếc kệ để đồ.",
            "D": "Họ đang sơn một căn phòng."
        },
        "ans": "D",
        "exp": "Phương án (D) miêu tả chính xác hành động trong ảnh: Hai người đang dùng cây lăn sơn để sơn tường trong phòng ('They're painting a room').",
        "vocab": [
            {"word": "paint", "ipa": "/peɪnt/", "pos": "v", "meaning": "sơn, quét sơn", "example": "They are painting the living room."},
            {"word": "shelving unit", "ipa": "/ˈʃel.vɪŋ ˌjuː.nɪt/", "pos": "n", "meaning": "kệ để đồ, giá sách", "example": "assemble a wooden shelving unit"}
        ],
        "collocations": [{"phrase": "paint a room", "meaning": "sơn một căn phòng"}],
        "grammar": [{"title": "Thì hiện tại tiếp diễn chủ động", "content": "S + are + V-ing diễn tả hành động đang diễn ra của nhóm người trong tranh."}]
    },
    2: {
        "stem": "Look at the picture marked No. 2 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 2 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "She’s cleaning an oven.",
            "B": "She’s moving a pot.",
            "C": "She’s opening a cabinet.",
            "D": "She’s holding a towel."
        },
        "optionsVi": {
            "A": "Cô ấy đang lau chùi lò nướng.",
            "B": "Cô ấy đang di chuyển một chiếc nồi.",
            "C": "Cô ấy đang mở một ngăn tủ.",
            "D": "Cô ấy đang cầm một chiếc khăn lau."
        },
        "ans": "C",
        "exp": "Phương án (C) miêu tả chính xác hành động: Người phụ nữ trong bếp đang dùng tay mở cánh cửa ngăn tủ trên ('She's opening a cabinet').",
        "vocab": [
            {"word": "cabinet", "ipa": "/ˈkæb.ɪ.nət/", "pos": "n", "meaning": "tủ đựng đồ, tủ bếp", "example": "kitchen cabinet"},
            {"word": "oven", "ipa": "/ˈʌv.ən/", "pos": "n", "meaning": "lò nướng", "example": "preheat the oven"}
        ],
        "collocations": [{"phrase": "open a cabinet", "meaning": "mở ngăn tủ"}],
        "grammar": [{"title": "Thì hiện tại tiếp diễn với hành động tay", "content": "She is opening + N."}]
    },
    3: {
        "stem": "Look at the picture marked No. 3 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 3 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "A ladder has been leaned against a tree.",
            "B": "There are piles of tree branches discarded in a park.",
            "C": "Wooden benches have been arranged in a circle.",
            "D": "A wooden structure has been built near some trees."
        },
        "optionsVi": {
            "A": "Một chiếc thang được dựng tựa vào thân cây.",
            "B": "Có những đống cành cây bị vứt bỏ trong công viên.",
            "C": "Những chiếc ghế dài bằng gỗ được sắp xếp thành vòng tròn.",
            "D": "Một kiến trúc bằng gỗ đã được xây dựng gần một vài cái cây."
        },
        "ans": "D",
        "exp": "Phương án (D) miêu tả chính xác khung cảnh tĩnh ngoài trời: Một công trình/kiến trúc bằng gỗ (chòi/nhà gỗ) được dựng gần các hàng cây ('A wooden structure has been built near some trees').",
        "vocab": [
            {"word": "structure", "ipa": "/ˈstrʌk.tʃər/", "pos": "n", "meaning": "công trình, kiến trúc kết cấu", "example": "a wooden structure"},
            {"word": "lean against", "ipa": "/liːn əˈɡenst/", "pos": "phr v", "meaning": "dựa vào, tựa vào", "example": "A ladder leaned against the wall."}
        ],
        "collocations": [{"phrase": "wooden structure", "meaning": "công trình bằng gỗ"}, {"phrase": "near some trees", "meaning": "gần những hàng cây"}],
        "grammar": [{"title": "Bị động thì hiện tại hoàn thành (has been built)", "content": "Diễn tả công trình đã hoàn thành và đang hiện hữu trong bức ảnh."}]
    },
    4: {
        "stem": "Look at the picture marked No. 4 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 4 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "One of the men is removing his hat.",
            "B": "A line of customers extends out a door.",
            "C": "Some workers are installing a sign.",
            "D": "Musicians have gathered in a circle."
        },
        "optionsVi": {
            "A": "Một trong những người đàn ông đang cởi mũ của mình.",
            "B": "Một hàng dài khách hàng kéo dài ra ngoài cửa.",
            "C": "Một số công nhân đang lắp đặt một biển hiệu.",
            "D": "Các nhạc công đã tụ họp lại thành một vòng tròn."
        },
        "ans": "B",
        "exp": "Phương án (B) miêu tả chính xác khung cảnh: Rất đông khách hàng đang xếp hàng dài nối đuôi nhau ra tận phía ngoài cửa tiệm ('A line of customers extends out a door').",
        "vocab": [
            {"word": "extend", "ipa": "/ɪkˈstend/", "pos": "v", "meaning": "kéo dài, trải dài", "example": "The queue extended around the block."},
            {"word": "line of customers", "ipa": "/laɪn əv ˈkʌs.tə.məz/", "pos": "n", "meaning": "hàng người mua sắm/khách hàng", "example": "wait in a line of customers"}
        ],
        "collocations": [{"phrase": "extend out a door", "meaning": "kéo dài ra ngoài cửa"}],
        "grammar": [{"title": "Động từ nội động chỉ trạng thái kéo dài", "content": "'Extend' dùng ở thì hiện tại đơn mô tả trạng thái trải dài của một hàng người."}]
    },
    5: {
        "stem": "Look at the picture marked No. 5 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 5 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "A railing is being removed.",
            "B": "A roof is under construction.",
            "C": "Some workers are carrying a ladder.",
            "D": "Some workers are holding sheets of metal."
        },
        "optionsVi": {
            "A": "Một thanh lan can đang bị dỡ bỏ.",
            "B": "Một mái nhà đang trong quá trình xây dựng.",
            "C": "Một số công nhân đang khiêng một chiếc thang.",
            "D": "Một số công nhân đang cầm các tấm kim loại."
        },
        "ans": "B",
        "exp": "Phương án (B) miêu tả chính xác công trường xây dựng: Phần mái nhà của công trình đang được thi công lợp mái ('A roof is under construction').",
        "vocab": [
            {"word": "under construction", "ipa": "/ˈʌn.dər kənˈstrʌk.ʃən/", "pos": "prep phr", "meaning": "đang được xây dựng/thi công", "example": "The new bridge is currently under construction."},
            {"word": "railing", "ipa": "/ˈreɪ.lɪŋ/", "pos": "n", "meaning": "lan can, rào chắn", "example": "hold onto the railing"}
        ],
        "collocations": [{"phrase": "under construction", "meaning": "đang trong quá trình thi công/xây dựng"}],
        "grammar": [{"title": "Cụm giới từ chỉ trạng thái (under + Noun)", "content": "'Under construction' mang nghĩa đang được xây dựng."}]
    },
    6: {
        "stem": "Look at the picture marked No. 6 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 6 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "Some tools have been left on a chair.",
            "B": "Some tool sets have been laid out.",
            "C": "A cup of coffee has spilled.",
            "D": "A table leg is being repaired."
        },
        "optionsVi": {
            "A": "Một số công cụ đã bị để lại trên một chiếc ghế.",
            "B": "Một số bộ công cụ đã được bày ra.",
            "C": "Một tách cà phê đã bị đổ tràn ra.",
            "D": "Một chân bàn đang được sửa chữa."
        },
        "ans": "D",
        "exp": "Phương án (D) miêu tả chính xác hành động: Người trong tranh đang dùng dụng cụ để siết ốc hoặc sửa chân chiếc bàn ('A table leg is being repaired').",
        "vocab": [
            {"word": "repair", "ipa": "/rɪˈpeər/", "pos": "v", "meaning": "sửa chữa", "example": "repair damaged furniture"},
            {"word": "tool set", "ipa": "/tuːl set/", "pos": "n", "meaning": "bộ dụng cụ đồ nghề", "example": "a complete mechanic's tool set"}
        ],
        "collocations": [{"phrase": "table leg", "meaning": "chân bàn"}],
        "grammar": [{"title": "Bị động hiện tại tiếp diễn (is/are being + V3/ed)", "content": "'is being repaired' nhấn mạnh hành động sửa chữa đang trực tiếp diễn ra."}]
    }
}

for qid, info in p1_info.items():
    q = q_map[qid]
    q["part"] = 1
    q["partName"] = "Part 1: Photographs"
    q["image"] = f"assets/images/test3/q{qid}.png"
    q["audio"] = "assets/audio/test3/part1.mp3"
    q["audioClip"] = f"assets/audio/test3/cuts/q{qid}.mp3"
    q["audioLabel"] = f"Nghe câu {qid}"
    q["questionText"] = info["stem"]
    q["questionTextVi"] = info["stemVi"]
    q["options"] = info["options"]
    q["optionsVi"] = info["optionsVi"]
    q["correctAnswer"] = info["ans"]
    q["explanation"] = info["exp"]
    q["transcript"] = "\n".join([f"({k}) {info['options'][k]}" for k in sorted(info['options'].keys())])
    q["transcriptVi"] = f"Đáp án chính xác: ({info['ans']})."
    q["vocabulary"] = info["vocab"]
    q["collocations"] = info["collocations"]
    q["grammar"] = info["grammar"]

print("Part 1 perfected!")

# ==========================================
# 2. PART 2 (Q7 - Q31)
# ==========================================
p2_clean_data = {
    7: {
        "text": "Why is there no flour on the shelf?",
        "options": {"A": "Because it's out of stock.", "B": "Those roses smell nice.", "C": "No, the other cake."},
        "ans": "A"
    },
    8: {
        "text": "When will the catering company arrive?",
        "options": {"A": "At four o'clock.", "B": "That's a delicious flavor.", "C": "Many vegetarian options."},
        "ans": "A"
    },
    9: {
        "text": "When's the meeting scheduled to start?",
        "options": {"A": "At a networking event.", "B": "I started this job six years ago.", "C": "Right after lunch."},
        "ans": "C"
    },
    10: {
        "text": "How much will the repairs cost?",
        "options": {"A": "I have two pairs of shoes.", "B": "Around 200 dollars.", "C": "The restaurant downtown."},
        "ans": "B"
    },
    11: {
        "text": "You went to the dentist this morning, didn't you?",
        "options": {"A": "Oh, I've already had breakfast.", "B": "Yes, for an annual checkup.", "C": "Let's take the bus."},
        "ans": "B"
    },
    12: {
        "text": "Where should we put the new printer?",
        "options": {"A": "In the corner by the stairs.", "B": "The third page of the document.", "C": "A reusable ink cartridge."},
        "ans": "A"
    },
    13: {
        "text": "What type of plant do you have in your office?",
        "options": {"A": "Whenever I sit at my desk.", "B": "Thanks—I just bought it.", "C": "One that doesn't require much water."},
        "ans": "C"
    },
    14: {
        "text": "There was a sale at the furniture store.",
        "options": {"A": "To the convention center.", "B": "Did you buy anything?", "C": "A new employee."},
        "ans": "B"
    },
    15: {
        "text": "Can you show me how to submit a tech help ticket?",
        "options": {"A": "Let me send you the link.", "B": "The machine is broken.", "C": "A twenty-dollar ticket."},
        "ans": "A"
    },
    16: {
        "text": "Where is the power button on this device?",
        "options": {"A": "I've never used that model before.", "B": "Ten euros per hour.", "C": "Yes, turn it to the right."},
        "ans": "A"
    },
    17: {
        "text": "Do you want to take a walk now, or would later be better?",
        "options": {"A": "A nearby lake.", "B": "I'm free to walk now.", "C": "She walked there yesterday."},
        "ans": "B"
    },
    18: {
        "text": "I ordered some new equipment for the factory.",
        "options": {"A": "The news program on Channel Ten.", "B": "Great—I can't wait to use it.", "C": "The car dealership."},
        "ans": "B"
    },
    19: {
        "text": "There's a nice place to rent on Mercer Street.",
        "options": {"A": "How many bedrooms does it have?", "B": "The rent is due on the first.", "C": "Yes, he's very nice."},
        "ans": "A"
    },
    20: {
        "text": "Is the heating system working?",
        "options": {"A": "Yes, that's my Web site.", "B": "A five-kilometer run.", "C": "Yes, the office is warm."},
        "ans": "C"
    },
    21: {
        "text": "Isn't the roadwork in front of city hall finished yet?",
        "options": {"A": "I just finished my conference presentation.", "B": "A lot of traffic in the evening.", "C": "No, they still have another month to go."},
        "ans": "C"
    },
    22: {
        "text": "Who will lead the new employee training today?",
        "options": {"A": "We're using a recorded video.", "B": "Yes, right after lunch.", "C": "Classroom 124."},
        "ans": "A"
    },
    23: {
        "text": "Is the safety inspection scheduled for this month or next month?",
        "options": {"A": "I thought I saved the file.", "B": "The factory supervisor.", "C": "It's this Wednesday."},
        "ans": "C"
    },
    24: {
        "text": "When is the harvest festival taking place?",
        "options": {"A": "Sometime in October.", "B": "At the community center.", "C": "Fresh fruits and vegetables."},
        "ans": "A"
    },
    25: {
        "text": "Was your new laptop expensive?",
        "options": {"A": "Do you have a new password?", "B": "I had a discount coupon.", "C": "Yes, it's very fast."},
        "ans": "B"
    },
    26: {
        "text": "Why don't we go on our camping trip next weekend?",
        "options": {"A": "Yes, that table lamp is quite nice.", "B": "Should we go left or right?", "C": "That works for me."},
        "ans": "C"
    },
    27: {
        "text": "The workshop for this afternoon was postponed, wasn't it?",
        "options": {"A": "At the post office.", "B": "Yes, until next Monday.", "C": "About thirty people attended."},
        "ans": "B"
    },
    28: {
        "text": "How were our production figures last month?",
        "options": {"A": "They produce electric cars.", "B": "Nine o'clock in the morning.", "C": "We were closed down for a week."},
        "ans": "C"
    },
    29: {
        "text": "When can I see the speech therapist?",
        "options": {"A": "Yes, I heard the speech.", "B": "On the third floor.", "C": "She has an opening tomorrow morning."},
        "ans": "C"
    },
    30: {
        "text": "Aren't you picking up the clients from the airport?",
        "options": {"A": "A product demonstration.", "B": "No, I believe Tomoko is doing that.", "C": "He prefers an aisle seat."},
        "ans": "B"
    },
    31: {
        "text": "How was your morning client meeting?",
        "options": {"A": "It's great to meet you.", "B": "No, over in conference room two.", "C": "The contract is now officially signed."},
        "ans": "C"
    }
}

for qid, p2info in p2_clean_data.items():
    q = q_map[qid]
    q["part"] = 2
    q["partName"] = "Part 2: Question-Response"
    q["audio"] = "assets/audio/test3/part2.mp3"
    q["audioClip"] = f"assets/audio/test3/cuts/q{qid}.mp3"
    q["audioLabel"] = f"Nghe câu {qid}"
    q["questionText"] = p2info["text"]
    q["options"] = p2info["options"]
    q["correctAnswer"] = p2info["ans"]
    q["transcript"] = f"Speaker: {p2info['text']}\n" + "\n".join([f"({k}) {p2info['options'][k]}" for k in sorted(p2info['options'].keys())])
    q["explanation"] = f"Phương án ({p2info['ans']}) là câu trả lời phù hợp và hợp lý nhất cho câu hỏi/phát biểu '{p2info['text']}'."

print("Part 2 perfected!")

# ==========================================
# 3. PART 4 FIX (Q97)
# ==========================================
if 97 in q_map:
    q_map[97]["questionText"] = "How can a change be confirmed?"
    q_map[97]["options"] = {
        "A": "By sending an e-mail",
        "B": "By providing an e-signature",
        "C": "By using an app",
        "D": "By returning a call"
    }
    q_map[97]["correctAnswer"] = "C"
    q_map[97]["explanation"] = "Người nói yêu cầu: 'Please let me know if you agree with this change by responding to the prompt within the app' (Vui lòng cho tôi biết bạn có đồng ý thay đổi này không bằng cách phản hồi lời nhắc trong ứng dụng) -> Đáp án chính xác là (C) By using an app."
    print("Q97 fixed!")

# ==========================================
# 4. PART 5 (Q101 - Q130) REBUILD
# ==========================================
p5_clean_data = {
    101: {
        "stem": "------- your order is being processed, please call customer service with any questions.",
        "stemVi": "------- đơn đặt hàng của bạn đang được xử lý, vui lòng gọi cho bộ phận chăm sóc khách hàng nếu có bất kỳ thắc mắc nào.",
        "options": {"A": "Still", "B": "Either", "C": "While", "D": "Also"},
        "optionsVi": {"A": "vẫn", "B": "hoặc", "C": "Trong khi", "D": "cũng"},
        "ans": "C",
        "exp": "Đứng đầu mệnh đề trạng ngữ chỉ thời gian diễn tả hai hành động diễn ra song song: 'While your order is being processed,...' (Trong khi đơn hàng đang được xử lý) -> chọn liên từ 'While'.",
        "vocab": [{"word": "process", "ipa": "/ˈprəʊ.ses/", "pos": "v", "meaning": "xử lý (đơn hàng/hồ sơ)", "example": "process an order"}],
        "collocations": [{"phrase": "customer service", "meaning": "dịch vụ chăm sóc khách hàng"}],
        "grammar": [{"title": "Liên từ chỉ thời gian (While + Clause)", "content": "'While' nối mệnh đề phụ chỉ thời gian với mệnh đề chính."}]
    },
    102: {
        "stem": "ABC Truck Supplies has the ------- selection of mufflers in the state.",
        "stemVi": "ABC Truck Supplies có sự lựa chọn các ống giảm thanh ------- nhất trong toàn bang.",
        "options": {"A": "natural", "B": "widest", "C": "overall", "D": "positive"},
        "optionsVi": {"A": "tự nhiên", "B": "đa dạng/rộng nhất", "C": "tổng thể", "D": "tích cực"},
        "ans": "B",
        "exp": "Trước danh từ 'selection' có mạo từ 'the' chỉ so sánh nhất: 'the widest selection' (sự lựa chọn đa dạng/phong phú nhất) là collocation chuẩn -> chọn 'widest'.",
        "vocab": [{"word": "muffler", "ipa": "/ˈmʌf.lər/", "pos": "n", "meaning": "ống giảm thanh (xe cộ)", "example": "truck mufflers"}],
        "collocations": [{"phrase": "widest selection", "meaning": "sự lựa chọn phong phú nhất"}],
        "grammar": [{"title": "So sánh nhất của tính từ (The + superlative + Noun)", "content": "The widest selection of something."}]
    },
    103: {
        "stem": "Sharswood Landscaping has received dozens of five-star ------- for its work.",
        "stemVi": "Công ty Cảnh quan Sharswood đã nhận được hàng tá các ------- năm sao cho các công trình của mình.",
        "options": {"A": "reviews", "B": "reviewer", "C": "reviewed", "D": "reviewing"},
        "optionsVi": {"A": "đánh giá (n-số nhiều)", "B": "người đánh giá (n)", "C": "đã xem xét", "D": "việc đánh giá"},
        "ans": "A",
        "exp": "Sau cụm từ chỉ số lượng 'dozens of' và tính từ 'five-star' cần một danh từ đếm được số nhiều: 'five-star reviews' (những đánh giá năm sao) -> chọn 'reviews'.",
        "vocab": [{"word": "landscaping", "ipa": "/ˈlænd.skeɪ.pɪŋ/", "pos": "n", "meaning": "nghề thiết kế cảnh quan", "example": "commercial landscaping services"}],
        "collocations": [{"phrase": "five-star reviews", "meaning": "những đánh giá xếp hạng 5 sao"}],
        "grammar": [{"title": "Danh từ đếm được số nhiều sau dozens of", "content": "Dozens of + N(plural): hàng chục, hàng tá cái gì."}]
    },
    104: {
        "stem": "Dr. Cho will visit the Teledarr Lab during the annual open house, since ------- may not have another chance to see it.",
        "stemVi": "Tiến sĩ Cho sẽ đến thăm Phòng thí nghiệm Teledarr trong ngày mở cửa thường niên, vì ------- có thể không có cơ hội khác để tham quan nơi này.",
        "options": {"A": "hers", "B": "she", "C": "her", "D": "herself"},
        "optionsVi": {"A": "của cô ấy (đại từ sở hữu)", "B": "cô ấy (đại từ chủ ngữ)", "C": "cô ấy (tân ngữ/tính từ sở hữu)", "D": "chính cô ấy (phản thân)"},
        "ans": "B",
        "exp": "Mệnh đề sau liên từ 'since' cần một đại từ nhân xưng làm chủ ngữ cho vị ngữ 'may not have' -> chọn đại từ chủ ngữ 'she'.",
        "vocab": [{"word": "open house", "ipa": "/ˌəʊ.pən ˈhaʊs/", "pos": "n", "meaning": "ngày hội mở cửa cho khách vào tham quan", "example": "annual open house"}],
        "collocations": [{"phrase": "annual open house", "meaning": "ngày hội mở cửa thường niên"}],
        "grammar": [{"title": "Đại từ nhân xưng làm chủ ngữ", "content": "Vị trí trước modal verb 'may' cần đại từ chủ ngữ (she)."}]
    },
    105: {
        "stem": "Dorn Department Store decided to ------- its already large selection of housewares.",
        "stemVi": "Cửa hàng bách hóa Dorn đã quyết định ------- bộ sưu tập đồ gia dụng vốn đã rất lớn của mình.",
        "options": {"A": "create", "B": "enforce", "C": "apply", "D": "expand"},
        "optionsVi": {"A": "tạo ra", "B": "thực thi", "C": "áp dụng", "D": "mở rộng"},
        "ans": "D",
        "exp": "Sau 'decided to' cần một động từ nguyên mẫu mang nghĩa mở rộng thêm danh mục mặt hàng sẵn có: 'expand its selection' (mở rộng chủng loại hàng) -> chọn 'expand'.",
        "vocab": [{"word": "housewares", "ipa": "/ˈhaʊs.weəz/", "pos": "n", "meaning": "đồ dùng gia đình/đồ gia dụng", "example": "kitchen housewares"}],
        "collocations": [{"phrase": "expand a selection", "meaning": "mở rộng danh mục/chủng loại hàng hóa"}],
        "grammar": [{"title": "Cấu trúc decide + to-V", "content": "Quyết định thực hiện một hành động cụ thể."}]
    },
    106: {
        "stem": "We ------- that you bring a portfolio of work samples to the interview.",
        "stemVi": "Chúng tôi ------- bạn mang theo một bộ hồ sơ năng lực gồm các sản phẩm mẫu tới buổi phỏng vấn.",
        "options": {"A": "was asking", "B": "having asked", "C": "ask", "D": "asks"},
        "optionsVi": {"A": "đã đang yêu cầu (sai hòa hợp số ít)", "B": "đã yêu cầu (phân từ)", "C": "yêu cầu (ngôi We)", "D": "yêu cầu (ngôi số ít)"},
        "ans": "C",
        "exp": "Chủ ngữ là 'We' (ngôi thứ nhất số nhiều) ở thì hiện tại đơn cần động từ nguyên mẫu 'ask'. Cấu trúc giả định thức: 'ask that S + V-bare (bring)' -> chọn 'ask'.",
        "vocab": [{"word": "portfolio", "ipa": "/pɔːtˈfəʊ.li.əʊ/", "pos": "n", "meaning": "hồ sơ năng lực, tập tác phẩm", "example": "design portfolio"}],
        "collocations": [{"phrase": "portfolio of work samples", "meaning": "bộ hồ sơ mẫu tác phẩm công việc"}],
        "grammar": [{"title": "Cấu trúc giả định thức (Subjunctive Mood)", "content": "Ask that + S + (should) + V-bare: yêu cầu rằng ai đó làm gì."}]
    },
    107: {
        "stem": "Members of the Bold Stone Farm Store receive ------- discounts on all purchases.",
        "stemVi": "Hội viên của Cửa hàng Nông trại Bold Stone nhận được các mức giảm giá ------- trên mọi hóa đơn mua hàng.",
        "options": {"A": "depth", "B": "deepen", "C": "deep", "D": "deeply"},
        "optionsVi": {"A": "độ sâu (n)", "B": "làm sâu thêm (v)", "C": "sâu, lớn (adj)", "D": "một cách sâu sắc (adv)"},
        "ans": "C",
        "exp": "Trước danh từ số nhiều 'discounts' cần một tính từ bổ nghĩa. 'Deep discounts' là collocation chỉ mức giảm giá sâu/giảm giá mạnh -> chọn tính từ 'deep'.",
        "vocab": [{"word": "purchase", "ipa": "/ˈpɜː.tʃəs/", "pos": "n", "meaning": "món hàng đã mua, sự mua hàng", "example": "discounts on purchases"}],
        "collocations": [{"phrase": "deep discounts", "meaning": "giảm giá sâu/mạnh"}],
        "grammar": [{"title": "Tính từ bổ nghĩa cho danh từ (Adj + Noun)", "content": "Deep (adj) bổ nghĩa cho danh từ 'discounts'."}]
    },
    108: {
        "stem": "If your plans change, please contact us at least 24 hours before the time of your -------.",
        "stemVi": "Nếu kế hoạch của bạn thay đổi, vui lòng liên hệ với chúng tôi ít nhất 24 giờ trước thời điểm ------- của bạn.",
        "options": {"A": "reserved", "B": "reservation", "C": "reservable", "D": "reserve"},
        "optionsVi": {"A": "đã đặt (adj/v-ed)", "B": "sự đặt chỗ (n)", "C": "có thể đặt", "D": "đặt chỗ (v)"},
        "ans": "B",
        "exp": "Sau tính từ sở hữu 'your' cần một danh từ: 'your reservation' (việc đặt chỗ trước của bạn) -> chọn danh từ 'reservation'.",
        "vocab": [{"word": "reservation", "ipa": "/ˌrez.əˈveɪ.ʃən/", "pos": "n", "meaning": "sự đặt chỗ trước", "example": "make a hotel reservation"}],
        "collocations": [{"phrase": "time of your reservation", "meaning": "thời điểm đặt chỗ của bạn"}],
        "grammar": [{"title": "Tính từ sở hữu + Danh từ", "content": "Your + Noun (reservation)."}]
    },
    109: {
        "stem": "Hold the tomato seedling gently by the stem in order to avoid harming ------- roots.",
        "stemVi": "Hãy giữ cây cà chua giống một cách nhẹ nhàng ở phần thân để tránh làm tổn hại tới rễ của -------.",
        "options": {"A": "its", "B": "them", "C": "that", "D": "in"},
        "optionsVi": {"A": "của nó (tính từ sở hữu)", "B": "chúng (tân ngữ)", "C": "đó", "D": "trong"},
        "ans": "A",
        "exp": "Đứng trước danh từ số nhiều 'roots' cần một tính từ sở hữu để thay thế cho 'the tomato seedling' (danh từ số ít chỉ thực vật) -> chọn 'its'.",
        "vocab": [{"word": "seedling", "ipa": "/ˈsiːd.lɪŋ/", "pos": "n", "meaning": "cây con, cây giống", "example": "tomato seedling"},
                  {"word": "stem", "ipa": "/stem/", "pos": "n", "meaning": "thân cây", "example": "hold by the stem"}],
        "collocations": [{"phrase": "avoid harming", "meaning": "tránh làm tổn hại"}],
        "grammar": [{"title": "Tính từ sở hữu (Possessive Adjective)", "content": "'Its' chỉ sở hữu của danh từ số ít 'seedling'."}]
    },
    110: {
        "stem": "At the registration table, be sure to collect your name tag ------- entering the conference.",
        "stemVi": "Tại bàn đăng ký, hãy nhớ lấy thẻ tên của bạn ------- khi bước vào hội nghị.",
        "options": {"A": "very", "B": "often", "C": "always", "D": "before"},
        "optionsVi": {"A": "rất", "B": "thường xuyên", "C": "luôn luôn", "D": "trước khi"},
        "ans": "D",
        "exp": "Sau chỗ trống là danh động từ 'entering the conference', cần một giới từ chỉ thời gian: 'before entering...' (trước khi vào...) -> chọn 'before'.",
        "vocab": [{"word": "name tag", "ipa": "/ˈneɪm tæɡ/", "pos": "n", "meaning": "thẻ ghi tên", "example": "wear a name tag"}],
        "collocations": [{"phrase": "before entering", "meaning": "trước khi bước vào"}],
        "grammar": [{"title": "Giới từ theo sau bởi V-ing (Preposition + Gerund)", "content": "Before + V-ing chỉ trình tự thời gian xảy ra trước."}]
    },
    111: {
        "stem": "Maihama vehicles include an extended ------- to cover engine repairs.",
        "stemVi": "Các dòng xe Maihama bao gồm một gói ------- mở rộng để chi trả cho việc sửa chữa động cơ.",
        "options": {"A": "record", "B": "operation", "C": "budget", "D": "warranty"},
        "optionsVi": {"A": "hồ sơ", "B": "sự vận hành", "C": "ngân sách", "D": "sự bảo hành"},
        "ans": "D",
        "exp": "Cụm danh từ 'extended warranty' nghĩa là gói bảo hành mở rộng (chi trả cho việc sửa chữa động cơ xe) -> chọn 'warranty'.",
        "vocab": [{"word": "warranty", "ipa": "/ˈwɒr.ən.ti/", "pos": "n", "meaning": "giấy bảo hành, sự bảo hành", "example": "under warranty"}],
        "collocations": [{"phrase": "extended warranty", "meaning": "bảo hành mở rộng"}],
        "grammar": [{"title": "Cụm danh từ ghép trong thương mại", "content": "Extended (adj) + warranty (n): gói bảo hành gia hạn."}]
    },
    112: {
        "stem": "The hotel's new Web site features an ------- collection of high-quality images.",
        "stemVi": "Trang web mới của khách sạn sở hữu một bộ sưu tập hình ảnh chất lượng cao đầy -------.",
        "options": {"A": "absolute", "B": "efficient", "C": "impressive", "D": "undefeated"},
        "optionsVi": {"A": "tuyệt đối", "B": "hiệu quả", "C": "ấn tượng", "D": "bất bại"},
        "ans": "C",
        "exp": "Sau mạo từ 'an' và trước danh từ 'collection' cần một tính từ bắt đầu bằng nguyên âm: 'an impressive collection' (một bộ sưu tập ấn tượng) -> chọn 'impressive'.",
        "vocab": [{"word": "impressive", "ipa": "/ɪmˈpres.ɪv/", "pos": "adj", "meaning": "ấn tượng, sâu sắc", "example": "an impressive performance"}],
        "collocations": [{"phrase": "impressive collection", "meaning": "bộ sưu tập đầy ấn tượng"}],
        "grammar": [{"title": "Mạo từ 'an' đi với tính từ bắt đầu bằng nguyên âm", "content": "An impressive + noun."}]
    },
    113: {
        "stem": "On behalf of everyone at Uniontown Bank, we ------- thank you for your continued patronage.",
        "stemVi": "Thay mặt cho toàn thể mọi người tại Ngân hàng Uniontown, chúng tôi ------- cảm ơn quý khách vì sự gắn bó ủng hộ liên tục.",
        "options": {"A": "deservedly", "B": "commonly", "C": "sincerely", "D": "perfectly"},
        "optionsVi": {"A": "xứng đáng", "B": "thông thường", "C": "chân thành", "D": "hoàn hảo"},
        "ans": "C",
        "exp": "Cụm 'sincerely thank you' (chân thành cảm ơn bạn) là trạng từ chuẩn mực để bày tỏ sự tri ân trong giao tiếp kinh doanh -> chọn 'sincerely'.",
        "vocab": [{"word": "patronage", "ipa": "/ˈpæt.rə.nɪdʒ/", "pos": "n", "meaning": "sự lui tới mua hàng, sự ủng hộ của khách quen", "example": "thank you for your patronage"}],
        "collocations": [{"phrase": "sincerely thank", "meaning": "chân thành cảm ơn"}, {"phrase": "on behalf of", "meaning": "thay mặt cho"}],
        "grammar": [{"title": "Trạng từ bổ nghĩa cho động từ (Adverb modifying Verb)", "content": "'Sincerely' đứng trước động từ 'thank' để nhấn mạnh mức độ chân thành."}]
    },
    114: {
        "stem": "Fragile equipment must be stored in a secure location so that nothing is ------- damaged.",
        "stemVi": "Thiết bị dễ vỡ phải được cất giữ ở một vị trí an toàn để không có thứ gì bị hư hỏng một cách -------.",
        "options": {"A": "accident", "B": "accidents", "C": "accidental", "D": "accidentally"},
        "optionsVi": {"A": "tai nạn (n)", "B": "tai nạn (n-số nhiều)", "C": "tình cờ, ngẫu nhiên (adj)", "D": "vô tình, do sơ suất (adv)"},
        "ans": "D",
        "exp": "Đứng giữa to be 'is' và quá khứ phân từ 'damaged' cần một trạng từ để bổ nghĩa cho động từ bị động: 'accidentally damaged' (bị làm hỏng do vô tình/sơ suất) -> chọn trạng từ 'accidentally'.",
        "vocab": [{"word": "fragile", "ipa": "/ˈfrædʒ.aɪl/", "pos": "adj", "meaning": "dễ vỡ, mỏng manh", "example": "fragile glassware"}],
        "collocations": [{"phrase": "accidentally damaged", "meaning": "vô tình bị làm hỏng"}],
        "grammar": [{"title": "Vị trí của trạng từ trong câu bị động (Be + adv + V3/ed)", "content": "Trạng từ đứng giữa trợ động từ và động từ chính."}]
    },
    115: {
        "stem": "Ms. Sampson will not arrive at the convention ------- after our team's presentation.",
        "stemVi": "Bà Sampson sẽ không đến hội nghị cho ------- sau bài thuyết trình của nhóm chúng ta.",
        "options": {"A": "until", "B": "lately", "C": "from", "D": "when"},
        "optionsVi": {"A": "cho tới khi", "B": "gần đây", "C": "từ", "D": "khi"},
        "ans": "A",
        "exp": "Cấu trúc phủ định với thời gian: 'not ... until' (không làm gì cho tới tận khi...) -> chọn 'until'.",
        "vocab": [{"word": "convention", "ipa": "/kənˈven.ʃən/", "pos": "n", "meaning": "hội nghị, đại hội", "example": "annual convention"}],
        "collocations": [{"phrase": "not until", "meaning": "mãi cho tới tận khi"}],
        "grammar": [{"title": "Cấu trúc Not ... until", "content": "Nhấn mạnh mốc thời gian sự việc bắt đầu diễn ra."}]
    },
    116: {
        "stem": "The community picnic will be held ------- the park behind the Seltzer Public Library.",
        "stemVi": "Buổi dã ngoại cộng đồng sẽ được tổ chức ------- công viên phía sau Thư viện Công cộng Seltzer.",
        "options": {"A": "in", "B": "all", "C": "for", "D": "here"},
        "optionsVi": {"A": "trong, tại", "B": "tất cả", "C": "cho", "D": "ở đây"},
        "ans": "A",
        "exp": "Giới từ chỉ địa điểm trong một không gian mở như công viên: 'in the park' (ở trong công viên) -> chọn 'in'.",
        "vocab": [{"word": "picnic", "ipa": "/ˈpɪk.nɪk/", "pos": "n", "meaning": "buổi dã ngoại", "example": "community picnic"}],
        "collocations": [{"phrase": "held in the park", "meaning": "được tổ chức tại công viên"}],
        "grammar": [{"title": "Giới từ chỉ nơi chốn (Preposition of Place: In)", "content": "In + park/garden/area: ở trong khu vực công viên."}]
    },
    117: {
        "stem": "The new hires ------- for an orientation on May 10 at 9:00 A.M.",
        "stemVi": "Các nhân viên mới tuyển dụng ------- để tham gia buổi định hướng vào ngày 10 tháng 5 lúc 9 giờ sáng.",
        "options": {"A": "to be gathering", "B": "will gather", "C": "gathering", "D": "to gather"},
        "optionsVi": {"A": "đang tụ họp", "B": "sẽ tập trung", "C": "việc tập trung", "D": "để tập trung"},
        "ans": "B",
        "exp": "Câu chưa có động từ vị ngữ chính. Với mốc thời gian trong tương lai (May 10), ta cần động từ chia thì tương lai đơn 'will gather' -> chọn (B).",
        "vocab": [{"word": "orientation", "ipa": "/ˌɔː.ri.enˈteɪ.ʃən/", "pos": "n", "meaning": "buổi định hướng, tập huấn nhập môn", "example": "employee orientation"}],
        "collocations": [{"phrase": "gather for an orientation", "meaning": "tập trung cho buổi định hướng"}],
        "grammar": [{"title": "Thì tương lai đơn diễn tả sự kiện đã lên lịch (Future Simple: will + V)", "content": "Đóng vai trò động từ vị ngữ chính của câu."}]
    },
    118: {
        "stem": "When Mr. Young approached the desk, the receptionist ------- offered him a seat in the waiting room.",
        "stemVi": "Khi ông Young tiến đến gần quầy, nhân viên lễ tân đã ------- mời ông ấy một chỗ ngồi trong phòng chờ.",
        "options": {"A": "politely", "B": "polite", "C": "politeness", "D": "politest"},
        "optionsVi": {"A": "một cách lịch sự (adv)", "B": "lịch sự (adj)", "C": "sự lịch sự (n)", "D": "lịch sự nhất"},
        "ans": "A",
        "exp": "Đứng trước động từ 'offered' cần một trạng từ để bổ nghĩa cách thức thực hiện hành động: 'politely offered' (lịch sự mời) -> chọn trạng từ 'politely'.",
        "vocab": [{"word": "receptionist", "ipa": "/rɪˈsep.ʃən.ɪst/", "pos": "n", "meaning": "nhân viên lễ tân", "example": "the hotel receptionist"}],
        "collocations": [{"phrase": "politely offer", "meaning": "lịch sự đề nghị/mời"}],
        "grammar": [{"title": "Trạng từ chỉ thể cách (Adverb of Manner)", "content": "Đứng trước động từ chính để mô tả thái độ lịch thiệp."}]
    },
    119: {
        "stem": "Members of the Marvale marketing team claimed that ------- was the best design for the new corporate logo.",
        "stemVi": "Các thành viên của đội tiếp thị Marvale khẳng định rằng thiết kế của ------- là thiết kế đẹp nhất cho logo mới của tập đoàn.",
        "options": {"A": "they", "B": "them", "C": "theirs", "D": "their"},
        "optionsVi": {"A": "họ (chủ ngữ)", "B": "họ (tân ngữ)", "C": "cái của họ (đại từ sở hữu)", "D": "của họ (tính từ sở hữu)"},
        "ans": "C",
        "exp": "Chủ ngữ của mệnh đề phụ đứng trước động từ 'was' mang nghĩa 'thiết kế của họ' (their design). Đại từ sở hữu 'theirs' = their design đóng vai trò làm chủ ngữ độc lập -> chọn 'theirs'.",
        "vocab": [{"word": "corporate logo", "ipa": "/ˈkɔː.pər.ət ˈləʊ.ɡəʊ/", "pos": "n", "meaning": "biểu trưng/logo doanh nghiệp", "example": "redesign the corporate logo"}],
        "collocations": [{"phrase": "corporate logo", "meaning": "logo doanh nghiệp"}],
        "grammar": [{"title": "Đại từ sở hữu làm chủ ngữ (Possessive Pronouns as Subject)", "content": "Theirs = Their design, tránh việc lặp từ 'design'."}]
    },
    120: {
        "stem": "The new Kitsuna video camera is currently on sale for $375, not ------- tax.",
        "stemVi": "Máy quay video Kitsuna mới hiện đang được giảm giá còn 375 đô la, chưa ------- thuế.",
        "options": {"A": "excepting", "B": "alongside", "C": "within", "D": "including"},
        "optionsVi": {"A": "ngoại trừ", "B": "bên cạnh", "C": "trong vòng", "D": "bao gồm"},
        "ans": "D",
        "exp": "Cụm từ quen thuộc trong mua sắm báo giá: 'not including tax' (chưa bao gồm thuế) -> chọn giới từ 'including'.",
        "vocab": [{"word": "video camera", "ipa": "/ˈvɪd.i.əʊ ˌkæm.rə/", "pos": "n", "meaning": "máy quay phim/video", "example": "high-definition video camera"}],
        "collocations": [{"phrase": "not including tax", "meaning": "chưa tính thuế"}],
        "grammar": [{"title": "Giới từ Including trong báo giá", "content": "Including + N: bao gồm cả cái gì."}]
    },
    121: {
        "stem": "All associates are ------- to follow the standard operating procedures outlined in the handbook.",
        "stemVi": "Tất cả các cộng tác viên được ------- phải tuân thủ các quy trình vận hành tiêu chuẩn được nêu trong cẩm nang.",
        "options": {"A": "concerned", "B": "tended", "C": "maintained", "D": "expected"},
        "optionsVi": {"A": "lo lắng", "B": "có xu hướng", "C": "duy trì", "D": "kỳ vọng, yêu cầu"},
        "ans": "D",
        "exp": "Cấu trúc bị động 'be expected to do something' (được yêu cầu/kỳ vọng phải làm gì) -> chọn 'expected'.",
        "vocab": [{"word": "procedure", "ipa": "/prəˈsiː.dʒər/", "pos": "n", "meaning": "quy trình, thủ tục", "example": "operating procedures"}],
        "collocations": [{"phrase": "standard operating procedures", "meaning": "quy trình vận hành tiêu chuẩn (SOP)"}],
        "grammar": [{"title": "Cấu trúc Be expected to-V", "content": "Diễn tả nghĩa vụ hoặc quy định bắt buộc phải tuân theo."}]
    },
    122: {
        "stem": "This month Framley Publishing House is embarking on its ------- expansion so far.",
        "stemVi": "Tháng này, Nhà xuất bản Framley đang bắt tay vào đợt mở rộng ------- từ trước đến nay.",
        "options": {"A": "ambitiously", "B": "most ambitiously", "C": "ambition", "D": "most ambitious"},
        "optionsVi": {"A": "đầy tham vọng (adv)", "B": "tham vọng nhất (adv)", "C": "tham vọng (n)", "D": "đầy tham vọng nhất (adj)"},
        "ans": "D",
        "exp": "Sau tính từ sở hữu 'its' và trước danh từ 'expansion' cần một tính từ so sánh nhất: 'its most ambitious expansion' (đợt mở rộng tham vọng nhất của hãng) -> chọn 'most ambitious'.",
        "vocab": [{"word": "embark on", "ipa": "/ɪmˈbɑːk ɒn/", "pos": "phr v", "meaning": "bắt tay vào, khởi sự", "example": "embark on a new campaign"}],
        "collocations": [{"phrase": "embark on an expansion", "meaning": "bắt tay vào việc mở rộng"}],
        "grammar": [{"title": "So sánh nhất của tính từ dài đứng trước danh từ", "content": "Possessive + most + adj + noun: its most ambitious expansion."}]
    },
    123: {
        "stem": "After months of collaboration, Matricks Technology's software developers ------- released a top-quality product.",
        "stemVi": "Sau nhiều tháng hợp tác, các nhà phát triển phần mềm của Matricks Technology ------- đã phát hành một sản phẩm chất lượng hàng đầu.",
        "options": {"A": "profoundly", "B": "overly", "C": "finally", "D": "intensely"},
        "optionsVi": {"A": "sâu sắc", "B": "quá mức", "C": "cuối cùng", "D": "mãnh liệt"},
        "ans": "C",
        "exp": "Sau một thời gian dài nỗ lực ('After months of collaboration'), hành động phát hành sản phẩm 'cuối cùng cũng diễn ra' -> dùng trạng từ 'finally' (cuối cùng thì).",
        "vocab": [{"word": "collaboration", "ipa": "/kəˌlæb.əˈreɪ.ʃən/", "pos": "n", "meaning": "sự cộng tác, hợp tác", "example": "in close collaboration with"}],
        "collocations": [{"phrase": "finally release", "meaning": "cuối cùng đã phát hành"}],
        "grammar": [{"title": "Trạng từ thời gian chỉ kết quả sau nỗ lực (Finally)", "content": "'Finally' bổ nghĩa cho động từ 'released'."}]
    },
    124: {
        "stem": "Tickets are valid for one-time access and do not allow for ------- into the venue.",
        "stemVi": "Vé chỉ có giá trị cho một lần vào cửa và không cho phép ------- vào địa điểm tổ chức.",
        "options": {"A": "duplication", "B": "reentry", "C": "permission", "D": "turnover"},
        "optionsVi": {"A": "sự nhân bản", "B": "sự vào lại", "C": "sự cho phép", "D": "doanh thu / luân chuyển"},
        "ans": "B",
        "exp": "Vé vào cửa 1 lần ('one-time access') không cho phép khán giả ra ngoài rồi 'vào lại' (reentry) -> chọn danh từ 'reentry'.",
        "vocab": [{"word": "reentry", "ipa": "/riːˈen.tri/", "pos": "n", "meaning": "việc đi vào lại", "example": "no reentry allowed without a wristband"}],
        "collocations": [{"phrase": "allow for reentry", "meaning": "cho phép vào lại"}],
        "grammar": [{"title": "Cụm động từ allow for + Noun", "content": "Allow for mang nghĩa tính đến hoặc cho phép điều gì xảy ra."}]
    },
    125: {
        "stem": "We hired Okafor Construction to do the renovation ------- it was not the lowest bidder on the project.",
        "stemVi": "Chúng tôi đã thuê Công ty Xây dựng Okafor cải tạo ------- họ không phải là bên đấu thầu giá thấp nhất cho dự án.",
        "options": {"A": "if only", "B": "alternatively", "C": "whereas", "D": "even though"},
        "optionsVi": {"A": "giá như", "B": "thay vào đó", "C": "trong khi (đối chiếu)", "D": "mặc dù"},
        "ans": "D",
        "exp": "Mệnh đề chỉ sự nhượng bộ, tương phản logic giữa việc thuê công ty và việc họ không phải bên chào giá thấp nhất -> dùng liên từ 'even though' (mặc dù).",
        "vocab": [{"word": "bidder", "ipa": "/ˈbɪd.ər/", "pos": "n", "meaning": "nhà thầu, người đấu giá", "example": "the lowest bidder"}],
        "collocations": [{"phrase": "lowest bidder", "meaning": "nhà thầu bỏ giá thấp nhất"}],
        "grammar": [{"title": "Mệnh đề trạng ngữ chỉ sự nhượng bộ (Concession Clauses)", "content": "Even though + clause: mặc dù."}]
    },
    126: {
        "stem": "The first ------- of the training will introduce staff to certain workplace responsibilities.",
        "stemVi": "------- đầu tiên của khóa đào tạo sẽ giới thiệu cho nhân viên về một số trách nhiệm tại nơi làm việc.",
        "options": {"A": "part", "B": "parted", "C": "parting", "D": "partial"},
        "optionsVi": {"A": "phần, giai đoạn (n)", "B": "đã chia", "C": "sự chia tay", "D": "một phần (adj)"},
        "ans": "A",
        "exp": "Sau số thứ tự 'The first' và trước giới từ 'of' cần một danh từ số ít làm chủ ngữ: 'The first part of the training' (Phần đầu tiên của khóa tập huấn) -> chọn 'part'.",
        "vocab": [{"word": "responsibility", "ipa": "/rɪˌspɒn.sɪˈbɪl.ə.ti/", "pos": "n", "meaning": "trách nhiệm", "example": "workplace responsibilities"}],
        "collocations": [{"phrase": "first part", "meaning": "phần đầu tiên"}],
        "grammar": [{"title": "Danh từ sau số thứ tự (The + Ordinal + Noun)", "content": "The first part."}]
    },
    127: {
        "stem": "According to industry -------, Ghira Company plans to relocate its headquarters to Australia.",
        "stemVi": "Theo các ------- trong ngành, Công ty Ghira có kế hoạch chuyển trụ sở chính sang Úc.",
        "options": {"A": "reported", "B": "reportedly", "C": "reporter", "D": "reports"},
        "optionsVi": {"A": "đã báo cáo", "B": "theo báo cáo (adv)", "C": "phóng viên", "D": "các báo cáo (n-số nhiều)"},
        "ans": "D",
        "exp": "Sau danh từ 'industry' cần một danh từ để tạo thành cụm danh từ ghép: 'industry reports' (các báo cáo chuyên ngành) -> chọn 'reports'.",
        "vocab": [{"word": "relocate", "ipa": "/ˌriː.ləʊˈkeɪt/", "pos": "v", "meaning": "chuyển địa điểm, dời đi", "example": "relocate the headquarters"}],
        "collocations": [{"phrase": "industry reports", "meaning": "các báo cáo trong ngành"}],
        "grammar": [{"title": "Cụm danh từ ghép (Noun + Noun)", "content": "Industry (bổ nghĩa) + reports (danh từ chính)."}]
    },
    128: {
        "stem": "Next month, the Kneath House will host an exhibition of ------- furniture and clothing from the eighteenth century.",
        "stemVi": "Tháng tới, Tòa nhà Kneath sẽ tổ chức triển lãm đồ nội thất và trang phục ------- từ thế kỷ thứ mười tám.",
        "options": {"A": "authentic", "B": "authentically", "C": "authenticate", "D": "authenticity"},
        "optionsVi": {"A": "nguyên bản, đích thực (adj)", "B": "một cách chân thực (adv)", "C": "xác thực (v)", "D": "tính xác thực (n)"},
        "ans": "A",
        "exp": "Trước cụm danh từ 'furniture and clothing' cần một tính từ để bổ nghĩa tính chất: 'authentic furniture' (đồ nội thất nguyên bản/cổ thật) -> chọn tính từ 'authentic'.",
        "vocab": [{"word": "authentic", "ipa": "/ɔːˈθen.tɪk/", "pos": "adj", "meaning": "chính thống, thật, nguyên bản", "example": "authentic antique furniture"}],
        "collocations": [{"phrase": "host an exhibition", "meaning": "đăng cai tổ chức triển lãm"}],
        "grammar": [{"title": "Tính từ bổ nghĩa cho danh từ", "content": "Authentic (adj) + Noun."}]
    },
    129: {
        "stem": "PKTM's regional managers serve ------- the direction of the vice president.",
        "stemVi": "Các nhà quản lý khu vực của PKTM làm việc ------- sự chỉ đạo của phó chủ tịch.",
        "options": {"A": "among", "B": "under", "C": "behind", "D": "opposite"},
        "optionsVi": {"A": "giữa nhiều người", "B": "dưới", "C": "đằng sau", "D": "đối diện"},
        "ans": "B",
        "exp": "Cụm giới từ cố định chỉ sự quản lý: 'under the direction of someone' (dưới sự chỉ đạo/hướng dẫn của ai) -> chọn 'under'.",
        "vocab": [{"word": "regional manager", "ipa": "/ˈriː.dʒən.əl ˈmæn.ɪ.dʒər/", "pos": "n", "meaning": "quản lý vùng/khu vực", "example": "regional sales manager"}],
        "collocations": [{"phrase": "under the direction of", "meaning": "dưới sự chỉ đạo của"}],
        "grammar": [{"title": "Cụm giới từ cố định (Fixed Prepositional Phrase)", "content": "Under the direction/supervision of someone."}]
    },
    130: {
        "stem": "------- a recent surge in demand, Vanita's Catering is hiring four additional servers.",
        "stemVi": "------- sự gia tăng đột biến gần đây về nhu cầu, Vanita's Catering đang tuyển thêm bốn nhân viên phục vụ.",
        "options": {"A": "Everywhere", "B": "Possibly", "C": "In total", "D": "Owing to"},
        "optionsVi": {"A": "Mọi nơi", "B": "Có thể", "C": "Tổng cộng", "D": "Nhờ vào, do vì"},
        "ans": "D",
        "exp": "Trước cụm danh từ 'a recent surge in demand' cần một cụm giới từ chỉ nguyên nhân: 'Owing to + Noun phrase' (Do vì...) -> chọn 'Owing to'.",
        "vocab": [{"word": "surge", "ipa": "/sɜːdʒ/", "pos": "n", "meaning": "sự tăng vọt, đột biến", "example": "a surge in customer demand"}],
        "collocations": [{"phrase": "owing to", "meaning": "do vì, nhờ có"}, {"phrase": "surge in demand", "meaning": "nhu cầu tăng đột biến"}],
        "grammar": [{"title": "Cụm giới từ chỉ nguyên nhân (Owing to + Noun)", "content": "Đóng vai trò trạng ngữ chỉ nguyên nhân cho mệnh đề chính."}]
    }
}

for qid, p5info in p5_clean_data.items():
    q = q_map[qid]
    q["part"] = 5
    q["partName"] = "Part 5: Incomplete Sentences"
    q["questionText"] = p5info["stem"]
    q["questionTextVi"] = p5info["stemVi"]
    q["options"] = p5info["options"]
    q["optionsVi"] = p5info["optionsVi"]
    q["correctAnswer"] = p5info["ans"]
    q["explanation"] = p5info["exp"]
    q["vocabulary"] = p5info["vocab"]
    q["collocations"] = p5info["collocations"]
    q["grammar"] = p5info["grammar"]

print("Part 5 perfected!")

# ==========================================
# 5. PART 6 (Q131 - Q146) VERIFY & ENHANCE
# ==========================================
p6_imgs = {
    131: 5, 132: 5, 133: 5, 134: 5,
    135: 6, 136: 6, 137: 6, 138: 6,
    139: 7, 140: 7, 141: 7, 142: 7,
    143: 8, 144: 8, 145: 8, 146: 8
}
for qid, pnum in p6_imgs.items():
    q = q_map[qid]
    q["pageImage"] = f"assets/images/test3/rc_page_{pnum}.png"
    q["image"] = f"assets/images/test3/rc_page_{pnum}.png"
print("Part 6 images linked!")

# ==========================================
# 6. PART 7 (Q147 - Q200) REBUILD & RESTORE
# ==========================================
p7_clean_questions = {
    147: {
        "stem": "What will happen at Medillo Shoes on May 10?",
        "options": {
            "A": "All shoes will be discounted.",
            "B": "Shop assistants will be hired.",
            "C": "A shoe style will be discontinued.",
            "D": "Operational hours will be extended."
        },
        "ans": "A",
        "pages": [9]
    },
    148: {
        "stem": "What is indicated about Medillo Shoes?",
        "options": {
            "A": "It has been in business for ten years.",
            "B": "It specializes in athletic footwear.",
            "C": "It is located next to a medical center.",
            "D": "It allows customers to make appointments."
        },
        "ans": "D",
        "pages": [9]
    },
    149: {
        "stem": "What is the purpose of the e-mail?",
        "options": {
            "A": "To register for a conference",
            "B": "To announce a new account",
            "C": "To schedule a meeting",
            "D": "To inform colleagues of an absence"
        },
        "ans": "D",
        "pages": [10]
    },
    150: {
        "stem": "What is most likely true about Ms. Soroka?",
        "options": {
            "A": "She will be traveling with Mr. Cullen.",
            "B": "She works on the Ezenx Industries account.",
            "C": "She is Ms. Choo's supervisor.",
            "D": "She will be out of the office until April 22."
        },
        "ans": "B",
        "pages": [10]
    },
    151: {
        "stem": "What change is the Building Permit Office making?",
        "options": {
            "A": "It is moving to a new location.",
            "B": "It is simplifying the permit application process.",
            "C": "It is reducing the number of days it will accept permit applications.",
            "D": "It is increasing the processing time for permit applications."
        },
        "ans": "C",
        "pages": [11]
    },
    152: {
        "stem": "According to the notice, why is the change being made?",
        "options": {
            "A": "To save the city money",
            "B": "To attract more residents",
            "C": "To improve the quality of service",
            "D": "To decrease the number of new permit applications"
        },
        "ans": "A",
        "pages": [11]
    },
    153: {
        "stem": "What is indicated about the river tour?",
        "options": {
            "A": "It is one hour long.",
            "B": "It comes with a meal.",
            "C": "It can be rescheduled.",
            "D": "It sells out quickly."
        },
        "ans": "B",
        "pages": [12]
    },
    154: {
        "stem": "How many tickets did Mr. Califf purchase?",
        "options": {
            "A": "1",
            "B": "2",
            "C": "4",
            "D": "6"
        },
        "ans": "C",
        "pages": [12]
    },
    155: {
        "stem": "How can customers receive a discount on a walking tour?",
        "options": {
            "A": "By making a reservation online",
            "B": "By paying with a credit card",
            "C": "By requesting a coupon from the captain",
            "D": "By mentioning a confirmation code"
        },
        "ans": "D",
        "pages": [12]
    },
    156: {
        "stem": 'At 8:12 A.M., what does Mr. Kwon most likely mean when he writes, "I see an office supply store across the street"?',
        "options": {
            "A": "He needs help finding a building.",
            "B": "He can purchase some paper.",
            "C": "He will look for a new printer.",
            "D": "He is going to negotiate a delivery schedule."
        },
        "ans": "B",
        "pages": [13]
    },
    157: {
        "stem": "What will Ms. Saunders most likely do next?",
        "options": {
            "A": "Reschedule a meeting",
            "B": "Prepare some refreshments",
            "C": "Check on an arrival time",
            "D": "Revise a design proposal"
        },
        "ans": "C",
        "pages": [13]
    },
    158: {
        "stem": "What is suggested about Ms. Omar?",
        "options": {
            "A": "She is an accountant.",
            "B": "She works for Mr. Piskorksi.",
            "C": "She operates a small company.",
            "D": "She is a Kipbank customer."
        },
        "ans": "C",
        "pages": [14]
    },
    159: {
        "stem": "What is stated about the credit cards?",
        "options": {
            "A": "They come in a variety of colors.",
            "B": "They require an annual fee.",
            "C": "They include discounts on certain purchases.",
            "D": "They can be used to buy personal items."
        },
        "ans": "C",
        "pages": [14]
    },
    160: {
        "stem": 'In which of the positions marked [1], [2], [3], and [4] does the following sentence best belong? "Everyday financial details only add more distractions."',
        "options": {
            "A": "[1]",
            "B": "[2]",
            "C": "[3]",
            "D": "[4]"
        },
        "ans": "A",
        "pages": [14]
    },
    161: {
        "stem": "What is the purpose of the article?",
        "options": {
            "A": "To profile a newly opened business",
            "B": "To analyze a trend in the electronics industry",
            "C": "To highlight a company's achievement",
            "D": "To discuss changes to an employment contract"
        },
        "ans": "C",
        "pages": [15]
    },
    162: {
        "stem": "What is suggested about Carila Corporation?",
        "options": {
            "A": "It no longer develops electronics.",
            "B": "It was once a struggling business.",
            "C": "It has been unable to attract more clients.",
            "D": "It is seeking to replace its CEO."
        },
        "ans": "B",
        "pages": [15]
    },
    163: {
        "stem": 'The word "solution" in paragraph 3, line 6, is closest in meaning to',
        "options": {
            "A": "mixture",
            "B": "proof",
            "C": "statement",
            "D": "answer"
        },
        "ans": "D",
        "pages": [15]
    },
    164: {
        "stem": "What Commbolt benefit does the advertisement mention?",
        "options": {
            "A": "Its low prices",
            "B": "Its excellent customer service",
            "C": "Its lifetime contracts",
            "D": "Its convenient installation schedule"
        },
        "ans": "B",
        "pages": [16]
    },
    165: {
        "stem": "What is the maximum amount a customer can earn when one referred person signs up for service?",
        "options": {
            "A": "$10.00",
            "B": "$20.00",
            "C": "$45.00",
            "D": "$60.00"
        },
        "ans": "B",
        "pages": [16]
    },
    166: {
        "stem": "What is true about the Commbolt promotion?",
        "options": {
            "A": "It may not be posted on social media.",
            "B": "It does not provide credit for more than three referrals.",
            "C": "It is expected to run for a full year.",
            "D": "It rewards both new and existing customers."
        },
        "ans": "D",
        "pages": [16]
    },
    167: {
        "stem": 'In which of the positions marked [1], [2], [3], or [4] does the following sentence best belong? "Just share your unique referral code with friends and family."',
        "options": {
            "A": "[1]",
            "B": "[2]",
            "C": "[3]",
            "D": "[4]"
        },
        "ans": "C",
        "pages": [16]
    },
    168: {
        "stem": "What is indicated about Sarah's Catering?",
        "options": {
            "A": "It uses locally sourced products.",
            "B": "It is twenty years old.",
            "C": "It specializes mainly in weddings.",
            "D": "It has an on-site dining room."
        },
        "ans": "A",
        "pages": [17]
    },
    169: {
        "stem": 'The word "taste" in paragraph 1, line 4, is closest in meaning to',
        "options": {
            "A": "preference",
            "B": "sample",
            "C": "experience",
            "D": "flavor"
        },
        "ans": "A",
        "pages": [17]
    },
    170: {
        "stem": "What is mentioned as a service provided by Sarah's Catering?",
        "options": {
            "A": "Entertainment planning",
            "B": "Cooking demonstrations",
            "C": "Cleanup after meals",
            "D": "Rentals of tables and chairs"
        },
        "ans": "C",
        "pages": [17]
    },
    171: {
        "stem": "Who most likely is Mr. Liu?",
        "options": {
            "A": "An employee of Sarah's Catering",
            "B": "A professional event manager",
            "C": "A customer of Sarah's Catering",
            "D": "An assistant at a marketing firm"
        },
        "ans": "C",
        "pages": [17]
    },
    172: {
        "stem": "Why does Mr. Steuber write to Ms. Rajan?",
        "options": {
            "A": "To invite her to a professional event",
            "B": "To check on the status of a meeting",
            "C": "To make travel plans for a business trip",
            "D": "To ask about an assistant's performance"
        },
        "ans": "B",
        "pages": [18, 19]
    },
    173: {
        "stem": 'At 10:45 A.M., what does Mr. Steuber most likely mean when he writes, "Let me check with my supervisor"?',
        "options": {
            "A": "He needs final approval on a book design.",
            "B": "He would like advice on changing an appointment.",
            "C": "He requires access to the corporate calendar.",
            "D": "He is uncertain how to add team members to the chat."
        },
        "ans": "B",
        "pages": [18, 19]
    },
    174: {
        "stem": "Who most likely is Ms. Benoit?",
        "options": {
            "A": "A writer",
            "B": "A designer",
            "C": "A production editor",
            "D": "A printing plant supervisor"
        },
        "ans": "A",
        "pages": [18, 19]
    },
    175: {
        "stem": "What will Ms. Rajan probably do next?",
        "options": {
            "A": "Suggest solutions to a printing issue",
            "B": "Arrange to visit the Singapore plant",
            "C": "Attend a meeting with Ms. Luong",
            "D": "Reschedule a video conference"
        },
        "ans": "D",
        "pages": [18, 19]
    },
    176: {
        "stem": "Who was originally scheduled to perform at the Bramley Theater?",
        "options": {
            "A": "Johanna Greenblatt",
            "B": "The Blass Brothers Band",
            "C": "The Rolling Dozen",
            "D": "Jefferson Cage"
        },
        "ans": "B",
        "pages": [20, 21]
    },
    177: {
        "stem": "What does the schedule suggest about the Rambling River Festival?",
        "options": {
            "A": "It takes place annually.",
            "B": "It requires a ticket for entry.",
            "C": "It features local food vendors.",
            "D": "It is mainly an outdoor event."
        },
        "ans": "D",
        "pages": [20, 21]
    },
    178: {
        "stem": "According to the text message, what can audience members do at Cole Hall?",
        "options": {
            "A": "Check coats",
            "B": "Store bulky items",
            "C": "Buy concert tickets",
            "D": "Pick up a schedule of events"
        },
        "ans": "A",
        "pages": [20, 21]
    },
    179: {
        "stem": 'In the text message, the word "pushed" in paragraph 2, line 1, is closest in meaning to',
        "options": {
            "A": "moved",
            "B": "extended",
            "C": "managed",
            "D": "pressured"
        },
        "ans": "A",
        "pages": [20, 21]
    },
    180: {
        "stem": "When will Kirschau perform?",
        "options": {
            "A": "At 3:30 P.M. on Friday",
            "B": "At 8:00 P.M. on Friday",
            "C": "At 2:30 P.M. on Saturday",
            "D": "At 6:30 P.M. on Saturday"
        },
        "ans": "B",
        "pages": [20, 21]
    },
    181: {
        "stem": "What is one purpose of the e-mail?",
        "options": {
            "A": "To provide details on a new privacy policy",
            "B": "To propose a survey of banking habits",
            "C": "To ask bank staff to test a mobile app",
            "D": "To inform managers of a company problem"
        },
        "ans": "D",
        "pages": [22, 23]
    },
    182: {
        "stem": "According to the e-mail, what percentage of the bank's customers use the mobile app?",
        "options": {
            "A": "23 percent",
            "B": "39 percent",
            "C": "78 percent",
            "D": "95 percent"
        },
        "ans": "B",
        "pages": [22, 23]
    },
    183: {
        "stem": 'In the article, the word "anticipates" in paragraph 3, line 5, is closest in meaning to',
        "options": {
            "A": "considers",
            "B": "waits for",
            "C": "prepares for",
            "D": "expects"
        },
        "ans": "D",
        "pages": [22, 23]
    },
    184: {
        "stem": "Who most likely attended a meeting at Ogden Bank headquarters on April 12?",
        "options": {
            "A": "Mr. Panzius",
            "B": "Ms. DeFreese",
            "C": "Mr. Baum",
            "D": "Ms. Reed"
        },
        "ans": "B",
        "pages": [22, 23]
    },
    185: {
        "stem": "What is suggested about Ogden Bank's management?",
        "options": {
            "A": "It prefers that account holders do their banking in person.",
            "B": "It is considering offering free checking to new account holders.",
            "C": "It is in the process of hiring more staff.",
            "D": "It prioritizes improvements in customer experience."
        },
        "ans": "D",
        "pages": [22, 23]
    },
    186: {
        "stem": "What is the purpose of the notice?",
        "options": {
            "A": "To highlight some books in the library",
            "B": "To announce a change in library hours",
            "C": "To promote an activity at the library",
            "D": "To introduce a new librarian"
        },
        "ans": "C",
        "pages": [24, 25]
    },
    187: {
        "stem": "What is suggested about the book Wild Open Range?",
        "options": {
            "A": "It is a best-selling title.",
            "B": "It is a work of nonfiction.",
            "C": "It was published ten years ago.",
            "D": "It is available at a discount for library members."
        },
        "ans": "B",
        "pages": [24, 25]
    },
    188: {
        "stem": "What author most likely wrote about a famous person?",
        "options": {
            "A": "Jaxon McDonald",
            "B": "Lucy Xi",
            "C": "Peter Landers",
            "D": "Kai Noble"
        },
        "ans": "D",
        "pages": [24, 25]
    },
    189: {
        "stem": "What can be concluded about Ms. Calle?",
        "options": {
            "A": "She is a library staff member.",
            "B": "She has written book reviews.",
            "C": "She is Ms. Frey's supervisor.",
            "D": "She favors historical fiction."
        },
        "ans": "A",
        "pages": [24, 25]
    },
    190: {
        "stem": "What does Ms. Frey indicate about the book she read?",
        "options": {
            "A": "It discussed a topic that was unfamiliar to her.",
            "B": "It had parts that she thought were inaccurate.",
            "C": "It was easy to read in the time available.",
            "D": "It inspired her to explore an old interest."
        },
        "ans": "D",
        "pages": [24, 25]
    },
    191: {
        "stem": "What is a policy of George Street Sweets?",
        "options": {
            "A": "Orders cannot be changed.",
            "B": "Orders placed less than 48 hours before pickup incur an extra fee.",
            "C": "Orders must be paid for when they are placed.",
            "D": "Orders cannot be refunded within 24 hours of pickup."
        },
        "ans": "D",
        "pages": [26, 27]
    },
    192: {
        "stem": "What is suggested about the building at 2 Spen Lane?",
        "options": {
            "A": "It has parking spaces behind a bicycle shop.",
            "B": "It is located within 10 kilometers of George Street Sweets.",
            "C": "It is a residential apartment building.",
            "D": "It is owned by Ms. Schwartz."
        },
        "ans": "B",
        "pages": [26, 27]
    },
    193: {
        "stem": "What can be concluded about the cake?",
        "options": {
            "A": "It has not been paid for yet.",
            "B": "It will have only chocolate icing.",
            "C": "It was ordered over the phone.",
            "D": "It contains ice cream."
        },
        "ans": "C",
        "pages": [26, 27]
    },
    194: {
        "stem": "In the second e-mail, what does Mr. Ordaz request?",
        "options": {
            "A": "A full refund",
            "B": "A different flavor",
            "C": "A response to an e-mail",
            "D": "An additional candle"
        },
        "ans": "C",
        "pages": [26, 27]
    },
    195: {
        "stem": "What does Mr. Ordaz mention about the event in his e-mail?",
        "options": {
            "A": "It will take place on April 29.",
            "B": "It is an anniversary party.",
            "C": "Its start time has changed.",
            "D": "It will be larger than expected."
        },
        "ans": "D",
        "pages": [26, 27]
    },
    196: {
        "stem": "In his e-mail, what does Mr. Grewal indicate about the survey?",
        "options": {
            "A": "It does not have an end date.",
            "B": "It requires the use of a password.",
            "C": "It can be completed on paper.",
            "D": "It should not be shared with others."
        },
        "ans": "D",
        "pages": [28, 29]
    },
    197: {
        "stem": "According to the e-mail, what do some Woolf Flooring employees disagree with?",
        "options": {
            "A": "The plan to hire consultants",
            "B": "The way a survey is structured",
            "C": "The way a budget report is presented",
            "D": "The departments selected to provide feedback"
        },
        "ans": "A",
        "pages": [28, 29]
    },
    198: {
        "stem": "What can be concluded about Ms. Mair?",
        "options": {
            "A": "She regularly provides ideas for change.",
            "B": "She has worked at Woolf Flooring for many years.",
            "C": "She will be helping to collect feedback.",
            "D": "She works in the production department."
        },
        "ans": "B",
        "pages": [28, 29]
    },
    199: {
        "stem": "In the survey, what does Ms. Mair note about her suggestion?",
        "options": {
            "A": "It may require some new equipment.",
            "B": "It has worked well at other companies.",
            "C": "It could be implemented right away.",
            "D": "It has been suggested to management before."
        },
        "ans": "C",
        "pages": [28, 29]
    },
    200: {
        "stem": "What recommendation made by Miyoko Consulting corresponds with Ms. Mair's suggestion?",
        "options": {
            "A": "Recommendation 1",
            "B": "Recommendation 2",
            "C": "Recommendation 3",
            "D": "Recommendation 4"
        },
        "ans": "D",
        "pages": [28, 29]
    }
}

for qid, p7info in p7_clean_questions.items():
    q = q_map[qid]
    q["part"] = 7
    q["partName"] = "Part 7: Reading Comprehension"
    q["questionText"] = p7info["stem"]
    q["options"] = p7info["options"]
    q["correctAnswer"] = p7info["ans"]
    
    img_list = [f"assets/images/test3/rc_page_{p}.png" for p in p7info["pages"]]
    q["pageImages"] = img_list
    q["pageImage"] = img_list[0]
    q["image"] = img_list[0]
    if qid >= 186:
        q["passageType"] = "Triple Passage"
    elif qid >= 176:
        q["passageType"] = "Double Passage"
    else:
        q["passageType"] = "Single Passage"

print("Part 7 perfected!")

# Final save
t3_data["title"] = "ETS TOEIC 2024 - TEST 03"
t3_data["testTitle"] = "ETS TOEIC 2024 - TEST 03"
t3_data["description"] = "Đề thi ETS TOEIC 2024 Test 3 chuẩn định dạng chuẩn quốc tế, đầy đủ 200 câu hỏi, âm thanh từng câu/đoạn, đáp án chính thức và giải thích chi tiết."
t3_data["totalQuestions"] = 200
t3_data["questions"] = [q_map[i] for i in range(1, 201)]

with open(os.path.join(BASE_DIR, "web", "data", "test3.json"), "w", encoding="utf-8") as f:
    json.dump(t3_data, f, ensure_ascii=False, indent=2)

print("Saved web/data/test3.json successfully with all 200 questions!")
