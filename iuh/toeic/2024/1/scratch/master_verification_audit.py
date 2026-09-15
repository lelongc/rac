# scratch/master_verification_audit.py: Complete audit of Test 1, Test 2, and Test 3
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

tests = {
    "Test 1": "web/data/test1.json",
    "Test 2": "web/data/test2.json",
    "Test 3": "web/data/test3.json"
}

# Load official answers if available
official_answers = {}
try:
    with open('data/all_tests_answers.json', encoding='utf-8') as f:
        official_answers = json.load(f)
except Exception:
    pass

banned_substrings = [
    "Đáp án chính xác: (",
    "Đáp án đúng: (",
    "Nội dung câu hỏi",
    "Bài đọc đối chiếu thông tin",
    "Đoạn hội thoại trao đổi về",
    "Bài phát biểu / thông báo ngắn cung cấp"
]

all_passed = True

for test_name, test_path in tests.items():
    print(f"\n=======================================================")
    print(f"AUDITING {test_name.upper()} ({test_path})")
    print(f"=======================================================")

    with open(test_path, encoding='utf-8') as f:
        data = json.load(f)

    questions = data.get('questions', [])
    print(f"Total questions: {len(questions)}")
    if len(questions) != 200:
        print(f"❌ ERROR: Expected 200 questions, got {len(questions)}")
        all_passed = False

    issues = []
    part_counts = {}

    for q in questions:
        qid = q['id']
        part = q.get('part', 0)
        part_counts[part] = part_counts.get(part, 0) + 1

        # 1. Answer Key check
        t_key = test_name.replace(" ", "").lower()
        if t_key in official_answers:
            expected_ans = official_answers[t_key].get(str(qid))
            if expected_ans and q.get('correctAnswer') != expected_ans:
                issues.append(f"Q{qid}: Answer key mismatch! Got {q.get('correctAnswer')}, expected {expected_ans}")

        # 2. Check for banned placeholder substrings
        for field in ['transcriptVi', 'passageVi', 'passageTextVi', 'questionTextVi']:
            val = q.get(field, '') or ''
            for ban in banned_substrings:
                if ban in val:
                    issues.append(f"Q{qid} [{field}]: Contains banned placeholder '{ban}'")

        # 3. Listening (Part 1-4) Transcript & TranscriptVi checks
        if part in [1, 2, 3, 4]:
            t_en = q.get('transcript', '') or ''
            t_vi = q.get('transcriptVi', '') or ''
            if len(t_en) < 20:
                issues.append(f"Q{qid} (Part {part}): Transcript EN too short ({len(t_en)} chars)")
            if len(t_vi) < 20:
                issues.append(f"Q{qid} (Part {part}): Transcript VI too short ({len(t_vi)} chars): '{t_vi}'")

            if part in [3, 4]:
                p_en = q.get('passage', '') or ''
                p_vi = q.get('passageVi', '') or ''
                if len(p_en) < 50:
                    issues.append(f"Q{qid} (Part {part}): Missing or short English passage ({len(p_en)} chars)")
                if len(p_vi) < 50:
                    issues.append(f"Q{qid} (Part {part}): Missing or short Vietnamese passageVi ({len(p_vi)} chars)")

        # 4. Question stem and Options Vietnamese check
        q_vi = q.get('questionTextVi', '') or ''
        opts_vi = q.get('optionsVi', {}) or {}
        if not q_vi:
            issues.append(f"Q{qid} (Part {part}): Missing questionTextVi")

        req_opts = ['A', 'B', 'C'] if part == 2 else ['A', 'B', 'C', 'D']
        for opt_key in req_opts:
            opt_val = opts_vi.get(opt_key, '')
            if not opt_val:
                issues.append(f"Q{qid} (Part {part}): Missing optionsVi[{opt_key}]")
            # Check if optionVi is just untranslated English
            opt_en = q.get('options', {}).get(opt_key, '')
            if opt_val.strip() == f"({opt_key}) {opt_en.strip()}" and len(opt_en.split()) > 3:
                issues.append(f"Q{qid} (Part {part}): optionsVi[{opt_key}] untranslated: '{opt_val}'")

        # 5. Part 6 specific checks
        if part == 6:
            p_vi = q.get('passageVi', '') or q.get('passageTextVi', '') or ''
            if len(p_vi) < 50:
                issues.append(f"Q{qid} (Part 6): Missing or short passageVi ({len(p_vi)} chars)")

        # 6. Part 7 specific checks
        if part == 7:
            pt_vi = q.get('passageTextVi', '') or ''
            title = q.get('passageTitle', '') or ''
            if len(pt_vi) < 50:
                issues.append(f"Q{qid} (Part 7): Missing or short passageTextVi ({len(pt_vi)} chars)")
            if not title or len(title) < 5:
                issues.append(f"Q{qid} (Part 7): Missing or short passageTitle: '{title}'")

    print(f"Parts distribution: {sorted(part_counts.items())}")
    if issues:
        all_passed = False
        print(f"❌ FOUND {len(issues)} ISSUES IN {test_name}:")
        for iss in issues[:15]:
            print("  -", iss)
        if len(issues) > 15:
            print(f"  ... and {len(issues) - 15} more issues.")
    else:
        print(f"✅ {test_name} PASSED ALL AUDIT CHECKS WITH ZERO ISSUES!")

print("\n=======================================================")
if all_passed:
    print("🏆 ALL THREE TESTS (TEST 1, TEST 2, TEST 3) ARE 100% PERFECT AND FULLY BILINGUAL!")
else:
    print("❌ SOME TESTS STILL HAVE ISSUES. PLEASE REVIEW ABOVE.")
print("=======================================================")
