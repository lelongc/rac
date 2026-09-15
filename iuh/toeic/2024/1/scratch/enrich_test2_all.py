# scratch/enrich_test2_all.py: Master enrichment script for Test 2
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

with open('all_tests_answers.json', encoding='utf-8') as f:
    all_ans = json.load(f)
t2_official = all_ans.get('test2', {})

with open('scratch/t2_p2_enrichment.json', encoding='utf-8') as f:
    t2_p2 = json.load(f)

with open('scratch/ocr_rc_test2.json', encoding='utf-8') as f:
    ocr2 = json.load(f)

with open('web/data/vocab_bank.json', encoding='utf-8') as f:
    vb_list = json.load(f)

# Build a lookup dictionary of high-quality vocab by lowercase word
vb_dict = {v['word'].lower(): v for v in vb_list}

# Curated vocabulary dictionary for Test 2 key topics
custom_vocab = {
    # Part 3: Ferry, boat, commute, cafe, clothing store, welding, seedlings, delivery
    "ferry": {"word": "ferry", "ipa": "/ˈfer.i/", "pos": "n", "meaning": "phà, tàu chở khách đường thủy", "example": "The commuter ferry docks at Pier 5 every thirty minutes."},
    "fog": {"word": "fog", "ipa": "/fɒɡ/", "pos": "n", "meaning": "sương mù dày đặc", "example": "Dense harbor fog delayed coastal ferry departures."},
    "dock": {"word": "dock", "ipa": "/dɒk/", "pos": "v, n", "meaning": "cập bến, bến tàu", "example": "The captain guided the passenger ship safely to the dock."},
    "cafe": {"word": "cafe", "ipa": "/ˈkæf.eɪ/", "pos": "n", "meaning": "quán cà phê, tiệm giải khát", "example": "Patrons enjoy fresh croissants at the outdoor sidewalk cafe."},
    "menu": {"word": "menu", "ipa": "/ˈmen.juː/", "pos": "n", "meaning": "thực đơn ăn uống", "example": "The chef added seasonal vegetable soups to the lunch menu."},
    "pastry": {"word": "pastry", "ipa": "/ˈpeɪ.stri/", "pos": "n", "meaning": "bánh ngọt nướng", "example": "The bakery specializes in flaky French fruit pastries."},
    "presentation": {"word": "presentation", "ipa": "/ˌprez.ənˈteɪ.ʃən/", "pos": "n", "meaning": "bài thuyết trình, phần trình bày", "example": "Prepare compelling visual slides for the investor presentation."},
    "handout": {"word": "handout", "ipa": "/ˈhænd.aʊt/", "pos": "n", "meaning": "tài liệu phát tay cho người dự", "example": "Distribute printed handouts before the seminar commences."},
    "feedback": {"word": "feedback", "ipa": "/ˈfiːd.bæk/", "pos": "n", "meaning": "ý kiến phản hồi, nhận xét", "example": "Customer feedback led to substantial software improvements."},
    "apparel": {"word": "apparel", "ipa": "/əˈpær.əl/", "pos": "n", "meaning": "quần áo, trang phục thời trang", "example": "The retail boutique stocks organic cotton children's apparel."},
    "inventory": {"word": "inventory", "ipa": "/ˈɪn.vən.tər.i/", "pos": "n", "meaning": "hàng tồn kho, sự kiểm kê", "example": "Conduct monthly inventory audits to detect warehouse discrepancies."},
    "discount": {"word": "discount", "ipa": "/ˈdɪs.kaʊnt/", "pos": "n", "meaning": "mức chiết khấu, giảm giá", "example": "Loyal members receive a ten percent discount on all merchandise."},
    "measure": {"word": "measure", "ipa": "/ˈmeʒ.ər/", "pos": "v", "meaning": "đo đạc kích thước", "example": "Measure the room dimensions before ordering conference tables."},
    "renovation": {"word": "renovation", "ipa": "/ˌren.əˈveɪ.ʃən/", "pos": "n", "meaning": "sự tu sửa, cải tạo công trình", "example": "The historic cinema underwent a modern architectural renovation."},
    "contractor": {"word": "contractor", "ipa": "/kənˈtræk.tər/", "pos": "n", "meaning": "nhà thầu thi công", "example": "The general contractor managed electrical and plumbing subteams."},
    "seedling": {"word": "seedling", "ipa": "/ˈsiːd.lɪŋ/", "pos": "n", "meaning": "cây giống, mầm cây non", "example": "Transplant tomato seedlings into fertile organic compost."},
    "greenhouse": {"word": "greenhouse", "ipa": "/ˈɡriːn.haʊs/", "pos": "n", "meaning": "nhà kính trồng hoa màu", "example": "Botanists cultivate rare tropical orchids inside the greenhouse."},
    "fertilizer": {"word": "fertilizer", "ipa": "/ˈfɜː.tɪ.laɪ.zər/", "pos": "n", "meaning": "phân bón cây trồng", "example": "Organic fertilizer improves soil vitality without toxic runoff."},
    "delivery": {"word": "delivery", "ipa": "/dɪˈlɪv.ər.i/", "pos": "n", "meaning": "sự giao hàng, chuyến hàng", "example": "Express parcel delivery takes less than twenty-four hours."},
    "receipt": {"word": "receipt", "ipa": "/rɪˈsiːt/", "pos": "n", "meaning": "hóa đơn thanh toán, biên lai", "example": "Keep the cash receipt to claim full merchandise refunds."},
    "confirm": {"word": "confirm", "ipa": "/kənˈfɜːm/", "pos": "v", "meaning": "xác nhận lại tính chính xác", "example": "Please confirm your arrival time with the front desk."},

    # Part 4: Jewelry, audio guide, radio broadcast, train delays, factory inspection
    "jewelry": {"word": "jewelry", "ipa": "/ˈdʒuː.əl.ri/", "pos": "n", "meaning": "đồ kim hoàn, trang sức", "example": "Artisans handcraft silver jewelry embellished with local gems."},
    "exhibition": {"word": "exhibition", "ipa": "/ˌek.sɪˈbɪʃ.ən/", "pos": "n", "meaning": "cuộc triển lãm, trưng bày", "example": "The gallery curator opened a retrospective photography exhibition."},
    "artisan": {"word": "artisan", "ipa": "/ˌɑː.tɪˈzæn/", "pos": "n", "meaning": "thợ thủ công lành nghề", "example": "Skilled artisans carved traditional wooden decorative masks."},
    "broadcast": {"word": "broadcast", "ipa": "/ˈbrɔːd.kɑːst/", "pos": "v, n", "meaning": "phát sóng; chương trình phát thanh", "example": "The national radio network broadcasts financial updates hourly."},
    "commuter": {"word": "commuter", "ipa": "/kəˈmjuː.tər/", "pos": "n", "meaning": "người đi làm bằng phương tiện công cộng", "example": "Commuters crowded onto platforms during Monday morning rush hour."},
    "platform": {"word": "platform", "ipa": "/ˈplæt.fɔːm/", "pos": "n", "meaning": "sân ga tàu hỏa, nền tảng", "example": "Passengers must wait behind the safety line on the platform."},
    "inspection": {"word": "inspection", "ipa": "/ɪnˈspek.ʃən/", "pos": "n", "meaning": "cuộc thanh tra, kiểm tra kỹ thuật", "example": "Routine safety inspections prevent dangerous workplace mishaps."},
    "regulation": {"word": "regulation", "ipa": "/ˌreɡ.jəˈleɪ.ʃən/", "pos": "n", "meaning": "quy định, quy chế pháp lý", "example": "Factories adhere strictly to environmental wastewater regulations."},
    "compliance": {"word": "compliance", "ipa": "/kəmˈplaɪ.əns/", "pos": "n", "meaning": "sự tuân thủ đúng chuẩn mực", "example": "Audit reports verified total compliance with safety codes."},

    # Part 7: Savan Business Center, Dine Out, Rainsy, Claro Vision, Qualiview, Fezker
    "webinar": {"word": "webinar", "ipa": "/ˈweb.ɪ.nɑːr/", "pos": "n", "meaning": "hội thảo trực tuyến", "example": "Register online for the interactive digital marketing webinar."},
    "announcement": {"word": "announcement", "ipa": "/əˈnaʊns.mənt/", "pos": "n", "meaning": "thông báo, bản tin công bố", "example": "The CEO made a formal announcement regarding the merger."},
    "restaurant": {"word": "restaurant", "ipa": "/ˈres.trɒnt/", "pos": "n", "meaning": "nhà hàng ẩm thực", "example": "Award-winning restaurants feature in the annual culinary guide."},
    "dining": {"word": "dining", "ipa": "/ˈdaɪ.nɪŋ/", "pos": "n", "meaning": "việc ăn uống tại nhà hàng", "example": "The city offers diverse fine dining experiences."},
    "headquarters": {"word": "headquarters", "ipa": "/ˌhedˈkwɔː.təz/", "pos": "n", "meaning": "trụ sở chính của công ty", "example": "Senior executives convene quarterly meetings at headquarters."},
    "branch": {"word": "branch", "ipa": "/brɑːntʃ/", "pos": "n", "meaning": "chi nhánh ngân hàng/công ty", "example": "The commercial bank opened three new regional branches."},
    "eyewear": {"word": "eyewear", "ipa": "/ˈaɪ.weər/", "pos": "n", "meaning": "kính mắt, kính thời trang", "example": "Optometrists stock designer prescription eyewear frames."},
    "examination": {"word": "examination", "ipa": "/ɪɡˌzæm.ɪˈneɪ.ʃən/", "pos": "n", "meaning": "cuộc kiểm tra sức khỏe/khám mắt", "example": "Schedule a comprehensive eye examination every two years."},
    "contract": {"word": "contract", "ipa": "/ˈkɒn.trækt/", "pos": "n", "meaning": "hợp đồng giao kết", "example": "Both parties signed the multi-year equipment lease contract."},
    "shipping": {"word": "shipping", "ipa": "/ˈʃɪp.ɪŋ/", "pos": "n", "meaning": "ngành vận tải đường biển/vận chuyển", "example": "Global shipping lines faced severe port container congestion."},
    "container": {"word": "container", "ipa": "/kənˈteɪ.nər/", "pos": "n", "meaning": "thùng công-ten-nơ chở hàng", "example": "Crews loaded freight containers onto the cargo vessel."},
    "cargo": {"word": "cargo", "ipa": "/ˈkɑː.ɡəʊ/", "pos": "n", "meaning": "hàng hóa chuyên chở bằng tàu/máy bay", "example": "Inspect customs manifests before discharging international cargo."},
    "ice cream": {"word": "ice cream", "ipa": "/ˌaɪs ˈkriːm/", "pos": "n", "meaning": "kem ăn tráng miệng", "example": "The artisan parlour crafts dairy-free gelato and ice cream."},
    "flavor": {"word": "flavor", "ipa": "/ˈfleɪ.vər/", "pos": "n", "meaning": "hương vị ẩm thực", "example": "Taste testers evaluated four experimental ice cream flavors."},
    "survey": {"word": "survey", "ipa": "/ˈsɜː.veɪ/", "pos": "n", "meaning": "cuộc khảo sát ý kiến khách hàng", "example": "Customer satisfaction survey results highlighted friendly service."},
    "team building": {"word": "team building", "ipa": "/ˈtiːm ˌbɪl.dɪŋ/", "pos": "n", "meaning": "hoạt động xây dựng tinh thần đồng đội", "example": "Outdoor obstacle courses foster corporate team building."},
    "review": {"word": "review", "ipa": "/rɪˈvjuː/", "pos": "n", "meaning": "bài đánh giá, nhận xét trải nghiệm", "example": "Read authentic client reviews before selecting retreat venues."},
    "organize": {"word": "organize", "ipa": "/ˈɔː.ɡən.aɪz/", "pos": "v", "meaning": "tổ chức sắp xếp sự kiện", "example": "Human resources will organize the annual staff sports day."}
}

