import fitz, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def parse_quadrant_answers(pdf_path, page_idx, x_range, y_range, offset=0):
    doc = fitz.open(pdf_path)
    page = doc[page_idx]
    words = page.get_text("words")
    
    # Filter words in quadrant
    q_words = [w for w in words if x_range[0] <= w[0] <= x_range[1] and y_range[0] <= w[1] <= y_range[1]]
    # sort by y, then x
    # We want pairs of (question_num, answer_char)
    # in TOEIC answer sheet, numbers are 1..100 or 101..200
    # and answers are (A), (B), (C), (D)
    text = " ".join([w[4] for w in sorted(q_words, key=lambda w: (round(w[1]/10)*10, w[0]))])
    
    # Find all pairs like "1 (A)" or "101 (B)" or "1(A)"
    # Sometimes number and (A) are together or separate
    pairs = re.findall(r'(\b\d{1,3}\b)\s*\(?([A-D])\)?', text)
    answers = {}
    for num_str, ans in pairs:
        num = int(num_str)
        if 1 <= num <= 200:
            answers[num] = ans
    return answers

# Test 4 LC: Page 2 (idx 1), x in [300, 595], y in [400, 793]
t4_lc = parse_quadrant_answers('giai/ĐÁP ÁN ETS 2024 LC.pdf', 1, (300, 595), (400, 793))
# Test 4 RC: Page 2 (idx 1), x in [300, 595], y in [400, 793]
t4_rc = parse_quadrant_answers('giai/ĐÁP ÁN ETS 2024 RC.pdf', 1, (300, 595), (400, 793))

t4_answers = {**t4_lc, **t4_rc}
print(f"Test 4 official answers parsed: {len(t4_answers)} / 200 (LC={len(t4_lc)}, RC={len(t4_rc)})")

# Test 5 LC: Page 3 (idx 2), x in [0, 320], y in [50, 420]
t5_lc = parse_quadrant_answers('giai/ĐÁP ÁN ETS 2024 LC.pdf', 2, (0, 320), (50, 420))
# Test 5 RC: Page 3 (idx 2), x in [0, 320], y in [50, 420]
t5_rc = parse_quadrant_answers('giai/ĐÁP ÁN ETS 2024 RC.pdf', 2, (0, 320), (50, 420))

t5_answers = {**t5_lc, **t5_rc}
print(f"Test 5 official answers parsed: {len(t5_answers)} / 200 (LC={len(t5_lc)}, RC={len(t5_rc)})")

with open('scratch/test4_official_answers.json', 'w', encoding='utf-8') as f:
    json.dump({str(k): v for k, v in sorted(t4_answers.items())}, f, indent=2)

with open('scratch/test5_official_answers.json', 'w', encoding='utf-8') as f:
    json.dump({str(k): v for k, v in sorted(t5_answers.items())}, f, indent=2)

print("Saved scratch/test4_official_answers.json and scratch/test5_official_answers.json")
