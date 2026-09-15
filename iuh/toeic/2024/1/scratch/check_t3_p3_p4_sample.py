import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/t3_p3_p4_bilingual.json', encoding='utf-8') as f:
    data = json.load(f)

print("=== Dialogue 32_34 ===")
print(data['dialogues_vi']['32_34'][:200])

print("\n=== Talk 71_73 ===")
print(data['talks_vi']['71_73'][:200])

print("\n=== Question 32 ===")
print(data['questions_vi']['32'])

print("\n=== Question 71 ===")
print(data['questions_vi']['71'])
