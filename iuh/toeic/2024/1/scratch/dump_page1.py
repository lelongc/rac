import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

reader_lc = pypdf.PdfReader(r"d:\folder\rac\iuh\toeic\2024\1\giai\ĐÁP ÁN ETS 2024 LC.pdf")
print("=== LC PAGE 1 FULL TEXT ===")
print(reader_lc.pages[0].extract_text()[:3000])

reader_rc = pypdf.PdfReader(r"d:\folder\rac\iuh\toeic\2024\1\giai\ĐÁP ÁN ETS 2024 RC.pdf")
print("=== RC PAGE 1 FULL TEXT ===")
print(reader_rc.pages[0].extract_text()[:3000])
