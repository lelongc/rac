import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/ĐÁP ÁN ETS 2024 RC.pdf')
page = doc[1] # Page 2
blocks = page.get_text("blocks")
print(f"Total blocks on RC Page 2: {len(blocks)}")
for b in blocks:
    if b[1] < 120 or 'TEST' in b[4]:
        print(f"({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}): {repr(b[4][:50])}")
