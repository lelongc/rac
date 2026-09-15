import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Update p3_p4_vocab with 100% verbatim terms
with open('scratch/t3_p3_p4_vocab.json', 'r', encoding='utf-8') as f:
    p3_p4 = json.load(f)

# Q33
p3_p4["33"] = [
    {"word": "staffers", "ipa": "/ˈstɑːf.əz/", "pos": "n pl", "meaning": "các nhân viên trong cơ quan/công ty", "example": "The company is considering hiring more staffers to handle the workload."},
    {"word": "workstation", "ipa": "/ˈwɜːkˌsteɪ.ʃən/", "pos": "n", "meaning": "bàn làm việc, góc làm việc cá nhân", "example": "The manager arranged the workstations so each employee has natural light."},
    {"word": "expand", "ipa": "/ɪkˈspænd/", "pos": "v", "meaning": "mở rộng diện tích/quy mô", "example": "Moving to the new floor allows the department to expand comfortably."}
]

# Q42
p3_p4["42"] = [
    {"word": "late for an appointment", "ipa": "/leɪt fər ən əˈpɔɪnt.mənt/", "pos": "phr", "meaning": "bị muộn một cuộc hẹn quan trọng", "example": "I'm upset that the train track repair made me late for an appointment."},
    {"word": "upset", "ipa": "/ʌpˈset/", "pos": "adj", "meaning": "bực bội, khó chịu vì sự cố", "example": "Passengers were upset to learn that no trains were departing from this track."},
    {"word": "appointment", "ipa": "/əˈpɔɪnt.mənt/", "pos": "n", "meaning": "cuộc hẹn đã định trước", "example": "He had a scheduled client appointment across town at two o'clock."}
]

# Q52
p3_p4["52"] = [
    {"word": "celebrate with", "ipa": "/ˈsel.ə.breɪt wɪð/", "pos": "phr v", "meaning": "ăn mừng chung vui cùng với ai", "example": "Sabine would love to celebrate with her former colleagues from other teams."},
    {"word": "former colleagues", "ipa": "/ˈfɔː.mər ˈkɒl.iːɡz/", "pos": "n pl", "meaning": "những đồng nghiệp cũ trước đây", "example": "She invited several former colleagues who now work in the sales division."},
    {"word": "team", "ipa": "/tiːm/", "pos": "n", "meaning": "đội nhóm, ban chuyên môn", "example": "Everyone on our project team was invited to the retirement party."}
]

# Q55
p3_p4["55"] = [
    {"word": "view hotel facilities", "ipa": "/vjuː həʊˈtel fəˈsɪl.ə.tiz/", "pos": "phr", "meaning": "khảo sát cơ sở vật chất của khách sạn", "example": "Mr. Ogawa booked a tour to view hotel facilities for an upcoming retreat."},
    {"word": "retreat", "ipa": "/rɪˈtriːt/", "pos": "n", "meaning": "chuyến dã ngoại / hội nghị nghỉ dưỡng công ty", "example": "The company chose the lakeside hotel for its annual executive retreat."},
    {"word": "facilities", "ipa": "/fəˈsɪl.ə.tiz/", "pos": "n pl", "meaning": "tiện nghi, cơ sở vật chất hội họp", "example": "The venue features modern conference facilities and a large banquet room."}
]

# Q60
p3_p4["60"] = [
    {"word": "schedule a doctor's visit", "ipa": "/ˈskedʒ.uːl ə ˈdɒk.təz ˈvɪz.ɪt/", "pos": "phr", "meaning": "đặt lịch khám bác sĩ trực tuyến", "example": "Patients can quickly schedule a doctor's visit online through the portal."},
    {"word": "schedule online", "ipa": "/ˈskedʒ.uːl ˌɒnˈlaɪn/", "pos": "phr", "meaning": "lên lịch khám trực tuyến trên web", "example": "There was an option to schedule online and receive text notifications."},
    {"word": "option", "ipa": "/ˈɒp.ʃən/", "pos": "n", "meaning": "tùy chọn, phương án lựa chọn", "example": "The website provides a convenient option to receive automated reminder texts."}
]

# Q61
p3_p4["61"] = [
    {"word": "cancel at the last minute", "ipa": "/ˈkæn.səl æt ðə lɑːst ˈmɪn.ɪt/", "pos": "phr", "meaning": "hủy lịch hẹn vào phút chót", "example": "Three patients had to cancel at the last minute, leaving open slots."},
    {"word": "available appointments", "ipa": "/əˈveɪ.lə.bəl əˈpɔɪnt.mənts/", "pos": "n pl", "meaning": "các suất hẹn khám còn trống", "example": "Other patients might have taken those available appointments if notified in time."},
    {"word": "patient", "ipa": "/ˈpeɪ.ʃənt/", "pos": "n", "meaning": "bệnh nhân đến khám chữa răng", "example": "The dental clinic strives to accommodate every registered patient promptly."}
]

