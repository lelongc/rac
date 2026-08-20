import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_pdf_text_with_rects(pdf_path):
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        print(f"\n=== PAGE {page_num+1} ===")
        blocks = page.get_text("blocks")
        for b in blocks:
            # b: (x0, y0, x1, y1, text, block_no, block_type)
            text_preview = b[4].strip().replace('\n', ' ')
            print(f"Block [{b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}] Type {b[6]}: {text_preview}")
        img_list = page.get_images()
        print(f"Images on page: {len(img_list)}")

print("--- THEORY PDF ---")
inspect_pdf_text_with_rects(r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\MÁY HỮU HẠN KHÔNG ĐƠN ĐỊNH SV nfa.pdf")
print("\n\n--- DESIGN PDF ---")
inspect_pdf_text_with_rects(r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\Thiết kế NFA SV.pdf")
