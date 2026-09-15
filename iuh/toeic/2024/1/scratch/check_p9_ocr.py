import subprocess

cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", r"d:\folder\rac\iuh\toeic\2024\1\scratch\t2_lc_p9.png"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print("=== PAGE 9 OCR ===")
print(res.stdout[:1500])
