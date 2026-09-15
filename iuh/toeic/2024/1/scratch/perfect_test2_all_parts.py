import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"

# Load existing test2.json
with open(os.path.join(BASE_DIR, "web", "data", "test2.json"), "r", encoding="utf-8") as f:
    t2_data = json.load(f)

questions = t2_data["questions"]
q_map = {q["id"]: q for q in questions}

# ==========================================
# 1. PART 1 (Q1 - Q6)
# ==========================================
# Ensure correct image paths and clean options
p1_info = {
    1: {
        "stem": "Look at the picture marked No. 1 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 1 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "She's inserting a cord into an outlet.",
            "B": "She's pressing a button on a machine.",
            "C": "She's gripping the handle of a drawer.",
            "D": "She's tacking a notice onto the wall."
        },
        "optionsVi": {
            "A": "Cô ấy đang cắm một sợi dây vào ổ điện.",
            "B": "Cô ấy đang bấm một nút trên máy móc.",
            "C": "Cô ấy đang nắm vào tay cầm của ngăn kéo.",
            "D": "Cô ấy đang ghim một thông báo lên tường."
        },
        "ans": "A",
        "exp": "Phương án (A) miêu tả chính xác trạng thái trong tranh: Người phụ nữ đang cúi người cắm dây nguồn vào ổ cắm điện trên tường ('She's inserting a cord into an outlet'). Các phương án khác không xuất hiện trong hình ảnh.",
        "vocab": [
            {"word": "insert", "ipa": "/ɪnˈsɜːt/", "pos": "v", "meaning": "cắm vào, đưa vào", "example": "She inserted the key into the lock."},
            {"word": "cord", "ipa": "/kɔːd/", "pos": "n", "meaning": "dây điện, dây cáp mềm", "example": "The electrical cord is plugged into the wall."},
            {"word": "outlet", "ipa": "/ˈaʊt.let/", "pos": "n", "meaning": "ổ cắm điện", "example": "Plug the lamp into the nearest wall outlet."}
        ],
        "collocations": [{"phrase": "insert a cord into an outlet", "meaning": "cắm dây điện vào ổ cắm"}],
        "grammar": [{"title": "Thì hiện tại tiếp diễn chỉ hành động của người", "content": "Cấu trúc S + is/are + V-ing diễn tả hành động đang xảy ra tại thời điểm quan sát trong bức tranh."}]
    },
    2: {
        "stem": "Look at the picture marked No. 2 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 2 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "Some window shutters are being replaced.",
            "B": "A pillow is being arranged on a seat.",
            "C": "An outdoor table is being cleared off.",
            "D": "Some wooden boards are being painted."
        },
        "optionsVi": {
            "A": "Một vài cánh cửa chớp đang được thay thế.",
            "B": "Một chiếc gối đang được sắp đặt trên chỗ ngồi.",
            "C": "Một chiếc bàn ngoài trời đang được dọn sạch.",
            "D": "Một vài tấm ván gỗ đang được sơn."
        },
        "ans": "B",
        "exp": "Phương án (B) miêu tả chính xác hành động: Người trong tranh đang chỉnh sửa, đặt chiếc gối lên băng ghế ngoài trời ('A pillow is being arranged on a seat').",
        "vocab": [
            {"word": "pillow", "ipa": "/ˈpɪl.əʊ/", "pos": "n", "meaning": "gối tựa, gối kê", "example": "She placed a decorative pillow on the sofa."},
            {"word": "arrange", "ipa": "/əˈreɪndʒ/", "pos": "v", "meaning": "sắp xếp, sắp đặt", "example": "The cushions were neatly arranged on the bench."},
            {"word": "shutter", "ipa": "/ˈʃʌt.ər/", "pos": "n", "meaning": "cửa chớp", "example": "The wooden shutters were closed."}
        ],
        "collocations": [{"phrase": "arrange a pillow", "meaning": "sắp xếp, đặt gối"}],
        "grammar": [{"title": "Bị động thì hiện tại tiếp diễn (is/are being + V3/ed)", "content": "Nhấn mạnh hành động đang được thực hiện bởi một người tác động lên đồ vật."}]
    },
    3: {
        "stem": "Look at the picture marked No. 3 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 3 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "Some utensils have been discarded in a bin.",
            "B": "Some bottles are being emptied into a sink.",
            "C": "A rolling chair has been placed next to a counter.",
            "D": "Some drawers have been left open."
        },
        "optionsVi": {
            "A": "Một số dụng cụ ăn uống đã bị vứt vào thùng rác.",
            "B": "Một vài cái chai đang được đổ hết vào bồn rửa.",
            "C": "Một chiếc ghế xoay có bánh xe đã được đặt cạnh quầy.",
            "D": "Một vài ngăn kéo đã bị để mở."
        },
        "ans": "C",
        "exp": "Phương án (C) miêu tả chính xác trạng thái tĩnh của đồ vật trong phòng: Chiếc ghế xoay có bánh xe đặt ngay bên cạnh chiếc bàn/quầy ('A rolling chair has been placed next to a counter').",
        "vocab": [
            {"word": "rolling chair", "ipa": "/ˈrəʊlɪŋ tʃeər/", "pos": "n", "meaning": "ghế xoay có bánh lăn", "example": "He sat on a rolling chair at the lab counter."},
            {"word": "counter", "ipa": "/ˈkaʊn.tər/", "pos": "n", "meaning": "quầy, bàn làm việc dài", "example": "Equipment was neatly organized on the counter."},
            {"word": "utensil", "ipa": "/juːˈten.sɪl/", "pos": "n", "meaning": "dụng cụ, đồ dùng (nhà bếp/thí nghiệm)", "example": "Cooking utensils are hung on the wall."}
        ],
        "collocations": [{"phrase": "rolling chair", "meaning": "ghế có bánh xe"}, {"phrase": "next to a counter", "meaning": "bên cạnh quầy"}],
        "grammar": [{"title": "Bị động thì hiện tại hoàn thành miêu tả trạng thái (have/has been + V3/ed)", "content": "Diễn tả đồ vật đã được đặt/để ở một vị trí cụ thể và trạng thái đó vẫn đang duy trì tại thời điểm chụp ảnh."}]
    },
    4: {
        "stem": "Look at the picture marked No. 4 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 4 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "A man is chopping some wood into pieces.",
            "B": "Leaves are scattered across the grass.",
            "C": "A man is closing a window.",
            "D": "Wood is piled near a fence."
        },
        "optionsVi": {
            "A": "Một người đàn ông đang chặt củi thành từng khúc.",
            "B": "Lá cây vương vãi khắp bãi cỏ.",
            "C": "Một người đàn ông đang đóng cửa sổ.",
            "D": "Gỗ củi được xếp thành đống gần hàng rào."
        },
        "ans": "D",
        "exp": "Phương án (D) miêu tả chính xác khung cảnh: Các khúc gỗ củi được xếp chất đống ngăn nắp sát cạnh hàng rào gỗ ('Wood is piled near a fence').",
        "vocab": [
            {"word": "pile", "ipa": "/paɪl/", "pos": "v", "meaning": "chất đống, xếp đống", "example": "Logs of firewood were piled neatly outside."},
            {"word": "fence", "ipa": "/fens/", "pos": "n", "meaning": "hàng rào", "example": "A wooden fence surrounds the garden."},
            {"word": "chop", "ipa": "/tʃɒp/", "pos": "v", "meaning": "chặt, đốn (củi)", "example": "He was chopping firewood in the yard."}
        ],
        "collocations": [{"phrase": "piled near a fence", "meaning": "chất đống gần hàng rào"}],
        "grammar": [{"title": "Cấu trúc bị động miêu tả vị trí (is/are + V3/ed + giới từ)", "content": "'Wood is piled near a fence' diễn tả trạng thái của đống củi."}]
    },
    5: {
        "stem": "Look at the picture marked No. 5 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 5 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "People are standing in line in a lobby.",
            "B": "Items are being loaded into shopping bags.",
            "C": "Tents have been set up in a parking area.",
            "D": "A worker is putting up a canopy."
        },
        "optionsVi": {
            "A": "Mọi người đang xếp hàng trong tiền sảnh.",
            "B": "Các món hàng đang được xếp vào túi mua sắm.",
            "C": "Những chiếc lều bạt đã được dựng lên trong khu vực bãi đỗ xe.",
            "D": "Một người công nhân đang dựng một mái hiên."
        },
        "ans": "C",
        "exp": "Phương án (C) miêu tả chính xác bức tranh: Những chiếc lều bạt trắng của hội chợ/chợ trời đã được dựng sẵn tại bãi đỗ xe ngoài trời ('Tents have been set up in a parking area').",
        "vocab": [
            {"word": "tent", "ipa": "/tent/", "pos": "n", "meaning": "lều bạt", "example": "Several vendor tents were set up in the lot."},
            {"word": "set up", "ipa": "/set ʌp/", "pos": "phr v", "meaning": "dựng lên, thiết lập", "example": "They set up their stalls early in the morning."},
            {"word": "canopy", "ipa": "/ˈkæn.ə.pi/", "pos": "n", "meaning": "mái che, bạt che nắng", "example": "A canopy provided shade for the customers."}
        ],
        "collocations": [{"phrase": "set up a tent", "meaning": "dựng lều"}, {"phrase": "parking area", "meaning": "khu vực đỗ xe"}],
        "grammar": [{"title": "Bị động thì hiện tại hoàn thành (have/has been set up)", "content": "Diễn tả hành động dựng lều đã hoàn thành trước đó và kết quả là các túp lều đang hiện diện trong ảnh."}]
    },
    6: {
        "stem": "Look at the picture marked No. 6 in your test book and choose the best statement:",
        "stemVi": "Nhìn vào bức tranh số 6 và chọn phương án miêu tả đúng nhất:",
        "options": {
            "A": "Some luggage is stacked next to an escalator.",
            "B": "A suitcase is being lifted onto a shuttle bus.",
            "C": "Some suitcases are displayed in a shop window.",
            "D": "A luggage rack has two levels."
        },
        "optionsVi": {
            "A": "Hành lý được xếp chồng lên nhau bên cạnh thang cuốn.",
            "B": "Một chiếc vali đang được nhấc lên xe buýt đưa đón.",
            "C": "Một vài chiếc vali được trưng bày trong tủ kính cửa hàng.",
            "D": "Một chiếc giá để hành lý có hai tầng."
        },
        "ans": "D",
        "exp": "Phương án (D) miêu tả chính xác chi tiết đặc trưng của đồ vật: Chiếc giá/kệ để hành lý trên tàu hoặc khoang hành khách có hai tầng rõ rệt ('A luggage rack has two levels').",
        "vocab": [
            {"word": "luggage rack", "ipa": "/ˈlʌɡ.ɪdʒ ræk/", "pos": "n", "meaning": "giá để hành lý", "example": "Place your large bags on the lower luggage rack."},
            {"word": "suitcase", "ipa": "/ˈsuːt.keɪs/", "pos": "n", "meaning": "vali", "example": "She packed two large suitcases for the trip."},
            {"word": "levels", "ipa": "/ˈlev.əlz/", "pos": "n", "meaning": "tầng bậc, cấp độ", "example": "The shelf has two distinct levels."}
        ],
        "collocations": [{"phrase": "luggage rack", "meaning": "giá để hành lý"}],
        "grammar": [{"title": "Cấu trúc miêu tả đặc điểm với 'have/has'", "content": "S + has/have + [đặc điểm] được dùng để mô tả kết cấu, số lượng ngăn/tầng của một đồ vật."}]
    }
}

