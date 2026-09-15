import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')
page61 = doc[60] # 0-indexed: 60 is page 61
page62 = doc[61] # 0-indexed: 61 is page 62

print("=== Page 61 text blocks ===")
for b in page61.get_text("blocks"):
    txt = b[4].strip()
    if any(k in txt for k in ['(A)', 'PART 1', 'M-Au', 'W-Br', 'M-Cn', 'W-Am']):
        print(f"Bbox ({b[0]:.1f},{b[1]:.1f},{b[2]:.1f},{b[3]:.1f}):\n{txt[:150]}\n---")

print("\n=== Page 62 text blocks ===")
for b in page62.get_text("blocks"):
    txt = b[4].strip()
    if any(k in txt for k in ['(A)', 'PART 1', 'PART 2', 'M-Au', 'W-Br', 'M-Cn', 'W-Am']):
        print(f"Bbox ({b[0]:.1f},{b[1]:.1f},{b[2]:.1f},{b[3]:.1f}):\n{txt[:150]}\n---")
