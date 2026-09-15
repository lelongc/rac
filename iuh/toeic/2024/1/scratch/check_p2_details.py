import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

reader = pypdf.PdfReader(r"d:\folder\rac\iuh\toeic\2024\1\giai\ĐÁP ÁN ETS 2024 LC.pdf")
page2 = reader.pages[1]

def visitor_body(text, cm, tm, font_dict, font_size):
    if text.strip():
        # tm[4] is x, tm[5] is y
        # print first few
        pass

# Let's inspect line by line
text = page2.extract_text()
print("Page 2 length:", len(text))
lines = [l.strip() for l in text.split('\n') if l.strip()]
print("Total lines:", len(lines))
for i, l in enumerate(lines):
    if "TEST" in l or "강의기출" in l:
        print(f"Line {i}: {l}")
        # print context
        for j in range(max(0, i-3), min(len(lines), i+5)):
            print(f"   [{j}] {lines[j]}")
