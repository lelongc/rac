# build_part7.py: Merge Part 7 batches into data_part7.json
import json
import part7_part1
import part7_part2
import part7_part3

all_p7 = part7_part1.P7_PART1 + part7_part2.P7_PART2 + part7_part3.P7_PART3

print(f"Total Part 7 questions: {len(all_p7)}")
ids = [q["id"] for q in all_p7]
expected = list(range(147, 201))
assert ids == expected, f"IDs mismatch! Missing: {set(expected) - set(ids)}"

with open("data_part7.json", "w", encoding="utf-8") as f:
    json.dump(all_p7, f, ensure_ascii=False, indent=2)

print("Saved data_part7.json successfully!")
