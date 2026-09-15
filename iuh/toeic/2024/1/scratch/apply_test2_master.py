# scratch/apply_test2_master.py: Master application & verification for Test 2
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

with open('all_tests_answers.json', encoding='utf-8') as f:
    all_answers = json.load(f)
t2_official = all_answers.get('test2', {})

with open('scratch/t2_p2_enrichment.json', encoding='utf-8') as f:
    t2_p2 = json.load(f)

with open('scratch/t2_p3_enrichment.json', encoding='utf-8') as f:
    t2_p3 = json.load(f)

with open('scratch/t2_p4_enrichment.json', encoding='utf-8') as f:
    t2_p4 = json.load(f)

with open('scratch/t2_p5_p6_addons.json', encoding='utf-8') as f:
    t2_p5_p6_addons = json.load(f)

with open('scratch/t2_p7_p1_enrichment.json', encoding='utf-8') as f:
    t2_p7_p1 = json.load(f)

with open('scratch/t2_p7_p2_enrichment.json', encoding='utf-8') as f:
    t2_p7_p2 = json.load(f)

t2_p7 = {**t2_p7_p1, **t2_p7_p2}

# Extract Part 7 passages from ocr_rc_test2.json
with open('scratch/ocr_rc_test2.json', encoding='utf-8') as f:
    ocr2 = json.load(f)

def clean_passage(text, end_pattern=r'\b(1[4-9][0-9]|200)\.'):
    m = re.search(end_pattern, text)
    if m:
        return text[:m.start()].strip()
    return text.strip()

p7_passages = {
    (147, 148): clean_passage(ocr2['9'][ocr2['9'].find('Questions 147-148'):]),
    (149, 150): clean_passage(ocr2['10'][ocr2['10'].find('Questions 149-150'):]),
    (151, 152): clean_passage(ocr2['11'][ocr2['11'].find('Questions 151-152'):]),
    (153, 154): clean_passage(ocr2['12'][ocr2['12'].find('Questions 153-154'):]),
    (155, 157): clean_passage(ocr2['13'][ocr2['13'].find('Questions 155-157'):]),
    (158, 160): clean_passage(ocr2['14'][ocr2['14'].find('Questions 158-160'):]),
    (161, 163): clean_passage(ocr2['15'][ocr2['15'].find('Questions 161-163'):]),
    (164, 167): clean_passage(ocr2['16'][ocr2['16'].find('Questions 164-167'):]),
    (168, 171): clean_passage(ocr2['17'][ocr2['17'].find('Questions 168-171'):]),
    (172, 175): clean_passage(ocr2['18'][ocr2['18'].find('Questions 172-175'):]),
    (176, 180): clean_passage(ocr2['20'][ocr2['20'].find('Questions 176-180'):]),
    (181, 185): clean_passage(ocr2['22'][ocr2['22'].find('Questions 181-185'):]),
    (186, 190): clean_passage(ocr2['24'][ocr2['24'].find('Questions 186-190'):]) + "\n\n" + clean_passage(ocr2['25']),
    (191, 195): clean_passage(ocr2['26'][ocr2['26'].find('Questions 191-195'):]) + "\n\n" + clean_passage(ocr2['27']),
    (196, 200): clean_passage(ocr2['28'][ocr2['28'].find('Questions 196-200'):]) + ("\n\n" + clean_passage(ocr2.get('29', '')) if ocr2.get('29', '') else "")
}

# Add extra collocations for Part 1
p1_extra_colloc = {
    1: {"phrase": "bend down", "meaning": "cúi người xuống"},
    2: {"phrase": "outdoor bench", "meaning": "băng ghế ngoài trời"},
    4: {"phrase": "wooden fence", "meaning": "hàng rào gỗ"},
    6: {"phrase": "two levels", "meaning": "hai tầng, hai ngăn"}
}

