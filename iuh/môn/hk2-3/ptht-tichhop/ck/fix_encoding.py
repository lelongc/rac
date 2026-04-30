import sys

def fix_mojibake(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split to fix only the corrupted part (before line 571)
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        if i < 571:
            try:
                # Revert UTF-8 string back to bytes using cp1252
                b = line.encode('cp1252')
                # Decode bytes using utf-8
                fixed = b.decode('utf-8')
                fixed_lines.append(fixed)
            except Exception as e:
                # If cp1252 fails, try cp1258 (Vietnamese ANSI)
                try:
                    b = line.encode('cp1258')
                    fixed = b.decode('utf-8')
                    fixed_lines.append(fixed)
                except:
                    fixed_lines.append(line)
        else:
            fixed_lines.append(line)
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(fixed_lines))

if __name__ == '__main__':
    fix_mojibake('d:\\folder\\rac\\iuh\\môn\\hk2-3\\ptht-tichhop\\ck\\du.md')
