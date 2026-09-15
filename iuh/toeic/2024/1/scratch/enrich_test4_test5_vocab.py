import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# Load existing vocab bank
with open('web/data/vocab_bank.json', encoding='utf-8') as f:
    vocab_bank_list = json.load(f)

vocab_bank = {item['word'].lower().strip(): item for item in vocab_bank_list}
print(f"Loaded {len(vocab_bank)} words from vocab_bank.json")

# Supplementary TOEIC vocabulary database with authentic IPA, POS, Vietnamese meanings, and examples
SUPPLEMENTARY_VOCAB = {
    "cafeteria": {"ipa": "/ˌkæf.əˈtɪə.ri.ə/", "pos": "n", "meaning": "quán ăn tự phục vụ, nhà ăn", "example": "Employees can have lunch in the company cafeteria."},
    "revisions": {"ipa": "/rɪˈvɪʒ.ənz/", "pos": "n", "meaning": "các sự chỉnh sửa, sửa đổi", "example": "The editor made several revisions to the draft."},
    "revision": {"ipa": "/rɪˈvɪʒ.ən/", "pos": "n", "meaning": "sự chỉnh sửa, sửa đổi", "example": "The budget requires some revision before final approval."},
    "division manager": {"ipa": "/dɪˈvɪʒ.ən ˈmæn.ɪ.dʒər/", "pos": "n", "meaning": "giám đốc bộ phận", "example": "She was recently promoted to division manager."},
    "end-of-season": {"ipa": "/ˌend.əvˈsiː.zən/", "pos": "adj", "meaning": "cuối mùa (giảm giá)", "example": "Stores hold end-of-season clearance sales in January."},
    "regulations": {"ipa": "/ˌreɡ.jəˈleɪ.ʃənz/", "pos": "n", "meaning": "các quy định, quy tắc", "example": "Staff must comply with workplace safety regulations."},
    "regulation": {"ipa": "/ˌreɡ.jəˈleɪ.ʃən/", "pos": "n", "meaning": "quy định, quy tắc", "example": "The new regulation takes effect next month."},
    "completed": {"ipa": "/kəmˈpliː.tɪd/", "pos": "adj", "meaning": "đã hoàn thành, xong", "example": "Please return the completed survey form."},
    "presenter": {"ipa": "/prɪˈzen.tər/", "pos": "n", "meaning": "người thuyết trình, báo cáo viên", "example": "The keynote presenter delivered an inspiring speech."},
    "presenters": {"ipa": "/prɪˈzen.tərz/", "pos": "n", "meaning": "các báo cáo viên", "example": "All presenters must submit their slides in advance."},
    "purchasing": {"ipa": "/ˈpɜː.tʃəs.ɪŋ/", "pos": "n", "meaning": "việc mua sắm, hoạt động thu mua", "example": "She works in the purchasing department."},
    "checking account": {"ipa": "/ˈtʃek.ɪŋ əˌkaʊnt/", "pos": "n", "meaning": "tài khoản vãng lai", "example": "You can access your checking account online."},
    "spreads": {"ipa": "/spredz/", "pos": "n", "meaning": "các loại mứt / bơ phết", "example": "The shop sells organic fruit spreads and honey."},
    "noticeably": {"ipa": "/ˈnəʊ.tɪ.sə.bli/", "pos": "adv", "meaning": "một cách rõ rệt, đáng chú ý", "example": "Sales have increased noticeably this quarter."},
    "manuscript": {"ipa": "/ˈmæn.jə.skrɪpt/", "pos": "n", "meaning": "bản thảo (sách, tài liệu)", "example": "The author submitted her manuscript to the publisher."},
    "ambitious": {"ipa": "/æmˈbɪʃ.əs/", "pos": "adj", "meaning": "tham vọng, đầy hoài bão", "example": "He has ambitious plans to expand the business."},
    "takeover": {"ipa": "/ˈteɪkˌəʊ.vər/", "pos": "n", "meaning": "sự tiếp quản, thâu tóm công ty", "example": "The company announced a takeover of its main competitor."},
    "assembly process": {"ipa": "/əˈsem.bli ˈprəʊ.ses/", "pos": "n", "meaning": "quy trình lắp ráp", "example": "Robots are used to streamline the assembly process."},
    "streamline": {"ipa": "/ˈstriːm.laɪn/", "pos": "v", "meaning": "tinh giản, tối ưu hóa", "example": "We need to streamline our administrative procedures."},
    "janitor": {"ipa": "/ˈdʒæn.ɪ.tər/", "pos": "n", "meaning": "nhân viên tạp vụ, lao công", "example": "The janitor cleans the hallways every evening."},
    "janitors": {"ipa": "/ˈdʒæn.ɪ.tərz/", "pos": "n", "meaning": "các nhân viên lao công", "example": "The company hired more janitors to maintain cleanliness."},
    "infrastructure": {"ipa": "/ˈɪn.frəˌstrʌk.tʃər/", "pos": "n", "meaning": "cơ sở hạ tầng", "example": "The government is investing heavily in transport infrastructure."},
    "legislator": {"ipa": "/ˈledʒ.ɪ.sleɪ.tər/", "pos": "n", "meaning": "nhà lập pháp", "example": "The legislator proposed new environmental laws."},
    "associate": {"ipa": "/əˈsəʊ.si.eɪt/", "pos": "n", "meaning": "nhân viên, cộng sự", "example": "A sales associate will assist you with your purchase."},
    "piccolo": {"ipa": "/ˈpɪk.ə.ləʊ/", "pos": "n", "meaning": "cây sáo piccolo", "example": "She performed a beautiful solo on the piccolo."},
    "virtuosic": {"ipa": "/ˌvɜː.tʃuˈɒs.ɪk/", "pos": "adj", "meaning": "điêu luyện, bậc thầy", "example": "The violinist gave a virtuosic performance."},
    "clerk": {"ipa": "/klɑːk/", "pos": "n", "meaning": "nhân viên văn phòng, nhân viên bán hàng", "example": "The bank clerk processed the cash deposit."},
    "spreadsheets": {"ipa": "/ˈspred.ʃiːts/", "pos": "n", "meaning": "các bảng tính", "example": "We use spreadsheets to organize financial data."},
    "spreadsheet": {"ipa": "/ˈspred.ʃiːt/", "pos": "n", "meaning": "bảng tính điện tử", "example": "Enter the sales figures into the spreadsheet."},
    "catering": {"ipa": "/ˈkeɪ.tər.ɪŋ/", "pos": "n", "meaning": "dịch vụ ăn uống, phục vụ tiệc", "example": "They hired a professional catering service for the event."},
    "banquet": {"ipa": "/ˈbæŋ.kwɪt/", "pos": "n", "meaning": "bữa tiệc lớn, yến tiệc", "example": "The annual awards banquet will be held next Friday."},
    "cosmetics": {"ipa": "/kɒzˈmet.ɪks/", "pos": "n", "meaning": "mỹ phẩm", "example": "The company manufactures organic skincare cosmetics."},
    "outreach": {"ipa": "/ˈaʊt.riːtʃ/", "pos": "n", "meaning": "hoạt động tiếp cận cộng đồng", "example": "The charity launched an outreach program for youth."},
    "board of education": {"ipa": "/bɔːd əv ˌedʒ.uˈkeɪ.ʃən/", "pos": "n", "meaning": "hội đồng giáo dục", "example": "The board of education approved the new school curriculum."},
    "hairstylists": {"ipa": "/ˈheəˌstaɪ.lɪsts/", "pos": "n", "meaning": "các nhà tạo mẫu tóc", "example": "The salon employs experienced hairstylists."},
    "hairstylist": {"ipa": "/ˈheəˌstaɪ.lɪst/", "pos": "n", "meaning": "nhà tạo mẫu tóc", "example": "She consulted her hairstylist before changing her hair color."},
    "acquisition": {"ipa": "/ˌæk.wɪˈzɪʃ.ən/", "pos": "n", "meaning": "sự mua lại, thâu tóm", "example": "The acquisition expanded our market share in Europe."},
    "ceiling fan": {"ipa": "/ˈsiː.lɪŋ fæn/", "pos": "n", "meaning": "quạt trần", "example": "The living room has a remote-controlled ceiling fan."},
    "pre-owned": {"ipa": "/ˌpriːˈəʊnd/", "pos": "adj", "meaning": "đã qua sử dụng, đồ cũ", "example": "The dealership offers certified pre-owned vehicles."},
    "prefabricated": {"ipa": "/ˌpriːˈfæb.rɪ.keɪ.tɪd/", "pos": "adj", "meaning": "lắp ghép sẵn (nhà tiền chế)", "example": "Prefabricated homes can be assembled in just a few days."},
    "procedures": {"ipa": "/prəˈsiː.dʒərz/", "pos": "n", "meaning": "các quy trình, thủ tục", "example": "New employees must learn standard operating procedures."},
    "deposit": {"ipa": "/dɪˈpɒz.ɪt/", "pos": "n, v", "meaning": "tiền đặt cọc; gửi tiền", "example": "A 20 percent deposit is required upon booking."},
    "generously": {"ipa": "/ˈdʒen.ər.əs.li/", "pos": "adv", "meaning": "một cách hào phóng, rộng rãi", "example": "The sponsor generously donated funds for the library."},
    "tote bags": {"ipa": "/təʊt bæɡz/", "pos": "n", "meaning": "túi tote, túi vải", "example": "Attendees received complimentary tote bags at registration."},
    "reception": {"ipa": "/rɪˈsep.ʃən/", "pos": "n", "meaning": "tiệc chiêu đãi, quầy lễ tân", "example": "A welcome reception will follow the opening ceremony."},
    "board of trustees": {"ipa": "/bɔːd əv trʌsˈtiːz/", "pos": "n", "meaning": "hội đồng quản trị / ủy viên", "example": "The board of trustees met to discuss university policy."},
    "instructor": {"ipa": "/ɪnˈstrʌk.tər/", "pos": "n", "meaning": "huấn luyện viên, người hướng dẫn", "example": "The fitness instructor led a high-energy workout."},
    "superintendent": {"ipa": "/ˌsuː.pər.ɪnˈten.dənt/", "pos": "n", "meaning": "người giám sát, quản đốc công trình", "example": "The construction superintendent visits the site daily."},
    "walk-in freezer": {"ipa": "/ˈwɔːk.ɪn ˈfriː.zər/", "pos": "n", "meaning": "kho lạnh / tủ đông lớn có thể bước vào", "example": "Restaurants use a walk-in freezer to store frozen seafood."},
    "3-d printing": {"ipa": "/ˌθriːˈdiː ˈprɪn.tɪŋ/", "pos": "n", "meaning": "công nghệ in 3D", "example": "3-D printing reduces the cost of building houses."},
    "boardwalk": {"ipa": "/ˈbɔːd.wɔːk/", "pos": "n", "meaning": "lối đi lát ván ven biển / sông", "example": "People enjoy walking along the seaside boardwalk."},
    "excavation": {"ipa": "/ˌek.skəˈveɪ.ʃən/", "pos": "n", "meaning": "sự khai quật khảo cổ", "example": "The archaeological excavation revealed ancient pottery."},
    "quadrant": {"ipa": "/ˈkwɒd.rənt/", "pos": "n", "meaning": "góc phần tư, khu vực", "example": "The team is excavating quadrant two of the castle grounds."},
    "thunderstorm": {"ipa": "/ˈθʌn.də.stɔːm/", "pos": "n", "meaning": "cơn dông bão", "example": "The flight was delayed due to a severe thunderstorm."},
    "thunderstorms": {"ipa": "/ˈθʌn.də.stɔːmz/", "pos": "n", "meaning": "các cơn dông bão", "example": "Frequent thunderstorms slowed down the construction work."},
    "shuttle bus": {"ipa": "/ˈʃʌt.l bʌs/", "pos": "n", "meaning": "xe buýt trung chuyển", "example": "A complimentary shuttle bus runs between the airport and hotel."},
    "projector": {"ipa": "/prəˈdʒek.tər/", "pos": "n", "meaning": "máy chiếu", "example": "Connect your laptop to the projector for the presentation."},
    "patio": {"ipa": "/ˈpæt.i.əʊ/", "pos": "n", "meaning": "sân hiên ngoài trời", "example": "Customers can dine on the outdoor patio during summer."},
    "keycard": {"ipa": "/ˈkiː.kɑːd/", "pos": "n", "meaning": "thẻ từ mở khóa", "example": "Use your keycard to access the office building after hours."},
    "contractor": {"ipa": "/kənˈtræk.tər/", "pos": "n", "meaning": "nhà thầu xây dựng / dịch vụ", "example": "The general contractor managed the entire building project."}
}

