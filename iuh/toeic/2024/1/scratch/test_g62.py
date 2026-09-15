from PIL import Image
import subprocess

im9 = Image.open(r"d:\folder\rac\iuh\toeic\2024\1\scratch\t2_lc_p9.png")
g62 = im9.crop((600, 140, 1100, 360))
g62.save(r"d:\folder\rac\iuh\toeic\2024\1\web\assets\images\test2\graphic_q62_64.png")

cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\ocr.ps1", "-ImagePath", r"d:\folder\rac\iuh\toeic\2024\1\web\assets\images\test2\graphic_q62_64.png"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print("=== NEW graphic_q62_64 OCR ===")
print(res.stdout)
