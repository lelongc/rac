import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')
p61 = doc[60]
print(f"Page 61 rect: {p61.rect}")

# Sort blocks by y0 (top to bottom), then x0 (left to right)
blocks = p61.get_text("blocks")
# Filter out the answer key table at the top if needed
for b in sorted(blocks, key=lambda x: (x[1], x[0])):
    txt = b[4].strip().replace('\n', ' ')
    if any(k in txt for k in ['PART 1', 'M-Au', 'W-Br', 'M-Cn', 'W-Am', 'painting a room', 'cleaning an oven', 'removing his hat', 'leaned against a tree', 'tools have been', 'railing is being', 'TEST 3']):
        print(f"y0={b[1]:.1f}, x0={b[0]:.1f} | {txt[:120]}")
