import fitz
import sys
from PIL import Image
import os

sys.stdout.reconfigure(encoding='utf-8')

# Render pages 27, 28, 29, 30 at 150 dpi
doc = fitz.open('ETS 2024 - LISTENING.pdf')

for pno in [27, 28, 29, 30]:
    page = doc[pno]
    pix = page.get_pixmap(dpi=150)
    pix.save(f'scratch/t3_lc_p{pno}.png')
    print(f"Saved scratch/t3_lc_p{pno}.png ({pix.width}x{pix.height})")

# Let's inspect the current web/assets/images/test3/q1.png to q6.png sizes
for i in range(1, 7):
    p = f'web/assets/images/test3/q{i}.png'
    sz = os.path.getsize(p) if os.path.exists(p) else 0
    img = Image.open(p) if os.path.exists(p) else None
    dims = f"{img.width}x{img.height}" if img else "None"
    print(f"Current web q{i}: size={sz}, dims={dims}")
