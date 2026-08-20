import fitz
import os

def extract_raw_images(pdf_path, out_dir, prefix):
    os.makedirs(out_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    img_count = 0
    for i, page in enumerate(doc):
        for img_info in page.get_images():
            xref = img_info[0]
            base_img = doc.extract_image(xref)
            img_bytes = base_img["image"]
            img_ext = base_img["ext"]
            img_name = f"{prefix}_p{i+1}_img{img_count}.{img_ext}"
            img_path = os.path.join(out_dir, img_name)
            with open(img_path, "wb") as f:
                f.write(img_bytes)
            print(f"Saved {img_path} ({len(img_bytes)} bytes)")
            img_count += 1

extract_raw_images(r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\MÁY HỮU HẠN KHÔNG ĐƠN ĐỊNH SV nfa.pdf", r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\raw_images", "theory")
extract_raw_images(r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\Thiết kế NFA SV.pdf", r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\raw_images", "design")
