import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

reader = pypdf.PdfReader(r"d:\folder\rac\iuh\toeic\2024\1\giai\ĐÁP ÁN ETS 2024 LC.pdf")
for i, page in enumerate(reader.pages):
    print(f"=== PAGE {i+1} ===")
    lines = page.extract_text().splitlines()
    for l in lines[:25]:
        print(l)