for q in t2['questions']:
    qid = q['id']
    s_id = str(qid)
    part = q.get('part', 1)

    # Official answer key enforcement
    if s_id in t2_official:
        q['correctAnswer'] = t2_official[s_id]

    # Part 1 extra collocations
    if part == 1 and qid in p1_extra_colloc:
        existing_colls = q.get('collocations', [])
        if not any(c['phrase'] == p1_extra_colloc[qid]['phrase'] for c in existing_colls):
            existing_colls.append(p1_extra_colloc[qid])
        q['collocations'] = existing_colls

    # Part 2 application
    elif s_id in t2_p2:
        e = t2_p2[s_id]
        q['explanation'] = e['exp']
        q['vocabulary'] = e['vocab']
        q['vocab'] = e['vocab']
        q['collocations'] = e['collocations']
        q['grammar'] = e['grammar']
        q['grammarPoints'] = e['grammar']

    # Part 3 application
    elif s_id in t2_p3:
        e = t2_p3[s_id]
        q['explanation'] = e['exp']
        q['vocabulary'] = e['vocab']
        q['vocab'] = e['vocab']
        q['collocations'] = e['collocations']
        q['grammar'] = e['grammar']
        q['grammarPoints'] = e['grammar']

    # Part 4 application
    elif s_id in t2_p4:
        e = t2_p4[s_id]
        q['explanation'] = e['exp']
        q['vocabulary'] = e['vocab']
        q['vocab'] = e['vocab']
        q['collocations'] = e['collocations']
        q['grammar'] = e['grammar']
        q['grammarPoints'] = e['grammar']

    # Part 5 & 6 polish addons
    elif part in [5, 6]:
        if s_id in t2_p5_p6_addons:
            addon = t2_p5_p6_addons[s_id]
            vocs = q.get('vocabulary') or q.get('vocab') or []
            if 'extra_vocab' in addon:
                for ev in addon['extra_vocab']:
                    if not any(v['word'] == ev['word'] for v in vocs):
                        vocs.append(ev)
            q['vocabulary'] = vocs
            q['vocab'] = vocs

            colls = q.get('collocations') or []
            if 'extra_colloc' in addon:
                for ec in addon['extra_colloc']:
                    if not any(c['phrase'] == ec['phrase'] for c in colls):
                        colls.append(ec)
            q['collocations'] = colls

    # Part 7 application
    elif s_id in t2_p7:
        e = t2_p7[s_id]
        q['explanation'] = e['exp']
        q['vocabulary'] = e['vocab']
        q['vocab'] = e['vocab']
        q['collocations'] = e['collocations']
        q['grammar'] = e['grammar']
        q['grammarPoints'] = e['grammar']

        # Populate passageText
        for (qstart, qend), ptext in p7_passages.items():
            if qstart <= qid <= qend:
                q['passageText'] = ptext
                break

    # Synchronize aliases
    if 'vocabulary' in q:
        q['vocab'] = q['vocabulary']
    elif 'vocab' in q:
        q['vocabulary'] = q['vocab']

    if 'grammar' in q:
        q['grammarPoints'] = q['grammar']
    elif 'grammarPoints' in q:
        q['grammar'] = q['grammarPoints']

# Save updated test2.json
with open('web/data/test2.json', 'w', encoding='utf-8') as f:
    json.dump(t2, f, ensure_ascii=False, indent=2)

print("Saved updated web/data/test2.json successfully!\n")

# Run exhaustive audit
dummy_vocab = 0
lt_2_vocab = 0
lt_2_colloc = 0
zero_grammar = 0
short_exp = 0
answer_mismatches = 0
missing_passage_p7 = 0

for q in t2['questions']:
    qid = q['id']
    vocs = q.get('vocabulary') or []
    colls = q.get('collocations') or []
    gram = q.get('grammar') or []
    exp = q.get('explanation') or ''
    ptext = q.get('passageText') or ''

    # Check dummy vocab
    for v in vocs:
        if v.get('meaning') == 'xác nhận, khẳng định' or v.get('ipa') == '/kənˈfɜːm/' or v.get('word') in ['what', 'there', 'which', 'will', 'have', 'most']:
            dummy_vocab += 1
            print(f"Warning: Dummy vocab in Q{qid}: {v}")

    if len(vocs) < 2:
        lt_2_vocab += 1
        print(f"Warning: Q{qid} has < 2 vocab: {len(vocs)}")

    if len(colls) < 2:
        lt_2_colloc += 1
        print(f"Warning: Q{qid} has < 2 collocations: {len(colls)}")

    if len(gram) < 1:
        zero_grammar += 1
        print(f"Warning: Q{qid} has 0 grammar")

    if len(exp) < 60:
        short_exp += 1
        print(f"Warning: Q{qid} has short explanation ({len(exp)} chars)")

    if q.get('part') == 7 and len(ptext) < 100:
        missing_passage_p7 += 1
        print(f"Warning: Q{qid} Part 7 has missing passageText")

    if str(qid) in t2_official:
        if q.get('correctAnswer') != t2_official[str(qid)]:
            answer_mismatches += 1
            print(f"Mismatch in Q{qid}: got {q.get('correctAnswer')} vs official {t2_official[str(qid)]}")

print("\n" + "="*50)
print("=== EXHAUSTIVE QUALITY AUDIT FOR TEST 2 ===")
print("="*50)
print(f"Total Questions Evaluated: {len(t2['questions'])} / 200")
print(f"Dummy confirm vocab count: {dummy_vocab}")
print(f"Questions with < 2 vocabulary: {lt_2_vocab}")
print(f"Questions with < 2 collocations: {lt_2_colloc}")
print(f"Questions with 0 grammar points: {zero_grammar}")
print(f"Questions with short explanations: {short_exp}")
print(f"Part 7 questions missing passageText: {missing_passage_p7}")
print(f"Answer key mismatches vs official keys: {answer_mismatches}")
print("="*50)