# Mapping of Part 7 passages by question range from ocr_rc_test2.json
p7_passages = {
    (147, 148): ocr2.get('9', '')[ocr2.get('9', '').find('Questions 147-148'):].strip(),
    (149, 150): ocr2.get('10', '')[ocr2.get('10', '').find('Questions 149-150'):].strip(),
    (151, 152): ocr2.get('11', '')[ocr2.get('11', '').find('Questions 151-152'):].strip(),
    (153, 154): ocr2.get('12', '')[ocr2.get('12', '').find('Questions 153-154'):].strip(),
    (155, 157): ocr2.get('13', '')[ocr2.get('13', '').find('Questions 155-157'):].strip(),
    (158, 160): ocr2.get('14', '')[ocr2.get('14', '').find('Questions 158-160'):].strip(),
    (161, 163): ocr2.get('15', '')[ocr2.get('15', '').find('Questions 161-163'):].strip(),
    (164, 167): ocr2.get('16', '')[ocr2.get('16', '').find('Questions 164-167'):].strip(),
    (168, 171): ocr2.get('17', '')[ocr2.get('17', '').find('Questions 168-171'):].strip(),
    (172, 175): ocr2.get('18', '')[ocr2.get('18', '').find('Questions 172-175'):].strip(),
    (176, 180): ocr2.get('20', '')[ocr2.get('20', '').find('Questions 176-180'):].strip() + "\n\n" + ocr2.get('21', '')[:500].strip(),
    (181, 185): ocr2.get('22', '')[ocr2.get('22', '').find('Questions 181-185'):].strip() + "\n\n" + ocr2.get('23', '')[:500].strip(),
    (186, 190): ocr2.get('24', '')[ocr2.get('24', '').find('Questions 186-190'):].strip() + "\n\n" + ocr2.get('25', '')[:500].strip(),
    (191, 195): ocr2.get('26', '')[ocr2.get('26', '').find('Questions 191-195'):].strip() + "\n\n" + ocr2.get('27', '')[:500].strip(),
    (196, 200): ocr2.get('28', '')[ocr2.get('28', '').find('Questions 196-200'):].strip() + "\n\n" + ocr2.get('29', '')[:500].strip()
}

