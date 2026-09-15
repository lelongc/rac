import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

import subprocess
txt_l = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", r"d:\folder\rac\iuh\toeic\2024\1\scratch\p_30_left.png"], capture_output=True, text=True, encoding="utf-8").stdout

# Remove directions header
if "on your answer sheet." in txt_l:
    txt_l = txt_l.split("on your answer sheet.", 1)[1]

# Remove leading numbers
txt_l = re.sub(r"^\s*[\d\.\s]+", "", txt_l)

# Split by (A)
parts = re.split(r"\(A\)", txt_l)
print(f"Parts count: {len(parts)}")

for i in range(1, len(parts)):
    # The stem was at the end of parts[i-1]
    stem = parts[i-1].strip()
    # If there are previous options in parts[i-1], stem is after (D)
    if "(D)" in stem:
        stem = re.split(r"\(D\)\s*[^\n\r]+", stem)[-1].strip()
        
    stem = re.sub(r"^\s*[\d\.\s]+", "", stem)
    
    # The options (A), (B), (C), (D) are in parts[i]
    opt_text = "(A)" + parts[i]
    m_opts = re.search(r"\(A\)\s*([^\(]+?)\s*\(B\)\s*([^\(]+?)\s*\(C\)\s*([^\(]+?)\s*\(D\)\s*([^\n\r\(]+)", opt_text)
    if m_opts:
        a = m_opts.group(1).strip()
        b = m_opts.group(2).strip()
        c = m_opts.group(3).strip()
        d = m_opts.group(4).strip()
        print(f"\nQuestion {i}:")
        print(f"  Stem: {stem}")
        print(f"  Opts: (A) {a} | (B) {b} | (C) {c} | (D) {d}")
