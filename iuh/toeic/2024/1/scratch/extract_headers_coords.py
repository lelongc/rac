import fitz, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect words on Page 2 for Test 4 and Page 3 for Test 5
def extract_test_answers(pdf_path, page_idx, test_header_text, is_rc=False):
    doc = fitz.open(pdf_path)
    page = doc[page_idx]
    
    # We find where `test_header_text` is located
    words = page.get_text("words")
    # find header word
    h_candidates = [w for w in words if test_header_text in w[4]]
    if not h_candidates:
        print(f"Header {test_header_text} not found in {pdf_path} page {page_idx+1}")
        return {}
    
    # In Page 2, there are 4 columns (Test 1, 2, 3, 4) or 2 columns with subcolumns
    # Let's inspect x0 coordinates of headers
    print(f"Headers on page {page_idx+1} for {pdf_path}:")
    for w in words:
        if 'TEST' in w[4]:
            print(f"  x0={w[0]:.1f}, y0={w[1]:.1f}: {w[4]}")
            
extract_test_answers('giai/ĐÁP ÁN ETS 2024 LC.pdf', 1, 'TEST 4')
extract_test_answers('giai/ĐÁP ÁN ETS 2024 LC.pdf', 2, 'TEST 5')
extract_test_answers('giai/ĐÁP ÁN ETS 2024 RC.pdf', 1, 'TEST 4')
extract_test_answers('giai/ĐÁP ÁN ETS 2024 RC.pdf', 2, 'TEST 5')
