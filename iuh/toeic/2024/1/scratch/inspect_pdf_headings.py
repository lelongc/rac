import pypdf
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def analyze_pdf(path):
    print("====================================")
    print("ANALYZING:", path)
    reader = pypdf.PdfReader(path)
    for p_idx, page in enumerate(reader.pages):
        text = page.extract_text()
        headings = re.findall(r'(TEST\s*\d+|동영상\s*강의기출\s*TEST\s*\d+|ANSWERS)', text, re.IGNORECASE)
        print(f"Page {p_idx + 1}: Found markers {headings}")
        # Print lines that look like headings
        for line in text.splitlines():
            if any(k in line for k in ["TEST", "ANSWERS", "강의기출"]):
                print(f"   Line: {line}")

analyze_pdf(r"d:\folder\rac\iuh\toeic\2024\1\giai\ĐÁP ÁN ETS 2024 LC.pdf")
analyze_pdf(r"d:\folder\rac\iuh\toeic\2024\1\giai\ĐÁP ÁN ETS 2024 RC.pdf")
