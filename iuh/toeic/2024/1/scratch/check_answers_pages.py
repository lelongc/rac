import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

for name in ['giai/ĐÁP ÁN ETS 2024 LC.pdf', 'giai/ĐÁP ÁN ETS 2024 RC.pdf']:
    doc = fitz.open(name)
    print(f"\n==================== {name} ====================")
    for pno in [1, 2, 3]:
        page = doc[pno]
        words = page.get_text("words")
        # find x coordinates of header row or unique columns
        print(f"Page {pno+1}: {len(words)} words, rect={page.rect}")
        # group words by line (similar y)
        lines_by_y = {}
        for w in words:
            y = round(w[1] / 5) * 5
            if y not in lines_by_y:
                lines_by_y[y] = []
            lines_by_y[y].append(w)
        # print first 5 lines
        sorted_y = sorted(lines_by_y.keys())
        for y in sorted_y[:5]:
            line_str = " | ".join([f"({w[0]:.0f}){w[4]}" for w in sorted(lines_by_y[y], key=lambda x: x[0])])
            print(f"  y~{y}: {line_str}")
