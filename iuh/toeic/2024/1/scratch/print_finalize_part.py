import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/finalize_test2_all_questions.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos5 = text.find("PART 5")
print(text[pos5:pos5+3000])
