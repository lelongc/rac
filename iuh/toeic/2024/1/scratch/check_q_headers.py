import fitz
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")

def inspect_test_structure(test_id):
    # Find test start page
    start_p = None
    for p in range(len(doc)):
        txt = doc[p].get_text()
        if re.search(rf"\bTEST\s*0?{test_id}\b", txt, re.IGNORECASE) and "ANSWERS" not in txt:
            start_p = p
            break
    print(f"Test {test_id} starts at PDF page {start_p + 1}")
    
    # Collect text of this test (approx 29-30 pages)
    test_text = "\n".join([doc[p].get_text() for p in range(start_p, min(start_p + 30, len(doc)))])
    
    # Let's check how many question markers we can find (from 1 to 100)
    found_qs = {}
    for q in range(1, 101):
        # In script nghe, question header can be:
        # "\n{q}\n" or "\n{q} M-Cn" or "\n{q} W-Am" or "\n{q-1}-{q}" or "\n{q}."
        m = re.search(rf"(?:^|\n)\s*{q}\s*(?:\n|[MW]-[A-Za-z]+|\.)", test_text)
        if m:
            found_qs[q] = m.start()
            
    print(f"  Found {len(found_qs)}/100 question headers directly!")
    missing = [q for q in range(1, 101) if q not in found_qs]
    if missing:
        print(f"  Missing markers: {missing[:15]}...")

for t in range(2, 11):
    inspect_test_structure(t)
