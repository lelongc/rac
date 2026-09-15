import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('ETS 2024 - LISTENING.pdf')

# Let's inspect pages 25 to 32
for pno in range(25, 33):
    page = doc[pno]
    imgs = page.get_images()
    print(f"Page {pno} (Book page?): {len(imgs)} images, rect={page.rect}")
