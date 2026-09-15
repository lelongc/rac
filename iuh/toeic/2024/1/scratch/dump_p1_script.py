import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')
for pno in [60, 61]:
    print(f"================== SCRIPT PAGE {pno+1} ==================")
    text = doc[pno].get_text()
    lines = text.splitlines()
    for idx, l in enumerate(lines):
        print(f"{idx}: {l}")
