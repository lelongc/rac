import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

for p in [5, 8, 9, 10]:
    img = f"web/assets/images/test2/rc_page_{p}.png"
    res = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', 'scratch/ocr_boxes.ps1', img], capture_output=True, text=True)
    lines = res.stdout.splitlines()
    print(f"=== rc_page_{p}.png (total words: {len(lines)}) ===")
    words = [l.split('[')[0] for l in lines[:30]]
    print(" ".join(words[:20]))
