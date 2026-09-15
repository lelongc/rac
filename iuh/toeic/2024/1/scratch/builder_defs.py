import json
import re
import fitz
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
with open(os.path.join(BASE_DIR, "all_tests_answers.json"), "r", encoding="utf-8") as f:
    ALL_ANS = json.load(f)

doc_script = fitz.open(os.path.join(BASE_DIR, "giai", "script nghe_0001.pdf"))

TEST_SCRIPT_PAGES = {
    1: (1, 31), 2: (31, 60), 3: (60, 90), 4: (90, 119), 5: (119, 148),
    6: (148, 178), 7: (178, 208), 8: (208, 238), 9: (238, 267), 10: (267, 296)
}

VOCAB_MAP = {
    "appliance": ("/əˈplaɪ.əns/", "n", "thiết bị gia dụng", "household electrical appliances"),
    "furniture": ("/ˈfɜː.nɪ.tʃər/", "n", "đồ nội thất", "a dining table and chairs"),
    "reimburse": ("/ˌriː.ɪmˈbɜːs/", "v", "hoàn trả, thanh toán lại", "reimburse business travel expenses"),
    "reimbursement": ("/ˌriː.ɪmˈbɜːs.mənt/", "n", "khoản bồi hoàn chi phí", "submit an expense reimbursement request"),
    "maintenance": ("/ˈmeɪn.tən.əns/", "n", "sự bảo trì, bảo dưỡng", "routine maintenance check"),
    "renovate": ("/ˈren.ə.veɪt/", "v", "cải tạo, nâng cấp", "renovate the downtown office branch"),
    "inventory": ("/ˈɪn.vən.tər.i/", "n", "hàng tồn kho, sự kiểm kê", "take monthly inventory of products"),
    "convenient": ("/kənˈviː.ni.ənt/", "adj", "thuận tiện, tiện lợi", "schedule a convenient delivery time"),
    "cooperation": ("/kəʊˌɒp.ərˈeɪ.ʃən/", "n", "sự hợp tác", "thank you for your cooperation"),
    "merchandise": ("/ˈmɜː.tʃən.daɪs/", "n", "hàng hóa", "return damaged merchandise to store"),
    "complimentary": ("/ˌkɒm.plɪˈmen.tər.i/", "adj", "miễn phí, tặng kèm", "enjoy complimentary continental breakfast"),
    "registration": ("/ˌredʒ.ɪˈstreɪ.ʃən/", "n", "sự đăng ký", "advance online registration is required"),
    "inspection": ("/ɪnˈspek.ʃən/", "n", "sự kiểm tra, thanh tra", "pass the annual health inspection"),
    "candidate": ("/ˈkæn.dɪ.dət/", "n", "ứng viên", "interview an experienced job candidate"),
    "proposal": ("/prəˈpəʊ.zəl/", "n", "đề xuất, phương án", "review the business expansion proposal"),
    "efficient": ("/ɪˈfɪʃ.ənt/", "adj", "hiệu quả, năng suất cao", "an efficient organizational workflow"),
    "supervisor": ("/ˈsuː.pə.vaɪ.zər/", "n", "người giám sát, quản lý", "consult with a direct team supervisor"),
    "deadline": ("/ˈded.laɪn/", "n", "hạn chót", "meet the tight project deadline"),
    "facility": ("/fəˈsɪl.ə.ti/", "n", "cơ sở vật chất, nhà xưởng", "a modern research and development facility"),
    "expand": ("/ɪkˈspænd/", "v", "mở rộng", "expand into international markets"),
    "temporary": ("/ˈtem.pər.ər.i/", "adj", "tạm thời", "a temporary employee parking permit"),
    "significant": ("/sɪɡˈnɪf.ɪ.kənt/", "adj", "đáng kể, quan trọng", "a significant increase in quarterly profit"),
    "recommend": ("/ˌrek.əˈmend/", "v", "khuyên, giới thiệu", "highly recommended by colleagues"),
    "secure": ("/sɪˈkjʊər/", "v/adj", "bảo đảm, an toàn", "secure funding for the initiative"),
    "notify": ("/ˈnəʊ.tɪ.faɪ/", "v", "thông báo cho ai", "notify attendees via email"),
    "available": ("/əˈveɪ.lə.bəl/", "adj", "có sẵn, rảnh rỗi", "conference rooms are available on Monday"),
    "advance": ("/ədˈvɑːns/", "adj/n/v", "trước, tiến bộ", "book your hotel tickets in advance"),
    "qualified": ("/ˈkwɒl.ɪ.faɪd/", "adj", "đủ điều kiện, có năng lực", "a well-qualified marketing professional"),
    "arrange": ("/əˈreɪndʒ/", "v", "sắp xếp, thu xếp", "arrange an urgent executive meeting"),
    "deliver": ("/dɪˈlɪv.ər/", "v", "giao hàng, phát biểu", "deliver packages on schedule"),
    "warranty": ("/ˈwɒr.ən.ti/", "n", "chế độ bảo hành", "comes with a comprehensive two-year warranty"),
    "confirm": ("/kənˈfɜːm/", "v", "xác nhận", "confirm the hotel reservation details"),
    "participate": ("/pɑːˈtɪs.ɪ.peɪt/", "v", "tham gia", "participate actively in the seminar"),
    "feedback": ("/ˈfiːd.bæk/", "n", "ý kiến phản hồi", "collect valuable client feedback"),
    "contract": ("/ˈkɒn.trækt/", "n", "hợp đồng", "sign a binding commercial contract"),
    "invoice": ("/ˈɪn.vɔɪs/", "n", "hóa đơn", "process the outstanding vendor invoice"),
    "policy": ("/ˈpɒl.ə.si/", "n", "chính sách, quy định", "adhere strictly to company safety policy"),
    "brochure": ("/ˈbrəʊ.ʃər/", "n", "cuốn cẩm nang giới thiệu", "distribute informational brochures to guests")
}

def extract_vocab(text, count=2):
    words = re.findall(r"[A-Za-z]{4,}", text.lower())
    found = []
    seen = set()
    for w in words:
        if w in VOCAB_MAP and w not in seen:
            seen.add(w)
            ipa, pos, mean, ex = VOCAB_MAP[w]
            found.append({"word": w, "ipa": ipa, "pos": pos, "meaning": mean, "example": ex})
            if len(found) >= count:
                break
    if not found:
        w0 = words[0] if words else "confirm"
        found.append({"word": w0, "ipa": "/kənˈfɜːm/", "pos": "v", "meaning": "xác nhận, khẳng định", "example": f"Please {w0} the information."})
    return found

def clean_txt(t):
    if not t: return ""
    t = re.split(r"[\uac00-\ud7a3]", t)[0].strip()
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()

print("Ready.")
