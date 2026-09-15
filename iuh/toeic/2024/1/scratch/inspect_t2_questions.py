import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("web/data/test2.json", "r", encoding="utf-8") as f:
    t2 = json.load(f)

for q in t2["questions"]:
    if q["id"] in [1, 2, 3, 4, 5, 6, 8, 10, 11, 32, 71, 101, 131, 147]:
        print(f"=== Q{q['id']} (Part {q['part']}) ===")
        print("Question text:", q.get("questionText"))
        print("Options:", q.get("options"))
        print("Image:", q.get("image"))
        print("PageImage:", q.get("pageImage") or q.get("pageImages"))
