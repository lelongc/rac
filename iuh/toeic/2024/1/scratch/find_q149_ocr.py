import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ocr_rc_test3.json', 'r', encoding='utf-8') as f:
    ocr = json.load(f)

print("Type of ocr:", type(ocr))
if isinstance(ocr, dict):
    print("Keys:", list(ocr.keys())[:10])
    for k, v in ocr.items():
        if isinstance(v, str) and ('Neil Cullen' in v or 'Soroka' in v or 'Ezenx' in v):
            print(f"Found in key {k}:")
            print(v[:500])
elif isinstance(ocr, list):
    for idx, item in enumerate(ocr):
        text = str(item)
        if 'Neil Cullen' in text or 'Soroka' in text:
            print(f"Found in index {idx}:")
            print(text[:500])
