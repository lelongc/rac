# make_p3_p4.py
import json

data = {}

def add_q(qid, stem, options, ans, exp, vocab, collocations, grammar):
    data[str(qid)] = {
        "stem": stem,
        "options": options,
        "ans": ans,
        "exp": exp,
        "vocab": vocab,
        "collocations": collocations,
        "grammar": grammar
    }

# 32 - 34
add_q(32, "What change is a company making?", {"A": "It is lowering some prices.", "B": "It is hiring more staffers.", "C": "It is moving to a new location.", "D": "It is expanding a product line."}, "C",
      "Người nói đề cập: 'year by moving offices. It's exciting that the new space will be much bigger' (chuyển văn phòng... không gian mới rộng hơn nhiều) -> Công ty đang dời sang địa điểm mới ('moving to a new location').",
      [{"word": "relocate", "ipa": "/ˌriː.ləʊˈkeɪt/", "pos": "v", "meaning": "chuyển địa điểm, di dời", "example": "The firm plans to relocate to a modern downtown office."},
       {"word": "spacious", "ipa": "/ˈspeɪ.ʃəs/", "pos": "adj", "meaning": "rộng rãi, thoáng đãng", "example": "The spacious conference room accommodates 50 guests."}],
      [{"phrase": "move offices", "meaning": "chuyển văn phòng làm việc"}],
      [{"title": "Mệnh đề chỉ phương thức với Giới từ 'by'", "rule": "by + V-ing", "content": "'by moving offices' diễn tả phương thức mà công ty thực hiện sự đổi mới."}])

add_q(33, "What suggestion does the woman make?", {"A": "Updating a handbook", "B": "Donating some furniture", "C": "Creating a schedule", "D": "Downloading a software program"}, "B",
      "Người phụ nữ đề xuất: 'Why don't we donate our surplus desks and chairs to a local charity?' (Tại sao chúng ta không quyên góp bàn ghế thừa cho tổ chức từ thiện?) -> Quyên góp đồ nội thất ('Donating some furniture').",
      [{"word": "donate", "ipa": "/dəʊˈneɪt/", "pos": "v", "meaning": "quyên góp, ủng hộ", "example": "Companies regularly donate surplus equipment to non-profit groups."},
       {"word": "surplus", "ipa": "/ˈsɜː.pləs/", "pos": "adj", "meaning": "dư thừa, vượt mức", "example": "Sell surplus inventory at discounted prices."}],
      [{"phrase": "donate furniture", "meaning": "quyên góp đồ nội thất"}],
      [{"title": "Mẫu câu gợi ý 'Why don't we...?'", "rule": "Why don't we + V-inf?", "content": "Cấu trúc đưa ra đề xuất mang tính xây dựng trong thảo luận công việc."}])

add_q(34, "What will the speakers most likely do next?", {"A": "Train a new employee", "B": "Review an application", "C": "Check a list", "D": "Talk to some directors"}, "D",
      "Người đàn ông nói: 'I'll consult with the board of directors this afternoon to get their approval' (Tôi sẽ trao đổi với ban giám đốc vào chiều nay để xin phê duyệt) -> Trao đổi với các giám đốc ('Talk to some directors').",
      [{"word": "director", "ipa": "/daɪˈrek.tər/", "pos": "n", "meaning": "giám đốc, ủy viên quản trị", "example": "The board of directors approved the acquisition."},
       {"word": "approval", "ipa": "/əˈpruː.vəl/", "pos": "n", "meaning": "sự chấp thuận, phê chuẩn", "example": "Obtain written approval prior to commencing work."}],
      [{"phrase": "board of directors", "meaning": "hội đồng quản trị"}],
      [{"title": "Hành động tiếp theo với 'I will...'", "rule": "S + will + V-inf", "content": "Câu trả lời cho 'What will happen next?' thường xuất hiện ở câu cuối cùng với động từ 'will'."}])

# 35 - 37
add_q(35, "Who most likely are the women?", {"A": "Company executives", "B": "Journalists", "C": "Health-care professionals", "D": "Safety inspectors"}, "B",
      "Người phụ nữ giới thiệu: 'We really wanted to interview you as the organizer from our newspaper' (Chúng tôi rất muốn phỏng vấn ông với tư cách là ban tổ chức đến từ tòa báo của chúng tôi) -> Họ là nhà báo ('Journalists').",
      [{"word": "journalist", "ipa": "/ˈdʒɜː.nə.lɪst/", "pos": "n", "meaning": "nhà báo, phóng viên", "example": "The award-winning journalist investigated business practices."},
       {"word": "interview", "ipa": "/ˈɪn.tə.vjuː/", "pos": "v", "meaning": "phỏng vấn", "example": "The reporter will interview the company founder today."}],
      [{"phrase": "conduct an interview", "meaning": "tiến hành phỏng vấn"}],
      [{"title": "Nhận diện nghề nghiệp qua từ khóa liên tưởng", "rule": "newspaper + interview -> journalist", "content": "Căn cứ vào danh từ 'newspaper' và hành động 'interview' để suy ra nghề nghiệp nhà báo."}])

