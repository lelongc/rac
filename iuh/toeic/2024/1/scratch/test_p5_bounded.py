import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open("scratch/ocr_rc_test2.json", encoding='utf-8'))
p5_txt = d.get('2', '') + "\n" + d.get('3', '') + "\n" + d.get('4', '')

# Replace special dashes with -------
p5_txt = p5_txt.replace("—", " ------- ").replace("–", " ------- ")
# Ensure spaces around (A), (B), (C), (D)
p5_txt = re.sub(r"\(?([ABCD])\)", r" (\1) ", p5_txt)

print("Testing chunking by question number:")
parsed = {}
for q in range(101, 131):
    next_q = q + 1
    # Match from q to next_q (or to PART 6 if q==130)
    patt = rf"\b{q}\b[\.\s]+([\s\S]*?)(?=\b{next_q}\b[\.\s]+|PART\s*6|\Z)"
    m = re.search(patt, p5_txt)
    if m:
        chunk = m.group(1).strip()
        # Extract stem and options
        # Stem is before (A)
        m_opts = re.search(r"\(A\)\s*([^\(]+?)\s*\(B\)\s*([^\(]+?)\s*\(C\)\s*([^\(]+?)\s*\(D\)\s*([^\(\n\r]+)", chunk)
        if m_opts:
            stem = chunk[:chunk.find("(A)")].strip()
            a = m_opts.group(1).strip()
            b = m_opts.group(2).strip()
            c = m_opts.group(3).strip()
            d = m_opts.group(4).strip()
            # Clean stem
            stem = re.sub(r"\s+", " ", stem)
            if "-------" not in stem:
                stem += " ------- ."
            parsed[q] = {
                "stem": stem,
                "A": a, "B": b, "C": c, "D": d
            }
        else:
            parsed[q] = {"raw": chunk[:100]}

print(f"Parsed {len(parsed)}/30 questions.")
for q in [101, 102, 103, 104, 105, 110, 120, 130]:
    print(f"Q{q}: {parsed.get(q)}")
