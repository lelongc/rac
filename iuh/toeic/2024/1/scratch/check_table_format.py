import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc_lc = fitz.open('giai/ĐÁP ÁN ETS 2024 LC.pdf')
print(f"LC pages: {len(doc_lc)}")
for i, page in enumerate(doc_lc):
    text = page.get_text("text")
    print(f"=== LC Page {i+1} ===")
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    for l in lines[:35]:
        print("  ", l)

doc_rc = fitz.open('giai/ĐÁP ÁN ETS 2024 RC.pdf')
print(f"RC pages: {len(doc_rc)}")
for i, page in enumerate(doc_rc):
    text = page.get_text("text")
    print(f"=== RC Page {i+1} ===")
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    for l in lines[:35]:
        print("  ", l)
