import fitz
from PIL import Image

doc = fitz.open('ETS 2024 - LISTENING.pdf')

c_top = (115, 140, 1085, 810)
c_bot = (115, 880, 1085, 1550)

# Page 28: Q1 and Q2
p28 = doc[28].get_pixmap(dpi=150)
p28.save('scratch/raw_t3_p28.png')
im28 = Image.open('scratch/raw_t3_p28.png')
q1_img = im28.crop(c_top)
q2_img = im28.crop(c_bot)
q1_img.save('web/assets/images/test3/q1.png')
q2_img.save('web/assets/images/test3/q2.png')

# Page 29: Q3 and Q4
p29 = doc[29].get_pixmap(dpi=150)
p29.save('scratch/raw_t3_p29.png')
im29 = Image.open('scratch/raw_t3_p29.png')
q3_img = im29.crop(c_top)
q4_img = im29.crop(c_bot)
q3_img.save('web/assets/images/test3/q3.png')
q4_img.save('web/assets/images/test3/q4.png')

# Page 30: Q5 and Q6
p30 = doc[30].get_pixmap(dpi=150)
p30.save('scratch/raw_t3_p30.png')
im30 = Image.open('scratch/raw_t3_p30.png')
q5_img = im30.crop(c_top)
q6_img = im30.crop(c_bot)
q5_img.save('web/assets/images/test3/q5.png')
q6_img.save('web/assets/images/test3/q6.png')

print("Cropped real Q1-Q6 for Test 3 successfully!")
