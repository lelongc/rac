# builder_engine.py: Master Generator for ETS TOEIC 2024 Tests 2 to 10
import fitz
import json
import re
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRATCH_DIR = os.path.join(BASE_DIR, "scratch")
DATA_DIR = os.path.join(BASE_DIR, "web", "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Load official answers
with open(os.path.join(BASE_DIR, "all_tests_answers.json"), "r", encoding="utf-8") as f:
    ALL_OFFICIAL_ANSWERS = json.load(f)

# Script PDF page ranges (1-indexed in PDF viewer, 0-indexed for fitz)
TEST_SCRIPT_RANGES = {
    1: (1, 31),
    2: (31, 60),
    3: (60, 90),
    4: (90, 119),
    5: (119, 148),
    6: (148, 178),
    7: (178, 208),
    8: (208, 238),
    9: (238, 267),
    10: (267, 296)
}

doc_script = fitz.open(os.path.join(BASE_DIR, "giai", "script nghe_0001.pdf"))

# Common TOEIC vocabulary database with IPA and Vietnamese translation
VOCAB_DB = {
    "arrange": ("/əˈreɪndʒ/", "v", "sắp xếp, thu xếp", "arrange a meeting"),
    "deliver": ("/dɪˈlɪv.ər/", "v", "giao hàng, phân phối", "deliver the package"),
    "schedule": ("/ˈʃedʒ.uːl/", "v/n", "lên lịch, lịch trình", "schedule an appointment"),
    "machinery": ("/məˈʃiː.nər.i/", "n", "máy móc, thiết bị", "operate machinery"),
    "dock": ("/dɒk/", "v/n", "cập bến, bến tàu", "dock at the port"),
    "delay": ("/dɪˈleɪ/", "n/v", "sự chậm trễ, hoãn lại", "cause a delay"),
    "equipment": ("/ɪˈkwɪp.mənt/", "n", "trang thiết bị", "safety equipment"),
    "appliance": ("/əˈplaɪ.əns/", "n", "thiết bị gia dụng", "household appliances"),
    "furniture": ("/ˈfɜː.nɪ.tʃər/", "n", "đồ nội thất", "office furniture"),
    "discount": ("/ˈdɪs.kaʊnt/", "n/v", "giảm giá, chiết khấu", "special discount"),
    "confirm": ("/kənˈfɜːm/", "v", "xác nhận", "confirm a reservation"),
    "renovate": ("/ˈren.ə.veɪt/", "v", "cải tạo, nâng cấp", "renovate the office"),
    "maintenance": ("/ˈmeɪn.tən.əns/", "n", "bảo trì, bảo dưỡng", "routine maintenance"),
    "cooperation": ("/kəʊˌɒp.ərˈeɪ.ʃən/", "n", "sự hợp tác", "thank you for your cooperation"),
    "inspection": ("/ɪnˈspek.ʃən/", "n", "sự kiểm tra, thanh tra", "conduct an inspection"),
    "budget": ("/ˈbʌdʒ.ɪt/", "n", "ngân sách", "within the budget"),
    "participate": ("/pɑːˈtɪs.ɪ.peɪt/", "v", "tham gia", "participate in a workshop"),
    "registration": ("/ˌredʒ.ɪˈstreɪ.ʃən/", "n", "sự đăng ký", "advance registration"),
    "complimentary": ("/ˌkɒm.plɪˈmen.tər.i/", "adj", "miễn phí, tặng kèm", "complimentary breakfast"),
    "presentation": ("/ˌprez.ənˈteɪ.ʃən/", "n", "bài thuyết trình", "give a presentation"),
    "supervisor": ("/ˈsuː.pə.vaɪ.zər/", "n", "người giám sát, quản lý", "speak to a supervisor"),
    "merchandise": ("/ˈmɜː.tʃən.daɪs/", "n", "hàng hóa", "damaged merchandise"),
    "announcement": ("/əˈnaʊns.mənt/", "n", "thông báo", "make an announcement"),
    "contract": ("/ˈkɒn.trækt/", "n", "hợp đồng", "sign a contract"),
    "policy": ("/ˈpɒl.ə.si/", "n", "chính sách, quy định", "company policy"),
    "warranty": ("/ˈwɒr.ən.ti/", "n", "bảo hành", "warranty coverage"),
    "ingredient": ("/ɪnˈɡriː.di.ənt/", "n", "nguyên liệu, thành phần", "fresh ingredients"),
    "inventory": ("/ˈɪn.vən.tər.i/", "n", "hàng tồn kho, sự kiểm kê", "take inventory"),
    "brochure": ("/ˈbrəʊ.ʃər/", "n", "cuốn cẩm nang, tờ rơi", "read the brochure"),
    "headquarters": ("/ˈhedˌkwɔː.təz/", "n", "trụ sở chính", "company headquarters"),
    "representative": ("/ˌrep.rɪˈzen.tə.tɪv/", "n", "người đại diện", "sales representative"),
    "recommend": ("/ˌrek.əˈmend/", "v", "khuyên, giới thiệu", "highly recommended"),
    "candidate": ("/ˈkæn.dɪ.dət/", "n", "ứng viên", "qualified candidate"),
    "requirement": ("/rɪˈkwaɪə.mənt/", "n", "yêu cầu, điều kiện", "meet the requirements"),
    "feedback": ("/ˈfiːd.bæk/", "n", "phản hồi, ý kiến", "customer feedback"),
    "proposal": ("/prəˈpəʊ.zəl/", "n", "đề xuất, phương án", "submit a proposal"),
    "convenient": ("/kənˈviː.ni.ənt/", "adj", "thuận tiện, tiện lợi", "convenient location"),
    "deadline": ("/ˈded.laɪn/", "n", "hạn chót", "meet the deadline"),
    "reimburse": ("/ˌriː.ɪmˈbɜːs/", "v", "hoàn trả, bồi hoàn", "reimburse travel expenses"),
    "invoice": ("/ˈɪn.vɔɪs/", "n", "hóa đơn", "review the invoice")
}

def get_word_info(text):
    words = re.findall(r"[A-Za-z]{4,}", text.lower())
    result = []
    seen = set()
    for w in words:
        if w in VOCAB_DB and w not in seen:
            seen.add(w)
            ipa, pos, meaning, ex = VOCAB_DB[w]
            result.append({
                "word": w,
                "ipa": ipa,
                "pos": pos,
                "meaning": meaning,
                "example": ex
            })
            if len(result) >= 3:
                break
    if not result:
        # Fallback default word
        result.append({
            "word": words[0] if words else "confirm",
            "ipa": "/kənˈfɜːm/",
            "pos": "v",
            "meaning": "xác nhận, khẳng định",
            "example": "Please confirm your reservation."
        })
    return result

def clean_ocr_text(txt):
    # Fix common OCR artifacts
    txt = txt.replace("", "-")
    txt = re.sub(r"[ \t]+", " ", txt)
    return txt.strip()

print("Loaded builder_engine core modules.")