for qid, info in p1_info.items():
    q = q_map[qid]
    q["image"] = f"assets/images/test2/q{qid}.png"
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
# 2. PART 4 FIXES (Q81, Q100)
# ==========================================
if 81 in q_map:
    q81 = q_map[81]
    if q81["questionText"].endswith(" to"):
        q81["questionText"] = q81["questionText"][:-3]
    print(f"Q81 fixed stem: {q81['questionText']}")

if 100 in q_map:
    q100 = q_map[100]
    if not q100["questionText"].endswith("?"):
        q100["questionText"] = "What does the speaker invite the listeners to do?"
    print(f"Q100 fixed stem: {q100['questionText']}")

# ==========================================
# 3. PART 5 (Q101 - Q130) REBUILD
# ==========================================
p5_data = {
    101: {
        "stem": "Before operating your handheld device, please ------- the enclosed cable to charge it.",
        "stemVi": "Trước khi vận hành thiết bị cầm tay, vui lòng ------- sợi cáp đi kèm để sạc pin.",
        "options": {"A": "plan", "B": "remain", "C": "use", "D": "finish"},
        "optionsVi": {"A": "lên kế hoạch", "B": "còn lại, giữ nguyên", "C": "sử dụng", "D": "hoàn thành"},
        "ans": "C",
        "exp": "Sau 'please' cần một động từ nguyên mẫu mang nghĩa phù hợp với ngữ cảnh 'sử dụng dây cáp đi kèm để sạc pin' -> chọn 'use' (sử dụng).",
        "vocab": [
            {"word": "handheld", "ipa": "/ˈhænd.held/", "pos": "adj", "meaning": "cầm tay", "example": "handheld electronic devices"},
            {"word": "enclosed", "ipa": "/ɪnˈkləʊzd/", "pos": "adj", "meaning": "được đính kèm, gửi kèm", "example": "Please find the enclosed document."}
        ],
        "collocations": [{"phrase": "enclosed cable", "meaning": "dây cáp đính kèm"}],
        "grammar": [{"title": "Câu mệnh lệnh lịch sự với Please + V-inf", "content": "Cấu trúc 'Please + V-bare' yêu cầu hoặc đề nghị ai đó làm gì."}]
    },
    102: {
        "stem": "Safile's new external hard drive can ------- store up to one terabyte of data.",
        "stemVi": "Ổ cứng ngoài mới của Safile có thể lưu trữ dữ liệu lên tới 1 terabyte một cách -------.",
        "options": {"A": "secure", "B": "security", "C": "securely", "D": "secured"},
        "optionsVi": {"A": "an toàn (adj/v)", "B": "sự an ninh (n)", "C": "một cách an toàn (adv)", "D": "được bảo đảm (v-ed)"},
        "ans": "C",
        "exp": "Vị trí nằm giữa trợ động từ khiếm khuyết 'can' và động từ chính 'store' cần một trạng từ (adverb) để bổ nghĩa cho động từ 'store' -> chọn 'securely'.",
        "vocab": [
            {"word": "securely", "ipa": "/sɪˈkjʊə.li/", "pos": "adv", "meaning": "một cách an toàn, chắc chắn", "example": "All files are stored securely in the cloud."},
            {"word": "external hard drive", "ipa": "/ɪkˈstɜː.nəl hɑːd draɪv/", "pos": "n", "meaning": "ổ cứng ngoài", "example": "Back up your data onto an external hard drive."}
        ],
        "collocations": [{"phrase": "store securely", "meaning": "lưu trữ an toàn"}],
        "grammar": [{"title": "Vị trí của trạng từ (Adverb Position)", "content": "Trạng từ đứng giữa trợ động từ (modal verb) và động từ chính (can + adv + V)."}]
    },
    103: {
        "stem": "Mr. Peterson will travel ------- the Tokyo office for the annual meeting.",
        "stemVi": "Ông Peterson sẽ đi đến ------- văn phòng Tokyo để tham dự cuộc họp thường niên.",
        "options": {"A": "to", "B": "through", "C": "in", "D": "over"},
        "optionsVi": {"A": "đến", "B": "xuyên qua", "C": "trong", "D": "qua, hơn"},
        "ans": "A",
        "exp": "Động từ 'travel' đi với giới từ 'to' chỉ phương hướng đến một địa điểm: 'travel to somewhere' -> chọn 'to'.",
        "vocab": [
            {"word": "annual", "ipa": "/ˈæn.ju.əl/", "pos": "adj", "meaning": "hàng năm, thường niên", "example": "the annual shareholders' meeting"}
        ],
        "collocations": [{"phrase": "travel to", "meaning": "đi đến (nơi nào)"}, {"phrase": "annual meeting", "meaning": "cuộc họp thường niên"}],
        "grammar": [{"title": "Giới từ chỉ phương hướng (Prepositions of Direction)", "content": "Travel to + destination: di chuyển đến địa điểm nào."}]
    },
    104: {
        "stem": "Yong-Soo Cosmetics will not charge for items on back order until ------- have left our warehouse.",
        "stemVi": "Yong-Soo Cosmetics sẽ không tính phí các mặt hàng chờ giao cho đến khi ------- rời khỏi kho của chúng tôi.",
        "options": {"A": "them", "B": "they", "C": "themselves", "D": "their"},
        "optionsVi": {"A": "chúng (tân ngữ)", "B": "chúng (chủ ngữ)", "C": "chính chúng (đại từ phản thân)", "D": "của chúng (tính từ sở hữu)"},
        "ans": "B",
        "exp": "Mệnh đề sau liên từ 'until' cần một đại từ nhân xưng làm chủ ngữ cho vị ngữ 'have left our warehouse'. Danh từ được thay thế là 'items' (số nhiều) -> chọn đại từ chủ ngữ 'they'.",
        "vocab": [
            {"word": "back order", "ipa": "/ˈbæk ˌɔː.dər/", "pos": "n", "meaning": "đơn hàng chờ nhập thêm hàng", "example": "The item is currently on back order."},
            {"word": "warehouse", "ipa": "/ˈweə.haʊs/", "pos": "n", "meaning": "kho hàng", "example": "Goods are stored in a large warehouse."}
        ],
        "collocations": [{"phrase": "on back order", "meaning": "đang chờ hàng về"}],
        "grammar": [{"title": "Đại từ nhân xưng làm chủ ngữ (Subject Pronouns)", "content": "Vị trí trước động từ chính 'have left' yêu cầu đại từ chủ ngữ 'they'."}]
    },
    105: {
        "stem": "Our premium day tour takes visitors to historic sites ------- the Aprico River.",
        "stemVi": "Chuyến tham quan trong ngày cao cấp của chúng tôi đưa du khách tới các địa điểm lịch sử ------- sông Aprico.",
        "options": {"A": "onto", "B": "since", "C": "inside", "D": "along"},
        "optionsVi": {"A": "lên trên", "B": "kể từ khi", "C": "bên trong", "D": "dọc theo"},
        "ans": "D",
        "exp": "Ngữ cảnh địa lý bên cạnh một dòng sông dùng giới từ 'along' (dọc theo): 'along the Aprico River' (dọc bờ sông Aprico) -> chọn (D).",
        "vocab": [
            {"word": "premium", "ipa": "/ˈpriː.mi.əm/", "pos": "adj", "meaning": "cao cấp, thượng hạng", "example": "premium travel package"},
            {"word": "historic", "ipa": "/hɪˈstɒr.ɪk/", "pos": "adj", "meaning": "mang tính lịch sử", "example": "historic landmark"}
        ],
        "collocations": [{"phrase": "historic sites", "meaning": "các di tích/địa điểm lịch sử"}, {"phrase": "along the river", "meaning": "dọc theo con sông"}],
        "grammar": [{"title": "Giới từ chỉ vị trí và phương hướng (along)", "content": "'Along' diễn tả sự trải dài men theo chiều dài của một con đường hoặc dòng sông."}]
    },
    106: {
        "stem": "Eighty percent of drivers surveyed said they would consider buying a vehicle that runs on -------.",
        "stemVi": "Tám mươi phần trăm tài xế được khảo sát cho biết họ sẽ cân nhắc mua một phương tiện chạy bằng -------.",
        "options": {"A": "electricity", "B": "electrically", "C": "electricians", "D": "electrify"},
        "optionsVi": {"A": "điện năng (n)", "B": "bằng điện (adv)", "C": "thợ điện (n-chỉ người)", "D": "điện khí hóa (v)"},
        "ans": "A",
        "exp": "Sau giới từ 'on' cần một danh từ chỉ nguồn năng lượng. Cụm 'run on electricity' (chạy bằng điện) là cách diễn đạt chuẩn -> chọn danh từ 'electricity'.",
        "vocab": [
            {"word": "vehicle", "ipa": "/ˈvɪə.kəl/", "pos": "n", "meaning": "phương tiện giao thông, xe cộ", "example": "electric vehicles"},
            {"word": "survey", "ipa": "/səˈveɪ/", "pos": "v", "meaning": "khảo sát", "example": "drivers surveyed about fuel consumption"}
        ],
        "collocations": [{"phrase": "run on electricity", "meaning": "chạy bằng điện năng"}],
        "grammar": [{"title": "Danh từ sau giới từ (Preposition + Noun)", "content": "Sau giới từ 'on' cần danh từ làm tân ngữ chỉ nguồn nhiên liệu."}]
    },
    107: {
        "stem": "Xinzhe Zu has ------- Petrin Engineering as the vice president of operations.",
        "stemVi": "Xinzhe Zu đã ------- công ty Kỹ thuật Petrin với tư cách là phó chủ tịch phụ trách vận hành.",
        "options": {"A": "attached", "B": "resigned", "C": "joined", "D": "combined"},
        "optionsVi": {"A": "đính kèm", "B": "từ chức", "C": "gia nhập", "D": "kết hợp"},
        "ans": "C",
        "exp": "Động từ 'join' mang nghĩa gia nhập một tổ chức/công ty: 'join Petrin Engineering' -> chọn 'joined'. 'Resigned' cần giới từ 'from'.",
        "vocab": [
            {"word": "join", "ipa": "/dʒɔɪn/", "pos": "v", "meaning": "gia nhập, tham gia", "example": "She joined the firm last month."},
            {"word": "vice president", "ipa": "/vaɪs ˈprez.ɪ.dənt/", "pos": "n", "meaning": "phó chủ tịch", "example": "vice president of operations"}
        ],
        "collocations": [{"phrase": "join a company", "meaning": "gia nhập một công ty"}],
        "grammar": [{"title": "Ngoại động từ trực tiếp (Transitive Verb)", "content": "'Join' là ngoại động từ đi kèm trực tiếp với tân ngữ chỉ công ty/tổ chức mà không cần giới từ."}]
    },
    108: {
        "stem": "Next month, Barder House Books will be holding ------- third author's hour in Cleveland.",
        "stemVi": "Tháng tới, Nhà sách Barder House sẽ tổ chức buổi giao lưu tác giả lần thứ ba của ------- tại Cleveland.",
        "options": {"A": "it", "B": "itself", "C": "its own", "D": "its"},
        "optionsVi": {"A": "nó (đại từ)", "B": "chính nó", "C": "của chính nó (cần mạo từ)", "D": "của nó (tính từ sở hữu)"},
        "ans": "D",
        "exp": "Trước cụm danh từ 'third author's hour' cần một tính từ sở hữu để chỉ sự sở hữu của 'Barder House Books' (danh từ số ít chỉ tổ chức) -> chọn 'its'.",
        "vocab": [
            {"word": "author", "ipa": "/ˈɔː.θər/", "pos": "n", "meaning": "tác giả", "example": "a best-selling author"}
        ],
        "collocations": [{"phrase": "hold an event", "meaning": "tổ chức một sự kiện"}],
        "grammar": [{"title": "Tính từ sở hữu (Possessive Adjectives)", "content": "'Its' đứng trước số thứ tự và cụm danh từ để bổ nghĩa sở hữu."}]
    },
    109: {
        "stem": "Chester's Tiles ------- expanded to a second location in Turnington.",
        "stemVi": "Chester's Tiles ------- mở rộng sang địa điểm thứ hai tại Turnington.",
        "options": {"A": "severely", "B": "usually", "C": "recently", "D": "exactly"},
        "optionsVi": {"A": "nghiêm trọng", "B": "thường xuyên", "C": "gần đây", "D": "chính xác"},
        "ans": "C",
        "exp": "Thì quá khứ đơn / hiện tại hoàn thành mô tả sự việc vừa mới xảy ra đi với trạng từ 'recently' (gần đây) -> chọn (C).",
        "vocab": [
            {"word": "recently", "ipa": "/ˈriː.sənt.li/", "pos": "adv", "meaning": "gần đây, mới đây", "example": "The company recently opened a branch."}
        ],
        "collocations": [{"phrase": "recently expanded", "meaning": "gần đây đã mở rộng"}],
        "grammar": [{"title": "Trạng từ thời gian (Adverbs of Time)", "content": "'Recently' thường dùng với thì quá khứ hoặc hiện tại hoàn thành."}]
    },
    110: {
        "stem": "Tabrino's has ------- increased the number of almonds in the Nut Medley snack pack.",
        "stemVi": "Hãng Tabrino đã tăng số lượng hạt hạnh nhân trong gói ăn vặt Nut Medley một cách -------.",
        "options": {"A": "significant", "B": "significance", "C": "signifies", "D": "significantly"},
        "optionsVi": {"A": "đáng kể (adj)", "B": "sự đáng kể (n)", "C": "báo hiệu (v)", "D": "một cách đáng kể (adv)"},
        "ans": "D",
        "exp": "Đứng giữa 'has' và động từ 'increased' cần một trạng từ chỉ mức độ để bổ nghĩa cho động từ -> chọn 'significantly' (đáng kể).",
        "vocab": [
            {"word": "significantly", "ipa": "/sɪɡˈnɪf.ɪ.kənt.li/", "pos": "adv", "meaning": "đáng kể", "example": "Sales increased significantly."},
            {"word": "almond", "ipa": "/ˈɑː.mənd/", "pos": "n", "meaning": "hạnh nhân", "example": "roasted almonds"}
        ],
        "collocations": [{"phrase": "significantly increase", "meaning": "tăng lên một cách đáng kể"}],
        "grammar": [{"title": "Trạng từ bổ nghĩa cho động từ (Adverb modifying Verb)", "content": "Has/have + adv + V3/ed là cấu trúc rất phổ biến trong đề thi TOEIC."}]
    },
    111: {
        "stem": "------- she travels, Jacintha Flores collects samples of local fabrics and patterns.",
        "stemVi": "------- cô ấy đi du lịch, Jacintha Flores đều sưu tầm các mẫu vải và hoa văn địa phương.",
        "options": {"A": "Wherever", "B": "In addition to", "C": "Either", "D": "In contrast to"},
        "optionsVi": {"A": "Bất cứ nơi nào", "B": "Ngoài ra, thêm vào", "C": "Hoặc", "D": "Trái ngược với"},
        "ans": "A",
        "exp": "Mệnh đề 'she travels' có đầy đủ chủ vị, đứng đầu câu cần một liên từ mệnh đề trạng ngữ chỉ nơi chốn: 'Wherever she travels' (Bất cứ nơi nào cô ấy đi đến) -> chọn (A). Các lựa chọn khác là giới từ cần danh từ.",
        "vocab": [
            {"word": "fabric", "ipa": "/ˈfæb.rɪk/", "pos": "n", "meaning": "vải vóc", "example": "silk and cotton fabrics"},
            {"word": "pattern", "ipa": "/ˈpæt.ən/", "pos": "n", "meaning": "hoa văn, họa tiết", "example": "geometric patterns"}
        ],
        "collocations": [{"phrase": "collect samples", "meaning": "thu thập/sưu tầm mẫu vật"}],
        "grammar": [{"title": "Mệnh đề trạng ngữ chỉ nơi chốn (Wherever + S + V)", "content": "'Wherever' đóng vai trò liên từ nối mệnh đề phụ với mệnh đề chính."}]
    },
    112: {
        "stem": "Most picture ------- at Glowing Photo Lab go on sale at 3:00 P.M. today.",
        "stemVi": "Hầu hết các ------- ảnh tại Glowing Photo Lab sẽ được giảm giá vào lúc 3 giờ chiều hôm nay.",
        "options": {"A": "framer", "B": "framing", "C": "framed", "D": "frames"},
        "optionsVi": {"A": "người đóng khung", "B": "việc đóng khung", "C": "đã đóng khung", "D": "khung (ảnh)"},
        "ans": "D",
        "exp": "Cụm danh từ ghép 'picture frames' (khung ảnh). Động từ theo sau là 'go' (nguyên mẫu số nhiều) cho thấy chủ ngữ phải là danh từ số nhiều -> chọn 'frames'.",
        "vocab": [
            {"word": "frame", "ipa": "/freɪm/", "pos": "n", "meaning": "khung (ảnh/tranh)", "example": "wooden picture frames"},
            {"word": "go on sale", "ipa": "/ɡəʊ ɒn seɪl/", "pos": "idm", "meaning": "bắt đầu được giảm giá", "example": "The items go on sale tomorrow."}
        ],
        "collocations": [{"phrase": "picture frame", "meaning": "khung ảnh"}, {"phrase": "go on sale", "meaning": "bán hạ giá"}],
        "grammar": [{"title": "Hòa hợp Chủ ngữ - Vị ngữ (Subject-Verb Agreement)", "content": "Chủ ngữ số nhiều 'Most picture frames' đi với động từ số nhiều 'go'."}]
    },
    113: {
        "stem": "All students in the business management class hold ------- college degrees.",
        "stemVi": "Tất cả các sinh viên trong lớp quản trị kinh doanh đều sở hữu bằng đại học -------.",
        "options": {"A": "late", "B": "developed", "C": "advanced", "D": "elated"},
        "optionsVi": {"A": "muộn", "B": "được phát triển", "C": "nâng cao, cao cấp", "D": "hân hoan"},
        "ans": "C",
        "exp": "Cụm danh từ cố định trong giáo dục: 'advanced degree' (bằng cấp nâng cao như Thạc sĩ, Tiến sĩ) -> chọn 'advanced'.",
        "vocab": [
            {"word": "advanced", "ipa": "/ədˈvɑːnst/", "pos": "adj", "meaning": "tiên tiến, nâng cao", "example": "an advanced degree in economics"},
            {"word": "degree", "ipa": "/dɪˈɡriː/", "pos": "n", "meaning": "bằng cấp", "example": "a bachelor's degree"}
        ],
        "collocations": [{"phrase": "advanced degree", "meaning": "bằng cấp sau đại học/nâng cao"}],
        "grammar": [{"title": "Tính từ đứng trước danh từ", "content": "'Advanced' là tính từ bổ nghĩa cho cụm danh từ 'college degrees'."}]
    },
    114: {
        "stem": "We hired Noah Wan of Shengyao Accounting Ltd. ------- our company's financial assets.",
        "stemVi": "Chúng tôi đã thuê Noah Wan từ công ty Kế toán Shengyao để ------- các tài sản tài chính của công ty chúng tôi.",
        "options": {"A": "to evaluate", "B": "to be evaluated", "C": "will be evaluated", "D": "evaluate"},
        "optionsVi": {"A": "để đánh giá", "B": "để được đánh giá", "C": "sẽ được đánh giá", "D": "đánh giá (V-bare)"},
        "ans": "A",
        "exp": "Cấu trúc 'hire someone to do something' (thuê ai đó để làm gì chỉ mục đích). Tân ngữ là 'financial assets' (chủ động) -> chọn 'to evaluate'.",
        "vocab": [
            {"word": "evaluate", "ipa": "/ɪˈvæl.ju.eɪt/", "pos": "v", "meaning": "đánh giá, định giá", "example": "evaluate company performance"},
            {"word": "assets", "ipa": "/ˈæs.ets/", "pos": "n", "meaning": "tài sản", "example": "financial assets"}
        ],
        "collocations": [{"phrase": "hire someone to do something", "meaning": "thuê ai làm việc gì"}, {"phrase": "financial assets", "meaning": "tài sản tài chính"}],
        "grammar": [{"title": "Động từ nguyên mẫu chỉ mục đích (To-infinitive of Purpose)", "content": "'hire someone + to-inf' diễn đạt mục đích thuê người đó."}]
    },
    115: {
        "stem": "Ms. Charisse is taking on a new account ------- she finishes the Morrison project.",
        "stemVi": "Bà Charisse sẽ đảm nhận một khách hàng mới ------- bà ấy hoàn thành dự án Morrison.",
        "options": {"A": "with", "B": "going", "C": "after", "D": "between"},
        "optionsVi": {"A": "với", "B": "đi", "C": "sau khi", "D": "ở giữa"},
        "ans": "C",
        "exp": "Nối hai mệnh đề chỉ trình tự thời gian: 'taking on a new account' diễn ra sau khi 'she finishes the Morrison project' -> dùng liên từ 'after' (sau khi).",
        "vocab": [
            {"word": "take on", "ipa": "/teɪk ɒn/", "pos": "phr v", "meaning": "đảm nhận, gánh vác", "example": "take on new responsibilities"},
            {"word": "account", "ipa": "/əˈkaʊnt/", "pos": "n", "meaning": "hợp đồng khách hàng", "example": "win a major advertising account"}
        ],
        "collocations": [{"phrase": "take on an account", "meaning": "nhận phụ trách một khách hàng"}],
        "grammar": [{"title": "Mệnh đề trạng ngữ chỉ thời gian (Time Clauses)", "content": "Trong mệnh đề thời gian sau 'after', động từ chia ở thì hiện tại đơn khi diễn tả tương lai."}]
    },
    116: {
        "stem": "Cormet Motors' profits are ------- this year than last year.",
        "stemVi": "Lợi nhuận của Cormet Motors năm nay ------- so với năm ngoái.",
        "options": {"A": "higher", "B": "high", "C": "highly", "D": "highest"},
        "optionsVi": {"A": "cao hơn", "B": "cao", "C": "rất, hết sức", "D": "cao nhất"},
        "ans": "A",
        "exp": "Có từ 'than' báo hiệu cấu trúc so sánh hơn của tính từ ngắn 'high' -> chọn 'higher'.",
        "vocab": [
            {"word": "profit", "ipa": "/ˈprɒf.ɪt/", "pos": "n", "meaning": "lợi nhuận", "example": "operating profits"}
        ],
        "collocations": [{"phrase": "higher than", "meaning": "cao hơn so với"}],
        "grammar": [{"title": "So sánh hơn của tính từ ngắn (Comparative Adjectives)", "content": "adj + -er + than."}]
    },
    117: {
        "stem": "In its ------- advertising campaign, Jaymor Tools demonstrates how reliable its products are.",
        "stemVi": "Trong chiến dịch quảng cáo ------- của mình, Jaymor Tools chứng minh các sản phẩm của hãng đáng tin cậy như thế nào.",
        "options": {"A": "current", "B": "relative", "C": "spacious", "D": "collected"},
        "optionsVi": {"A": "hiện tại", "B": "tương đối", "C": "rộng rãi", "D": "thu thập được"},
        "ans": "A",
        "exp": "Cụm danh từ 'advertising campaign' kết hợp với tính từ 'current' (hiện tại) tạo thành 'current advertising campaign' (chiến dịch quảng cáo hiện tại).",
        "vocab": [
            {"word": "current", "ipa": "/ˈkʌr.ənt/", "pos": "adj", "meaning": "hiện tại, đang lưu hành", "example": "under current market conditions"},
            {"word": "reliable", "ipa": "/rɪˈlaɪ.ə.bəl/", "pos": "adj", "meaning": "đáng tin cậy", "example": "reliable machinery"}
        ],
        "collocations": [{"phrase": "advertising campaign", "meaning": "chiến dịch quảng cáo"}],
        "grammar": [{"title": "Tính từ bổ nghĩa cho danh từ", "content": "Tính từ 'current' đứng trước bổ nghĩa cho cụm danh từ 'advertising campaign'."}]
    },
    118: {
        "stem": "Remember to submit receipts for reimbursement ------- returning from a business trip.",
        "stemVi": "Hãy nhớ nộp hóa đơn để được hoàn tiền ------- trở về từ chuyến công tác.",
        "options": {"A": "such as", "B": "when", "C": "then", "D": "within"},
        "optionsVi": {"A": "chẳng hạn như", "B": "khi", "C": "sau đó", "D": "trong vòng"},
        "ans": "B",
        "exp": "Rút gọn mệnh đề trạng ngữ cùng chủ ngữ dạng 'when + V-ing': 'when returning from a business trip' (khi trở về từ chuyến công tác) -> chọn 'when'.",
        "vocab": [
            {"word": "reimbursement", "ipa": "/ˌriː.ɪmˈbɜːs.mənt/", "pos": "n", "meaning": "sự hoàn tiền, bồi hoàn", "example": "claim reimbursement for travel expenses"},
            {"word": "receipt", "ipa": "/rɪˈsiːt/", "pos": "n", "meaning": "biên lai, hóa đơn", "example": "keep your sales receipts"}
        ],
        "collocations": [{"phrase": "submit receipts", "meaning": "nộp hóa đơn"}, {"phrase": "business trip", "meaning": "chuyến công tác"}],
        "grammar": [{"title": "Rút gọn mệnh đề trạng ngữ (when + V-ing)", "content": "Khi hai mệnh đề có cùng chủ ngữ, có thể lược bỏ chủ ngữ và biến động từ thành V-ing sau liên từ chỉ thời gian 'when'."}]
    },
    119: {
        "stem": "Patrons will be able to access Westside Library's ------- acquired collection of books on Tuesday.",
        "stemVi": "Các độc giả sẽ có thể tiếp cận bộ sưu tập sách ------- được bổ sung của Thư viện Westside vào thứ Ba.",
        "options": {"A": "instantly", "B": "newly", "C": "early", "D": "naturally"},
        "optionsVi": {"A": "ngay lập tức", "B": "mới (được)", "C": "sớm", "D": "tự nhiên"},
        "ans": "B",
        "exp": "Cụm 'newly acquired' là collocation chuẩn miêu tả thứ gì đó vừa mới được thu nhận, mua lại hay bổ sung -> chọn trạng từ 'newly'.",
        "vocab": [
            {"word": "patron", "ipa": "/ˈpeɪ.trən/", "pos": "n", "meaning": "khách hàng quen, độc giả thư viện", "example": "library patrons"},
            {"word": "acquire", "ipa": "/əˈkwaɪər/", "pos": "v", "meaning": "mua được, có được", "example": "newly acquired collection"}
        ],
        "collocations": [{"phrase": "newly acquired", "meaning": "mới mua được/mới tiếp nhận"}],
        "grammar": [{"title": "Trạng từ bổ nghĩa cho quá khứ phân từ (Adv + Past Participle)", "content": "'newly' đóng vai trò trạng từ bổ nghĩa cho tính từ phân từ 'acquired'."}]
    },
    120: {
        "stem": "Please ------- any questions about time sheets to Tabitha Jones in the payroll department.",
        "stemVi": "Vui lòng ------- bất kỳ thắc mắc nào về bảng chấm công đến cô Tabitha Jones ở bộ phận tính lương.",
        "options": {"A": "direction", "B": "directive", "C": "directed", "D": "direct"},
        "optionsVi": {"A": "phương hướng (n)", "B": "chỉ thị (adj/n)", "C": "đã chuyển (v-ed)", "D": "chuyển tiếp, hướng dẫn (v-bare)"},
        "ans": "D",
        "exp": "Sau 'Please' trong câu mệnh lệnh cần động từ nguyên mẫu: 'Please direct questions to someone' (vui lòng chuyển câu hỏi đến ai) -> chọn 'direct'.",
        "vocab": [
            {"word": "direct", "ipa": "/daɪˈrekt/", "pos": "v", "meaning": "gửi tới, hướng tới", "example": "Direct inquiries to the helpdesk."},
            {"word": "payroll", "ipa": "/ˈpeɪ.rəʊl/", "pos": "n", "meaning": "bảng lương, bộ phận tính lương", "example": "the payroll department"}
        ],
        "collocations": [{"phrase": "direct questions to", "meaning": "chuyển các câu hỏi tới (ai)"}],
        "grammar": [{"title": "Câu mệnh lệnh với Please + V-inf", "content": "Động từ 'direct' ở dạng nguyên mẫu không 'to' sau 'Please'."}]
    },
    121: {
        "stem": "Before signing a delivery -------, be sure to double-check that all the items ordered are in the shipment.",
        "stemVi": "Trước khi ký vào ------- giao hàng, hãy nhớ kiểm tra lại kỹ lưỡng để đảm bảo rằng tất cả các mặt hàng đã đặt đều có trong kiện hàng.",
        "options": {"A": "decision", "B": "announcement", "C": "receipt", "D": "limit"},
        "optionsVi": {"A": "quyết định", "B": "thông báo", "C": "biên nhận, giấy biên nhận", "D": "giới hạn"},
        "ans": "C",
        "exp": "Cụm danh từ 'delivery receipt' nghĩa là biên nhận giao nhận hàng (chứng từ ký nhận khi nhận hàng) -> chọn 'receipt'.",
        "vocab": [
            {"word": "receipt", "ipa": "/rɪˈsiːt/", "pos": "n", "meaning": "giấy biên nhận, biên lai", "example": "sign the delivery receipt"},
            {"word": "double-check", "ipa": "/ˌdʌb.əlˈtʃek/", "pos": "v", "meaning": "kiểm tra lại kỹ càng", "example": "Always double-check your work."}
        ],
        "collocations": [{"phrase": "delivery receipt", "meaning": "biên lai/biên nhận giao hàng"}],
        "grammar": [{"title": "Cụm danh từ ghép (Compound Nouns)", "content": "'Delivery' (danh từ/danh từ bổ nghĩa) + 'receipt' (danh từ chính)."}]
    },
    122: {
        "stem": "Funds have been added to the budget for expenses ------- with the new building.",
        "stemVi": "Tiền đã được bổ sung vào ngân sách cho các chi phí ------- với tòa nhà mới.",
        "options": {"A": "associated", "B": "association", "C": "associate", "D": "associates"},
        "optionsVi": {"A": "gắn liền, liên quan (v-ed)", "B": "sự liên kết (n)", "C": "liên kết (v)", "D": "các cộng sự (n-số nhiều)"},
        "ans": "A",
        "exp": "Rút gọn mệnh đề quan hệ dạng bị động: 'expenses [which are] associated with...' -> chọn quá khứ phân từ 'associated'. Cụm 'associated with' mang nghĩa liên quan/gắn liền với.",
        "vocab": [
            {"word": "associated", "ipa": "/əˈsəʊ.si.eɪ.tɪd/", "pos": "adj", "meaning": "liên quan, gắn liền", "example": "costs associated with the project"},
            {"word": "budget", "ipa": "/ˈbʌdʒ.ɪt/", "pos": "n", "meaning": "ngân sách", "example": "within the operating budget"}
        ],
        "collocations": [{"phrase": "expenses associated with", "meaning": "chi phí gắn liền với"}],
        "grammar": [{"title": "Rút gọn mệnh đề quan hệ bị động (Reduced Relative Clauses)", "content": "N + V3/ed thay cho N + which/that + be + V3/ed."}]
    },
    123: {
        "stem": "Ms. Bernard ------- that a deadline was approaching, so she requested some assistance.",
        "stemVi": "Bà Bernard ------- rằng thời hạn chót đang đến gần, vì vậy bà đã yêu cầu sự trợ giúp.",
        "options": {"A": "noticed", "B": "obscured", "C": "withdrew", "D": "appeared"},
        "optionsVi": {"A": "nhận thấy", "B": "che khuất", "C": "rút lui", "D": "xuất hiện"},
        "ans": "A",
        "exp": "Ngữ cảnh bà ấy nhận thấy hạn chót sắp đến nên mới yêu cầu giúp đỡ -> chọn 'noticed' (nhận thấy).",
        "vocab": [
            {"word": "notice", "ipa": "/ˈnəʊ.tɪs/", "pos": "v", "meaning": "nhận thấy, chú ý", "example": "She noticed that the light was on."},
            {"word": "assistance", "ipa": "/əˈsɪs.təns/", "pos": "n", "meaning": "sự trợ giúp", "example": "request technical assistance"}
        ],
        "collocations": [{"phrase": "request assistance", "meaning": "yêu cầu sự giúp đỡ"}],
        "grammar": [{"title": "Động từ theo sau bởi mệnh đề That (Verb + that-clause)", "content": "Notice that + S + V diễn tả việc nhận thức được một sự việc."}]
    },
    124: {
        "stem": "Mr. Moscowitz is ------- that Dr. Tanaka will agree to present the keynote speech at this year's conference.",
        "stemVi": "Ông Moscowitz ------- rằng Tiến sĩ Tanaka sẽ đồng ý phát biểu đề dẫn tại hội nghị năm nay.",
        "options": {"A": "hopes", "B": "hoped", "C": "hopeful", "D": "hopefully"},
        "optionsVi": {"A": "hy vọng (v)", "B": "đã hy vọng (v-ed)", "C": "tràn trề hy vọng (adj)", "D": "đầy hy vọng (adv)"},
        "ans": "C",
        "exp": "Sau động từ to be 'is' cần một tính từ chỉ thái độ của chủ ngữ: 'be hopeful that...' (hy vọng rằng...) -> chọn 'hopeful'.",
        "vocab": [
            {"word": "hopeful", "ipa": "/ˈhəʊp.fəl/", "pos": "adj", "meaning": "đầy hy vọng, lạc quan", "example": "We are hopeful of a positive outcome."},
            {"word": "keynote speech", "ipa": "/ˈkiː.nəʊt spiːtʃ/", "pos": "n", "meaning": "bài phát biểu chủ đề/đề dẫn", "example": "deliver the keynote speech"}
        ],
        "collocations": [{"phrase": "keynote speech", "meaning": "bài diễn văn then chốt/chủ đạo"}],
        "grammar": [{"title": "Tính từ sau to be (Linking Verb + Adjective)", "content": "Be + hopeful that + clause."}]
    },
    125: {
        "stem": "Two Australian companies are developing new smartphones, but it is unclear ------- phone will become available first.",
        "stemVi": "Hai công ty Úc đang phát triển các dòng điện thoại thông minh mới, nhưng vẫn chưa rõ chiếc điện thoại ------- sẽ ra mắt trước.",
        "options": {"A": "if", "B": "which", "C": "before", "D": "because"},
        "optionsVi": {"A": "liệu rằng", "B": "nào (lựa chọn)", "C": "trước khi", "D": "bởi vì"},
        "ans": "B",
        "exp": "Đại từ/từ hạn định nghi vấn chỉ sự lựa chọn trong một nhóm giới hạn (ở đây là 2 công ty) đứng trước danh từ 'phone' -> dùng 'which' ('which phone': chiếc điện thoại nào).",
        "vocab": [
            {"word": "unclear", "ipa": "/ʌnˈklɪər/", "pos": "adj", "meaning": "chưa rõ ràng", "example": "It is unclear what caused the delay."}
        ],
        "collocations": [{"phrase": "become available", "meaning": "trở nên có sẵn/ra mắt"}],
        "grammar": [{"title": "Từ hạn định nghi vấn Which (Wh-determiner)", "content": "'Which' dùng khi có sự lựa chọn giữa các đối tượng đã được xác định trước."}]
    },
    126: {
        "stem": "Corners Gym offers its members a free lesson in how to use ------- properly.",
        "stemVi": "Phòng tập Corners Gym tặng các hội viên một buổi học miễn phí về cách sử dụng ------- đúng cách.",
        "options": {"A": "weighs", "B": "weights", "C": "weighty", "D": "weighed"},
        "optionsVi": {"A": "cân nặng (v)", "B": "tạ tập thể hình (n-số nhiều)", "C": "nặng nề (adj)", "D": "đã cân (v-ed)"},
        "ans": "B",
        "exp": "Sau ngoại động từ 'use' cần một danh từ làm tân ngữ. Trong phòng gym, 'weights' là danh từ chỉ các loại tạ tập thể hình -> chọn 'weights'.",
        "vocab": [
            {"word": "weights", "ipa": "/weɪts/", "pos": "n", "meaning": "tạ tập thể hình", "example": "lift weights at the gym"},
            {"word": "properly", "ipa": "/ˈprɒp.əl.i/", "pos": "adv", "meaning": "đúng cách, hợp lý", "example": "make sure equipment is used properly"}
        ],
        "collocations": [{"phrase": "use properly", "meaning": "sử dụng đúng cách"}],
        "grammar": [{"title": "Tân ngữ trực tiếp của động từ (Direct Object)", "content": "Verb + noun: 'use weights' (tập với tạ)."}]
    },
    127: {
        "stem": "------- the rules, overnight parking is not permitted at the clubhouse facility.",
        "stemVi": "------- các quy định, việc đỗ xe qua đêm không được phép tại cơ sở nhà câu lạc bộ.",
        "options": {"A": "Prior to", "B": "Except for", "C": "Instead of", "D": "According to"},
        "optionsVi": {"A": "Trước khi", "B": "Ngoại trừ", "C": "Thay vì", "D": "Theo như"},
        "ans": "D",
        "exp": "Cụm giới từ chỉ nguồn thông tin hoặc căn cứ quy định: 'According to the rules' (Theo như quy định) -> chọn 'According to'.",
        "vocab": [
            {"word": "overnight", "ipa": "/ˌəʊ.vəˈnaɪt/", "pos": "adj/adv", "meaning": "qua đêm", "example": "overnight parking"},
            {"word": "permitted", "ipa": "/pəˈmɪt.ɪd/", "pos": "adj", "meaning": "được cho phép", "example": "Smoking is not permitted."}
        ],
        "collocations": [{"phrase": "according to the rules", "meaning": "theo đúng quy định"}],
        "grammar": [{"title": "Cụm giới từ chỉ căn cứ (According to + Noun)", "content": "'According to' dùng để dẫn chiếu nguồn thông tin, điều luật."}]
    },
    128: {
        "stem": "Once everyone -------, we can begin the conference call.",
        "stemVi": "Một khi mọi người -------, chúng ta có thể bắt đầu cuộc gọi hội nghị.",
        "options": {"A": "arrived", "B": "is arriving", "C": "to arrive", "D": "has arrived"},
        "optionsVi": {"A": "đã đến (quá khứ)", "B": "đang đến", "C": "để đến", "D": "đã đến nơi (hiện tại hoàn thành)"},
        "ans": "D",
        "exp": "Trong mệnh đề trạng ngữ chỉ thời gian với liên từ 'Once', để diễn tả hành động hoàn tất trước hành động ở mệnh đề chính (can begin), ta dùng thì hiện tại hoàn thành 'has arrived'. Lưu ý 'everyone' là đại từ bất định đi với động từ số ít 'has'.",
        "vocab": [
            {"word": "conference call", "ipa": "/ˈkɒn.fər.əns kɔːl/", "pos": "n", "meaning": "cuộc gọi hội nghị qua điện thoại", "example": "schedule a conference call"}
        ],
        "collocations": [{"phrase": "conference call", "meaning": "cuộc gọi họp từ xa"}],
        "grammar": [{"title": "Mệnh đề thời gian với Once và sự hòa hợp số ít của Everyone", "content": "'Once + S + has/have + V3/ed'. 'Everyone' luôn đi với động từ chia số ít (has arrived)."}]
    },
    129: {
        "stem": "Each summer a motivational video that highlights the past year's ------- is shown to all company employees.",
        "stemVi": "Mỗi mùa hè, một video truyền cảm hứng nêu bật những ------- trong năm qua sẽ được chiếu cho toàn thể nhân viên công ty.",
        "options": {"A": "preferences", "B": "accomplishments", "C": "communications", "D": "uncertainties"},
        "optionsVi": {"A": "sở thích", "B": "thành tựu, thành tích", "C": "sự giao tiếp", "D": "sự bất định"},
        "ans": "B",
        "exp": "Video truyền cảm hứng trong công ty nêu bật các 'thành tựu' đã đạt được trong năm qua -> chọn danh từ 'accomplishments'.",
        "vocab": [
            {"word": "accomplishment", "ipa": "/əˈkʌm.plɪʃ.mənt/", "pos": "n", "meaning": "thành tựu, thành tích", "example": "highlight employee accomplishments"},
            {"word": "motivational", "ipa": "/ˌməʊ.tɪˈveɪ.ʃən.əl/", "pos": "adj", "meaning": "truyền cảm hứng, tạo động lực", "example": "a motivational speaker"}
        ],
        "collocations": [{"phrase": "past year's accomplishments", "meaning": "những thành tựu của năm vừa qua"}],
        "grammar": [{"title": "Sở hữu cách với danh từ (Noun's + Noun)", "content": "The past year's + danh từ (accomplishments)."}]
    },
    130: {
        "stem": "Employees who wish to attend the retirement dinner ------- Ms. Howell's 30 years of service should contact Mr. Lee.",
        "stemVi": "Những nhân viên muốn tham dự bữa tiệc về hưu để ------- 30 năm cống hiến của bà Howell nên liên hệ với ông Lee.",
        "options": {"A": "honor", "B": "to honor", "C": "will honor", "D": "will be honored"},
        "optionsVi": {"A": "tôn vinh (v-bare)", "B": "để tôn vinh (to-V)", "C": "sẽ tôn vinh", "D": "sẽ được tôn vinh"},
        "ans": "B",
        "exp": "Động từ nguyên mẫu có 'to' chỉ mục đích của bữa tiệc về hưu: bữa tiệc được tổ chức 'để vinh danh' (to honor) 30 năm cống hiến -> chọn 'to honor'.",
        "vocab": [
            {"word": "honor", "ipa": "/ˈɒn.ər/", "pos": "v", "meaning": "vinh danh, tôn vinh", "example": "a banquet to honor retiring staff"},
            {"word": "retirement", "ipa": "/rɪˈtaɪə.mənt/", "pos": "n", "meaning": "sự về hưu", "example": "retirement dinner"}
        ],
        "collocations": [{"phrase": "retirement dinner", "meaning": "tiệc mừng về hưu"}, {"phrase": "years of service", "meaning": "nhiều năm cống hiến"}],
        "grammar": [{"title": "To-infinitive chỉ mục đích (Purpose)", "content": "Dinner + to honor: bữa tiệc nhằm mục đích vinh danh."}]
    }
}

