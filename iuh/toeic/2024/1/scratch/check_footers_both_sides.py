import fitz, sys
from PIL import Image

doc = fitz.open('ETS 2024 - LISTENING.pdf')

for pno in range(40, 60):
    p = doc[pno]
    # Check text or check bottom left and bottom right
    pix_left = p.get_pixmap(dpi=100, clip=fitz.Rect(20, 720, 250, 792))
    pix_right = p.get_pixmap(dpi=100, clip=fitz.Rect(350, 720, 595, 792))
    pix_left.save(f'scratch/foot_L_{pno}.png')
    pix_right.save(f'scratch/foot_R_{pno}.png')

print("Saved left and right footers for pages 40-59")
