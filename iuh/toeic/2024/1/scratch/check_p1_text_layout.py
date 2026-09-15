import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('ETS 2024 - LISTENING.pdf')

for page_idx in [28, 29, 30]:
    page = doc[page_idx]
    print(f"=== Page {page_idx} ===")
    text_instances = page.get_text("blocks")
    for b in text_instances:
        # b is (x0, y0, x1, y1, text, block_no, block_type)
        txt = b[4].strip().replace('\n', ' ')
        if any(w in txt for w in ['1', '2', '3', '4', '5', '6', 'Part 1', 'NO.', 'No.']):
            print(f"  bbox=({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}) text: {txt}")
