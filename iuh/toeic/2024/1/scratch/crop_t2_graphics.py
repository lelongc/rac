import fitz
from PIL import Image
import os

BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
doc_lc = fitz.open(os.path.join(BASE_DIR, "ETS 2024 - LISTENING.pdf"))

# For Test 2:
# Page 9 (index 21) has Q62-64 graphic: "Area 1 Electric scooters..."
# Page 10 (index 22) has Q65-67 graphic: "Tree Eastern redbud..." and Q68-70 graphic: "Ways to Save at SHELBY's..."
# Page 13 (index 25) has Q95-97 graphic: "City New York, Philadelphia..." and Q98-100 graphic: "Terminal B..."

dest_dir = os.path.join(BASE_DIR, "web", "assets", "images", "test2")

# Page 9: Q62-64
pix9 = doc_lc[21].get_pixmap(dpi=150)
im9 = Image.frombytes("RGB", [pix9.width, pix9.height], pix9.samples)
# In im9 (1205x1661), let's crop the table box for Q62-64 (Area 1, 2, 3, 4)
# It is located around x: 100-1100, y: 880-1150
g62 = im9.crop((120, 890, 1080, 1130))
g62.save(os.path.join(dest_dir, "graphic_q62_64.png"))

# Page 10: Q65-67 and Q68-70
pix10 = doc_lc[22].get_pixmap(dpi=150)
im10 = Image.frombytes("RGB", [pix10.width, pix10.height], pix10.samples)
# Q65-67 table: "Tree Eastern redbud..." around top-left
g65 = im10.crop((120, 120, 600, 480))
g65.save(os.path.join(dest_dir, "graphic_q65_67.png"))

# Q68-70 table: "Ways to Save at SHELBY's" around top-right
g68 = im10.crop((600, 120, 1080, 480))
g68.save(os.path.join(dest_dir, "graphic_q68_70.png"))

# Page 13: Q95-97 and Q98-100
pix13 = doc_lc[25].get_pixmap(dpi=150)
im13 = Image.frombytes("RGB", [pix13.width, pix13.height], pix13.samples)
# Q95-97 table: City New York...
g95 = im13.crop((120, 120, 600, 480))
g95.save(os.path.join(dest_dir, "graphic_q95_97.png"))

# Q98-100 table: Terminal B...
g98 = im13.crop((600, 120, 1080, 480))
g98.save(os.path.join(dest_dir, "graphic_q98_100.png"))

print("Test 2 graphics cropped successfully!")
print("g62 size:", g62.size)
print("g65 size:", g65.size)
print("g68 size:", g68.size)
print("g95 size:", g95.size)
print("g98 size:", g98.size)