add_q(36, "What does the man say he is pleased about?", {"A": "The number of event participants", "B": "The amount of money raised", "C": "The quality of vendors", "D": "The variety of presentations"}, "A",
      "Người đàn ông nói: 'I'm thrilled with the high turnout. We have over 500 attendees registered' (Tôi rất vui mừng trước lượng người tham dự đông đảo... hơn 500 người đăng ký) -> Hài lòng về số lượng người tham dự ('The number of event participants'). Paraphrasing: turnout / attendees -> event participants.",
      [{"word": "turnout", "ipa": "/ˈtɜːn.aʊt/", "pos": "n", "meaning": "lượng người tham dự, số người có mặt", "example": "The charity gala had an extraordinary turnout."},
       {"word": "participant", "ipa": "/pɑːˈtɪs.ɪ.pənt/", "pos": "n", "meaning": "người tham gia", "example": "Every participant received a commemorative certificate."}],
      [{"phrase": "high turnout", "meaning": "lượng người tham gia cao"}],
      [{"title": "Hiện tượng đồng nghĩa (Paraphrasing) trong TOEIC", "rule": "turnout / attendees = participants", "content": "TOEIC thường kiểm tra khả năng nhận biết từ đồng nghĩa chỉ tập hợp người tham gia."}])

add_q(37, "What will the women do next?", {"A": "Watch a demonstration", "B": "Get some refreshments", "C": "Register for an event", "D": "Take a photograph"}, "D",
      "Người phụ nữ hỏi: 'Can we get a photo of you in front of the poster for the show? - Certainly!' (Chúng tôi có thể chụp một bức ảnh của ông trước tấm áp phích triển lãm được không? - Chắc chắn rồi!) -> Chụp ảnh ('Take a photograph'). Paraphrasing: get a photo -> take a photograph.",
      [{"word": "photograph", "ipa": "/ˈfəʊ.tə.ɡrɑːf/", "pos": "n", "meaning": "bức ảnh chụp", "example": "The brochure features high-resolution photographs."},
       {"word": "poster", "ipa": "/ˈpəʊ.stər/", "pos": "n", "meaning": "tấm áp phích quảng cáo", "example": "Hang the promotional poster on the bulletin board."}],
      [{"phrase": "take a photograph", "meaning": "chụp một bức ảnh"}],
      [{"title": "Cấu trúc xin phép lịch sự 'Can we get...?'", "rule": "Can we get + Noun?", "content": "'get a photo' là cách diễn đạt thông dụng tương đương với 'take a picture/photo'."}])

# 38 - 40
add_q(38, "What most likely is the woman's job?", {"A": "Professional chef", "B": "Bank executive", "C": "Administrative assistant", "D": "Web designer"}, "D",
      "Người phụ nữ nói: 'I've been redesigning Ace Bancorp's Web site to add new online banking functions' (Tôi đang thiết kế lại trang web của ngân hàng Ace Bancorp để bổ sung tính năng ngân hàng điện tử) -> Nghề nghiệp là thiết kế web ('Web designer').",
      [{"word": "web designer", "ipa": "/web dɪˈzaɪ.nər/", "pos": "n", "meaning": "nhà thiết kế trang web", "example": "Our web designer launched the e-commerce store."},
       {"word": "redesign", "ipa": "/ˌriː.dɪˈzaɪn/", "pos": "v", "meaning": "thiết kế lại", "example": "Redesign the layout for improved mobile accessibility."}],
      [{"phrase": "redesign a website", "meaning": "thiết kế lại trang web"}],
      [{"title": "Thì Hiện tại hoàn thành tiếp diễn", "rule": "have/has been + V-ing", "content": "'I've been redesigning...' nhấn mạnh tính liên tục của dự án thiết kế."}])

add_q(39, "What will the man most likely do?", {"A": "Buy some materials from the woman", "B": "Check the woman’s work", "C": "List investment options", "D": "Update some client information"}, "B",
      "Người phụ nữ hỏi: 'I wonder whether you could test out the redeveloped site for me? - Sure, I can do that' (Tôi tự hỏi liệu bạn có thể kiểm thử trang web đã phát triển lại giúp tôi không? - Được chứ) -> Người đàn ông sẽ kiểm tra công việc của cô ấy ('Check the woman's work'). Paraphrasing: test out the site -> check the work.",
      [{"word": "test out", "ipa": "/test aʊt/", "pos": "phr v", "meaning": "kiểm thử, dùng thử nghiệm", "example": "Engineers test out the updated software before release."},
       {"word": "functionality", "ipa": "/ˌfʌŋk.ʃənˈæl.ə.ti/", "pos": "n", "meaning": "tính năng hoạt động", "example": "Verify the functionality of all hyperlinks."}],
      [{"phrase": "test out", "meaning": "kiểm thử tính năng"}],
      [{"title": "Câu nhờ vả gián tiếp lịch sự 'I wonder whether...'", "rule": "I wonder whether + S + could + V-inf", "content": "Mẫu câu trang trọng dùng khi nhờ đồng nghiệp hỗ trợ công việc."}])