for qid, info in p5_data.items():
    q = q_map[qid]
    q["part"] = 5
    q["partName"] = "Part 5: Incomplete Sentences"
    q["questionText"] = info["stem"]
    q["questionTextVi"] = info["stemVi"]
    q["options"] = info["options"]
    q["optionsVi"] = info["optionsVi"]
    q["correctAnswer"] = info["ans"]
    q["explanation"] = info["exp"]
    q["vocabulary"] = info["vocab"]
    q["collocations"] = info["collocations"]
    q["grammar"] = info["grammar"]

print("Part 5 perfected!")

# ==========================================
# 4. PART 6 (Q131 - Q146) REBUILD PASSAGES
# ==========================================
p6_passages = {
    "p6_1": {
        "title": "E-mail: Order Update from Dellwyn Home Store",
        "pageImage": "assets/images/test2/rc_page_5.png",
        "text": "To: Myung-Hee Hahn\nFrom: Dellwyn Home Store\nDate: January 15\nSubject: Order update\n\nDear Ms. Hahn,\nYour order of a red oak dining table and six matching chairs arrived at our store this morning. This was a [131] order because it required custom woodworking. We would now like to arrange for the delivery of the [132]. Please call us at 517-555-0188 and ask [133] Coleman Cobb, our delivery manager. [134].\n\nCustomer Service,\nDellwyn Home Store",
        "textVi": "Người nhận: Myung-Hee Hahn\nNgười gửi: Cửa hàng Đồ gỗ Gia đình Dellwyn\nNgày: 15 tháng 1\nTiêu đề: Cập nhật đơn hàng\n\nKính gửi bà Hahn,\nĐơn đặt hàng bàn ăn gỗ sồi đỏ và sáu chiếc ghế đồng bộ của bà đã được chuyển tới cửa hàng chúng tôi sáng nay. Đây là một đơn hàng [131] vì nó yêu cầu gia công gỗ theo yêu cầu riêng. Hiện tại chúng tôi muốn sắp xếp việc giao số [132] này. Vui lòng gọi cho chúng tôi theo số 517-555-0188 và yêu cầu [133] ông Coleman Cobb, người quản lý giao hàng của chúng tôi. [134].\n\nBộ phận Chăm sóc Khách hàng,\nCửa hàng Đồ gỗ Dellwyn",
        "questions": {
            131: {
                "stem": "Select the best answer for blank [131]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [131]:",
                "options": {"A": "specially", "B": "specialize", "C": "special", "D": "specializing"},
                "optionsVi": {"A": "đặc biệt (adv)", "B": "chuyên về (v)", "C": "đặc biệt (adj)", "D": "chuyên về (v-ing)"},
                "ans": "C",
                "exp": "Trước danh từ 'order' cần một tính từ bổ nghĩa: 'special order' (đơn đặt hàng đặc biệt/đơn làm riêng) -> chọn (C).",
                "vocab": [{"word": "custom", "ipa": "/ˈkʌs.təm/", "pos": "adj", "meaning": "làm theo đơn đặt hàng riêng", "example": "custom woodworking"}],
                "collocations": [{"phrase": "special order", "meaning": "đơn đặt hàng đặc biệt"}],
                "grammar": [{"title": "Tính từ đứng trước danh từ", "content": "a/an + adj + noun: a special order."}]
            },
            132: {
                "stem": "Select the best answer for blank [132]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [132]:",
                "options": {"A": "furniture", "B": "appliances", "C": "refund", "D": "tools"},
                "optionsVi": {"A": "đồ nội thất", "B": "thiết bị gia dụng", "C": "tiền hoàn trả", "D": "dụng cụ"},
                "ans": "A",
                "exp": "Đoạn trước đề cập 'dining table and six matching chairs' (bàn ăn và 6 ghế). Danh từ chung bao quát nhóm này là 'furniture' (đồ nội thất) -> chọn (A).",
                "vocab": [{"word": "furniture", "ipa": "/ˈfɜː.nɪ.tʃər/", "pos": "n", "meaning": "đồ nội thất", "example": "wooden furniture"}],
                "collocations": [{"phrase": "delivery of the furniture", "meaning": "việc giao đồ nội thất"}],
                "grammar": [{"title": "Danh từ không đếm được (Uncountable Nouns)", "content": "'Furniture' là danh từ không đếm được dùng để chỉ chung bàn ghế, giường tủ."}]
            },
            133: {
                "stem": "Select the best answer for blank [133]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [133]:",
                "options": {"A": "speak", "B": "spoken", "C": "is speaking", "D": "to speak"},
                "optionsVi": {"A": "nói (v-bare)", "B": "đã nói (V3)", "C": "đang nói", "D": "để nói chuyện (to-V)"},
                "ans": "D",
                "exp": "Cấu trúc 'ask to speak with/to someone' (yêu cầu được nói chuyện với ai) -> chọn 'to speak' (D).",
                "vocab": [{"word": "delivery manager", "ipa": "/dɪˈlɪv.ər.i ˈmæn.ɪ.dʒər/", "pos": "n", "meaning": "quản lý giao nhận", "example": "contact the delivery manager"}],
                "collocations": [{"phrase": "ask to speak to someone", "meaning": "yêu cầu được nói chuyện với ai"}],
                "grammar": [{"title": "Động từ theo sau bởi to-inf (Verb + to-infinitive)", "content": "'Ask to do something': yêu cầu xin phép được làm gì."}]
            },
            134: {
                "stem": "Select the best answer for blank [134]:",
                "stemVi": "Chọn câu văn phù hợp nhất cho chỗ trống [134]:",
                "options": {
                    "A": "He can schedule a convenient time.",
                    "B": "He began working here yesterday.",
                    "C": "He can meet you at 11 A.M.",
                    "D": "He recently moved to Dellwyn."
                },
                "optionsVi": {
                    "A": "Anh ấy có thể sắp xếp một khung giờ thuận tiện.",
                    "B": "Anh ấy mới bắt đầu làm việc tại đây hôm qua.",
                    "C": "Anh ấy có thể gặp bạn lúc 11 giờ sáng.",
                    "D": "Anh ấy mới chuyển đến Dellwyn gần đây."
                },
                "ans": "A",
                "exp": "Câu trước khuyên khách hàng gọi điện gặp người quản lý giao hàng. Câu tiếp nối hợp lý nhất là giải thích người này có thể lên lịch hẹn giao hàng phù hợp cho khách -> chọn (A).",
                "vocab": [{"word": "convenient", "ipa": "/kənˈviː.ni.ənt/", "pos": "adj", "meaning": "thuận tiện", "example": "a convenient time"}],
                "collocations": [{"phrase": "schedule a convenient time", "meaning": "sắp xếp thời gian thuận tiện"}],
                "grammar": [{"title": "Tính mạch lạc của đoạn văn (Coherence)", "content": "Câu được chọn phát triển tiếp ý về việc lên lịch giao nhận đồ nội thất."}]
            }
        }
    },
    "p6_2": {
        "title": "Advertisement: Keep Cool Service Contractors",
        "pageImage": "assets/images/test2/rc_page_6.png",
        "text": "Keep Cool Service Contractors:\n67 Main Road, Edinburgh Village\nChaguanas, Trinidad and Tobago\n\nKeep Cool Service Contractors can bring you peace of mind. As part of an annual contract, we will service your air-conditioning system, ensuring your [135] and comfort. This includes inspecting the system, making repairs as needed, and professionally cleaning your air ducts. [136] if necessary, we can replace your old air-conditioning system with a new, cost-efficient one. Our workers are highly qualified licensed technicians who stay up-to-date with ongoing training. [137]. We promise you fair prices and professional work, [138] by our Keep Cool guarantee.\n\nCall 1-868-555-0129 for a free quote today.",
        "textVi": "Nhà thầu Dịch vụ Keep Cool:\n67 Main Road, Edinburgh Village\nChaguanas, Trinidad and Tobago\n\nNhà thầu Dịch vụ Keep Cool có thể mang lại cho bạn sự an tâm tuyệt đối. Là một phần của hợp đồng thường niên, chúng tôi sẽ bảo dưỡng hệ thống điều hòa không khí của bạn, đảm bảo sự [135] và tiện nghi của bạn. Dịch vụ bao gồm kiểm tra hệ thống, sửa chữa khi cần thiết và vệ sinh đường ống dẫn khí một cách chuyên nghiệp. [136] nếu cần thiết, chúng tôi có thể thay thế hệ thống điều hòa cũ của bạn bằng hệ thống mới tiết kiệm chi phí. Đội ngũ nhân viên của chúng tôi là những kỹ thuật viên có chứng chỉ chuyên môn cao và luôn cập nhật kiến thức qua các khóa đào tạo liên tục. [137]. Chúng tôi cam kết mức giá hợp lý và tác phong chuyên nghiệp, được [138] bởi sự bảo đảm Keep Cool của chúng tôi.\n\nHãy gọi 1-868-555-0129 để nhận báo giá miễn phí ngay hôm nay.",
        "questions": {
            135: {
                "stem": "Select the best answer for blank [135]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [135]:",
                "options": {"A": "safe", "B": "safely", "C": "safest", "D": "safety"},
                "optionsVi": {"A": "an toàn (adj)", "B": "một cách an toàn (adv)", "C": "an toàn nhất", "D": "sự an toàn (n)"},
                "ans": "D",
                "exp": "Cấu trúc song hành qua liên từ 'and': 'your [135] and comfort'. 'Comfort' là danh từ nên vị trí [135] cũng phải là một danh từ -> chọn 'safety' (sự an toàn).",
                "vocab": [{"word": "comfort", "ipa": "/ˈkʌm.fət/", "pos": "n", "meaning": "sự tiện nghi, thoải mái", "example": "ensure passenger comfort"}],
                "collocations": [{"phrase": "safety and comfort", "meaning": "sự an toàn và tiện nghi"}],
                "grammar": [{"title": "Cấu trúc song hành (Parallel Structure)", "content": "Noun + and + Noun: safety and comfort."}]
            },
            136: {
                "stem": "Select the best answer for blank [136]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [136]:",
                "options": {"A": "On one hand", "B": "Nonetheless", "C": "Furthermore", "D": "And yet"},
                "optionsVi": {"A": "Một mặt", "B": "Dẫu vậy", "C": "Hơn nữa, ngoài ra", "D": "Tuy nhiên"},
                "ans": "C",
                "exp": "Bổ sung thêm một dịch vụ giá trị gia tăng khác (thay thế hệ thống cũ bằng hệ thống mới) -> dùng từ nối bổ sung ý 'Furthermore' (Hơn thế nữa).",
                "vocab": [{"word": "cost-efficient", "ipa": "/ˌkɒst.ɪˈfɪʃ.ənt/", "pos": "adj", "meaning": "tiết kiệm chi phí, hiệu quả kinh tế", "example": "cost-efficient cooling systems"}],
                "collocations": [{"phrase": "if necessary", "meaning": "nếu cần thiết"}],
                "grammar": [{"title": "Liên từ nối bổ sung thông tin (Transition Words of Addition)", "content": "'Furthermore' dùng để đưa thêm thông tin củng cố cho ý trước đó."}]
            },
            137: {
                "stem": "Select the best answer for blank [137]:",
                "stemVi": "Chọn câu văn phù hợp nhất cho chỗ trống [137]:",
                "options": {
                    "A": "Take advantage of dozens of useful online tools.",
                    "B": "Moreover, the air conditioner you chose is very popular.",
                    "C": "Plus, they are friendly, clean, and knowledgeable.",
                    "D": "Thank you for visiting our contractor showroom."
                },
                "optionsVi": {
                    "A": "Hãy tận dụng hàng tá công cụ trực tuyến hữu ích.",
                    "B": "Hơn nữa, chiếc máy điều hòa bạn chọn rất được ưa chuộng.",
                    "C": "Thêm vào đó, họ rất thân thiện, sạch sẽ và am hiểu chuyên môn.",
                    "D": "Cảm ơn bạn đã ghé thăm phòng trưng bày nhà thầu của chúng tôi."
                },
                "ans": "C",
                "exp": "Câu trước nói về 'Our workers are highly qualified licensed technicians...' (Công nhân của chúng tôi là thợ có bằng cấp...). Câu bổ sung đặc điểm tính cách của công nhân 'Plus, they are friendly, clean, and knowledgeable' (Hơn nữa, họ rất thân thiện, gọn gàng và am hiểu) -> chọn (C).",
                "vocab": [{"word": "knowledgeable", "ipa": "/ˈnɒl.ɪ.dʒə.bəl/", "pos": "adj", "meaning": "am hiểu, có kiến thức sâu rộng", "example": "knowledgeable staff"}],
                "collocations": [{"phrase": "licensed technician", "meaning": "kỹ thuật viên có chứng chỉ"}],
                "grammar": [{"title": "Tính liên kết đại từ (Pronoun Reference)", "content": "'They' ở câu (C) thay thế chuẩn xác cho danh từ số nhiều 'Our workers' ở câu trước."}]
            },
            138: {
                "stem": "Select the best answer for blank [138]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [138]:",
                "options": {"A": "backed", "B": "backs", "C": "backing", "D": "back"},
                "optionsVi": {"A": "được bảo đảm/hậu thuẫn (V3)", "B": "hậu thuẫn (ngôi 3 số ít)", "C": "đang hậu thuẫn (v-ing)", "D": "trở lại, lưng"},
                "ans": "A",
                "exp": "Rút gọn mệnh đề quan hệ dạng bị động: 'work, [which is] backed by our Keep Cool guarantee' (công việc được bảo đảm bởi...) -> chọn quá khứ phân từ 'backed'.",
                "vocab": [{"word": "guarantee", "ipa": "/ˌɡær.ənˈtiː/", "pos": "n", "meaning": "sự bảo đảm, cam kết", "example": "money-back guarantee"}],
                "collocations": [{"phrase": "backed by", "meaning": "được đảm bảo/hậu thuẫn bởi"}],
                "grammar": [{"title": "Phân từ hai bị động (Past Participle as Reduced Relative Clause)", "content": "Noun + backed by: danh từ được bảo chứng bởi điều gì."}]
            }
        }
    },
    "p6_3": {
        "title": "E-mail: Information on Price Increase from Light Idea",
        "pageImage": "assets/images/test2/rc_page_7.png",
        "text": "To: All Customers\nFrom: asquires@lightidea.com\nDate: March 6\nSubject: Information\n\nDear Light Idea Customers,\nLight Idea is enacting a price increase on select energy-efficient products, effective April 17. Specific product pricing will [139]. Please contact your sales representative for details and questions. The last date for ordering at current prices is April 16. All orders [140] after this date will follow the new price list. [141]. We will continue to provide quality products and [142] service to our valued customers. Thank you for your business.\n\nSincerely,\nArvin Squires\nHead of Sales, Light Idea",
        "textVi": "Người nhận: Toàn thể Khách hàng\nNgười gửi: asquires@lightidea.com\nNgày: 6 tháng 3\nTiêu đề: Thông tin\n\nKính gửi Quý khách hàng của Light Idea,\nLight Idea sẽ áp dụng mức tăng giá đối với một số sản phẩm tiết kiệm năng lượng chọn lọc, có hiệu lực từ ngày 17 tháng 4. Mức giá cụ thể của từng sản phẩm sẽ [139]. Vui lòng liên hệ với đại diện bán hàng của bạn để biết chi tiết và giải đáp thắc mắc. Ngày cuối cùng để đặt hàng theo giá hiện tại là ngày 16 tháng 4. Tất cả các đơn hàng [140] sau ngày này sẽ áp dụng theo bảng giá mới. [141]. Chúng tôi sẽ tiếp tục cung cấp các sản phẩm chất lượng và dịch vụ [142] tới quý khách hàng trân quý. Cảm ơn sự hợp tác của bạn.\n\nTrân trọng,\nArvin Squires\nTrưởng bộ phận Bán hàng, Light Idea",
        "questions": {
            139: {
                "stem": "Select the best answer for blank [139]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [139]:",
                "options": {"A": "agree", "B": "vary", "C": "wait", "D": "decline"},
                "optionsVi": {"A": "đồng ý", "B": "thay đổi, khác nhau", "C": "chờ đợi", "D": "giảm sút, từ chối"},
                "ans": "B",
                "exp": "Sau modal verb 'will' cần động từ nguyên mẫu mang nghĩa giá cả của từng mặt hàng cụ thể sẽ khác nhau/tùy thuộc vào từng loại: 'pricing will vary' -> chọn 'vary' (B).",
                "vocab": [{"word": "vary", "ipa": "/ˈveə.ri/", "pos": "v", "meaning": "khác nhau, biến đổi", "example": "Prices vary depending on the model."}],
                "collocations": [{"phrase": "pricing will vary", "meaning": "giá cả sẽ khác nhau tùy mặt hàng"}],
                "grammar": [{"title": "Động từ sau Modal Verb (will + V-bare)", "content": "'Vary' là nội động từ diễn tả sự khác biệt giữa các chủng loại."}]
            },
            140: {
                "stem": "Select the best answer for blank [140]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [140]:",
                "options": {"A": "receiving", "B": "having received", "C": "received", "D": "will be received"},
                "optionsVi": {"A": "đang nhận", "B": "đã nhận rồi", "C": "được tiếp nhận (V3)", "D": "sẽ được nhận"},
                "ans": "C",
                "exp": "Mệnh đề chính đã có vị ngữ 'will follow the new price list'. Do đó vị trí [140] là phân từ rút gọn mệnh đề quan hệ bị động: 'All orders [that are] received after this date...' -> chọn 'received' (C).",
                "vocab": [{"word": "effective", "ipa": "/ɪˈfek.tɪv/", "pos": "adj", "meaning": "có hiệu lực kể từ", "example": "effective April 17"}],
                "collocations": [{"phrase": "orders received", "meaning": "các đơn hàng được tiếp nhận"}],
                "grammar": [{"title": "Rút gọn mệnh đề quan hệ bị động (Past Participle)", "content": "Orders received = orders that are received."}]
            },
            141: {
                "stem": "Select the best answer for blank [141]:",
                "stemVi": "Chọn câu văn phù hợp nhất cho chỗ trống [141]:",
                "options": {
                    "A": "The updated price list will be available on March 20.",
                    "B": "We apologize for this inconvenience.",
                    "C": "Your orders will be shipped after April 17.",
                    "D": "We are increasing prices because of rising costs."
                },
                "optionsVi": {
                    "A": "Bảng giá cập nhật sẽ có sẵn vào ngày 20 tháng 3.",
                    "B": "Chúng tôi xin lỗi vì sự bất tiện này.",
                    "C": "Các đơn đặt hàng của bạn sẽ được giao sau ngày 17 tháng 4.",
                    "D": "Chúng tôi tăng giá vì chi phí gia tăng."
                },
                "ans": "A",
                "exp": "Câu trước nói về 'the new price list' (bảng giá mới). Câu sau đó bổ sung thông tin rằng bảng giá cập nhật sẽ có sẵn từ ngày 20/3 trên trang web: 'The updated price list will be available on March 20' -> chọn (A).",
                "vocab": [{"word": "updated", "ipa": "/ʌpˈdeɪ.tɪd/", "pos": "adj", "meaning": "đã được cập nhật", "example": "an updated price list"}],
                "collocations": [{"phrase": "price list", "meaning": "bảng giá"}],
                "grammar": [{"title": "Liên kết từ vựng đồng nghĩa (Lexical Cohesion)", "content": "'the new price list' liên kết trực tiếp với 'The updated price list'."}]
            },
            142: {
                "stem": "Select the best answer for blank [142]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [142]:",
                "options": {"A": "exceptionally", "B": "exception", "C": "exceptional", "D": "exceptionalism"},
                "optionsVi": {"A": "một cách đặc biệt (adv)", "B": "ngoại lệ (n)", "C": "xuất sắc, đặc biệt tốt (adj)", "D": "chủ nghĩa ngoại lệ (n)"},
                "ans": "C",
                "exp": "Đứng trước danh từ 'service' cần một tính từ bổ nghĩa: 'exceptional service' (dịch vụ xuất sắc vượt trội) -> chọn tính từ 'exceptional' (C).",
                "vocab": [{"word": "exceptional", "ipa": "/ɪkˈsep.ʃən.əl/", "pos": "adj", "meaning": "xuất sắc, đặc biệt", "example": "exceptional customer service"}],
                "collocations": [{"phrase": "exceptional service", "meaning": "dịch vụ xuất sắc"}],
                "grammar": [{"title": "Tính từ bổ nghĩa cho danh từ (Adjective before Noun)", "content": "Quality products and exceptional service: cấu trúc song hành giữa hai cụm tính từ + danh từ."}]
            }
        }
    },
    "p6_4": {
        "title": "E-mail: Good News from Okim Jewelry",
        "pageImage": "assets/images/test2/rc_page_8.png",
        "text": "To: Jang-Ho Kwon <jkwon@newart.nz>\nFrom: Kenneth Okim <k.okim@okimjewelry.nz>\nSubject: Good news\nDate: 30 August\n\nDear Jang-Ho,\nThank you for the shipment last month of 80 units of your jewelry pieces. I am happy to report that they have been selling very well in my shop. My [143] love the colourful designs as well as the quality of your workmanship. [144]. I would like to increase the number of units I order from you. Would you be able to [145] my order for the September shipment?\n\nFinally, I would like to discuss the possibility of featuring your work exclusively in my store. I believe that I could reach your target audience best and that the agreement would serve [146] both very well. I look forward to hearing from you.\n\nBest regards,\nKenneth Okim\nOkim Jewelry",
        "textVi": "Người nhận: Jang-Ho Kwon <jkwon@newart.nz>\nNgười gửi: Kenneth Okim <k.okim@okimjewelry.nz>\nTiêu đề: Tin tốt\nNgày: 30 tháng 8\n\nKính gửi Jang-Ho,\nCảm ơn bạn vì lô hàng 80 món trang sức vào tháng trước. Tôi rất vui mừng thông báo rằng chúng bán rất chạy tại cửa hàng của tôi. Các [143] của tôi rất yêu thích các thiết kế rực rỡ sắc màu cũng như chất lượng gia công khéo léo của bạn. [144]. Tôi muốn tăng số lượng sản phẩm đặt hàng từ bạn. Bạn có thể [145] đơn hàng của tôi cho đợt giao hàng tháng 9 không?\n\nCuối cùng, tôi muốn thảo luận về khả năng trưng bày độc quyền các tác phẩm của bạn tại cửa hàng của tôi. Tôi tin rằng tôi có thể tiếp cận đối tượng khách hàng mục tiêu của bạn một cách tốt nhất và thỏa thuận này sẽ mang lại lợi ích cho cả hai [146] chúng ta. Tôi rất mong sớm nhận được phản hồi từ bạn.\n\nTrân trọng,\nKenneth Okim\nTiệm trang sức Okim",
        "questions": {
            143: {
                "stem": "Select the best answer for blank [143]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [143]:",
                "options": {"A": "patients", "B": "students", "C": "customers", "D": "teammates"},
                "optionsVi": {"A": "bệnh nhân", "B": "học sinh", "C": "khách hàng", "D": "đồng đội"},
                "ans": "C",
                "exp": "Tại một cửa tiệm bán lẻ đồ trang sức ('in my shop'), những người mua hàng và yêu thích sản phẩm là 'customers' (khách hàng) -> chọn (C).",
                "vocab": [{"word": "workmanship", "ipa": "/ˈwɜːk.mən.ʃɪp/", "pos": "n", "meaning": "tay nghề, sự khéo léo chế tác", "example": "fine jewelry workmanship"}],
                "collocations": [{"phrase": "reach target audience", "meaning": "tiếp cận đối tượng mục tiêu"}],
                "grammar": [{"title": "Danh từ chỉ người phù hợp ngữ cảnh", "content": "Shop -> customers (khách hàng mua đồ tại cửa tiệm)."}]
            },
            144: {
                "stem": "Select the best answer for blank [144]:",
                "stemVi": "Chọn câu văn phù hợp nhất cho chỗ trống [144]:",
                "options": {
                    "A": "If you need more time, please let me know.",
                    "B": "Unfortunately, I do not have adequate shelf space at this time.",
                    "C": "I would like to show you some of my own designs.",
                    "D": "The reasonable prices also make your pieces a great value."
                },
                "optionsVi": {
                    "A": "Nếu bạn cần thêm thời gian, vui lòng báo cho tôi biết.",
                    "B": "Thật không may, hiện tại tôi không có đủ không gian kệ.",
                    "C": "Tôi muốn cho bạn xem một số thiết kế của riêng tôi.",
                    "D": "Mức giá hợp lý cũng khiến các tác phẩm của bạn có giá trị tuyệt vời."
                },
                "ans": "D",
                "exp": "Câu trước khen ngợi thiết kế đẹp và tay nghề chế tác tốt: 'love the colourful designs as well as the quality...'. Câu (D) tiếp tục bổ sung thêm điểm cộng về mặt giá cả hợp lý ('The reasonable prices also make your pieces a great value') -> chọn (D).",
                "vocab": [{"word": "reasonable", "ipa": "/ˈriː.zən.ə.bəl/", "pos": "adj", "meaning": "hợp lý, phải chăng", "example": "reasonable prices"}],
                "collocations": [{"phrase": "great value", "meaning": "giá trị tuyệt vời"}],
                "grammar": [{"title": "Tính mạch lạc phát triển ý khen ngợi (Cohesion)", "content": "Câu (D) bổ sung lý do tại sao khách hàng yêu thích sản phẩm."}]
            },
            145: {
                "stem": "Select the best answer for blank [145]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [145]:",
                "options": {"A": "include", "B": "double", "C": "repeat", "D": "insure"},
                "optionsVi": {"A": "bao gồm", "B": "gấp đôi (v)", "C": "lặp lại", "D": "bảo hiểm"},
                "ans": "B",
                "exp": "Câu trước tác giả bày tỏ mong muốn tăng số lượng đặt hàng ('increase the number of units I order from you'). Vì vậy câu hỏi 'Would you be able to double my order...?' (Bạn có thể tăng gấp đôi đơn hàng của tôi... không?) là hoàn toàn chuẩn xác -> chọn 'double' (B).",
                "vocab": [{"word": "double", "ipa": "/ˈdʌb.əl/", "pos": "v", "meaning": "tăng gấp đôi", "example": "double the production output"}],
                "collocations": [{"phrase": "double an order", "meaning": "gấp đôi đơn đặt hàng"}],
                "grammar": [{"title": "Động từ nguyên mẫu sau Modal Verb (Would you be able to + V-bare)", "content": "'Double' đóng vai trò ngoại động từ mang nghĩa tăng gấp đôi số lượng."}]
            },
            146: {
                "stem": "Select the best answer for blank [146]:",
                "stemVi": "Chọn đáp án đúng nhất cho chỗ trống [146]:",
                "options": {"A": "us", "B": "you", "C": "we", "D": "these"},
                "optionsVi": {"A": "chúng ta, chúng tôi (tân ngữ)", "B": "bạn", "C": "chúng ta (chủ ngữ)", "D": "những thứ này"},
                "ans": "A",
                "exp": "Sau ngoại động từ 'serve' cần đại từ tân ngữ để kết hợp với 'both' chỉ cả hai bên (người bán và người mua): 'serve us both very well' (mang lại lợi ích lớn cho cả hai chúng ta) -> chọn đại từ tân ngữ 'us' (A).",
                "vocab": [{"word": "exclusively", "ipa": "/ɪkˈskluː.sɪv.li/", "pos": "adv", "meaning": "độc quyền", "example": "available exclusively at our store"}],
                "collocations": [{"phrase": "serve us both", "meaning": "phục vụ/mang lại lợi ích cho cả hai chúng ta"}],
                "grammar": [{"title": "Đại từ tân ngữ đứng trước 'both' (Object Pronoun + both)", "content": "Serve us both = serve both of us."}]
            }
        }
    }
}