# Q62
p3_p4["62"] = [
    {"word": "buy the employees", "ipa": "/baɪ ði ɪmˈplɔɪ.iːz/", "pos": "phr", "meaning": "mua quà tặng cho các nhân viên", "example": "Have you had a chance to look for something I could buy the employees?"},
    {"word": "thank everyone", "ipa": "/θæŋk ˈev.ri.wʌn/", "pos": "phr", "meaning": "gửi lời cảm ơn tới tất cả mọi người", "example": "I want to be sure I thank everyone for their hard work throughout the year."},
    {"word": "hard work", "ipa": "/hɑːd wɜːk/", "pos": "n", "meaning": "sự nỗ lực và chăm chỉ làm việc", "example": "The director presented holiday gifts to recognize the staff's hard work."}
]

# Q75
p3_p4["75"] = [
    {"word": "explain complicated ideas", "ipa": "/ɪkˈspleɪn ˈkɒm.plɪ.keɪ.tɪd aɪˈdɪəz/", "pos": "phr", "meaning": "giải thích những khái niệm phức tạp một cách dễ hiểu", "example": "Ms. Bertrand is particularly skilled at explaining complicated ideas clearly."},
    {"word": "marketing on social media", "ipa": "/ˈmɑː.kɪ.tɪŋ ɒn ˈsəʊ.ʃəl ˈmiː.di.ə/", "pos": "n phr", "meaning": "tiếp thị quảng bá trên mạng xã hội", "example": "The podcast episode analyzes marketing on social media for small brands."},
    {"word": "complicated", "ipa": "/ˈkɒm.plɪ.keɪ.tɪd/", "pos": "adj", "meaning": "phức tạp, nhiều tầng ý nghĩa", "example": "The host broke down complicated algorithmic trends into simple takeaways."}
]

# Q85
p3_p4["85"] = [
    {"word": "bridge replacement project", "ipa": "/brɪdʒ rɪˈpleɪs.mənt ˈprɒdʒ.ekt/", "pos": "n phr", "meaning": "dự án thi công thay thế cây cầu mới", "example": "Here is an update on the Springdale bridge replacement project."},
    {"word": "transportation agency", "ipa": "/ˌtræn.spɔːˈteɪ.ʃən ˈeɪ.dʒən.si/", "pos": "n", "meaning": "cơ quan / sở quản lý giao thông vận tải", "example": "Officials gathered for the monthly regional transportation agency meeting."},
    {"word": "opening ceremony", "ipa": "/ˈəʊ.pən.ɪŋ ˈser.ɪ.mə.ni/", "pos": "n", "meaning": "lễ khánh thành đưa công trình vào vận hành", "example": "The speaker suggested organizing a public opening ceremony upon completion."}
]

# Q91
p3_p4["91"] = [
    {"word": "clogged oil filter", "ipa": "/klɒɡd ɔɪl ˈfɪl.tər/", "pos": "n phr", "meaning": "bộ lọc dầu động cơ bị tắc nghẽn", "example": "The sluggish acceleration could be caused by a clogged oil filter."},
    {"word": "open at eight", "ipa": "/ˈəʊ.pən æt eɪt/", "pos": "phr", "meaning": "mở cửa đón khách lúc 8 giờ sáng", "example": "The auto service garage will open at eight tomorrow morning."},
    {"word": "repair", "ipa": "/rɪˈpeər/", "pos": "n, v", "meaning": "công việc sửa chữa; sửa xe", "example": "Prices vary depending on the complexity of the automotive repair."}
]

with open('scratch/t3_p3_p4_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(p3_p4, f, ensure_ascii=False, indent=2)

# Update p7_vocab with 100% verbatim terms
with open('scratch/t3_p7_vocab.json', 'r', encoding='utf-8') as f:
    p7 = json.load(f)

# Q162
p7["162"] = [
    {"word": "bankruptcy", "ipa": "/ˈbæŋ.krəpt.si/", "pos": "n", "meaning": "sự phá sản, khánh tận tài chính", "example": "Carila Corporation went from near bankruptcy to a highly profitable enterprise."},
    {"word": "profitable", "ipa": "/ˈprɒf.ɪ.tə.bəl/", "pos": "adj", "meaning": "sinh lời cao, kinh doanh có lãi", "example": "New management strategies turned the tech manufacturer into a profitable firm."},
    {"word": "viability", "ipa": "/ˌvaɪ.əˈbɪl.ə.ti/", "pos": "n", "meaning": "khả năng sinh tồn và phát triển lâu dài", "example": "Strategic reforms ensured the corporation's long-term commercial viability."}
]

# Q164
p7["164"] = [
    {"word": "direction of CEO", "ipa": "/daɪˈrek.ʃən əv ˌsiː.iːˈəʊ/", "pos": "n phr", "meaning": "sự chỉ đạo lãnh đạo của Tổng giám đốc", "example": "Under the direction of CEO Atsak Kakar, operating profits grew rapidly."},
    {"word": "electronics sector", "ipa": "/ɪˌlekˈtrɒn.ɪks ˈsek.tər/", "pos": "n", "meaning": "ngành công nghiệp sản xuất thiết bị điện tử", "example": "Carila Corporation is recognized as a major player in the electronics sector."},
    {"word": "corporate prize", "ipa": "/ˈkɔː.pər.ət praɪz/", "pos": "n", "meaning": "giải thưởng doanh nghiệp danh giá", "example": "The Waldenstone Corporate Prize honors sustainable business vision."}
]

with open('scratch/t3_p7_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(p7, f, ensure_ascii=False, indent=2)

print("Successfully refined all 16 terms to be 100% verbatim with question context!")
