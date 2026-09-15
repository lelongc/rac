import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')
p61_text = doc[60].get_text("text").splitlines()

print("Page 61 lines 0 to 142:")
for i in range(0, min(142, len(p61_text))):
    print(f"{i}: {p61_text[i]}")
