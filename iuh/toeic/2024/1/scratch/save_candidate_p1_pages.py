import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

# Let's check the tab / side header on the right or left of pages 40, 41, 53, 54, 55
doc = fitz.open('ETS 2024 - LISTENING.pdf')

for pno in [40, 41, 42, 43, 53, 54, 55, 56, 57]:
    p = doc[pno]
    # Check side tabs: x in [0, 50] or [540, 595], y in [150, 400]
    pix = p.get_pixmap(dpi=100)
    pix.save(f'scratch/p{pno}_full.png')
    print(f"Saved scratch/p{pno}_full.png")
