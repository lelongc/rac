import fitz
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("all_tests_answers.json", "r", encoding="utf-8") as f:
    ALL_ANS = json.load(f)

TEST_PAGES = {
    1: (1, 31), 2: (31, 60), 3: (60, 90), 4: (90, 119), 5: (119, 148),
    6: (148, 178), 7: (178, 208), 8: (208, 238), 9: (238, 267), 10: (267, 296)
}

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")

def check_p1_mapping(test_id):
    p1, _ = TEST_PAGES[test_id]
    text = "\n".join([doc[p].get_text() for p in range(p1, p1 + 4)])
    
    # Let's search for question numbers 1, 2, 3, 4, 5, 6 specifically
    # In script nghe, the question number appears right before the speaker label or options!
    # For example: "\n 1 \n M-Cn \n (A) ... \n (B) ... \n (C) ... \n (D) ..."
    # Or in Korean answer section: "1 (A)", "2 (B)", "3 (C)", "4 (D)", "5 (C)", "6 (D)"
    print(f"\n--- TEST {test_id} OFFICIAL P1 ANSWERS: {[ALL_ANS[f'test{test_id}'][str(i)] for i in range(1, 7)]} ---")
    
    # Let's inspect where 1, 2, 3, 4, 5, 6 appear in text
    for q in range(1, 7):
        # Look for "{q}\n" or "{q} [MW]-"
        m = re.search(rf"(?:^|\n)\s*{q}\s*\n(?:[MW]-[A-Za-z]+\s*\n)?\s*(\([A]\)[\s\S]*?\([D]\)\s*[^\n\r]+)", text)
        if m:
            print(f"  Q{q} found with regex direct match!")
        else:
            # Look for index of "\n{q}\n"
            idx = text.find(f"\n{q}\n")
            if idx != -1:
                sub = text[idx:idx+250].replace('\n', ' ')
                print(f"  Q{q} snippet: {sub[:80]}")

for t in [2, 3, 4, 5]:
    check_p1_mapping(t)
