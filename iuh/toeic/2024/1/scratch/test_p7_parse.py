import json
import re

d = json.load(open('scratch/ocr_rc_test2.json', encoding='utf-8'))

part7_sets = [
    (147, 148, [9], 'Single Passage: Invitation / Advertisement'),
    (149, 150, [10], 'Single Passage: Text Message Discussion'),
    (151, 152, [11], 'Single Passage: Schedule / Notice'),
    (153, 154, [12], 'Single Passage: E-mail / Letter'),
    (155, 157, [13], 'Single Passage: Article / Report'),
    (158, 160, [14], 'Single Passage: Customer Feedback Form'),
    (161, 163, [15], 'Single Passage: Online Chat Discussion'),
    (164, 167, [16], 'Single Passage: Information Leaflet'),
    (168, 171, [17, 18], 'Single Passage: Webpage & Policy'),
    (172, 175, [19], 'Single Passage: Memo & Instructions'),
    (176, 180, [20, 21], 'Double Passage: E-mail and Schedule'),
    (181, 185, [22, 23], 'Double Passage: Product Brochure and Review'),
    (186, 190, [24, 25], 'Triple Passage: Announcement, Form, and Email'),
    (191, 195, [26, 27], 'Triple Passage: Webpage, Invoice, and Memo'),
    (196, 200, [28, 29], 'Triple Passage: Article, Email, and Table')
]

found_q_count = 0
for start_q, end_q, pages, title in part7_sets:
    combined = '\n\n'.join(d.get(str(p), '') for p in pages)
    for qid in range(start_q, end_q + 1):
        # Look for qid
        m = re.search(rf'(?:^|\n|\s){qid}\.?\s+(.+?)(?=\([A]\)|\bA\b[\.\)])\s*\(A\)\s*([^\(]+?)\s*\(B\)\s*([^\(]+?)\s*\(C\)\s*([^\(]+?)\s*\(D\)\s*([^\(\n\r]+)', combined, re.DOTALL)
        if m:
            found_q_count += 1
            stem = m.group(1).strip().replace('\n', ' ')
            stem = re.sub(r'^\d+\s+', '', stem)
            opt_d = m.group(5).strip().split('\n')[0].strip()
        else:
            print(f'MISSING Q{qid} in pages {pages}')

print(f'Total Part 7 questions matched: {found_q_count} / 54')
