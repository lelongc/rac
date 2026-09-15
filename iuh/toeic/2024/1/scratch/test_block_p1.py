import fitz
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

TEST_PAGES = {
    1: (1, 31), 2: (31, 60), 3: (60, 90), 4: (90, 119), 5: (119, 148),
    6: (148, 178), 7: (178, 208), 8: (208, 238), 9: (238, 267), 10: (267, 296)
}

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")

def get_p1_for_test(test_id):
    p_start, _ = TEST_PAGES[test_id]
    # Check page p_start and p_start+1 (or p_start+1 and p_start+2)
    # Let's find which page has "Part 1"
    target_pages = []
    for p in range(p_start, p_start + 4):
        txt = doc[p].get_text()
        if "(A)" in txt and "(B)" in txt and ("shutters" in txt or "pieces" in txt or "She’s" in txt or "They’re" in txt or "Some" in txt or "worker" in txt or "standing" in txt):
            target_pages.append(p)
            
    # Extract option blocks from these pages
    extracted_blocks = []
    for p in target_pages:
        blocks = doc[p].get_text("blocks")
        # Filter blocks that contain (A) and (B) and have English text
        opt_blocks = []
        for b in blocks:
            txt = b[4].strip()
            if "(A)" in txt and "(B)" in txt:
                lines = [l.strip() for l in txt.split("\n") if l.strip()]
                # Check if it has English options
                opts = {}
                for l in lines:
                    m = re.match(r"^\(([ABCD])\)\s*([A-Za-z][^\n\r]+)", l)
                    if m:
                        opts[m.group(1)] = re.split(r"[\uac00-\ud7a3]", m.group(2))[0].strip()
                if len(opts) >= 3:
                    opt_blocks.append((b[0], b[1], opts))
                    
        # Sort blocks: column 1 first (x < 300) sorted by y, then column 2 (x >= 300) sorted by y
        col1 = sorted([b for b in opt_blocks if b[0] < 300], key=lambda x: x[1])
        col2 = sorted([b for b in opt_blocks if b[0] >= 300], key=lambda x: x[1])
        for _, _, opts in col1 + col2:
            # Check if not already added
            if not any(opts.get('A') == eb.get('A') for eb in extracted_blocks):
                extracted_blocks.append(opts)
                
    return extracted_blocks

for t in range(2, 11):
    blks = get_p1_for_test(t)
    print(f"Test {t:2d}: Extracted {len(blks)} Part 1 blocks")
    for i, b in enumerate(blks[:6]):
        print(f"  Q{i+1}: (A) {b.get('A', '')[:35]} | (B) {b.get('B', '')[:35]}")
