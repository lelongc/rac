import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz

folder = os.path.join('d:', os.sep, 'folder', 'rac', 'iuh', 'môn', 'hk2-3', 'ptht-tichhop', 'co-gui')
files = ['LAB_03_Threads.pdf', 'LAB 06_ontap.pdf', 'LAB 07_RMI.pdf', 'LAB 08_JDBC.pdf']

for fname in files:
    fpath = os.path.join(folder, fname)
    print(f'\n{"="*60}')
    print(f'  {fname}')
    print(f'{"="*60}')
    doc = fitz.open(fpath)
    for page in doc:
        text = page.get_text()
        print(text)
    doc.close()
