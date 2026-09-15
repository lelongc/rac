import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

reader = pypdf.PdfReader(r"d:\folder\rac\iuh\toeic\2024\1\giai\ĐÁP ÁN ETS 2024 LC.pdf")
print("Num pages:", len(reader.pages))
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if "TEST 1" in text or "Test 1" in text:
        print(f"--- Page {i+1} ---")
        print(text[:1000])
