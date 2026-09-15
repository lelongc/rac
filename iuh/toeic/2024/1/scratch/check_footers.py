import fitz, sys
from PIL import Image

doc = fitz.open('ETS 2024 - LISTENING.pdf')

for pno in [40, 41, 42, 43, 44, 53, 54, 55, 56, 57]:
    # Crop the bottom right area where page numbers are: x from 450 to 595, y from 700 to 792
    p = doc[pno]
    pix = p.get_pixmap(dpi=150, clip=fitz.Rect(350, 720, 595, 792))
    pix.save(f'scratch/footer_p{pno}.png')
    print(f"Page {pno} footer saved")
