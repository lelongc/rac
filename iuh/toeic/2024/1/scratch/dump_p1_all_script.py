import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('giai/script nghe_0001.pdf')
p61_text = doc[60].get_text("text").splitlines()
p62_text = doc[61].get_text("text").splitlines()

all_lines = p61_text + p62_text

# Find where PART 1 appears
for idx, line in enumerate(all_lines):
    if 'PART 1' in line or '1 M-Au' in line:
        start_idx = idx
        break

print(f"Printing lines from index {start_idx} onwards:")
for i in range(start_idx, min(start_idx + 180, len(all_lines))):
    print(f"{i}: {all_lines[i]}")
