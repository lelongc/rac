import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"d:\folder\rac\iuh\toeic\2024\1\giai\script nghe_0001.pdf")

test_ranges = {
    2: (31, 35),
    3: (60, 64),
    4: (90, 94),
    5: (119, 123)
}

for t, (p_start, p_end) in test_ranges.items():
    print(f"\n=================== TEST {t} PART 1 ===================")
    t_text = "\n".join([doc[p].get_text() for p in range(p_start, p_end)])
    # Find all (A), (B), (C), (D) lines that are English
    # English lines have mostly ASCII characters
    matches = re.findall(r"\(([ABCD])\)\s*([A-Za-z][^\n\r]+)", t_text)
    # Filter English sentences
    clean_opts = []
    for letter, txt in matches:
        txt = txt.strip()
        # Keep lines where text is English sentence
        ascii_ratio = sum(1 for c in txt if c.isascii()) / len(txt) if txt else 0
        if ascii_ratio > 0.85 and len(txt) > 15:
            clean_opts.append((letter, txt))
            
    print(f"Found {len(clean_opts)} clean English option lines:")
    for l, txt in clean_opts[:12]:
        print(f"  ({l}) {txt}")
