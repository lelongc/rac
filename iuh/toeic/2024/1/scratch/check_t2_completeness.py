import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/test2.json', encoding='utf-8') as f:
    t2 = json.load(f)

print("=== CHECKING TEST 2 COMPLETENESS ===")
for part_no in [1, 2, 3, 4, 5, 6, 7]:
    qs = [q for q in t2['questions'] if q.get('part') == part_no]
    print(f"\n--- Part {part_no} (count: {len(qs)}) ---")
    sample = qs[0]
    print(f"Q{sample['id']}:")
    print("  questionTextVi:", sample.get('questionTextVi', '')[:80])
    print("  optionsVi:", sample.get('optionsVi'))
    print("  transcript preview:", (sample.get('transcript') or '')[:80].replace('\n', ' '))
    print("  transcriptVi preview:", (sample.get('transcriptVi') or '')[:80].replace('\n', ' '))
    if 'passageVi' in sample:
        print("  passageVi preview:", sample.get('passageVi', '')[:80].replace('\n', ' '))
    if 'passageTextVi' in sample:
        print("  passageTextVi preview:", sample.get('passageTextVi', '')[:80].replace('\n', ' '))

# Check for any remaining placeholder strings in test 2
bad_phrases = ["Đáp án chính xác: (", "Nội dung câu hỏi", "Bài đọc đối chiếu thông tin", "Chọn phương án thích hợp nhất cho", "Đoạn hội thoại trao đổi về"]
issues = []
for q in t2['questions']:
    qid = q['id']
    t_vi = q.get('transcriptVi', '')
    p_vi = q.get('passageVi', '')
    pt_vi = q.get('passageTextVi', '')
    q_vi = q.get('questionTextVi', '')
    opts_vi = q.get('optionsVi', {})
    
    if len(t_vi) < 20 and q.get('part') in [1, 2, 3, 4]:
        issues.append(f"Q{qid}: short transcriptVi ({len(t_vi)} chars): '{t_vi}'")
    if p_vi and ("trao đổi về" in p_vi or len(p_vi) < 40):
        issues.append(f"Q{qid}: placeholder passageVi: '{p_vi}'")
    if pt_vi and ("Bài đọc đối chiếu thông tin" in pt_vi or len(pt_vi) < 40):
        issues.append(f"Q{qid}: placeholder passageTextVi: '{pt_vi}'")
    if not q_vi:
        issues.append(f"Q{qid}: missing questionTextVi")

print(f"\nTotal issues found in Test 2: {len(issues)}")
if issues:
    for iss in issues[:10]:
        print(" ", iss)
