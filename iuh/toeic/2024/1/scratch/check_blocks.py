import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    for pno in range(len(doc)):
        page = doc[pno]
        print(f"--- Page {pno+1} ({page.rect}) ---")
        blocks = page.get_text("blocks")
        for b in blocks[:15]:
            # x0, y0, x1, y1, text, block_no, block_type
            text = b[4].replace('\n', ' ')
            print(f"  ({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}): {text[:60]}")

print("=== LC BLOCKS ===")
inspect_blocks('giai/ĐÁP ÁN ETS 2024 LC.pdf')
