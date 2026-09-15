# phase1_setup.py: Organize Audio for Tests 1-10 and Extract Official Answer Keys
import os
import shutil
import json
import re
import fitz

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_SRC = os.path.join(BASE_DIR, "AUDIO CẮT TỪNG PART")
AUDIO_DEST = os.path.join(BASE_DIR, "web", "assets", "audio")

# 1. Organize Audio
print("--- [1/2] Organizing Audio Files for Tests 1-10 ---")
os.makedirs(AUDIO_DEST, exist_ok=True)

# Copy Test 1 if not already in test1
t1_dir = os.path.join(AUDIO_DEST, "test1")
os.makedirs(t1_dir, exist_ok=True)
for p in range(1, 5):
    src_t1 = os.path.join(AUDIO_SRC, f"PART {p}", f"PART {p} - TEST 1.mp3")
    dst_t1 = os.path.join(t1_dir, f"part{p}.mp3")
    if not os.path.exists(dst_t1) and os.path.exists(src_t1):
        shutil.copy2(src_t1, dst_t1)
        print(f"Copied Test 1 Part {p} audio")

# Tests 2 to 5
for t in range(2, 6):
    t_dir = os.path.join(AUDIO_DEST, f"test{t}")
    os.makedirs(t_dir, exist_ok=True)
    for p in range(1, 5):
        src = os.path.join(AUDIO_SRC, f"PART {p}", f"PART {p} - TEST {t}.mp3")
        dst = os.path.join(t_dir, f"part{p}.mp3")
        if not os.path.exists(dst):
            if os.path.exists(src):
                shutil.copy2(src, dst)
                print(f"Copied Test {t} Part {p} audio")
            else:
                print(f"WARNING: Source audio not found: {src}")

# Tests 6 to 10
for t in range(6, 11):
    t_str = f"{t:02d}"
    t_dir = os.path.join(AUDIO_DEST, f"test{t}")
    os.makedirs(t_dir, exist_ok=True)
    for p in range(1, 5):
        src = os.path.join(AUDIO_SRC, f"Test_{t_str}", f"Test_{t_str}-Part{p}.mp3")
        dst = os.path.join(t_dir, f"part{p}.mp3")
        if not os.path.exists(dst):
            if os.path.exists(src):
                shutil.copy2(src, dst)
                print(f"Copied Test {t} Part {p} audio")
            else:
                print(f"WARNING: Source audio not found: {src}")

print("Audio organization complete!\n")

# 2. Extract Official Answer Keys
print("--- [2/2] Extracting Official Answer Keys for All 10 Tests ---")

def extract_answers_from_pdf(pdf_path, is_rc=False):
    doc = fitz.open(pdf_path)
    page_test_map = {
        1: [1, 2, 3, 4],
        2: [5, 6, 7, 8],
        3: [9, 10]
    }
    
    test_answers = {t: {} for t in range(1, 11)}
    
    for p_idx, test_nums in page_test_map.items():
        page = doc[p_idx]
        blocks = [b for b in page.get_text("blocks") if b[6] == 0]
        num_cols = len(test_nums)
        # Cluster blocks by x0 coordinate into columns
        # First sort by x0
        sorted_by_x = sorted(blocks, key=lambda b: b[0])
        # Find distinct column clusters
        cols = []
        for b in sorted_by_x:
            matched = False
            for c in cols:
                # If within 40 pixels of existing column cluster average
                avg_x = sum(item[0] for item in c) / len(c)
                if abs(avg_x - b[0]) < 35:
                    c.append(b)
                    matched = True
                    break
            if not matched:
                cols.append([b])
        
        # Sort columns left to right
        cols = sorted(cols, key=lambda c: sum(item[0] for item in c) / len(c))
        
        if len(cols) != num_cols:
            print(f"Warning: Expected {num_cols} columns on page {p_idx+1}, got {len(cols)}")
            # Fallback: slice blocks sequentially
            chunk_size = len(blocks) // num_cols
            cols = [blocks[i*chunk_size : (i+1)*chunk_size] for i in range(num_cols)]
            
        for t_idx, t_num in enumerate(test_nums):
            col_blocks = sorted(cols[t_idx], key=lambda b: b[1]) # top to bottom
            text = "\n".join(b[4] for b in col_blocks)
            pairs = re.findall(r"(\d+)\s*\(([ABCD])\)", text)
            for q, a in pairs:
                test_answers[t_num][int(q)] = a
                
    return test_answers

lc_answers = extract_answers_from_pdf(os.path.join(BASE_DIR, "giai", "ĐÁP ÁN ETS 2024 LC.pdf"))
rc_answers = extract_answers_from_pdf(os.path.join(BASE_DIR, "giai", "ĐÁP ÁN ETS 2024 RC.pdf"), is_rc=True)

all_keys = {}
for t in range(1, 11):
    t_dict = {}
    lc_t = lc_answers.get(t, {})
    rc_t = rc_answers.get(t, {})
    
    for q in range(1, 101):
        t_dict[str(q)] = lc_t.get(q, "")
    for q in range(101, 201):
        t_dict[str(q)] = rc_t.get(q, "")
        
    all_keys[f"test{t}"] = t_dict
    
    # Validation
    missing_lc = [q for q in range(1, 101) if not t_dict[str(q)]]
    missing_rc = [q for q in range(101, 201) if not t_dict[str(q)]]
    print(f"Test {t}: LC answers={len(lc_t)} (missing: {len(missing_lc)}), RC answers={len(rc_t)} (missing: {len(missing_rc)})")

with open(os.path.join(BASE_DIR, "all_tests_answers.json"), "w", encoding="utf-8") as f:
    json.dump(all_keys, f, ensure_ascii=False, indent=2)

print("Saved all_tests_answers.json successfully!")
