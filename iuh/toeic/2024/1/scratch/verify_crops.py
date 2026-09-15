import subprocess

for name in ["graphic_q62_64.png", "graphic_q65_67.png", "graphic_q68_70.png", "graphic_q95_97.png", "graphic_q98_100.png"]:
    p = rf"d:\folder\rac\iuh\toeic\2024\1\web\assets\images\test2\{name}"
    cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", p]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(f"=== {name} ===")
    print(res.stdout.strip()[:200])