for pid, pdata in p6_passages.items():
    for qid, qinfo in pdata["questions"].items():
        q = q_map[qid]
        q["part"] = 6
        q["partName"] = "Part 6: Text Completion"
        q["passageId"] = pid
        q["passageTitle"] = pdata["title"]
        q["passageText"] = pdata["text"]
        q["passageTextVi"] = pdata["textVi"]
        q["pageImage"] = pdata["pageImage"]
        q["questionText"] = qinfo["stem"]
        q["questionTextVi"] = qinfo["stemVi"]
        q["options"] = qinfo["options"]
        q["optionsVi"] = qinfo["optionsVi"]
        q["correctAnswer"] = qinfo["ans"]
        q["explanation"] = qinfo["exp"]
        q["vocabulary"] = qinfo["vocab"]
        q["collocations"] = qinfo["collocations"]
        q["grammar"] = qinfo["grammar"]

print("Part 6 perfected!")

# ==========================================
# 5. PART 7 (Q147 - Q200) IMAGE MAPPING & DEFECT FIXES
# ==========================================
# Page mapping: exactly matching book pages
# Q147-148: page 9
# Q149-150: page 10
# Q151-152: page 11
# Q153-154: page 12
# Q155-157: page 13
# Q158-160: page 14
# Q161-163: page 15
# Q164-167: page 16
# Q168-171: page 17, 18
# Q172-175: page 19
# Q176-180: page 20, 21
# Q181-185: page 22, 23
# Q186-190: page 24, 25
# Q191-195: page 26, 27
# Q196-200: page 28, 29

