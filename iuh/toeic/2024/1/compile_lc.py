# compile_lc.py: Extracts dialogues, talks, questions and options for Q32 - Q100
import re, json

with open(r'd:\folder\rac\lc_all_ocr_questions.txt', 'r', encoding='utf-8') as f:
    ocr_text = f.read()

with open(r'd:\folder\rac\lc_test1_raw.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()

# 1. Parse questions from OCR text
ocr_questions = {}
pattern = re.compile(r'\b(100|[3-9]\d)[\.\s]+([A-Z][^\?]+\?)\s*\(A\)\s*(.*?)\s*\(B\)\s*(.*?)\s*\(C\)\s*(.*?)\s*\(D\)\s*([^\(]+?)(?=\b(?:100|[3-9]\d)[\.\s]+|\Z)', re.DOTALL)
for m in pattern.finditer(ocr_text):
    q_num = int(m.group(1))
    q_text = m.group(2).strip().replace('\n', ' ')
    a = m.group(3).strip().replace('\n', ' ')
    b = m.group(4).strip().replace('\n', ' ')
    c = m.group(5).strip().replace('\n', ' ')
    d = m.group(6).strip().replace('\n', ' ')
    ocr_questions[q_num] = {
        "text": q_text,
        "options": {"A": a, "B": b, "C": c, "D": d}
    }

print(f"Extracted {len(ocr_questions)} questions from OCR text.")

# 2. Parse from raw_text for any missing questions
raw_q_pattern = re.compile(r'\b(100|[3-9]\d)\s*\n\s*([A-Z][^\n\?]+\?)\s*\n\s*\(A\)\s*([^\n]+)\n\s*\(B\)\s*([^\n]+)\n\s*\(C\)\s*([^\n]+)\n\s*\(D\)\s*([^\n]+)', re.MULTILINE)
for m in raw_q_pattern.finditer(raw_text):
    q_num = int(m.group(1))
    if q_num not in ocr_questions:
        q_text = m.group(2).strip()
        a = m.group(3).strip()
        b = m.group(4).strip()
        c = m.group(5).strip()
        d = m.group(6).strip()
        ocr_questions[q_num] = {
            "text": q_text,
            "options": {"A": a, "B": b, "C": c, "D": d}
        }

print(f"Total questions after merging with raw text: {len(ocr_questions)}")

# Check missing between 32 and 100
missing = [q for q in range(32, 101) if q not in ocr_questions]
print(f"Still missing: {missing}")
