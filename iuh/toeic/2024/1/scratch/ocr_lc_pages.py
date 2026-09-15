import fitz, subprocess, os, json, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('ETS 2024 - LISTENING.pdf')

def ocr_page(pno, name):
    pix = doc[pno].get_pixmap(dpi=150)
    img_path = f'scratch/{name}_p{pno+1}.png'
    pix.save(img_path)
    cmd = ['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', r'd:\folder\rac\ocr.ps1', '-ImagePath', img_path]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    return res.stdout

# Test 4: Part 3 & 4 (p47 to p53, 0-indexed 46 to 52)
t4_ocr = {}
for p in range(46, 53):
    print(f'OCRing T4 LC page {p+1}...')
    t4_ocr[str(p+1)] = ocr_page(p, 't4_lc')

with open('scratch/t4_lc_ocr.json', 'w', encoding='utf-8') as f:
    json.dump(t4_ocr, f, ensure_ascii=False, indent=2)

# Test 5: Part 3 & 4 (p59 to p66, 0-indexed 58 to 65)
t5_ocr = {}
for p in range(58, 66):
    print(f'OCRing T5 LC page {p+1}...')
    t5_ocr[str(p+1)] = ocr_page(p, 't5_lc')

with open('scratch/t5_lc_ocr.json', 'w', encoding='utf-8') as f:
    json.dump(t5_ocr, f, ensure_ascii=False, indent=2)

print('Done OCRing LC pages for Test 4 and Test 5!')