p7_page_ranges = [
    (147, 148, [9], "Single Passage"),
    (149, 150, [10], "Single Passage"),
    (151, 152, [11], "Single Passage"),
    (153, 154, [12], "Single Passage"),
    (155, 157, [13], "Single Passage"),
    (158, 160, [14], "Single Passage"),
    (161, 163, [15], "Single Passage"),
    (164, 167, [16], "Single Passage"),
    (168, 171, [17, 18], "Double Passage"),
    (172, 175, [19], "Single Passage"),
    (176, 180, [20, 21], "Double Passage"),
    (181, 185, [22, 23], "Double Passage"),
    (186, 190, [24, 25], "Triple Passage"),
    (191, 195, [26, 27], "Triple Passage"),
    (196, 200, [28, 29], "Triple Passage"),
]

for start_q, end_q, pages, ptype in p7_page_ranges:
    img_list = [f"assets/images/test2/rc_page_{p}.png" for p in pages]
    for qid in range(start_q, end_q + 1):
        if qid in q_map:
            q = q_map[qid]
            q["part"] = 7
            q["partName"] = "Part 7: Reading Comprehension"
            q["passageType"] = ptype
            q["pageImages"] = img_list
            q["pageImage"] = img_list[0]
            q["image"] = img_list[0]

# Fix specific Part 7 question defects identified in audit:

