import hashlib
from PIL import Image

def get_h(img):
    return hashlib.md5(img.tobytes()).hexdigest()

# Crop coords: (115, 140, 1085, 810) and (115, 880, 1085, 1550)
p27 = Image.open('scratch/t3_lc_p27.png')
p28 = Image.open('scratch/t3_lc_p28.png')
p29 = Image.open('scratch/t3_lc_p29.png')
p30 = Image.open('scratch/t3_lc_p30.png')

c_top = (115, 140, 1085, 810)
c_bot = (115, 880, 1085, 1550)

p27_top = p27.crop(c_top)
p27_bot = p27.crop(c_bot)
p28_top = p28.crop(c_top)
p28_bot = p28.crop(c_bot)
p29_top = p29.crop(c_top)
p29_bot = p29.crop(c_bot)
p30_top = p30.crop(c_top)
p30_bot = p30.crop(c_bot)

q1_web = Image.open('web/assets/images/test3/q1.png')
q2_web = Image.open('web/assets/images/test3/q2.png')
q3_web = Image.open('web/assets/images/test3/q3.png')

print("Hash of p27_top (Directions sample):", get_h(p27_top))
print("Hash of web q1:", get_h(q1_web))
print("Match p27_top == q1_web?", get_h(p27_top) == get_h(q1_web))

print("Hash of p28_top (Real Q1):", get_h(p28_top))
print("Match p28_top == q1_web?", get_h(p28_top) == get_h(q1_web))
print("Match p28_top == q3_web?", get_h(p28_top) == get_h(q3_web))
