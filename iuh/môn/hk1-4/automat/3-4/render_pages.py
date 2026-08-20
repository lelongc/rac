import fitz # PyMuPDF
import os

def render_pdf_pages(pdf_path, output_dir, prefix):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        out_path = os.path.join(output_dir, f"{prefix}_page_{i+1}.png")
        pix.save(out_path)
        print(f"Saved {out_path}")

render_pdf_pages(r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\MÁY HỮU HẠN KHÔNG ĐƠN ĐỊNH SV nfa.pdf", r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\images", "theory")
render_pdf_pages(r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\Thiết kế NFA SV.pdf", r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\images", "design")