# Process each question in Test 2
for q in t2['questions']:
    qid = q['id']
    part = q.get('part', 1)
    
    # Check official answer
    if str(qid) in t2_official:
        q['correctAnswer'] = t2_official[str(qid)]
        
    # Part 2 application
    if str(qid) in t2_p2:
        e = t2_p2[str(qid)]
        q['explanation'] = e['exp']
        q['vocabulary'] = e['vocab']
        q['vocab'] = e['vocab']
        q['collocations'] = e['collocations']
        q['grammar'] = e['grammar']
        q['grammarPoints'] = e['grammar']
        continue

    # Part 7 passageText population
    if part == 7:
        for (qstart, qend), ptext in p7_passages.items():
            if qstart <= qid <= qend and ptext:
                q['passageText'] = ptext
                break

    # Clean up dummy confirm vocab in any remaining question
    vocs = q.get('vocabulary') or q.get('vocab') or []
    has_dummy = False
    for v in vocs:
        if v.get('meaning') == 'xác nhận, khẳng định' or v.get('ipa') == '/kənˈfɜːm/' or v.get('word') in ['what', 'there', 'which', 'will', 'have', 'most']:
            has_dummy = True
            break
            
    if has_dummy:
        # Search for words in transcript / questionText / options
        context_text = f"{q.get('questionText', '')} {str(q.get('options', {}))} {q.get('transcript', '')} {q.get('passageText', '')[:300]}"
        context_words = re.findall(r'[A-Za-z]{4,}', context_text.lower())
        
        replacement_vocabs = []
        for w in context_words:
            if w in custom_vocab and custom_vocab[w] not in replacement_vocabs:
                replacement_vocabs.append(custom_vocab[w])
            elif w in vb_dict and vb_dict[w] not in replacement_vocabs:
                # Ensure it's not a dummy word in vb_dict
                if vb_dict[w].get('meaning') != 'xác nhận, khẳng định':
                    replacement_vocabs.append(vb_dict[w])
            if len(replacement_vocabs) >= 3:
                break
                
        # If fewer than 2 found, pick contextual defaults from custom_vocab
        if len(replacement_vocabs) < 2:
            defaults = [custom_vocab["confirm"], custom_vocab["schedule"], custom_vocab["presentation"]]
            for d in defaults:
                if d not in replacement_vocabs:
                    replacement_vocabs.append(d)
                if len(replacement_vocabs) >= 2:
                    break

        q['vocabulary'] = replacement_vocabs
        q['vocab'] = replacement_vocabs

        # Enrich explanation if it was generic
        cur_exp = q.get('explanation', '')
        if 'Căn cứ nội dung' in cur_exp or 'Phương án (' in cur_exp and len(cur_exp) < 70:
            ans_letter = q.get('correctAnswer', 'A')
            ans_text = q.get('options', {}).get(ans_letter, '')
            if part in [3, 4]:
                q['explanation'] = f"Căn cứ vào manh mối được người nói nhắc tới trong đoạn thoại/bài phát biểu, phương án ({ans_letter}) '{ans_text}' là câu trả lời chính xác nhất, phản ánh đúng thông tin chi tiết và từ khóa đã nghe."
            elif part == 7:
                q['explanation'] = f"Đối chiếu thông tin chi tiết trong bài đọc, phương án ({ans_letter}) '{ans_text}' phản ánh chính xác nhất dữ kiện được nêu trong văn bản, hoàn toàn phù hợp với nội dung câu hỏi."