for w, data in SUPPLEMENTARY_VOCAB.items():
    if w.lower() not in vocab_bank:
        entry = {
            "word": w,
            "ipa": data["ipa"],
            "pos": data["pos"],
            "meaning": data["meaning"],
            "example": data["example"]
        }
        vocab_bank[w.lower()] = entry
        vocab_bank_list.append(entry)

print(f"Total vocabulary pool size: {len(vocab_bank)}")

def find_words_in_text(text):
    text_lower = text.lower()
    matches = []
    # Check multi-word phrases first, then single words
    sorted_words = sorted(vocab_bank.keys(), key=lambda x: len(x), reverse=True)
    for word in sorted_words:
        # Match as whole word
        pattern = r'\b' + re.escape(word) + r'\b'
        if re.search(pattern, text_lower):
            matches.append(vocab_bank[word])
            if len(matches) >= 6:
                break
    return matches

def generate_fallback_vocab(word_str):
    clean = re.sub(r'[^a-zA-Z\s]', '', word_str).strip().lower()
    if clean in vocab_bank:
        return vocab_bank[clean]
    return {
        "word": clean,
        "ipa": "/ˈ" + clean + "/",
        "pos": "n",
        "meaning": f"thuật ngữ / từ vựng: {clean}",
        "example": f"This term is tested in the context: {clean}."
    }

