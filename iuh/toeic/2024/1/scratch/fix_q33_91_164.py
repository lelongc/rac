import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Update Q33 and Q91 in scratch/t3_p3_p4_vocab.json
with open('scratch/t3_p3_p4_vocab.json', 'r', encoding='utf-8') as f:
    p3_p4 = json.load(f)

p3_p4["33"] = [
    {"word": "donate furniture", "ipa": "/dəʊˈneɪt ˈfɜː.nɪ.tʃər/", "pos": "phr", "meaning": "quyên góp, cho tặng đồ nội thất cũ", "example": "The woman suggested donating old desks and chairs to a local charity."},
    {"word": "handbook", "ipa": "/ˈhænd.bʊk/", "pos": "n", "meaning": "sổ tay hướng dẫn của công ty", "example": "The committee discussed updating the employee relocation handbook."},
    {"word": "suggestion", "ipa": "/səˈdʒes.tʃən/", "pos": "n", "meaning": "lời gợi ý, đề xuất giải pháp", "example": "The manager welcomed her constructive suggestion regarding surplus equipment."}
]

p3_p4["91"] = [
    {"word": "service", "ipa": "/ˈsɜː.vɪs/", "pos": "v, n", "meaning": "bảo trì, kiểm tra bảo dưỡng máy móc", "example": "Some specialized shop machinery will be serviced early tomorrow morning."},
    {"word": "close early", "ipa": "/kləʊz ˈɜː.li/", "pos": "phr", "meaning": "đóng cửa sớm hơn giờ thường lệ", "example": "The repair shop will close early on Friday for a staff training event."},
    {"word": "available", "ipa": "/əˈveɪ.lə.bəl/", "pos": "adj", "meaning": "còn trống, có thể sắp xếp được", "example": "An appointment will probably become available later in the afternoon."}
]

with open('scratch/t3_p3_p4_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(p3_p4, f, ensure_ascii=False, indent=2)

# Update Q164 in scratch/t3_p7_vocab.json
with open('scratch/t3_p7_vocab.json', 'r', encoding='utf-8') as f:
    p7 = json.load(f)

p7["164"] = [
    {"word": "customer service", "ipa": "/ˈkʌs.tə.mər ˈsɜː.vɪs/", "pos": "n", "meaning": "dịch vụ chăm sóc và hỗ trợ khách hàng", "example": "Commbolt is celebrated for providing exceptional 24/7 customer service."},
    {"word": "contract", "ipa": "/ˈkɒn.trækt/", "pos": "n", "meaning": "hợp đồng dịch vụ cam kết thời hạn", "example": "Unlike rival providers, we never lock customers into restrictive contracts."},
    {"word": "installation", "ipa": "/ˌɪn.stəˈleɪ.ʃən/", "pos": "n", "meaning": "việc lắp đặt đường truyền / thiết bị mạng", "example": "Subscribers can schedule a convenient weekend time for broadband installation."},
    {"word": "benefit", "ipa": "/ˈben.ɪ.fɪt/", "pos": "n", "meaning": "lợi ích, điểm ưu việt nổi bật", "example": "The advertisement highlights several key benefits of switching to Commbolt."}
]

with open('scratch/t3_p7_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(p7, f, ensure_ascii=False, indent=2)

print("Updated Q33, Q91, Q164 successfully!")
