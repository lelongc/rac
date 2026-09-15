import pypdf
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def extract_answers_from_pdf(pdf_path, test_num=2):
    reader = pypdf.PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    return full_text

lc_text = extract_answers_from_pdf('giai/ĐÁP ÁN ETS 2024 LC.pdf', 2)
rc_text = extract_answers_from_pdf('giai/ĐÁP ÁN ETS 2024 RC.pdf', 2)

print("LC text length:", len(lc_text))
print("RC text length:", len(rc_text))

# Let's search for TEST 02 or TEST 2 in both
print("\n--- LC sample matches ---")
for m in re.finditer(r'(TEST\s*0?2|Test\s*0?2)', lc_text):
    start = max(0, m.start() - 50)
    end = min(len(lc_text), m.end() + 300)
    print(lc_text[start:end])
    print("="*40)
    break

print("\n--- RC sample matches ---")
for m in re.finditer(r'(TEST\s*0?2|Test\s*0?2)', rc_text):
    start = max(0, m.start() - 50)
    end = min(len(rc_text), m.end() + 300)
    print(rc_text[start:end])
    print("="*40)
    break