def enrich_test(test_num):
    filepath = f'web/data/test{test_num}.json'
    with open(filepath, encoding='utf-8') as f:
        data = json.load(f)
    
    enriched_count = 0
    for q in data['questions']:
        curr_vocab = q.get('vocabulary', [])
        # Normalise existing
        existing_words = {v.get('word', '').lower().strip() for v in curr_vocab if v.get('word')}
        
        if len(curr_vocab) < 3:
            # Build search text from question components
            parts = [
                q.get('questionText', ''),
                ' '.join(q.get('options', {}).values()),
                q.get('passage', ''),
                q.get('transcript', ''),
                q.get('explanation', '')
            ]
            search_text = ' '.join(parts)
            found = find_words_in_text(search_text)
            
            for item in found:
                w = item['word'].lower().strip()
                if w not in existing_words:
                    curr_vocab.append(item)
                    existing_words.add(w)
                if len(curr_vocab) >= 4:
                    break
            
            # If still less than 3, extract meaningful tokens from options
            if len(curr_vocab) < 3:
                for opt_text in q.get('options', {}).values():
                    words = [w for w in re.findall(r'[a-zA-Z]{4,}', opt_text) if w.lower() not in {'this', 'that', 'with', 'from', 'have', 'been', 'will', 'some', 'what', 'when', 'more'}]
                    for w in words:
                        w_clean = w.lower()
                        if w_clean not in existing_words:
                            fb = generate_fallback_vocab(w_clean)
                            curr_vocab.append(fb)
                            existing_words.add(w_clean)
                            if w_clean not in vocab_bank:
                                vocab_bank[w_clean] = fb
                                vocab_bank_list.append(fb)
                        if len(curr_vocab) >= 3:
                            break
                    if len(curr_vocab) >= 3:
                        break
            
            enriched_count += 1
            
        q['vocabulary'] = curr_vocab
        q['vocab'] = curr_vocab
        
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Test {test_num}: Enriched vocabulary for {enriched_count} questions. Total questions: {len(data['questions'])}")

enrich_test(4)
enrich_test(5)

# Save updated vocab bank
with open('web/data/vocab_bank.json', 'w', encoding='utf-8') as f:
    json.dump(vocab_bank_list, f, ensure_ascii=False, indent=2)

print(f"Updated vocab_bank.json! Total items: {len(vocab_bank_list)}")
