import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")
# Pages 24 to 29 contain Test 1 Part 4
full_text = ""
for p in range(23, 29):
    full_text += f"\n--- PAGE {p+1} ---\n" + doc[p].get_text()

# Find questions and their options/answers
for qid in [83, 85, 89, 92, 94, 95, 99, 100]:
    print(f"\n=================== QUESTION {qid} IN SCRIPT NGHE ===================")
    pattern = rf"(?:^|\n)({qid}\s*\n[\s\S]*?(?=\n\d{{1,3}}\s*\n|\n\d{{2,3}}-\d{{2,3}}|\Z))"
    m = re.search(pattern, full_text)
    if m:
        print(m.group(1)[:500])
    else:
        # search simpler
        lines = full_text.splitlines()
        for idx, line in enumerate(lines):
            if re.match(rf"^{qid}\s*$", line.strip()):
                print("\n".join(lines[max(0, idx-2):min(len(lines), idx+15)]))
                break