# Q153: Fix stem missing "Liu"
if 153 in q_map:
    q_map[153]["questionText"] = "What is suggested about the paper Mr. Liu is shopping for?"

# Q165: Option D remove trailing "64"
if 165 in q_map:
    opt_d = q_map[165]["options"]["D"]
    if opt_d.endswith("64"):
        q_map[165]["options"]["D"] = opt_d[:-2].strip()

# Q182: Fix stem missing "to"
if 182 in q_map:
    q_map[182]["questionText"] = 'On the Web page, the word "suit" in paragraph 2, line 4, is closest in meaning to'

# Q184: Real options from OCR Page 23
if 184 in q_map:
    q_map[184]["questionText"] = "According to the letter, what is one of Ms. Smith's responsibilities at MODA?"
    q_map[184]["options"] = {
        "A": "Hiring fashion designers",
        "B": "Writing drafts of advertisements",
        "C": "Managing a production process",
        "D": "Researching sustainable clothing options"
    }
    q_map[184]["correctAnswer"] = "C"

# Q185: Real options from OCR Page 23
if 185 in q_map:
    q_map[185]["questionText"] = "What most likely is Medesheen?"
    q_map[185]["options"] = {
        "A": "A brand of cosmetics",
        "B": "A fashion blog",
        "C": "An online magazine",
        "D": "An advertising agency"
    }
    q_map[185]["correctAnswer"] = "B"

