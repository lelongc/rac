import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')

for pno in [60, 61]:
    page = doc[pno]
    # Page text with rotation applied
    text = page.get_text("text")
    print(f"==================== PAGE {pno+1} (Normalized) ====================")
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    for idx, line in enumerate(lines):
        if any(w in line for w in ['PART 1', 'PART 2', '01', '02', '03', '04', '05', '06', 'M-Au', 'W-Br', 'M-Cn', 'W-Am', 'painting', 'cleaning', 'removing', 'ladder', 'tools', 'railing']):
            print(f"Line {idx}: {line}")
