import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test1.json', encoding='utf-8') as f:
    t1 = json.load(f)

with open('web/data/vocab_bank.json', encoding='utf-8') as f:
    vb_list = json.load(f)

vb_dict = {v['word'].lower(): v for v in vb_list if v.get('meaning') != 'xác nhận, khẳng định'}

# Part 7 passage propagation across sets
p7_ranges = [
    (147, 148), (149, 150), (151, 152), (153, 154), (155, 157),
    (158, 160), (161, 163), (164, 167), (168, 171), (172, 175),
    (176, 180), (181, 185), (186, 190), (191, 195), (196, 200)
]

for s, e in p7_ranges:
    group = [q for q in t1['questions'] if s <= q['id'] <= e]
    if not group:
        continue
    longest_p = max((q.get('passageText') or '' for q in group), key=len)
    if len(longest_p) > 100:
        for q in group:
            if len(q.get('passageText') or '') < len(longest_p):
                q['passageText'] = longest_p

# For any question in Test 1 with < 2 vocab or < 2 collocations, enrich them
for q in t1['questions']:
    vocs = q.get('vocabulary') or q.get('vocab') or []
    colls = q.get('collocations') or []
    
    # Enrich vocab if < 2
    if len(vocs) < 2:
        context = f"{q.get('questionText', '')} {q.get('transcript', '')} {q.get('passage', '')} {q.get('passageText', '')[:300]}"
        words = re.findall(r'[A-Za-z]{4,}', context.lower())
        for w in words:
            if w in vb_dict:
                item = vb_dict[w]
                if not any(v.get('word', '').lower() == w for v in vocs):
                    vocs.append(item)
                    if len(vocs) >= 2:
                        break
        # Fallback if still < 2
        fallbacks = [
            {"word": "schedule", "ipa": "/ˈʃedʒ.uːl/", "pos": "n, v", "meaning": "lịch trình, thời gian biểu", "example": "The conference schedule was distributed to all attendees."},
            {"word": "requirement", "ipa": "/rɪˈkwaɪə.mənt/", "pos": "n", "meaning": "yêu cầu, điều kiện cần thiết", "example": "Applicants must meet all educational requirements for the job."},
            {"word": "feedback", "ipa": "/ˈfiːd.bæk/", "pos": "n", "meaning": "ý kiến phản hồi, nhận xét", "example": "Client feedback helped us improve our services significantly."}
        ]
        for fb in fallbacks:
            if len(vocs) >= 2:
                break
            if not any(v.get('word', '').lower() == fb['word'] for v in vocs):
                vocs.append(fb)

    q['vocabulary'] = vocs
    q['vocab'] = vocs

    # Enrich collocations if < 2
    if len(colls) < 2:
        extra_c = [
            {"phrase": "customer satisfaction", "meaning": "sự hài lòng của khách hàng"},
            {"phrase": "work efficiently", "meaning": "làm việc hiệu quả, năng suất"},
            {"phrase": "business trip", "meaning": "chuyến đi công tác"}
        ]
        for ec in extra_c:
            if len(colls) >= 2:
                break
            if not any(c.get('phrase') == ec['phrase'] for c in colls):
                colls.append(ec)
        q['collocations'] = colls

    # Sync grammar
    if 'grammar' in q:
        q['grammarPoints'] = q['grammar']
    elif 'grammarPoints' in q:
        q['grammar'] = q['grammarPoints']

with open('web/data/test1.json', 'w', encoding='utf-8') as f:
    json.dump(t1, f, ensure_ascii=False, indent=2)

print("Polished Test 1 successfully!")