# Q186: Real options from OCR Page 25
if 186 in q_map:
    q_map[186]["questionText"] = "Why did Mr. Nakashima send the e-mail?"
    q_map[186]["options"] = {
        "A": "He did not receive an item he ordered.",
        "B": "He was mistakenly charged twice for an item.",
        "C": "He received a receipt that was not detailed enough.",
        "D": "He did not get a confirmation e-mail for a purchase he made."
    }
    q_map[186]["correctAnswer"] = "C"

# Q187: Real options from OCR Page 25
if 187 in q_map:
    q_map[187]["questionText"] = "According to the second e-mail, what will Mr. Nakashima receive with his next order?"
    q_map[187]["options"] = {
        "A": "A catalog",
        "B": "A free pen",
        "C": "A printed receipt",
        "D": "A price discount"
    }
    q_map[187]["correctAnswer"] = "D"

# Q194: Real options from OCR Page 27
if 194 in q_map:
    q_map[194]["questionText"] = "Where most likely did Ms. Fong make her purchase?"
    q_map[194]["options"] = {
        "A": "On a Web site",
        "B": "In a boutique shop",
        "C": "At a café",
        "D": "In a department store"
    }
    q_map[194]["correctAnswer"] = "D"

# Q195: Real options from OCR Page 27
if 195 in q_map:
    q_map[195]["questionText"] = "What is suggested about Ms. Fong?"
    q_map[195]["options"] = {
        "A": "She often buys food from Crawford and Duval.",
        "B": "She is a member of the Frequent Purchase Club.",
        "C": "She applied a gift card to her purchase.",
        "D": "She shopped during a grand-opening event."
    }
    q_map[195]["correctAnswer"] = "B"

# Q198: Clean option D footer
if 198 in q_map:
    q_map[198]["options"]["D"] = "She used to be an event planner."

# Q199: Real options from OCR Page 29
if 199 in q_map:
    q_map[199]["questionText"] = "What can be concluded about Whitten Tech?"
    q_map[199]["options"] = {
        "A": "It changed its number of event participants.",
        "B": "It provided its staff with free passes to museums.",
        "C": "It was unable to schedule its first-choice activity.",
        "D": "It was not able to hold its event outside."
    }
    q_map[199]["correctAnswer"] = "C"

# Q200: Clean option D footer
if 200 in q_map:
    q_map[200]["options"]["D"] = "The uninteresting facilitator"

print("Part 7 perfected!")

# Save perfected test2.json
t2_data["questions"] = [q_map[i] for i in range(1, 201)]

with open(os.path.join(BASE_DIR, "web", "data", "test2.json"), "w", encoding="utf-8") as f:
    json.dump(t2_data, f, ensure_ascii=False, indent=2)

print("Saved web/data/test2.json successfully with all 200 questions!")
