import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test2.json', encoding='utf-8') as f:
    ocr2 = json.load(f)

def clean_passage(text, end_pattern=r'\b(1[4-9][0-9]|200)\.'):
    # Find where the questions start
    m = re.search(end_pattern, text)
    if m:
        return text[:m.start()].strip()
    return text.strip()

passages = {}

# 147-148 (Page 9)
p9 = ocr2['9']
# find start "Questions 147-148"
p147 = p9[p9.find('Questions 147-148'):]
passages[(147, 148)] = clean_passage(p147)

# 149-150 (Page 10)
p10 = ocr2['10']
passages[(149, 150)] = clean_passage(p10[p10.find('Questions 149-150'):])

# 151-152 (Page 11)
p11 = ocr2['11']
passages[(151, 152)] = clean_passage(p11[p11.find('Questions 151-152'):])

# 153-154 (Page 12)
p12 = ocr2['12']
passages[(153, 154)] = clean_passage(p12[p12.find('Questions 153-154'):])

# 155-157 (Page 13)
p13 = ocr2['13']
passages[(155, 157)] = clean_passage(p13[p13.find('Questions 155-157'):])

# 158-160 (Page 14)
p14 = ocr2['14']
passages[(158, 160)] = clean_passage(p14[p14.find('Questions 158-160'):])

# 161-163 (Page 15)
p15 = ocr2['15']
passages[(161, 163)] = clean_passage(p15[p15.find('Questions 161-163'):])

# 164-167 (Page 16)
p16 = ocr2['16']
passages[(164, 167)] = clean_passage(p16[p16.find('Questions 164-167'):])

# 168-171 (Page 17)
p17 = ocr2['17']
passages[(168, 171)] = clean_passage(p17[p17.find('Questions 168-171'):])

# 172-175 (Page 18)
p18 = ocr2['18']
passages[(172, 175)] = clean_passage(p18[p18.find('Questions 172-175'):])

# 176-180 (Page 20)
p20 = ocr2['20']
passages[(176, 180)] = clean_passage(p20[p20.find('Questions 176-180'):])

# 181-185 (Page 22)
p22 = ocr2['22']
passages[(181, 185)] = clean_passage(p22[p22.find('Questions 181-185'):])

# 186-190 (Page 24 & 25)
p24 = ocr2['24']
p25 = ocr2['25']
pass_24 = clean_passage(p24[p24.find('Questions 186-190'):])
pass_25 = clean_passage(p25)
passages[(186, 190)] = pass_24 + "\n\n" + pass_25

# 191-195 (Page 26 & 27)
p26 = ocr2['26']
p27 = ocr2['27']
pass_26 = clean_passage(p26[p26.find('Questions 191-195'):])
pass_27 = clean_passage(p27)
passages[(191, 195)] = pass_26 + "\n\n" + pass_27

# 196-200 (Page 28 & 29)
p28 = ocr2['28']
p29 = ocr2.get('29', '')
pass_28 = clean_passage(p28[p28.find('Questions 196-200'):])
pass_29 = clean_passage(p29)
passages[(196, 200)] = pass_28 + ("\n\n" + pass_29 if pass_29 else "")

for (s, e), p in passages.items():
    print(f"[{s}-{e}] Length: {len(p)} | Start: {p[:60].replace(chr(10), ' ')}... | End: ...{p[-50:].replace(chr(10), ' ')}")
