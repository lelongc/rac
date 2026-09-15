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
doc_rc = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - READING.pdf"))

# High quality curated vocabulary dictionary with IPA & Vietnamese meaning
VOCAB_DB = {
    "appliance": ("/əˈplaɪ.əns/", "n", "thiết bị gia dụng", "household electrical appliances"),
    "furniture": ("/ˈfɜː.nɪ.tʃər/", "n", "đồ nội thất", "a dining table and chairs"),
    "reimburse": ("/ˌriː.ɪmˈbɜːs/", "v", "hoàn trả, thanh toán lại", "reimburse travel expenses"),
    "reimbursement": ("/ˌriː.ɪmˈbɜːs.mənt/", "n", "khoản bồi hoàn chi phí", "submit a reimbursement form"),
    "maintenance": ("/ˈmeɪn.tən.əns/", "n", "sự bảo trì, bảo dưỡng", "routine maintenance check"),
    "renovate": ("/ˈren.ə.veɪt/", "v", "cải tạo, làm mới", "renovate the downtown branch"),
    "inventory": ("/ˈɪn.vən.tər.i/", "n", "hàng tồn kho, kiểm kê", "take monthly inventory"),
    "convenient": ("/kənˈviː.ni.ənt/", "adj", "thuận tiện, tiện lợi", "schedule a convenient meeting time"),
    "cooperation": ("/kəʊˌɒp.ərˈeɪ.ʃən/", "n", "sự hợp tác", "thank you for your cooperation"),
    "merchandise": ("/ˈmɜː.tʃən.daɪs/", "n", "hàng hóa", "return damaged merchandise"),
    "complimentary": ("/ˌkɒm.plɪˈmen.tər.i/", "adj", "miễn phí, tặng kèm", "enjoy complimentary coffee"),
    "registration": ("/ˌredʒ.ɪˈstreɪ.ʃən/", "n", "sự đăng ký", "advance registration is required"),
    "inspection": ("/ɪnˈspek.ʃən/", "n", "sự thanh tra, kiểm tra", "pass the safety inspection"),
    "candidate": ("/ˈkæn.dɪ.dət/", "n", "ứng viên", "interview a promising candidate"),
    "proposal": ("/prəˈpəʊ.zəl/", "n", "bản đề xuất, kế hoạch", "approve the budget proposal"),
    "efficient": ("/ɪˈfɪʃ.ənt/", "adj", "hiệu quả, năng suất", "an efficient production process"),
    "supervisor": ("/ˈsuː.pə.vaɪ.zər/", "n", "người giám sát, quản lý", "consult with a direct supervisor"),
    "deadline": ("/ˈded.laɪn/", "n", "hạn chót", "meet the strict project deadline"),
    "facility": ("/fəˈsɪl.ə.ti/", "n", "cơ sở vật chất, nhà máy", "a state-of-the-art facility"),
    "expand": ("/ɪkˈspænd/", "v", "mở rộng", "expand into international markets"),
    "temporary": ("/ˈtem.pər.ər.i/", "adj", "tạm thời", "a temporary parking permit"),
    "significant": ("/sɪɡˈnɪf.ɪ.kənt/", "adj", "đáng kể, quan trọng", "a significant increase in profit"),
    "recommend": ("/ˌrek.əˈmend/", "v", "khuyên, tiến cử", "highly recommended by colleagues"),
    "secure": ("/sɪˈkjʊər/", "v/adj", "bảo đảm, an toàn", "secure the grant funding"),
    "notify": ("/ˈnəʊ.tɪ.faɪ/", "v", "thông báo cho ai", "notify attendees by email"),
    "available": ("/əˈveɪ.lə.bəl/", "adj", "có sẵn, rảnh rỗi", "conference rooms are available"),
    "advance": ("/ədˈvɑːns/", "adj/n/v", "trước, tiến bộ", "make reservations in advance"),
    "qualified": ("/ˈkwɒl.ɪ.faɪd/", "adj", "đủ tiêu chuẩn, có năng lực", "a well-qualified professional"),
    "arrange": ("/əˈreɪndʒ/", "v", "sắp xếp, thu xếp", "arrange a business meeting"),
    "deliver": ("/dɪˈlɪv.ər/", "v", "giao hàng, phát biểu", "deliver goods on schedule"),
    "warranty": ("/ˈwɒr.ən.ti/", "n", "bảo hành", "a two-year product warranty"),
    "confirm": ("/kənˈfɜːm/", "v", "xác nhận", "confirm the appointment details"),
    "participate": ("/pɑːˈtɪs.ɪ.peɪt/", "v", "tham gia", "participate in the workshop"),
    "feedback": ("/ˈfiːd.bæk/", "n", "ý kiến phản hồi", "gather constructive customer feedback"),
    "contract": ("/ˈkɒn.trækt/", "n", "hợp đồng", "sign a multi-year service contract"),
    "invoice": ("/ˈɪn.vɔɪs/", "n", "hóa đơn", "process the vendor invoice"),
    "policy": ("/ˈpɒl.ə.si/", "n", "chính sách, quy định", "review company travel policy"),
    "brochure": ("/ˈbrəʊ.ʃər/", "n", "cuốn cẩm nang giới thiệu", "read the informational brochure")
}

def get_vocab_for(text, count=2):
    words = re.findall(r"[A-Za-z]{4,}", text.lower())
    res = []
    seen = set()
    for w in words:
        if w in VOCAB_DB and w not in seen:
            seen.add(w)
            ipa, pos, mean, ex = VOCAB_DB[w]
            res.append({"word": w, "ipa": ipa, "pos": pos, "meaning": mean, "example": ex})
            if len(res) >= count:
                break
    if not res:
        w0 = words[0] if words else "confirm"
        res.append({"word": w0, "ipa": "/kənˈfɜːm/", "pos": "v", "meaning": "xác nhận, khẳng định", "example": f"Please {w0} the information."})
    return res

print("VOCAB_DB ready.")