add_q(40, "What will the woman most likely send to the man?", {"A": "A cost estimate", "B": "A revised schedule", "C": "A building plan", "D": "A list of changes"}, "D",
      "Người đàn ông đề xuất: 'Why don't you send me a list of the specific updates you made?' (Tại sao bạn không gửi cho tôi danh sách những cập nhật cụ thể mà bạn đã làm?) -> Người phụ nữ sẽ gửi danh sách các điểm thay đổi ('A list of changes'). Paraphrasing: specific updates -> list of changes.",
      [{"word": "specific updates", "ipa": "/spəˈsɪf.ɪk ʌpˈdeɪts/", "pos": "n pl", "meaning": "các mục cập nhật cụ thể", "example": "Review specific updates listed in the patch notes."},
       {"word": "revision", "ipa": "/rɪˈvɪʒ.ən/", "pos": "n", "meaning": "bản chỉnh sửa", "example": "Submit the revision to the editor before Friday."}],
      [{"phrase": "list of changes", "meaning": "danh sách các điểm thay đổi"}],
      [{"title": "Paraphrasing danh từ: updates -> changes", "rule": "updates = changes = revisions", "content": "'Updates' và 'changes' thường xuyên được dùng thay thế cho nhau trong phần nghe TOEIC."}])

# 41 - 43
add_q(41, "Why are some train services suspended?", {"A": "Tracks are being repaired.", "B": "A severe storm is approaching.", "C": "Staff are on strike.", "D": "A power outage occurred."}, "A",
      "Người phụ nữ giải thích: 'Unfortunately, some tracks are being repaired, so no trains are departing from this platform' (Không may là một số đường ray đang được sửa chữa, nên không có chuyến tàu nào khởi hành từ ga này) -> Đường ray đang được sửa chữa ('Tracks are being repaired').",
      [{"word": "track", "ipa": "/træk/", "pos": "n", "meaning": "đường ray tàu hỏa", "example": "Track maintenance is scheduled during off-peak hours."},
       {"word": "platform", "ipa": "/ˈplæt.fɔːm/", "pos": "n", "meaning": "sân ga xe lửa", "example": "Wait on platform 3 for the express commuter train."}],
      [{"phrase": "repair tracks", "meaning": "sửa chữa đường ray"}],
      [{"title": "Bị động Hiện tại tiếp diễn chỉ sự gián đoạn", "rule": "are being + V3/ed (tracks are being repaired)", "content": "Diễn tả hành vi sửa chữa đang xảy ra gây ảnh hưởng trực tiếp đến hoạt động chạy tàu."}])

add_q(42, "What is the man concerned about?", {"A": "Losing a ticket", "B": "Missing a flight", "C": "Being late for an appointment", "D": "Paying extra fees"}, "C",
      "Người đàn ông bực bội: 'And I'm upset that now I'm late for an appointment' (Và tôi khó chịu vì bây giờ tôi bị trễ một cuộc hẹn) -> Lo lắng bị muộn giờ hẹn ('Being late for an appointment').",
      [{"word": "appointment", "ipa": "/əˈpɔɪnt.mənt/", "pos": "n", "meaning": "cuộc hẹn", "example": "Confirm your appointment with the client by email."},
       {"word": "upset", "ipa": "/ʌpˈset/", "pos": "adj", "meaning": "bực bội, khó chịu", "example": "Commuters were upset about transit service interruptions."}],
      [{"phrase": "late for an appointment", "meaning": "bị trễ một cuộc hẹn"}],
      [{"title": "Cụm tính từ miêu tả sự lo lắng/bực bội", "rule": "be upset / worried that + Clause", "content": "Chỉ rõ tâm trạng lo âu của nhân vật về hậu quả phát sinh trong tình huống."}])

add_q(43, "What will the man most likely do next?", {"A": "Purchase a snack", "B": "Take a shuttle bus", "C": "File a complaint", "D": "Download a map"}, "B",
      "Người phụ nữ hướng dẫn: 'they're providing free bus service to the next few stations. You can catch a shuttle bus from the south side' (họ cung cấp xe buýt miễn phí... Bạn có thể bắt xe buýt trung chuyển ở phía nam ga) -> Đi xe buýt trung chuyển ('Take a shuttle bus').",
      [{"word": "shuttle bus", "ipa": "/ˈʃʌt.əl bʌs/", "pos": "n", "meaning": "xe buýt trung chuyển", "example": "A shuttle bus transports guests between terminal gates."},
       {"word": "catch a bus", "ipa": "/kætʃ ə bʌs/", "pos": "phr", "meaning": "bắt xe buýt", "example": "Walk to the transit hub to catch a bus."}],
      [{"phrase": "take a shuttle bus", "meaning": "đi xe buýt trung chuyển"}],
      [{"title": "Động từ 'take' đi kèm phương tiện giao thông", "rule": "take + a bus / a train / a cab", "content": "Trong tiếng Anh, 'take a bus' mang nghĩa sử dụng xe buýt làm phương tiện di chuyển."}])

# Save checkpoint
with open('scratch/enrich_p3_p4.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"make_p3_p4.py saved {len(data)} questions!")
