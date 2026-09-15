import fitz, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

def extract_answers_table(pdf_path, is_rc=False):
    doc = fitz.open(pdf_path)
    # The tables usually span pages 2, 3, 4
    full_text = ""
    for p in doc:
        full_text += p.get_text() + "\n"
    
    # We want answers for TEST 01 through TEST 10
    # Let's inspect the layout of text
    lines = [l.strip() for l in full_text.splitlines() if l.strip()]
    return lines

lines_lc = extract_answers_table('giai/ĐÁP ÁN ETS 2024 LC.pdf')
lines_rc = extract_answers_table('giai/ĐÁP ÁN ETS 2024 RC.pdf')

print(f"LC lines: {len(lines_lc)}, sample: {lines_lc[15:35]}")
print(f"RC lines: {len(lines_rc)}, sample: {lines_rc[15:35]}")
