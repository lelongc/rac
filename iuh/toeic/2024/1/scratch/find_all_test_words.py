import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

for name in ['giai/ĐÁP ÁN ETS 2024 LC.pdf', 'giai/ĐÁP ÁN ETS 2024 RC.pdf']:
    doc = fitz.open(name)
    print(f"\n=== {name} ===")
    for pno in range(len(doc)):
        words = doc[pno].get_text("words")
        for i, w in enumerate(words):
            if 'TEST' in w[4].upper():
                nxt = words[i+1][4] if i+1 < len(words) else ""
                print(f"  Page {pno+1} at x={w[0]:.1f}, y={w[1]:.1f}: '{w[4]}' '{nxt}'")
