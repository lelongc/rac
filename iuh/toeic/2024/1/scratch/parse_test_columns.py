import fitz, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

# In fitz, extract words with coordinates (x0, y0, x1, y1, word, block_no, line_no, word_no)
# Each test is a column!

def parse_answer_pdf(pdf_path, is_rc=False):
    doc = fitz.open(pdf_path)
    # Collect all words across all pages
    all_words = []
    for pno in range(len(doc)):
        words = doc[pno].get_text("words")
        for w in words:
            # (x0, y0, x1, y1, text, block, line, word)
            all_words.append((pno, w[0], w[1], w[2], w[3], w[4]))
            
    # Print header or test names
    test_headers = [w for w in all_words if 'TEST' in w[5].upper()]
    print(f"{pdf_path}: found {len(test_headers)} test headers")
    for th in test_headers[:10]:
        print(f"  Page {th[0]+1} at x={th[1]:.1f}, y={th[2]:.1f}: {th[5]}")

parse_answer_pdf('giai/ĐÁP ÁN ETS 2024 LC.pdf')
parse_answer_pdf('giai/ĐÁP ÁN ETS 2024 RC.pdf', is_rc=True)
