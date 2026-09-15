import os
import hashlib
import subprocess

p1 = r"d:\folder\rac\iuh\toeic\2024\1\web\assets\images\rc_page_5.png"
p2 = r"d:\folder\rac\iuh\toeic\2024\1\web\assets\images\test2\rc_page_5.png"

def get_h(p):
    with open(p, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

print("rc_page_5.png in root:", get_h(p1))
print("rc_page_5.png in test2:", get_h(p2))

# Let's OCR test2 rc_page_5.png to see what it is
cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", p2]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print("=== OCR of test2 rc_page_5.png ===")
print(res.stdout[:500])
