import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

for name in ['giai/ĐÁP ÁN ETS 2024 LC.pdf', 'giai/ĐÁP ÁN ETS 2024 RC.pdf']:
    doc = fitz.open(name)
    print(f"\n=== {name} (Pages: {len(doc)}) ===")
    for i in range(min(3, len(doc))):
        print(f"Page {i+1} text snippet:\n{doc[i].get_text()[:300]}")
