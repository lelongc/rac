import os
from PIL import Image

for t in range(1, 11):
    p = f"web/assets/images/test{t}/q1.png" if t > 1 else "web/assets/images/q1.png"
    if os.path.exists(p):
        im = Image.open(p)
        print(f"Test {t:2d} q1.png: size={im.size}, mode={im.mode}")
    else:
        print(f"Test {t:2d} q1.png: MISSING")
