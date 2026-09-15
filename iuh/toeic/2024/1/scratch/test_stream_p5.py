import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("all_tests_answers.json", "r", encoding="utf-8") as f:
    ALL_ANS = json.load(f)

def clean_opt(s):
    # take up to first punctuation or capital word that starts next sentence
    s = s.strip()
    # remove trailing numbers
    s = re.sub(r"\s+\d+\.?$", "", s)
    return s.strip()

def parse_part5_stream(test_id):
    d = json.load(open(f"scratch/ocr_rc_test{test_id}.json", encoding='utf-8'))
    txt = d.get('2', '') + "\n" + d.get('3', '') + "\n" + d.get('4', '')
    
    # Clean text
    txt = txt.replace("—", " ------- ").replace("–", " ------- ")
    # remove directions
    if "PART 5 Directions:" in txt:
        txt = txt.split("on your answer sheet.", 1)[1]
    elif "Directions:" in txt:
        txt = txt.split("sheet.", 1)[1]
        
    # Split text into tokens around (A) ... (B) ... (C) ... (D)
    # Match: sentence ... (A) optA (B) optB (C) optC (D) optD
    pattern = r"\(A\)\s*([^\(]+?)\s*\(B\)\s*([^\(]+?)\s*\(C\)\s*([^\(]+?)\s*\(D\)\s*([^\(\n\r]+)"
    matches = list(re.finditer(pattern, txt))
    
    questions = []
    t_ans = ALL_ANS[f"test{test_id}"]
    
    # Stem of first question is before first (A)
    first_stem = txt[:matches[0].start()].strip() if matches else ""
    first_stem = re.sub(r"^[\d\.\s]+", "", first_stem)
    
    for i, m in enumerate(matches):
        qid = 101 + i
        if qid > 130: break
        
        a = m.group(1).strip()
        b = m.group(2).strip()
        c = m.group(3).strip()
        d_full = m.group(4).strip()
        
        # d_full contains optD + possibly next question stem!
        # In Part 5 options are 1-3 words: e.g. "finish", "secured", "to", "their", "significantly"
        d_words = d_full.split()
        # Option D is usually the first 1 or 2 words (e.g. up to 3 words)
        # Next sentence starts where a word is capitalized and sentence continues
        opt_d = d_words[0] if d_words else ""
        next_stem = ""
        if len(d_words) > 1:
            # Check if 2nd word is lowercase (like "to be", "will do", "in addition")
            if d_words[1][0].islower() and len(d_words) > 2 and d_words[2][0].isupper():
                opt_d = d_words[0] + " " + d_words[1]
                next_stem = " ".join(d_words[2:])
            elif d_words[1][0].isupper():
                opt_d = d_words[0]
                next_stem = " ".join(d_words[1:])
            else:
                # heuristic: find first capitalized word that looks like a sentence start
                for w_idx in range(1, len(d_words)):
                    if d_words[w_idx][0].isupper() and not d_words[w_idx].isupper(): # Title Case
                        opt_d = " ".join(d_words[:w_idx])
                        next_stem = " ".join(d_words[w_idx:])
                        break
                if not next_stem:
                    opt_d = d_words[0]
                    next_stem = " ".join(d_words[1:])
                    
        # Remove trailing question numbers from next_stem
        next_stem = re.sub(r"^\s*[\d\.\s]+", "", next_stem)
        
        current_stem = first_stem if i == 0 else prev_next_stem
        prev_next_stem = next_stem
        
        # Clean current stem
        current_stem = re.sub(r"^\s*[\d\.\s]+", "", current_stem).strip()
        if "-------" not in current_stem:
            current_stem += " ------- ."
            
        ans = t_ans.get(str(qid), "A")
        opts = {
            "A": clean_opt(a),
            "B": clean_opt(b),
            "C": clean_opt(c),
            "D": clean_opt(opt_d)
        }
        
        questions.append({
            "id": qid,
            "stem": current_stem,
            "opts": opts,
            "ans": ans
        })
        
    return questions

t2_p5 = parse_part5_stream(2)
print(f"Test 2 Part 5 parsed: {len(t2_p5)}/30 questions")
for q in t2_p5[:8]:
    print(f"\nQ{q['id']} (Ans: {q['ans']}):")
    print(f"  Stem: {q['stem']}")
    print(f"  Opts: {q['opts']}")
