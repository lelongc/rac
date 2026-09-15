import fitz
from PIL import Image

doc = fitz.open('ETS 2024 - LISTENING.pdf')

# Save full page 28, 29, 30 as high-res PNG so we can inspect them
for pno in [28, 29, 30]:
    page = doc[pno]
    pix = page.get_pixmap(dpi=150)
    pix.save(f'scratch/full_page_{pno}.png')
    print(f"Saved scratch/full_page_{pno}.png: {pix.width}x{pix.height}")
