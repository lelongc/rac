import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/data/vocab_bank.json', encoding='utf-8') as f:
    vb = json.load(f)

print(f"Total words in vocab_bank.json: {len(vb)}")
print("Sample entries:")
for item in vb[:5]:
    print(f"  {item.get('word')}: {item.get('ipa')} | {item.get('pos')} | {item.get('meaning')}")
