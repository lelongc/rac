import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

for name in ['giai/ĐÁP ÁN ETS 2024 LC.pdf', 'giai/ĐÁP ÁN ETS 2024 RC.pdf']:
    doc = fitz.open(name)
    print(f"\n==================== {name} ====================")
    for pno in range(len(doc)):
        text = doc[pno].get_text()
        first_line = text.splitlines()[0] if text.splitlines() else "EMPTY"
        tests_found = [l for l in text.splitlines() if 'TEST' in l]
        print(f"Page {pno+1}: tests found: {tests_found[:10]}")