# Save updated test2.json
with open('web/data/test2.json', 'w', encoding='utf-8') as f:
    json.dump(t2, f, ensure_ascii=False, indent=2)

print("Enrichment applied to web/data/test2.json successfully!")

# Strict audit for Test 2
dummy_vocab = 0
zero_vocab = 0
zero_grammar = 0
zero_colloc = 0
answer_mismatches = 0

for q in t2['questions']:
    qid = q['id']
    vocs = q.get('vocabulary', [])
    if len(vocs) == 0:
        zero_vocab += 1
    for v in vocs:
        if v.get('meaning') == 'xác nhận, khẳng định' or v.get('ipa') == '/kənˈfɜːm/' or v.get('word') in ['what', 'there', 'which', 'will', 'have', 'most']:
            dummy_vocab += 1
            break
            
    if len(q.get('collocations', [])) == 0:
        zero_colloc += 1
        
    if len(q.get('grammar', []) or q.get('grammarPoints', [])) == 0:
        zero_grammar += 1
        
    if str(qid) in t2_official:
        if q['correctAnswer'] != t2_official[str(qid)]:
            answer_mismatches += 1

print("\n=== STRICT AUDIT RESULTS FOR TEST 2 ===")
print(f"Total Questions: {len(t2['questions'])}")
print(f"Dummy confirm vocab: {dummy_vocab}")
print(f"Zero vocab questions: {zero_vocab}")
print(f"Zero grammar questions: {zero_grammar}")
print(f"Zero collocation questions: {zero_colloc}")
print(f"Answer mismatches vs official keys: {answer_mismatches}")
